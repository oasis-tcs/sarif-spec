# Conformance

## Conformance targets

This document defines requirements for the SARIF file format and for certain software components that interact with it. The entities ("conformance targets") for which this document defines requirements are:

- **SARIF log file**: A log file in the format defined by this document.

- **SARIF producer**: A program which emits output in the SARIF format.

- **Direct producer**: An analysis tool which acts as a SARIF producer.

- **Converter**: A SARIF producer that transforms the output of an analysis tool from its native output format into the SARIF format.

- **SARIF post-processor**: A SARIF producer that transforms an existing SARIF log file into a new SARIF log file, for example, by removing or redacting security-sensitive elements.

- **SARIF consumer**: A program that reads and interprets a SARIF log file.

- **Viewer**: A SARIF consumer that reads a SARIF log file, displays a list of the results it contains, and allows an end user to view each result in the context of the artifact in which it occurs.

- **Result management system**: a software system that consumes the log files produced by analysis tools, produces reports that enable engineering teams to assess the quality of their software artifacts at a point in time and to observe trends in the quality over time, and performs functions such as filing bugs and displaying information about individual results.

- **Engineering system**: a software development environment within which analysis tools execute. It might include a build system, a source control system, a [result management system](#def_result_management_system), a bug tracking system, a test execution system, and so on.

The normative content in this document defines requirements for SARIF log files, except for those normative requirements that are explicitly designated as defining the behavior of another conformance target.

## Conformance Clause 1: SARIF log file

A text file satisfies the "SARIF log file" conformance profile if:

- It conforms to the syntax and semantics defined in [§3](#file-format)

## Conformance Clause 2: SARIF producer

A program satisfies the "SARIF producer" conformance profile if:

- It produces output in the SARIF format, according to the semantics defined in [§3](#file-format)

- It satisfies those normative requirements in [§3](#file-format) that are designated as applying to SARIF producers.

## Conformance Clause 3: Direct producer

An analysis tool satisfies the "Direct producer" conformance profile if:

- It satisfies the "SARIF producer" conformance profile.

- It additionally satisfies those normative requirements in [§3](#file-format) that are designated as applying to "direct producers" or to "analysis tools".

- It does not emit any objects, properties, or values which, according to [§3](#file-format), are intended to be produced only by converters.

## Conformance Clause 4: Converter

A converter satisfies the "Converter" conformance profile if:

- It satisfies the "SARIF producer" conformance profile.

- It additionally satisfies those normative requirements in [§3](#file-format) that are designated as applying to converters.

- It does not emit any objects, properties, or values which, according to [§3](#file-format), are intended to be produced only by direct producers.

## Conformance Clause 5: SARIF post-processor

A SARIF post-processor satisfies the "SARIF post-processor" conformance profile if:

- It satisfies the "SARIF consumer" conformance profile.

- It satisfies the "SARIF producer" conformance profile.

- It additionally satisfies those normative requirements in [§3](#file-format) that are designated as applying to post-processors.

## Conformance Clause 6: SARIF consumer

A consumer satisfies the "SARIF consumer" conformance profile if:

- It reads SARIF log files and interprets them according to the semantics defined in [§3](#file-format)

- It satisfies those normative requirements in [§3](#file-format) that are designated as applying to SARIF consumers.

## Conformance Clause 7: Viewer

A viewer satisfies the "viewer" conformance profile if:

- It satisfies the "SARIF consumer" conformance profile.

- It additionally satisfies the normative requirements in [§3](#file-format) that are designated as applying to viewers.

## Conformance Clause 8: Result management system

A result management system satisfies the "result management system" conformance profile if:

- It satisfies the "SARIF consumer" conformance profile.

- It additionally satisfies the normative requirements in [§3](#file-format) and [Appendix B](#normative-use-of-fingerprints-by-result-management-systems) ("Use of fingerprints by result management systems") that are designated as applying to result management systems.

## Conformance Clause 9: Engineering system

An engineering system satisfies the "engineering system" conformance profile if:

- It satisfies the normative requirements in [§3](#file-format) that are designated as applying to engineering systems.
