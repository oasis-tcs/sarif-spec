## toolComponent object

### General{#toolcomponent-object--general}

A `toolComponent` object represents one of the components which comprise an analysis tool or a converter, either its driver or one of its extensions. For more information, see [sec](#tool-object--general).

SARIF also uses `toolComponent` objects to represent other components that participate in the analysis, including:

- Taxonomies ([sec](#taxonomies))

- Translations ([sec](#translations))

- Policies ([sec](#policies))

> NOTE: SARIF makes this design choice because `toolComponent` objects contain properties that are useful in all of these other types of components: properties that represent the component’s identity, localizable properties ([sec](#localizable-strings)) that label the component and describe its purpose, and properties that define rules and similar items that participate in the analysis. Not every property is useful in every component type; for example, `translationMetadata` ([sec](#translationmetadata-property)) is useful only in `toolComponent` objects that represent translations.

### Constraints{#toolcomponent-object--constraints}

At least one of `version` ([sec](#toolcomponent-object--version-property)) and `semanticVersion` ([sec](#semanticversion-property)) **SHOULD** be present.

### Taxonomies

A taxonomy is a classification of results into a set of categories. Some taxonomies are defined publicly, without reference to any particular tool; we refer to these as "standard taxonomies." An example is the Common Weakness Enumeration \[[CWE](#CWE)\]. A tool can also define its own classification (in addition to the classification implied by its rule definitions); we refer to this as a "custom taxonomy." We refer to a category within a taxonomy as a "taxon" (*pl.* "taxa").

A taxonomy is represented by a `toolComponent` object. Its taxa are stored in the `taxa` property ([sec](#toolcomponent-object--taxa-property)).

A taxon is represented by a `reportingDescriptor` object ([sec](#reportingdescriptor-object)); hence `toolComponent.taxa` is an array of `reportingDescriptor` objects. This is the same object that represents rules and notifications, so a taxon can specify identity properties such as `id` ([sec](#reportingdescriptor-object--id-property)) and `guid` ([sec](#reportingdescriptor-object--guid-property)), localizable ([sec](#localizable-strings)) descriptive properties such as `name` ([sec](#reportingdescriptor-object--name-property)) and `fullDescription` ([sec](#reportingdescriptor-object--fulldescription-property)), and configuration properties in `defaultConfiguration` ([sec](#defaultconfiguration-property)).

Standard taxonomies **SHALL** be stored in the `run.taxonomies` array ([sec](#taxonomies-property)). Every `toolComponent` object in this array **SHALL** contain a `taxa` property ([sec](#toolcomponent-object--taxa-property)), and **SHALL NOT** contain `rules` ([sec](#rules-property)) or `notifications` ([sec](#notifications-property)) properties.

A custom taxonomy is represented by providing a `toolComponent` object in `tool.driver` ([sec](#driver-property)) or `tool.extensions` ([sec](#extensions-property)) with a `taxa` property. Such a `toolComponent` object **MAY** still contain `rules` and/or `notifications` as usual.

> EXAMPLE 1: In this example, the tool driver supports the CWE™ taxonomy, and also supports a custom taxonomy that it defines. Any result that violates the driver’s rule `"CA2101"` falls into the `"MemoryManagement"` taxon of its custom taxonomy, as shown by the `"superset"` relationship from the `"MemoryManagement"` taxon to the rule (which is interpreted as "The `MemoryManagement` taxon is a superset of rule `CA2101`"). For more information on relationships, see [sec](#reportingdescriptor-object--relationships-property) and [sec](#reportingdescriptorrelationship-object).
> 
> ```json
> {                                  # A run object (§3.14).
>   "tool": {                        # See §3.14.6.
>     "driver": {                    # See §3.18.2.
>       "name": "CodeScanner",
>       "semanticVersion": "3.3",    # See §3.19.12.
>       "guid": "11111111-1111-1111-8888-111111111111",
>       ...
>       "rules": [
>         {
>           "id": "CA2101",
>           "shortDescription": {
>             "text": "Failed to release dynamic memory."
>           },
>           "relationships": [       # See §3.49.15.
>             {              # A reportingDescriptorRelationship object (§3.53).
>               "target": {          # See §3.53.2
>                 "id": "MemoryManagement",
>                 "guid": "66666666-6666-1111-8888-666666666666",
>                 "toolComponent": {
>                   "name": "CodeScanner",
>                   "guid": "11111111-1111-1111-8888-111111111111"
>                 }
>               },
>               "kinds": [           # See §3.53.3.
>                 "superset"
>               ]
>             }
>           ]
>         },
>         ...
>       ],
>       "taxa": [
>         {
>           "id": "MemoryManagement",
>           "guid": "66666666-6666-1111-8888-666666666666",
>           "shortDescription": {
>             "text": "Improper usage of dynamic memory."
>           }
>         },
>         {
>           "id": "Cryptography",
>           "guid": "77777777-7777-1111-8888-777777777777",
>           "shortDescription": {
>             "text": "Insecure use of cryptography."
>           }
>         }
>       ],
>       "supportedTaxonomies": [
>         {
>           "name": "CodeScanner",
>           "guid": "11111111-1111-1111-8888-111111111111"
>         },
>         {
>           "name": "CWE",
>           "index": 1,
>           "guid": "33333333-0000-1111-8888-000000000000"
>         }
>       ]
>     }
>   },
> 
>   "taxonomies": [
>     {
>       "name": "CWE",
>       "version": "3.2",
>       "releaseDateUtc": "2019-01-03",
>       "guid": "33333333-0000-1111-8888-000000000000",
>       "informationUri": "https://cwe.mitre.org/data/published/cwe_v3.2.pdf/",
>       "downloadUri": "https://cwe.mitre.org/data/xml/cwec_v3.2.xml.zip",
>       "organization": "MITRE",
>       "shortDescription": {
>         "text": "The MITRE Common Weakness Enumeration"
>       },
>       "contents": [
>         "localizedData",
>         "nonLocalizedData"
>       ],
>       "isComprehensive": true,
>       "minimumRequiredLocalizedDataSemanticVersion": "3.2",
>       "taxa": [
>         {
>           "id": "327",
>           "guid": "33333333-0000-1111-8888-111111111111",
>           "name": "BrokenOrRiskyCryptographicAlgorithm",
>           "shortDescription": {
>             "text": "Use of a Broken or Risky Cryptographic Algorithm."
>           },
>           "defaultConfiguration": {
>             "level": "warning"
>           }
>         },
>         {
>           "id": "924",
>           "guid": "33333333-0000-1111-8888-222222222222",
>           "name": "TransmittedMessageIntegrity",
>           "shortDescription": {
>             "text": "Improper Enforcement of Message Integrity ..."
>           },
>           "defaultConfiguration": {
>             "level": "warning"
>           }
>         },
>         ...
>       ]
>     }
>   ],
> 
>   ...
> }
> ```

### Translations

A translation is the rendering of a `toolComponent` object’s localizable strings ([sec](#localizable-strings)) into another language.

A translation is itself represented by a `toolComponent` object whose localizable properties are the translated versions of the corresponding properties in the component being translated. A translation specifies the tool component to which it applies by way of its `associatedComponent` property ([sec](#associatedcomponent-property)).

Translations **SHALL** be stored in the `run.translations` array ([sec](#translations-property)).

A translation **SHALL** specify the component that it translates by way of its `associatedComponent` property ([sec](#associatedcomponent-property)). `associatedComponent` **SHALL NOT** refer to another translation.

A translation component **SHALL** contain the translations of every localizable string in the translated component, even if the translated string is identical to the original string. It **MAY** contain additional strings that do not appear in the translated component.

To some degree, translations and the components they translate can version independently. The versioning relationship between a translation and the translated component is explained in the sections describing `localizedDataSemanticVersion` ([sec](#localizeddatasemanticversion-property)), populated by translations, and `requiredMinimumLocalizedDataSemanticVersion` ([sec](#minimumrequiredlocalizeddatasemanticversion-property)), populated by translated components.

A translation **SHOULD** include the value `"localizedData"` in its `contents` array ([sec](#toolcomponent-object--contents-property)). It **MAY** also include the value `"nonLocalizedData"`.

To facilitate the identification of translations that are associated with a given component, a `toolComponent` **SHOULD** populate its `guid` property ([sec](#toolcomponent-object--guid-property)), and a translation for that component **SHOULD** set its `guid` property to the same value.

In many cases, a new version of a `toolComponent` defines new localizable strings or requires changes to existing ones (for example, when the tool defines new analysis rules). But in some cases, a new version of a `toolComponent` can use existing translations (for example, in the case of a bug fix release). To ensure that new translations are created only when necessary, a translation component **SHOULD** populate `localizedDataSemanticVersion` ([sec](#localizeddatasemanticversion-property)), and a translatable component **SHOULD** populate `minimumRequiredLocalizedDataSemanticVersion` ([sec](#minimumrequiredlocalizeddatasemanticversion-property)). See the descriptions of those two properties for an explanation of the interaction between them.

> EXAMPLE 1: In this example, a French translation is available. It translates localizable component-level properties such as `toolComponent.name` ([sec](#toolcomponent-object--name-property)), as well as rule-level properties such as `reportingDescriptor.shortDescription` ([sec](#reportingdescriptor-object--shortdescription-property)). The translation can be used because its `localizedDataSemanticVersion` property ([sec](#localizeddatasemanticversion-property)) is compatible with the translated component’s `minimumRequiredLocalizedDataSemantic` version property ([sec](#minimumrequiredlocalizeddatasemanticversion-property)).
> 
> ```json
> {                                  # A run object (§3.14).
>   "tool": {                        # See §3.14.6.
>     "driver": {                    # See §3.18.2.
>       "name": "CodeScanner",
>       "semanticVersion": "3.3",    # See §3.19.12.
>       "minimumRequiredLocalizedDataSemanticVersion": "3.1",
>       ...
>       "rules": [
>         {
>           "id": "CA2101",
>           "shortDescription": {
>             "text": "Do not do dangerous things."
>           }
>         }
>       ]
>     }
>   },
>   "translations": [
>     {                              # A toolComponent object.
>       "language": "fr-FR",
>       "semanticVersion": "3.1.3",
>       "localizedDataSemanticVersion": "3.1.2",
>       "contents": [
>         "localizedData"
>       ],
>       "translationMetadata": {
>         "name": "French translation for CodeScanner"
>       },
>       "name": "<The tool name 'CodeScanner' translated into French>",
>       ...
>       "rules": [
>         {
>           "id": "CA2101",
>           "shortDescription": {
>             "text": "<'Do not do dangerous things.' Translated into French>"
>           }
>         }
>       ]
>     }
>   ],
>   ...
> }
> ```
> 
### Policies

A policy is a set of rule configurations that specify how results that violate the rules defined by a particular tool component are to be treated.

A policy is represented by a `toolComponent` object. A policy specifies the tool component to which it applies by way of its `associatedComponent` property ([sec](#associatedcomponent-property)).

A policy **SHALL** contain a `rules` property ([sec](#rules-property)), each `reportingDescriptor`-valued ([sec](#reportingdescriptor-object)) element of which in turn contains a `defaultConfiguration` property ([sec](#defaultconfiguration-property)). Each element of the `rules` array **SHALL** correspond to a rule defined by the associated component. The `rules` array **MAY** contain elements describing any or all of the rules defined by the associated component. The elements of the `rules` array **MAY** alter rule properties such as `level` ([sec](#reportingconfiguration-object--level-property)), and **MAY** enable or disable rules. In this way, the policy defines the code analysis standard that is expected of the engineering team.

Policies **SHALL** be stored in the `run.policies` array ([sec](#policies-property)).

A SARIF consumer **MAY** offer the user the option of treating results according to the associated component’s default rule configuration (possibly modified by command line options stored in `theInvocation.ruleConfigurationOverrides` ([sec](#ruleconfigurationoverrides-property)), by configuration files, by environment variables, or by any other means), or according to the configuration defined by a selected element of `run.policies`. If the user selects a policy, then for any result that violates a rule covered by that policy, the SARIF consumer **SHALL** treat the result according to the policy, regardless of the associated component’s default configuration, regardless of any configuration overrides, and regardless of whether the `result` object ([sec](#result-object)) itself specifies a configuration property such as `level` ([sec](#result-object--level-property)).

> NOTE: The rationale is that when a user asks to see how a policy views a set of results, they want to see exactly what the policy has to say, regardless of any configuration options that might have been selected when the log was created.

> EXAMPLE 1: In this example, the tool driver defines rule `CA2101` to be a warning and disables rule `CA2551` by default. However, the corporate security policy specifies that a violation of rule `CA2101` is an error and requires rule `CA2551` to be run. The presence of `run.policies` allows a SARIF viewer to display the results according to the tool’s view or the policy’s view.

```json
{                                  # A run object (§3.14).
  "tool": {                        # See §3.14.6.
    "driver": {                    # See §3.18.2.
      "name": "CodeScanner",
      "rules": [                   # See §3.19.23.
        {                          # A reportingDescriptor object (§3.49).
          "id": "CA2101",
          "defaultConfiguration" { # See §3.49.14.
            "level": "warning"
          }
        },
        {
          "id": "CA2551",
          "defaultConfiguration": {
            "level": "warning",
            "enabled": false
          }
        }
      ]
    }
  },
  "policies": [
    {                              # A toolComponent object (§3.19).
      "name": "Example Corp. Security Policy",
      "semanticVersion": "7.0",
      "rules": [
        {
          "id": "CA2101",
          "defaultConfiguration" {
            "level": "error"
          }
        },
        {
          "id": "CA2551",
          "defaultConfiguration" {
            "enabled": true
          }
        }
      ]
    }
  ]
}
```

### guid property{#toolcomponent-object--guid-property}

A `toolComponent` object **MAY** contain a property named `guid` whose value is a GUID-valued string ([sec](#guid-valued-strings)) that provides a unique, stable identifier for the component. `guid` **SHALL NOT** vary between versions of a given component.

### Product hierarchy properties

The `name` ([sec](#toolcomponent-object--name-property)) or `fullName` ([sec](#toolcomponent-object--fullname-property)), `product` ([sec](#product-property)), and `productSuite` ([sec](#productsuite-property)) properties establish a hierarchy of related software: the tool component identified by `name` and/or `fullName` is part of the product named by `product`, which in turn is part of the product suite identified by `productSuite`.

### name property{#toolcomponent-object--name-property}

A `toolComponent` object **SHALL** contain a property named `name` whose value is a localizable string ([sec](#localizable-strings)) containing the name of the tool component.

> EXAMPLE 1: `"CodeScanner"`

> EXAMPLE 2: `"CodeScanner Security Rules Plugin"`

> EXAMPLE 3: `"CodeScanner configuration file"`

### fullName property{#toolcomponent-object--fullname-property}

A `toolComponent` object **MAY** contain a property named `fullName` whose value is a localizable string ([sec](#localizable-strings)) containing the name of the tool component along with its version and any other useful identifying information, such as its locale.

> EXAMPLE 1: `"CodeScanner 1.1, Developer Preview (en-US)"`

### product property

A `toolComponent` object **MAY** contain a property named `product` whose value is a localizable string ([sec](#localizable-strings)) containing the name of the product to which the tool component belongs.

> EXAMPLE 1: `"product": "Example Software Corp. Security Scanner"`

### productSuite property

A `toolComponent` object **MAY** contain a property named `productSuite` whose value is a localizable string ([sec](#localizable-strings)) containing the name of the suite of products to which the tool component belongs.

> EXAMPLE 1: `"productSuite": "Example Software Corp. Quality Tools"`

### semanticVersion property

A `toolComponent` object **MAY** contain a property named `semanticVersion` whose value is a string containing the tool component’s version in a format that conforms to the syntax and semantics specified by Semantic Versioning \[[cite](#SEMVER)\].

> EXAMPLE 1: `"semanticVersion": "1.1.2-beta.12"`

> NOTE 1: Semantic versions are sortable in chronological order of release. The presence of the `semanticVersion` property allows results management systems to (for example) restrict the results they display to versions newer than a specified version, or to restrict the results to a particular major version.

Unless the author of the converter knows that the version number of the tool from which it converts is intended to be interpreted according to Semantic Versioning \[[cite](#SEMVER)\], the converter **SHALL NOT** emit the `semanticVersion` property in `run.tool` ([sec](#run-object--tool-property)), although of course it may emit its own `semanticVersion` property (the one in `run.conversion.tool` ([sec](#conversion-object--tool-property))).

### version property{#toolcomponent-object--version-property}

A `toolComponent` object **MAY** contain a property named `version` whose value is a string containing the tool component’s version in whatever format the component natively provides.

> NOTE: Plugins are often binary files whose version can be determined; configuration files are typically text files with no embedded version information.

### dottedQuadFileVersion property

If the operating system on which the tool runs provides a value for the file version of the tool component's primary executable file, and if that value logically consists of an ordered set of four non-negative integers, then the `toolComponent` object **MAY** contain a property named `dottedQuadFileVersion` whose value is a string representation of that file version in this syntax:

    dottedQuadFileVersion = non negative integer, 3*(".", non negative integer);

where the `non negative integer`s follow the logical order of the components of the file version.

If the operating system does not provide such a value, the `dottedQuadFileVersion` property **SHALL** be absent.

> EXAMPLE 1: On the Microsoft Windows® platform, this information is available in the `FILEVERSION` member of the `VERSIONINFO` structure.

### releaseDateUtc property

A `toolComponent` object **MAY** contain a property named `releaseDateUtc` whose value is a string in the format specified in [sec](#datetime-properties), specifying the UTC date (and optionally, the time) of the component’s release.

### downloadUri property{#toolcomponent-object--downloaduri-property}

A `toolComponent` object **MAY** contain a property named `downloadUri` whose value is a localizable string ([sec](#localizable-strings)) containing the absolute URI \[[cite](#RFC3986)\] from which this version of the tool component can be downloaded.

> NOTE: This property is localizable to allow different language versions of a tool to be downloaded from their own URIs.

### informationUri property{#toolcomponent-object--informationuri-property}

A `toolComponent` object **MAY** contain a property named `informationUri` whose value is a localizable string ([sec](#localizable-strings)) containing the absolute URI \[[cite](#RFC3986)\] at which information about this version of the tool component can be found.

> NOTE: This property is localizable to allow tool information in different languages to be found at different URIs.

### organization property

A `toolComponent` object **MAY** contain a property named `organization` whose value is a localizable string ([sec](#localizable-strings)) containing the name of the company or organization that produced the tool component.

> EXAMPLE 1: `"organization": "Example Software Corp."`

### shortDescription property{#toolcomponent-object--shortdescription-property}

A `toolComponent` object **MAY** contain a property named `shortDescription` whose value is a localizable `multiformatMessageString` object ([sec](#multiformatmessagestring-object), [sec](#localizable-multiformatmessagestrings)) containing a brief description of the tool component.

The `shortDescription` property **SHOULD** be a single sentence that is understandable when visible space is limited to a single line of text.

### fullDescription property{#toolcomponent-object--fulldescription-property}

A `toolComponent` object **MAY** contain a property named `fullDescription` whose value is a localizable `multiformatMessageString` object ([sec](#multiformatmessagestring-object), [sec](#localizable-multiformatmessagestrings)) containing a comprehensive description of the tool component.

The beginning of `fullDescription` (for example, its first sentence) **SHOULD** provide a concise description of the tool component, suitable for display in cases where available space is limited. Tools that construct `fullDescription` in this way do not need to provide a value for `shortDescription` ([sec](#toolcomponent-object--shortdescription-property)). Tools that do not construct `fullDescription` in this way **SHOULD** provide a value for `shortDescription`.

> NOTE: The rationale for this guidance is that in the absence of `shortDescription`, a viewer with limited display space might display a truncated version of `fullDescription`, for example, the first sentence (if a sentence is identifiable), the first paragraph, or the first 100 characters. If this guidance is not followed, that truncated description might not be understandable.

### language property

Depending on the circumstances, a `toolComponent` object either **SHALL** or **MAY** contain a property named `language` whose value is a string specifying the language of the localizable strings ([sec](#localizable-strings)) contained in the component (except for those in the `translationMetadata` property ([sec](#translationmetadata-property))), in a subset of the format specified by the language tags standard \[[cite](#RFC5646)\]. The subset consists of strings conforming to the syntax

    language value = language code, "-", country code;

    language code = ? ISO 2-character language name \[[cite](#ISO639-1;2002)\] ?;

    country code = ? ISO country code \[[cite](#ISO3166-1;2013)\] ?;

If this object represents a translation (see [sec](#translations)), `language` **SHALL** be present; otherwise it **MAY** be present.

If this property is absent, it **SHALL** default to `"en-US"`.

> EXAMPLE 1: The language is region-neutral English:
> 
>     "language": "en"

> EXAMPLE 2: The language is French as spoken in France:
> 
>     "language": "fr-FR"

### globalMessageStrings property

A `toolComponent` object **MAY** contain a property named `globalMessageStrings` whose value is an object ([sec](#object-properties)) each of whose property values is a localizable `multiformatMessageString` object ([sec](#multiformatmessagestring-object), [sec](#localizable-multiformatmessagestrings)). The property names correspond to `id` properties ([sec](#message-object--id-property)) within `message` objects ([sec](#message-object)).

> EXAMPLE 1:
> 
> ```json
> "driver": {                       # A toolComponent object (§3.19).
>   "globalMessageStrings": {
>     "call": {                     # A multiformatMessageString object (§3.12).
>       "text": "Function call",
>       "markdown": "Function **call**"
>     },
>     "return": {
>       "text": "Function return",
>       "markdown": "Function **return**"
>     }
>   }
> }
> ```

> NOTE: The message strings in this property are not associated with a single rule (hence the "global" in the property name.

### rules property

A `toolComponent` object **MAY** contain a property named `rules` whose value is an array of zero or more unique ([sec](#array-properties-with-unique-values)) `reportingDescriptor` objects ([sec](#reportingdescriptor-object)) each of which provides information about an analysis rule supported by the tool component.

Some tools use the same identifier to refer to multiple distinct (although logically related) rules. Therefore, the `id` properties ([sec](#reportingdescriptor-object--id-property)) of the `reportingDescriptor` objects do not need to be unique within the array.

> EXAMPLE 1: In this example, two distinct but related rules have the same rule id. They are distinguished by their message strings.
> 
> ```json
> "driver": {                       # A toolComponent object (§3.19).
>   "name": "CodeScaner",
>   "rules": [
>     {                             # A reportingDescriptor object (§3.49).
>       "id": "CA1711",
>       "shortDescription": {
>         "text": "Certain type name suffixes should not be used."
>       },
>       "messageStrings": {
>         "default": {
>           "text": "Rename type name {0} so that it does not end in '{1}'."
>         }
>       }
>     },
>     {
>       "id": "CA1711",
>       "shortDescription": {
>         "text": "Certain type name suffixes have preferred alternatives."
>       },
>       "messageStrings": {
>         "default": {
>           "text": "Either replace the suffix '{0}' in member name '{1}' with
>                   the suggested numeric alternate or provide
>                   a more meaningful suffix."
>         }
>       }
>     }
>   ]
> }
> ```

### notifications property

A `toolComponent` object **MAY** contain a property named `notifications` whose value is an array of zero or more unique ([sec](#array-properties-with-unique-values)) `reportingDescriptor` objects ([sec](#reportingdescriptor-object)) each of which provides information about a notification provided by the tool component.

A tool might use the same identifier to refer to multiple distinct (although logically related) notifications. Therefore, the `id` properties ([sec](#reportingdescriptor-object--id-property)) of the `reportingDescriptor` objects do not need to be unique within the array.

> EXAMPLE 1: In this example, two distinct but related notifications have the same id. They are distinguished by their descriptions and message strings.
> 
> ```json
> "driver": {                      # A toolComponent object (§3.19).
>   "notifications": [
>     {                            # A reportingDescriptor object (§3.49).
>       "id": "ERR0001",
>       "level": "error",
>       "shortDescription": {
>         "text": "A plugin could not be loaded because it does not exist."
>       },
>       "messageStrings": {
>         "default": "Cannot load plugin '{0}' because it was not found."
>       }
>     },
>     {
>       "id": "ERR0001",
>       "level": "error",
>       "shortDescription": {
>         "text": "A plugin could not be loaded because it is not signed."
>       },
>       "messageStrings": {
>         "default": "Cannot load plugin '{0}' because it is not signed."
>       }
>     }
>   ]
> }
> ```
> 
### taxa property{#toolcomponent-object--taxa-property}

A `toolComponent` object **MAY** contain a property named `taxa` whose value is an array of zero or more unique ([sec](#array-properties-with-unique-values)) `reportingDescriptor` objects ([sec](#reportingdescriptor-object)) each of which provides information about a taxon defined by the component.

If the `toolComponent` describes a standard taxonomy (for example, the Common Weakness Enumeration \[[CWE](#CWE)\]), it **SHALL NOT** contain `rules` ([sec](#rules-property)) or `notifications` ([sec](#notifications-property)).

> NOTE: Tool components representing standard taxonomies are stored in `run.taxonomies` ([sec](#taxonomies-property)), but will typically be persisted to external property files (see [sec](#rationale)).

If the `toolComponent` describes a tool driver or plugin that defines its own custom taxonomy, it **MAY** contain all of `rules`, `notifications`, and `taxa`.

> EXAMPLE 1: In this example, a `toolComponent` object represents the Common Weakness Enumeration.
> 
> ```json
> {                                   # A toolComponent object.
>   "name": "CWE",
>   "version": "3.2",
>   "guid": "11111111-1111-1111-8888-111111111111",
>   "releaseDateUtc": "2019-01-03",
>   "informationUri": "https://cwe.mitre.org/data/published/cwe_v3.2.pdf/",
>   "downloadUri": "https://cwe.mitre.org/data/xml/cwec_v3.2.xml.zip",
>   "organization": "MITRE",
>   "shortDescription": {
>     "text": "The MITRE Common Weakness Enumeration"
>   },
>   "taxa": [
>     {
>       "id": "327",
>       "name": "BrokenOrRiskyCryptographicAlgorithm",
>       "shortDescription": {
>         "text": "Use of a broken or risky cryptographic algorithm."
>       },
>       "defaultConfiguration": {
>         "level": "warning"
>       }
>     },
>     ...
>   ]
> }
> ```

### supportedTaxonomies property

A `toolComponent` object **MAY** contain a property named `supportedTaxonomies` whose value is an array of zero or more unique ([sec](#array-properties-with-unique-values)) `toolComponentReference` objects ([sec](#toolcomponentreference-object)) each of which refers to a taxonomy ([sec](#taxonomies)) that the component uses to classify results.

A `toolComponent` object that contains a `supportedTaxonomies` property **SHALL** declare which taxa (if any) each of its rules falls into by providing the `relationships` property ([sec](#reportingdescriptor-object--relationships-property)) as appropriate on each `reportingDescriptor` object ([sec](#reportingdescriptor-object)) in its `rules` array ([sec](#rules-property)).

> NOTE: A SARIF consumer could infer the set of taxonomies that a component supports by examining the set of `relationships` properties of each element of `toolComponent.rules`. The `supportedTaxonomies` property is a convenience, intended to enable consumers to see this information at a glance.

If a `toolComponent` supports a custom taxonomy, it **SHOULD** include a reference to itself in `supportedTaxonomies`.

> EXAMPLE 1: In this example, a `toolComponent` claims to support the Common Weakness Enumeration \[[CWE](#CWE)\], and also supports a custom taxonomy.
> 
> ```json
> {                                 # A run object (§3.14)
>   "tool": {                       # See §3.14.6.
>     "driver": {                   # See §3.18.2.
>       "name": "CodeScanner",
>       "guid": "22222222-2222-1111-8888-222222222222",
>       "rules": [                  # See §3.19.23.
>         ...
>       ],
>       "taxa": [                   # See §3.19.25. Here, defines a custom
>         ...                       #  taxonomy.
>       ]
>       "supportedTaxonomies": [
>         {                         # A toolComponentReference object (§3.54).
>           "name": "CWE",          # Declares support for CWE.
>           "index": 0,
>           "guid": "11111111-1111-1111-8888-111111111111"
>         },
>         {
>           "name": "CodeScanner",  # Declares support for its custom taxonomy.
>           "guid": "22222222-2222-1111-8888-222222222222"
>         }
>       ]
>     }
>   },
>   "taxonomies": [
>     {                           # A toolComponentReference object.
>       "name": "CWE",
>       "version": "3.2",
>       "guid": "11111111-1111-1111-8888-111111111111",
>       ...
>       "taxa": [
>         ...
>       ]
>     }
>   ],
>   ...
> }
> ```
> 
### translationMetadata property

If a `toolComponent` object represents a translation ([sec](#translations)), it **SHALL** contain a property named `translationMetadata` whose value is a `translationMetadata` object ([sec](#translationmetadata-object)) that contains descriptive information about the translation itself, as opposed to describing the component whose localizable strings ([sec](#localizable-strings)) it translates. Otherwise, `translationMetadata` **SHALL** be absent.

### locations property{#toolcomponent-object--locations-property}

A `toolComponent` object **MAY** contain a property named `locations` whose value is an array of zero or more unique ([sec](#array-properties-with-unique-values)) `artifactLocation` objects ([sec](#artifactlocation-object)) each of which specifies the location of one of the files comprising this tool component.

### contents property{#toolcomponent-object--contents-property}

A `toolComponent` object **SHOULD** contain a property named `contents` whose value is an array of zero or more unique ([sec](#array-properties-with-unique-values)) strings each of which is one of the following values with the specified meanings:

- `"localizedData"`: The component includes localizable strings ([sec](#localizable-strings)) such as rule messages.

- `"nonLocalizedData"`: The component includes non-localizable properties such as rule severity levels.

If `contents` is absent, it **SHALL** default to `[ "localizedData", "nonLocalizedData" ]`.

> NOTE: The purpose of this property is to help protect components from misuse. Within a SARIF file, the component types are all stored in their own properties, so there is no danger of mistaking, for example, a translation (stored in `run.translations` ([sec](#translations-property))) for a policy (stored in `run.policies` ([sec](#policies-property))). But components such as translations and policies are typically authored independently from a tool and stored separately from its log files. The author of a translation (which contains only `"localizedData"`) can help prevent its misuse as a policy (which requires `"nonLocalizedData"`) by setting `contents` to `[ "localizedData" ]`.
> 
> For example, a user might specify the path to a policy file on a tool’s command line. If the specified file does not claim to contain `"nonLocalizedData"`, the tool could conclude that the file does not contain a policy and warn the user.

### isComprehensive property

A `toolComponent` object **SHOULD** contain a property named `isComprehensive` whose value is a Boolean that is `true` if the component contains complete information for the content types specified by `contents` ([sec](#toolcomponent-object--contents-property)) and `false` otherwise.

If `isComprehensive` is absent, it **SHALL** default to `false`.

> NOTE: This property is useful because tools are permitted to emit `rules` ([sec](#rules-property)), `notifications` ([sec](#notifications-property)), or `taxa` ([sec](#toolcomponent-object--taxa-property)) properties that contain only those items relevant to the current run. For example, a tool might define hundreds of rules, but if a scan detects violations of only two of them, then the `rules` property (if it is present at all, which it does not need to be) need only contain metadata for those two rules.
> 
> So, for example, the author of a translation ([sec](#translations)) would want to work from a log file whose `contents` array includes `"localizedData"` and whose `isComprehensive` property is set to `true`. Similarly, the author of a policy ([sec](#policies)) would want to work from a log file whose `contents` array contains `"nonLocalizedData"` and whose `isComprehensive` property is set to `true`.

### localizedDataSemanticVersion property

If a `toolComponent` object represents a translation ([sec](#translations)), it **SHOULD** contain a property named `localizedDataSemanticVersion` whose value is a string that specifies the semantic version \[[cite](#SEMVER)\] of the translated strings. Otherwise, `localizedDataSemanticVersion` **MAY** be present, in which case it represents the semantic version of the localizable strings ([sec](#localizable-strings)) that are present in this component.

If `localizedDataSemanticVersion` is absent, it **SHALL** default to `thisObject.semanticVersion` ([sec](#semanticversion-property)).

> NOTE 1: See the description of `minimumRequiredLocalizedDataSemanticVersion` ([sec](#minimumrequiredlocalizeddatasemanticversion-property)) for an explanation of how these two properties interact.

> NOTE 2: In a translation, `localizedDataSemanticVersion` will usually be the same as `semanticVersion`. They will differ only if it is necessary to revise the translation component to correct an error unrelated to the translated strings, for example, an error in its `translationMetadata` ([sec](#translationmetadata-property)). In that case, `semanticVersion` would be incremented but `localizedDataSemanticVersion` would not.

### minimumRequiredLocalizedDataSemanticVersion property

If a `toolComponent` object does not represent a translation ([sec](#translations)), it **SHOULD** contain a property named `minimumRequiredLocalizedDataSemanticVersion` whose value is a string that specifies the minumum semantic version \[[cite](#SEMVER)\] of the translated strings that it requires. Otherwise, `minimumRequiredLocalizedDataSemanticVersion` **SHALL** be absent.

If `minimumRequiredLocalizedDataSemanticVersion` is absent, it **SHALL** default to `thisObject.semanticVersion` ([sec](#semanticversion-property)).

When a SARIF consumer is seeking a translation for this object, it **SHALL** only accept one whose `localizedDataSemanticVersion` ([sec](#localizeddatasemanticversion-property)) is greater than or equal to (in the SEMVER sense) but has the same major version component as `thisObject.minimumRequiredLocalizedDataSemanticVersion`.

> NOTE: `minimumRequiredocalizedDataSemanticVersion` can differ from `semanticVersion` for two reasons. First, successive versions of a translated component (even versions whose minor version component is incremented) might be able to use the same set of translated strings. Second, the translation itself might be versioned if, for example, the translation author discovers a typo or decides to clarify a message string.

> EXAMPLE 1: In this example, the tool is at version 3.3, but it only requires strings at version 3.1, because tool versions 3.2 and 3.3 didn’t affect any user-facing localizable strings. Therefore, the translation at index 0 in `theRun.translations` ([sec](#translations-property)) is acceptable.
> 
> ```json
> {                                  # A run object (§3.14).
>   "tool": {                        # See §3.14.6.
>     "driver": {                    # See §3.18.2.
>       "name": "CodeScanner",
>       "semanticVersion": "3.3",    # See §3.19.12.
>       "minimumRequiredLocalizedDataSemanticVersion": "3.1",
>       ...
>     }
>   },
>   "translations": [
>     {                              # A toolComponent object.
>       "language": "fr-FR",
>       "localizedDataSemanticVersion": "3.1.2",
>       ...
>     }
>   ],
>   ...
> }
> ```
> 
### associatedComponent property

If this `toolComponent` object represents a plugin (see [sec](#tool-object--general)), a taxonomy ([sec](#taxonomies)), a translation ([sec](#translations)), or a policy ([sec](#policies)), it **MAY** contain a property named `associatedComponent` whose value is a `toolComponentReference` object ([sec](#toolcomponentreference-object)) which identifies the component (either `theTool.driver` ([sec](#driver-property)) or an element of `theTool.extensions` ([sec](#extensions-property))) to which this plugin, translation, or policy applies. If `associatedComponent` is absent, it **SHALL** default to a reference to `theTool.driver`.

> NOTE: The scenario for a taxonomy component to have an `associatedComponent` property is when a party other than the tool vendor defines a custom taxonomy to categorize the rules defined by a specific tool. In this case, `associatedComponent` would specify the tool’s driver. A custom taxonomy defined by the tool vendor would be defined in in the `taxa` property ([sec](#toolcomponent-object--taxa-property)) of the driver itself, so `associatedComponent` would not be necessary.

The associated `toolComponent` object **MAY** itself contain an `associatedComponent` property; for example, a translation might be associated with a plugin which in turn is associated with the driver (see [sec](#tool-object--general)).
