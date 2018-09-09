# Editor's report

Laurence J. Golding and Michael Fanning

Presented at TC Meeting #23, September 12th, 2018

1. The following issues were closed without further action:

    1. [Issue #201](https://github.com/oasis-tcs/sarif-spec/issues/201): "Make region kind more explicit"

        The clear separation between line/column and offset/length properties (described in the change draft for #204),
        together with our new understanding that we can detect a "missing" offset property at the SDK level (by having it
        default to -1, rather than to 0, which is a valid value) means that there's nothing more we need to do about
        this issue.

1. After being approved as amended at the last TC meeting (#22), the following spec changes were merged into the provisional draft:

    1. [Issue #204](https://github.com/oasis-tcs/sarif-spec/issues/204): "Clearly separate start/end vs. charOffset/length region property domains"

    1. [Issue #210](https://github.com/oasis-tcs/sarif-spec/issues/210): "Provide log deconstruction mechanism to enable more efficient read/write"

    1. [Issue #216](https://github.com/oasis-tcs/sarif-spec/issues/216): "Remove result.ruleMessageId"
 
    1. [Issue #220](https://github.com/oasis-tcs/sarif-spec/issues/220): "Add a correlationGuid property to run" -- made available on August 28th, 2018.

    1. [Issue #221](https://github.com/oasis-tcs/sarif-spec/issues/221): "Allow invocation.executableLocation to be relative"

    1. [Issue #222](https://github.com/oasis-tcs/sarif-spec/issues/222): "Make invocation.workingDirectory a fileLocation object"

1. I made the following changes at editorial discretion:

    1. [Issue #192](https://github.com/oasis-tcs/sarif-spec/issues/192): "Missing word in "ruleId property" section."

1. The formal spec language for the following issues was made available for review on the specified dates, and we will move their adoption in today's meeting:

    1. [Issue #174](https://github.com/oasis-tcs/sarif-spec/issues/174): "Result mgmt. systems merge SARIF files. Can we provide a count of occurrences?" -- made available on September 5th, 2018. 

    1. [Issue #233](https://github.com/oasis-tcs/sarif-spec/issues/233): "Consider not requiring rule.id" -- made available on September 5th, 2018.

    1. [Issue #235](https://github.com/oasis-tcs/sarif-spec/issues/235): "Wrap externalized files with contextual information" -- made available on September 5th, 2018.

    1. [Issue #237](https://github.com/oasis-tcs/sarif-spec/issues/237): "run.graphs and result.graphs should be dictionaries, not arrays." -- made available on September 9th, 2018.