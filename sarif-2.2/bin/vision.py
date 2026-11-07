"""SARIF vision: records and the schema are the sources, the views are derived and checked.

Usage (from sarif-2.2/):
  python -I bin/vision.py migrate   seed records/examples.yaml from the twins (once; review the hosts afterwards)
  python -I bin/vision.py migrate-notes      turn margin notes into keys (see, object, ref) where the text round-trips
  python -I bin/vision.py migrate-constraints  seed records/constraints.yaml from the keyword-set statements (once)
  python -I bin/vision.py migrate-defaults     seed records/defaults.yaml from the default sentences (once)
  python -I bin/vision.py migrate-presence     append records for sections with conditional presence claims (review after)
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
KEYWORD_SET = re.compile(r'either \*\*[A-Z ,]+\*\*(?:, \*\*[A-Z ]+\*\*)*,? or \*\*[A-Z ]+\*\*')  # [A-Z ,]: "**MAY, SHALL NOT**" too
JOINED_BOLD = re.compile(r'\*\*(?:' + KW + r'), (?:' + KW + r')\*\*')
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
                    b = None if names else BROKEN_KEY.match(text)
                    broken = text if not names and (b or '`' in text) else None  # names a property, not as `` `name` Property ``
                    if b:
                        names = [b.group(1)]
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
    """The marker grammar of the twins: `twins.markers` in prose/edit/etc/nide.yaml (nide checks the twins with it)."""
    rec = yaml.safe_load((PROSE / 'etc' / 'nide.yaml').read_text(encoding='utf-8'))['twins']['markers']
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


def elided_objects(node, good, path=''):
    """Paths (as after strip_markers) of the objects whose display elides members: what they lack is unknown."""
    out = []
    if isinstance(node, dict):
        if any(good.match(k) for k in node):
            out.append(path)
        for k, v in node.items():
            if not good.match(k):
                out += elided_objects(v, good, f'{path}/{k}' if path else k)
    elif isinstance(node, list):
        kept = [v for v in node if not (isinstance(v, str) and good.match(v)) and not (isinstance(v, dict) and len(v) == 1 and good.match(next(iter(v))))]
        for i, v in enumerate(kept):
            out += elided_objects(v, good, f'{path}/{i}' if path else str(i))
    return out


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
        item = {'twin': rec['twin'], 'host': rec.get('host'), 'note': rec.get('note', ''), 'injected': [], 'errors': [], 'markers': [],
                'derived': bool(rec.get('display')), 'snippet': rec.get('snippet', '')}
        raw = json.loads(path.read_text(encoding='utf-8'))
        data = strip_markers(copy.deepcopy(raw), good, bad, item['markers'])
        if item['host']:
            data, item['injected'] = with_context(data, item['host'])
            item['errors'] = [f'/{"/".join(map(str, e.absolute_path))}: {e.message[:150]}' for e in content_errors(data, item['host'])]
            item['data'], item['elided'] = data, elided_objects(raw, good)
        out.append(item)
    return out


# ── views ──────────────────────────────────────────────────────────────────────

def md_escape(text):
    return text.replace('|', '\\|')


def view_examples(items):
    lines = [
        '# Examples: the twins against the schema',
        '',
        'Derived by `bin/vision.py derive` from `records/examples.yaml`, the twins and the schema; do not edit.',
        'Each twin is validated as its host definition after its markers are removed and the context the schema',
        'requires is injected (`injected` counts those members). What remains is what the example says about SARIF.',
        '',
        f'{sum(1 for i in items if i["host"] and not i["errors"] and not i["markers"])} of {len(items)} twins are valid this way.',
        f'{sum(1 for i in items if i["derived"])} of {len(items)} prose snippets are derived from their twins (records/examples.yaml, `display`),',
        'byte for byte: `make check` fails when a snippet in the prose differs from its twin. The others are still',
        'hand-written, for the reason given: where the twin and the snippet say different things, one of them drifted.',
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
        lines.append(f'| `{i["twin"]}` | {i["host"] or "-"} | {len(i["injected"])} | {result} | {"derived" if i["derived"] else "hand-written: " + md_escape(i["snippet"])} |')
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


def findings(sections, headings, statements, fences, items, constraints=()):
    out = ['# Findings', '', 'What `bin/vision.py derive` noticed in the prose, the twins and the schema; do not edit.',
           'Each finding names the place to change; decisions for the TC are marked **TC**.', '']

    # A3 against A1: properties and their headings (nide quality, SARIF-SCHEMA-HEADINGS, refuses every other difference)
    out += ['## Prose and schema', '']
    for d in drift_records():
        what = PROSE_ONLY if d['kind'] == 'prose-only' else SCHEMA_ONLY
        out.append(f'- **TC** `{d["property"]}`: {what} ({d["id"]}, `known` of SARIF-SCHEMA-HEADINGS in prose/edit/etc/rules/spec.rules.yaml)')
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
    out += default_findings()  # records/defaults.yaml against the schema
    out += at_least_one_findings(statements)
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
            out.append(f'- `{i["twin"]}`: malformed marker `{m}` (twins.markers in prose/edit/etc/nide.yaml)')
        for e in i['errors']:
            out.append(f'- **TC** `{i["twin"]}` as {i["host"]}: {md_escape(e)}')
    for i in items:
        if not i['derived']:
            out.append(f'- `{i["twin"]}`: snippet still hand-written: {md_escape(i["snippet"])}')
    for f in sorted((ROOT / 'example').glob('*.json')):
        errs = list(jsonschema.Draft202012Validator(SCHEMA).iter_errors(json.loads(f.read_text(encoding='utf-8'))))
        for e in errs[:3]:
            out.append(f'- example/{f.name}: /{"/".join(map(str, e.absolute_path))}: {e.message[:120]}')
    out.append('')

    # A4 against A1 and the prose: what the margin notes claim
    out += ['## Margin notes', '']
    out += note_findings() or ['- none']
    out.append('')

    # A3: statements
    out += ['## Statements', '']
    sets = [s for s in statements if KEYWORD_SET.search(s['text'])]
    out.append(f'- {len(sets)} statements announce a set of keywords ("either **SHALL** or **MAY**"); the rule is the sum of '
               'the sentences that follow (records/constraints.yaml, views/constraints.md):')
    for s in sets:
        out.append(f'  - {s["file"]}:{s["line"]} ({s["heading"]})')
    out += list(constraints)
    out += [f'- {s["file"]}:{s["line"]}: one bold span holds two keywords ({JOINED_BOLD.search(s["text"]).group(0)}): bold each keyword'
            for s in statements if JOINED_BOLD.search(s['text'])]
    for name in bound_files():
        for i, line in enumerate((SRC / name).read_text(encoding='utf-8').splitlines(), 1):
            if not line.lstrip().startswith(('>', '|', '#')) and re.search(r'(?<![`*\w])shall(?![`*\w])', line):
                out.append(f'- {name}:{i}: normative "shall" in lower case')
    return '\n'.join(out) + '\n'


PROSE_ONLY = 'a property section in the prose, no such property in the schema'
SCHEMA_ONLY = 'in the schema, not described in the prose'


RULES = PROSE / 'etc' / 'rules' / 'spec.rules.yaml'


def drift_records():
    """The known differences between property sections and schema properties: the `known` of SARIF-SCHEMA-HEADINGS."""
    rules = yaml.safe_load(RULES.read_text(encoding='utf-8'))['rules']
    check = next(r['check'] for r in rules if r['id'] == 'SARIF-SCHEMA-HEADINGS')
    return [{'id': k['reason'].split(':', 1)[0], 'property': k['key'], 'kind': k['kind']} for k in check['known']]


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


# ── margin notes as keys ──────────────────────────────────────────────────────

SEE_NOTE = re.compile(r'^# See \(#([\w.-]+)\)\.$')
OBJECT_NOTE = re.compile(r'^# (An?) (\w+) object(?: \(\(#([\w.-]+)\)\))?(\.?)$')
REFERENCE = re.compile(r'\(#([\w.-]+)\)')


def note_text(n):
    """A margin note as the prose shows it: from its keys (`see`, `object`/`ref`) or its free `note` text."""
    if 'see' in n:
        return f'# See (#{n["see"]}).'
    if 'object' in n:
        name = n['object']
        text = f'# {"An" if name[0] in "aeiouAEIOU" else "A"} {name} object'
        text += f' ((#{n["ref"]}))' if n.get('ref') else ''
        return text + ('' if n.get('dot') is False else '.')
    return n['note']


def note_keys(note):
    """The keys of a note's text, when its text can be regenerated from them exactly; else None."""
    if m := SEE_NOTE.match(note):
        keys = {'see': m.group(1)}
    elif m := OBJECT_NOTE.match(note):
        keys = {'object': m.group(2)} | ({'ref': m.group(3)} if m.group(3) else {}) | ({} if m.group(4) else {'dot': False})
    else:
        return None
    return keys if note_text(keys) == note else None


def label_index():
    """Every section label of the prose: its heading text and the object section it belongs to."""
    etc = PROSE / 'etc'
    labels = json.loads((etc / 'section-display-to-label.json').read_text(encoding='utf-8'))
    texts = json.loads((etc / 'section-display-to-text.json').read_text(encoding='utf-8'))
    out = {}
    for display, label in labels.items():
        text = texts.get(display, '').replace('`', '')
        owner, parts = None, display.split('.')
        for n in range(len(parts), 0, -1):
            m = re.match(r'^(\w+) Object$', texts.get('.'.join(parts[:n]), '').replace('`', ''))
            if m:
                owner = m.group(1)
                break
        out[label] = {'display': display, 'text': text, 'object': owner}
    return out


def schema_at(host, pointer):
    """The schema definition name of the value at `pointer` in a twin hosted by `host` (None when unknown)."""
    node, name = (SCHEMA, LOG) if host == LOG else (DEFS[host], host)
    for token in [t for t in pointer.split('/')[1:]]:
        token = token.replace('~1', '/').replace('~0', '~')
        while '$ref' in node:
            name = node['$ref'].rsplit('/', 1)[-1]
            node = DEFS[name]
        if node.get('type') == 'array' or 'items' in node:
            node, name = node.get('items', {}), None
        elif token in node.get('properties', {}):
            node, name = node['properties'][token], None
        elif isinstance(node.get('additionalProperties'), dict):
            node, name = node['additionalProperties'], None
        else:
            return None
    while '$ref' in node:
        name = node['$ref'].rsplit('/', 1)[-1]
        node = DEFS[name]
    if name is None and node.get('type') == 'object' and node is SCHEMA:
        name = LOG
    return name


def note_findings():
    """What the margin notes claim, checked against the section labels and the schema."""
    labels = label_index()
    object_label = {v['text'][:-len(' Object')]: k for k, v in labels.items() if v['text'].endswith(' Object')}
    out, unreferenced = [], 0
    for rec in snippet_records():
        twin, host = rec['twin'], rec.get('host')
        notes = list(rec['display'].get('notes', []))
        notes += [{'at': None, 'note': line.split('#', 1)[1].join(['#', ''])} for lines in rec['display'].get('before', {}).values()
                  for line in lines if '#' in line]
        for n in notes:
            where = f'`{twin}` at ' + ('a line of its own' if n['at'] is None else f'`{n["at"] or "/"}`')
            text = note_text(n)
            for label in REFERENCE.findall(text):
                if label not in labels:
                    out.append(f'- {where}: the note refers to `#{label}`, which no section has (a broken key)')
            if re.search(r'\(#[\w.-]+\)\.\d+', text):
                out.append(f'- {where}: stray text after the reference: "{text}" (a remnant of a section number)')
            if 'object' in n and host and n['at'] is not None:
                actual = schema_at(host, n['at'])
                if actual and actual.lower() != n['object'].lower():
                    out.append(f'- {where}: the note says "{n["object"]} object", the schema says `{actual}`')
                if n.get('ref') and object_label.get(n['object']) not in (None, n['ref']):
                    out.append(f'- {where}: "{n["object"]} object" refers to `#{n["ref"]}`, its section is `#{object_label[n["object"]]}`')
                if not n.get('ref'):
                    unreferenced += 1
            if 'see' in n and host and n['at']:
                key = n['at'].rsplit('/', 1)[-1]
                target = labels.get(n['see'])
                m = re.match(r'^(\w+) Property$', target['text']) if target else None
                if m and key != m.group(1) and not key.isdigit():
                    out.append(f'- {where}: "See (#{n["see"]})" names the property `{m.group(1)}`, the line holds `{key}`')
    if unreferenced:
        out.append(f'- {unreferenced} object notes name their object without a reference ("A run object."); a key '
                   '`ref` would link them like the others')
    return out


def broken_keys():
    """Margin-note references to sections that do not exist: check refuses them."""
    labels = label_index()
    out = []
    for rec in snippet_records():
        texts = [note_text(n) for n in rec['display'].get('notes', [])]
        texts += [line for lines in rec['display'].get('before', {}).values() for line in lines]
        out += [f'{rec["twin"]}: margin note refers to #{label}, which no section has'
                for t in texts for label in REFERENCE.findall(t) if label not in labels]
    return out


def migrate_notes():
    """Turn margin notes into keys where their text can be regenerated from the keys exactly."""
    path = RECORDS / 'examples.yaml'
    data = yaml.safe_load(path.read_text(encoding='utf-8'))
    counts = Counter()
    for rec in data['examples']:
        for n in rec.get('display', {}).get('notes', []):
            if 'note' in n and (keys := note_keys(n['note'])):
                del n['note']
                n.update(keys)
                counts['keyed'] += 1
            elif 'note' in n:
                counts['text'] += 1
    header = [line for line in path.read_text(encoding='utf-8').splitlines() if line.startswith('#')]
    if not any('see:' in line for line in header):
        header.append('# Notes as keys (`bin/vision.py migrate-notes`): `see: <label>` renders "# See (#<label>).", `object: <name>`')
        header.append('# with optional `ref: <label>` renders "# A <name> object ((#<label>))."; `note` keeps free text.')
    path.write_text('\n'.join(header) + '\n\n' + yaml.safe_dump(data, sort_keys=False, allow_unicode=True, width=150), encoding='utf-8')
    print(', '.join(f'{v} {k}' for k, v in counts.items()))


def snippet_records():
    return [r for r in yaml.safe_load((RECORDS / 'examples.yaml').read_text(encoding='utf-8'))['examples'] if r.get('display')]


def derive_prose():
    """The prose files with the constraint sentences of each record written verbatim.

    The snippets of the twins are nide's: `nide derive` writes them, `nide quality` (SARIF-TWINS) checks them.
    """
    files = {}
    _, _, statements, _ = read_prose()
    for name in dict.fromkeys(r['file'] for r in constraint_records()):
        text = files.get(name) or (SRC / name).read_text(encoding='utf-8')
        files[name] = derive_sentences(name, text, statements)
    return files


def derive_all():
    sections, headings, statements, fences = read_prose()
    items = examples()
    records = constraint_records()
    rules = schema_rules(records)
    fixture_files, _ = rule_fixtures(rules)  # marks the rules the schema says already
    in_schema = [x for x in rules if x.get('in_schema')]
    rules = [x for x in rules if not x.get('in_schema')]
    violations = rule_violations(items, rules)
    bound = sorted(set(rule_violations(items, schema_rules(records, bound=True))) - set(violations))
    views = {**{f'fixtures/{name}': json.dumps(inst, indent=2) + '\n' for name, inst in fixture_files.items()},
             'examples.md': view_examples(items), 'findings.md': findings(sections, headings, statements, fences, items, constraint_findings(records, violations, bound)),
             'constraints.md': view_constraints(records, rules, violations, in_schema),
             'constraints.schema.json': json.dumps({'$comment': 'Derived by bin/vision.py from records/constraints.yaml: presence rules the schema can say. '
                                                    'A proposal for the TC; do not edit.',
                                                    '$defs': {d: {'allOf': [{'if': x['if'], 'then': x['then']} for x in rules if x['def'] == d]}
                                                              for d in dict.fromkeys(x['def'] for x in rules)}}, indent=2) + '\n'}
    views |= view_roles(statements)
    return views


# ── commands ───────────────────────────────────────────────────────────────────

# ── constraints: presence rules with conditions ───────────────────────────────

ANNOUNCED = re.compile(r'(?<=[*, ])(' + KW + r')(?=\*\*|,)')  # each keyword of the bold spans, joined ones included


def presences(sentence, prop):
    """The presence keywords a sentence gives *prop*, in order: `p` SHALL be present, it MAY be absent, ..."""
    subject = rf'(?:`{re.escape(prop)}`|\b{re.escape(prop)}\b|\bit\b|\bthen again `{re.escape(prop)}`)'
    return re.findall(subject + r'[^.;`]*?\*\*(' + KW + r')\*\* be (?:present|absent)', sentence)  # no other name in between


ABSENT = {'SHALL': 'SHALL NOT', 'SHOULD': 'SHOULD NOT', 'MUST': 'MUST NOT', 'MAY': 'MAY'}
CLAIM = re.compile(r'\*\*(' + KW + r')\*\* contain a property named `(\$?[\w.]+)`'
                   r'|`(\$?[\w.]+)`(?: property)?(?: \((?:[^()]|\([^()]*\))*\))? (?:\*\*[A-Z ]+\*\* be present and )?\*\*(' + KW + r')\*\* be (present|absent)'
                   r'|\b(it|then again) \*\*(' + KW + r')\*\* be (present|absent)')
CONDITIONAL = re.compile(r'^(?:If|Unless|When|Otherwise)\b|, (?:if|unless|when) ')


def claims(sentence, prop):
    """The presence claims of a sentence, in order: (property, level), "**SHALL** be absent" read as **SHALL NOT**."""
    out = []
    for m in CLAIM.finditer(sentence):
        if m.group(1):
            out.append((m.group(2), m.group(1)))
        elif m.group(3):
            out.append((m.group(3), m.group(4) if m.group(5) == 'present' else ABSENT.get(m.group(4), m.group(4))))
        else:
            out.append((prop, m.group(7) if m.group(8) == 'present' else ABSENT.get(m.group(7), m.group(7))))
    return out


DEFINITION = re.compile(r'^An? `(\w+)` object \*\*(' + KW + r')\*\* contain a property named `(\$?\w+)`')
AT_LEAST_ONE = re.compile(r'^At least one of (.*?) \*\*SHALL\*\* be present')


def definition_keys(statements):
    """Refusals: an unconditional "An `x` object **SHALL** contain a property named `p`" whose level the schema's
    `required` contradicts (SHALL: required; any other keyword: optional), unless SARIF-SCHEMA-HEADINGS knows `x.p`."""
    drift = {d['property'] for d in drift_records()}
    out = []
    for s in statements:
        m = DEFINITION.match(s['text'])
        if not m or CONDITIONAL.search(s['text']):
            continue
        obj, level, prop = m.groups()
        sch = schema_of(obj)
        if sch is None or f'{obj}.{prop}' in drift or prop not in sch.get('properties', {}):
            continue  # an object or property the schema lacks: nide quality (SARIF-SCHEMA-HEADINGS) speaks for it
        if (level == 'SHALL') != (prop in sch.get('required', [])):
            out.append(f'{s["file"]}:{s["line"]}: `{obj}.{prop}` is **{level}** in the prose, '
                       f'{"required" if prop in sch.get("required", []) else "optional"} in the schema')
    return out


def at_least_one_findings(statements):
    """An unconditional "At least one of `a` or `b` **SHALL** be present" against the `anyOf` of the object's definition."""
    out = []
    for s in statements:
        m = AT_LEAST_ONE.match(s['text'])
        if not m or not s['obj']:
            continue
        names = set(re.findall(r'`(\$?\w+)`', re.sub(r'\(\[sec\][^)]*\)', '', m.group(1))))
        alts = [set(a.get('required', [])) for a in (schema_of(s['obj']) or {}).get('anyOf', [])]
        if not (all(len(a) == 1 for a in alts) and set().union(*alts) == names):
            out.append(f'- **TC** `{s["obj"]}`: the prose requires at least one of {", ".join(f"`{n}`" for n in sorted(names))} '
                       f'({s["file"]}:{s["line"]}); the schema has {"no such anyOf" if not alts else "a different anyOf"}')
    return out


def unannounced_sections(statements):
    """Property sections without an announcement that make a conditional presence claim: (file, obj, prop, statements)."""
    announced = {(a['file'], a['obj'], a['prop']) for a, _ in constraint_sections(statements)}
    groups = defaultdict(list)
    for s in statements:
        if s['obj'] and s['prop'] and (s['file'], s['obj'], s['prop']) not in announced:
            groups[(s['file'], s['obj'], s['prop'])].append(s)
    return [(*k, v) for k, v in groups.items() if any(CONDITIONAL.search(s['text']) and claims(s['text'], k[2]) for s in v)]


def constraint_sections(statements):
    """Each keyword-set statement with the other statements of its property section, in prose order."""
    out = []
    for a in statements:
        if KEYWORD_SET.search(a['text']):
            rest = [s for s in statements if s['file'] == a['file'] and s['heading'] == a['heading'] and s is not a]
            out.append((a, rest))
    return out


def sentence_sequence(r):
    """The statements a record gives its section, in prose order (a sentence shared by two branches once)."""
    out = list(r.get('also', []))
    for b in r['branches']:
        if not out or out[-1] != b['sentence']:
            out.append(b['sentence'])
        out += b.get('also', [])
    return out


def _loose(sentence):
    return re.compile(r'\s+'.join(map(re.escape, sentence.split())))


def derive_sentences(name, text, statements):
    """*text* of prose file *name* with the statements of each constraint section replaced by its record's, in order."""
    sections = [(a['file'], a['obj'], a['prop'], rest, a['text'].split(' whose ')[0]) for a, rest in constraint_sections(statements)]
    sections += [(f, o, p, rest, None) for f, o, p, rest in unannounced_sections(statements)]
    records = {r['property']: r for r in constraint_records()}
    for file, obj, prop, rest, anchor in sections:
        r = records.get(f'{obj}.{prop}')
        if file != name or r is None or len(rest) != len(sentence_sequence(r)):
            continue  # constraint_keys refuses a missing record or a different count
        start = _loose(anchor).search(text).start() if anchor else _loose(rest[0]['text']).search(text).start()
        for old, new in zip((s['text'] for s in rest), sentence_sequence(r)):
            m = _loose(old).search(text, start)  # a statement may span lines: whitespace collapsed in the record
            if old != new:
                text = text[:m.start()] + new + text[m.end():]
            start = m.start() + (len(new) if old != new else len(m.group(0)))
    return text


DEFAULT_ANY = re.compile(r'\*\*SHALL\*\* default to ')


def default_statements(statements):
    """Each statement that gives a default, with its property: `object.property` of its section."""
    return [(f'{s["obj"]}.{s["prop"]}', s) for s in statements if s['obj'] and s['prop'] and DEFAULT_ANY.search(s['text'])]


def default_records():
    path = RECORDS / 'defaults.yaml'
    return yaml.safe_load(path.read_text(encoding='utf-8'))['defaults'] if path.is_file() else []


def default_keys():
    """Refusals: a default sentence of the prose without a record, a record whose sentence the prose lacks."""
    _, _, statements, _ = read_prose()
    found = {(k, s['text']) for k, s in default_statements(statements)}
    recorded = {(r['property'], r['sentence']) for r in default_records()}
    return ([f'`{k}`: a default in the prose without a record in records/defaults.yaml: {t[:80]}' for k, t in sorted(found - recorded)]
            + [f'records/defaults.yaml: `{k}`: its sentence is not in the property section: {t[:80]}' for k, t in sorted(recorded - found)])


def default_findings():
    out = []
    for r in default_records():
        obj, prop = r['property'].split('.', 1)
        ps = (schema_of(obj) or {}).get('properties', {}).get(prop, {})
        if 'value' not in r:
            if 'default' in ps:
                out.append(f'- `{r["property"]}`: the prose default depends on other values, the schema gives the constant `{json.dumps(ps["default"])}`')
        elif 'default' not in ps and r['value'] is not None:  # "default to null": absent means unknown, which a schema cannot say
            out.append(f'- `{r["property"]}`: the prose gives the default `{json.dumps(r["value"])}`, the schema gives none')
        elif 'default' in ps and r['value'] != ps['default']:
            out.append(f'- **TC** `{r["property"]}`: default `{json.dumps(r["value"])}` in the prose, `{json.dumps(ps["default"])}` in the schema')
    return out


def migrate_defaults():
    target = RECORDS / 'defaults.yaml'
    if target.exists():
        sys.exit(f'{target.relative_to(ROOT)} exists: migrate-defaults seeds it once')
    _, _, statements, _ = read_prose()
    records = []
    for key, s in default_statements(statements):
        prop = key.split('.', 1)[1]
        m = re.match(rf'^If (?:`{re.escape(prop)}`|this property) is absent, it \*\*SHALL\*\* default to (?:the array )?(?:`([^`]+)`|(-?\d+)\b)', s['text'])
        rec = {'property': key}
        try:
            rec['value'] = json.loads(m.group(1) or m.group(2))
        except (AttributeError, TypeError, ValueError):
            rec['depends'] = 'a condition or other values: see the sentence'
        rec['sentence'] = s['text']
        records.append(rec)
    head = ('# Defaults: what a property means when it is absent, as the prose says it (A3), against the schema\'s `default` (A1).\n'
            '#   property  object.property of the section that gives the default\n'
            '#   value     a constant default (JSON); compared with the schema\'s `default` in views/findings.md\n'
            '#   depends   instead of value: the default follows other values (in words)\n'
            '#   sentence  the prose sentence, verbatim; check refuses a default sentence without a record, and back\n\n')
    target.write_text(head + yaml.safe_dump({'defaults': records}, sort_keys=False, allow_unicode=True, width=120), encoding='utf-8')
    print(f'seeded {len(records)} default records')


def constraint_records():
    path = RECORDS / 'constraints.yaml'
    return yaml.safe_load(path.read_text(encoding='utf-8'))['constraints'] if path.is_file() else []


SCOPES = ('object', 'log', 'world', 'rest')
SCHEMA_LEVELS = ('SHALL', 'SHALL NOT')


def schema_rules(records, bound=False):
    """The branches the schema can say, as if/then: SHALL or SHALL NOT at object scope, after object-scope branches only.

    With *bound*, also those that bind a role: what the log files would break if the TC made them rules of the log file.
    """
    out = []
    for r in records:
        obj, prop = r['property'].split('.', 1)
        earlier = []
        for b in r['branches']:
            target = b.get('property', prop)
            if b['scope'] == 'object' and b['presence'] in SCHEMA_LEVELS and (bound or 'binds' not in b) and (not b['otherwise'] or all(e['scope'] == 'object' for e in earlier)):
                cond = {'allOf': [b['if'], *({'not': e['if']} for e in earlier)]} if b['otherwise'] and earlier else b['if']
                then = {'required': [target]} if b['presence'] == 'SHALL' else {'not': {'required': [target]}}
                out.append({'def': obj, 'property': f'{obj}.{target}', 'presence': b['presence'], 'when': b['when'], 'if': cond, 'then': then})
            earlier.append(b)
    return out


def schema_reason(r, i):
    """Why branch *i* of record *r* gives no if/then, or None when it does."""
    b = r['branches'][i]
    if b['presence'] not in SCHEMA_LEVELS:
        return f'{b["presence"]} does not invalidate'
    if 'binds' in b:
        return f'binds {b["binds"]}s, not the log file'
    if b['scope'] != 'object':
        return {'log': 'needs other parts of the log', 'world': 'only the producer knows', 'rest': 'follows from the other branches'}[b['scope']]
    if b['otherwise'] and any(e['scope'] != 'object' for e in r['branches'][:i]):
        return 'an earlier branch outside the object takes precedence'
    return None


def extended_schema(rules):
    schema = copy.deepcopy(SCHEMA)
    for rule in rules:
        schema['$defs'][rule['def']].setdefault('allOf', []).append({'if': rule['if'], 'then': rule['then']})
    return schema


def _meets(instance, cond):
    return jsonschema.Draft202012Validator({'$defs': DEFS, **cond}).is_valid(instance)


def satisfy(base, cond, node):
    """*base* changed so that it meets *cond*: members a negated `required` names removed, the required ones added
    (trying the enum values of each until the condition holds)."""
    out = dict(base)
    for name in cond.get('not', {}).get('required', []) if set(cond.get('not', {})) == {'required'} else []:
        out.pop(name, None)
    props = node.get('properties', {})
    for name in cond.get('required', []):
        out.setdefault(name, minimal(props.get(name, {})))
        for value in [out[name], *resolve(props.get(name, {})).get('enum', [])]:
            if _meets({**out, name: value}, cond):
                out[name] = value
                break
    return out


def rule_fixtures(rules):
    """Two fixtures per derived if/then rule, from the definition's minimal instance with the condition true: one that
    keeps the rule and one that breaks it.  Returns ({file name: instance}, problems)."""
    extended = extended_schema(rules)
    files, problems = {}, []
    for rule in rules:
        prop = rule['property'].split('.', 1)[1]
        node = DEFS[rule['def']]
        base = satisfy(minimal(node), rule['if'], node)
        stem = f'{rule["property"]}.{rule["presence"].lower().replace(" ", "-")}'
        if not _meets(base, rule['if']):
            problems.append(f'{stem}: the minimal {rule["def"]} does not meet the condition; no fixture can be derived')
            continue
        for other in rules:  # keep the other derived rules of the definition, so only this one decides
            other_prop = other['property'].split('.', 1)[1]
            if other is rule or other['def'] != rule['def'] or not _meets(base, other['if']):
                continue
            kept = {**base, other_prop: base.get(other_prop, minimal(node['properties'][other_prop]))} if other['presence'] == 'SHALL' \
                else {k: v for k, v in base.items() if k != other_prop}
            if _meets(kept, rule['if']):  # never at the price of this rule's own condition
                base = kept
        present = {**base, prop: minimal(node['properties'][prop])}
        absent = {k: v for k, v in base.items() if k != prop}
        keep, brk = (present, absent) if rule['presence'] == 'SHALL' else (absent, present)
        if not validator_for(rule['def']).is_valid(brk) and validator_for(rule['def']).is_valid(keep):
            rule['in_schema'] = True  # the schema says it already (an anyOf): no proposal, no fixture
            continue
        for kind, instance, should_fail in (('valid', keep, False), ('invalid', brk, True)):
            files[f'{stem}.{kind}.json'] = instance
            if not validator_for(rule['def']).is_valid(instance):
                problems.append(f'views/fixtures/{stem}.{kind}.json: invalid under the schema as it is')
            root = {'$schema': extended['$schema'], '$defs': extended['$defs'], '$ref': f'#/$defs/{rule["def"]}'}
            errors = list(jsonschema.Draft202012Validator(root).iter_errors(instance))
            if bool(errors) != should_fail:
                problems.append(f'views/fixtures/{stem}.{kind}.json: {"passes" if should_fail else "fails"} the derived rule')
    return files, problems


def rule_violations(items, rules):
    """Errors the derived if/then rules add to the twins and example/ files (none below an injected path)."""
    schema = extended_schema(rules)

    def validator(host):
        root = schema if host == LOG else {'$schema': schema['$schema'], '$defs': schema['$defs'], '$ref': f'#/$defs/{host}'}
        return jsonschema.Draft202012Validator(root)

    def new_errors(data, host, injected, elided=()):
        base = {(tuple(e.absolute_path), e.message) for e in validator_for(host).iter_errors(data)}
        out = []
        for e in validator(host).iter_errors(data):
            path = '/'.join(map(str, e.absolute_path))
            if (tuple(e.absolute_path), e.message) in base or any(path == j or path.startswith(j + '/') for j in injected) or path in elided:
                continue  # an injected object, or one whose display elides members: what it lacks is unknown
            out.append(f'/{path}: {e.message[:150]}')
        return out

    found = [(i['twin'], err) for i in items if i.get('data') is not None for err in new_errors(i['data'], i['host'], i['injected'], i['elided'])]
    for f in sorted((ROOT / 'example').glob('*.json')):
        found += [(f'example/{f.name}', err) for err in new_errors(json.loads(f.read_text(encoding='utf-8')), LOG, [])]
    return found


def generated_sentence(prop, b):
    """The uniform wording of a branch: what a sentence derived from the record's fields would say."""
    clause = f'`{prop}` **{b["presence"]}** be present'
    if b['scope'] == 'rest':
        return f'Otherwise, {clause}.'
    return f'{"Otherwise, if" if b["otherwise"] else "If"} {b["when"]}, {clause}.'


def view_constraints(records, rules, violations, in_schema=()):
    by_scope = Counter(b['scope'] for r in records for b in r['branches'])
    out = ['# Constraints', '', 'Derived by `bin/vision.py derive` from `records/constraints.yaml`; do not edit.', '',
           f'{len(records)} presence rules ({sum(1 for r in records if r["announce"])} announced with a set of keywords, '
           f'{sum(1 for r in records if not r["announce"])} with conditional claims only), {sum(by_scope.values())} branches: '
           + ', '.join(f'{by_scope[s]} {s}' for s in SCOPES) + ' scope.',
           f'{len(rules) + len(in_schema)} branches the schema can say; {len(in_schema)} it says already '
           f'({", ".join(f"`{x["property"]}`" for x in in_schema) or "none"}), {len(rules)} are derived as `if`/`then` into `views/constraints.schema.json`, '
           f'a proposal for the TC; against the twins and `example/` they find {len(violations)} violation(s).',
           f'Each rule has a fixture that keeps it and one that breaks it (`views/fixtures/`); both pass the schema as it is. '
           'They start from the smallest instance the schema allows, so an empty object in them (an `artifactLocation` '
           'without `uri` and `index`) is what the schema accepts, not what the prose asks for.',
           '', 'Below each table, the wording a sentence generated from the record would have: a proposal for the TC, '
           'until which the prose keeps its own sentences (derived verbatim from the records).', '']
    for r in records:
        out += [f'## `{r["property"]}`', '', f'{r["file"]}; announced: ' + ', '.join(f'**{k}**' for k in r['announce']), '',
                '| | Presence | When | Scope | Schema |', '|---|---|---|---|---|']
        for i, b in enumerate(r['branches'], 1):
            reason = schema_reason(r, i - 1)
            out.append(f'| {i} | **{b["presence"]}** | {"otherwise, " if b["otherwise"] else ""}{md_escape(b["when"])} | {b["scope"]} | '
                       f'{"if/then" if reason is None else reason} |')
        prop = r['property'].split('.', 1)[1]
        out += ['', *(f'{i}. {generated_sentence(prop, b)}' for i, b in enumerate(r['branches'], 1)), '']
    return '\n'.join(out)


def constraint_findings(records, violations, bound_violations=()):
    out = []
    for r in records:
        missing = [k for k in r['announce'] if k not in {b['presence'] for b in r['branches']}]
        extra = sorted({b['presence'] for b in r['branches']} - set(r['announce']))
        if missing:
            out.append(f'- **TC** `{r["property"]}`: announced ' + ', '.join(f'**{k}**' for k in missing) + ' is given by no branch')
        if extra:
            out.append(f'- **TC** `{r["property"]}`: a branch gives ' + ', '.join(f'**{k}**' for k in extra) + ', which the announcement lacks')
        out += [f'- **TC** `{r["property"]}`: {md_escape(q)}' for q in r.get('tc', [])]
        prop = r['property'].split('.', 1)[1]
        if any('binds' in b for b in r['branches']):
            out += [f'  - as a rule of the log file, `{where}` would break it: {md_escape(err)}'
                    for where, err in bound_violations if f"'{prop}'" in err]
    out += [f'- `{where}` breaks a derived presence rule: {md_escape(err)} (if the example is a fragment, it lacks an elision marker)'
            for where, err in violations]
    return out


def constraint_keys():
    """Refusals: a record out of step with its property section, an announcing statement without a record."""
    _, _, statements, _ = read_prose()
    records = {r['property']: r for r in constraint_records()}
    problems = []
    for a, rest in constraint_sections(statements):
        key = f'{a["obj"]}.{a["prop"]}'
        r = records.pop(key, None)
        if r is None:
            problems.append(f'{a["file"]}:{a["line"]}: `{key}` announces a set of keywords; records/constraints.yaml has no record')
            continue
        where = f'records/constraints.yaml: `{key}`'
        if r['announce'] != ANNOUNCED.findall(KEYWORD_SET.search(a['text']).group(0)):
            problems.append(f'{where}: announce differs from the prose')
        if len(rest) != len(sentence_sequence(r)):
            problems.append(f'{where}: the section has {len(rest)} statements, the record {len(sentence_sequence(r))}: '
                            'add or remove a sentence in the record, then make derive')
        for i, b in enumerate(r['branches'], 1):
            if b['presence'] not in presences(b['sentence'], a['prop']):
                problems.append(f'{where}: branch {i}: its sentence does not give **{b["presence"]}**')
            if b['scope'] not in SCOPES:
                problems.append(f'{where}: branch {i}: scope {b["scope"]!r} is none of {", ".join(SCOPES)}')
            if (b['scope'] == 'object') != ('if' in b):
                problems.append(f'{where}: branch {i}: an object-scope branch needs its condition as `if`, and only it')
            elif 'if' in b:
                try:
                    jsonschema.Draft202012Validator.check_schema(b['if'])
                except jsonschema.SchemaError as e:
                    problems.append(f'{where}: branch {i}: `if` is no JSON Schema: {e.message[:90]}')
    for file, obj, prop, rest in unannounced_sections(statements):
        key = f'{obj}.{prop}'
        r = records.pop(key, None)
        where = f'records/constraints.yaml: `{key}`'
        if r is None:
            problems.append(f'{file}:{rest[0]["line"]}: `{key}` makes a conditional presence claim; records/constraints.yaml has no record')
            continue
        if r['announce']:
            problems.append(f'{where}: announce lists keywords, the prose announces none')
        if len(rest) != len(sentence_sequence(r)):
            problems.append(f'{where}: the section has {len(rest)} statements, the record {len(sentence_sequence(r))}: '
                            'add or remove a sentence in the record, then make derive')
        for i, b in enumerate(r['branches'], 1):
            if (b.get('property', prop), b['presence']) not in claims(b['sentence'], prop):
                problems.append(f'{where}: branch {i}: its sentence does not claim **{b["presence"]}** for `{b.get("property", prop)}`')
            if b['scope'] not in SCOPES:
                problems.append(f'{where}: branch {i}: scope {b["scope"]!r} is none of {", ".join(SCOPES)}')
            if (b['scope'] == 'object') != ('if' in b):
                problems.append(f'{where}: branch {i}: an object-scope branch needs its condition as `if`, and only it')
    problems += [f'records/constraints.yaml: `{key}`: no section with an announcement or a conditional presence claim' for key in records]
    problems += definition_keys(statements)
    if not problems:
        problems += rule_fixtures(schema_rules(constraint_records()))[1]  # the rules the schema says already are no problem
    return problems


WHEN = re.compile(r'^(?:Otherwise,?\s*(?:\(that is, )?)?(?:If|When|Unless)\s+(.+?),\s+(?:then\s+)?(?:it|its|the|an?|`|enough|at least|again)\b')
LOG_WORDS = re.compile(r'\bthe(?:Run|Result|Tool|SarifLog|Component|Descriptor|Parent)\b|element of|any `?result')


def migrate_presence():
    """Append a record for each unannounced section with a conditional presence claim; scope by rule, review after."""
    target = RECORDS / 'constraints.yaml'
    have = {r['property'] for r in constraint_records()}
    _, _, statements, _ = read_prose()
    new = []
    for file, obj, prop, rest in unannounced_sections(statements):
        if f'{obj}.{prop}' in have:
            continue
        rec = {'property': f'{obj}.{prop}', 'file': file, 'announce': [], 'also': [], 'branches': []}
        for st in rest:
            found = claims(st['text'], prop)
            m = WHEN.match(st['text'])
            when = m.group(1) if m else ('in all other cases' if st['text'].startswith('Otherwise') else 'always')
            scope = 'rest' if not m else ('log' if LOG_WORDS.search(when) else 'world')
            for target_prop, level in found:
                b = {'presence': level, 'when': when, 'scope': scope, 'otherwise': st['text'].startswith('Otherwise')}
                if target_prop != prop:
                    b['property'] = target_prop
                rec['branches'].append({**b, 'sentence': st['text']})
            if not found:
                (rec['branches'][-1].setdefault('also', []) if rec['branches'] else rec['also']).append(st['text'])
        if not rec['also']:
            del rec['also']
        new.append(rec)
    text = target.read_text(encoding='utf-8')
    target.write_text(text.rstrip('\n') + '\n' + yaml.safe_dump(new, sort_keys=False, allow_unicode=True, width=120), encoding='utf-8')
    print(f'appended {len(new)} records without an announcement, {sum(len(r["branches"]) for r in new)} branches: review when and scope')


def migrate_constraints():
    target = RECORDS / 'constraints.yaml'
    if target.exists():
        sys.exit(f'{target.relative_to(ROOT)} exists: migrate-constraints seeds it once')
    _, _, statements, _ = read_prose()
    records = []
    for a, rest in constraint_sections(statements):
        branches, also = [], []
        for s in rest:
            found = presences(s['text'], a['prop'])
            for level in found:
                branches.append({'presence': level, 'when': 'TODO', 'scope': 'TODO', 'otherwise': s['text'].startswith('Otherwise'),
                                 'sentence': s['text']})
            if not found:
                (branches[-1].setdefault('also', []) if branches else also).append(s['text'])
        records.append({'property': f'{a["obj"]}.{a["prop"]}', 'file': a['file'],
                        'announce': ANNOUNCED.findall(KEYWORD_SET.search(a['text']).group(0)), 'also': also, 'branches': branches})
    target.write_text(yaml.safe_dump({'constraints': records}, sort_keys=False, allow_unicode=True, width=1000), encoding='utf-8')
    print(f'seeded {len(records)} constraint records, {sum(len(r["branches"]) for r in records)} branches')


def migrate():
    target = RECORDS / 'examples.yaml'
    if target.exists():
        sys.exit(f'{target.relative_to(ROOT)} exists: migrate seeds it once; edit the record instead')
    good, bad = markers()
    lines = [
        '# One record per example twin (prose/edit/src/json-examples/): the schema definition that hosts it.',
        '# Seeded by `bin/vision.py migrate` from the twin\'s top-level keys and its section; reviewed by hand.',
        '# `host` is a $defs name or sarifLog; derive validates the twin as that definition after removing the',
        '# markers (twins.markers in prose/edit/etc/nide.yaml) and injecting the required context. `note` explains a missing host.',
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


def _no_duplicates(pairs):
    keys = [k for k, _ in pairs]
    dupes = sorted({k for k in keys if keys.count(k) > 1})
    if dupes:
        raise ValueError(', '.join(dupes))
    return dict(pairs)


def check_records():
    problems = []
    for path in sorted(TWINS.glob('*.json')):
        try:
            json.loads(path.read_text(encoding='utf-8'), object_pairs_hook=_no_duplicates)
        except ValueError as e:
            problems.append(f'{path.relative_to(ROOT)}: duplicate key {e} (a second marker in one object needs a number)')
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
    if command == 'migrate-notes':
        migrate_notes()
        return
    if command == 'migrate-constraints':
        migrate_constraints()
        return
    if command == 'migrate-presence':
        migrate_presence()
        return
    if command == 'migrate-defaults':
        migrate_defaults()
        return
    problems = check_records() + broken_keys() + constraint_keys() + default_keys()  # the twins' keys and snippets: nide quality
    if problems:
        sys.exit('\n'.join(problems))
    views = derive_all()
    prose = derive_prose()
    if command == 'derive':
        for rel, text in views.items():
            path = VIEWS / rel
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(text, encoding='utf-8')
        for name, text in prose.items():
            (SRC / name).write_text(text, encoding='utf-8')
        sentences = sum(len(sentence_sequence(r)) for r in constraint_records())
        print(f'derived {len(views)} views into views/, {sentences} constraint sentences into {len(prose)} prose files (the snippets: nide derive)')
    elif command == 'check':
        stale = [rel for rel, text in views.items() if not (VIEWS / rel).is_file() or (VIEWS / rel).read_text(encoding='utf-8') != text]
        extra = sorted(str(p.relative_to(VIEWS)) for p in VIEWS.rglob('*') if p.is_file() and str(p.relative_to(VIEWS)) not in views)
        stale += [f'prose/edit/src/{name}' for name, text in prose.items() if (SRC / name).read_text(encoding='utf-8') != text]
        if stale or extra:
            sys.exit('views differ from the sources (run make derive):\n' + '\n'.join(f'  {r}' for r in stale + extra))
        print(f'{len(views)} views and the constraint sentences match the sources (the snippets: nide derive --check)')
    else:
        sys.exit(__doc__)


main()
