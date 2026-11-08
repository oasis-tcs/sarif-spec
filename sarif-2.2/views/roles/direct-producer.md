# Statements binding: Direct producer (conformance clause 3)

Derived by `bin/vision.py derive` from `records/statements.yaml` and `records/roles.yaml`; do not edit.
12 statements of its own; SHALL 2, SHALL NOT 2, SHOULD 3, SHOULD NOT 3, MAY 2.
Its profile includes [log-file](log-file.md), [producer](producer.md): 895 statements in all.


## Messages with Embedded Links

`file-format-11-message-object.md`

- If the `link destination` is an integer, and hence specifies a `location` object belonging to `theResult`, the tool **SHOULD** replace the integer with a string representation of the specified location. (line 200)

## `conversion` Property

`file-format-14-run-object.md`

- A direct producer **SHALL NOT** emit the `conversion` property. (line 93)

## `guid` Property

`file-format-27-result-object.md`

- Direct SARIF producers and SARIF converters **MAY** but do not need to set this property. (line 28)

## `correlationGuid` Property

`file-format-27-result-object.md`

- Direct SARIF producers and SARIF converters **SHOULD NOT** set this property. (line 36)

## `ruleId` Property

`file-format-27-result-object.md`

- Direct producers **SHALL** emit either or both of `ruleId` and `rule.id` ([sec](#rule-property), [sec](#reportingdescriptorreference-object--id-property)). (line 96)
- If `rule.id` is absent, `ruleId` **SHALL** be present. (line 96)
- If `rule.id` is present, `ruleId` **MAY** be present. (line 96)

## `fingerprints` Property

`file-format-27-result-object.md`

- A direct SARIF producer **SHOULD NOT** populate this property. (line 561)

## `location` Propertyy

`file-format-38-threadflowlocation-object.md`

- A SARIF direct producer which creates such code flows **SHOULD** populate `location.message`, even if no actual location information is available. (line 109)

## `level` Property

`file-format-58-notification-object.md`

- Analysis tools **SHOULD** treat notifications whose `level` property is `"error"` as failures and treat the entire run as having failed (for example, by settings the exit code to the value that the tool uses to indicate failure, typically a non-zero value). (line 106)
- Because a notification whose `level` property is `"error"` describes a failed run, an analysis tool **SHALL NOT** override the severity of such a notification. (line 109)

## Annex C Use of Fingerprints by Result Management Systems

`fingerprints.md`

- An analysis tool **SHOULD NOT** include in `partialFingerprints` information that a result management system could deduce from other information in the SARIF file, for example, file hashes. (line 22)
