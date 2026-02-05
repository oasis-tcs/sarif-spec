## `artifactChange` Object

### General{#artifactchange-object--general}

An `artifactChange` object represents a change to a single artifact.

> EXAMPLE 1:
>
> ```json
> {                             # A fix object ((#fix-object)).
>   "artifactChanges": [        # See (#artifactchanges-property).
>     {                          
>       "artifactLocation": {   # See (#artifactchange-object--artifactlocation-property).
>         "uri": "a.h"
>       },
>       "replacements": [       # See (#replacements-property).
>         {                     # A replacement object ((#replacement-object)).
>           ...
>         },
>         {                     # Another replacement object.
>           ...
>         }
>       ]
>     }
>   ]
> }
> ```

### `artifactLocation` Property{#artifactchange-object--artifactlocation-property}

An `artifactChange` object **SHALL** contain a property named `artifactLocation` whose value is an `artifactLocation` object ([sec](#artifactlocation-object)) that represents the location of the artifact.

### `replacements` Property

An `artifactChange` object **SHALL** contain a property named `replacements` whose value is an array of one or more `replacement` objects ([sec](#replacement-object)) each of which represents the replacement of a single region of the artifact specified by the `artifactLocation` property ([sec](#artifactchange-object--artifactlocation-property)).
