# Statements binding: SARIF consumer (conformance clause 6)

Derived by `bin/vision.py derive` from `records/statements.yaml` and `records/roles.yaml`; do not edit.
48 statements of its own; SHALL 29, SHALL NOT 7, SHOULD 4, SHOULD NOT 3, MAY 7.


## `uriBaseId` Property

`file-format-04-artifactlocation-object.md`

- A SARIF consumer **SHALL** use the following procedure to resolve a `uriBaseId` to an absolute URI: (line 46)
- If the end user has configured the SARIF consumer with a value for the `uriBaseId` (for example, on the consumer’s command line or through a user interface prompt), then the consumer **SHALL** use the configured value. (line 48)
- If `uriBaseId` is not yet resolved and `theRun.originalUriBaseIds` ([sec](#originaluribaseids-property)) is present, the consumer **SHALL** attempt to resolve the `uriBaseId` from the information in `originalUriBaseIds`, in the manner specified in [sec](#originaluribaseids-property). (line 54)
- If `uriBaseId` is not yet resolved, the consumer **MAY** use other information or heuristics to locate the artifact. (line 56)

## General

`file-format-05-string-properties.md`

- A SARIF consumer **SHALL** interpret the values of a hierarchical string as forming a logical hierarchy. (line 70)
- In string-valued properties and property names that are *not* described as hierarchical, the forward slash character has no special meaning, and a SARIF consumer **SHALL NOT** interpret it as dividing the value into hierarchical components. (line 78)

## Versioned Hierarchical Strings

`file-format-05-string-properties.md`

- then a SARIF consumer **SHALL** consider that component to represent the version number of the entity specified by the string. (line 88)
- In string-valued properties and property names that are described as hierarchical but *not* as versioned, a final `component` matching the syntax of `version component` has no special meaning, and a SARIF consumer **SHALL NOT** interpret it as a version number. (line 94)

## Security Implications

`file-format-11-message-object.md`

- For security reasons, SARIF producers and consumers **SHALL** adhere to the following: (line 48)
- To reduce this risk, SARIF consumers **SHALL** use a Markdown processor that is hardened against such attacks. (line 52)
- - To reduce the risk posed by possibly malicious SARIF files that do contain arbitrary HTML (including, for example, `javascript:` links), SARIF consumers **SHALL** either disable HTML processing (for example, by using an option such as the `--safe` option in the cmark Markdown processor) or run the resulting HTML through an HTML sanitizer. (line 56)
- SARIF consumers that are not prepared to deal with the security implications of formatted messages **SHALL NOT** attempt to render them and **SHALL** instead fall back to the corresponding plain text messages. (line 58)

## Messages with Placeholders

`file-format-11-message-object.md`

- When a SARIF consumer displays the message, it **SHALL** replace every occurrence of the placeholder `{n}` with the string value at index `n` in the `arguments` array. (line 70)

## Message String Lookup

`file-format-11-message-object.md`

- When a SARIF consumer needs to locate a message string from a `message` object, it **SHALL** follow the procedure specified in this section. (line 224)
- The lookup **SHALL** occur entirely within the context of a single `toolComponent` object ([sec](#toolcomponent-object)) which we refer to as `theComponent`. (line 226)
- At various points in this procedure, we state that the consumer uses an object’s "`text` property or `markdown` property, as appropriate." This means that if the consumer can render formatted messages, it **MAY** use the `markdown` property, if present; otherwise it **SHALL** use the `text` property, but if the consumer cannot render formatted messages, it **SHALL** use the `text` property. (line 230)

## `markdown` Property

`file-format-11-message-object.md`

- SARIF consumers that cannot (or choose not to) render formatted text **SHALL** ignore the `markdown` property and use the `text` property instead. (line 284)

## `markdown` Property

`file-format-12-multiformatmessagestring-object.md`

- SARIF consumers that cannot (or choose not to) render formatted text **SHALL** ignore the `markdown` property and use the `text` property ([sec](#multiformatmessagestring-object--text-property)) instead. (line 21)

## `originalUriBaseIds` Property

`file-format-14-run-object.md`

- A SARIF consumer **SHALL** use the following procedure to resolve a URI base id from the information in `originalUriBaseIds`: (line 188)

## `columnKind` Property

`file-format-14-run-object.md`

- If a SARIF consumer uses a column measurement unit other than that specified by `columnKind`, and if the consumer is required to interact with the artifact’s contents (for example, by displaying the artifact in an editor and highlighting a region), the consumer **SHALL** recompute column numbers in its (the consumer’s) native measurement unit. (line 412)

## Rationale

`file-format-15-externalpropertyfilereferences-object.md`

- A SARIF consumer **SHALL** treat the value of an object-valued property stored in an external property file exactly as if it had appeared inline in the root file as the value of the corresponding property. (line 20)
- A SARIF consumer **SHALL** treat the value of an array-valued property stored in an external property file exactly as if its elements had appeared inline in the root file, appended to the existing value, if any, of that property. (line 22)

## `location` Property

`file-format-16-externalpropertyfilereference-object.md`

- If `location` is absent, then a SARIF consumer that needs to locate the externalized properties **SHALL** do so using the `guid` property ([sec](#externalpropertyfilereference-object--guid-property)). (line 20)

## Policies

`file-format-19-toolcomponent-object.md`

- A SARIF consumer **MAY** offer the user the option of treating results according to the associated component’s default rule configuration (possibly modified by command line options stored in `theInvocation.ruleConfigurationOverrides` ([sec](#ruleconfigurationoverrides-property)), by configuration files, by environment variables, or by any other means), or according to the configuration defined by a selected element of `run.policies`. (line 226)
- If the user selects a policy, then for any result that violates a rule covered by that policy, the SARIF consumer **SHALL** treat the result according to the policy, regardless of the associated component’s default configuration, regardless of any configuration overrides, and regardless of whether the `result` object ([sec](#result-object)) itself specifies a configuration property such as `level` ([sec](#result-object--level-property)). (line 226)

## `minimumRequiredLocalizedDataSemanticVersion` Property

`file-format-19-toolcomponent-object.md`

- When a SARIF consumer is seeking a translation for this object, it **SHALL** only accept one whose `localizedDataSemanticVersion` ([sec](#localizeddatasemanticversion-property)) is greater than or equal to (in the SEMVER sense) but has the same major version component as `thisObject.minimumRequiredLocalizedDataSemanticVersion`. (line 639)

## `commandLine` Property

`file-format-20-invocation-object.md`

- For this reason, a SARIF consumer that receives a SARIF log file from an untrusted source **SHOULD NOT** execute the command line without first examining it carefully. (line 28)
- In particular, an automated SARIF consumer **SHALL NOT** execute a command line in a SARIF log file from an untrusted source. (line 28)

## `toolExecutionNotifications` Property

`file-format-20-invocation-object.md`

- A SARIF consumer **SHALL NOT** assume that a failed run contains a complete set of analysis results. (line 227)

## Source language identifier conventions and practices

`file-format-24-artifact-object.md`

- To maximize interoperability, SARIF producers and consumers **SHOULD** conform to the following conventions and practices with respect to the value of this property: (line 211)

## `hashes` Property

`file-format-24-artifact-object.md`

- SARIF consumers that need to verify hash values **SHOULD** be able to compute any hash function whose name appears in the IANA registry. (line 248)
- SARIF consumers that need to verify hash values **SHALL** be able to compute a SHA-256 hash. (line 250)
- A SARIF consumer **MAY** implement any hash function, but it does not have to implement any hash function that does not appear in the IANA registry. (line 252)
- SARIF consumers **SHALL** treat the property name as case insensitive (even when comparing to hash function names in the IANA registry). (line 256)

## `displayBase` Property

`file-format-25-speciallocations-object.md`

- A consumer **MAY** act on this hint as follows: (line 14)

## `ruleId` Property

`file-format-27-result-object.md`

- Therefore, a SARIF consumer **SHOULD NOT** attempt to compare or combine the output from different converters for the same analysis tool. (line 102)

## `suppressions` Property

`file-format-27-result-object.md`

- In this case, if the array is empty, a consumer **SHALL** treat the result as not suppressed. (line 729)
- If the array is non-empty, a consumer that needs to determine the result’s suppression state **SHALL** examine the `status` properties ([sec](#status-property)) of the `suppression` objects in the array. (line 729)
- A SARIF consumer **SHALL** treat such a result as not suppressed. (line 731)

## Text Regions

`file-format-30-region-object.md`

- A SARIF consumer **SHALL** consider an artifact to have the encoding specified by `artifact.encoding` ([sec](#encoding-property)), if present, or else by `theRun.defaultEncoding` ([sec](#defaultencoding-property)), if present. (line 45)
- If neither is present, the consumer **MAY** use any heuristic or procedure to determine the encoding, including (for example) prompting the user. (line 45)

## `justification` Property

`file-format-35-suppression-object.md`

- Therefore, SARIF consumers **SHOULD** exercise appropriate caution when displaying, sharing, or publishing this information. (line 64)

## `kinds` Property

`file-format-38-threadflowlocation-object.md`

- A SARIF consumer that wishes to act based on such values **SHOULD** examine `theTool` to determine if it (the consumer) knows how to interpret them. (line 265)
- A SARIF consumer that knows how to interpret `kinds` for this tool **MAY** use this additional information. (line 269)

## `deletedRegion` Property

`file-format-57-replacement-object.md`

- If the length of the region specified by `deletedRegion` is zero, then `deletedRegion` specifies an insertion point, and the SARIF consumer performing the replacement **SHALL NOT** remove any content. (line 82)

## `insertedContent` Property

`file-format-57-replacement-object.md`

- If `insertedContent` is absent or its properties specify content whose length is zero, the SARIF consumer performing the replacement **SHALL NOT** insert any content. (line 91)

## General

`external-property-file-format.md`

- A SARIF consumer **SHALL** treat the value of an externalized property exactly as if it had appeared inline in the root file as the value of the corresponding property. (line 8)

## Annex D Production of SARIF by Converters

`converters.md`

- Since each converter might synthesize SARIF elements differently (notably the rule id; see [sec](#ruleid-property)), a SARIF consumer **SHOULD NOT** attempt to combine results produced by different converters for the same tool. (line 16)
