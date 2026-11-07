# Findings

What `bin/vision.py derive` noticed in the prose, the twins and the schema; do not edit.
Each finding names the place to change; decisions for the TC are marked **TC**.

## Prose and schema

- **TC** `attachment.location`: a property section in the prose, no such property in the schema
- **TC** `externalProperties.$schema`: a property section in the prose, no such property in the schema
- `externalProperties.schema`: in the schema, not described in the prose
- **TC** `suppression.justificationType`: a property section in the prose, no such property in the schema
- file-format-20-invocation-object.md:37: heading "arguments property" does not give its property as `` `name` Property ``
- file-format-23-versioncontroldetails-object.md:19: heading "revisionId` Property" does not give its property as `` `name` Property ``
- file-format-24-artifact-object.md:7: heading "`location property" does not give its property as `` `name` Property ``
- file-format-27-result-object.md:23: heading "guid property" does not give its property as `` `name` Property ``
- `run.language`: the prose gives the default `"en-US"`, the schema gives none
- **TC** `run.columnKind`: the prose lists the value `"bytes"`, the schema enum does not have it
- `toolComponent.language`: the prose gives the default `"en-US"`, the schema gives none

## Examples

- 119 of 127 JSON code blocks in the prose are not JSON (margin comments, elisions): only their twins can be validated
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

## Statements

- 15 statements announce a set of keywords ("either **SHALL** or **MAY**"); the rule is the sum of the sentences that follow (constraint record candidates):
  - file-format-04-artifactlocation-object.md:18 (`uri` Property)
  - file-format-04-artifactlocation-object.md:83 (`index` Property)
  - file-format-14-run-object.md:347 (`results` Property)
  - file-format-16-externalpropertyfilereference-object.md:16 (`location` Property)
  - file-format-16-externalpropertyfilereference-object.md:24 (`guid` Property)
  - file-format-19-toolcomponent-object.md:379 (`language` Property)
  - file-format-24-artifact-object.md:10 (`location property)
  - file-format-24-artifact-object.md:59 (`offset` Property)
  - file-format-27-result-object.md:42 (`ruleId` Property)
  - file-format-27-result-object.md:114 (`rule` Property)
  - file-format-28-location-object.md:38 (`physicalLocation` Property)
  - file-format-28-location-object.md:42 (`logicalLocations` Property)
  - file-format-33-logicallocation-object.md:74 (`fullyQualifiedName` Property)
  - file-format-38-threadflowlocation-object.md:10 (`index` Property)
  - external-property-file-format.md:74 (`version` Property)
- file-format-52-reportingdescriptorreference-object.md:153: normative "shall" in lower case
