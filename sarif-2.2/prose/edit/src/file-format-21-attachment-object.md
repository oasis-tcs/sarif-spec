## attachment object

### General{#attachment-object--general}

An `attachment` object describes an artifact relevant to the detection of a result (see [sec](#attachments-property)).

A SARIF producer **MAY** embed the contents of an attachment in the log file by mentioning the attachment in `theRun.artifacts` ([sec](#artifacts-property)) and providing a value for `artifact.contents` ([sec](#artifact-object--contents-property)).

> EXAMPLE: In this example, `image001.png` is a screen shot of the program being analyzed at the point where the result was detected. Note that this example is more appropriate to a dynamic analysis tool than to a static analysis tool.
> 
> ```json
> {                                             # A result object (§3.27).
>   ...
>   "attachments": [                            # See §3.27.26.
>     {                                         # An attachment object.
>       "description": {                        # See §3.21.2.
>         "text": "Screen shot"
>       },
>       "location": {                           # See §3.21.3.
>         "uri": "file:///C:/ScanOutput/image001.png"
>       }
>     }
>   ]
> }
> ```

### description property{#attachment-object--description-property}

An `attachment` object **SHOULD** contain a property named `description` whose value is a `message` object ([sec](#message-object)) describing the role played by the attachment.

### location property{#attachment-object--location-property}

An `attachment` object **SHALL** contain a property named `location` whose value is an `artifactLocation` object ([sec](#artifactlocation-object)) that specifies the location of the attachment.

### regions property

An `attachment` object **MAY** contain a property named `regions` whose value is an array of zero or more unique ([sec](#array-properties-with-unique-values)) `region` objects ([sec](#region-object)) each of which **SHALL** specify a region of interest within the attachment, and **SHOULD** contain a `message` property ([sec](#region-object--message-property)) so a user can understand its relevance.

### rectangles property

An `attachment` object **MAY** contain a property named `rectangles` whose value is an array of zero or more unique ([sec](#array-properties-with-unique-values)) `rectangle` objects ([sec](#rectangle-object)). If the attachment is an image (for example `.png` or `.svg`), each `rectangle` object **SHALL** specify an area of interest within the image, and **SHOULD** contain a `message` property ([sec](#rectangle-object--message-property)) so a user can understand its relevance.

If the attachment is not an image, and `rectangles` is present, its value **SHALL** be an empty array.
