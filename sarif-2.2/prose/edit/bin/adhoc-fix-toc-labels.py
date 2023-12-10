#! /usr/bin/env python
"""Transform volatile stem-counter ToC label-ref pairs to a context free path-like form.

This one off script expects a specific form of markdown with visual patches.
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

MULTIPLE_DETECT = re.compile(r'\]\(#(?P<stem>\w(-?\w)*)-(?P<ctr>\d+)\)')  # Stem-counter pattern
GENESIS_DETECT = re.compile(r'\]\(#(?P<genesis>[^)1-9]+)\)')  # Stem only pattern
TARGET_DETECT = re.compile(r'\]\(#(?P<parentsec>[^)1-9]+)\)')  # Assuming parent sections have stem only labels


def begin_of_toc_in(text: str) -> bool:
    """Detect the begin of the table of contents."""
    return text.startswith('Table of Contents')


def end_of_toc_in(text: str) -> bool:
    """Detect the end of the table of contents."""
    return text.startswith('#') and ' Introduction' in text


def label_in(text: str) -> bool:
    """Detect if the text line contains a label."""
    return '](#' in text


def main(in_file: str) -> int:
    """Drive the transform."""

    # Read lines from the huge GFM+gh_cosmetics text file
    lines = pathlib.Path(in_file).open('rt', encoding=ENCODING).readlines()

    # Collect all labels with counters and their left space offset as indent level for parent section search
    first_toc_line: Union[int, None] = None  # Offset for later region only algorithms to derive global slot
    toc_lines = []  # Local extract with region only lines
    ctr_toc_slot_stem_ctr_line_quad = []  # Extracted label facts for the creation of the transform
    indent_of_stem_ctr = {}  # indent map for subsequent search of parent section labels
    in_toc = False  # state variable
    for slot, line in enumerate(lines):
        if in_toc:
            # In region of interest (table of contents)
            if end_of_toc_in(line):
                # Base case (ensure exit after ToC)
                break
            toc_lines.append(line)
            if label_in(line):
                non_unique = MULTIPLE_DETECT.search(line)
                if non_unique:
                    # Found ToC label in stem-counter format
                    found = non_unique.groupdict()
                    stem = found['stem']
                    ctr = found['ctr']
                    stem_ctr = f'{stem}-{ctr}'
                    # Extract label facts and left indent representing logical indent level
                    ctr_toc_slot_stem_ctr_line_quad.append((slot, stem, ctr, line))
                    indent_of_stem_ctr[stem_ctr] = len(line) - len(line.lstrip())
            continue
        if not in_toc:
            # Region start detected
            if begin_of_toc_in(line):
                in_toc = True
                first_toc_line = slot
                toc_lines.append(line)
            continue

    # Harvest the stem set from the quads (resulting stems set assumed to be small)
    stems = set((stem for _, stem, _, _ in ctr_toc_slot_stem_ctr_line_quad))

    # We could use counter container, but we may not for such a one off task coding as we go ;-)
    stem_maxima = {}
    for stem in sorted(stems):
        stem_maxima[stem] = max(ctr for _, stem_cand, ctr, _ in ctr_toc_slot_stem_ctr_line_quad if stem_cand == stem)

    # Second run over ToC lines with stems detects per ToC line to harvest stem quads
    ctr = 0  # Cartesian approach extending the counter domain beyond the minimum to ease processing
    for rel_slot, line in enumerate(toc_lines):
        if end_of_toc_in(line):
            # Base case (ensure exit after ToC)
            break
        if label_in(line):
            candidate = GENESIS_DETECT.search(line)
            if candidate:
                stem_cand = candidate.groupdict()['genesis']
                if stem_cand in stems:
                    # Found a matching stem label
                    stem_ctr = f'{stem_cand}-{ctr}'
                    slot = rel_slot + first_toc_line  # type: ignore
                    # Amend processing structures with extract label facts and left indent representing logical level
                    ctr_toc_slot_stem_ctr_line_quad.append((slot, stem_cand, ctr, line))
                    indent_of_stem_ctr[stem_ctr] = len(line) - len(line.lstrip())
        continue

    # For every quad traverse lines from its slot in reverse until indent less and harvest the stem from that line
    transform_pairs = {}  # Final processing map for the transform loop
    for slot, stem, ctr, line in ctr_toc_slot_stem_ctr_line_quad:
        stem_ctr = f'{stem}-{ctr}'  # Derive the key
        level_up = indent_of_stem_ctr[stem_ctr] - 1  # Derive parent section level
        curr = slot  # Init the reverse loop start
        while curr > first_toc_line:  # type: ignore
            curr -= 1
            preceding = lines[curr]
            if preceding.strip() and label_in(preceding):
                indent = len(preceding) - len(preceding.lstrip())
                if indent <= level_up:
                    parent_section = TARGET_DETECT.search(preceding)
                    if parent_section:
                        parent_section_label = parent_section.groupdict()['parentsec']
                        parentsec_stem = f'{parent_section_label}--{stem}'
                        source_str = stem_ctr if ctr else stem
                        transform_pairs[source_str] = parentsec_stem  # Add the old -> new mapping
                        # Base guard: reset for next stem
                        curr = first_toc_line  # type: ignore

    # Define and drive the actual transformation mapping old to new values (ToC labels and refs)
    for slot, line in enumerate(lines):
        text = line
        for old, new in transform_pairs.items():
            toc = TOK_TOC.replace('$thing$', old)
            cot = TOK_TOC.replace('$thing$', new)
            sec = TOK_SEC.replace('$thing$', old)
            ces = TOK_SEC.replace('$thing$', new)
            text = text.replace(toc, cot).replace(sec, ces)
            lines[slot] = text

    # Write the transformed lines to the derived file name
    out_file = in_file.replace('.md', '-transformed.md')
    with open(out_file, 'wt', encoding=ENCODING) as resource:
        resource.write(''.join(lines))

    print(f'transform result written to {out_file}', file=sys.stderr)
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1]))
