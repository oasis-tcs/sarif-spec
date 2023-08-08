## codeFlow object

### General{#codeflow-object--general}

A `codeFlow` object describes the progress of one or more programs through one or more thread flows, which together lead to the detection of a problem in the system being analyzed. We define a thread flow as a temporally ordered sequence of code locations occurring within a single thread of execution, typically an operating system thread or a fiber. The thread flows in a code flow **MAY** lie within a single process, within multiple processes on the same machine, or within multiple processes on multiple machines.

> EXAMPLE
> 
> ```json
> {                                       # A result object ((#result-object)).
>   "codeFlows": [                        # See (#codeflows-property).
>     {                                   # A codeFlow object.
>       "message": {                      # See (#codeflow-object--message-property).
>         "text": "..."
>       },
> 
>       "threadFlows": [                  # See (#threadflows-property).
>         {                               # A threadFlow object ((#threadflow-object)).
>           "id": "thread-123",           # See (#threadflow-object--id-property).
>           "message": {                  # See (#threadflow-object--message-property).
>             "text": "..."
>           },
> 
>           "locations": [                # See (#threadflow-object--locations-property).
>             {                           # A threadFlowLocation object ((#threadflowlocation-object)).
>               "location": {             # See (#threadflowlocation-object--location-property).
>                 "physicalLocation": {   # See (#physicallocation-property).
>                   "artifactLocation": {
>                     "uri": "ui/window.c",
>                     "uriBaseId": "SRCROOT"
>                   },
> 
>                   "region": {
>                     "startLine": 42
>                   }
>                 }
>               },
> 
>               "state": {                # See (#state-property).
>                 "x": {
>                   "text": "42"
>                 },
>                 "y": {
>                   "text": "54"
>                 },
>                 "x + y": {
>                   "text": "96"
>                 }
>               },
> 
>               "nestingLevel": 0,        # See (#nestinglevel-property).
>               "executionOrder": 2       # See (#executionorder-property).
>             }
>           ]
>         }
>       ]
>     }
>   ]
> }
> ```

### message property{#codeflow-object--message-property}

A `codeFlow` object **MAY** contain a property named `message` whose value is a `message` object ([sec](#message-object)) relevant to the code flow.

### threadFlows property

A `codeFlow` object **SHALL** contain a property named `threadFlows` whose value is an array of one or more `threadFlow` objects ([sec](#threadflow-object)) each of which describes the progress of a program through a single thread of execution such as an operating system thread or a fiber.
