# Constraints

Derived by `bin/vision.py derive` from `records/constraints.yaml`; do not edit.

15 presence rules announced with a set of keywords, 44 branches: 8 object, 17 log, 15 world, 4 rest scope.
2 branches the schema can say are derived as `if`/`then` into `views/constraints.schema.json`, a proposal for the TC; against the twins and `example/` they find 1 violation(s).
Each rule has a fixture that keeps it and one that breaks it (`views/fixtures/`); both pass the schema as it is. They start from the smallest instance the schema allows, so an empty object in them (an `artifactLocation` without `uri` and `index`) is what the schema accepts, not what the prose asks for.

Below each table, the wording a sentence generated from the record would have: a proposal for the TC, until which the prose keeps its own sentences (derived verbatim from the records).

## `artifactLocation.uri`

file-format-04-artifactlocation-object.md; announced: **SHALL**, **SHALL NOT**, **MAY**

| | Presence | When | Scope | Schema |
|---|---|---|---|---|
| 1 | **MAY** | it is the value of a top-level property of `theRun.originalUriBaseIds` | log | MAY does not invalidate |
| 2 | **SHALL** | otherwise, `index` is absent | object | an earlier branch outside the object takes precedence |
| 3 | **SHALL NOT** | otherwise, it describes a nested artifact whose location within its parent can be expressed only by a byte offset | world | only the producer knows |
| 4 | **MAY** | otherwise, in all other cases | rest | MAY does not invalidate |

1. If it is the value of a top-level property of `theRun.originalUriBaseIds`, `uri` **MAY** be present.
2. Otherwise, if `index` is absent, `uri` **SHALL** be present.
3. Otherwise, if it describes a nested artifact whose location within its parent can be expressed only by a byte offset, `uri` **SHALL NOT** be present.
4. Otherwise, `uri` **MAY** be present.

## `artifactLocation.index`

file-format-04-artifactlocation-object.md; announced: **MAY**, **SHALL NOT**, **SHALL**, **SHOULD**

| | Presence | When | Scope | Schema |
|---|---|---|---|---|
| 1 | **MAY** | it is the `location` of an `artifact` object in `theRun.artifacts` | log | MAY does not invalidate |
| 2 | **SHALL NOT** | otherwise, `theRun.artifacts` is absent or has no element for the artifact | log | needs other parts of the log |
| 3 | **SHALL** | otherwise, `uri` is absent | object | an earlier branch outside the object takes precedence |
| 4 | **SHOULD** | otherwise, `uri` is present and `theRun.artifacts` has an element for the artifact | log | SHOULD does not invalidate |

1. If it is the `location` of an `artifact` object in `theRun.artifacts`, `index` **MAY** be present.
2. Otherwise, if `theRun.artifacts` is absent or has no element for the artifact, `index` **SHALL NOT** be present.
3. Otherwise, if `uri` is absent, `index` **SHALL** be present.
4. Otherwise, if `uri` is present and `theRun.artifacts` has an element for the artifact, `index` **SHOULD** be present.

## `run.results`

file-format-14-run-object.md; announced: **SHALL**, **MAY**

| | Presence | When | Scope | Schema |
|---|---|---|---|---|
| 1 | **MAY** | the tool failed to start and the engineering system synthesized the log file | world | MAY does not invalidate |
| 2 | **MAY** | the tool started but failed to begin its analysis | world | MAY does not invalidate |
| 3 | **SHALL** | otherwise, in all other circumstances | rest | follows from the other branches |

1. If the tool failed to start and the engineering system synthesized the log file, `results` **MAY** be present.
2. If the tool started but failed to begin its analysis, `results` **MAY** be present.
3. Otherwise, `results` **SHALL** be present.

## `externalPropertyFileReference.location`

file-format-16-externalpropertyfilereference-object.md; announced: **SHALL**, **MAY**

| | Presence | When | Scope | Schema |
|---|---|---|---|---|
| 1 | **SHALL** | the externalized properties are persisted in a separate file | log | needs other parts of the log |
| 2 | **MAY** | otherwise, the externalized properties are an element of `theSarifLog.inlineExternalProperties` | log | MAY does not invalidate |

1. If the externalized properties are persisted in a separate file, `location` **SHALL** be present.
2. Otherwise, if the externalized properties are an element of `theSarifLog.inlineExternalProperties`, `location` **MAY** be present.

## `externalPropertyFileReference.guid`

file-format-16-externalpropertyfilereference-object.md; announced: **SHALL**, **MAY**

| | Presence | When | Scope | Schema |
|---|---|---|---|---|
| 1 | **SHALL** | the externalized properties are an element of `theSarifLog.inlineExternalProperties` and `location` is absent | log | needs other parts of the log |
| 2 | **MAY** | otherwise, in all other cases (a separate file, or inline with location present) | rest | MAY does not invalidate |

1. If the externalized properties are an element of `theSarifLog.inlineExternalProperties` and `location` is absent, `guid` **SHALL** be present.
2. Otherwise, `guid` **MAY** be present.

## `toolComponent.language`

file-format-19-toolcomponent-object.md; announced: **SHALL**, **MAY**

| | Presence | When | Scope | Schema |
|---|---|---|---|---|
| 1 | **SHALL** | it represents a translation (an element of `theRun.translations`) | log | needs other parts of the log |
| 2 | **MAY** | otherwise, in all other cases | rest | MAY does not invalidate |

1. If it represents a translation (an element of `theRun.translations`), `language` **SHALL** be present.
2. Otherwise, `language` **MAY** be present.

## `artifact.location`

file-format-24-artifact-object.md; announced: **SHALL**, **MAY**, **SHALL NOT**

| | Presence | When | Scope | Schema |
|---|---|---|---|---|
| 1 | **SHALL** | it represents a top-level artifact (`parentIndex` absent) | object | if/then |
| 2 | **SHALL** | it represents a nested artifact whose location can be expressed only by a path | world | only the producer knows |
| 3 | **SHALL NOT** | it represents a nested artifact whose location can be expressed only by a byte offset | world | only the producer knows |
| 4 | **MAY** | it represents a nested artifact whose location can be expressed either way | world | MAY does not invalidate |

1. If it represents a top-level artifact (`parentIndex` absent), `location` **SHALL** be present.
2. If it represents a nested artifact whose location can be expressed only by a path, `location` **SHALL** be present.
3. If it represents a nested artifact whose location can be expressed only by a byte offset, `location` **SHALL NOT** be present.
4. If it represents a nested artifact whose location can be expressed either way, `location` **MAY** be present.

## `artifact.offset`

file-format-24-artifact-object.md; announced: **SHALL**, **MAY**, **SHALL NOT**

| | Presence | When | Scope | Schema |
|---|---|---|---|---|
| 1 | **SHALL NOT** | it represents a top-level artifact (`parentIndex` absent) | object | if/then |
| 2 | **SHALL** | it represents a nested artifact whose location can be expressed only by a byte offset | world | only the producer knows |
| 3 | **SHALL NOT** | it represents a nested artifact whose location can be expressed only by a path | world | only the producer knows |
| 4 | **MAY** | it represents a nested artifact whose location can be expressed either way | world | MAY does not invalidate |

1. If it represents a top-level artifact (`parentIndex` absent), `offset` **SHALL NOT** be present.
2. If it represents a nested artifact whose location can be expressed only by a byte offset, `offset` **SHALL** be present.
3. If it represents a nested artifact whose location can be expressed only by a path, `offset` **SHALL NOT** be present.
4. If it represents a nested artifact whose location can be expressed either way, `offset` **MAY** be present.

## `result.ruleId`

file-format-27-result-object.md; announced: **SHALL**, **MAY**, **SHALL NOT**

| | Presence | When | Scope | Schema |
|---|---|---|---|---|
| 1 | **SHALL** | `rule.id` is absent | object | binds direct producers, not the log file |
| 2 | **MAY** | `rule.id` is present | object | MAY does not invalidate |

1. If `rule.id` is absent, `ruleId` **SHALL** be present.
2. If `rule.id` is present, `ruleId` **MAY** be present.

## `result.rule`

file-format-27-result-object.md; announced: **SHALL NOT**, **SHOULD**, **MAY**

| | Presence | When | Scope | Schema |
|---|---|---|---|---|
| 1 | **SHALL NOT** | `theTool` has no `reportingDescriptor` for the rule | log | needs other parts of the log |
| 2 | **SHOULD** | `theDescriptor` is in `theTool.extensions` | log | SHOULD does not invalidate |
| 3 | **SHOULD** | `theDescriptor` is in `theTool.driver` and `ruleIndex` is absent | log | SHOULD does not invalidate |
| 4 | **MAY** | `theDescriptor` is in `theTool.driver` and `ruleIndex` is present | log | MAY does not invalidate |

1. If `theTool` has no `reportingDescriptor` for the rule, `rule` **SHALL NOT** be present.
2. If `theDescriptor` is in `theTool.extensions`, `rule` **SHOULD** be present.
3. If `theDescriptor` is in `theTool.driver` and `ruleIndex` is absent, `rule` **SHOULD** be present.
4. If `theDescriptor` is in `theTool.driver` and `ruleIndex` is present, `rule` **MAY** be present.

## `location.physicalLocation`

file-format-28-location-object.md; announced: **SHALL**, **MAY**, **SHALL NOT**

| | Presence | When | Scope | Schema |
|---|---|---|---|---|
| 1 | **SHALL** | physical location information is available and `logicalLocations` is absent or empty | world | only the producer knows |
| 2 | **MAY** | physical location information is available and `logicalLocations` is non-empty | world | MAY does not invalidate |
| 3 | **SHALL NOT** | physical location information is not available | world | only the producer knows |

1. If physical location information is available and `logicalLocations` is absent or empty, `physicalLocation` **SHALL** be present.
2. If physical location information is available and `logicalLocations` is non-empty, `physicalLocation` **MAY** be present.
3. If physical location information is not available, `physicalLocation` **SHALL NOT** be present.

## `location.logicalLocations`

file-format-28-location-object.md; announced: **SHALL**, **MAY**, **SHALL NOT**

| | Presence | When | Scope | Schema |
|---|---|---|---|---|
| 1 | **SHALL** | logical location information is available and `physicalLocation` is absent | world | only the producer knows |
| 2 | **MAY** | logical location information is available and `physicalLocation` is present | world | MAY does not invalidate |
| 3 | **SHALL NOT** | logical location information is not available | world | only the producer knows |

1. If logical location information is available and `physicalLocation` is absent, `logicalLocations` **SHALL** be present.
2. If logical location information is available and `physicalLocation` is present, `logicalLocations` **MAY** be present.
3. If logical location information is not available, `logicalLocations` **SHALL NOT** be present.

## `logicalLocation.fullyQualifiedName`

file-format-33-logicallocation-object.md; announced: **SHOULD**, **MAY**

| | Presence | When | Scope | Schema |
|---|---|---|---|---|
| 1 | **MAY** | it represents a top-level logical location (`parentIndex` absent) | object | MAY does not invalidate |
| 2 | **SHOULD** | it represents a nested logical location (`parentIndex` present) | object | SHOULD does not invalidate |

1. If it represents a top-level logical location (`parentIndex` absent), `fullyQualifiedName` **MAY** be present.
2. If it represents a nested logical location (`parentIndex` present), `fullyQualifiedName` **SHOULD** be present.

## `threadFlowLocation.index`

file-format-38-threadflowlocation-object.md; announced: **MAY**, **SHALL NOT**, **SHALL**

| | Presence | When | Scope | Schema |
|---|---|---|---|---|
| 1 | **MAY** | it is an element of `theRun.threadFlowLocations` | log | MAY does not invalidate |
| 2 | **SHALL NOT** | otherwise, `theRun.threadFlowLocations` is absent or has no cached object for it | log | needs other parts of the log |
| 3 | **SHALL** | otherwise, it belongs to a result and `theRun.threadFlowLocations` has a cached object for it | log | needs other parts of the log |

1. If it is an element of `theRun.threadFlowLocations`, `index` **MAY** be present.
2. Otherwise, if `theRun.threadFlowLocations` is absent or has no cached object for it, `index` **SHALL NOT** be present.
3. Otherwise, if it belongs to a result and `theRun.threadFlowLocations` has a cached object for it, `index` **SHALL** be present.

## `externalProperties.version`

external-property-file-format.md; announced: **SHALL**, **MAY**

| | Presence | When | Scope | Schema |
|---|---|---|---|---|
| 1 | **SHALL** | it is the root of an external property file | log | needs other parts of the log |
| 2 | **MAY** | otherwise, it is an element of `theSarifLog.inlineExternalProperties` | log | MAY does not invalidate |

1. If it is the root of an external property file, `version` **SHALL** be present.
2. Otherwise, if it is an element of `theSarifLog.inlineExternalProperties`, `version` **MAY** be present.
