## specialLocations object

### General{#speciallocations-object--general}

A `specialLocations` object defines locations of special significance to SARIF consumers.

> NOTE: This version of SARIF defines only one such location, `displayBase` ([sec](#displaybase-property)). In the future, other specially treated locations might be defined.

### displayBase property

A `specialLocations` object **MAY** contain a property named `displayBase` whose value is an `artifactLocation` object ([sec](#artifactlocation-object)) which provides a suggestion to consumers to display file paths relative to the specified location.

A consumer **MAY** act on this hint as follows:

1.  Resolve `displayBase` to a URI (the "base URI") by the procedure defined in [sec](#originaluribaseids-property) or any procedure with the same result. If the result is not an absolute URI, the procedure fails.

2.  Normalize the base URI and the displayed URI by the procedures defined in [sec](#uri-valued-properties--general) and [sec](#normalizing-file-scheme-uris) or any procedures with the same result.

3.  If the base URI and the displayed URI have the identical scheme, authority, and initial path segments, then display only the remaining path segments of the displayed URI, or "." if there are no remaining path segments.

4.  Otherwise, render the displayed URI as an absolute URI (or in some other appropriate form, such as a (`uriBaseId`, `uri`) pair.

> EXAMPLE 1: Given the following:
> 
> ```json
> {                           # A run object (§3.14).
>   "originalUriBaseIds": {   # See §3.14.14.
>     "WEBHOST": {
>       "uri": "http://www.example.com/"
>     },
>     "ROOT": {
>       "uri": "file:///"
>     },
>     "HOME": {
>      "uri": "/home/user/",
>      "uriBaseId": "ROOT"
>     },
>     "PACKAGE": {
>       "uri": "mySoftware/",
>       "uriBaseId": "HOME"
>     },
>     "SRC": {
>       "uri": "src/",
>       "uriBaseId": "PACKAGE"
>     }
>   },
> 
>   "specialLocations": {
>     "displayBase": {        # An artifactLocation object (§3.4).
>       "uri": "",            # Empty string is valid relative reference.
>       "uriBaseId": "PACKAGE"
>     }
>   }
> }
> ```
> 
> These equivalent locations would display as `src/f.c` because the scheme, authority, and initial path segments match:
> 
> ```json
> {
>   "uri": "f.c",
>   "uriBaseId": "SRC"
> }
> 
> {
>   "uri": "src/f.c",
>   "uriBaseId": "PACKAGE"
> }
> 
> {
>   "uri": "file:///home/user/mySoftware/src/f.c"
> }
> ```
> 
> These equivalent locations would display as `/usr/include/stdio.h` because the scheme and authority match, but not the path:
> 
> ```json
> {
>   "uri": "/usr/include/stdio.h",
>   "uriBaseId": "ROOT"
> }
> 
> {
>   "uri": "file:///usr/include/stdio.h"
> }
> ```
> 
> These equivalent locations would display as `http://www.example.com/hello` because the scheme and authority do not match:
> 
> ```
> {
>   "uri": "hello",
>   "uriBaseId": "WEBHOST"
> }
> 
> {
>   "uri": "http://www.example.com/hello"
> }
> ```
> 
> If `displayBase` were changed to
> 
> ```json
> "displayBase": {
>   "uri": "",
>   "uriBaseId": "HOME"
> }
> ```
> 
> the URIs displayed as `src/f.c` would instead be displayed as `mySoftware/src/f.c`. All other display values would be unchanged.
