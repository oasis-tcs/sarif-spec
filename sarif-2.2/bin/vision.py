"""SARIF vision: records and the schema are the sources, the views are derived and checked.

Usage (from sarif-2.2/):
  python -I bin/vision.py migrate   seed records/examples.yaml from the twins (once; review the hosts afterwards)
  python -I bin/vision.py migrate-snippets   seed the `display` of each twin whose prose snippet round-trips exactly
  python -I bin/vision.py migrate-notes      turn margin notes into keys (see, object, ref) where the text round-trips
  python -I bin/vision.py derive    write views/ from the schema, the records, the twins and the prose
  python -I bin/vision.py check     fail when a view differs from what derive would write, or a record is incomplete

Keyed, not textual, wherever the sources allow it: objects by their `` ## `x` Object `` headings, properties by
their `` ### `p` Property `` headings, matched to the schema's $defs by name; examples by their twin file and the
schema definition that hosts them; statements by bold BCP 14 keywords. See VISION.md.
"""

import copy
import json
import unicodedata
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
        item = {'twin': rec['twin'], 'host': rec.get('host'), 'note': rec.get('note', ''), 'injected': [], 'errors': [], 'markers': [],
                'derived': bool(rec.get('display')), 'snippet': rec.get('snippet', '')}
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


# ── snippets: the prose's JSON code blocks derived from the twins ─────────────

QUOTE = re.compile(r'^(> ?)?')
SPACES = re.compile(r'\s+')


def _dumps(value):
    """JSON as the prose writes it: non-ASCII as is, control and separator characters escaped."""
    text = json.dumps(value, ensure_ascii=False)
    return ''.join(f'\\u{ord(c):04x}' if unicodedata.category(c) in ('Cc', 'Zl', 'Zp') else c for c in text)


def _pointer(parent, key):
    return f'{parent}/{str(key).replace("~", "~0").replace("/", "~1")}'


def render_twin(data, root):
    """The twin as display lines (pointer, text): two-space indent, markers as `...`, `root: member` without braces."""
    good, _ = markers()
    out = []

    def is_marker(v):
        return (isinstance(v, str) and good.match(v)) or (isinstance(v, dict) and len(v) == 1 and good.match(next(iter(v))))

    def emit(v, ptr, ind, prefix, comma):
        pad = ' ' * ind
        if isinstance(v, (dict, list)) and v:
            pairs = list(v.items()) if isinstance(v, dict) else list(enumerate(v))
            out.append((ptr, pad + prefix + ('{' if isinstance(v, dict) else '[')))
            members(pairs, ptr, ind + 2, isinstance(v, dict))
            out.append((ptr + '#end', pad + ('}' if isinstance(v, dict) else ']') + comma))
        else:
            out.append((ptr, pad + prefix + _dumps(v) + comma))

    def members(pairs, ptr, ind, named):
        for n, (k, x) in enumerate(pairs):
            last = n == len(pairs) - 1
            if (named and good.match(k)) or (not named and is_marker(x)):
                out.append((_pointer(ptr, k), ' ' * ind + '...'))
                continue
            prefix = json.dumps(k, ensure_ascii=False) + ': ' if named else ''
            emit(x, _pointer(ptr, k), ind, prefix, '' if last else ',')

    if root == 'member' and isinstance(data, dict):
        members(list(data.items()), '', 0, True)
    else:
        emit(data, '', 0, '', '')
    return out


def split_note(line):
    """A snippet line as (code, note, column): the note is a `#` comment outside any string."""
    quoted = False
    for i, ch in enumerate(line):
        if ch == '"' and (i == 0 or line[i - 1] != '\\'):
            quoted = not quoted
        elif ch == '#' and not quoted and i > 0 and line[i - 1] == ' ' and line[i + 1:i + 2] in (' ', ''):
            return line[:i].rstrip(), line[i:], i
    return line.rstrip(), None, None


def json_fences(name, unmarked=False):
    """The JSON code blocks of a prose file: (first body line index, end index, line prefix) per block.

    The prefix is what stands before the fence: a quote marker and any indentation (`>   ```json`). With `unmarked`,
    code blocks without a language count too (they hold JSON in a few places, but render without highlighting).
    """
    lines = (SRC / name).read_text(encoding='utf-8').splitlines()
    out, start, prefix = [], None, ''
    for i, line in enumerate(lines):
        m = re.match(r'^((?:> ?)?\s*)```(\w*)\s*$', line)
        if not m:
            continue
        if start is None:
            start, prefix, lang = i + 1, m.group(1), m.group(2)
        else:
            if lang == 'json' or (unmarked and lang == ''):
                out.append((start, i, prefix))
            start = None
    return lines, out


def _unprefix(line, prefix):
    if line.startswith(prefix):
        return line[len(prefix):]
    return QUOTE.sub('', line, count=1) if prefix else line


def _closing(canon, i):
    """The index of the line that closes the value opened on canonical line i."""
    end = canon[i][0] + '#end'
    return next(k for k in range(i + 1, len(canon)) if canon[k][0] == end)


def _inline(canon, i):
    """Canonical lines i .. closing as one line, `[ a, b ]` style, or None when the value nests."""
    c = _closing(canon, i)
    inner = [t.strip().rstrip(',') for _, t in canon[i + 1:c]]
    if any(x.endswith(('{', '[')) for x in inner):
        return None, c
    close = canon[c][1].strip()
    return canon[i][1] + ' ' + ', '.join(inner) + ' ' + close, c


def learn_display(twin, body, prefix):
    """Migrate one snippet: its display record against the twin's canonical lines, or (None, reason)."""
    snippet = [_unprefix(line, prefix) for line in body]
    parsed = [split_note(line) for line in snippet]
    first = next((p[0] for p in parsed if p[0].strip()), '')
    root = 'member' if first.lstrip().startswith('"') else None
    canon = render_twin(twin, root)
    notes, breaks, before, inline, opened, trailing, spacing, expanded = [], {}, {}, [], {}, [], {}, {}
    pending = []  # blank lines and lines with only a note, verbatim, until the next line of the twin
    cols = Counter(c for _, n, c in parsed if n)
    default_col = cols.most_common(1)[0][0] if cols else None
    i = j = 0
    while i < len(canon) and j < len(parsed):
        ptr, text = canon[i]
        code = parsed[j][0]
        if not code.strip():
            pending.append(body[j])
            j += 1
            continue
        if pending:
            before[ptr], pending = pending, []
        span, step = [j], 1
        if code != text:
            if text.rstrip().endswith(('[', '{')) and (one := _inline(canon, i))[0] == code:
                inline.append(ptr)
                step = one[1] - i + 1
            elif text.strip() == '...' and code.strip() in ('{', '[') and j + 2 < len(parsed) and parsed[j + 1][0].strip() == '...':
                opened[ptr] = [code.strip(), parsed[j + 2][0].strip()]
                span = [j, j + 1, j + 2]
            elif SPACES.sub(' ', code.strip()) == SPACES.sub(' ', text.strip()):
                spacing[ptr] = code  # the same line, spaced differently
            elif (m := re.match(r'^(.*[\[{])([\]}],?)$', text)) and code == m.group(1) and j + 1 < len(parsed) \
                    and parsed[j + 1][0].strip() == m.group(2):
                expanded[ptr] = len(parsed[j + 1][0]) - len(parsed[j + 1][0].lstrip())  # [] written as [ and ]
                span = [j, j + 1]
            else:
                acc, cuts = code, []
                while acc != text and text.startswith(acc) and span[-1] + 1 < len(parsed):
                    nxt = parsed[span[-1] + 1][0]
                    cuts.append([len(acc), len(nxt) - len(nxt.lstrip())])
                    acc = acc + ' ' + nxt.lstrip()
                    span.append(span[-1] + 1)
                if acc != text:
                    return None, f'line {j + 1} differs from the twin: {code.strip()[:60]!r} vs {text.strip()[:60]!r}'
                breaks[ptr] = cuts
        for offset, k in enumerate(span):
            _, note, col = parsed[k]
            trail = len(snippet[k]) - len(snippet[k].rstrip())
            if trail and not note:
                trailing.append([ptr, offset, trail])
            if note:
                rec = {'at': ptr, 'note': note}
                if offset:
                    rec['line'] = offset
                if col != default_col:
                    rec['column'] = col
                notes.append(rec)
        i, j = i + step, span[-1] + 1
    while j < len(parsed) and not parsed[j][0].strip():
        pending.append(body[j])
        j += 1
    if pending:
        before['#tail'] = pending
    if i < len(canon) or j < len(parsed):
        return None, 'the snippet and the twin have a different number of lines'
    display = {'root': root} if root else {}
    for key, value in (('column', default_col), ('inline', inline), ('open', opened), ('notes', notes),
                       ('breaks', breaks), ('trailing', trailing), ('spacing', spacing), ('expanded', expanded),
                       ('before', before)):
        if value or value == 0:
            display[key] = value
    return display, None


def render_snippet(twin, display, prefix):
    canon = render_twin(twin, display.get('root'))
    lines, i = [], 0
    before = display.get('before', {})
    while i < len(canon):
        ptr, text = canon[i]
        lines += [(None, -1, raw) for raw in before.get(ptr, [])]
        if ptr in display.get('inline', []):
            text, c = _inline(canon, i)
            lines.append((ptr, 0, text))
            i = c + 1
            continue
        if ptr in display.get('open', {}):
            pad = text[:len(text) - len(text.lstrip())]
            lines += [(ptr, 0, pad + display['open'][ptr][0]), (ptr, 1, pad + '  ...'), (ptr, 2, pad + display['open'][ptr][1])]
            i += 1
            continue
        if ptr in display.get('expanded', {}):
            m = re.match(r'^(.*[\[{])([\]}],?)$', text)
            lines += [(ptr, 0, m.group(1)), (ptr, 1, ' ' * display['expanded'][ptr] + m.group(2))]
            i += 1
            continue
        own = display.get('spacing', {}).get(ptr)
        if own is not None and SPACES.sub(' ', own.strip()) == SPACES.sub(' ', text.strip()):
            text = own  # spacing only: the twin's content still wins
        cuts = display.get('breaks', {}).get(ptr)
        if cuts:
            pieces, prev = [], 0
            for cut, _ in cuts:
                pieces.append(text[prev:cut])
                prev = cut + 1
            pieces.append(text[prev:])
            lines += [(ptr, k, (' ' * cuts[k - 1][1] if k else '') + piece) for k, piece in enumerate(pieces)]
        else:
            lines.append((ptr, 0, text))
        i += 1
    lines += [(None, -1, raw) for raw in before.get('#tail', [])]
    notes = {(n['at'], n.get('line', 0)): n for n in display.get('notes', [])}
    trail = {(p, k): n for p, k, n in display.get('trailing', [])}
    rendered = []
    for ptr, k, line in lines:
        if k == -1:
            rendered.append(line)  # verbatim, with its own quote prefix
            continue
        n = notes.get((ptr, k))
        if n:
            col = n.get('column', display.get('column'))
            line = line + ' ' * max(col - len(line), 1) + note_text(n)
        line += ' ' * trail.get((ptr, k), 0)
        rendered.append(prefix + line)
    return rendered


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
    """The prose files with every derived snippet rendered from its twin into its code block."""
    by_file = defaultdict(list)
    for rec in snippet_records():
        by_file[rec['display']['file']].append(rec)
    files = {}
    for name, recs in by_file.items():
        lines, fences = json_fences(name, unmarked=True)
        for rec in sorted(recs, key=lambda r: -r['display']['fence']):
            start, end, prefix = fences[rec['display']['fence']]
            twin = json.loads((TWINS / rec['twin']).read_text(encoding='utf-8'))
            lines[start:end] = render_snippet(twin, rec['display'], prefix)
        files[name] = '\n'.join(lines) + '\n'
    return files


def migrate_snippets():
    """Seed `display` for every twin whose snippet round-trips byte for byte; report the others."""
    path = RECORDS / 'examples.yaml'
    records = yaml.safe_load(path.read_text(encoding='utf-8'))['examples']
    taken, report = set(), Counter()
    for rec in records:
        if rec.get('display'):
            taken.add((rec['display']['file'], rec['display']['fence']))
    for rec in records:
        if rec.get('display'):
            continue
        twin = json.loads((TWINS / rec['twin']).read_text(encoding='utf-8'))
        name = rec['twin'].split('_')[0] + '.md'
        if not (SRC / name).is_file():
            report['no prose file'] += 1
            continue
        lines, fences = json_fences(name, unmarked=True)
        reason, depth = 'no code block of its file matches', -1
        for n, (start, end, prefix) in enumerate(fences):
            if (name, n) in taken:
                continue
            display, why = learn_display(twin, lines[start:end], prefix)
            if display is None:
                m = re.match(r'line (\d+)', why)
                if m and int(m.group(1)) > depth:
                    depth, reason = int(m.group(1)), f'closest is code block {n}, whose {why}'
                continue
            if render_snippet(twin, display, prefix) != lines[start:end]:
                reason = f'block {n} renders differently'
                continue
            rec['display'] = {'file': name, 'fence': n} | display
            taken.add((name, n))
            break
        else:
            rec['snippet'] = reason
        report['derived' if rec.get('display') else 'hand-written'] += 1
    header = [line for line in path.read_text(encoding='utf-8').splitlines() if line.startswith('#')]
    header += [
        '# `display` (seeded by `bin/vision.py migrate-snippets`): the snippet in the prose derived from this twin.',
        '# file/fence: the prose file and the number of its JSON code block (from 0); root: member shows the members',
        '# without braces; column: where margin notes start; notes: a margin note at a JSON pointer (#end: the closing',
        '# line; line: a continuation line); breaks: a long line continued on the next line, [cut, indent] per break;',
        '# inline: arrays on one line; open: an elided object as { ... }; spacing: a line spaced differently (whitespace',
        '# only, the twin still wins); expanded: [] written over two lines; before: blank and note-only lines, verbatim.',
        '# `snippet`: why the snippet is still hand-written.',
    ]
    body = yaml.safe_dump({'examples': records}, sort_keys=False, allow_unicode=True, width=150)
    path.write_text('\n'.join(dict.fromkeys(header)) + '\n\n' + body, encoding='utf-8')
    print(', '.join(f'{v} {k}' for k, v in report.items()))


def derive_all():
    sections, headings, statements, fences = read_prose()
    items = examples()
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
    if command == 'migrate-snippets':
        migrate_snippets()
        return
    if command == 'migrate-notes':
        migrate_notes()
        return
    problems = check_records() + broken_keys()
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
        print(f'derived {len(views)} views into views/, {len(snippet_records())} snippets into {len(prose)} prose files')
    elif command == 'check':
        stale = [rel for rel, text in views.items() if not (VIEWS / rel).is_file() or (VIEWS / rel).read_text(encoding='utf-8') != text]
        extra = sorted(str(p.relative_to(VIEWS)) for p in VIEWS.rglob('*.md') if str(p.relative_to(VIEWS)) not in views)
        stale += [f'prose/edit/src/{name}' for name, text in prose.items() if (SRC / name).read_text(encoding='utf-8') != text]
        if stale or extra:
            sys.exit('views differ from the sources (run make derive):\n' + '\n'.join(f'  {r}' for r in stale + extra))
        print(f'{len(views)} views and {len(snippet_records())} derived snippets match the sources')
    else:
        sys.exit(__doc__)


main()
