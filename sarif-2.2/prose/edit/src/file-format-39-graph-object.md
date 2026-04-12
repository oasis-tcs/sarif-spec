## `graph` Object

### General{#graph-object--general}

A `graph` object represents a directed graph, a network of nodes and directed edges that describes some aspect of the structure of the code (for example, a call graph). `graph` objects **MAY** be defined both at the run level in `run.graphs` ([sec](#run-object--graphs-property)) and at the result level in `result.graphs` ([sec](#result-object--graphs-property)).

A path through a graph, called a "graph traversal," is represented by a `graphTraversal` object ([sec](#graphtraversal-object)).

### `description` Property{#graph-object--description-property}

A `graph` object **MAY** contain a property named `description` whose value is a `message` object ([sec](#message-object)) that describes the graph.

### `nodes` Property

A `graph` object **MAY** contain a property named `nodes` whose value is an array of zero or more unique ([sec](#array-properties-with-unique-values)) `node` objects ([sec](#node-object)) which represent the nodes of the graph.

### `edges` Property

A `graph` object **MAY** contain a property named `edges` whose value is an array of zero or more unique ([sec](#array-properties-with-unique-values)) `edge` objects ([sec](#edge-object)) which represent the edges of the graph.
