#!/usr/local/bin/python3
"""
    Copyright (c) 2024 Deciso B.V.
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
import zipfile
import shutil
import hashlib

def extract_zip(zip_path, extract_to):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        for member in zip_ref.namelist():
            # Remove the top-level directory name
            member_name = member.split('/', 1)[1] if '/' in member else member
            target_path = os.path.join(extract_to, member_name)
            if not member.endswith('/'):
                with zip_ref.open(member) as source, open(target_path, 'wb') as target:
                    shutil.copyfileobj(source, target)
            else:
                os.makedirs(target_path, exist_ok=True)

def extract_file(file_path, extract_to):
    if zipfile.is_zipfile(file_path):
        extract_zip(file_path, extract_to)
    else:
        shutil.copy(file_path, os.path.join(extract_to, 'LATEST.FD'))

def create_tar_bz2(source_dir, output_file):
    shutil.make_archive(
        base_name=output_file,
        format='gztar',
        root_dir=source_dir
    )

def merge_files(file1_path, file2_path, output_path):
    temp_dir = 'temp_extracted'
    os.makedirs(temp_dir, exist_ok=True)

    extract_file(file1_path, temp_dir)

    extract_file(file2_path, temp_dir)

    output_dir_name = os.path.splitext(os.path.basename(output_path))[0]
    combined_dir = os.path.join(temp_dir, output_dir_name)
    os.makedirs(combined_dir, exist_ok=True)
    
    for item in os.listdir(temp_dir):
        item_path = os.path.join(temp_dir, item)
        if item != output_dir_name:
            shutil.move(item_path, combined_dir)

    create_tar_bz2(combined_dir, output_path)
    shutil.rmtree(temp_dir)

def calculate_sha256(file_path):
    sha256_hash = hashlib.sha256()
    with open(file_path, 'rb') as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--platform', help='BIOS platform [A10|A20|A30]')
    parser.add_argument('--source', help='BIOS ROM image name in source/hardware/files')

    args = parser.parse_args()
    if not args.platform or args.platform not in ['A10', 'A20', 'A30']:
        print('invalid platform')
        exit(1)

    if not args.source.endswith('.FD'):
        print('invalid source file, must be a .FD file')
        exit(1)

    static = 'source/hardware/files/BIOS_update_sources.zip'
    source = f'source/hardware/files/{args.source}'
    output = f'source/hardware/files/{args.platform}_bios'

    merge_files(static, source, output)
    print(calculate_sha256(f'{output}.tar.gz'), f'{output}.tar.gz')
    
