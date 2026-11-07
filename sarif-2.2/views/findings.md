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
- **TC** `examples_comprehensive-sarif-file_codeblock-json-1.sarif.json` as sarifLog: /runs/0/invocations/0/toolConfigurationNotifications/0/associatedRule: Additional properties are not allowed ('ruleId' was unexpected)
- **TC** `examples_comprehensive-sarif-file_codeblock-json-1.sarif.json` as sarifLog: /runs/0/results/0: Additional properties are not allowed ('addresses' was unexpected)
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
- **TC** `file-format-33-logicallocation-object_kind-property_example-2.json` as run: /results/0/locations/0: Additional properties are not allowed ('logicalLocation' was unexpected)
- **TC** `file-format-33-logicallocation-object_kind-property_example-2.json` as run: /results/1/locations/0: Additional properties are not allowed ('logicalLocation' was unexpected)
- **TC** `file-format-43-edgetraversal-object_stepoveredgecount-property_example-1.json` as result: /graphs/0/nodes/0/children/1/label: 'Call functionB' is not of type 'object'
- **TC** `file-format-43-edgetraversal-object_stepoveredgecount-property_example-1.json` as result: /graphs/0/nodes/1: Additional properties are not allowed ('nodes' was unexpected)
- **TC** `file-format-50-reportingconfiguration-object_parameters-property_example-1.json` as reportingDescriptor: /name: {'text': 'LimitSourceLineLength'} is not of type 'string'
- `file-format-55-fix-object_description-property_example-1.json`: no host definition: the fix is shown under a label key `fix`, which no SARIF object has; the twin should hold the fix itself
- **TC** `file-format-57-replacement-object_general_example-1.json` as fix: /artifactChanges/0: Additional properties are not allowed ('deletedRegion', 'insertedContent' were unexpected)
- **TC** `file-format-57-replacement-object_general_example-1.json` as fix: /artifactChanges/1: Additional properties are not allowed ('deletedRegion' was unexpected)
- **TC** `file-format-57-replacement-object_general_example-1.json` as fix: /artifactChanges/2: Additional properties are not allowed ('deletedRegion', 'insertedContent' were unexpected)
- `examples_comprehensive-sarif-file_codeblock-json-1.sarif.json`: snippet still hand-written: closest is code block 3, whose line 6 differs from the twin: '"addresses": [' vs '"automationDetails": {'
- `examples_minimal-valid-sarif-log-file_codeblock-json-1.sarif.json`: snippet still hand-written: closest is code block 0, whose line 10 differs from the twin: '"results": [' vs '"results": []'
- `external-property-file-format_externalproperties-object_general_example-1.json`: snippet still hand-written: closest is code block 0, whose line 7 differs from the twin: '' vs '"guid": "00001111-2222-1111-8888-555566667777",'
- `file-format-13-sariflog-object_inlineexternalproperties-property_example-1.json`: snippet still hand-written: closest is code block 1, whose line 43 differs from the twin: '...' vs '{'
- `file-format-14-run-object_artifacts-property_example-1.json`: snippet still hand-written: closest is code block 6, whose line 2 differs from the twin: '...' vs '"artifacts": ['
- `file-format-14-run-object_newlinesequences-property_example-2.json`: snippet still hand-written: closest is code block 6, whose line 3 differs from the twin: '"newlineSequences": [ "\\r\\n", "\\n", "\\u0085", "\\u2028" ],' vs '"newlineSequences": ['
- `file-format-14-run-object_originaluribaseIds-property_example-1.json`: snippet still hand-written: closest is code block 2, whose line 2 differs from the twin: '"PROJECTROOT": {' vs '"PROJECTROOT": {'
- `file-format-14-run-object_versioncontrolprovenance-property_example-1.json`: snippet still hand-written: closest is code block 6, whose line 2 differs from the twin: '...' vs '"versionControlProvenance": ['
- `file-format-20-invocation-object_responsefiles-property_example-1.json`: snippet still hand-written: closest is code block 0, whose line 2 differs from the twin: '"commandLine": "/quiet @analyzer.rsp @strict.rsp @options.rs' vs '"commandLine": "/quiet @analyzer.rsp @strict.rsp @options.rs'
- `file-format-22-conversion-object_general_example-1.json`: snippet still hand-written: closest is code block 0, whose line 16 differs from the twin: '' vs '"invocation": "Sarif.Multitool.exe convert -t AndroidStudio '
- `file-format-24-artifact-object_encoding-property_example-1.json`: snippet still hand-written: closest is code block 1, whose line 9 differs from the twin: '' vs '},'
- `file-format-25-speciallocations-object_displaybase-property_example-1.json`: snippet still hand-written: closest is code block 0, whose line 10 differs from the twin: '"uri": "/home/user/",' vs '"uri": "/home/user/",'
- `file-format-27-result-object_fingerprints-property_example-1.json`: snippet still hand-written: closest is code block 7, whose line 2 differs from the twin: '"fingerprints": {' vs '"fingerprints": {'
- `file-format-27-result-object_partialfingerprints-property_example-4.json`: snippet still hand-written: closest is code block 7, whose line 2 differs from the twin: '"fingerprints": {' vs '...'
- `file-format-27-result-object_relatedlocations-property_example-1.json`: snippet still hand-written: closest is code block 12, whose line 37 differs from the twin: '...' vs '...'
- `file-format-33-logicallocation-object_kind-property_example-1.json`: snippet still hand-written: closest is code block 3, whose line 51 differs from the twin: '"fullyQualifiedName": "/orders/order[1]/total/text()",' vs '"fullyQualifiedName": "/orders/order[1]/text()",'
- `file-format-33-logicallocation-object_kind-property_example-2.json`: snippet still hand-written: closest is code block 3, whose line 6 differs from the twin: '"logicalLocations": [' vs '"logicalLocation": {'
- `file-format-38-threadflowlocation-object_kinds-property_example-3.json`: snippet still hand-written: no code block of its file matches
- `file-format-49-reportingdescriptor-object_messagestrings-property_example-1.json`: snippet still hand-written: closest is code block 3, whose line 3 differs from the twin: '"objectCreation":  {' vs '"objectCreation": {'
- `file-format-51-configurationoverride-object_general_example-1.json`: snippet still hand-written: closest is code block 0, whose line 20 differs from the twin: '' vs '"descriptor": {'
- `file-format-52-reportingdescriptorreference-object_index-property_example-1.json`: snippet still hand-written: closest is code block 2, whose line 21 differs from the twin: '' vs '"rule": {'
- `file-format-53-reportingdescriptorrelationship-object_general_example-2.json`: snippet still hand-written: closest is code block 1, whose line 23 differs from the twin: '"guid": "11111111-0000-1111-8888-000000000002"' vs '"guid": "11111111-0000-1111-8888-000000000002",'
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
