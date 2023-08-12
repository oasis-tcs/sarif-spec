## artifactLocation object

### General{#artifactlocation--general}

Certain properties in this document specify the location of an artifact. SARIF represents an artifact’s location with an `artifactLocation` object. The most important member of an `artifactLocation` object is its `uri` property ([sec](#uri-property)). If the `uri` property contains a relative reference (the term used in the URI standard \[[cite](#RFC3986)\] for what is commonly called a "relative URI"), the `uriBaseId` property ([sec](#uribaseid-property)) can sometimes be used to resolve the relative reference to an absolute URI.

### Constraints{#artifactlocation-object--constraints}

At least one of the `uri` property ([sec](#uri-property)) or the `index` property ([sec](#artifactlocation-object--index-property)) **SHALL** be present. In certain circumstances (see [sec](#uribaseid-property) and [sec](#artifactlocation-object--index-property)), they **MAY** both be present.

> NOTE: Providing both `uri` and `index` makes the log file more readable at the expense of increased size. Providing only `index` reduces log file size but makes it less readable to an end user, who has to determine the URI by locating the `artifact` object ([sec](#artifact-object)) at the index within `theRun.artifacts` ([sec](#artifacts-property)) specified by `index`.

If both `uri` and `index` are present, they **SHALL** both denote the same artifact. That is, let URI<sub>1</sub> be the fully resolved URI of the artifact specified by an `artifactLocation` object as determined by the `uriBaseId` resolution procedure described in [sec](#uribaseid-property). Let URI<sub>2</sub> be the fully resolved URI of the artifact specified by the `artifact` object indicated by `index`, determined in the same way. Then URI<sub>1</sub> and URI<sub>2</sub> **SHALL** be equivalent in the sense described in [sec](#uri-valued-properties--general).

### uri property

Depending on the circumstances, an `artifactLocation` object either **SHALL**, **SHALL NOT**, or **MAY** contain a property named `uri` whose value is a string containing a URI \[[cite](#RFC3986)\] that specifies the location of the artifact.

If `thisObject` describes a nested artifact whose location within its parent container can be expressed by a path from the root of the container, then if `uri` is present, it **SHALL** specify a relative-path reference per section 4.2 of \[[cite](#RFC3986)\] expressing that path. A relative reference **SHALL NOT** begin with two slash characters (a ‘network-path’ reference per section 4.2 of \[[cite](#RFC3986)\]. A relative reference **SHALL NOT** begin with a single slash character (an ‘absolute-path’ reference per section 4.2 of \[[cite](#RFC3986)\]) unless doing so is required to distinguish between distinct items in archive formats, such as zip and tar.

> NOTE 1: For example, `"/a.txt"` and `"a.txt"` can both exist as distinct files in the same archive.

> NOTE 2: A relative path is useful to reference any artifact with a fixed location relative to a non-deterministic root, e.g., the relative version control path of a file as distinct from a local enlistment root. The uriBaseId (3.4.4) property can be used to express the non-deterministic absolute URI root. This approach assists in log file diffing and other scenarios where a clear distinction between data that is consistent or not between scan environments is helpful.

If the nested artifact is a member of an archive file (for example, zip \[[cite](#ZIP)\] or tar \[[cite](#TAR)\]), `uri` **SHOULD** specify the member name or path as specified by the archive.

If `thisObject` occurs as the value of a "top-level" property in `theRun.originalBaseIds` ([sec](#originaluribaseids-property)), then `uri` **MAY** be absent. See [sec](#originaluribaseids-property) for an explanation and an example of this point. Otherwise:

If `index` ([sec](#artifactlocation-object--index-property)) is absent, `uri` **SHALL** be present.

> NOTE 3: This ensures that there is a way to locate the artifact specified by the `artifactLocation` object.

If `thisObject` represents a nested artifact whose location within its parent container can be expressed only by means of a byte offset, then `uri` **SHALL NOT** be present.

> NOTE 4: This implies that `index` will be present; see [sec](#artifactlocation-object--index-property).

Otherwise, `uri` **MAY** be present.

### uriBaseId property

If this `artifactLocation` object describes a top-level artifact and the value of its `uri` property ([sec](#uri-property)) is a relative reference, the `artifactLocation` object **SHOULD** contain a property named `uriBaseId` whose value is a string which indirectly specifies the absolute URI with respect to which that relative reference is interpreted. If the `uri` property contains an absolute URI, the `uriBaseId` property **SHALL** be absent. If this `artifactLocation` object describes a nested artifact, `uriBaseId` **SHALL** be absent.

If a SARIF consumer requires an absolute URI (for example, to display the specified artifact to a user), then it needs to resolve `uriBaseId` to an absolute URI, which it can then combine with the relative reference stored in the `uri` property.

A SARIF consumer **SHALL** use the following procedure to resolve a `uriBaseId` to an absolute URI:

1.  If the end user has configured the SARIF consumer with a value for the `uriBaseId` (for example, on the consumer’s command line or through a user interface prompt), then the consumer **SHALL** use the configured value.

> EXAMPLE 1: In this example the SARIF consumer’s command line specifies that any `uriBaseId` property whose value is `"SRCROOT"` refers to the absolute URI `"file:///C:/browser/src/"`:
>
>      C:> SarifAnalyzer --input log.sarif --uriBaseId SRCROOT="file:///C:/browser/src/"

2.  If `uriBaseId` is not yet resolved and `theRun.originalUriBaseIds` ([sec](#originaluribaseids-property)) is present, the consumer **SHALL** attempt to resolve the `uriBaseId` from the information in `originalUriBaseIds`, in the manner specified in [sec](#originaluribaseids-property).

3.  If `uriBaseId` is not yet resolved, the consumer **MAY** use other information or heuristics to locate the artifact.

The `uriBaseId` property can be any string; it does not need to have any particular syntax or follow any particular naming convention. In particular, it does not need to designate a machine environment variable or similar value, although it might. The SARIF producer and any SARIF consumers need to agree on the meanings of any values for the `uriBaseId` property that appear in the log file.

> EXAMPLE 2: In this example, the analysis tool has set the `uri` property of an `artifactLocation` object ([sec](#artifactlocation-object)) to a relative reference. The tool has also set the `uriBaseId` property to `"%srcroot%"`. The analysis tool and the SARIF consumers have agreed upon a convention whereby this indicates that the relative reference is expressed relative to the root of the source tree in which the file appears.
>
> ```json
> "artifactLocation": {
>   "uri": "drivers/video/hidef/driver.c",
>   "uriBaseId": "%srcroot%"
> }
> ```

> NOTE: There are various reasons for providing the `uriBaseId` property:
>
> - Portability: A log file that contains relative references together with `uriBaseId` properties can be interpreted on a machine where the files are located at a different absolute location.
>
> - Determinism: A log file that uses `uriBaseId` properties has a better chance of being "deterministic"; that is, of being identical from run to run if none of its inputs have changed, even if those runs occur on machines where the files are located at different absolute locations. For more information on this point, see Appendix F.
>
> - Security: The use of `uriBaseId` properties avoids the persistence of absolute path names in the log file. Absolute path names can reveal information that might be sensitive.
>
> - Semantics: Assuming the reader of the log file (an end user or another tool) has the necessary context, they can understand the meaning of the location specified by the `uri` property, for example, "this is a source file".
>
For more guidance on the intended use of the `uriBaseId` property, see [sec](#guidance-on-the-use-of-artifactlocation-objects).

### index property{#artifactlocation-object--index-property}

Depending on the circumstances, an `artifactLocation` object either **MAY**, **SHALL NOT**, **SHALL**, or **SHOULD** contain a property named `index` whose value is the array index ([sec](#array-indices)) within `theRun.artifacts` ([sec](#artifacts-property)) of the `artifact` object ([sec](#artifact-object)), if any, that describes the artifact specified by this `artifactLocation` object.

If `thisObject` occurs as the `location` property ([sec](#artifact-object--location-property)) of an `artifact` object in `theRun.artifacts`, then `index` **MAY** be present. If present, it **SHALL** equal the array index within `theRun.artifacts` of the containing `artifact` object.

Otherwise, if `theRun.artifacts` is absent or does not contain an element that describes the artifact specified by `thisObject`, then `index` **SHALL NOT** be present.

> NOTE 1: `index` cannot be present in this case because there is no array element for it to point to. But this implies that `uri` is present, because otherwise there would be no way to locate the artifact specified by `thisObject`.

Otherwise, if the `uri` property ([sec](#uri-property)) is absent, then `index` **SHALL** be present.

> NOTE 2: Again, this ensures that there is a way to locate the artifact specified by `thisObject`.

Otherwise (that is, if `uri` is present but there *is* a relevant `artifact` object in `theRun.artifacts`), `index` **SHOULD** be present.

> NOTE 3: If `index` is absent, the SARIF consumer will not be able to locate the additional information contained in the `artifact` object about the artifact specified by `thisObject`.

> EXAMPLE 1: In this example, `results[0].locations[0].physicalLocation.artifactLocation.index` specifies the `artifact` object located at `artifacts[0]`.
>
> ```json
> {                                    # A run object ((#run-object)).
>   "artifacts": [
>     {
>       "location": {
>         "uri": "file:///C:/Code/main.c"
>       },
>       "sourceLanguage": "c"
>     }
>   ],
>   "results": [
>     {
>       "ruleId": "CA2101",
>       "level": "error",
>       "locations": [
>         {
>           "physicalLocation": {
>             "artifactLocation": {
>               "uri": "file:///C:/Code/main.c",
>               "index": 0
>             },
>             "region": {
>               "startLine": 24,
>               "startColumn": 9
>             }
>           }
>         }
>       ]
>     }
>   ]
> }
> ```

### description property{#artifactlocation-object--description-property}

An `artifactLocation` object **MAY** have a property named `description` whose value is a `message` object ([sec](#message-object)) that describes this location.

> EXAMPLE 1: In this example, the property values in `run.originalUriBaseIds` ([sec](#originaluribaseids-property)), which are `artifactLocation` objects, have `description` properties. This allows a SARIF viewer to display helpful information when prompting a user to supply values for the base id symbols.
>
> ```json
> {                                                # A run object ((#run-object)).
>   "originalUriBaseIds": {                        # See (#originaluribaseids-property).
>     "PROJROOT": {
>       "uri": "file:///C:/browser/",
>       "description": {
>         "text": "The project root directory."
>       }
>     },
>     "SRCROOT": {
>       "uri": "file:///C:/browser/src/",
>       "description": {
>         "text": "The root of the source code tree."
>       }
>     },
>     "BINROOT": {
>       "uri": "file:///C:/browser/bin/",
>       "description": {
>         "text": "The build output directory."
>       }
>     }
>   }
> }
> ```

### Guidance on the use of artifactLocation objects

Some URIs are "deterministic" in the sense that they will be the same from one run to the next and are independent of machine-specific information such as volume names or drive letters. Internet addresses are typically deterministic.

In contrast, file system paths are typically non-deterministic. For example, a source code enlistment might exist at different paths on different machines.

`artifactLocation` objects **MAY** represent both deterministic and non-deterministic URIs. In either case, the `uri` property ([sec](#uri-property)) **SHOULD** be deterministic, either because it is a deterministic relative reference (for example, the relative path to a file from the root of the directory tree containing the analyzed source code) or because it is an absolute URI. If the URI is non-deterministic, the `uriBaseId` property ([sec](#uribaseid-property)) **SHOULD** capture the non-deterministic portion of the URI, for example, the absolute path to the root of the directory tree containing the analyzed source code.

> EXAMPLE 1: In this example, the location of a result detected by a tool is specified by a relative reference together with a `uriBaseId` that specifies the root of the source code enlistment.
>
> ```json
> {                                                # A run object ((#run-object)).
>   "originalUriBaseIds": {                        # See (#originaluribaseids-property).
>     "SRCROOT": {
>       "uri": "file:///C:/browser/src/"
>     }
>   },
> 
>   "results": [                                   # See (#results-property).                                     
>     {                                            # A result object ((#result-object)). 
>       "locations": [                             # See (#result-object--locations-property).
>         {                                        # A location object ((#location-object)).
>           "physicalLocation": {                  # See (#physicallocation-property).
>             "artifactLocation": {                # An artifactLocation object.
>               "uri": "ui/window.cpp",
>               "uriBaseId": "SRCROOT"
>             }
>           }
>         }
>       ]
>     }
>   ]
> }
> ```
