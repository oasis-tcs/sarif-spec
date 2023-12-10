## Property bags

### General{#property-bags--general}

Certain properties in this document are defined to be "property bags". A property bag is an object ([sec](#object-properties)) containing an unordered set of properties with arbitrary names.

The property names are hierarchical strings ([sec](#hierarchical-strings)). The components of the property names **SHOULD** be camelCase strings, but see [sec](#normative-production-of-sarif-by-converters) for exceptions.

The property values **MAY** be of any JSON type, including strings, numbers, arrays, objects, Booleans, and null. If a property value is a string, it **MAY** be an empty string.

In addition to those properties that are explicitly documented, every object defined in this document **MAY** contain a property named `properties` whose value is a property bag. This allows SARIF producers to include information about each object that is not explicitly specified in the SARIF format.

### Tags

#### General{#tags--general}

If a property bag contains a property named `tags`, the property value **SHALL** be an array of zero or more unique ([sec](#array-properties-with-unique-values)), hierarchical ([sec](#hierarchical-strings)) strings. Two strings **SHALL** be considered the same if they consist of the same sequence of Unicode [cite](#UNICODE12) code points.

Tags **SHOULD NOT** be used to label a result or a rule as belonging to a category in a classification system such as the Common Weakness Enumeration [cite](#CWE) (for example, by adding a tag `"CWE/622"`). Instead, taxonomies ([sec](#taxonomies)) **SHOULD** be used for this purpose.

Even when defining a custom classification system used within an engineering team, taxonomies **SHOULD** be used rather than tags when labeling a result or a rule.

> EXAMPLE 1: Rather than adding the tag `"shipBlocking"` to a result, consider defining a taxonomy such as "Shipping Impact". This enables metadata such as a description and a help URI to be associated with each taxonomic category.

> EXAMPLE 2: In this example, the SARIF producer tags an artifact with the string `"openSource"`.
>
> ```json
> {                              # A run object ((#run-object)).
>   "artifacts": [               # See (#artifacts-property).
>     {                          # An artifact object ((#artifact-object)).
>       "location": {            # See (#artifact-object--location-property).
>         "uri": "http://www.example.com/libraries/jsonParser.js"
>       },
>       "properties": {
>         "tags": [
>           "openSource"
>         ]
>       }
>     }
>   ],
>   ...
> }
> ```

> NOTE: Anything a tag expresses can also be expressed with a named property bag entry, for example `"openSource": true`, but a tag is more concise.

#### Tag metadata

A SARIF log file **MAY** provide additional information about any tag value by including a property whose name is the same as that tag value and whose value is any JSON value. If present, this property **SHALL** be located by searching first in the property bag that contains the tag, and then in the property bag of the containing `run` object ([sec](#run-object)) `theRun`, if any.

> EXAMPLE 1: Continuing the example from [sec](#tags--general), suppose the tool wishes to provide additional information about using open source code. It might provide that information within the property bag containing the tag (the property bag belonging to the `artifact` object):
>
> ```json
> {                              # An artifact object ((#artifact-object)).
>   "location": {
>     "uri": "http://www.example.com/libraries/jsonParser.js"
>   },
>   "properties": {
>     "tags": [
>       "openSource"
>     ],
>     "openSource": {
>       "informationUri":
>         "http://www.example.com/procedures/usingOpenSource.html"
>     }
>   }
> }
> ```

> EXAMPLE 2: There might be several open source files. To avoid duplicating information, the tool might choose to place the tag metadata in the property bag belonging to `theRun`:
>
> ```json
> {                              # A run object ((#run-object)).
>   "artifacts": [
>     {                          # An artifact object ((#artifact-object)).
>       "location": {
>         "uri": "http://www.example.com/libraries/jsonParser.js"
>       },
>       "properties": {
>         "tags": [
>           "openSource"
>         ]
>       }
>     },
>     ...
>   ],
>   ...
>   "properties": {              # The property bag of the containing run.
>     "openSource": {
>       "informationUri":
>         "http://www.example.com/procedures/usingOpenSource.html"
>     }
>   }
> }
> ```
