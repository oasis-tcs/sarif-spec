# Constraints

Derived by `bin/vision.py derive` from `records/constraints.yaml`; do not edit.

15 presence rules announced with a set of keywords, 44 branches: 8 object, 17 log, 15 world, 4 rest scope.
2 branches the schema can say are derived as `if`/`then` into `views/constraints.schema.json`, a proposal for the TC; against the twins and `example/` they find 1 violation(s).

## `artifactLocation.uri`

file-format-04-artifactlocation-object.md; announced: **SHALL**, **SHALL NOT**, **MAY**

| | Presence | When | Scope | Schema |
|---|---|---|---|---|
| 1 | **MAY** | it is the value of a top-level property of theRun.originalUriBaseIds | log | MAY does not invalidate |
| 2 | **SHALL** | otherwise, index is absent | object | an earlier branch outside the object takes precedence |
| 3 | **SHALL NOT** | otherwise, it describes a nested artifact whose location within its parent can be expressed only by a byte offset | world | only the producer knows |
| 4 | **MAY** | otherwise, in all other cases | rest | MAY does not invalidate |

## `artifactLocation.index`

file-format-04-artifactlocation-object.md; announced: **MAY**, **SHALL NOT**, **SHALL**, **SHOULD**

| | Presence | When | Scope | Schema |
|---|---|---|---|---|
| 1 | **MAY** | it is the location of an artifact object in theRun.artifacts | log | MAY does not invalidate |
| 2 | **SHALL NOT** | otherwise, theRun.artifacts is absent or has no element for the artifact | log | needs other parts of the log |
| 3 | **SHALL** | otherwise, uri is absent | object | an earlier branch outside the object takes precedence |
| 4 | **SHOULD** | otherwise, uri is present and theRun.artifacts has an element for the artifact | log | SHOULD does not invalidate |

## `run.results`

file-format-14-run-object.md; announced: **SHALL**, **MAY**

| | Presence | When | Scope | Schema |
|---|---|---|---|---|
| 1 | **MAY** | the tool failed to start and the engineering system synthesized the log file | world | MAY does not invalidate |
| 2 | **MAY** | the tool started but failed to begin its analysis | world | MAY does not invalidate |
| 3 | **SHALL** | otherwise, in all other circumstances | rest | follows from the other branches |

## `externalPropertyFileReference.location`

file-format-16-externalpropertyfilereference-object.md; announced: **SHALL**, **MAY**

| | Presence | When | Scope | Schema |
|---|---|---|---|---|
| 1 | **SHALL** | the externalized properties are persisted in a separate file | log | needs other parts of the log |
| 2 | **MAY** | otherwise, the externalized properties are an element of theSarifLog.inlineExternalProperties | log | MAY does not invalidate |

## `externalPropertyFileReference.guid`

file-format-16-externalpropertyfilereference-object.md; announced: **SHALL**, **MAY**

| | Presence | When | Scope | Schema |
|---|---|---|---|---|
| 1 | **SHALL** | the externalized properties are an element of theSarifLog.inlineExternalProperties and location is absent | log | needs other parts of the log |
| 2 | **MAY** | otherwise, in all other cases (a separate file, or inline with location present) | rest | MAY does not invalidate |

## `toolComponent.language`

file-format-19-toolcomponent-object.md; announced: **SHALL**, **MAY**

| | Presence | When | Scope | Schema |
|---|---|---|---|---|
| 1 | **SHALL** | it represents a translation (an element of theRun.translations) | log | needs other parts of the log |
| 2 | **MAY** | otherwise, in all other cases | rest | MAY does not invalidate |

## `artifact.location`

file-format-24-artifact-object.md; announced: **SHALL**, **MAY**, **SHALL NOT**

| | Presence | When | Scope | Schema |
|---|---|---|---|---|
| 1 | **SHALL** | it represents a top-level artifact (parentIndex absent) | object | if/then |
| 2 | **SHALL** | it represents a nested artifact whose location can be expressed only by a path | world | only the producer knows |
| 3 | **SHALL NOT** | it represents a nested artifact whose location can be expressed only by a byte offset | world | only the producer knows |
| 4 | **MAY** | it represents a nested artifact whose location can be expressed either way | world | MAY does not invalidate |

## `artifact.offset`

file-format-24-artifact-object.md; announced: **SHALL**, **MAY**, **SHALL NOT**

| | Presence | When | Scope | Schema |
|---|---|---|---|---|
| 1 | **SHALL NOT** | it represents a top-level artifact (parentIndex absent) | object | if/then |
| 2 | **SHALL** | it represents a nested artifact whose location can be expressed only by a byte offset | world | only the producer knows |
| 3 | **SHALL NOT** | it represents a nested artifact whose location can be expressed only by a path | world | only the producer knows |
| 4 | **MAY** | it represents a nested artifact whose location can be expressed either way | world | MAY does not invalidate |

## `result.ruleId`

file-format-27-result-object.md; announced: **SHALL**, **MAY**, **SHALL NOT**

| | Presence | When | Scope | Schema |
|---|---|---|---|---|
| 1 | **SHALL** | rule.id is absent | object | binds direct producers, not the log file |
| 2 | **MAY** | rule.id is present | object | MAY does not invalidate |

## `result.rule`

file-format-27-result-object.md; announced: **SHALL NOT**, **SHOULD**, **MAY**

| | Presence | When | Scope | Schema |
|---|---|---|---|---|
| 1 | **SHALL NOT** | theTool has no reportingDescriptor for the rule | log | needs other parts of the log |
| 2 | **SHOULD** | the descriptor is in theTool.extensions | log | SHOULD does not invalidate |
| 3 | **SHOULD** | the descriptor is in theTool.driver and ruleIndex is absent | log | SHOULD does not invalidate |
| 4 | **MAY** | the descriptor is in theTool.driver and ruleIndex is present | log | MAY does not invalidate |

## `location.physicalLocation`

file-format-28-location-object.md; announced: **SHALL**, **MAY**, **SHALL NOT**

| | Presence | When | Scope | Schema |
|---|---|---|---|---|
| 1 | **SHALL** | physical location information is available and logicalLocations is absent or empty | world | only the producer knows |
| 2 | **MAY** | physical location information is available and logicalLocations is non-empty | world | MAY does not invalidate |
| 3 | **SHALL NOT** | physical location information is not available | world | only the producer knows |

## `location.logicalLocations`

file-format-28-location-object.md; announced: **SHALL**, **MAY**, **SHALL NOT**

| | Presence | When | Scope | Schema |
|---|---|---|---|---|
| 1 | **SHALL** | logical location information is available and physicalLocation is absent | world | only the producer knows |
| 2 | **MAY** | logical location information is available and physicalLocation is present | world | MAY does not invalidate |
| 3 | **SHALL NOT** | logical location information is not available | world | only the producer knows |

## `logicalLocation.fullyQualifiedName`

file-format-33-logicallocation-object.md; announced: **SHOULD**, **MAY**

| | Presence | When | Scope | Schema |
|---|---|---|---|---|
| 1 | **MAY** | it represents a top-level logical location (parentIndex absent) | object | MAY does not invalidate |
| 2 | **SHOULD** | it represents a nested logical location (parentIndex present) | object | SHOULD does not invalidate |

## `threadFlowLocation.index`

file-format-38-threadflowlocation-object.md; announced: **MAY**, **SHALL NOT**, **SHALL**

| | Presence | When | Scope | Schema |
|---|---|---|---|---|
| 1 | **MAY** | it is an element of theRun.threadFlowLocations | log | MAY does not invalidate |
| 2 | **SHALL NOT** | otherwise, theRun.threadFlowLocations is absent or has no cached object for it | log | needs other parts of the log |
| 3 | **SHALL** | otherwise, it belongs to a result and theRun.threadFlowLocations has a cached object for it | log | needs other parts of the log |

## `externalProperties.version`

external-property-file-format.md; announced: **SHALL**, **MAY**

| | Presence | When | Scope | Schema |
|---|---|---|---|---|
| 1 | **SHALL** | it is the root of an external property file | log | needs other parts of the log |
| 2 | **MAY** | otherwise, it is an element of theSarifLog.inlineExternalProperties | log | MAY does not invalidate |
