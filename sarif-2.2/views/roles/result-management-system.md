# Statements binding: Result management system (conformance clause 8)

Derived by `bin/vision.py derive` from `records/statements.yaml` and `records/roles.yaml`; do not edit.
22 statements of its own; SHALL 2, SHOULD 7, SHOULD NOT 2, MAY 12.
Its profile includes [consumer](consumer.md): 70 statements in all.


## `id` Property

`file-format-17-runautomationdetails-object.md`

- A result management system or other components of the engineering system **MAY** use `run.automationDetails.id` to associate the information in the log with additional information not provided by the analysis tool that produced it. (line 50)

## `guid` Property

`file-format-17-runautomationdetails-object.md`

- A result management system or other components of the engineering system **MAY** use `run.automationDetails.guid` to associate the information in the log with additional information not provided by the analysis tool that produced it. (line 70)

## Distinguishing logically identical from logically distinct results

`file-format-27-result-object.md`

- Result management systems that compute fingerprints **SHOULD** populate the `fingerprints` property ([sec](#fingerprints-property)). (line 22)
- Result management systems that group results into equivalence classes based on an arbitrary unique identifier **SHOULD** populate the `correlationGuid` property ([sec](#result-object--correlationguid-property)), regardless of whether they also compute a fingerprint. (line 22)

## `guid` Property

`file-format-27-result-object.md`

- A result management system **SHOULD** set this property when it ingests a SARIF log file. (line 28)
- If it does so, then later, when a SARIF consumer retrieves results in SARIF format from the result management system, the result management system **SHALL** set this property to the value it assigned. (line 28)
- A result management system **MAY** store multiple results with identical fingerprints (see [sec](#fingerprints-property) and [sec](#use-of-fingerprints-by-result-management-systems)), but the `guid` properties for those results **SHALL** be distinct. (line 30)

## `correlationGuid` Property

`file-format-27-result-object.md`

- A result management system **MAY** set this property when it ingests a SARIF log file. (line 36)
- If it does so, then later, when a SARIF consumer retrieves results in SARIF format from the result management system, the result management system **MAY** set this property to the value it assigned. (line 36)

## `ruleId` Property

`file-format-27-result-object.md`

- A SARIF viewer or result management system **MAY** use the additional hierarchical components to allow a user to suppress a subset of the violations of a given rule. (line 46)
- A result management system **MAY** also use the additional components to more precisely match results between runs. (line 46)

## `fingerprints` Property

`file-format-27-result-object.md`

- A result management system **MAY** use the property names to identify the method used to calculate the fingerprint. (line 520)
- When a result management system uses fingerprint information to determine whether two results are logically identical, it **SHOULD** use the latest version of the fingerprint available in both results. (line 532)
- A result management system **MAY** populate this property when it ingests a SARIF file. (line 561)
- If it does so, then later, when a SARIF consumer retrieves results in SARIF format from the result management system, the result management system **MAY** set this property to the value it assigned. (line 561)

## `partialFingerprints` Property

`file-format-27-result-object.md`

- When a result management system uses partial fingerprint information to determine whether two results are logically identical, it **SHOULD** use the latest version of the partial fingerprint available in both results. (line 585)
- A result management system **MAY** use any algorithm to combine the information contained in the various partial fingerprints. (line 608)
- A result management system with that knowledge **MAY** use the property names to decide which partial fingerprints to include in its fingerprint computation. (line 610)
- A result management system lacking that knowledge **SHOULD NOT** attempt to interpret the information embodied in the partial fingerprint names. (line 610)

## Annex C Use of Fingerprints by Result Management Systems

`fingerprints.md`

- A result management system **SHOULD** construct a fingerprint by using information contained in the SARIF file such as (line 10)
- A result management system **SHOULD** include the information in `partialFingerprints` in its fingerprint computation. (line 20)
- A result management system **SHOULD NOT** include an absolute line number (or an absolute byte location in a binary artifact) in its fingerprint computation. (line 26)
