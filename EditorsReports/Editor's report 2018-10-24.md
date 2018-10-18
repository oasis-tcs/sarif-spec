# Editor's report

Laurence J. Golding and Michael Fanning

Presented at TC Meeting #26, October 24th, 2018

1. The following issues were closed without further action:

    1. [Issue #3](https://github.com/oasis-tcs/sarif-spec/issues/3): "Introduce result.taxonomies"

        Previously closed; reopened during Microsoft internal SARIF testing. Now closing again; per @michaelcfanning:
        > Hierarchical tags satisfy the parties that prompted reactivation.

    1. [Issue #200](https://github.com/oasis-tcs/sarif-spec/issues/200): "Require everything to be UTF-8"

        I added the following [comment](https://github.com/oasis-tcs/sarif-spec/issues/200#issuecomment-431111049) to the issue explaining why the spec can't say any more about file encoding than it already does:

        > I agree that the spec says as much as it can about encoding:
        > - The SARIF log file must be encoded in UTF-8 (§3.1).
        > - As a result, embedded file content (`fileContent.text`, §3.2.2) must be UTF-8 (transcoded from the original file encoding if necessary).
        > - `file.encoding` (§3.19.9) is optional, and if absent, the original file encoding is taken to be unknown.
        >
        > I believe it's that last point that @katrinaoneil's colleague objects to, but it's unavoidable in some cases. For example, Semmle takes a _snapshot_ of a code base, saves the snapshot in UTF-8, and then analyzes the snapshot. Once the snapshot is taken, Semmle does not remember the original file encoding.
        >
        > That might seem to imply that the encoding in this case is UTF-8. The problem is that if the SARIF file includes `fix` objects, those fixes might refer to the wrong portion of the original file if that file is in any other encoding. In this scenario, the SARIF log file needs to record the fact that it just doesn't know the original file encoding.

    1. [Issue #264](https://github.com/oasis-tcs/sarif-spec/issues/264): "Do we need an escaping mechanism for slashes in hierarchical strings?"

        Resolved as duplicate of [Issue #183](https://github.com/oasis-tcs/sarif-spec/issues/183): "Consider providing a mechanism to escape forward slashes in hierarchical strings"

1. After being approved as amended at the last TC meeting (#24), the following spec changes were merged into the provisional draft:

    1. [Issue #217](https://github.com/oasis-tcs/sarif-spec/issues/217): "Consider adding a discrete 'id' object"

    1. [Issue #219](https://github.com/oasis-tcs/sarif-spec/issues/219): "Delete 'threadFlowLocation.step' property"

    1. [Issue #249](https://github.com/oasis-tcs/sarif-spec/issues/249): "Rename versionControlDetails.tag to revisionTag"

    1. [Issue #250](https://github.com/oasis-tcs/sarif-spec/issues/250): "Consider result-level URI for alternate viewer"

1. I made the following changes at editorial discretion:

    1. [Issue #213](https://github.com/oasis-tcs/sarif-spec/issues/213): "Avoid use of implementation specific JSON term where possible"

    1. [Issue #257](https://github.com/oasis-tcs/sarif-spec/issues/257): "Editorial: Remove misleading uriBaseId examples"

1. The formal spec language for the following issues was made available for review on the specified dates, and we will move their adoption in today's meeting:

