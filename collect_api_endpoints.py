#!/usr/local/bin/python
"""
    Copyright (c) 2020 Ad Schellevis <ad@opnsense.org>
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
import re
EXCLUDE_CONTROLLERS = ['Core/Api/FirmwareController.php']


def parse_api_php(src_filename):
    base_filename = os.path.basename(src_filename)
    controller = re.sub('(?<!^)(?=[A-Z])', '_', os.path.basename(base_filename.split('Controller.php')[0])).lower()
    module_name = src_filename.replace('\\', '/').split('/')[-3].lower()

    data = open(src_filename).read()
    function_callouts = re.findall(r"(\n\s+(private|public|protected)\s+function\s+(\w+)\((.*)\))", data)
    result = list()
    for idx, function in enumerate(function_callouts):
        begin_marker = data.find(function_callouts[idx][0])
        if idx+1 < len(function_callouts):
            end_marker = data.find(function_callouts[idx+1][0])
        else:
            end_marker = -1
        code_block = data[begin_marker+len(function[0]):end_marker]
        if function[2].endswith('Action'):
            record = {
                'method': 'GET',
                'module': module_name,
                'controller': controller,
                'command': function[2][:-6],
                'parameters': function[3].replace(' ', ''),
                'type': 'Service' if controller.find('service') > -1 else 'Resources',
                'filename': base_filename
            }
            # find most likely method (default => GET)
            if code_block.find('request->isPost(') > -1:
                record['method'] = 'POST'
            elif code_block.find('$this->delBase') > -1:
                record['method'] = 'POST'
            elif code_block.find('$this->addBase') > -1:
                record['method'] = 'POST'
            elif code_block.find('$this->setBase') > -1:
                record['method'] = 'POST'
            elif code_block.find('$this->toggleBase') > -1:
                record['method'] = 'POST'
            elif code_block.find('$this->searchBase') > -1:
                record['method'] = '*'
            result.append(record)

    return sorted(result, key=lambda i: i['command'])


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('source', help='source directory')
    parser.add_argument('--repo', help='target repository', default="core")
    cmd_args = parser.parse_args()

    # collect all endpoints
    all_modules = dict()
    for root, dirs, files in os.walk(cmd_args.source):
        for fname in sorted(files):
            filename = os.path.join(root, fname)
            skip = False
            for to_exclude in EXCLUDE_CONTROLLERS:
                if filename.endswith(to_exclude):
                    skip = True
                    break
            if not skip and filename.lower().endswith('controller.php') and filename.find('mvc/app/controllers') > -1 \
                    and root.endswith('Api'):
                payload = parse_api_php(filename)
                if len(payload) > 0:
                    if payload[0]['module'] not in all_modules:
                        all_modules[payload[0]['module']] = list()
                    all_modules[payload[0]['module']].append(payload)

    # writeout .rst files
    for module_name in all_modules:
        target_filename = "%s/source/development/api/%s/%s.rst" % (
            os.path.dirname(__file__), cmd_args.repo, module_name
        )
        print("update %s" % target_filename)
        with open(target_filename, 'w') as f_out:
            f_out.write("%s\n" % module_name.title())
            f_out.write("".join('~' for x in range(len(module_name))))
            f_out.write("\n\n")
            for controller in all_modules[module_name]:
                f_out.write(".. csv-table:: %s (%s)\n" % (controller[0]['type'], controller[0]['filename']))
                f_out.write("   :header: \"Method\", \"Module\", \"Controller\", \"Command\", \"Parameters\"\n")
                f_out.write("   :widths: 4, 15, 15, 30, 40\n\n")
                for endpoint in controller:
                    f_out.write(
                        "    \"``%(method)s``\",\"%(module)s\",\"%(controller)s\",\"%(command)s\",\"%(parameters)s\"\n"
                        % endpoint
                    )
                f_out.write("\n")
