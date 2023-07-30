## resultProvenance object

### General{#resultprovenance-object--general}

A `resultProvenance` object contains information about the how and when `theResult` was detected.

> NOTE: This information is useful to various human and automated participants in an engineering system. For example:
> 
> - A build engineer might use the information to understand the specific tool invocation that produced the result, for example, if the violated rule should not have been configured to run at all.
> 
> - A developer reviewing results might use the information to determine how long an issue has existed in the code.
> 
> - A result management system might be responsible for associating logically identical results from one run to the next, making it possible for the developer to determine how long the result has existed. Such a result management system might populate this information.

### firstDetectionTimeUtc property

A `resultProvenance` object **MAY** contain a property named `firstDetectionTimeUtc` whose value is a string in the format specified in [§3.9](#datetime-properties), specifying the UTC date and time at which the result was first detected. It **SHOULD** specify the start time of the run in which the result was first detected, as opposed to, for example, the time within the run at which the result was actually generated.

> NOTE: Using the run’s start time makes it possible to group together results that were first detected in the same run.

### lastDetectionTimeUtc property

A `resultProvenance` object **MAY** contain a property named `lastDetectionTimeUtc` whose value is a string in the format specified in [§3.9](#datetime-properties), specifying the UTC date and time at which the result was most recently detected. It **SHOULD** specify the start time of the run in which the result was most recently detected, as opposed to, for example, the time within the run at which the result was actually generated.

> NOTE: Using the run’s start time makes it possible to group together results that were detected in the same run.

If `lastDetectionTimeUtc` is absent, its default value **SHALL** be determined as follows:

1.  If `run.invocations` is present, and if the `startTimeUtc` property ([§3.20.7](#starttimeutc-property)) is present on any of the `invocation` objects ([§3.20](#invocation-object)) in that array, then the default is the earliest of those times.

2.  Otherwise, there is no default.

### firstDetectionRunGuid property

A `resultProvenance` object **MAY** contain a property named `firstDetectionRunGuid` whose value is a GUID-valued string ([§3.5.3](#guid-valued-strings)) which **SHALL** equal the `automationDetails.guid` property ([§3.14.3](#automationdetails-property), [§3.17.4](#runautomationdetails-object--guid-property)) of the run in which `theResult` was first detected (either the current run or some previous run).

### lastDetectionRunGuid property

A `resultProvenance` object **MAY** contain a property named `lastDetectionRunGuid` whose value is a GUID-valued string ([§3.5.3](#guid-valued-strings)) which **SHALL** equal the `automationDetails.guid` property ([§3.14.3](#automationdetails-property), [§3.17.4](#runautomationdetails-object--guid-property)) of the run in which `theResult` was most recently detected (either the current run or some previous run).

### invocationIndex property

If `theRun.invocations` ([§3.14.11](#invocations-property)) is present, a `resultProvenance` object **MAY** contain a property named `invocationIndex` whose value is the array index ([§3.7.4](#array-indices)) within the `invocations` property of the `invocation` object ([§3.20](#invocation-object)) that describes the tool invocation as a result of which `theResult` was detected.

If `theRun.invocations` is absent, `invocationIndex` **SHALL** be absent.

> NOTE 1: The purpose of this property is to allow a result to be associated with the tool invocation that produced it.

If `invocationIndex` is absent and `theRun.invocations` is present and contains a single element, it **SHALL** default to 0; otherwise it **SHALL** default to -1, which indicates that the value is unknown (not set).

> NOTE 2: This provides a sensible default in the common case where there is only a single tool invocation in the run.

### conversionSources property

Some analysis tools produce output files that describe the analysis run as a whole; we refer to these as "per-run" files. Some tools produce one or more output files for each result; we refer to these as "per-result" files. Some tools produce both per-run and per-result files.

A `resultProvenance` object **MAY** contain a property named `conversionSources` whose value is an array of zero or more unique ([§3.7.3](#array-properties-with-unique-values)) `physicalLocation` objects ([§3.29](#physicallocation-object)).

If `theResult` was produced by a converter, and if the analysis tool whose output was converted to SARIF produced any per-result files for this result, then the `physicalLocation` objects in the array **SHALL** specify the relevant portions of the per-result files for this result.

Otherwise (that is, if the `run` object was not produced by a converter, or if there were no per-run files for this result), then if `conversionSources` is present, its value **SHALL** be an empty array.

Per-run files are handled by the `conversion.analysisToolLogFiles` property ([§3.22.4](#analysistoollogfiles-property)).

> NOTE: This property is intended to be useful to developers of converters, to help them debug the conversion from the analysis tool’s native output format to the SARIF format.

> EXAMPLE: Given this analysis tool’s output file:
> 
> ```xml
> <?xml version="1.0" encoding="UTF-8"?>
> <problems>
>   <problem>
>     <file></file>
>     <line>242</line>
>     ...
>     <problem_class ...>Assertions</problem_class>
>     ...
>     <description>Assertions are unreliable. ...</description>
>   </problem>
> </problems>
> ```
> 
> a SARIF converter might transform it into the following SARIF log file:
> 
> ```json
> {
>   ...
>   "runs": [
>     {
>       "tool": {
>         "driver": {
>           "name": "CodeScanner"
>         }
>       },
>       "conversion": {  # A conversion object (see §3.22).
>         ...
>       },
>       "results": [
>         {
>           "ruleId": "Assertions",
>           "message": {
>             "text": "Assertions are unreliable. ..."
>           },
>           ...
>           "provenance": {              # See §3.27.29.
>             "conversionSources": [     # An array of physicalLocation objects 
>               {                        # (§3.29).
>                 "artifactLocation": {  # See §3.29.3.
>                   "uri": "CodeScanner.log",
>                   "uriBaseId": "$LOGSROOT"
>                 },
>                 "region": {            # See §3.29.4.
>                   "startLine": 3,
>                   "startColumn": 3,
>                   "endLine": 12,
>                   "endColumn": 13,
>                   "snippet": {
>                     "text": "<problem>\n ... \n  </problem>"
>                   }
>                 }
>               }
>             ],
>             ...
>           }
>         }
>       ]
>     }
>   ]
> }
> ```
