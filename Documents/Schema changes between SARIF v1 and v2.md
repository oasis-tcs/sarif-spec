# Schema changes between SARIF v1 and v2

This document summarizes the changes in the SARIF JSON schema between v1 (the version
defined by the initial working draft and implemented by many Microsoft tools such as its C++, C#, and VB compilers) and v2 (the first public version released by the
OASIS SARIF TC).

- Remove the following properties:

    - `annotatedCodeLocation.id`
    - `annotatedCodeLocation.essential`.

    These properties, defined in the JSON schema but marked "OBSOLETE", were holdovers from versions of the SARIF format prior to the first working draft.

- [Issue 25](https://github.com/oasis-tcs/sarif-spec/issues/25): `result.message` is not
    required.

    Issue 25 clarifies that one of `result.message` or `result.templatedMessage` is required,
    which means that the schema can't mark the `message` property as `required`.

- [Issue #27](https://github.com/oasis-tcs/sarif-spec/issues/27): "Add a help property to rule"

    In the `rule` object:

    - Add the property `help` of type `string`, optional.

- [Issue #33](https://github.com/oasis-tcs/sarif-spec/issues/33): "Should we allow formatting in messages?"

    Add the following optional properties, containing rich text messages:

    - `annotatedCodeLocation.richMessage`
    - `annotation.richMessage`
    - `codeFlow.richMessage`
    - `fix.richDescription`
    - `result.richMessage`
    - `rule.richDescription`
    - `rule.richHelp`
    - `rule.richMessageTemplates`
    - `stack.richMessage`
    - `stackFrame.richMessage`

    Due to confusion about the term "formatted message"
    (some people thought it meant "messages containing Markdown",
    although the spec originally used it to mean "messages with `{n}` replacement sequences"),
    rename the following objects:

    - `formattedMessage` &rarr; `templatedMessage`
    
    For the same reason, rename the following properties:

    - `formattedMessage.formatId` &rarr; `templatedMessage.templateId`
    - `result.formattedRuleMessage` &rarr; `result.templatedMessage`
    - `rule.messageFormats` &rarr; `rule.messageTemplates`
    
	Add the following optional property with the specified default value:

    - `run.richMessageMimeType`: `"text/markdown;variant=GFM"`.

- [Issue #61](https://github.com/oasis-tcs/sarif-spec/issues/61): "Provide a format for links embedded in our plain text messages"

    In the `physicalLocation` object:

    - Add the property `id` of type `integer`, optional.

- [Issue #66](https://github.com/oasis-tcs/sarif-spec/issues/66): "Enable traceability from converted SARIF file to original analysis tool log file"

    Define the `conversion` object with the following properties:

    - `tool` of type `tool`, required
    - `invocation` of type `invocation`, optional
    - `analysisToolLogFileUri` of type string, containing a valid URI, optional
    - `analysisToolLogFileUriBaseId` of type string, containing a URI base id, optional

    Define the `analysisToolLogFileContents` object with the following properties:

    - `region` of type `region`, optional
    - `snippet` of type `string`, optional
    - `analysisToolLogFileUri` of type string, containing a valid URI, optional
    - `analysisToolLogFileUriBaseId` of type string, containing a URI base id, optional

    In the `run` object:

    - Add the property `conversion` of type `conversion`, optional.

    In the `result` object:

    - Add the property `conversionProvenance` of type `analysisToolLogFileContents[]`, optional.

- [Issue #69](https://github.com/oasis-tcs/sarif-spec/issues/69): "Provide a physicalLocation on a stack frame"

    In the `stackFrame object`:

    - Remove the properties `uri`, `uriBaseId`, `line`, and `column`.
    - Add the property `physicalLocation` of type `physicalLocation`, optional.

- [Issue #72](https://github.com/oasis-tcs/sarif-spec/issues/72): "tool.language property needs a default value"

    Specify a default value for the following optional property, which subsumes the deleted properties:

    - `tool.language`: `"en-US"`

- [Issue #81](https://github.com/oasis-tcs/sarif-spec/issues/81): "Add 'open' as a result level"

    In the `result` object:

    - Add an additional enumerated value `"open"` to the `level` property.

- [Issue #82](https://github.com/oasis-tcs/sarif-spec/issues/82): "Add instance id to result object"

    In the `result` object:

    - Add the property `id` of type `string`, optional

- [Issue #90](https://github.com/oasis-tcs/sarif-spec/issues/82): "Introduce fileLocation object"

    Define the `fileLocation` object with the following properties:

    - `uri` of type `string`, required
    - `uriBaseId` of type `string`, optional

    In the `conversion` object:

    - Remove the properties `analysisToolLogFileUri` and `analysisToolLogFileUriBaseId`.
    - Add the property `analysisToolLogFileLocation` of type `fileLocation`, optional.

    In the `file`object:

    - Remove the properties `uri` and `uriBaseId`.
    - Add the property `fileLocation` of type `fileLocation`, optional.

    In the `analysisToolLogFileContents` object:

    - Remove the properties `analysisToolLogFileUri` and `analysisToolLogFileUriBaseId`.
    - Add the property `analysisToolLogFileLocation` of type `fileLocation`, optional.

    In the `physicalLocation` object:

    - Remove the properties `uri` and `uriBaseId`.
    - Add the property `fileLocation` of type `fileLocation`, optional.

    In the `fileChange` object:

    - Remove the properties `uri` and `uriBaseId`.
    - Add the property `fileLocation` of type `fileLocation`, optional.

- [Issue #83](https://github.com/oasis-tcs/sarif-spec/issues/83): "Consider adding attachments property"

    Define the `attachment` object with the following properties:

    - `description` of type `string`, optional.
    - `fileLocation` of type `fileLocation`, required.

    In the `invocation` object:

    - Add the property `attachments` of type `attachment[]`, optional.

    In the `result` object:

    - Add the property `attachments` of type `attachment[]`, optional.

- [Issue #94](https://github.com/oasis-tcs/sarif-spec/issues/94): "Add an invocation.arguments property"

    In the `invocation` object:

    - Add the property `arguments` of type `string[]`, optional.

- [Issue #91](https://github.com/oasis-tcs/sarif-spec/issues/91): "Represent original values for uriBaseId properties"

    In the `run` object:

    - Add the property `originalUriBaseIds`, of type `object`, with property values of type `string`.

