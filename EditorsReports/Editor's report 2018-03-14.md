# Editor's report

Laurence J. Golding and Michael Fanning

Presented at TC Meeting #12, March 14, 2018

1. After being approved at the last TC meeting (#11), the spec changes for the following issues were merged into the provisional draft:

    1. Issue [#82](https://github.com/oasis-tcs/sarif-spec/issues/82): "Add instance id to result object".

    2. Issue [#83](https://github.com/oasis-tcs/sarif-spec/issues/83): "Consider adding attachments property".

    3. Issue [#89](https://github.com/oasis-tcs/sarif-spec/issues/89): "date/time property issues with seconds".

    4. Issue [#90](https://github.com/oasis-tcs/sarif-spec/issues/90): "Introduce fileLocation object". 

    5. Issue [#91](https://github.com/oasis-tcs/sarif-spec/issues/91): "Represent original values for uriBaseId properties".

        As we agreed at TC #11, we specified in Appendix F that run.originalUriBaseIds is non-deterministic.

    6. Issue [#92](https://github.com/oasis-tcs/sarif-spec/issues/92): "Add stdin/stdout/stderr on invocation".
    
        This version proposes using `physicalLocation` objects rather than embedded strings to specify the contents of the streams.

    7. Issue [#94](https://github.com/oasis-tcs/sarif-spec/issues/94): "Add an invocation.arguments property".
 
    8. Issue [#104](https://github.com/oasis-tcs/sarif-spec/issues/104): "Introduce "producer" profile". 

2. The formal spec language for the following issues was made available for review on the specified dates, and we will move for their adoption in today's meeting:

    1. 