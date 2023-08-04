<span id="def;analysis-target" class="anchor"></span>**analysis target**
- [artifact](def;artifact) which an [analysis tool](def;static-analysis-tool) is instructed to analyze

<span id="def;artifact" class="anchor"></span>**artifact**
- sequence of bytes addressable *via* a URI
- Examples: A physical file in a file system such as a source file, an object file, a configuration file or a data file; a specific version of a file in a version control system; a database table accessed *via* an HTTP request; an arbitrary stream of bytes returned from an HTTP request.

<span id="def;baseline" class="anchor"></span>**baseline**
- set of [results](def;result) produced by a single [run](#def-run) of a set of [analysis tools](def;static-analysis-tool) on a set of [artifacts](def;artifact)

    NOTE: A [result management system](def;result-management-system) can compare the results of a subsequent [run](def;run) to a baseline produced by a [baseline run](def;baseline-run) to determine whether new results have been introduced.

<span id="def;baseline-run" class="anchor"></span>**baseline run**
- [run](def;run) that produces a [baseline](#def-baseline) to which subsequent runs can be compared

<span id="def;binary-file" class="anchor"></span>**binary artifact**
- [artifact](def;artifact) considered as a sequence of bytes

<span id="def;binary-region" class="anchor"></span>**binary region**
- [region](#def-region) representing a contiguous range of zero or more bytes in a [binary artifact](def;binary-file)

<span id="def;call-stack" class="anchor"></span>**call stack**
- sequence of nested function calls

<span id="def;camelcase-name" class="anchor"></span>**camelCase name**
- name that begins with a lowercase letter, in which each subsequent word begins with an uppercase letter

    Example: `camelCase`, `version`, `fullName`.

<span id="def;code-flow" class="anchor"></span>**code flow**
- set of one or more [thread flows](def;thread-flow) which together specify a pattern of code execution relevant to detecting a [result](def;result)

<span id="def;column" class="anchor"></span>**column (number)**
- 1-based index of a character within a [line](def;line)

<span id="def;configuration-file" class="anchor"></span>**configuration file**
- file, typically textual, that configures the execution of an [analysis tool](def;static-analysis-tool) or [tool component](def;tool-component)

<span id="def;converter" class="anchor"></span>**converter**
- [SARIF producer](def;sarif-producer) that transforms the output of an [analysis tool](def;static-analysis-tool) from its native output format into the SARIF format

<span id="def;custom-taxonomy" class="anchor"></span>**custom taxonomy**
- [taxonomy](def;taxonomic-category) defined by and intended for use with a particular [analysis tool](def;static-analysis-tool)

<span id="def;direct-producer" class="anchor"></span>**direct producer**
- [analysis tool](def;static-analysis-tool) which acts as a [SARIF producer](def;sarif-producer)

<span id="def;driver" class="anchor"></span>**driver**
- [tool component](def;tool-component) containing an [analysis tool](def;static-analysis-tool)’s or [converter](def;converter)’s primary executable, which controls the tool’s or converter’s execution, and which in the case of an analysis tool typically defines a set of analysis [rules](#def-rule)

<span id="def;embedded-link" class="anchor"></span>**embedded link**
- syntactic construct which enables a [message string](def;message-string) to refer to a location within an [artifact](def;artifact) mentioned in a [result](#def-result)

<span id="def;engineering-system" class="anchor"></span>**engineering system**
- software development environment within which [analysis tools](def;static-analysis-tool) execute
 
    NOTE: An engineering system might include a build system, a source control system, a [result management system](def;result-management-system), a bug tracking system, a test execution system, and so on.

<span id="def;empty-array" class="anchor"></span>**empty array**
- array that contains no elements, and so has a length of 0

<span id="def;empty-object" class="anchor"></span>**empty object**
- object that contains no properties

<span id="def;empty-string" class="anchor"></span>**empty string**
- string that contains no characters, and so has a length of 0

<span id="def;end-user" class="anchor"></span>**(end) user**
- person who uses the information in a [log file](def;log-file) to investigate, [triage](def;triage), or resolve [results](#def-result)

<span id="def;extension" class="anchor"></span>**extension**
- [tool component](def;tool-component) other than the [driver](def;driver) (for example, a [plugin](#def-plugin), a [configuration file](def;configuration-file), or a [taxonomy](def;taxonomic-category))

<span id="def;external-property-file" class="anchor"></span>**external property file**
- file containing the values of one or more [externalized properties](def;externalized-property)

<span id="def;externalizable-property" class="anchor">**externalizable property**
- property that can be contained in an [external property file](def;external-property-file)

<span id="def;externalized-property" class="anchor"></span>**externalized property**
- property stored outside of the [SARIF log file](def;log-file) to which it logically belongs

<span id="def;false-positive" class="anchor">**false positive**
- [result](def;result) which an [end user](def;end-user) decides does not actually represent a [problem](def;problem)

<span id="def;fingerprint" class="anchor">**fingerprint**
- [stable value](def;stable-value) that can be used by a [result management system](def;result-management-system) to uniquely identify a [result](def;result) over time, even if a relevant [artifact](#def-artifact) is modified

<span id="def;fully-qualified-logical-name" class="anchor"></span>**formatted message**
- [message string](def;message-string) which contains formatting information such as Markdown formatting characters

<span id="def;fully-qualified-logical-name" class="anchor">**fully qualified logical name**
- string that fully identifies the programmatic construct specified by a [logical location](def;logical-location), typically by means of a hierarchical identifier.

    Example: The fully qualified logical name of the C# method `f(void)` in class `C` in namespace `N` is `"N.C.f(void)"`. Its [logical name](def;logical-name) is `"f(void)"`.

<span id="def;hierarchical-string" class="anchor">**hierarchical string**
- string in the format `<component>{/<component>}*`

<span id="def;line" class="anchor"></span>**line**
- contiguous sequence of characters, starting either at the beginning of an [artifact](def;artifact) or immediately after a [newline sequence](def;newline-sequence), and ending at and including the nearest subsequent newline sequence, if one is present, or else extending to the end of the artifact

<span id="def;line-number" class="anchor">**line (number)**
- 1-based index of a line within a file

    NOTE: Abbreviated to "line" when there is no danger of ambiguity with "[line](def;line)" in the sense of a sequence of characters.

<span id="def;localizable" class="anchor"></span>**localizable**
- subject to being translated from one natural language to another

<span id="def;log-file" class="anchor"></span>**log file**
- output file produced by an [analysis tool](def;static-analysis-tool), which enumerates the [results](def;result) produced by the tool

<span id="def;log-file-viewer" class="anchor"></span>**(log file) viewer**
- [SARIF consumer](def;sarif-consumer) that reads a [log file](def;log-file), displays a list of the [results](def;result) it contains, and allows an [end user](def;end-user) to view each result in the context of the [artifact](def;artifact) in which it occurs

<span id="def;logical-location" class="anchor"></span>**logical location**
- location specified by reference to a programmatic construct, without specifying the [artifact](def;artifact) within which that construct occurs

    Example: A class name, a method name, a namespace.

<span id="def;logical-name" class="anchor"></span>**logical name**
- string that partially identifies the programmatic construct specified by a [logical location](def;logical-location) by specifying the most specific (often the rightmost) component of its [fully qualified logical name](#def;fully-qualified-logical-name).

    Example: The logical name of the C# method `f(void)` in class `C` in namespace `N` is `"f(void)"`. Its [fully qualified logical name](#def;fully-qualified-logical-name) is `"N.C.f(void)"`.

<span id="def;message-string" class="anchor"></span>**message string**
- human-readable string that conveys information relevant to an element in a SARIF file

<span id="def;nested-artifact" class="anchor"></span>**nested artifact**
- [artifact](def;artifact) that is contained within another artifact

<span id="def;nested-logical-location" class="anchor">**nested logical location**
- [logical location](def;logical-location) that is contained within another logical location

    Example: A method within a class in C++

<span id="def;newline-sequence" class="anchor"></span>**newline sequence**
- sequence of one or more characters representing the end of a line of text

    NOTE: Some systems represent a newline sequence with a single newline character; others represent it as a carriage return character followed by a newline character.

<span id="def;notification" class="anchor"></span>**notification**
- [reporting item](def;reporting-item) that describes a condition encountered by a [tool](def;static-analysis-tool) during its execution

<span id="def;opaque" class="anchor">**opaque**
- neither human-readable nor machine-parseable into constituent parts

<span id="def;parent-artifact" class="anchor">**parent (artifact)**
- [artifact](def;artifact) which contains one or more [nested artifacts](def;nested-artifact)

<span id="def;physical-location" class="anchor">**physical location**
- location specified by reference to an [artifact](def;artifact), possibly together with a [region](#def-region) within that artifact

<span id="def;plain-text-message" class="anchor">**plain text message**
- [message string](def;message-string) which does not contain any formatting information

<span id="def;plugin" class="anchor"></span>**plugin**
- [tool component](def;tool-component) that defines additional [rules](def;rule)

<span id="def;policy" class="anchor">**policy**
- set of [rule configurations](def;rule-configuration) that specify how [results](def;result) that violate the [rules](#def-rule) defined by a particular [tool component](def;tool-component) are to be treated

<span id="def;problem" class="anchor"></span>**problem**
- [result](def;result) which indicates a condition that has the potential to detract from the quality of the program

    Example: A security vulnerability, a deviation from contractual or legal requirements, a deviation from stylistic standards.

<span id="def;property" class="anchor"></span>**property**
- attribute of an object consisting of a name and a value associated with the name

<span id="def;property-bag" class="anchor"></span>**property bag**
- object consisting of an unordered set of non-standardized [properties](def;property) with arbitrary [camelCase names](def;camelCase-name)

<span id="def;redactable-property" class="anchor"></span>**redactable property**
- [property](def;property) that potentially contains sensitive information that a SARIF [direct producer](def;direct-producer) or a [SARIF post-processor](def;post-processor) might wish to redact

<span id="def;region" class="anchor"></span>**region**
- contiguous portion of an [artifact](def;artifact)

<span id="def;reporting-item" class="anchor"></span>**reporting item**
- unit of output produced by a [tool](def;static-analysis-tool), either a [result](def;result) or a [notification](#def-notification)

<span id="def;reporting-configuration" class="anchor"></span>**reporting configuration**
- the subset of [reporting metadata](def;reporting-metadata) that a [tool](def;static-analysis-tool) can configure at runtime, before performing its scan  
 
    Examples: severity level, rank

<span id="def;reporting-descriptor" class="anchor"></span>**reporting descriptor**
- container for [reporting metadata](def;reporting-metadata)

<span id="def;reporting-metadata" class="anchor"></span>**reporting metadata**
- information that describes a class of related [reporting items](def;reporting-item)  
    
    Examples: id, description

<span id="def;repository" class="anchor"></span>**repository**
- container for a related set of files in a version control system

<span id="def;response-file" class="anchor"></span>**response file**
- file containing arguments for a [tool](def;static-analysis-tool), which are interpreted as if they had appeared directly on the command line

<span id="def;result" class="anchor"></span>**result**
- [reporting item](def;reporting-item) that describes a condition present in an [artifact](def;artifact)

<span id="def;result-file" class="anchor"></span>**result file**
- [artifact](#def-artifact) in which an [analysis tool](def;static-analysis-tool) detects a [result](def;result)

<span id="def;result-management-system" class="anchor"></span>**result management system**
- software system that consumes the [log files](def;log-file) produced by [analysis tools](def;static-analysis-tool), produces reports that enable engineering teams to assess the quality of their software [artifacts](def;artifact) at a point in time and to observe trends in the quality over time, and performs functions such as filing bugs and displaying information about individual [results](#def-result)

    NOTE: A result management system can interact with a [log file viewer](def;log-file-viewer) to display information about individual defects.

<span id="def;result-matching" class="anchor"></span>**result matching**
- process of determining whether two [results](def;result) are reporting the same condition in the code

<span id="def;root-file" class="anchor"></span>**root file**
- [SARIF log file](def;log-file) to which one or more [external property files](def;external-property-file) logically belong

<span id="def;rule" class="anchor"></span>**rule**
- specific criterion for correctness verified by an [analysis tool](def;static-analysis-tool)

    NOTE 1: Many analysis tools associate a [rule id](def;rule-id) with each [result](def;result) they report, but some do not.

    NOTE 2: Some rules verify generally accepted criteria for correctness; others verify conventions in use in a particular team or organization.

    Examples: "Variables must be initialized before use.", "Class names must begin with an uppercase letter.".

<span id="def;rule-configuration" class="anchor"></span>**rule configuration**
- [reporting configuration](def;reporting-configuration) that applies to a [rule](def;rule)

<span id="def;rule-id" class="anchor"></span>**rule id**
- [stable value](def;stable-value) which an [analysis tool](def;static-analysis-tool) associates with a [rule](def;rule)

    NOTE: A rule id is more likely to remain stable if it is a symbolic or numeric value, as opposed to a descriptive string.

    Example: `CA2001`

<span id="def;rule-metadata" class="anchor"></span>**rule metadata**
- [reporting metadata](def;reporting-metadata) that describes a [rule](def;rule)

<span id="def;run" class="anchor"></span>**run**
- 1\. invocation of a specified [analysis tool](def;static-analysis-tool) on a specified version of a specified set of [analysis targets](def;analysis-target), with a specified set of runtime parameters
- 2\. set of [results](def;result) produced by such an invocation

<span id="def;sarif-consumer" class="anchor"></span>**SARIF consumer**
- program that reads and interprets a SARIF log file

<span id="def;sarif-log-file" class="anchor"></span>**SARIF log file**
- [log file](def;log-file) in the format defined by this document

<span id="def;post-processor" class="anchor"></span>**SARIF post-processor**
- [SARIF producer](def;sarif-producer) that transforms an existing [SARIF log file](def;sarif-log-file) into a new SARIF log file, for example, by removing or redacting security-sensitive elements.

<span id="def;sarif-producer" class="anchor"></span>**SARIF producer**
- program that emits output in the SARIF format

<span id="def;stable-value" class="anchor"></span>**stable value**
- value which, once established, never changes over time

<span id="def;standard-taxonomy" class="anchor"></span>**standard taxonomy**
- [taxonomy](def;taxonomic-category) defined without reference to a particular [analysis tool](def;static-analysis-tool)

<span id="def;static-analysis-tool" class="anchor"></span>**(static analysis) tool**
- program that examines [artifacts](def;artifact) to detect problems, without executing the program

    Example: Lint

<span id="def;taxon-pl-taxa" class="anchor"></span>**taxon (pl. taxa)**
- one of a set of categories which together comprise a [taxonomy](def;taxonomic-category)

<span id="def;taxonomic-category" class="anchor"></span>**taxonomy**
- classification of analysis results into a set of categories

<span id="def;tag" class="anchor"></span>**tag**
- string that conveys additional information about the SARIF [log file](def;log-file) element to which it applies

<span id="def;text-file" class="anchor"></span>**text artifact**
- [artifact](def;artifact) considered as a sequence of characters organized into [lines](#def-line) and [columns](def;column)

<span id="def;text-region" class="anchor"></span>**text region**
- [region](#def-region) representing a contiguous range of zero or more characters in a [text artifact](def;text-file)

<span id="def;thread-flow" class="anchor"></span>**thread flow**
- temporally ordered set of code locations specifying a possible execution path through the code, which occur within a single thread of execution, such as an operating system thread or a fiber

<span id="def;tool-component" class="anchor"></span>**tool component**
- component of an [analysis tool](def;static-analysis-tool) or [converter](def;converter), either its [driver](#def-driver) or an [extension](def;extension), consisting of one or more files

<span id="def;top-level-artifact" class="anchor"></span>**top-level artifact**
- [artifact](#def-artifact) which is not contained within any other artifact

<span id="def;top-level-logical-location" class="anchor"></span>**top-level logical location**
- [logical location](def;logical-location) that is not nested within another logical location

    Example: A global function in C++

<span id="def;translation" class="anchor"></span>**translation**
- rendering of a [tool component](def;tool-component)’s [localizable](def;localizable) strings into another language

<span id="def;triage" class="anchor"></span>**triage**
- decide whether a [result](def;result) indicates a [problem](#def-problem) that needs to be corrected

<span id="def;user" class="anchor"></span>**user**
- see [end user](def;end-user).

<span id="def;vcs" class="anchor"></span>**VCS**
- version control system

<span id="def;viewer" class="anchor"></span>**viewer**
- see [log file viewer](def;log-file-viewer).

<span id="def;web-analysis-tool" class="anchor"></span>**web analysis tool**
- [analysis tool](def;static-analysis-tool) that models and analyzes the interaction between a web client and a server.
