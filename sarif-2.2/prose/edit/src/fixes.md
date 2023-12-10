<!--
---
toc:
  auto: false
  label: (Informative) Guidance on fixes
  enumerate: Appendix G.
---
-->
# (Informative) Guidance on fixes

Tools that produce SARIF files which include `fix` objects should take care to structure those fixes in such a way as to affect a minimal range of content. This maximizes the likelihood that an automated tool can safely apply multiple fixes to the same artifact.

The following example will clarify what this means and why it is important. Consider an XML file containing the following element:

    <lineItem partNumber=A3101 />

Suppose that a (domain-specific) XML scanning tool reported two results:

- The value of the `partNumber` attribute is not enclosed in quotes.

- The part numbering scheme has changed, and part numbers beginning with "`A`" now begin with "`AA`".

Fixing only result #1 would produce the element

    <lineItem partNumber="A3101" />

Fixing only result #2 would produce the element

    <lineItem partNumber=AA3101 />

Fixing both results should produce the element

    <lineItem partNumber="AA3101" />

The fix for result #1 might be specified in various ways, for example:

1.  As a single replacement:

    - Replace the characters `A3101` with the characters `"A3101"`.

2.  As a sequence of two replacements:

    a. Insert a quotation mark before `A3101`.

    b. Insert a quotation mark after `A3101`.

The fix for result #2 is most simply specified as a single replacement:

- Replace the characters `A3101` with the characters `AA3101`.

Suppose there exists an automated tool which reads a SARIF file containing `fix` objects and applies as many of the specified fixes as possible to the source files.

If the fix for result #1 were structured as a single replacement, then after applying the fix, the tool would not be able to fix result #2, because the range of characters specified by the fix for result #2 would have been replaced. On the other hand, if the fix for result #1 were structured as two replacements (with a separate insertion for each quotation mark), the tool would still be able to apply the fix for result #2, because the targeted range of characters would still exist.

Therefore, structuring fixes as sequences of minimal, disjoint replacements maximizes the amount of work that can be done by automated fixup tools.
