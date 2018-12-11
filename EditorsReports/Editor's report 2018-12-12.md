# Editor's report

Laurence J. Golding and Michael Fanning

Presented at TC Meeting #29, December 12th, 2018

1. After being approved as amended at the last TC meeting (#28), the following spec changes were merged into the provisional draft:

    1. [Issue #186](https://github.com/oasis-tcs/sarif-spec/issues/186): "Ensure spec conforms to philosophy around not specifying result mgmt. behavior"

    1. [Issue #188](https://github.com/oasis-tcs/sarif-spec/issues/188): "Specify a default value for columnKind"

    1. [Issue #274](https://github.com/oasis-tcs/sarif-spec/issues/274): "Rename fileVersion to dottedQuadFileVersion and specify format constraint"

    1. [Issue #279](https://github.com/oasis-tcs/sarif-spec/issues/279): "logicalLocation.kind: remove 'package'"

    1. [Issue #280](https://github.com/oasis-tcs/sarif-spec/issues/280): "Provide optional result.rank value of 0.0 to 100.0"

    1. [Issue #284](https://github.com/oasis-tcs/sarif-spec/issues/284): "baselineState s/be present on all results or none"

    1. [Issue #285](https://github.com/oasis-tcs/sarif-spec/issues/285): "Provide a mechanism to associate a result with an invocation."

    1. [Issue #288](https://github.com/oasis-tcs/sarif-spec/issues/288): "ruleConfiguration.defaultLevel should not contain an 'open' value"

1. The following issues were closed without further action:

    1. [Issue #44](https://github.com/oasis-tcs/sarif-spec/issues/44): "Consider: Adding support for metrics"

        Marked `"future"`. Consider in next version of SARIF.

    1. [Issue #47](https://github.com/oasis-tcs/sarif-spec/issues/47): "Consider: adding field for cryptographically secure digital signature"

        A standard like "JSON Web Signature" (JWS) ([RFC7515](https://tools.ietf.org/html/rfc7515), [IANA JOSE](https://www.iana.org/assignments/jose/jose.xhtml)), which wraps an arbitrary Base64-encoded payload in a JSON object, serves the purpose without extending SARIF itself with properties for digital signing.

    1. [Issue #85](https://github.com/oasis-tcs/sarif-spec/issues/85): "Add language around signing SARIF files in spec"

        This was either a duplicate of [Issue #47](https://github.com/oasis-tcs/sarif-spec/issues/47) ("Consider: adding field for cryptographically secure digital signature"), or it was a request to add language to the spec suggesting the use of an external standard like [JSON Web Signature](https://tools.ietf.org/html/rfc7515). Either way, we're not doing it.

    1. [Issue #142](https://github.com/oasis-tcs/sarif-spec/issues/142): "Do we need to persist directory information?"

        The newly filed [Issue #294](https://github.com/oasis-tcs/sarif-spec/issues/294), "Add run.scope", generalizes this suggestion.

    1. [Issue #180](https://github.com/oasis-tcs/sarif-spec/issues/180): "Consider renaming result.analysisTarget to result.analysisScope"

        I restored this issue's original name, and marked it `resolved-by-design`, to emphasize that we have considered and rejected the request in its original form.
        
        In analyzing that request, I pointed out that there was in fact a new concept of "analysis scope", _distinct from "analysis target"_, that SARIF does not represent. The newly filed [Issue #294](https://github.com/oasis-tcs/sarif-spec/issues/294), "Add run.scope", captures that concept.

    1. [Issue #198](https://github.com/oasis-tcs/sarif-spec/issues/198): "Support for incremental scan results"

        The new `result.resultProvenance` object, which states the range of times and runs during which the result was detected, seems to cover Ykaterina's needs.

    1. [Issue #261](https://github.com/oasis-tcs/sarif-spec/issues/261): "Explore static text for clickthrough links"

        Nobody has strongly advocated for this.

1. I made the following changes at editorial discretion:

    1. [Issue #295](https://github.com/oasis-tcs/sarif-spec/issues/295): "Fix mistakes in Appendix I samples."

        Paul found several errors in the samples. Thanks!

1. The following issue was closed with a schema change that did not affect the spec or the object model:

    1. [Issue #151](https://github.com/oasis-tcs/sarif-spec/issues/151): "DRY out definitions of property bags in the schema"

        Rather than repeating the definition of the property bag on every object in the schema, we define it once and refer to the definition from every object.

1. The formal spec language for the following issues was made available for review on the specified dates, and we will move their adoption in today's meeting:

    1. [Issue #248](https://github.com/oasis-tcs/sarif-spec/issues/248): "Version control details not strongly associated with results" -- made available on December 9th, 2018.

    1. [Issue #270](https://github.com/oasis-tcs/sarif-spec/issues/270): "Schema needs to be carefully scrubbed for minItems and uniqueItems use for all arrays" -- made available on December 4th, 2018.

    1. [Issue #286](https://github.com/oasis-tcs/sarif-spec/issues/286): "Specify optional property file.sourceLanguage to guide in syntax-driven colorization of snippets" -- made available on December 10th, 2018.

    1. [Issue #287](https://github.com/oasis-tcs/sarif-spec/issues/287): "Define default for resultProvenance.lastDetectionTimeUtc" -- made available on December 9th, 2018.

    1. [Issue #292](https://github.com/oasis-tcs/sarif-spec/issues/292): "Specify a default for result.rank" -- made available on December 11th, 2018.

    1. [Issue #293](https://github.com/oasis-tcs/sarif-spec/issues/293): "Add rule.deprecatedIds" -- made available on December 7th, 2018.