## `stackFrame` Object

### General{#stackframe-object--general}

A `stackFrame` object describes a single stack frame within a call stack ([sec](#stack-object)).

### `location` Property{#stackframe-object--location-property}

A `stackFrame` object **MAY** contain a property named `location` whose value is a `location` object ([sec](#location-object)) specifying the location to which this stack frame refers.

If location information is unavailable (as it might be, for example, when stepping from application code into library code or operating system code), `location` **SHOULD** be present and **SHOULD** contain a `message` property ([sec](#location-object)) (for example, with a message string `"Call into external code"`).

### `module` Property{#stackframe-object--module-property}

A `stackFrame` object **MAY** contain a property named `module` whose value is a string containing the name of the module that contains the location to which this stack frame refers.

### `threadId` Property{#stackframe-object--threadid-property}

A `stackFrame` object **MAY** contain a property named `threadId` whose value is an integer which identifies the thread on which the code at the location specified by this object was executed.

### `parameters` Property{#stackframe-object--parameters-property}

A `stackFrame` object **MAY** contain a property named parameters whose value is an array of zero or more strings representing the parameters of the function call represented by this stack frame.
