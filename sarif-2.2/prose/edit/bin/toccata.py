#! /usr/bin/env python
"""Patch the table of contents and other portions of the HTML delivery item."""
import json
import pathlib
import re
import sys
from typing import Union

ENCODING = 'utf-8'
NL = '\n'
SP = ' '
BACK_TICK = '`'
COLON = ':'
DASH = '-'
DOT = '.'

LANG_PATCH = '<html xmlns="http://www.w3.org/1999/xhtml" lang="en" xml:lang="en">'
LOGO_TARGET = 'https://docs.oasis-open.org/templates/OASISLogo-v3.0.png'

TOC_STARTSWITH_TRIGGER = '<h1 id="table-of-contents'
INTRO_STARTSWITH_TRIGGER = '<h1 id="1-introduction'

# Configuration and runtime parameter candidates:
BUILD_AT = pathlib.Path('build')
HTML_IN_AT = BUILD_AT / 'tmp.html'
TOC_AT = BUILD_AT / 'toc-mint.json'
LOGO_AT = pathlib.Path('..') / 'media' / 'logo-data-url.txt'
BASE_CSS_AT = pathlib.Path('..') / 'share' / 'style' / 'base.css'
SKIN_CSS_AT = pathlib.Path('..') / 'share' / 'style' / 'skin.css'

IN_TITLE_TRIGGER_IS = '<title>'
TITLE_INNER_HTML_MARKER_IS = 'tmp'
PATCH_TITLE_INNER_HTML = 'Static Analysis Results Interchange Format (SARIF) Version 2.2'
CODE_TERM_DETECT = re.compile(r'(?P<intro>[^`]*)`(?P<code>[^`]+)`(?P<rest>.*)')  # intro*`code-term`rest* pattern

# Type declarations:
MetaTocType = dict[str, dict[str, Union[bool, str, list[dict[str, str]]]]]
SecLvlCntType = tuple[int, int, int, int, int, int]
ApxLvlUnionType = Union[bool, int]
SecNumDispType = str
SecTocText = str
SecTocTargetSlug = str
TocEntryType = tuple[SecLvlCntType, ApxLvlUnionType, SecNumDispType, SecTocText, SecTocTargetSlug]


def load_toc(toc_at: Union[str, pathlib.Path]) -> list[TocEntryType]:
    """Load the TOC JSON file into a list of toc entries."""
    with open(toc_at, 'rt', encoding=ENCODING) as resource:
        return [(tuple(e[0]), *e[1:]) for e in json.load(resource) if e]  # type: ignore # noqa


def patch_code_term_in_html_toc_entry(text: str) -> str:
    """Best effort patching of our toc entry use case with code rest."""
    term = CODE_TERM_DETECT.match(text)
    if term:
        # Found inline code term in text
        found = term.groupdict()
        intro = found['intro']
        code = found['code']
        rest = found['rest']
        return f'{intro}<code>{code}</code>{rest}' if code and rest else text
    return text


def generate_toc(toc_db: list[TocEntryType]) -> str:
    """Generate the table of contents from the database."""
    entries_prefix = ['<div id="toc_container">', '<ul class="toc_list">']
    entries_postfix = ['</ul>', '</div>']
    entries = []
    past = 0
    in_appendix = False
    for slot, toc_entry in enumerate(toc_db):
        _levels, is_appendix_level, num_disp, text, slug = toc_entry
        if BACK_TICK in text:
            text = patch_code_term_in_html_toc_entry(text)
        pres = num_disp.rstrip('.').count(DOT) + 1 if not is_appendix_level else is_appendix_level
        if is_appendix_level and not in_appendix:
            in_appendix = True
            # past = 3
        if past == 0:
            if pres != 1:
                raise RuntimeError(f'error in first toc db entry: ({toc_entry})')
            hack_a_did_ack = '<ul>' if slot else ''
            entries.append(f'{hack_a_did_ack}<li>{num_disp} <a href="#{slug}">{text}</a></li>')
            past = pres
            continue
        if pres == past:
            entries.append(f'<li>{num_disp} <a href="#{slug}">{text}</a></li>')
            past = pres
            continue
        if pres > past:
            patch_me = entries[slot - 1]
            there = len('</li>')
            entries[slot - 1] = patch_me[:-there] + '<ul>'
            entries.append(f'<li>{num_disp} <a href="#{slug}">{text}</a></li>')
            past = pres
            continue
        if pres < past:
            stack = past
            closing = ''
            while stack > pres:
                closing += '</ul></li>'
                stack -= 1
            entries.append(f'{closing}<li>{num_disp} <a href="#{slug}">{text}</a></li>')
            past = pres
            continue

    return NL.join(entries_prefix + entries + entries_postfix)


def main(args: list[str]) -> int:
    """Drive the injections."""
    if args:
        print('ERROR: No parameters expected.')
        return 2

    toc_db = load_toc(TOC_AT)
    the_toc = generate_toc(toc_db)

    # Load the CSS and logo file data to inject later into the single-file HTML delivery item
    with open('../share/style/base.css', 'rt', encoding=ENCODING) as handle:
        base_css = handle.read()
    with open('../share/style/skin.css', 'rt', encoding=ENCODING) as handle:
        skin_css = handle.read()
    with open(LOGO_AT, 'rt', encoding=ENCODING) as handle:
        logo_data = handle.read().strip()

    # Pick up the previous stage HTML delivery item for processing
    with open('build/tmp.html', 'rt', encoding=ENCODING) as handle:
        incoming = handle.readlines()

    outgoing = []
    in_toc = False
    for line in incoming:
        # HTML head/title inner HTML processing needed?
        if TITLE_INNER_HTML_MARKER_IS in line:
            # Patch the title to match the spec
            line = line.replace(TITLE_INNER_HTML_MARKER_IS, PATCH_TITLE_INNER_HTML)

        # Table of content processing needed?
        if in_toc:
            if line.startswith(INTRO_STARTSWITH_TRIGGER):
                in_toc = False
                outgoing.append(line)
            else:
                pass
            continue
        if not in_toc and line.startswith(TOC_STARTSWITH_TRIGGER):
            in_toc = True
            outgoing.append(line)
            outgoing.append(the_toc)  # Here we inject the gerenated table of content
            continue

        # Patch an unescaped opening angle bracket to pacify the markdown parser
        if '<component>' in line:
            line = line.replace('<component>', '&lt;component>')

        # Various patches
        if line.startswith('<html xmlns'):
            line = LANG_PATCH  # Add a matching english language value
        elif '</style>' in line:
            line = NL + base_css + NL + skin_css + NL + line  # Inject inline styles
        elif 'style/base.css' in line:
            continue
        elif 'style/skin.css' in line:
            continue
        elif LOGO_TARGET in line:
            line = line.replace(LOGO_TARGET, logo_data)  # inject logo as data URL

        outgoing.append(line)

    # Write the HTML delivery item of this stage
    with open('build/injected.html', 'wt', encoding=ENCODING) as handle:
        handle.write(''.join(outgoing))
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
