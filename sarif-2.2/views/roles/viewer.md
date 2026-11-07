# Statements naming: SARIF viewer

Derived by `bin/vision.py derive` from the prose and `records/roles.yaml`; do not edit.
16 statements; SHALL 1, SHALL NOT 1, SHOULD 3, MAY 11.


## `defaultSourceLanguage` Property

`file-format-14-run-object.md`

- In that case, a SARIF viewer **MAY** use any method or heuristic to determine the source language of each file, for example by examining the file’s file name extension or MIME type, or by prompting the user. (line 373)

## `toolExecutionNotifications` Property

`file-format-20-invocation-object.md`

- However, viewers **MAY** still present tool notifications to users, so users are aware of any tool problems. (line 231)
- At a minimum, viewers **SHOULD** make users aware of tool notifications whose `level` property is `"error"`. (line 231)

## `toolConfigurationNotifications` Property

`file-format-20-invocation-object.md`

- However, viewers **MAY** still present configuration notifications to users, so users are aware of any configuration problems. (line 243)
- At a minimum, viewers **SHOULD** make users aware of configuration notifications whose `level` property is `"error"`. (line 243)

## General

`file-format-24-artifact-object.md`

- In that case, a SARIF viewer **MAY** use any method or heuristic to determine the artifact’s source language, for example, by examining its file name extension or MIME type, or by prompting the user. (line 207)

## `ruleId` Property

`file-format-27-result-object.md`

- A SARIF viewer or result management system **MAY** use the additional hierarchical components to allow a user to suppress a subset of the violations of a given rule. (line 46)

## Text Regions

`file-format-30-region-object.md`

- A SARIF viewer **MAY** choose to present column numbers that match the visual offset of each character from the beginning of the line. (line 41)

## `message` Property

`file-format-30-region-object.md`

- A SARIF viewer **MAY** display this message when the user interacts with the region. (line 261)

## `sourceLanguage` Property

`file-format-30-region-object.md`

- In that case, a SARIF viewer **MAY** use any method or heuristic to determine the region’s source language, for example, by examining the file’s file name extension or MIME type, or by prompting the user. (line 271)

## General

`file-format-31-rectangle-object.md`

- When a SARIF viewer displays an image, it **MAY** indicate the presence of these areas, for example, by highlighting them or surrounding them with a border. (line 6)

## `message` Property

`file-format-31-rectangle-object.md`

- A SARIF viewer **MAY** display this message when the user interacts with the area. (line 17)

## `state` Property

`file-format-38-threadflowlocation-object.md`

- A SARIF viewer **SHALL NOT** assume that expressions mentioned in previous steps but not mentioned in the current step are still present with unchanged values. (line 342)

## `nestingLevel` Property

`file-format-38-threadflowlocation-object.md`

- A viewer that renders a `threadFlow` **SHOULD** provide a visual representation of the value of `nestingLevel`. (line 393)

## `finalState` Property

`file-format-43-edgetraversal-object.md`

- A SARIF viewer **SHALL** display only those properties that are explicitly present in the `finalState` property of the current `edgeTraversal`. (line 22)

## `stepOverEdgeCount` Property

`file-format-43-edgetraversal-object.md`

- If this property is present, a SARIF viewer **MAY** provide a visual cue informing the user that they have the option of either stepping over the current edge and into the nested graph, or of stepping over the entire traversal of the nested graph. (line 32)
