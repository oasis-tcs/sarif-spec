# Statements naming: converter

Derived by `bin/vision.py derive` from the prose and `records/roles.yaml`; do not edit.
23 statements; SHALL 5, SHALL NOT 1, SHOULD 7, SHOULD NOT 5, MAY 6.


## General

`file-format-08-property-bags.md`

- The components of the property names **SHOULD** be camelCase strings, but see [sec](#production-of-sarif-by-converters) for exceptions. (line 8)

## `conversion` Property

`file-format-14-run-object.md`

- If a `run` object was produced by a converter, it **MAY** contain a property named `conversion` whose value is a `conversion` object ([sec](#conversion-object)) that describes how the converter transformed the analysis tool’s native output format into the SARIF format. (line 91)

## `semanticVersion` Property

`file-format-19-toolcomponent-object.md`

- Unless the author of the converter knows that the version number of the tool from which it converts is intended to be interpreted according to Semantic Versioning [cite](#SEMVER), the converter **SHALL NOT** emit the `semanticVersion` property in `run.tool` ([sec](#run-object--tool-property)), although of course it may emit its own `semanticVersion` property (the one in `run.conversion.tool` ([sec](#conversion-object--tool-property))). (line 321)

## `tool` Property

`file-format-22-conversion-object.md`

- A `conversion` object **SHALL** contain a property named `tool` whose value is a `tool` object ([sec](#tool-object)) that describes the converter. (line 46)

## `invocation` Property

`file-format-22-conversion-object.md`

- A `conversion` object **MAY** contain a property named `invocation` whose value is an `invocation` object ([sec](#invocation-object)) that describes the invocation of the converter. (line 50)

## guid property

`file-format-27-result-object.md`

- Direct SARIF producers and SARIF converters **MAY** but do not need to set this property. (line 28)

## `correlationGuid` Property

`file-format-27-result-object.md`

- Direct SARIF producers and SARIF converters **SHOULD NOT** set this property. (line 36)

## `ruleId` Property

`file-format-27-result-object.md`

- A SARIF converter which converts the output of such an analysis tool to the SARIF format **SHOULD** synthesize `ruleId` from other information available in the analysis tool's output. (line 100)
- Therefore, a SARIF consumer **SHOULD NOT** attempt to compare or combine the output from different converters for the same analysis tool. (line 102)

## `fingerprints` Property

`file-format-27-result-object.md`

- A SARIF converter **MAY** populate this property if the analysis tool’s native output format provides a value that qualifies as a fingerprint (a stable identifier for the result). (line 561)

## `location` Propertyy

`file-format-38-threadflowlocation-object.md`

- However, if the native output format associates a human readable message with such a step, the SARIF converter **SHOULD** create a `location` object and populate only its `message` property ([sec](#location-object--message-property)). (line 109)

## `conversionSources` Property

`file-format-48-resultprovenance-object.md`

- If `theResult` was produced by a converter, and if the analysis tool whose output was converted to SARIF produced any per-result files for this result, then the `physicalLocation` objects in the array **SHALL** specify the relevant portions of the per-result files for this result. (line 60)
- Otherwise (that is, if the `run` object was not produced by a converter, or if there were no per-run files for this result), then if `conversionSources` is present, its value **SHALL** be an empty array. (line 62)

## Annex D Production of SARIF by Converters

`converters.md`

- A converter **SHOULD** populate those elements of the SARIF format for which a direct equivalent exists in the input data. (line 6)
- If the input data includes information for which there is no SARIF equivalent, a converter **MAY** use it to populate the various property bags ([sec](#property-bags)) and tag lists ([sec](#tags)) defined by the SARIF format, or they **MAY** simply omit it from the output. (line 8)
- When populating a property bag with such information, a converter **SHOULD** use a property name that matches the name of that piece of information in the native tool format, even if that name does not conform to the camelCase convention used in the rest of this document. (line 8)
- When serializing SARIF as JSON, a converter **SHALL** replace any characters in string-valued properties that cannot occur in a JSON string with the appropriate escape sequence as defined by JSON [cite](#RFC8259). (line 12)
- If the input data does not include an equivalent for any SARIF element, a converter **MAY** attempt to synthesize that element. (line 14)
- Since each converter might synthesize SARIF elements differently (notably the rule id; see [sec](#ruleid-property)), a SARIF consumer **SHOULD NOT** attempt to combine results produced by different converters for the same tool. (line 16)
- A converter **SHOULD** populate its own semantic version [cite](#SEMVER) property `theRun.conversion.tool.driver.semanticVersion` ([sec](#semanticversion-property)). (line 18)
- If it does, and if a subsequent version of the converter synthesizes SARIF elements in a sematically incompatible way, it **SHALL** increment the major version component of its semantic version. (line 18)
- - A converter that knows which artifact a result was detected in, but not which artifact the analysis tool was originally instructed to scan, **SHOULD** populate `result.locations` ([sec](#result-object--locations-property)), but **SHOULD NOT** attempt to populate `result.analysisTarget` ([sec](#analysistarget-property)). (line 22)
- - A converter **SHOULD NOT** populate the analysis tool’s `toolComponent.semanticVersion` ([sec](#semanticversion-property)) unless it knows that the tool component's version string is intended to be interpreted as a semantic version [cite](#SEMVER) version string. (line 23)
