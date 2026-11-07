# Constraints

Derived by `bin/vision.py derive` from `records/constraints.yaml`; do not edit.

79 presence rules (19 announced with a set of keywords, 60 with conditional claims only), 163 branches: 17 object, 52 log, 73 world, 21 rest scope.
9 branches the schema can say; 2 it says already (`physicalLocation.address`, `physicalLocation.artifactLocation`), 7 are derived as `if`/`then` into `views/constraints.schema.json`, a proposal for the TC; against the twins and `example/` they find 11 violation(s).
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

## `address.index`

file-format-32-address-object.md; announced: **MAY**, **SHALL NOT**, **SHALL**

| | Presence | When | Scope | Schema |
|---|---|---|---|---|
| 1 | **MAY** | it is an element of `theRun.addresses` | log | MAY does not invalidate |
| 2 | **SHALL NOT** | otherwise, `theRun.addresses` is absent or has no cached object for it | log | needs other parts of the log |
| 3 | **SHALL** | otherwise, it belongs to a result and `theRun.addresses` has a cached object for it | log | needs other parts of the log |

1. If it is an element of `theRun.addresses`, `index` **MAY** be present.
2. Otherwise, if `theRun.addresses` is absent or has no cached object for it, `index` **SHALL NOT** be present.
3. Otherwise, if it belongs to a result and `theRun.addresses` has a cached object for it, `index` **SHALL** be present.

## `logicalLocation.index`

file-format-33-logicallocation-object.md; announced: **MAY**, **SHALL NOT**, **SHALL**

| | Presence | When | Scope | Schema |
|---|---|---|---|---|
| 1 | **MAY** | it is an element of `theRun.logicalLocations` | log | MAY does not invalidate |
| 2 | **SHALL NOT** | otherwise, `theRun.logicalLocations` is absent or has no cached object for it | log | needs other parts of the log |
| 3 | **SHALL** | otherwise, it belongs to a result and `theRun.logicalLocations` has a cached object for it | log | needs other parts of the log |

1. If it is an element of `theRun.logicalLocations`, `index` **MAY** be present.
2. Otherwise, if `theRun.logicalLocations` is absent or has no cached object for it, `index` **SHALL NOT** be present.
3. Otherwise, if it belongs to a result and `theRun.logicalLocations` has a cached object for it, `index` **SHALL** be present.

## `webRequest.index`

file-format-46-webrequest-object.md; announced: **MAY**, **SHALL NOT**, **SHALL**

| | Presence | When | Scope | Schema |
|---|---|---|---|---|
| 1 | **MAY** | it is an element of `theRun.webRequests` | log | MAY does not invalidate |
| 2 | **SHALL NOT** | otherwise, `theRun.webRequests` is absent or has no cached object for it | log | needs other parts of the log |
| 3 | **SHALL** | otherwise, it belongs to a result and `theRun.webRequests` has a cached object for it | log | needs other parts of the log |

1. If it is an element of `theRun.webRequests`, `index` **MAY** be present.
2. Otherwise, if `theRun.webRequests` is absent or has no cached object for it, `index` **SHALL NOT** be present.
3. Otherwise, if it belongs to a result and `theRun.webRequests` has a cached object for it, `index` **SHALL** be present.

## `webResponse.index`

file-format-47-webresponse-object.md; announced: **MAY**, **SHALL NOT**, **SHALL**

| | Presence | When | Scope | Schema |
|---|---|---|---|---|
| 1 | **MAY** | it is an element of `theRun.webResponses` | log | MAY does not invalidate |
| 2 | **SHALL NOT** | otherwise, `theRun.webResponses` is absent or has no cached object for it | log | needs other parts of the log |
| 3 | **SHALL** | otherwise, it belongs to a result and `theRun.webResponses` has a cached object for it | log | needs other parts of the log |

1. If it is an element of `theRun.webResponses`, `index` **MAY** be present.
2. Otherwise, if `theRun.webResponses` is absent or has no cached object for it, `index` **SHALL NOT** be present.
3. Otherwise, if it belongs to a result and `theRun.webResponses` has a cached object for it, `index` **SHALL** be present.

## `artifactContent.text`

file-format-03-artifactcontent-object.md; announced: 

| | Presence | When | Scope | Schema |
|---|---|---|---|---|
| 1 | **SHOULD** | the external artifact is a text artifact | world | SHOULD does not invalidate |
| 2 | **SHALL NOT** | the external artifact is a binary artifact | world | only the producer knows |

1. If the external artifact is a text artifact, `text` **SHOULD** be present.
2. If the external artifact is a binary artifact, `text` **SHALL NOT** be present.

## `artifactContent.binary`

file-format-03-artifactcontent-object.md; announced: 

| | Presence | When | Scope | Schema |
|---|---|---|---|---|
| 1 | **SHALL** | the external artifact is a binary artifact, or if the SARIF producer cannot determine whether the external artifact is a text artifact or a binary artifact | world | only the producer knows |
| 2 | **MAY** | the external artifact is a text artifact in an encoding other than UTF-8 | world | MAY does not invalidate |
| 3 | **SHOULD NOT** | the external artifact is a UTF-8 text artifact | world | SHOULD NOT does not invalidate |

1. If the external artifact is a binary artifact, or if the SARIF producer cannot determine whether the external artifact is a text artifact or a binary artifact, `binary` **SHALL** be present.
2. If the external artifact is a text artifact in an encoding other than UTF-8, `binary` **MAY** be present.
3. If the external artifact is a UTF-8 text artifact, `binary` **SHOULD NOT** be present.

## `artifactLocation.uriBaseId`

file-format-04-artifactlocation-object.md; announced: 

| | Presence | When | Scope | Schema |
|---|---|---|---|---|
| 1 | **SHOULD** | this `artifactLocation` object describes a top-level artifact and the value of its `uri` property ([sec](#uri-property)) is a relative reference | world | SHOULD does not invalidate |
| 2 | **SHALL NOT** | the `uri` property contains an absolute URI | object | if/then |
| 3 | **SHALL NOT** | this `artifactLocation` object describes a nested artifact | world | only the producer knows |

1. If this `artifactLocation` object describes a top-level artifact and the value of its `uri` property ([sec](#uri-property)) is a relative reference, `uriBaseId` **SHOULD** be present.
2. If the `uri` property contains an absolute URI, `uriBaseId` **SHALL NOT** be present.
3. If this `artifactLocation` object describes a nested artifact, `uriBaseId` **SHALL NOT** be present.

## `message.arguments`

file-format-11-message-object.md; announced: 

| | Presence | When | Scope | Schema |
|---|---|---|---|---|
| 1 | **SHALL** | a message string given by `text`, `markdown` or `id` (looked up elsewhere in the log) contains placeholders | log | needs other parts of the log |
| 2 | **MAY** | none of the message strings given by `text`, `markdown` or `id` contains placeholders | log | MAY does not invalidate |

1. If a message string given by `text`, `markdown` or `id` (looked up elsewhere in the log) contains placeholders, `arguments` **SHALL** be present.
2. If none of the message strings given by `text`, `markdown` or `id` contains placeholders, `arguments` **MAY** be present.

## `run.conversion`

file-format-14-run-object.md; announced: 

| | Presence | When | Scope | Schema |
|---|---|---|---|---|
| 1 | **MAY** | a `run` object was produced by a converter | world | MAY does not invalidate |

1. If a `run` object was produced by a converter, `conversion` **MAY** be present.

## `run.originalUriBaseIds`

file-format-14-run-object.md; announced: 

| | Presence | When | Scope | Schema |
|---|---|---|---|---|
| 1 | **MAY** | always | rest | MAY does not invalidate |
| 2 | **SHALL** | the `uri` of an `artifactLocation` value is a relative reference | log | needs other parts of the log |
| 3 | **SHALL NOT** | otherwise, the `uri` of an `artifactLocation` value is absolute or absent | log | needs other parts of the log |

1. Otherwise, `originalUriBaseIds` **MAY** be present.
2. If the `uri` of an `artifactLocation` value is a relative reference, `originalUriBaseIds` **SHALL** be present.
3. Otherwise, if the `uri` of an `artifactLocation` value is absolute or absent, `originalUriBaseIds` **SHALL NOT** be present.

## `run.columnKind`

file-format-14-run-object.md; announced: 

| | Presence | When | Scope | Schema |
|---|---|---|---|---|
| 1 | **SHALL** | a SARIF producer processes text artifacts and `theRun.results` ([sec](#results-property)) is non-empty | log | needs other parts of the log |
| 2 | **MAY** | a SARIF producer processes text artifacts and `theRun.results` is empty | log | MAY does not invalidate |
| 3 | **SHALL NOT** | the SARIF producer does not process text artifacts | world | only the producer knows |

1. If a SARIF producer processes text artifacts and `theRun.results` ([sec](#results-property)) is non-empty, `columnKind` **SHALL** be present.
2. If a SARIF producer processes text artifacts and `theRun.results` is empty, `columnKind` **MAY** be present.
3. If the SARIF producer does not process text artifacts, `columnKind` **SHALL NOT** be present.

## `run.redactionTokens`

file-format-14-run-object.md; announced: 

| | Presence | When | Scope | Schema |
|---|---|---|---|---|
| 1 | **SHALL** | the value of any redactable property ([sec](#redactable-strings)) in `theRun` has been redacted | log | needs other parts of the log |
| 2 | **SHALL NOT** | no text in `theRun` has been redacted | log | needs other parts of the log |

1. If the value of any redactable property ([sec](#redactable-strings)) in `theRun` has been redacted, `redactionTokens` **SHALL** be present.
2. If no text in `theRun` has been redacted, `redactionTokens` **SHALL NOT** be present.

## `externalPropertyFileReference.itemCount`

file-format-16-externalpropertyfilereference-object.md; announced: 

| | Presence | When | Scope | Schema |
|---|---|---|---|---|
| 1 | **MAY** | an `externalPropertyFileReference` object specifies an external property file that contains all or a portion of an array-valued property | world | MAY does not invalidate |
| 2 | **SHALL NOT** | the `externalPropertyFileReference` object specifies an external property file that contains an object-valued property | world | only the producer knows |

1. If an `externalPropertyFileReference` object specifies an external property file that contains all or a portion of an array-valued property, `itemCount` **MAY** be present.
2. If the `externalPropertyFileReference` object specifies an external property file that contains an object-valued property, `itemCount` **SHALL NOT** be present.

## `tool.extensions`

file-format-18-tool-object.md; announced: 

| | Presence | When | Scope | Schema |
|---|---|---|---|---|
| 1 | **SHOULD** | the tool used any extensions during the run | world | SHOULD does not invalidate |

1. If the tool used any extensions during the run, `extensions` **SHOULD** be present.

## `toolComponent.dottedQuadFileVersion`

file-format-19-toolcomponent-object.md; announced: 

| | Presence | When | Scope | Schema |
|---|---|---|---|---|
| 1 | **MAY** | the operating system on which the tool runs provides a value for the file version of the tool component's primary executable file, and if that value logically consists of an ordered set of four non-negative integers | world | MAY does not invalidate |
| 2 | **SHALL NOT** | the operating system does not provide such a value | world | only the producer knows |

1. If the operating system on which the tool runs provides a value for the file version of the tool component's primary executable file, and if that value logically consists of an ordered set of four non-negative integers, `dottedQuadFileVersion` **MAY** be present.
2. If the operating system does not provide such a value, `dottedQuadFileVersion` **SHALL NOT** be present.

## `toolComponent.translationMetadata`

file-format-19-toolcomponent-object.md; announced: 

| | Presence | When | Scope | Schema |
|---|---|---|---|---|
| 1 | **SHALL** | it represents a translation (an element of `theRun.translations`) | log | needs other parts of the log |
| 2 | **SHALL NOT** | otherwise, in all other cases | rest | follows from the other branches |

1. If it represents a translation (an element of `theRun.translations`), `translationMetadata` **SHALL** be present.
2. Otherwise, `translationMetadata` **SHALL NOT** be present.

## `toolComponent.localizedDataSemanticVersion`

file-format-19-toolcomponent-object.md; announced: 

| | Presence | When | Scope | Schema |
|---|---|---|---|---|
| 1 | **SHOULD** | it represents a translation (an element of `theRun.translations`) | log | SHOULD does not invalidate |
| 2 | **MAY** | otherwise, in all other cases | rest | MAY does not invalidate |

1. If it represents a translation (an element of `theRun.translations`), `localizedDataSemanticVersion` **SHOULD** be present.
2. Otherwise, `localizedDataSemanticVersion` **MAY** be present.

## `toolComponent.minimumRequiredLocalizedDataSemanticVersion`

file-format-19-toolcomponent-object.md; announced: 

| | Presence | When | Scope | Schema |
|---|---|---|---|---|
| 1 | **SHOULD** | it does not represent a translation (no element of `theRun.translations`) | log | SHOULD does not invalidate |
| 2 | **SHALL NOT** | otherwise, in all other cases | rest | follows from the other branches |

1. If it does not represent a translation (no element of `theRun.translations`), `minimumRequiredLocalizedDataSemanticVersion` **SHOULD** be present.
2. Otherwise, `minimumRequiredLocalizedDataSemanticVersion` **SHALL NOT** be present.

## `toolComponent.associatedComponent`

file-format-19-toolcomponent-object.md; announced: 

| | Presence | When | Scope | Schema |
|---|---|---|---|---|
| 1 | **MAY** | this `toolComponent` object represents a plugin (see [sec](#tool-object--general)) | world | MAY does not invalidate |

1. If this `toolComponent` object represents a plugin (see [sec](#tool-object--general)), `associatedComponent` **MAY** be present.

## `invocation.exitCode`

file-format-20-invocation-object.md; announced: 

| | Presence | When | Scope | Schema |
|---|---|---|---|---|
| 1 | **SHOULD** | the SARIF producer process did not exit due to a signal | world | SHOULD does not invalidate |
| 2 | **SHALL NOT** | the SARIF producer process exited due to a signal | world | only the producer knows |

1. If the SARIF producer process did not exit due to a signal, `exitCode` **SHOULD** be present.
2. If the SARIF producer process exited due to a signal, `exitCode` **SHALL NOT** be present.

## `invocation.exitCodeDescription`

file-format-20-invocation-object.md; announced: 

| | Presence | When | Scope | Schema |
|---|---|---|---|---|
| 1 | **MAY** | the SARIF producer process did not exit due to a signal | world | MAY does not invalidate |

1. If the SARIF producer process did not exit due to a signal, `exitCodeDescription` **MAY** be present.

## `invocation.exitSignalName`

file-format-20-invocation-object.md; announced: 

| | Presence | When | Scope | Schema |
|---|---|---|---|---|
| 1 | **SHOULD** | the SARIF producer process exited due to a signal | world | SHOULD does not invalidate |
| 2 | **SHALL NOT** | the SARIF producer process did not exit due to a signal | world | only the producer knows |

1. If the SARIF producer process exited due to a signal, `exitSignalName` **SHOULD** be present.
2. If the SARIF producer process did not exit due to a signal, `exitSignalName` **SHALL NOT** be present.

## `invocation.exitSignalNumber`

file-format-20-invocation-object.md; announced: 

| | Presence | When | Scope | Schema |
|---|---|---|---|---|
| 1 | **MAY** | the SARIF producer process exited due to a signal | world | MAY does not invalidate |
| 2 | **SHALL NOT** | the SARIF producer process did not exit due to a signal | world | only the producer knows |

1. If the SARIF producer process exited due to a signal, `exitSignalNumber` **MAY** be present.
2. If the SARIF producer process did not exit due to a signal, `exitSignalNumber` **SHALL NOT** be present.

## `invocation.processStartFailureMessage`

file-format-20-invocation-object.md; announced: 

| | Presence | When | Scope | Schema |
|---|---|---|---|---|
| 1 | **MAY** | the analysis tool process failed to start | world | MAY does not invalidate |
| 2 | **SHALL NOT** | the analysis tool process started successfully (regardless of whether or how it subsequently failed) | world | only the producer knows |

1. If the analysis tool process failed to start, `processStartFailureMessage` **MAY** be present.
2. If the analysis tool process started successfully (regardless of whether or how it subsequently failed), `processStartFailureMessage` **SHALL NOT** be present.

## `artifact.parentIndex`

file-format-24-artifact-object.md; announced: 

| | Presence | When | Scope | Schema |
|---|---|---|---|---|
| 1 | **SHALL** | this `artifact` object represents a nested artifact | world | only the producer knows |
| 2 | **SHALL NOT** | this `artifact` object represents a top-level artifact | world | only the producer knows |

1. If this `artifact` object represents a nested artifact, `parentIndex` **SHALL** be present.
2. If this `artifact` object represents a top-level artifact, `parentIndex` **SHALL NOT** be present.

## `artifact.encoding`

file-format-24-artifact-object.md; announced: 

| | Presence | When | Scope | Schema |
|---|---|---|---|---|
| 1 | **MAY** | an `artifact` object represents a text artifact | world | MAY does not invalidate |
| 2 | **SHALL NOT** | the `artifact` object represents a binary artifact | world | only the producer knows |

1. If an `artifact` object represents a text artifact, `encoding` **MAY** be present.
2. If the `artifact` object represents a binary artifact, `encoding` **SHALL NOT** be present.

## `result.ruleIndex`

file-format-27-result-object.md; announced: 

| | Presence | When | Scope | Schema |
|---|---|---|---|---|
| 1 | **MAY** | `theDescriptor` exists (that is, if `theTool` contains a `reportingDescriptor` object ([sec](#reportingdescriptor-object)) that describes the rule that was violated) | log | MAY does not invalidate |
| 2 | **SHALL NOT** | otherwise, in all other cases | rest | follows from the other branches |

1. If `theDescriptor` exists (that is, if `theTool` contains a `reportingDescriptor` object ([sec](#reportingdescriptor-object)) that describes the rule that was violated), `ruleIndex` **MAY** be present.
2. Otherwise, `ruleIndex` **SHALL NOT** be present.

## `result.analysisTarget`

file-format-27-result-object.md; announced: 

| | Presence | When | Scope | Schema |
|---|---|---|---|---|
| 1 | **SHOULD** | the analysis target differs from the result file | world | SHOULD does not invalidate |
| 2 | **SHOULD NOT** | the analysis target and the result file are the same | world | SHOULD NOT does not invalidate |

1. If the analysis target differs from the result file, `analysisTarget` **SHOULD** be present.
2. If the analysis target and the result file are the same, `analysisTarget` **SHOULD NOT** be present.

## `result.graphTraversals`

file-format-27-result-object.md; announced: 

| | Presence | When | Scope | Schema |
|---|---|---|---|---|
| 1 | **MAY** | a `result` object contains a `graphs` property ([sec](#result-object--graphs-property)), or if `theRun` contains a `graphs` property ([sec](#run-object--graphs-property)) | log | MAY does not invalidate |
| 2 | **SHALL NOT** | neither the `result` object nor `theRun` contains a `graphs` property | log | needs other parts of the log |

1. If a `result` object contains a `graphs` property ([sec](#result-object--graphs-property)), or if `theRun` contains a `graphs` property ([sec](#run-object--graphs-property)), `graphTraversals` **MAY** be present.
2. If neither the `result` object nor `theRun` contains a `graphs` property, `graphTraversals` **SHALL NOT** be present.

## `result.baselineState`

file-format-27-result-object.md; announced: 

| | Presence | When | Scope | Schema |
|---|---|---|---|---|
| 1 | **MAY** | always | rest | MAY does not invalidate |
| 2 | **SHALL** | `baselineState` is present on any `result` object in `theRun` | log | needs other parts of the log |

1. Otherwise, `baselineState` **MAY** be present.
2. If `baselineState` is present on any `result` object in `theRun`, `baselineState` **SHALL** be present.

## `result.rank`

file-format-27-result-object.md; announced: 

| | Presence | When | Scope | Schema |
|---|---|---|---|---|
| 1 | **MAY** | always | rest | MAY does not invalidate |
| 2 | **SHALL NOT** | `kind` is present with a value other than `"fail"` | object | if/then |

1. Otherwise, `rank` **MAY** be present.
2. If `kind` is present with a value other than `"fail"`, `rank` **SHALL NOT** be present.

## `physicalLocation.artifactLocation`

file-format-29-physicallocation-object.md; announced: 

| | Presence | When | Scope | Schema |
|---|---|---|---|---|
| 1 | **MAY** | always | rest | MAY does not invalidate |
| 2 | **SHALL** | `artifactLocation` is absent | object | if/then |

1. Otherwise, `artifactLocation` **MAY** be present.
2. If `artifactLocation` is absent, `artifactLocation` **SHALL** be present.

## `physicalLocation.contextRegion`

file-format-29-physicallocation-object.md; announced: 

| | Presence | When | Scope | Schema |
|---|---|---|---|---|
| 1 | **SHALL NOT** | `region` is absent | object | if/then |

1. If `region` is absent, `contextRegion` **SHALL NOT** be present.

## `physicalLocation.address`

file-format-29-physicallocation-object.md; announced: 

| | Presence | When | Scope | Schema |
|---|---|---|---|---|
| 1 | **SHALL** | `address` is absent | object | if/then |

1. If `address` is absent, `address` **SHALL** be present.

## `region.startLine`

file-format-30-region-object.md; announced: 

| | Presence | When | Scope | Schema |
|---|---|---|---|---|
| 1 | **SHALL** | a `region` object represents a text region specified by line/column properties | world | only the producer knows |

1. If a `region` object represents a text region specified by line/column properties, `startLine` **SHALL** be present.

## `region.startColumn`

file-format-30-region-object.md; announced: 

| | Presence | When | Scope | Schema |
|---|---|---|---|---|
| 1 | **MAY** | a `region` object represents a text region specified by line/column properties | world | MAY does not invalidate |

1. If a `region` object represents a text region specified by line/column properties, `startColumn` **MAY** be present.

## `region.endLine`

file-format-30-region-object.md; announced: 

| | Presence | When | Scope | Schema |
|---|---|---|---|---|
| 1 | **MAY** | a `region` object represents a text region specified by line/column properties | world | MAY does not invalidate |

1. If a `region` object represents a text region specified by line/column properties, `endLine` **MAY** be present.

## `region.endColumn`

file-format-30-region-object.md; announced: 

| | Presence | When | Scope | Schema |
|---|---|---|---|---|
| 1 | **MAY** | a `region` object represents a text region specified by line/column properties | world | MAY does not invalidate |

1. If a `region` object represents a text region specified by line/column properties, `endColumn` **MAY** be present.

## `region.charOffset`

file-format-30-region-object.md; announced: 

| | Presence | When | Scope | Schema |
|---|---|---|---|---|
| 1 | **SHALL** | a `region` object represents a text region specified by offset/length properties | world | only the producer knows |

1. If a `region` object represents a text region specified by offset/length properties, `charOffset` **SHALL** be present.

## `region.charLength`

file-format-30-region-object.md; announced: 

| | Presence | When | Scope | Schema |
|---|---|---|---|---|
| 1 | **MAY** | a `region` object represents a text region specified by offset/length properties | world | MAY does not invalidate |

1. If a `region` object represents a text region specified by offset/length properties, `charLength` **MAY** be present.

## `region.byteOffset`

file-format-30-region-object.md; announced: 

| | Presence | When | Scope | Schema |
|---|---|---|---|---|
| 1 | **SHALL** | a `region` object represents a binary region | world | only the producer knows |

1. If a `region` object represents a binary region, `byteOffset` **SHALL** be present.

## `region.byteLength`

file-format-30-region-object.md; announced: 

| | Presence | When | Scope | Schema |
|---|---|---|---|---|
| 1 | **MAY** | a `region` object represents a binary region | world | MAY does not invalidate |

1. If a `region` object represents a binary region, `byteLength` **MAY** be present.

## `region.sourceLanguage`

file-format-30-region-object.md; announced: 

| | Presence | When | Scope | Schema |
|---|---|---|---|---|
| 1 | **MAY** | the `region` object represents a portion of a text artifact that contains source code | world | MAY does not invalidate |
| 2 | **SHALL NOT** | the `region` object does not represent a portion of a text artifact containing source code | world | only the producer knows |

1. If the `region` object represents a portion of a text artifact that contains source code, `sourceLanguage` **MAY** be present.
2. If the `region` object does not represent a portion of a text artifact containing source code, `sourceLanguage` **SHALL NOT** be present.

## `address.relativeAddress`

file-format-32-address-object.md; announced: 

| | Presence | When | Scope | Schema |
|---|---|---|---|---|
| 1 | **MAY** | `parentIndex` ([sec](#address-object--parentindex-property)) is present | object | MAY does not invalidate |
| 2 | **SHALL NOT** | `parentIndex` is absent | object | if/then |

1. If `parentIndex` ([sec](#address-object--parentindex-property)) is present, `relativeAddress` **MAY** be present.
2. If `parentIndex` is absent, `relativeAddress` **SHALL NOT** be present.

## `address.offsetFromParent`

file-format-32-address-object.md; announced: 

| | Presence | When | Scope | Schema |
|---|---|---|---|---|
| 1 | **MAY** | `parentIndex` ([sec](#address-object--parentindex-property)) is present | object | MAY does not invalidate |
| 2 | **SHALL NOT** | `parentIndex` is absent | object | if/then |

1. If `parentIndex` ([sec](#address-object--parentindex-property)) is present, `offsetFromParent` **MAY** be present.
2. If `parentIndex` is absent, `offsetFromParent` **SHALL NOT** be present.

## `address.length`

file-format-32-address-object.md; announced: 

| | Presence | When | Scope | Schema |
|---|---|---|---|---|
| 1 | **MAY** | always | rest | MAY does not invalidate |

1. Otherwise, `length` **MAY** be present.

## `address.parentIndex`

file-format-32-address-object.md; announced: 

| | Presence | When | Scope | Schema |
|---|---|---|---|---|
| 1 | **SHALL** | `theParent` exists (that is, if `thisObject` is expressed as an offset from some other address) | log | needs other parts of the log |
| 2 | **SHALL NOT** | `theParent` does not exist | log | needs other parts of the log |

1. If `theParent` exists (that is, if `thisObject` is expressed as an offset from some other address), `parentIndex` **SHALL** be present.
2. If `theParent` does not exist, `parentIndex` **SHALL NOT** be present.

## `logicalLocation.kind`

file-format-33-logicallocation-object.md; announced: 

| | Presence | When | Scope | Schema |
|---|---|---|---|---|
| 1 | **SHOULD** | always | rest | SHOULD does not invalidate |

1. Otherwise, `kind` **SHOULD** be present.

## `logicalLocation.parentIndex`

file-format-33-logicallocation-object.md; announced: 

| | Presence | When | Scope | Schema |
|---|---|---|---|---|
| 1 | **SHALL** | this `logicalLocation` object represents a nested logical location | world | only the producer knows |
| 2 | **SHALL NOT** | `thisObject` represents a top-level logical location | world | only the producer knows |

1. If this `logicalLocation` object represents a nested logical location, `parentIndex` **SHALL** be present.
2. If `thisObject` represents a top-level logical location, `parentIndex` **SHALL NOT** be present.

## `graphTraversal.resultGraphIndex`

file-format-42-graphtraversal-object.md; announced: 

| | Presence | When | Scope | Schema |
|---|---|---|---|---|
| 1 | **SHALL** | a `graphTraversal` object represents the traversal of a `graph` object ([sec](#graph-object)) that resides in `theResult.graphs` ([sec](#result-object--graphs-property)) | log | needs other parts of the log |

1. If a `graphTraversal` object represents the traversal of a `graph` object ([sec](#graph-object)) that resides in `theResult.graphs` ([sec](#result-object--graphs-property)), `resultGraphIndex` **SHALL** be present.

## `graphTraversal.runGraphIndex`

file-format-42-graphtraversal-object.md; announced: 

| | Presence | When | Scope | Schema |
|---|---|---|---|---|
| 1 | **SHALL** | a `graphTraversal` object represents the traversal of a `graph` object ([sec](#graph-object)) that resides in `theRun.graphs` ([sec](#run-object--graphs-property)) | log | needs other parts of the log |

1. If a `graphTraversal` object represents the traversal of a `graph` object ([sec](#graph-object)) that resides in `theRun.graphs` ([sec](#run-object--graphs-property)), `runGraphIndex` **SHALL** be present.

## `stackFrame.location`

file-format-45-stackframe-object.md; announced: 

| | Presence | When | Scope | Schema |
|---|---|---|---|---|
| 1 | **MAY** | always | rest | MAY does not invalidate |
| 2 | **SHOULD** | location information is unavailable (as it might be, for example, when stepping from application code into library code or operating system code) | world | SHOULD does not invalidate |

1. Otherwise, `location` **MAY** be present.
2. If location information is unavailable (as it might be, for example, when stepping from application code into library code or operating system code), `location` **SHOULD** be present.

## `webRequest.body`

file-format-46-webrequest-object.md; announced: 

| | Presence | When | Scope | Schema |
|---|---|---|---|---|
| 1 | **MAY** | always | rest | MAY does not invalidate |
| 2 | **SHOULD** | the request body is entirely textual | world | SHOULD does not invalidate |
| 3 | **MAY** | the request body is entirely textual | world | MAY does not invalidate |
| 4 | **SHALL** | the request body consists partially or entirely of binary data | world | only the producer knows |
| 5 | **SHALL NOT** | the request body consists partially or entirely of binary data | world | only the producer knows |

1. Otherwise, `body` **MAY** be present.
2. If the request body is entirely textual, `body` **SHOULD** be present.
3. If the request body is entirely textual, `body` **MAY** be present.
4. If the request body consists partially or entirely of binary data, `body` **SHALL** be present.
5. If the request body consists partially or entirely of binary data, `body` **SHALL NOT** be present.

## `webResponse.body`

file-format-47-webresponse-object.md; announced: 

| | Presence | When | Scope | Schema |
|---|---|---|---|---|
| 1 | **MAY** | always | rest | MAY does not invalidate |
| 2 | **SHOULD** | the response body is entirely textual | world | SHOULD does not invalidate |
| 3 | **MAY** | the response body is entirely textual | world | MAY does not invalidate |
| 4 | **SHALL** | the response body consists partially or entirely of binary data | world | only the producer knows |
| 5 | **SHALL NOT** | the response body consists partially or entirely of binary data | world | only the producer knows |

1. Otherwise, `body` **MAY** be present.
2. If the response body is entirely textual, `body` **SHOULD** be present.
3. If the response body is entirely textual, `body` **MAY** be present.
4. If the response body consists partially or entirely of binary data, `body` **SHALL** be present.
5. If the response body consists partially or entirely of binary data, `body` **SHALL NOT** be present.

## `webResponse.noResponseReceived`

file-format-47-webresponse-object.md; announced: 

| | Presence | When | Scope | Schema |
|---|---|---|---|---|
| 1 | **SHALL** | no response to the HTTP request was received (for example, because of a network failure) | world | only the producer knows |

1. If no response to the HTTP request was received (for example, because of a network failure), `noResponseReceived` **SHALL** be present.

## `resultProvenance.invocationIndex`

file-format-48-resultprovenance-object.md; announced: 

| | Presence | When | Scope | Schema |
|---|---|---|---|---|
| 1 | **MAY** | `theRun.invocations` ([sec](#invocations-property)) is present | log | MAY does not invalidate |
| 2 | **SHALL NOT** | `theRun.invocations` is absent | log | needs other parts of the log |

1. If `theRun.invocations` ([sec](#invocations-property)) is present, `invocationIndex` **MAY** be present.
2. If `theRun.invocations` is absent, `invocationIndex` **SHALL NOT** be present.

## `toolComponentReference.index`

file-format-54-toolcomponentreference-object.md; announced: 

| | Presence | When | Scope | Schema |
|---|---|---|---|---|
| 1 | **MAY** | `theComponent` is an element of `theTool.extensions` ([sec](#extensions-property)) | log | MAY does not invalidate |

1. If `theComponent` is an element of `theTool.extensions` ([sec](#extensions-property)), `index` **MAY** be present.

## `replacement.insertedContent`

file-format-57-replacement-object.md; announced: 

| | Presence | When | Scope | Schema |
|---|---|---|---|---|
| 1 | **MAY** | always | rest | MAY does not invalidate |

1. Otherwise, `insertedContent` **MAY** be present.

## `notification.associatedRule`

file-format-58-notification-object.md; announced: 

| | Presence | When | Scope | Schema |
|---|---|---|---|---|
| 1 | **SHOULD** | the condition described by the `notification` object is relevant to a particular analysis rule | world | SHOULD does not invalidate |

1. If the condition described by the `notification` object is relevant to a particular analysis rule, `associatedRule` **SHOULD** be present.

## `notification.locations`

file-format-58-notification-object.md; announced: 

| | Presence | When | Scope | Schema |
|---|---|---|---|---|
| 1 | **MAY** | the condition described by the `notification` object is relevant to one or more locations | world | MAY does not invalidate |

1. If the condition described by the `notification` object is relevant to one or more locations, `locations` **MAY** be present.

## `notification.exception`

file-format-58-notification-object.md; announced: 

| | Presence | When | Scope | Schema |
|---|---|---|---|---|
| 1 | **MAY** | the notification is a result of a runtime exception | world | MAY does not invalidate |
| 2 | **SHALL NOT** | the notification is not the result of a runtime exception | world | only the producer knows |

1. If the notification is a result of a runtime exception, `exception` **MAY** be present.
2. If the notification is not the result of a runtime exception, `exception` **SHALL NOT** be present.

## `exception.kind`

file-format-59-exception-object.md; announced: 

| | Presence | When | Scope | Schema |
|---|---|---|---|---|
| 1 | **SHOULD** | always | rest | SHOULD does not invalidate |
| 2 | **SHALL NOT** | the tool does not have access to information about the object that was thrown | world | only the producer knows |

1. Otherwise, `kind` **SHOULD** be present.
2. If the tool does not have access to information about the object that was thrown, `kind` **SHALL NOT** be present.

## `exception.message`

file-format-59-exception-object.md; announced: 

| | Presence | When | Scope | Schema |
|---|---|---|---|---|
| 1 | **SHOULD** | always | rest | SHOULD does not invalidate |
| 2 | **SHALL NOT** | the tool does not have access to an appropriate property of the thrown object | world | only the producer knows |

1. Otherwise, `message` **SHOULD** be present.
2. If the tool does not have access to an appropriate property of the thrown object, `message` **SHALL NOT** be present.

## `externalProperties.runGuid`

external-property-file-format.md; announced: 

| | Presence | When | Scope | Schema |
|---|---|---|---|---|
| 1 | **MAY** | the externalized properties contained in this `externalProperties` object are associated with a single `run` object ([sec](#run-object)) `theRun`, and if `theRun` contains an `automationDetails.guid` property ([sec](#automationdetails-property), [sec](#runautomationdetails-object--guid-property)) | log | MAY does not invalidate |
| 2 | **SHALL NOT** | otherwise, in all other cases | rest | follows from the other branches |

1. If the externalized properties contained in this `externalProperties` object are associated with a single `run` object ([sec](#run-object)) `theRun`, and if `theRun` contains an `automationDetails.guid` property ([sec](#automationdetails-property), [sec](#runautomationdetails-object--guid-property)), `runGuid` **MAY** be present.
2. Otherwise, `runGuid` **SHALL NOT** be present.
