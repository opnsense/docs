#!/usr/local/bin/python3

"""
    Copyright (c) 2025 Cedrik Pischem
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

import argparse
import xml.etree.ElementTree as ET
from pathlib import Path
from textwrap import wrap

OUTPUT_BASE = Path("source/manual/forms")

def format_help(text: str, width: int = 100) -> str:
    return "\n".join(wrap(text.strip(), width=width))

def extract_tabs(xml_content: str, fallback_tab_name: str) -> dict:
    """Extracts tab entries from an XML content string."""
    root = ET.fromstring(xml_content)
    fields = root.findall(".//field")
    current_tab = fallback_tab_name
    tabs = {current_tab: []}

    for field in fields:
        field_type = field.findtext("type")
        label = field.findtext("label")
        help_text = field.findtext("help") or ""

        # If this field is a header, switch current tab.
        if field_type == "header" and label:
            current_tab = label.strip()
            tabs.setdefault(current_tab, [])
            continue

        if label:
            desc = format_help(help_text) if help_text else ""
            tabs[current_tab].append((f"**{label}**", desc))

    return tabs

def generate_rst(tab_data: dict) -> str:
    """Generates reStructuredText content from tab data."""
    lines = [".. tabs::", ""]
    for tab_name, entries in tab_data.items():
        if not entries:
            continue

        col1_width = max(len(label) for label, _ in entries)
        col2_width = 100
        header = f"{'=' * col1_width} {'=' * col2_width}"

        lines.extend([
            f"    .. tab:: {tab_name}",
            "",
            f"        {header}",
            f"        {'**Option**'.ljust(col1_width)} {'**Description**'}",
            f"        {header}"
        ])

        for label, description in entries:
            if not description:
                lines.append(f"        {label.ljust(col1_width)}")
            else:
                description_lines = description.splitlines()
                lines.append(f"        {label.ljust(col1_width)} {description_lines[0]}")
                for line in description_lines[1:]:
                    lines.append(f"        {' ' * col1_width} {line}")

        lines.extend([f"        {header}", ""])

    return "\n".join(lines)

def clean_name(name: str) -> str:
    """Cleans up the filename to create a default tab name."""
    return (name.replace("dialog", "")
               .replace(".xml", "")
               .replace("_", " ")
               .replace("-", " ")
               .strip()
               .title())

def get_subcomponent(input_dir: Path) -> str:
    """
    Determines the subcomponent name from the input path.
    Expected structure: .../<Subcomponent>/forms/
    """
    try:
        parts = input_dir.parts
        forms_index = parts.index("forms")
        return parts[forms_index - 1]
    except (ValueError, IndexError):
        raise ValueError("Could not determine subcomponent. Expected */<Subcomponent>/forms/")

def process_files(input_dir: Path) -> None:
    """Processes each XML file in the input directory."""
    try:
        subcomponent = get_subcomponent(input_dir)
    except ValueError as e:
        print(e)
        return

    output_dir = OUTPUT_BASE / subcomponent
    output_dir.mkdir(parents=True, exist_ok=True)

    for xml_file in sorted(input_dir.glob("*.xml")):
        try:
            xml_content = xml_file.read_text(encoding="utf-8")
            default_tab = clean_name(xml_file.name)
            tabs = extract_tabs(xml_content, fallback_tab_name=default_tab)
            rst_content = generate_rst(tabs)
            out_file = output_dir / f"{xml_file.stem.lower()}.rst"
            out_file.write_text(rst_content, encoding="utf-8")
            print(f"Generated: {out_file}")
        except ET.ParseError as err:
            print(f"Error parsing {xml_file.name}: {err}")

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Generate one .rst file per form XML using headers as tabs."
    )
    parser.add_argument('--input', required=True,
                        help='Path to a "forms" folder containing XML files.')
    args = parser.parse_args()
    input_dir = Path(args.input).resolve()

    if not input_dir.is_dir():
        print(f"Input path is not a directory: {input_dir}")
        return

    process_files(input_dir)

if __name__ == "__main__":
    main()

