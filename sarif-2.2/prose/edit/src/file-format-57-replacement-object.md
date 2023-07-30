## replacement object

### General{#replacement-object--general}

A `replacement` object represents the replacement of a single region of an artifact. If the region’s length is zero, it represents an insertion point.

If a replacement object specifies both the removal of a region by means of the `deletedRegion` property ([§3.57.3](#deletedregion-property)) and the insertion of new content by means of the `insertedContent` property ([§3.57.4](#insertedcontent-property)), then the effect of the replacement **SHALL** be as if the removal were performed before the insertion.

If a single `artifactChange` object ([§3.56](#artifactchange-object)) specifies more than one replacement, then the effect of the replacements **SHALL** be as if they were performed in the order they appear in the `replacements` array ([§3.56.3](#replacements-property)). The `deletedRegion` property of each `replacement` object **SHALL** specify the location of the replacement in the unmodified artifact.

> EXAMPLE 1: Suppose an `artifactChange` object contains a `replacements` property whose value is the following array of `replacement` objects:
> 
> ```json
> "artifactChanges": [
>   {
>     "deletedRegion": {
>       "byteOffset": 12,
>       "byteLength": 5
>     },
>     "insertedContent": {
>       "binary": "ZXhhbXBsZQ=="
>     }
>   },
>   {
>     "deletedRegion": {
>       "byteOffset": 20,
>       "byteLength": 3
>     }
>   },
>   {
>     "deletedRegion": {
>       "byteOffset": 312,
>       "byteLength": 0
>     },
>     "insertedContent": {
>       "binary": "ZXhhbXBsZQ=="
>     }
>   }
> ]
> ```
> 
> The first `replacement` object removes 5 bytes starting at offset 12; that is, it removes bytes 12–16. Then it inserts the 7 bytes specified by the MIME Base64-encoded string in the `insertedContent.binary` property at the same offset.
> 
> The second `replacement` object removes 3 bytes starting at offset 20 *with respect to the unmodified file*. Since 5 bytes were removed and 7 bytes inserted *before* byte 20, the 3 bytes removed actually start at byte 22 of the contents after the first change. Since the `insertedContent` property is absent, no content is inserted in place of the deleted bytes.
> 
> In the third `replacement` object, the length of the region specified by the `deletedRegion` property is zero, so the region represents an insertion point. The 7 bytes specified by the `insertedContent.binary` property are inserted at offset 312 with respect to the unmodified artifact.

A `replacement` object can represent either a textual replacement or a binary replacement, depending on whether the `deletedRegion` property ([§3.57.3](#deletedregion-property)) specifies a text region ([§3.30.2](#text-regions)) or a binary region ([§3.30.3](#binary-regions)).

> EXAMPLE 2: In this example, the `replacements` property specifies a replacement in a text file.
> 
> ```json
> "replacements": [
>   {
>     "deletedRegion": { # The region object represents a text region (§3.30.2).
>       "startLine": 12,
>       "startColumn": 5,
>       "endColumn": 9
>     },
>     "insertedContent": {
>       "text": "example" # The insertedContent property contains a text
>     }                   # property instead of a binary property.
>   }
> ]
> ```

When performing a replacement in a text artifact, the SARIF producer **SHOULD** specify a text replacement rather than a binary replacement. This allows the SARIF producer to specify the region without regard to whether the artifact starts with a byte order mark (BOM).

### Constraints{#replacement-object--constraints}

If the `deletedRegion` property ([§3.57.3](#deletedregion-property)) specifies a text region ([§3.30.2](#text-regions)) and the `insertedContent` property ([§3.57.4](#insertedcontent-property)) is present, then the `insertedContent` property **SHOULD** contain a `text` property ([§3.3.2](#artifactcontent-object--text-property)).

If the `deletedRegion` property specifies a binary region ([§3.30.3](#binary-regions)) and the `insertedContent` property is present, then the `insertedContent` property **SHALL** contain a `binary` property ([§3.3.3](#binary-property)).

Although it is possible to construct a `replacement` object that neither removes nor adds any content, a `replacement` object **SHOULD** have a material effect on the target artifact, either because `deletedRegion` denotes a non-empty region to delete, or because `insertedContent` specifies non-empty content to insert, or both.

### deletedRegion property

A `replacement` object **SHALL** contain a property named `deletedRegion` whose value is a `region` object ([§3.30](#region-object)) specifying the region to delete.

If the length of the region specified by `deletedRegion` is zero, then `deletedRegion` specifies an insertion point, and the SARIF consumer performing the replacement **SHALL NOT** remove any content.

### insertedContent property

A `replacement` object **MAY** contain a property named `insertedContent` whose value is an `artifactContent` object ([§3.3](#artifactcontent-object)) that specifies the content to insert in place of the region specified by the `deletedRegion` property (or at the point specified by `deletedRegion`, if `deletedRegion` has a length of zero and therefore specifies an insertion point).

If the inserted content is specified as text, the text **SHALL** be transcoded from UTF-8 (the encoding of all text in all SARIF log files) to the encoding of the target artifact before being inserted.

> NOTE: This implies that a text fix cannot be safely applied unless the target artifact’s encoding is known.

If `insertedContent` is absent or its properties specify content whose length is zero, the SARIF consumer performing the replacement **SHALL NOT** insert any content.
