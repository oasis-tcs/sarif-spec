## General{#file-format--general}

SARIF defines an object model, the top level of which is the `sarifLog` object ([sec](#sariflog-object)),
which contains the results of one or more analysis runs.
The runs do not need to be produced by the same analysis tool.

A SARIF log file **SHALL** contain a serialization of the SARIF object model into the JSON format.

> NOTE 1: In the future, other serializations might be defined.

The top-level value in the log file, representing the `sarifLog` object,
**SHALL** conform to the JSON object grammar;
that is, it **SHALL** consist of a comma-separated sequence of name/value pairs,
enclosed in curly brackets, as specified by JSON [cite](#RFC8259).

The case of names (keys) of the name/value pairs is as defined in this specification.
Using identical letters but different case leads to different names as per JSON [cite](#RFC8259),
i.e. the identity of two keys is a case sensitive operation.

A SARIF log file **SHALL** be encoded in UTF-8 [cite](#RFC3629).

> NOTE 2: JSON [cite](#RFC8259) requires this encoding for any JSON text "exchanged between systems
> that are not part of a closed ecosystem."

Regardless of future added formats,
SARIF files **SHOULD NOT** contain case only variations of required properties.

> NOTE 3: SARIF files with properties name variations on e.g. runs like RUNS, Runs,
> or similar can confuse processors and human consumers alike.
