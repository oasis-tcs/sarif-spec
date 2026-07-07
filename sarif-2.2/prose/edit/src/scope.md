# Scope

This document defines a standard format for the output of static analysis tools.
The format is referred to as the "Static Analysis Results Interchange Format" and is abbreviated as SARIF.

Software developers use a variety of analysis tools to assess the quality of their programs.
These tools report results which can indicate problems related to program qualities such as correctness, security, performance, compliance with contractual or legal requirements,
compliance with stylistic standards, understandability, and maintainability.
To form an overall picture of program quality, developers often need to aggregate the results produced by all of these tools.
This aggregation is more difficult if each tool produces output in a different format.

Although most static analysis tools analyze files on disk, SARIF can represent results detected in any URI-addressable artifact (for example, the text returned by an HTTP query).
This specification uses the term "artifact" to refer to any item that a tool might analyze. It uses the more restrictive term "file" when referring specifically to a file on disk.

---
