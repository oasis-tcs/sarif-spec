# Statements naming: SARIF post-processor

Derived by `bin/vision.py derive` from the prose and `records/roles.yaml`; do not edit.
3 statements; SHALL 1, SHOULD NOT 1, MAY 1.


## Redactable Strings

`file-format-05-string-properties.md`

- If a SARIF producer or a SARIF post-processor chooses to redact sensitive information in a redactable property, it **SHALL** replace the sensitive information with a string whose value is an element of `theRun.redactionTokens` ([sec](#redactiontokens-property)). (line 15)

## Plain Text Messages

`file-format-11-message-object.md`

- A SARIF post-processor **MAY** normalize line breaks to any desired convention, including escaping or removing the line breaks so that the entire message renders on a single line. (line 26)
- A SARIF post-processor **SHOULD NOT** modify line break sequences (except perhaps to adapt them to a particular viewing environment). (line 36)
