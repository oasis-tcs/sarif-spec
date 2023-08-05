## configurationOverride object

### General{#configurationoverride-object--general}

A `configurationOverride` object modifies the effective runtime configuration of a specified `reportingDescriptor` object ([sec](#reportingdescriptor-object)), which we refer to as `theDescriptor`.

> NOTE: Together with `toolComponent.rules` ([sec](#rules-property)), the `configurationOverride` object allows the SARIF consumer to determine exactly how the tool’s analysis rules were configured during the run. This is useful in compliance scenarios where, for example, an auditor might want to confirm that a particular rule was reconfigured from a warning to an error. It might also be useful for reproducing a run.

The `configurationOverride` object’s `descriptor` property ([sec](#configurationoverride-object--descriptor-property)) identifies `theDescriptor`. Its `configuration` property ([sec](#configuration-property)) overrides the values specified in `theDescriptor.defaultConfiguration` ([sec](#defaultconfiguration-property)).

> EXAMPLE 1: In this example, rule `CA2101` is treated as a warning rather than an error.
> 
> ```json
> {                                           # A run object (§3.14).
>   "tool": {                                 # See §3.14.6.
>     "driver": {                             # See §3.18.2.
>       "name": "CodeScanner",
>       "rules": [                            # See §3.19.23.
>         {                                   # A reportingDescriptor object
>           "id": "CA2101",                   #  (§3.49).
>           "defaultConfiguration": {
>             "level": "error"
>           }
>         }
>       ]
>     }
>   },
> 
>   "invocations": [                          # See §3.14.11.
>     {                                       # An invocation object (§3.20).
>       "ruleConfigurationOverrides": [       # See §3.20.5.
>         {                                   # A configurationOverride object
>                                             #  (§3.51).
>           "descriptor": {                   # See §3.51.2.
>             "index": 0
>           },
>           "configuration": {                # See §3.51.3.
>             "level": "warning"
>           }
>         }
>       ],
>       ...
>     }
>   ]
> }
> ```

### descriptor property{#configurationoverride-object--descriptor-property}

A `configurationOverride` object **SHALL** contain a property named `descriptor` whose value is a `reportingDescriptorReference` object ([sec](#reportingdescriptorreference-object)) that identifies the `reportingDescriptor` ([sec](#reportingdescriptor-object)) whose runtime configuration is to be modified, which we refer to as `theDescriptor`.

### configuration property

A `configurationOverride` object **SHALL** contain a property named `configuration` whose value is a `reportingConfiguration` object ([sec](#reportingconfiguration-object)) each of whose properties overrides the corresponding property in `theDescriptor.defaultConfiguration` ([sec](#defaultconfiguration-property)). If any property of `configuration` is absent, the corresponding property of `theDescriptor.defaultConfiguration` is respected.
