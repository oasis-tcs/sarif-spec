## `address` Object

### General{#address-object--general}

An `address` object describes a physical or virtual address, or a range of addresses, in an "addressable region" (memory or a binary file).

### Parent-child Relationships

`address` objects can be linked by their `parentIndex` properties ([sec](#address-object--parentindex-property)) to form a chain in which each address is specified as an offset from a "parent" object which we refer to as `theParent`.

> EXAMPLE 1: In this example, the location of the Sections region of a Windows ® Portable Executable file [cite](#PE) is expressed as an offset from the start of the module. The location of the .text section is in turn expressed as an offset from Sections.
>
> ```json
> {                                  # A run object ((#run-object)).
>   "addresses": [                   # See (#addresses-property).
>     {
>       "name": "Multitool.exe",     # See (#address-object--name-property).
>       "kind": "module",            # See (#address-object--kind-property).
>       "absoluteAddress": 1024      # See (#absoluteaddress-property).
>     },
>     {
>       "name": "Sections",
>       "kind": "header",
>       "parentIndex": 0,            # See (#address-object--parentindex-property).
>       "offsetFromParent": 376,     # See (#offsetfromparent-property).
>       "absoluteAddress": 1400,
>       "relativeAddress": 376       # See (#relativeaddress-property).
>     },
>     {
>       "name": ".text",
>       "kind": "section",
>       "parentIndex": 1,
>       "offsetFromParent": 136,
>       "absoluteAddress": 1536,
>       "relativeAddress": 512
>     }
>   ],
>   ...
> }
> ```

### Absolute Address Calculation

Each `address` object has an associated value called its "absolute address" which is the offset of the address from the start of the addressable region. The absolute address is calculated by executing the function `CalculateAbsoluteAddress` defined below on `thisObject` or by any procedure with the same result.

This procedure assumes that the `offsetFromParent` ([sec](#offsetfromparent-property)) and `parentIndex` ([sec](#address-object--parentindex-property)) properties are either both present or both absent; if this is not the case, the SARIF file is invalid.

FUNCTION `CalculateAbsoluteAddress`(`addr`)

&emsp;&emsp;IF `addr.absoluteAddress` exists THEN

&emsp;&emsp;&emsp;&emsp;RETURN `addr.absoluteAddress`

&emsp;&emsp;ELSE IF `addr.parentIndex` exists THEN

&emsp;&emsp;&emsp;&emsp;LET `theParent` = the parent object (see [sec](#parent-child-relationships)) of `addr`

&emsp;&emsp;&emsp;&emsp;RETURN `addr.offsetFromParent` + `CalculateAbsoluteAddress`(`theParent`)

&emsp;&emsp;ELSE

&emsp;&emsp;&emsp;&emsp;ERROR "Absolute address cannot be determined".

If `CalculateAbsoluteAddress`(`thisObject`) or any of its recursive invocations encounters an ERROR, the absolute address cannot be determined.

If both `absoluteAddress` and `offsetFromParent` exist, then `absoluteAddress` **SHALL** equal the value that `CalculateAbsoluteAddress` would have returned if `absoluteAddress` were absent, if `CalculateAbsoluteAddress` would have returned successfully in that circumstance.

### Relative Address Calculation

Each `address` object has an associated value called its "relative address" which is the offset of the address from the address of the top-most object in its parent chain. The relative address is calculated by executing the function `CalculateRelativeAddress` defined below on `thisObject` or by any procedure with the same result.

This procedure assumes that the `offsetFromParent` ([sec](#offsetfromparent-property)) and `parentIndex` ([sec](#address-object--parentindex-property)) properties are either both present or both absent; if this is not the case, the SARIF file is invalid.

FUNCTION `CalculateRelativeAddress`(`addr`)

&emsp;&emsp;IF `addr.relativeAddress` exists THEN

&emsp;&emsp;&emsp;&emsp;RETURN `addr.relativeAddress`

&emsp;&emsp;ELSE IF `addr.parentIndex` exists THEN

&emsp;&emsp;&emsp;&emsp;LET `theParent` = the parent object (see [sec](#parent-child-relationships)) of `addr`

&emsp;&emsp;&emsp;&emsp;RETURN `addr.offsetFromParent` + `CalculateRelativeAddress`(`theParent`)

&emsp;&emsp;ELSE

&emsp;&emsp;&emsp;&emsp;RETURN 0

If `CalculateRelativeAddress`(`thisObject`) or any of its recursive invocations encounters an ERROR, the relative address cannot be determined.

If both `relativeAddress` and `offsetFromParent` exist, then `relativeAddress` **SHALL** equal the value that `CalculateRelativeAddress` would have returned if `relativeAddress` were absent, if `CalculateRelativeAddress` would have returned successfully in that circumstance.

### `index` Property{#address-object--index-property}

Depending on the circumstances, an `address` object either **MAY, SHALL NOT**, or **SHALL** contain a property named `index` whose value is the array index ([sec](#array-indices)) within `theRun.addresses` ([sec](#addresses-property)) of an `address` object that provides the properties for `thisObject`. We refer to the object in `theRun.addresses` as the "cached object."

If `thisObject` is an element of `theRun.addresses`, then `index` **MAY** be present. If present, its value **SHALL** be the index of `thisObject` within `theRun.addresses`.

Otherwise, if `theRun.addresses` is absent, or if it does not contain a cached object for `thisObject`, then `index` **SHALL NOT** be present.

Otherwise (that is, if `thisObject` belongs to a result, and `theRun.addresses` contains a cached object for `thisObject`), then `index` **SHALL** be present, and its value **SHALL** be the array index within `theRun.addresses` of the cached object.

If `index` is present, `thisObject` **SHALL** take all properties present on the cached object. If `thisObject` contains any properties other than `index`, they **SHALL** equal the corresponding properties of the cached object.

> NOTE 1: This allows a SARIF producer to reduce the size of the log file by reusing the same `address` object in multiple results.

> NOTE 2: For examples of the use of an `index` property to locate a cached object, see [sec](#threadflowlocation-object--index-property).

### `absoluteAddress` Property

An `address` object **MAY** contain a property named `absoluteAddress` whose value is a non-negative integer containing the absolute address (see [sec](#absolute-address-calculation)) of `thisObject`.

If `absoluteAddress` is absent, it **SHALL** default to -1, which indicates that the value is unknown (not set).

### `relativeAddress` Property

If `parentIndex` ([sec](#address-object--parentindex-property)) is present, an `address` object **MAY** contain a property named `relativeAddress` whose value, if present, is an integer containing the relative address (see [sec](#relative-address-calculation)) of `thisObject`.

If `parentIndex` is absent, `relativeAddress` **SHALL** be absent.

If `relativeAddress` is absent, it **SHALL** default to `null`, which indicates that the value is unknown (not set).

### `offsetFromParent` Property

If `parentIndex` ([sec](#address-object--parentindex-property)) is present, an `address` object **MAY** contain a property named `offsetFromParent` whose value, if present, is an integer containing the offset of this address from the absolute address of `theParent` (see [sec](#parent-child-relationships)). This is the case even if the absolute address of the parent cannot be determined by the procedure in [sec](#absolute-address-calculation).

> NOTE 1: The rationale is that the absolute address always exists, even if the log file does not contain enough information to determine it, so it is always sensible to talk about an offset from that address.

If `parentIndex` is absent, `offsetFromParent` **SHALL** be absent.

If `offsetFromParent` is absent, it **SHALL** default to `null`, which indicates that the value is unknown (not set).

### `length` Property{#address-object--length-property}

An `address` object **MAY** contain a property named `length` whose value, if present, is an integer whose absolute value specifies the number of bytes in the range of addresses specified by this object.

A negative value for `length` **SHALL** mean that the data structure being described grows from higher addresses towards lower addresses (as, for example, is often the case for a stack).

If `length` is absent, it **SHALL** default to `null`, which indicates that the value is unknown (not set).

### `name` Property{#address-object--name-property}

An `address` object **MAY** contain a property named `name` whose value is a string containing the name of this address.

### `fullyQualifiedName` Property{#address-object--fullyqualifiedname-property}

An `address` object **MAY** contain a property named `fullyQualifiedName` whose value is a string containing the fully qualified name of this address.

> EXAMPLE 1: `"fullyQualifiedName": "MyDll.dll+0x47"`
>
> This name consists of two components. The first component is the name of the address at which the module was loaded into memory. The second component represents an offset from that address.

### `kind` Property{#address-object--kind-property}

An `address` object **MAY** contain a property named `kind` whose value is a string that specifies the kind of addressable region in which this address is located.

When possible, SARIF producers **SHOULD** use the following values, with the specified meanings.

- `"data"`: An addressable location containing non-executable data.

- `"header"`: A data structure that precedes one or more addressable regions and specifies the layout and location of objects within the address space.

- `"function"`: An addressable region, possibly named, containing a sequence of instructions that perform a specified task.

- `"instruction"`: An addressable location containing executable code.

- `"page"`: An addressable region whose contents can be moved between primary and secondary storage.

- `"section"`: A named region of a file containing executable code or data, which in some circumstances is loaded into memory.

- `"segment"`: 1. A data structure in a binary that describes a region of memory, specifying its addressing and permissions information, as well as information about which sections are to be loaded into the segment. 2. A region of memory whose contents are specified by the information in a segment defined in a binary, or by the operating system.

- `"stack"`: An addressable region containing a call stack.

- `"stackFrame"`: An addressable region containing a single frame from within a call stack.

- `"module"`: The location at which a module was loaded.

- `"table"`: An addressable region with a distinct purpose and a specified internal organization

The definitions of some of these `"kind"` values vary across operating systems. A SARIF producer **SHOULD** use the term most appropriate for the target operating system.

Although a function does contain executable code, the value `"function"` **SHOULD** be used for the address of the start of a function, because it is more specific. The value `"instruction"` **SHOULD** be used for an address within the body of a function.

&emsp;&emsp;If none of these values are appropriate, a SARIF producer **MAY** use any value.

### `parentIndex` Property{#address-object--parentindex-property}

If `theParent` exists (that is, if `thisObject` is expressed as an offset from some other address), then an `address` object **SHALL** contain a property named `parentIndex` whose value is the array index ([sec](#array-indices)) of `theParent` within `theRun.addresses` ([sec](#addresses-property)).

If `theParent` does not exist, then `parentIndex` **SHALL** be absent.
