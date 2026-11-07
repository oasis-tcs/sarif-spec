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
| the twins `prose/edit/src/json-examples/*.json` (unchanged) | `views/examples.md`; the example findings |
| `records/examples.yaml`: one record per twin, its host definition | the validation of each twin as that definition |
| `records/markers.yaml`: the grammar of the elision markers | the marker checks; the elision in a future snippet |
| `records/roles.yaml`: the roles and the words the prose uses for them | `views/roles/<role>.md`: the statements per role |
| the prose (unchanged, still hand-written Markdown) | `views/findings.md`: what disagrees with the schema |

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
members were injected, the result, and whether a JSON code block of the prose says the same as the twin.

## Done

1. **Records, checks and views (2026-11-07).** `bin/vision.py migrate` seeded `records/examples.yaml` from the twins'
   top-level keys and sections; three hosts were set by hand (the redaction example is a `run`, the external properties
   example an `externalProperties` object, the `fix` description example has no host: it wraps the fix in a label key).
   `derive` writes the findings, the examples view and the role views; `check` keeps them in step.
   The findings reproduce the hand-checked assessment in `../assessment/README.md`, now as a derived view.
   State: 101 of 120 twins are valid after injection; 81 of 120 twins say the same as a snippet of their prose file.

## Next steps

2. **Snippets derived from twins.** A display record per example (or keys in the twin's record): which members to
   elide (the markers already say where), and the margin notes as keys, a JSON pointer and a section label per note,
   rendered as today's `# An artifact object ((#artifact-object)).` comments. The 81 agreeing snippets become derived
   first, proven lossless by comparing the rendered prose; the other 39 are decided one by one (the twin or the
   snippet drifted). After that, a renamed section or a moved property is a broken key found by the build, not a
   stale margin note found by a reader.
3. **Heading keys.** Fix the four property headings that do not give their property as `` `name` Property ``, then
   let `check` refuse such a heading, and refuse a property section without a schema property (and back).
4. **Constraint records (A2).** The presence rules and conditional defaults as records: one record per rule, from
   which the sentences, a JSON Schema `if`/`then` where the schema can say it, and one test fixture per branch are
   derived. Start with the 15 statements that announce a set of keywords ("either **SHALL** or **MAY**").
5. **Statement records with subjects (A3).** Each statement records whom it binds (the log file, a producer, a
   consumer, a viewer ...); the role views are then derived from the records instead of from the wording.
6. **TC findings.** Bring the findings marked **TC** in `views/findings.md` to the TC: they are decisions, not edits.
   The largest: `suppression.justificationType` (#672) and the `columnKind` value `"bytes"` (#740) exist only in the
   prose; `attachment.location` and `externalProperties.$schema` differ from the schema's names; 16 example twins
   contradict the schema (most often the pre-2.1 form `physicalLocation.uri`; the conversion example, hidden behind
   a malformed marker in the assessment, has two more).

## Files

- `bin/vision.py`: migrate, derive, check (Python with jsonschema and PyYAML, the repository's pyenv environment)
- `records/`: examples, markers, roles
- `views/`: findings, examples, `roles/<role>.md` (derived, never edit)
- `makefile`: derive, check, prose
