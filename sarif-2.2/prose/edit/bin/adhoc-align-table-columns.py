#! /usr/bin/env python
"""Align GF markdown tables with correct but misaligned columns in text files.

Example:

Incoming:

```console
❯ cat test/fixtures/adhoc/misaligned-single-gfm-table.md
|    nothing | something     |     a long column head |
|:---|----:|:---------:|
| 1  | 42  |       999 |
| left|right |centered|
||||
```

Processing:

```console
❯ bin/adhoc-align-table-columns.py test/fixtures/adhoc/misaligned-single-gfm-table.md
document with aligned tables written to build/misaligned-single-gfm-table.md
```

Outgoing:

```console
❯ cat build/misaligned-single-gfm-table.md
| nothing | something | a long column head |
|:--------|----------:|:------------------:|
| 1       |        42 |        999         |
| left    |     right |      centered      |
|         |           |                    |
```

This one off script expects a specific form of markdown not spreading a reference across two lines.
The presence in the repository is merely for documentary purposes as it aided in the historic
transformation of the SARIF v2.1.0 prose from a vendor proprietary format to markdown with
the goal to seed work on the SARIF v2.2 specification in markdown format.

Note: The dashes in the filename indicate that this file is intended for execution only and not for import.
"""
import pathlib
import sys
from typing import Union

ENCODING = 'utf-8'
DASH = '-'
NL = '\n'
SPACE = ' '

# Configuration and runtime parameter candidates:
BUILD_AT = pathlib.Path('build')

# Specific tokens:
COLUMN_SEP = '|'  # GF markdown table column separator
HEAD_SEP = DASH  # main table header separating line
ALIGN_MARK = ':'  # left-only, both for center, or right-only
FORMAT_LINE_LEFT = '|:'
FORMAT_LINE_RIGHT = ':|'
ALIGNMENT_CODES = ('l', 'c', 'r')  # left, center, right; unspecified -> left


def table_in(text: str) -> bool:
    """Detect if the text line contains a table line."""
    return text.startswith(COLUMN_SEP)


def section_ref(text: str) -> bool:
    """Detect if the text references a section."""
    return text.startswith('§') or text.startswith('Appendix ')


def is_table_head_sep(text: str) -> bool:
    """Detect a table head separating line per character removal and guard against empty or space only cells."""
    allowed_chars = (ALIGN_MARK, COLUMN_SEP, HEAD_SEP, SPACE)
    other = ''.join(set(text.split()))
    for char in allowed_chars:
        other = other.replace(char, '')
    return bool(text.strip().replace(COLUMN_SEP, '')) and not other


def parse_table_col_widths(tokens: list[str]) -> list[int]:
    """Parse table token lists for column widths."""
    return [len(text) for text in tokens]


def table_col_widths(col_widths: list[list[int]]) -> list[int]:
    """Aggregate column widths per maximum for table wide column widths."""
    table_spec = col_widths[0]
    for widths in col_widths[1:]:
        for slot, width in enumerate(widths):
            table_spec[slot] = max(table_spec[slot], width)
    return table_spec


def parse_table_head_sep(tokens: list[str]) -> list[str]:
    """Parse table head separator token list for column count and their horizontal alignments."""
    alignments = []
    for text in tokens:
        left = text.startswith(ALIGN_MARK)
        right = text.endswith(ALIGN_MARK)
        code = 'c' if left and right else ('l' if left else ('r' if right else 'l'))
        alignments.append(code)
    return alignments


def parse_table_line(text: str) -> tuple[list[str], bool]:
    """Parse a table line into an annotated token list assuming no pipe in cells.

    The text '| a | b |' yields ([' a ', ' b '], False).
    The text '|:--|--:|' yields ([':--', '--:'], True).
    """
    return [cell.strip() for cell in text.split(COLUMN_SEP)[1:-1]], is_table_head_sep(text)


def left(text: str, width: int, fill: str = SPACE) -> str:
    """Left align the content text left and fill up to the width with fill (default: spaces)."""
    return text.ljust(width, fill)


def center(text: str, width: int, fill: str = SPACE) -> str:
    """Center the content text left and fill up to the width with fill (default: spaces)."""
    return text.center(width, fill)


def right(text: str, width: int, fill: str = SPACE) -> str:
    """Right align the content text left and fill up to the width with fill (default: spaces)."""
    return text.rjust(width, fill)


def render_text_row(header_tokens: list[str], alignments: list[str], widths: list[int]) -> str:
    """Render a table header (column labels) or data line according to column alignments and widths.

    The row width segregation is(m: marker single space, c: aligned content):
        |mcm|mcm|...m|

    The content is either left aligned (code 'l'), right aligned (code 'r'), or centered ('c').

    The result receives a trailing new line to simplify the patch upstream.
    """
    data = []
    for text, code, width in zip(header_tokens, alignments, widths):
        if code == 'l':
            cell = left(text, width)
        elif code == 'c':
            cell = center(text, width)
        else:
            cell = right(text, width)
        # Effective width has to be amended for the width of the two alignment markers
        data.append(SPACE + cell + SPACE)
    return COLUMN_SEP + COLUMN_SEP.join(data) + COLUMN_SEP + NL


def render_separator_row(ignored_tokens: list[str], alignments: list[str], widths: list[int]) -> str:
    """Derive the table separator line according from column alignments and widths.

    The row width segregation is(m and n: marker single spaces (left and right), f: fill characters '-'):
        |mfn|mfn|...n|

    The left marker is either ':' when column is left aligned (code 'l') or centered ('c').
    The right marker is either ':' when column is centered ('c') or right aligned (code 'r').

    The result receives a trailing new line to simplify the patch upstream.
    """
    data = []
    for _, code, width in zip(ignored_tokens, alignments, widths):
        inner_text = HEAD_SEP * width
        if code == 'l':
            left, right = ALIGN_MARK, HEAD_SEP
        elif code == 'c':
            left, right = ALIGN_MARK, ALIGN_MARK
        else:
            left, right = HEAD_SEP, ALIGN_MARK
        data.append(left + inner_text + right)
    return COLUMN_SEP + COLUMN_SEP.join(data) + COLUMN_SEP + NL


def main(argv: list[str]) -> int:
    """Drive the transform."""

    for name in argv:
        resource = pathlib.Path(name)
        with open(resource, 'rt', encoding=ENCODING) as handle:
            lines = handle.readlines()
        table_lines = []
        table_line_data: list[tuple[list[str], bool]] = []
        in_table = False
        first_table_line: Union[int, None] = None
        for slot, line in enumerate(lines):
            if table_in(line):
                if first_table_line is None:
                    first_table_line = slot
                    in_table = True
                table_lines.append(line)
                table_line_data.append(parse_table_line(line.rstrip(NL)))
                if slot < len(lines) - 1:
                    # Base case insurance
                    continue
            if in_table:
                # Process the table and inject the patch the upstream lines
                col_widths = []
                # Derive the specification of table wide column widths and alignments
                for where, entry in enumerate(table_line_data):
                    if not entry[1]:
                        col_widths.append(parse_table_col_widths(entry[0]))
                    else:
                        col_widths.append([len(':-:') for _ in entry[0]])  # minimum width of three for separator cells
                        alignments = parse_table_head_sep(entry[0])
                table_spec = table_col_widths(col_widths)
                # Render the table rows into the table lines
                for where, (data, is_sep) in enumerate(table_line_data):
                    if not is_sep:
                        line = render_text_row(data, alignments, table_spec)
                    else:
                        line = render_separator_row(data, alignments, table_spec)
                    table_lines[where] = line

                lines[first_table_line : first_table_line + len(table_lines)] = table_lines  # type: ignore
                table_lines = []
                in_table = False

        with open(BUILD_AT / resource.name, 'wt', encoding=ENCODING) as handle:
            handle.write(''.join(lines))
        print(f'document with aligned tables written to {BUILD_AT / resource.name}', file=sys.stderr)

    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
