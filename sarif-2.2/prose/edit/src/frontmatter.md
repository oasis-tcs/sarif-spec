![OASIS Logo](https://docs.oasis-open.org/templates/OASISLogo-v3.0.png)

-------

# Static Analysis Results Interchange Format (SARIF) Version 2.2

## Committee Specification Draft 01

## 05 February 2026

### This stage:
https://docs.oasis-open.org/sarif/sarif/v2.2/csd01/sarif-v2.2-csd01.md (Authoritative) \
https://docs.oasis-open.org/sarif/sarif/v2.2/csd01/sarif-v2.2-csd01.html \
https://docs.oasis-open.org/sarif/sarif/v2.2/csd01/sarif-v2.2-csd01.pdf

#### Previous stage:
N/A

#### Latest stage:
https://docs.oasis-open.org/sarif/sarif/v2.2/sarif-v2.2.md (Authoritative) \
https://docs.oasis-open.org/sarif/sarif/v2.2/sarif-v2.2.html \
https://docs.oasis-open.org/sarif/sarif/v2.2/sarif-v2.2.pdf

#### Technical Committee:
[OASIS Static Analysis Results Interchange Format (SARIF) TC](https://www.oasis-open.org/committees/sarif/)

#### Chairs:
Aditya Sharad (<adityasharad@github.com>), Microsoft Corporation \
Stefan Hagen (<stefan@hagen.link>), [Individual](https://stefan-hagen.website)

#### Editors:
Michael Fanning (<michael.fanning@microsoft.com>), [Microsoft Corporation](https://www.microsoft.com/) \
Stefan Hagen (<stefan@hagen.link>), [Individual](https://stefan-hagen.website)

#### Additional artifacts:
This prose specification is one component of a Work Product that also includes:

* SARIF schema: https://docs.oasis-open.org/sarif/sarif/v2.2/csd01/schema/sarif.json. \
  Latest stage: https://docs.oasis-open.org/sarif/sarif/v2.2/schema/sarif.json
* SARIF External Property File schema: https://docs.oasis-open.org/sarif/sarif/v2.2/csd01/schema/sarif-external-property-file-schema-2.2.json. \
  Latest stage: https://docs.oasis-open.org/sarif/sarif/v2.2/schema/sarif-external-property-file-schema-2.2.json

#### Related work:
This specification replaces or supersedes:

_Static Analysis Results Interchange Format (SARIF) Version 2.1.0 Plus Errata 01_. Edited by Michael C. Fanning and Laurence J. Golding. 12 July 2023. OASIS Standard incorporating Approved Errata. https://docs.oasis-open.org/sarif/sarif/v2.1.0/errata01/os/sarif-v2.1.0-errata01-os-complete.html. Latest stage: https://docs.oasis-open.org/sarif/sarif/v2.1.0/sarif-v2.1.0.html.

#### Abstract:
This document defines a standard format for the output of static analysis tools. The format is referred to as the "Static Analysis Results Interchange Format" and is abbreviated as SARIF.

#### Status:
This document was last revised or approved by the OASIS Static Analysis Results Interchange Format (SARIF) TC on the above date. The level of approval is also listed above. Check the "Latest stage" location noted above for possible later revisions of this document. Any other numbered Versions and other technical work produced by the Technical Committee (TC) are listed at <https://www.oasis-open.org/committees/tc_home.php?wg_abbrev=sarif#technical>.

TC members should send comments on this document to the TC's email list. Others should send comments to the TC's public comment list, after subscribing to it by following the instructions at the "[Send A Comment](https://www.oasis-open.org/committees/comments/index.php?wg_abbrev=sarif)" button on the TC's web page at <https://www.oasis-open.org/committees/sarif/>.

This specification is provided under the [RF on RAND Terms](https://www.oasis-open.org/policies-guidelines/ipr/#RF-on-RAND-Mode) Mode of the [OASIS IPR Policy](https://www.oasis-open.org/policies-guidelines/ipr/), the mode chosen when the Technical Committee was established. For information on whether any patents have been disclosed that may be essential to implementing this specification, and any offers of patent licensing terms, please refer to the Intellectual Property Rights section of the TC's web page (<https://www.oasis-open.org/committees/sarif/ipr.php>).

Note that any machine-readable content ([Computer Language Definitions](https://www.oasis-open.org/policies-guidelines/tc-process/#wpComponentsCompLang)) declared Normative for this Work Product is provided in separate plain text files. In the event of a discrepancy between any such plain text file and display content in the Work Product's prose narrative document(s), the content in the separate plain text file prevails.

#### Citation format:
When referencing this specification, the following citation format should be used:

**\[SARIF-v2.2\]**

_Static Analysis Results Interchange Format (SARIF) Version 2.2_. Edited by Michael Fanning and Stefan Hagen. 05 February 2026. Committees Specification Draft. https://docs.oasis-open.org/sarif/sarif/v2.2/csd01/sarif-v2.2-csd01.html. Latest stage: https://docs.oasis-open.org/sarif/sarif/v2.2/sarif-v2.2.html.


-------

## Notices

Copyright © OASIS Open 2026. All Rights Reserved.

All capitalized terms in the following text have the meanings assigned to them in the OASIS Intellectual Property Rights Policy (the "OASIS IPR Policy"). The full [Policy](https://www.oasis-open.org/policies-guidelines/ipr/) may be found at the OASIS website.

This document and translations of it may be copied and furnished to others, and derivative works that comment on or otherwise explain it or assist in its implementation may be prepared, copied, published, and distributed, in whole or in part, without restriction of any kind, provided that the above copyright notice and this section are included on all such copies and derivative works. However, this document itself may not be modified in any way, including by removing the copyright notice or references to OASIS, except as needed for the purpose of developing any document or deliverable produced by an OASIS Technical Committee (in which case the rules applicable to copyrights, as set forth in the OASIS IPR Policy, must be followed) or as required to translate it into languages other than English.

The limited permissions granted above are perpetual and will not be revoked by OASIS or its successors or assigns.

This document and the information contained herein is provided on an "AS IS" basis and OASIS DISCLAIMS ALL WARRANTIES, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO ANY WARRANTY THAT THE USE OF THE INFORMATION HEREIN WILL NOT INFRINGE ANY OWNERSHIP RIGHTS OR ANY IMPLIED WARRANTIES OF MERCHANTABILITY OR FITNESS FOR A PARTICULAR PURPOSE.

OASIS requests that any OASIS Party or any other party that believes it has patent claims that would necessarily be infringed by implementations of this OASIS Committee Specification or OASIS Standard, to notify OASIS TC Administrator and provide an indication of its willingness to grant patent licenses to such patent claims in a manner consistent with the IPR Mode of the OASIS Technical Committee that produced this specification.

OASIS invites any party to contact the OASIS TC Administrator if it is aware of a claim of ownership of any patent claims that would necessarily be infringed by implementations of this specification by a patent holder that is not willing to provide a license to such patent claims in a manner consistent with the IPR Mode of the OASIS Technical Committee that produced this specification. OASIS may include such claims on its website, but disclaims any obligation to do so.

OASIS takes no position regarding the validity or scope of any intellectual property or other rights that might be claimed to pertain to the implementation or use of the technology described in this document or the extent to which any license under such rights might or might not be available; neither does it represent that it has made any effort to identify any such rights. Information on OASIS' procedures with respect to rights in any document or deliverable produced by an OASIS Technical Committee can be found on the OASIS website. Copies of claims of rights made available for publication and any assurances of licenses to be made available, or the result of an attempt made to obtain a general license or permission for the use of such proprietary rights by implementers or users of this OASIS Committee Specification or OASIS Standard, can be obtained from the OASIS TC Administrator. OASIS makes no representation that any information or list of intellectual property rights will at any time be complete, or that any claims in such list are, in fact, Essential Claims.

The name "OASIS" is a trademark of [OASIS](https://www.oasis-open.org/), the owner and developer of this specification, and should be used only to refer to the organization and its official outputs. OASIS welcomes reference to, and implementation and use of, specifications, while reserving the right to enforce its marks against misleading uses. Please see <https://www.oasis-open.org/policies-guidelines/trademark/> for above guidance.
