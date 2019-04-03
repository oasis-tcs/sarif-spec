# Editor's report

Laurence J. Golding and Michael Fanning

Presented at TC Meeting #34, April 3th, 2019

1. After being approved as amended at previous TC meetings, the following spec changes were merged into the provisional draft:

    1. [Issue #330](https://github.com/oasis-tcs/sarif-spec/issues/330): "Rename 'invocation.toolNotifications' and 'configurationNotifications' to 'toolExecutionNotifications' and 'toolConfigurationNotifications'.

    1. [Issue #340](https://github.com/oasis-tcs/sarif-spec/issues/340): "Inline logical location object to location."

1. The following issues were closed without further action:

    1. [Issue #190](https://github.com/oasis-tcs/sarif-spec/issues/190): "Distinguish 'tool-specific' from 'generic' properties"

        This was an editorial task that I opened last year. I decided (and Michael agreed) it was not worth doing.

    1. [Issue #214](https://github.com/oasis-tcs/sarif-spec/issues/214): "Improve look-up semantics for message strings"

        This was about saying that you look up `result.message` in `theRule.messageStrings` first, and only then look for it in `theComponent.globalMessageStrings`. Actually the spec already said that, but I clarified it as part of the rework of the lookup procedure that resulted from #179 (toolComponent), #311 (notification metadata), #324 (descriptor reference), #325 (remove old localization), and #338 (New localization and policies).

    1. [Issue #328](https://github.com/oasis-tcs/sarif-spec/issues/328): "Consider renaming invocation.executableLocation to invocation.driverLocation"

        We decided to reject this because the "driver" component might consist of multiple files, and here we particularly want to specify the primary executable,
        that is, the file containing the entry point. So `executableLocation` is good.

1. The following change drafts were made available prior to TC #33, but were inadvertently omitted from the Editor's Report:

    1. [Issue #291](https://github.com/oasis-tcs/sarif-spec/issues/291): "Update logical location kinds to accommodate XML and JSON paths"

    1. [Issue #326](https://github.com/oasis-tcs/sarif-spec/issues/326): "Change run.graphs and result.graphs from objects to arrays"

1. The following changes were made directly in the provisional draft, at editorial discretion:

    1. [Issue #106](https://github.com/oasis-tcs/sarif-spec/issues/106): "Scrub for broken links"

    1. [Issue #117](https://github.com/oasis-tcs/sarif-spec/issues/117): "Scrub for 'run vs. file' errors"

    1. [Issue #301](https://github.com/oasis-tcs/sarif-spec/issues/301): "Editorial issues from Jim Kupsch, part 2"

    1. [Issue #342](https://github.com/oasis-tcs/sarif-spec/issues/342): "Tracking item for minor adjustments to design and errata during spec authoring"

1. Change drafts were made available for the following issues:

    1. [Issue #168](https://github.com/oasis-tcs/sarif-spec/issues/168): "Consider adding codeflow.state to capture initial execution state for things like static variables"

    1. Combined change draft for:

        - [Issue #179](https://github.com/oasis-tcs/sarif-spec/issues/168): "Define tool component object to represent tool driver and its extensions/plugins"

        - [Issue #336](https://github.com/oasis-tcs/sarif-spec/issues/336): "Changes to toolComponent properties"

    1. [Issue #202](https://github.com/oasis-tcs/sarif-spec/issues/202): "Restore threadFlowLocation.kind"

    1. [Issue #302](https://github.com/oasis-tcs/sarif-spec/issues/302): "Add address property to physicalLocation object"

    1. [Issue #309](https://github.com/oasis-tcs/sarif-spec/issues/309): "Rename run.files to run.artifacts, fileLocation to artifactLocation."

    1. Combined change draft for:

        - [Issue #311](https://github.com/oasis-tcs/sarif-spec/issues/311): "Provide full metadata objects for notifications"

        - [Issue #324](https://github.com/oasis-tcs/sarif-spec/issues/324): "Define a reportingDescriptorReference object"

        - [Issue #325](https://github.com/oasis-tcs/sarif-spec/issues/325): "Remove current localization mechanism"

    1. [Issue #314](https://github.com/oasis-tcs/sarif-spec/issues/314): "Define result taxonomies"

    1. [Issue #315](https://github.com/oasis-tcs/sarif-spec/issues/315): "Specify URI normalization algorithm"

    1. [Issue #318](https://github.com/oasis-tcs/sarif-spec/issues/318): "Define protocol to allow embedded messages links to refer to other results"

    1. [Issue #319](https://github.com/oasis-tcs/sarif-spec/issues/319): "Converge all messages into a common format strings object"

    1. [Issue #320](https://github.com/oasis-tcs/sarif-spec/issues/320): "Provide a caching mechanism for duplicated code flow data"

    1. Combined change draft for:

        - [Issue #321](https://github.com/oasis-tcs/sarif-spec/issues/321): "Provide mechanism for inlining externalized properties data into the root log"

        - [Issue #335](https://github.com/oasis-tcs/sarif-spec/issues/335): "External property file related renames"

    1. [Issue #327](https://github.com/oasis-tcs/sarif-spec/issues/327): "Remove invocation.attachments"

    1. [Issue #337](https://github.com/oasis-tcs/sarif-spec/issues/337): "Allow toolComponents to be externalized"

    1. Combined change draft for:

        - 1. [Issue #338](https://github.com/oasis-tcs/sarif-spec/issues/338): "Localization and policies"

        - 1. [Issue #347](https://github.com/oasis-tcs/sarif-spec/issues/347): "Add 'referencedOnCommandLine' as a role"

    1. [Issue #341](https://github.com/oasis-tcs/sarif-spec/issues/341): "Rename all 'instanceGuid' properties to 'guid'"

    1. [Issue #344](https://github.com/oasis-tcs/sarif-spec/issues/344): "Add suppression object to allow persisting location data for in-source suppressions"

    1. [Issue #346](https://github.com/oasis-tcs/sarif-spec/issues/346): "Add 'reportingDescriptor.deprecatedNames' and 'deprecatedGuids' to match 'deprecatedIds' property"

    1. [Issue #348](https://github.com/oasis-tcs/sarif-spec/issues/348): "SARIF needs a mechanism to denote an in-flight or completed suppressions review"

    1. [Issue #350](https://github.com/oasis-tcs/sarif-spec/issues/350): "Rename reportingConfigurationOverride to configurationOverride"

    1. [Issue #353](https://github.com/oasis-tcs/sarif-spec/issues/353): "Rename reportingConfigurationOverride to configurationOverride"