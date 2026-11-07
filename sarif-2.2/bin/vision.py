"""SARIF vision: records and the schema are the sources, the views are derived and checked.

Usage (from sarif-2.2/):
  python -I bin/vision.py migrate   seed records/examples.yaml from the twins (once; review the hosts afterwards)
  python -I bin/vision.py derive    write views/ from the schema, the records, the twins and the prose
  python -I bin/vision.py check     fail when a view differs from what derive would write, or a record is incomplete

Keyed, not textual, wherever the sources allow it: objects by their `` ## `x` Object `` headings, properties by
their `` ### `p` Property `` headings, matched to the schema's $defs by name; examples by their twin file and the
schema definition that hosts them; statements by bold BCP 14 keywords. See VISION.md.
"""

import copy
import json
import pathlib
import re
import sys
from collections import Counter, defaultdict

import jsonschema
import yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent
PROSE = ROOT / 'prose' / 'edit'
SRC = PROSE / 'src'
TWINS = SRC / 'json-examples'
RECORDS = ROOT / 'records'
VIEWS = ROOT / 'views'
SCHEMA = json.loads((ROOT / 'schema' / 'sarif.json').read_text(encoding='utf-8'))
DEFS = SCHEMA['$defs']
DEFS_LC = {k.lower(): k for k in DEFS}
LOG = 'sarifLog'  # the root of the schema, named as the prose names it

KW = r'SHALL NOT|SHOULD NOT|MUST NOT|SHALL|SHOULD|MUST|MAY|REQUIRED|RECOMMENDED|OPTIONAL'
BOLD_KW = re.compile(r'\*\*(' + KW + r')\*\*')
OBJ_H = re.compile(r'^## `(\w+)` Object')
PROP_H = re.compile(r'^(#{3,4}) (.*?)\s*(?:\{#[^}]*\})?\s*$')
WELL_FORMED = re.compile(r'^(?:`\$?\w+`(?:, and |, | and )?)+ Propert(?:y|ies)$')
BROKEN_KEY = re.compile(r'^`?(\$?\w+)`? [Pp]roperty$')
NAMES = re.compile(r'`(\$?\w+)`')
KEYWORD_SET = re.compile(r'either \*\*[A-Z ]+\*\*(?:, \*\*[A-Z ]+\*\*)*,? or \*\*[A-Z ]+\*\*')
DEFAULT = re.compile(r'^If (?:this property|`([\w.]+)`) is absent, (?:it|`[\w.]+`) \*\*SHALL\*\* default to (?:the array )?`([^`]+)`')


# ── sources ───────────────────────────────────────────────────────────────────

def bound_files():
    names = [n.strip() for n in (PROSE / 'etc' / 'bind.txt').read_text(encoding='utf-8').splitlines()]
    return [n for n in names if n.endswith('.md') and (SRC / n).is_file()]


def sentences(text):
    text = re.sub(r'\s+', ' ', text)
    return [s.strip() for s in re.split(r'(?<=[.;:])\s+(?=[A-Z(`"*])', text) if s.strip()]


TABLE_ROWS = '\n'.join(line for name in bound_files() for line in (SRC / name).read_text(encoding='utf-8').splitlines() if line.lstrip().startswith('|'))


def read_prose():
    """Sections (object -> property -> text), headings, statements and JSON fences, in bind order."""
    sections = defaultdict(lambda: defaultdict(list))
    headings, statements, fences = [], [], []
    for name in bound_files():
        obj, prop, heading = None, None, ''
        in_fence, fence, start, para = False, [], 0, []

        def flush(line_no):
            text = ' '.join(para)
            if text and not text.lstrip().startswith('>'):
                for s in sentences(text):
                    if BOLD_KW.search(s):
                        statements.append({'file': name, 'line': line_no, 'obj': obj, 'prop': prop, 'heading': heading, 'text': s})
            para.clear()

        for i, line in enumerate((SRC / name).read_text(encoding='utf-8').splitlines(), 1):
            bare = re.sub(r'^> ?', '', line)
            if bare.startswith('```'):
                if in_fence:
                    fences.append({'file': name, 'line': start, 'lang': lang, 'obj': obj, 'body': '\n'.join(fence)})
                else:
                    flush(i)
                    fence, start, lang = [], i, bare[3:].strip()
                in_fence = not in_fence
                continue
            if in_fence:
                fence.append(bare)
                continue
            if line.startswith('#'):
                flush(i)
                heading = re.sub(r'\{#[^}]*\}', '', line.lstrip('#')).strip()
                if line.startswith('## '):
                    m = OBJ_H.match(line)
                    obj, prop = (m.group(1) if m else None), None
                elif obj and (m := PROP_H.match(line)) and re.search(r'[Pp]ropert(?:y|ies)\s*$', m.group(2)):
                    text = m.group(2)
                    names = NAMES.findall(text) if WELL_FORMED.match(text) else []
                    broken = None
                    if not names and (b := BROKEN_KEY.match(text)):
                        names, broken = [b.group(1)], text
                    headings.append({'file': name, 'line': i, 'obj': obj, 'names': names, 'text': text, 'broken': broken})
                    prop = names[0] if names else None
                    for n in names[1:]:
                        sections[obj][n] += []
                else:
                    prop = None
                continue
            if obj:
                sections[obj][prop].append(line)
            if line.strip():
                para.append(line)
            else:
                flush(i)
        flush(i)
    return sections, headings, statements, fences


def schema_of(obj):
    if obj == LOG:
        return SCHEMA
    key = DEFS_LC.get(obj.lower())
    return DEFS[key] if key else None


# ── examples: markers, context, validation ────────────────────────────────────

def markers():
    rec = yaml.safe_load((RECORDS / 'markers.yaml').read_text(encoding='utf-8'))
    return re.compile(rec['pattern']), re.compile(rec['looks-like'])


def strip_markers(node, good, bad, found):
    """The twin without its markers; malformed markers are collected in `found`."""
    if isinstance(node, dict):
        out = {}
        for k, v in node.items():
            if good.match(k):
                continue
            if bad.search(k):
                found.append(k)
                continue
            out[k] = strip_markers(v, good, bad, found)
        return out
    if isinstance(node, list):
        out = []
        for v in node:
            if isinstance(v, str) and good.match(v):
                continue
            if isinstance(v, dict) and len(v) == 1 and good.match(next(iter(v))):
                continue
            if isinstance(v, str) and bad.search(v):
                found.append(v)
                continue
            out.append(strip_markers(v, good, bad, found))
        return out
    return node


def resolve(node):
    while '$ref' in node:
        node = DEFS[node['$ref'].rsplit('/', 1)[-1]]
    return node


def minimal(node, depth=0):
    """The smallest value the schema accepts for `node`: required members only, first alternatives."""
    node = resolve(node)
    if depth > 12:
        return {}
    if 'enum' in node:
        return node['enum'][0]
    if 'const' in node:
        return node['const']
    kind = node.get('type', 'object')
    kind = kind[0] if isinstance(kind, list) else kind
    if kind == 'object':
        required = list(node.get('required', []))
        for alt in node.get('anyOf', node.get('oneOf', []))[:1]:
            required += alt.get('required', [])
        return {r: minimal(node.get('properties', {}).get(r, {}), depth + 1) for r in required}
    if kind == 'array':
        return [minimal(node.get('items', {}), depth + 1)] if node.get('minItems', 0) else []
    if kind == 'string':
        if node.get('format') in ('uri', 'uri-reference'):
            return 'file:///x'
        if node.get('format') == 'date-time':
            return '2026-01-01T00:00:00Z'
        if 'pattern' in node:
            return '00000000-0000-0000-0000-000000000000'
        return 'x'
    if kind in ('integer', 'number'):
        return max(node.get('minimum', 0), 0)
    if kind == 'boolean':
        return False
    return None


def at(instance, path):
    for p in path:
        instance = instance[p]
    return instance


def validator_for(host):
    if host == LOG:
        return jsonschema.Draft202012Validator(SCHEMA)
    return jsonschema.Draft202012Validator({'$schema': SCHEMA['$schema'], '$defs': DEFS, '$ref': f'#/$defs/{host}'})


def with_context(data, host):
    """Inject what the schema requires and the display leaves out; return the instance and the injected paths."""
    v = validator_for(host)
    injected = []
    for _ in range(40):
        todo = []
        for e in v.iter_errors(data):
            if e.validator == 'required':
                name = re.match(r"'([^']+)'", e.message).group(1)
                todo.append((list(e.absolute_path), name, e.schema.get('properties', {}).get(name, {})))
            elif e.validator == 'minItems' and isinstance(e.instance, list) and not e.instance:
                todo.append((list(e.absolute_path), None, e.schema.get('items', {})))  # an array the display elided
            elif e.validator in ('anyOf', 'oneOf') and e.context and all(c.validator == 'required' for c in e.context):
                first = (e.schema.get('anyOf') or e.schema.get('oneOf'))[0]
                for name in first.get('required', []):
                    todo.append((list(e.absolute_path), name, e.schema.get('properties', {}).get(name, {})))
        if not todo:
            break
        for path, name, node in todo:
            target = at(data, path)
            if name is None and isinstance(target, list) and not target:
                target.append(minimal(node))
                injected.append('/'.join(map(str, path + [0])))
            elif isinstance(target, dict) and name not in target:
                target[name] = minimal(node)
                injected.append('/'.join(map(str, path + [name])))
    return data, injected


def content_errors(data, host):
    return [e for e in validator_for(host).iter_errors(data) if e.validator != 'uniqueItems']


def guess_host(data, section_obj):
    """For `migrate` only: the definition whose properties cover the twin's top-level keys."""
    if not isinstance(data, dict):
        return None
    keys = set(data)
    if {'version', 'runs'} & keys and keys <= set(SCHEMA['properties']):
        return LOG
    cands = [d for d, v in DEFS.items() if keys and keys <= set(v.get('properties', {}))]
    if not cands:
        return LOG if keys <= set(SCHEMA['properties']) else None
    prefer = [section_obj, 'run', 'result', 'tool', 'toolComponent', 'invocation', 'fix', 'artifactChange']
    return min(cands, key=lambda d: (prefer.index(d) if d in prefer else 50, d.startswith('externalProp')))


def twin_section(stem):
    """The prose file a twin belongs to and the object of that file, from the twin's name."""
    file = stem.split('_')[0]
    m = re.match(r'file-format-\d+-(\w+?)-object$', file)
    obj = DEFS_LC.get(m.group(1)) if m else ('externalProperties' if file.startswith('external-property') else None)
    if m and m.group(1) == 'sariflog':
        obj = LOG
    return file, obj


def examples():
    good, bad = markers()
    records = yaml.safe_load((RECORDS / 'examples.yaml').read_text(encoding='utf-8'))['examples']
    out = []
    for rec in records:
        path = TWINS / rec['twin']
        item = {'twin': rec['twin'], 'host': rec.get('host'), 'note': rec.get('note', ''), 'injected': [], 'errors': [], 'markers': []}
        raw = json.loads(path.read_text(encoding='utf-8'))
        data = strip_markers(copy.deepcopy(raw), good, bad, item['markers'])
        if item['host']:
            data, item['injected'] = with_context(data, item['host'])
            item['errors'] = [f'/{"/".join(map(str, e.absolute_path))}: {e.message[:150]}' for e in content_errors(data, item['host'])]
        out.append(item)
    return out


# ── views ──────────────────────────────────────────────────────────────────────

def md_escape(text):
    return text.replace('|', '\\|')


def _norm_twin(text):
    text = re.sub(r'"\.{0,3}(?:member|object|string|item)-in[a-z]+ct(?:-\d+)?"\s*:\s*"\.\.\."', '...', text)
    text = re.sub(r'\{\s*\.\.\.\s*\}', '...', text)
    text = re.sub(r'"\.{0,3}(?:member|object|string)-in[a-z]+ct(?:-\d+)?"', '...', text)
    return re.sub(r'[\s,]+', '', text).replace('…', '...')


def _norm_snippet(body):
    body = '\n'.join(re.sub(r'\s#\s.*$', '', line) for line in body.splitlines())
    return re.sub(r'[\s,]+', '', body).replace('…', '...')


def snippet_agreement(items, fences):
    """Per twin: does a JSON code block of its prose file say the same (layout, commas, margin notes, markers aside)?"""
    by_file = defaultdict(list)
    for f in fences:
        by_file[f['file'][:-3]].append(_norm_snippet(f['body']))
    for i in items:
        twin = _norm_twin((TWINS / i['twin']).read_text(encoding='utf-8'))
        i['same'] = twin in by_file.get(i['twin'].split('_')[0], [])


def view_examples(items):
    lines = [
        '# Examples: the twins against the schema',
        '',
        'Derived by `bin/vision.py derive` from `records/examples.yaml`, the twins and the schema; do not edit.',
        'Each twin is validated as its host definition after its markers are removed and the context the schema',
        'requires is injected (`injected` counts those members). What remains is what the example says about SARIF.',
        '',
        f'{sum(1 for i in items if i["host"] and not i["errors"] and not i["markers"])} of {len(items)} twins are valid this way.',
        f'{sum(1 for i in items if i["same"])} of {len(items)} twins say the same as a JSON code block of their prose file',
        '(layout, commas, margin notes and markers aside): those snippets can be derived from their twins without a',
        'change of content. The others differ: one of the two drifted, or a notation is not yet normalised.',
        '',
        '| Twin | Host | Injected | Result | Prose snippet |',
        '|---|---|---:|---|---|',
    ]
    for i in items:
        if not i['host']:
            result = f'no host: {i["note"]}' if i['note'] else 'no host'
        elif i['markers']:
            result = 'malformed marker: ' + ', '.join(f'`{m}`' for m in i['markers'])
        elif i['errors']:
            result = f'{len(i["errors"])} error(s), see findings'
        else:
            result = 'valid'
        lines.append(f'| `{i["twin"]}` | {i["host"] or "-"} | {len(i["injected"])} | {result} | {"same" if i["same"] else "differs"} |')
    return '\n'.join(lines) + '\n'


def role_records():
    return yaml.safe_load((RECORDS / 'roles.yaml').read_text(encoding='utf-8'))['roles']


def view_roles(statements):
    roles = role_records()
    rx = {r['id']: re.compile(r'\b(?:' + '|'.join(r['terms']) + r')\b', re.I) for r in roles}
    by_role = defaultdict(list)
    for s in statements:
        named = [r['id'] for r in roles if rx[r['id']].search(s['text'])]
        for r in named or ['no-role']:
            by_role[r].append(s)
    views = {}
    for r in roles + [{'id': 'no-role', 'name': 'no role named', 'shared': '-'}]:
        items = by_role.get(r['id'], [])
        kw = Counter(k for s in items for k in set(BOLD_KW.findall(s['text'])))
        lines = [
            f'# Statements naming: {r["name"]}',
            '',
            'Derived by `bin/vision.py derive` from the prose and `records/roles.yaml`; do not edit.',
            f'{len(items)} statements; ' + ', '.join(f'{k} {kw[k]}' for k in ('SHALL', 'SHALL NOT', 'SHOULD', 'SHOULD NOT', 'MAY') if kw[k]) + '.',
            '',
        ]
        current = None
        for s in items:
            where = f'{s["file"]}: {s["heading"]}'
            if where != current:
                lines += ['', f'## {s["heading"]}', '', f'`{s["file"]}`', '']
                current = where
            lines.append(f'- {s["text"]} (line {s["line"]})')
        views[f'roles/{r["id"]}.md'] = '\n'.join(lines) + '\n'
    return views


def findings(sections, headings, statements, fences, items):
    out = ['# Findings', '', 'What `bin/vision.py derive` noticed in the prose, the twins and the schema; do not edit.',
           'Each finding names the place to change; decisions for the TC are marked **TC**.', '']

    # A3 against A1: properties and their headings
    out += ['## Prose and schema', '']
    for obj, props in sorted(sections.items()):
        sch = schema_of(obj)
        if sch is None:
            out.append(f'- `{obj}`: an object section without a schema definition')
            continue
        schema_props = set(sch.get('properties', {}))
        prose_props = {p for p in props if p}
        files = {h['file'] for h in headings if h['obj'] == obj}
        text = '\n'.join((SRC / f).read_text(encoding='utf-8') for f in files)
        for p in sorted(prose_props - schema_props):
            out.append(f'- **TC** `{obj}.{p}`: a property section in the prose, no such property in the schema')
        for p in sorted(schema_props - prose_props - {'properties'}):
            if f'`{p}`' in text or f'`{p}`' in TABLE_ROWS:
                continue  # described together with others: in the same file, or in a table (the externalized properties)
            out.append(f'- `{obj}.{p}`: in the schema, not described in the prose')
    for h in headings:
        if h['broken']:
            out.append(f'- {h["file"]}:{h["line"]}: heading "{h["text"]}" does not give its property as `` `name` Property ``')
    for obj, props in sorted(sections.items()):
        for prop, lines in props.items():
            ps = (schema_of(obj) or {}).get('properties', {}).get(prop) if prop else None
            if not ps:
                continue
            text = '\n'.join(lines)
            enum = ps.get('enum') or ps.get('items', {}).get('enum')
            if enum:
                listed = set(re.findall(r'^\s*(?:[-*]|\d+\.)\s+`"?([\w.-]+)"?`', text, re.M))
                for v in sorted(listed - set(enum)):
                    out.append(f'- **TC** `{obj}.{prop}`: the prose lists the value `"{v}"`, the schema enum does not have it')
                for v in enum:
                    if v not in listed and f'"{v}"' not in text:
                        out.append(f'- `{obj}.{prop}`: the schema value `"{v}"` is not described in the prose')
            for s in sentences(text):
                m = DEFAULT.search(s)
                if not m or (m.group(1) and m.group(1) != prop) or re.search(r'thisObject|theResult|theRun', m.group(2)):
                    continue  # a default that depends on other values is a constraint, not a schema default
                prose_default = _json_or_text(m.group(2).rstrip('.'))
                if 'default' not in ps and prose_default is None:
                    continue  # "default to null": absent means not known, which the schema cannot say for an array
                if 'default' not in ps:
                    out.append(f'- `{obj}.{prop}`: the prose gives the default `{m.group(2)}`, the schema gives none')
                elif prose_default != ps['default']:
                    out.append(f'- **TC** `{obj}.{prop}`: default `{m.group(2)}` in the prose, `{json.dumps(ps["default"])}` in the schema')
    out.append('')

    # A4 against A1: the examples
    out += ['## Examples', '']
    json_fences = [f for f in fences if f['lang'] == 'json']
    parse_ok = sum(1 for f in json_fences if _parses(f['body']))
    out.append(f'- {len(json_fences) - parse_ok} of {len(json_fences)} JSON code blocks in the prose are not JSON '
               '(margin comments, elisions): only their twins can be validated')
    twin_files = Counter(i['twin'].split('_')[0] for i in items)
    for file in sorted({f['file'][:-3] for f in json_fences} - set(twin_files)):
        out.append(f'- {file}.md: JSON code blocks without a twin')
    for i in items:
        if not i['host']:
            out.append(f'- `{i["twin"]}`: no host definition{": " + i["note"] if i["note"] else ""}')
        for m in i['markers']:
            out.append(f'- `{i["twin"]}`: malformed marker `{m}` (records/markers.yaml)')
        for e in i['errors']:
            out.append(f'- **TC** `{i["twin"]}` as {i["host"]}: {md_escape(e)}')
    for f in sorted((ROOT / 'example').glob('*.json')):
        errs = list(jsonschema.Draft202012Validator(SCHEMA).iter_errors(json.loads(f.read_text(encoding='utf-8'))))
        for e in errs[:3]:
            out.append(f'- example/{f.name}: /{"/".join(map(str, e.absolute_path))}: {e.message[:120]}')
    out.append('')

    # A3: statements
    out += ['## Statements', '']
    sets = [s for s in statements if KEYWORD_SET.search(s['text'])]
    out.append(f'- {len(sets)} statements announce a set of keywords ("either **SHALL** or **MAY**"); the rule is the sum of '
               'the sentences that follow (constraint record candidates):')
    for s in sets:
        out.append(f'  - {s["file"]}:{s["line"]} ({s["heading"]})')
    for name in bound_files():
        for i, line in enumerate((SRC / name).read_text(encoding='utf-8').splitlines(), 1):
            if not line.lstrip().startswith(('>', '|', '#')) and re.search(r'(?<![`*\w])shall(?![`*\w])', line):
                out.append(f'- {name}:{i}: normative "shall" in lower case')
    return '\n'.join(out) + '\n'


def _json_or_text(text):
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        return text


def _parses(body):
    try:
        json.loads(body)
        return True
    except json.JSONDecodeError:
        return False


def derive_all():
    sections, headings, statements, fences = read_prose()
    items = examples()
    snippet_agreement(items, fences)
    views = {'examples.md': view_examples(items), 'findings.md': findings(sections, headings, statements, fences, items)}
    views |= view_roles(statements)
    return views


# ── commands ───────────────────────────────────────────────────────────────────

def migrate():
    target = RECORDS / 'examples.yaml'
    if target.exists():
        sys.exit(f'{target.relative_to(ROOT)} exists: migrate seeds it once; edit the record instead')
    good, bad = markers()
    lines = [
        '# One record per example twin (prose/edit/src/json-examples/): the schema definition that hosts it.',
        '# Seeded by `bin/vision.py migrate` from the twin\'s top-level keys and its section; reviewed by hand.',
        '# `host` is a $defs name or sarifLog; derive validates the twin as that definition after removing the',
        '# markers (records/markers.yaml) and injecting the required context. `note` explains a missing host.',
        '',
        'examples:',
    ]
    for path in sorted(TWINS.glob('*.json')):
        data = strip_markers(json.loads(path.read_text(encoding='utf-8')), good, bad, [])
        _, obj = twin_section(path.stem)
        host = guess_host(data, obj)
        lines.append(f'- twin: {path.name}')
        lines.append(f'  host: {host}' if host else '  host: null')
    target.write_text('\n'.join(lines) + '\n', encoding='utf-8')
    print(f'wrote {target.relative_to(ROOT)}: review the hosts, then run derive')


def check_records():
    problems = []
    names = {r['twin'] for r in yaml.safe_load((RECORDS / 'examples.yaml').read_text(encoding='utf-8'))['examples']}
    on_disk = {p.name for p in TWINS.glob('*.json')}
    problems += [f'records/examples.yaml: no record for twin {n}' for n in sorted(on_disk - names)]
    problems += [f'records/examples.yaml: record for a missing twin {n}' for n in sorted(names - on_disk)]
    for rec in yaml.safe_load((RECORDS / 'examples.yaml').read_text(encoding='utf-8'))['examples']:
        if rec.get('host') and rec['host'] != LOG and rec['host'] not in DEFS:
            problems.append(f'records/examples.yaml: {rec["twin"]}: host {rec["host"]} is no schema definition')
    return problems


def main():
    command = sys.argv[1] if len(sys.argv) > 1 else 'check'
    if command == 'migrate':
        migrate()
        return
    problems = check_records()
    if problems:
        sys.exit('\n'.join(problems))
    views = derive_all()
    if command == 'derive':
        for rel, text in views.items():
            path = VIEWS / rel
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(text, encoding='utf-8')
        print(f'derived {len(views)} views into views/')
    elif command == 'check':
        stale = [rel for rel, text in views.items() if not (VIEWS / rel).is_file() or (VIEWS / rel).read_text(encoding='utf-8') != text]
        extra = sorted(str(p.relative_to(VIEWS)) for p in VIEWS.rglob('*.md') if str(p.relative_to(VIEWS)) not in views)
        if stale or extra:
            sys.exit('views differ from the sources (run make derive):\n' + '\n'.join(f'  {r}' for r in stale + extra))
        print(f'{len(views)} views match the sources')
    else:
        sys.exit(__doc__)


main()
