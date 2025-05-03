#!/usr/local/bin/python3
"""
    Copyright (c) 2020-2025 Ad Schellevis <ad@opnsense.org>
    All rights reserved.

    Redistribution and use in source and binary forms, with or without
    modification, are permitted provided that the following conditions are met:

    1. Redistributions of source code must retain the above copyright notice,
     this list of conditions and the following disclaimer.

    2. Redistributions in binary form must reproduce the above copyright
     notice, this list of conditions and the following disclaimer in the
     documentation and/or other materials provided with the distribution.

    THIS SOFTWARE IS PROVIDED ``AS IS'' AND ANY EXPRESS OR IMPLIED WARRANTIES,
    INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY
    AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
    AUTHOR BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY,
    OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
    SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
    INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
    CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
    ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
    POSSIBILITY OF SUCH DAMAGE.
"""
import os
import argparse
from jinja2 import Template
from lib import ApiParser

EXCLUDE_CONTROLLERS = ['Core/Api/FirmwareController.php']


def source_url(repo, src_filename):
    parts = src_filename.split('/')
    if repo == 'plugins':
        return "https://github.com/opnsense/plugins/blob/master/%s" % "/".join(parts[parts.index('src') - 2:])
    else:
        return "https://github.com/opnsense/core/blob/master/%s" % "/".join(parts[parts.index('src'):])


def collect_api_modules(source: str, debug: bool = False) -> dict[str, list[dict]]:
    # collect all endpoints
    all_modules = dict()
    for root, dirs, files in os.walk(source):
        for fname in sorted(files):
            filename = os.path.join(root, fname)
            skip = False
            for to_exclude in EXCLUDE_CONTROLLERS:
                if filename.endswith(to_exclude):
                    skip = True
                    break
            if not skip and filename.lower().endswith('controller.php') and filename.find('mvc/app/controllers') > -1 \
                    and root.endswith('Api'):
                payload = ApiParser(filename, debug).parse_api_php()
                if len(payload) > 0:
                    if payload['module'] not in all_modules:
                        all_modules[payload['module']] = list()
                    all_modules[payload['module']].append(payload)
    return all_modules


def render(all_modules: dict[str, list[dict]], repo: str):
    # writeout .rst files
    for module_name in all_modules:
        target_filename = "%s/source/development/api/%s/%s.rst" % (
            os.path.dirname(__file__), repo, module_name
        )
        print("update %s" % target_filename)
        template_data = {
            'title': "%s" % module_name.title(),
            'title_underline': "".join('~' for x in range(len(module_name))),
            'controllers': []
        }
        for controller in all_modules[module_name]:
            payload = {
                'type': controller['type'],
                'module': controller['module'],
                'controller': controller['controller'],
                'filename': controller['filename'],
                'is_abstract': controller['is_abstract'],
                'base_class': controller['base_class'],
                'endpoints': [],
                'uses': []
            }
            for endpoint in controller['actions']:
                payload['endpoints'].append(endpoint)
            if controller['model_filename']:
                payload['uses'].append({
                    'type': 'model',
                    'link': source_url(cmd_args.repo, controller['model_filename']),
                    'name': os.path.basename(controller['model_filename'])
                })
            template_data['controllers'].append(payload)

        with open(target_filename, 'w') as f_out:
            if os.path.isfile("%s.in" % target_filename):
                template_filename = "%s.in" % target_filename
            else:
                template_filename = "collect_api_endpoints.in"
            template = Template(open(template_filename, "r").read())
            f_out.write(template.render(template_data))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('source', help='source directory')
    parser.add_argument('--repo', help='target repository', default="core")
    parser.add_argument('--debug', help='enable debug mode', default=False, action='store_true')
    cmd_args = parser.parse_args()

    modules = collect_api_modules(cmd_args.source, cmd_args.debug)
    render(modules, cmd_args.repo)
