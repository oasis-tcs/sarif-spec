## toolComponentReference object

### General{#toolcomponentreference-object--general}

A `toolComponentReference` object identifies a particular `toolComponent` object ([§3.19](#toolcomponent-object)), either `theTool.driver` ([§3.18.2](#driver-property)) or an element of `theTool.extensions` ([§3.18.3](#extensions-property)). We refer to the identified `toolComponent` object as `theComponent`.

### toolComponent lookup

If neither `index` ([§3.54.4](#toolcomponentreference-object--index-property)) nor `guid` ([§3.54.5](#toolcomponentreference-object--guid-property)) is present, `theComponent` **SHALL** be `theTool.driver` ([§3.18.2](#driver-property)).

If `index` is present, `theComponent` **SHALL** be the object at array index `index` within `theTool.extensions` ([§3.18.3](#extensions-property)).

If `index` is absent and `guid` is present, `theComponent` **SHALL** be either `theTool.driver` or an element of `theTool.extensions`, whichever one has a matching `guid` property.

### name property{#toolcomponentreference-object--name-property}

A `toolComponentReference` object **MAY** contain a property named `name` whose value is a string equal to `theComponent.name` ([§3.19.8](#toolcomponent-object--name-property)).

> NOTE: This property does not participate in the lookup, but its presence improves the readability of the log file at the expense of increased file size.

### index property{#toolcomponentreference-object--index-property}

If `theComponent` is an element of `theTool.extensions` ([§3.18.3](#extensions-property)), a `toolComponentReference` object **MAY** contain a property named `index` whose value is the array index ([§3.7.4](#array-indices)) of that element. Otherwise, `index` SHALL be absent.

### guid property{#toolcomponentreference-object--guid-property}

A `toolComponentReference` object **MAY** contain a property named `guid` whose value is a GUID-valued string ([§3.5.3](#guid-valued-strings)) equal to `theComponent.guid` ([§3.19.6](#toolcomponent-object--guid-property)).
