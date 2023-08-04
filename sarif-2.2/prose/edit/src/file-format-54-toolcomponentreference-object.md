## toolComponentReference object

### General{#toolcomponentreference-object--general}

A `toolComponentReference` object identifies a particular `toolComponent` object ([sec](#toolcomponent-object)), either `theTool.driver` ([sec](#driver-property)) or an element of `theTool.extensions` ([sec](#extensions-property)). We refer to the identified `toolComponent` object as `theComponent`.

### toolComponent lookup

If neither `index` ([sec](#toolcomponentreference-object--index-property)) nor `guid` ([sec](#toolcomponentreference-object--guid-property)) is present, `theComponent` **SHALL** be `theTool.driver` ([sec](#driver-property)).

If `index` is present, `theComponent` **SHALL** be the object at array index `index` within `theTool.extensions` ([sec](#extensions-property)).

If `index` is absent and `guid` is present, `theComponent` **SHALL** be either `theTool.driver` or an element of `theTool.extensions`, whichever one has a matching `guid` property.

### name property{#toolcomponentreference-object--name-property}

A `toolComponentReference` object **MAY** contain a property named `name` whose value is a string equal to `theComponent.name` ([sec](#toolcomponent-object--name-property)).

> NOTE: This property does not participate in the lookup, but its presence improves the readability of the log file at the expense of increased file size.

### index property{#toolcomponentreference-object--index-property}

If `theComponent` is an element of `theTool.extensions` ([sec](#extensions-property)), a `toolComponentReference` object **MAY** contain a property named `index` whose value is the array index ([sec](#array-indices)) of that element. Otherwise, `index` SHALL be absent.

### guid property{#toolcomponentreference-object--guid-property}

A `toolComponentReference` object **MAY** contain a property named `guid` whose value is a GUID-valued string ([sec](#guid-valued-strings)) equal to `theComponent.guid` ([sec](#toolcomponent-object--guid-property)).
