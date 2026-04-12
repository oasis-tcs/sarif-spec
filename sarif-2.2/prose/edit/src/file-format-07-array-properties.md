## Array Properties

### General{#array-properties--general}

Certain properties in this document are defined to be arrays. Examples are the `invocation.toolExecutionNotifications` property ([sec](#toolexecutionnotifications-property)) and the property bag `tags` property ([sec](#tags)).

### Default Value

If an array-valued property is absent, it **SHALL** default to an empty array unless the property’s description specifies otherwise.

### Array Properties with Unique Values

Certain array-valued properties in this document are described as having "unique" elements. When a property is so described, it means that no two elements of the array **SHALL** have equal values. For purposes of this document, two array elements **SHALL** be considered equal when they satisfy the condition for equality described in the JSON Schema standard [cite](#JSCHEMA01), [sec](#externalproperties-object), "Instance equality". In particular, two strings are considered equal when they consist of the same sequence of Unicode [cite](#UNICODE12) code points.

### Array Indices

If any property in this document is described as an "array index," it **SHALL** contain an integer that is a zero-based index into the specified array. If any such property is absent, it **SHALL** default to -1, which indicates that the value is unknown (not set), unless the property’s description specifies otherwise.
