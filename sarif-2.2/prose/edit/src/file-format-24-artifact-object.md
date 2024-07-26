## artifact object

### General{#artifact-object--general}

An `artifact` object represents a single artifact.

### location property{#artifact-object--location-property}

Depending on the circumstances, an `artifact` object either **SHALL**, **MAY**, or **SHALL NOT** contain a property named `location` whose value is an `artifactLocation` object ([sec](#artifactlocation-object)).

If the `artifact` object represents a top-level artifact, then `location` **SHALL** be present.

If the `artifact` object represents a nested artifact whose location relative to the root of its parent can be expressed only by means of a path, then `location` **SHALL** be present, and the value of its `uri` property **SHALL** be a relative reference [cite](#RFC3986) beginning with `"/"` expressing that path.

If the `artifact` object represents a nested artifact whose location within its parent can be expressed only by a byte offset from the start of the parent, and not by means of a path, then `location` **SHALL NOT** be present.

If the `artifact` object represents a nested artifact whose location within its parent can be expressed either by means of a path or by means of a byte offset from the start of the parent, then `location` **MAY** be present; if it is absent, then `offset` ([sec](#offset-property)) **SHALL** be present. If `location` is present, the value of its `uri` property **SHALL** be a relative reference expressing the path of the nested artifact within the parent.

For an example, see [sec](#artifact-object--parentindex-property).

### parentIndex property{#artifact-object--parentindex-property}

If this `artifact` object represents a nested artifact, then it **SHALL** contain a property named `parentIndex` whose value is the array index ([sec](#array-indices)) of the parent artifact's `artifact` object within `theRun.artifacts` ([sec](#artifacts-property)).

If this `artifact` object represents a top-level artifact, then `parentIndex` **SHALL** be absent.

> NOTE: `parentIndex` makes it possible to navigate from the `artifact` object representing a nested artifact to the `artifact` objects representing each of its parent artifacts in turn, up to the top-level artifact.

> EXAMPLE 1: This example demonstrates two levels of artifact nesting. The top-level artifact is a ZIP archive represented by the `artifact` object at index 0 in the `artifacts` array. The archive contains a word processing document at the specified absolute path from its root; the document is represented by the `artifact` object at index 1. Finally, the document contains an embedded media object of the specified length at the specified offset from its beginning; the media object is represented by the `artifact` object at index 2. The media object’s `parentIndex` property refers to its parent document; the document’s `parentIndex` property refers to its parent ZIP archive, and the ZIP archive does not have a `parentIndex` property.
>
> ```json
> "artifacts": [
>   {
>     "location": {
>       "uri": "file:///C:/Code/app.zip"
>     },
>     "mimeType": "application/zip"
>   },
>   {
>     "location": {
>       "uri": "/docs/intro.docx"
>     },
>     "mimeType":
>       "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
>     "parentIndex": 0
>   },
>   {
>     "offset": 17522,
>     "length": 4050,
>     "mimeType": "application/x-contoso-animation",
>     "parentIndex": 1
>   }
> ]
> ```

### offset property

Depending on the circumstances, an `artifact` object either **SHALL**, **MAY**, or **SHALL NOT** contain a property named `offset` whose value is a non-negative integer.

If the `artifact` object represents a top-level artifact, then `offset` **SHALL NOT** be present.

If the `artifact` object represents a nested artifact whose location relative to its parent can be expressed only by means of a byte offset from the start of its parent artifact, then `offset` **SHALL** be present, and its value **SHALL** be that byte offset.

If the `artifact` object represents a nested artifact whose location within its parent can only be expressed by means of a path, and not by means of a byte offset from the start of the parent, then `offset` **SHALL NOT** be present.

If the `artifact` object represents a nested artifact whose location within its parent can be expressed either by means of a path or by means of a byte offset from the start of the parent, then `offset` **MAY** be present; if it is absent, then `location` ([sec](#artifact-object--location-property)) **SHALL** be present. If `offset` is present, its value **SHALL** be that byte offset.

### length property{#artifact-object--length-property}

An `artifact` object **MAY** contain a property named `length` whose value is a non-negative integer specifying the length of the artifact in bytes.

If `length` is absent, it **SHALL** default to -1, which indicates that the value is unknown (not set).

### roles property

An `artifact` object **MAY** contain a property named `roles` whose value is an array of zero or more unique ([sec](#array-properties-with-unique-values)) strings each of which specifies a role that this artifact played in the analysis.

Each array element **SHALL** have one of the following values, with the specified meanings:

- `"analysisTarget"`: The analysis tool was instructed to scan this artifact.

- `"attachment"`: The artifact is an attachment mentioned in `result.attachments` ([sec](#attachments-property)).

- `"conversionSource"`: The artifact is an output from an analysis tool in a non-SARIF format that was converted to SARIF.

- `"debugOutputFile"`: The artifact contains debug output from the tool.

- `"directory"`: The artifact is a directory (a container for other files and directories) rather than a file.

    NOTE 1: URIs do not represent "directories" in the file system sense. Even if the URI `https://www.example.com/dir/file` addresses a resource, the URI `https://www.example.com/dir` might also address a resource. Nonetheless, if the analysis tool knows that `https://www.example.com/dir` is not itself a resource, but only a prefix for other URIs that *are* resources, it is appropriate for the tool to mark `https://www.example.com/dir` with the `"directory"` role.

- `"driver"`: The file belongs to the analysis tool’s driver ([sec](#driver-property)).

- `"extension"`: The file belongs to one of the analysis tool’s extensions ([sec](#extensions-property)).

- `"externalPropertyFile"`: The artifact is an external property file ([sec](#external-property-file-format)).

- `"memoryContents"`: The artifact contains the contents of a portion of memory.

- `"policy"`: The file belongs to a policy ([sec](#policies)).

- `"referencedOnCommandLine"`: The artifact was referenced on the command line.

- `"repositoryRoot"`: The artifact is the root directory of a source control repository containing files that were analyzed

    NOTE 2: A single run might analyze files from multiple repositories.

- `"responseFile"`: The artifact contains command line arguments to a program, as specified in `invocation.responseFiles` ([sec](#responsefiles-property)).

- `"resultFile"`: A result was detected in this artifact (which the analysis tool was not explicitly instructed to scan).

    NOTE 3: For example, a scanner might be configured to analyze a C source file and find a result in a header file that it includes. The header file may be marked with the `"resultFile"` role. The C file should be marked with the `"analysisTarget"` role, however, as it was explicitly configured as a scan target.

- `"standardStream"`: The artifact contains the contents of one of the standard input or output streams, as specified in `invocation.stdin`, `invocation.stdout`, `invocation.stderr`, or `invocation.stdoutStderr` ([sec](#stdin-stdout-stderr-and-stdoutstderr-properties)).

- `"taxonomy"`: The file belongs to a taxonomy ([sec](#taxonomies)).

- `"toolSpecifiedConfiguration"`: The artifact is a configuration file provided by the tool.

- `"tracedFile"`: The analysis tool traced through this artifact while executing or simulating the execution of the code under test.

- `"translation"`: The file belongs to a translation ([sec](#translations)).

- `"userSpecifiedConfiguration"`: The artifact is a configuration file provided by the user.

> The following role values denote artifacts that have changed since some previous time which we refer to as the "baseline time."
>
> A SARIF producer **MAY** determine the baseline time in any way. (For example, if `theRun.baselineGuid` ([sec](#baselineguid-property)) is present, the tool might use its start time as the baseline time. Alternatively, the tool might use version control information, such as the time of some commit before the one being analyzed.)

- `"added"`: The artifact was added after the baseline time.

- `"deleted"`: The artifact was deleted after the baseline time.

- `"modified"`: The artifact was modified after the baseline time.

- `"renamed"`: The artifact was renamed after the baseline time. In this case, the `artifact` object specifies the new name.

- `"uncontrolled"`: The artifact is not under version control.

- `"unmodified"`: The artifact has not been modified since the baseline time.

    NOTE 4: The information conveyed by these values could be extracted from a VCS. These properties exist so SARIF consumers can have this information without needing access to the VCS.

### mimeType property

An `artifact` object **MAY** contain a property named `mimeType` whose value is a string that specifies the artifact’s MIME type [cite](#RFC2045). For information about the use of mimeType by SARIF viewers, see Appendix C.

### contents property{#artifact-object--contents-property}

An `artifact` object **MAY** contain a property named contents whose value is an `artifactContent` object ([sec](#artifactcontent-object)) representing the entire contents of the artifact.

### encoding property

If an `artifact` object represents a text artifact, it **MAY** contain a property named `encoding` whose value is a case-sensitive string that specifies the artifact’s text encoding. The string **SHALL** be one of the character set names defined by IANA [cite](#IANA-ENC).

If the `artifact` object represents a text artifact and this property is absent, it **SHALL** default to the value of `theRun.defaultEncoding` ([sec](#defaultencoding-property)), if that property is present; otherwise, the artifact’s encoding **SHALL** be taken to be unknown.

If the `artifact` object represents a binary artifact, `encoding` **SHALL** be absent.

> EXAMPLE 1: In this example, the encoding of output.txt is UTF-16BE (obtained from the default), but the encoding of data.txt is UTF-16LE:
>
> ```json
> {                                      # A run object ((#run-object)).
>   "defaultEncoding": "UTF-16BE",       # See (#defaultencoding-property).
> 
>   "artifacts": [                       # See (#artifacts-property).
>     {
>       "location": {
>         "uri": "output.txt"
>       }
>       # encoding property omitted
>     },
> 
>     {
>       "location": {
>         "uri": "data.txt"
>       },
>       "encoding": "UTF-16LE"
>     }
>   ]
> }
> ```

### sourceLanguage property{#artifact-object--sourcelanguage-property}

#### General{#sourcelanguage-property--general}

If an `artifact` object represents a text artifact that contains source code, it **MAY** contain a property named `sourceLanguage` whose value is a hierarchical string ([sec](#hierarchical-strings)) that specifies the programming language in which the source code is written. If the `artifact` object does not represent a text artifact containing source code, `sourceLanguage` **SHALL** be absent.

For the remainder of this section, we assume that the `artifact` object represents a text artifact that contains source code.

> NOTE 1: This property is intended to help SARIF viewers to render code snippets ([sec](#snippet-property)) with appropriate syntax coloring.

If the artifact contains source code in a mix of languages, and if it is possible to identify one of those languages as the "primary" language of the artifact, then `sourceLanguage` **SHALL** specify that language.

> NOTE 2: Typically, this is the language implied by the file name extension.

> EXAMPLE 1: In an HTML file that contains embedded JavaScript™, `sourceLanguage` would be `"html"`.

If it is not possible to identify a primary language, `sourceLanguage` **MAY** specify any language used in the artifact, or it **MAY** be absent.

> NOTE 3: In either case, it is possible to specify a source language for any region by using `region.sourceLanguage` (see [sec](#region-object--sourcelanguage-property)).

If `sourceLanguage` is absent, it **SHALL** default to the value of `theRun.defaultSourceLanguage` ([sec](#defaultsourcelanguage-property)). If both `artifact.sourceLanguage` and `theRun.defaultSourceLanguage` are absent, the artifact’s source language **SHALL** be taken to be unknown. In that case, a SARIF viewer **MAY** use any method or heuristic to determine the artifact’s source language, for example, by examining its file name extension or MIME type, or by prompting the user.

#### Source language identifier conventions and practices

To maximize interoperability, SARIF producers and consumers **SHOULD** conform to the following conventions and practices with respect to the value of this property:

- Producers:

  - Use only lower-case letters, and numbers (for example, `"c"` rather than `"C")`.

  - Spell out symbols (for example, `"csharp"` rather than `"c#"`).

  - To denote a language variant, use the hierarchical string mechanism (for example, `"csharp/7"`).

  - Do not abbreviate (for example, `"visualbasic"`™ rather than `"vb"`).

- Consumers

  - Accept source language identifiers that conform to the above producer conventions.

  - In addition, accept a variety of common industry forms, for example, {`"cplusplus"`, `"c++"`, `"cpp"`}, or `{"javascript"`, `"js"`}.

  - Compare source language identifiers case-insensitively.

[sec](#informative-sample-sourcelanguage-values), "Sample sourceLanguage values," provides sample values for common programming languages.

### hashes property

An `artifact` object **MAY** contain a property named `hashes` whose value is a non-empty object ([sec](#object-properties)) each of whose property names specifies the name of a hash function, and each of whose property values represents the value produced by that hash function.

> EXAMPLE 1: In this example, each of the hash functions SHA-256 and SHA-512 were used to compute hash values for the file.
>
> ```json
> {                   # A file object.
>   "hashes": {
>     "sha-256": "...",
>     "sha-512": "..."
>   }
> }
> ```

To maximize interoperability, the property names **SHOULD** appear in the IANA registry of hash function textual names [cite](#IANA-HASH). SARIF consumers that need to verify hash values **SHOULD** be able to compute any hash function whose name appears in the IANA registry.

The object **SHOULD** contain a property named `"sha-256"`. SARIF consumers that need to verify hash values **SHALL** be able to compute a SHA-256 hash.

The object **MAY** contain properties whose names do not appear in the IANA registry, but at the expense of interoperability. A SARIF consumer **MAY** implement any hash function, but it does not have to implement any hash function that does not appear in the IANA registry.

If the hash function is one whose name appears in the IANA registry, the property name **SHALL** equal the name as it appears in the registry (for example, `"sha-256"` rather than `"sha256"`); otherwise the property name **MAY** be any suitable name, but it **SHALL NOT** equal any name defined in the IANA registry.

SARIF consumers **SHALL** treat the property name as case insensitive (even when comparing to hash function names in the IANA registry).

Each property value **SHALL** be a string representation of the hash digest of the artifact, computed by the hash function specified by the property name. The string **SHALL** conform to the format produced by the hash algorithm (for example, if the hash algorithm produces a string of hexadecimal digits, the producer would not prepend "0x" to it).

> NOTE 1: The value is represented as a string because hash values are typically represented in hexadecimal notation, and JSON integer values must be decimal.

> NOTE 2: A hash value for an analysis target can be useful when a log file is processed by a result management system. The value can be used as a key when persisting results in a database. This allows a build system to use cached results, rather than repeating the analysis, when a target has not changed. A file hash can also be useful for validating results in a policy compliance system, allowing an auditor to validate that rerunning analysis against a target that hashes to a specific value reproduces the provided results.  
>
> The `artifact` object defines a set of hash values, rather than a single hash value, to allow a log file to be consumed by multiple tool chains that might expect hash values produced by differing hash function. Compliance systems, for example, will favor the use of more secure hash functions (such as SHA-256) that minimize the possibility that two different targets will produce the same hash (at the expense of speed to produce the hash). In situations where compliance and security are not a concern, a system might prefer to use a fast hash function (such as MD5 or SHA-1) even though they have known weaknesses that allow adversaries to more easily generate hash collisions.  
>
> To populate the `hashes` property, an analysis tool needs the ability to produce hashes for its analysis targets. Alternatively, the hashes could be added to the log file as a post-processing step.  
>
> To make the best use of such an analysis tool, a user (such as a build engineer) would determine what systems in their build environment will consume the log file. The user would then configure the tool to produce hashes using the hash functions required by those systems. Analysis tools that are configurable to produce hashes with a variety of commonly used hash functions will interoperate most easily with such systems.

### lastModifiedTimeUtc property

An `artifact` object **MAY** contain a property named `lastModifiedTimeUtc` whose value is a string in the format specified in [sec](#datetime-properties), specifying the UTC date and time at which the artifact was most recently modified.

> NOTE: In scenarios where a tool has analyzed files on a network file share or on a local disk, an engineering system might use this property, rather than `hashes` ([sec](#hashes-property)), as the most lightweight mechanism to determine whether the analysis needs to be repeated.

### description property{#artifact-object--description-property}

An `artifact` object **MAY** have a property named `description` whose value is a `message` object ([sec](#message-object)) that describes the artifact.
