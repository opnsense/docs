#!/usr/local/bin/python3
"""
    Copyright (c) 2020-2021 Ad Schellevis <ad@opnsense.org>
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
import requests
import zipfile
import collections
import re
import pathlib
from packaging import version
from jinja2 import Template

def download_zip(target_filename):
    req = requests.get("https://github.com/opnsense/changelog/archive/master.zip", stream=True)
    if req.status_code == 200:
        req.raw.decode_content = True
        with open(target_filename, 'wb') as f_out:
            while True:
                data = req.raw.read(10240)
                if not data:
                    break
                else:
                     f_out.write(data)

def parse_change_log(payload, this_version, links):
    result = {
        "release_date": "---",
        "prelude": list(),
        "content": list()
    }
    all_tokens = set()
    all_token_links = dict()
    first_line = False
    prelude_line = this_version.count(".") == 1
    rst_content = list()
    lines = payload.split("\n")
    for idx, line in enumerate(lines):
        content_line = None
        # general cleanups
        line = line.replace('*', '\*')
        if line.find('`') > -1:
            line = re.sub(r'(`)([^`|\']*)([`|\'])', r':code:`\2`', line)
        #
        for token in re.findall(r'(\[[0-9]{1,2}\])', line):
            all_tokens.add(token)
        if idx < 3 and line.find('@') > -1:
            result["release_date"] = line.split('@')[1].strip()
        elif first_line is False and line.strip() != "":
            # strip tag line
            first_line = idx
            if line.find('OPNsense') > -1:
                content_line = line
        elif line == '--':
            # chop tagine
            del result['content'][-3:]
        elif line.startswith('o '):
            content_line = "*%s" % line[1:] # bullet list
        elif line.startswith('# '):
            # literal (code) block
            if not lines[idx-1].startswith('# '):
                content_line = ".. code-block::\n\n    %s" % line
            else:
                content_line = "    %s" % line
        elif line.startswith('[') and line[0:line.find(']')+1] in all_tokens:
            token = line[0:line.find(']')+1]
            all_token_links[token] = line[len(token)+1:].strip()
        else:
            content_line = line

        if content_line is not None:
            result['content'].append(content_line)
            if prelude_line:
                result['prelude'].append(content_line)

        # prelude exit
        if prelude_line and line.find('https://opnsense.org/download/') > -1:
            prelude_line = False

    result["content"] = "\n".join(result["content"])
    result["prelude"] = "\n".join(result["prelude"])
    # replace links
    for section in ['content', 'prelude']:
        for token in all_token_links:
            target_uri = all_token_links[token]
            tmp = all_token_links[token].split(':')
            if tmp[0] in links and len(tmp) == 2:
                target_uri = links[tmp[0]]['url']
                version = tmp[1]
                if links[tmp[0]]['regex']:
                    match = re.match(r"s/(.+)/(.*)/(\w*)", links[tmp[0]]['regex'])
                    if match:
                        count = 0 if match.group(3).startswith('g') else 1
                        version = re.sub(match.group(1), match.group(2), tmp[1], count=count)
                if target_uri.find('%s') > -1:
                    target_uri = target_uri % version

            result[section] = result[section].replace(token, " `%s <%s>`__ " % (token, target_uri))
    return result


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--skip_download', help='skip downloading github rep', action='store_true')
    cmd_args = parser.parse_args()

    root_dir = os.path.dirname(os.path.abspath(__file__))
    changelog_zip = "%s/changelog_github.zip" % root_dir
    if not cmd_args.skip_download:
        download_zip(changelog_zip)

    if os.path.isfile(changelog_zip):
        version_metadata = {
            'community': {
                'prefix': 'CE',
                'name': 'Community Edition'
            },
            'business':  {
                'prefix': 'BE',
                'name': 'Business Edition'
            }
        }
        external_links = dict()
        all_versions = {'community': dict(), 'business': dict()}
        # read all changelogs (from zip)
        this_dir = str(pathlib.Path(".").resolve())
        with zipfile.ZipFile(changelog_zip, mode='r', compression=zipfile.ZIP_DEFLATED) as zf:
            for item in zf.infolist():
                fparts = item.filename.split('/')
                if len(fparts) > 3 and fparts[1] in all_versions and item.file_size > 0:
                    all_versions[fparts[1]][fparts[3]] = zf.open(item).read().decode()
                elif len(fparts) == 3 and fparts[1] in all_versions and not item.is_dir():
                    # resolve links
                    tmp =  pathlib.Path("%s/%s" % (os.path.dirname(item.filename), zf.open(item).read().decode()))
                    link_to = str(tmp.resolve()).replace(this_dir, '')[1:]
                    for item2 in zf.infolist():
                        if item2.filename.startswith(link_to) and not item2.is_dir():
                            all_versions[fparts[1]][os.path.basename(item2.filename)] = zf.open(item2).read().decode()
                elif len(fparts) == 3 and fparts[1] == 'Links' and item.file_size > 0:
                    tmp = zf.open(item).read().decode().strip().split()
                    external_links[os.path.basename(item.filename)] = {
                        'url': tmp[0],
                        'regex': tmp[1] if len(tmp) > 1 else None
                    }

        for flavour in all_versions:
            version_prefix = version_metadata[flavour]['prefix']
            template_data = {
                'major_versions': collections.OrderedDict(),
                'versions': collections.OrderedDict(),
                'nicknames': collections.OrderedDict(),
                'flavour': flavour
            }
            template_data.update(version_metadata[flavour])
            versions = all_versions[flavour]
            for my_version in sorted(versions, key=lambda x: version.Version(x.replace('.r','rc')), reverse=True):
                major_version = ".".join(my_version.split('.')[:2])
                if major_version not in template_data['major_versions']:
                    template_data['major_versions'][major_version] = dict()
                template_data['versions'][my_version] = parse_change_log(
                    versions[my_version], my_version, external_links
                )

                if major_version == my_version:
                    template_data['nicknames'][my_version] = ""
                    tmp = versions[my_version].replace('\n', ' ')
                    m = re.match(r'.*nicknamed ["\'](?P<nickname>[^"\']+)', tmp)
                    if m:
                        template_data['nicknames'][my_version] =  m.groupdict()['nickname']

            # root menu index
            with open("%s/source/%s_releases.rst" % (root_dir, version_prefix), 'w') as f_out:
                template = Template(open("%s/source/releases.rst.in" % root_dir, "r").read())
                f_out.write(template.render(template_data))

            # per version rst file
            template = Template(open("%s/source/releases/default.rst.in" % root_dir, "r").read())
            for major_version in template_data['major_versions']:
                if major_version in template_data['versions']:
                    # wait for the main version before writing a changelog
                    with open("%s/source/releases/%s_%s.rst" % (root_dir, version_prefix, major_version), 'w') as f_out:
                        template_data['this_version'] = major_version
                        f_out.write(template.render(template_data))
