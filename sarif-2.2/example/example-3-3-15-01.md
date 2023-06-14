### 3.13.5 inlineExternalProperties property

A sarifLog object MAY contain a property named inlineExternalProperties whose value is an array of zero or more unique (§3.7.3) externalProperties objects (§4.3).

NOTE: This property allows multiple runs to share large data sets in a single, self-contained log file.

EXAMPLE: In this example, two tools analyze the same set of image files, stored in sarifLog.inlineExternalProperties[0].artifacts. The first tool locates the inline externalProperties object by means of a URI with the sarif scheme (see §3.10.3). The second tool locates the object by means of its guid property (§4.3.4).

```{label=example-3-13-5-01}
{
  "$schema": "https://docs.oasis-open.org/sarif/sarif/v2.1.0/errata01/csd01/schemas/sarif-schema-2.1.0.json",
  "version": "2.1.0",

  "inlineExternalProperties": [
    {                                           
      "guid": "00001111-2222-1111-8888-555566667777", # See §4.3.4.

      "artifacts": [                                  # See §4.3.6.
        {
          "location": {
            "uri": "apple.png"
          },
          "mimeType": "image/png"
        },
        {
          "location": {
            "uri": "banana.png"
          },
          "mimeType": "image/png"
        }
      ]
    }
  ],

  "runs": [                                           # See §3.13.4.
    {                                                 # A run object (§3.14).
      "tool": {                                       # See §3.14.6.
        "driver": {
          "name": "ImageAccessibilityScanner"
        }
      },
      "externalPropertyFileReferences": {             # See §3.14.2.
        "artifacts": [
          {
            "location": {
              "uri": "sarif:/inlineExternalPropertyFiles/0"
            }
          }
        ]
      },
      "results": [
        ...
      ]
    },
    {
      "tool": {
        "driver": {
          "name": "ImageSuitabilityScanner"
        }
      },
      "externalPropertyFileReferences": {
        "artifacts": [
          {
            "guid": "00001111-2222-1111-8888-555566667777"
          }
        ]
      },
      "results": [
        ...
      ]
    }
  ]
}
```