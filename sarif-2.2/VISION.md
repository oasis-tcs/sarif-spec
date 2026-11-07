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
| the twins `prose/edit/src/json-examples/*.json` | the prose snippets of all 120 examples, byte for byte; `views/examples.md` |
| `records/examples.yaml`: one record per twin: its host definition, and its `display` | the validation of each twin; the snippet's layout and margin notes |
| `records/markers.yaml`: the grammar of the elision markers | the marker checks; the elision in a future snippet |
| `records/roles.yaml`: the roles and the words the prose uses for them | `views/roles/<role>.md`: the statements per role |
| `records/constraints.yaml`: the presence rules announced with a set of keywords, one branch per condition | `views/constraints.md`; `views/constraints.schema.json` (the if/then the schema can say, a proposal for the TC); the constraint findings |
| `records/drift.yaml`: the known differences between property sections and schema properties, each waiting for the TC | the refusal of every other difference; the TC entries of `views/findings.md` |
| the prose (hand-written Markdown, except the derived snippets) | `views/findings.md`: what disagrees with the schema |

Workflow: edit a source, run `make derive`, review the diff of the views, run `make check` before committing.
`make check` fails when a view is stale or a record is incomplete (a twin without a record, a host that is no schema
definition), and when a property heading or section has no key in the schema (below, step 6). `make prose` runs the check and then the usual nide build in `prose/edit`.

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

The `display` of an example record says how its twin appears in the prose: the prose file (`file`), whose code block
carries the twin as its key (```` ```{.json twin="<twin file>"} ````, an attribute pandoc renders as a JSON block and
nide's quality engine ignores until it has a definition for it), `root: member` for a snippet that shows members
without the enclosing braces, and then the layout, keyed by JSON pointers into the twin, never by line numbers:

- `notes`: the margin notes (`# An artifact object ((#artifact-object)).`) at a pointer (`#end` for the closing line,
  `line` for a continuation line), all starting at `column` unless a note says otherwise;
- `breaks`: a long line continued on the next line (inside a string or after a key), `[cut, indent]` per break;
- `inline`: arrays shown on one line (`[ "a", "b" ]`); `open`: an elided object shown as `{ ... }`;
- `blank-before` and `trailing`: blank lines and trailing spaces, kept so the prose stays byte-identical.

Edit the twin to change what an example says; edit its `display` to change how it looks; run `make derive`, and the
prose snippet follows. Never edit a derived snippet in the prose: `make check` fails. To add an example, add the twin,
its record with `host`, and run `python -I bin/vision.py migrate-snippets` after writing the snippet once by hand
(or write the `display` directly); it keys the code block for you. Code blocks can move freely: `check` finds each
derived snippet by its key, and refuses a key without a record, a record without its key, and a key used twice.

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

3. **The remaining snippets decided (2026-11-07).** The learner gained the notations the last snippets use: lines
   spaced differently (kept only while the twin's line says the same apart from whitespace), empty arrays over two
   lines, escaped separator characters, blank and note-only lines kept verbatim, indented code blocks inside quotes
   and code blocks without a language. Four twins had drifted from the prose and now follow it (the prose was right):
   the comprehensive SARIF file (valid in the prose; the twin had invented `associatedRule.ruleId` and
   `result.addresses`), the two logicalLocation `kind` examples (`/orders/order[1]/total/text()`; `logicalLocations`),
   and the `inlineExternalProperties` example (the prose elides two results). Each change left the prose untouched.
   One snippet was wrong in the prose, relationship example 2: its outer object was never closed, a comma before an
   elision was missing, and a margin note called the relationship "A reportingDescriptor object". Decided with the
   editor: the snippet follows its twin, the note now reads "A reportingDescriptorRelationship object". The only
   change to the published prose in this step: those three lines.
   State: all 120 snippets derived; 105 of 120 twins valid after injection, 14 contradict the schema in prose and
   twin alike (findings marked **TC**).

4. **Margin notes as keys (2026-11-07).** `bin/vision.py migrate-notes` turned 407 of 471 margin notes into keys:
   `see: <label>` renders "# See (#label).", `object: <name>` with `ref: <label>` renders "# A name object ((#label))."
   (64 notes stay free text, their references are still checked). The prose stayed byte-identical. Three checks:
   every referenced label exists (`check` refuses a broken key), an object note names the schema definition at its
   JSON pointer, and a "See" note on a member line names that member's property section. First findings: three
   examples whose own notes name the right property while the code holds a wrong one (`baseAddress` where the note
   says `absoluteAddress`, `offset` / `offsetFromParent`, `analysisToolLogFileLocation` / `analysisToolLogFiles`),
   a `taxonomies` element called "A toolComponentReference object", a SARIF 1.0 "file object", four remnants of
   section numbers after a reference (`(#run-object).14`), and 43 object notes without a reference.

5. **Code blocks keyed by their twins (2026-11-07).** `bin/vision.py annotate-fences` replaced the block numbers in
   the records by a key in the prose: 120 opening fence lines now read ```` ```{.json twin="..."} ```` (two of them had
   no language before and now render as JSON). The last positional key is gone. For tools to see these keys inside
   quoted examples, vyyhti now scans fences inside block quotes (`Location.quote`), and nide's legacy-syntax rewrite
   keeps a quote prefix; both wait for their releases.

6. **Heading keys (2026-11-07).** The four property headings that did not give their property as
   `` `name` Property `` now do (`arguments`, `revisionId`, `location`, `guid`); their labels are unchanged, only the
   heading texts in `prose/edit/etc/section-display-to-text.json` changed (`nide harvest`). `check` refuses a heading
   that names a property in another form (a backtick, or `x property`), a property section without a schema property,
   and a schema property the prose does not describe, unless `records/drift.yaml` records the difference; it also
   refuses an entry there that no longer holds. The four recorded ones are the assessment's S1, S3 and S4 (both
   sides), all **TC**. Group headings such as "Product hierarchy properties" name no property and stay free.

7. **Constraint records, first part (2026-11-07).** `bin/vision.py migrate-constraints` seeded
   `records/constraints.yaml` from the 15 statements that announce a set of keywords ("either **SHALL** or **MAY**
   contain a property named ..."); the conditions, their scope and the `if` were written by hand. Each record holds
   the announced keywords and one branch per condition, in prose order: its presence keyword, the condition in words,
   its scope (object, log, world, rest), whether it applies only "otherwise", the condition as JSON Schema where the
   object alone decides it, and the sentence verbatim; the other statements of the section are kept as `also`.
   `check` refuses a record out of step with its section (a sentence changed or added, a branch whose sentence lacks
   its keyword, a scope outside the four, an object branch without `if`) and an announcement without a record.
   Of 44 branches, 8 are decided by the object, 17 by other parts of the log, 15 only by the producer's knowledge,
   4 are the rest. Two become `if`/`then` (`views/constraints.schema.json`): a top-level `artifact` (no `parentIndex`)
   has a `location` and no `offset`. Validated against the twins and `example/` (objects with an elision marker or
   injected context excluded), they find one example that lacks an elision marker. Found on the way, all in
   `views/findings.md`: `result.ruleId` announces **SHALL NOT** and no branch gives it; its branches bind direct
   producers ("Direct producers **SHALL** emit either or both ...", `binds` in the record), so they stay out of the
   schema, and the findings list what a log-file rule would reject (3 `example/` files, 18 twins); `run.results` may
   be `null` in the prose, not in the schema; the prose names `theRun.originalBaseIds` for `originalUriBaseIds`.

8. **Constraint records, second part (2026-11-07).** The records are now the source of their sentences: each branch
   carries the statements that follow it (`also`), so a record gives its section's statements in prose order, and
   `make derive` writes them into the prose verbatim (78 statements in 15 sections; the prose came out
   byte-identical). `check` fails when the prose differs and refuses a section with more or fewer statements than
   its record: a sentence is added in the record, not in the prose. The prose typo `theRun.originalBaseIds` is now a
   one-line record edit. Each derived `if`/`then` has two fixtures in `views/fixtures/` (one keeps the rule, one
   breaks it, both valid under the schema as it is); `check` refuses a rule whose fixtures do not behave so.
   `views/constraints.md` shows below each table the wording a sentence generated from the record's fields would
   have ("Otherwise, if `index` is absent, `uri` **SHALL** be present."): a proposal for the TC; the `when` texts
   mark property names in backticks for it.

## Next steps

9. **Constraint records, third part.** The defaults as records (the prose's "If absent, it **SHALL** default to
   ..." against the schema's `default`), then the presence rules that are not announced with a set of keywords
   ("If ..., `x` **SHALL** be present" elsewhere), with records of the same shape.
10. **Statement records with subjects (A3).** Each statement records whom it binds (the log file, a producer, a
   consumer, a viewer ...); the role views are then derived from the records instead of from the wording.
11. **TC findings.** Bring the findings marked **TC** in `views/findings.md` to the TC: they are decisions, not edits.
   The largest: `suppression.justificationType` (#672) and the `columnKind` value `"bytes"` (#740) exist only in the
   prose; `attachment.location` and `externalProperties.$schema` differ from the schema's names; 14 examples
   contradict the schema in prose and twin alike (most often the pre-2.1 form `physicalLocation.uri`; the
   conversion example, hidden behind a malformed marker in the assessment, has two more).

## Files

- `bin/vision.py`: migrate, derive, check (Python with jsonschema and PyYAML, the repository's pyenv environment)
- `records/`: examples, markers, roles, drift, constraints
- `views/`: findings, examples, constraints (and its schema proposal), `roles/<role>.md` (derived, never edit)
- `makefile`: derive, check, prose
