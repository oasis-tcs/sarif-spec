## runAutomationDetails object

### General{#runautomationdetails-object--general}

A `runAutomationDetails` object contains information that specifies `theRun`’s identity and role within an engineering system.

> EXAMPLE 1: In this example, a run contains the results from one nightly execution of a single security tool over a specified set of binaries. `theRun.automationDetails` describes the run. Its `id` and `guid` properties both identify the run; the former in human-readable form, the latter in a form that might be more useful in an engineering system’s database. Its `correlationGuid` property specifies the set of runs identified by *all but the last component* of `id`’s hierarchical string; that is, it identifies the set of runs `"Nightly CredScan run for sarif-sdk/master/x86/debug"`.
> 
> The run in this example is part of an aggregate of runs which together comprise the nightly execution of the engineering system’s full suite of security tools. `theRun.runAggregates[0]` describes that aggregate. Its `id` and `guid` properties both identify the aggregate. Its `correlationGuid` property specifies the collection of such aggregates identified by *all but the last component* of `id`’s hierarchical string; that is, it identifies the collection of aggregates `"Nightly security tools run for sarif-sdk/master/x86/debug"`.
> 
> ```json
> {                              # A run object ((#run-object)).
>   "automationDetails": {       # See (#automationdetails-property).
>     "description": {
>       "text": "This is the {0} nightly run of the Credential Scanner tool on
>              all product binaries in the '{1}' branch of the '{2}' repo. The
>              scanned binaries are architecture '{3}' and build type '{4}'.",
>       "arguments": [
>         "October 10, 2018",
>         "master",
>         "sarif-sdk",
>         "x86",
>         "debug"
>       ]
>     },
>     "id": "Nightly CredScan run for sarif-sdk/master/x86/debug/2018-10-05",
>     "guid": "11111111-1111-1111-8888-111111111111",
>     "correlationGuid": "22222222-2222-1111-8888-222222222222"
>   },
>   "runAggregates": [           # See (#runaggregates-property).
>     {
>       "id":
>         "Nightly security tools run for sarif-sdk/master/x86/debug/2018-10-05",
>       "guid": "33333333-3333-1111-8888-333333333333",
>       "correlationGuid": "44444444-4444-1111-8888-444444444444"
>     }
>   ]
> }
> ```

### description property{#runautomationdetails-object--description-property}

A `runAutomationDetails` object **MAY** contain a property named `description` whose value is a `message` object ([sec](#message-object)) that describes the role played within the engineering system by `theRun`.

### id property{#runautomationdetails-object--id-property}

A `runAutomationDetails` object **MAY** contain a property named `id` whose value is a hierarchical string ([sec](#hierarchical-strings)) that uniquely identifies `theRun` within the engineering system.

A result management system or other components of the engineering system **MAY** use `run.automationDetails.id` to associate the information in the log with additional information not provided by the analysis tool that produced it.

An engineering system **MAY** define any number of components and interpret them in any way desired.

> NOTE: The intent is to use the components of `id` to group results from similar runs, such as "all nightly Credential Scanner runs." A SARIF viewer might display a set of runs in a tree view, grouped by the components of `id`.

> EXAMPLE 1: A run whose `id` is `"My Nightly Run/Debug/x64/2018-10-10"` belongs to the category `"My Nightly Run/Debug/x64"`. Presumably, this is the run from October 10, 2018.

The trailing component of `id` **MAY** be empty; note that the grammar for a hierarchical identifier ([sec](#hierarchical-strings--general)) permits any component to be empty. This **SHALL** be taken to signify that the run belongs to the specified category, but that the run itself has no unique identifier.

> EXAMPLE 2: A run whose `id` is `"My Nightly Run/Debug/x64/"` belongs to the category `"My Nightly Run/Debug/x64"` but is not distinguished from other runs in that category.

`id` **MAY** consist of a single component. This **SHALL** be taken to specify a unique identifier for the run, withough specifying any category that the run belongs to.

> EXAMPLE 3: A run whose `id` is `"My Nightly Run Debug x64 2018-10-10"` has a unique identifier but cannot be inferred to belong to any category.

### guid property{#runautomationdetails-object--guid-property}

A `runAutomationDetails` object **MAY** contain a property named `guid` whose value is a GUID-valued string ([sec](#guid-valued-strings)) that provides a unique, stable identifier for `theRun`.

A result management system or other components of the engineering system **MAY** use `run.automationDetails.guid` to associate the information in the log with additional information not provided by the analysis tool that produced it.

### correlationGuid property{#runautomationdetails-object--correlationguid-property}

A `runAutomationDetails` object **MAY** contain a property named `correlationGuid` whose value is a GUID-valued string ([sec](#guid-valued-strings)) which is shared by all such runs of the same type, and differs between any two runs of different types.

If `id` ([sec](#runautomationdetails-object--id-property)) is present, `correlationGuid` **SHALL** identify the category of runs specified by all but the last hierarchical component (which **MAY** be empty according to the grammar ([sec](#hierarchical-strings--general)) for hierarchical strings) of `id`.

> NOTE: Consider an engineering system that allows engineers to define "build definitions", and that assigns a GUID to each build definition. In such a system, the build definition’s GUID could serve as `run.automationDetails.correlationGuid`. It would be the same for all runs produced by the same build definition, and different between any two runs produced by different build definitions.
