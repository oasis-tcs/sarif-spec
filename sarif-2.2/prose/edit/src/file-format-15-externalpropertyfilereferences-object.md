## externalPropertyFileReferences object

### General{#externalpropertyfilereferences-object--general}

An `externalPropertyFileReferences` object contains information that enables a SARIF consumer to locate the external property files (see [sec](#rationale)) that contain the values of all externalized properties associated with `theRun`.

### Rationale

In some engineering environments, a single tool run might analyze hundreds of thousands of files and produce millions of results. This causes problems for both producers and consumers of such large SARIF log files:

- The log file might be too large for a consumer to hold in memory and might take several minutes to read.

- During production, some information (such as the complete set of artifacts that were analyzed, the complete set of rules that were violated, or the end time of the run) cannot be known until the run is complete. Therefore, it is likely to be serialized at the end of the log file. However, consumers might need to access some of that information before reading the entire file. For example, a SARIF viewer might need to display rule metadata along with each result it displays, or to display the start and end times of a set of tool runs.

To mitigate these problems, SARIF allows certain properties of a `run` object and its sub-objects to be stored in separate files. We refer to these files as "external property files", and we refer to the file containing the `run` object itself as the "root file". We refer to a property that can be stored in an external property file as an "externalizable property." We refer to a property that *has* been stored in an external property file as an "externalized property."

The format of an external property file is described in [sec](#external-property-file-format)

A SARIF consumer **SHALL** treat the value of an object-valued property stored in an external property file exactly as if it had appeared inline in the root file as the value of the corresponding property.

A SARIF consumer **SHALL** treat the value of an array-valued property stored in an external property file exactly as if its elements had appeared inline in the root file, appended to the existing value, if any, of that property.

> NOTE: This allows a SARIF producer to begin writing the elements of an array-valued property to the root file, and then, if the file grows too large, to "spill" the additional elements into one or more external property files.

### Properties

The following table lists all the externalizable properties together with their corresponding property names in the `externalPropertyFileReferences` object:

| Externalizable property   | Property name            | Type   |
|:--------------------------|:-------------------------|:-------|
| `run.addresses`           | `addresses`              | array  |
| `run.artifacts`           | `artifacts`              | array  |
| `run.conversion`          | `conversion`             | object |
| `run.graphs`              | `graphs`                 | array  |
| `run.invocations`         | `invocations`            | array  |
| `run.logicalLocations`    | `logicalLocations`       | array  |
| `run.policies`            | `policies`               | array  |
| `run.properties`          | `externalizedProperties` | object |
| `run.webRequests`         | `webRequests`            | array  |
| `run.webResponses`        | `webResponses`           | array  |
| `run.results`             | `results`                | array  |
| `run.taxonomies`          | `taxonomies`             | array  |
| `run.threadFlowLocations` | `threadFlowLocations`    | array  |
| `run.translations`        | `translations`           | array  |
| `run.tool.driver`         | `driver`                 | object |
| `run.tool.extensions`     | `extensions`             | array  |

> NOTE 1: `run.properties` is externalized under the property name `externalizedProperties` to allow this object to have a property bag named `properties`, consistent with all other objects in this document.

> NOTE 2: Note that `run.conversion.tool.driver` and `run.conversion.tool.extensions` are not separately externalizable. Rather, the `run.conversion` property as a whole is externalizable.

Every externalizable property whose type is shown in the table as "object" **SHALL**, if externalized, be stored in a single external property file. In that case, the value of the corresponding property in `externalPropertyFileReferences` **SHALL** be an `externalPropertyFileReference` object ([sec](#externalpropertyfilereference-object)) specifying the location of the external property file.

Every externalizable property whose type is shown in the table as "array" **SHALL**, if externalized, be stored in one or more external property files. In that case, the value of the corresponding property in `externalPropertyFileReferences` **SHALL** be an array of zero or more `externalPropertyFileReference` objects specifying the locations of those external property files.

> EXAMPLE 1: In this example, `run.conversion` is stored in the file `C:\logs\scantool.conversion.sarif-external-properties` and `run.results` is divided into the files `C:\logs\scantools.results-1.sarif-external-properties` and `C:\logs\scantools.results-2.sarif-external-properties`.
>
> ```json
> {                           # A run object.
>   "originalUriBaseIds": {   # See (#originaluribaseids-property).
>     "LOGSDIR": {
>       "uri": "file:///C:/logs/"
>     }
>   },
>   "externalPropertyFileReferences": {
>     "conversion": {         # An externalPropertyFileReference object ((#externalpropertyfilereference-object)).
>       "location": {         # See (#externalpropertyfilereference-object--location-property).
>         "uri": "scantool.conversion.sarif-external-properties",
>         "uriBaseId": "LOGSDIR"
>       },
>       "guid": "11111111-1111-1111-8888-111111111111" # See (#externalpropertyfilereference-object--guid-property).
>     },
>     "results": [
>       {
>         "location": {
>           "uri": "scantool.results-1.sarif-external-properties",
>           "uriBaseId": "LOGSDIR"
>         },
>         "guid": "22222222-2222-1111-8888-222222222222",
>         "itemCount": 10000
>       },
>       {
>         "location": {
>           "uri": "scantool.results-2.sarif-external-properties",
>           "uriBaseId": "LOGSDIR"
>         },
>         "guid": "33333333-3333-1111-8888-333333333333",
>         "itemCount": 4277
>       }
>     ]
>   },
>   ...
> }
> ```

With one exception described below, if a property appears inline in the root file, its name **SHALL NOT** appear as one of the property names in `externalPropertyFileReferences`. Since an external property file can contain multiple externalized properties, `externalPropertyFileReference` objects belonging to distinct properties **MAY** denote the same external property file. However, if an array-valued externalizable property is divided among multiple external property files, the `externalPropertyFileReference` objects belonging to that property **SHALL** denote distinct external property files.

> EXAMPLE 2: In this example, `theRun.conversion` and `theRun.properties` are stored in the same external property file.
>
> ```json
> {                            # A run object ((#run-object)).
>   "originalUriBaseIds": {    # See (#originaluribaseids-property).
>     "LOGSDIR": {
>       "uri": "file:///C:/logs/"
>     }
>   },
>   "externalPropertyFileReferences": {
>     "conversion": {     # An externalPropertyFileReference object (see §3.16).
>       "location": {          # See (#externalpropertyfilereference-object--location-property).
>         "uri": "scantool.sarif-external-properties",
>         "uriBaseId": "LOGSDIR",
>         "index": 0
>       },
>       "guid": "11111111-1111-1111-8888-111111111111" # See (#externalpropertyfilereference-object--guid-property).
>     },
>     "externalizedProperties": {
>       "location": {
>         "uri": "scantool.sarif-external-properties",
>         "uriBaseId": "LOGSDIR",
>         "index": 0
>       },
>       "guid": "11111111-1111-1111-8888-111111111111"
>     }
>   },
>   ...
> }
> ```

> EXAMPLE 3: This example represents invalid SARIF because both elements of the array belonging to the `results` property denote the same external property file.
>
> ```json
> {                            # A run object ((#run-object)).
>   "originalUriBaseIds": {    # See (#originaluribaseids-property).
>     "LOGSDIR": {
>       "uri": "file:///C:/logs/"
>     }
>   },
>   "externalPropertyFileReferences": {
>     "results": [
>       {                 # An externalPropertyFileReference object (see §3.16).
>         "location": {
>           "uri": "scantool.results.sarif-external-properties",
>           "uriBaseId": "LOGSDIR",
>           "index": 0
>         },
>         "guid": "22222222-2222-1111-8888-222222222222"
>       },
>       {              # INVALID: The two external property files are the same.
>         "location": {
>           "uri": "scantool.results.sarif-external-properties",
>           "uriBaseId": "LOGSDIR",
>           "index": 0
>         },
>         "guid": "22222222-2222-1111-8888-222222222222"
>       }
>     ]
>   },
>   ...
> }
> ```

The exception is that if `run.tool.driver` is externalized, it **SHALL** still occur inline in the root file. The inline `driver` property **SHOULD** contain only properties that identify the tool, such as `name` ([sec](#toolcomponent-object--name-property)) and `semanticVersion` ([sec](#semanticversion-property)); it **SHOULD NOT** contain properties such as `globalMessageStrings` ([sec](#globalmessagestrings-property)), `rules` ([sec](#rules-property)), `notifications` ([sec](#notifications-property)), and `taxa` ([sec](#toolcomponent-object--taxa-property)), which take up a large amount of space.

> NOTE 3: This makes it possible to identify the tool that produced the log file without locating and opening the external property file, while still getting the benefit of externalizing those properties that take up a large amount of space.
