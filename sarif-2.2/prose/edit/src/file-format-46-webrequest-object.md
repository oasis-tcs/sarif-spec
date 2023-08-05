## webRequest object

### General{#webrequest-object--general}

A `webRequest` object describes an HTTP request \[[cite](#RFC7230)\]. The response to the request is described by a `webResponse` object ([sec](#webresponse-object)).

> NOTE 1: This object is primarily useful to web analysis tools.

A `webRequest` object does not need to represent a valid HTTP request.

> NOTE 2: This allows an analysis tool that intentionally sends invalid HTTP requests to use the `webRequest` object.

### index property{#webrequest-object--index-property}

Depending on the circumstances, a `webRequest` object either **MAY, SHALL NOT**, or **SHALL** contain a property named `index` whose value is the array index ([sec](#array-indices)) within `theRun.webRequests` ([sec](#webrequests-property)) of a `webRequest` object that provides the properties for `thisObject`. We refer to the object in `theRun.webRequests` as the "cached object."

If `thisObject` is an element of `theRun.webRequests`, then `index` **MAY** be present. If present, its value **SHALL** be the index of `thisObject` within `theRun.webRequests`.

Otherwise, if `theRun.webRequests` is absent, or if it does not contain a cached object for `thisObject`, then `index` **SHALL NOT** be present.

Otherwise (that is, if `thisObject` belongs to a result, and `theRun.webRequests` contains a cached object for `thisObject`), then `index` **SHALL** be present, and its value **SHALL** be the array index within `theRun.webRequests` of the cached object.

If `index` is present, `thisObject` **SHALL** take all properties present on the cached object. If `thisObject` contains any properties other than `index`, they **SHALL** equal the corresponding properties of the cached object.

> NOTE 1: This allows a SARIF producer to reduce the size of the log file by reusing the same `webRequest` object in multiple results.

> NOTE 2: For examples of the use of an `index` property to locate a cached object, see [sec](#threadflowlocation-object--index-property).

### protocol property{#webrequest-object--protocol-property}

A `webRequest` object **SHOULD** contain a property named `protocol` whose value is a string containing the name of the web protocol used in the request, found on the HTTP request line.

> EXAMPLE 1: `"protocol": "HTTP"`

### version property{#webrequest-object--version-property}

A `webRequest` object **SHOULD** contain a property named `version` whose value is a string containing the version of the web protocol used in the request, found on the HTTP request line.

> EXAMPLE 1: `"version": "1.1"`

### target property{#webrequest-object--target-property}

A `webRequest` object **SHOULD** contain a property named `target` whose value is a string containing the target of the request, found on the HTTP request line, in the form defined by [§5.3](#conformance-clause-2-sarif-producer) ("Request Target") of the HTTP standard \[[cite](#RFC7230)\].

### method property

A `webRequest` object **SHOULD** contain a property named `method` whose value is a string containing the HTTP method used in the request, found on the HTTP request line. The string **SHOULD** be one of the values `"GET"`, `"PUT"`, `"POST"`, `"DELETE"`, `"PATCH"`, `"HEAD"`, `"OPTIONS"`, `"TRACE"`, or `"CONNECT"`.

### headers property{#webrequest-object--headers-property}

A `webRequest` object **SHOULD** contain a property named `headers` whose value is an object ([sec](#object-properties)) whose property names are the names of the HTTP headers in the request (for example, `"Content-Type"`) and whose corresponding values are the header values (for example, `"text/plain; charset=ascii"`).

### parameters property{#webrequest-object--parameters-property}

A `webRequest` object **MAY** contain a property named `parameters` whose value is an object ([sec](#object-properties)) whose property names are the names of the parameters in the request and whose corresponding values are the values of those parameters.

> NOTE: The `parameters` property exists as a convenience for the log file consumer. If it is absent, the consumer can parse the parameters from `body` ([sec](#webrequest-object--body-property)), in the case of a forms post, or from the query portion of `uri` ([sec](#webrequest-object--target-property)).

### body property{#webrequest-object--body-property}

A `webRequest` object **MAY** contain a property named `body` whose value is an `artifactContent` object ([sec](#artifactcontent-object)) containing the body of the request.

If the request body is entirely textual, `body.text` ([sec](#artifactcontent-object--text-property)) **SHOULD** be present. If present, it **SHALL** contain the request body, transcoded to UTF-8 if necessary.

> NOTE 1: The transcoding is required because all textual content in a SARIF log file is represented in UTF-8 (see [sec](#file-format--general)).

> NOTE 2: If necessary, the character encoding actually used in the request can be deduced from the value of the `Content-Type` header (see [sec](#webrequest-object--headers-property)), for example, `"text/plain; charset=ascii"`.

If the request body is entirely textual, `body.binary` ([sec](#binary-property)) **MAY** be present. If present, it **SHALL** contain the MIME Base64 encoding \[[cite](#RFC2045)\] of the body as it was actually transmitted.

If the request body consists partially or entirely of binary data, `body.binary` **SHALL** be present and **SHALL** contain the MIME Base64 encoding of the body. In this situation, `body.text` **SHALL** be absent.
