## run object

### General{#run-object--general}

A `run` object describes a single run of an analysis tool and contains the output of that run.

> EXAMPLE:
> 
> ```json
> {
>   "tool": {       # See §3.14.6.
>     ...           # A tool object (§3.18).
>   },
>   "results": [    # See §3.14.23.
>     {
>       ...         # A result object (§3.27).
>     },
>     ...
>     {
>       ...         # Another result object.
>     }
>   ]
> }
> ```

### externalPropertyFileReferences property

A `run` object **MAY** contain a property named `externalPropertyFileReferences` whose value is an `externalPropertyFileReferences` object ([§3.15](#externalpropertyfilereferences-object)) that specifies the locations of the external property files (see [§3.15.2](#rationale)) associated with this log file.

### automationDetails property

A `run` object **MAY** contain a property named `automationDetails` whose value is a `runAutomationDetails` object ([§3.17](#runautomationdetails-object)) that describes this run.

For an example, see [§3.17.1](#runautomationdetails-object--general).

### runAggregates property

A `run` object **MAY** contain a property named `runAggregates` whose value is an array of zero or more unique ([§3.7.3](#array-properties-with-unique-values)) `runAutomationDetails` objects ([§3.17](#runautomationdetails-object)) each of which describes an aggregate of runs to which this run belongs.

For an example, see [§3.17.1](#runautomationdetails-object--general).

### baselineGuid property

A `run` object **MAY** contain a property named `baselineGuid` whose value is a GUID-valued string ([§3.5.3](#guid-valued-strings)) which **SHALL** equal the `automationDetails.guid` property ([§3.14.3](#automationdetails-property), [§3.17.4](#runautomationdetails-object--guid-property)) of some previous run.

> NOTE: This ensures that only "similar" runs are compared.

If `baselineGuid` is present, the `result.baselineState` property ([§3.27.24](#baselinestate-property)) of every `result` object ([§3.27](#result-object)) in `theRun` **SHALL** be computed with respect to the run specified by `baselineGuid`.

### tool property{#run-object--tool-property}

A `run` object **SHALL** contain a property named `tool` whose value is a `tool` object ([§3.18](#tool-object)) that describes the analysis tool that was run.

### language

A `run` object **MAY** contain a property named `language` whose value is a string specifying the language of the localizable strings ([§3.5.1](#localizable-strings)) in `theRun` (except for localizable strings that occur within `theRun.translations` ([§3.14.9](#translations-property))), in the format specified by the language tags standard \[[RFC5646](#RFC5646)\]. If this property is absent, it **SHALL** default to `"en-US"`.

> EXAMPLE 1: The language is region-neutral English:
> 
>       "language": "en"

> EXAMPLE 2: The language is French as spoken in France:
> 
>       "language": "fr-FR"

### taxonomies property

A `run` object **MAY** contain a property named `taxonomies` whose value is an array of zero or more unique ([§3.7.3](#array-properties-with-unique-values)) `toolComponent` objects ([§3.19](#toolcomponent-object)) each of which represents a standard taxonomy ([§3.19.3](#taxonomies)).

> NOTE: Analysis tools can define their own custom taxonomies; see [§3.19.3](#taxonomies) and [§3.19.25](#toolcomponent-object--taxa-property).

### translations property

A `run` object **MAY** contain a property named `translations` whose value is an array of zero or more unique ([§3.7.3](#array-properties-with-unique-values)) `toolComponent` objects ([§3.19](#toolcomponent-object)) each of which represents a translation ([§3.19.4](#translations)).

### policies property

A `run` object **MAY** contain a property named `policies` whose value is an array of zero or more unique ([§3.7.3](#array-properties-with-unique-values)) `toolComponent` objects ([§3.19](#toolcomponent-object)) each of which represents a policy ([§3.19.5](#policies)).

### invocations property

A `run` object **MAY** contain a property named `invocations` whose value is an array of zero or more `invocation` objects ([§3.20](#invocation-object)) that together describe a single run of a single analysis tool.

> NOTE: Normally, an analysis tool runs as a single process, and the `invocations` array requires only one element. The `invocations` property is defined as an array, rather than as a single `invocation` object, to accommodate tools which execute a sequence of programs to produce results. For example, a tool might run one program to determine the set of artifacts to analyze and another program to analyze those artifacts.

The elements of the `invocations` array **SHOULD**, as far as possible, be arranged in chronological order according to the start time of each process. If some of the processes run in parallel, this might not be possible.

### conversion property

If a `run` object was produced by a converter, it **MAY** contain a property named `conversion` whose value is a `conversion` object ([§3.22](#conversion-object)) that describes how the converter transformed the analysis tool’s native output format into the SARIF format.

A direct producer **SHALL NOT** emit the `conversion` property.

### versionControlProvenance property

A `run` object **MAY** contain a property named `versionControlProvenance` whose value is an array of zero or more unique ([§3.7.3](#array-properties-with-unique-values)) `versionControlDetails` objects ([§3.23](#versioncontroldetails-object)). Each array entry specifies a revision in a repository containing files that were scanned during the run.

> NOTE 1: This property allows an engineering system to reproduce a scan by retrieving the specified revision of the required files from each repository before repeating the analysis run.

> NOTE 2: This property is an array, rather than a single `versionControlDetails` object, to support scenarios where a tool scans files from multiple repositories in a single run.

> NOTE 3: This document refers to a container for a related set of files in a VCS as a "repository." Different VCSs might use different terms.

> NOTE 4: This document refers to a fixed revision of a set of files as a "revision". Different VCSs use different terms; for example, Git calls it a "commit".

> EXAMPLE: In this example, an analysis tool has scanned files from one repository: the GitHub repository `example/browser`.
> 
>   ```json
>   {                                    # A run object.
>      "versionControlProvenance": [
>       {                                # A versionControlDetails object (§3.23).
>           "repositoryUri": "https://github.com/example/browser",   # See §3.23.3.
>           "revisionId": "1a0c6554caa37144459cb97cb15429b27831476e" # See §3.23.4.
>           "branch": "master"             # See §3.23.5.
>       }
>       ]
>   }
> ```

### originalUriBaseIds property

A `run` object **MAY** contain a property named `originalUriBaseIds` whose value is an object ([§3.6](#object-properties)) each of whose property names designates a URI base id ([§3.4.4](#uribaseid-property)) and each of whose property values is an `artifactLocation` object ([§3.4](#artifactlocation-object)) that specifies (in the manner described below) the absolute URI \[[RFC3986](#RFC3986)\] of that URI base id on the machine where the SARIF producer ran.

If the `artifactLocation` object’s `uri` property ([§3.4.3](#uri-property)) is a relative reference, its `uriBaseId` property ([§3.4.4](#uribaseid-property)) **SHALL** be present. Otherwise (that is, if `uri` is an absolute URI, or if it is absent), `uriBaseId` **SHALL** be absent.

If the actual value of `uri` would have been an absolute URI, `uri` **MAY** be omitted.

> NOTE 1: A SARIF producer might omit such an absolute URI, or a SARIF postprocessor might remove it, for various reasons:
> 
> - To avoid revealing sensitive information such as a user name in a URI, for example, `file:///C:/Users/Mary/code/TheProject/`.
> 
> - To produce deterministic output (see [Appendix F](#informative-producing-deterministic-sarif-log-files)) by avoiding path names that differ depending on the machine where the analysis tool runs.

> EXAMPLE 1: In this example, the "top-level" property `PROJECTROOT` specifies a URI containing a username:
> 
> ```json
> "originalUriBaseIds": {
>  "PROJECTROOT": {
>     "uri": "file:///C:/Users/Mary/code/TheProject/",
>     "description": {
>       "text": "The root directory for all project files."
>     }
>  },
>   "SRCROOT": {
>     "uri": "src/",
>     "uriBaseId": "PROJECTROOT",
>     "description": {
>       "text": "The root of the source tree."
>     }
>   }
> }
> ```
> 
> A post-processor might remove `uri` to avoid revealing a username. The advantage of this approach over removing the entire `PROJECTROOT` property is that it retains the `description` property:
> 
> ```json
> "originalUriBaseIds": {
>  "PROJECTROOT": {
>     "description": {
>       "text": "The root directory for all project files."
>     }
>  },
>   "SRCROOT": {
>     "uri": "src/",
>     "uriBaseId": "PROJECTROOT",
>     "description": {
>       "text": "The root of the source tree."
>     }
>   }
> }
> ```

The values of the `uriBaseId` properties in the `artifactLocation` objects in `originalUriBaseIds` **SHALL NOT** form a loop, in the sense described in the URI base id resolution procedure below.

The values of the `uri` properties in the `artifactLocation` objects in `originalUriBaseIds`:

- **SHALL** end with a single forward slash .

- **SHALL NOT** include a query or fragment component as defined in URI Generic Syntax \[[RFC3986](#RFC3986)\].

- **SHALL NOT** include `".."` path segments.

    NOTE 2: The rationale for these restrictions is to allow the `uriBaseId` resolution procedure described below to work by simple concatenation of the `uri` properties in `originalUriBaseIds`. The prohibition of `".."` path segments ensures that the resolution procedure works with `file` scheme URIs, without concern for the presence of symbolic links. See [§3.10.2](#normalizing-file-scheme-uris) for more information on this point.

This property allows SARIF consumers to resolve any relative references which appear in any `artifactLocation` objects elsewhere in the run, as long as the consumer runs either on the same machine as the producer, or on a machine with an identical file system layout. This is useful for individual developers who wish to run analysis tools and examine the results in a viewer. It is also useful for teams which share a convention for their file system layout.

A SARIF consumer **SHALL** use the following procedure to resolve a URI base id from the information in `originalUriBaseIds`:

> NOTE 3: This procedure is part of an overall URI base id resolution procedure described in [§3.4.4](#uribaseid-property).

> NOTE 4: In this procedure, we refer to the resolved URI value by the variable name `resolvedUri`.

1.  Set `resolvedUri` to an empty string.

2.  Fetch the `artifactLocation` object whose property name within `originalUriBaseIds` is the value of `uriBaseId`. If there is no such property, the resolution procedure fails.

3.  Prepend `artifactLocation.uri` to `resolvedUri`.

4.  If `artifactLocation.uri` is an absolute URI, `resolvedUri` is the final resolved URI, and the procedure succeeds.  
      
    Otherwise:

5.  If `uriBaseId` is absent, the resolution procedure fails.

    &emsp;&emsp;NOTE 3: This would not occur in a valid SARIF file, but the file might not be valid.

6.  If the value of `uriBaseId` has already been encountered during this resolution procedure (that is, if there is a loop in the sequence of URI base ids), the resolution procedure fails.

    &emsp;&emsp;NOTE 4: This would not occur in a valid SARIF file, but the file might not be valid.

7.  Otherwise (that is, if `uriBaseId` is present and its value has not previously been encountered during this resolution), return to Step 2.

>   EXAMPLE 2: In this example, the URI base id `"SRCROOT"` on the machine where the SARIF producer ran was `"file:///C:/code/MyProject/src/"`. The producer detected a result in a file whose location relative to that URI base id was `"lib/memory.c"`. A viewer which wished to display that file would first attempt to locate it on the local file system at `"C:\code\MyProject\src\lib\memory.c"`. If the file did not exist at that location, the viewer might prompt the user for the location.
> 
> ```json
> {                                         # A run object.
>   "originalUriBaseIds": {
>     "PROJECTROOT": {
>       "uri": "file:///C:/code/TheProject/"
>     },
>     "SRCROOT": {
>       "uri": " src/",
>       "uriBaseId": "PROJECTROOT"
>     }
>   },
> 
>   "results": [
>     {                                     # A result object (§3.27).
>       "ruleId": "CA1001",
>       "locations": [
>         {                                 # A location object (§3.28).
>           "physicalLocation": {           # See §3.28.3.
>             "artifactLocation": {         # An artifactLocation object (§3.4).
>               "uri": "lib/memory.c",
>               "uriBaseId": "SRCROOT"
>             }
>           }
>         }
>       ]
>     }
>   ]
> }
> ```

### artifacts property

A `run` object **MAY** contain a property named `artifacts` whose value is an array of zero or more unique ([§3.7.3](#array-properties-with-unique-values)) `artifact` objects ([§3.24](#artifact-object)) each of which represents an artifact relevant to the run.

The array **SHOULD** contain elements representing at least those artifacts in which results were detected, but it **MAY** contain elements representing all artifacts examined by the tool (whether or not results were detected in those artifacts), or any subset of those artifacts. It **MAY** also include other artifacts relevant to the run, such as attachments ([§3.27.26](#attachments-property)).

> NOTE: `artifact` objects contain information that is useful for viewers. Viewers will be able to provide the most information to users if the `artifacts` property is present and contains information for every artifact in which results were detected.

> EXAMPLE:
> 
>   ```json
>   "artifacts": [
>    {
>       "location": {
>           "uri": "file:///C:/Code/main.c"
>       },
>       "sourceLanguage": "c",
>       "hashes": {
>            "sha-256": "b13ce2678a8807ba0765ab94a0ecd394f869bc81"
>       }
>     }
>   }
>   ```

In some cases, an artifact might be nested within another artifact (for example, a compressed container), referred to as its "parent." An artifact that is not nested within another artifact is referred to as a "top-level artifact". An artifact that is nested within another artifact is referred to as a "nested artifact". Within the `artifacts` array, an `artifact` object representing a nested artifact is linked to its parent *via* its `parentIndex` property ([§3.24.3](#artifact-object--parentindex-property)). For an example, see [§3.24.3](#artifact-object--parentindex-property).

If a nested artifact appears in the `artifacts` array, then the `artifacts` array **SHALL** also contain elements describing each of its parents, up to and including the top-level artifact.

### specialLocations property

A `run` object **MAY** contain a property named `specialLocations` whose value is a `specialLocations` object ([§3.25](#speciallocations-object)) that defines locations of special significance to SARIF consumers.

### logicalLocations property{#run-object--logicallocations-property}

A `run` object **MAY** contain a property named `logicalLocations` whose value is an array of zero or more unique ([§3.7.3](#array-properties-with-unique-values)) `logicalLocation` objects ([§3.33](#logicallocation-object)) each of which represents a logical location relevant to one or more results detected during the run.

In some cases, a logical location might be nested within another logical location (for example, a class nested within a namespace), referred to as its "parent." A logical location that is not nested within another logical location is referred to as a "top-level logical location". A logical location that is nested within another logical location is referred to as a "nested logical location". Within the `logicalLocations` array, a `logicalLocation` object representing a nested logical location is linked to its parent *via* its `parentIndex` property ([§3.33.8](#logicallocation-object--parentindex-property)).

If a nested logical location appears in the `logicalLocations` array, then the `logicalLocations` array **SHALL** also contain elements describing each of its parents, up to and including the top-level logical location.

> EXAMPLE: In this example, a result was detected in the C++ class `namespaceA::namespaceB::classC`. The `logicalLocations` array contains not only an element describing the class, but also elements describing its containing namespaces.
> 
> ```json
> "logicalLocations": [
>   {
>     "name": "classC",
>     "fullyQualifiedName": "namespaceA::namespaceB::classC",
>     "kind": "type",
>     "parentIndex": 1
>   },
>   {
>     "name": "namespaceB",
>     "fullyQualifiedName": "namespaceA::namespaceB",
>     "kind": "namespace"
>     "parentIndex": 2
>   },
>   {
>     "fullyQualifiedName": "namespaceA",
>     "kind": "namespace"
>   }
> ]
> ```

> NOTE: The detailed information in `logicalLocations` is useful, even though much of it is captured in `logicalLocation.fullyQualifiedName` ([§3.33.5](#logicallocation-object--fullyqualifiedname-property)), because it allows results management systems and other SARIF consumers to organize analysis results, for example, by asking questions such as "How many results were found in the namespace `namespaceA::namespaceB`?". Programs can ask these questions without having to know how to parse the `fullyQualifiedName` string.

### addresses property

A `run` object **MAY** contain a property named `addresses` whose value is an array of zero or more unique ([§3.7.3](#array-properties-with-unique-values)) `address` objects ([§3.32](#address-object)) representing addresses that appear in `physicalLocation` objects ([§3.29](#physicallocation-object)) within `theRun`.

In some cases, an address might be nested within another address (for example, an offset within a table within a section). An address that is nested within another address is referred to as a "nested address". Within the `addresses` array, an `address` object representing a nested address is linked to its parent *via* its `parentIndex` property ([§3.32.13](#address-object--parentindex-property)).

If a nested address appears in the `addresses` array, then `addresses` **SHALL** also contain elements describing each of its parents, up to and including the top-level address.

### threadFlowLocations property

A `run` object **MAY** contain a property named `threadFlowLocations` whose value is an array of zero or more unique ([§3.7.3](#array-properties-with-unique-values)) `threadFlowLocation` objects ([§3.38](#threadflowlocation-object)) representing locations that appear in `threadFlow` objects ([§3.37](#threadflow-object)) within `theRun`.

The `threadFlowLocations` array may contain all or any subset of the `threadFlowLocation` objects in the run.

> NOTE: Defining `threadFlowLocation` objects within `run.threadFlowLocations` can reduce the size of the log file if certain locations occur frequently, either within a single thread flow (for example, if the thread flow represents a loop) or across thread flows (for example, if all thread flows start at the program entry point and share their first few locations).

### graphs property{#run-object--graphs-property

A `run` object **MAY** contain a property named `graphs` whose value is an array of zero or more unique ([§3.7.3](#array-properties-with-unique-values)) `graph` objects ([§3.39](#graph-object)). A `graph` object represents a directed graph: a network of nodes and directed edges that describes some aspect of the structure of the code (for example, a call graph).

A `graph` object defined at the `run` level **MAY** be referenced by a `graphTraversal` object ([§3.42](#graphtraversal-object)) defined in the `graphTraversals` property ([§3.27.20](#graphtraversals-property)) of any `result` object ([§3.27](#result-object)) in `theRun`.

### webRequests property

A `run` object **MAY** contain a property named `webRequests` whose value is an array of zero or more unique ([§3.7.3](#array-properties-with-unique-values)) `webRequest` objects ([§3.46](#webrequest-object)) representing HTTP requests that appear in `result` objects ([§3.27](#result-object)) within `theRun`.

> NOTE: This property is primarily useful to web analysis tools.

### webResponses property

A `run` object **MAY** contain a property named `webResponses` whose value is an array of zero or more unique ([§3.7.3](#array-properties-with-unique-values)) `webResponse` objects ([§3.47](#webresponse-object)) representing HTTP responses that appear in `result` objects ([§3.27](#result-object)) within `theRun`.

> NOTE: This property is primarily useful to web analysis tools.

### results property

Depending on the circumstances, a `run` object either **SHALL** or **MAY** contain a property named `results` whose value, again depending on circumstances, is either `null` or an array of zero or more `result` objects ([§3.27](#result-object)) each of which represents a single result detected in the course of the run.

> NOTE: The `results` array is not defined to contain unique ([§3.7.3](#array-properties-with-unique-values)) elements because some tools report a line number but not a column number for a result’s location. Such a tool might report the same result twice on the same line, in some cases producing multiple identical `result` objects.

If the tool failed to start, and if the engineering system responsible for running the tool synthesized a SARIF file to record the failure, then `results` **MAY** be present. If it is present, its value **SHALL** be `null`. See [§3.20.13](#processstartfailuremessage-property), `invocation.processStartFailureMessage`, for more about this scenario.

If the tool started but failed to begin its analysis (for example, because its command line was invalid), then again `results` **MAY** be present, and if present **SHALL** be `null`.

In all other circumstances, `results` **SHALL** be present and **SHALL** contain all results detected by the tool. If the tool did not detect any results, `results` **SHALL** be an empty array.

If `results` is absent, it **SHALL** default to `null`.

### defaultEncoding property

A `run` object **MAY** contain a property named `defaultEncoding` whose value is a case-sensitive string that provides a default for the `encoding` property ([§3.24.9](#encoding-property)) of any `artifact` object ([§3.24](#artifact-object)) in `theRun.artifacts` ([§3.14.15](#artifacts-property)) that refers to a text artifact. The string **SHALL** be one of the character set names defined by IANA \[[IANA-ENC](#IANA_ENC)\].

If this property is absent, it **SHALL** be interpreted as meaning that there is no default file encoding. In that case, the encoding of any `artifact` object that does not contain an `encoding` property **SHALL** be taken to be unknown.

For an example, see [§3.24.9](#encoding-property).

### defaultSourceLanguage property

A `run` object **MAY** contain a property named `defaultSourceLanguage` whose value is a hierarchical string ([§3.5.4](#hierarchical-strings)) that provides a default value for the `sourceLanguage` property ([§3.24.10](#artifact-object--sourcelanguage-property)) of any `artifact` object ([§3.24](#artifact-object)) in `theRun.artifacts` ([§3.14.15](#artifacts-property)) which refers to a text artifact that contains source code.

If `defaultSourceLanguage` is present, its value **SHOULD** conform to the conventions defined in [§3.24.10.2](#source-language-identifier-conventions-and-practices).

If `defaultSourceLanguage` is absent, it **SHALL** be taken to mean that there is no default source language. In that case, the source language of any `artifact` object that does not contain a `sourceLanguage` property **SHALL** be taken to be unknown. In that case, a SARIF viewer **MAY** use any method or heuristic to determine the source language of each file, for example by examining the file’s file name extension or MIME type, or by prompting the user.

### newlineSequences property

A `run` object **MAY** contain a property named `newlineSequences` whose value is an array of one or more unique ([§3.7.3](#array-properties-with-unique-values)) strings each of which specifies a character sequence that the tool treated as a line break during this run.

If this property is absent, it **SHALL** default to the array `[ "\r\n", "\n" ]`.

The order of the elements in the array is significant. It **SHALL** mean that at potential line breaks, the tool "greedily" attempted to match each element of the array in order.

> EXAMPLE 1: If `newlineSequences` has the value `[ "\r\n", "\r", "\n" ]`, the character sequence `"\r\n"` counts as one line break, not two.

> NOTE: This property is useful for SARIF consumers that are sensitive to the value of the line number properties `startLine` ([§3.30.5](#startline-property)) and `endLine` ([§3.30.7](#endline-property)) in `region` objects ([§3.30](#region-object)). It ensures that the consumer counts lines in the same way as the producer. A SARIF viewer might use this property when highlighting a region to ensure that it highlights the correct lines. More critically, a tool that applies fixes (see [§3.55](#fix-object)), especially one that applies them automatically, can use this property to ensure that it inserts and removes content on the correct lines.

> EXAMPLE 2: In this example, the SARIF producer accepts the Unicode characters NEXT LINE (U+0085) and LINE SEPARATOR (U+2028) as line separators in addition to the usual values.
> 
> ```json
> {         # A run object (§3.14).
>   ...
>   "newlineSequences": [ "\r\n", "\n", "\u0085", "\u2028" ],
>   ...
> }
> ```

### columnKind property

If a SARIF producer processes text artifacts and `theRun.results` ([§3.14.23](#results-property)) is non-empty, the `run` object **SHALL** contain a property named `columnKind` whose value is a string that specifies the unit in which the analysis tool measures columns. If a SARIF producer processes text artifacts and `theRun.results` is empty, `columnKind` **MAY** be present.

`columnKind` **SHALL** have one of the following values, with the specified meanings:

- `"utf16CodeUnits"`: Each UTF-16 code unit is considered to occupy one column. This means that a surrogate pair is considered to occupy two columns.

- `"unicodeCodePoints"`: Each Unicode code point (abstract character) is considered to occupy one column. This means that even a character that is represented in UTF-16 by a surrogate pair is considered to occupy one column.

If the SARIF producer does not process text artifacts, `columnKind` **SHALL** be absent.

If a SARIF consumer uses a column measurement unit other than that specified by `columnKind`, and if the consumer is required to interact with the artifact’s contents (for example, by displaying the artifact in an editor and highlighting a region), the consumer **SHALL** recompute column numbers in its (the consumer’s) native measurement unit.

### redactionTokens property

If the value of any redactable property ([§3.5.2](#redactable-strings)) in `theRun` has been redacted, `theRun` **SHALL** contain a property named `redactionTokens` whose value is an array of zero or more unique ([§3.7.3](#array-properties-with-unique-values)) strings any of which can be used to replace redacted text. If no text in `theRun` has been redacted, `redactionTokens` **SHALL** be absent.

If `redactionTokens` contains a single element, that element **SHOULD** be the string `"[REDACTED]"`; if it contains more than one, each additional element **SHOULD** be of the form `"[REDACTED-`*n*`]"` where *n* is a positive integer.

> NOTE 1: The rationale for recommending the alternate form only for the second and subsequent tokens is that a tool might create one token and only later discover that additional tokens are required. With this recommendation, the tool does not have to rename the token it has already created.

> NOTE 2: Redaction tokens have no special meaning in properties not specified as "redactable."

If for any reason different values are used, they **MAY** be any readily identifiable strings. An example of a situation where a SARIF producer might choose a different redaction token is if the string `"[REDACTED]"` occurs in the value of a redactable property in `theRun`.

> EXAMPLE 1: In this example, the leading portion of a full path name has been redacted from the redactable property `invocation.commandLine` to avoid revealing information about the machine’s directory layout.
> 
> ```json
> {                     # A run object (§3.14).
>   "redactionTokens": [
>     "[REDACTED]"
>   ],
> 
>   "invocation": {
>     "commandLine": "SourceScanner --input [REDACTED]/src/ui"
>   }
>   ...
> }
> ```
