## result object

### General{#result-object--general}

A `result` object describes a single result detected by an analysis tool.

Each result is produced by the evaluation of a rule. If `theTool` contains a `reportingDescriptor` object ([sec](#reportingdescriptor-object)) that describes that rule, we refer to that object as `theDescriptor`, and we refer to the `toolComponent` object ([sec](#toolcomponent-object)) that defines `theDescriptor` as `theComponent`.

### Distinguishing logically identical from logically distinct results

Successive runs might detect the same condition in the code. When two `result` objects represent the same condition, we say that the results are "logically identical;" when they represent different conditions, we say that the results are "logically distinct." Two results can be logically identical even if the `result` objects are not identical. For example, if code is inserted into a file between runs, the same condition might be reported on two different lines.

To avoid reporting the same condition repeatedly, result management systems typically group results into equivalence classes such that results in any one class are logically identical and results in different classes are logically distinct.

Some result management systems do this by calculating a "fingerprint" for each result and considering results with the same fingerprint to be logically identical. A fingerprint is calculated from information contained in the result and might contain readable information from the result.

Other result management systems group results into equivalence classes *without* associating a computed fingerprint with each result, and they denote each equivalence class with an arbitrary unique identifier. This identifier is opaque: it is ­*not* calculated from information stored in the result, and hence contains no readable information about the result.

Still other result management systems compute a fingerprint, associate an arbitrary unique identifier with the fingerprint, and use that identifier rather than the fingerprint to identify the equivalence class of results.

SARIF accommodates all these types of result management systems. Result management systems that compute fingerprints **SHOULD** populate the `fingerprints` property ([sec](#fingerprints-property)). Result management systems that group results into equivalence classes based on an arbitrary unique identifier **SHOULD** populate the `correlationGuid` property ([sec](#result-object--correlationguid-property)), regardless of whether they also compute a fingerprint.

### guid property{#result-object--guid-property}

A `result` object **MAY** contain a property named `guid` whose value is a GUID-valued string ([sec](#guid-valued-strings)) defining a unique, stable identifier for the result.

Direct SARIF producers and SARIF converters **MAY** but do not need to set this property. A result management system **SHOULD** set this property when it ingests a SARIF log file. If it does so, then later, when a SARIF consumer retrieves results in SARIF format from the result management system, the result management system **SHALL** set this property to the value it assigned.

A result management system **MAY** store multiple results with identical fingerprints (see [sec](#fingerprints-property) and [sec](#normative-use-of-fingerprints-by-result-management-systems)), but the `guid` properties for those results **SHALL** be distinct.

### correlationGuid property{#result-object--correlationguid-property}

A `result` object **MAY** contain a property named `correlationGuid` whose value is a GUID-valued string ([sec](#guid-valued-strings)) that is shared by all results that are considered logically identical, and that is different between any two results that are considered logically distinct.

Direct SARIF producers and SARIF converters **SHOULD NOT** set this property. A result management system **MAY** set this property when it ingests a SARIF log file. If it does so, then later, when a SARIF consumer retrieves results in SARIF format from the result management system, the result management system **MAY** set this property to the value it assigned.

> NOTE: `correlationGuid` and `fingerprints` ([sec](#fingerprints-property)) provide two different ways for result management systems to associate results that are logically identical. See [sec](#distinguishing-logically-identical-from-logically-distinct-results) for more information.

### ruleId property

Depending on the circumstances, a `result` object either **SHALL**, **MAY**, or **SHALL NOT** contain a property named `ruleId` whose value is a hierarchical string ([sec](#hierarchical-strings)) whose leading components specify the stable identifier of the rule that was evaluated to produce the result. In addition to being stable, `ruleId` **SHOULD** be opaque.

> NOTE: `ruleId` will usually consist entirely of the rule’s stable opaque identifier. In some cases, it might be helpful to specify additional hierarchical components to more precisely describe the rule violation.

A SARIF viewer or result management system **MAY** use the additional hierarchical components to allow a user to suppress a subset of the violations of a given rule. A result management system **MAY** also use the additional components to more precisely match results between runs.

> EXAMPLE 1: In this example, the first result describes a violation of rule `CA2101`. Its `ruleId` consists entirely of the rule’s identifier. The second and third results both describe violations of rule `CA5350`. Each of their `ruleId`s specifies an additional hierarchical component that more precisely describes the rule violation. Note that `rule.index` ([sec](#rule-property), [sec](#reportingdescriptorreference-object--index-property)) for both those results is `1`; despite the additional hierarchical components in `ruleId`, both results describe violations of the same rule.
>
> A SARIF viewer or result management system might allow a user to suppress, for example, only those violations of rule `CA5350` which specify `md5` as the second hierarchical component of `ruleId`; that is, to allow the use of MD5 but still warn about the uses of other weak cryptographic algorithms.
>
> ```json
> {
>   "tool": {
>     "driver": {
>       "name": "CodeScanner",
>       "rules": [
>         {
>           "id": "CA2101",
>           "shortDescription": {
>             "text": "Specify marshaling for P/Invoke string arguments."
>           }
>         },
>         {
>           "id": "CA5350",
>           "shortDescription": {
>             "text": "Do not use weak cryptographic algorithms."
>           }
>         }
>       ]
>     }
>   },
>   "results": [
>     {
>       "ruleId": "CA2101",
>       "rule": {
>         "index": 0
>       }
>     },
>     {
>       "ruleId": "CA5350/md5",
>       "rule": {
>         "index": 1
>       }
>     },
>     {
>       "ruleId": "CA5350/sha-1",
>       "rule": {
>         "index": 1
>       }
>     }
>   ]
> }
> ```

Direct producers **SHALL** emit either or both of `ruleId` and `rule.id` ([sec](#rule-property), [sec](#reportingdescriptorreference-object--id-property)). If `rule.id` is absent, `ruleId` **SHALL** be present. If `rule.id` is present, `ruleId` **MAY** be present. If `ruleId` and `rule.id` are both present, they **SHALL** be equal.

For an example of the interaction between `ruleId` and `rule.id`, see [sec](#reportingdescriptorreference-object--id-property).

Not all existing analysis tools emit the equivalent of a `ruleId` in their output. A SARIF converter which converts the output of such an analysis tool to the SARIF format **SHOULD** synthesize `ruleId` from other information available in the analysis tool's output.

Each SARIF converter might synthesize `ruleId` in a different way. Therefore, a SARIF consumer **SHOULD NOT** attempt to compare or combine the output from different converters for the same analysis tool. See Appendix D for more information about production of SARIF by converters.

### ruleIndex property

If `theDescriptor` exists (that is, if `theTool` contains a `reportingDescriptor` object ([sec](#reportingdescriptor-object)) that describes the rule that was violated), a `result` object **MAY** contain a property named `ruleIndex` whose value is the array index ([sec](#array-indices)) of `theDescriptor` within `theComponent.ruleDescriptors` ([sec](#rules-property)). Otherwise, `ruleIndex` **SHALL** be absent.

The semantics of `ruleIndex` are identical to the semantics of `reportingDescriptorReference.index` ([sec](#reportingdescriptorreference-object--index-property)), and are described there.

If `ruleIndex` and `rule.index` ([sec](#rule-property), [sec](#reportingdescriptorreference-object--index-property)) are both present, they **SHALL** be equal.

### rule property

Depending on the circumstances, a `result` object either **SHALL NOT**, **SHOULD**, or **MAY** contain a property named `rule` whose value is a `reportingDescriptorReference` object ([sec](#reportingdescriptorreference-object)) that identifies `theDescriptor`. The procedure for looking up a `reportingDescriptor` from a `reportingDescriptorReference` is described in [sec](#reportingdescriptor-lookup).

If `theDescriptor` does not exist (that is, if `theTool` does not contain a `reportingDescriptor` object ([sec](#reportingdescriptor-object)) that describes the rule that was violated), then `rule` **SHALL NOT** be present.

If `theDescriptor` occurs in `theTool.extensions` ([sec](#extensions-property)), then `rule` **SHOULD** be present.

> NOTE 1: If `theDescriptor` occurs in `theTool.extensions` and `rule` is absent, the SARIF consumer will not be able to locate the rule metadata, even if `ruleIndex` ([sec](#ruleindex-property)) is present, because `ruleIndex` alone does not specify which extension contains `theDescriptor`.

If `theDescriptor` occurs in `theTool.driver` ([sec](#driver-property)) and `ruleIndex` is absent, then again `rule` **SHOULD** be present.

> NOTE 2: If `theDescriptor` occurs in `theTool.driver` and `ruleIndex` is absent, the SARIF consumer will not be able to locate the rule metadata within `theTool.driver.ruleDescriptors`.

If `theDescriptor` occurs in `theTool.driver` and `ruleIndex` is present, then `rule` **MAY** be present.

> NOTE 3: If `theDescriptor` occurs in `theTool.driver`, then `ruleIndex` suffices to locate the rule metadata within `theTool.driver.ruleDescriptors`.

If `rule.id` ([sec](#reportingdescriptorreference-object--id-property)) is absent, it **SHALL** default to `thisObject.ruleId`. If `rule.id` and `thisObject.ruleId` are both present, they **SHALL** be equal.

If `rule.index` ([sec](#reportingdescriptorreference-object--index-property)) is absent, it **SHALL** default to `thisObject.ruleIndex`. If `rule.index` and `thisObject.ruleIndex` are both present, they **SHALL** be equal.

If `rule` is absent, it **SHALL** default to a `reportingDescriptorReference` object whose `id` property is set to `thisObject.ruleId` and whose `index` property is set to `thisObject.ruleIndex`.

> NOTE: If the relevant rule is defined by the driver (see [sec](#tool-object--general)), which is likely to be the most common case, then `ruleId` and/or `ruleIndex` suffice to identify the rule, and take up less space in the log file than `rule`.

### taxa property{#result-object--taxa-property}

A `result` object **MAY** contain a property named `taxa` whose value is an array of zero or more unique ([sec](#array-properties-with-unique-values)) `reportingDescriptorReference` objects ([sec](#reportingdescriptorreference-object)) each of which refers to a taxon (see [sec](#taxonomies)) into which this result falls.

If the `toolComponent` object ([sec](#toolcomponent-object)) `theComponent` that defines the rule that was violated contains a `reportingDescriptor` object ([sec](#reportingdescriptor-object)) `theDescriptor` (a member of `toolComponent.rules` ([sec](#rules-property))) that describes that rule, then `thisObject.taxa` **SHALL** contain elements corresponding to those elements of `theDescriptor.relationships` ([sec](#reportingdescriptor-object--relationships-property)) that describe taxa into which this result falls. `thisObject.taxa` does not need to contain elements which correspond to `superset` or `equals` relationships; rather, the result **SHALL** implicitly be taken to fall into all the taxa described by those relationships.

> NOTE 1: See the example below for an illustration of this point. See [sec](#reportingdescriptorrelationship-object--kinds-property) for descriptions of the various types of relationships.

Otherwise (that is, if `theDescriptor` does not exist), `thisObject.taxa` **SHALL** contain elements that describe all taxa into which the result falls.

In either case, if there is no `toolComponent` that defines the taxonomy to which an element of `thisObject.taxa` refers, then that element (a `reportingDescriptorReference` object) **SHALL NOT** contain `index` ([sec](#reportingdescriptorreference-object--index-property)) or `toolComponent.index` ([sec](#toolcomponent-property), [sec](#toolcomponentreference-object--index-property)).

> NOTE 2: The rationale for this restriction is that `toolComponent.index` serves to locate the `toolComponent` object defining the rule, and `index` serves to locate the rule within that `toolComponent`. If there is no relevant `toolComponent` object, neither of those properties is meaningful. On the other hand, properties such as `id` ([sec](#reportingdescriptorreference-object--id-property)), `guid` ([sec](#reportingdescriptorreference-object--guid-property)), `toolComponent.name` ([sec](#toolcomponentreference-object--name-property)), and `toolComponent.guid` ([sec](#toolcomponentreference-object--guid-property)) are useful for readability and for identification, even if the `toolComponent` itself is absent, so they are permitted.

> EXAMPLE 1: In this example, a tool defines a custom taxonomy (see [sec](#taxonomies)) consisting of three taxa with ids `"SUP"`, `"INC1"`, and `"INC2"`. The tool emits a result that falls into the taxa `"SUP"` and `"INC2"`, but not into `"INC1"`. According to `relationships[0]`, `"SUP"` is a superset of `"CA2101"`; that is, every result that violates `"CA2101"` falls into the taxon `"SUP"`. Therefore, it is not necessary to mention `"SUP"` in `theResult.taxa`. On the other hand, according to `relationships[2]`, `"INC2"` is incomparable to `"CA2101"`; that is, the set of results that violate `"CA2101"` intersects with but is neither a superset nor a subset of the set of results that fall into the taxon `"INC2"`. Therefore, it is necessary to mention `"INC2"` in `theResult.taxa`.
>
> ```json
> {                                     # A run object ((#run-object)).
>   "tool": {
>     "driver": {
>       "name": "CodeScanner",
>       ...
>       "rules": [
>         {
>           "id": "CA2101",
>           ...
>           "relationships": [
>             {
>               "target": {
>                 "id": "SUP",
>                 "guid": "11111111-1111-1111-8888-111111111111"
>               },
>               "kinds": [
>                 "superset"
>               ]
>             },
>             {
>               "target": {
>                 "id": "INC1",
>                 "guid": "22222222-2222-1111-8888-222222222222"
>               },
>               "kinds": [
>                 "incomparable"
>               ]
>             },
>             {
>               "target": {
>                 "id": "INC2",
>                 "guid": "33333333-3333-1111-8888-333333333333"
>               },
>               "kinds": [
>                 "incomparable"
>               ]
>             }
>           ]
>         }
>       ],
>       "taxa": [
>         {
>           "id": "SUP",
>           "guid": "11111111-1111-1111-8888-111111111111",
> 
>           ...
>         },
>         {
>           "id": "INC1",
>           "guid": "22222222-2222-1111-8888-222222222222",
>           ...
>         },
>         {
>           "id": "INC2",
>           "guid": "33333333-3333-1111-8888-333333333333",
>           ...
>         }
>       ]
>     }
>   },
>   "results": [
>     {
>       "ruleId": "CA2101",
>       "rule": {
>         "index": 0
>       },
>       "taxa": [
>         {
>           "id": "INC2",
>           "guid": "33333333-3333-1111-8888-333333333333"
>         }
>       ]
>     }
>   ]
> }
> ```

### kind property{#result-object--kind-property}

A `result` object **MAY** contain a property named `kind` whose value is one of a fixed set of strings that specify the nature of the result.

If present, the `kind` property **SHALL** have one of the following values, with the specified meanings:

- `"pass"`: The rule specified by `ruleId` ([sec](#ruleid-property)), `ruleIndex` ([sec](#ruleindex-property)), and/or `rule` ([sec](#rule-property)) was evaluated, and no problem was found.

- `"open"`: The specified rule was evaluated, and the tool concluded that there was insufficient information to decide whether a problem exists.

    NOTE 1: This value is used by proof-based tools. Sometimes such a tool can prove that there is no violation (`kind` = `"pass"`), sometimes it can prove that there is a violation (`kind` = `"fail"`), and sometimes it does not detect a violation but is unable to prove that there is none (`kind` = `"open"`). In such a tool, a `kind` value of `"open"` might be an indication that the user should add additional assertions to enabe the tool to determine if there is a violation.

- `"informational"`: The specified rule was evaluated and produced a purely informational result that does not indicate the presence of a problem. (See the example below.)

- `"notApplicable"`: The rule specified by `ruleId` was not evaluated, because it does not apply to the analysis target.

> EXAMPLE 1: In this example, a binary checker has a rule that applies to 32-bit binaries only. It produces a `"notApplicable"` result if it is run on a 64-bit binary. It also has a rule that checks the compiler version and produces an informational result:
>
> ```json
> "results": [
>   {
>     "ruleId": "ABC0001",
>     "kind": "notApplicable",
>     "message": {
>       "text": "\"MyTool64.exe\" was not evaluated for rule ABC0001
>                because it is not a 32-bit binary."
>     },
>     "locations": [
>       {
>         "physicalLocation": {
>           "uri": "file://C:/bin/MyTool64.exe"
>         }
>       }
>     ]
>   },
>   {
>     "ruleId": "ABC0002",
>     "kind": "informational",
>     "message": {
>       "text": "\"MyTool64.exe\" was compiled with Example Corporation
>                Compiler version 10.2.2."
>     },
>     "locations": [
>       {
>         "physicalLocation": {
>           "uri": "file://C:/bin/MyTool64.exe"
>         }
>       }
>     ]
>   }
> ]
> ```

- `"review"`: The result requires review by a human user to decide if it represents a problem.

    NOTE 2: This value is used by tools that are unable to check for certain conditions, but that wish to bring to the user’s attention the possibility that there might be a problem. For example, an accessibility checker might produce a result with the message "Do not use color alone to highlight important information," with `kind` = `"review"`. A user might address this issue by visually inspecting the UI.

- `"fail"`: The result represents a problem whose severity is specified by the `level` property ([sec](#result-object--level-property)).

If `kind` is absent, it **SHALL** default to `"fail"`.

If `level` has any value other than `"none"` and `kind` is present, then `kind` **SHALL** have the value `"fail"`.

### level property{#result-object--level-property}

A `result` object **MAY** contain a property named `level` whose value is one of a fixed set of strings that specify the severity level of the result.

If present, the `level` property **SHALL** have one of the following values, with the specified meanings:

- `"warning"`: The rule specified by `ruleId` was evaluated and a problem was found.

- `"error"`: The rule specified by `ruleId` was evaluated and a serious problem was found.

- `"note"`: The rule specified by `ruleId` was evaluated and a minor problem or an opportunity to improve the code was found.

- `"none"`: The concept of "severity" does not apply to this result because the `kind` property ([sec](#result-object--kind-property)) has a value other than `"fail"`.

> EXAMPLE 1: In this example, the tool reports an opportunity to improve the code.
>
> ```json
> "results": [
>   {
>     "ruleId": "ABC0003",
>     "kind": "fail",
>     "level": "note",
>     "message": {
>       "text": "Consider using 'nameof(start)' instead of hard-coding
>                the parameter name 'start'."
>     },
>     "locations": [
>       {
>         "physicalLocation": {
>           "uri": "file:///C:/code/a.cs",
>           "region": {
>             "startLine": 6
>           }
>         }
>       }
>     ]
>   }
> ]
> ```

If `kind` ([sec](#result-object--kind-property)) has any value other than `"fail"`, then if `level` is absent, it **SHALL** default to `"none"`, and if it is present, it **SHALL** have the value `"none"`.

If `kind` has the value `"fail"` and `level` is absent, then `level` **SHALL** be determined by the following procedure:

IF rule ([sec](#rule-property)) is present THEN

&emsp;&emsp;LET `theDescriptor` be the `reportingDescriptor` object ([sec](#reportingdescriptor-object)) that it specifies.

&emsp;&emsp;# Is there a configuration override for the `level` property?

&emsp;&emsp;IF `result.provenance.invocationIndex` ([sec](#provenance-property), [sec](#invocationindex-property)) is >= 0 THEN

&emsp;&emsp;&emsp;&emsp;LET `theInvocation` be the `invocation` object ([sec](#invocation-object)) that it specifies.

&emsp;&emsp;&emsp;&emsp;IF `theInvocation.ruleConfigurationOverrides` ([sec](#ruleconfigurationoverrides-property)) is present

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;AND it contains a `configurationOverride` object ([sec](#configurationoverride-object)) whose

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;`descriptor` property ([sec](#configurationoverride-object--descriptor-property)) specifies `theDescriptor` THEN

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;LET `theOverride` be that `configurationOverride` object.

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;IF `theOverride.configuration.level` ([sec](#configuration-property), [sec](#reportingconfiguration-object--level-property)) is present THEN

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;Set `level` to `theConfiguration.level`.

&emsp;&emsp;ELSE

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;# There is no configuration override for `level`. Is there a default configuration for it?

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;IF `theDescriptor.defaultConfiguration.level` ([sec](#defaultconfiguration-property), [sec](#reportingconfiguration-object--level-property)) is present THEN

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;SET level to `theDescriptor.defaultConfiguration.level`.

IF `level` has not yet been set THEN

&emsp;&emsp;SET `level` to `"warning"`.

### message property{#result-object--message-property}

A `result` object **SHALL** contain a property named `message` whose value is a `message` object ([sec](#message-object)) that describes the result.

The `message` property **SHOULD** provide sufficient details to allow an end user to resolve any problem that the result might indicate. In particular, it **SHALL** include all of the following information that is available and relevant to the result:

- Information sufficient to identify the analysis target, and the location within the target where the problem occurred.

- The condition within the analysis target that led to the problem being reported.

- The risks potentially associated with not fixing the problem.

- The full range of responses to the problem that the end user could take (including the definition of conditions where it might be appropriate not to fix the problem, or to conclude that the result is a false positive).

> EXAMPLE 1: This is an example of a `message`:
>
> ```json
> "results": [
>   {
>     "message": {
>       "text": "Deleting member 'x' of variable 'y' may compromise
>                performance on subsequent accesses of 'y'. Consider
>                setting object member 'x' to null instead, unless this
>                object is a dictionary or if runtime semantics otherwise
>                dictate that the existence of a null member is distinct
>                from one that is not present at all. This violation can
>                also be ignored for infrequently called code paths."
>     }
>   }
> ]
> ```

See [sec](#message-string-lookup) for the procedure for looking up a message string from a `message` object, in particular, for the case where the `message` object occurs as the value of `result.message`.

> EXAMPLE 2: In this example, `message.id` refers to the property named `default` defined in the `messageStrings` property of the `reportingDescriptor` object identified by `"CA2101"`.
>
> ```json
> {                                 # A run object ((#run-object)).
>   "tool": {                       # See (#run-object--tool-property).
>     "driver": {                   # See (#driver-property).
>       "name": "CodeScanner",
>       "rules": [                  # See (#rules-property).
>         {                         # A reportingDescriptor object ((#reportingdescriptor-object)).
>           "id": "CA2101",
>           "messageStrings": {
>             "default": {          # A multiformatMessageString object ((#multiformatmessagestring-object)).
>               "text": "The default message for this rule.",
>               "markdown": "The default message for *this* rule."
>             },
>             "special": {
>               "text": "Another message, for special cases.",
>               "markdown": "Another message, for *special*   cases."
>             }
>           }
>         }
>       ]
>     }
>   },
>   "results": [
>     {                             # A result object ((#result-object)).
>       "ruleId": "CA2101",
>       "rule": {
>         "index": 0
>       },
>       "message": {
>         "id": "default"
>       },
>       ...
>     }
>   ]
> }
> ```

### locations property{#result-object--locations-property}

A `result` object **SHOULD** contain a property named `locations` whose value is an array of zero or more `location` objects ([sec](#location-object)) each of which specifies a location where the result occurred.

> NOTE 1: In rare circumstances, it might not be possible to specify a location for a result. However, the `locations` property contains very valuable information for anyone who needs to diagnose and correct the condition described by the result, so the authors of analysis tools should make every effort to provide it.

> EXAMPLE 1: If a C++ analyzer detects that no file defines a global function `main`, then that result cannot be associated with a file.

> NOTE 2: The `locations` array is not defined to contain unique ([sec](#array-properties-with-unique-values)) elements because some tools report a line number but not a column number for a result’s location. Such a tool might report the same result twice on the same line, in some cases producing multiple identical `location` objects.

The `locations` array **SHALL NOT** contain more than one element unless the condition indicated by the result, if any, can only be corrected by making a change at every location specified in the array.

> EXAMPLE 2: In C#, which supports "partial" classes, portions of the declaration of a single class can occur at multiple locations in the source code. If an analysis tool reports that the name of such a class does not conform to a specified convention, then the resulting log file might contain a single result object, which would contain a `locations` array each of whose elements specifies a location in the source code where the class name occurs.

The `locations` array **SHALL NOT** be used to specify distinct occurrences of the same result which can be corrected independently.

> EXAMPLE 3: Consider an analysis tool which locates misspelled words in documentation, and suppose this tool scans a document in which the same word is misspelled in two distinct locations. Then the resulting log file must contain two distinct `result` objects each of which contains a `locations` array containing a single `location` object specifying the location of one instance of the misspelled word.  
  
> EXAMPLE 4: In contrast, consider a tool which locates misspelled words in variable names. If the tool detects a misspelled variable name, it might produce a single `result` object whose `locations` array contains the location of every reference to the variable, since fixing some but not all of the references would cause a compilation error.

### analysisTarget property

If the analysis target differs from the result file, a `result` object **SHOULD** contain a property named `analysisTarget` whose value is an `artifactLocation` object ([sec](#artifactlocation-object)) that specifies the analysis target.

If the analysis target and the result file are the same, the `analysisTarget` property **SHOULD** be absent.

> EXAMPLE 1: In this example, the tool’s analysis target was the file mouse.c. During the scan, the tool detected a result in the included file mouse.h.
>
> ```json
> {                                 # A result object ((#result-object)).
>   "analysisTarget": {             # An artifactLocation object ((#artifactlocation-object)).
>     "uri": "input/mouse.c",
>     "uriBaseId": "SRCROOT"
>   },
> 
>   "locations": [                  # See (#result-object--locations-property).
>     {                             # A location object ((#location-object)).
>       "physicalLocation": {       # See (#physicallocation-property).
>         "artifactLocation": {     # An artifactLocation object.
>           "uri": "input/mouse.h",
>           "uriBaseId": "SRCROOT"
>         },
> 
>         "region": {
>           "startLine": 42
>         }
>       }
>     }
>   ]
> }
> ```

### webRequest property{#result-object--webrequest-property}

A `result` object **MAY** contain a property named `webRequest` whose value is a `webRequest` object ([sec](#webrequest-object)) that describes the HTTP request which led to this result.

> NOTE: This property is primarily useful to web analysis tools.

### webResponse property{#result-object--webresponse-property}

A `result` object **MAY** contain a property named `webResponse` whose value is a `webResponse` object ([sec](#webresponse-object)) that describes the response to the HTTP request which led to this result.

> NOTE: This property is primarily useful to web analysis tools.

### fingerprints property

A `result` object **MAY** contain a property named `fingerprints` whose value is an object ([sec](#object-properties)).

Each property value in this object **SHALL** be a string that provides a stable identifier for the result. This identifier **SHALL**, to the extent that it is feasible, be the same for all results that are logically identical, and different for any two results that are logically distinct. This requirement is intended to ensure that a fingerprint is resistant to changes that do not affect the logical identity of the result, such as the location of the root of a source code enlistment, or the line number where a result appears in a source file.

Each property name in this object **SHALL** be a versioned hierarchical string ([sec](#versioned-hierarchical-strings)). A result management system **MAY** use the property names to identify the method used to calculate the fingerprint.

> EXAMPLE 1: In this example, the producer has calculated a fingerprint using version 2 of a fingerprinting method it refers to as `"stableResultHash"`:
>
> ```json
> {
>     "fingerprints": {
>       "stableResultHash/v2": "097886bc876fe"
>     }
> }
> ```

When a result management system uses fingerprint information to determine whether two results are logically identical, it **SHOULD** use the latest version of the fingerprint available in both results.

> EXAMPLE 2: In this example, one result has values for versions 1 and 2 of the "context region hash" fingerprint. Another result has values for versions 2 and 3. A result management system would use version 2 (the greatest common version) to compare the two results.
>
> ```json
> {                                  # A run object ((#run-object)).
>   "results": [                     # See (#results-property).
>     {                              # A result object.
>       "fingerprints": {
>         "stableResultHash/v1": "1234567900abc",
>         "stableResultHash/v2": "234567900abcd"
>       }
>     },
>     {
>       "fingerprints": {
>         "stableResultHash/v2": "234567900abcd",
>         "stableResultHash/v3": "34567900abcde"
>       }
>     }
>   ]
> }
> ```

> NOTE: This property is an array, rather than a single string, for two reasons:

- To allow a result management system to continue to support outdated fingerprinting algorithms while upgrading to a newer, more reliable algorithm.

- Less likely but possible, to allow multiple result management systems to record their final fingerprints.

A direct SARIF producer **SHOULD NOT** populate this property. A SARIF converter **MAY** populate this property if the analysis tool’s native output format provides a value that qualifies as a fingerprint (a stable identifier for the result). A result management system **MAY** populate this property when it ingests a SARIF file. If it does so, then later, when a SARIF consumer retrieves results in SARIF format from the result management system, the result management system **MAY** set this property to the value it assigned.

[sec](#normative-use-of-fingerprints-by-result-management-systems) provides requirements for how a result management system computes fingerprints.

> NOTE: `fingerprints` and `correlationGuid` ([sec](#result-object--correlationguid-property)) provide two different ways for result management systems to associate results that are logically identical. See [sec](#distinguishing-logically-identical-from-logically-distinct-results) for more information.

### partialFingerprints property

A `result` object **MAY** contain a property named `partialFingerprints` whose value is an object ([sec](#object-properties)).

Each property value in this object **SHALL** be a string that contributes to the stable, unique identity, or "fingerprint," of the result (see [sec](#fingerprints-property)). Appendix B explains how a result management system can compute these fingerprints.

Each property name in this object **SHALL** be a versioned hierarchical string ([sec](#versioned-hierarchical-strings)). A SARIF producer **MAY** use the property name to identify the nature of the information used to compute the partial fingerprint.

> EXAMPLE 1: In this example, the producer has calculated a partial fingerprint using version 3 of a partial fingerprint value it refers to as `"prohibitedWordHash"`:
>
> ```json
> {                                 # A result object ((#result-object)).
>   "partialFingerprints": {
>     "prohibitedWordHash/v3": "097886bc876fe"
>   }
> }
> ```

When a result management system uses partial fingerprint information to determine whether two results are logically identical, it **SHOULD** use the latest version of the partial fingerprint available in both results.

> EXAMPLE 2: In this example, one result has values for versions 1 and 2 of the "prohibited word hash" partial fingerprint. Another result has values for versions 2 and 3. A result management system would use version 2 (the greatest common version) to compare the two results.
>
> ```json
> {                                  # A run object ((#run-object)).
>   "results": [                     # See (#results-property).
>     {                              # A result object.
>       "partialFingerprints": {
>         "prohibitedWordHash/v1": "1234567900abc",
>         "prohibitedWordHash/v2": "234567900abcd"
>       }
>     },
>     {
>       "partialFingerprints": {
>         "prohibitedWordHash/v2": "234567900abcd",
>         "prohibitedWordHash/v3": "34567900abcde"
>       }
>     }
>   ]
> }
> ```

A result management system **MAY** use any algorithm to combine the information contained in the various partial fingerprints. (For example, it might decide that two results are logically identically if any one of their partial fingerprints match, or only if a majority of them match, or only if all of them match.)

To make use of the information, if any, embodied in the property names, a result management system requires knowledge of the naming convention used by the SARIF producer. A result management system with that knowledge **MAY** use the property names to decide which partial fingerprints to include in its fingerprint computation. A result management system lacking that knowledge **SHOULD NOT** attempt to interpret the information embodied in the partial fingerprint names.

Because result management systems might come to depend on the choice of property names, SARIF producers that use property names to identify the nature of the information used to compute the partial fingerprint **SHOULD** adhere to the following guidelines:

- Choose meaningful property names that describe the information used to compute the partial fingerprint.

- Document the property names.

- When introducing a partial fingerprint computed with a different approach, associate it with a new property name.

- Avoid removing existing property names and partial fingerprints, since existing result management systems might rely on them.

> EXAMPLE 3: In this example, a SARIF-producing document checker has computed a partial fingerprint that hashes a word that should not appear in a document together with the document’s language.
>
> ```json
> {                           # A result object.
>   ...
>   "partialFingerprints": {
>     "wordPlusLangHash":
>       "2c26b46b68ffc68ff99b453c1d30413413422d706483bfa0f98a5e886266e7ae"
>   }
> }
> ```

> EXAMPLE 4. In this example, the SARIF producer has chosen an arbitrary value for the property name.
>
> ```
> {                           # A result object
>   ...
>   "partialFingerprints": {
>     "1": "56eaf900cc8f6"
>   }
> }
> ```

### codeFlows property

A `result` object **MAY** contain a property named `codeFlows` whose value is an array of zero or more `codeFlow` objects ([sec](#codeflow-object)). The `codeFlows` property is intended for use by analysis tools that provide execution path details that illustrate a possible problem in the code.

> NOTE: The SARIF file format allows multiple `codeFlow` objects within a single `result` object to allow for the possibility that more than one code flow might be relevant to a single result.

### graphs property{#result-object--graphs-property}

A `result` object **MAY** contain a property named `graphs` whose value is an array of zero or more unique ([sec](#array-properties-with-unique-values)) `graph` objects ([sec](#graph-object)). A `graph` object represents a directed graph: a network of nodes and directed edges that describes some aspect of the structure of the code (for example, a call graph).

A `graph` object defined at the `result` level **SHALL** be referenced only by `graphTraversal` objects ([sec](#graphtraversal-object)) defined in the `graphTraversals` property ([sec](#graphtraversals-property)) of the `result` object in which it is defined. This contrasts with `graph` objects defined at the `run` level ([sec](#run-object--graphs-property)), which **MAY** be referenced by `graphTraversal` objects defined in the `graphTraversals` property of any `result` object in `theRun`.

### graphTraversals property

If a `result` object contains a `graphs` property ([sec](#result-object--graphs-property)), or if `theRun` contains a `graphs` property ([sec](#run-object--graphs-property)), then the `result` object **MAY** contain a property named `graphTraversals` whose value is an array of zero or more unique ([sec](#array-properties-with-unique-values)) `graphTraversal` objects ([sec](#graphtraversal-object)). If neither the `result` object nor `theRun` contains a `graphs` property, the `graphTraversals` property **SHALL** be absent. A graph traversal is a path through the code that visits one or more nodes in a specified graph.

### stacks property

A `result` object **MAY** contain a property named `stacks` whose value is an array of zero or more unique ([sec](#array-properties-with-unique-values)) `stack` objects ([sec](#stack-object)). The `stacks` property is intended for use by analysis tools that compute or collect call stack information in the process of producing results.

> NOTE: The SARIF file format allows multiple `stack` objects within a single `result` object to allow for the possibility that more than one call stack might be relevant to a single result.

### relatedLocations property

A `result` object **MAY** contain a property named `relatedLocations` whose value is an array of zero or more unique ([sec](#array-properties-with-unique-values)) `location` objects ([sec](#location-object)) each of which represents a location relevant to understanding the result.

> EXAMPLE 1: Suppose that a tool for analyzing JavaScript™ has a rule that reports a problem when a variable declared in an inner scope hides a variable with the same name in an enclosing scope. The tool would report the problem on the line where the inner variable is declared. The tool could choose to add an element to the `relatedLocations` array, specifying the location where the outer variable was declared.  
>
> The result might appear in the log file like this:
>
> ```json
> "results": [
>   {
>     "ruleId": "JS3056",
>     "level": "error",
>     "message": {
>       "text": "Name 'index' cannot be used in this scope because
>                it would give a different meaning to 'index'
>                ([declared here](0))."
>     },
>     "locations": [
>       {
>         "physicalLocation": {
>           "uri": "file:///C:/Code/a.js",
>           "region": {
>             "startLine": "6",
>             "startColumn": "10"
>           }
>         }
>       }
>     ],
>     "relatedLocations": [   # An array of location objects ((#location-object)).
>       {                     # A location object.
>         "id": 0,
>         "message": {
>           "text": "The previous declaration of 'index' was here."
>         },
>         "physicalLocation": {
>           "uri": "file:///C:/Code/a.js",
>           "region": {
>             "startLine": "2",
>             "startColumn": "6"
>           }
>         }
>       }
>     ]
>   },
>     ...
> ]
> ```
>
> The tool might write messages to the console like this:
>
> ```console
> C:\Code\a.js(6,10-10): error : JS3056: Name 'index' cannot be used in this scope because it would give a different meaning to 'index'.
> C:\Code\a.js(2,6-6): info : JS3056: The previous declaration of 'index' was here.
> ```

### suppressions property

A `result` object **MAY** contain a property named `suppressions` whose value is an array of zero or more unique ([sec](#array-properties-with-unique-values)) `suppression` objects ([sec](#suppression-object)) each of which describes a request to "suppress" a result (that is, to exclude it from result lists, bug counts, *etc.*).

If `suppressions` is absent, it **SHALL** default to `null.`

The presence of an array value, whether or not the array is empty, **SHALL** mean that suppression information is available for the result. In this case, if the array is empty, a consumer **SHALL** treat the result as not suppressed. If the array is non-empty, a consumer that needs to determine the result’s suppression state **SHALL** examine the `status` properties ([sec](#status-property)) of the `suppression` objects in the array.

The absence of an array value, or the presence of a `null` value, **SHALL** mean that suppression information is not available for the result. A SARIF consumer **SHALL** treat such a result as not suppressed.

The `suppressions` values for all `result` objects in `theRun` **SHALL** be either all `null` or all non-`null`.

> NOTE: The rationale is that an engineering system will generally evaluate all results for suppression, or none of them. Requiring that the `suppressions` values be either all `null` or all non-`null` enables a consumer to determine whether suppression information is available for the run by examining a single `result` object.

### baselineState property

A `result` object **MAY** contain a property named `baselineState` whose value is a string that specifies the state of this result with respect to some previous run, which we refer to as the "baseline run."

If `theRun.baselineGuid` ([sec](#baselineguid-property)) is present, its value **SHALL** specify the baseline run.

This property **SHALL** have one of the following values, with the specified meanings:

- `"new"`: This result was detected in the current run but was not detected in the baseline run.

- `"unchanged"`: This result was detected both in the current run and in the baseline run, and it did not change between those two runs in any way that the tool considers significant.

- `"updated"`: This result was detected both in the current run and in the baseline run, but it changed between those two runs in a way that the tool considers significant.

- `"absent"`: This result was detected in the baseline run but was not detected in the current run.

> NOTE 1: The purpose of `baselineState` is to allow (for example) a measurement of how many new results were introduced in the run, and how many previously existing results no longer appear.
>
> To assign a value to `baselineState`, a tool needs a way to determine whether a result is logically "the same", in some sense, as a result that appeared in the baseline. [sec](#normative-use-of-fingerprints-by-result-management-systems) discusses how a result management system can assign a "fingerprint" to each result. See also the description of the `fingerprints` ([sec](#fingerprints-property)) and `partialFingerprints` ([sec](#partialfingerprints-property)) properties.
>
> An analysis tool that works together with such a result management system can use the fingerprint to determine whether two results are logically the same; two results with the same fingerprint are considered logically the same.

> NOTE 2: A result management system might respond to a "new" result by filing an issue in a bug tracking system. It might respond to an "updated" result by editing the details of an existing issue in the bug tracking system, or by attaching an updated SARIF log to the issue. It might respond to an "absent" result by resolving the issue. It might take no action at all for an "unchanged" issue, or it might simply update its internal information about the range of runs that contained the result.

If `baselineState` is present on any `result` object in `theRun`, it **SHALL** be present on every such `result` object.

> NOTE 3: The presence of `baselineState` on any `result` implies that the SARIF producer performed a comprehensive comparison between the results in the current run and those in some previous run. A SARIF consumer is entitled to expect that the differencing operation produced a `baselineState` value for every result.
>
> This is conceptually similar to a tool that compares two text files, and for every line, concludes that it exists in the left-hand file, the right-hand file, or both. The tool must provide this information for every line in both files; it cannot leave some lines "undetermined."

### rank property{#result-object--rank-property}

A `result` object **MAY** contain a property named `rank` whose value is a number between `0.0` and `100.0` inclusive, representing the priority or importance of the result. `0.0` is the lowest priority and `100.0` is the highest.

`rank` is only meaningful if `kind` ([sec](#result-object--kind-property)) has the value `"fail"`.

If `kind` has the value `"fail"`, then if `rank` is absent, it **SHALL** default to the value determined by the procedure defined for `level` ([sec](#result-object--level-property)), except throughout the procedure, replace `"level"` with `"rank"` and replace `"warning"` with `-1.0`.

If `kind` has any other value, then `rank` **SHALL** be absent.

If `rank` is absent, it **SHALL** default to `-1.0`, which indicates that the value is unknown (not set).

> NOTE: `rank` values produced by different tools are in general not commensurable. If Tool A produces one result with rank `0.65` and a second result with rank `0.70`, the consumer is entitled to assume that the second result is of higher priority than the first. But if Tool A produces a result with rank `0.65` and Tool B produces a result with rank `0.70`, the result produced by Tool B might or might not be of higher priority than the result produced by Tool A. In an engineering system that aggregates results from multiple tools, rank values might need to be adjusted, either automatically or by end users, so that rank values from different tools can be interleaved in a meaningful way.

### attachments property

A `result` object **MAY** contain a property named `attachments` whose value is an array of zero or more unique ([sec](#array-properties-with-unique-values)) `attachment` objects ([sec](#attachment-object)) each of which describes an artifact relevant to the detection of the result.

### workItemUris property

A `result` object **MAY** contain a property named `workItemUris` whose value is either `null` or an array of zero or more unique ([sec](#array-properties-with-unique-values)) strings each of which contains the absolute URI [cite](#RFC3986) of a work item associated with this result.

If `workItemUris` is absent, it **SHALL** default to `null`.

An empty array **SHALL** mean that there are no work items associated with this result. `null` **SHALL** mean that the set of work items associated with this result, if any, is not known.

The `workItemUris` values for all `result` objects in `theRun` **SHALL** be either all `null` or all non-`null`.

> NOTE 1: The rationale is that an engineering system will generally track work item status for all results or for none of them. Requiring that the `workItemUris` values be either all `null` or all non-`null` enables a consumer to determine whether work item information is available for the run by examining a single `result` object.

> NOTE 2: Result management systems are likely to generate work items from at least some of the results in a SARIF log file. Depending on the engineering system, these work items might take the form of Git issues, Jira tickets, TFS work items, or the equivalent in other work item tracking systems.

### hostedViewerUri property

A `result` object **MAY** contain a property named `hostedViewerUri` whose value is a string containing an absolute URI [cite](#RFC3986) at which the result can be viewed. The URI **SHALL** be valid as of the time the tool generated this result. It is not guaranteed to be valid at later times (for example, the hosting environment might not keep results older than a specified age).

> NOTE: This property can be used by tools that provide an online viewing experience for the results they generate. This experience might be specifically designed to display the results from that tool, as opposed to a generic SARIF viewer that displays results from any tool that produces SARIF.

### provenance property

A `result` object **MAY** contain a property named `provenance` whose value is a `resultProvenance` object ([sec](#resultprovenance-object)) that contains information about how and when the result was detected.

### fixes property

A `result` object **MAY** contain a property named `fixes` whose value is an array of zero or more unique ([sec](#array-properties-with-unique-values)) `fix` objects ([sec](#fix-object)).

### occurrenceCount property

A `result` object **MAY** contain a property named `occurrenceCount` whose value is a positive integer specifying the number of times a result with `theResult.correlationGuid` ([sec](#result-object--correlationguid-property)) has been observed.

> NOTE: This property is intended for the scenario where multiple SARIF files are being merged into a single SARIF file, with the intent that each logically distinct result (see [sec](#distinguishing-logically-identical-from-logically-distinct-results)) occurs only once in the merged file. In that case, the system performing the merge would select one occurrence of each logically distinct result to serve as the exemplar for that class of results, and it would set `occurrenceCount` on that instance to the number of times a result with that `correlationGuid` occurred in the input files.
>
> This property can also be useful even in the context of a single log file. Consider an accessibility checker that detects an accessibility problem at a particular location. Suppose the checker has access to activity logs that trace user paths through the application. The checker could use those logs to determine how many times users encountered the location with the accessibility problem, and store that information in `occurrenceCount`.
