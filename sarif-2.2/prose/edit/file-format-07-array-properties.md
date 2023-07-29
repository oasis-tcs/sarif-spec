## Array properties

### General{#array-properties--general}

Certain properties in this document are defined to be arrays. Examples are the `invocation.toolExecutionNotifications` property ([§3.20.21](#toolexecutionnotifications-property)) and the property bag `tags` property ([§3.8.2](#tags)).

### Default value

If an array-valued property is absent, it **SHALL** default to an empty array unless the property’s description specifies otherwise.

### Array properties with unique values

Certain array-valued properties in this document are described as having "unique" elements. When a property is so described, it means that no two elements of the array **SHALL** have equal values. For purposes of this document, two array elements **SHALL** be considered equal when they satisfy the condition for equality described in the JSON Schema standard \[[JSCHEMA01](#JSCHEMA01)\], [§4.3](#externalproperties-object), "Instance equality". In particular, two strings are considered equal when they consist of the same sequence of Unicode \[[UNICODE12](#UNICODE12)\] code points.

### Array indices

If any property in this document is described as an "array index," it **SHALL** contain an integer that is a zero-based index into the specified array. If any such property is absent, it **SHALL** default to -1, which indicates that the value is unknown (not set), unless the property’s description specifies otherwise.
