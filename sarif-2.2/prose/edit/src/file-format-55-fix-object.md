## fix object

### General{#fix-object--general}

A `fix` object represents a proposed fix for the problem indicated by `theResult`. It specifies a set of artifacts to modify. For each artifact, it specifies regions to remove, and provides new content to insert.

> EXAMPLE 1:
>
> ```json
> {                                   # A result object ((#result-object)).
>   "fixes": [                        # See (#fixes-property).
>     {                               # A fix object.
>       "description": {              # See (#fix-object--description-property).
>         "text": "Private member names begin with '_'"
>       },
>       "artifactChanges": [          # See (#artifactchanges-property).
>         {                           # An artifactChange object ((#artifactchange-object)).
>           ...
>         }
>       ]
>     }
>   ],
>   ...
> }
> ```

### description property{#fix-object--description-property}

A `fix` object **SHOULD** contain a property named `description` whose value is a `message` object ([sec](#message-object)) that describes the proposed fix.

> NOTE: The purpose of the `description` property is to enable a SARIF viewer to present the proposed fix to the end user.

> EXAMPLE 1:
>
> ```json
> "fix": {
>   "description": {
>     "text": "Combine declaration and initialization of variable 'x'."
>   },
>   ...
> }
> ```

### artifactChanges property

A `fix` object **SHALL** contain a property named `artifactChanges` whose value is an array of one or more unique ([sec](#array-properties-with-unique-values)) `artifactChange` objects ([sec](#artifactchange-object)) each of which describes the changes to a single artifact that are necessary to effect the fix.

> NOTE: `artifactChanges` is an array because a fix might require changes to multiple artifacts.

The array elements **SHALL** refer to distinct artifacts.

> EXAMPLE 1: In this example, two `artifactChange` objects make identical changes (commenting out the first line) in two distinct C-language files, `src/a.c` and `src/b.c`.
>
> ```json
> {                                    # A fix object.
>   "artifactChanges": [                   
>     {                                # An artifactChange object ((#artifactchange-object)).
>       "artifactLocation": {          # See (#artifactchange-object--artifactlocation-property).
>         "uri": "src/a.c"
>       },
>       "replacements": [              # See (#replacements-property).
>         {                            # A replacement object ((#replacement-object)).
>           "deletedRegion": {         # See (#deletedregion-property).
>             "startLine": 1,
>             "startColumn": 1,
>             "endColumn": 1
>           },
>           "insertedContent": {       # See (#insertedcontent-property).
>             "text": "// "
>           }
>         }
>       ]
>     },
>     {
>       "artifactLocation": {
>         "uri": "src/b.c"
>       },
>       "replacements": [
>         {
>           "deletedRegion": {
>             "startLine": 1,
>             "startColumn": 1,
>             "endColumn": 1
>           },
>           "insertedContent": {
>             "text": "// "
>           }
>         }
>       ]
>     }
>   ]
> }
> ```

> EXAMPLE 2: This example represents invalid SARIF because the two `artifactChange` objects refer to the same file, `src/a.c`. It is invalid even though the `artifactChange` objects are distinguished by their `replacements` properties.
>
> ```json
> {                                    # A fix object.
>   "artifactChanges": [                   
>     {                                # An artifactChange object ((#artifactchange-object)).
>       "artifactLocation": {          # See (#artifactchange-object--artifactlocation-property).
>         "uri": "src/a.c"
>       },
>       "replacements": [              # See (#replacements-property).
>         {                            # A replacement object ((#replacement-object)).
>           "deletedRegion": {         # See (#deletedregion-property).
>             "startLine": 1,
>             "startColumn": 1,
>             "endColumn": 1
>           },
>           "insertedContent": {       # See (#insertedcontent-property).
>             "text": "// "
>           }
>         }
>       ]
>     },
>     {
>       "artifactLocation": {
>         "uri": "src/a.c"             # Invalid: refers to the same file.
>       },
>       "replacements": [
>         {
>           "deletedRegion": {
>             "startLine": 2,          # Invalid even though it affects a
>             "startColumn": 1,        #  different line.
>             "endColumn": 1
>           },
>           "insertedContent": {
>             "text": "// "
>           }
>         }
>       ]
>     }
>   ]
> }
> ```
