# Editor's report

Laurence J. Golding and Michael Fanning

Presented at TC Meeting #27, November 14th, 2018

1. After being approved as amended at the last TC meeting (#26), the following spec changes were merged into the provisional draft:

    1. [Issue #118](https://github.com/oasis-tcs/sarif-spec/issues/118): "SARIF file naming convention"

    1. [Issue #183](https://github.com/oasis-tcs/sarif-spec/issues/183): "Consider providing a mechanism to escape forward slashes in hierarchical strings"

        The grammar already prohibited forward slashes. I just added a NOTE to call attention to that fact.

    1. [Issue #262](https://github.com/oasis-tcs/sarif-spec/issues/262): "Remove run.architecture"

    1. [Issue #263](https://github.com/oasis-tcs/sarif-spec/issues/263): "Clarify distinguishing presence or non-presence of logical and instance id components"

    1. [Issue #267](https://github.com/oasis-tcs/sarif-spec/issues/267): "Allow an external file to contain multiple properties".

1. I made the following changes at editorial discretion:

    1. [Issue #223](https://github.com/oasis-tcs/sarif-spec/issues/223): "Remove uniqueItems constraint from result.locations"

        This is related to [Issue #75](https://github.com/oasis-tcs/sarif-spec/issues/75): "Ensure spec properly accounts for tools that emit line #'s only for code locations".
        A tool might detect the same result multiple times on the same line but in different columns.
        If the tool does not report the column number, then the two results might be identical.
        We fixed this in March by removing the `uniqueItems` constraint from `run.results`.

        But we overlooked the fact that some tools report multiple locations within a single result --
        and again, if the locations are on the same line but the tool does not report the column number, the two locations
        might be identical.
        The fix is to remove the `uniqueItems` constraint from `result.locations`.

    1. [Issue #271](https://github.com/oasis-tcs/sarif-spec/issues/271): : "Error in format of intermediate spec versions"

        The spec text omitted part of our agreed-upon format for the version number for intermediate versions of the spec.
        We agreed on "`2.0.0-csd.2.beta-yyyy-mm-dd`", but the spec text omitted the "`csd.2`"

1. The formal spec language for the following issues was made available for review on the specified dates, and we will move their adoption in today's meeting:

    1. [Issue #256](https://github.com/oasis-tcs/sarif-spec/issues/256): "Make Run.Files an array" -- made available on October 29th, 2018.