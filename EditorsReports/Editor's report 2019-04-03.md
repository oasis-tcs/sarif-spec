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

1. The following change drafts were available prior to TC #33 and they are still available:

    1. [Issue #291](https://github.com/oasis-tcs/sarif-spec/issues/291): "Update logical location kinds to accommodate XML and JSON paths"

1. Change drafts were made available for the following issues which had previously been "design approved" by the TC:

    1. [Issue #309](https://github.com/oasis-tcs/sarif-spec/issues/309): "Rename run.files to run.artifacts, fileLocation to artifactLocation."

    1. Combined change draft for:

        - [Issue #321](https://github.com/oasis-tcs/sarif-spec/issues/321): "Provide mechanism for inlining externalized properties data into the root log"

        - [Issue #335](https://github.com/oasis-tcs/sarif-spec/issues/335): "External property file related renames"

    1. [Issue #341](https://github.com/oasis-tcs/sarif-spec/issues/341): "Rename all 'instanceGuid' properties to 'guid'"
