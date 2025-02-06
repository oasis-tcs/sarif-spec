## suppression object

### General{#suppression-object--general}

A `suppression` object describes a request to suppress a result.

> NOTE 1: The `suppression` object is valuable in compliance scenarios, where teams must show an auditor that they have looked at all results that corporate policy requires, and either fixed them or explicitly decided not to fix them. The `kind` property ([sec](#suppression-object--kind-property)) enables a review process that ensures that the engineering team agrees with the suppression, and makes the agreement explicit in the log file.

> NOTE 2: The treatment of suppressed results depends on the development environment within which the log file is used, for example, a build system, an integrated development environment (IDE), or a result management system. Typically, development environments do not expose suppressed results to the user. For example, they do not include them in build log files, display them in error lists, or include them in bug counts.

### kind property{#suppression-object--kind-property}

A `suppression` object **SHALL** contain a property named `kind` whose value is a string with one of the following values, with the specified meanings:

- `"inSource"`: The result is suppressed by a syntactic construct offered by the programming language.

    EXAMPLE 1: The `SuppressMessage` attribute in the .NET Framework.

- `"external"`: The result is suppressed in an external, persistent store.

    EXAMPLE 1: A database containing historical information about the results from analysis tools. Such a store might offer the ability to mark a result as "suppressed," meaning that if the result is encountered again, it is to be ignored.

### status property

A `suppression` object **MAY** contain a property named `status` whose value is a string with one of the following values, with the specified meanings:

- `"accepted"`: The suppression is accepted.

- `"underReview"`: The engineering team is discussing the result to decide if they will suppress it.

- `"rejected"`: The engineering team decided not to suppress the result.

### location property{#suppression-object--location-property}

A `suppression` object **MAY** contain a property named `location` whose value is a `location` object ([sec](#location-object)) that specifies the location where the suppression is persisted.

> NOTE: In the common scenario, a suppression is represented by a source code construct (which we will refer to as a "suppression construct") such as an attribute or a specially formatted comment at the location where the result was detected. In this scenario, `location` is unnecessary, although it is permitted, because an end user who navigates from the result to the source code location will see the suppression attribute or comment near the relevant code.
>
> Nevertheless, there are several scenarios where `location` is useful. Here are some examples:
>
> When the suppression construct is placed in a separate compiled source file, `kind` ([sec](#suppression-object--kind-property)) is `"inSource"`, and `location.physicalLocation` ([sec](#physicallocation-property)) specifies the location of the suppression attribute in that separate file.
>
> Even when the suppression construct is adjacent to the result line, `location.physicalLocation` can be useful because it allows you to include in the log file a source code snippet containing the suppression construct, using `location.physicalLocation.region.snippet` ([sec](#region-property), [sec](#snippet-property)).
>
> When a tool detects a result within a method, but the suppression construct is applied to some higher-level construct such as the enclosing class, then `kind` is again `"inSource"`, `location.logicalLocation` ([sec](#location-object--logicallocations-property)) can specify the construct to which the suppression was applied, and `location.physicalLocation` can still usefully specify the location of the suppression construct in the source file, since it is distant from the result.
>
> In a similar case, a binary analysis tool that detected the suppression within an executable file’s metadata could provide `location.logicalLocation` even if it could not provide `location.physicalLocation`.
>
> If a suppression is stored in a separate, non-compiled file, sometimes called a "sidecar file," `kind` is `"external"`, and `location.physicalLocation` specifies the location of the suppression within the sidecar file. The sidecar file might even be another SARIF file.
>
> If a suppression is stored in a database, `kind` is again `"external"`, and `location.physicalLocation` might specify the URI of a query that returns the database information that describes the suppression.

### guid property{#suppression-object--guid-property}

A `suppression` object **MAY** contain a property named `guid` whose value is a GUID-valued string ([sec](#guid-valued-strings)).

> NOTE: This can be used, for example, to link a `suppression` object in a SARIF file to suppression information in a result management system’s database.

### justification property

A `suppression` object **MAY** contain a property named `justification` whose value is a user-supplied string that explains why the result was suppressed.

This is one of the few properties that contain textual content supplied by a user rather than by a tool or taxonomy (see [sec](#taxonomies)) vendor. As such, it might contain undesirable content. Therefore, SARIF consumers **SHOULD** exercise appropriate caution when displaying, sharing, or publishing this information.

> NOTE: This property exists because the information it contains is commonly made available by existing suppression mechanisms such as the `SuppressMessage` attribute in the .NET Framework.

### justificationType property

A suppression is a filter on an existing result. The free-form `justification` field for arbitrary textual descriptions of a suppression is not easy to parse or to map to finite states. The `justificationType` property is an enumeration providing a useful set of tags to help sort and differentiate suppressions. As with other areas of SARIF design, such buckets assist in routing information to specific actors in end-to-end result management systems.

The `justificationType` property is an enumeration with the following five values:

```
FixDeferred
NotForRelease
RiskAccepted
ToolNoise
VulnerabilityNotFeasible
```

> The suggested situations represented by these five enumeration values are the following:
>
> `ToolNoise` for example filters a result because it comprises a false positive.
> The primary responder to this class of suppression is a tool vendor
> (with other actual code owners in a secondary role to guarantee the finding is,
> in fact, incorrect).
>
> `VulnerabilityNotFeasible` designates a vulnerability that looks accurate on surface which
> cannot be realized or exploited in production due to factors or contexts that are not (or cannot be) considered by the quality tool.
> The appropriate responders are other code owners to confirm a vulnerability does not impact production
> (with tool vendors in a secondary review role to look for opportunities to improve or refine analysis).
>
> `NotForRelease` filters a result because it fired against code that does not ship (and therefore affords no quality or security risk).
> The appropriate responder/reviewer for this class of suppression might be an automation owner who can adjust tool configuration to not scan non-shipping code.
>
> `FixDeferred` acknowledges a result as a true positive but simply requests time to resolve.
> The appropriate responders are security reviewers and leads accountable for prioritizing or scheduling work items.
>
> `RiskAccepted` acknowledges a result as a true positive but definitively proposes not to act on it.
> Appropriate responders include security reviewers and leads accountable for signing off on quality and risk.
>
> The buckets represented through the enumeration values aim to be a clear, minimal set that together handle prominent routing and response use cases.
> It is possible, for example, that `ToolNoise` and `VulnerabilityNotFeasible` could be collapsed into a single `FalsePositive` designation.
> The rationale for preserving both is the distinction between the primary responder for the two cases (tool vendor and code owner).
