## multiformatMessageString object

### General{#multiformatmessagestring-object--general}

A `multiformatMessageString` object groups together all available textual formats for a message string.

### Localizable multiformatMessageStrings

Certain `multiformatMessageString`-valued properties in this document, for example, `reportingDescriptor.shortDescription` ([sec](#reportingdescriptor-object--shortdescription-property)), can be translated into other languages. We describe these properties as being "localizable." The description of every localizable property will state that it is localizable.

### text property{#multiformatmessagestring-object--text-property}

A `multiformatMessageString` object **SHALL** contain a property named `text` whose value is a non-empty string containing a plain text representation of the message including any links.

> NOTE: This property is required to ensure that the message is viewable even in contexts that do not support the rendering of formatted text.

### markdown property{#multiformatmessagestring-object--markdown-property}

A `multiformatMessageString` object **MAY** contain a property named `markdown` whose value is a non-empty string containing a formatted message ([sec](#formatted-messages)) expressed in GitHub-Flavored Markdown [cite](#GFM).

SARIF consumers that cannot (or choose not to) render formatted text **SHALL** ignore the `markdown` property and use the `text` property ([sec](#multiformatmessagestring-object--text-property)) instead.
