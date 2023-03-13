#!/usr/local/bin/python3
"""
    Copyright (c) 2022 Ad Schellevis <ad@opnsense.org>
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
from jinja2 import Template

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-template_filename', default='source/support.rst.in', help='')
    parser.add_argument('source', help='source directory')
    cmd_args = parser.parse_args()

    # collect all plugins
    plugin_tiers = dict()
    for root, dirs, files in os.walk(cmd_args.source):
        if 'Makefile' in files and 'pkg-descr' in files:
            plugin_tier = 3
            with open(os.path.join(root, 'Makefile'), 'rt') as f_in:
                for line in f_in.read().split('\n'):
                    parts = line.split()
                    if len(parts) >= 2 and parts[0].startswith('PLUGIN_TIER') and parts[-1].isdigit():
                        plugin_tier = int(parts[-1])
            plugin_name = root[len(cmd_args.source)+1:]
            if plugin_tier not in plugin_tiers:
                plugin_tiers[plugin_tier] = {}
            plugin_tiers[plugin_tier][plugin_name] = {
                'tier': plugin_tier,
                'name': plugin_name
            }
            with open(os.path.join(root, 'pkg-descr'), 'rt') as f_in:
                descr = f_in.read().strip().split('\n\n')[0].replace('\n', ' ').replace('"', "'")
                plugin_tiers[plugin_tier][plugin_name]['descr'] = descr

    template = Template(open(cmd_args.template_filename, "rt").read())
    if cmd_args.template_filename.endswith('.in'):
        with open(cmd_args.template_filename[:-3], 'w') as f_out:
            f_out.write(template.render({'tiers': plugin_tiers}))
    else:
        print(template.render({'tiers': plugin_tiers}))
