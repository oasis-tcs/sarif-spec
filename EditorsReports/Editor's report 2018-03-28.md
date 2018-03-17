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

        NOTE: The merged text includes the amendment to avoid the term "absolute path" when referring to the path to a nested file from the root of its outermost container. (This also affects Issue #64, below.)

    5. [Issue #29](https://github.com/oasis-tcs/sarif-spec/issues/29): "Introduce object-valued rule configuration"
 
        NOTE: I changed the issue title to correctly reflect the change as we approved it.

        NOTE: The merged text includes the amendment we agreed to, to fix a typo from "properties" to "parameters".

    6. [Issue #63](https://github.com/oasis-tcs/sarif-spec/issues/63): "Clarify that the keys in the run.files dictionary must be distinct when normalized"

    7. [Issue #64](https://github.com/oasis-tcs/sarif-spec/issues/64): "run.files keys can collide if specified by relative URLs"

        NOTE: The merged text includes the amendment we agreed to:

        - Don't use the term "absolute path" when referring to the path to a nested file from the root of its outermost container. (This also affects Issue #23, above.)

        - Add requirement that `uriBaseId` can't include `"#"` character.

        - Fix typo "valueed" => "valued"

    8. [Issue #76](https://github.com/oasis-tcs/sarif-spec/issues/76): "Clarify encoding requirements for properties that contain text from source files"

    9. [Issue #84](https://github.com/oasis-tcs/sarif-spec/issues/84): "Enable localization for all message strings"

    10. [Issue #97](https://github.com/oasis-tcs/sarif-spec/issues/97): "file object's contents property"

    11. [Issue #102](https://github.com/oasis-tcs/sarif-spec/issues/102): "run.invocation should be an array of invocation objects"

        NOTE: The merged text includes the amendments we agreed to:

        - The elements of the `invocation` array SHOULD be arranged in chronological order if possible. (It might not be possible if some of the processes run in parallel.)

        - The `toolNotifications` and `configurationNotifications` belong in the `invocation` object, not in the `run` object. This was always true, but making `run.invocation` into an array made it clear that each process might produce its own notifications.

        NOTE: I changed the property name from `invocation` to `invocations` because otherwise it would be the only array-valued property in the specification with a singular name.

    12. [Issue #110](https://github.com/oasis-tcs/sarif-spec/issues/110): "Specify how to treat a file that contains interleaved stdout/stderr"

    13. [Issue #128](https://github.com/oasis-tcs/sarif-spec/issues/128): "Specify SARIF file encoding as UTF-8"

        NOTE: We approved this in the TC meeting. It was not tracked by an issue. I filed the issue _post hoc_.

2. I made the following editorial changes:

    1. Since our first public version will be `2.0.0`, I changed the description of `run.version` to require its value to be `2.0.0` instead of `1.0.0`, and I fixed up the examples that mentioned `run.version`.

    2. Removed FIPS PUB 180-4 from the list of normative references (it's no longer referenced).


