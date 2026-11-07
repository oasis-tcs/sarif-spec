# SARIF vision: author once, derive the rest

This tree is SARIF 2.2 CSD01 (in public review) on the spike branch `sarif-2-3-spike`, extended by records and derived
views. The specification itself is unchanged so far: the prose, the schema and the examples are exactly those of the
draft. What is new is a second way of reading them, built so that every restatement is derived or checked, never
neither.

The aim is the one of the CSAF, DPS PM and MQTT-SN reworks: editors author each fact once, in the place that fits it
(the schema, a record, a twin), and the views (prose snippets, tables, role views, test fixtures) are derived from it.
Bionic and cybernetic collaboration does the transcription, the cross-checking and the tracing back to the source;
the editors and the TC keep the decisions.

SARIF is not a network protocol. It is closer to what USB-C did for a fragmented adapter market: one format that tool
vendors can carry their own ideas into. The many **MAY** are intended and not counted as findings here.

## Where errors live in SARIF

| ID | Area | Carried by in SARIF | State in CSD01 |
|---|---|---|---|
| A0 | Intent | TC decisions, accepted proposals | two accepted proposals reached the prose only (see findings) |
| A1 | Shape | `schema/sarif.json` (54 definitions, 51 closed) | consistent; enums complete |
| A2 | Constraint | rules beyond the shape: presence rules, conditional defaults | prose only, spread over several sentences |
| A3 | Statement | 996 normative sentences | most name no role; the log file is their subject |
| A4 | Illustration | 127 JSON snippets, 120 example twins, 7 example files | snippets unvalidatable as written; twins validatable |
| A5 | Implementation | validators, converters, viewers, result management systems | outside this tree |
| A6 | Operation | SARIF logs exchanged between tools | outside this tree |

## What an editor authors, what is derived

| You edit | Derived from it (never edit) |
|---|---|
| `schema/sarif.json` (unchanged) | the schema side of every check |
| the twins `prose/edit/src/json-examples/*.json` | the prose snippets of 98 examples, byte for byte; `views/examples.md` |
| `records/examples.yaml`: one record per twin: its host definition, and its `display` | the validation of each twin; the snippet's layout and margin notes |
| `records/markers.yaml`: the grammar of the elision markers | the marker checks; the elision in a future snippet |
| `records/roles.yaml`: the roles and the words the prose uses for them | `views/roles/<role>.md`: the statements per role |
| the prose (hand-written Markdown, except the derived snippets) | `views/findings.md`: what disagrees with the schema |

Workflow: edit a source, run `make derive`, review the diff of the views, run `make check` before committing.
`make check` fails when a view is stale or a record is incomplete (a twin without a record, a host that is no schema
definition). `make prose` runs the check and then the usual nide build in `prose/edit`.

### How an example is validated

A twin is the full example as JSON. Where the prose leaves something out, the twin carries a marker
(`"...member-inject": "..."` for elided members, `{"...object-inject": "..."}` or `"...string-inject"` for elided
array elements; see `records/markers.yaml`). For validation, derive

1. removes the markers (a key or string that only looks like a marker is reported as malformed),
2. injects what the schema requires and the display leaves out: required members, the first of required
   alternatives, one element in a required array that the display elided, each the smallest value the schema accepts,
3. validates the result as the host definition from `records/examples.yaml`.

What remains is what the example itself says about SARIF. `views/examples.md` lists, per twin, the host, how many
members were injected, the result, and whether its prose snippet is derived or still hand-written.

### How a snippet is derived

The `display` of an example record says how its twin appears in the prose: the prose file and the number of its JSON
code block (`file`, `fence`, counted from 0), `root: member` for a snippet that shows members without the enclosing
braces, and then the layout, keyed by JSON pointers into the twin, never by line numbers:

- `notes`: the margin notes (`# An artifact object ((#artifact-object)).`) at a pointer (`#end` for the closing line,
  `line` for a continuation line), all starting at `column` unless a note says otherwise;
- `breaks`: a long line continued on the next line (inside a string or after a key), `[cut, indent]` per break;
- `inline`: arrays shown on one line (`[ "a", "b" ]`); `open`: an elided object shown as `{ ... }`;
- `blank-before` and `trailing`: blank lines and trailing spaces, kept so the prose stays byte-identical.

Edit the twin to change what an example says; edit its `display` to change how it looks; run `make derive`, and the
prose snippet follows. Never edit a derived snippet in the prose: `make check` fails. To add an example, add the twin,
its record with `host`, and run `python -I bin/vision.py migrate-snippets` after writing the snippet once by hand
(or write the `display` directly). Inserting a JSON code block before a derived one in the same file shifts the
`fence` numbers: `make check` then fails and names the file.

## Done

1. **Records, checks and views (2026-11-07).** `bin/vision.py migrate` seeded `records/examples.yaml` from the twins'
   top-level keys and sections; three hosts were set by hand (the redaction example is a `run`, the external properties
   example an `externalProperties` object, the `fix` description example has no host: it wraps the fix in a label key).
   `derive` writes the findings, the examples view and the role views; `check` keeps them in step.
   The findings reproduce the hand-checked assessment in `assessment/README.md`, now as a derived view.
   State then: 101 of 120 twins were valid after injection; 81 of 120 twins said the same as a snippet of their file.

2. **Snippets derived from twins (2026-11-07).** `bin/vision.py migrate-snippets` learned a `display` for every
   twin whose snippet it can reproduce byte for byte; `derive` writes those snippets into the prose and `check`
   guards them. Proof of losslessness: after `derive`, git sees no change in any prose file. Proof of derivation:
   changing a URI in the property-bag twin changed the prose snippet, line break and margin note kept.
   The marker typos in three twins were fixed on the way (`...member-inkect`, `member-insert`, `member-inject`,
   `...item-inject`); they never reached the prose. `check` now also refuses a twin with a duplicate key.
   State: 98 of 120 snippets derived; 103 of 120 twins valid after injection; 22 snippets still hand-written,
   listed in the findings with the first line where twin and snippet part: mostly real divergences (a missing
   `guid`, `results: []` against an elided list, `logicalLocation` against `logicalLocations`, other URIs and
   paths), a few layout habits a later round can learn (a double space before `{`).

## Next steps

3. **The remaining 22 snippets.** Decide per example which side drifted, correct the twin or the snippet, derive.
   Then the margin notes: today they are text (`((#artifact-object))`); as keys (a section label checked against the
   prose) a renamed section is a broken key found by the build, not a stale note found by a reader.
4. **Heading keys.** Fix the four property headings that do not give their property as `` `name` Property ``, then
   let `check` refuse such a heading, and refuse a property section without a schema property (and back).
5. **Constraint records (A2).** The presence rules and conditional defaults as records: one record per rule, from
   which the sentences, a JSON Schema `if`/`then` where the schema can say it, and one test fixture per branch are
   derived. Start with the 15 statements that announce a set of keywords ("either **SHALL** or **MAY**").
6. **Statement records with subjects (A3).** Each statement records whom it binds (the log file, a producer, a
   consumer, a viewer ...); the role views are then derived from the records instead of from the wording.
7. **TC findings.** Bring the findings marked **TC** in `views/findings.md` to the TC: they are decisions, not edits.
   The largest: `suppression.justificationType` (#672) and the `columnKind` value `"bytes"` (#740) exist only in the
   prose; `attachment.location` and `externalProperties.$schema` differ from the schema's names; 16 example twins
   contradict the schema (most often the pre-2.1 form `physicalLocation.uri`; the conversion example, hidden behind
   a malformed marker in the assessment, has two more).

## Files

- `bin/vision.py`: migrate, derive, check (Python with jsonschema and PyYAML, the repository's pyenv environment)
- `records/`: examples, markers, roles
- `views/`: findings, examples, `roles/<role>.md` (derived, never edit)
- `makefile`: derive, check, prose
