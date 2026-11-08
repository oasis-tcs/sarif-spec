# Statements binding: SARIF producer (conformance clause 2)

Derived by `bin/vision.py derive` from `records/statements.yaml` and `records/roles.yaml`; do not edit.
32 statements of its own; SHALL 8, SHALL NOT 2, SHOULD 10, SHOULD NOT 2, MAY 10.
Its profile includes [log-file](log-file.md): 883 statements in all.


## `text` Property

`file-format-03-artifactcontent-object.md`

- Since SARIF log files are encoded in UTF-8 ([cite](#RFC3629); see [sec](#file-format--general)), this means that if the external artifact is a text artifact in any encoding other than UTF-8, the SARIF producer **SHALL** transcode the text to UTF-8 before assigning it to the `text` property. (line 10)
- The SARIF producer **SHALL** escape any characters that JSON [cite](#RFC8259) requires to be escaped. (line 10)
- Notwithstanding any necessary transcoding and escaping, the SARIF producer **SHALL** preserve the text artifact’s line breaking convention (for example, `"\n"` or `"\r\n"`). (line 12)

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

## `responseFiles` Property

`file-format-20-invocation-object.md`

- A SARIF producer **MAY** embed the contents of a response file in the SARIF log file by mentioning the response file in `theRun.artifacts` ([sec](#artifacts-property)) and providing a value for `artifact.contents` ([sec](#artifact-object--contents-property)). (line 58)

## `stdin`, `stdout`, `stderr`, and `stdoutStderr` Properties

`file-format-20-invocation-object.md`

- A SARIF producer **MAY** embed the stream contents in the log file by mentioning the corresponding file in `theRun.artifacts` ([sec](#artifacts-property)) and providing a value for `artifact.contents` ([sec](#artifact-object--contents-property)). (line 302)

## General

`file-format-21-attachment-object.md`

- A SARIF producer **MAY** embed the contents of an attachment in the log file by mentioning the attachment in `theRun.artifacts` ([sec](#artifacts-property)) and providing a value for `artifact.contents` ([sec](#artifact-object--contents-property)). (line 8)

## Source language identifier conventions and practices

`file-format-24-artifact-object.md`

- To maximize interoperability, SARIF producers and consumers **SHOULD** conform to the following conventions and practices with respect to the value of this property: (line 211)

## `partialFingerprints` Property

`file-format-27-result-object.md`

- A SARIF producer **MAY** use the property name to identify the nature of the information used to compute the partial fingerprint. (line 573)
- Because result management systems might come to depend on the choice of property names, SARIF producers that use property names to identify the nature of the information used to compute the partial fingerprint **SHOULD** adhere to the following guidelines: (line 612)

## `kind` Property

`file-format-32-address-object.md`

- When possible, SARIF producers **SHOULD** use the following values, with the specified meanings. (line 159)
- A SARIF producer **SHOULD** use the term most appropriate for the target operating system. (line 183)
- &emsp;&emsp;If none of these values are appropriate, a SARIF producer **MAY** use any value. (line 187)

## `kinds` Property

`file-format-34-locationrelationship-object.md`

- When possible, SARIF producers **SHOULD** use the following values, with the specified meanings. (line 87)
- If none of these values are appropriate, a SARIF producer **MAY** use any value. (line 95)

## `kinds` Property

`file-format-38-threadflowlocation-object.md`

- When possible, SARIF producers **SHOULD** use the following values, with the specified meanings. (line 189)
- If none of these values are appropriate, a SARIF producer **MAY** use any value. (line 263)
- A SARIF producer **MAY** provide additional kind-dependent information by populating `threadFlowLocation.properties` with properties whose names and values depend on the kind. (line 269)

## `kinds` Property

`file-format-53-reportingdescriptorrelationship-object.md`

- When possible, SARIF producers **SHOULD** use the following values, with the specified meanings. (line 110)
- If none of these values are appropriate, a SARIF producer **MAY** use any value. (line 132)

## General

`file-format-57-replacement-object.md`

- When performing a replacement in a text artifact, the SARIF producer **SHOULD** specify a text replacement rather than a binary replacement. (line 68)
