## reportingDescriptorReference object

### General{#reportingdescriptorreference-object--general}

A `reportingDescriptorReference` object identifies a particular `reportingDescriptor` object ([sec](#reportingdescriptor-object)), which we refer to as `theDescriptor`, among all `reportingDescriptor` objects defined by `theTool`, including those defined by `theTool.driver` ([sec](#driver-property)) and `theTool.extensions` ([sec](#extensions-property)).

In some cases, there is no `reportingDescriptor` object associated with a `reportingDescriptorReference` object. In that case, the `reportingDescriptorReference` object **SHALL** contain only the `id` property ([sec](#reportingdescriptorreference-object--id-property)), and `theDescriptor` does not exist.

> EXAMPLE 1: In this example, a tool emits a tool execution notification that refers to a rule. The tool does not provide rule metadata. Therefore, `associatedRule` ([sec](#associatedrule-property)) contains only an `id` property, whose value is the id of the rule that failed. Similarly, the tool does not provide metadata about its notifications, so `"descriptor"` ([sec](#notification-object--descriptor-property)) contains only the id of the notification.
> 
> ```json
> {                                            # An invocation object ((#invocation-object)).
>   "toolExecutionNotifications": [            # See (#toolexecutionnotifications-property).
>     {                                        # A notification object ((#notification-object)).
>       "descriptor": {                        # See (#notification-object--descriptor-property).
>         "id": "CTN9999"
>       },
>       "associatedRule": {                    # See (#associatedrule-property).
>         "id": "C2001"
>       },
>       "level": "error",
>       "message": {
>         "text": "Exception evaluating rule 'C2001'. Rule disabled;
>                  run continues."
>       }
>     }
>   ]
> }
> ```

### Constraints{#reportingdescriptorreference-object--constraints}

If metadata is present, at least one of `index` ([sec](#reportingdescriptorreference-object--index-property)) and `guid` ([sec](#reportingdescriptorreference-object--guid-property)) **SHALL** be present. If both are present, they **SHALL** identify the same `reportingDescriptor` object ([sec](#reportingdescriptor-object)).

### reportingDescriptor lookup

`theDescriptor` **SHALL** be located within the `toolComponent` object ([sec](#toolcomponent-object)) identified by the `toolComponent` property ([sec](#toolcomponent-property)), which we refer to as `theComponent`. The procedure for looking up a `toolComponent` from a `toolComponentReference` is described in [sec](#toolcomponent-lookup).

`theDescriptor` **SHALL** be located either within `theComponent.rules` ([sec](#rules-property)) or `theComponent.notifications` ([sec](#notifications-property)), according to this table:

| If the `reportingDescriptorReference` occurs in:                                                      | ... then `theDescriptor` is an element of: |
|:------------------------------------------------------------------------------------------------------|:-------------------------------------------|
| `invocation.ruleConfigurationOverrides` ([sec](#ruleconfigurationoverrides-property))                 | `rules`                                    |
| `invocation.notificationConfigurationOverrides` ([sec](#notificationconfigurationoverrides-property)) | `notifications`                            |
| `result.rule` ([sec](#rule-property))                                                                 | `rules`                                    |
| `notification.descriptor` ([sec](#notification-object--descriptor-property))                          | `notifications`                            |
| `notification.associatedRule` ([sec](#associatedrule-property))                                       | `rules`                                    |

### id property{#reportingdescriptorreference-object--id-property}

A `reportingDescriptorReference` object **MAY** contain a property named `id` whose value is a hierarchical string ([sec](#hierarchical-strings)) that either equals `theDescriptor.id` ([sec](#reportingdescriptor-object--id-property)) or equals `theDescriptor.id` plus one additional hierarchical component.

> NOTE: This property does not participate in the lookup, but its presence improves the readability of the log file at the expense of increased file size.

If `id` is absent and `theResult.ruleId` ([sec](#ruleid-property)) is present, then `id` **SHALL** default to `theResult.ruleId`. If both are present, they **SHALL** be equal.

For more information about the semantics of `id` when `theDescriptor` is a rule, in particular the usage of the hierarchical components of `id`, see the description of `result.ruleId` ([sec](#ruleid-property)).

> EXAMPLE 1: In this example, the first `result` object is valid because `rule.id` (inherited from `ruleId`) equals `theDescriptor.id`. The second `result` object is also valid because `rule.id` (this time specified directly) equals `theDescriptor.id` plus one additional hierarchical component (`"ghi"`). The third `result` object is invalid because `theDescriptor.id` is not a "component-wise" prefix of `rule.id`. The fourth `result` object is invalid because `ruleId` does not equal `rule.id`.
> 
> ```json
> {                             # A run object ((#run-object)).
>   "tool": {                   # See (#run-object--tool-property).
>     "driver": {               # See (#driver-property).
>       "name": "CodeScanner",
>       "rules": [              # See (#rules-property).
>         {                     # A reportingDescriptor object ((#reportingdescriptor-object)).
>           "id": "abc/def",    # See (#reportingdescriptor-object--id-property).
>           ...
>         },
>         ...
>       ]
>     }
>   },
>   "results": [                # See (#results-property).
>     {                         # A result object ((#result-object)).
>       "ruleId": "abc/def",    # See (#ruleid-property).
>       "rule": {
>         "index": 0
>       }
>     },
>     {
>       "rule": {
>         "id": "abc/def/ghi",
>         "index": 0
>       }
>     },
>     {
>       "rule": {
>         "id": "abc/defg",     # INVALID: theDescriptor.id is not a
>         "index": 0            #   "component-wise" prefix of id.
>       }
>     },
>     {
>       "ruleId": "abc/def",
>       "rule": {
>         "id": "abc/defg/hij", # INVALID: Not equal to ruleId.
>         "index": 0
>       }
>     }
>   ]
> }
> ```

### index property{#reportingdescriptorreference-object--index-property}

A `reportingDescriptorReference` object **MAY** contain a property named `index` whose value is the array index ([sec](#array-indices)) into `theComponent.rules` ([sec](#rules-property)) or `theComponent.notifications` ([sec](#notifications-property)), according to the table in [sec](#reportingdescriptor-lookup).

> EXAMPLE 1: In this example, there is more than one rule with id `CA1711`. `index` uniquely specifies the relevant rule, whether or not there are multiple rules with the same id.
> 
> ```json
> {                            # A run object ((#run-object)).
>   "tool": {                  # See (#run-object--tool-property).
>     "driver": {              # See (#driver-property).
>       "name": "CodeScanner",
>       "rules": [             # See (#rules-property).
>         {                    # A reportingDescriptor object ((#reportingdescriptor-object)).
>           "id": "CA1711",    # See (#reportingdescriptor-object--id-property).
>           ...
>         },
>         {                    # Another reportingDescriptor with the same id.
>           "id": "CA1711",    #  rule.index points to this one.
>           ...
>         }
>       ]
>     }
>   },
>   "results": [               # See (#results-property).
>     {                        # A result object ((#result-object)).
>       "ruleId": "CA1711",    # See (#ruleid-property).
> 
>                              # A reportingDescriptorReference object.
>       "rule": {
>         "index": 1
>       }
>     }
>   ]
> }
> ```

If `index` is absent and `theResult.ruleIndex` ([sec](#ruleindex-property)) is present, `index` **SHALL** default to `theResult.ruleIndex`. If both are present, they **SHALL** be equal.

### guid property{#reportingdescriptorreference-object--guid-property}

A `reportingDescriptorReference` object **MAY** contain a property named `guid` whose value is a GUID-valued string ([sec](#guid-valued-strings)) equal to `theDescriptor.guid` ([sec](#reportingdescriptor-object--guid-property)).

### toolComponent property

A `reportingDescriptorReference` object **MAY** contain a property named `toolComponent` whose value is a `toolComponentReference` object ([sec](#toolcomponentreference-object)) that identifies `theComponent`.

If `toolComponent` is absent, `theComponent` shall be taken to be `theTool.driver` ([sec](#driver-property)).
