#! /usr/bin/env python
"""Transform evaluated into purely semantic ref (citation code) references.

Example: [ISO14977:1996](#ISO14977) -> [cite](#ISO14977;1996) (initial harmonization)

In the user facing delivery item generation phase we derive the text to replace "cite" from
the unique label and the template for the output format.
Targeting GFM+gh_cosmetics that would then yield [ISO14977:1996](#ISO14977;1996).
Note, that the goal is to minimize the out-of-band data needed to construct both
markdown file representations only by given the visible citation code plus one extra rule
that ensures the "fragments" (the identifier in the link part) are valid for all consuming
processors considered - browser history may not work with colons in such fragments, thus:

rule: label_text(':') <-> link_identifier(';')

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

CITE_REF_DETECT = re.compile(r'\\\[\[(?P<text>[^]]+)\]\(#(?P<label>[^)]+)\)\\\]')  # \[[ref_text](#label)\] pattern

# Configuration and runtime parameter candidates:
BINDER_AT = pathlib.Path('etc') / 'bind.txt'
SOURCE_AT = pathlib.Path('src')
BUILD_AT = pathlib.Path('build')


REF_REMAP = {
    '(#BCP14)': '(#BCP14)',
    '(#ECMA404)': '(#ECMA404)',
    '(#GFM)': '(#GFM)',
    '(#IANA_ENC)': '(#IANA-ENC)',
    '(#IANA_HASH)': '(#IANA-HASH)',
    '(#ISO3166)': '(#ISO3166-1;2013)',
    '(#ISO639)': '(#ISO639-1;2002)',
    '(#ISO86012004)': '(#ISO8601;2004)',
    '(#ISO14977)': '(#ISO14977;1996)',
    '(#JSCHEMA01)': '(#JSCHEMA01)',
    '(#RFC2119)': '(#RFC2119)',
    '(#RFC2045)': '(#RFC2045)',
    '(#RFC2048)': '(#RFC2048)',
    '(#RFC3629)': '(#RFC3629)',
    '(#RFC3986)': '(#RFC3986)',
    '(#RFC3987)': '(#RFC3987)',
    '(#RFC4122)': '(#RFC4122)',
    '(#RFC5646)': '(#RFC5646)',
    '(#RFC6901)': '(#RFC6901)',
    '(#RFC7230)': '(#RFC7230)',
    '(#RFC8174)': '(#RFC8174)',
    '(#RFC8089)': '(#RFC8089)',
    '(#SEMVER)': '(#SEMVER)',
    '(#UNICODE12)': '(#UNICODE12)',
    '(#CMARK)': '(#CMARK)',
    '(#CWE)': '(#CWE)',
    '(#GFMCMARK)': '(#GFMCMARK)',
    '(#GFMENG)': '(#GFMENG)',
    '(#ISO9899)': '(#ISO9899;2011)',  # not present in upstream
    '(#ISO14882)': '(#ISO9899;2017)',  # not present in upstream
    '(#ISO23270)': '(#ISO23270;2006)',  # not present in upstream
    '(#PE)': '(#PE)',
    '(#TAR)': '(#TAR)',
    '(#ZIP)': '(#ZIP)',
}


def load_binder(binder_at: Union[str, pathlib.Path]) -> list[pathlib.Path]:
    """Load the linear binder text file into a list of file paths."""
    with open(binder_at, 'rt', encoding=ENCODING) as resource:
        return [pathlib.Path(entry.strip()) for entry in resource.readlines() if entry.strip()]


def label_in(text: str) -> bool:
    """Detect if the text line contains a label."""
    return '](#' in text


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
                for ref in CITE_REF_DETECT.finditer(line):
                    if ref:
                        # Found citation label in HTML span id class anchor format
                        found = ref.groupdict()
                        text = found['text']
                        label = found['label']
                        evil_ref = f'\\[[{text}](#{label})\\]'  # \[[GFMCMARK](#GFMCMARK)\]
                        sem_ref = f'\\[[cite](#{label})\\]'
                        print('-', f'{resource}:{slot + 1}', evil_ref, '-->', sem_ref)
                        line = line.replace(evil_ref, sem_ref)
                        lines[slot] = line

        with open(BUILD_AT / resource, 'wt', encoding=ENCODING) as handle:
            handle.write(''.join(lines))
        print(f'transform result written to {BUILD_AT / resource}', file=sys.stderr)

    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
