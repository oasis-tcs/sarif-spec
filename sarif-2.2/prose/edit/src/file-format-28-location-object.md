## location object

### General{#location-object--general}

A `location` object describes a location. Depending on the circumstances, a `location` object is described by physical location ([sec](#physicallocation-object)), a logical location ([sec](#logicallocation-object)), both, or in rare circumstances, neither (see below).

A logical location specifies a programmatic construct, for example, a class name or a function name, without specifying the artifact within which that construct occurs.

> NOTE: Among the reasons for including logical locations in the SARIF format in addition to physical locations are the following:
>
> - In the absence of symbol information, binary analysis tools might not have source code locations available, so information about line and column numbers might not be present in the log file. In this case, code editors, other programs, or end users can use logical location to navigate from a result to the correct source code location.
>
> - Logical location information is an important contributor to fingerprinting scenarios because it is typically more resilient to changes in source code than are the line numbers included in physical locations. See [sec](#normative-use-of-fingerprints-by-result-management-systems) for more information about fingerprinting. The `logicalLocation.fullyQualifiedName` property ([sec](#logicallocation-object--fullyqualifiedname-property)) is particularly convenient for fingerprinting.
>
> - In the analysis of structured data files such as XML or JSON, internal structural information (such as an XML path like `"/orders[2]/customers/lastName"`) might be helpful.

In rare circumstances, there might be neither physical nor logical location information available for a `location` object. See [sec](#threadflowlocation-object) for an example. In that case, the location object **SHOULD** contain a message property ([sec](#location-object--message-property)) explaining the significance of this "location."

### id property{#location-object--id-property}

A `location` object **MAY** contain a property named `id` whose value is a non-negative integer that is unique among all `location` objects belonging to `theLocationOwner`. The value does not need to be unique across all `result` ([sec](#result-object)) or `notification` ([sec](#notification-object)) objects in `theRun`.

If `id` is absent, it **SHALL** default to -1, which indicates that the value is unknown (not set).

> NOTE: Negative values are forbidden because their use would suggest some non-obvious semantic difference between positive and negative values.

> EXAMPLE 1: Within a `result` object, the following property values (among others) are `location` objects, and no two of them can have the same value for `id`:
>
>     result.relatedLocations[0]
>     result.codeFlows[0].threadFlows[0].locations[0].location
>     result.stacks[0].frames[0].location

The `id` property has two purposes: to enable an embedded link ([sec](#messages-with-embedded-links)) within a `message` object ([sec](#message-object)) to refer to `thisObject`, and to identify `thisObject` as the target of a `locationRelationship` ([sec](#locationrelationship-object)). If no `message` object within `theLocationOwner` refers to `thisObject` *via* an embedded link and no `locationRelationship` object within `theLocationOwner` specifies `thisObject` as its target, the `id` property does not need to appear.

### physicalLocation property

Depending on the circumstances, a `location` object either **SHALL**, **MAY**, or **SHALL NOT** contain a property named `physicalLocation` whose value is a `physicalLocation` object ([sec](#physicallocation-object)) that identifies the file within which the location lies. If physical location information is available and the `logicalLocations` property ([sec](#location-object--logicallocations-property)) is absent or empty, `physicalLocation` **SHALL** be present. If physical location is available and `logicalLocations` is present and non-empty, `physicalLocation` **MAY** be present. If physical location information is not available, `physicalLocation` **SHALL NOT** be present.

### logicalLocations property{#location-object--logicallocations-property}

Depending on the circumstances, a `location` object either **SHALL**, **MAY**, or **SHALL NOT** contain a property named `logicalLocations` whose value is an array of zero or more unique ([sec](#array-properties-with-unique-values)) `logicalLocation` objects ([sec](#logicallocation-object)) that identify the programmatic construct within which the location lies. If logical location information is available and the `physicalLocation` property ([sec](#physicallocation-property)) is absent, `logicalLocations` **SHALL** be present and non-empty. If logical location information is available and `physicalLocation` is present, `logicalLocations` **MAY** be present. If logical location information is not available, `logicalLocations` **SHALL NOT** be present.

> NOTE: `logicalLocations` is an array because some logical locations can be expressed in more than one way. For example, the logical location of an element in an HTML document might be expressed by an XML Path expression such as `/html/body/img[1]` or by a CSS selector such as `#logo`.

### message property{#location-object--message-property}

A `location` object **MAY** contain a property named `message` whose value is a `message` object ([sec](#message-object)) relevant to the location.

### annotations property

A `location` object **MAY** contain a property named `annotations` whose value is an array of zero or more unique ([sec](#array-properties-with-unique-values)) `region` objects ([sec](#region-object)) each of which describes a region within the artifact specified by the `location` object that is relevant to the location. Each of these `region` objects **SHOULD** contain a `message` property ([sec](#region-object--message-property)) that explains the relevance of the region to the location.

> EXAMPLE 1: Consider a `location` object which describes the declaration statement
>
> ```cs
> int x = (y + z) * q;
> ```
>
> If the analysis tool wanted to emphasize the expression `(y + z)`, it might set the `annotations` property to:
>
> ```json
> "annotations": [                  # An array of region objects.
>   {                               # A region object ((#region-object)).
>     "startLine": 12,
>     "startColumn": 9,
>     "endColumn": 16,
>     "message": {
>       "text": "(y + z) = 42"
>     }
>   }
> ]
> ```

### relationships property{#location-object--relationships-property}

A `location` object **MAY** contain a property named `relationships` whose value is an array of zero or more unique ([sec](#array-properties-with-unique-values)) `locationRelationship` objects ([sec](#locationrelationship-object)) each of which declares one or more directed relationship from `thisObject` to another `location` object, which we refer to as `theTarget`, specified by `locationRelationship.target` ([sec](#locationrelationship-object--target-property)). The natures of the relationships between `thisObject` and `theTarget` are specified by `locationRelationship.kinds` ([sec](#locationrelationship-object--kinds-property)).
