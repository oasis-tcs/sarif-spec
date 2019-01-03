# Editor's report

Laurence J. Golding and Michael Fanning

Presented at TC Meeting #30, January 9th, 2019

1. After being approved without amendment at the last TC meeting (#29), I merged the following spec changes into the provisional draft:

    1. [Issue #248](https://github.com/oasis-tcs/sarif-spec/issues/248): "Version control details not strongly associated with results"

    1. [Issue #270](https://github.com/oasis-tcs/sarif-spec/issues/270): "Schema needs to be carefully scrubbed for minItems and uniqueItems use for all arrays"

    1. [Issue #287](https://github.com/oasis-tcs/sarif-spec/issues/287): "Define default for resultProvenance.lastDetectionTimeUtc"

    1. [Issue #292](https://github.com/oasis-tcs/sarif-spec/issues/292): "Specify a default for result.rank"

    1. [Issue #293](https://github.com/oasis-tcs/sarif-spec/issues/293): "Add rule.deprecatedIds"

    1. [Issue #297](https://github.com/oasis-tcs/sarif-spec/issues/297): "Move conversionProvenance under result.provenance"

1. I made the following changes at editorial discretion:

    1. [Issue #296](https://github.com/oasis-tcs/sarif-spec/issues/296): "Editorial: change examples from 'Code small' to 'Code' wherever possible"

        For readability.

    1. [Issue #299](https://github.com/oasis-tcs/sarif-spec/issues/299): "Constraint on locations"

        The spec said that `location` had to have at least one of `fullyQualifiedLogicalName` or `logicalLocationIndex`.
        That's only true if the `location` object specifies logical location information, so say that.

    1. Clarified condition for when `fileLocation.fileIndex` can be present by adding the phrase in italics:

        > If the containing `run` object (§3.13) contains a `files` property (§3.13.11) _and the `files` array contains a `file` object (§3.21) that describes the file specified by this `fileLocation` object_, then the `fileLocation` object **SHOULD** contain a property named `fileIndex`...

1. The formal spec language for the following issues was made available for review on the specified dates, and we will move their adoption in today's meeting:

    1. [Issue #286](https://github.com/oasis-tcs/sarif-spec/issues/286): "Specify optional property file.sourceLanguage to guide syntax-driven colorization of snippets" -- made available on January 3rd, 2019.

    Incorporate feedback from TC #29. Add `region.sourceLanguage` to support multi-language files.

    1. [Issue #298](https://github.com/oasis-tcs/sarif-spec/issues/298): "Only 'index' properties should be used for array lookup" -- made available on December 14th, 2018.