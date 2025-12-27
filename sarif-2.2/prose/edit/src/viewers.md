<!--
---
toc:
  auto: false
  label: (Informative) Use of SARIF by log file viewers
  enumerate: Appendix C.
---
-->
# (Informative) Use of SARIF by Log File Viewers

It is frequently useful for an end user to view the results produced by an analysis tool in the context of the artifacts in which they occur. A log file viewer is a program that allows an end user to do this.

Typically, the user opens a log file in the viewer, which presents a list of the results in the log file. When the user selects a result from the list, the viewer displays the source code from the file specified in the result, and displays information about the result in the vicinity of the region where the result occurred. For example, the viewer might interleave result information between lines of source code.

There are various reasons why a viewer might need to know the type of information contained in a source file that it displays:

- If the viewer knows the programming language, it can provide services such as syntax highlighting.

- If the result occurs in a source file that is nested within (for example) a compressed container file, then the viewer needs to know the file type of the container so that it can extract the source file.

There are various ways that a viewer might obtain file type information. In the SARIF format, the `mimeType` ([sec](#mimetype-property)) and `sourceLanguage` ([sec](#artifact-object--sourcelanguage-property)) properties of the `artifact` object ([sec](#artifact-object)) provides this information. In the absence of these properties, a viewer can fall back to examining the filename extension, for example ".c".
