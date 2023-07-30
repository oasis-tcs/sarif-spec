## graph object

### General{#graph-object--general}

A `graph` object represents a directed graph, a network of nodes and directed edges that describes some aspect of the structure of the code (for example, a call graph). `graph` objects **MAY** be defined both at the run level in `run.graphs` ([§3.14.20](#run-object--graphs-property)) and at the result level in `result.graphs` ([§3.27.19](#result-object--graphs-property)).

A path through a graph, called a "graph traversal," is represented by a `graphTraversal` object ([§3.42](#graphtraversal-object)).

### description property{#graph-object--description-property}

A `graph` object **MAY** contain a property named `description` whose value is a `message` object ([§3.11](#message-object)) that describes the graph.

### nodes property

A `graph` object **MAY** contain a property named `nodes` whose value is an array of zero or more unique ([§3.7.3](#array-properties-with-unique-values)) `node` objects ([§3.40](#node-object)) which represent the nodes of the graph.

### edges property

A `graph` object **MAY** contain a property named `edges` whose value is an array of zero or more unique ([§3.7.3](#array-properties-with-unique-values)) `edge` objects ([§3.41](#edge-object)) which represent the edges of the graph.
