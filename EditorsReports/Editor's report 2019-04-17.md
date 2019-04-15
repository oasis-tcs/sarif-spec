# Editor's report

Laurence J. Golding and Michael Fanning

Presented at TC Meeting #35, April 17th, 2019

1. The following issues were closed without further action:

    1. [Issue #209](https://github.com/oasis-tcs/sarif-spec/issues/209): "Suggestion: platform specific data to indicate file path case sensitivity"

        Resolved duplicate of [Issue #315](https://github.com/oasis-tcs/sarif-spec/issues/315), "Specify URI normalization algorithm". We won't add any properties to hold
        platform-specific data (so you could argue for resolving this "won't fix" rather than duplicate), but
        the case sensitivity issue is addressed in the draft for #315.

    1. [Issue #331](https://github.com/oasis-tcs/sarif-spec/issues/331): "Explain how a converter emits its own notifications (as opposed to transcribing the tool's)"

        `run.conversion` has everything it needs from it's full-fledged `tool` and `invocation` objects. See the issue for more details.

1. The following change was made at editorial discretion:

    1. [Issue #266](https://github.com/oasis-tcs/sarif-spec/issues/266): "Define an object type for the value of run.externalPropertyFileReferences"

        The spec says that the value of `run.externalPropertyFileReferences` is an object and describes the properties of that object --
        but it doesn't give that set of properties a name, unlike every other object in the spec. Define an `externalPropertyFileReferences` object.

    1. [Issue #323](https://github.com/oasis-tcs/sarif-spec/issues/323): "Clarify constraints on the invocations array"

        Add some words to emphasize that the `invocations` array conceptually still represents a single run of a single tool,
        although that run might spawn or consist of multiple processes.

1. After being approved as amended at TC #34, the following spec change was merged into the provisional draft:

    1. [Issue #353](https://github.com/oasis-tcs/sarif-spec/issues/353): "Punch list"

1. After being design approved at TC #34, the following spec changes were made directly in the provisional draft (but for your convenience, change drafts are available in the Accepted folder):

    1. [Issue #354](https://github.com/oasis-tcs/sarif-spec/issues/354): "Modify look-up procedure to look for the "closest" string first, then choose your preferred format"

    1. [Issue #355](https://github.com/oasis-tcs/sarif-spec/issues/355): "Refine URL normalization guidance for file URLs"

    1. [Issue #356](https://github.com/oasis-tcs/sarif-spec/issues/356): "Consider expressing taxonomy relationships to rules"

1. The following issues raised by TC members since TC #34 have been addressed and merged into the provisional draft. Again, change drafts are available in the Accepted folder:

    1. [Issue #357](https://github.com/oasis-tcs/sarif-spec/issues/357): "Default toolComponent.associatedComponent to theTool.driver" -- raised by Luke Cartey.

    1. [Issue #358](https://github.com/oasis-tcs/sarif-spec/issues/358): "originalUriBaseIds and uri resolution" -- raised by James Kupsch.

    1. [Issue #359](https://github.com/oasis-tcs/sarif-spec/issues/359): "Constraints in state objects" -- raised by James Kupsch.

    1. [Issue #361](https://github.com/oasis-tcs/sarif-spec/issues/361): "state variables should not have syntax restriction and s/be multiformat strings" -- raised by Michael Fanning.

    1. [Issue #362](https://github.com/oasis-tcs/sarif-spec/issues/362): "Define request and response objects" -- raised by Larry Golding.

    1. [Issue #363](https://github.com/oasis-tcs/sarif-spec/issues/363): "Allow the artifactIndex property to be absent when the artifactLocation is within an artifact" -- raised by Luke Cartey.

    1. [Issue #364](https://github.com/oasis-tcs/sarif-spec/issues/364): "Remove overly restrictive advice on stable, opaque ids" -- raised by Luke Cartey.

    1. [Issue #365](https://github.com/oasis-tcs/sarif-spec/issues/365): "ruleId hierarchical string is incompatible with Semmle rule ids" -- raised by Luke Cartey.

    1. [Issue #366](https://github.com/oasis-tcs/sarif-spec/issues/366): "Review comments from @kupsch" -- raised by James Kupsch.

    1. [Issue #367](https://github.com/oasis-tcs/sarif-spec/issues/367): "Downgrade artifact.mimeType from SHOULD to MAY" -- raised by Luke Cartey

    1. [Issue #368](https://github.com/oasis-tcs/sarif-spec/issues/368): "artifactLocation.artifactIndex => index; artifact.artifactLocation => location; attachment.artifactLocation => location`" -- raised by Larry Golding

    1. [Issue #369](https://github.com/oasis-tcs/sarif-spec/issues/369): "run.invocations is externalizable" -- raised by Larry Golding

    1. [Issue #370](https://github.com/oasis-tcs/sarif-spec/issues/370): "Incorrect statement of meaning of non-empty suppressions array" -- raised by Larry Golding

    1. [Issue #371](https://github.com/oasis-tcs/sarif-spec/issues/371): "Separate suppression status from kind" -- raised by Michael Fanning

    1. [Issue #372](https://github.com/oasis-tcs/sarif-spec/issues/372): "Add roles for configuration files" -- raised by Michael Fanning

    1. [Issue #373](https://github.com/oasis-tcs/sarif-spec/issues/373): "Add suppression.justification" -- raised by Michael Fanning

    1. [Issue #374](https://github.com/oasis-tcs/sarif-spec/issues/374): "Loosen restrictions on RMS usage of partial fingerprints" -- raised by Michael Fanning

    1. [Issue #374](https://github.com/oasis-tcs/sarif-spec/issues/374): "@kupsch feedback responses" -- raised by James Kupsch

1. Typographical and substantive issues raised by Paul Anderson and Henny Sipma were addressed.

1. The following changes approved in e-ballot-3 had already been speculatively merged into the provisional draft:

    1. [Issue #179](https://github.com/oasis-tcs/sarif-spec/issues/168): "Define tool component object to represent tool driver and its extensions/plugins"

    1. [Issue #202](https://github.com/oasis-tcs/sarif-spec/issues/202): "Restore threadFlowLocation.kind"

    1. [Issue #302](https://github.com/oasis-tcs/sarif-spec/issues/302): "Add address property to physicalLocation object"

    1. [Issue #311](https://github.com/oasis-tcs/sarif-spec/issues/311): "Provide full metadata objects for notifications"

    1. [Issue #314](https://github.com/oasis-tcs/sarif-spec/issues/314): "Define result taxonomies"

    1. [Issue #315](https://github.com/oasis-tcs/sarif-spec/issues/315): "Specify URI normalization algorithm"

    1. [Issue #318](https://github.com/oasis-tcs/sarif-spec/issues/318): "Define protocol to allow embedded messages links to refer to other results"

    1. [Issue #319](https://github.com/oasis-tcs/sarif-spec/issues/319): "Converge all messages into a common format strings object"

    1. [Issue #324](https://github.com/oasis-tcs/sarif-spec/issues/324): "Define a reportingDescriptorReference object"

    1. [Issue #325](https://github.com/oasis-tcs/sarif-spec/issues/325): "Remove current localization mechanism"

    1. [Issue #326](https://github.com/oasis-tcs/sarif-spec/issues/326): "Change run.graphs and result.graphs from dictionaries to arrays"

    1. [Issue #327](https://github.com/oasis-tcs/sarif-spec/issues/327): "Remove invocation.attachments"

    1. [Issue #336](https://github.com/oasis-tcs/sarif-spec/issues/336): "Changes toolComponent properties"

    1. [Issue #337](https://github.com/oasis-tcs/sarif-spec/issues/337): "Allow toolComponents to be externalized"

    1. [Issue #338](https://github.com/oasis-tcs/sarif-spec/issues/338): "Localization and policies"

    1. [Issue #344](https://github.com/oasis-tcs/sarif-spec/issues/344): "Add suppression object to allow persisting location data for in-source suppressions"

    1. [Issue #346](https://github.com/oasis-tcs/sarif-spec/issues/346): "Add 'reportingDescriptor.deprecatedNames' and 'deprecatedGuids' to match 'deprecatedIds' property"

    1. [Issue #347](https://github.com/oasis-tcs/sarif-spec/issues/347): "Add 'referencedOnCommandLine' as a role"

    1. [Issue #348](https://github.com/oasis-tcs/sarif-spec/issues/348): "SARIF needs a mechanism to denote an in-flight or completed suppressions review"

    1. [Issue #350](https://github.com/oasis-tcs/sarif-spec/issues/350): "Rename reportingConfigurationOverride to configurationOverride"
