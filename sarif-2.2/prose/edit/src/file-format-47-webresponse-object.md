## webResponse object

### General{#webresponse-object--general}

A `webResponse` object describes the response to an HTTP request \[[cite](#RFC7230)\]. The request itself is described by a `webRequest` object ([sec](#webrequest-object)).

> NOTE: This object is primarily useful to web analysis tools.

A `webResponse` object does not need to represent a valid HTTP response.

> NOTE 2: This allows an analysis tool to describe a situation where a server produces an invalid response.

### index property{#webresponse-object--index-property}

Depending on the circumstances, a `webResponse` object either **MAY, SHALL NOT**, or **SHALL** contain a property named `index` whose value is the array index ([sec](#array-indices)) within `theRun.webResponses` ([sec](#webresponses-property)) of a `webResponse` object that provides additional properties for `thisObject`. We refer to the object in `theRun.webResponses` as the "cached object."

If `thisObject` is an element of `theRun.webResponses`, then `index` **MAY** be present. If present, its value **SHALL** be the index of `thisObject` within `theRun.webResponses`.

Otherwise, if `theRun.webResponses` is absent, or if it does not contain a cached object for `thisObject`, then `index` **SHALL NOT** be present.

Otherwise (that is, if `thisObject` belongs to a result, and `theRun.webResponses` contains a cached object for `thisObject`), then `index` **SHALL** be present, and its value **SHALL** be the array index within `theRun.webResponses` of the cached object.

If `index` is present, `thisObject` **SHALL** take all properties present on the cached object. If `thisObject` contains any properties other than `index`, they **SHALL** equal the corresponding properties of the cached object.

> NOTE 1: This allows a SARIF producer to reduce the size of the log file by reusing the same `webResponse` object in multiple results.

> NOTE 2: For examples of the use of an `index` property to locate a cached object, see [sec](#threadflowlocation-object--index-property).

### protocol property{#webresponse-object--protocol-property}

A `webResponse` object **SHOULD** contain a property named `protocol` whose value is a string containing the name of the web protocol used in the response, found on the HTTP status line.

> EXAMPLE 1: `"protocol": "HTTP"`

### version property{#webresponse-object--version-property}

A `webResponse` object **SHOULD** contain a property named `version` whose value is a string containing the version of the web protocol used in the response, found on the HTTP status line.

> EXAMPLE 1: `"version": "1.1"`

### statusCode property

A `webResponse` object **SHOULD** contain a property named `statusCode` whose value is an integer containing the status code that describes the result of the request, found on the HTTP status line.

> EXAMPLE 1: `"statusCode": 200`

### reasonPhrase property

A `webResponse` object **SHOULD** contain a property named `reasonPhrase` whose value is a string containing the textual description of the `statusCode` ([sec](#statuscode-property)) found on the HTTP status line.

> EXAMPLE 1: `"reasonPhrase": "OK"`

If `noResponseReceived` ([sec](#noresponsereceived-property)) is `true`, then `reasonPhrase` **SHOULD** instead contain a string describing the reason that no response was received.

### headers property{#webresponse-object--headers-property}

A `webResponse` object **SHOULD** contain a property named `headers` whose value is an object ([sec](#object-properties)) whose property names are the names of the HTTP headers in the response (for example, `"Content-Type"`) and whose corresponding values are the header values (for example, `"text/plain; charset=ascii"`).

### body property{#webresponse-object--body-property}

A `webResponse` object **MAY** contain a property named `body` whose value is an `artifactContent` object ([sec](#artifactcontent-object)) containing the body of the response.

If the response body is entirely textual, `body.text` ([sec](#artifactcontent-object--text-property)) **SHOULD** be present. If present, it **SHALL** contain the response body, transcoded to UTF-8 if necessary.

> NOTE 1: The transcoding is required because all textual content in a SARIF log file is represented in UTF-8 (see [sec](#file-format--general)).

> NOTE 2: If necessary, the character encoding actually used in the response can be deduced from the value of the `Content-Type` header (see [sec](#webresponse-object--headers-property)), for example, `"text/plain; charset=ascii"`.

If the response body is entirely textual, `body.binary` ([sec](#binary-property)) **MAY** be present. If present, it **SHALL** contain the MIME Base64 encoding \[[cite](#RFC2045)\] of the body as it was actually transmitted.

If the response body consists partially or entirely of binary data, `body.binary` **SHALL** be present and **SHALL** contain the MIME Base64 encoding of the body. In this situation, `body.text` **SHALL** be absent.

### noResponseReceived property

If no response to the HTTP request was received (for example, because of a network failure), the `webResponse` object **SHALL** contain a property named `noResponseReceived` whose value is a Boolean `true`. If a response was received, `noResponseReceived` **SHALL** either be present with the value `false`, or absent, in which case it defaults to `false`.

If `noResponseReceived` is `true`, then `reasonPhrase` ([sec](#reasonphrase-property)), which normally contains the reason phrase from the HTTP response line, **SHOULD** instead contain a string describing the reason that no response was received.
