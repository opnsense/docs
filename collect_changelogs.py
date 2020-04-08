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
import requests
import zipfile
import collections
import re
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

def parse_change_log(payload, this_version):
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
        elif line.startswith('o '):
            content_line = "*%s" % line[1:]
        elif line.startswith('# '):
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
            result[section] = result[section].replace(token, " `%s <%s>`__ " % (token, all_token_links[token]))
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
        template_data = {
            'major_versions': collections.OrderedDict(),
            'versions': collections.OrderedDict(),
            'nicknames': collections.OrderedDict(),
        }
        all_versions = dict()
        # read all changelogs (from zip)
        with zipfile.ZipFile(changelog_zip, mode='r', compression=zipfile.ZIP_DEFLATED) as zf:
            for item in zf.infolist():
                fparts = item.filename.split('/')
                if len(fparts) > 3 and fparts[1] == 'doc' and item.file_size > 0:
                    all_versions[fparts[3]] = zf.open(item).read().decode()

        for my_version in sorted(all_versions, key=lambda x: version.Version(x.replace('.r','rc')), reverse=True):
            major_version = ".".join(my_version.split('.')[:2])
            if major_version not in template_data['major_versions']:
                template_data['major_versions'][major_version] = dict()
            template_data['versions'][my_version] = parse_change_log(all_versions[my_version], my_version)

            if major_version == my_version:
                template_data['nicknames'][my_version] = ""
                tmp = all_versions[my_version].replace('\n', ' ')
                m = re.match(r'.*nicknamed ["\'](?P<nickname>[^"\']+)', tmp)
                if m:
                    template_data['nicknames'][my_version] =  m.groupdict()['nickname']

        # root menu index
        with open("%s/source/releases.rst" % root_dir, 'w') as f_out:
            template = Template(open("%s/source/releases.rst.in" % root_dir, "r").read())
            f_out.write(template.render(template_data))

        # per version rst file
        template = Template(open("%s/source/releases/default.rst.in" % root_dir, "r").read())
        for major_version in template_data['major_versions']:
            with open("%s/source/releases/%s.rst" % (root_dir, major_version), 'w') as f_out:
                template_data['this_version'] = major_version
                f_out.write(template.render(template_data))
