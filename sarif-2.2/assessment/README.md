# SARIF 2.2 CSD01: Assessment Toward a Derived Specification

Assessed: branch `sarif-2-3-spike` (state of SARIF v2.2 CSD01 in public review), 2026-11-07.
Read-only: nothing in `sarif-2.2/` was changed.

Reproduce (any Python with `jsonschema` >= 4.18):

```
python -I assessment/assess.py . assessment/assess-2026-11-07.json   # from sarif-2.2/
```

The raw results are in `assess-2026-11-07.json`; this page is the reading of them.
Every finding listed as confirmed was checked by hand against the source; counts are from the script.

## Method

Keyed, not textual, wherever the sources allow it:

- objects by their headings `` ## `x` Object ``, matched to the schema's `$defs` by name;
- properties by their headings `` ### `p` Property `` (and grouped headings such as
  `` ### `top`, `left`, `bottom`, and `right` Properties ``), matched to the schema's properties of that object;
- normative statements by bold BCP 14 keywords, sentence by sentence, outside quoted blocks (notes, examples);
- example twins (`prose/edit/src/json-examples/`) validated against the schema definition whose properties cover
  the twin's top-level keys, preferring the section's own object;
  a twin that is a whole log (`version` and `runs`) is validated against the full schema and sorted by hand;
  validation errors are sorted into *context* (a required property or a required alternative is missing: the snippet
  shows a fragment), *marker* (an injection marker or a duplicate created by markers) and *content* (anything else).

Vocabulary as in the CD26 talk:
L1 shape (schema), L2 constraint (rules beyond the shape), L3 statement (normative sentence), L4 illustration
(examples, tables, figures); a *restatement* repeats a fact of another level, *drift* is a restatement that no longer
equals its source.

## In numbers

| What | Count |
|---|---|
| Schema | 54 `$defs`, 51 of them closed (`additionalProperties: false`), 420 properties, 12 enums, 114 defaults |
| Prose objects | 52 object sections; every schema object has one, except `propertyBag` (described as a concept in "Property Bags") |
| Normative statements | 996 sentences with bold keywords |
| Keywords | SHALL 475 · MAY 385 · SHOULD 145 · SHALL NOT 60 · SHOULD NOT 20 · MUST, MUST NOT, REQUIRED, RECOMMENDED, NOT RECOMMENDED, OPTIONAL 1 each (the conventions sentence) |
| Subject of a statement | 645 an object or property (the log file: binds the producer implicitly) · 237 name a role · 114 no subject found |
| Presence rules | 97 statements on presence or absence of a property, 87 of them conditional |
| Code blocks | 148 fences, 127 of them JSON; 8 of the 127 parse as JSON |
| JSON blocks | 107 with comments (`#`), 83 with section references in the margin, 50 with elisions (`...`) |
| Twins | 120 (one JSON section has none: `region` object); 25 valid as they stand, 75 valid except for context or markers, 15 with content errors, 5 not matchable to one definition |
| Example folder | 7 files; 6 valid, `graft.json` declares version `2.1.0` and fails the 2.2 schema |

On requirement levels: the many MAY are intended. SARIF has to let tool vendors carry their own ideas into the format
(it is closer to what USB-C did for a fragmented adapter market than to a network protocol), so permissiveness is not
counted as a finding here.

## Findings: the prose and the schema disagree (L3 vs L1)

All four confirmed by hand.

| # | Where | Prose says | Schema says | Origin |
|---|---|---|---|---|
| S1 | `suppression` | a property `justificationType`, "an enumeration with the following five values" | no such property (`suppression` is closed, so a document using it is invalid) | prose added by #672 (issue 574); schema never followed |
| S2 | `run.columnKind` | three values, including `"bytes"` | enum `utf16CodeUnits`, `unicodeCodePoints` | prose added by #740 (issue 466); schema never followed |
| S3 | `attachment` | property `location` | property `artifactLocation` | the twin of the attachment example uses `location` and fails |
| S4 | `externalProperties` | property `$schema` | property `schema` (while `sarifLog` uses `$schema`) | |

S1 and S2 are the pattern of the talk in its purest form: a change accepted into one level, not into the other, with
nothing that would notice.

Related, smaller:

- Defaults stated only in the prose: `run.language` and `toolComponent.language` "SHALL default to `"en-US"`", the
  schema has no default for either.
  Several further defaults are conditional (`result.level`, `resultProvenance.invocationIndex`,
  `reportingDescriptorReference.id`/`index`): JSON Schema can express some of these (`if`/`then`), not all; they belong
  in constraint records (L2) that the prose and the tests are derived from.
- Enumerations otherwise agree: all 12 schema enums are listed completely in their property sections, apart from S2.

## Findings: headings that break the key

Four property headings cannot be found by their key (and their anchors depend on manual labels):

| File | Heading |
|---|---|
| `file-format-20-invocation-object.md` | `### arguments property` (no backticks) |
| `file-format-23-versioncontroldetails-object.md` | ``### revisionId` Property`` (opening backtick missing) |
| `file-format-24-artifact-object.md` | ``### `location property`` (closing backtick misplaced) |
| `file-format-27-result-object.md` | `### guid property` (no backticks) |

The rendered spec looks almost right; a tool that maps sections to schema properties does not.

## Findings: examples (L4)

### The snippets cannot be checked as they are

Of 127 JSON blocks in the prose, 8 parse as JSON.
The rest carry margin comments (`# An artifact object ((#artifact-object)).`), elisions, or both.
So no example in the prose has ever been validated where it stands; the twins are the first validatable form.

### What the twins show

The twins (recovered from the Word era) are already close to a derivable source: 25 are valid fragments, and 75 more
are valid apart from missing context (`tool`, `message`, `executionSuccessful`, `id` ...) and injection markers.
That context is exactly what the display wants to leave out and the validator needs, so it should be injected at
validation time, not typed into the display.

Injection markers in use: `...member-inject` 69, `...object-inject` 18, `...member-inkect` 5 (typo),
`member-inject` 1 (no dots), `member-insert` 1, `...string-inject` 1 (a third kind, as array element).
A marker grammar with a check would remove the typos and make the kinds explicit.

### Content errors: the illustration contradicts the shape

15 twins fail for reasons injection cannot fix. Grouped by cause:

| Cause | Twins | Note |
|---|---|---|
| `physicalLocation.uri` (pre-2.1 form; now `physicalLocation.artifactLocation.uri`) | message-object embedded links ex. 2, result `kind` ex. 1, result `level` ex. 1, result `relatedLocations` ex. 1 | the most frequent fossil |
| region line and column numbers as strings (`"6"`) | result `relatedLocations` ex. 1 | |
| `associatedRule.ruleId` (the property is `id`) | invocation `toolConfigurationNotifications` ex. 1 (and the comprehensive example's twin only, see correction below) | |
| `result.addresses` (addresses live in `run.addresses`; a result refers to them through locations) | the comprehensive example's twin only | see correction below |
| notification descriptors with `level` and string `messageStrings` | toolComponent `notifications` ex. 1 | level belongs in `defaultConfiguration`; message strings are objects |
| `reportingDescriptor.name` as an object | reportingConfiguration `parameters` ex. 1 | `name` is a string |
| `location.logicalLocation` (singular; the property is `logicalLocations`) | logicalLocation `kind` ex. 2, twin only | see correction below |
| `address` with `baseAddress` and `offset` | artifactContent `rendered` ex. 1 | neither exists in `address` |
| graph nodes with string labels and nested `nodes` | edgeTraversal `stepOverEdgeCount` ex. 1 | `label` is a message, children are `children` |
| replacements written as artifact changes | replacement general ex. 1 | either elided a level or nested wrongly; to decide |
| `attachment.location` | attachment general ex. 1 | follows S3 |
| marker typos | toolComponent `taxonomies` ex. 1 (`member-insert`), `supportedTaxonomies` ex. 1 (`...string-inject`) | |

Each is a finding for the TC in the sense of the talk: one example cell, one schema fact, and they disagree.

### The margin

83 JSON blocks carry section references in comments.
In a derived form these become keys on the twin (a JSON pointer and a section label per note), rendered into the
margin for the display and dropped for validation, so a renamed section or a moved property is a broken key, found by
the build, instead of a stale reference.

## Findings: statements (L3)

- Lexical waivers are rare: 4 statements with hedges ("as appropriate", "typically") and 3 with escape clauses
  ("unless", "to the extent that it is feasible").
  The fear of "wash your hands" wording is not confirmed by these markers.
- The pattern that does recur is structural: 22 sentences open with "Depending on the circumstances", 19 of them
  announce a set of keywords ("either **SHALL** or **MAY** contain") that later sentences resolve.
  Read alone, such a sentence binds nothing; the rule exists only as the sum of several sentences.
  These are presence rules (97, of which 87 conditional) and are the natural first candidates for constraint records:
  one record per rule, from which the sentence, a JSON Schema `if`/`then` where possible, and a test fixture per
  branch are derived.
- One normative lowercase "shall": `file-format-52-reportingdescriptorreference-object.md`
  ("`theComponent` shall be taken to be `theTool.driver`").
- Subjects: 645 of 996 statements are about the log file (an object or property is the subject), which implicitly
  binds the producer; 237 name a role; 114 have no subject the script could find.

### Roles, as named in statements

| Role | Statements |
|---|---|
| producer (incl. analysis tool, direct producer) | 122 |
| consumer | 53 |
| driver / extension (tool components; not a role in the conformance sense) | 24 |
| result management system | 24 |
| converter | 23 |
| viewer | 16 |
| engineering system | 7 |
| post-processor | 3 |

Enough to derive role views (what a producer, a consumer, a viewer, a converter must do) once each statement records
its subject; the 645 document-level statements go to the producer view by default and to the consumer view where they
constrain interpretation.

## Reading it in the talk's terms

- The schema (L1) is in good shape and the enums agree; the drift is where the prose was changed and the schema was
  not (S1, S2) and in names (S3, S4).
- The examples (L4) are the weakest level: unvalidated where they stand, with fossils from earlier drafts.
  The twins turn that around: they are the first form of the examples that a build can check.
- The normative statements (L3) are not hedged as feared; their problem is that many rules are spread over several
  sentences, and most say nothing about who acts.

## Suggested order for the transform

1. Report S1 to S4 and the content errors to the TC as findings (they are decisions, not edits).
2. Examples first: the twins become the source; a marker grammar replaces ad hoc markers; context is injected for
   validation and elided for display; margin notes are keys (JSON pointer + section label), not text.
   The snippets in the prose are then derived, and every one is validated in every build.
3. Heading keys: fix the four headings, then a check that every property heading maps to a schema property and back.
4. Presence rules as constraint records (start with the 19 "Depending on the circumstances" groups).
5. Subjects for statements, then role views.

## Correction (2026-11-07, vision step 3)

The example findings above were made on the twins. When every twin was compared with its prose snippet, three of
them turned out to be the twin's own drift, not the prose's: the comprehensive SARIF file in the prose is valid
against the schema (its twin had invented `associatedRule.ruleId` and `result.addresses`), and logicalLocation
`kind` example 2 uses `logicalLocations` in the prose. The twins now follow the prose. The other example findings
hold for the prose too: there the twin and the snippet say the same. See `VISION.md`, step 3.

