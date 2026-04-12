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
