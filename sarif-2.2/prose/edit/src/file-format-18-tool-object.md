## tool object

### General{#tool-object--general}

A `tool` object describes the analysis tool or converter that was run. The `tool` object in `run.tool` ([§3.14.6](#run-object--tool-property)) describes an analysis tool; the `tool` object in `run.conversion.tool` ([§3.14.12](#conversion-property), [§3.22.2](#conversion-object--tool-property)) describes a converter.

A tool consists of one or more "tool components," each of which consists of one or more files. We refer to the component that contains the tool’s primary executable file as the "driver." It controls the tool’s execution and typically defines a set of analysis rules. We refer to all other tool components as "extensions." Extensions can include:

- Libraries of additional rules, which we refer to as "plugins."

- Files that affect the behavior of the tool, which we refer to as "configuration files."

    NOTE: Configuration files that affect the analysis output are of particular interest in compliance scenarios, where, for example, it is necessary to demonstrate that a particular set of rules has been evaluated.

Each tool component is represented by a `toolComponent` object ([§3.19](#toolcomponent-object)).

If another tool post-processes the log file (for example, by removing certain results, or by adding information that was not known to the analysis tool), the post-processing tool **SHOULD NOT** alter any part of the tool object.

> EXAMPLE:
> 
> ```json
> {                          # A tool object.
>   "driver": {              # See §3.18.2.
>     "name": "CodeScanner",
>     "fullName": "CodeScanner 1.1, Developer Preview (en-US)",
>     "semanticVersion": "1.1.2-beta.12",
>     "version": "1.1.2b12",
>     ...
>   },
>   "extensions": [          # See §3.18.3.
>     {
>       "name": "CodeScanner Security Rules",
>       "version": "3.1",
>       ...
>     }
>   ]
> }
> ```

### driver property

A `tool` object **SHALL** contain a property named `driver` whose value is a `toolComponent` object ([§3.19](#toolcomponent-object)) that describes the component containing the tool’s primary executable file.

### extensions property

If the tool used any extensions during the run, the `tool` object **SHOULD** contain a property named `extensions` whose value is an array of one or more unique ([§3.7.3](#array-properties-with-unique-values)) `toolComponent` objects ([§3.19](#toolcomponent-object)) that describe those extensions. If the tool did not use any extensions during the run, then `extensions` **SHALL** either be absent or an empty array.