<span id="def_analysis_target" class="anchor"></span>**analysis target**
- [artifact](#def_artifact) which an [analysis tool](#def_static_analysis_tool) is instructed to analyze

<span id="def_artifact" class="anchor"></span>**artifact**
- sequence of bytes addressable *via* a URI
- Examples: A physical file in a file system such as a source file, an object file, a configuration file or a data file; a specific version of a file in a version control system; a database table accessed *via* an HTTP request; an arbitrary stream of bytes returned from an HTTP request.

<span id="def_baseline" class="anchor"></span>**baseline**
- set of [results](#def_result) produced by a single [run](#def_run) of a set of [analysis tools](#def_static_analysis_tool) on a set of [artifacts](#def_artifact)

    NOTE: A [result management system](#def_result_management_system) can compare the results of a subsequent [run](#def_run) to a baseline produced by a [baseline run](#def_baseline_run) to determine whether new results have been introduced.

<span id="def_baseline_run" class="anchor"></span>**baseline run**
- [run](#def_run) that produces a [baseline](#def_baseline) to which subsequent runs can be compared

<span id="def_binary_file" class="anchor"></span>**binary artifact**
- [artifact](#def_artifact) considered as a sequence of bytes

**binary region**
- [region](#def_region) representing a contiguous range of zero or more bytes in a [binary artifact](#def_binary_file)

**call stack**
- sequence of nested function calls

<span id="def_camelCase_name" class="anchor"></span>**camelCase name**
- name that begins with a lowercase letter, in which each subsequent word begins with an uppercase letter

    Example: `camelCase`, `version`, `fullName`.

**code flow**
- set of one or more [thread flows](#def_thread_flow) which together specify a pattern of code execution relevant to detecting a [result](#def_result)

<span id="def_column" class="anchor"></span>**column (number)**
- 1-based index of a character within a [line](#def_line)

<span id="def_configuration_file" class="anchor"></span>**configuration file**
- file, typically textual, that configures the execution of an [analysis tool](#def_static_analysis_tool) or [tool component](#def_tool_component)

<span id="def_converter" class="anchor"></span>**converter**
- [SARIF producer](#def_sarif_producer) that transforms the output of an [analysis tool](#def_static_analysis_tool) from its native output format into the SARIF format

**custom taxonomy**
- [taxonomy](#def_taxonomic_category) defined by and intended for use with a particular [analysis tool](#def_static_analysis_tool)

<span id="def_direct_producer" class="anchor"></span>**direct producer**
- [analysis tool](#def_static_analysis_tool) which acts as a [SARIF producer](#def_sarif_producer)

<span id="def_driver" class="anchor"></span>**driver**
- [tool component](#def_tool_component) containing an [analysis tool](#def_static_analysis_tool)’s or [converter](#def_converter)’s primary executable, which controls the tool’s or converter’s execution, and which in the case of an analysis tool typically defines a set of analysis [rules](#def_rule)

**embedded link**
- syntactic construct which enables a [message string](#def_message_string) to refer to a location within an [artifact](#def_artifact) mentioned in a [result](#def_result)

**engineering system**
- software development environment within which [analysis tools](#def_static_analysis_tool) execute
 
    NOTE: An engineering system might include a build system, a source control system, a [result management system](#def_result_management_system), a bug tracking system, a test execution system, and so on.

**empty array**
- array that contains no elements, and so has a length of 0

**empty object**
- object that contains no properties

**empty string**
- string that contains no characters, and so has a length of 0

<span id="def_end_user" class="anchor"></span>**(end) user**
- person who uses the information in a [log file](#def_log_file) to investigate, [triage](#def_triage), or resolve [results](#def_result)

<span id="def_extension" class="anchor"></span>**extension**
- [tool component](#def_tool_component) other than the [driver](#def_driver) (for example, a [plugin](#def_plugin), a [configuration file](#def_configuration_file), or a [taxonomy](#def_taxonomic_category))

<span id="def_external_property_file" class="anchor"></span>**external property file**
- file containing the values of one or more [externalized properties](#def_externalized_property)

**externalizable property**
- property that can be contained in an [external property file](#def_external_property_file)

<span id="def_externalized_property" class="anchor"></span>**externalized property**
- property stored outside of the [SARIF log file](#def_log_file) to which it logically belongs

**false positive**
- [result](#def_result) which an [end user](#def_end_user) decides does not actually represent a [problem](#def_problem)

**fingerprint**
- [stable value](#def_stable_value) that can be used by a [result management system](#def_result_management_system) to uniquely identify a [result](#def_result) over time, even if a relevant [artifact](#def_artifact) is modified

<span id="def_fully_qualified_logical_name" class="anchor"></span>**formatted message**
- [message string](#def_message_string) which contains formatting information such as Markdown formatting characters

**fully qualified logical name**
- string that fully identifies the programmatic construct specified by a [logical location](#def_logical_location), typically by means of a hierarchical identifier.

    Example: The fully qualified logical name of the C# method `f(void)` in class `C` in namespace `N` is `"N.C.f(void)"`. Its [logical name](#def_logical_name) is `"f(void)"`.

**hierarchical string**
- string in the format `<component>{/<component>}*`

<span id="def_line" class="anchor"></span>**line**
- contiguous sequence of characters, starting either at the beginning of an [artifact](#def_artifact) or immediately after a [newline sequence](#def_newline_sequence), and ending at and including the nearest subsequent newline sequence, if one is present, or else extending to the end of the artifact

**line (number)**
- 1-based index of a line within a file

    NOTE: Abbreviated to "line" when there is no danger of ambiguity with "[line](#def_line)" in the sense of a sequence of characters.

<span id="def_localizable" class="anchor"></span>**localizable**
- subject to being translated from one natural language to another

<span id="def_log_file" class="anchor"></span>**log file**
- output file produced by an [analysis tool](#def_static_analysis_tool), which enumerates the [results](#def_result) produced by the tool

<span id="def_log_file_viewer" class="anchor"></span>**(log file) viewer**
- [SARIF consumer](#def_sarif_consumer) that reads a [log file](#def_log_file), displays a list of the [results](#def_result) it contains, and allows an [end user](#def_end_user) to view each result in the context of the [artifact](#def_artifact) in which it occurs

<span id="def_logical_location" class="anchor"></span>**logical location**
- location specified by reference to a programmatic construct, without specifying the [artifact](#def_artifact) within which that construct occurs

    Example: A class name, a method name, a namespace.

<span id="def_logical_name" class="anchor"></span>**logical name**
- string that partially identifies the programmatic construct specified by a [logical location](#def_logical_location) by specifying the most specific (often the rightmost) component of its [fully qualified logical name](#def_fully_qualified_logical_name).

    Example: The logical name of the C# method `f(void)` in class `C` in namespace `N` is `"f(void)"`. Its [fully qualified logical name](#def_fully_qualified_logical_name) is `"N.C.f(void)"`.

<span id="def_message_string" class="anchor"></span>**message string**
- human-readable string that conveys information relevant to an element in a SARIF file

<span id="def_nested_artifact" class="anchor"></span>**nested artifact**
- [artifact](#def_artifact) that is contained within another artifact

**nested logical location**
- [logical location](#def_logical_location) that is contained within another logical location

    Example: A method within a class in C++

<span id="def_newline_sequence" class="anchor"></span>**newline sequence**
- sequence of one or more characters representing the end of a line of text

    NOTE: Some systems represent a newline sequence with a single newline character; others represent it as a carriage return character followed by a newline character.

<span id="def_notification" class="anchor"></span>**notification**
- [reporting item](#def_reporting_item) that describes a condition encountered by a [tool](#def_static_analysis_tool) during its execution

**opaque**
- neither human-readable nor machine-parseable into constituent parts

**parent (artifact)**
- [artifact](#def_artifact) which contains one or more [nested artifacts](#def_nested_artifact)

**physical location**
- location specified by reference to an [artifact](#def_artifact), possibly together with a [region](#def_region) within that artifact

**plain text message**
- [message string](#def_message_string) which does not contain any formatting information

<span id="def_plugin" class="anchor"></span>**plugin**
- [tool component](#def_tool_component) that defines additional [rules](#def_rule)

**policy**
- set of [rule configurations](#def_rule_configuration) that specify how [results](#def_result) that violate the [rules](#def_rule) defined by a particular [tool component](#def_tool_component) are to be treated

<span id="def_problem" class="anchor"></span>**problem**
- [result](#def_result) which indicates a condition that has the potential to detract from the quality of the program

    Example: A security vulnerability, a deviation from contractual or legal requirements, a deviation from stylistic standards.

<span id="def_property" class="anchor"></span>**property**
- attribute of an object consisting of a name and a value associated with the name

**property bag**
- object consisting of an unordered set of non-standardized [properties](#def_property) with arbitrary [camelCase names](#def_camelCase_name)

**redactable property**
- [property](#def_property) that potentially contains sensitive information that a SARIF [direct producer](#def_direct_producer) or a [SARIF post-processor](#def_post_processor) might wish to redact

<span id="def_region" class="anchor"></span>**region**
- contiguous portion of an [artifact](#def_artifact)

<span id="def_reporting_item" class="anchor"></span>**reporting item**
- unit of output produced by a [tool](#def_static_analysis_tool), either a [result](#def_result) or a [notification](#def_notification)

<span id="def_reporting_configuration" class="anchor"></span>**reporting configuration**
- the subset of [reporting metadata](#def_reporting_metadata) that a [tool](#def_static_analysis_tool) can configure at runtime, before performing its scan  
 
    Examples: severity level, rank

**reporting descriptor**
- container for [reporting metadata](#def_reporting_metadata)

<span id="def_reporting_metadata" class="anchor"></span>**reporting metadata**
- information that describes a class of related [reporting items](#def_reporting_item)  
    
    Examples: id, description

**repository**
- container for a related set of files in a version control system

**response file**
- file containing arguments for a [tool](#def_static_analysis_tool), which are interpreted as if they had appeared directly on the command line

<span id="def_result" class="anchor"></span>**result**
- [reporting item](#def_reporting_item) that describes a condition present in an [artifact](#def_artifact)

**result file**
- [artifact](#def_artifact) in which an [analysis tool](#def_static_analysis_tool) detects a [result](#def_result)

<span id="def_result_management_system" class="anchor"></span>**result management system**
- software system that consumes the [log files](#def_log_file) produced by [analysis tools](#def_static_analysis_tool), produces reports that enable engineering teams to assess the quality of their software [artifacts](#def_artifact) at a point in time and to observe trends in the quality over time, and performs functions such as filing bugs and displaying information about individual [results](#def_result)

    NOTE: A result management system can interact with a [log file viewer](#def_log_file_viewer) to display information about individual defects.

**result matching**
- process of determining whether two [results](#def_result) are reporting the same condition in the code

**root file**
- [SARIF log file](#def_log_file) to which one or more [external property files](#def_external_property_file) logically belong

<span id="def_rule" class="anchor"></span>**rule**
- specific criterion for correctness verified by an [analysis tool](#def_static_analysis_tool)

    NOTE 1: Many analysis tools associate a [rule id](#def_rule_id) with each [result](#def_result) they report, but some do not.

    NOTE 2: Some rules verify generally accepted criteria for correctness; others verify conventions in use in a particular team or organization.

    Examples: "Variables must be initialized before use.", "Class names must begin with an uppercase letter.".

<span id="def_rule_configuration" class="anchor"></span>**rule configuration**
- [reporting configuration](#def_reporting_configuration) that applies to a [rule](#def_rule)

<span id="def_rule_id" class="anchor"></span>**rule id**
- [stable value](#def_stable_value) which an [analysis tool](#def_static_analysis_tool) associates with a [rule](#def_rule)

    NOTE: A rule id is more likely to remain stable if it is a symbolic or numeric value, as opposed to a descriptive string.

    Example: `CA2001`

**rule metadata**
- [reporting metadata](#def_reporting_metadata) that describes a [rule](#def_rule)

<span id="def_run" class="anchor"></span>**run**
- 1\. invocation of a specified [analysis tool](#def_static_analysis_tool) on a specified version of a specified set of [analysis targets](#def_analysis_target), with a specified set of runtime parameters
- 2\. set of [results](#def_result) produced by such an invocation

<span id="def_sarif_consumer" class="anchor"></span>**SARIF consumer**
- program that reads and interprets a SARIF log file

<span id="def_sarif_log_file" class="anchor"></span>**SARIF log file**
- [log file](#def_log_file) in the format defined by this document

<span id="def_post_processor" class="anchor"></span>**SARIF post-processor**
- [SARIF producer](#def_sarif_producer) that transforms an existing [SARIF log file](#def_sarif_log_file) into a new SARIF log file, for example, by removing or redacting security-sensitive elements.

<span id="def_sarif_producer" class="anchor"></span>**SARIF producer**
- program that emits output in the SARIF format

<span id="def_stable_value" class="anchor"></span>**stable value**
- value which, once established, never changes over time

**standard taxonomy**
- [taxonomy](#def_taxonomic_category) defined without reference to a particular [analysis tool](#def_static_analysis_tool)

<span id="def_static_analysis_tool" class="anchor"></span>**(static analysis) tool**
- program that examines [artifacts](#def_artifact) to detect problems, without executing the program

    Example: Lint

**taxon (pl. taxa)**
- one of a set of categories which together comprise a [taxonomy](#def_taxonomic_category)

<span id="def_taxonomic_category" class="anchor"></span>**taxonomy**
- classification of analysis results into a set of categories

**tag**
- string that conveys additional information about the SARIF [log file](#def_log_file) element to which it applies

<span id="def_text_file" class="anchor"></span>**text artifact**
- [artifact](#def_artifact) considered as a sequence of characters organized into [lines](#def_line) and [columns](#def_column)

**text region**
- [region](#def_region) representing a contiguous range of zero or more characters in a [text artifact](#def_text_file)

<span id="def_thread_flow" class="anchor"></span>**thread flow**
- temporally ordered set of code locations specifying a possible execution path through the code, which occur within a single thread of execution, such as an operating system thread or a fiber

<span id="def_tool_component" class="anchor"></span>**tool component**
- component of an [analysis tool](#def_static_analysis_tool) or [converter](#def_converter), either its [driver](#def_driver) or an [extension](#def_extension), consisting of one or more files

**top-level artifact**
- [artifact](#def_artifact) which is not contained within any other artifact

**top-level logical location**
- [logical location](#def_logical_location) that is not nested within another logical location

    Example: A global function in C++

**translation**
- rendering of a [tool component](#def_tool_component)’s [localizable](#def_localizable) strings into another language

<span id="def_triage" class="anchor"></span>**triage**
- decide whether a [result](#def_result) indicates a [problem](#def_problem) that needs to be corrected

**user**
- see [end user](#def_end_user).

**VCS**
- version control system

**viewer**
- see [log file viewer](#def_log_file_viewer).

**web analysis tool**
- [analysis tool](#def_static_analysis_tool) that models and analyzes the interaction between a web client and a server.
