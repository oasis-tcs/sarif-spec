## physicalLocation object

### General{#physicallocation-object--general}

A `physicalLocation` object represents the physical location where a result was detected. A physical location specifies a reference to an artifact together with a region within that artifact.

### Constraints{#physicallocation-object--constraints}

Either the `artifactLocation` property ([sec](#physicallocation-object--artifactlocation-property)), the `address` property ([sec](#address-property)), or both **SHALL** be present.

If `region.byteLength` ([sec](#region-property), [sec](#bytelength-property)) and `address.length` ([sec](#address-property), [sec](#address-object--length-property)) are both present, then `region.byteLength` **SHALL** equal the absolute value of `address.length`.

### artifactLocation property{#physicallocation-object--artifactlocation-property}

A `physicalLocation` object **MAY** contain a property named `artifactLocation` whose value is an `artifactLocation` object ([sec](#artifactlocation-object)) that represents the location of the artifact. If `artifactLocation` is absent, then `address` ([sec](#address-property)) **SHALL** be present.

### region property

A `physicalLocation` object **MAY** contain a property named `region` whose value is a `region` object ([sec](#region-object)) that represents a relevant portion of the artifact. In particular, if the `physicalLocation` object occurs within the `locations` property ([sec](#result-object--locations-property)) of a `result` object ([sec](#result-object)), the region property **SHALL** specify the region within the artifact where the result was detected.

> EXAMPLE 1: In this example, a `physicalLocation` object specifies the location where a result was detected. Its `region` property specifies the portion of the file where the result was detected.
> 
> ```json
> {                              # A result object (§3.27).
>   "locations": [               # See §3.27.12.
>     {                          # A location object (§3.28).
>       "physicalLocation": {    # See §3.28.3.
>         "artifactLocation": {  # A artifactLocation object.
>           "uri": "ui/window.c",
>           "uriBaseId": "SRCROOT"
>         },
> 
>         "region": {            # The region specifies the portion of the file
>           "startLine": 42      # where the result was detected.
>         }
>       }
>     }
>   ]
> }
> ```

If the `physicalLocation` object specifies a location in a nested artifact, then the `region` property **SHALL** specify the location with respect to the innermost nested artifact.

> EXAMPLE 2: If a result occurs in a C++ file contained in a compressed archive, then the region would represent the line and column number of the result with the C++ file. It would not represent (for example) the offset of the C++ file from the start of the archive.

If the `region` property is absent, the `physicalLocation` object refers to the entire artifact.

### contextRegion property

If a `physicalLocation` object contains a `region` property ([sec](#region-property)), it **MAY** also contain a property named `contextRegion` whose value is a `region` object ([sec](#region-object)) which specifies a region that is a proper superset of the region specified by the `region` property. If `region` is absent, `contextRegion` **SHALL** be absent.

> NOTE: `contextRegion` enables a viewer to provide visual context when displaying a portion of an artifact. It can also be used to improve result matching.

> EXAMPLE In this example, an analysis tool detected a result on line 42. The tool provides additional context for SARIF viewers by specifying a range of content surrounding the result line.
> 
> ```json
> {                                       # A result object (§3.27).
>   "locations": [                        # See §3.27.12.
>     {                                   # A location object (§3.28).
>       "physicalLocation": {             # A physicalLocation object (§3.29).
>         "artifactLocation": {           # An artifactLocation object (§3.4).
>           "uri": "ui/window.c",
>           "uriBaseId": "SRCROOT"
>         },
> 
>         "region": {                      # See §3.29.4.
>           "startLine": 42,
>           "snippet": {
>             "text": "int n = m + 1;"
>           }
>         },
> 
>         "contextRegion": {
>           "startLine": 41,
>           "endLine": 43,
>           "snippet": {
>             "text": "int m;\nint n = m + 1\n\n"
>           }
>         }
>       }
>     }
>   ]
> }
> ```

### address property

A `physicalLocation` object **MAY** contain a property named address whose value is an `address` object ([sec](#address-object)) that represents the physical or virtual address of this location. If `address` is absent, then `artifactLocation` ([sec](#physicallocation-object--artifactlocation-property)) **SHALL** be present.
