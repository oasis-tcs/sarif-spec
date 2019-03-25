# Editor's report

Laurence J. Golding and Michael Fanning

Presented at TC Meeting #34, April 3th, 2019

1. After being approved as amended at previous TC meetings, the following spec changes were merged into the provisional draft:

    1. [Issue #330](https://github.com/oasis-tcs/sarif-spec/issues/330): "Rename 'invocation.toolNotifications' and 'configurationNotifications' to 'toolExecutionNotifications' and 'toolConfigurationNotifications'.

    1. [Issue #340](https://github.com/oasis-tcs/sarif-spec/issues/340): "Inline logical location object to location."

1. The following issues were closed without further action:

    1. [Issue #328](https://github.com/oasis-tcs/sarif-spec/issues/328): "Consider renaming invocation.executableLocation to invocation.driverLocation"

        We decided to reject this because the "driver" component might consist of multiple files, and here we particularly want to specify the primary executable,
        that is, the file containing the entry point. So `executableLocation` is good.

1. The following change drafts were made available prior to TC #33, but were inadvertently omitted from the Editor's Report:

    1. [Issue #291](https://github.com/oasis-tcs/sarif-spec/issues/291): "Update logical location kinds to accommodate XML and JSON paths"

    1. [Issue #326](https://github.com/oasis-tcs/sarif-spec/issues/326): "Change run.graphs and result.graphs from objects to arrays"

1. Change drafts were made available for the following issues:

    1. [Issue #168](https://github.com/oasis-tcs/sarif-spec/issues/168): "Consider adding codeflow.state to capture initial execution state for things like static variables"

    1. Combined change draft for:

        - [Issue #179](https://github.com/oasis-tcs/sarif-spec/issues/168): "Define tool component object to represent tool driver and its extensions/plugins"

        - [Issue #336](https://github.com/oasis-tcs/sarif-spec/issues/336): "Changes to toolComponent properties"

    1. [Issue #309](https://github.com/oasis-tcs/sarif-spec/issues/309): "Rename run.files to run.artifacts, fileLocation to artifactLocation."

    1. [Issue #319](https://github.com/oasis-tcs/sarif-spec/issues/319): "Converge all messages into a common format strings object"

    1. Combined change draft for:

        - [Issue #321](https://github.com/oasis-tcs/sarif-spec/issues/321): "Provide mechanism for inlining externalized properties data into the root log"

        - [Issue #335](https://github.com/oasis-tcs/sarif-spec/issues/335): "External property file related renames"

    1. [Issue #337](https://github.com/oasis-tcs/sarif-spec/issues/337): "Allow toolComponents to be externalized"

    1. [Issue #341](https://github.com/oasis-tcs/sarif-spec/issues/341): "Rename all 'instanceGuid' properties to 'guid'"

    1. Combined change draft for:

        - [Issue #311](https://github.com/oasis-tcs/sarif-spec/issues/311): "Provide full metadata objects for notifications"

        - [Issue #324](https://github.com/oasis-tcs/sarif-spec/issues/324): "Define a reportingDescriptorReference object"

        - [Issue #325](https://github.com/oasis-tcs/sarif-spec/issues/325): "Remove current localization mechanism"
    
    1. [Issue #314](https://github.com/oasis-tcs/sarif-spec/issues/314): "Define result taxonomies"

    1. [Issue #327](https://github.com/oasis-tcs/sarif-spec/issues/327): "Remove invocation.attachments"

    1. [Issue #344](https://github.com/oasis-tcs/sarif-spec/issues/344): "Add suppression object to allow persisting location data for in-source suppressions"

    1. [Issue #346](https://github.com/oasis-tcs/sarif-spec/issues/346): "Add 'reportingDescriptor.deprecatedNames' and 'deprecatedGuids' to match 'deprecatedIds' property"
