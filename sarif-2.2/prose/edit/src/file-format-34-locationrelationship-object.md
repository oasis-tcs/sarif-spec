## locationRelationship object

### General{#locationrelationship-object--general}

A `locationRelationship` object specifies one or more directed relationships from one `location` object ([sec](#location-object)), which we refer to as `theSource`, to another one, which we refer to as `theTarget`.

`locationRelationship` objects appear as elements of the `location.relationships` array ([sec](#location-object--relationships-property)). The `location` object containing this property is `theSource`.

> EXAMPLE 1: In this example, the location relationships specify that the file f.h in which the result was found is included by g.h, which is in turn included by g.c. Depending on the circumstances, it might or might not be useful to include both the `"includes"` and `"isIncludedBy"` relationships, as this example does for g.h.
> 
> ```json
> {                                        # A result object (§3.27).
>   "locations": [                         # See §3.27.12.
>     {                                    # A location object (§3.28).
>       "id": 0,                           # See §3.28.2.
>       "physicalLocation": {
>         "artifactLocation": {
>           "uri": "f.h"
>         },
>         "region": {
>           "startLine": 42
>         }
>       },
>       "relationships": [                 # See §3.28.7
>         {                                # A locationRelationship object.
>           "target": 1,                   # See §3.34.2.
>           "kinds": [ "isIncludedBy" ]    # See §3.34.3.
>         }
>       ]
>     }
>   ],
> 
>   "relatedLocations": [                  # See §3.27.22.
>     {
>       "id": 1,
>       "physicalLocation": {
>         "artifactLocation": {
>           "uri": "g.h"
>         },
>         "region": {
>           "startLine": 17                # The line that includes f.h.
>         }
>       },
>       "relationships": [
>         {
>           "target": 0,
>           "kinds": [ "includes" ]
>         },
>         {
>           "target": 2,
>           "kinds": [ "isIncludedBy" ]
>         }
>       ]
>     },
>     {
>       "id": 2
>       "physicalLocation": {
>         "artifactLocation": {
>           "uri": "g.c"
>         },
>         "region": {
>           "startLine": 8                 # The line that includes g.h.
>         }
>       },
>       "relationships": [
>         {
>           "target": 1,
>           "kinds": [ "includes" ]
>         }
>       ]
>     }
>   ]
> }
> ```

### target property{#locationrelationship-object--target-property}

A `locationRelationship` object **SHALL** contain a property named `target` whose value is a non-negative integer which identifies `theTarget` (see [sec](#locationrelationship-object--general)) among all `location` objects ([sec](#location-object)) in `theResult` by virtue of being equal to `theTarget.id` ([sec](#location-object--id-property)).

> NOTE: Negative values are forbidden because their use might suggest some non-obvious semantic difference between positive and negative values.

### kinds property{#locationrelationship-object--kinds-property}

A `locationRelationship` object **MAY** contain a property named `kinds` whose value is an array of one or more unique ([sec](#array-properties-with-unique-values)) strings each of which specifies a relationship between `theSource` and `theTarget` (see [sec](#locationrelationship-object--general)). If `kinds` is absent, it **SHALL** default to `[ "relevant" ]` (see below for the meaning of `"relevant"`).

When possible, SARIF producers **SHOULD** use the following values, with the specified meanings.

- `"includes"`: The artifact identified by `theSource` includes the artifact identified by `theTarget`.

- `"isIncludedBy"`: The artifact identified by `theSource` is included by the artifact identified by `theTarget`.

- `"relevant"`: `theTarget` is relevant to `theSource` in a way not covered by other relationship kinds.

If none of these values are appropriate, a SARIF producer **MAY** use any value.

> NOTE: Although `"relevant"` is a catch-all for any relationship not described by the other values, a producer might still wish to define its own more specific values.

In particular, the values defined for `logicalLocation.kind` ([sec](#logicallocation-object--kind-property)) and `threadFlowLocation.kinds` ([sec](#threadflowlocation-object--kinds-property)) might prove useful.

### description property{#locationrelationship-object--description-property}

A `locationRelationship` object **MAY** contain a property named `description` whose value is a `message` object ([sec](#message-object)) that describes the relationship.
