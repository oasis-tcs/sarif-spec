# Introduction

Software developers use a variety of analysis tools to assess the quality of their programs. These tools report results which can indicate problems related to program qualities such as correctness, security, performance, compliance with contractual or legal requirements, compliance with stylistic standards, understandability, and maintainability. To form an overall picture of program quality, developers often need to aggregate the results produced by all of these tools. This aggregation is more difficult if each tool produces output in a different format.

This document defines a standard format for the output of static analysis tools, called the Static Analysis Results Interchange Format, or "SARIF"[^1]. The goals of the format are:

- Comprehensively capture the range of data produced by commonly used static analysis tools.

- Be a useful format for analysis tools to emit directly, and also an effective interchange format into which the output of any analysis tool can be converted.

- Be suitable for use in a variety of scenarios related to analysis result management and be extensible for use in new scenarios.

- Reduce the cost and complexity of aggregating the results of various analysis tools into common workflows.

- Capture information that is useful for assessing a project’s compliance with corporate policy or certification standards.

- Adopt a widely used serialization format that can be parsed by readily available tools.

- Represent analysis results for all kinds of artifacts, including source code and object code.

Although most static analysis tools analyze files on disk, SARIF can represent results detected in any URI-addressable artifact (for example, the text returned by an HTTP query). This specification uses the term "artifact" to refer to any item that a tool might analyze. It uses the more restrictive term "file" when referring specifically to a file on disk.

## Trademarks

CWE™ is the trademark of a product supplied by The MITRE Corporation.

JavaScript™ is the trademark of Oracle America, Inc.

Linux® is the registered trademark of a product supplied by The Linux Foundation.

Visual Basic™ is the trademark of a product supplied by Microsoft Corporation.

UNIX® is the registered trademark of a product supplied by The Open Group.

Windows® is the registered trademark of a product supplied by Microsoft Corporation.

This information is given for the convenience of users of this document and does not constitute an endorsement by OASIS of any of the products named. Equivalent products may be used if they can be shown to lead to the same results.

## Changes From the Previous Version

### File Format Extensions

* 2.5 (now 3.2.4): added `"theLocationOwner"` to generalize location-handling between `result` and `notification` objects (#540) (#736)

* 3.9 (now 5.9): added examples of expiry dates (#492) (#644)
* 3.12 (now 5.12) `multiformatMessage` object: `"text"` property can now contain embedded links (#471) (#636)
* 3.13 (now 5.13) `sarifLog` object: added `"guid"` property (#483) (#641)
* 3.14 (now 5.14) `run` object: added `"bytes"` as a value for the `columnKind` property (#466) (#740)
* 3.23 (now 5.23) `artefact` object: added `"scannedFile"` as a value for the `role` property (#459) (#642)
* 3.35 (now 5.35) `suppression` object: added `"justificationType"` property (#574) (#672)

* 3.38 (now 5.38) `threadflowlocation` object: added new values to `"kinds`":
  * `"catch"` for catching an exception (#735) (#756)
  * `"expose"`: for exposure of a secret across a trust boundary (e.g. password written to a logfile or an uninitialized stack copied from kernel back to user space) (#530) (#671)
  * `"longjmp"` for calls to `longjmp` that rewind the program counter/stack to the location of a previous `setjmp` call (#735) (#756)
  * `"sensitive"`: for a value that is known to be secret e.g. a password or a private key (#530) (#671)
  * `"setjmp"` for calls to `setjmp` (#735) (#756)
  * `"throw"` for throwing an exception (#735) (#756)</mark>
  * `"uninitialized"`: for uninitialized memory (#530) (#671)
  * `"unwind"` for unwinding stack frame(s) during exception-handling (#735) (#756)

* 3.58 (now 5.58) `notification` object: added `"relatedLocations"` property (#491) (#643)

* Appendix J (now Appendix 9): **Sample `"sourceLanguage"` Values**: added:
  * `"algol68"` (#751) (#754)
  * `"assembler"` (#608) (#748)
  * `"sarif"` (#654) (#690)
  * `"systemverilog"` (#687) (#688)
  * `"zig"` (#746) (#749)

* Section 7: **Safety, Security and Data Protection**: new section (#732) (#738)

### Other changes

* The SARIF specification is now maintained as a collection of Markdown files, rather than a Word document (#599) (#633)
* Fixed the JSON Example for logicalLocation/kind (#670) (#673)
* Fixed the Comprehensible Example (#719) (#742)
* Fix typo in XML example of logical locations (#669) (#675)
* Fixed errors in the algorithm for calculating `result.level` (#470) (#758)

---
