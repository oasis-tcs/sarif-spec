## reportingConfiguration object

### General{#reportingconfiguration-object--general}

A `reportingConfiguration` object contains the information in a `reportingDescriptor` ([§3.49](#reportingdescriptor-object)) that a SARIF producer can modify at runtime, before executing its scan. We refer to the `reportingDescriptor` object whose configuration is established or modified by a `reportingConfiguration` object as `theDescriptor`.

When a `reportingConfiguration` object appears as the value of `theDescriptor.defaultConfiguration` ([§3.49.14](#defaultconfiguration-property)), it specifies `theReportingDescriptor`’s default configuration. When a `reportingConfiguration` object appears as the value of `configurationOverride.configuration` ([§3.51.3](#configuration-property)), it overrides the default values in the `reportingDescriptor` identified by `configurationOverride.descriptor` ([§3.51.2](#configurationoverride-object--descriptor-property)).

For an example, see [§3.50.5](#reportingconfiguration-object--parameters-property).

### enabled property

A `reportingConfiguration` object **MAY** contain a property named `enabled` whose value is a Boolean that specifies whether the condition described by `theDescriptor` was checked for during the scan.

If this property is absent, it **SHALL** default to `true`.

> EXAMPLE: In this example, a tool allows the user to enable or disable rules or notifications:
> 
>     SecurityScanner --disable "SEC4002,SEC4003" --enable SEC6012

### level property{#reportingconfiguration-object--level-property}

A `reportingConfiguration` object **MAY** contain a property named `level` whose value is one of the strings `"warning"`, `"error"`, `"note"`, or `"none"`, with the same meanings as when those strings appear as the value of `result.level` ([§3.27.10](#result-object--level-property)) or `notification.level` ([§3.58.6](#notification-object--level-property)).

If `level` is absent, it **SHALL** default to `"warning"`.

If `theDescriptor` describes a rule, then if `level` is present, it **SHALL** provide the value for the `level` property of any `result` object ([§3.27](#result-object)) whose `ruleIndex` ([§3.27.6](#ruleindex-property)) or `rule` property ([§3.27.7](#rule-property)), either explicitly supplied or inferred from its default, identifies `theDescriptor` and which does not itself specify a `level` property. For details of the configuration property resolution procedure, see [§3.27.10](#result-object--level-property) (which illustrates the procedure for the specific case of the `result.level` property).

If `theDescriptor` describes a notification, then if `level` is present, it **SHALL** provide the value for the `level` property of any `notification` object ([§3.58](#notification-object)) whose `descriptor` property ([§3.58.2](#notification-object--descriptor-property)) identifies `theDescriptor` and which does not itself specify a `level` property.

> EXAMPLE: In this example, a tool allows the user to override a rule or notification’s default level:
> 
>     WebScanner --level "WEB1002:error,WEB1005:warning"

### rank property{#reportingconfiguration-object--rank-property}

A `reportingConfiguration` object **MAY** contain a property named `rank` whose value is a number between `0.0` and `100.0` inclusive, with the same interpretation as the value of the `result.rank` ([§3.27.25](#result-object--rank-property)).

If `rank` is absent, it **SHALL** default to `-1.0`, which indicates that the value is unknown (not set).

If `theDescriptor` describes a rule, then if `rank` is present, it **SHALL** provide the value for the `rank` property of any `result` object ([§3.27](#result-object)) whose `ruleIndex` ([§3.27.6](#ruleindex-property)) or `rule` property ([§3.27.7](#rule-property)), either explicitly supplied or inferred from its default, identifies `theDescriptor` and which does not itself specify a `rank` property.

`rank` is not applicable to notifications.

### parameters property{#reportingconfiguration-object--parameters-property}

A `reportingConfiguration` object **MAY** contain a property named `parameters` whose value is a property bag ([§3.8](#property-bags)). This allows a `reportingDescriptor` object ([§3.49](#reportingdescriptor-object)) to define configuration information that is specific to that descriptor.

> EXAMPLE: In this example, a rule that specifies the maximum permitted source line length is parameterized by the maximum length.
> 
> ```json
> {                                  # A reportingDescriptor object (§3.49).
>   "id": "SA2707",
>   "name": {
>     "text": "LimitSourceLineLength"
>   },
>   "shortDescription": {
>     "text": "Limit source line length for readability."
>   },
>   "defaultConfiguration": {
>     "enabled": true,
>     "level": "warning",
>     "parameters": {
>       "maxLength": 120
>     }
>   }
> }
> ```
> 
> The rule provides a default value, but the tool allows the user to override it:
> 
>     StyleScanner *.c --rule-config "SA2707:maxLength=80"
