# Editor's report

Laurence J. Golding and Michael Fanning

Presented at TC Meeting #12, March 14, 2018

1. After being approved at the last TC meeting (#11), the spec changes for the following issues were merged into the provisional draft:

    1. [Issue #82](https://github.com/oasis-tcs/sarif-spec/issues/82): "Add instance id to result object".

    2. [Issue #83](https://github.com/oasis-tcs/sarif-spec/issues/83): "Consider adding attachments property".

    3. [Issue #89](https://github.com/oasis-tcs/sarif-spec/issues/89): "date/time property issues with seconds".

    4. [Issue #90](https://github.com/oasis-tcs/sarif-spec/issues/90): "Introduce fileLocation object". 

    5. [Issue #91](https://github.com/oasis-tcs/sarif-spec/issues/91): "Represent original values for uriBaseId properties".

        As we agreed at TC #11, we specified in Appendix F that run.originalUriBaseIds is non-deterministic.

    6. [Issue #92](https://github.com/oasis-tcs/sarif-spec/issues/92): "Add stdin/stdout/stderr on invocation".
    
        This version proposes using `physicalLocation` objects rather than embedded strings to specify the contents of the streams.

    7. [Issue #94](https://github.com/oasis-tcs/sarif-spec/issues/94): "Add an invocation.arguments property".
 
    8. [Issue #104](https://github.com/oasis-tcs/sarif-spec/issues/104): "Introduce "producer" profile".

2. We made the following (presumably non-controversial) changes, and we will move their adoption in today's meeting:

    1. Specify that the `result.attachments` array and the `invocation.attachments` array each consist of one or more unique elements.

3. We made the following purely editorial changes:

    1. When a property is defined to be of type "JSON object", add a cross-reference to §3.4, "Object properties".

    2. Fix a section heading ("Attachments" => "attachments property"). 

2. The formal spec language for the following issues was made available for review on the specified dates, and we will move their adoption in today's meeting:

    1. [Issue #10](https://github.com/oasis-tcs/sarif-spec/issues/10): "Do we want an array of computed fingerprints on result?" -- made available on March 6th, 2018.

    2. [Issue #15](https://github.com/oasis-tcs/sarif-spec/issues/15): "Document how converters should provide notifications" -- made available on March 6th, 2018.

    3. [Issue #23](https://github.com/oasis-tcs/sarif-spec/issues/23): "Clarify requirement for format of URI-valued properties for nested files" -- made available on March 6th, 2018.

    4. [Issue #29](https://github.com/oasis-tcs/sarif-spec/issues/29): "Document rule.configuration" -- made available on March 6th, 2018.

    5. [Issue #84](https://github.com/oasis-tcs/sarif-spec/issues/84): "Enable localization for all message strings" -- made available on March 5th, 2018.