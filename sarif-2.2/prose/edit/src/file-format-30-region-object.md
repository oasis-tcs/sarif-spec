## region object

### General{#region-object--general}

A `region` object represents a region, that is, a contiguous portion of an artifact.

The `region` object defines both "text properties" and "binary properties." The text properties represent a region as a contiguous range of zero or more characters (a "text region"). The binary properties represent a region as a contiguous range of zero or more bytes (a "binary region").

A region SHALL contain at least one of startLine, charOffset, or byteOffset.

If `startLine` ([§3.30.5](#startline-property)) > 0 or `charOffset` ([§3.30.10](#charlength-property)) >= 0, this `region` object **SHALL** define a text region. If `byteOffset` ([§3.30.11](#byteoffset-property)) >= 0, this `region` object **SHALL** define a binary region. If a `region` object defines both a text region and a binary region, the text region and the binary region **SHALL** specify the identical range of bytes in the artifact, as determined by the artifact’s character encoding.

For regions in text artifacts, a `region` object **SHOULD** define a text region and **MAY** also define a binary region; it **SHALL** define either a text region or a binary region or both.

For regions in binary artifacts, a region object **SHALL** define a binary region and **SHALL NOT** define a text region.

If any text properties are present, enough text properties **SHALL** be present to fully specify a text region (see [§3.30.2](#text-regions)). If any binary properties are present, then enough binary properties **SHALL** be present to fully specify a binary region (see [§3.30.3](#binary-regions)).

### Text regions

> NOTE 1: The examples in this section assume a text file with the following contents:
> 
>     abcd\r\nefg\r\nhijk\r\nlmn\r\n
> 
> Breaking the lines for the sake of readability, the contents are:
> 
>     abcd\r\n
>     efg\r\n
>     hijk\r\n
>     lmn\r\n
> 
> The file contains four lines, each of which ends with the two-character newline sequence `"\r\n"`, which is explicitly displayed for clarity.

The line number of the first line in a text artifact **SHALL** be 1. The column number of the first character in each line **SHALL** be 1. The character offset of the first character in the artifact **SHALL** be 0.

The values of text properties **SHALL NOT** depend on the presence or absence of a byte order mark (BOM) at the start of the artifact.

Column numbers are expressed in the measurement unit specified by `theRun.columnKind` ([§3.14.27](#columnkind-property)).

A SARIF viewer **MAY** choose to present column numbers that match the visual offset of each character from the beginning of the line. These "visual" column numbers might not match the column numbers contained in the SARIF file.

> NOTE 2: Such a mismatch might occur if, for example, the line contains a tab character, or an accented character represented by a base character plus a combining character.

A text artifact’s character encoding determines the number of bytes that represent each character, and therefore determines the range of bytes represented by a text region. A SARIF consumer **SHALL** consider an artifact to have the encoding specified by `artifact.encoding` ([§3.24.9](#encoding-property)), if present, or else by `theRun.defaultEncoding` ([§3.14.24](#defaultencoding-property)), if present. If neither is present, the consumer **MAY** use any heuristic or procedure to determine the encoding, including (for example) prompting the user.

> NOTE 3: If a consumer incorrectly determines an artifact’s encoding, it might not display the artifact correctly. For example, when it attempts to highlight a region, it might highlight an incorrect range of characters.

A text region **MAY** be specified in two ways:

- By means of the "line/column" properties `startLine` ([§3.30.5](#startline-property)), `startColumn` ([§3.30.6](#startcolumn-property)), `endLine` ([§3.30.7](#endline-property)), and `endColumn` ([§3.30.8](#endcolumn-property)).

- By means of the "offset/length" properties `charOffset` ([§3.30.9](#charoffset-property)) and `charLength` ([§3.30.10](#charlength-property)).

A text region **SHALL** specify both its start (the location of its first character) and its end (the location of its last character).

> NOTE 4: The end of a text region does not have to be specified explicitly if the default values for `endLine`, `endColumn`, and/or `charLength` correctly describe the region.

A text region does not include the character specified by `endColumn` (see [§3.30.8](#endcolumn-property)).

> EXAMPLE 1: The following regions (among others) all specify the range of characters `"bc"`.
> 
> ```json
> {
>   "startLine": 1,
>   "startColumn": 2,
>   "endLine": 1,
>   "endColumn": 4     # The region excludes the character at endColumn.
> } 
> 
> {
>   "charOffset": 1,
>   "charLength": 2
> }
> 
> {
>   "startLine": 1,
>   "startColumn": 2,
>   "endLine": 1,
>   "endColumn": 4,
>   "charOffset": 1,
>   "charLength": 2
> }
> ```

> EXAMPLE 2: The following region is invalid, even though it might appear to specify the same range of characters `"bc"` as in > EXAMPLE 1:
> 
> ```json
> {
>   "startLine": 1,
>   "charOffset": 1,   # Specifies the "b"
>   "endColumn": 4     # Specifies the column one past the "c"
> }
> ```
> 
> This is because the line/column properties and the offset/length properties, taken independently, specify different regions:
> 
> - `"startColumn"` is absent, and so defaults to 1 (see [§3.30.6](#startcolumn-property)).
> 
> - `"endLine"` is absent, and so defaults to `"startLine"`, which in this example is 1 (see [§3.30.7](#endline-property)).
> 
> - `"charLength"` is absent, and so defaults to 0 (see [§3.30.10](#charlength-property)).
> 
> In summary, the above region is equivalent to the region
> 
> ```json
> {
>   "startLine": 1,
>   "startColumn": 1,
>   "endLine": 1,
>   "endColumn": 4,
> 
>   "charOffset": 1,
>   "charLength": 0
> }
> ```
> 
> Now we can see that the line/column properties represent the range of characters `"abc"`, while the offset/length properties represent an insertion point before the character `"b"` (see [§3.30.10](#charlength-property)). Those two regions are not the same, and so the region is invalid.
> 
If a region spans one or more lines, it **SHALL** include the newline sequences of all but the last line in the region.

> NOTE 5: This is not an independent requirement; it is a consequence of the specification for the default value of `endColumn`.

> EXAMPLE 3: The region
> 
>     { "startLine": 2 }
> 
> includes the characters `"efg"`.

> EXAMPLE 4: The region
> 
>     { "startLine": 2, "endLine": 3 }
> 
> includes the characters `"efg\r\nhijk"`.

To specify an entire line together with its trailing newline sequence, specify the region’s end point to be column 1 on the next line.

> NOTE 6: This is again a consequence of the specification of `endColumn`, which states that it specifies the character one past the end of the region.

> EXAMPLE 5: The region
> 
>     { "startLine": 2, "endLine": 3, "endColumn": 1 }
> 
> includes the characters `"efg\r\n"`.

A region of length 0 is referred to as an "insertion point." An insertion point **MAY** be specified either by specifying `charLength` as 0, or by specifying the same values for `startColumn` and `endColumn`.

> NOTE 7: Once more, this is again a consequence of the specification of `endColumn`.

> EXAMPLE 6: These regions (among others) specify an insertion point before the `"b"` on line 1.
> 
>     { "startLine": 1, "startColumn": 2, "endColumn": 2 }
>     { "charOffset": 1, "charLength": 0 }

> EXAMPLE 7: These regions (among others) specify an insertion point at the beginning of the file:
> 
>     { "startLine": 1, "startColumn": 1, "endColumn": 1 }
>     { "charOffset": 0, "charLength": 0 }

To specify an insertion point after the last character in an artifact, set `endLine` to the number of the last line in the artifact, and set `endColumn` to a value one greater than the number of characters on the line, *including* any trailing newline sequence.

> EXAMPLE 8: These regions (among others) specify an insertion point at the very end of the file. Note that the last line contains the five characters (including the newline sequence) `"lmn\r\n"`.
> 
>     { "startLine": 4, "startColumn": 6, "endColumn": 6 }
>     { "charOffset": 22, "charLength": 0 }

### Binary regions

The byte offset of the first byte in an artifact **SHALL** be 0.

To specify a byte region, at least `byteOffset` ([§3.30.11](#byteoffset-property)) **SHALL** be present. `byteLength` ([§3.30.12](#bytelength-property)) **MAY** also be present. `byteOffset` specifies the start of the region. `byteLength` specifies the region’s length and thereby, indirectly, its end. A `byteLength` value of 0 represents an insertion point before the byte specified by `byteOffset`.

### Independence of text and binary regions

The text-related and binary-related properties in a `region` object **SHALL** be treated independently. That is, the value of a text-related property **SHALL NOT** be inferred from the value of any set of binary-related properties, and *vice versa*.

> EXAMPLE: This example is based on the sample text file shown in NOTE 1 of [§3.30.2](#text-regions). It represents invalid SARIF because the text-related and binary-related properties are inconsistent. At first glance they appear to be consistent because the byte at offset 2 is indeed on line 1:
> 
>     { "startLine": 1, "byteOffset": 2, "byteLength": 6 }
> 
> However, because the default values for the missing text-related properties are determined entirely from the existing text-related properties, and independently of any binary-related properties, this region is in fact equivalent to this one:
> 
> ```json
> {
>   "startLine": 1,
>   "startColumn": 1,  // Missing startColumn defaults to 1.
>   "endLine": 1,      // Missing endLine defaults to startLine.
>   "endColumn": 5,    // Missing endColumn defaults to (length of endLine + 1),
>                      // exclusive of newline sequence.
>   "byteOffset": 2,
>   "byteLength": 6
> }
> ```

This makes it clear that the text-related and binary-related properties represent different ranges of bytes, and therefore the region is invalid.

### startLine property

When a `region` object represents a text region specified by line/column properties, it **SHALL** contain a property named `startLine` whose value is a positive integer equal to the line number of the line containing the first character in the region.

### startColumn property

When a `region` object represents a text region specified by line/column properties, it **MAY** contain a property named `startColumn` whose value is a positive integer equal to the column number of the first character in the region.

If `startColumn` is absent, it **SHALL** default to 1.

### endLine property

When a `region` object represents a text region specified by line/column properties, it **MAY** contain a property named `endLine` whose value is a positive integer equal to the line number of the line containing the last character in the region.

If `endLine` is absent, its value **SHALL** default to `startLine`.

### endColumn property

When a `region` object represents a text region specified by line/column properties, it **MAY** contain a property named `endColumn` whose value is an integer whose value is one greater than the column number of the last character in the region.

If `endColumn` is absent, it **SHALL** default to a value one greater than the column number of the last character on the line, excluding any newline sequence.

### charOffset property

When a `region` object represents a text region specified by offset/length properties, it **SHALL** contain a property named `charOffset` whose value is an integer equal to the zero-based character offset of the first character in the region from the beginning of the artifact. If `charOffset` is absent, it **SHALL** default to -1, which indicates that the value is unknown (not set).

### charLength property

When a `region` object represents a text region specified by offset/length properties, it **MAY** contain a property named `charLength` whose value is a non-negative integer equal to the number of characters in the region.

If `charLength` is absent, it **SHALL** default to 0, which **SHALL** be interpreted as an insertion point at the position specified by `charOffset` ([§3.30.9](#charoffset-property))

The sum of `charOffset` and `charLength` **SHALL** be greater than or equal to 0 and less than or equal to the number of characters in the artifact.

A region whose `charOffset` is equal to the number of characters in the artifact and whose `charLength` is 0 is permitted and **SHALL** represent an insertion point at the end of the artifact.

### byteOffset property

When a `region` object represents a binary region, it **SHALL** contain a property named `byteOffset` whose value is an integer equal to the zero-based byte offset of the first byte in the region from the beginning of the artifact. If `byteOffset` is absent, it **SHALL** default to -1, which indicates that the value is unknown (not set).

### byteLength property

When a `region` object represents a binary region, it **MAY** contain a property named `byteLength` whose value is an integer equal to the number of bytes in the region. If `byteLength` is absent, it **SHALL** default to 0, which **SHALL** be interpreted as an insertion point at the position specified by `byteOffset` ([§3.30.11](#byteoffset-property)).

The sum of `byteOffset` and `byteLength` **SHALL** be greater than or equal to 0 and less than or equal to the number of bytes in the artifact.

A `region` object whose `byteOffset` equals the number of bytes in the artifact and whose `byteLength` is 0 is permitted, and **SHALL** represent an insertion point at the end of the artifact.

### snippet property

A `region` object **MAY** contain a property named `snippet` whose value is an `artifactContent` object ([§3.3](#artifactcontent-object)) representing the portion of the artifact specified by the `region` object.

> NOTE: The `snippet` property has various uses:
>
> - It allows a SARIF viewer to present the contents of the region even if the artifact from which it was taken is not available.
> 
> - It also allows an end user examining a SARIF log file to see the relevant content without opening another file.
> 
> - It can be used to improve result matching.

### message property{#region-object--message-property}

A `region` object **MAY** contain a property named `message` whose value is a `message` object ([§3.11](#message-object)) containing a message relevant to the region.

A SARIF viewer **MAY** display this message when the user interacts with the region. (For example, if the user hovers over the region with the mouse, the viewer might present the message as hover text.)

### sourceLanguage property{#region-object--sourcelanguage-property}

If the `region` object represents a portion of a text artifact that contains source code, it **MAY** contain a property named `sourceLanguage` whose value is a hierarchical string ([§3.5.4](#hierarchical-strings)) that specifies the programming language in which this portion of the source code is written. If the `region` object does not represent a portion of a text artifact containing source code, then `sourceLanguage` **SHALL** be absent.

For the remainder of this section, we assume that the `region` object represents a portion of a text artifact that contains source code.

> NOTE: This property is intended to help SARIF viewers to render code snippets ([§3.30.13](#snippet-property)) with appropriate syntax coloring. It is intended for use in mixed-language files, such as HTML files that contain JavaScript™. For more information about this usage, see [§3.24.10](#artifact-object--sourcelanguage-property).

if `sourceLanguage` is absent, it **SHALL** default to the value of the `sourceLanguage` property ([§3.24.10](#artifact-object--sourcelanguage-property)) of the `artifact` object ([§3.24](#artifact-object)) which describes the artifact that contains the region. `artifact.sourceLanguage` in turn defaults to `theRun.defaultSourceLanguage` ([§3.14.25](#defaultsourcelanguage-property)). If all three of `region.sourceLanguage`, `artifact.sourceLanguage`, and `theRun.defaultSourceLanguage` are absent, the source language of the region object **SHALL** be taken to be unknown. In that case, a SARIF viewer **MAY** use any method or heuristic to determine the region’s source language, for example, by examining the file’s file name extension or MIME type, or by prompting the user.

For conventions and practices regarding the value of this property, see [§3.24.10.2](#source-language-identifier-conventions-and-practices).
