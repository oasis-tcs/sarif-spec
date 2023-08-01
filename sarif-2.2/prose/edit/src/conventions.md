# Conventions

## General{#conventions--general}

The following conventions are used within this document.

## Format examples

This document contains several partial examples of the JSON serialization of the SARIF format. The examples are formatted for clarity, as permitted by JSON \[[RFC8259](#RFC8259)\], which allows "insignificant whitespace" before or after any token; implementations do not need to follow the whitespace convention used in these examples. The examples also employ typographical conventions that are not part of the JSON or SARIF formats:

- An ellipsis (…) is used to indicate that portions of the log file text required by this document have been omitted for brevity.

- A ‘`#`’ character introduces a comment that extends to the end of the line.

- When a JSON string is too long to fit on a line, it is broken into multiple lines.

- Some examples have italicized line numbers in the left margin.

## Property notation

A SARIF object consists of a set of properties. The value of a property can itself be an object, allowing arbitrary nesting. When necessary for clarity or to avoid ambiguity, we use the "dot" notation to refer to nested values. For example, the `physicalLocation` object defines a property `region` whose value is a `region` object, which in turn contains a `charLength` property. For clarity, we can refer to the `charLength` property as `physicalLocation.region.charLength`.

## Syntax notation

Where this document describes a syntactic construct, it uses the extended Backus-Naur form (EBNF) \[[ISO14977:1996](#ISO14977)\].

In all EBNF definitions in this spec:

- The following syntax rules are assumed:
  ```
  decimal digit = '0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9';

  non negative integer =

  "0"

  | decimal digit – '0', { decimal digit };
  ```

- The following "special sequence" (see EBNF \[[ISO14977:1996](#ISO14977)\], §4.19 and §5.11 and ) refers to any character that can appear in a JSON string according to JSON \[[ECMA404](#ECMA404)\]:

    ```
    ? JSON string character ?
    ```

## Commonly used objects

This document uses the following notation for certain commonly used objects:

| Notation        | Commonly used object                                                                                                                                                                                                                                                                                                                                                                                                                       |
|:----------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `theSarifLog`   | The root object of the SARIF log file.                                                                                                                                                                                                                                                                                                                                                                                                     |
| `theRun`        | The `run` object ([§3.14](#run-object)) containing the object under discussion.                                                                                                                                                                                                                                                                                                                                                            |
| `theTool`       | The value of `theRun.tool` ([§3.14.6](#run-object--tool-property))                                                                                                                                                                                                                                                                                                                                                                         |
| `theDescriptor` | The `reportingDescriptor` object ([§3.49](#reportingdescriptor-object)) identified by the `reportingDescriptorReference` object ([§3.52](#reportingdescriptorreference-object)) under discussion.                                                                                                                                                                                                                                          |
| `theComponent`  | The `toolComponent` object ([§3.19](#toolcomponent-object)) identified by the `toolComponentReference` object ([§3.54](#toolcomponentreference-object)) under discussion.                                                                                                                                                                                                                                                                  |
| `theResult`     | The `result` object ([§3.27](#result-object)) containing the object under discussion.                                                                                                                                                                                                                                                                                                                                                      |
| `thisObject`    | The object containing the property under discussion.<br>NOTE: Usually when the description of a property refers to another property of the same object, the other property is referred to by its unqualified name. When necessary to avoid confusion, the name of the other property is qualified with \"`thisObject.`\" to emphasize that it is a property of the object under discussion. For an example, see [§3.27.7](#rule-property). |
