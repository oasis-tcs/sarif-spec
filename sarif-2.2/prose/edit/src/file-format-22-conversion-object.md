## conversion object

### General{#conversion-object--general}

A `conversion` object describes how a converter transformed the output of an analysis tool from the analysis tool’s native output format into the SARIF format.

> EXAMPLE 1: In this example, a converter has converted an AndroidStudio output file into a SARIF log file:
> 
> ```json
> {
>   ...
>   "runs": [
>     {
>       "tool": {
>         "driver": {
>           "name": "AndroidStudio"
>         }
>       },
>       "conversion": {
>         "tool": {                                    # See (#conversion-object--tool-property).
>           "driver": {
>             "name": "SARIF SDK Multitool"
>           }
>         },
>                                                      # See (#invocation-property).
>         "invocation":
>           "Sarif.Multitool.exe convert -t AndroidStudio northwind.log",
> 
>         "analysisToolLogFileLocation": {             # See (#analysistoollogfiles-property).
>           "uri": "northwind.log",   
>           "uriBaseId": "$LOG_DIR$"
>         } 
>       },
>       "results": [
>         ...
>       ]
>     }
>   ]
> }
> ```
> 

### tool property{#conversion-object--tool-property}

A `conversion` object **SHALL** contain a property named `tool` whose value is a `tool` object ([sec](#tool-object)) that describes the converter.

### invocation property

A `conversion` object **MAY** contain a property named `invocation` whose value is an `invocation` object ([sec](#invocation-object)) that describes the invocation of the converter.

### analysisToolLogFiles property

Some analysis tools produce one or more output files that describe the analysis run as a whole; we refer to these as "per-run" files. Some tools produce one or more output files for each result; we refer to these as "per-result" files. Some tools produce both per-run and per-result files.

A `conversion` object **MAY** contain a property named `analysisToolLogFiles` whose value is an array of zero or more unique ([sec](#array-properties-with-unique-values)) `artifactLocation` objects ([sec](#artifactlocation-object)) that specify the locations of the per-run files.

If the analysis tool did not produce any per-run files, and `analysisToolLogFiles` is present, its value **SHALL** be an empty array.

Per-result files are handled by the `resultProvenance.conversionSources` property ([sec](#conversionsources-property)).
