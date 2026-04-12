#! /usr/bin/env python
"""Transform evaluated into purely semantic section reference displays in code block regions.

Example: ' # A run object (§3.14).' -> ' # A run object ((#run-object)).'

In the user facing delivery item generation phase we derive the text to replace "sec" from
the unique label and the template for the output format.
Targeting GFM+gh_cosmetics that would again yield ' # A run object (§3.14).'.

This one off script expects a specific form of markdown not spreading a reference across two lines.
The presence in the repository is merely for documentary purposes as it aided in the historic
transformation of the SARIF v2.1.0 prose from a vendor proprietary format to markdown with
the goal to seed work on the SARIF v2.2 specification in markdown format.

Note: The dashes in the filename indicate that this file is intended for execution only and not for import.
"""
import json
import pathlib
import re
import sys
from typing import Union

ENCODING = 'utf-8'
TOK_TOC = '(#$thing$)'  # Transform phase ToC label string template replacing $thing$ with the old value
TOK_SEC = "<a id='$thing$'></a>"  # Transform phase section title label string template ($thing$ -> old value)
PARA = '§'

# Detecting code block references with display values
# e.g. ' # A run object (§3.14).' or ' #  (§3.1.2).'
SEC_DISP_BRACKET_CB_DETECT = re.compile(r'\ +#\ +[^(]+\((?P<disp>§[0-9.]+)\)\.')
SEC_DISP_FREE_CB_DETECT = re.compile(r'\ +#\ +[^(]+(?P<disp>§[0-9.]+)\.')  # e.g. ' # See §3.14.14.'

# Reverse detection patterns for documentation purposes
# e.g. ' #  ((#run-object)).'
SEC_LABEL_BRACKET_CB_DETECT = re.compile(r'\ +#\ +[^(]+\((?P<label>\(#(?P<value>[0-9a-z-]+)\))\)\.')
# e.g. ' #  (#run-object).'
SEC_LABEL_FREE_CB_DETECT = re.compile(r'\ +#\ +[^(]+(?P<label>\(#(?P<value>[0-9a-z-]+)\))\.')

# Configuration and runtime parameter candidates:
BINDER_AT = pathlib.Path('etc') / 'bind.txt'
SOURCE_AT = pathlib.Path('src')
BUILD_AT = pathlib.Path('build')
SECTION_DISPLAY_TO_LABEL_AT = pathlib.Path('etc') / 'section-display-to-label.json'
SECTION_LABEL_TO_DISPLAY_AT = pathlib.Path('etc') / 'section-label-to-display.json'


def load_binder(binder_at: Union[str, pathlib.Path]) -> list[pathlib.Path]:
    """Load the linear binder text file into a list of file paths."""
    with open(binder_at, 'rt', encoding=ENCODING) as resource:
        return [pathlib.Path(entry.strip()) for entry in resource.readlines() if entry.strip()]


def para_in(text: str) -> bool:
    """Detect if the text line contains a code block display ref."""
    return PARA in text


def section_ref(text: str) -> bool:
    """Detect if the text references a section."""
    return text.startswith(PARA) or text.startswith('Appendix ')


def main(argv: list[str]) -> int:
    """Drive the transform."""

    bind_seq_path = pathlib.Path(argv[0]) if argv else BINDER_AT
    binder = load_binder(bind_seq_path)
    for resource in binder:
        if not (SOURCE_AT / resource).is_file():
            print(f'Problem reading {resource}')
            return 1

    # Load the display to label mapping
    with SECTION_DISPLAY_TO_LABEL_AT.open('rt', encoding=ENCODING) as handle:
        label_from = json.load(handle)

    for resource in binder:
        with open(SOURCE_AT / resource, 'rt', encoding=ENCODING) as handle:
            lines = handle.readlines()
        for slot, line in enumerate(lines):
            if para_in(line):
                for ref in SEC_DISP_BRACKET_CB_DETECT.finditer(line):
                    if ref:
                        # Found bracketed display ref to section in code block
                        disp = ref.groupdict()['disp']
                        if not section_ref(disp):
                            continue
                        label = label_from[disp]
                        evil_ref = f'({disp})'
                        sem_ref = f'((#{label}))'
                        line = line.replace(evil_ref, sem_ref)
                        lines[slot] = line
                for ref in SEC_DISP_FREE_CB_DETECT.finditer(line):
                    if ref:
                        # Found free display ref to section in code block
                        disp = ref.groupdict()['disp']
                        if not section_ref(disp):
                            continue
                        label = label_from[disp]
                        evil_ref = f'{disp}'
                        sem_ref = f'(#{label})'
                        line = line.replace(evil_ref, sem_ref)
                        lines[slot] = line

        with open(BUILD_AT / resource, 'wt', encoding=ENCODING) as handle:
            handle.write(''.join(lines))
        print(f'transform result written to {BUILD_AT / resource}', file=sys.stderr)

    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
