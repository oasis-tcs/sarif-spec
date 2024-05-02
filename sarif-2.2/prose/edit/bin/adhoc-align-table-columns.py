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

Note: Some incorrect table representations raise attention through exceptions while others may slip through.

This one off script expects a specific form of markdown not spreading a reference across two lines.
The presence in the repository is merely for documentary purposes as it aided in the historic
transformation of the SARIF v2.1.0 prose from a vendor proprietary format to markdown with
the goal to seed work on the SARIF v2.2 specification in markdown format.

Note: The dashes in the filename indicate that this file is intended for execution only and not for import.
"""
import datetime as dti
import logging
import pathlib
import sys
from typing import Union, no_type_check

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

# Logging on module level
log = logging.getLogger()  # Module level logger is sufficient
LOG_LEVEL = logging.INFO
TS_FORMAT_LOG = '%Y-%m-%dT%H:%M:%S'


@no_type_check
def formatTime_RFC3339(self, record, datefmt=None):
    """HACK A DID ACK we could inject .astimezone() to localize ..."""
    return dti.datetime.fromtimestamp(record.created, dti.timezone.utc).isoformat()


@no_type_check
def init_logger(name=None, level=None):
    """Initialize module level logger"""
    global log

    log_format = {
        'format': '%(asctime)s %(levelname)s [%(name)s]: %(message)s',
        'datefmt': TS_FORMAT_LOG,
        'level': LOG_LEVEL if level is None else level,
    }
    logging.Formatter.formatTime = formatTime_RFC3339
    logging.basicConfig(**log_format)
    log = logging.getLogger('tool' if name is None else name)
    log.propagate = True


init_logger(name='tabla', level=None)


class Table:
    """A GFM format markdown table."""

    def __init__(self, resource: pathlib.Path, offset: int, table_lines: list[str]):
        """Load from table lines into the internal data structures."""
        self.resource = resource
        self.offset: Union[int, None] = offset
        self.lines: list[str] = [line for line in table_lines]
        self.line_count = len(self.lines)
        self.end_index = self.offset + self.line_count  # type: ignore
        self.table_line_data: list[tuple[list[str], bool]] = [
            Table.parse_table_line(line.rstrip(NL)) for line in self.lines
        ]
        self.alignments: list[str]
        self.widths: list[list[int]] = []
        self.spec: list[int]

    def separator_line_count(self) -> int:
        """Return the number of separator lines."""
        return sum(1 if is_sep else 0 for _, is_sep in self.table_line_data)

    def validate_spec(self) -> bool:
        """Validate the table specification."""
        sep_line_count = self.separator_line_count()
        if sep_line_count == 1:
            return True
        diagnose = '(no separator line detected)' if not sep_line_count else '(ambiguous separator lines detected)'
        message = (
            f'expected 1 separator line but found {sep_line_count}'
            f' in location({self.resource.name}:{self.end_index + 1}@table[{self.line_count}]) -> {diagnose}'
        )
        log.error(message)
        return False

    def derive_table_spec(self) -> list[int]:
        """Derive alignments and column widths from data."""
        column_count_guard = None
        # Derive the specification of table wide column widths and alignments
        for where, entry in enumerate(self.table_line_data):
            detected_col_count = len(entry[0])
            if column_count_guard is None:
                column_count_guard = detected_col_count
            elif column_count_guard != detected_col_count:
                message = (
                    f'expected cols({column_count_guard}) but found cols({detected_col_count})'
                    f' in location({self.resource.name}:{self.offset + where + 1}@table[{where}]) ->'
                    f' ({self.lines[where].rstrip(NL)})'
                )
                log.error(message)
                return []
            if not entry[1]:
                self.widths.append(Table.parse_table_col_widths(entry[0]))
            else:
                self.widths.append([len(':-:') for _ in entry[0]])  # minimum width of three for separator cells
                self.alignments = Table.parse_table_head_sep(entry[0])
        self.spec = Table.table_col_widths(self.widths)
        return self.spec

    def render_text_row(self, header_tokens: list[str]) -> str:
        """Render a table header (column labels) or data line according to column alignments and widths.

        The row width segregation is(m: marker single space, c: aligned content):
            |mcm|mcm|...m|

        The content is either left aligned (code 'l'), right aligned (code 'r'), or centered ('c').

        The result receives a trailing new line to simplify the patch upstream.
        """
        data = []
        for text, code, width in zip(header_tokens, self.alignments, self.spec):
            if code == 'l':
                cell = Table.left(text, width)
            elif code == 'c':
                cell = Table.center(text, width)
            else:
                cell = Table.right(text, width)
            # Effective width has to be amended for the width of the two alignment markers
            data.append(SPACE + cell + SPACE)
        return COLUMN_SEP + COLUMN_SEP.join(data) + COLUMN_SEP + NL

    def render_separator_row(self, ignored_tokens: list[str]) -> str:
        """Derive the table separator line according from column alignments and widths.

        The row width segregation is(m and n: marker single spaces (left and right), f: fill characters '-'):
            |mfn|mfn|...n|

        The left marker is either ':' when column is left aligned (code 'l') or centered ('c').
        The right marker is either ':' when column is centered ('c') or right aligned (code 'r').

        The result receives a trailing new line to simplify the patch upstream.
        """
        data = []
        for _, code, width in zip(ignored_tokens, self.alignments, self.spec):
            inner_text = HEAD_SEP * width
            if code == 'l':
                left, right = ALIGN_MARK, HEAD_SEP
            elif code == 'c':
                left, right = ALIGN_MARK, ALIGN_MARK
            else:
                left, right = HEAD_SEP, ALIGN_MARK
            data.append(left + inner_text + right)
        return COLUMN_SEP + COLUMN_SEP.join(data) + COLUMN_SEP + NL

    def render(self) -> None:
        """Render the table in-place into the lines."""
        for where, (data, is_sep) in enumerate(self.table_line_data):
            if not is_sep:
                line = self.render_text_row(data)
            else:
                line = self.render_separator_row(data)
            self.lines[where] = line

    @staticmethod
    def table_in(text: str) -> bool:
        """Detect if the text line contains a table line."""
        return text.startswith(COLUMN_SEP)

    @staticmethod
    def is_table_head_sep(text: str) -> bool:
        """Detect a table head separating line per character removal and guard against empty or space only cells."""
        if HEAD_SEP not in text or not text.strip().replace(COLUMN_SEP, ''):
            return False
        allowed_chars = (ALIGN_MARK, HEAD_SEP, COLUMN_SEP, SPACE)
        other = ''.join(set(text.split()))
        for char in allowed_chars:
            other = other.replace(char, '')
        return not other

    @staticmethod
    def parse_table_col_widths(tokens: list[str]) -> list[int]:
        """Parse table token lists for column widths."""
        return [len(text) for text in tokens]

    @staticmethod
    def table_col_widths(col_widths: list[list[int]]) -> list[int]:
        """Aggregate column widths per maximum for table wide column widths."""
        table_spec = col_widths[0]
        for widths in col_widths[1:]:
            for slot, width in enumerate(widths):
                table_spec[slot] = max(table_spec[slot], width)
        return table_spec

    @staticmethod
    def parse_table_head_sep(tokens: list[str]) -> list[str]:
        """Parse table head separator token list for column count and their horizontal alignments."""
        alignments = []
        for text in tokens:
            left = text.startswith(ALIGN_MARK)
            right = text.endswith(ALIGN_MARK)
            code = 'c' if left and right else ('l' if left else ('r' if right else 'l'))
            alignments.append(code)
        return alignments

    @staticmethod
    def parse_table_line(text: str) -> tuple[list[str], bool]:
        """Parse a table line into an annotated token list assuming no pipe in cells.

        The text '| a | b |' yields ([' a ', ' b '], False).
        The text '|:--|--:|' yields ([':--', '--:'], True).
        """
        return [cell.strip() for cell in text.split(COLUMN_SEP)[1:-1]], Table.is_table_head_sep(text)

    @staticmethod
    def left(text: str, width: int, fill: str = SPACE) -> str:
        """Left align the content text left and fill up to the width with fill (default: spaces)."""
        return text.ljust(width, fill)

    @staticmethod
    def center(text: str, width: int, fill: str = SPACE) -> str:
        """Center the content text left and fill up to the width with fill (default: spaces)."""
        return text.center(width, fill)

    @staticmethod
    def right(text: str, width: int, fill: str = SPACE) -> str:
        """Right align the content text left and fill up to the width with fill (default: spaces)."""
        return text.rjust(width, fill)

    def validate_post_table_line(self, text: str, last_line_is_table: bool) -> bool:
        """Blank or table was already last line of file is valid."""
        blank = not bool(text.rstrip(NL))
        has_col_sep = bool(text.lstrip().startswith(COLUMN_SEP))
        if last_line_is_table or blank and not has_col_sep:
            return True
        # We enforce blank line after tables
        diagnose = f'column separator ({COLUMN_SEP})' if COLUMN_SEP in text else 'non-blank line'
        message = (
            f'expected either table, blank line, or end of file but found {diagnose}'
            f' in location({self.resource.name}:{self.end_index + 1}@table[{self.line_count + 1}]) ->'
            f' ({text.rstrip(NL)})'
        )
        log.error(message)
        return False


def main(argv: list[str]) -> int:
    """Drive the transform."""

    for name in argv:
        resource = pathlib.Path(name)
        with open(resource, 'rt', encoding=ENCODING) as handle:
            lines = handle.readlines()
        table_lines = []
        in_table = False
        first_table_line: Union[int, None] = None
        last_line_is_table = False
        for slot, line in enumerate(lines):
            if Table.table_in(line):
                if first_table_line is None:
                    first_table_line = slot
                    last_line_is_table = False
                    in_table = True
                table_lines.append(line)
                continue
            if slot == len(lines):
                # Base case insurance
                log.warning(f'File {resource.name} ends with table line')
                last_line_is_table = in_table

            if in_table:
                # In file loop processing
                table = Table(resource, first_table_line, table_lines)  # type: ignore
                if not table.validate_post_table_line(line, last_line_is_table=last_line_is_table):
                    return 1
                if not table.validate_spec():
                    return 1
                if not table.derive_table_spec():
                    return 1
                table.render()
                lines[table.offset : table.offset + len(table.lines)] = table.lines  # type: ignore

                # Reset processing structures for further tables
                table_lines = []
                in_table = False

        # Post file loop processing - in case the table is at the end of the file (resource)
        if table_lines:
            table = Table(resource, first_table_line, table_lines)  # type: ignore
            if not table.validate_spec():
                return 1
            if not table.derive_table_spec():
                return 1
            table.render()
            lines[table.offset : table.offset + len(table.lines)] = table.lines  # type: ignore

        with open(BUILD_AT / resource.name, 'wt', encoding=ENCODING) as handle:
            handle.write(''.join(lines))
        log.info(f'document with aligned tables written to {BUILD_AT / resource.name}')

    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
