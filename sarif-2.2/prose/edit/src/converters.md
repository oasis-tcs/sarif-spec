<!--
---
toc:
  auto: false
  label: (Normative) Production of SARIF by converters
  enumerate: Appendix D.
---
-->
# (Normative) Production of SARIF by Converters

There are two broad categories of tools that can produce output in the SARIF format. Analysis tools produce SARIF as a result of performing a scan on a set of analysis targets. Converters translate existing data from a non-SARIF format into the SARIF format. That data might come from an analysis tool that produces output in a non-SARIF format, from a bug database, or from any other source.

A converter **SHOULD** populate those elements of the SARIF format for which a direct equivalent exists in the input data.

If the input data includes information for which there is no SARIF equivalent, a converter **MAY** use it to populate the various property bags ([sec](#property-bags)) and tag lists ([sec](#tags)) defined by the SARIF format, or they **MAY** simply omit it from the output. When populating a property bag with such information, a converter **SHOULD** use a property name that matches the name of that piece of information in the native tool format, even if that name does not conform to the camelCase convention used in the rest of this document.

> NOTE: This makes it easier to match these properties with the source data in the native tool format.

When serializing SARIF as JSON, a converter **SHALL** replace any characters in string-valued properties that cannot occur in a JSON string with the appropriate escape sequence as defined by JSON [cite](#RFC8259).

If the input data does not include an equivalent for any SARIF element, a converter **MAY** attempt to synthesize that element. (For example, a converter might heuristically extract a rule id from the text of an unstructured error message.)

Since each converter might synthesize SARIF elements differently (notably the rule id; see [sec](#ruleid-property)), a SARIF consumer **SHOULD NOT** attempt to combine results produced by different converters for the same tool.

A converter **SHOULD** populate its own semantic version [cite](#SEMVER) property `theRun.conversion.tool.driver.semanticVersion` ([sec](#semanticversion-property)). If it does, and if a subsequent version of the converter synthesizes SARIF elements in a sematically incompatible way, it **SHALL** increment the major version component of its semantic version.

Notwithstanding this general guidance recommending that a converter synthesize SARIF elements where possible:

- A converter that knows which artifact a result was detected in, but not which artifact the analysis tool was originally instructed to scan, **SHOULD** populate `result.locations` ([sec](#result-object--locations-property)), but **SHOULD NOT** attempt to populate `result.analysisTarget` ([sec](#analysistarget-property)).

- A converter **SHOULD NOT** populate the analysis tool’s `toolComponent.semanticVersion` ([sec](#semanticversion-property)) unless it knows that the tool component's version string is intended to be interpreted as a semantic version [cite](#SEMVER) version string.
