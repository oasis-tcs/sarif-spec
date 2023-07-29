## reportingDescriptorReference object

### General{#reportingdescriptorreference-object--general}

A `reportingDescriptorReference` object identifies a particular `reportingDescriptor` object ([§3.49](#reportingdescriptor-object)), which we refer to as `theDescriptor`, among all `reportingDescriptor` objects defined by `theTool`, including those defined by `theTool.driver` ([§3.18.2](#driver-property)) and `theTool.extensions` ([§3.18.3](#extensions-property)).

In some cases, there is no `reportingDescriptor` object associated with a `reportingDescriptorReference` object. In that case, the `reportingDescriptorReference` object **SHALL** contain only the `id` property ([§3.52.4](#reportingdescriptorreference-object--id-property)), and `theDescriptor` does not exist.

> EXAMPLE: In this example, a tool emits a tool execution notification that refers to a rule. The tool does not provide rule metadata. Therefore, `associatedRule` ([§3.58.3](#associatedrule-property)) contains only an `id` property, whose value is the id of the rule that failed. Similarly, the tool does not provide metadata about its notifications, so `"descriptor"` ([§3.58.2](#notification-object--descriptor-property)) contains only the id of the notification.
> 
> ```json
> {                                            # An invocation object (§3.20).
>   "toolExecutionNotifications": [            # See §3.20.21.
>     {                                        # A notification object (§3.58).
>       "descriptor": {                        # See §3.58.2.
>         "id": "CTN9999"
>       },
>       "associatedRule": {                    # See §.3.58.3
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

If metadata is present, at least one of `index` ([§3.52.5](#reportingdescriptorreference-object--index-property)) and `guid` ([§3.52.6](#reportingdescriptorreference-object--guid-property)) **SHALL** be present. If both are present, they **SHALL** identify the same `reportingDescriptor` object ([§3.49](#reportingdescriptor-object)).

### reportingDescriptor lookup

`theDescriptor` **SHALL** be located within the `toolComponent` object ([§3.19](#toolcomponent-object)) identified by the `toolComponent` property ([§3.52.7](#toolcomponent-property)), which we refer to as `theComponent`. The procedure for looking up a `toolComponent` from a `toolComponentReference` is described in [§3.54.2](#toolcomponent-lookup).

`theDescriptor` **SHALL** be located either within `theComponent.rules` ([§3.19.23](#rules-property)) or `theComponent.notifications` ([§3.19.24](#notifications-property)), according to this table:

| If the `reportingDescriptorReference` occurs in:                                                          | ... then `theDescriptor` is an element of: |
|:----------------------------------------------------------------------------------------------------------|:-------------------------------------------|
| `invocation.ruleConfigurationOverrides` ([§3.20.5](#ruleconfigurationoverrides-property))                 | `rules`                                    |
| `invocation.notificationConfigurationOverrides` ([§3.20.6](#notificationconfigurationoverrides-property)) | `notifications`                            |
| `result.rule` ([§3.27.7](#rule-property))                                                                 | `rules`                                    |
| `notification.descriptor` ([§3.58.2](#notification-object--descriptor-property))                          | `notifications`                            |
| `notification.associatedRule` ([§3.58.3](#associatedrule-property))                                       | `rules`                                    |

### id property{#reportingdescriptorreference-object--id-property}

A `reportingDescriptorReference` object **MAY** contain a property named `id` whose value is a hierarchical string ([§3.5.4](#hierarchical-strings)) that either equals `theDescriptor.id` ([§3.49.3](#reportingdescriptor-object--id-property)) or equals `theDescriptor.id` plus one additional hierarchical component.

> NOTE: This property does not participate in the lookup, but its presence improves the readability of the log file at the expense of increased file size.

If `id` is absent and `theResult.ruleId` ([§3.27.5](#ruleid-property)) is present, then `id` **SHALL** default to `theResult.ruleId`. If both are present, they **SHALL** be equal.

For more information about the semantics of `id` when `theDescriptor` is a rule, in particular the usage of the hierarchical components of `id`, see the description of `result.ruleId` ([§3.27.5](#ruleid-property)).

> EXAMPLE: In this example, the first `result` object is valid because `rule.id` (inherited from `ruleId`) equals `theDescriptor.id`. The second `result` object is also valid because `rule.id` (this time specified directly) equals `theDescriptor.id` plus one additional hierarchical component (`"ghi"`). The third `result` object is invalid because `theDescriptor.id` is not a "component-wise" prefix of `rule.id`. The fourth `result` object is invalid because `ruleId` does not equal `rule.id`.
> 
> ```json
> {                             # A run object (§3.14).
>   "tool": {                   # See §3.14.6.
>     "driver": {               # See §3.18.2.
>       "name": "CodeScanner",
>       "rules": [              # See §3.19.23.
>         {                     # A reportingDescriptor object (§3.49).
>           "id": "abc/def",    # See §3.49.3.
>           ...
>         },
>         ...
>       ]
>     }
>   },
>   "results": [                # See §3.14.23.
>     {                         # A result object (§3.27).
>       "ruleId": "abc/def",    # See §3.27.5.
>       "rule": {
>         "index": 0
>       },
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
>     }
>   ]
> }
> ```

### index property{#reportingdescriptorreference-object--index-property}

A `reportingDescriptorReference` object **MAY** contain a property named `index` whose value is the array index ([§3.7.4](#array-indices)) into `theComponent.rules` ([§3.19.23](#rules-property)) or `theComponent.notifications` ([§3.19.24](#notifications-property)), according to the table in [§3.52.3](#reportingdescriptor-lookup).

> EXAMPLE 1: In this example, there is more than one rule with id `CA1711`. `index` uniquely specifies the relevant rule, whether or not there are multiple rules with the same id.
> 
> ```json
> {                            # A run object (§3.14).
>   "tool": {                  # See §3.14.6.
>     "driver": {              # See §3.18.2.
>       "name": "CodeScanner",
>       "rules": [             # See §3.19.23.
>         {                    # A reportingDescriptor object (§3.49).
>           "id": "CA1711",    # See §3.49.3.
>           ...
>         },
>         {                    # Another reportingDescriptor with the same id.
>           "id": "CA1711",    #  rule.index points to this one.
>           ...
>         }
>       ]
>     }
>   },
>   "results": [               # See §3.14.23.
>     {                        # A result object (§3.27).
>       "ruleId": "CA1711",    # See §3.27.5.
> 
>                              # A reportingDescriptorReference object.
>       "rule": {
>         "index": 1
>       }
>     }
>   ]
> }
> ```

If `index` is absent and `theResult.ruleIndex` ([§3.27.6](#ruleindex-property)) is present, `index` **SHALL** default to `theResult.ruleIndex`. If both are present, they **SHALL** be equal.

### guid property{#reportingdescriptorreference-object--guid-property}

A `reportingDescriptorReference` object **MAY** contain a property named `guid` whose value is a GUID-valued string ([§3.5.3](#guid-valued-strings)) equal to `theDescriptor.guid` ([§3.49.5](#reportingdescriptor-object--guid-property)).

### toolComponent property

A `reportingDescriptorReference` object **MAY** contain a property named `toolComponent` whose value is a `toolComponentReference` object ([§3.54](#toolcomponentreference-object)) that identifies `theComponent`.

If `toolComponent` is absent, `theComponent` shall be taken to be `theTool.driver` ([§3.18.2](#driver-property)).
