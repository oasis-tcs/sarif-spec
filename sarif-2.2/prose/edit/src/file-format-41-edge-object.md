## edge object

### General{#edge-object--general}

An `edge` object represents a directed edge in the graph represented by `theGraph`.

### id property{#edge-object--id-property}

An `edge` object **SHALL** contain a property named `id` whose value is a string that uniquely identifies the edge within `theGraph`.

### label property{#edge-object--label-property}

An `edge` object **MAY** contain a property named `label` whose value is a `message` object ([sec](#message-object)) that provides a short description of the edge.

### sourceNodeId property

An `edge` object **SHALL** contain a property named `sourceNodeId` whose value is a string that identifies the source node (the node at which the edge starts). It **SHALL** equal the `id` property ([sec](#node-object--id-property)) of one of the `node` objects ([sec](#node-object)) in `theGraph`. It **MAY** equal the id of any node within `theGraph`, regardless of nesting (see [sec](#children-property)).

> EXAMPLE 1: In this example, an edge connects two nodes defined in unrelated nested graphs.
>
> ```json
> {                             # A graph object ((#graph-object)).
>   "nodes": [                  # See (#nodes-property).
>     {                         # A node object.
>       "id": "n1",
>       "children": [           # See (#children-property).
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
>   "edges": [                  # See (#edges-property).
>     {
>       "sourceNodeId": "n3",   # Source node and target node are in separate
>       "targetNodeId": "n4"    # nested graphs: ok.
>     }
>   ],
>   ...
> }
> ```

### targetNodeId property

An `edge` object **SHALL** contain a property named `targetNodeId` whose value is a string that identifies the target node (the node at which the edge ends). It **SHALL** equal the `id` property ([sec](#node-object--id-property)) of one of the `node` objects ([sec](#node-object)) in `theGraph`. It **MAY** equal `sourceNodeId` ([sec](#sourcenodeid-property)).
