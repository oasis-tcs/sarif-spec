# Statements naming: no role named

Derived by `bin/vision.py derive` from the prose and `records/roles.yaml`; do not edit.
775 statements; SHALL 378, SHALL NOT 46, SHOULD 100, SHOULD NOT 5, MAY 295.


## Key Words

`document-conventions.md`

- The key words "**MUST**", "**MUST NOT**", "**REQUIRED**", "**SHALL**", "**SHALL NOT**", "**SHOULD**", "**SHOULD NOT**", "**RECOMMENDED**", "**NOT RECOMMENDED**", "**MAY**", and "**OPTIONAL**" in this document are to be interpreted as described in BCP 14 [cite](#RFC2119) and [cite](#RFC8174) when, and only when, they appear in all capitals, as shown here. (line 9)

## General

`file-format-01-general.md`

- A SARIF log file **SHALL** contain a serialization of the SARIF object model into the JSON format. (line 8)
- The top-level value in the log file, representing the `sarifLog` object, **SHALL** conform to the JSON object grammar; that is, it **SHALL** consist of a comma-separated sequence of name/value pairs, enclosed in curly brackets, as specified by JSON [cite](#RFC8259). (line 15)
- A SARIF log file **SHALL** be encoded in UTF-8 [cite](#RFC3629). (line 21)
- Regardless of future added formats, SARIF files **SHOULD NOT** contain case only variations of required properties. (line 27)

## SARIF File Naming Convention

`file-format-02-sarif-file-naming-convention.md`

- The file name of a SARIF log file **SHOULD** end with the extension `".sarif"`. (line 4)
- The file name **MAY** end with the additional extension `".json"`. (line 8)

## `text` Property

`file-format-03-artifactcontent-object.md`

- If the external artifact is a text artifact, an `artifactContent` object **SHOULD** contain a property named `text` whose value is a string containing the relevant text. (line 10)
- If the external artifact is a binary artifact, the `text` property **SHALL** be absent. (line 14)

## `binary` Property

`file-format-03-artifactcontent-object.md`

- If the external artifact is a text artifact in an encoding other than UTF-8, the `binary` property **MAY** be present, in which case it **SHALL** contain the MIME Base64 encoding of the bytes representing the relevant text in its original encoding. (line 20)
- If the external artifact is a UTF-8 text artifact, the `binary` property **SHOULD** be absent. (line 22)
- If it is present, it **SHALL** contain the MIME Base64 encoding of the UTF-8 bytes representing the relevant text. (line 22)

## `rendered` Property

`file-format-03-artifactcontent-object.md`

- An `artifactContent` object **MAY** contain a property named `rendered` whose value is a `multiformatMessageString` object ([sec](#multiformatmessagestring-object)) that provides a rendered view of the contents. (line 26)

## Constraints

`file-format-04-artifactlocation-object.md`

- At least one of the `uri` property ([sec](#uri-property)) or the `index` property ([sec](#artifactlocation-object--index-property)) **SHALL** be present. (line 10)
- In certain circumstances (see [sec](#uribaseid-property) and [sec](#artifactlocation-object--index-property)), they **MAY** both be present. (line 10)
- If both `uri` and `index` are present, they **SHALL** both denote the same artifact. (line 14)
- Then URI<sub>1</sub> and URI<sub>2</sub> **SHALL** be equivalent in the sense described in [sec](#uri-valued-properties--general). (line 14)

## `uri` Property

`file-format-04-artifactlocation-object.md`

- Depending on the circumstances, an `artifactLocation` object either **SHALL**, **SHALL NOT**, or **MAY** contain a property named `uri` whose value is a string containing a URI [cite](#RFC3986) that specifies the location of the artifact. (line 18)
- If `thisObject` describes a nested artifact whose location within its parent container can be expressed by a path from the root of the container, then if `uri` is present, it **SHALL** specify a relative-path reference per section 4.2 of [cite](#RFC3986) expressing that path. (line 20)
- A relative reference **SHALL NOT** begin with two slash characters (a ‘network-path’ reference per section 4.2 of [cite](#RFC3986). (line 20)
- A relative reference **SHALL NOT** begin with a single slash character (an ‘absolute-path’ reference per section 4.2 of [cite](#RFC3986)) unless doing so is required to distinguish between distinct items in archive formats, such as zip and tar. (line 20)
- If the nested artifact is a member of an archive file (for example, zip [cite](#ZIP) or tar [cite](#TAR)), `uri` **SHOULD** specify the member name or path as specified by the archive. (line 26)
- If `thisObject` occurs as the value of a "top-level" property in `theRun.originalBaseIds` ([sec](#originaluribaseids-property)), then `uri` **MAY** be absent. (line 28)
- If `index` ([sec](#artifactlocation-object--index-property)) is absent, `uri` **SHALL** be present. (line 30)
- If `thisObject` represents a nested artifact whose location within its parent container can be expressed only by means of a byte offset, then `uri` **SHALL NOT** be present. (line 34)
- Otherwise, `uri` **MAY** be present. (line 38)

## `uriBaseId` Property

`file-format-04-artifactlocation-object.md`

- If this `artifactLocation` object describes a top-level artifact and the value of its `uri` property ([sec](#uri-property)) is a relative reference, the `artifactLocation` object **SHOULD** contain a property named `uriBaseId` whose value is a string which indirectly specifies the absolute URI with respect to which that relative reference is interpreted. (line 42)
- If the `uri` property contains an absolute URI, the `uriBaseId` property **SHALL** be absent. (line 42)
- If this `artifactLocation` object describes a nested artifact, `uriBaseId` **SHALL** be absent. (line 42)

## `index` Property

`file-format-04-artifactlocation-object.md`

- Depending on the circumstances, an `artifactLocation` object either **MAY**, **SHALL NOT**, **SHALL**, or **SHOULD** contain a property named `index` whose value is the array index ([sec](#array-indices)) within `theRun.artifacts` ([sec](#artifacts-property)) of the `artifact` object ([sec](#artifact-object)), if any, that describes the artifact specified by this `artifactLocation` object. (line 83)
- If `thisObject` occurs as the `location` property ([sec](#artifact-object--location-property)) of an `artifact` object in `theRun.artifacts`, then `index` **MAY** be present. (line 85)
- If present, it **SHALL** equal the array index within `theRun.artifacts` of the containing `artifact` object. (line 85)
- Otherwise, if `theRun.artifacts` is absent or does not contain an element that describes the artifact specified by `thisObject`, then `index` **SHALL NOT** be present. (line 87)
- Otherwise, if the `uri` property ([sec](#uri-property)) is absent, then `index` **SHALL** be present. (line 91)
- Otherwise (that is, if `uri` is present but there *is* a relevant `artifact` object in `theRun.artifacts`), `index` **SHOULD** be present. (line 95)

## `description` Property

`file-format-04-artifactlocation-object.md`

- An `artifactLocation` object **MAY** have a property named `description` whose value is a `message` object ([sec](#message-object)) that describes this location. (line 136)

## Guidance on the Use of `artifactLocation` Objects

`file-format-04-artifactlocation-object.md`

- `artifactLocation` objects **MAY** represent both deterministic and non-deterministic URIs. (line 171)
- In either case, the `uri` property ([sec](#uri-property)) **SHOULD** be deterministic, either because it is a deterministic relative reference (for example, the relative path to a file from the root of the directory tree containing the analyzed source code) or because it is an absolute URI. (line 171)
- If the URI is non-deterministic, the `uriBaseId` property ([sec](#uribaseid-property)) **SHOULD** capture the non-deterministic portion of the URI, for example, the absolute path to the root of the directory tree containing the analyzed source code. (line 171)

## Versioned Hierarchical Strings

`file-format-05-string-properties.md`

- A hierarchical string without a version component **SHALL** be considered older than any corresponding string with a version component. (line 99)

## Object Properties

`file-format-06-object-properties.md`

- Unless otherwise specified in the description of a specific property, if any such object is empty, then either the property **SHALL** be represented as an empty object `{}`, or it **SHALL** be absent. (line 3)

## Default Value

`file-format-07-array-properties.md`

- If an array-valued property is absent, it **SHALL** default to an empty array unless the property’s description specifies otherwise. (line 10)

## Array Properties with Unique Values

`file-format-07-array-properties.md`

- When a property is so described, it means that no two elements of the array **SHALL** have equal values. (line 14)
- For purposes of this document, two array elements **SHALL** be considered equal when they satisfy the condition for equality described in the JSON Schema standard [cite](#JSCHEMA01), [sec](#externalproperties-object), "Instance equality". (line 14)

## Array Indices

`file-format-07-array-properties.md`

- If any property in this document is described as an "array index," it **SHALL** contain an integer that is a zero-based index into the specified array. (line 17)
- If any such property is absent, it **SHALL** default to -1, which indicates that the value is unknown (not set), unless the property’s description specifies otherwise. (line 17)

## General

`file-format-08-property-bags.md`

- The property values **MAY** be of any JSON type, including strings, numbers, arrays, objects, Booleans, and null. (line 10)
- If a property value is a string, it **MAY** be an empty string. (line 10)
- In addition to those properties that are explicitly documented, every object defined in this document **MAY** contain a property named `properties` whose value is a property bag. (line 12)
- If a property bag contains a property named `tags`, the property value **SHALL** be an array of zero or more unique ([sec](#array-properties-with-unique-values)), hierarchical ([sec](#hierarchical-strings)) strings. (line 18)
- Two strings **SHALL** be considered the same if they consist of the same sequence of Unicode [cite](#UNICODE12) code points. (line 18)
- Tags **SHOULD NOT** be used to label a result or a rule as belonging to a category in a classification system such as the Common Weakness Enumeration [cite](#CWE) (for example, by adding a tag `"CWE/622"`). (line 20)
- Instead, taxonomies ([sec](#taxonomies)) **SHOULD** be used for this purpose. (line 20)
- Even when defining a custom classification system used within an engineering team, taxonomies **SHOULD** be used rather than tags when labeling a result or a rule. (line 22)

## Tag Metadata

`file-format-08-property-bags.md`

- A SARIF log file **MAY** provide additional information about any tag value by including a property whose name is the same as that tag value and whose value is any JSON value. (line 50)
- If present, this property **SHALL** be located by searching first in the property bag that contains the tag, and then in the property bag of the containing `run` object ([sec](#run-object)) `theRun`, if any. (line 50)

## Date/time Properties

`file-format-09-datetime-properties.md`

- The value of every such property, if present, **SHALL** be a string in the following format, which is compatible with the ISO standard for date and time formats [cite](#ISO8601;2004): (line 4)
- The time component of every date/time-valued property **SHALL** be expressed in Coordinated Universal Time (UTC). (line 45)
- The time components of date/time-valued properties in property bags ([sec](#property-bags)) **SHOULD** also be expressed in UTC. (line 49)

## General

`file-format-10-uri-valued-properties.md`

- The value of every such property, if present, **SHALL** be a string in the format specified by the standard [cite](#RFC3986). (line 6)
- If a URI reference refers to a file stored in a version control system (VCS), its value **SHALL** include sufficient information (for example, a commit id) to enable the correct version of the target file to be retrieved from the VCS. (line 8)
- If a URI reference refers to a file stored on a physical file system, it **MAY** be specified as a relative reference that omits root information details (such as hard drive letter and an arbitrarily named root directory associated with a source code enlistment). (line 8)
- The URI **SHALL** specify the location of the artifact at the time the analysis was performed. (line 12)
- Two URI references **SHALL** be considered equivalent if their normalized forms are the same, as described in the standard [cite](#RFC3986). (line 14)

## Normalizing File Scheme URIs

`file-format-10-uri-valued-properties.md`

- If it does so, then to maximize interoperability with previous versions of the URI specification, the URI **SHOULD** start with `"file:///"`, as in EXAMPLE 2. (line 40)

## URIs That use the SARIF Scheme

`file-format-10-uri-valued-properties.md`

- The authority, query and fragment URI components **SHALL NOT** be present. (line 92)

## Internationalized Resource Identifiers (IRIs)

`file-format-10-uri-valued-properties.md`

- The string value of a URI-valued property **SHALL NOT** include Unicode characters such as `"é"`; such characters are permitted in IRIs but are not permitted in URIs. [sec](#file-format--general) of the standard [cite](#RFC3987) describes how to replace such characters with "percent-encoded" equivalents to produce a valid URI. (line 98)

## Constraints

`file-format-11-message-object.md`

- At least one of the `text` ([sec](#message-object--text-property)) or `id` ([sec](#message-object--id-property)) properties **SHALL** be present. (line 18)

## Plain Text Messages

`file-format-11-message-object.md`

- A plain text message **SHALL NOT** contain formatting information, for example, HTML tags or white space whose purpose is to provide indentation or suggest some structure to the message. (line 24)
- If a plain text message consists of multiple paragraphs, it **MAY** contain line breaks (for example, `"\r\n"` or `"\n"`, if the SARIF log file is serialized as JSON) to separate the paragraphs. (line 26)
- Line breaks **MAY** follow any convention (for example, `"\n"` or `"\r\n"`). (line 26)
- The message string **MAY** contain placeholders ([sec](#messages-with-placeholders)) and embedded links ([sec](#messages-with-embedded-links)). (line 28)
- If the message consists of more than one sentence, its first sentence **SHOULD** provide a useful summary of the message, suitable for display in cases where UI space is limited. (line 30)

## General

`file-format-11-message-object.md`

- Formatted messages **MAY** be of arbitrary length and **MAY** contain formatting information. (line 42)
- The message string **MAY** also contain placeholders ([sec](#messages-with-placeholders)) and embedded links ([sec](#messages-with-embedded-links)). (line 42)
- Formatted messages **SHALL** be expressed in GitHub-Flavored Markdown [cite](#GFM). (line 44)

## Messages with Placeholders

`file-format-11-message-object.md`

- A message string **MAY** include one or more "placeholders." The syntax of a placeholder is: (line 62)
- Within both plain text and formatted message strings, the characters "`{`" and "`}`" **SHALL** be represented by the character sequences "`{{`" and "`}}`" respectively. (line 70)
- - The plain text and formatted message strings **MAY** contain different numbers of placeholders. (line 74)
- - A given placeholder index **SHALL** have the same meaning in the plain text and formatted message strings (so they can be replaced with the same element of the `arguments` array). (line 76)

## Messages with Embedded Links

`file-format-11-message-object.md`

- A message string **MAY** include one or more links to locations within artifacts mentioned in the enclosing `result` object ([sec](#result-object)). (line 102)
- Within a formatted message ([sec](#formatted-messages)), an embedded link **SHALL** conform to the syntax of a GitHub Flavored Markdown link (see [cite](#GFM), §6.6, "Links"). (line 104)
- Within a plain text message ([sec](#plain-text-messages)), an embedded link **SHALL** conform to the following syntax (which is a greatly restricted subset of the GFM link syntax) before JSON encoding: (line 108)
- Literal square brackets ("`[`" and "`]`") in the link text of a plain text message **SHALL** be escaped with a backslash (`"\"`). (line 126)
- Literal square brackets and backslashes anywhere else in a plain text message **MAY** be written either without escaping, or escaped with a backslash (`"\"`). (line 140)
- In both plain text and formatted messages, if `link destination` is a non-negative integer, it **SHALL** refer to a `location` object ([sec](#location-object)) whose `id` property ([sec](#location-object--id-property)) equals the value of `link destination`. (line 148)
- In this case, `theResult` **SHALL** contain exactly one `location` object with that `id`. (line 148)
- The `link destination` in embedded links in both plain text messages and formatted messages **MAY** use the `sarif` URI scheme ([sec](#uris-that-use-the-sarif-scheme)). (line 186)
- When a tool displays on the console a result message containing an embedded link, it **MAY** reformat the link (for example, by removing the square brackets around the `link text`). (line 200)

## Message String Lookup

`file-format-11-message-object.md`

- The `run` object **SHALL** contain enough information for the procedure to succeed. (line 224)
- The lookup **SHALL** occur entirely within the context of a single `toolComponent` object ([sec](#toolcomponent-object)) which we refer to as `theComponent`. (line 226)

## `text` Property

`file-format-11-message-object.md`

- A `message` object **MAY** contain a property named `text` whose value is a non-empty string containing a plain text message ([sec](#plain-text-messages)). (line 274)

## `markdown` Property

`file-format-11-message-object.md`

- A `message` object **MAY** contain a property named `markdown` whose value is a non-empty string containing a formatted message ([sec](#formatted-messages)) expressed in GitHub-Flavored Markdown [cite](#GFM). (line 278)
- If the `markdown` property is present, the `text` property ([sec](#message-object--text-property)) **SHALL** also be present. (line 280)

## `id` Property

`file-format-11-message-object.md`

- A `message` object **MAY** contain a property named `id` whose value is a non-empty string containing the identifier for the desired message. (line 288)

## `arguments` Property

`file-format-11-message-object.md`

- If none of the properties `text`, `markdown`, or `id` contains any placeholders, then `arguments` **MAY** be absent. (line 294)
- The `arguments` array **SHALL** contain as many elements as required by the maximum placeholder index among all the message strings specified by the `text`, `markdown`, and `id` properties. (line 296)

## `text` Property

`file-format-12-multiformatmessagestring-object.md`

- A `multiformatMessageString` object **SHALL** contain a property named `text` whose value is a non-empty string containing a plain text representation of the message including any links. (line 14)

## `markdown` Property

`file-format-12-multiformatmessagestring-object.md`

- A `multiformatMessageString` object **MAY** contain a property named `markdown` whose value is a non-empty string containing a formatted message ([sec](#formatted-messages)) expressed in GitHub-Flavored Markdown [cite](#GFM). (line 20)

## `version` Property

`file-format-13-sariflog-object.md`

- A `sarifLog` object **SHALL** contain a property named `version` whose value is a string designating the version of the SARIF specification to which this log file conforms. (line 27)
- This string **SHALL** have the value `"2.2"`. (line 27)
- Although the order in which properties appear in a JSON object value is not semantically significant, the `version` property **SHOULD** appear first. (line 29)

## `$schema` Property

`file-format-13-sariflog-object.md`

- A `sarifLog` object **MAY** contain a property named `$schema` whose value is a string containing an absolute URI from which a JSON schema document [cite](#JSCHEMA01) describing the version of the SARIF format to which this log file conforms can be obtained. (line 35)
- If the `$schema` property is present, the JSON schema obtained from the specified URI **SHALL** describe the version of the SARIF format specified by the `version` property ([sec](#sariflog-object--version-property)). (line 37)

## `runs` Property

`file-format-13-sariflog-object.md`

- A `sarifLog` object **SHALL** contain a property named `runs` whose value is either `null` or an array of zero or more `run` objects ([sec](#run-object)). (line 45)
- The value of `runs` **SHALL** be an array with at least one element except in the following circumstances: (line 47)

## `inlineExternalProperties` Property

`file-format-13-sariflog-object.md`

- A `sarifLog` object **MAY** contain a property named `inlineExternalProperties` whose value is an array of zero or more unique ([sec](#array-properties-with-unique-values)) `externalProperties` objects ([sec](#externalproperties-object)). (line 59)

## `guid` Property

`file-format-13-sariflog-object.md`

- A `sarifLog` object **SHOULD** contain a property named `guid` whose value is a GUID-valued string ([sec](#guid-valued-strings)) that provides a unique, stable identifier for the `sarifLog` designating that the log itself has a conceptual identity as a bundle of tool runs for tracking a SARIF log through a distributed results processing pipeline. (line 135)

## `externalPropertyFileReferences` Property

`file-format-14-run-object.md`

- A `run` object **MAY** contain a property named `externalPropertyFileReferences` whose value is an `externalPropertyFileReferences` object ([sec](#externalpropertyfilereferences-object)) that specifies the locations of the external property files (see [sec](#rationale)) associated with this log file. (line 29)

## `automationDetails` Property

`file-format-14-run-object.md`

- A `run` object **MAY** contain a property named `automationDetails` whose value is a `runAutomationDetails` object ([sec](#runautomationdetails-object)) that describes this run. (line 33)

## `runAggregates` Property

`file-format-14-run-object.md`

- A `run` object **MAY** contain a property named `runAggregates` whose value is an array of zero or more unique ([sec](#array-properties-with-unique-values)) `runAutomationDetails` objects ([sec](#runautomationdetails-object)) each of which describes an aggregate of runs to which this run belongs. (line 39)

## `baselineGuid` Property

`file-format-14-run-object.md`

- A `run` object **MAY** contain a property named `baselineGuid` whose value is a GUID-valued string ([sec](#guid-valued-strings)) which **SHALL** equal the `automationDetails.guid` property ([sec](#automationdetails-property), [sec](#runautomationdetails-object--guid-property)) of some previous run. (line 45)
- If `baselineGuid` is present, the `result.baselineState` property ([sec](#baselinestate-property)) of every `result` object ([sec](#result-object)) in `theRun` **SHALL** be computed with respect to the run specified by `baselineGuid`. (line 49)

## `language` Property

`file-format-14-run-object.md`

- A `run` object **MAY** contain a property named `language` whose value is a string specifying the language of the localizable strings ([sec](#localizable-strings)) in `theRun` (except for localizable strings that occur within `theRun.translations` ([sec](#translations-property))), in the format specified by the language tags standard [cite](#RFC5646). (line 57)
- If this property is absent, it **SHALL** default to `"en-US"`. (line 57)

## `taxonomies` Property

`file-format-14-run-object.md`

- A `run` object **MAY** contain a property named `taxonomies` whose value is an array of zero or more unique ([sec](#array-properties-with-unique-values)) `toolComponent` objects ([sec](#toolcomponent-object)) each of which represents a standard taxonomy ([sec](#taxonomies)). (line 69)

## `translations` Property

`file-format-14-run-object.md`

- A `run` object **MAY** contain a property named `translations` whose value is an array of zero or more unique ([sec](#array-properties-with-unique-values)) `toolComponent` objects ([sec](#toolcomponent-object)) each of which represents a translation ([sec](#translations)). (line 75)

## `policies` Property

`file-format-14-run-object.md`

- A `run` object **MAY** contain a property named `policies` whose value is an array of zero or more unique ([sec](#array-properties-with-unique-values)) `toolComponent` objects ([sec](#toolcomponent-object)) each of which represents a policy ([sec](#policies)). (line 79)

## `invocations` Property

`file-format-14-run-object.md`

- The elements of the `invocations` array **SHOULD**, as far as possible, be arranged in chronological order according to the start time of each process. (line 87)

## `versionControlProvenance` Property

`file-format-14-run-object.md`

- A `run` object **MAY** contain a property named `versionControlProvenance` whose value is an array of zero or more unique ([sec](#array-properties-with-unique-values)) `versionControlDetails` objects ([sec](#versioncontroldetails-object)). (line 97)

## `originalUriBaseIds` Property

`file-format-14-run-object.md`

- If the `artifactLocation` object’s `uri` property ([sec](#uri-property)) is a relative reference, its `uriBaseId` property ([sec](#uribaseid-property)) **SHALL** be present. (line 125)
- Otherwise (that is, if `uri` is an absolute URI, or if it is absent), `uriBaseId` **SHALL** be absent. (line 125)
- If the actual value of `uri` would have been an absolute URI, `uri` **MAY** be omitted. (line 127)
- The values of the `uriBaseId` properties in the `artifactLocation` objects in `originalUriBaseIds` **SHALL NOT** form a loop, in the sense described in the URI base id resolution procedure below. (line 174)
- - **SHALL** end with a single forward slash . (line 178)
- - **SHALL NOT** include a query or fragment component as defined in URI Generic Syntax [cite](#RFC3986). (line 180)
- - **SHALL NOT** include `".."` path segments. (line 182)

## `artifacts` Property

`file-format-14-run-object.md`

- A `run` object **MAY** contain a property named `artifacts` whose value is an array of zero or more unique ([sec](#array-properties-with-unique-values)) `artifact` objects ([sec](#artifact-object)) each of which represents an artifact relevant to the run. (line 248)
- It **MAY** also include other artifacts relevant to the run, such as attachments ([sec](#attachments-property)). (line 250)
- If a nested artifact appears in the `artifacts` array, then the `artifacts` array **SHALL** also contain elements describing each of its parents, up to and including the top-level artifact. (line 272)

## `logicalLocations` Property

`file-format-14-run-object.md`

- A `run` object **MAY** contain a property named `logicalLocations` whose value is an array of zero or more unique ([sec](#array-properties-with-unique-values)) `logicalLocation` objects ([sec](#logicallocation-object)) each of which represents a logical location relevant to one or more results detected during the run. (line 280)
- If a nested logical location appears in the `logicalLocations` array, then the `logicalLocations` array **SHALL** also contain elements describing each of its parents, up to and including the top-level logical location. (line 284)

## `addresses` Property

`file-format-14-run-object.md`

- A `run` object **MAY** contain a property named `addresses` whose value is an array of zero or more unique ([sec](#array-properties-with-unique-values)) `address` objects ([sec](#address-object)) representing addresses that appear in `physicalLocation` objects ([sec](#physicallocation-object)) within `theRun`. (line 313)
- If a nested address appears in the `addresses` array, then `addresses` **SHALL** also contain elements describing each of its parents, up to and including the top-level address. (line 317)

## `threadFlowLocations` Property

`file-format-14-run-object.md`

- A `run` object **MAY** contain a property named `threadFlowLocations` whose value is an array of zero or more unique ([sec](#array-properties-with-unique-values)) `threadFlowLocation` objects ([sec](#threadflowlocation-object)) representing locations that appear in `threadFlow` objects ([sec](#threadflow-object)) within `theRun`. (line 321)

## `graphs` Property

`file-format-14-run-object.md`

- A `run` object **MAY** contain a property named `graphs` whose value is an array of zero or more unique ([sec](#array-properties-with-unique-values)) `graph` objects ([sec](#graph-object)). (line 329)
- A `graph` object defined at the `run` level **MAY** be referenced by a `graphTraversal` object ([sec](#graphtraversal-object)) defined in the `graphTraversals` property ([sec](#graphtraversals-property)) of any `result` object ([sec](#result-object)) in `theRun`. (line 331)

## `webRequests` Property

`file-format-14-run-object.md`

- A `run` object **MAY** contain a property named `webRequests` whose value is an array of zero or more unique ([sec](#array-properties-with-unique-values)) `webRequest` objects ([sec](#webrequest-object)) representing HTTP requests that appear in `result` objects ([sec](#result-object)) within `theRun`. (line 335)

## `webResponses` Property

`file-format-14-run-object.md`

- A `run` object **MAY** contain a property named `webResponses` whose value is an array of zero or more unique ([sec](#array-properties-with-unique-values)) `webResponse` objects ([sec](#webresponse-object)) representing HTTP responses that appear in `result` objects ([sec](#result-object)) within `theRun`. (line 341)

## `results` Property

`file-format-14-run-object.md`

- Depending on the circumstances, a `run` object either **SHALL** or **MAY** contain a property named `results` whose value, again depending on circumstances, is either `null` or an array of zero or more `result` objects ([sec](#result-object)) each of which represents a single result detected in the course of the run. (line 347)
- If it is present, its value **SHALL** be `null`. (line 351)
- If `results` is absent, it **SHALL** default to `null`. (line 357)

## `defaultEncoding` Property

`file-format-14-run-object.md`

- A `run` object **MAY** contain a property named `defaultEncoding` whose value is a case-sensitive string that provides a default for the `encoding` property ([sec](#encoding-property)) of any `artifact` object ([sec](#artifact-object)) in `theRun.artifacts` ([sec](#artifacts-property)) that refers to a text artifact. (line 361)
- The string **SHALL** be one of the character set names defined by IANA [cite](#IANA-ENC). (line 361)
- If this property is absent, it **SHALL** be interpreted as meaning that there is no default file encoding. (line 363)
- In that case, the encoding of any `artifact` object that does not contain an `encoding` property **SHALL** be taken to be unknown. (line 363)

## `defaultSourceLanguage` Property

`file-format-14-run-object.md`

- A `run` object **MAY** contain a property named `defaultSourceLanguage` whose value is a hierarchical string ([sec](#hierarchical-strings)) that provides a default value for the `sourceLanguage` property ([sec](#artifact-object--sourcelanguage-property)) of any `artifact` object ([sec](#artifact-object)) in `theRun.artifacts` ([sec](#artifacts-property)) which refers to a text artifact that contains source code. (line 369)
- If `defaultSourceLanguage` is present, its value **SHOULD** conform to the conventions defined in [sec](#source-language-identifier-conventions-and-practices). (line 371)
- If `defaultSourceLanguage` is absent, it **SHALL** be taken to mean that there is no default source language. (line 373)
- In that case, the source language of any `artifact` object that does not contain a `sourceLanguage` property **SHALL** be taken to be unknown. (line 373)

## `newlineSequences` Property

`file-format-14-run-object.md`

- If this property is absent, it **SHALL** default to the array `[ "\r\n", "\n" ]`. (line 379)

## `columnKind` Property

`file-format-14-run-object.md`

- `columnKind` **SHALL** have one of the following values, with the specified meanings: (line 401)

## `redactionTokens` Property

`file-format-14-run-object.md`

- If the value of any redactable property ([sec](#redactable-strings)) in `theRun` has been redacted, `theRun` **SHALL** contain a property named `redactionTokens` whose value is an array of zero or more unique ([sec](#array-properties-with-unique-values)) strings any of which can be used to replace redacted text. (line 416)
- If no text in `theRun` has been redacted, `redactionTokens` **SHALL** be absent. (line 416)
- If `redactionTokens` contains a single element, that element **SHOULD** be the string `"[REDACTED]"`; if it contains more than one, each additional element **SHOULD** be of the form `"[REDACTED-`*n*`]"` where *n* is a positive integer. (line 418)
- If for any reason different values are used, they **MAY** be any readily identifiable strings. (line 424)

## Properties

`file-format-15-externalpropertyfilereferences-object.md`

- Every externalizable property whose type is shown in the table as "object" **SHALL**, if externalized, be stored in a single external property file. (line 55)
- In that case, the value of the corresponding property in `externalPropertyFileReferences` **SHALL** be an `externalPropertyFileReference` object ([sec](#externalpropertyfilereference-object)) specifying the location of the external property file. (line 55)
- Every externalizable property whose type is shown in the table as "array" **SHALL**, if externalized, be stored in one or more external property files. (line 57)
- In that case, the value of the corresponding property in `externalPropertyFileReferences` **SHALL** be an array of zero or more `externalPropertyFileReference` objects specifying the locations of those external property files. (line 57)
- With one exception described below, if a property appears inline in the root file, its name **SHALL NOT** appear as one of the property names in `externalPropertyFileReferences`. (line 99)
- Since an external property file can contain multiple externalized properties, `externalPropertyFileReference` objects belonging to distinct properties **MAY** denote the same external property file. (line 99)
- However, if an array-valued externalizable property is divided among multiple external property files, the `externalPropertyFileReference` objects belonging to that property **SHALL** denote distinct external property files. (line 99)
- The exception is that if `run.tool.driver` is externalized, it **SHALL** still occur inline in the root file. (line 165)

## Constraints

`file-format-16-externalpropertyfilereference-object.md`

- At least one of the `location` property ([sec](#externalpropertyfilereference-object--location-property)) or the `guid` property ([sec](#externalpropertyfilereference-object--guid-property)) **SHALL** be present. (line 10)
- If both are present, they **SHALL** identify the same set of externalized properties (possibly located inline; see [sec](#inlineexternalproperties-property)). (line 10)

## `location` Property

`file-format-16-externalpropertyfilereference-object.md`

- Depending on the circumstances, an `externalPropertyFileReference` object either **SHALL** or **MAY** contain a property named `location` whose value is an `artifactLocation` object ([sec](#artifactlocation-object)) that specifies the location of the external property file. (line 16)
- If the externalized properties are persisted in a separate file, `location` **SHALL** be present. (line 18)
- In that case, if the `artifactLocation` object’s `uri` property ([sec](#uri-property)) specifies a relative reference and its `uriBaseId` property ([sec](#uribaseid-property)) is absent, then `uri` **SHALL** be interpreted relative to the location of the root file. (line 18)
- Otherwise (that is, if the externalized properties are persisted as an element of `theSarifLog.inlineExternalProperties` ([sec](#inlineexternalproperties-property))), then `location` **MAY** be present. (line 20)
- If `location` is present, its `uri` property **SHALL** resolve to an absolute URI using the `sarif` scheme ([sec](#uris-that-use-the-sarif-scheme)). (line 20)

## `guid` Property

`file-format-16-externalpropertyfilereference-object.md`

- Depending on the circumstances, an `externalPropertyFileReference` object either **SHALL** or **MAY** contain a property named `guid` whose value is a GUID-valued string ([sec](#guid-valued-strings)) which provides a unique, stable identifier for the external property file. (line 24)
- If the externalized properties are persisted in an element of `theSarifLog.inlineExternalProperties` ([sec](#inlineexternalproperties-property)) and `location` ([sec](#externalpropertyfilereference-object--location-property)) is absent, then `guid` **SHALL** be present. (line 26)
- Otherwise (that is, if the externalized properties are persisted in a separate file, in which case `location` is required, or if the externalized properties are persisted in an element of `theSarifLog.inlineExternalProperties` but `location` is present), guid **MAY** be present. (line 28)
- If `guid` is present, it **SHALL** equal the `guid` property ([sec](#externalproperties-object--guid-property)) of the `externalProperties` object ([sec](#externalproperties-object)) identified by `guid` and/or `location`. (line 32)

## `itemCount` Property

`file-format-16-externalpropertyfilereference-object.md`

- If an `externalPropertyFileReference` object specifies an external property file that contains all or a portion of an array-valued property, it **MAY** contain a property named `itemCount` whose value is a non-negative integer that specifies the number of items in the externalized property array in that file. (line 36)
- If the `externalPropertyFileReference` object specifies an external property file that contains an object-valued property, `itemCount` **SHALL** be absent. (line 36)
- If `itemCount` is absent, it **SHALL** default to -1, which indicates that the value is unknown (not set). (line 38)

## `id` Property

`file-format-17-runautomationdetails-object.md`

- The trailing component of `id` **MAY** be empty; note that the grammar for a hierarchical identifier ([sec](#hierarchical-strings--general)) permits any component to be empty. (line 58)
- This **SHALL** be taken to signify that the run belongs to the specified category, but that the run itself has no unique identifier. (line 58)
- `id` **MAY** consist of a single component. (line 62)
- This **SHALL** be taken to specify a unique identifier for the run, withough specifying any category that the run belongs to. (line 62)

## `guid` Property

`file-format-17-runautomationdetails-object.md`

- A `runAutomationDetails` object **MAY** contain a property named `guid` whose value is a GUID-valued string ([sec](#guid-valued-strings)) that provides a unique, stable identifier for `theRun`. (line 68)

## `correlationGuid` Property

`file-format-17-runautomationdetails-object.md`

- A `runAutomationDetails` object **MAY** contain a property named `correlationGuid` whose value is a GUID-valued string ([sec](#guid-valued-strings)) which is shared by all such runs of the same type, and differs between any two runs of different types. (line 74)
- If `id` ([sec](#runautomationdetails-object--id-property)) is present, `correlationGuid` **SHALL** identify the category of runs specified by all but the last hierarchical component (which **MAY** be empty according to the grammar ([sec](#hierarchical-strings--general)) for hierarchical strings) of `id`. (line 76)

## Constraints

`file-format-19-toolcomponent-object.md`

- At least one of `version` ([sec](#toolcomponent-object--version-property)) and `semanticVersion` ([sec](#semanticversion-property)) **SHOULD** be present. (line 20)

## Taxonomies

`file-format-19-toolcomponent-object.md`

- Standard taxonomies **SHALL** be stored in the `run.taxonomies` array ([sec](#taxonomies-property)). (line 30)
- Every `toolComponent` object in this array **SHALL** contain a `taxa` property ([sec](#toolcomponent-object--taxa-property)), and **SHALL NOT** contain `rules` ([sec](#rules-property)) or `notifications` ([sec](#notifications-property)) properties. (line 30)
- Such a `toolComponent` object **MAY** still contain `rules` and/or `notifications` as usual. (line 32)

## Translations

`file-format-19-toolcomponent-object.md`

- Translations **SHALL** be stored in the `run.translations` array ([sec](#translations-property)). (line 154)
- A translation **SHALL** specify the component that it translates by way of its `associatedComponent` property ([sec](#associatedcomponent-property)). (line 156)
- `associatedComponent` **SHALL NOT** refer to another translation. (line 156)
- A translation component **SHALL** contain the translations of every localizable string in the translated component, even if the translated string is identical to the original string. (line 158)
- It **MAY** contain additional strings that do not appear in the translated component. (line 158)
- A translation **SHOULD** include the value `"localizedData"` in its `contents` array ([sec](#toolcomponent-object--contents-property)). (line 162)
- It **MAY** also include the value `"nonLocalizedData"`. (line 162)
- To facilitate the identification of translations that are associated with a given component, a `toolComponent` **SHOULD** populate its `guid` property ([sec](#toolcomponent-object--guid-property)), and a translation for that component **SHOULD** set its `guid` property to the same value. (line 164)
- To ensure that new translations are created only when necessary, a translation component **SHOULD** populate `localizedDataSemanticVersion` ([sec](#localizeddatasemanticversion-property)), and a translatable component **SHOULD** populate `minimumRequiredLocalizedDataSemanticVersion` ([sec](#minimumrequiredlocalizeddatasemanticversion-property)). (line 166)

## Policies

`file-format-19-toolcomponent-object.md`

- A policy **SHALL** contain a `rules` property ([sec](#rules-property)), each `reportingDescriptor`-valued ([sec](#reportingdescriptor-object)) element of which in turn contains a `defaultConfiguration` property ([sec](#defaultconfiguration-property)). (line 222)
- Each element of the `rules` array **SHALL** correspond to a rule defined by the associated component. (line 222)
- The `rules` array **MAY** contain elements describing any or all of the rules defined by the associated component. (line 222)
- The elements of the `rules` array **MAY** alter rule properties such as `level` ([sec](#reportingconfiguration-object--level-property)), and **MAY** enable or disable rules. (line 222)
- Policies **SHALL** be stored in the `run.policies` array ([sec](#policies-property)). (line 224)

## `guid` Property

`file-format-19-toolcomponent-object.md`

- A `toolComponent` object **MAY** contain a property named `guid` whose value is a GUID-valued string ([sec](#guid-valued-strings)) that provides a unique, stable identifier for the component. (line 279)
- `guid` **SHALL NOT** vary between versions of a given component. (line 279)

## `dottedQuadFileVersion` Property

`file-format-19-toolcomponent-object.md`

- If the operating system does not provide such a value, the `dottedQuadFileVersion` property **SHALL** be absent. (line 337)

## `releaseDateUtc` Property

`file-format-19-toolcomponent-object.md`

- A `toolComponent` object **MAY** contain a property named `releaseDateUtc` whose value is a string in the format specified in [sec](#datetime-properties), specifying the UTC date (and optionally, the time) of the component’s release. (line 343)

## `shortDescription` Property

`file-format-19-toolcomponent-object.md`

- The `shortDescription` property **SHOULD** be a single sentence that is understandable when visible space is limited to a single line of text. (line 367)

## `fullDescription` Property

`file-format-19-toolcomponent-object.md`

- Tools that do not construct `fullDescription` in this way **SHOULD** provide a value for `shortDescription`. (line 373)

## `language` Property

`file-format-19-toolcomponent-object.md`

- Depending on the circumstances, a `toolComponent` object either **SHALL** or **MAY** contain a property named `language` whose value is a string specifying the language of the localizable strings ([sec](#localizable-strings)) contained in the component (except for those in the `translationMetadata` property ([sec](#translationmetadata-property))), in a subset of the format specified by the language tags standard [cite](#RFC5646). (line 379)
- If this object represents a translation (see [sec](#translations)), `language` **SHALL** be present; otherwise it **MAY** be present. (line 387)
- If this property is absent, it **SHALL** default to `"en-US"`. (line 389)

## `globalMessageStrings` Property

`file-format-19-toolcomponent-object.md`

- A `toolComponent` object **MAY** contain a property named `globalMessageStrings` whose value is an object ([sec](#object-properties)) each of whose property values is a localizable `multiformatMessageString` object ([sec](#multiformatmessagestring-object), [sec](#localizable-multiformatmessagestrings)). (line 401)

## `taxa` Property

`file-format-19-toolcomponent-object.md`

- A `toolComponent` object **MAY** contain a property named `taxa` whose value is an array of zero or more unique ([sec](#array-properties-with-unique-values)) `reportingDescriptor` objects ([sec](#reportingdescriptor-object)) each of which provides information about a taxon defined by the component. (line 500)
- If the `toolComponent` describes a standard taxonomy (for example, the Common Weakness Enumeration \[[CWE](#CWE)\]), it **SHALL NOT** contain `rules` ([sec](#rules-property)) or `notifications` ([sec](#notifications-property)). (line 502)
- If the `toolComponent` describes a tool driver or plugin that defines its own custom taxonomy, it **MAY** contain all of `rules`, `notifications`, and `taxa`. (line 506)

## `supportedTaxonomies` Property

`file-format-19-toolcomponent-object.md`

- A `toolComponent` object **MAY** contain a property named `supportedTaxonomies` whose value is an array of zero or more unique ([sec](#array-properties-with-unique-values)) `toolComponentReference` objects ([sec](#toolcomponentreference-object)) each of which refers to a taxonomy ([sec](#taxonomies)) that the component uses to classify results. (line 540)
- A `toolComponent` object that contains a `supportedTaxonomies` property **SHALL** declare which taxa (if any) each of its rules falls into by providing the `relationships` property ([sec](#reportingdescriptor-object--relationships-property)) as appropriate on each `reportingDescriptor` object ([sec](#reportingdescriptor-object)) in its `rules` array ([sec](#rules-property)). (line 542)
- If a `toolComponent` supports a custom taxonomy, it **SHOULD** include a reference to itself in `supportedTaxonomies`. (line 546)

## `translationMetadata` Property

`file-format-19-toolcomponent-object.md`

- If a `toolComponent` object represents a translation ([sec](#translations)), it **SHALL** contain a property named `translationMetadata` whose value is a `translationMetadata` object ([sec](#translationmetadata-object)) that contains descriptive information about the translation itself, as opposed to describing the component whose localizable strings ([sec](#localizable-strings)) it translates. (line 593)
- Otherwise, `translationMetadata` **SHALL** be absent. (line 593)

## `locations` Property

`file-format-19-toolcomponent-object.md`

- A `toolComponent` object **MAY** contain a property named `locations` whose value is an array of zero or more unique ([sec](#array-properties-with-unique-values)) `artifactLocation` objects ([sec](#artifactlocation-object)) each of which specifies the location of one of the files comprising this tool component. (line 597)

## `contents` Property

`file-format-19-toolcomponent-object.md`

- A `toolComponent` object **SHOULD** contain a property named `contents` whose value is an array of zero or more unique ([sec](#array-properties-with-unique-values)) strings each of which is one of the following values with the specified meanings: (line 601)
- If `contents` is absent, it **SHALL** default to `[ "localizedData", "nonLocalizedData" ]`. (line 607)

## `isComprehensive` Property

`file-format-19-toolcomponent-object.md`

- A `toolComponent` object **SHOULD** contain a property named `isComprehensive` whose value is a Boolean that is `true` if the component contains complete information for the content types specified by `contents` ([sec](#toolcomponent-object--contents-property)) and `false` otherwise. (line 615)
- If `isComprehensive` is absent, it **SHALL** default to `false`. (line 617)

## `localizedDataSemanticVersion` Property

`file-format-19-toolcomponent-object.md`

- If a `toolComponent` object represents a translation ([sec](#translations)), it **SHOULD** contain a property named `localizedDataSemanticVersion` whose value is a string that specifies the semantic version [cite](#SEMVER) of the translated strings. (line 625)
- Otherwise, `localizedDataSemanticVersion` **MAY** be present, in which case it represents the semantic version of the localizable strings ([sec](#localizable-strings)) that are present in this component. (line 625)
- If `localizedDataSemanticVersion` is absent, it **SHALL** default to `thisObject.semanticVersion` ([sec](#semanticversion-property)). (line 627)

## `minimumRequiredLocalizedDataSemanticVersion` Property

`file-format-19-toolcomponent-object.md`

- If a `toolComponent` object does not represent a translation ([sec](#translations)), it **SHOULD** contain a property named `minimumRequiredLocalizedDataSemanticVersion` whose value is a string that specifies the minumum semantic version [cite](#SEMVER) of the translated strings that it requires. (line 635)
- Otherwise, `minimumRequiredLocalizedDataSemanticVersion` **SHALL** be absent. (line 635)
- If `minimumRequiredLocalizedDataSemanticVersion` is absent, it **SHALL** default to `thisObject.semanticVersion` ([sec](#semanticversion-property)). (line 637)

## `associatedComponent` Property

`file-format-19-toolcomponent-object.md`

- If this `toolComponent` object represents a plugin (see [sec](#tool-object--general)), a taxonomy ([sec](#taxonomies)), a translation ([sec](#translations)), or a policy ([sec](#policies)), it **MAY** contain a property named `associatedComponent` whose value is a `toolComponentReference` object ([sec](#toolcomponentreference-object)) which identifies the component (either `theTool.driver` ([sec](#driver-property)) or an element of `theTool.extensions` ([sec](#extensions-property))) to which this plugin, translation, or policy applies. (line 669)
- If `associatedComponent` is absent, it **SHALL** default to a reference to `theTool.driver`. (line 669)
- The associated `toolComponent` object **MAY** itself contain an `associatedComponent` property; for example, a translation might be associated with a plugin which in turn is associated with the driver (see [sec](#tool-object--general)). (line 672)

## arguments property

`file-format-20-invocation-object.md`

- If `arguments` is absent, it **SHALL** default to `null`. (line 42)
- `null` **SHALL** mean that the command line arguments, if any, are not known. (line 44)

## `responseFiles` Property

`file-format-20-invocation-object.md`

- If `responseFiles` is absent, it **SHALL** default to `null`. (line 54)
- `null` **SHALL** mean that it is not known whether any command line arguments specified a response file. (line 56)

## `ruleConfigurationOverrides` Property

`file-format-20-invocation-object.md`

- An `invocation` object **MAY** contain a property named `ruleConfigurationOverrides` whose value is an array of zero or more unique ([sec](#array-properties-with-unique-values)) `configurationOverride` objects ([sec](#configurationoverride-object)) each of which overrides the `defaultConfiguration` property ([sec](#defaultconfiguration-property)) of a `reportingDescriptor` object ([sec](#conversionsources-property)) that describes a rule (that is, a `reportingDescriptor` object that is an array element of the `rules` property ([sec](#rules-property)) of some `toolComponent` object ([sec](#toolcomponent-object))). (line 86)

## `notificationConfigurationOverrides` Property

`file-format-20-invocation-object.md`

- An `invocation` object **MAY** contain a property named `notificationConfigurationOverrides` whose value is an array of zero or more unique ([sec](#array-properties-with-unique-values)) `configurationOverride` objects ([sec](#configurationoverride-object)) each of which overrides the `defaultConfiguration` property ([sec](#defaultconfiguration-property)) of a `reportingDescriptor` object ([sec](#reportingdescriptor-object)) that describes a notification (that is, a `reportingDescriptor` object that is an array element of the `notifications` property ([sec](#notifications-property)) of some `toolComponent` object ([sec](#toolcomponent-object))). (line 90)

## `startTimeUtc` Property

`file-format-20-invocation-object.md`

- An `invocation` object **MAY** contain a property named `startTimeUtc` whose value is a string in the format specified in [sec](#datetime-properties), specifying the UTC date and time at which the invocation started. (line 94)

## `endTimeUtc` Property

`file-format-20-invocation-object.md`

- An `invocation` object **MAY** contain a property named `endTimeUtc` whose value is a string in the format specified in [sec](#datetime-properties), specifying the UTC date and time at which the invocation ended. (line 98)

## `machine` Property

`file-format-20-invocation-object.md`

- An `invocation` object **MAY** contain a property named `machine` whose value is a redactable ([sec](#redactable-strings)) string containing the name of the machine on which the invocation occurred. (line 187)

## `account` Property

`file-format-20-invocation-object.md`

- An `invocation` object **MAY** contain a property named `account` whose value is a redactable ([sec](#redactable-strings)) string containing the name of the account under which the invocation occurred. (line 191)

## `processId` Property

`file-format-20-invocation-object.md`

- An `invocation` object **MAY** contain a property named `processId` whose value is an integer containing the id of the process in which the invocation occurred. (line 195)

## `executableLocation` Property

`file-format-20-invocation-object.md`

- An `invocation` object **MAY** contain a property named `executableLocation` whose value is an `artifactLocation` object ([sec](#artifactlocation-object)) specifying the location of the primary executable file for the program or script that was invoked. (line 199)

## `workingDirectory` Property

`file-format-20-invocation-object.md`

- An `invocation` object **MAY** contain a property named `workingDirectory` whose value is an `artifactLocation` object ([sec](#artifactlocation-object)) specifying the fully qualified path name of the process’s working directory (a directory that the operating system associates with the process, with respect to which the operating system interprets relative file paths). (line 209)

## `environmentVariables` Property

`file-format-20-invocation-object.md`

- An `invocation` object **MAY** contain a property named `environmentVariables` whose value is an object. (line 215)
- The value of each property **SHALL** be a string containing the value of the specified environment variable. (line 215)
- If the value of the environment variable is an empty string, the corresponding property value **SHALL** be an empty string. (line 215)
- A distinct redaction token ([sec](#redactiontokens-property)) **SHALL** be used for each redacted property name. (line 221)

## `toolExecutionNotifications` Property

`file-format-20-invocation-object.md`

- An `invocation` object **MAY** contain a property named `toolExecutionNotifications` whose value is an array of zero or more `notification` objects ([sec](#notification-object)). (line 227)
- The presence within this array of any `notification` object whose level property ([sec](#notification-object--level-property)) is `"error"` **SHALL** mean that the run failed. (line 227)

## `toolConfigurationNotifications` Property

`file-format-20-invocation-object.md`

- An `invocation` object **MAY** contain a property named `toolConfigurationNotifications` whose value is an array of zero or more `notification` objects ([sec](#notification-object)). (line 241)
- The presence within this array of any `notification` object whose `level` property ([sec](#notification-object--level-property)) is `"error"` **SHALL** mean that the run failed. (line 241)

## `description` Property

`file-format-21-attachment-object.md`

- An `attachment` object **SHOULD** contain a property named `description` whose value is a `message` object ([sec](#message-object)) describing the role played by the attachment. (line 30)

## `location` Property

`file-format-21-attachment-object.md`

- An `attachment` object **SHALL** contain a property named `location` whose value is an `artifactLocation` object ([sec](#artifactlocation-object)) that specifies the location of the attachment. (line 34)

## `regions` Property

`file-format-21-attachment-object.md`

- An `attachment` object **MAY** contain a property named `regions` whose value is an array of zero or more unique ([sec](#array-properties-with-unique-values)) `region` objects ([sec](#region-object)) each of which **SHALL** specify a region of interest within the attachment, and **SHOULD** contain a `message` property ([sec](#region-object--message-property)) so a user can understand its relevance. (line 38)

## `rectangles` Property

`file-format-21-attachment-object.md`

- An `attachment` object **MAY** contain a property named `rectangles` whose value is an array of zero or more unique ([sec](#array-properties-with-unique-values)) `rectangle` objects ([sec](#rectangle-object)). (line 42)
- If the attachment is an image (for example `.png` or `.svg`), each `rectangle` object **SHALL** specify an area of interest within the image, and **SHOULD** contain a `message` property ([sec](#rectangle-object--message-property)) so a user can understand its relevance. (line 42)
- If the attachment is not an image, and `rectangles` is present, its value **SHALL** be an empty array. (line 43)

## `analysisToolLogFiles` Property

`file-format-22-conversion-object.md`

- A `conversion` object **MAY** contain a property named `analysisToolLogFiles` whose value is an array of zero or more unique ([sec](#array-properties-with-unique-values)) `artifactLocation` objects ([sec](#artifactlocation-object)) that specify the locations of the per-run files. (line 56)

## Constraints

`file-format-23-versioncontroldetails-object.md`

- A `versionControlDetails` object **SHOULD** contain sufficient information to uniquely and permanently identify the revision of the files that were scanned. (line 12)

## `repositoryUri` Property

`file-format-23-versioncontroldetails-object.md`

- A `versionControlDetails` object **SHALL** contain a property named `repositoryUri` whose value is a string containing an absolute URI [cite](#RFC3986) that specifies the location of the repository containing the scanned files. (line 18)

## revisionId` Property

`file-format-23-versioncontroldetails-object.md`

- A `versionControlDetails` object **SHOULD** contain a property named `revisionId` whose value is a redactable ([sec](#redactable-strings)) string that uniquely and permanently identifies the appropriate revision of the scanned files. (line 22)

## `branch` Property

`file-format-23-versioncontroldetails-object.md`

- A `versionControlDetails` object **MAY** contain a property named `branch` whose value is a redactable ([sec](#redactable-strings)) string containing the name of a branch containing the correct revision of the scanned files. (line 26)

## `revisionTag` Property

`file-format-23-versioncontroldetails-object.md`

- A `versionControlDetails` object **MAY** contain a property named `revisionTag` whose value is a redactable ([sec](#redactable-strings)) string containing a tag that has been applied to the revision in the VCS. (line 30)

## `asOfTimeUtc` Property

`file-format-23-versioncontroldetails-object.md`

- A `versionControlDetails` object **MAY** contain a property named `asOfTimeUtc` whose value is a string in the format specified in [sec](#datetime-properties), specifying a UTC date and time that can be used to synchronize an enlistment to the state of the repository as of that time. (line 38)

## `mappedTo` Property

`file-format-23-versioncontroldetails-object.md`

- A `versionControlDetails` object **MAY** contain a property named `mappedTo` whose value is an `artifactLocation` object ([sec](#artifactlocation-object)) that specifies the location in the local file system to which the root of the repository was mapped at the time of the analysis. (line 44)
- The mapping algorithm **SHALL** be as follows, or any algorithm with the same result (a clarifying example follows): (line 46)

## `location property

`file-format-24-artifact-object.md`

- Depending on the circumstances, an `artifact` object either **SHALL**, **MAY**, or **SHALL NOT** contain a property named `location` whose value is an `artifactLocation` object ([sec](#artifactlocation-object)). (line 10)
- If the `artifact` object represents a top-level artifact, then `location` **SHALL** be present. (line 12)
- If the `artifact` object represents a nested artifact whose location relative to the root of its parent can be expressed only by means of a path, then `location` **SHALL** be present, and the value of its `uri` property **SHALL** be a relative reference [cite](#RFC3986) beginning with `"/"` expressing that path. (line 14)
- If the `artifact` object represents a nested artifact whose location within its parent can be expressed only by a byte offset from the start of the parent, and not by means of a path, then `location` **SHALL NOT** be present. (line 16)
- If the `artifact` object represents a nested artifact whose location within its parent can be expressed either by means of a path or by means of a byte offset from the start of the parent, then `location` **MAY** be present; if it is absent, then `offset` ([sec](#offset-property)) **SHALL** be present. (line 18)
- If `location` is present, the value of its `uri` property **SHALL** be a relative reference expressing the path of the nested artifact within the parent. (line 18)

## `parentIndex` Property

`file-format-24-artifact-object.md`

- If this `artifact` object represents a nested artifact, then it **SHALL** contain a property named `parentIndex` whose value is the array index ([sec](#array-indices)) of the parent artifact's `artifact` object within `theRun.artifacts` ([sec](#artifacts-property)). (line 24)
- If this `artifact` object represents a top-level artifact, then `parentIndex` **SHALL** be absent. (line 26)

## `offset` Property

`file-format-24-artifact-object.md`

- Depending on the circumstances, an `artifact` object either **SHALL**, **MAY**, or **SHALL NOT** contain a property named `offset` whose value is a non-negative integer. (line 59)
- If the `artifact` object represents a top-level artifact, then `offset` **SHALL NOT** be present. (line 61)
- If the `artifact` object represents a nested artifact whose location relative to its parent can be expressed only by means of a byte offset from the start of its parent artifact, then `offset` **SHALL** be present, and its value **SHALL** be that byte offset. (line 63)
- If the `artifact` object represents a nested artifact whose location within its parent can only be expressed by means of a path, and not by means of a byte offset from the start of the parent, then `offset` **SHALL NOT** be present. (line 65)
- If the `artifact` object represents a nested artifact whose location within its parent can be expressed either by means of a path or by means of a byte offset from the start of the parent, then `offset` **MAY** be present; if it is absent, then `location` ([sec](#artifact-object--location-property)) **SHALL** be present. (line 67)
- If `offset` is present, its value **SHALL** be that byte offset. (line 67)

## `length` Property

`file-format-24-artifact-object.md`

- An `artifact` object **MAY** contain a property named `length` whose value is a non-negative integer specifying the length of the artifact in bytes. (line 71)
- If `length` is absent, it **SHALL** default to -1, which indicates that the value is unknown (not set). (line 73)

## `roles` Property

`file-format-24-artifact-object.md`

- An `artifact` object **MAY** contain a property named `roles` whose value is an array of zero or more unique ([sec](#array-properties-with-unique-values)) strings each of which specifies a role that this artifact played in the analysis. (line 77)
- Each array element **SHALL** have one of the following values, with the specified meanings: (line 79)

## `mimeType` Property

`file-format-24-artifact-object.md`

- An `artifact` object **MAY** contain a property named `mimeType` whose value is a string that specifies the artifact’s MIME type [cite](#RFC2045). (line 149)

## `contents` Property

`file-format-24-artifact-object.md`

- An `artifact` object **MAY** contain a property named contents whose value is an `artifactContent` object ([sec](#artifactcontent-object)) representing the entire contents of the artifact. (line 153)

## `encoding` Property

`file-format-24-artifact-object.md`

- If an `artifact` object represents a text artifact, it **MAY** contain a property named `encoding` whose value is a case-sensitive string that specifies the artifact’s text encoding. (line 157)
- The string **SHALL** be one of the character set names defined by IANA [cite](#IANA-ENC). (line 157)
- If the `artifact` object represents a text artifact and this property is absent, it **SHALL** default to the value of `theRun.defaultEncoding` ([sec](#defaultencoding-property)), if that property is present; otherwise, the artifact’s encoding **SHALL** be taken to be unknown. (line 159)
- If the `artifact` object represents a binary artifact, `encoding` **SHALL** be absent. (line 161)

## General

`file-format-24-artifact-object.md`

- If an `artifact` object represents a text artifact that contains source code, it **MAY** contain a property named `sourceLanguage` whose value is a hierarchical string ([sec](#hierarchical-strings)) that specifies the programming language in which the source code is written. (line 191)
- If the `artifact` object does not represent a text artifact containing source code, `sourceLanguage` **SHALL** be absent. (line 191)
- If the artifact contains source code in a mix of languages, and if it is possible to identify one of those languages as the "primary" language of the artifact, then `sourceLanguage` **SHALL** specify that language. (line 197)
- If it is not possible to identify a primary language, `sourceLanguage` **MAY** specify any language used in the artifact, or it **MAY** be absent. (line 203)
- If `sourceLanguage` is absent, it **SHALL** default to the value of `theRun.defaultSourceLanguage` ([sec](#defaultsourcelanguage-property)). (line 207)
- If both `artifact.sourceLanguage` and `theRun.defaultSourceLanguage` are absent, the artifact’s source language **SHALL** be taken to be unknown. (line 207)

## `hashes` Property

`file-format-24-artifact-object.md`

- An `artifact` object **MAY** contain a property named `hashes` whose value is a non-empty object ([sec](#object-properties)) each of whose property names specifies the name of a hash function, and each of whose property values represents the value produced by that hash function. (line 235)
- To maximize interoperability, the property names **SHOULD** appear in the IANA registry of hash function textual names [cite](#IANA-HASH). (line 248)
- The object **SHOULD** contain a property named `"sha-256"`. (line 250)
- The object **MAY** contain properties whose names do not appear in the IANA registry, but at the expense of interoperability. (line 252)
- If the hash function is one whose name appears in the IANA registry, the property name **SHALL** equal the name as it appears in the registry (for example, `"sha-256"` rather than `"sha256"`); otherwise the property name **MAY** be any suitable name, but it **SHALL NOT** equal any name defined in the IANA registry. (line 254)
- Each property value **SHALL** be a string representation of the hash digest of the artifact, computed by the hash function specified by the property name. (line 258)

## `lastModifiedTimeUtc` Property

`file-format-24-artifact-object.md`

- An `artifact` object **MAY** contain a property named `lastModifiedTimeUtc` whose value is a string in the format specified in [sec](#datetime-properties), specifying the UTC date and time at which the artifact was most recently modified. (line 272)

## `description` Property

`file-format-24-artifact-object.md`

- An `artifact` object **MAY** have a property named `description` whose value is a `message` object ([sec](#message-object)) that describes the artifact. (line 277)

## `name` Property

`file-format-26-translationmetadata-object.md`

- A `translationMetadata` object **SHALL** contain a property named `name` whose value is a string containing a name for the translation. (line 35)

## `fullName` Property

`file-format-26-translationmetadata-object.md`

- A `translationMetadata` object **MAY** contain a property named `fullName` whose value is a string containing the name of the translation along with any other useful identifying information. (line 39)

## `shortDescription` Property

`file-format-26-translationmetadata-object.md`

- A `translationMetadata` object **MAY** contain a property named `shortDescription` whose value is a `multiformatMessageString` object ([sec](#multiformatmessagestring-object)) containing a brief description of the translation. (line 43)

## `fullDescription` Property

`file-format-26-translationmetadata-object.md`

- A `translationMetadata` object **MAY** contain a property named `fullDescription` whose value is a `multiformatMessageString` object ([sec](#multiformatmessagestring-object)) containing a comprehensive description of the translation. (line 47)

## `downloadUri` Property

`file-format-26-translationmetadata-object.md`

- A `translationMetadata` object **MAY** contain a property named `downloadUri` whose value is a string containing the absolute URI [cite](#RFC3986) from which the translation can be downloaded. (line 51)

## `informationUri` Property

`file-format-26-translationmetadata-object.md`

- A `translationMetadata` object **MAY** contain a property named `informationUri` whose value is a string containing the absolute URI [cite](#RFC3986) at which information about the translation can be found. (line 54)

## guid property

`file-format-27-result-object.md`

- A `result` object **MAY** contain a property named `guid` whose value is a GUID-valued string ([sec](#guid-valued-strings)) defining a unique, stable identifier for the result. (line 26)

## `correlationGuid` Property

`file-format-27-result-object.md`

- A `result` object **MAY** contain a property named `correlationGuid` whose value is a GUID-valued string ([sec](#guid-valued-strings)) that is shared by all results that are considered logically identical, and that is different between any two results that are considered logically distinct. (line 34)

## `ruleId` Property

`file-format-27-result-object.md`

- Depending on the circumstances, a `result` object either **SHALL**, **MAY**, or **SHALL NOT** contain a property named `ruleId` whose value is a hierarchical string ([sec](#hierarchical-strings)) whose leading components specify the stable identifier of the rule that was evaluated to produce the result. (line 42)
- In addition to being stable, `ruleId` **SHOULD** be opaque. (line 42)
- If `rule.id` is absent, `ruleId` **SHALL** be present. (line 96)
- If `rule.id` is present, `ruleId` **MAY** be present. (line 96)
- If `ruleId` and `rule.id` are both present, they **SHALL** be equal. (line 96)

## `ruleIndex` Property

`file-format-27-result-object.md`

- If `theDescriptor` exists (that is, if `theTool` contains a `reportingDescriptor` object ([sec](#reportingdescriptor-object)) that describes the rule that was violated), a `result` object **MAY** contain a property named `ruleIndex` whose value is the array index ([sec](#array-indices)) of `theDescriptor` within `theComponent.ruleDescriptors` ([sec](#rules-property)). (line 106)
- Otherwise, `ruleIndex` **SHALL** be absent. (line 106)
- If `ruleIndex` and `rule.index` ([sec](#rule-property), [sec](#reportingdescriptorreference-object--index-property)) are both present, they **SHALL** be equal. (line 110)

## `rule` Property

`file-format-27-result-object.md`

- Depending on the circumstances, a `result` object either **SHALL NOT**, **SHOULD**, or **MAY** contain a property named `rule` whose value is a `reportingDescriptorReference` object ([sec](#reportingdescriptorreference-object)) that identifies `theDescriptor`. (line 114)
- If `theDescriptor` does not exist (that is, if `theTool` does not contain a `reportingDescriptor` object ([sec](#reportingdescriptor-object)) that describes the rule that was violated), then `rule` **SHALL NOT** be present. (line 116)
- If `theDescriptor` occurs in `theTool.extensions` ([sec](#extensions-property)), then `rule` **SHOULD** be present. (line 118)
- If `theDescriptor` occurs in `theTool.driver` ([sec](#driver-property)) and `ruleIndex` is absent, then again `rule` **SHOULD** be present. (line 122)
- If `theDescriptor` occurs in `theTool.driver` and `ruleIndex` is present, then `rule` **MAY** be present. (line 126)
- If `rule.id` ([sec](#reportingdescriptorreference-object--id-property)) is absent, it **SHALL** default to `thisObject.ruleId`. (line 130)
- If `rule.id` and `thisObject.ruleId` are both present, they **SHALL** be equal. (line 130)
- If `rule.index` ([sec](#reportingdescriptorreference-object--index-property)) is absent, it **SHALL** default to `thisObject.ruleIndex`. (line 132)
- If `rule.index` and `thisObject.ruleIndex` are both present, they **SHALL** be equal. (line 132)
- If `rule` is absent, it **SHALL** default to a `reportingDescriptorReference` object whose `id` property is set to `thisObject.ruleId` and whose `index` property is set to `thisObject.ruleIndex`. (line 134)

## `taxa` Property

`file-format-27-result-object.md`

- A `result` object **MAY** contain a property named `taxa` whose value is an array of zero or more unique ([sec](#array-properties-with-unique-values)) `reportingDescriptorReference` objects ([sec](#reportingdescriptorreference-object)) each of which refers to a taxon (see [sec](#taxonomies)) into which this result falls. (line 140)
- If the `toolComponent` object ([sec](#toolcomponent-object)) `theComponent` that defines the rule that was violated contains a `reportingDescriptor` object ([sec](#reportingdescriptor-object)) `theDescriptor` (a member of `toolComponent.rules` ([sec](#rules-property))) that describes that rule, then `thisObject.taxa` **SHALL** contain elements corresponding to those elements of `theDescriptor.relationships` ([sec](#reportingdescriptor-object--relationships-property)) that describe taxa into which this result falls. (line 142)
- `thisObject.taxa` does not need to contain elements which correspond to `superset` or `equals` relationships; rather, the result **SHALL** implicitly be taken to fall into all the taxa described by those relationships. (line 142)
- Otherwise (that is, if `theDescriptor` does not exist), `thisObject.taxa` **SHALL** contain elements that describe all taxa into which the result falls. (line 146)
- In either case, if there is no `toolComponent` that defines the taxonomy to which an element of `thisObject.taxa` refers, then that element (a `reportingDescriptorReference` object) **SHALL NOT** contain `index` ([sec](#reportingdescriptorreference-object--index-property)) or `toolComponent.index` ([sec](#toolcomponent-property), [sec](#toolcomponentreference-object--index-property)). (line 148)

## `kind` Property

`file-format-27-result-object.md`

- A `result` object **MAY** contain a property named `kind` whose value is one of a fixed set of strings that specify the nature of the result. (line 234)
- If present, the `kind` property **SHALL** have one of the following values, with the specified meanings: (line 236)
- If `kind` is absent, it **SHALL** default to `"fail"`. (line 291)
- If `level` has any value other than `"none"` and `kind` is present, then `kind` **SHALL** have the value `"fail"`. (line 293)

## `level` Property

`file-format-27-result-object.md`

- A `result` object **MAY** contain a property named `level` whose value is one of a fixed set of strings that specify the severity level of the result. (line 297)
- If present, the `level` property **SHALL** have one of the following values, with the specified meanings: (line 299)
- If `kind` ([sec](#result-object--kind-property)) has any value other than `"fail"`, then if `level` is absent, it **SHALL** default to `"none"`, and if it is present, it **SHALL** have the value `"none"`. (line 335)
- If `kind` has the value `"fail"` and `level` is absent, then `level` **SHALL** be determined by the following procedure: (line 337)

## `message` Property

`file-format-27-result-object.md`

- A `result` object **SHALL** contain a property named `message` whose value is a `message` object ([sec](#message-object)) that describes the result. (line 379)
- The `message` property **SHOULD** provide sufficient details to allow an end user to resolve any problem that the result might indicate. (line 381)
- In particular, it **SHALL** include all of the following information that is available and relevant to the result: (line 381)

## `locations` Property

`file-format-27-result-object.md`

- A `result` object **SHOULD** contain a property named `locations` whose value is an array of zero or more `location` objects ([sec](#location-object)) each of which specifies a location where the result occurred. (line 452)
- The `locations` array **SHALL NOT** contain more than one element unless the condition indicated by the result, if any, can only be corrected by making a change at every location specified in the array. (line 460)
- The `locations` array **SHALL NOT** be used to specify distinct occurrences of the same result which can be corrected independently. (line 464)

## `analysisTarget` Property

`file-format-27-result-object.md`

- If the analysis target differs from the result file, a `result` object **SHOULD** contain a property named `analysisTarget` whose value is an `artifactLocation` object ([sec](#artifactlocation-object)) that specifies the analysis target. (line 472)
- If the analysis target and the result file are the same, the `analysisTarget` property **SHOULD** be absent. (line 474)

## `webRequest` Property

`file-format-27-result-object.md`

- A `result` object **MAY** contain a property named `webRequest` whose value is a `webRequest` object ([sec](#webrequest-object)) that describes the HTTP request which led to this result. (line 504)

## `webResponse` Property

`file-format-27-result-object.md`

- A `result` object **MAY** contain a property named `webResponse` whose value is a `webResponse` object ([sec](#webresponse-object)) that describes the response to the HTTP request which led to this result. (line 510)

## `fingerprints` Property

`file-format-27-result-object.md`

- A `result` object **MAY** contain a property named `fingerprints` whose value is an object ([sec](#object-properties)). (line 516)
- Each property value in this object **SHALL** be a string that provides a stable identifier for the result. (line 518)
- This identifier **SHALL**, to the extent that it is feasible, be the same for all results that are logically identical, and different for any two results that are logically distinct. (line 518)
- Each property name in this object **SHALL** be a versioned hierarchical string ([sec](#versioned-hierarchical-strings)). (line 520)

## `partialFingerprints` Property

`file-format-27-result-object.md`

- A `result` object **MAY** contain a property named `partialFingerprints` whose value is an object ([sec](#object-properties)). (line 569)
- Each property value in this object **SHALL** be a string that contributes to the stable, unique identity, or "fingerprint," of the result (see [sec](#fingerprints-property)). (line 571)
- Each property name in this object **SHALL** be a versioned hierarchical string ([sec](#versioned-hierarchical-strings)). (line 573)

## `codeFlows` Property

`file-format-27-result-object.md`

- A `result` object **MAY** contain a property named `codeFlows` whose value is an array of zero or more `codeFlow` objects ([sec](#codeflow-object)). (line 647)

## `graphs` Property

`file-format-27-result-object.md`

- A `result` object **MAY** contain a property named `graphs` whose value is an array of zero or more unique ([sec](#array-properties-with-unique-values)) `graph` objects ([sec](#graph-object)). (line 653)
- A `graph` object defined at the `result` level **SHALL** be referenced only by `graphTraversal` objects ([sec](#graphtraversal-object)) defined in the `graphTraversals` property ([sec](#graphtraversals-property)) of the `result` object in which it is defined. (line 655)
- This contrasts with `graph` objects defined at the `run` level ([sec](#run-object--graphs-property)), which **MAY** be referenced by `graphTraversal` objects defined in the `graphTraversals` property of any `result` object in `theRun`. (line 655)

## `graphTraversals` Property

`file-format-27-result-object.md`

- If a `result` object contains a `graphs` property ([sec](#result-object--graphs-property)), or if `theRun` contains a `graphs` property ([sec](#run-object--graphs-property)), then the `result` object **MAY** contain a property named `graphTraversals` whose value is an array of zero or more unique ([sec](#array-properties-with-unique-values)) `graphTraversal` objects ([sec](#graphtraversal-object)). (line 659)
- If neither the `result` object nor `theRun` contains a `graphs` property, the `graphTraversals` property **SHALL** be absent. (line 659)

## `stacks` Property

`file-format-27-result-object.md`

- A `result` object **MAY** contain a property named `stacks` whose value is an array of zero or more unique ([sec](#array-properties-with-unique-values)) `stack` objects ([sec](#stack-object)). (line 663)

## `relatedLocations` Property

`file-format-27-result-object.md`

- A `result` object **MAY** contain a property named `relatedLocations` whose value is an array of zero or more unique ([sec](#array-properties-with-unique-values)) `location` objects ([sec](#location-object)) each of which represents a location relevant to understanding the result. (line 669)

## `suppressions` Property

`file-format-27-result-object.md`

- A `result` object **MAY** contain a property named `suppressions` whose value is an array of zero or more unique ([sec](#array-properties-with-unique-values)) `suppression` objects ([sec](#suppression-object)) each of which describes a request to "suppress" a result (that is, to exclude it from result lists, bug counts, *etc.*). (line 725)
- If `suppressions` is absent, it **SHALL** default to `null.` (line 727)
- The presence of an array value, whether or not the array is empty, **SHALL** mean that suppression information is available for the result. (line 729)
- The absence of an array value, or the presence of a `null` value, **SHALL** mean that suppression information is not available for the result. (line 731)
- The `suppressions` values for all `result` objects in `theRun` **SHALL** be either all `null` or all non-`null`. (line 733)

## `baselineState` Property

`file-format-27-result-object.md`

- A `result` object **MAY** contain a property named `baselineState` whose value is a string that specifies the state of this result with respect to some previous run, which we refer to as the "baseline run." (line 739)
- If `theRun.baselineGuid` ([sec](#baselineguid-property)) is present, its value **SHALL** specify the baseline run. (line 741)
- This property **SHALL** have one of the following values, with the specified meanings: (line 743)
- If `baselineState` is present on any `result` object in `theRun`, it **SHALL** be present on every such `result` object. (line 761)

## `rank` Property

`file-format-27-result-object.md`

- A `result` object **MAY** contain a property named `rank` whose value is a number between `0.0` and `100.0` inclusive, representing the priority or importance of the result. (line 769)
- If `kind` has the value `"fail"`, then if `rank` is absent, it **SHALL** default to the value determined by the procedure defined for `level` ([sec](#result-object--level-property)), except throughout the procedure, replace `"level"` with `"rank"` and replace `"warning"` with `-1.0`. (line 773)
- If `kind` has any other value, then `rank` **SHALL** be absent. (line 775)
- If `rank` is absent, it **SHALL** default to `-1.0`, which indicates that the value is unknown (not set). (line 777)

## `precision` Property

`file-format-27-result-object.md`

- This value **MAY** be represented as a floating-point number. (line 783)

## `securitySeverity` Property

`file-format-27-result-object.md`

- A `result` object **MAY** contain a property named `securitySeverity` whose value is a number between `0.0` and `100.0` inclusive, representing a numerical estimate of the severity of the class of vulnerabilities found by this result. (line 791)
- This value **MAY** be represented as a floating-point number. (line 791)

## `attachments` Property

`file-format-27-result-object.md`

- A `result` object **MAY** contain a property named `attachments` whose value is an array of zero or more unique ([sec](#array-properties-with-unique-values)) `attachment` objects ([sec](#attachment-object)) each of which describes an artifact relevant to the detection of the result. (line 801)

## `workItemUris` Property

`file-format-27-result-object.md`

- A `result` object **MAY** contain a property named `workItemUris` whose value is either `null` or an array of zero or more unique ([sec](#array-properties-with-unique-values)) strings each of which contains the absolute URI [cite](#RFC3986) of a work item associated with this result. (line 805)
- If `workItemUris` is absent, it **SHALL** default to `null`. (line 807)
- An empty array **SHALL** mean that there are no work items associated with this result. (line 809)
- `null` **SHALL** mean that the set of work items associated with this result, if any, is not known. (line 809)
- The `workItemUris` values for all `result` objects in `theRun` **SHALL** be either all `null` or all non-`null`. (line 811)

## `hostedViewerUri` Property

`file-format-27-result-object.md`

- A `result` object **MAY** contain a property named `hostedViewerUri` whose value is a string containing an absolute URI [cite](#RFC3986) at which the result can be viewed. (line 819)

## `provenance` Property

`file-format-27-result-object.md`

- A `result` object **MAY** contain a property named `provenance` whose value is a `resultProvenance` object ([sec](#resultprovenance-object)) that contains information about how and when the result was detected. (line 825)

## `fixes` Property

`file-format-27-result-object.md`

- A `result` object **MAY** contain a property named `fixes` whose value is an array of zero or more unique ([sec](#array-properties-with-unique-values)) `fix` objects ([sec](#fix-object)). (line 829)

## `occurrenceCount` Property

`file-format-27-result-object.md`

- A `result` object **MAY** contain a property named `occurrenceCount` whose value is a positive integer specifying the number of times a result with `theResult.correlationGuid` ([sec](#result-object--correlationguid-property)) has been observed. (line 833)

## General

`file-format-28-location-object.md`

- In that case, the location object **SHOULD** contain a message property ([sec](#location-object--message-property)) explaining the significance of this "location." (line 18)

## `id` Property

`file-format-28-location-object.md`

- A `location` object **MAY** contain a property named `id` whose value is a non-negative integer that is unique among all `location` objects belonging to `theLocationOwner`. (line 22)
- If `id` is absent, it **SHALL** default to -1, which indicates that the value is unknown (not set). (line 24)

## `physicalLocation` Property

`file-format-28-location-object.md`

- Depending on the circumstances, a `location` object either **SHALL**, **MAY**, or **SHALL NOT** contain a property named `physicalLocation` whose value is a `physicalLocation` object ([sec](#physicallocation-object)) that identifies the file within which the location lies. (line 38)
- If physical location information is available and the `logicalLocations` property ([sec](#location-object--logicallocations-property)) is absent or empty, `physicalLocation` **SHALL** be present. (line 38)
- If physical location is available and `logicalLocations` is present and non-empty, `physicalLocation` **MAY** be present. (line 38)
- If physical location information is not available, `physicalLocation` **SHALL NOT** be present. (line 38)

## `logicalLocations` Property

`file-format-28-location-object.md`

- Depending on the circumstances, a `location` object either **SHALL**, **MAY**, or **SHALL NOT** contain a property named `logicalLocations` whose value is an array of zero or more unique ([sec](#array-properties-with-unique-values)) `logicalLocation` objects ([sec](#logicallocation-object)) that identify the programmatic construct within which the location lies. (line 42)
- If logical location information is available and the `physicalLocation` property ([sec](#physicallocation-property)) is absent, `logicalLocations` **SHALL** be present and non-empty. (line 42)
- If logical location information is available and `physicalLocation` is present, `logicalLocations` **MAY** be present. (line 42)
- If logical location information is not available, `logicalLocations` **SHALL NOT** be present. (line 42)

## `message` Property

`file-format-28-location-object.md`

- A `location` object **MAY** contain a property named `message` whose value is a `message` object ([sec](#message-object)) relevant to the location. (line 48)

## `annotations` Property

`file-format-28-location-object.md`

- A `location` object **MAY** contain a property named `annotations` whose value is an array of zero or more unique ([sec](#array-properties-with-unique-values)) `region` objects ([sec](#region-object)) each of which describes a region within the artifact specified by the `location` object that is relevant to the location. (line 52)
- Each of these `region` objects **SHOULD** contain a `message` property ([sec](#region-object--message-property)) that explains the relevance of the region to the location. (line 52)

## `relationships` Property

`file-format-28-location-object.md`

- A `location` object **MAY** contain a property named `relationships` whose value is an array of zero or more unique ([sec](#array-properties-with-unique-values)) `locationRelationship` objects ([sec](#locationrelationship-object)) each of which declares one or more directed relationship from `thisObject` to another `location` object, which we refer to as `theTarget`, specified by `locationRelationship.target` ([sec](#locationrelationship-object--target-property)). (line 76)

## Constraints

`file-format-29-physicallocation-object.md`

- Either the `artifactLocation` property ([sec](#physicallocation-object--artifactlocation-property)), the `address` property ([sec](#address-property)), or both **SHALL** be present. (line 10)
- If `region.byteLength` ([sec](#region-property), [sec](#bytelength-property)) and `address.length` ([sec](#address-property), [sec](#address-object--length-property)) are both present, then `region.byteLength` **SHALL** equal the absolute value of `address.length`. (line 12)

## `artifactLocation` Property

`file-format-29-physicallocation-object.md`

- A `physicalLocation` object **MAY** contain a property named `artifactLocation` whose value is an `artifactLocation` object ([sec](#artifactlocation-object)) that represents the location of the artifact. (line 16)
- If `artifactLocation` is absent, then `address` ([sec](#address-property)) **SHALL** be present. (line 16)

## `region` Property

`file-format-29-physicallocation-object.md`

- A `physicalLocation` object **MAY** contain a property named `region` whose value is a `region` object ([sec](#region-object)) that represents a relevant portion of the artifact. (line 20)
- In particular, if the `physicalLocation` object occurs within the `locations` property ([sec](#result-object--locations-property)) of a `result` object ([sec](#result-object)), the region property **SHALL** specify the region within the artifact where the result was detected. (line 20)
- If the `physicalLocation` object specifies a location in a nested artifact, then the `region` property **SHALL** specify the location with respect to the innermost nested artifact. (line 43)

## `contextRegion` Property

`file-format-29-physicallocation-object.md`

- If a `physicalLocation` object contains a `region` property ([sec](#region-property)), it **MAY** also contain a property named `contextRegion` whose value is a `region` object ([sec](#region-object)) which specifies a region that is a proper superset of the region specified by the `region` property. (line 51)
- If `region` is absent, `contextRegion` **SHALL** be absent. (line 51)

## `address` Property

`file-format-29-physicallocation-object.md`

- A `physicalLocation` object **MAY** contain a property named address whose value is an `address` object ([sec](#address-object)) that represents the physical or virtual address of this location. (line 88)
- If `address` is absent, then `artifactLocation` ([sec](#physicallocation-object--artifactlocation-property)) **SHALL** be present. (line 88)

## General

`file-format-30-region-object.md`

- If `startLine` ([sec](#startline-property)) > 0 or `charOffset` ([sec](#charlength-property)) >= 0, this `region` object **SHALL** define a text region. (line 12)
- If `byteOffset` ([sec](#byteoffset-property)) >= 0, this `region` object **SHALL** define a binary region. (line 12)
- If a `region` object defines both a text region and a binary region, the text region and the binary region **SHALL** specify the identical range of bytes in the artifact, as determined by the artifact’s character encoding. (line 12)
- For regions in text artifacts, a `region` object **SHOULD** define a text region and **MAY** also define a binary region; it **SHALL** define either a text region or a binary region or both. (line 14)
- For regions in binary artifacts, a region object **SHALL** define a binary region and **SHALL NOT** define a text region. (line 16)
- If any text properties are present, enough text properties **SHALL** be present to fully specify a text region (see [sec](#text-regions)). (line 18)
- If any binary properties are present, then enough binary properties **SHALL** be present to fully specify a binary region (see [sec](#binary-regions)). (line 18)

## Text Regions

`file-format-30-region-object.md`

- The line number of the first line in a text artifact **SHALL** be 1. (line 35)
- The column number of the first character in each line **SHALL** be 1. (line 35)
- The character offset of the first character in the artifact **SHALL** be 0. (line 35)
- The values of text properties **SHALL NOT** depend on the presence or absence of a byte order mark (BOM) at the start of the artifact. (line 37)
- A text region **MAY** be specified in two ways: (line 49)
- A text region **SHALL** specify both its start (the location of its first character) and its end (the location of its last character). (line 55)
- A region of length 0 is referred to as an "insertion point." An insertion point **MAY** be specified either by specifying `charLength` as 0, or by specifying the same values for `startColumn` and `endColumn`. (line 146)

## Binary Regions

`file-format-30-region-object.md`

- The byte offset of the first byte in an artifact **SHALL** be 0. (line 169)
- To specify a byte region, at least `byteOffset` ([sec](#byteoffset-property)) **SHALL** be present. (line 171)
- `byteLength` ([sec](#bytelength-property)) **MAY** also be present. (line 171)

## Independence of Text and Binary Regions

`file-format-30-region-object.md`

- The text-related and binary-related properties in a `region` object **SHALL** be treated independently. (line 175)
- That is, the value of a text-related property **SHALL NOT** be inferred from the value of any set of binary-related properties, and *vice versa*. (line 175)

## `startLine` Property

`file-format-30-region-object.md`

- When a `region` object represents a text region specified by line/column properties, it **SHALL** contain a property named `startLine` whose value is a positive integer equal to the line number of the line containing the first character in the region. (line 199)

## `startColumn` Property

`file-format-30-region-object.md`

- When a `region` object represents a text region specified by line/column properties, it **MAY** contain a property named `startColumn` whose value is a positive integer equal to the column number of the first character in the region. (line 203)
- If `startColumn` is absent, it **SHALL** default to 1. (line 205)

## `endLine` Property

`file-format-30-region-object.md`

- When a `region` object represents a text region specified by line/column properties, it **MAY** contain a property named `endLine` whose value is a positive integer equal to the line number of the line containing the last character in the region. (line 209)
- If `endLine` is absent, its value **SHALL** default to `startLine`. (line 211)

## `endColumn` Property

`file-format-30-region-object.md`

- When a `region` object represents a text region specified by line/column properties, it **MAY** contain a property named `endColumn` whose value is an integer whose value is one greater than the column number of the last character in the region. (line 215)
- If `endColumn` is absent, it **SHALL** default to a value one greater than the column number of the last character on the line, excluding any newline sequence. (line 217)

## `charOffset` Property

`file-format-30-region-object.md`

- When a `region` object represents a text region specified by offset/length properties, it **SHALL** contain a property named `charOffset` whose value is an integer equal to the zero-based character offset of the first character in the region from the beginning of the artifact. (line 221)
- If `charOffset` is absent, it **SHALL** default to -1, which indicates that the value is unknown (not set). (line 221)

## `charLength` Property

`file-format-30-region-object.md`

- When a `region` object represents a text region specified by offset/length properties, it **MAY** contain a property named `charLength` whose value is a non-negative integer equal to the number of characters in the region. (line 225)
- If `charLength` is absent, it **SHALL** default to 0, which **SHALL** be interpreted as an insertion point at the position specified by `charOffset` ([sec](#charoffset-property)) (line 227)
- The sum of `charOffset` and `charLength` **SHALL** be greater than or equal to 0 and less than or equal to the number of characters in the artifact. (line 229)
- A region whose `charOffset` is equal to the number of characters in the artifact and whose `charLength` is 0 is permitted and **SHALL** represent an insertion point at the end of the artifact. (line 231)

## `byteOffset` Property

`file-format-30-region-object.md`

- When a `region` object represents a binary region, it **SHALL** contain a property named `byteOffset` whose value is an integer equal to the zero-based byte offset of the first byte in the region from the beginning of the artifact. (line 235)
- If `byteOffset` is absent, it **SHALL** default to -1, which indicates that the value is unknown (not set). (line 235)

## `byteLength` Property

`file-format-30-region-object.md`

- When a `region` object represents a binary region, it **MAY** contain a property named `byteLength` whose value is an integer equal to the number of bytes in the region. (line 239)
- If `byteLength` is absent, it **SHALL** default to 0, which **SHALL** be interpreted as an insertion point at the position specified by `byteOffset` ([sec](#byteoffset-property)). (line 239)
- The sum of `byteOffset` and `byteLength` **SHALL** be greater than or equal to 0 and less than or equal to the number of bytes in the artifact. (line 241)
- A `region` object whose `byteOffset` equals the number of bytes in the artifact and whose `byteLength` is 0 is permitted, and **SHALL** represent an insertion point at the end of the artifact. (line 243)

## `snippet` Property

`file-format-30-region-object.md`

- A `region` object **MAY** contain a property named `snippet` whose value is an `artifactContent` object ([sec](#artifactcontent-object)) representing the portion of the artifact specified by the `region` object. (line 247)

## `message` Property

`file-format-30-region-object.md`

- A `region` object **MAY** contain a property named `message` whose value is a `message` object ([sec](#message-object)) containing a message relevant to the region. (line 259)

## `sourceLanguage` Property

`file-format-30-region-object.md`

- If the `region` object represents a portion of a text artifact that contains source code, it **MAY** contain a property named `sourceLanguage` whose value is a hierarchical string ([sec](#hierarchical-strings)) that specifies the programming language in which this portion of the source code is written. (line 265)
- If the `region` object does not represent a portion of a text artifact containing source code, then `sourceLanguage` **SHALL** be absent. (line 265)
- if `sourceLanguage` is absent, it **SHALL** default to the value of the `sourceLanguage` property ([sec](#artifact-object--sourcelanguage-property)) of the `artifact` object ([sec](#artifact-object)) which describes the artifact that contains the region. (line 271)
- If all three of `region.sourceLanguage`, `artifact.sourceLanguage`, and `theRun.defaultSourceLanguage` are absent, the source language of the region object **SHALL** be taken to be unknown. (line 271)

## `top`, `left`, `bottom`, and `right` Properties

`file-format-31-rectangle-object.md`

- A `rectangle` object **SHALL** contain properties named `top`, `left`, `bottom`, and `right`, each of which contains a number (as defined by the JSON Schema standard [cite](#JSCHEMA01)) specifying one of the coordinates of the rectangle within the image. (line 10)
- These properties **SHALL** be measured in the image format’s natural units (for example, pixels for raster-based image formats). (line 10)
- These values **MAY** be positive or negative, depending on the natural coordinate system of the image format. (line 10)
- They **MAY** increase either from left to right or from right to left, and either from top to bottom or from bottom to top, again depending on the natural coordinate system of the image format. (line 10)

## `message` Property

`file-format-31-rectangle-object.md`

- A `rectangle` object **SHOULD** contain a property named `message` whose value is a `message` object ([sec](#message-object)) containing a message relevant to this area of the image. (line 16)

## Absolute Address Calculation

`file-format-32-address-object.md`

- If both `absoluteAddress` and `offsetFromParent` exist, then `absoluteAddress` **SHALL** equal the value that `CalculateAbsoluteAddress` would have returned if `absoluteAddress` were absent, if `CalculateAbsoluteAddress` would have returned successfully in that circumstance. (line 67)

## Relative Address Calculation

`file-format-32-address-object.md`

- If both `relativeAddress` and `offsetFromParent` exist, then `relativeAddress` **SHALL** equal the value that `CalculateRelativeAddress` would have returned if `relativeAddress` were absent, if `CalculateRelativeAddress` would have returned successfully in that circumstance. (line 93)

## `index` Property

`file-format-32-address-object.md`

- Depending on the circumstances, an `address` object either **MAY, SHALL NOT**, or **SHALL** contain a property named `index` whose value is the array index ([sec](#array-indices)) within `theRun.addresses` ([sec](#addresses-property)) of an `address` object that provides the properties for `thisObject`. (line 97)
- If `thisObject` is an element of `theRun.addresses`, then `index` **MAY** be present. (line 99)
- If present, its value **SHALL** be the index of `thisObject` within `theRun.addresses`. (line 99)
- Otherwise, if `theRun.addresses` is absent, or if it does not contain a cached object for `thisObject`, then `index` **SHALL NOT** be present. (line 101)
- Otherwise (that is, if `thisObject` belongs to a result, and `theRun.addresses` contains a cached object for `thisObject`), then `index` **SHALL** be present, and its value **SHALL** be the array index within `theRun.addresses` of the cached object. (line 103)
- If `index` is present, `thisObject` **SHALL** take all properties present on the cached object. (line 105)
- If `thisObject` contains any properties other than `index`, they **SHALL** equal the corresponding properties of the cached object. (line 105)

## `absoluteAddress` Property

`file-format-32-address-object.md`

- An `address` object **MAY** contain a property named `absoluteAddress` whose value is a non-negative integer containing the absolute address (see [sec](#absolute-address-calculation)) of `thisObject`. (line 113)
- If `absoluteAddress` is absent, it **SHALL** default to -1, which indicates that the value is unknown (not set). (line 115)

## `relativeAddress` Property

`file-format-32-address-object.md`

- If `parentIndex` ([sec](#address-object--parentindex-property)) is present, an `address` object **MAY** contain a property named `relativeAddress` whose value, if present, is an integer containing the relative address (see [sec](#relative-address-calculation)) of `thisObject`. (line 119)
- If `parentIndex` is absent, `relativeAddress` **SHALL** be absent. (line 121)
- If `relativeAddress` is absent, it **SHALL** default to `null`, which indicates that the value is unknown (not set). (line 123)

## `offsetFromParent` Property

`file-format-32-address-object.md`

- If `parentIndex` ([sec](#address-object--parentindex-property)) is present, an `address` object **MAY** contain a property named `offsetFromParent` whose value, if present, is an integer containing the offset of this address from the absolute address of `theParent` (see [sec](#parent-child-relationships)). (line 127)
- If `parentIndex` is absent, `offsetFromParent` **SHALL** be absent. (line 131)
- If `offsetFromParent` is absent, it **SHALL** default to `null`, which indicates that the value is unknown (not set). (line 133)

## `length` Property

`file-format-32-address-object.md`

- An `address` object **MAY** contain a property named `length` whose value, if present, is an integer whose absolute value specifies the number of bytes in the range of addresses specified by this object. (line 137)
- A negative value for `length` **SHALL** mean that the data structure being described grows from higher addresses towards lower addresses (as, for example, is often the case for a stack). (line 139)
- If `length` is absent, it **SHALL** default to `null`, which indicates that the value is unknown (not set). (line 141)

## `name` Property

`file-format-32-address-object.md`

- An `address` object **MAY** contain a property named `name` whose value is a string containing the name of this address. (line 145)

## `fullyQualifiedName` Property

`file-format-32-address-object.md`

- An `address` object **MAY** contain a property named `fullyQualifiedName` whose value is a string containing the fully qualified name of this address. (line 149)

## `kind` Property

`file-format-32-address-object.md`

- An `address` object **MAY** contain a property named `kind` whose value is a string that specifies the kind of addressable region in which this address is located. (line 157)
- Although a function does contain executable code, the value `"function"` **SHOULD** be used for the address of the start of a function, because it is more specific. (line 185)
- The value `"instruction"` **SHOULD** be used for an address within the body of a function. (line 185)

## `parentIndex` Property

`file-format-32-address-object.md`

- If `theParent` exists (that is, if `thisObject` is expressed as an offset from some other address), then an `address` object **SHALL** contain a property named `parentIndex` whose value is the array index ([sec](#array-indices)) of `theParent` within `theRun.addresses` ([sec](#addresses-property)). (line 191)
- If `theParent` does not exist, then `parentIndex` **SHALL** be absent. (line 192)

## Logical Location Naming Rules

`file-format-33-logicallocation-object.md`

- Whenever possible, logical names and fully qualified logical names **SHOULD** conform to the syntax of the programming language in which the programmatic construct specified by the logical location was expressed. (line 14)

## `index` Property

`file-format-33-logicallocation-object.md`

- Depending on the circumstances, a `logicalLocation` object either **MAY, SHALL NOT**, or **SHALL** contain a property named `index` whose value is the array index ([sec](#array-indices)) within `theRun.logicalLocations` ([sec](#run-object--logicallocations-property)) of a `logicalLocation` object that provides the properties for `thisObject`. (line 40)
- If `thisObject` is an element of `theRun.logicalLocations`, then `index` **MAY** be present. (line 42)
- If present, its value **SHALL** be the index of `thisObject` within `theRun.logicalLocations`. (line 42)
- Otherwise, if `theRun.logicalLocations` is absent, or if it does not contain a cached object for `thisObject`, then `index` **SHALL NOT** be present. (line 44)
- Otherwise (that is, if `thisObject` belongs to a result, and `theRun.logicalLocations` contains a cached object for `thisObject`), then `index` **SHALL** be present, and its value **SHALL** be the array index within `theRun.logicalLocations` of the cached object. (line 46)
- If `index` is present, `thisObject` **SHALL** take all properties present on the cached object. (line 48)
- If `thisObject` contains any properties other than `index`, they **SHALL** equal the corresponding properties of the cached object. (line 48)

## `name` Property

`file-format-33-logicallocation-object.md`

- A `logicalLocation` object **SHOULD** contain a property named `name` whose value is the logical name of the programmatic construct specified by this object. (line 56)
- The `name` property **SHALL** be suitable for display and **SHALL** follow the naming rules for logical names described in [sec](#logical-location-naming-rules). (line 58)

## `fullyQualifiedName` Property

`file-format-33-logicallocation-object.md`

- Depending on the circumstances, a `logicalLocation` object either **SHOULD** or **MAY** contain a property named `fullyQualifiedName` whose value is the fully qualified name of the logical location. (line 74)
- This name **SHALL** follow the naming rules for fully qualified names described in [sec](#logical-location-naming-rules). (line 74)
- If this `logicalLocation` object represents a top-level logical location, then `fullyQualifiedName` **MAY** be present. (line 76)
- If present, it **SHALL** equal `name`; if absent, it **SHALL** default to `name`. (line 76)
- If this object does not represent a top-level logical location, `fullyQualifiedName` **SHOULD** be present. (line 76)

## `decoratedName` Property

`file-format-33-logicallocation-object.md`

- A `logicalLocation` object **MAY** contain a property named `decoratedName` whose value is a string containing the compiler's internal representation of the logical location associated with this `location` object. (line 143)

## `kind` Property

`file-format-33-logicallocation-object.md`

- A `logicalLocation` object **SHOULD** contain a property named `kind` whose value is one of the following strings, if any of those strings accurately describes the construct identified by this object. (line 159)
- Although the values suggested here are useful in the specified categories (for example, `"member"` is useful in describing executable code), they **MAY** be used in other contexts as appropriate. (line 161)
- If a logical location is both a member and a type (for example, a nested class in C++ or C#), the value of `kind`, if present, **SHALL** be `"type"`. (line 361)

## `parentIndex` Property

`file-format-33-logicallocation-object.md`

- If this `logicalLocation` object represents a nested logical location, then it **SHALL** contain a property named `parentIndex` whose value is the array index ([sec](#array-indices)) of the parent `logicalLocation` object within `theRun.logicalLocations` ([sec](#run-object--logicallocations-property)). (line 367)
- If `thisObject` represents a top-level logical location, then `parentIndex` **SHALL** be absent. (line 369)

## `target` Property

`file-format-34-locationrelationship-object.md`

- A `locationRelationship` object **SHALL** contain a property named `target` whose value is a non-negative integer which identifies `theTarget` (see [sec](#locationrelationship-object--general)) among all `location` objects ([sec](#location-object)) in `theResult` by virtue of being equal to `theTarget.id` ([sec](#location-object--id-property)). (line 79)

## `kinds` Property

`file-format-34-locationrelationship-object.md`

- A `locationRelationship` object **MAY** contain a property named `kinds` whose value is an array of one or more unique ([sec](#array-properties-with-unique-values)) strings each of which specifies a relationship between `theSource` and `theTarget` (see [sec](#locationrelationship-object--general)). (line 85)
- If `kinds` is absent, it **SHALL** default to `[ "relevant" ]` (see below for the meaning of `"relevant"`). (line 85)

## `description` Property

`file-format-34-locationrelationship-object.md`

- A `locationRelationship` object **MAY** contain a property named `description` whose value is a `message` object ([sec](#message-object)) that describes the relationship. (line 102)

## `kind` Property

`file-format-35-suppression-object.md`

- A `suppression` object **SHALL** contain a property named `kind` whose value is a string with one of the following values, with the specified meanings: (line 14)

## `status` Property

`file-format-35-suppression-object.md`

- A `suppression` object **MAY** contain a property named `status` whose value is a string with one of the following values, with the specified meanings: (line 26)

## `location` Property

`file-format-35-suppression-object.md`

- A `suppression` object **MAY** contain a property named `location` whose value is a `location` object ([sec](#location-object)) that specifies the location where the suppression is persisted. (line 36)

## `guid` Property

`file-format-35-suppression-object.md`

- A `suppression` object **MAY** contain a property named `guid` whose value is a GUID-valued string ([sec](#guid-valued-strings)). (line 56)

## `justification` Property

`file-format-35-suppression-object.md`

- A `suppression` object **MAY** contain a property named `justification` whose value is a user-supplied string that explains why the result was suppressed. (line 62)

## General

`file-format-36-codeflow-object.md`

- The thread flows in a code flow **MAY** lie within a single process, within multiple processes on the same machine, or within multiple processes on multiple machines. (line 6)

## `message` Property

`file-format-36-codeflow-object.md`

- A `codeFlow` object **MAY** contain a property named `message` whose value is a `message` object ([sec](#message-object)) relevant to the code flow. (line 65)

## `threadFlows` Property

`file-format-36-codeflow-object.md`

- A `codeFlow` object **SHALL** contain a property named `threadFlows` whose value is an array of one or more `threadFlow` objects ([sec](#threadflow-object)) each of which describes the progress of a program through a single thread of execution such as an operating system thread or a fiber. (line 68)

## `id` Property

`file-format-37-threadflow-object.md`

- A `threadFlow` object **MAY** contain a property named `id` whose value is a string that uniquely identifies this `threadFlow` within its containing `codeFlow` object ([sec](#codeflow-object)). (line 12)

## `message` Property

`file-format-37-threadflow-object.md`

- A `threadFlow` object **MAY** contain a property named `message` whose value is a `message` object ([sec](#message-object)) relevant to the thread flow. (line 18)

## `initialState` Property

`file-format-37-threadflow-object.md`

- A `threadFlow` object **MAY** contain a property named `initialState` whose value is an object ([sec](#object-properties)) each of whose property values is a `multiformatMessageString` object ([sec](#multiformatmessagestring-object)) that represents the initial value of a relevant item prior to the first location in the thread flow. (line 22)
- This property **SHOULD NOT** include items whose values remain constant throughout the thread flow. (line 24)
- Such items **SHOULD** be stored in the `immutableState` property ([sec](#threadflow-object--immutablestate-property)). (line 24)

## `immutableState` Property

`file-format-37-threadflow-object.md`

- A `threadFlow` object **MAY** contain a property named `immutableState` whose value is an object ([sec](#object-properties)) each of whose property values is a `multiformatMessageString` object ([sec](#multiformatmessagestring-object)) that represents the value of a relevant item that remains constant throughout the thread flow. (line 30)

## `locations` Property

`file-format-37-threadflow-object.md`

- A `threadFlow` object **SHALL** contain a property named `locations` whose value is an array of one or more `threadFlowLocation` objects ([sec](#threadflowlocation-object)). (line 46)

## `index` Property

`file-format-38-threadflowlocation-object.md`

- Depending on the circumstances, a `threadFlowLocation` object either **MAY**, **SHALL NOT**, or **SHALL** contain a property named `index` whose value is the array index ([sec](#array-indices)) within `theRun.threadFlowLocations` ([sec](#threadflowlocations-property)) of a `threadFlowLocation` object that provides the properties for `thisObject`. (line 10)
- If `thisObject` is an element of `theRun.threadFlowLocations`, then `index` **MAY** be present. (line 12)
- If present, its value **SHALL** be the index of `thisObject` within `theRun.threadFlowLocations`. (line 12)
- Otherwise, if `theRun.threadFlowLocations` is absent, or if it does not contain a cached object for `thisObject`, then `index` **SHALL NOT** be present. (line 14)
- Otherwise (that is, if `thisObject` belongs to a result, and `theRun.threadFlowLocations` contains a cached object for `thisObject`), then `index` **SHALL** be present, and its value **SHALL** be the index within `theRun.threadFlowLocations` of the cached object. (line 16)
- If `index` is present, `thisObject` **SHALL** take all properties present on the cached object. (line 18)
- If `thisObject` contains any properties other than `index`, they **SHALL** equal the corresponding properties of the cached object. (line 18)

## `location` Propertyy

`file-format-38-threadflowlocation-object.md`

- If location information is available, a `threadFlowLocation` object **SHALL** contain a property named `location` whose value is a `location` object ([sec](#location-object)) that specifies the location to which the `threadFlowLocation` object refers. (line 107)
- If location information is not available, `location` **SHALL** be absent. (line 107)

## `module` Property

`file-format-38-threadflowlocation-object.md`

- A `threadFlowLocation` object **MAY** contain a property named `module` whose value is a string containing the name of the module that contains the code location specified by this object. (line 167)

## `stack` Property

`file-format-38-threadflowlocation-object.md`

- A `threadFlowLocation` object **MAY** contain a property named `stack` whose value is a `stack` object ([sec](#stack-object)) that represents the call stack leading to this location. (line 171)

## `webRequest` Property

`file-format-38-threadflowlocation-object.md`

- A `threadFlowLocation` object **MAY** contain a property named `webRequest` whose value is a `webRequest` object ([sec](#webrequest-object)) that describes an HTTP request sent from this location. (line 175)

## `webResponse` Property

`file-format-38-threadflowlocation-object.md`

- A `threadFlowLocation` object **MAY** contain a property named `webResponse` whose value is a `webResponse` object ([sec](#webresponse-object)) that describes the response to the HTTP request sent from this location. (line 181)

## `kinds` Property

`file-format-38-threadflowlocation-object.md`

- A `threadFlowLocation` object **MAY** contain a property named `kinds` whose value is an array of unique ([sec](#array-properties-with-unique-values)) strings that describe the meaning of this location. (line 187)
- The strings **SHOULD** be human-readable (as opposed to, for example, GUIDs or hash values). (line 187)

## `state` Property

`file-format-38-threadflowlocation-object.md`

- A `threadFlowLocation` object **MAY** contain a property named `state` whose value is an object ([sec](#object-properties)) in which each property name represents an item relevant to the location in the context of the code flow, and the corresponding property value is a `multiformatMessageString` object ([sec](#multiformatmessagestring-object)) that specifies either the value of or a constraint on that item. (line 338)
- A constraint which expresses the equality of `"{expr}"` with a literal value **SHALL** be considered equivalent to that literal value. (line 385)

## `nestingLevel` Property

`file-format-38-threadflowlocation-object.md`

- A `threadFlowLocation` object **MAY** contain a property named `nestingLevel` whose value is a non-negative integer that represents any type of logical containment hierarchy among the `threadFlowLocation` objects in the `threadFlow`. (line 391)

## `executionOrder` Property

`file-format-38-threadflowlocation-object.md`

- A `threadFlowLocation` object **MAY** contain a property named `executionOrder` whose value is a non-negative integer that represents the temporal order in which execution reached this location, across all `threadFlowLocation` objects within all `threadFlow` objects belonging to a single `codeFlow` ([sec](#codeflow-object)). (line 397)
- For that reason, values of `executionOrder` within a single `threadFlow` **SHALL** be unique. (line 397)
- If `executionOrder` is absent, it **SHALL** default to -1, which indicates that the value is unknown (not set). (line 401)

## `executionTimeUtc` Property

`file-format-38-threadflowlocation-object.md`

- A `threadFlowLocation` object **MAY** contain a property named `executionTimeUtc` whose value is a string in the format specified in [sec](#datetime-properties), specifying the UTC date and time at which the thread of execution through the code reached this location. (line 407)

## `importance` Property

`file-format-38-threadflowlocation-object.md`

- A `threadFlowLocation` **MAY** contain a property named `importance` whose value is a string that specifies the importance of this `threadFlowLocation` in understanding the code flow. (line 411)
- The `importance` property **SHALL** have one of the following values, with the specified meanings: (line 413)
- If this property is absent, it **SHALL** be considered to have the value `"important"`. (line 421)

## `taxa` Property

`file-format-38-threadflowlocation-object.md`

- A `threadFlowLocation` **MAY** contain a property named `taxa` whose value is an array of zero or more unique ([sec](#array-properties-with-unique-values)) `reportingDescriptorReference` objects each of which specifies a category into which this `threadFlowLocation` falls. (line 433)

## General

`file-format-39-graph-object.md`

- `graph` objects **MAY** be defined both at the run level in `run.graphs` ([sec](#run-object--graphs-property)) and at the result level in `result.graphs` ([sec](#result-object--graphs-property)). (line 6)

## `description` Property

`file-format-39-graph-object.md`

- A `graph` object **MAY** contain a property named `description` whose value is a `message` object ([sec](#message-object)) that describes the graph. (line 12)

## `nodes` Property

`file-format-39-graph-object.md`

- A `graph` object **MAY** contain a property named `nodes` whose value is an array of zero or more unique ([sec](#array-properties-with-unique-values)) `node` objects ([sec](#node-object)) which represent the nodes of the graph. (line 16)

## `edges` Property

`file-format-39-graph-object.md`

- A `graph` object **MAY** contain a property named `edges` whose value is an array of zero or more unique ([sec](#array-properties-with-unique-values)) `edge` objects ([sec](#edge-object)) which represent the edges of the graph. (line 19)

## `id` Property

`file-format-40-node-object.md`

- A `node` object **SHALL** contain a property named `id` whose value is a string that uniquely identifies the node within `theGraph`. (line 10)
- `id` **SHALL** be unique among all nodes in `theGraph`, regardless of nesting (see [sec](#children-property)). (line 10)

## `label` Property

`file-format-40-node-object.md`

- A `node` object **MAY** contain a property named `label` whose value is a `message` object ([sec](#message-object)) that provides a short description of the node. (line 40)

## `location` Property

`file-format-40-node-object.md`

- A `node` object **SHOULD** have a property named `location` whose value is a `location` object ([sec](#location-object)) that specifies the location associated with the node. (line 44)

## `children` Property

`file-format-40-node-object.md`

- A `node` object **MAY** contain a property named `children` whose value is an array of zero or more unique ([sec](#array-properties-with-unique-values)) `node` objects, referred to as "child nodes." (line 48)

## `id` Property

`file-format-41-edge-object.md`

- An `edge` object **SHALL** contain a property named `id` whose value is a string that uniquely identifies the edge within `theGraph`. (line 10)

## `label` Property

`file-format-41-edge-object.md`

- An `edge` object **MAY** contain a property named `label` whose value is a `message` object ([sec](#message-object)) that provides a short description of the edge. (line 14)

## `sourceNodeId` Property

`file-format-41-edge-object.md`

- An `edge` object **SHALL** contain a property named `sourceNodeId` whose value is a string that identifies the source node (the node at which the edge starts). (line 18)
- It **SHALL** equal the `id` property ([sec](#node-object--id-property)) of one of the `node` objects ([sec](#node-object)) in `theGraph`. (line 18)
- It **MAY** equal the id of any node within `theGraph`, regardless of nesting (see [sec](#children-property)). (line 18)

## `targetNodeId` Property

`file-format-41-edge-object.md`

- An `edge` object **SHALL** contain a property named `targetNodeId` whose value is a string that identifies the target node (the node at which the edge ends). (line 53)
- It **SHALL** equal the `id` property ([sec](#node-object--id-property)) of one of the `node` objects ([sec](#node-object)) in `theGraph`. (line 53)
- It **MAY** equal `sourceNodeId` ([sec](#sourcenodeid-property)). (line 53)

## Constraints

`file-format-42-graphtraversal-object.md`

- Exactly one of the `resultGraphIndex` property ([sec](#resultgraphindex-property)) and the `runGraphIndex` property ([sec](#rungraphindex-property)) **SHALL** be present. (line 10)

## `resultGraphIndex` Property

`file-format-42-graphtraversal-object.md`

- If a `graphTraversal` object represents the traversal of a `graph` object ([sec](#graph-object)) that resides in `theResult.graphs` ([sec](#result-object--graphs-property)), the `graphTraversal` object **SHALL** contain a property named `resultGraphIndex` whose value is the array index ([sec](#array-indices)) within `theResult.graphs` of that `graph` object. (line 14)

## `runGraphIndex` Property

`file-format-42-graphtraversal-object.md`

- If a `graphTraversal` object represents the traversal of a `graph` object ([sec](#graph-object)) that resides in `theRun.graphs` ([sec](#run-object--graphs-property)), the `graphTraversal` object **SHALL** contain a property named `runGraphIndex` whose value is the array index ([sec](#array-indices)) within `theRun.graphs` of that `graph` object. (line 18)

## `description` Property

`file-format-42-graphtraversal-object.md`

- A `graphTraversal` object **MAY** contain a property named `description` whose value is a `message` object ([sec](#message-object)) that describes the graph traversal. (line 22)

## `initialState` Property

`file-format-42-graphtraversal-object.md`

- A `graphTraversal` object **MAY** contain a property named `initialState` whose value is an object ([sec](#object-properties)) each of whose properties is a `multiformatMessageString` object ([sec](#multiformatmessagestring-object)) that represents the value of a relevant item at the point of entry to the graph. (line 26)
- This property **SHOULD NOT** include items whose value remains constant throughout the traversal. (line 28)
- Such items **SHOULD** be stored in the `immutableState` property ([sec](#graphtraversal-object--immutablestate-property)). (line 28)

## `immutableState` Property

`file-format-42-graphtraversal-object.md`

- A `graphTraversal` object **MAY** contain a property named `immutableState` whose value is an object ([sec](#object-properties)) each of whose properties is a `multiformatMessageString` object ([sec](#multiformatmessagestring-object)) that represents the value of a relevant item that remains constant throughout the traversal. (line 34)

## `edgeTraversals` Property

`file-format-42-graphtraversal-object.md`

- A `graphTraversal` object **MAY** contain a property named `edgeTraversals` whose value is an array of zero or more `edgeTraversal` objects ([sec](#edgetraversal-object)) which together represent the sequence of edges traversed during this graph traversal. (line 50)
- The `edgeTraversal` objects **SHALL** be connected end to end; that is, the target node of every traversed edge except the last **SHALL** equal the source node of the next edge. (line 52)

## `edgeId` Property

`file-format-43-edgetraversal-object.md`

- An `edgeTraversal` object **SHALL** contain a property named `edgeId` whose value is a string which equals the `id` property ([sec](#edge-object--id-property)) of one of the `edge` objects ([sec](#edge-object)) in the graph identified by the `resultGraphIndex` property ([sec](#resultgraphindex-property)) or the `runGraphIndex` property ([sec](#rungraphindex-property)) of the containing `graphTraversal` object ([sec](#graphtraversal-object)). (line 10)

## `message` Property

`file-format-43-edgetraversal-object.md`

- An `edgeTraversal` object **MAY** contain a property named `message` whose value is a `message` object ([sec](#message-object)) that contains a message to display to the user as the edge is traversed. (line 14)

## `finalState` Property

`file-format-43-edgetraversal-object.md`

- An `edgeTraversal` object **MAY** contain a property named `finalState` whose value is an object ([sec](#object-properties)) each of whose properties is a `multiformatMessageString` object ([sec](#multiformatmessagestring-object)) that represents the value of a relevant item after the edge has been traversed. (line 18)
- It **SHALL NOT** assume that properties present in previous steps are still present with unchanged values. (line 22)

## `stepOverEdgeCount` Property

`file-format-43-edgetraversal-object.md`

- An `edgeTraversal` object **MAY** contain a property named `stepOverEdgeCount` whose value is a non-negative integer specifying the number of edges a user can step over. (line 28)
- Therefore, this property **SHOULD** be specified only on an edge that leads from a node to one of its child nodes, and its value **SHOULD** be the number of edges the user would need to traverse to return to the current nesting level. (line 30)

## `message` Property

`file-format-44-stack-object.md`

- A `stack` object **MAY** contain a property named `message` whose value is `message` object ([sec](#message-object)) relevant to this call stack. (line 10)

## `frames` Property

`file-format-44-stack-object.md`

- A stack object **SHALL** contain a property named `frames` whose value is an array of zero or more `stackFrame` objects ([sec](#stackframe-object)). (line 14)

## `location` Property

`file-format-45-stackframe-object.md`

- A `stackFrame` object **MAY** contain a property named `location` whose value is a `location` object ([sec](#location-object)) specifying the location to which this stack frame refers. (line 10)
- If location information is unavailable (as it might be, for example, when stepping from application code into library code or operating system code), `location` **SHOULD** be present and **SHOULD** contain a `message` property ([sec](#location-object)) (for example, with a message string `"Call into external code"`). (line 12)

## `module` Property

`file-format-45-stackframe-object.md`

- A `stackFrame` object **MAY** contain a property named `module` whose value is a string containing the name of the module that contains the location to which this stack frame refers. (line 16)

## `threadId` Property

`file-format-45-stackframe-object.md`

- A `stackFrame` object **MAY** contain a property named `threadId` whose value is an integer which identifies the thread on which the code at the location specified by this object was executed. (line 20)

## `parameters` Property

`file-format-45-stackframe-object.md`

- A `stackFrame` object **MAY** contain a property named parameters whose value is an array of zero or more strings representing the parameters of the function call represented by this stack frame. (line 23)

## `index` Property

`file-format-46-webrequest-object.md`

- Depending on the circumstances, a `webRequest` object either **MAY, SHALL NOT**, or **SHALL** contain a property named `index` whose value is the array index ([sec](#array-indices)) within `theRun.webRequests` ([sec](#webrequests-property)) of a `webRequest` object that provides the properties for `thisObject`. (line 16)
- If `thisObject` is an element of `theRun.webRequests`, then `index` **MAY** be present. (line 18)
- If present, its value **SHALL** be the index of `thisObject` within `theRun.webRequests`. (line 18)
- Otherwise, if `theRun.webRequests` is absent, or if it does not contain a cached object for `thisObject`, then `index` **SHALL NOT** be present. (line 20)
- Otherwise (that is, if `thisObject` belongs to a result, and `theRun.webRequests` contains a cached object for `thisObject`), then `index` **SHALL** be present, and its value **SHALL** be the array index within `theRun.webRequests` of the cached object. (line 22)
- If `index` is present, `thisObject` **SHALL** take all properties present on the cached object. (line 24)
- If `thisObject` contains any properties other than `index`, they **SHALL** equal the corresponding properties of the cached object. (line 24)

## `protocol` Property

`file-format-46-webrequest-object.md`

- A `webRequest` object **SHOULD** contain a property named `protocol` whose value is a string containing the name of the web protocol used in the request, found on the HTTP request line. (line 32)

## `version` Property

`file-format-46-webrequest-object.md`

- A `webRequest` object **SHOULD** contain a property named `version` whose value is a string containing the version of the web protocol used in the request, found on the HTTP request line. (line 38)

## `method` Property

`file-format-46-webrequest-object.md`

- A `webRequest` object **SHOULD** contain a property named `method` whose value is a string containing the HTTP method used in the request, found on the HTTP request line. (line 48)
- The string **SHOULD** be one of the values `"GET"`, `"PUT"`, `"POST"`, `"DELETE"`, `"PATCH"`, `"HEAD"`, `"OPTIONS"`, `"TRACE"`, or `"CONNECT"`. (line 48)

## `headers` Property

`file-format-46-webrequest-object.md`

- A `webRequest` object **SHOULD** contain a property named `headers` whose value is an object ([sec](#object-properties)) whose property names are the names of the HTTP headers in the request (for example, `"Content-Type"`) and whose corresponding values are the header values (for example, `"text/plain; charset=ascii"`). (line 52)

## `parameters` Property

`file-format-46-webrequest-object.md`

- A `webRequest` object **MAY** contain a property named `parameters` whose value is an object ([sec](#object-properties)) whose property names are the names of the parameters in the request and whose corresponding values are the values of those parameters. (line 56)

## `body` Property

`file-format-46-webrequest-object.md`

- A `webRequest` object **MAY** contain a property named `body` whose value is an `artifactContent` object ([sec](#artifactcontent-object)) containing the body of the request. (line 62)
- If the request body is entirely textual, `body.text` ([sec](#artifactcontent-object--text-property)) **SHOULD** be present. (line 64)
- If present, it **SHALL** contain the request body, transcoded to UTF-8 if necessary. (line 64)
- If the request body is entirely textual, `body.binary` ([sec](#binary-property)) **MAY** be present. (line 70)
- If present, it **SHALL** contain the MIME Base64 encoding [cite](#RFC2045) of the body as it was actually transmitted. (line 70)
- If the request body consists partially or entirely of binary data, `body.binary` **SHALL** be present and **SHALL** contain the MIME Base64 encoding of the body. (line 71)
- In this situation, `body.text` **SHALL** be absent. (line 71)

## `index` Property

`file-format-47-webresponse-object.md`

- Depending on the circumstances, a `webResponse` object either **MAY, SHALL NOT**, or **SHALL** contain a property named `index` whose value is the array index ([sec](#array-indices)) within `theRun.webResponses` ([sec](#webresponses-property)) of a `webResponse` object that provides additional properties for `thisObject`. (line 16)
- If `thisObject` is an element of `theRun.webResponses`, then `index` **MAY** be present. (line 18)
- If present, its value **SHALL** be the index of `thisObject` within `theRun.webResponses`. (line 18)
- Otherwise, if `theRun.webResponses` is absent, or if it does not contain a cached object for `thisObject`, then `index` **SHALL NOT** be present. (line 20)
- Otherwise (that is, if `thisObject` belongs to a result, and `theRun.webResponses` contains a cached object for `thisObject`), then `index` **SHALL** be present, and its value **SHALL** be the array index within `theRun.webResponses` of the cached object. (line 22)
- If `index` is present, `thisObject` **SHALL** take all properties present on the cached object. (line 24)
- If `thisObject` contains any properties other than `index`, they **SHALL** equal the corresponding properties of the cached object. (line 24)

## `protocol` Property

`file-format-47-webresponse-object.md`

- A `webResponse` object **SHOULD** contain a property named `protocol` whose value is a string containing the name of the web protocol used in the response, found on the HTTP status line. (line 32)

## `version` Property

`file-format-47-webresponse-object.md`

- A `webResponse` object **SHOULD** contain a property named `version` whose value is a string containing the version of the web protocol used in the response, found on the HTTP status line. (line 38)

## `statusCode` Property

`file-format-47-webresponse-object.md`

- A `webResponse` object **SHOULD** contain a property named `statusCode` whose value is an integer containing the status code that describes the result of the request, found on the HTTP status line. (line 44)

## `reasonPhrase` Property

`file-format-47-webresponse-object.md`

- A `webResponse` object **SHOULD** contain a property named `reasonPhrase` whose value is a string containing the textual description of the `statusCode` ([sec](#statuscode-property)) found on the HTTP status line. (line 50)
- If `noResponseReceived` ([sec](#noresponsereceived-property)) is `true`, then `reasonPhrase` **SHOULD** instead contain a string describing the reason that no response was received. (line 54)

## `headers` Property

`file-format-47-webresponse-object.md`

- A `webResponse` object **SHOULD** contain a property named `headers` whose value is an object ([sec](#object-properties)) whose property names are the names of the HTTP headers in the response (for example, `"Content-Type"`) and whose corresponding values are the header values (for example, `"text/plain; charset=ascii"`). (line 58)

## `body` Property

`file-format-47-webresponse-object.md`

- A `webResponse` object **MAY** contain a property named `body` whose value is an `artifactContent` object ([sec](#artifactcontent-object)) containing the body of the response. (line 62)
- If the response body is entirely textual, `body.text` ([sec](#artifactcontent-object--text-property)) **SHOULD** be present. (line 64)
- If present, it **SHALL** contain the response body, transcoded to UTF-8 if necessary. (line 64)
- If the response body is entirely textual, `body.binary` ([sec](#binary-property)) **MAY** be present. (line 70)
- If present, it **SHALL** contain the MIME Base64 encoding [cite](#RFC2045) of the body as it was actually transmitted. (line 70)
- If the response body consists partially or entirely of binary data, `body.binary` **SHALL** be present and **SHALL** contain the MIME Base64 encoding of the body. (line 72)
- In this situation, `body.text` **SHALL** be absent. (line 72)

## `noResponseReceived` Property

`file-format-47-webresponse-object.md`

- If no response to the HTTP request was received (for example, because of a network failure), the `webResponse` object **SHALL** contain a property named `noResponseReceived` whose value is a Boolean `true`. (line 76)
- If a response was received, `noResponseReceived` **SHALL** either be present with the value `false`, or absent, in which case it defaults to `false`. (line 76)
- If `noResponseReceived` is `true`, then `reasonPhrase` ([sec](#reasonphrase-property)), which normally contains the reason phrase from the HTTP response line, **SHOULD** instead contain a string describing the reason that no response was received. (line 77)

## `firstDetectionTimeUtc` Property

`file-format-48-resultprovenance-object.md`

- A `resultProvenance` object **MAY** contain a property named `firstDetectionTimeUtc` whose value is a string in the format specified in [sec](#datetime-properties), specifying the UTC date and time at which the result was first detected. (line 18)
- It **SHOULD** specify the start time of the run in which the result was first detected, as opposed to, for example, the time within the run at which the result was actually generated. (line 18)

## `lastDetectionTimeUtc` Property

`file-format-48-resultprovenance-object.md`

- A `resultProvenance` object **MAY** contain a property named `lastDetectionTimeUtc` whose value is a string in the format specified in [sec](#datetime-properties), specifying the UTC date and time at which the result was most recently detected. (line 24)
- It **SHOULD** specify the start time of the run in which the result was most recently detected, as opposed to, for example, the time within the run at which the result was actually generated. (line 24)
- If `lastDetectionTimeUtc` is absent, its default value **SHALL** be determined as follows: (line 28)

## `firstDetectionRunGuid` Property

`file-format-48-resultprovenance-object.md`

- A `resultProvenance` object **MAY** contain a property named `firstDetectionRunGuid` whose value is a GUID-valued string ([sec](#guid-valued-strings)) which **SHALL** equal the `automationDetails.guid` property ([sec](#automationdetails-property), [sec](#runautomationdetails-object--guid-property)) of the run in which `theResult` was first detected (either the current run or some previous run). (line 36)

## `lastDetectionRunGuid` Property

`file-format-48-resultprovenance-object.md`

- A `resultProvenance` object **MAY** contain a property named `lastDetectionRunGuid` whose value is a GUID-valued string ([sec](#guid-valued-strings)) which **SHALL** equal the `automationDetails.guid` property ([sec](#automationdetails-property), [sec](#runautomationdetails-object--guid-property)) of the run in which `theResult` was most recently detected (either the current run or some previous run). (line 40)

## `invocationIndex` Property

`file-format-48-resultprovenance-object.md`

- If `theRun.invocations` is absent, `invocationIndex` **SHALL** be absent. (line 46)
- If `invocationIndex` is absent and `theRun.invocations` is present and contains a single element, it **SHALL** default to 0; otherwise it **SHALL** default to -1, which indicates that the value is unknown (not set). (line 50)

## `conversionSources` Property

`file-format-48-resultprovenance-object.md`

- A `resultProvenance` object **MAY** contain a property named `conversionSources` whose value is an array of zero or more unique ([sec](#array-properties-with-unique-values)) `physicalLocation` objects ([sec](#physicallocation-object)). (line 58)

## Constraints

`file-format-49-reportingdescriptor-object.md`

- Either the `shortDescription` property ([sec](#reportingdescriptor-object--shortdescription-property)) or the `fullDescription` property ([sec](#reportingdescriptor-object--fulldescription-property)) or both **SHOULD** be present. (line 12)

## `id` Property

`file-format-49-reportingdescriptor-object.md`

- A `reportingDescriptor` object **SHALL** contain a property named `id` whose value is a string. (line 16)
- In the case of a rule, `id` **SHALL** contain a stable identifier for the rule and **SHOULD** be opaque. (line 16)
- In the case of a notification, `id` does not need be a stable, opaque identifier; it **MAY** be a user-readable identifier. (line 16)

## `guid` Property

`file-format-49-reportingdescriptor-object.md`

- A `reportingDescriptor` object **MAY** contain a property named `guid` whose value is a GUID-valued string ([sec](#guid-valued-strings)) that uniquely identifies the descriptor. (line 148)

## `name` Property

`file-format-49-reportingdescriptor-object.md`

- A `reportingDescriptor` object **MAY** contain a property named `name` whose value is a localizable string ([sec](#localizable-strings)) containing an identifier that is understandable to an end user. (line 156)

## `deprecatedNames` Property

`file-format-49-reportingdescriptor-object.md`

- The array elements **SHALL** occur in the same order in every translation ([sec](#taxonomies)). (line 166)

## `shortDescription` Property

`file-format-49-reportingdescriptor-object.md`

- A `reportingDescriptor` object **MAY** contain a property named `shortDescription` whose value is a localizable `multiformatMessageString` object ([sec](#multiformatmessagestring-object), [sec](#localizable-multiformatmessagestrings)) that provides a concise description of the reporting item. (line 170)
- The `shortDescription` property **SHOULD** be a single sentence that is understandable when visible space is limited to a single line of text. (line 170)

## `fullDescription` Property

`file-format-49-reportingdescriptor-object.md`

- A `reportingDescriptor` object **SHOULD** contain a property named `fullDescription` whose value is a localizable `multiformatMessageString` object ([sec](#multiformatmessagestring-object), [sec](#localizable-multiformatmessagestrings)) that comprehensively describes the reporting item. (line 184)
- The `fullDescription` property **SHOULD**, as far as possible, provide details sufficient to enable resolution of any problem indicated by the reporting item. (line 186)
- The beginning of `fullDescription` (for example, its first sentence) **SHOULD** provide a concise description of the reporting item, suitable for display in cases where available space is limited. (line 188)
- Tools that do not construct `fullDescription` in this way **SHOULD** provide a value for `shortDescription`. (line 188)

## `messageStrings` Property

`file-format-49-reportingdescriptor-object.md`

- A `reportingDescriptor` object **MAY** contain a property named `messageStrings` whose value is an object ([sec](#object-properties)) consisting of a set of properties with arbitrary names, each of whose values is a localizable `multiformatMessageString` object ([sec](#multiformatmessagestring-object), [sec](#localizable-multiformatmessagestrings)). (line 194)
- If the `reportingDescriptor` object defines a rule, the set of property names appearing in the `messageStrings` property **SHALL** contain at least the set of strings which occur as values of `result.message.id` properties ([sec](#result-object--message-property), [sec](#message-object--id-property)) in the current `run` object. (line 196)
- The `messageStrings` property **MAY** contain additional properties whose names do not appear as the value of the `result.message.id` property for any `result` object in the `run`. (line 196)
- If the `reportingDescriptor` object describes a notification, the set of property names appearing in the `messageStrings` property **SHALL** contain at least the set of strings which occur as values of `notification.message.id` for any `notification` object in the run. (line 198)

## `helpUri` Property

`file-format-49-reportingdescriptor-object.md`

- A `reportingDescriptor` object **MAY** contain a property named `helpUri` whose value is a localizable string ([sec](#localizable-strings)) containing the absolute URI [cite](#RFC3986) of the primary documentation for the reporting item. (line 226)

## `help` Property

`file-format-49-reportingdescriptor-object.md`

- A `reportingDescriptor` object **MAY** contain a property named `help` whose value is a localizable `multiformatMessageString` object ([sec](#multiformatmessagestring-object), [sec](#localizable-multiformatmessagestrings)) which provides the primary documentation for the reporting item. (line 234)

## `defaultConfiguration` Property

`file-format-49-reportingdescriptor-object.md`

- A `reportingDescriptor` object **MAY** contain a property named `defaultConfiguration` whose value is a `reportingConfiguration` object ([sec](#reportingconfiguration-object)). (line 240)
- If this property is absent, it **SHALL** be taken to be present, and its properties **SHALL** be taken to have the default values specified in [sec](#reportingconfiguration-object). (line 242)
- The rule- or notification-specific configuration parameters for a `reportingDescriptor`, if any, **SHALL NOT** be stored in its property bag ([sec](#property-bags)) Rather, they **SHALL** be stored in `defaultConfiguration.parameters` ([sec](#reportingconfiguration-object--parameters-property)). (line 244)

## `precision` Property

`file-format-49-reportingdescriptor-object.md`

- This value **MAY** be represented as a floating-point number. (line 248)

## `securitySeverity` Property

`file-format-49-reportingdescriptor-object.md`

- A `reportingDescriptor` object that describes a rule **MAY** contain a property named `securitySeverity` whose value is a number between `0.0` and `100.0` inclusive, representing a numerical estimate of the severity of the class of vulnerabilities found by results produced by the rule. (line 258)
- This value **MAY** be represented as a floating-point number. (line 258)

## `relationships` Property

`file-format-49-reportingdescriptor-object.md`

- A `reportingDescriptor` object **MAY** contain a property named `relationships` whose value is an array of zero or more unique ([sec](#array-properties-with-unique-values)) `reportingDescriptorRelationship` objects ([sec](#reportingdescriptorrelationship-object)) each of which declares one or more directed relationships from `thisObject` to another `reportingDescriptor` object, which we refer to as `theTarget`, specified by `reportingDescriptorRelationship`.`target` ([sec](#reportingdescriptorrelationship-object--target-property)). (line 269)

## `enabled` Property

`file-format-50-reportingconfiguration-object.md`

- A `reportingConfiguration` object **MAY** contain a property named `enabled` whose value is a Boolean that specifies whether the condition described by `theDescriptor` was checked for during the scan. (line 14)
- If this property is absent, it **SHALL** default to `true`. (line 16)

## `level` Property

`file-format-50-reportingconfiguration-object.md`

- A `reportingConfiguration` object **MAY** contain a property named `level` whose value is one of the strings `"warning"`, `"error"`, `"note"`, or `"none"`, with the same meanings as when those strings appear as the value of `result.level` ([sec](#result-object--level-property)) or `notification.level` ([sec](#notification-object--level-property)). (line 24)
- If `level` is absent, it **SHALL** default to `"warning"`. (line 26)
- If `theDescriptor` describes a rule, then if `level` is present, it **SHALL** provide the value for the `level` property of any `result` object ([sec](#result-object)) whose `ruleIndex` ([sec](#ruleindex-property)) or `rule` property ([sec](#rule-property)), either explicitly supplied or inferred from its default, identifies `theDescriptor` and which does not itself specify a `level` property. (line 28)
- If `theDescriptor` describes a notification, then if `level` is present, it **SHALL** provide the value for the `level` property of any `notification` object ([sec](#notification-object)) whose `descriptor` property ([sec](#notification-object--descriptor-property)) identifies `theDescriptor` and which does not itself specify a `level` property. (line 30)

## `rank` Property

`file-format-50-reportingconfiguration-object.md`

- A `reportingConfiguration` object **MAY** contain a property named `rank` whose value is a number between `0.0` and `100.0` inclusive, with the same interpretation as the value of the `result.rank` ([sec](#result-object--rank-property)). (line 38)
- If `rank` is absent, it **SHALL** default to `-1.0`, which indicates that the value is unknown (not set). (line 40)
- If `theDescriptor` describes a rule, then if `rank` is present, it **SHALL** provide the value for the `rank` property of any `result` object ([sec](#result-object)) whose `ruleIndex` ([sec](#ruleindex-property)) or `rule` property ([sec](#rule-property)), either explicitly supplied or inferred from its default, identifies `theDescriptor` and which does not itself specify a `rank` property. (line 42)

## `parameters` Property

`file-format-50-reportingconfiguration-object.md`

- A `reportingConfiguration` object **MAY** contain a property named `parameters` whose value is a property bag ([sec](#property-bags)). (line 48)

## `descriptor` Property

`file-format-51-configurationoverride-object.md`

- A `configurationOverride` object **SHALL** contain a property named `descriptor` whose value is a `reportingDescriptorReference` object ([sec](#reportingdescriptorreference-object)) that identifies the `reportingDescriptor` ([sec](#reportingdescriptor-object)) whose runtime configuration is to be modified, which we refer to as `theDescriptor`. (line 51)

## `configuration` Property

`file-format-51-configurationoverride-object.md`

- A `configurationOverride` object **SHALL** contain a property named `configuration` whose value is a `reportingConfiguration` object ([sec](#reportingconfiguration-object)) each of whose properties overrides the corresponding property in `theDescriptor.defaultConfiguration` ([sec](#defaultconfiguration-property)). (line 54)

## General

`file-format-52-reportingdescriptorreference-object.md`

- In that case, the `reportingDescriptorReference` object **SHALL** contain only the `id` property ([sec](#reportingdescriptorreference-object--id-property)), and `theDescriptor` does not exist. (line 8)

## Constraints

`file-format-52-reportingdescriptorreference-object.md`

- If metadata is present, at least one of `index` ([sec](#reportingdescriptorreference-object--index-property)) and `guid` ([sec](#reportingdescriptorreference-object--guid-property)) **SHALL** be present. (line 34)
- If both are present, they **SHALL** identify the same `reportingDescriptor` object ([sec](#reportingdescriptor-object)). (line 34)

## Reportingdescriptor Lookup

`file-format-52-reportingdescriptorreference-object.md`

- `theDescriptor` **SHALL** be located within the `toolComponent` object ([sec](#toolcomponent-object)) identified by the `toolComponent` property ([sec](#toolcomponent-property)), which we refer to as `theComponent`. (line 38)
- `theDescriptor` **SHALL** be located either within `theComponent.rules` ([sec](#rules-property)) or `theComponent.notifications` ([sec](#notifications-property)), according to this table: (line 40)

## `id` Property

`file-format-52-reportingdescriptorreference-object.md`

- A `reportingDescriptorReference` object **MAY** contain a property named `id` whose value is a hierarchical string ([sec](#hierarchical-strings)) that either equals `theDescriptor.id` ([sec](#reportingdescriptor-object--id-property)) or equals `theDescriptor.id` plus one additional hierarchical component. (line 54)
- If `id` is absent and `theResult.ruleId` ([sec](#ruleid-property)) is present, then `id` **SHALL** default to `theResult.ruleId`. (line 58)
- If both are present, they **SHALL** be equal. (line 58)

## `index` Property

`file-format-52-reportingdescriptorreference-object.md`

- A `reportingDescriptorReference` object **MAY** contain a property named `index` whose value is the array index ([sec](#array-indices)) into `theComponent.rules` ([sec](#rules-property)) or `theComponent.notifications` ([sec](#notifications-property)), according to the table in [sec](#reportingdescriptor-lookup). (line 110)
- If `index` is absent and `theResult.ruleIndex` ([sec](#ruleindex-property)) is present, `index` **SHALL** default to `theResult.ruleIndex`. (line 144)
- If both are present, they **SHALL** be equal. (line 144)

## `guid` Property

`file-format-52-reportingdescriptorreference-object.md`

- A `reportingDescriptorReference` object **MAY** contain a property named `guid` whose value is a GUID-valued string ([sec](#guid-valued-strings)) equal to `theDescriptor.guid` ([sec](#reportingdescriptor-object--guid-property)). (line 148)

## `toolComponent` Property

`file-format-52-reportingdescriptorreference-object.md`

- A `reportingDescriptorReference` object **MAY** contain a property named `toolComponent` whose value is a `toolComponentReference` object ([sec](#toolcomponentreference-object)) that identifies `theComponent`. (line 152)

## `target` Property

`file-format-53-reportingdescriptorrelationship-object.md`

- A `reportingDescriptorRelationship` object **SHALL** contain a property named `target` whose value is a `reportingDescriptorReference` object which identifies `theTarget` (see [sec](#reportingdescriptorrelationship-object--general)). (line 103)

## `kinds` Property

`file-format-53-reportingdescriptorrelationship-object.md`

- A `reportingDescriptorRelationship` object **MAY** contain a property named `kinds` whose value is an array of one or more unique ([sec](#array-properties-with-unique-values)) strings each of which specifies a relationship between `theSource` and `theTarget` (see [sec](#reportingdescriptorrelationship-object--general)). (line 107)
- If `kinds` is absent, it **SHALL** default to `[ "relevant" ]` (see below for the meaning of `"relevant"`). (line 107)

## `description` Property

`file-format-53-reportingdescriptorrelationship-object.md`

- A `reportingDescriptorRelationship` object **MAY** contain a property named `description` whose value is a `message` object ([sec](#message-object)) that describes the relationship. (line 138)

## Toolcomponent Lookup

`file-format-54-toolcomponentreference-object.md`

- If neither `index` ([sec](#toolcomponentreference-object--index-property)) nor `guid` ([sec](#toolcomponentreference-object--guid-property)) is present, `theComponent` **SHALL** be `theTool.driver` ([sec](#driver-property)). (line 10)
- If `index` is present, `theComponent` **SHALL** be the object at array index `index` within `theTool.extensions` ([sec](#extensions-property)). (line 12)
- If `index` is absent and `guid` is present, `theComponent` **SHALL** be either `theTool.driver` or an element of `theTool.extensions`, whichever one has a matching `guid` property. (line 14)

## `name` Property

`file-format-54-toolcomponentreference-object.md`

- A `toolComponentReference` object **MAY** contain a property named `name` whose value is a string equal to `theComponent.name` ([sec](#toolcomponent-object--name-property)). (line 18)

## `index` Property

`file-format-54-toolcomponentreference-object.md`

- If `theComponent` is an element of `theTool.extensions` ([sec](#extensions-property)), a `toolComponentReference` object **MAY** contain a property named `index` whose value is the array index ([sec](#array-indices)) of that element. (line 24)

## `guid` Property

`file-format-54-toolcomponentreference-object.md`

- A `toolComponentReference` object **MAY** contain a property named `guid` whose value is a GUID-valued string ([sec](#guid-valued-strings)) equal to `theComponent.guid` ([sec](#toolcomponent-object--guid-property)). (line 27)

## `description` Property

`file-format-55-fix-object.md`

- A `fix` object **SHOULD** contain a property named `description` whose value is a `message` object ([sec](#message-object)) that describes the proposed fix. (line 30)

## `artifactChanges` Property

`file-format-55-fix-object.md`

- A `fix` object **SHALL** contain a property named `artifactChanges` whose value is an array of one or more unique ([sec](#array-properties-with-unique-values)) `artifactChange` objects ([sec](#artifactchange-object)) each of which describes the changes to a single artifact that are necessary to effect the fix. (line 47)
- The array elements **SHALL** refer to distinct artifacts. (line 51)

## `artifactLocation` Property

`file-format-56-artifactchange-object.md`

- An `artifactChange` object **SHALL** contain a property named `artifactLocation` whose value is an `artifactLocation` object ([sec](#artifactlocation-object)) that represents the location of the artifact. (line 32)

## `replacements` Property

`file-format-56-artifactchange-object.md`

- An `artifactChange` object **SHALL** contain a property named `replacements` whose value is an array of one or more `replacement` objects ([sec](#replacement-object)) each of which represents the replacement of a single region of the artifact specified by the `artifactLocation` property ([sec](#artifactchange-object--artifactlocation-property)). (line 35)

## General

`file-format-57-replacement-object.md`

- If a replacement object specifies both the removal of a region by means of the `deletedRegion` property ([sec](#deletedregion-property)) and the insertion of new content by means of the `insertedContent` property ([sec](#insertedcontent-property)), then the effect of the replacement **SHALL** be as if the removal were performed before the insertion. (line 8)
- If a single `artifactChange` object ([sec](#artifactchange-object)) specifies more than one replacement, then the effect of the replacements **SHALL** be as if they were performed in the order they appear in the `replacements` array ([sec](#replacements-property)). (line 10)
- The `deletedRegion` property of each `replacement` object **SHALL** specify the location of the replacement in the unmodified artifact. (line 10)

## Constraints

`file-format-57-replacement-object.md`

- If the `deletedRegion` property ([sec](#deletedregion-property)) specifies a text region ([sec](#text-regions)) and the `insertedContent` property ([sec](#insertedcontent-property)) is present, then the `insertedContent` property **SHOULD** contain a `text` property ([sec](#artifactcontent-object--text-property)). (line 72)
- If the `deletedRegion` property specifies a binary region ([sec](#binary-regions)) and the `insertedContent` property is present, then the `insertedContent` property **SHALL** contain a `binary` property ([sec](#binary-property)). (line 74)
- Although it is possible to construct a `replacement` object that neither removes nor adds any content, a `replacement` object **SHOULD** have a material effect on the target artifact, either because `deletedRegion` denotes a non-empty region to delete, or because `insertedContent` specifies non-empty content to insert, or both. (line 76)

## `deletedRegion` Property

`file-format-57-replacement-object.md`

- A `replacement` object **SHALL** contain a property named `deletedRegion` whose value is a `region` object ([sec](#region-object)) specifying the region to delete. (line 80)

## `insertedContent` Property

`file-format-57-replacement-object.md`

- A `replacement` object **MAY** contain a property named `insertedContent` whose value is an `artifactContent` object ([sec](#artifactcontent-object)) that specifies the content to insert in place of the region specified by the `deletedRegion` property (or at the point specified by `deletedRegion`, if `deletedRegion` has a length of zero and therefore specifies an insertion point). (line 86)
- If the inserted content is specified as text, the text **SHALL** be transcoded from UTF-8 (the encoding of all text in all SARIF log files) to the encoding of the target artifact before being inserted. (line 88)

## `descriptor` Property

`file-format-58-notification-object.md`

- A `notification` object **SHOULD** contain a property named `descriptor` whose value is a `reportingDescriptorReference` object ([sec](#reportingdescriptorreference-object)) that identifies this notification. (line 13)
- If the `reportingDescriptor` object ([sec](#reportingdescriptor-object)) `theDescriptor` to which `descriptor` refers exists (that is, if `theTool` contains a `reportingDescriptor` object that describes this notification), then `descriptor` **SHOULD** refer to `theDescriptor`. (line 17)

## `associatedRule` Property

`file-format-58-notification-object.md`

- If the condition described by the `notification` object is relevant to a particular analysis rule, the `notification` object **SHOULD** contain a property named `associatedRule` whose value is a `reportingDescriptorReference` object ([sec](#reportingdescriptorreference-object)) that identifies the rule. (line 26)

## `locations` Property

`file-format-58-notification-object.md`

- If the condition described by the `notification` object is relevant to one or more locations, the `notification` object **MAY** contain a property named `locations` whose value is an array of zero or more unique ([sec](#array-properties-with-unique-values)) `location` objects ([sec](#location-object)) that identify those locations to which the condition described by the notification applies. (line 75)

## `message` Property

`file-format-58-notification-object.md`

- A `notification` object **SHALL** contain a property named `message` whose value is a `message` object ([sec](#message-object)) that describes the condition that was encountered. (line 82)

## `level` Property

`file-format-58-notification-object.md`

- A `notification` object **MAY** contain a property named `level` whose value is one of a fixed set of strings that specify the severity level of the notification. (line 87)
- If present, the `level` property **SHALL** have one of the following values, with the specified meanings: (line 89)
- If `level` is absent, it **SHALL** default to the value determined by the procedure defined for `result.level` ([sec](#result-object--level-property)), except throughout the procedure, replace `ruleConfigurationOverrides` with `notificationConfigurationOverrides`. (line 103)

## `threadId` Property

`file-format-58-notification-object.md`

- A `notification` object **MAY** contain a property named `threadId` whose value is an integer which identifies the thread associated with this notification. (line 114)

## `exception` Property

`file-format-58-notification-object.md`

- If the notification is a result of a runtime exception, the `notification` object **MAY** contain a property named `exception` whose value is an `exception` object ([sec](#exception-object)). (line 124)
- If the notification is not the result of a runtime exception, the `exception` property **SHALL** be absent. (line 126)

## `relatedLocations` Property

`file-format-58-notification-object.md`

- A `notification` object **MAY** contain a property named `relatedLocations` whose value is an array of zero or more unique ([sec](#array-properties-with-unique-values)) `location` objects ([sec](#location-object)) that identify those locations relevant to understanding the `notification`. (line 132)
- The `relatedLocations` property **SHOULD** allow `notification` objects to distinguish between the following types of locations: (line 134)
- - Locations to which the condition described by the `notification` object **SHALL** apply. - Other locations to which the condition described by the `notification` object **SHALL NOT** apply but are relevant to understanding the result. (line 137)

## `kind` Property

`file-format-59-exception-object.md`

- An `exception` object **SHOULD** contain a property named `kind` whose value is a string describing the exception. (line 10)
- If the exception represents a thrown object, `kind` **SHALL** be the fully qualified type name of the object that was thrown, if that information is available. (line 12)
- If the exception represents a POSIX signal, `kind` **SHALL** be the symbolic name of the signal as specified in `<signal.h>`. (line 16)

## `message` Property

`file-format-59-exception-object.md`

- An `exception` object **SHOULD** contain a property named `message` whose value is a string that describes the exception. (line 24)

## `stack` Property

`file-format-59-exception-object.md`

- An `exception` object **MAY** contain a property named `stack` whose value is a `stack` object ([sec](#stack-object)) that describes the sequence of function calls leading to the exception. (line 34)

## `innerExceptions` Property

`file-format-59-exception-object.md`

- An `exception` object **MAY** contain a property named `innerExceptions` whose value is an array of zero or more `exception` objects each of which is considered a cause of the containing exception. (line 38)

## General

`external-property-file-format.md`

- An external property file **SHALL** contain one or more externalized properties. (line 8)

## External Property File Naming Convention

`external-property-file-format.md`

- The file name of an external property file **SHOULD** end with the extension `".sarif-external-properties"`. (line 12)
- The file name **MAY** end with the additional extension `".json"`. (line 16)

## General

`external-property-file-format.md`

- The top-level element of an external property file **SHALL** be an object which we refer to as an `externalProperties` object. (line 24)

## `$schema` Property

`external-property-file-format.md`

- An `externalProperties` object **MAY** contain a property named `$schema` whose value is a string containing an absolute URI from which a JSON schema document describing the version of the external property file format to which this external property file conforms can be obtained. (line 64)
- If the `$schema` property is present, the JSON schema obtained from the specified URI **SHALL** describe the version of the external property file format corresponding to the SARIF version specified by the `version` property ([sec](#externalproperties-object--version-property)). (line 66)

## `version` Property

`external-property-file-format.md`

- Depending on the circumstances, an `externalProperties` object either **SHALL** or **MAY** contain a property named `version` whose value is a string designating the version of the SARIF specification to which this external property file conforms. (line 74)
- If present, this string **SHALL** have the value `"2.2"`. (line 74)
- If this `externalProperties` object is the root element of an external property file (see [sec](#rationale)), then `version` **SHALL** be present. (line 76)
- Otherwise (that is, if this `externalProperties` object is an element of `theSarifLog.inlineExternalProperties` ([sec](#inlineexternalproperties-property))), then `version` **MAY** be present. (line 78)
- If absent, it **SHALL** default to the value of `theSarifLog.version` ([sec](#sariflog-object--version-property)). (line 78)
- Although the order in which properties appear in a JSON object value is not semantically significant, the `version` property **SHOULD** appear first. (line 80)

## `guid` Property

`external-property-file-format.md`

- An `externalProperties` object **SHOULD** contain a property named `guid` whose value is a GUID-valued string ([sec](#guid-valued-strings)) that equals the `guid` property ([sec](#externalpropertyfilereference-object--guid-property)) of the corresponding `externalPropertyFileReference` object ([sec](#externalpropertyfilereference-object)) in the `run.externalPropertyFiles` property ([sec](#externalpropertyfilereferences-property)) in the root file. (line 86)

## `runGuid` Property

`external-property-file-format.md`

- If the externalized properties contained in this `externalProperties` object are associated with a single `run` object ([sec](#run-object)) `theRun`, and if `theRun` contains an `automationDetails.guid` property ([sec](#automationdetails-property), [sec](#runautomationdetails-object--guid-property)), the `externalProperties` object **MAY** contain a property named `runGuid` whose value is a GUID-valued string ([sec](#guid-valued-strings)) that equals `theRun.automationDetails.guid`. (line 90)
- Otherwise (that is, if this `externalProperties` object is associated with more than one `run` object, or if `theRun` does not define `automationDetails.guid`), then `runGuid` **SHALL** be absent. (line 90)

## The Property Value Properties

`external-property-file-format.md`

- An `externalProperties` object **SHALL** contain zero or more externalized properties. (line 94)

## Minimal Valid SARIF Log File

`examples.md`

- It contains only those elements required by this document (elements which the document states **SHALL** be present). (line 8)

## Minimal Recommended SARIF Log File with Source Information

`examples.md`

- The file contains those elements recommended by this document (elements which the document states "**SHOULD**" be present), in addition to the required elements. (line 33)
- It does not contain a `run.logicalLocations` property ([sec](#run-object--logicallocations-property)), because when physical location information is available, that property is optional (it "**MAY**" be present). (line 39)

## Minimal Recommended SARIF Log File without Source Information

`examples.md`

- The file contains those elements recommended by this document (elements which the document states "**SHOULD**" be present), in addition to the required elements. (line 116)
