# Findings

What `bin/vision.py derive` noticed in the prose, the twins and the schema; do not edit.
Each finding names the place to change; decisions for the TC are marked **TC**.

## Prose and schema

- **TC** `attachment.location`: a property section in the prose, no such property in the schema (S3, records/drift.yaml)
- **TC** `externalProperties.$schema`: a property section in the prose, no such property in the schema (S4, records/drift.yaml)
- **TC** `externalProperties.schema`: in the schema, not described in the prose (S4, records/drift.yaml)
- **TC** `suppression.justificationType`: a property section in the prose, no such property in the schema (S1, records/drift.yaml)
- `run.language`: the prose gives the default `"en-US"`, the schema gives none
- **TC** `run.columnKind`: the prose lists the value `"bytes"`, the schema enum does not have it
- `toolComponent.language`: the prose gives the default `"en-US"`, the schema gives none

## Examples

- 9 of 10 JSON code blocks in the prose are not JSON (margin comments, elisions): only their twins can be validated
- file-format-30-region-object.md: JSON code blocks without a twin
- **TC** `external-property-file-format_externalproperties-object_general_example-1.json` as externalProperties: /: Additional properties are not allowed ('$schema' was unexpected)
- **TC** `file-format-03-artifactcontent-object_rendered-property_example-1.json` as physicalLocation: /address: Additional properties are not allowed ('baseAddress', 'offset' were unexpected)
- **TC** `file-format-11-message-object_messages-with-embedded-links_example-2.json` as result: /locations/0/physicalLocation: Additional properties are not allowed ('uri' was unexpected)
- **TC** `file-format-11-message-object_messages-with-embedded-links_example-2.json` as result: /relatedLocations/0/physicalLocation: Additional properties are not allowed ('uri' was unexpected)
- **TC** `file-format-14-run-object_redactiontokens-property_example-1.json` as run: /: Additional properties are not allowed ('invocation' was unexpected)
- **TC** `file-format-19-toolcomponent-object_notifications-property_example-1.json` as tool: /driver/notifications/0: Additional properties are not allowed ('level' was unexpected)
- **TC** `file-format-19-toolcomponent-object_notifications-property_example-1.json` as tool: /driver/notifications/0/messageStrings/default: "Cannot load plugin '{0}' because it was not found." is not of type 'object'
- **TC** `file-format-19-toolcomponent-object_notifications-property_example-1.json` as tool: /driver/notifications/1: Additional properties are not allowed ('level' was unexpected)
- **TC** `file-format-19-toolcomponent-object_notifications-property_example-1.json` as tool: /driver/notifications/1/messageStrings/default: "Cannot load plugin '{0}' because it is not signed." is not of type 'object'
- **TC** `file-format-20-invocation-object_toolconfigurationnotifications-property_example-1.json` as invocation: /toolConfigurationNotifications/0/associatedRule: Additional properties are not allowed ('ruleId' was unexpected)
- **TC** `file-format-21-attachment-object_general_example-1.json` as result: /attachments/0: Additional properties are not allowed ('location' was unexpected)
- **TC** `file-format-22-conversion-object_general_example-1.json` as sarifLog: /runs/0/conversion: Additional properties are not allowed ('analysisToolLogFileLocation' was unexpected)
- **TC** `file-format-22-conversion-object_general_example-1.json` as sarifLog: /runs/0/conversion/invocation: 'Sarif.Multitool.exe convert -t AndroidStudio northwind.log' is not of type 'object'
- **TC** `file-format-27-result-object_kind-property_example-1.json` as run: /results/0/locations/0/physicalLocation: Additional properties are not allowed ('uri' was unexpected)
- **TC** `file-format-27-result-object_kind-property_example-1.json` as run: /results/1/locations/0/physicalLocation: Additional properties are not allowed ('uri' was unexpected)
- **TC** `file-format-27-result-object_level-property_example-1.json` as run: /results/0/locations/0/physicalLocation: Additional properties are not allowed ('uri' was unexpected)
- **TC** `file-format-27-result-object_relatedlocations-property_example-1.json` as run: /results/0/locations/0/physicalLocation: Additional properties are not allowed ('uri' was unexpected)
- **TC** `file-format-27-result-object_relatedlocations-property_example-1.json` as run: /results/0/locations/0/physicalLocation/region/startLine: '6' is not of type 'integer'
- **TC** `file-format-27-result-object_relatedlocations-property_example-1.json` as run: /results/0/locations/0/physicalLocation/region/startColumn: '10' is not of type 'integer'
- **TC** `file-format-27-result-object_relatedlocations-property_example-1.json` as run: /results/0/relatedLocations/0/physicalLocation: Additional properties are not allowed ('uri' was unexpected)
- **TC** `file-format-27-result-object_relatedlocations-property_example-1.json` as run: /results/0/relatedLocations/0/physicalLocation/region/startLine: '2' is not of type 'integer'
- **TC** `file-format-27-result-object_relatedlocations-property_example-1.json` as run: /results/0/relatedLocations/0/physicalLocation/region/startColumn: '6' is not of type 'integer'
- **TC** `file-format-43-edgetraversal-object_stepoveredgecount-property_example-1.json` as result: /graphs/0/nodes/0/children/1/label: 'Call functionB' is not of type 'object'
- **TC** `file-format-43-edgetraversal-object_stepoveredgecount-property_example-1.json` as result: /graphs/0/nodes/1: Additional properties are not allowed ('nodes' was unexpected)
- **TC** `file-format-50-reportingconfiguration-object_parameters-property_example-1.json` as reportingDescriptor: /name: {'text': 'LimitSourceLineLength'} is not of type 'string'
- `file-format-55-fix-object_description-property_example-1.json`: no host definition: the fix is shown under a label key `fix`, which no SARIF object has; the twin should hold the fix itself
- **TC** `file-format-57-replacement-object_general_example-1.json` as fix: /artifactChanges/0: Additional properties are not allowed ('deletedRegion', 'insertedContent' were unexpected)
- **TC** `file-format-57-replacement-object_general_example-1.json` as fix: /artifactChanges/1: Additional properties are not allowed ('deletedRegion' was unexpected)
- **TC** `file-format-57-replacement-object_general_example-1.json` as fix: /artifactChanges/2: Additional properties are not allowed ('deletedRegion', 'insertedContent' were unexpected)
- example/graft.json: /version: '2.1.0' is not one of ['2.2']

## Margin notes

- `diagnosing-results_example-1.json` at `/originalUriBaseIds`: stray text after the reference: "# See (#run-object).14" (a remnant of a section number)
- `file-format-03-artifactcontent-object_rendered-property_example-1.json` at `/address/baseAddress`: "See (#absoluteaddress-property)" names the property `absoluteAddress`, the line holds `baseAddress`
- `file-format-03-artifactcontent-object_rendered-property_example-1.json` at `/address/offset`: "See (#offsetfromparent-property)" names the property `offsetFromParent`, the line holds `offset`
- `file-format-19-toolcomponent-object_supportedtaxonomies-property_example-1.json` at `/taxonomies/0`: the note says "toolComponentReference object", the schema says `toolComponent`
- `file-format-19-toolcomponent-object_taxonomies_example-1.json` at `/tool/driver/rules/0/relationships/0/target`: stray text after the reference: "# See (#reportingdescriptorrelationship-object).2" (a remnant of a section number)
- `file-format-22-conversion-object_general_example-1.json` at `/runs/0/conversion/analysisToolLogFileLocation`: "See (#analysistoollogfiles-property)" names the property `analysisToolLogFiles`, the line holds `analysisToolLogFileLocation`
- `file-format-24-artifact-object_hashes-property_example-1.json` at `/`: the note says "file object", the schema says `artifact`
- `file-format-33-logicallocation-object_name-property_example-1.json` at `/kind`: stray text after the reference: "# See (#logicallocation-object).7" (a remnant of a section number)
- `file-format-34-locationrelationship-object_general_example-1.json` at `/locations/0/relationships`: stray text after the reference: "# See (#location-object).7" (a remnant of a section number)
- 43 object notes name their object without a reference ("A run object."); a key `ref` would link them like the others

## Statements

- 15 statements announce a set of keywords ("either **SHALL** or **MAY**"); the rule is the sum of the sentences that follow (records/constraints.yaml, views/constraints.md):
  - file-format-04-artifactlocation-object.md:18 (`uri` Property)
  - file-format-04-artifactlocation-object.md:83 (`index` Property)
  - file-format-14-run-object.md:347 (`results` Property)
  - file-format-16-externalpropertyfilereference-object.md:16 (`location` Property)
  - file-format-16-externalpropertyfilereference-object.md:24 (`guid` Property)
  - file-format-19-toolcomponent-object.md:379 (`language` Property)
  - file-format-24-artifact-object.md:10 (`location` Property)
  - file-format-24-artifact-object.md:59 (`offset` Property)
  - file-format-27-result-object.md:42 (`ruleId` Property)
  - file-format-27-result-object.md:114 (`rule` Property)
  - file-format-28-location-object.md:38 (`physicalLocation` Property)
  - file-format-28-location-object.md:42 (`logicalLocations` Property)
  - file-format-33-logicallocation-object.md:74 (`fullyQualifiedName` Property)
  - file-format-38-threadflowlocation-object.md:10 (`index` Property)
  - external-property-file-format.md:74 (`version` Property)
- **TC** `run.results`: the prose allows the value null when the tool failed; the schema type of results is array only
- **TC** `result.ruleId`: announced **SHALL NOT** is given by no branch
- **TC** `result.ruleId`: the branches follow "Direct producers **SHALL** emit either or both of `ruleId` and `rule.id`": is a log file without both invalid, or only its direct producer at fault (a converter **SHOULD** synthesize `ruleId`)?
  - as a rule of the log file, `example/example-3-13-5-01.json` would break it: /runs/0/results/0: 'ruleId' is a required property
  - as a rule of the log file, `example/example-3-13-5-01.json` would break it: /runs/1/results/0: 'ruleId' is a required property
  - as a rule of the log file, `example/example-3-3-4-01.json` would break it: /runs/0/results/0: 'ruleId' is a required property
  - as a rule of the log file, `file-format-04-artifactlocation-object_guidance-on-the-use-of-artifactlocation-objects_example-1.json` would break it: /results/0: 'ruleId' is a required property
  - as a rule of the log file, `file-format-05-string-properties_versioned-hierarchical-strings_example-1.json` would break it: /: 'ruleId' is a required property
  - as a rule of the log file, `file-format-27-result-object_analysistarget-property_example-1.json` would break it: /: 'ruleId' is a required property
  - as a rule of the log file, `file-format-27-result-object_fingerprints-property_example-1.json` would break it: /: 'ruleId' is a required property
  - as a rule of the log file, `file-format-27-result-object_fingerprints-property_example-2.json` would break it: /results/0: 'ruleId' is a required property
  - as a rule of the log file, `file-format-27-result-object_fingerprints-property_example-2.json` would break it: /results/1: 'ruleId' is a required property
  - as a rule of the log file, `file-format-27-result-object_message-property_example-1.json` would break it: /results/0: 'ruleId' is a required property
  - as a rule of the log file, `file-format-27-result-object_partialfingerprints-property_example-1.json` would break it: /: 'ruleId' is a required property
  - as a rule of the log file, `file-format-27-result-object_partialfingerprints-property_example-2.json` would break it: /results/0: 'ruleId' is a required property
  - as a rule of the log file, `file-format-27-result-object_partialfingerprints-property_example-2.json` would break it: /results/1: 'ruleId' is a required property
  - as a rule of the log file, `file-format-29-physicallocation-object_contextregion-property_example-1.json` would break it: /: 'ruleId' is a required property
  - as a rule of the log file, `file-format-29-physicallocation-object_region-property_example-1.json` would break it: /: 'ruleId' is a required property
  - as a rule of the log file, `file-format-33-logicallocation-object_kind-property_example-2.json` would break it: /results/0: 'ruleId' is a required property
  - as a rule of the log file, `file-format-33-logicallocation-object_kind-property_example-2.json` would break it: /results/1: 'ruleId' is a required property
  - as a rule of the log file, `file-format-34-locationrelationship-object_general_example-1.json` would break it: /: 'ruleId' is a required property
  - as a rule of the log file, `file-format-36-codeflow-object_general_example-1.json` would break it: /: 'ruleId' is a required property
  - as a rule of the log file, `file-format-42-graphtraversal-object_edgetraversals-property_example-1.json` would break it: /: 'ruleId' is a required property
  - as a rule of the log file, `file-format-43-edgetraversal-object_stepoveredgecount-property_example-1.json` would break it: /: 'ruleId' is a required property
- `file-format-24-artifact-object_hashes-property_example-1.json` breaks a derived presence rule: /: 'location' is a required property (if the example is a fragment, it lacks an elision marker)
- file-format-52-reportingdescriptorreference-object.md:153: normative "shall" in lower case
