This document presents the principles that govern how the SARIF TC incorporates changes
into the SARIF spec, and describes the workflow for incorporating agreed-upon changes.

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
be identified with the label `ready-for-review`in advance of each meeting. Relevant
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

* This process (with additional details) will be documented in the file `Workflow.md` in
  the repository.

* Changes to this process will be requested by opening an issue in the repository, and
  must be approved at a TC meeting.
