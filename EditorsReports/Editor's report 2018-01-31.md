# Editor's report

Laurence J. Golding and Michael Fanning

Presented at TC Meeting #9, January 31, 2018

1. [Issue #77](https://github.com/oasis-tcs/sarif-spec/issues/77): "Retitle the provisional draft to 'v2'"

    The title of the specification is now Static Analysis Results Interchange Format (SARIF) Version **2.0**, and the provisional draft document is renamed accordingly.

    This avoids breaking Microsoft compilers and other tools which already produce and consumer SARIF v1.0.0.

2. After being approved at the last TC meeting (#8), the spec changes for the following issues were merged into the provisional draft:

    1. Issue [#33](https://github.com/oasis-tcs/sarif-spec/issues/33): "Should we allow formatting in messages?"

    2. Issue [#61](https://github.com/oasis-tcs/sarif-spec/issues/61): "Consider specifying a format for links embedded in our plain text messages."

    3. Issue [#69](https://github.com/oasis-tcs/sarif-spec/issues/69): "Consider providing a physicalLocation on a stackFrame"

    4. Issue [#72](https://github.com/oasis-tcs/sarif-spec/issues/72): "run.lang property needs a default value"

    5. A small set of clarifications, editorial changes, and corrections of inaccuracies.

3. After being approved as within editorial discretion, the spec changes for the following issues were made in the provisional draft:

    1. Issue [#65](https://github.com/oasis-tcs/sarif-spec/issues/65): "Ensure all syntax specifications are in EBNF"
    
    2. Issue [#73](https://github.com/oasis-tcs/sarif-spec/issues/73): "Alphabetize terms"
     
4. The formal spec language for the following issues was made available for review on the specified dates, and we will move for their adoption in today's meeting:

    1. Issue [#63](https://github.com/oasis-tcs/sarif-spec/issues/63): "Clarify that the keys in the run.files dictionary must be distinct when normalized" -- made available on January 20th, 2018.

    2. Issue [#66](https://github.com/oasis-tcs/sarif-spec/issues/66): "Enable traceability from converted SARIF file to original analysis tool log file" -- made available on January 20th, 2018.

5. Per discussion at the most recent teleconference (Meeting #8), the following issue is closed (we will not consider it further for SARIF v2):

    1. Issue [#46](https://github.com/oasis-tcs/sarif-spec/issues/46): "Consider: should the result object support graph information?"

6. The following issues are closed, because the concerns they raised have been addressed by Issue [#56](https://github.com/oasis-tcs/sarif-spec/issues/56): "Consider adding namespaces to tags"

    1. Issue [#3](https://github.com/oasis-tcs/sarif-spec/issues/3): "Introduce result.taxonomies"

    2. Issue [#35](https://github.com/oasis-tcs/sarif-spec/issues/35): "Consider: Adding CWE property to result object" 

7. The following issues are deferred to the next teleconference, when all interested parties can attend:

    1. Issue [#55](https://github.com/oasis-tcs/sarif-spec/issues/55): "Consider restructuring SARIF to be location, not results-focused"

