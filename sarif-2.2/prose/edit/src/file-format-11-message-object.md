## message object

### General{#message-object--general}

Certain objects in this document define messages intended to be viewed by a user. SARIF represents such a message with a `message` object, which offers the following features:

- Message strings in plain text ("plain text messages") ([sec](#plain-text-messages)).

- Message strings that incorporate formatting information ("formatted messages") in GitHub Flavored Markdown [cite](#GFM) ([sec](#formatted-messages)).

- Message strings with placeholders for variable information ([sec](#messages-with-placeholders)).

- Message strings with embedded links ([sec](#messages-with-embedded-links)).

### Constraints{#message-object--constraints}

At least one of the `text` ([sec](#message-object--text-property)) or `id` ([sec](#message-object--id-property)) properties **SHALL** be present.

> NOTE: This ensures that a SARIF consumer can locate the text of the message.

### Plain text messages

A plain text message **SHALL NOT** contain formatting information, for example, HTML tags or white space whose purpose is to provide indentation or suggest some structure to the message.

If a plain text message consists of multiple paragraphs, it **MAY** contain line breaks (for example, `"\r\n"` or `"\n"`, if the SARIF log file is serialized as JSON) to separate the paragraphs. Line breaks **MAY** follow any convention (for example, `"\n"` or `"\r\n"`). A SARIF post-processor **MAY** normalize line breaks to any desired convention, including escaping or removing the line breaks so that the entire message renders on a single line.

The message string **MAY** contain placeholders ([sec](#messages-with-placeholders)) and embedded links ([sec](#messages-with-embedded-links)).

If the message consists of more than one sentence, its first sentence **SHOULD** provide a useful summary of the message, suitable for display in cases where UI space is limited.

> NOTE 1: If a tool does not construct the message in this way, the initial portion of the message that a viewer displays where UI space is limited might not be understandable.

> NOTE 2: The rationale for these guidelines is that the SARIF format is intended to make it feasible to merge the outputs of multiple tools into a single user experience. A uniform approach to message authoring enhances the quality of that experience.

A SARIF post-processor **SHOULD NOT** modify line break sequences (except perhaps to adapt them to a particular viewing environment).

### Formatted messages

#### General{#formatted-messages--general}

Formatted messages **MAY** be of arbitrary length and **MAY** contain formatting information. The message string **MAY** also contain placeholders ([sec](#messages-with-placeholders)) and embedded links ([sec](#messages-with-embedded-links)).

Formatted messages **SHALL** be expressed in GitHub-Flavored Markdown [cite](#GFM). Since GFM is a superset of CommonMark [cite](#CMARK), any CommonMark Markdown syntax is acceptable.

#### Security implications

For security reasons, SARIF producers and consumers **SHALL** adhere to the following:

- SARIF producers **SHALL NOT** emit messages that contain HTML, even though all variants of Markdown permit it.

- Deeply nested markup can cause a stack overflow in the Markdown processor [cite](#GFMENG). To reduce this risk, SARIF consumers **SHALL** use a Markdown processor that is hardened against such attacks.

    NOTE: One example is the GitHub fork of the cmark Markdown processor [cite](#GFMCMARK).

- To reduce the risk posed by possibly malicious SARIF files that do contain arbitrary HTML (including, for example, `javascript:` links), SARIF consumers **SHALL** either disable HTML processing (for example, by using an option such as the `--safe` option in the cmark Markdown processor) or run the resulting HTML through an HTML sanitizer.

SARIF consumers that are not prepared to deal with the security implications of formatted messages **SHALL NOT** attempt to render them and **SHALL** instead fall back to the corresponding plain text messages.

### Messages with placeholders

A message string **MAY** include one or more "placeholders." The syntax of a placeholder is:

    placeholder = "{", index, "}";

    index = non negative integer;

`index` represents a zero-based index into the array of strings contained in the `arguments` property ([sec](#message-object--arguments-property)).

When a SARIF consumer displays the message, it **SHALL** replace every occurrence of the placeholder `{n}` with the string value at index `n` in the `arguments` array. Within both plain text and formatted message strings, the characters "`{`" and "`}`" **SHALL** be represented by the character sequences "`{{`" and "`}}`" respectively.

Within a given `message` object:

- The plain text and formatted message strings **MAY** contain different numbers of placeholders.

- A given placeholder index **SHALL** have the same meaning in the plain text and formatted message strings (so they can be replaced with the same element of the `arguments` array).

> EXAMPLE 1: Suppose a `message` object’s `text` property ([sec](#message-object--text-property)) contains this string:
>
> `"The variable \"{0}\" defined on line {1} is never used. Consider removing \"{0}\"."`
>
> There are two distinct placeholders, `{0}` and `{1}` (although `{0}` occurs twice). Therefore, the `arguments` array will have at least two elements, the first corresponding to `{0}` and the second corresponding to `{1}`.

> EXAMPLE 2: In this example, the SARIF consumer will replace the placeholder `{0}` in `message.text` with the value `"pBuffer"` from the 0 element of `message.arguments`.
>
> ```json
> {                                                   # A run object ((#run-object)).
>   "results": [                                      # See (#results-property).
>     {                                               # A result object ((#result-object)).
>       "ruleId": "CA2101",                           # See (#ruleid-property).
>       "message": {                                  # See (#result-object--message-property).
>         "text": "Variable '{0}' is uninitialized.", # See (#message-object--text-property).
>         "arguments": [ "pBuffer" ]                  # See (#message-object--arguments-property).
>       }
>     }
>   ]
> }
> ```

### Messages with embedded links

A message string **MAY** include one or more links to locations within artifacts mentioned in the enclosing `result` object ([sec](#result-object)). We refer to these links as "embedded links".

Within a formatted message ([sec](#formatted-messages)), an embedded link **SHALL** conform to the syntax of a GitHub Flavored Markdown link (see [cite](#GFM), §6.6, "Links").

> NOTE 1: The GFM link syntax is very flexible. Since a SARIF viewer that renders formatted messages will presumably rely on a full-featured GFM processor, there is no need to restrict the embedded link syntax in SARIF formatted messages.

Within a plain text message ([sec](#plain-text-messages)), an embedded link **SHALL** conform to the following syntax (which is a greatly restricted subset of the GFM link syntax) before JSON encoding:

```
    escaped link character = "\" | "[" | "]";

    normal link character = ? JSON string character ? – escaped link character;

    link character = normal link character | ("\", escaped link character);

    link text = { link character };

    link destination = ? Any valid URI ?;

    embedded link = "[", link text, "](", link destination, ")";
```

`link text` is the message text visible to the user.

Literal square brackets ("`[`" and "`]`") in the link text of a plain text message **SHALL** be escaped with a backslash (`"\"`).

> NOTE 2: When a SARIF log file is serialized as JSON, JSON encoding doubles the backslash.

> EXAMPLE 1: Consider this embedded link whose link text contains square brackets and backslashes:
>
>       "message": {
>         "text": "Prohibited term used in [para\\[0\\]\\\\spans\\[2\\]](1)."
>       }
>
> A SARIF viewer would render it as follows:
>
> Prohibited term used in para\[0\]\spans\[2\].

Literal square brackets and (doubled) backslashes **MAY** appear anywhere else in a plain text message without being escaped.

In both plain text and formatted messages, if `link destination` is a non-negative integer, it **SHALL** refer to a `location` object ([sec](#location-object)) whose `id` property ([sec](#location-object--id-property)) equals the value of `link destination`. In this case, `theResult` **SHALL** contain exactly one `location` object with that `id`.

> NOTE 3: Negative values are forbidden because their use would suggest some non-obvious semantic difference between positive and negative values.

> EXAMPLE 2: In this example, a plain text message contains an embedded link to a location with a file. The `result` object contains exactly one `location` object whose `id` property matches the `link destination`.
>
> ```json
> {                                  # A result object ((#result-object)).
>   "ruleId": "TNT0001",
>   "message": {
>     "text": "Tainted data was used. The data came from [here](3)."
>   },
>   "locations": [
>     {
>       "physicalLocation": {
>         "uri": "file:///C:/code/main.c",
>         "region": {
>           "startLine": 15,
>           "startColumn": 9
>         }
>       }
>     }
>   ],
>   "relatedLocations": [
>     {
>       "id": 3,
>       "physicalLocation": {
>         "uri": "file:///C:/code/input.c",
>         "region": {
>           "startLine": 25,
>           "startColumn": 19
>         }
>       }
>     }
>   ]
> }
> ```

The `link destination` in embedded links in both plain text messages and formatted messages **MAY** use the `sarif` URI scheme ([sec](#uris-that-use-the-sarif-scheme)). This allows a message to refer to any content elsewhere in the SARIF log file.

> EXAMPLE 1: A `result.message` ([sec](#result-object--message-property)) can refer to another result in the same run (or, for that matter, in another run within the same log file) as follows:
>
> `"There was [another result](sarif:/runs/0/results/42) found by this code flow."`
>
> A SARIF viewer executing in an IDE might respond to a click on such a link by selecting the target result in an error list window and navigating the editor to that result’s location.

Because the `"sarif"` URI scheme uses JSON pointer [cite](#RFC6901), which locates array elements by their array index, these URIs are potentially fragile if the SARIF log file is transformed by a post-processor.

> EXAMPLE 2: If a post-processor concatenates two runs into a single log file, the links within the run at index 1 will be incorrect, and will need to be updated from `"sarif:/runs/0/…"` to `"sarif:/runs/1/…"`.

> EXAMPLE 3: If a post-processor removes results from a run, any links that refer to results at indices following the removed results will need to be adjusted. For example, `sarif:/runs/0/results/54` might need to be adjusted to `sarif:/runs/0/results/42`.

When a tool displays on the console a result message containing an embedded link, it **MAY** reformat the link (for example, by removing the square brackets around the `link text`). If the `link destination` is an integer, and hence specifies a `location` object belonging to `theResult`, the tool **SHOULD** replace the integer with a string representation of the specified location.

> EXAMPLE 4: Suppose a tool chooses to display the result message from Example 3, which contains an integer-valued `link destination`, on the console. The output might be:  
>
> `Tainted data was used. The data came from here: C:\code\input.c(25, 19).`  
>
> Note that in addition to providing a string representation of the location, the tool removed the `[…](…)` link syntax and separated the link text from the location with a colon. Finally, the tool recognized that the location’s URI used the `file` scheme and chose to display it as a file system path rather than a URI.

### Message string lookup

A `message` object can directly contain message strings in its `text` ([sec](#message-object--text-property)) and `markdown` ([sec](#message-object--markdown-property)) properties. It can also indirectly refer to message strings through its `id` ([sec](#message-object--id-property)) property.

When a SARIF consumer needs to locate a message string from a `message` object, it **SHALL** follow the procedure specified in this section. The `run` object **SHALL** contain enough information for the procedure to succeed.

The lookup **SHALL** occur entirely within the context of a single `toolComponent` object ([sec](#toolcomponent-object)) which we refer to as `theComponent`. If the SARIF consumer is displaying messages in the language specified by `theRun.language` ([sec](#language)), then `theComponent` is the tool component that defines the message. If the consumer is displaying messages in any other language – in which case a translation ([sec](#translations)) is in use – then `theComponent` is the tool component that contains the translation.

In this procedure, we refer to the `message` object whose string is being looked up as `theMessage`.

At various points in this procedure, we state that the consumer uses an object’s "`text` property or `markdown` property, as appropriate." This means that if the consumer can render formatted messages, it **MAY** use the `markdown` property, if present; otherwise it **SHALL** use the `text` property, but if the consumer cannot render formatted messages, it **SHALL** use the `text` property.

The procedure is:

IF `theMessage.text` is present and the desired language is `theRun.language` THEN

&emsp;&emsp;Use the `text` or `markdown` property of `theMessage` as appropriate.

IF the string has not yet been found THEN

&emsp;&emsp;IF `theMessage` occurs as the value of `result.message` ([sec](#result-object--message-property)) THEN

&emsp;&emsp;&emsp;&emsp;LET `theRule` be the `reportingDescriptor` object ([sec](#reportingdescriptor-object)), an element of `theComponent.rules` ([sec](#rules-property)), which defines the rule that was violated by this result.

&emsp;&emsp;&emsp;&emsp;IF `theRule` exists AND `theRule.messageStrings` ([sec](#messagestrings-property)) is present AND contains a property whose name equals `theMessage.id` THEN

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;LET `theMFMS` be the `multiformatMessageString` object ([sec](#multiformatmessagestring-object)) that is the value of that property.

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;Use the `text` or `markdown` property of `theMFMS` as appropriate.

&emsp;&emsp;ELSE IF `theMessage` occurs as the value of `notification.message` ([sec](#notification-object--message-property)) THEN

&emsp;&emsp;&emsp;&emsp;LET `theDescriptor` be the `reportingDescriptor` object ([sec](#reportingdescriptor-object)), an element of `theComponent.notifications` ([sec](#rules-property)), which describes this notification.

&emsp;&emsp;&emsp;&emsp;IF `theDescriptor` exists AND `theDescriptor.messageStrings` is present AND contains a property whose name equals `theMessage.id` THEN

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;LET `theMFMS` be the `multiformatMessageString` object that is the value of that property.

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;Use the `text` or `markdown` property of `theMFMS` as appropriate.

IF the string has not yet been found THEN

&emsp;&emsp;IF `theComponent.globalMessageStrings` ([sec](#globalmessagestrings-property)) is present AND contains a property whose name equals `theMessage.id` THEN

&emsp;&emsp;&emsp;&emsp;LET `theMFMS` be the `multiformatMessageString` object that is the value of that property.

&emsp;&emsp;&emsp;&emsp;Use the `text` or `markdown` property of `theMFMS` as appropriate.

IF the string has not yet been found THEN

&emsp;&emsp;The lookup procedure fails (which means the SARIF log file is invalid).

### text property{#message-object--text-property}

A `message` object **MAY** contain a property named `text` whose value is a non-empty string containing a plain text message ([sec](#plain-text-messages)).

### markdown property{#message-object--markdown-property}

A `message` object **MAY** contain a property named `markdown` whose value is a non-empty string containing a formatted message ([sec](#formatted-messages)) expressed in GitHub-Flavored Markdown [cite](#GFM).

If the `markdown` property is present, the `text` property ([sec](#message-object--text-property)) **SHALL** also be present.

> NOTE: This ensures that the message is viewable even in contexts that do not support the rendering of formatted text.

SARIF consumers that cannot (or choose not to) render formatted text **SHALL** ignore the `markdown` property and use the `text` property instead.

### id property{#message-object--id-property}

A `message` object **MAY** contain a property named `id` whose value is a non-empty string containing the identifier for the desired message. See [sec](#message-string-lookup) for details of the message string lookup procedure.

### arguments property{#message-object--arguments-property}

If the message string specified by any of the properties `text` ([sec](#message-object--text-property)), `markdown` ([sec](#message-object--markdown-property)), or `id` ([sec](#message-object--id-property)) contains any placeholders ([sec](#messages-with-placeholders)), the `message` object **SHALL** contain a property named `arguments` whose value is an array of strings. [sec](#messages-with-placeholders) specifies how a SARIF consumer combines the contents of the `arguments` array with the message string to construct the message that it presents to the end user, and provides an example.

If none of the properties `text`, `markdown`, or `id` contains any placeholders, then `arguments` **MAY** be absent.

The `arguments` array **SHALL** contain as many elements as required by the maximum placeholder index among all the message strings specified by the `text`, `markdown`, and `id` properties.

> EXAMPLE 1: If the highest numbered placeholder in the `text` message string is `{3}` and the highest numbered placeholder in the `markdown` message string is `{5}`, the `arguments` array must contain at least 6 elements.
