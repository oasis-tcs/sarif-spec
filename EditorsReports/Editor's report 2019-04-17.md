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

1. After being approved as amended at TC #34, the following spec change was merged into the provisional draft:

    1. [Issue #353](https://github.com/oasis-tcs/sarif-spec/issues/353): "Punch list"

1. After being design approved at TC #34, the following spec changes were made directly in the provisional draft (but for your convenience, change drafts are available in the Accepted folder):

    1. [Issue #354](https://github.com/oasis-tcs/sarif-spec/issues/354): "Modify look-up procedure to look for the "closest" string first, then choose your preferred format"

    1. [Issue #355](https://github.com/oasis-tcs/sarif-spec/issues/355): "Refine URL normalization guidance for file URLs"

    1. [Issue #356](https://github.com/oasis-tcs/sarif-spec/issues/356): "Consider expressing taxonomy relationships to rules"

1. The following issues (which I believe to be non-controversial) raised by TC members since TC #34 have been addressed and merged into the provisional draft. Again, change drafts are available in the Accepted folder:

    1. [Issue #357](https://github.com/oasis-tcs/sarif-spec/issues/357): "Default toolComponent.associatedComponent to theTool.driver" -- raised by Luke Cartey.

    1. [Issue #359](https://github.com/oasis-tcs/sarif-spec/issues/357): "Constraints in state objects" -- raised by James Kupsch.

    1. [Issue #361](https://github.com/oasis-tcs/sarif-spec/issues/361): "state variables should not have syntax restriction and s/be multiformat strings" -- raised by Michael Fanning.

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
