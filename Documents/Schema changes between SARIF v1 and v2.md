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

    Add the following optional property:

    - `rule.help`

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

    Add the following optional property:

    - `physicalLocation.id`.

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

    Add the following optional properties:

    - `run.conversion` of type `conversion`
    - `result.conversionProvenance` of type array of `analysisToolLogFileContents`


- [Issue #69](https://github.com/oasis-tcs/sarif-spec/issues/69): "Provide a physicalLocation on a stack frame"

    Remove the following optional properties:

    - `stackFrame.uri`
    - `stackFrame.uriBaseId`
    - `stackFrame.line`
    - `stackrame.column`
    
    Add the following optional property:

    - `stackFrame.physicalLocation`

- [Issue #72](https://github.com/oasis-tcs/sarif-spec/issues/72): "tool.language property needs a default value"

    Specify a default value for the following optional property, which subsumes the deleted properties:

    - `tool.language`: `"en-US"`

- [Issue #81](https://github.com/oasis-tcs/sarif-spec/issues/81): "Add 'open' as a result level"

    Add an additional enumerated value `"open"` to the `result.level` property.