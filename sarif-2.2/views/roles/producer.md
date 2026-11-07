# Statements naming: SARIF producer

Derived by `bin/vision.py derive` from the prose and `records/roles.yaml`; do not edit.
122 statements; SHALL 39, SHALL NOT 5, SHOULD 22, SHOULD NOT 10, MAY 50.


## `text` Property

`file-format-03-artifactcontent-object.md`

- Since SARIF log files are encoded in UTF-8 ([cite](#RFC3629); see [sec](#file-format--general)), this means that if the external artifact is a text artifact in any encoding other than UTF-8, the SARIF producer **SHALL** transcode the text to UTF-8 before assigning it to the `text` property. (line 10)
- The SARIF producer **SHALL** escape any characters that JSON [cite](#RFC8259) requires to be escaped. (line 10)
- Notwithstanding any necessary transcoding and escaping, the SARIF producer **SHALL** preserve the text artifact’s line breaking convention (for example, `"\n"` or `"\r\n"`). (line 12)

## `binary` Property

`file-format-03-artifactcontent-object.md`

- If the external artifact is a binary artifact, or if the SARIF producer cannot determine whether the external artifact is a text artifact or a binary artifact, an `artifactContent` object **SHALL** contain a property named `binary` whose value is a string containing the MIME Base64 encoding [cite](#RFC2045) of the bytes in the relevant portion of the artifact. (line 18)

## Redactable Strings

`file-format-05-string-properties.md`

- If a SARIF producer or a SARIF post-processor chooses to redact sensitive information in a redactable property, it **SHALL** replace the sensitive information with a string whose value is an element of `theRun.redactionTokens` ([sec](#redactiontokens-property)). (line 15)

## Date/time Properties

`file-format-09-datetime-properties.md`

- A SARIF producer **SHOULD NOT** provide more digits in `fraction` than warranted by the precision of the clock on the computer on which it runs. (line 53)
- A SARIF producer **SHOULD** express date/time properties, except for those that express product release dates, to a precision of at least whole seconds. (line 54)

## General

`file-format-10-uri-valued-properties.md`

- Aside from normalization, SARIF producers **SHALL NOT** make any other changes to the text of a URI reference; for example, they **SHALL NOT** convert the path to upper case or to lower case. (line 22)

## Normalizing File Scheme URIs

`file-format-10-uri-valued-properties.md`

- If a URI uses the `"file"` scheme [cite](#RFC8089) and the specified path is network-accessible, the SARIF producer **SHALL** include the host name. (line 28)
- If a URI uses the `"file"` scheme and the specified path is *not* network-accessible, the SARIF producer **SHOULD NOT** include the host name. (line 34)
- A SARIF producer **MAY** choose to omit the hostname (authority) from a file URI, for example, for security reasons. (line 40)
- SARIF producers **SHALL** create `"file"` scheme URIs by means of the following procedure or any procedure with the same result: (line 42)

## Internationalized Resource Identifiers (IRIs)

`file-format-10-uri-valued-properties.md`

- If a URI-valued property refers to a resource identified by an Internationalized Resource Identifier (IRI) [cite](#RFC3987), the SARIF producer **SHALL** first transform the IRI into a URI, using the mapping mechanism specified in [sec](#file-format--general) of the standard [cite](#RFC3987), and then assign the transformed value to the property. (line 98)

## Security Implications

`file-format-11-message-object.md`

- For security reasons, SARIF producers and consumers **SHALL** adhere to the following: (line 48)
- - SARIF producers **SHALL NOT** emit messages that contain HTML, even though all variants of Markdown permit it. (line 50)

## Messages with Embedded Links

`file-format-11-message-object.md`

- However, if a sequence of literal characters in a plain text message could be parsed as an embedded link, a SARIF producer **SHOULD** escape the literal square brackets with a backslash (`"\"`) to avoid ambiguity. (line 140)
- If the `link destination` is an integer, and hence specifies a `location` object belonging to `theResult`, the tool **SHOULD** replace the integer with a string representation of the specified location. (line 200)

## `runs` Property

`file-format-13-sariflog-object.md`

- - If a SARIF producer finds no data with which to populate `runs`, then its value **SHALL** be an empty array. (line 49)
- - If a SARIF producer tries to populate `runs` but fails, then its value **SHALL** be `null`. (line 53)

## `tool` Property

`file-format-14-run-object.md`

- A `run` object **SHALL** contain a property named `tool` whose value is a `tool` object ([sec](#tool-object)) that describes the analysis tool that was run. (line 53)

## `invocations` Property

`file-format-14-run-object.md`

- A `run` object **MAY** contain a property named `invocations` whose value is an array of zero or more `invocation` objects ([sec](#invocation-object)) that together describe a single run of a single analysis tool. (line 83)

## `conversion` Property

`file-format-14-run-object.md`

- If a `run` object was produced by a converter, it **MAY** contain a property named `conversion` whose value is a `conversion` object ([sec](#conversion-object)) that describes how the converter transformed the analysis tool’s native output format into the SARIF format. (line 91)
- A direct producer **SHALL NOT** emit the `conversion` property. (line 93)

## `originalUriBaseIds` Property

`file-format-14-run-object.md`

- A `run` object **MAY** contain a property named `originalUriBaseIds` whose value is an object ([sec](#object-properties)) each of whose property names designates a URI base id ([sec](#uribaseid-property)) and each of whose property values is an `artifactLocation` object ([sec](#artifactlocation-object)) that specifies (in the manner described below) the absolute URI [cite](#RFC3986) of that URI base id on the machine where the SARIF producer ran. (line 123)

## `artifacts` Property

`file-format-14-run-object.md`

- The array **SHOULD** contain elements representing at least those artifacts in which results were detected, but it **MAY** contain elements representing all artifacts examined by the tool (whether or not results were detected in those artifacts), or any subset of those artifacts. (line 250)

## `results` Property

`file-format-14-run-object.md`

- If the tool failed to start, and if the engineering system responsible for running the tool synthesized a SARIF file to record the failure, then `results` **MAY** be present. (line 351)
- If the tool started but failed to begin its analysis (for example, because its command line was invalid), then again `results` **MAY** be present, and if present **SHALL** be `null`. (line 353)
- In all other circumstances, `results` **SHALL** be present and **SHALL** contain all results detected by the tool. (line 355)
- If the tool did not detect any results, `results` **SHALL** be an empty array. (line 355)

## `newlineSequences` Property

`file-format-14-run-object.md`

- A `run` object **MAY** contain a property named `newlineSequences` whose value is an array of one or more unique ([sec](#array-properties-with-unique-values)) strings each of which specifies a character sequence that the tool treated as a line break during this run. (line 377)
- It **SHALL** mean that at potential line breaks, the tool "greedily" attempted to match each element of the array in order. (line 381)

## `columnKind` Property

`file-format-14-run-object.md`

- If a SARIF producer processes text artifacts and `theRun.results` ([sec](#results-property)) is non-empty, the `run` object **SHALL** contain a property named `columnKind` whose value is a string that specifies the unit in which the analysis tool measures columns. (line 399)
- If a SARIF producer processes text artifacts and `theRun.results` is empty, `columnKind` **MAY** be present. (line 399)
- If the SARIF producer does not process text artifacts, `columnKind` **SHALL** be absent. (line 410)

## Properties

`file-format-15-externalpropertyfilereferences-object.md`

- The inline `driver` property **SHOULD** contain only properties that identify the tool, such as `name` ([sec](#toolcomponent-object--name-property)) and `semanticVersion` ([sec](#semanticversion-property)); it **SHOULD NOT** contain properties such as `globalMessageStrings` ([sec](#globalmessagestrings-property)), `rules` ([sec](#rules-property)), `notifications` ([sec](#notifications-property)), and `taxa` ([sec](#toolcomponent-object--taxa-property)), which take up a large amount of space. (line 165)

## `id` Property

`file-format-17-runautomationdetails-object.md`

- A result management system or other components of the engineering system **MAY** use `run.automationDetails.id` to associate the information in the log with additional information not provided by the analysis tool that produced it. (line 50)

## `guid` Property

`file-format-17-runautomationdetails-object.md`

- A result management system or other components of the engineering system **MAY** use `run.automationDetails.guid` to associate the information in the log with additional information not provided by the analysis tool that produced it. (line 70)

## General

`file-format-18-tool-object.md`

- If another tool post-processes the log file (for example, by removing certain results, or by adding information that was not known to the analysis tool), the post-processing tool **SHOULD NOT** alter any part of the tool object. (line 18)

## `driver` Property

`file-format-18-tool-object.md`

- A `tool` object **SHALL** contain a property named `driver` whose value is a `toolComponent` object ([sec](#toolcomponent-object)) that describes the component containing the tool’s primary executable file. (line 43)

## `extensions` Property

`file-format-18-tool-object.md`

- If the tool used any extensions during the run, the `tool` object **SHOULD** contain a property named `extensions` whose value is an array of one or more unique ([sec](#array-properties-with-unique-values)) `toolComponent` objects ([sec](#toolcomponent-object)) that describe those extensions. (line 46)
- If the tool did not use any extensions during the run, then `extensions` **SHALL** either be absent or an empty array. (line 46)

## `name` Property

`file-format-19-toolcomponent-object.md`

- A `toolComponent` object **SHALL** contain a property named `name` whose value is a localizable string ([sec](#localizable-strings)) containing the name of the tool component. (line 287)

## `fullName` Property

`file-format-19-toolcomponent-object.md`

- A `toolComponent` object **MAY** contain a property named `fullName` whose value is a localizable string ([sec](#localizable-strings)) containing the name of the tool component along with its version and any other useful identifying information, such as its locale. (line 297)

## `product` Property

`file-format-19-toolcomponent-object.md`

- A `toolComponent` object **MAY** contain a property named `product` whose value is a localizable string ([sec](#localizable-strings)) containing the name of the product to which the tool component belongs. (line 303)

## `productSuite` Property

`file-format-19-toolcomponent-object.md`

- A `toolComponent` object **MAY** contain a property named `productSuite` whose value is a localizable string ([sec](#localizable-strings)) containing the name of the suite of products to which the tool component belongs. (line 309)

## `semanticVersion` Property

`file-format-19-toolcomponent-object.md`

- A `toolComponent` object **MAY** contain a property named `semanticVersion` whose value is a string containing the tool component’s version in a format that conforms to the syntax and semantics specified by Semantic Versioning [cite](#SEMVER). (line 315)
- Unless the author of the converter knows that the version number of the tool from which it converts is intended to be interpreted according to Semantic Versioning [cite](#SEMVER), the converter **SHALL NOT** emit the `semanticVersion` property in `run.tool` ([sec](#run-object--tool-property)), although of course it may emit its own `semanticVersion` property (the one in `run.conversion.tool` ([sec](#conversion-object--tool-property))). (line 321)

## `version` Property

`file-format-19-toolcomponent-object.md`

- A `toolComponent` object **MAY** contain a property named `version` whose value is a string containing the tool component’s version in whatever format the component natively provides. (line 325)

## `dottedQuadFileVersion` Property

`file-format-19-toolcomponent-object.md`

- If the operating system on which the tool runs provides a value for the file version of the tool component's primary executable file, and if that value logically consists of an ordered set of four non-negative integers, then the `toolComponent` object **MAY** contain a property named `dottedQuadFileVersion` whose value is a string representation of that file version in this syntax: (line 331)

## `downloadUri` Property

`file-format-19-toolcomponent-object.md`

- A `toolComponent` object **MAY** contain a property named `downloadUri` whose value is a localizable string ([sec](#localizable-strings)) containing the absolute URI [cite](#RFC3986) from which this version of the tool component can be downloaded. (line 347)

## `informationUri` Property

`file-format-19-toolcomponent-object.md`

- A `toolComponent` object **MAY** contain a property named `informationUri` whose value is a localizable string ([sec](#localizable-strings)) containing the absolute URI [cite](#RFC3986) at which information about this version of the tool component can be found. (line 353)

## `organization` Property

`file-format-19-toolcomponent-object.md`

- A `toolComponent` object **MAY** contain a property named `organization` whose value is a localizable string ([sec](#localizable-strings)) containing the name of the company or organization that produced the tool component. (line 359)

## `shortDescription` Property

`file-format-19-toolcomponent-object.md`

- A `toolComponent` object **MAY** contain a property named `shortDescription` whose value is a localizable `multiformatMessageString` object ([sec](#multiformatmessagestring-object), [sec](#localizable-multiformatmessagestrings)) containing a brief description of the tool component. (line 365)

## `fullDescription` Property

`file-format-19-toolcomponent-object.md`

- A `toolComponent` object **MAY** contain a property named `fullDescription` whose value is a localizable `multiformatMessageString` object ([sec](#multiformatmessagestring-object), [sec](#localizable-multiformatmessagestrings)) containing a comprehensive description of the tool component. (line 371)
- The beginning of `fullDescription` (for example, its first sentence) **SHOULD** provide a concise description of the tool component, suitable for display in cases where available space is limited. (line 373)

## `rules` Property

`file-format-19-toolcomponent-object.md`

- A `toolComponent` object **MAY** contain a property named `rules` whose value is an array of zero or more unique ([sec](#array-properties-with-unique-values)) `reportingDescriptor` objects ([sec](#reportingdescriptor-object)) each of which provides information about an analysis rule supported by the tool component. (line 424)

## `notifications` Property

`file-format-19-toolcomponent-object.md`

- A `toolComponent` object **MAY** contain a property named `notifications` whose value is an array of zero or more unique ([sec](#array-properties-with-unique-values)) `reportingDescriptor` objects ([sec](#reportingdescriptor-object)) each of which provides information about a notification provided by the tool component. (line 464)

## `commandLine` Property

`file-format-20-invocation-object.md`

- An `invocation` object **MAY** contain a property named `commandLine` whose value is a string containing the completely specified command line used to invoke the tool, starting with the name of the tool's executable or script file, optionally qualified by the relative or absolute path to the file. (line 10)

## `arguments` Property

`file-format-20-invocation-object.md`

- An `invocation` object **MAY** contain a property named `arguments` whose value is either `null` or an array of zero or more strings, containing in order the command line arguments passed to the tool from the operating system. (line 40)
- An empty array **SHALL** mean that the tool was invoked with no command line arguments. (line 44)

## `responseFiles` Property

`file-format-20-invocation-object.md`

- An `invocation` object **MAY** contain a property named `responseFiles` whose value is either `null` or an array of zero or more unique ([sec](#array-properties-with-unique-values)) `artifactLocation` objects ([sec](#artifactlocation-object)) each of which represents a response file specified on the tool's command line. (line 52)
- An empty array **SHALL** mean that the tool was invoked with no command line arguments that specified response files. (line 56)
- A SARIF producer **MAY** embed the contents of a response file in the SARIF log file by mentioning the response file in `theRun.artifacts` ([sec](#artifacts-property)) and providing a value for `artifact.contents` ([sec](#artifact-object--contents-property)). (line 58)

## `exitCode` Property

`file-format-20-invocation-object.md`

- If the SARIF producer process did not exit due to a signal, an `invocation` object **SHOULD** contain a property named `exitCode` whose value is an integer specifying the process exit code. (line 102)
- If the SARIF producer process exited due to a signal, the `exitCode` property **SHALL** be absent. (line 104)

## `exitCodeDescription` Property

`file-format-20-invocation-object.md`

- If the SARIF producer process did not exit due to a signal, an `invocation` object **MAY** contain a property named `exitCodeDescription` whose value is a string describing the reason for the process exit. (line 110)

## `exitSignalName` Property

`file-format-20-invocation-object.md`

- If the SARIF producer process exited due to a signal, an `invocation` object **SHOULD** contain a property named `exitSignalName` whose value is a string containing the name of the signal that caused the process to exit. (line 132)
- If the SARIF producer process did not exit due to a signal, the `exitSignalName` property **SHALL** be absent. (line 134)

## `exitSignalNumber` Property

`file-format-20-invocation-object.md`

- If the SARIF producer process exited due to a signal, an `invocation` object **MAY** contain a property named `exitSignalNumber` whose value is an integer specifying the numeric value of the signal that caused the process to exit. (line 140)
- If the SARIF producer process did not exit due to a signal, the `exitSignalNumber` property **SHALL** be absent. (line 142)

## `processStartFailureMessage` Property

`file-format-20-invocation-object.md`

- If the analysis tool process failed to start, an `invocation` object **MAY** contain a property named `processStartFailureMessage` whose value is a string containing the operating system’s message describing the failure. (line 155)
- If the analysis tool process started successfully (regardless of whether or how it subsequently failed), the `processStartFailureMessage` property **SHALL** be absent. (line 159)

## `executionSuccessful` Property

`file-format-20-invocation-object.md`

- An `invocation` object **SHALL** contain a property named `executionSuccessful` whose value is a Boolean that is `true` if the engineering system that started the process knows that the analysis tool succeeded, and `false` if the engineering system knows that the tool failed. (line 171)

## `environmentVariables` Property

`file-format-20-invocation-object.md`

- The property names in this object **SHALL** contain the names of all the environment variables in the tool's execution environment. (line 215)

## `stdin`, `stdout`, `stderr`, and `stdoutStderr` Properties

`file-format-20-invocation-object.md`

- An `invocation` object **MAY** contain any or all of the properties `stdin`, `stdout`, `stderr`, and `stdoutStderr`, whose values are `artifactLocation` objects ([sec](#artifactlocation-object)) referring to files that contain the input to and output from the SARIF producer process. (line 301)
- A SARIF producer **MAY** embed the stream contents in the log file by mentioning the corresponding file in `theRun.artifacts` ([sec](#artifacts-property)) and providing a value for `artifact.contents` ([sec](#artifact-object--contents-property)). (line 302)

## General

`file-format-21-attachment-object.md`

- A SARIF producer **MAY** embed the contents of an attachment in the log file by mentioning the attachment in `theRun.artifacts` ([sec](#artifacts-property)) and providing a value for `artifact.contents` ([sec](#artifact-object--contents-property)). (line 8)

## `analysisToolLogFiles` Property

`file-format-22-conversion-object.md`

- If the analysis tool did not produce any per-run files, and `analysisToolLogFiles` is present, its value **SHALL** be an empty array. (line 58)

## Source language identifier conventions and practices

`file-format-24-artifact-object.md`

- To maximize interoperability, SARIF producers and consumers **SHOULD** conform to the following conventions and practices with respect to the value of this property: (line 211)

## `hashes` Property

`file-format-24-artifact-object.md`

- The string **SHALL** conform to the format produced by the hash algorithm (for example, if the hash algorithm produces a string of hexadecimal digits, the producer would not prepend "0x" to it). (line 258)

## `guid` Property

`file-format-27-result-object.md`

- Direct SARIF producers and SARIF converters **MAY** but do not need to set this property. (line 28)

## `correlationGuid` Property

`file-format-27-result-object.md`

- Direct SARIF producers and SARIF converters **SHOULD NOT** set this property. (line 36)

## `ruleId` Property

`file-format-27-result-object.md`

- Direct producers **SHALL** emit either or both of `ruleId` and `rule.id` ([sec](#rule-property), [sec](#reportingdescriptorreference-object--id-property)). (line 96)
- A SARIF converter which converts the output of such an analysis tool to the SARIF format **SHOULD** synthesize `ruleId` from other information available in the analysis tool's output. (line 100)
- Therefore, a SARIF consumer **SHOULD NOT** attempt to compare or combine the output from different converters for the same analysis tool. (line 102)

## `fingerprints` Property

`file-format-27-result-object.md`

- A direct SARIF producer **SHOULD NOT** populate this property. (line 561)
- A SARIF converter **MAY** populate this property if the analysis tool’s native output format provides a value that qualifies as a fingerprint (a stable identifier for the result). (line 561)

## `partialFingerprints` Property

`file-format-27-result-object.md`

- A SARIF producer **MAY** use the property name to identify the nature of the information used to compute the partial fingerprint. (line 573)
- Because result management systems might come to depend on the choice of property names, SARIF producers that use property names to identify the nature of the information used to compute the partial fingerprint **SHOULD** adhere to the following guidelines: (line 612)

## `precision` Property

`file-format-27-result-object.md`

- A `result` object **MAY** contain a property named `precision` whose value is a number between `0.0` and `100.0` inclusive, representing the tool or tool maintainer's confidence that this result is a true positive. (line 783)

## `hostedViewerUri` Property

`file-format-27-result-object.md`

- The URI **SHALL** be valid as of the time the tool generated this result. (line 819)

## `kind` Property

`file-format-32-address-object.md`

- When possible, SARIF producers **SHOULD** use the following values, with the specified meanings. (line 159)
- A SARIF producer **SHOULD** use the term most appropriate for the target operating system. (line 183)
- &emsp;&emsp;If none of these values are appropriate, a SARIF producer **MAY** use any value. (line 187)

## `kind` Property

`file-format-33-logicallocation-object.md`

- If none of those strings accurately describes the construct, kind **MAY** contain any value specified by the analysis tool. (line 359)

## `kinds` Property

`file-format-34-locationrelationship-object.md`

- When possible, SARIF producers **SHOULD** use the following values, with the specified meanings. (line 87)
- If none of these values are appropriate, a SARIF producer **MAY** use any value. (line 95)

## `locations` Property

`file-format-37-threadflow-object.md`

- Each element of the array **SHALL** represent a single location visited by the tool in the course of producing the result. (line 46)
- This array does not need to include every location visited by the tool, but the elements that are present **SHALL** occur in the execution order that demonstrates the problem. (line 46)

## `location` Propertyy

`file-format-38-threadflowlocation-object.md`

- A SARIF direct producer which creates such code flows **SHOULD** populate `location.message`, even if no actual location information is available. (line 109)

## `kinds` Property

`file-format-38-threadflowlocation-object.md`

- When possible, SARIF producers **SHOULD** use the following values, with the specified meanings. (line 189)
- If none of these values are appropriate, a SARIF producer **MAY** use any value. (line 263)
- A SARIF producer **MAY** provide additional kind-dependent information by populating `threadFlowLocation.properties` with properties whose names and values depend on the kind. (line 269)

## `frames` Property

`file-format-44-stack-object.md`

- This array **SHALL** include every function call in the stack for which the tool has information, and the entries that are present **SHALL** occur in chronological order with the most recent (innermost) call first and the least recent (outermost) call last. (line 14)

## `target` Property

`file-format-46-webrequest-object.md`

- A `webRequest` object **SHOULD** contain a property named `target` whose value is a string containing the target of the request, found on the HTTP request line, in the form defined by [sec](#conformance-clause-2-sarif-producer) ("Request Target") of the HTTP standard [cite](#RFC7230). (line 44)

## `invocationIndex` Property

`file-format-48-resultprovenance-object.md`

- If `theRun.invocations` ([sec](#invocations-property)) is present, a `resultProvenance` object **MAY** contain a property named `invocationIndex` whose value is the array index ([sec](#array-indices)) within the `invocations` property of the `invocation` object ([sec](#invocation-object)) that describes the tool invocation as a result of which `theResult` was detected. (line 44)

## `conversionSources` Property

`file-format-48-resultprovenance-object.md`

- If `theResult` was produced by a converter, and if the analysis tool whose output was converted to SARIF produced any per-result files for this result, then the `physicalLocation` objects in the array **SHALL** specify the relevant portions of the per-result files for this result. (line 60)

## `deprecatedIds` Property

`file-format-49-reportingdescriptor-object.md`

- A `reportingDescriptor` object **MAY** contain a property named `deprecatedIds` whose value is an array of zero or more unique ([sec](#array-properties-with-unique-values)) strings each of which contains an id (see [sec](#reportingdescriptor-object--id-property)) by which this reporting item was known in some previous version of the analysis tool. (line 32)

## `deprecatedGuids` Property

`file-format-49-reportingdescriptor-object.md`

- A `reportingDescriptor` object **MAY** contain a property named `deprecatedGuids` whose value is an array of zero or more unique ([sec](#array-properties-with-unique-values)) GUID-valued strings ([sec](#guid-valued-strings)) each of which was used by a previous version of the tool as the value of the `guid` property ([sec](#reportingdescriptor-object--guid-property)) for this object. (line 152)

## `deprecatedNames` Property

`file-format-49-reportingdescriptor-object.md`

- A `reportingDescriptor` object **MAY** contain a property named `deprecatedNames` whose value is an array of zero or more unique ([sec](#array-properties-with-unique-values)) localizable ([sec](#localizable-strings)) strings each of which was used by a previous version of the tool as the value of the `name` property ([sec](#reportingdescriptor-object--name-property)) for this object. (line 164)

## `precision` Property

`file-format-49-reportingdescriptor-object.md`

- A `reportingDescriptor` object that describes a rule **MAY** contain a property named `precision` whose value is a number between `0.0` and `100.0` inclusive, representing the tool or tool maintainer's confidence that results produced by the rule are true positives. (line 248)

## `kinds` Property

`file-format-53-reportingdescriptorrelationship-object.md`

- When possible, SARIF producers **SHOULD** use the following values, with the specified meanings. (line 110)
- If none of these values are appropriate, a SARIF producer **MAY** use any value. (line 132)

## General

`file-format-57-replacement-object.md`

- When performing a replacement in a text artifact, the SARIF producer **SHOULD** specify a text replacement rather than a binary replacement. (line 68)

## `level` Property

`file-format-58-notification-object.md`

- Analysis tools **SHOULD** treat notifications whose `level` property is `"error"` as failures and treat the entire run as having failed (for example, by settings the exit code to the value that the tool uses to indicate failure, typically a non-zero value). (line 106)
- Because a notification whose `level` property is `"error"` describes a failed run, an analysis tool **SHALL NOT** override the severity of such a notification. (line 109)

## `timeUtc` Property

`file-format-58-notification-object.md`

- A `notification` object **MAY** contain a property named `timeUtc` whose value is a string in the format specified [sec](#datetime-properties), specifying the UTC date and time at which the analysis tool generated the notification. (line 119)

## `kind` Property

`file-format-59-exception-object.md`

- If the tool does not have access to information about the object that was thrown, the `kind` property **SHALL** be absent. (line 20)

## `message` Property

`file-format-59-exception-object.md`

- If the tool does not have access to an appropriate property of the thrown object, the `message` property **SHALL** be absent. (line 26)

## Annex C Use of Fingerprints by Result Management Systems

`fingerprints.md`

- An analysis tool **SHOULD NOT** include in `partialFingerprints` information that a result management system could deduce from other information in the SARIF file, for example, file hashes. (line 22)

## Annex D Production of SARIF by Converters

`converters.md`

- - A converter that knows which artifact a result was detected in, but not which artifact the analysis tool was originally instructed to scan, **SHOULD** populate `result.locations` ([sec](#result-object--locations-property)), but **SHOULD NOT** attempt to populate `result.analysisTarget` ([sec](#analysistarget-property)). (line 22)
- - A converter **SHOULD NOT** populate the analysis tool’s `toolComponent.semanticVersion` ([sec](#semanticversion-property)) unless it knows that the tool component's version string is intended to be interpreted as a semantic version [cite](#SEMVER) version string. (line 23)
