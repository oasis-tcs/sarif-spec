## `artifactContent` Object

### General{#artifactcontent-object--general}

Certain properties in this document represent the contents of portions of artifacts external to the log file, for example, artifacts that were scanned by an analysis tool. SARIF represents such content with an `artifactContent` object. Depending on the circumstances, the SARIF log file might need to represent this content as readable text, raw bytes, or both.

### `text` Property{#artifactcontent-object--text-property}

If the external artifact is a text artifact, an `artifactContent` object **SHOULD** contain a property named `text` whose value is a string containing the relevant text. Since SARIF log files are encoded in UTF-8 ([cite](#RFC3629); see [sec](#file-format--general)), this means that if the external artifact is a text artifact in any encoding other than UTF-8, the SARIF producer **SHALL** transcode the text to UTF-8 before assigning it to the `text` property. The SARIF producer **SHALL** escape any characters that JSON [cite](#RFC8259) requires to be escaped.

Notwithstanding any necessary transcoding and escaping, the SARIF producer **SHALL** preserve the text artifact’s line breaking convention (for example, `"\n"` or `"\r\n"`).

If the external artifact is a binary artifact, the `text` property **SHALL** be absent.

### `binary` Property

If the external artifact is a binary artifact, or if the SARIF producer cannot determine whether the external artifact is a text artifact or a binary artifact, an `artifactContent` object **SHALL** contain a property named `binary` whose value is a string containing the MIME Base64 encoding [cite](#RFC2045) of the bytes in the relevant portion of the artifact.

If the external artifact is a text artifact in an encoding other than UTF-8, the `binary` property **MAY** be present, in which case it **SHALL** contain the MIME Base64 encoding of the bytes representing the relevant text in its original encoding.

If the external artifact is a UTF-8 text artifact, the `binary` property **SHOULD** be absent. If it is present, it **SHALL** contain the MIME Base64 encoding of the UTF-8 bytes representing the relevant text.

### `rendered` Property

An `artifactContent` object **MAY** contain a property named `rendered` whose value is a `multiformatMessageString` object ([sec](#multiformatmessagestring-object)) that provides a rendered view of the contents.

> EXAMPLE 1: In this example, a `physicalLocation` object ([sec](#physicallocation-object)) denotes a memory address. Its `region.snippet.rendered` property ([sec](#region-property), [sec](#snippet-property)) offers a hex view of the relevant address range. The `markdown` property ([sec](#multiformatmessagestring-object--markdown-property)) emphasizes a byte of particular interest.
>
> ```json
> {                                # A physicalLocation object ((#physicallocation-object)).
>   "address": {                   # See (#address-property).
>     "baseAddress": 4202880,      # See (#absoluteaddress-property).
>     "offset": 64                 # See (#offsetfromparent-property).
>   },
> 
>   "region": {                    # See (#region-property).
>     "snippet": {                 # An artifactContent object. See (#snippet-property).
>       "rendered": {              # A multiformatMessageString object ((#multiformatmessagestring-object)).
>         "text": "00 00 01 00 00 00 00 00",
>         "markdown": "00 00 **01** 00 00 00 00 00"
>       }
>     }
>   }
> }
> ```
