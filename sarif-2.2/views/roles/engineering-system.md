# Statements naming: engineering system

Derived by `bin/vision.py derive` from the prose and `records/roles.yaml`; do not edit.
7 statements; SHALL 1, MAY 6.


## `results` Property

`file-format-14-run-object.md`

- If the tool failed to start, and if the engineering system responsible for running the tool synthesized a SARIF file to record the failure, then `results` **MAY** be present. (line 351)

## `description` Property

`file-format-17-runautomationdetails-object.md`

- A `runAutomationDetails` object **MAY** contain a property named `description` whose value is a `message` object ([sec](#message-object)) that describes the role played within the engineering system by `theRun`. (line 44)

## `id` Property

`file-format-17-runautomationdetails-object.md`

- A `runAutomationDetails` object **MAY** contain a property named `id` whose value is a hierarchical string ([sec](#hierarchical-strings)) that uniquely identifies `theRun` within the engineering system. (line 48)
- A result management system or other components of the engineering system **MAY** use `run.automationDetails.id` to associate the information in the log with additional information not provided by the analysis tool that produced it. (line 50)
- An engineering system **MAY** define any number of components and interpret them in any way desired. (line 52)

## `guid` Property

`file-format-17-runautomationdetails-object.md`

- A result management system or other components of the engineering system **MAY** use `run.automationDetails.guid` to associate the information in the log with additional information not provided by the analysis tool that produced it. (line 70)

## `executionSuccessful` Property

`file-format-20-invocation-object.md`

- An `invocation` object **SHALL** contain a property named `executionSuccessful` whose value is a Boolean that is `true` if the engineering system that started the process knows that the analysis tool succeeded, and `false` if the engineering system knows that the tool failed. (line 171)
