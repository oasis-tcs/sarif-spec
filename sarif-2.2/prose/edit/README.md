# Place to edit the prose

Many users are used to consume online renditions of annotated text (e.g. markdown, org, restructured text) files (UX).

We keep the editor source versions separate from the online viewer optimized single file version.
This separation of concerns optimizes both the reading experience of users (UX) and supports the editors in creating traceable changes (DX). 

This way we can edit coherent and well-sized parts of the prose (which as of SARIF v2.1.0 combines to around ten thousand lines of text).
Thereby we minimize manual handling of workarounds for visual effects of the online rendition for specific processors
(like those in use at Bitbucket, Codeberg, GitHub, GitLab, or sourcehut) and can focus on the responsible evolution of the work products.

The editors ensure consistency of the prose with:

- the related SARIF schema set revision
- the examples
- other required terms and statements within the prose text

## Target formats (WIP)

The user facing delivery items of the build process are:

- hyper text markup language (HTML)
- portable document format (PDF)
- single file GitHub flavored markdown plus visual cosmetic patches (GFM+gh_cosmetics)

The developer artifacts include the user facing delivery items as well as:

- build and test reports
- developer documentation (like this document)
- example snippets of SARIF files with the additions needed to validate them

## Structure of this tree

The directory structure is:

- `bin`: any specific tools for building and testing the user documents
- `etc`: files providing context for builds and for configuring tools
- `src`: the actual source files, optimized for editing, tracing, and verification
- `test`: test code to ensure correctness of changes

**Note**: Any `build` folder in here is local-only and supports building user targeting document formats from the sources in `src`.
