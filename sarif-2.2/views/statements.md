# Statements and whom they bind (A3)

Derived by `bin/vision.py derive` from `records/statements.yaml` and `records/roles.yaml`; do not edit.

996 normative statements (a sentence with a bold BCP 14 keyword). The conformance section makes the SARIF log
file the target of every statement that designates no other; a target designated by a statement is named in it.

| Target | Clause | Own | SHALL | SHOULD | MAY | With what its profile includes |
|---|--:|--:|--:|--:|--:|--:|
| [SARIF log file](roles/log-file.md) | 1 | 851 | 452 | 115 | 333 | 851 |
| [SARIF producer](roles/producer.md) | 2 | 32 | 10 | 12 | 10 | 883 |
| [Direct producer](roles/direct-producer.md) | 3 | 12 | 4 | 6 | 2 | 895 |
| [Converter](roles/converter.md) | 4 | 15 | 3 | 7 | 5 | 898 |
| [SARIF post-processor](roles/post-processor.md) | 5 | 3 | 1 | 1 | 1 | 931 |
| [SARIF consumer](roles/consumer.md) | 6 | 48 | 36 | 7 | 7 | 48 |
| [Viewer](roles/viewer.md) | 7 | 17 | 3 | 3 | 11 | 65 |
| [Result management system](roles/result-management-system.md) | 8 | 22 | 2 | 9 | 12 | 70 |
| [Engineering system](roles/engineering-system.md) | 9 | 3 | 0 | 0 | 3 | 3 |

SHALL counts **SHALL** and **SHALL NOT** (likewise SHOULD); a statement with two keywords counts in both columns.
A statement binding two targets counts for each.

## Under review (1)

The seed could not tell whom these bind; their record carries `review`.

- `versionControlDetails.mappedTo`: The mapping algorithm **SHALL** be as follows, or any algorithm with the same result (a clarifying example follows): -- "The mapping algorithm" is a procedure, not part of the log file: whose is it?
