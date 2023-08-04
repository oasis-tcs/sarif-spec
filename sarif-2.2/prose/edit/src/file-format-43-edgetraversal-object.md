## edgeTraversal object

### General{#edgetraversal-object--general}

An `edgeTraversal` object represents the traversal of a single edge during a graph traversal.

### edgeId property

An `edgeTraversal` object **SHALL** contain a property named `edgeId` whose value is a string which equals the `id` property ([sec](#edge-object--id-property)) of one of the `edge` objects ([sec](#edge-object)) in the graph identified by the `resultGraphIndex` property ([sec](#resultgraphindex-property)) or the `runGraphIndex` property ([sec](#rungraphindex-property)) of the containing `graphTraversal` object ([sec](#graphtraversal-object)).

### message property{#edgetraversal-object--message-property}

An `edgeTraversal` object **MAY** contain a property named `message` whose value is a `message` object ([sec](#message-object)) that contains a message to display to the user as the edge is traversed.

### finalState property

An `edgeTraversal` object **MAY** contain a property named `finalState` whose value is an object ([sec](#object-properties)) each of whose properties is a `multiformatMessageString` object ([sec](#multiformatmessagestring-object)) that represents the value of a relevant item after the edge has been traversed.

> NOTE: This property, together with `graphTraversal.initialState` ([sec](#graphtraversal-object--initialstate-property)), enables a viewer to present a debugger-like "watch window" experience as the user traverses a graph.

A SARIF viewer **SHALL** display only those properties that are explicitly present in the `finalState` property of the current `edgeTraversal`. It **SHALL NOT** assume that properties present in previous steps are still present with unchanged values.

For details of how properties within a "state" object are represented, see [sec](#state-property).

### stepOverEdgeCount property

An `edgeTraversal` object **MAY** contain a property named `stepOverEdgeCount` whose value is a non-negative integer specifying the number of edges a user can step over.

This property is intended to enable a viewing experience in which the user can either step over or step into the traversal of a nested graph ([sec](#children-property)). Therefore, this property **SHOULD** be specified only on an edge that leads from a node to one of its child nodes, and its value **SHOULD** be the number of edges the user would need to traverse to return to the current nesting level.

If this property is present, a SARIF viewer **MAY** provide a visual cue informing the user that they have the option of either stepping over the current edge and into the nested graph, or of stepping over the entire traversal of the nested graph.

> EXAMPLE: This example defines a graph containing two nested graphs, the first representing code locations in function `A` and the second representing locations in function `B`. Node `na2` in function `A` represents a call to function `B`.
> 
> The example defines a graph traversal consisting of a set of edge traversals which start at node `"na1"` in function `A`, call into function `B`, and ultimately return to and continue execution in function `A`.
> 
> Suppose the user executes the first edge traversal, which traverses edge `ea1`.The next edge traversal has a `stepOverEdgeCount` property value of 4. Therefore, the SARIF viewer informs her that she can now choose to either step into function `B` by traversing edge `"eab"`, or step over the function call by traversing 4 edges, the last of which (edge `"eba"`) returns to function `A` at node `"na3"`.
> 
> If she chooses to enter the nested graph, she will visit the following nodes, in this order:
> 
> &emsp;&emsp;`[ na1, na2, nb1, nb2, nb3, na3, na4 ]`
> 
> If she chooses not to enter the nested graph, the traversal of the edges
> 
> &emsp;&emsp;`[ eab, eb1, eb2, eba ]`
> 
> will be collapsed into a single "step over." As a result, she will visit the following nodes, in this order:
> 
> &emsp;&emsp;`[ na1, na2, na3, na4 ]`
> 
> ```json
> {                                           # A result object (§3.27).
>   "graphs": [                               # See §3.27.19.
>     {                                       # A graph object (§3.39).
>       "nodes": [
>         {
>           "id": "functionA",
>           "children": [
>             { "id": "na1" },
>             { "id": "na2", "label": "Call functionB" },
>             { "id": "na3" },
>             { "id": "na4" }
>           ]
>         },
>         {
>           "id": "functionB",
>           "nodes": [
>             { "id": "nb1" },
>             { "id": "nb2" },
>             { "id": "nb3" }
>           ],
>         }
>       ]
>       "edges": [
>         { "id": "ea1", "sourceNodeId": "na1", "targetNodeId": "na2" },
>         { "id": "ea2", "sourceNodeId": "na2", "targetNodeId": "na3" },
>         { "id": "eab", "sourceNodeId": "na2", "targetNodeId": "nb1" },
>         { "id": "ea3", "sourceNodeId": "na3", "targetNodeId": "na4" },
>         { "id": "eb1", "sourceNodeId": "nb1", "targetNodeId": "nb2" },
>         { "id": "eb2", "sourceNodeId": "nb2", "targetNodeId": "nb3" },
>         { "id": "eba", "sourceNodeId": "nb3", "targetNodeId": "na3" }
>       ]
>     }
>   ],
> 
>   "graphTraversals": [                      # See §3.27.20.
>     {                                       # A graphTraversal object (§3.42).
>       "resultGraphIndex": 0,                # The graph being traversed.
>       "edgeTraversals": [
>         { "edgeId": "ea1" },
>         {
>           "edgeId": "eab",
>           "stepOverEdgeCount": 4
>         },
>         { "edgeId": "eb1" },
>         { "edgeId": "eb2" },
>         { "edgeId": "eba" },
>         { "edgeId": "ea3" }
>       ]
>     }
>   ]
> }
> ```
