## sarifLog object

### General{#sariflog-object--general}

A `sarifLog` object specifies the version of the file format and contains the output from one or more runs.

> EXAMPLE 1:
>
> ```json
> {
>   "version": "2.1.0", # See (#sariflog-object--version-property).
>   "runs": [           # See (#runs-property).
>     {
>       ...             # A run object ((#run-object)).
>     },
>     ...
>     {
>       ...             # Another run object.
>     }
>   ]
> }
> ```

### version property{#sariflog-object--version-property}

A `sarifLog` object **SHALL** contain a property named `version` whose value is a string designating the version of the SARIF specification to which this log file conforms. This string **SHALL** have the value `"2.1.0"`.

Although the order in which properties appear in a JSON object value is not semantically significant, the `version` property **SHOULD** appear first.

> NOTE: This will make it easier for parsers to handle multiple versions of the SARIF format if new versions are defined in the future.

### \$schema property{#sariflog-object--schema-property}

A `sarifLog` object **MAY** contain a property named `\$schema` whose value is a string containing an absolute URI from which a JSON schema document [cite](#JSCHEMA01) describing the version of the SARIF format to which this log file conforms can be obtained.

If the `\$schema` property is present, the JSON schema obtained from the specified URI **SHALL** describe the version of the SARIF format specified by the `version` property ([sec](#sariflog-object--version-property)).

> NOTE 1: The purpose of the `\$schema` property is to allow JSON schema validation tools to locate an appropriate schema against which to validate the log file. This is useful, for example, for tool authors who wish to ensure that logs produced by their tools conform to the SARIF format.

> NOTE 2: The SARIF schema is available at <https://docs.oasis-open.org/sarif/sarif/v2.1.0/errata01/csd01/schemas/sarif-schema-2.1.0.json>.

### runs property

A `sarifLog` object **SHALL** contain a property named `runs` whose value is either `null` or an array of zero or more `run` objects ([sec](#run-object)).

The value of `runs` **SHALL** be an array with at least one element except in the following circumstances:

- If a SARIF producer finds no data with which to populate `runs`, then its value **SHALL** be an empty array.

    NOTE 1: This would happen if, for example, the log file were the output of a query on a result management system, and the query did not match any runs stored in the result management system.

- If a SARIF producer tries to populate `runs` but fails, then its value **SHALL** be `null`.

    NOTE 2: This would happen if, for example, the log file were the output of a query on a result management system, and the query was malformed.

### inlineExternalProperties property

A `sarifLog` object **MAY** contain a property named `inlineExternalProperties` whose value is an array of zero or more unique ([sec](#array-properties-with-unique-values)) `externalProperties` objects ([sec](#externalproperties-object)).

> NOTE: This property allows multiple runs to share large data sets in a single, self-contained log file.

> EXAMPLE 1: In this example, two tools analyze the same set of image files, stored in `sarifLog.inlineExternalProperties[0].artifacts`. The first tool locates the inline `externalProperties` object by means of a URI with the `sarif` scheme (see [sec](#uris-that-use-the-sarif-scheme)). The second tool locates the object by means of its `guid` property ([sec](#externalproperties-object--guid-property)).
>
> ```json
> {
>   "version": "2.1.0",
>   "$schema": "https://docs.oasis-open.org/sarif/sarif/v2.1.0/errata01/csd01/schemas/sarif-schema-2.1.0.json",
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
