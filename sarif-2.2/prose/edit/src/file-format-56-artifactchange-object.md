## artifactChange object

### General{#artifactchange-object--general}

An `artifactChange` object represents a change to a single artifact.

> EXAMPLE 1:
> 
> ```json
> {                             # A fix object (§3.55).
>   "artifactChanges": [        # See §3.55.3.
>     {                          
>       "artifactLocation": {   # See §3.56.2.
>         "uri": "a.h"
>       },
>       "replacements": [       # See §3.56.3.
>         {                     # A replacement object (§3.57).
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

### artifactLocation property{#artifactchange-object--artifactlocation-property}

An `artifactChange` object **SHALL** contain a property named `artifactLocation` whose value is an `artifactLocation` object ([sec](#artifactlocation-object)) that represents the location of the artifact.

### replacements property

An `artifactChange` object **SHALL** contain a property named `replacements` whose value is an array of one or more `replacement` objects ([sec](#replacement-object)) each of which represents the replacement of a single region of the artifact specified by the `artifactLocation` property ([sec](#artifactchange-object--artifactlocation-property)).
