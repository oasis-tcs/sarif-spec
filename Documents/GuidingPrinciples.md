
1. The primary purpose of SARIF is to enable low cost development of rich functionality (viewers, work item filers, etc.) that operates against a broad range of SARIF producers. A key design principle for all SARIF properties, therefore, is that any proposed data should be clearly useful in a consumption scenario.

2. As an important but secondary concern, SARIF is designed to allow the output of existing tools to be normalized to a common format. In order to support the ability for consumers to process, display, etc., this information in an appropriate and consistent way, it must be possible to normalize any proposed SARIF data to a common form.

3. The SARIF format specification should clearly describe the semantic meaning and intended purpose for all properties, to assist producers in populating this data with values that drive effective consumption.

4. SARIF defines a range of data that shall be expressed in order to best support static analysis tooling. The specification describes a JSON implementation of this standard. It should be possible to define other implementations (such as XML).

5. SARIF is designed for static analysis tools and any concept that generally applies for this scenario shall be considered for the format. SARIF can clearly be used for many dynamic analysis scenarios and we should consider augmenting the format for this class of tooling, but not in cases where what is proposed is applicable to the dynamic analysis domain only.

6. SARIF is domain-agnostic; that is, it does not contain objects or properties that are specific to a single domain, such as security or compliance. However, SARIF might define specific values for properties that are specific to a single domain. For example, the proposed result.taxonomies property might define a dictionary entry whose key invokes a standard classification for memory safety issues only.

7. The SARIF design is focused on expressing results as produced by a tool at a specific point-in-time and current excludes detailed thinking related to results management (associated result work item, false positive evaluation, etc.). These concepts may be addressed by defining or proposing 'profiles' that broaden SARIF's design surface area, contingent on progress with core work.

8. In cases where SARIF permits the same information to be expressed in more than one way, any or all of those representations may be present. This allows producers to persist all the information they have, and it allows consumers to choose the representation they prefer. SARIF requires all the representations to be consistent.

    Example: SARIF allows you to specify the start of a `region` either with the `startLine` and `startColumn` properties, or with the `offset` property. It's ok for both to be present, as long as they're consistent.