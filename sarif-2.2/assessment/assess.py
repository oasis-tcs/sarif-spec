"""Read-only assessment of the SARIF 2.2 CSD01 prose against its schema, examples and twins.

Usage: python assess.py <sarif-2.2 dir> <out.json>
Keyed where possible: objects by `## `x` Object` headings, properties by `### `p` Property` headings, both matched
to the schema's $defs and properties by name; statements by bold BCP 14 keywords.
"""

import json
import pathlib
import re
import sys
from collections import Counter, defaultdict

import jsonschema

ROOT = pathlib.Path(sys.argv[1])
SRC = ROOT / 'prose' / 'edit' / 'src'
SCHEMA = json.loads((ROOT / 'schema' / 'sarif.json').read_text(encoding='utf-8'))
DEFS = SCHEMA['$defs']
DEFS_LC = {k.lower(): k for k in DEFS}
BIND = [line.strip() for line in (ROOT / 'prose' / 'edit' / 'etc' / 'bind.txt').read_text().splitlines() if line.strip()]

KW = r'SHALL NOT|SHOULD NOT|MUST NOT|SHALL|SHOULD|MUST|MAY|REQUIRED|RECOMMENDED|OPTIONAL|NOT RECOMMENDED'
BOLD_KW = re.compile(r'\*\*(' + KW + r')\*\*')
PLAIN_KW_LOWER = re.compile(r'(?<![\w*`])(must|shall|must not|shall not|required)(?![\w*`])')
OBJ_H = re.compile(r'^## `(\w+)` Object')
PROP_H = re.compile(r'^#{3,4} (.*?)[Pp]ropert(?:y|ies)\b')
NAMES = re.compile(r'`([$\w]+)`')
FENCE = re.compile(r'^(> ?)?```(\w*)')
ROLES = {
    'producer': r'\b(SARIF )?producers?\b|\banalysis tools?\b|\bthe tool\b|\bdirect producers?\b',
    'consumer': r'\b(SARIF )?consumers?\b',
    'viewer': r'\bviewers?\b',
    'converter': r'\bconverters?\b',
    'post-processor': r'\bpost-processors?\b',
    'result management system': r'\bresult management systems?\b',
    'engineering system': r'\bengineering systems?\b',
    'driver/extension': r'\bdrivers?\b|\bextensions?\b',
}
HEDGES = [
    'as appropriate', 'if appropriate', 'in some cases', 'might choose', 'can choose', 'where possible', 'if possible',
    'it is up to', 'at the discretion', 'reasonable', 'sensible', 'as needed', 'if desired', 'typically', 'usually',
    'in general', 'generally', 'for the most part', 'ordinarily',
]
TYPE_WORDS = {
    'string': 'string', 'integer': 'integer', 'number': 'number', 'boolean': 'boolean', 'array': 'array',
    'object': 'object', 'Boolean': 'boolean',
}


def sentences(text):
    text = re.sub(r'\s+', ' ', text)
    return [s.strip() for s in re.split(r'(?<=[.;:])\s+(?=[A-Z(`"])', text) if s.strip()]


def parse():
    """Walk the bound sources in order: sections, statements, fences."""
    current_obj, current_prop = None, None
    sections = defaultdict(lambda: defaultdict(list))  # obj -> prop -> lines
    statements, fences, lower_kw, hedges = [], [], [], []
    for name in BIND:
        path = SRC / name
        if not path.is_file():
            continue
        lines = path.read_text(encoding='utf-8').splitlines()
        in_fence, fence_lines, fence_start, fence_lang = False, [], 0, ''
        para = []

        def flush(para, line_no):
            if not para:
                return
            text = ' '.join(para)
            quoted = text.lstrip().startswith('>')
            for s in sentences(text.lstrip('> ')):
                kws = BOLD_KW.findall(s)
                if kws and not quoted:
                    statements.append({'file': name, 'line': line_no, 'obj': current_obj, 'prop': current_prop, 'kws': kws, 'text': s})
                for m in PLAIN_KW_LOWER.finditer(s):
                    if not quoted:
                        lower_kw.append({'file': name, 'line': line_no, 'word': m.group(1), 'text': s})
                low = s.lower()
                for h in HEDGES:
                    if re.search(r'\b' + re.escape(h) + r'\b', low) and BOLD_KW.search(s):
                        hedges.append({'file': name, 'line': line_no, 'hedge': h, 'text': s})

        for i, line in enumerate(lines, 1):
            m = FENCE.match(line.strip()) if line.strip().lstrip('> ').startswith('```') or line.strip().startswith('```') else None
            stripped = re.sub(r'^> ?', '', line)
            if stripped.startswith('```'):
                if not in_fence:
                    flush(para, i)
                    para = []
                    in_fence, fence_lines, fence_start, fence_lang = True, [], i, stripped[3:].strip()
                else:
                    fences.append({'file': name, 'line': fence_start, 'lang': fence_lang, 'obj': current_obj, 'prop': current_prop, 'body': '\n'.join(fence_lines)})
                    in_fence = False
                continue
            if in_fence:
                fence_lines.append(stripped)
                continue
            if line.startswith('#'):
                flush(para, i)
                para = []
                if line.startswith('## '):
                    mo = OBJ_H.match(line)
                    current_obj = mo.group(1) if mo else None
                    current_prop = None
                elif (mp := PROP_H.match(line)) and NAMES.findall(mp.group(1)):
                    names = NAMES.findall(mp.group(1))
                    current_prop = names[0]
                    for extra in names[1:]:
                        sections[current_obj][extra] += []
                elif line.startswith('### '):
                    current_prop = None
                continue
            if current_obj:
                sections[current_obj][current_prop].append(line)
            if not line.strip():
                flush(para, i)
                para = []
            else:
                para.append(line)
        flush(para, len(lines))
    return sections, statements, fences, lower_kw, hedges


def schema_coverage(sections):
    out = {'objects_missing_in_prose': [], 'objects_without_schema_def': [], 'props_missing_in_prose': {}, 'props_without_schema': {}}
    prose_objs = {o.lower(): o for o in sections}
    for d in DEFS:
        if d.lower() not in prose_objs and DEFS[d].get('type') == 'object':
            out['objects_missing_in_prose'].append(d)
    for o in sections:
        key = DEFS_LC.get(o.lower())
        if o.lower() == 'sariflog':
            schema_props = set(SCHEMA.get('properties', {}))
        elif key:
            schema_props = set(DEFS[key].get('properties', {}))
        else:
            out['objects_without_schema_def'].append(o)
            continue
        prose_props = {p for p in sections[o] if p}
        miss = sorted(schema_props - prose_props - {'properties'})
        extra = sorted(prose_props - schema_props)
        if miss:
            out['props_missing_in_prose'][o] = miss
        if extra:
            out['props_without_schema'][o] = extra
    return out


def prop_schema(obj, prop):
    if obj.lower() == 'sariflog':
        return SCHEMA.get('properties', {}).get(prop)
    key = DEFS_LC.get(obj.lower())
    return DEFS[key].get('properties', {}).get(prop) if key else None


def enum_and_defaults(sections):
    enums, defaults, types, presence = [], [], [], []
    for obj, props in sections.items():
        for prop, lines in props.items():
            if not prop:
                continue
            ps = prop_schema(obj, prop)
            if ps is None:
                continue
            text = '\n'.join(lines)
            schema_enum = ps.get('enum') or ps.get('items', {}).get('enum')
            if schema_enum:
                # values as list items or table cells: `value` or "value" at the start of an item / cell
                listed = set(re.findall(r'^\s*(?:[-*]|\d+\.)\s+`"?([\w-]+)"?`', text, re.M))
                listed |= set(re.findall(r'^\|\s*`"?([\w-]+)"?`\s*\|', text, re.M))
                quoted = set(re.findall(r'`"([\w.-]+)"`', text)) | set(re.findall(r'"([\w.-]+)"', text))
                missing = sorted(v for v in schema_enum if v not in listed and v not in quoted)
                unknown = sorted(v for v in listed if v not in schema_enum)
                enums.append({'obj': obj, 'prop': prop, 'schema': schema_enum, 'listed': sorted(listed), 'missing': missing, 'unknown': unknown})
            m = re.search(r'(?:SHALL\*\* default to|default value (?:is|of [^.]*? is)|defaults? to)\s+`?"?([\w.-]+)"?`?', text)
            if m:
                sd = ps.get('default')
                pd = m.group(1) if m else None
                sdn = json.dumps(sd).strip('"') if sd is not None else None
                if sdn != pd and not (sd is not None and pd is not None and str(sd).lower() == pd.lower()):
                    defaults.append({'obj': obj, 'prop': prop, 'schema': sd, 'prose': pd})
            st = ps.get('type')
            mt = re.search(r'whose value is an? (string|integer|number|Boolean|boolean|array|object)\b', text)
            if st and mt and TYPE_WORDS[mt.group(1)] != st and not (st == 'integer' and mt.group(1) == 'number'):
                types.append({'obj': obj, 'prop': prop, 'schema': st, 'prose': mt.group(1)})
            first = next((s for s in sentences(text) if BOLD_KW.search(s)), '')
            key = 'sarifLog' if obj.lower() == 'sariflog' else DEFS_LC.get(obj.lower())
            req = prop in (SCHEMA.get('required', []) if key == 'sarifLog' else DEFS.get(key, {}).get('required', []))
            kw = BOLD_KW.search(first).group(1) if first else None
            if kw and (req and kw in ('MAY', 'SHOULD')) or (not req and kw == 'SHALL' and 'contain' in first and 'If' not in first[:3]):
                presence.append({'obj': obj, 'prop': prop, 'schema_required': req, 'prose_kw': kw, 'text': first[:220]})
    return enums, defaults, types, presence


def subjects(statements):
    c = Counter()
    for s in statements:
        t = s['text']
        if any(re.search(rx, t, re.I) for rx in ROLES.values()):
            c['role named'] += 1
        elif re.search(r'`|thisObject|objects?|propert(y|ies)|log file|SARIF file', t):
            c['document (object/property is subject)'] += 1
        else:
            c['no subject found'] += 1
    presence = [s for s in statements if re.search(r'\*\*(SHALL|SHALL NOT|SHOULD|SHOULD NOT)\*\* (?:also )?(?:be present|be absent|not be present)', s['text'])]
    conditional = [s for s in presence if re.match(r'(If|When|Unless|Otherwise|In|Depending)', s['text'])]
    return {'by_subject': dict(c), 'presence_rules': len(presence), 'conditional_presence_rules': len(conditional)}


def classify(statements):
    subj = Counter()
    restates = 0
    by_role = Counter()
    unbound = 0
    schema_like = re.compile(
        r'SHALL\*\* (?:be|contain|have)|\*\*(?:SHALL|MAY|SHOULD)\*\* contain a property|whose value is|'
        r'default|array of|unique|\bminimum\b|non-negative|integer|one of the following values|SHALL NOT\*\* be present', re.I)
    for s in statements:
        t = s['text']
        roles = [r for r, rx in ROLES.items() if re.search(rx, t, re.I)]
        for r in roles:
            by_role[r] += 1
        if not roles:
            unbound += 1
        if schema_like.search(t) and s['prop']:
            restates += 1
        for k in s['kws']:
            subj[k] += 1
    return {'keywords': dict(subj), 'by_role': dict(by_role), 'statements': len(statements), 'no_role_named': unbound, 'schema_like_in_property_sections': restates}


MARKER = re.compile(r'^\.{0,3}(member|object)-in[jk]ect')


def classify_error(e):
    msg = e.message
    if e.validator == 'required':
        return 'context'
    if e.validator == 'additionalProperties' and all(MARKER.match(k) for k in re.findall(r"'([^']+)'", msg.split('(')[-1])):
        return 'marker'
    if e.validator in ('anyOf', 'oneOf') and not list(e.absolute_path):
        return 'context'
    if e.validator in ('anyOf', 'oneOf'):
        sub = [classify_error(c) for c in e.context]
        return 'context' if sub and all(c in ('context', 'marker') for c in sub) else 'content'
    if e.validator == 'uniqueItems':
        return 'marker'
    return 'content'


def find_def_for(fragment):
    if not isinstance(fragment, dict):
        return None
    keys = set(fragment)
    if {'version', 'runs'} <= keys:
        return '#'
    keys = {k for k in keys if not MARKER.match(k)}
    cands = [d for d, v in DEFS.items() if keys and keys <= set(v.get('properties', {}))]
    return cands


def twins_and_examples():
    reg_schema = jsonschema.Draft202012Validator(SCHEMA)
    out = {'twins': [], 'examples': []}
    for f in sorted((SRC / 'json-examples').glob('*.json')):
        rec = {'file': f.name}
        try:
            data = json.loads(f.read_text(encoding='utf-8'))
        except json.JSONDecodeError as e:
            rec['parse'] = str(e)
            out['twins'].append(rec)
            continue
        target = find_def_for(data)
        if target == '#':
            errs = list(reg_schema.iter_errors(data))
            rec['as'] = 'sarifLog'
            rec['errors'] = [f'{"/".join(map(str, e.absolute_path))}: {e.message[:140]}' for e in errs[:5]]
            rec['n_errors'] = len(errs)
        elif target:
            results = {}
            for d in target:
                sub = {'$schema': SCHEMA['$schema'], '$defs': DEFS, '$ref': f'#/$defs/{d}'}
                errs = list(jsonschema.Draft202012Validator(sub).iter_errors(data))
                results[d] = errs
            section_obj = DEFS_LC.get(f.name.split('_')[0].split('-object')[0].rsplit('-', 1)[-1].replace('-', ''))
            prefer = [section_obj, 'run', 'result', 'tool', 'toolComponent', 'invocation']
            rank = lambda d: (len([e for e in results[d] if classify_error(e) == 'content']), len(results[d]), prefer.index(d) if d in prefer else 99, d.startswith('externalProp'))
            best = min(results, key=rank)
            rec['classes'] = Counter(classify_error(e) for e in results[best])
            rec['as'] = best
            rec['n_errors'] = len(results[best])
            rec['errors'] = [f'{"/".join(map(str, e.absolute_path))}: {e.message[:160]}' for e in results[best] if classify_error(e) == 'content'][:6]
        else:
            rec['as'] = None
            rec['top_keys'] = sorted(data)[:12] if isinstance(data, dict) else type(data).__name__
        out['twins'].append(rec)
    for f in sorted((ROOT / 'example').glob('*.json')):
        data = json.loads(f.read_text(encoding='utf-8'))
        errs = list(reg_schema.iter_errors(data))
        out['examples'].append({'file': f.name, 'n_errors': len(errs), 'errors': [f'{"/".join(map(str, e.absolute_path))}: {e.message[:140]}' for e in errs[:5]]})
    return out


def marker_stats():
    c = Counter()
    for f in (SRC / 'json-examples').glob('*.json'):
        for m in re.finditer(r'"(\.{0,3}(?:member|object)-in[a-z]+ct[-\w]*)"', f.read_text(encoding='utf-8')):
            c[re.sub(r'-\d+$', '', m.group(1))] += 1
    return dict(c)


def twin_mapping(fences):
    per_file_fences = Counter(f['file'][:-3] for f in fences if f['lang'] == 'json')
    per_file_twins = Counter(t.name.split('_')[0] for t in (SRC / 'json-examples').glob('*.json'))
    return {'json_fences_by_file': dict(per_file_fences), 'twins_by_file': dict(per_file_twins),
            'files_fences_without_twin': sorted(k for k in per_file_fences if k not in per_file_twins)}


def snippet_stats(fences):
    langs = Counter(f['lang'] or '(none)' for f in fences)
    json_f = [f for f in fences if f['lang'] in ('json', 'jsonc', 'json5')]
    parse_ok, elided, commented, margin_refs = 0, 0, 0, 0
    for f in json_f:
        b = f['body']
        if re.search(r'\.\.\.|…', b):
            elided += 1
        if re.search(r'\s#\s', b) or re.search(r'//', b):
            commented += 1
        if '((#' in b or '(#' in b or '§' in b:
            margin_refs += 1
        try:
            json.loads(b)
            parse_ok += 1
        except json.JSONDecodeError:
            pass
    return {'fences': len(fences), 'langs': dict(langs), 'json': len(json_f), 'json_parse_ok': parse_ok, 'json_elided': elided,
            'json_with_comments': commented, 'json_with_section_refs': margin_refs}


def main():
    sections, statements, fences, lower_kw, hedges = parse()
    cov = schema_coverage(sections)
    enums, defaults, types, presence = enum_and_defaults(sections)
    result = {
        'coverage': cov,
        'enums': enums,
        'defaults': defaults,
        'types': types,
        'presence': presence,
        'statements': classify(statements),
        'statement_samples_no_role': [s for s in statements if not any(re.search(rx, s['text'], re.I) for rx in ROLES.values())][:0],
        'lower_kw': lower_kw,
        'hedges': hedges,
        'snippets': snippet_stats(fences),
        'markers': marker_stats(),
        'twin_mapping': twin_mapping(fences),
        'subjects': subjects(statements),
        'twins_examples': twins_and_examples(),
        'n_sections_objects': len(sections),
    }
    pathlib.Path(sys.argv[2]).write_text(json.dumps(result, indent=1, default=str), encoding='utf-8')


main()
