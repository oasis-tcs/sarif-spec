## `externalPropertyFileReference` Object

### General{#externalpropertyfilereference-object--general}

An `externalPropertyFileReference` object contains information that enables a SARIF consumer to locate the external property file (see [sec](#rationale)) that contains the value of an externalized property associated with `theRun`.

### Constraints{#externalpropertyfilereference-object--constraints}

At least one of the `location` property ([sec](#externalpropertyfilereference-object--location-property)) or the `guid` property ([sec](#externalpropertyfilereference-object--guid-property)) **SHALL** be present. If both are present, they **SHALL** identify the same set of externalized properties (possibly located inline; see [sec](#inlineexternalproperties-property)).

> NOTE: This constraint ensures that it is possible to locate the externalized properties.

### `location` Property{#externalpropertyfilereference-object--location-property}

Depending on the circumstances, an `externalPropertyFileReference` object either **SHALL** or **MAY** contain a property named `location` whose value is an `artifactLocation` object ([sec](#artifactlocation-object)) that specifies the location of the external property file.

If the externalized properties are persisted in a separate file, `location` **SHALL** be present. In that case, if the `artifactLocation` object’s `uri` property ([sec](#uri-property)) specifies a relative reference and its `uriBaseId` property ([sec](#uribaseid-property)) is absent, then `uri` **SHALL** be interpreted relative to the location of the root file.

Otherwise (that is, if the externalized properties are persisted as an element of `theSarifLog.inlineExternalProperties` ([sec](#inlineexternalproperties-property))), then `location` **MAY** be present. If `location` is present, its `uri` property **SHALL** resolve to an absolute URI using the `sarif` scheme ([sec](#uris-that-use-the-sarif-scheme)). If `location` is absent, then a SARIF consumer that needs to locate the externalized properties **SHALL** do so using the `guid` property ([sec](#externalpropertyfilereference-object--guid-property)).

### `guid` Property{#externalpropertyfilereference-object--guid-property}

Depending on the circumstances, an `externalPropertyFileReference` object either **SHALL** or **MAY** contain a property named `guid` whose value is a GUID-valued string ([sec](#guid-valued-strings)) which provides a unique, stable identifier for the external property file.

If the externalized properties are persisted in an element of `theSarifLog.inlineExternalProperties` ([sec](#inlineexternalproperties-property)) and `location` ([sec](#externalpropertyfilereference-object--location-property)) is absent, then `guid` **SHALL** be present.

Otherwise (that is, if the externalized properties are persisted in a separate file, in which case `location` is required, or if the externalized properties are persisted in an element of `theSarifLog.inlineExternalProperties` but `location` is present), guid **MAY** be present.

> NOTE: The rationale for these constraints is to ensure that there is enough information to locate the external properties. If the properties are in an external file, then `location` is necessary but `guid` can still be present; if the properties are inline, either `location` or `guid` suffices but both can be present.

If `guid` is present, it **SHALL** equal the `guid` property ([sec](#externalproperties-object--guid-property)) of the `externalProperties` object ([sec](#externalproperties-object)) identified by `guid` and/or `location`.

### `itemCount` Property

If an `externalPropertyFileReference` object specifies an external property file that contains all or a portion of an array-valued property, it **MAY** contain a property named `itemCount` whose value is a non-negative integer that specifies the number of items in the externalized property array in that file. If the `externalPropertyFileReference` object specifies an external property file that contains an object-valued property, `itemCount` **SHALL** be absent.

If `itemCount` is absent, it **SHALL** default to -1, which indicates that the value is unknown (not set).

> NOTE: This information is useful to a SARIF consumer that needs to locate the item at a specified array index in an externalized array-valued property. Without this information, the consumer would have to open in turn each external property file belonging to that property, counting the number of array elements in each, until it reached the file containing the desired element.

> EXAMPLE 1: In EXAMPLE 1 in [sec](#properties), the array-valued property `results` is divided into two files, the first containing 10,000 elements and the second containing 4,277 elements. A SARIF consumer that needs to access element 12,000 knows immediately that it is contained in the second file, at index 2,000.
