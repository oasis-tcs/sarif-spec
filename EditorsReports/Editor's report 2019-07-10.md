# Editor's report

Laurence J. Golding and Michael Fanning

Presented at TC Meeting #36, July 10th, 2019

This report describes the changes that were made in response to comments on SARIF v2.1.0 CSD.1.
All the comments were from the TC; there were no public comments.
All the changes are bug fixes which we are making at editorial discretion. In the opinion of the Editors, there are no substantive changes.
We will discuss whether [Issue #429](https://github.com/oasis-tcs/sarif-spec/issues/429) is a substantive change or whether it is (as the Editors believe)
a clarification of an obvious point.

Changes to the schema:

- [Issue #420](https://github.com/oasis-tcs/sarif-spec/issues/420): Missing "additionalProperties": false in schema, and missing object descriptions.
- [Issue #421](https://github.com/oasis-tcs/sarif-spec/issues/421): uri-reference format not supported in draft-04

Changes to the spec text:

- [Issue #422](https://github.com/oasis-tcs/sarif-spec/issues/422): Ensure all GUIDs in format examples are invalid.
- [Issue #423](https://github.com/oasis-tcs/sarif-spec/issues/423): Ballot comments from Yekaterina: typo and alphabetized roles
- [Issue #425](https://github.com/oasis-tcs/sarif-spec/issues/425): Fix mistake in originalUriBaseIds example
- [Issue #426](https://github.com/oasis-tcs/sarif-spec/issues/426): Fix broken links
- [Issue #427](https://github.com/oasis-tcs/sarif-spec/issues/427): §3.27.7: Fix obsolete mentions of "ruleDescriptorReference"
- [Issue #429](https://github.com/oasis-tcs/sarif-spec/issues/429): Add missing constraint: result.ruleId == result.rule.id
