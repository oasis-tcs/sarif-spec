## edge object

### General{#edge-object--general}

An `edge` object represents a directed edge in the graph represented by `theGraph`.

### id property{#edge-object--id-property}

An `edge` object **SHALL** contain a property named `id` whose value is a string that uniquely identifies the edge within `theGraph`.

### label property{#edge-object--label-property}

An `edge` object **MAY** contain a property named `label` whose value is a `message` object ([§3.11](#message-object)) that provides a short description of the edge.

### sourceNodeId property

An `edge` object **SHALL** contain a property named `sourceNodeId` whose value is a string that identifies the source node (the node at which the edge starts). It **SHALL** equal the `id` property ([§3.40.2](#node-object--id-property)) of one of the `node` objects ([§3.40](#node-object)) in `theGraph`. It **MAY** equal the id of any node within `theGraph`, regardless of nesting (see [§3.40.5](#children-property)).

> EXAMPLE: In this example, an edge connects two nodes defined in unrelated nested graphs.
> 
> ```json
> {                             # A graph object (§3.39).
>   "nodes": [                  # See §3.39.3.
>     {                         # A node object.
>       "id": "n1",
>       "children": [           # See §3.40.5.
>         {
>           "id": "n3"
>         }
>       ]
>     },
>     {
>       "id": "n2",
>       "children": [
>         {
>           "id": "n4"
>         }
>       ]
>     }
>   ],
>   "edges": [                  # See §3.39.4.
>     {
>       "sourceNodeId": "n3",   # Source node and target node are in separate
>       "targetNodeId": "n4"    # nested graphs: ok.
>     }
>   ],
>   ...
> }
> ```

### targetNodeId property

An `edge` object **SHALL** contain a property named `targetNodeId` whose value is a string that identifies the target node (the node at which the edge ends). It **SHALL** equal the `id` property ([§3.40.2](#node-object--id-property)) of one of the `node` objects ([§3.40](#node-object)) in `theGraph`. It **MAY** equal `sourceNodeId` ([§3.41.4](#sourcenodeid-property)).
