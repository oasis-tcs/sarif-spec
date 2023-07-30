## URI-valued properties

### General{#uri-valued-properties--general}

Certain properties in this document specify either an absolute URI or a URI reference (the term used in the URI standard \[[RFC3986](#RFC3986)\] to describe either an absolute URI or a relative reference). The value of every such property, if present, **SHALL** be a string in the format specified by the standard \[[RFC3986](#RFC3986)\].

If a URI reference refers to a file stored in a version control system (VCS), its value **SHALL** include sufficient information (for example, a commit id) to enable the correct version of the target file to be retrieved from the VCS. If a URI reference refers to a file stored on a physical file system, it **MAY** be specified as a relative reference that omits root information details (such as hard drive letter and an arbitrarily named root directory associated with a source code enlistment).

> NOTE 1: A URI reference (even a relative reference) might contain information that represents unwanted information disclosure, particularly in cases where a tool is analyzing files stored on a physical file system. For example, a file path might contain the account name of a developer.

The URI **SHALL** specify the location of the artifact at the time the analysis was performed.

Two URI references **SHALL** be considered equivalent if their normalized forms are the same, as described in the standard \[[RFC3986](#RFC3986)\].

> NOTE 2: Features of this normalized form include using upper-case hexadecimal digits for percent-encoded characters and expressing the scheme component in lower-case. For the full specification of the normalized URI form, see the standard \[[RFC3986](#RFC3986)\].

For additional normalization requirements for URIs that use the `"file"` scheme, see [§3.10.2](#normalizing-file-scheme-uris).

When two URI references are not equivalent in this sense (that is, when their normalized forms are not the same), we will say that they are "distinct."

Aside from normalization, SARIF producers **SHALL NOT** make any other changes to the text of a URI reference; for example, they **SHALL NOT** convert the path to upper case or to lower case.

> NOTE 3: This is especially important when the same SARIF file might be consumed on multiple platforms, for example, a platform such as Microsoft Windows®, whose NTFS file system is case-insensitive but case-preserving, and a platform such as Linux®, whose file system is case-sensitive. Consider a scenario where a tool runs on a Windows® system using NTFS, and the tool decides to lower-case the file names in the log. If the source files and the SARIF log were transferred to a Linux® system, the URI references in the log file would not match the path names on the destination system.

### Normalizing file scheme URIs

If a URI uses the `"file"` scheme \[[RFC8089](#RFC8089)\] and the specified path is network-accessible, the SARIF producer **SHALL** include the host name.

> EXAMPLE 1: A file-based URI that references a network share.
> 
>       file://build.example.com/drops/Build-2018-04-19.01/src

If a URI uses the `"file"` scheme and the specified path is *not* network-accessible, the SARIF producer **SHOULD NOT** include the host name.

> EXAMPLE 2: A file-based URI that references the local file system.
> 
>       file:///C:/src

A SARIF producer **MAY** choose to omit the hostname (authority) from a file URI, for example, for security reasons. If it does so, then to maximize interoperability with previous versions of the URI specification, the URI **SHOULD** start with `"file:///"`, as in EXAMPLE 2. See the standard \[[RFC8089](#RFC8089)\] for more information on this point.

SARIF producers **SHALL** create `"file"` scheme URIs by means of the following procedure or any procedure with the same result:

1.  In the case of a direct producer, preserve the file system’s casing, even if the file system is case-insensitive. In the case of a converter (which might not know the file system’s casing), preserve the casing specified in the analysis tool’s native output file.

2.  Remove `"."` path segments.

3.  Remove empty path segments.

4.  If the path contains `".."` path segments, then in the case of a direct producer, resolve the path to a canonical absolute path, using an appropriate algorithm for the operating system on which the tool ran.

    NOTE 1: This is necessary because, for example, the path `/d1/../f` naively converted to a URI is `file:///d1/../f`, which resolves to `file:///f` according to the URI standard \[[RFC3986](#RFC3986)\]. But if `/d1` is a symbolic link to the directory `d2/d3`, then the correct URI is `file:///d2/f`.

    NOTE 2: ".." path segments are dangerous because the semantics of the file system on which the SARIF log file was produced might not match the semantics of the file system on which it is consumed. For example, the presence of a symbolic link in the path might redirect the consumer to an unpredictable location.

5.  Create a URI from the resulting path.

6.  Optionally, divide the resulting URI into a base URI and a relative URI (preserving case in both parts), and create an entry for the base URI in `theRun.originalUriBaseIds` ([§3.14.14](#originaluribaseids-property)).

> NOTE 3: URI and path manipulation are complex topics. Many operating systems, languages, and frameworks provide methods to perform these operations, which is preferable to having every SARIF producer reimplement them. For example, in C#, the operation can be performed as follows:
> 
> ```cs
> using System;
> 
> using System.IO;
> 
> ...
> 
> string path = ...;
> 
> string fullPath = Path.GetFullPath(path);
> 
> var uri = new Uri(fullPath, UriKind.Absolute);
> 
> string uriString = uri.AbsoluteUri;
> ```

SARIF consumers SHALL NOT normalize ".." segments out of a path. A consumer SHOULD reject paths that contain ".." segments, otherwise a consumer SHALL treat distinct portions of paths up to and including the rightmost ".." segment as unique directories on the file system, even if \[[RFC3986](#RFC3986)\] normalization would produce identical paths.

> EXAMPLE 3: Consider the following three URIs:
> 
> - `file:///d1/../f1`
> 
> - `file:///d1/../f2`
> 
> - `file:///d1/d2/../../f3`

A consumer would treat `f1` and `f2` as residing in the same directory. So, for example, if a viewer prompted the user to supply the directory where `f1` resides, it could search for `f2` in the same directory, without prompting again. On the other hand, even though `f3` appears to reside in the same directory as `f1` and `f2`, the viewer would not assume that, and would prompt the user to supply the directory where `f3` resides.

### URIs that use the sarif scheme

In certain circumstances, a URI can refer to an element of the current SARIF log file (for example, see [§3.16.3](#externalpropertyfilereference-object--location-property)). Such a URI uses the `sarif` scheme. The `sarif` URI scheme consists of only a scheme (with the value `sarif`) and a path component. The path component is interpreted as a JSON pointer \[[RFC6901](#RFC6901)\] into the SARIF document containing the URI. The authority, query and fragment URI components **SHALL NOT** be present.

> EXAMPLE: The URI `"sarif:/inlineExternalProperties/0"` refers to the 0<sup>th</sup> element of the array contained in the `inlineExternalProperties` property ([§3.13.5](#inlineexternalproperties-property)) at the root of the log file.

### Internationalized Resource Identifiers (IRIs)

If a URI-valued property refers to a resource identified by an Internationalized Resource Identifier (IRI) \[[RFC3987](#RFC3987)\], the SARIF producer **SHALL** first transform the IRI into a URI, using the mapping mechanism specified in [§3.1](#file-format--general) of the standard \[[RFC3987](#RFC3987)\], and then assign the transformed value to the property. The string value of a URI-valued property **SHALL NOT** include Unicode characters such as `"é"`; such characters are permitted in IRIs but are not permitted in URIs. [§3.1](#file-format--general) of the standard \[[RFC3987](#RFC3987)\] describes how to replace such characters with "percent-encoded" equivalents to produce a valid URI.

> EXAMPLE: Suppose a URI-valued property needs to refer to a resource identified by the string `"http://www.example.com/hu/sör.txt"`. This string contains the character `"ö"`, so it is a valid IRI but not a valid URI. Following the procedure in [§3.1](#file-format--general) of the standard \[[RFC3987](#RFC3987)\], a SARIF producer would transform this string to the valid URI `"http://www.example.com/hu/s%C3%B6r.txt"` before assigning it to the property.
