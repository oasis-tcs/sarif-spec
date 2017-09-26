# Introduction

This document presents the principles that govern how the SARIF TC incorporates changes
into the SARIF spec, and describes the workflow for incorporating agreed-upon changes.

# Principals and process

* We encourage discussion on the public issues. The Editors will ensure that issues are
filed in the GitHub repo, and will "curate" them by applying issue labels, ensuring
content from other sources (email) is recorded in the GitHub issue, etc.

* Any issues that require time-sensitive discussion will be driven through the mailing
list (this should be rare).

* Once a revision of the Working Draft has been accepted (for example,
`sarif-v1.0-wd01.docx`), the Editors will create a "provisional" draft with the next
number, for example `sarif-v1.0-wd02-provisional.docx`.

* The Editors will make all changes in the provisional copy, with change tracking enabled.

* Issues that are ready for final approval or which warrant discussion on the telecon will
be identified with the label `ready-for-approval`in advance of each meeting. Relevant
tracked changes and open comments in the current provisional working draft will also
reflect this status.

* After telecon approval/rejection, the Editors will "Accept" or "Reject" the relevant
changes in the Word document, remove the relevant comments from the document, and close
the GitHub issue, labeling it as either `resolved-fixed` or `resolved-wont-fix`.

* At certain times, the TC might decide to capture the current state of the Working Draft
in a _revised_ Working Draft (with the next revision number). In that case, the Editors
will:
    1. Copy the provisional draft (say, `sarif-v1.0-wd02-provisional.docx`) to a file
    with the correct name for the next "real" draft (in this example, copying
    `sarif-v1.0-wd02-provisional.docx` to `sarif-v1.0-wd02.docx`).

    2. _Revert all change-tracked changes, and remove all comments_ in the real draft
    (because none of those changes will have been accepted yet.

    3. Modify the metadata in the real draft so that the correct document identifier (in
    this example, `sarif-v1.0-wd02`) appears in the document footer.

    4. Rename the “provisional” draft to the next version number (in this example,
    renaming `sarif-v1.0-wd02-provisional.docx` to `sarif-v1.0-wd03-provisional.docx`).

* This process will be documented in the file `Workflow.md` in the repository.

* Changes to this process will be requested by opening an issue in the repository, and
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
- `ready-for-approval`: The issue has been discussed and a resolution reached, the spec has been edited with change tracking to reflect the change, and the change is ready for approval at the next TC meeting.
- `resolved-by-design`: If the issue is a bug, this label means that the existing behavior is as intended and will not be changed.
- `resolved-deferred`: The issue is deferred for consideration in a future version of the specification.
- `resolved-duplicate`: The issue is a duplicate of another.
- `resolved-fixed`: The changes to the spec have been approved at a TC meeting and have been merged into the Working Draft.
- `resolved-wont-fix`: If the issue is a bug, this label means that the bug will not be fixed. (This should be rare!) If the issue is an enhancement, this label means that the TC has decided not to incorporate the proposed change into the spec.