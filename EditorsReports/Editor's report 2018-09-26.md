# Editor's report

Laurence J. Golding and Michael Fanning

Presented at TC Meeting #24, September 26th, 2018

1. The following issues are verified as fixed, and closed:

    1. [Issue #193](https://github.com/oasis-tcs/sarif-spec/issues/193): "rule.id should be optional if it matches the dictionary key name"

        I filed this issue twice, the second time as [#233](https://github.com/oasis-tcs/sarif-spec/issues/233). Since all the documentation of this change (the change draft, the agenda, the Editor's Report, and the Schema Changes document) link to [#233](https://github.com/oasis-tcs/sarif-spec/issues/233), I resolved [#193](https://github.com/oasis-tcs/sarif-spec/issues/193) as the duplicate, even thought it was the first one to be filed.

    1. [Issue #225](https://github.com/oasis-tcs/sarif-spec/issues/225): "sarif-schema.json has invalid requirement on stackFrame object"

        [Sarif.Sdk 2.0.0-csd.2.0.3](https://www.nuget.org/packages/Sarif.Sdk/2.0.0-csd.1.0.3) is published to NuGet, and the version at [http://json.schemastore.org/sarif-2.0.0]() has the fix.

    1. [Issue #228](https://github.com/oasis-tcs/sarif-spec/issues/228): "CSD.1 spec incorrectly places result 'correlationGuid' property on the run object"

        The schema and the spec now define `correlationGuid` on both `run` and `result`.

1. After being approved at the last TC meeting (#23), the following spec changes were merged into the provisional draft:

    1. [Issue #174](https://github.com/oasis-tcs/sarif-spec/issues/174): "Result mgmt. systems merge SARIF files. Can we provide a count of occurrences?"

    1. [Issue #233](https://github.com/oasis-tcs/sarif-spec/issues/233): "Consider not requiring rule.id"

    1. [Issue #237](https://github.com/oasis-tcs/sarif-spec/issues/237): "run.graphs and result.graphs should be dictionaries, not arrays"

1. The formal spec language for the following issues was made available for review on the specified dates, and we will move their adoption in today's meeting:

    1. [Issue #243](https://github.com/oasis-tcs/sarif-spec/issues/243): "Consider making file.hashes a dictionary" -- made available on September 13th, 2018.

    1. [Issue #240](https://github.com/oasis-tcs/sarif-spec/issues/240): "Consider removing type inconsistency with message property in exception object" -- made available on September 14th, 2018.