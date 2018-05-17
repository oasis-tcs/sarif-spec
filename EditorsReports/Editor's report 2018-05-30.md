# Editor's report

Laurence J. Golding and Michael Fanning

Presented at TC Meeting #18, May 30th, 2018

1. After being approved as amended at the last TC meeting (#16), the following spec changes were merged into the provisional draft:

    1. [Issue #103](https://github.com/oasis-tcs/sarif-spec/issues/103): "Specify handling of line breaks"

    1. [Issue #138](https://github.com/oasis-tcs/sarif-spec/issues/138): "Consider a download/install uri for the tool"

    1. [Issue #141](https://github.com/oasis-tcs/sarif-spec/issues/141): "Consider adding timestamp to file object"

    1. [Issue #143](https://github.com/oasis-tcs/sarif-spec/issues/143): "Add 'returnType', 'parameter' and 'variable' to logical location kind enum"

    1. [Issue #153](https://github.com/oasis-tcs/sarif-spec/issues/153): "Clarify treatment of backslashes and square brackets with respect to embedded links"

    1. [Issue #157](https://github.com/oasis-tcs/sarif-spec/issues/157): "Clarify requirements on tool.semanticVersion"

    1. [Issue #159](https://github.com/oasis-tcs/sarif-spec/issues/159): "Id property renames"

    1. [Issue #160](https://github.com/oasis-tcs/sarif-spec/issues/160): "Roles for edited files"

    1. [Issue #161](https://github.com/oasis-tcs/sarif-spec/issues/161): "Expand code flows to represent dynamic execution events"

    1. [Issue #162](https://github.com/oasis-tcs/sarif-spec/issues/162): "run.automationId is namespaced"

    1. [Issue #163](https://github.com/oasis-tcs/sarif-spec/issues/163): "Add result.workItemLocation"

    1. [Issue #165](https://github.com/oasis-tcs/sarif-spec/issues/165): "Add run.description"

    1. [Issue #166](https://github.com/oasis-tcs/sarif-spec/issues/166): "Define an "engineering system" conformance profile"

1. I made the following changes at editorial discretion:

    1. [Issue #167](https://github.com/oasis-tcs/sarif-spec/issues/167): "Document comprehensive example is out of date"

    1. [Issue #170](https://github.com/oasis-tcs/sarif-spec/issues/170): "logicalLocation.name: text and examples are unclear/wrong"

    1. Fix up the remaining places where I said "the B object in which A occurs" instead of my preferred formulation, "the A object's containing B object".

    1. Introduced the concept of "baseline run" ("baseline") already existed and used it to describe both `file.roles` and `result.baselineState`. Added quasi-editorial statement that engineering system **SHALL** provide out of band information to determine baseline run.

1. The formal spec language for the following additional issues was made available for review on the specified dates, and we will move their adoption in today's meeting:

    1. ...