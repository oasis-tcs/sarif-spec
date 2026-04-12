## `translationMetadata` Object

### General{#translationmetadata-object--general}

A `translationMetadata` object describes a translation. It is necessary because in a `toolComponent` object that represents a translation, the usual descriptive properties `name` ([sec](#toolcomponent-object--name-property)), `fullName` ([sec](#toolcomponent-object--fullname-property)), *etc.* contain the translations of the corresponding strings in the `toolComponent` being translated; therefore, they are not available to hold descriptive information for the translation itself.

Because they occur only in `toolComponent` objects that represent translations, the properties of a `translationMetadata` object are not themselves localized ([sec](#localizable-strings)).

> EXAMPLE 1:
>
> ```json
> {                           # A toolComponent object ((#toolcomponent-object)).
>   "language": "fr-FR",      # The language of the translation (see (#language-property)).
> 
>   "translationMetadata": {  # A translation metadata object.
>     "name": "CodeScanner translation for fr-FR ",
>     "fullName": "CodeScanner translation for fr-FR by Example Corp.",
>     "shortDescription": {
>       "text": "A good translation"
>     },
>     "fullDescription": {
>       "text": "A good translation performed by native en-US speakers."
>     }
>   },
> 
>   "name": "(fr-FR translation of translated component’s name)",
>   "fullName": "(fr-FR translation of translated component’s full name)",
>   ...
> }
> ```

### `name` Property{#translationmetadata-object--name-property}

A `translationMetadata` object **SHALL** contain a property named `name` whose value is a string containing a name for the translation.

### `fullName` Property{#translationmetadata-object--fullname-property}

A `translationMetadata` object **MAY** contain a property named `fullName` whose value is a string containing the name of the translation along with any other useful identifying information.

### `shortDescription` Property{#translationmetadata-object--shortdescription-property}

A `translationMetadata` object **MAY** contain a property named `shortDescription` whose value is a `multiformatMessageString` object ([sec](#multiformatmessagestring-object)) containing a brief description of the translation.

### `fullDescription` Property{#translationmetadata-object--fulldescription-property}

A `translationMetadata` object **MAY** contain a property named `fullDescription` whose value is a `multiformatMessageString` object ([sec](#multiformatmessagestring-object)) containing a comprehensive description of the translation.

### `downloadUri` Property{#translationmetadata-object--downloaduri-property}

A `translationMetadata` object **MAY** contain a property named `downloadUri` whose value is a string containing the absolute URI [cite](#RFC3986) from which the translation can be downloaded.

### `informationUri` Property{#translationmetadata-object--informationuri-property}

A `translationMetadata` object **MAY** contain a property named `informationUri` whose value is a string containing the absolute URI [cite](#RFC3986) at which information about the translation can be found.
