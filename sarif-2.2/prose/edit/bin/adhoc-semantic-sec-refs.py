#! /usr/bin/env python
"""Transform evaluated into purely semantic section references.

Example: [§3.24.4](#offset-property) -> [sec](#offset-property)

In the user facing delivery item generation phase we derive the text to replace "sec" from
the unique label and the template for the output format.
Targeting GFM+gh_cosmetics that would again yield [§3.24.4](#offset-property).

This one off script expects a specific form of markdown not spreading a reference across two lines.
The presence in the repository is merely for documentary purposes as it aided in the historic
transformation of the SARIF v2.1.0 prose from a vendor proprietary format to markdown with
the goal to seed work on the SARIF v2.2 specification in markdown format.

Note: The dashes in the filename indicate that this file is intended for execution only and not for import.
"""
import pathlib
import re
import sys
from typing import Union

ENCODING = 'utf-8'
TOK_TOC = '(#$thing$)'  # Transform phase ToC label string template replacing $thing$ with the old value
TOK_SEC = "<a id='$thing$'></a>"  # Transform phase section title label string template ($thing$ -> old value)

REF_DETECT = re.compile(r'\[(?P<text>[^]]+)\]\(#(?P<label>[^)1-9]+)\)')  # [ref_text](#label) pattern

# Configuration and runtime parameter candidates:
BINDER_AT = pathlib.Path('etc') / 'bind.txt'
SOURCE_AT = pathlib.Path('src')
BUILD_AT = pathlib.Path('build')


def load_binder(binder_at: Union[str, pathlib.Path]) -> list[pathlib.Path]:
    """Load the linear binder text file into a list of file paths."""
    with open(binder_at, 'rt', encoding=ENCODING) as resource:
        return [pathlib.Path(entry.strip()) for entry in resource.readlines() if entry.strip()]


def label_in(text: str) -> bool:
    """Detect if the text line contains a label."""
    return '](#' in text


def section_ref(text: str) -> bool:
    """Detect if the text references a section."""
    return text.startswith('§') or text.startswith('Appendix ')


def main(argv: list[str]) -> int:
    """Drive the transform."""

    bind_seq_path = pathlib.Path(argv[0]) if argv else BINDER_AT
    binder = load_binder(bind_seq_path)
    for resource in binder:
        if not (SOURCE_AT / resource).is_file():
            print(f'Problem reading {resource}')
            return 1

    for resource in binder:
        with open(SOURCE_AT / resource, 'rt', encoding=ENCODING) as handle:
            lines = handle.readlines()
        for slot, line in enumerate(lines):
            if label_in(line):
                for ref in REF_DETECT.finditer(line):
                    if ref:
                        # Found ToC label in stem-counter format
                        found = ref.groupdict()
                        text = found['text']
                        if not section_ref(text):
                            continue
                        label = found['label']
                        evil_ref = f'[{text}](#{label})'
                        sem_ref = f'[sec](#{label})'
                        print('-', f'{resource}:{slot + 1}', evil_ref, '-->', sem_ref)
                        line = line.replace(evil_ref, sem_ref)
                        lines[slot] = line

        with open(BUILD_AT / resource, 'wt', encoding=ENCODING) as handle:
            handle.write(''.join(lines))
        print(f'transform result written to {BUILD_AT / resource}', file=sys.stderr)

    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
