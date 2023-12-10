## configurationOverride object

### General{#configurationoverride-object--general}

A `configurationOverride` object modifies the effective runtime configuration of a specified `reportingDescriptor` object ([sec](#reportingdescriptor-object)), which we refer to as `theDescriptor`.

> NOTE: Together with `toolComponent.rules` ([sec](#rules-property)), the `configurationOverride` object allows the SARIF consumer to determine exactly how the tool’s analysis rules were configured during the run. This is useful in compliance scenarios where, for example, an auditor might want to confirm that a particular rule was reconfigured from a warning to an error. It might also be useful for reproducing a run.

The `configurationOverride` object’s `descriptor` property ([sec](#configurationoverride-object--descriptor-property)) identifies `theDescriptor`. Its `configuration` property ([sec](#configuration-property)) overrides the values specified in `theDescriptor.defaultConfiguration` ([sec](#defaultconfiguration-property)).

> EXAMPLE 1: In this example, rule `CA2101` is treated as a warning rather than an error.
>
> ```json
> {                                           # A run object ((#run-object)).
>   "tool": {                                 # See (#run-object--tool-property).
>     "driver": {                             # See (#driver-property).
>       "name": "CodeScanner",
>       "rules": [                            # See (#rules-property).
>         {                                   # A reportingDescriptor object
>           "id": "CA2101",                   #  ((#reportingdescriptor-object)).
>           "defaultConfiguration": {
>             "level": "error"
>           }
>         }
>       ]
>     }
>   },
>
>   "invocations": [                          # See (#invocations-property).
>     {                                       # An invocation object ((#invocation-object)).
>       "ruleConfigurationOverrides": [       # See (#ruleconfigurationoverrides-property).
>         {                                   # A configurationOverride object
>                                             #  ((#configurationoverride-object)).
>           "descriptor": {                   # See (#configurationoverride-object--descriptor-property).
>             "index": 0
>           },
>           "configuration": {                # See (#configuration-property).
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
