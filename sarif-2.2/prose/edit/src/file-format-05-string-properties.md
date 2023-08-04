## String properties

### Localizable strings

Certain string-valued properties in this document, for example, `toolComponent.name` ([sec](#toolcomponent-object--name-property)), can be translated into other languages. We describe these properties as being "localizable." The description of every localizable property will state that it is localizable.

### Redactable strings

Certain string-valued properties in this document (for example, `invocation.commandLine` ([sec](#commandline-property))) might contain sensitive information that a SARIF producer or a SARIF post-processor might choose to redact. We describe these properties as "redactable." The description of every redactable property will state that it is redactable.

If a SARIF producer or a SARIF post-processor chooses to redact sensitive information in a redactable property, it **SHALL** replace the sensitive information with a string whose value is an element of `theRun.redactionTokens` ([sec](#redactiontokens-property)).

### GUID-valued strings

Certain string-valued properties in this document provide unique stable identifiers in the form of a GUID or UUID \[[cite](#RFC4122)\]. This document uses the term "GUID".

> EXAMPLE: `"f81d4fae-7dec-11d0-a765-00a0c91e6bf6"`

> NOTE 1: The UUID standard \[[cite](#RFC4122)\] allows hex digits in either upper or lower case. It does not permit delimiters such as curly braces (`"{"`, `"}"`) around the value.

The description of every GUID-valued property will state that it is GUID-valued.

> NOTE 2: In the examples, the values shown for GUID-valued properties are valid GUIDs. In some cases, they are illustrative values such as `"11111111-1111-1111-8888-111111111111"` which are intended to make it easy to identify situations where two GUIDs in the same example are required to be the same. In these illustrative values, the third and fourth component are always `"1111-8888"`, a sample value that conforms to the restrictions on the values of those components.

### Hierarchical strings

#### General{#hierarchical-strings--general}

Certain string-valued properties and certain property names in this document (for example, the value of the `runAutomationDetails.id` property ([sec](#runautomationdetails-object--id-property)), and the property names in a property bag ([sec](#property-bags))) are said to be "hierarchical." This means that the string consists of a sequence of forward-slash-separated components, with this syntax:

```
hierarchical string = component, { "/", component };

component = { component character };

component character = ? JSON string character ? - "/";
```

> NOTE 1: The grammar prohibits a `component` from containing a forward slash. There is no escape mechanism to allow a `component` to include a forward slash.

For examples, see [sec](#tags) and [sec](#runautomationdetails-object--id-property).

The description of every hierarchical string will state that it is hierarchical.

A SARIF consumer **SHALL** interpret the values of a hierarchical string as forming a logical hierarchy. The first component represents the top level of the hierarchy, the second component represents the second level, and so on.

> NOTE 2: A hierarchical string does not need to include any forward slashes. The syntax permits a single string of non-forward-slash characters. The purpose of this section is to define the semantics of the forward slash character in those properties that respect it.

In string-valued properties and property names that are *not* described as hierarchical, the forward slash character has no special meaning, and a SARIF consumer **SHALL NOT** interpret it as dividing the value into hierarchical components.

#### Versioned hierarchical strings

Certain hierarchical strings in this document (for example, the property names in `result.fingerprints` ([sec](#fingerprints-property)) and `result.partialFingerprints` ([sec](#partialfingerprints-property))) are said to be "versioned." This means that if the last `component` of the string is of the form

    version component = "v", non negative integer;

then a SARIF consumer **SHALL** consider that component to represent the version number of the entity specified by the string.

The description of every versioned hierarchical string will state that it is versioned.

In string-valued properties and property names that are described as hierarchical but *not* as versioned, a final `component` matching the syntax of `version component` has no special meaning, and a SARIF consumer **SHALL NOT** interpret it as a version number.

> NOTE 1: A versioned hierarchical string does not need to include a version component. The syntax permits but does not require it.

A hierarchical string without a version component **SHALL** be considered older than any corresponding string with a version component.

> EXAMPLE: In this example, the partial fingerprint whose property name is `"prohibitedWordHash"` is considered to have been computed with an older version of the "prohibited word hash" algorithm than the partial fingerprint whose property name is `"prohibitedWordHash/v1"`.
> 
> ```json
> {                                 # A result object (§3.27).
>   "partialFingerprints": {        # See §3.27.17.
>     "prohibitedWordHash": "4efcc21977b55",
>     "prohibitedWordHash/v2": "097886bc876fe"
>   }
> }
> ```

> NOTE 2: When a previously unversioned string is later versioned, as in the example above, it might be clearer to specify `"v2"` for the first explicitly versioned string.
