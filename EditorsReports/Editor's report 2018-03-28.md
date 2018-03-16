# Editor's report

Laurence J. Golding and Michael Fanning

Presented at TC Meeting #13, March 28, 2018

1. After being approved at the last TC meeting (#11), the following spec changes were merged into the provisional draft:

    1. Editorial changes as described in Editor's Report of March 14th, 2018.
   
    2. [Issue #10](https://github.com/oasis-tcs/sarif-spec/issues/10): "Do we want an array of fingerprint contributions on result?"

        NOTE 1: I changed the issue title to correctly reflect the change as we approved it.

        NOTE 2: The merged text includes the amendment to rename `toolFingerprintContributions` to `fingerprintContributions`.

    3. [Issue #15](https://github.com/oasis-tcs/sarif-spec/issues/15): "Document how converters should provide notifications"


    4. [Issue #23](https://github.com/oasis-tcs/sarif-spec/issues/23): "Clarify requirement for format of URI-valued properties for nested files"

        NOTE: The merged text includes the amendment to avoid the term "absolute path" when referring to the path to a nested file from the root of its outermost container.

    5. [Issue #29](https://github.com/oasis-tcs/sarif-spec/issues/29): "Introduce object-valued rule configuration"
 
        NOTE: I changed the issue title to correctly reflect the change as we approved it.

        NOTE: The merged text includes the amendment we agreed to, to fix a typo from "properties" to "parameters".

    6. [Issue #84](https://github.com/oasis-tcs/sarif-spec/issues/84): "Enable localization for all message strings"

    7. [Issue #110](https://github.com/oasis-tcs/sarif-spec/issues/110): "Specify how to treat a file that contains interleaved stdout/stderr"

2. I made the following editorial changes:

    1. Since our first public version will be `2.0.0`, I changed the description of `run.version` to require its value to be `2.0.0` instead of `1.0.0`, and I fixed up the examples that mentioned `run.version`.
