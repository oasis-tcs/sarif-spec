## threadFlowLocation object

### General{#threadflowlocation-object--general}

A `threadFlowLocation` object represents a location visited by an analysis tool in the course of simulating or monitoring the execution of a program.

### index property{#threadflowlocation-object--index-property}

Depending on the circumstances, a `threadFlowLocation` object either **MAY**, **SHALL NOT**, or **SHALL** contain a property named `index` whose value is the array index ([sec](#array-indices)) within `theRun.threadFlowLocations` ([sec](#threadflowlocations-property)) of a `threadFlowLocation` object that provides the properties for `thisObject`. We refer to the object in `theRun.threadFlowLocations` as the "cached object."

If `thisObject` is an element of `theRun.threadFlowLocations`, then `index` **MAY** be present. If present, its value **SHALL** be the index of `thisObject` within `theRun.threadFlowLocations`.

Otherwise, if `theRun.threadFlowLocations` is absent, or if it does not contain a cached object for `thisObject`, then `index` **SHALL NOT** be present.

Otherwise (that is, if `thisObject` belongs to a result, and `theRun.threadFlowLocations` contains a cached object for `thisObject`), then `index` **SHALL** be present, and its value **SHALL** be the index within `theRun.threadFlowLocations` of the cached object.

If `index` is present, `thisObject` **SHALL** take all properties present on the cached object. If `thisObject` contains any properties other than `index`, they **SHALL** equal the corresponding properties of the cached object.

> NOTE 1: This allows a SARIF producer to reduce the size of the log file by reusing the same `threadFlowLocation` object in multiple thread flows.

> EXAMPLE 1: In this example, `thisObject` is an element of `theRun.threadFlowLocations`. Its array index is known to be 1, so `thisObject.index` does not need to be present, but since it is present, it equals the array index, as required.
> 
> ```json
> {                                 # A run object (§3.14).
>   "threadFlowLocations": [        # See §3.14.19.
>     ...
>     {                             # A threadFlowLocation object: thisObject.
>       "index": 1,                 # Optional.
>       "location": {
>         ...
>       }
>     },
>     ...
>   ],
>   ...
> }
> ```

> EXAMPLE 2: In this example, `thisObject` is not an element of `theRun.threadFlowLocations`; rather, it is an element of `theResult.codeFlows[0].threadFlows[0].locations`. There is no cached object; that is, there is no object in `theRun.threadFlowLocations` that provides the properties for `thisObject`. Therefore, `thisObject.index` is absent, as required.
> 
> ```json
> {                                 # A run object (§3.14).
>   "results": [                    # See §3.14.23.
>     {                             # A result object (§3.27).
>       "codeFlows": [              # See §3.27.18.
>         {                         # A codeFlow object (§3.36).
>           "threadFlows": [        # See §3.36.3.
>             {                     # A threadFlow object (§3.37).
>               "locations": [      # See §3.37.6.
>                 {                 # A threadFlowLocation object (thisObject).
>                   "location": {   # See §3.38.3.
>                     ...
>                   }
>                 }
>               ]
>             }
>           ]
>         }
>       ],
>       ...
>     }
>   ],
>   ...
>   "threadFlowLocations": [        # See §3.14.19.
>     ...
>   ]
> }
> ```

> EXAMPLE 3: In this example, `thisObject` is again an element of `theResult.codeFlows[0].threadFlows[0].locations`, not an element of `theRun.threadFlowLocations`. But in this example, there is a cached object, an element of `theRun.threadFlowLocations` that provides the properties for `thisObject`. Therefore, `thisObject.index` is present, as required.
> 
> ```json
> {                                 # A run object (§3.14).
>   "results": [                    # See §3.14.23.
>     {                             # A result object (§3.27).
>       "codeFlows": [              # See §3.27.18.
>         {                         # A codeFlow object (§3.36).
>           "threadFlows": [        # See §3.36.3.
>             {                     # A threadFlow object (§3.37).
>               "locations": [      # See §3.37.6.
>                 {                 # An threadFlowLocation object: thisObject.
>                   "index": 0      # index is present so no other properties.
>                 }
>               ]
>             }
>           ]
>         }
>       ],
>       ...
>     }
>   ],
>   ...
>   "threadFlowLocations": [        # See §3.14.19.
>     {                             # The cached threadFlowLocation object.
>       "location": {               # See §3.38.3.
>         ...
>       }
>     },
>     ...
>   ]
> }
> ```

### location property{#threadflowlocation-object--location-property}

If location information is available, a `threadFlowLocation` object **SHALL** contain a property named `location` whose value is a `location` object ([sec](#location-object)) that specifies the location to which the `threadFlowLocation` object refers. If location information is not available, `location` **SHALL** be absent.

There are analysis tools whose native output format includes the equivalent of a SARIF code flow, but which do not provide location information for every step in the code flow. A SARIF converter for such a format might not be able to populate `location`. However, if the native output format associates a human readable message with such a step, the SARIF converter **SHOULD** create a `location` object and populate only its `message` property ([sec](#location-object--message-property)). A SARIF direct producer which creates such code flows **SHOULD** populate `location.message`, even if no actual location information is available.

> EXAMPLE 1: In this example, a file is locked by another program before a thread attempts to write to it. The analysis tool has no location information for the other program; in fact, the analysis tool might merely be simulating an execution sequence in which a *hypothetical* external program locks the file. Nevertheless, it provides a helpful message.
> 
> Note the use of `executionOrder` ([sec](#executionorder-property)) to ensure that the location in the external program executes before the location in the program being analyzed.
> 
> ```json
> {                                     # A codeFlow object (§3.36).
>   "threadFlows": [                    # See §3.36.3.
>     {                                 # A threadFlow object (§3.37).
>       "message": {                    # See §3.37.3.
>         "text": "An external program."
>       },
>       "locations": [                  # See §3.37.6.
>         {                             # A threadFlowLocation object.
>           "executionOrder": 1,
>           "location": {               # A location object with only a message.
>             "message": {
>               "text": "File is now locked."
>             }
>           }
>         }
>       ]
>     },
>     {                                 # Another threadFlow object.
>       "message": {
>         "text": "The program being analyzed."
>       },
>       "locations": [
>         ...
>         {
>           "executionOrder": 2,
>           "location": {
>             "message": {
>               "text": "Attempt to write to the file."
>             },
>             "physicalLocation": {
>               "artifactLocation": {
>                 "uri": "io/logger.c",
>                 "uriBaseId": "SRCROOT"
>               },
>               "region": {
>                 "startLine": 42,
>                 "snippet": {
>                   "text": "    fprintf(fd, \"test\\n\");"
>                 }
>               } 
>             }
>           }
>         }
>       ]
>     }
>   ]
> }
> ```

### module property{#threadflowlocation-object--module-property}

A `threadFlowLocation` object **MAY** contain a property named `module` whose value is a string containing the name of the module that contains the code location specified by this object.

### stack property{#threadflowlocation-object--stack-property}

A `threadFlowLocation` object **MAY** contain a property named `stack` whose value is a `stack` object ([sec](#stack-object)) that represents the call stack leading to this location.

### webRequest property{#threadflowlocation-object--webrequest-property}

A `threadFlowLocation` object **MAY** contain a property named `webRequest` whose value is a `webRequest` object ([sec](#webrequest-object)) that describes an HTTP request sent from this location.

> NOTE: This property is primarily useful to web analysis tools.

### webResponse property{#threadflowlocation-object--webresponse-property}

A `threadFlowLocation` object **MAY** contain a property named `webResponse` whose value is a `webResponse` object ([sec](#webresponse-object)) that describes the response to the HTTP request sent from this location.

> NOTE: This property is primarily useful to web analysis tools.

### kinds property{#threadflowlocation-object--kinds-property}

A `threadFlowLocation` object **MAY** contain a property named `kinds` whose value is an array of unique ([sec](#array-properties-with-unique-values)) strings that describe the meaning of this location. The strings **SHOULD** be human-readable (as opposed to, for example, GUIDs or hash values).

When possible, SARIF producers **SHOULD** use the following values, with the specified meanings.

Verbs:

- `"acquire"`: Gain ownership of something.

- `"release"`: Relinquish ownership of something.

- `"enter"`: Entry point to a section of the program such as a function.

- `"exit"`: Exit point from a section of the program such as a function.

- `"call"`: Point of call into a section of the program such as a function.

- `"return"`: Point of return from a section of the program such as a function.

- `"branch"`: Conditional transfer of control.

    NOTE 1: These values are typically combined with nouns from the list below, as in the examples below.

Nouns:

- `"taint"`: Value obtained from user input.

- `"function"`: Section of a program that can be called into and returned from.

- `"handler"`: Code invoked in response to an exception, signal, or event.

- `"lock"`: Limits access to a resource.

- `"memory"`: Portion of computer’s internal storage.

- `"resource"`: Anything that can be acquired and released.

- `"scope"`: Section of a program that limits the visibility of variables defined within it.

- `"value"`: The value of a variable.

    NOTE 2: `"kinds": [ "acquire", "value" ]` can be used to denote a variable assignment or initialization.

Miscellaneous:

- `"implicit"`: Code was invoked implicitly, for example by a garbage collector.

- `"false"`: A condition evaluated to false.

- `"true"`: A condition evaluated to true.

- `"caution"`: Execution of the code at this location in the current circumstance requires care.

- `"danger"`: Execution of the code at this location in the current circumstance is dangerous.

- `"unknown"`: The state of an item is not known.

- `"unreachable"`: Code at this location is unreachable.

    NOTE 3: Some analysis tools effectively "uncomment" unreachable code, allowing a simulated execution to flow through it. If such a tool detected a problem in the uncommented code, it could mark the `threadFlowLocation` as `"unreachable"`. An engineering team might then decide to treat this problem with lower priority.

If none of these values are appropriate, a SARIF producer **MAY** use any value.

The interpretations of values other than those above depends on the producer. A SARIF consumer that wishes to act based on such values **SHOULD** examine `theTool` to determine if it (the consumer) knows how to interpret them.

> NOTE 4: This might not be necessary if, for example, the consumer has out of band information telling it how to interpret the values.

A SARIF producer **MAY** provide additional kind-dependent information by populating `threadFlowLocation.properties` with properties whose names and values depend on the kind. A SARIF consumer that knows how to interpret `kinds` for this tool **MAY** use this additional information.

> EXAMPLE 1: In this example, tainted data enters the system at this location.
> 
> ```json
> "kinds": [
>   "acquire",
>   "taint"
> ]
> ```

> EXAMPLE 2: In this example, the "taint" state of a data item at this location is unknown:
> 
> ```json
> "kinds": [
>   "taint",
>   "unknown"
> ]
> ```

> EXAMPLE 3: In this example, control leaves a function at this location.
> 
> ```
> "kinds": [
>   "exit",
>   "function"
> ]
> ```

### state property

A `threadFlowLocation` object **MAY** contain a property named `state` whose value is an object ([sec](#object-properties)) in which each property name represents an item relevant to the location in the context of the code flow, and the corresponding property value is a `multiformatMessageString` object ([sec](#multiformatmessagestring-object)) that specifies either the value of or a constraint on that item.

> NOTE: This property enables a SARIF viewer to present a debugger-like "watch window" experience as the user navigates through a code flow.

A SARIF viewer **SHALL NOT** assume that expressions mentioned in previous steps but not mentioned in the current step are still present with unchanged values.

> EXAMPLE 1: In this example, the `state` property captures the values of the expressions `"x"`, `"y"`, and `"x + y"`, and a constraint on the expression `"y – x"`.
> 
> ```json
> {                              # A threadFlowLocation object.
>   "state": {
>     "x": {
>       "text": "42"
>     },
>     "y": {
>       "text": "54"
>     },
>     "x + y": {
>       "text": "96"
>     },
>     "y – x": {
>       "text": "{expr} > 0"
>     }
>   }
> }
> ```

> EXAMPLE 2: In C++, a property name within the `state` object might be:
> 
> - A variable name such as `"index"`.
> 
> - An array element reference such as `"names[index]"`.
> 
> - An object property reference such as `"names[index]->first"`.
> 
> - Any other expression that produces a value.

> EXAMPLE 3: In C++, a property value within the `state` object might be:
> 
> - An integer such as `"42"` (note that the property value is a string).
> 
> - A string such as `"\"John\""` (the double quotes are escaped as they would be in a JSON serialization; other serializations might represent the double quotes differently).
> 
> - A Boolean such as `"true"`.

In a property value that represents a constraint, the item being constrained **SHALL BE** represented by the string `"{expr}"`. (See > EXAMPLE 1 above, which shows a constraint on the expression `"y – x"`.)

A constraint which expresses the equality of `"{expr}"` with a literal value **SHALL** be considered equivalent to that literal value.

> EXAMPLE 4: In a language where `==` denotes value equality, the property value `"{expr} == 42"`, which represents a constraint, is identical in meaning to the property value `"42"`, which represents a value.

### nestingLevel property

A `threadFlowLocation` object **MAY** contain a property named `nestingLevel` whose value is a non-negative integer that represents any type of logical containment hierarchy among the `threadFlowLocation` objects in the `threadFlow`. Typically, it represents function call depth.

A viewer that renders a `threadFlow` **SHOULD** provide a visual representation of the value of `nestingLevel`. Typically, this would be an indentation indicating the depth of each location in the call tree.

### executionOrder property

A `threadFlowLocation` object **MAY** contain a property named `executionOrder` whose value is a non-negative integer that represents the temporal order in which execution reached this location, across all `threadFlowLocation` objects within all `threadFlow` objects belonging to a single `codeFlow` ([sec](#codeflow-object)). `executionOrder` values are assigned in increasing order of time; for example, execution reaches a `threadFlowLocation` whose `executionOrder` is 2 occurs before it reaches a `threadFlowLocation` whose `executionOrder` is 3. If two `threadFlowLocation`s in different `threadFlow` objects within the same `codeFlow` have the same value for `executionOrder`, it means that execution reached both of those locations simultaneously. For that reason, values of `executionOrder` within a single `threadFlow` **SHALL** be unique.

It is only necessary to assign a value to `executionOrder` when the temporal ordering of a `threadFlowLocation` relative to a location in a different `threadFlow` is significant to the detection of a result.

If `executionOrder` is absent, it **SHALL** default to -1, which indicates that the value is unknown (not set).

> NOTE: Negative values are forbidden because their use would suggest some non-obvious semantic difference between positive and negative values.

### executionTimeUtc property

A `threadFlowLocation` object **MAY** contain a property named `executionTimeUtc` whose value is a string in the format specified in [sec](#datetime-properties), specifying the UTC date and time at which the thread of execution through the code reached this location.

### importance property

A `threadFlowLocation` **MAY** contain a property named `importance` whose value is a string that specifies the importance of this `threadFlowLocation` in understanding the code flow.

The `importance` property **SHALL** have one of the following values, with the specified meanings:

- `"important"`: this location is important for understanding the code flow.

- `"essential"`: this location is essential for understanding the code flow.

- `"unimportant"`: this location contributes to a more detailed understanding of the code flow but is not normally needed.

If this property is absent, it **SHALL** be considered to have the value `"important"`.

> NOTE: A viewer might use this property to offer the user three options for viewing a lengthy code flow:
> 
> - A "normal view," which omits locations whose `importance` property is `"unimportant"`.
> 
> - An "abbreviated view," which displays only those locations whose `importance` property is `"essential"`.
> 
> - A "verbose view," which displays all the locations in the code flow.

### taxa property{#threadflowlocation-object--taxa-property}

A `threadFlowLocation` **MAY** contain a property named `taxa` whose value is an array of zero or more unique ([sec](#array-properties-with-unique-values)) `reportingDescriptorReference` objects each of which specifies a category into which this `threadFlowLocation` falls.

> NOTE: The motivation for this property is an analysis tool that uses a set of rules to guide its analysis as it traces tainted data from a source to a sink. For example, at one location, the tool might apply a rule that says: "If the input to `String.Substr` is tainted, then so is the return value." Such a tool can represent these "helper rules" as a custom taxonomy ([sec](#taxonomies)), an array of `reportingDescriptor` objects ([sec](#reportingdescriptor-object)). Each member of `threadFlowLocation.taxa` can reference one of these helper rules.

> EXAMPLE 1: This example illustrates the scenario in the above note.
> 
> ```json
> {                                # A run object (§3.14).
>   "tool": {                      # See §3.14.6.
>     "driver": {
>       "name": "TaintDetector",
>       "rules": [
>         {
>           "id": "TD0001",
>           "name": "UntrustedDataStoredInDatabase",
>           "shortDescription": {
>             "text": "Data from an untrusted source was stored in a database."
>           }
>         },
>         ...
>       ],
>       "taxa": [                  # Custom taxonomy (§3.19.3) for helper rules.
>         {                        # A reportingDescriptor object (§3.49).
>           "id": "HR0001",
>           "name": "SubstrPropogatesTaint",
>           "shortDescription": {
>             "text": "If the input to String.Substr is tainted,
>                      so is the return value."
>           }
>         },
>         ...
>       ]
>     }
>   },
> 
>   "results": [                   # See §3.14.23.
>     {                            # A result object §3.27.
>       "ruleId": "TD0001",
>       ...
>       "codeFlows": [             # See §3.27.18.
>         {                        # A codeFlow object (§3.36).
>           "threadFlows": [       # See §3.36.3.
>             {                    # A threadFlow object (§3.37).
>               "locations": [     # See §3.37.6.
>                 ...
>                 {                # A threadFlowLocation object.
>                   "location": {  # See §3.38.3.
>                     "physicalLocation": {
>                       "artifactLocation": {
>                         "uri": "io/input.c",
>                         "uriBaseId": "SRCROOT"
>                       },
>                       "region": {
>                         "startLine": 32
>                       }
>                     }
>                   },
>                   "taxa": [
>                     {        # A reportingDescriptorReference object (§3.52).
>                       "id": "HR0001",
>                       "index": 0
>                     }
>                   ]
>                 },
>                 ...
>               ]
>             }
>           ]
>         }
>       ]
>     }
>   ]
> }
> ```
