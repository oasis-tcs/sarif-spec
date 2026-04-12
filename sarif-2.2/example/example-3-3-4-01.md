### 3.3.4 rendered property

An artifactContent object MAY contain a property named rendered whose value is a multiformatMessageString object (§3.12) that provides a rendered view of the contents.

EXAMPLE: In this example, a physicalLocation object (§3.29) denotes a memory address. Its region.snippet.rendered property (§3.29.4, §3.30.13) offers a hex view of the relevant address range. The markdown property (§3.12.4) emphasizes a byte of particular interest.

```{label=example-3-3-4-01}
{                                # A physicalLocation object (§3.29).
  "address": {                   # See §3.29.6.
    "baseAddress": 4202880,      # See §3.32.6.
    "offset": 64                 # See §3.32.8.
  },

 
  "region": {                    # See §3.29.4.
    "snippet": {                 # An artifactContent object. See §3.30.13.
      "rendered": {              # A multiformatMessageString object (§3.12).
        "text": "00 00 01 00 00 00 00 00",
        "markdown": "00 00 **01** 00 00 00 00 00"
      }
    }
  }
}
```
