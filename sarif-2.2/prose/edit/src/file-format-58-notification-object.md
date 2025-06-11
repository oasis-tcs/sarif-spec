## notification object

### General{#notification-object--general}

A `notification` object describes a condition encountered during the execution of an analysis tool which is relevant to the operation of the tool itself, as opposed to being relevant to an artifact being analyzed by the tool. Conditions relevant to artifacts being analyzed by a tool are represented by `result` objects ([sec](#result-object)).

### descriptor property{#notification-object--descriptor-property}

A `notification` object **SHOULD** contain a property named `descriptor` whose value is a `reportingDescriptorReference` object ([sec](#reportingdescriptorreference-object)) that identifies this notification.

If the `reportingDescriptor` object ([sec](#reportingdescriptor-object)) `theDescriptor` to which `descriptor` refers exists (that is, if `theTool` contains a `reportingDescriptor` object that describes this notification), then `descriptor` **SHOULD** refer to `theDescriptor`.

> NOTE: If `theDescriptor` exists but `descriptor` does not refer to it, a SARIF consumer will not be able to locate the metadata for this notification.

### associatedRule property

If the condition described by the `notification` object is relevant to a particular analysis rule, the `notification` object **SHOULD** contain a property named `associatedRule` whose value is a `reportingDescriptorReference` object ([sec](#reportingdescriptorreference-object)) that identifies the rule.

> EXAMPLE 1: In this example, there is more than one rule with id `CA1711`. `associatedRule.index` uniquely specifies the relevant rule.
>
> ```json
> {                                      # A run object ((#run-object)).
>   "tool": {                            # See (#run-object--tool-property).
>     "driver": {                        # See (#driver-property).
>       "name": "CodeScanner",
>       "rules": [                       # See (#rules-property).
>         {                              # A reportingDescriptor object ((#reportingdescriptor-object)).
>           "id": "CA1711",
>           ...
>         },
>         {                              # Another reportingDescriptor object
>           "id": "CA1711",              #  with the same id. associatedRule.id
>           ...                          #  identifies this one.
>         }
>       ]
>     }
>   },
>   "invocations": [                      # See (#invocations-property).
>     {                                   # An invocation object ((#invocation-object)).
>       "toolConfigurationNotifications": [ # See (#toolconfigurationnotifications-property).
>         {                               # A notification object ((#notification-object)).
>           "descriptor": {
>             "id": "CFG0001"
>           },
>           "message": {
>             "text": "Rule configuration is missing."
>           },
>           "associatedRule": {
>             "id": "CA1711",
>             "index": 1
>           }
>         }
>       ],
>       ...
>     }
>   ]
> }
> ```

### locations property{#notification-object--locations-property}

If the condition described by the `notification` object is relevant to one or more locations, the `notification` object **MAY** contain
a property named `locations` whose value is an array of zero or more unique ([sec](#array-properties-with-unique-values)) `location` objects ([sec](#location-object))
that identify those locations to which the condition described by the notification applies.

### message property{#notification-object--message-property}

A `notification` object **SHALL** contain a property named `message` whose value is a `message` object ([sec](#message-object)) that describes the condition that was encountered. See [sec](#message-string-lookup) for the procedure for looking up a message string from a `message` object, in particular, for the case where the `message` object occurs as the value of `notification.message`.

### level property{#notification-object--level-property}

A `notification` object **MAY** contain a property named `level` whose value is one of a fixed set of strings that specify the severity level of the notification.

If present, the `level` property **SHALL** have one of the following values, with the specified meanings:

- `"error"`: A serious problem was found. The condition encountered by the tool resulted in the analysis being halted or caused the results to be incorrect or incomplete.

- `"warning"`: A problem that is not considered serious was found. The condition encountered by the tool is such that it is uncertain whether a problem occurred, or is such that the analysis might be incomplete but the results that were generated are probably valid.

- `"note"`: The notification is purely informational. There is no required action.

- `"none"`: This is a trace notification (typically, debug output from the tool).

If `level` is absent, it **SHALL** default to the value determined by the procedure defined for `result.level` ([sec](#result-object--level-property)), except throughout the procedure, replace `ruleConfigurationOverrides` with `notificationConfigurationOverrides`.

Analysis tools **SHOULD** treat notifications whose `level` property is `"error"` as failures and treat the entire run as having failed (for example, by settings the exit code to the value that the tool uses to indicate failure, typically a non-zero value).

Because a notification whose `level` property is `"error"` describes a failed run, an analysis tool **SHALL NOT** override the severity of such a notification.

### threadId property{#notification-object--threadid-property}

A `notification` object **MAY** contain a property named `threadId` whose value is an integer which identifies the thread associated with this notification.

### timeUtc property

A `notification` object **MAY** contain a property named `timeUtc` whose value is a string in the format specified [sec](#datetime-properties), specifying the UTC date and time at which the analysis tool generated the notification.

### exception property

If the notification is a result of a runtime exception, the `notification` object **MAY** contain a property named `exception` whose value is an `exception` object ([sec](#exception-object)).

If the notification is not the result of a runtime exception, the `exception` property **SHALL** be absent.

### relatedLocations property{#notification-object--relatedlocations-property}

A `notification` object **MAY** contain a property named `relatedLocations` whose value is an array of zero or more unique ([sec](#array-properties-with-unique-values)) `location` objects ([sec](#location-object)) that identify those locations relevant to understanding the result.

The `relatedLocations` property **SHOULD** allow `notification` objects to distinguish between the following types of locations:

- Locations to which the condition described by the `notification` object **SHALL** apply.
- Other locations to which the condition described by the `notification` object **SHALL NOT** apply but are relevant to understanding the result.
