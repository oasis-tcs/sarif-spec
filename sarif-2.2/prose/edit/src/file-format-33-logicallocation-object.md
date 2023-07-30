## logicalLocation object

### General{#logicallocation-object--general}

A `logicalLocation` object describes a logical location. A logical location is a location specified by a programmatic construct such as a namespace, a type, or a method, without regard to the physical location where the construct occurs.

`logicalLocation` objects occur in two places: as array elements of `run.logicalLocations` ([§3.14.17](#run-object--logicallocations-property)) and as array elements of `location.logicalLocations` ([§3.28.4](#location-object--logicallocations-property)).

### Logical location naming rules

Every logical location has a "fully qualified logical name" (more briefly, a "fully qualified name") that fully specifies the programmatic construct to which it refers. When programmatic constructs are nested (such as a method within a class within a namespace), the fully qualified name is typically a hierarchical identifier such as `"N.C.F(void)"` or `"N::C::F(void)"`. We refer to the rightmost component of this hierarchical identifier as the "logical name" (more briefly, the "name") of the logical location.

Whenever possible, logical names and fully qualified logical names **SHOULD** conform to the syntax of the programming language in which the programmatic construct specified by the logical location was expressed.

> EXAMPLE 1: The fully qualified logical name of the C++ method `f(void)` in class `C` in namespace `N` is `"N::C::f(void)"`. Its logical name is `"f(void)"`.

This is not always possible, for two reasons:

- For certain values of `logicalLocation.kind` ([§3.33.7](#logicallocation-object--kind-property)), there is no language syntax to specify the fully qualified name.

> EXAMPLE 2: Suppose the logical location is the local variable `pBuffer` in the C++ method `"N::C::f(void)"`. `logicalLocation.kind` is `"variable"`. There is no way to express the fully qualified name in C++. The SARIF producer might choose a fully qualified name such as `"N::C::f(void)?pBuffer"`.

- For other values of `logicalLocation.kind`, it is sometimes but not always possible to express the logical location in language syntax.

> EXAMPLE 3: Suppose the logical location is the anonymous callback function in this JavaScript™ function:
> 
> ```js
> function click_it() {
>   $("button").click(function(){
>       alert("Clicked");
>   });
> }
> ```
> 
> `logicalLocation.kind` is `"function"`, for which it is sometimes possible to specify a fully qualified name. But there is no language syntax to express the name of an anonymous callback. The SARIF producer might choose a fully qualified name such as `"click_it?anon-1"`.

### index property{#logicallocation-object--index-property}

Depending on the circumstances, a `logicalLocation` object either **MAY, SHALL NOT**, or **SHALL** contain a property named `index` whose value is the array index ([§3.7.4](#array-indices)) within `theRun.logicalLocations` ([§3.14.17](#run-object--logicallocations-property)) of a `logicalLocation` object that provides the properties for `thisObject`. We refer to the object in `theRun.logicalLocations` as the "cached object."

If `thisObject` is an element of `theRun.logicalLocations`, then `index` **MAY** be present. If present, its value **SHALL** be the index of `thisObject` within `theRun.logicalLocations`.

Otherwise, if `theRun.logicalLocations` is absent, or if it does not contain a cached object for `thisObject`, then `index` **SHALL NOT** be present.

Otherwise (that is, if `thisObject` belongs to a result, and `theRun.logicalLocations` contains a cached object for `thisObject`), then `index` **SHALL** be present, and its value **SHALL** be the array index within `theRun.logicalLocations` of the cached object.

If `index` is present, `thisObject` **SHALL** take all properties present on the cached object. If `thisObject` contains any properties other than `index`, they **SHALL** equal the corresponding properties of the cached object.

> NOTE 1: This allows a SARIF producer to reduce the size of the log file by reusing the same `logicalLocation` object in multiple results.

> NOTE 2: For examples of the use of an `index` property to locate a cached object, see [§3.38.2](#threadflowlocation-object--index-property).

### name property{#logicallocation-object--name-property}

A `logicalLocation` object **SHOULD** contain a property named `name` whose value is the logical name of the programmatic construct specified by this object. For example, this property might contain the name of a class or a method.

The `name` property **SHALL** be suitable for display and **SHALL** follow the naming rules for logical names described in [§3.33.2](#logical-location-naming-rules).

> NOTE: A C++ analysis tool might have available both the source code form of a function name and the compiler’s "decorated" function name (which encodes the function signature in a manner that is compiler-dependent and not easily readable). The tool would place the source code form of the function name in the `name` property, and the decorated name in the `decoratedName` property ([§3.33.6](#decoratedname-property)).

> EXAMPLE: In this C++ example, the fully qualified name is `"b::c(float)"`, so `"name"` is the rightmost component, `"c(float)"`.
> 
> ```json
> {                                      # A logicalLocation object.
>   "name": "c(float)",
>   "fullyQualifiedName": "b::c(float)", # See §3.33.5.
>   "kind": "function"                   # See §3.33.7
> }
> ```

### fullyQualifiedName property{#logicallocation-object--fullyqualifiedname-property}

Depending on the circumstances, a `logicalLocation` object either **SHOULD** or **MAY** contain a property named `fullyQualifiedName` whose value is the fully qualified name of the logical location. This name **SHALL** follow the naming rules for fully qualified names described in [§3.33.2](#logical-location-naming-rules).

If this `logicalLocation` object represents a top-level logical location, then `fullyQualifiedName` **MAY** be present. If present, it **SHALL** equal `name`; if absent, it **SHALL** default to `name`. If this object does not represent a top-level logical location, `fullyQualifiedName` **SHOULD** be present.

It is possible for two or more distinct logical locations to have the same fully qualified name.

> NOTE: This is an extremely rare corner case.

> EXAMPLE: Suppose a tool analyzes two C++ source files:
> 
> ```cpp
> // file1.cpp
> namespace A {
>     class B {
>     }
> }
> 
> // file2.cpp
> namespace A {
>     namespace B {
>         class C {
>         }
>     }
> } 
> ```
> 
> These could not coexist in the same compilation, but there is no reason two such source files could not exist.
> 
> If the tool detected one result in `class B` in *file1.cpp*, and another result in `namespace B` in *file2.cpp*, the `fullyQualifiedName` for both would be `A::B`. However, they would be distinguished by their `parentIndex` properties:
> 
> ```json
> "logicalLocations": [
>   {
>     "name": "B",
>     "fullyQualifiedName": "A::B", 
>     "kind": "namespace",
>     "parentIndex": 1
>   },
>   {
>     "name": "A",
>     "kind": "namespace"
>   },
>   {
>     "name": "B",
>     "fullyQualifiedName": "A::B",
>     "kind": "type",
>     "parentIndex": 3
>   },
>   {
>     "name": "A",
>     "kind": "namespace"
>   }
> ]
> ```

> NOTE: There are a few reasons the `fullyQualifiedName` property exists, even though the information it contains can be reconstructed from the `name` properties of this object and its parent objects in `run.logicalLocations`:
> 
> - `run.logicalLocations` might not be present.
> 
> - It allows a SARIF viewer to display the logical location in a way that is easily understood by users.
> 
> - As mentioned in [§3.28.1](#location-object--general), `fullyQualifiedName` is also particularly convenient for fingerprinting, although the more detailed information in `run.logicalLocations` could be used instead.
> 
> - It relieves viewers from having to format the logical location from the more detailed information in `run.logicalLocations`.
> 
> - It is useful for producing readable in-source suppressions (for example, "suppress all instance of rule `CA2101` in the class `NamespaceA.NamespaceB.ClassC`").

### decoratedName property

A `logicalLocation` object **MAY** contain a property named `decoratedName` whose value is a string containing the compiler's internal representation of the logical location associated with this `location` object.

> NOTE: Some compilers refer to this representation as a "mangled name." It typically encodes the function’s name, signature, return type, and the class and namespace (if any) to which it belongs.

> EXAMPLE: In this example, the `decoratedName` property contains a "mangled" name emitted by a C++ compiler:
> 
> ```json
> {                                              # A logicalLocation object
>   "name": "c(float)",
>   "fullyQualifiedName": "b::c(float)",
>   "decoratedName": "?c@b@@AAGXM@Z"
> }
> ```

### kind property{#logicallocation-object--kind-property}

A `logicalLocation` object **SHOULD** contain a property named `kind` whose value is one of the following strings, if any of those strings accurately describes the construct identified by this object.

Although the values suggested here are useful in the specified categories (for example, `"member"` is useful in describing executable code), they **MAY** be used in other contexts as appropriate.

- Values for locations within executable code:

  - `"function"`

  - `"member"`

  - `"module"`

  - `"namespace"`

  - `"resource"`

  - `"type"`

  - `"returnType"`

  - `"parameter"`

  - `"variable"`

- Values for locations within XML or HTML documents:

  - `"element"`

  - `"attribute"`

  - `"text"`

  - `"comment"`

  - `"processingInstruction"`

  - `"dtd"`

  - `"declaration"`

> EXAMPLE 1: Consider the following XML document:
> 
> ```xml
> 1.  <?xml version="1.0"?>
> 2.  <orders>
> 3.    <order number="">
> 4.      <total>-$3.25</total>
> 5.    </order>
> 6.  </order>
> ```
> 
> Suppose that an analysis tool detects errors on line 3 (the order number is blank) and line 4 (the total is negative). It might represent the logical locations of these errors as XML Paths (although this is not required), as follows:
> 
> ```json
> {                                 # A run object (§3.14)
>   "results": [                    # See §3.14.23.
>     {                             # A result object (§3.27).
>       "locations": [              # See §3.27.12.
>         {                         # A location object (§3.28).
>           "logicalLocations": [   # See §3.28.4.
>             {                     # A logicalLocation object.
>               "fullyQualifiedName": "/orders/order[1]/@number",
>               "index": 2
>             }
>           ]
>         }
>       ],
>       ...
>     },
>     {
>       "locations": [
>         {
>           "logicalLocations": [
>             {
>               "fullyQualifiedName": "/orders/order[1]/total/text()",
>               "index": 3
>             }
>           ]
>         }
>       ],
>       ...
>     }
>   ],
> 
>   "logicalLocations": [           # See §3.14.17.
>     {                             # A logicalLocation object.
>       "name": "orders",
>       "fullyQualifiedName": "/orders",
>       "kind": "element"
>     },
>     {
>       "name": "order[1]",
>       "fullyQualifiedName": "/orders/order[1]",
>       "kind": "element",
>       "parentIndex": 0
>     },
>     {
>       "name": "number",
>       "fullyQualifiedName": "/orders/order[1]/@number",
>       "kind": "attribute",
>       "parentIndex": 1
>     },
>     {
>       "name": "text",
>       "fullyQualifiedName": "/orders/order[1]/text()",
>       "kind": "text",
>       "parentIndex": 1
>     }
>   ]
> }
> ```
> 
> - Values for locations within JSON documents:
> 
>   - `"object"`
> 
>   - `"array"`
> 
>   - `"property"`
> 
>   - `"value"`

> EXAMPLE 2: Consider the following JSON document:
> 
> ```json
> 1.  {
> 2.    "orders": [
> 3.      {
> 4.        "productIds": [ "A-101", "", "A-223" ],
> 5.        "total": "-$3.25"
> 6.      }
> 7.    ]
> 8.  }
> ```
> 
> Suppose that an analysis tool detects errors on line 4 (one of the product ids blank) and line 5 (the total is negative). It might represent the logical locations of these errors as JSON Pointers (although this is not required), as follows:
> 
> ```json
> {                                 # A run object (§3.14)
>   "results": [                    # See §3.14.23.
>     {                             # A result object (§3.27).
>       "locations": [              # See §3.27.12.
>         {                         # A location object (§3.28).
>           "logicalLocation": {    # See §3.28.4.
>             "fullyQualifiedName": "/orders/0/productIds/1",
>             "index": 3
>           }
>         }
>       ]
>     },
>     {
>       "locations": [
>         {
>           "logicalLocation": {
>             "fullyQualifiedName": "/orders/0/total",
>             "index": 4
>           }
>         }
>       ]
>     }
>   ],
> 
>   "logicalLocations": [           # See §3.14.17.
>     {                             # A logicalLocation object (§3.33).
>       "name": "orders",
>       "fullyQualifiedName": "/orders",
>       "kind": "array"
>     },
>     {
>       "name": "0",
>       "fullyQualifiedName": "/orders/0",
>       "kind": "object",
>       "parentIndex": 0
>     },
>     {
>       "name": "productIds",
>       "fullyQualifiedName": "/orders/0/productIds",
>       "kind": "array",
>       "parentIndex": 1
>     },
>     {
>       "name": "1",
>       "fullyQualifiedName": "/orders/0/productIds/1",
>       "kind": "value",
>       "parentIndex": 2
>     },
>     {
>       "name": "total",
>       "fullyQualifiedName": "/orders/0/total",
>       "kind": "property",
>       "parentIndex": 1
>     }
>   ]
> } 
> ```

If none of those strings accurately describes the construct, kind **MAY** contain any value specified by the analysis tool.

If a logical location is both a member and a type (for example, a nested class in C++ or C#), the value of `kind`, if present, **SHALL** be `"type"`.

> NOTE: The purpose of this property is to help result management systems group results that occur in the same logical location. If one result specifies the logical location "namespace A", and another result specifies the logical location "class A", the difference in the `kind` property between the two results tells the result management system to sort them into different groups.

### parentIndex property{#logicallocation-object--parentindex-property}

If this `logicalLocation` object represents a nested logical location, then it **SHALL** contain a property named `parentIndex` whose value is the array index ([§3.7.4](#array-indices)) of the parent `logicalLocation` object within `theRun.logicalLocations` ([§3.14.17](#run-object--logicallocations-property)).

If `thisObject` represents a top-level logical location, then `parentIndex` **SHALL** be absent.

> NOTE: `parentIndex` makes it possible to navigate from the `logicalLocation` object representing a nested logical location to the `logicalLocation` objects representing each of its parent logical locations in turn, up to the top-level logical location.

> EXAMPLE: In this example, the logical location `n::f(void)` is nested within the top-level logical location `n`. The `logicalLocation` object representing `n::f(void)` contains a `parentIndex` property that points to the object representing `n`; the object representing `n` does not contain a `parentIndex` property.
> 
> ```json
> {                                            # A run object (§3.14).
>   "logicalLocations": [                      # See §3.14.17.
>     {
>       "name": "f(void)",                     # See §3.33.4.
>       "fullyQualifiedName": "n::f(void)",    # See §3.33.5.
>       "kind": "function",                    # See §3.33.7.
>       "parentIndex": 1
>     },
>     {
>       "name": "n",
>       "kind": "namespace"
>     }
>   ]
> }
> ```
