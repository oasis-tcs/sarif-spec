## threadFlow object

### General{#threadflow-object--general}

A thread flow is a sequence of code locations that specify a possible path through a single thread of execution such as an operating system thread or a fiber.

For an example, see [sec](#codeflow-object--general).

### id property{#threadflow-object--id-property}

A `threadFlow` object **MAY** contain a property named `id` whose value is a string that uniquely identifies this `threadFlow` within its containing `codeFlow` object ([sec](#codeflow-object)).

> NOTE: A tool might choose to use an operating system thread id for this purpose. However, if thread ids are reused on a single machine, or if the code flow includes thread flows from more than one machine, the thread id might not be unique.

### message property{#threadflow-object--message-property}

A `threadFlow` object **MAY** contain a property named `message` whose value is a `message` object ([sec](#message-object)) relevant to the thread flow.

### initialState property{#threadflow-object--initialstate-property}

A `threadFlow` object **MAY** contain a property named `initialState` whose value is an object ([sec](#object-properties)) each of whose property values is a `multiformatMessageString` object ([sec](#multiformatmessagestring-object)) that represents the initial value of a relevant item prior to the first location in the thread flow. This property, together with `threadFlowLocation.state` ([sec](#state-property)), enables a SARIF viewer to present a debugger-like "watch window" experience as the user traverses a thread flow.

This property **SHOULD NOT** include items whose values remain constant throughout the thread flow. Such items **SHOULD** be stored in the `immutableState` property ([sec](#threadflow-object--immutablestate-property)).

For details of how properties within a "state" object are represented, see EXAMPLE 1 in [sec](#state-property).

### immutableState property{#threadflow-object--immutablestate-property}

A `threadFlow` object **MAY** contain a property named `immutableState` whose value is an object ([sec](#object-properties)) each of whose property values is a `multiformatMessageString` object ([sec](#multiformatmessagestring-object)) that represents the value of a relevant item that remains constant throughout the thread flow.

> EXAMPLE 1: In this example, `immutableState` holds the value of a global variable that remains constant throughout the thread flow.
>
> ```json
> {                                          # A threadFlow object.
>   "immutableState": {
>     "MaxFiles": {
>       "text": "1000"
>     }
>   }
> }
> ```

### locations property{#threadflow-object--locations-property}

A `threadFlow` object **SHALL** contain a property named `locations` whose value is an array of one or more `threadFlowLocation` objects ([sec](#threadflowlocation-object)). Each element of the array **SHALL** represent a single location visited by the tool in the course of producing the result. This array does not need to include every location visited by the tool, but the elements that are present **SHALL** occur in the execution order that demonstrates the problem. The elements do not need to be unique within the array.

> NOTE: The locations array might include multiple identical elements if, for example, the analysis tool simulated the execution of a loop in the course of producing the result.
