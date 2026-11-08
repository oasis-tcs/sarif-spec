# Statements binding: Converter (conformance clause 4)

Derived by `bin/vision.py derive` from `records/statements.yaml` and `records/roles.yaml`; do not edit.
15 statements of its own; SHALL 2, SHALL NOT 1, SHOULD 5, SHOULD NOT 2, MAY 5.
Its profile includes [log-file](log-file.md), [producer](producer.md): 898 statements in all.


## `conversion` Property

`file-format-14-run-object.md`

- If a `run` object was produced by a converter, it **MAY** contain a property named `conversion` whose value is a `conversion` object ([sec](#conversion-object)) that describes how the converter transformed the analysis tool’s native output format into the SARIF format. (line 91)

## `semanticVersion` Property

`file-format-19-toolcomponent-object.md`

- Unless the author of the converter knows that the version number of the tool from which it converts is intended to be interpreted according to Semantic Versioning [cite](#SEMVER), the converter **SHALL NOT** emit the `semanticVersion` property in `run.tool` ([sec](#run-object--tool-property)), although of course it may emit its own `semanticVersion` property (the one in `run.conversion.tool` ([sec](#conversion-object--tool-property))). (line 321)

## `guid` Property

`file-format-27-result-object.md`

- Direct SARIF producers and SARIF converters **MAY** but do not need to set this property. (line 28)

## `correlationGuid` Property

`file-format-27-result-object.md`

- Direct SARIF producers and SARIF converters **SHOULD NOT** set this property. (line 36)

## `ruleId` Property

`file-format-27-result-object.md`

- A SARIF converter which converts the output of such an analysis tool to the SARIF format **SHOULD** synthesize `ruleId` from other information available in the analysis tool's output. (line 100)

## `fingerprints` Property

`file-format-27-result-object.md`

- A SARIF converter **MAY** populate this property if the analysis tool’s native output format provides a value that qualifies as a fingerprint (a stable identifier for the result). (line 561)

## `location` Propertyy

`file-format-38-threadflowlocation-object.md`

- However, if the native output format associates a human readable message with such a step, the SARIF converter **SHOULD** create a `location` object and populate only its `message` property ([sec](#location-object--message-property)). (line 109)

## Annex D Production of SARIF by Converters

`converters.md`

- A converter **SHOULD** populate those elements of the SARIF format for which a direct equivalent exists in the input data. (line 6)
- If the input data includes information for which there is no SARIF equivalent, a converter **MAY** use it to populate the various property bags ([sec](#property-bags)) and tag lists ([sec](#tags)) defined by the SARIF format, or they **MAY** simply omit it from the output. (line 8)
- When populating a property bag with such information, a converter **SHOULD** use a property name that matches the name of that piece of information in the native tool format, even if that name does not conform to the camelCase convention used in the rest of this document. (line 8)
- When serializing SARIF as JSON, a converter **SHALL** replace any characters in string-valued properties that cannot occur in a JSON string with the appropriate escape sequence as defined by JSON [cite](#RFC8259). (line 12)
- If the input data does not include an equivalent for any SARIF element, a converter **MAY** attempt to synthesize that element. (line 14)
- A converter **SHOULD** populate its own semantic version [cite](#SEMVER) property `theRun.conversion.tool.driver.semanticVersion` ([sec](#semanticversion-property)). (line 18)
- If it does, and if a subsequent version of the converter synthesizes SARIF elements in a sematically incompatible way, it **SHALL** increment the major version component of its semantic version. (line 18)
- - A converter **SHOULD NOT** populate the analysis tool’s `toolComponent.semanticVersion` ([sec](#semanticversion-property)) unless it knows that the tool component's version string is intended to be interpreted as a semantic version [cite](#SEMVER) version string. (line 23)
