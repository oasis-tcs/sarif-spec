### inlineExternalProperties property

A `sarifLog` object **MAY** contain a property named `inlineExternalProperties` whose value is an array of zero or more unique ([sec](#array-properties-with-unique-values)) `externalProperties` objects ([sec](#externalproperties-object)).

> NOTE: This property allows multiple runs to share large data sets in a single, self-contained log file.

> EXAMPLE 1: In this example, two tools analyze the same set of image files, stored in `sarifLog.inlineExternalProperties[0].artifacts`. The first tool locates the inline `externalProperties` object by means of a URI with the `sarif` scheme (see [sec](#uris-that-use-the-sarif-scheme)). The second tool locates the object by means of its `guid` property ([sec](#externalproperties-object--guid-property)).
>
> ```json
> {
>   "version": "2.2",
>   "$schema": "https://docs.oasis-open.org/sarif/sarif/v2.2/schema/sarif.json",
> 
>   "inlineExternalProperties": [
>     {                                            
>       "guid": "00001111-2222-1111-8888-555566667777", # See (#externalproperties-object--guid-property).
> 
>       "artifacts": [                                  # See (#the-property-value-properties).
>         {
>           "location": {
>             "uri": "apple.png"
>           },
>           "mimeType": "image/png"
>         },
>         {
>           "location": {
>             "uri": "banana.png"
>           },
>           "mimeType": "image/png"
>         }
>       ]
>     }
>   ],
> 
>   "runs": [                                           # See (#runs-property).
>     {                                                 # A run object ((#run-object)).
>       "tool": {                                       # See (#run-object--tool-property).
>         "driver": {
>           "name": "ImageAccessibilityScanner"
>         }
>       },
>       "externalPropertyFileReferences": {             # See (#externalpropertyfilereferences-property).
>         "artifacts": [
>           {
>             "location": {
>               "uri": "sarif:/inlineExternalPropertyFiles/0"
>             }
>           }
>         ]
>       },
>       "results": [
>         ...
>       ]
>     },
>     {
>       "tool": {
>         "driver": {
>           "name": "ImageSuitabilityScanner"
>         }
>       },
>       "externalPropertyFileReferences": {
>         "artifacts": [
>           {
>             "guid": "00001111-2222-1111-8888-555566667777"
>           }
>         ]
>       },
>       "results": [
>         ...
>       ]
>     }
>   ]
> }
> ```
