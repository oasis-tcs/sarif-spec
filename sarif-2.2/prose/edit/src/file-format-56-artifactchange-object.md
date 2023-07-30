## artifactChange object

### General{#artifactchange-object--general}

An `artifactChange` object represents a change to a single artifact.

> EXAMPLE:
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

An `artifactChange` object **SHALL** contain a property named `artifactLocation` whose value is an `artifactLocation` object ([§3.4](#artifactlocation-object)) that represents the location of the artifact.

### replacements property

An `artifactChange` object **SHALL** contain a property named `replacements` whose value is an array of one or more `replacement` objects ([§3.57](#replacement-object)) each of which represents the replacement of a single region of the artifact specified by the `artifactLocation` property ([§3.56.2](#artifactchange-object--artifactlocation-property)).
