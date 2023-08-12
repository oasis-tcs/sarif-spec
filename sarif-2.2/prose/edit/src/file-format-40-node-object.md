## node object

### General{#node-object--general}

A `node` object represents a node in the graph represented by the containing `graph` object ([sec](#graph-object)), which we refer to as `theGraph`.

### id property{#node-object--id-property}

A `node` object **SHALL** contain a property named `id` whose value is a string that uniquely identifies the node within `theGraph`. `id` **SHALL** be unique among all nodes in `theGraph`, regardless of nesting (see [sec](#children-property)).

> EXAMPLE 1: This graph is invalid because two nodes have the same `id`, even though the nodes are within unrelated nested graphs.
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
>           "id": "n3"          # INVALID: duplicate id.
>         }
>       ]
>     }
>   ],
>   ...
> }
> ```

### label property{#node-object--label-property}

A `node` object **MAY** contain a property named `label` whose value is a `message` object ([sec](#message-object)) that provides a short description of the node.

### location property{#node-object--location-property}

A `node` object **SHOULD** have a property named `location` whose value is a `location` object ([sec](#location-object)) that specifies the location associated with the node.

### children property

A `node` object **MAY** contain a property named `children` whose value is an array of zero or more unique ([sec](#array-properties-with-unique-values)) `node` objects, referred to as "child nodes."

Child nodes are logically subordinate to their containing node, and form a "nested graph" within that node.
