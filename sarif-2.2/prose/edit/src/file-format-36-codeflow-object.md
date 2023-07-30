## codeFlow object

### General{#codeflow-object--general}

A `codeFlow` object describes the progress of one or more programs through one or more thread flows, which together lead to the detection of a problem in the system being analyzed. We define a thread flow as a temporally ordered sequence of code locations occurring within a single thread of execution, typically an operating system thread or a fiber. The thread flows in a code flow **MAY** lie within a single process, within multiple processes on the same machine, or within multiple processes on multiple machines.

> EXAMPLE
> 
> ```json
> {                                       # A result object (§3.27).
>   "codeFlows": [                        # See §3.27.18.
>     {                                   # A codeFlow object.
>       "message": {                      # See §3.36.2.
>         "text": "..."
>       },
> 
>       "threadFlows": [                  # See §3.36.3.
>         {                               # A threadFlow object (§3.37).
>           "id": "thread-123",           # See §3.37.2.
>           "message": {                  # See §3.37.3.
>             "text": "..."
>           },
> 
>           "locations": [                # See §3.37.6.
>             {                           # A threadFlowLocation object (§3.38).
>               "location": {             # See §3.38.3.
>                 "physicalLocation": {   # See §3.28.3.
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
>               "state": {                # See §3.38.9.
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
>               "nestingLevel": 0,        # See §3.38.10.
>               "executionOrder": 2       # See §3.38.11.
>             }
>           ]
>         }
>       ]
>     }
>   ]
> }
> ```

### message property{#codeflow-object--message-property}

A `codeFlow` object **MAY** contain a property named `message` whose value is a `message` object ([§3.11](#message-object)) relevant to the code flow.

### threadFlows property

A `codeFlow` object **SHALL** contain a property named `threadFlows` whose value is an array of one or more `threadFlow` objects ([§3.37](#threadflow-object)) each of which describes the progress of a program through a single thread of execution such as an operating system thread or a fiber.
