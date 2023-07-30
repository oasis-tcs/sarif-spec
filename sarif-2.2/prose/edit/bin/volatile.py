#! /usr/bin/env python
"""Volatile script file for prototyping that may take on different behaviors in time.

This one off script is a constant place to document the early stages of tools for processing the editable
sources and build the delivery items.

Currently impersonating phase zero concatenate and map from the initial sources to the GFM+gh_cosmetics file.
"""
import pathlib
import sys
from typing import Union

import yaml

ENCODING = 'utf-8'
NL = '\n'
CB_END = '}'
FULL_STOP = '.'

# Configuration and runtime parameter candidates:
BINDER_AT = pathlib.Path('etc') / 'bind.txt'
SOURCE_AT = pathlib.Path('src')
BUILD_AT = pathlib.Path('build')

# Specific tokens:
HC_BEG = '<!--'
HC_END = '-->'
YAML_SEP = '---'
TOK_TOC = '(#$thing$)'  # Transform phase ToC label string template replacing $thing$ with the old value
TOK_SEC = "<a id='$thing$'></a>"  # Transform phase section title label string template ($thing$ -> old value)
TOK_LAB = '{#'
H = '#'
TOC_HEADER = """Table of Contents
"""

TOC_TEMPLATE = {
    1: '$sec_cnt_disp$ [$text$](#$label$)  ',
    2: '\t$sec_cnt_disp$ [$text$](#$label$)  ',
    3: '\t\t$sec_cnt_disp$ [$text$](#$label$)  ',
    4: '\t\t\t$sec_cnt_disp$ [$text$](#$label$)  ',
}

# This value leads to empty line needed on GitHub to respect the new line for non-numerically starting lines
TOC_VERTICAL_SPACER = ''

# Data interface robustness hacks:
CHILDREN = 'children'
ENUMERATE = 'enumerate'
LABEL = 'label'
TOC = 'toc'

# Type declarations:
META_TOC_TYPE = dict[str, dict[str, Union[bool, str, list[dict[str, str]]]]]


def load_binder(binder_at: Union[str, pathlib.Path]) -> list[pathlib.Path]:
    """Load the linear binder text file into a list of file paths."""
    with open(binder_at, 'rt', encoding=ENCODING) as resource:
        return [pathlib.Path(entry.strip()) for entry in resource.readlines() if entry.strip()]


def end_of_toc_in(text: str) -> bool:
    """Detect the end of the table of contents."""
    return text.startswith('#') and ' Introduction' in text


def detect_meta(text_lines: list[str]) -> tuple[META_TOC_TYPE, list[str]]:
    """Extract any YAML data from top, remove used lines from text lines, and yield meta as well as remaining lines."""
    meta_lines = []
    if text_lines[0].startswith(HC_BEG) and text_lines[1].startswith(YAML_SEP):
        for line in text_lines[2:]:
            if line.startswith(YAML_SEP):
                break
            meta_lines.append(line)

    from_here = len(meta_lines) + 4
    if from_here > 4:
        text_lines = text_lines[from_here:]

    return yaml.safe_load(''.join(meta_lines)) if meta_lines else {}, text_lines


def load_document(path: Union[str, pathlib.Path]) -> tuple[META_TOC_TYPE, list[str]]:
    """Load the text file into a list of strings and harvest any YAML meta info (if present remove the lines)."""
    with open(path, 'rt', encoding=ENCODING) as resource:
        return detect_meta(resource.readlines())


def dump_assembly(text_lines: list[str], to_path: Union[str, pathlib.Path]) -> None:
    """Dump the lines of text into the text file at path."""
    with open(to_path, 'wt', encoding=ENCODING) as resource:
        resource.write(''.join(text_lines))


def label_derive_from(text: str) -> str:
    """Transform text to kebab style conventional label assuming no newlines present."""
    good_nuff = (' ', '.', ',', ';', '?', '!', '_', '(', ')', '[', ']', '{', '}', '<', '>', '\\', '/', '$', ':')
    slug = text.strip()
    for bad in good_nuff:
        slug = slug.replace(bad, '-')
    parts = slug.split('-')
    slug = '-'.join(s for s in parts if s and s != '-')
    return slug.lower()


def main(argv: list[str]) -> int:
    """Drive the assembly."""

    bind_seq_path = pathlib.Path(argv[0]) if argv else BINDER_AT
    binder = load_binder(bind_seq_path)
    for resource in binder:
        if not (SOURCE_AT / resource).is_file():
            print(f'Problem reading {resource}')
            return 1

    lines: list[str] = []
    meta_hooks = {}
    first_meta_slot = None
    for resource in binder:
        meta, part_lines = load_document(SOURCE_AT / resource)
        if part_lines[-1] != NL:
            part_lines.append(NL)
        if meta:
            meta_hooks[len(lines)] = meta
            meta_hooks[len(lines) + len(part_lines) - 1] = {}
            if first_meta_slot is None:
                first_meta_slot = len(lines) + len(part_lines) - 1
        lines.extend(part_lines)

    # TODO: counter management -> class
    lvl_min, lvl_sup = 1, 7
    sec_cnt = {f'{H * level} ': 0 for level in range(lvl_min, lvl_sup)}
    sec_lvl = {f'{H * level} ': level for level in range(lvl_min, lvl_sup)}
    lvl_sec = {level: f'{H * level} ' for level in range(lvl_min, lvl_sup)}
    H1 = f'{H} '
    cur_lvl = sec_lvl[H1]
    meta_hook = {}
    # TODO: ToC builder -> class
    tic_toc = [TOC_HEADER]
    did_appendix_sep = False
    for slot, line in enumerate(lines):
        if meta_hooks.get(slot) is not None:
            meta_hook = meta_hooks[slot]
        for tag in sec_cnt:
            if line.startswith(tag):
                # manage counter
                if not meta_hook:
                    # auto counters
                    nxt_lvl = sec_lvl[tag]
                    sec_cnt[tag] += 1
                    if nxt_lvl < cur_lvl:
                        for level in range(nxt_lvl + 1, lvl_sup):
                            sec_cnt[lvl_sec[level]] = 0
                    sec_cnt_disp_vec = []
                    for s_tag, cnt in sec_cnt.items():
                        if cnt == 0:
                            raise RuntimeError(f'counting is hard: {sec_cnt} at {tag} for {slot}:{line.rstrip(NL)}')
                        sec_cnt_disp_vec.append(str(cnt))
                        if s_tag == tag:
                            break
                    sec_cnt_disp = FULL_STOP.join(sec_cnt_disp_vec)
                    # Hack to amend first level numeric section counter displays with a full stop - do not ask ...
                    if FULL_STOP not in sec_cnt_disp:
                        sec_cnt_disp += FULL_STOP
                else:
                    # pull in counters from meta
                    app_lvl = 1  # belt and braces ...
                    text = line.split(tag, 1)[1].rstrip()
                    if TOK_LAB in text:
                        # special label
                        label = text.split(TOK_LAB, 1)[1].rstrip(CB_END)
                        text = text.split(TOK_LAB, 1)[0]
                    if text == meta_hook[TOC][LABEL]:
                        sec_cnt_disp = meta_hook[TOC][ENUMERATE]  # type: ignore
                        app_lvl = 1
                    elif meta_hook[TOC].get(CHILDREN):
                        for cand in meta_hook[TOC][CHILDREN]:  # type: ignore
                            if text == cand[LABEL]:  # type: ignore
                                sec_cnt_disp = cand[ENUMERATE]  # type: ignore
                                app_lvl = 2

                # manage label
                text = line.split(tag, 1)[1].rstrip()
                if TOK_LAB in text:
                    # special label
                    label = text.split(TOK_LAB, 1)[1].rstrip(CB_END)
                    text = text.split(TOK_LAB, 1)[0]
                else:
                    label = label_derive_from(text)

                line = tag + text + ' ' + TOK_SEC.replace('$thing$', label)

                line = line.replace(tag, f'{tag}{sec_cnt_disp} ', 1) + NL
                lines[slot] = line
                cur_lvl = nxt_lvl
                if not did_appendix_sep and meta_hook and slot < first_meta_slot:  # type: ignore
                    tic_toc.append(TOC_VERTICAL_SPACER)
                    did_appendix_sep = True
                toc_template = TOC_TEMPLATE[cur_lvl if not meta_hook else app_lvl]
                tic_toc.append(
                    toc_template.replace('$sec_cnt_disp$', sec_cnt_disp)
                    .replace('$text$', text)
                    .replace('$label$', label)
                )

    tic_toc.append(NL)
    # Inject the table of contents:
    for slot, line in enumerate(lines):
        if end_of_toc_in(line):
            lines[slot] = NL.join(tic_toc) + line
            break

    # remove any trailing blank line
    while lines[-1] == NL:
        del lines[-1]

    BUILD_AT.mkdir(parents=True, exist_ok=True)

    dump_assembly(lines, BUILD_AT / 'tmp.md')

    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
