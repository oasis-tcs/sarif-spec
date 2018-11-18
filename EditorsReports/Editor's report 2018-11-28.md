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

    1. [Issue #195](https://github.com/oasis-tcs/sarif-spec/issues/195): "You should be able to omit fileLocation.uri if it matches the files dictionary property name"

        This is moot because `run.files` is no longer a dictionary.

    1. [Issue #278](https://github.com/oasis-tcs/sarif-spec/issues/278): "Should the sections be reordered?"

       This is an editorial issue raised by Jim. Michael and I discussed and we feel the current ordering approach reasonable as a whole (although we might decide to make small changes consistent with the current approach).

1. I made the following changes at editorial discretion:

    1. [Issue #277](https://github.com/oasis-tcs/sarif-spec/issues/277): "Editorial issues from Jim Kupsch"

        Jim submitted a large set of proposed changes. Of the changes that are purely editorial, so far I've incorporated 27 in some form, I decided against 9 of them, and 8 were moot because of recent spec changes.

        There are still 16 more editorial suggestions not yet addressed, and a couple dozen other suggestions that might become
    functional changes (but I'm trying not to dump them all into GitHub before reviewing them in person with Jim.) None of the suggested functional changes are large.

1. The formal spec language for the following issues was made available for review on the specified dates, and we will move their adoption in today's meeting:

    1. [Issue #186](https://github.com/oasis-tcs/sarif-spec/issues/186): "Ensure spec conforms to philosophy around not specifying result mgmt. behavior" -- made available on November 18th, 2018.

    1. [Issue #274](https://github.com/oasis-tcs/sarif-spec/issues/274): "Rename fileVersion to dottedQuadFileVersion and specify format constraint" -- made available on November 18th, 2018.