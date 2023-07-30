## reportingDescriptorRelationship object

### General{#reportingdescriptorrelationship-object--general}

A `reportingDescriptorRelationship` object specifies one or more directed relationships from one `reportingDescriptor` object ([§3.49](#reportingdescriptor-object)), which we refer to as `theSource`, to another one, which we refer to as `theTarget`.

`reportingDescriptorRelationship` objects appear as elements of the `reportingDescriptor.relationships` array ([§3.49.15](#reportingdescriptor-object--relationships-property)). The `reportingDescriptor` object containing this property is `theSource`.

`reportingDescriptorRelationship` objects are useful in various scenarios:

1.  In relating analysis rules to taxonomic categories ("taxa"; see [§3.19.3](#taxonomies)).

> EXAMPLE 1: In this example, the definition of rule `CA1000` states that every result that violates this rule falls into the taxonomic category ("taxon") specified by ID 327 of the Common Weakness Enumeration \[[CWE](#CWE)™\]:
> 
> ```json
> {                              # A run object (§3.14).
>   "tool": {                    # See §3.14.6.
>     "driver": {                # See §3.18.2.
>       "name": "CodeScanner",
>       "rules": [               # See §3.19.23.
>         {                      # A reportingDescriptor object (§3.49).
>           "id": "CA1000",
>           "relationships": [
>             {                  # A reportingDescriptorRelationship object.
>               "target": {      # See §3.53.2.
>                 "id": "327",
>                 "guid": "33333333-0000-1111-8888-111111111111",
>                 "toolComponent": {
>                   "name": "CWE",
>                   "guid": "33333333-0000-1111-8888-000000000000",
>                 }
>               },
>               "kinds": [
>                 "superset"
>               ]
>             }
>           ]
>         }
>       ]
>     }
>   },
> 
>   "taxonomies": [
>     {
>       "name": "CWE",
>       "guid": "33333333-0000-1111-8888-000000000000",
>       ...
>       "taxa": [
>         {
>           "id": "327",
>           "guid": "33333333-0000-1111-8888-111111111111",
>           "name": "BrokenOrRiskyCryptographicAlgorithm",
>           ...
>         },
>         ...
>       ]
>     }
>   ],
> 
>   ...
> }
> ```

2.  In relating one analysis rule to another.

> EXAMPLE 2: In this example, the definition of rule `CA1000` states that every violation of this rule will lead to a violation of rule `CA2000`.
> 
> ```json
> {                              # A run object (§3.14).
>   "tool": {                    # See §3.14.6.
>     "driver": {                # See §3.18.2.
>       "name": "CodeScanner",
>       "rules": [               # See §3.19.23.
>         {                      # A reportingDescriptor object (§3.49).
>           "id": "CA1000",
>           "guid": "11111111-0000-1111-8888-000000000001"
>           "relationships": [
>             {                  # A reportingDescriptor object.
>               "target": {      # See §3.53.2.
>                 "id": "CA2000",
>                 "guid": "11111111-0000-1111-8888-000000000002",
>               },
>               "kinds": [
>                 "willFollow"
>               ]
>             }
>           ]
>         },
>         {
>           "id": "CA2000",
>           "guid": "11111111-0000-1111-8888-000000000002"
>           ...
>         }
>       ]
>     }
>   },
>   ...
> ```

### target property{#reportingdescriptorrelationship-object--target-property}

A `reportingDescriptorRelationship` object **SHALL** contain a property named `target` whose value is a `reportingDescriptorReference` object which identifies `theTarget` (see [§3.53.1](#reportingdescriptorrelationship-object--general)).

### kinds property{#reportingdescriptorrelationship-object--kinds-property}

A `reportingDescriptorRelationship` object **MAY** contain a property named `kinds` whose value is an array of one or more unique ([§3.7.3](#array-properties-with-unique-values)) strings each of which specifies a relationship between `theSource` and `theTarget` (see [§3.53.1](#reportingdescriptorrelationship-object--general)). If `kinds` is absent, it **SHALL** default to `[ "relevant" ]` (see below for the meaning of `"relevant"`).

When possible, SARIF producers **SHOULD** use the following values, with the specified meanings.

- `"equal"`: `theTarget` identifies essentially the same set of items as does `theSource` (for example, a taxonomic category that identifies the same set of results as this rule).

- `"superset"`: `theTarget` identifies a superset of the items identified by `theSource` (for example, a taxonomic category that identifies a superset of the results identified by this rule).

- `"subset"`: `theTarget` identifies a subset of the items identified by `theSource` (for example, a taxonomic category that identifies a subset of the results identified by this rule)

- `"disjoint"`: The sets of items identified by `theTarget` does not intersect with the set of items identified by `theSource`.

- `"incomparable"`: The sets of items identified by `theTarget` intersects with the set of items identified by `theSource` but is neither a superset nor a subset.

- `"canFollow"`: Items identified by `theTarget` can be caused by, or occur downstream of, items identified by `theSource`.

- `"canPrecede"`: Items identified by `theSource` can be caused by, or occur downstream of, items identified by `theTarget`.

- `"willFollow"`: Items identified by `theTarget` will be caused by, or occur downstream of, items identified by `theSource`.

- `"willPrecede"`: Items identified by `theSource` will be caused by, or occur downstream of, items identified by `theTarget`.

- `"relevant"`: `theTarget` is relevant to `theSource` in a way not covered by other relationship kinds.

If none of these values are appropriate, a SARIF producer **MAY** use any value.

> NOTE 1: Although `"relevant"` is a catch-all for any relationship not described by the other values, a producer might still wish to define its own more specific values.

> NOTE 2: The values `"equal"` and `"superset"` are special in that they allow certain elements of `result.taxa` ([§3.27.8](#result-object--taxa-property)) to be elided. See [§3.27.8](#result-object--taxa-property), paragraph 2, for more information on this point.

### description property{#reportingdescriptorrelationship-object--description-property}

A `reportingDescriptorRelationship` object **MAY** contain a property named `description` whose value is a `message` object ([§3.11](#message-object)) that describes the relationship.
