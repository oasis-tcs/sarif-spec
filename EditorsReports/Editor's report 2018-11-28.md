# Editor's report

Laurence J. Golding and Michael Fanning

Presented at TC Meeting #28, November 28th, 2018

1. After being approved as amended at the last TC meeting (#26), the following spec changes were merged into the provisional draft:

    1. [Issue #169](https://github.com/oasis-tcs/sarif-spec/issues/169): "Decide how to handle uncommon line break characters"

    1. [Issue #256](https://github.com/oasis-tcs/sarif-spec/issues/256): "Make Run.Files an array"

    1. [Issue #269](https://github.com/oasis-tcs/sarif-spec/issues/269): "Add optional "itemCount" property to externalPropertyFile"

    1. [Issue #272](https://github.com/oasis-tcs/sarif-spec/issues/272): "Introduce resultProvenance object"

        I did not specify the default value for `resultProvenance.lastDetectionTimeUtc` that we approved in TC #27,
    because it turned out to be more complicated than we thought.
    I filed new [Issue #287](https://github.com/oasis-tcs/sarif-spec/issues/287): "Define default for resultProvenance.lastDetectionTimeUtc",
    which we'll discuss today.

    1. [Issue #275](https://github.com/oasis-tcs/sarif-spec/issues/275): "Specify how to store IRIs in URI-valued properties"

1. The following issues were closed without further action:

    1. [Issue #87](https://github.com/oasis-tcs/sarif-spec/issues/87): "Review polyspace designations to ensure SARIF expresses these sufficiently"

        Closed by @michaelcfanning as duplicate of [Issue #59](https://github.com/oasis-tcs/sarif-spec/issues/59): "Consider a tool validation or 'selectivity' annotation"

    1. [Issue #195](https://github.com/oasis-tcs/sarif-spec/issues/195): "You should be able to omit fileLocation.uri if it matches the files dictionary property name"

        This is moot because `run.files` is no longer a dictionary.

    1. [Issue #278](https://github.com/oasis-tcs/sarif-spec/issues/278): "Should the sections be reordered?"

        This is an editorial issue raised by Jim. Michael and I discussed and we feel that he current ordering approach reasonable as a whole (although we might decide to make small changes consistent with the current approach).

    1. [Issue #283](https://github.com/oasis-tcs/sarif-spec/issues/283): "result.message SHALL be present constraint dropped from schema"

        Both the spec and the schema are correct. The spec says that _either_ `message` must be present (if the log specifies its messages "inline"), _or_ `ruleMessageId` must be present (if the log just provides a resource identifier together that locates the message string), or both.

        Now even if the log file specifies a message indirectly _via_ `ruleMessageId`, you still need `message` if the resource string has any replacement sequences `{n}` that need to be filled from `message.arguments`. But if the resource string has no replacement sequences, you don't need `message` at all.

    1. [Issue #289](https://github.com/oasis-tcs/sarif-spec/issues/289): "Consider making log.version placement as first property a SHALL"

        We shouldn't do this because the producer might be using a JSON library that doesn't support specifying serialization order.
        The spec currently says "**SHOULD**", which means "do it unless you have a good reason not to". "My JSON serializer can't do it" would be a good enough reason.

1. I made the following changes at editorial discretion:

    1. [Issue #277](https://github.com/oasis-tcs/sarif-spec/issues/277): "Editorial issues from Jim Kupsch"

        Jim submitted a large set of proposed changes. Of the changes that are purely editorial, so far I've incorporated 27 in some form, I decided against 9 of them, and 8 were moot because of recent spec changes.

        There are still 16 more editorial suggestions not yet addressed, and a couple dozen other suggestions that might become
    functional changes (but I'm trying not to dump them all into GitHub before reviewing them in person with Jim.) None of the suggested functional changes are large.

    1. [Issue #283](https://github.com/oasis-tcs/sarif-spec/issues/283): "result.message SHALL be present constraint should be added to schema"

        The spec text already says:

        > A `result` object **SHALL** contain a property named `message`...

        It's just a bug that we neglected to mark the property `required` in the schema. The comment thread in the issue explains how this bug crept in.

        I added this change to the "schema changes" document so that Michael will fix it when he updates the schema with the changes for TC <span>#</span>28.

    1. [Issue #290](https://github.com/oasis-tcs/sarif-spec/issues/290): "Add registered trademarks as appropriate"

        Microsoft Windows &reg;, Linux &reg;, and Unix &reg; are all registered trademarks. Mark them as such in the text.

1. The formal spec language for the following issues was made available for review on the specified dates, and we will move their adoption in today's meeting:

    1. [Issue #186](https://github.com/oasis-tcs/sarif-spec/issues/186): "Ensure spec conforms to philosophy around not specifying result mgmt. behavior" -- made available on November 18th, 2018.

    1. [Issue #274](https://github.com/oasis-tcs/sarif-spec/issues/274): "Rename fileVersion to dottedQuadFileVersion and specify format constraint" -- made available on November 18th, 2018.

    1. [Issue #279](https://github.com/oasis-tcs/sarif-spec/issues/279): "logicalLocation.kind: remove "package" and "function"" -- made available on November 24th, 2018.

    1. [Issue #280](https://github.com/oasis-tcs/sarif-spec/issues/280): "Provide optional result.rank value of 0.0 to 100.0" -- made available on November 26th, 2018.

    1. [Issue #284](https://github.com/oasis-tcs/sarif-spec/issues/284): "baselineState s/be present on all results or none" -- made available on November 21st, 2018.

    1. [Issue #285](https://github.com/oasis-tcs/sarif-spec/issues/285): "Provide a mechanism to associate a result with an invocation." -- made available on November 18th, 2018.

    1. [Issue #288](https://github.com/oasis-tcs/sarif-spec/issues/288): "ruleConfiguration.defaultLevel should not contain an 'open' value" -- made available on November 21st, 2018.

1. The formal spec language for the following issues was made available for review on the specified dates. If a motion to amend the agenda is approved, we will move their adoption in today's meeting:

    1. [Issue #188](https://github.com/oasis-tcs/sarif-spec/issues/188): "Consider specifying an implied default value when columnKind is missing" -- made available on November 27th, 2018.