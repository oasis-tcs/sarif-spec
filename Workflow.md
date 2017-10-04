# Introduction

This document presents the principles that govern how the SARIF TC incorporates changes
into the SARIF spec, and describes the workflow for incorporating agreed-upon changes.

# Principals and process

1. We encourage discussion on the public issues. The Editors will ensure that issues are
filed in the GitHub repo, and will "curate" them by applying issue labels, ensuring
content from other sources (email) is recorded in the GitHub issue, _etc._

1. Any issues that require time-sensitive discussion will be driven through the mailing
list (this should be rare).

1. Once a revision of the Working Draft has been accepted (for example,
`sarif-v1.0-wd01.docx`), the Editors will create a "provisional" draft with the next
number (for example `sarif-v1.0-wd02-provisional.docx`).

1. When a change is proposed, the Editors will push a copy of the _current_ Working Draft
    to the Drafts folder of the repo.
    The copy will have a name of the form `sarif-issue-<issueNumber>-<mnemonic>.docx`.
    We refer to this copy as a "change draft".

    **NOTE**: This does *not* require a PR.

    The "mnemonic" is a short string (at most a few words) that distinguishes
    this change from other, competing proposals that address the same issue.
    For example, if there are two competing proposals to address Issue #&#xfeff;3,
    there might be two change drafts:

    * `sarif-issue-3-multiple-classifications.docx`

    * `sarif-issue-3-single-classification.docx`

1. The Editors will make all changes in the change draft, with change tracking enabled.

1. When an issue is ready for final approval, the Editors will:

    1. Label the issue `ready-for-approval`.

    1. Place a comment at the top of the change draft stating that the proposal is ready.

    1. Push the latest version of the change draft to the repo.

           **NOTE**: This does *not* require a PR.

1. If an issue requires further discussion at the next TC meeting, the Editors will:

    1. Label the issue `discussion-ongoing`.

    1. Place a comment at the top of the change draft stating that the proposal requires
    further discussion.

    1. Push the latest version of the change draft to the repo.

           **NOTE**: This does *not* require a PR.

1. If the TC approves a change (or one of a set of competing changes), the Editors will:

    1. Merge the changes from the approved change draft into the provisional draft, with change tracking enabled.

           **NOTE**: We can use Word's "Combine documents" feature (on the Review tab of the ribbon) to accomplish this easily.

    1. Label the issue `resolved-fixed`.

    1. Close the issue.

    1. Place a comment at the top of the approved change draft stating that the proposal was approved.

    1. Place a comment at the top of any competing change draft stating that the proposal was rejected.

1. If the TC rejects a change (or rejects every one of a set of competing changes),
and if the TC further decides not to continue to address the issue, the Editors will:

    1. Label the issue `resolved-wont-fix`.

    1. Close the issue.

    1. Place a comment at the top of every associated change draft stating that the proposal
    was rejected.

1. At certain times, the TC might decide to capture the current state of the provisional draft
in a revised Working Draft (with the next revision number). In that case, the Editors
will:

    1. Accept all change-tracked changes in the provisional draft
    (for example, `sarif-v1.0-wd02-provisional.docx`), and remove all comments.
    
    1. Modify the document metadata in the provisional draft so that the correct document identifier
    (in this example, `sarif-v1.0-wd02`) appears in the document footer.

    1. Copy the provisional draft  to a file with the correct name for the next Working Draft
    (in this example, copying `sarif-v1.0-wd02-provisional.docx` to `sarif-v1.0-wd02.docx`).

    1. Rename the provisional draft to the next version number (in this example,
    renaming `sarif-v1.0-wd02-provisional.docx` to `sarif-v1.0-wd03-provisional.docx`).

1. This process will be documented in the file `Workflow.md` in the repository.

1. Changes to this process will be requested by opening an issue in the repository, and
  must be approved at a TC meeting.

# Issue labels

We will track the workflow status of issues in the repo with a set of labels.
These labels are mostly a subset of the labels in the [original spec repo](https://github.com/sarif-standard/sarif-spec):

- `bug`: The issue prevents the file format from correctly and consistently representing the information necessary to support the scenarios for which it is designed.
- `enhancement`: The proposal adds support to the spec for a new scenario, or provide richer support for a supported scenario.
- `domain-result-management`: The issue is specific to the domain of result management.
- `domain-security`: The issue is specific to the security domain.
- `impact-breaks-consumers`: The proposed change to the format would prevent consumers of the format, such as viewers or result management systems, from consuming some or all valid log files.
- `impact-breaks-producers`: The proposed change to the format would render invalid log files created by existing producers, such as analysis tools or converters.
- `impact-documentation-only`: The proposed change clarifies or enhances the documentation, but does not affect the format.
- `impact-non-breaking-change`: The proposed change to the format is backward compatible with all conforming producers and consumers.
- `process`: The issue relates to the process of producing the TC's work products, rather than to the content of the work products themselves.
- `prototype-needed`: The practicality of implementing the proposed change is unclear; the change should be prototyped in code before being considered for adoption.
- `question`: The issue is a request for information, not a proposal to change the format or the documentation.
- `discussion-ongoing`: The issue requires further discussion at the next TC meeting.
- `ready-for-approval`: The issue has been discussed and a resolution reached, the spec has been edited with change tracking to reflect the change, and the change is ready for approval at the next TC meeting.
- `resolved-by-design`: If the issue is a bug, this label means that the existing behavior is as intended and will not be changed.
- `resolved-deferred`: The issue is deferred for consideration in a future version of the specification.
- `resolved-duplicate`: The issue is a duplicate of another.
- `resolved-fixed`: The changes to the spec have been approved at a TC meeting and have been merged into the Working Draft.
- `resolved-wont-fix`: If the issue is a bug, this label means that the bug will not be fixed. (This should be rare!) If the issue is an enhancement, this label means that the TC has decided not to incorporate the proposed change into the spec.