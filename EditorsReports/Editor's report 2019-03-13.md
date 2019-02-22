# Editor's report

Laurence J. Golding and Michael Fanning

Presented at TC Meeting #33, March 13th, 2019

1. After being approved as amended at the last TC meeting (#33), the following spec changes were merged into the provisional draft:

    1. [Issue #146](https://github.com/oasis-tcs/sarif-spec/issues/146): "Make result.ruleId a hierarchical string to accommodate 'sub-rules'"

    1. [Issue #312](https://github.com/oasis-tcs/sarif-spec/issues/312): "Consider adding 'updated' baselineState"

    1. [Issue #317](https://github.com/oasis-tcs/sarif-spec/issues/317): "Consider splitting resultLevel into result.level and result.kind"

    1. [Issue #322](https://github.com/oasis-tcs/sarif-spec/issues/322): "Please add a 'directory' role"

1. The following issues were closed without further action:

    1. [Issue #215](https://github.com/oasis-tcs/sarif-spec/issues/215): "Consider: 'review' or 'audit' result level. and reconsider 'note'"

        We added `"review"` as part of the change draft for #317. And add the F2F, we decided against introducing a new level like `"observation"` to cover one of the two current uses of `"note"`.

    1. [Issue #268](https://github.com/oasis-tcs/sarif-spec/issues/268): "Add result.useful and result.suppressionReasons"

        This is a p2 issue whose design we did not resolve. Changed labeling from `csd.2` to `future` and closed.

    1. [Issue #247](https://github.com/oasis-tcs/sarif-spec/issues/247): "Another request to add a formal web request object"

        Another p2 request that never made its way to the forefront of our attention. Changed labeling from `csd.2` to `future` and closed.

1. The formal spec language for the following issues was made available for review, and we will move their adoption in today's meeting:

    1. [Issue #327](https://github.com/oasis-tcs/sarif-spec/issues/327): "Remove invocation.attachments" -- made available on February 22, 2019.
