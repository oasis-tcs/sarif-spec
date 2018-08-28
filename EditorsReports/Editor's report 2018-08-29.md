# Editor's report

Laurence J. Golding and Michael Fanning

Presented at TC Meeting #22, August 29th, 2018

1. We closed the following issues:

    1. [Issue #70](https://github.com/oasis-tcs/sarif-spec/issues/70): "Document recommendations for serialization order"

        We opened this item because we wanted to optimize access to the information in the file. We're now going to address that by deconstructing the log file ([Issue #210](https://github.com/oasis-tcs/sarif-spec/issues/210)).

    1. [Issue #185](https://github.com/oasis-tcs/sarif-spec/issues/185): "Publish v2 SARIF JSON schema to assist in editor/other online validation"

        Michael has published the schema to schemastore.org.
    1. [Issue #207](https://github.com/oasis-tcs/sarif-spec/issues/207): "Support tool plug-ins"

        This was a duplicate of [Issue #179](https://github.com/oasis-tcs/sarif-spec/issues/179): "Consider whether SARIF covers plug-ins/rules versioning sufficiently".

    1. [Issue #211](https://github.com/oasis-tcs/sarif-spec/issues/211): "Provide log deconstruction mechanism that leverages file names"

        This was an enhancement to [Issue #210](https://github.com/oasis-tcs/sarif-spec/issues/210) ("Provide log deconstruction mechanism to enable more efficient read/write") that would have allowed externalized log file fragments to be named by convention. We decided against introducing this feature because of the additional complexity, and because it would burden consumers, who would always have to probe for the conventionally named files, which usually wouldn't exist.

1. The formal spec language for the following issues was made available for review on the specified dates, and we will move their adoption in today's meeting:

    1. [Issue #204](https://github.com/oasis-tcs/sarif-spec/issues/204): "Clearly separate start/end vs. charOffset/length region property domains" -- made available on August 24, 2018.

    1. [Issue #210](https://github.com/oasis-tcs/sarif-spec/issues/210): "Provide log deconstruction mechanism to enable more efficient read/write" -- made available on August 25, 2018.

    1. [Issue #216](https://github.com/oasis-tcs/sarif-spec/issues/216): "Remove result.ruleMessageId" -- made available on August 24, 2018.
 
    1. [Issue #220](https://github.com/oasis-tcs/sarif-spec/issues/220): "Add a correlationGuid property to run" -- made available on August 28th, 2018.

    1. [Issue #221](https://github.com/oasis-tcs/sarif-spec/issues/221): "Allow invocation.executableLocation to be relative" -- made available on August 27th, 2018.

    1. [Issue #222](https://github.com/oasis-tcs/sarif-spec/issues/222): "Make invocation.workingDirectory a fileLocation object" -- made available on August 27th, 2018.