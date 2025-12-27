## `versionControlDetails` Object

### General{#versioncontroldetails-object--general}

A `versionControlDetails` object specifies the information necessary to retrieve from a version control system (VCS) the correct revision of the files that were scanned during the run.

For an example, see [sec](#versioncontrolprovenance-property).

### Constraints{#versioncontroldetails-object--constraints}

A `versionControlDetails` object **SHOULD** contain sufficient information to uniquely and permanently identify the revision of the files that were scanned.

> NOTE: The required set of properties depends on the VCS and on the engineering system within which it is used. Consider Git as an example. The `revisionId` property (containing a commit id) would suffice. The `branch` property ([sec](#branch-property)) might not suffice because a Git branch is a pointer to the latest commit along a line of development; however, `branch` together with `asOfTimeUtc` ([sec](#asoftimeutc-property)) might suffice (although that is not an idiomatic use of Git). Similarly, `revisionTag` ([sec](#revisiontag-property)) might not suffice because a Git tag can be removed, but if the engineering system guaranteed that certain tags (such as those specifying public releases) were stable, then `revisionTag` might suffice.

### `repositoryUri` Property

A `versionControlDetails` object **SHALL** contain a property named `repositoryUri` whose value is a string containing an absolute URI [cite](#RFC3986) that specifies the location of the repository containing the scanned files.

### revisionId` Property

A `versionControlDetails` object **SHOULD** contain a property named `revisionId` whose value is a redactable ([sec](#redactable-strings)) string that uniquely and permanently identifies the appropriate revision of the scanned files.

### `branch` Property

A `versionControlDetails` object **MAY** contain a property named `branch` whose value is a redactable ([sec](#redactable-strings)) string containing the name of a branch containing the correct revision of the scanned files.

### `revisionTag` Property

A `versionControlDetails` object **MAY** contain a property named `revisionTag` whose value is a redactable ([sec](#redactable-strings)) string containing a tag that has been applied to the revision in the VCS.

> NOTE 1: This document refers to an identifier for a revision in a VCS as a "tag". Different VCSs use different terms; for example, Visual Studio Team Services Version Control calls it a "label".

> NOTE 2: Although VCSs generally allow a revision to have more than one tag, the `revisionTag` property is not an array. The purpose of `revisionTag` is to aid in identifying a revision so that a scan can be reproduced, not to exhaustively describe the revision.

### `asOfTimeUtc` Property

A `versionControlDetails` object **MAY** contain a property named `asOfTimeUtc` whose value is a string in the format specified in [sec](#datetime-properties), specifying a UTC date and time that can be used to synchronize an enlistment to the state of the repository as of that time.

> NOTE: In some VCSs, the "synchronize by date" feature requires the time to be expressed in the server’s time zone. In such a case, the SARIF producer would need to know the server’s time zone to correctly populate `asOfTimeUtc`.

### `mappedTo` Property

A `versionControlDetails` object **MAY** contain a property named `mappedTo` whose value is an `artifactLocation` object ([sec](#artifactlocation-object)) that specifies the location in the local file system to which the root of the repository was mapped at the time of the analysis.

This property makes it possible to map any `artifactLocation` to the repository, if any, to which the file belongs. The mapping algorithm **SHALL** be as follows, or any algorithm with the same result (a clarifying example follows):

1.  Resolve the `artifactLocation` as far as possible using the procedure specified in [sec](#originaluribaseids-property). Denote the resolved `artifactLocation` by `a`.

2.  For every `versionControlDetails` object `vcd` in `theRun.versionControlProvenance` ([sec](#versioncontrolprovenance-property)), resolve the `artifactLocation` object specified by `vcd.mappedTo`, again using the procedure specified in [sec](#originaluribaseids-property). Denote each such resolved `artifactLocation` object by `v`.

3.  Let S be the set of all `versionControlDetails` objects `vcd` for which `v.uriBaseId` equals `a.uriBaseId` and `v.uri` is a prefix of `a.uri`.

4.  If S is the empty set, then the file specified by `artifactLocation` does not belong to any repository.

5.  Otherwise, the file specified by `artifactLocation` belongs to the repository specified by the member of S with the longest `v.uri`.

> EXAMPLE 1: This example illustrates the mapping algorithm. Consider this SARIF file:
> ```json
> {
>   "originalUriBaseIds": {
>     "HOME": {
>       "uri": "file:///home/user/"
>     },
>     "PACKAGE_ROOT": {
>       "uri": "package/",
>       "uriBaseId": "HOME"
>     }
>   },
> 
>   "versionControlProvenance": [
>     {
>       "repositoryUri": "https://github.com/example-corp/package",
>       "revisionId": "b87c4e9",
>       "mappedTo": {
>         "uriBaseId": "PACKAGE_ROOT"
>       }
>     },
>     {
>       "repositoryUri": "https://github.com/example-corp/plugin1",
>       "revisionId": "cafdac7",
>       "mappedTo": {
>         "uriBaseId": "PACKAGE_ROOT",
>         "uri": "plugin1"
>       }
>     },
>     {
>       "repositoryUri": "https://github.com/example-corp/plugin2",
>       "revisionId": "d0dc2c0",
>       "mappedTo": {
>         "uriBaseId": "PACKAGE_ROOT",
>         "uri": "plugin2"
>       }
>     }
>   ],
> 
>   "results": [
>     {
>       "ruleId": "CA1000",
>       "locations": [
>         {
>           "physicalLocation": {
>             "artifactLocation": {
>               "uri": "plugin1/x.c",
>               "uriBaseId": "PACKAGE_ROOT"
>             }
>           }
>         }
>       ]
>     }
>   ]
> }
> ```
>
> The object is to determine to which repository, if any, the file `plugin1/x.c` specified by the result location belongs. The algorithm proceeds as follows, using a simplified notation (*uriBaseId*, *uri*) to denote an `artifactLocation`:
>
> 1.  Use the information in `originalUriBaseIds` and the procedure specified in [sec](#originaluribaseids-property) to calculate the "resolved artifact location" `a`:  
>
>     `(PACKAGE_ROOT, plugin1/x.c)` → `(HOME, package/plugin1/x.c)` → `(null, file:///home/user/package/plugin1/x.c)`.
>
> 2.  In the same way, calculate the resolved artifact location `v` from the `mappedTo` property of each element `vcd` of the `versionControlProvenance` array:
>
>     - `(PACKAGE_ROOT, null)` → `(HOME, package)` → `(null, file:///home/user/package)`
>
>     - `(PACKAGE_ROOT, plugin1)` → `(HOME, package/plugin1)` → `(null, file:///home/user/package/plugin1)`
>
>     - `(PACKAGE_ROOT, plugin2)` → `(HOME, package/plugin2)` → `(null, file:///home/user/package/plugin2)`
>
> 3.  The set of `vcd` for which `v.uriBaseId` equals `a.uriBaseId` (which is `null`) and for which `v.uri` is a *prefix* of `a.uri` (which is `file:///home/user/package/plugin1/x.c`) contains the objects at indices 0 and 1. It does not contain the object at index 2 because `file:///home/user/package/plugin2` is not a prefix of `file:///home/user/package/plugin1/x.c`.
>
> 4.  The set is not empty (it contains indices 0 and 1).
>
> 5.  The member of the set for with the longest `v.uri` is the object at index 1, because `file:///home/user/package/plugin1` is longer than `file:///home/user/package`.
>
Therefore, the specified file belongs to the repository specified by the `versionControlDetails` object at index 1, namely `https://github.com/example-corp/plugin1`.
