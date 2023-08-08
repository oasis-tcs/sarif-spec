## graphTraversal object

### General{#graphtraversal-object--general}

A `graphTraversal` object represents a "graph traversal," that is, a path through a graph specified by a sequence of connected "edge traversals," each of which is represented by an `edgeTraversal` object ([sec](#edgetraversal-object)). For an example, see [sec](#edgetraversals-property).

### Constraints{#graphtraversal-object--constraints}

Exactly one of the `resultGraphIndex` property ([sec](#resultgraphindex-property)) and the `runGraphIndex` property ([sec](#rungraphindex-property)) **SHALL** be present.

### resultGraphIndex property

If a `graphTraversal` object represents the traversal of a `graph` object ([sec](#graph-object)) that resides in `theResult.graphs` ([sec](#result-object--graphs-property)), the `graphTraversal` object **SHALL** contain a property named `resultGraphIndex` whose value is the array index ([sec](#array-indices)) within `theResult.graphs` of that `graph` object.

### runGraphIndex property

If a `graphTraversal` object represents the traversal of a `graph` object ([sec](#graph-object)) that resides in `theRun.graphs` ([sec](#run-object--graphs-property)), the `graphTraversal` object **SHALL** contain a property named `runGraphIndex` whose value is the array index ([sec](#array-indices)) within `theRun.graphs` of that `graph` object.

### description property{#graphtraversal-object--description-property}

A `graphTraversal` object **MAY** contain a property named `description` whose value is a `message` object ([sec](#message-object)) that describes the graph traversal.

### initialState property{#graphtraversal-object--initialstate-property}

A `graphTraversal` object **MAY** contain a property named `initialState` whose value is an object ([sec](#object-properties)) each of whose properties is a `multiformatMessageString` object ([sec](#multiformatmessagestring-object)) that represents the value of a relevant item at the point of entry to the graph. This property, together with `edgeTraversal.finalState` ([sec](#finalstate-property)), enables a SARIF viewer to present a debugger-like "watch window" experience as the user traverses a graph.

This property **SHOULD NOT** include items whose value remains constant throughout the traversal. Such items **SHOULD** be stored in the `immutableState` property ([sec](#graphtraversal-object--immutablestate-property)).

For details of how properties within a "state" object are represented, see EXAMPLE 1 in [sec](#state-property).

### immutableState property{#graphtraversal-object--immutablestate-property}

A `graphTraversal` object **MAY** contain a property named `immutableState` whose value is an object ([sec](#object-properties)) each of whose properties is a `multiformatMessageString` object ([sec](#multiformatmessagestring-object)) that represents the value of a relevant item that remains constant throughout the traversal.

> EXAMPLE 1: In this example, `immutableState` holds the value of a global variable that remains constant throughout the traversal.
> 
> ```json
> {                                          # A graphTraversal object.
>   "immutableState": {
>     "MaxFiles": {
>       "text": "1000"
>     }
>   }
> }
> ```

### edgeTraversals property

A `graphTraversal` object **MAY** contain a property named `edgeTraversals` whose value is an array of zero or more `edgeTraversal` objects ([sec](#edgetraversal-object)) which together represent the sequence of edges traversed during this graph traversal.

The `edgeTraversal` objects **SHALL** be connected end to end; that is, the target node of every traversed edge except the last **SHALL** equal the source node of the next edge.

> EXAMPLE 1: In this example, the `graphTraversal` contains two `edgeTraversal` objects. The id of the first traversed edge is `"e1"`, which connects node `"n1"` to node `"n2"`. The id of the second traversed edge is `"e3"`, which connects node `"n2"` to node `"n4"`. This is a valid graph traversal because the target node of each traversed edge is the source node of the next.
> 
> This example also demonstrates the usage of `graphTraversal.initialState` ([sec](#graphtraversal-object--initialstate-property)) and `edgeTraversal.finalState` ([sec](#finalstate-property)).
> 
> ```json
> {                                          # A result object ((#result-object)).
>   "graphs": [                              # See (#result-object--graphs-property).
>     {                                      # A graph object ((#graph-object)).
>       "nodes": [                           # See (#nodes-property).
>         { "id": "n1" },                    # A node object ((#node-object)).
>         { "id": "n2" },
>         { "id": "n3" },
>         { "id": "n4" }
>       ],
> 
>       "edges": [                           # See (#edges-property).
>         {                                  # An edge object ((#edge-object)).
>           "id": "e1",                      # See (#edge-object--id-property).
>           "sourceNodeId": "n1",            # See (#sourcenodeid-property).
>           "targetNodeId": "n2"             # See (#targetnodeid-property).
>         },
>         {
>           "id": "e2",
>           "sourceNodeId": "n2",
>           "targetNodeId": "n3"
>         },
>         {
>           "id": "e3",
>           "sourceNodeId": "n2",
>           "targetNodeId": "n4"
>         }
>       ]
>     }
>   ],
> 
>   "graphTraversals": [                     # See (#graphtraversals-property).
>     {                                      # A graphTraversal object ((#graphtraversal-object)).
>       "resultGraphIndex": 0,               # See (#resultgraphindex-property).
> 
>       "initialState": {                    # See (#graphtraversal-object--initialstate-property).
>         "x": {
>           "text": "1"
>         },
>         "y": {
>           "text": "2"
>         },
>         "x + y": {
>           "text": "3"
>         }
>       },
> 
>       "edgeTraversals": [                  # See (#edgetraversals-property).
>         {                                  # An edgeTraversal object ((#edgetraversal-object)).
>           "edgeId": "e1",                  # See (#edgeid-property).
> 
>           "finalState": {                  # See (#finalstate-property).
>             "x": {
>               "text": "4"
>             },
>             "y": {
>               "text": "2"
>             },
>             "x + y": {
>               "text": "6"
>             }
>           }
>         },
>         {
>           "edgeId": "e3",
> 
>           "finalState": {
>             "x": {
>               "text": "4"
>             },
>             "y": {
>               "text": "7"
>             },
>             "x + y": {
>               "text": "11"
>             }
>           }
>         }
>       ]
>     }
>   ]
> }
> ```
