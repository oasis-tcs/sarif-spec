## stack object

### General{#stack-object--general}

A `stack` object describes a single call stack. A call stack is a sequence of nested function calls, each of which is referred to as a stack frame.

### message property{#stack-object--message-property}

A `stack` object **MAY** contain a property named `message` whose value is `message` object ([sec](#message-object)) relevant to this call stack.

### frames property

A stack object **SHALL** contain a property named `frames` whose value is an array of zero or more `stackFrame` objects ([sec](#stackframe-object)). This array **SHALL** include every function call in the stack for which the tool has information, and the entries that are present **SHALL** occur in chronological order with the most recent (innermost) call first and the least recent (outermost) call last. The entries in this array do not need to be unique within the array.

> NOTE 1: It is possible for the same frame to occur multiple times if the call stack includes a recursion.

> NOTE 2: It is possible that the analysis tool will not have location information for every frame in the call stack. This might happen if, for example, application code for which location information is available calls into operating system code for which location information is not available, which in turn calls back into application code.
