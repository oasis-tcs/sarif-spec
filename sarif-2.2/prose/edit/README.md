# Place to edit the prose

Per sites like GitHub many users are used to see markdown like documents rendered directly online (UX).

We keep the editor source versions separate from the online viewer optimized single file version.
This separation of concerns optimizes both the reading experience of users (UX) and supports the editors in creating traceable changes (DX). 

This way we can slice and dice well-sized and coherent parts of the prose and minimize workarounds that enable the online rendition for specific processors (like those in use at Bitbucket, Codeberg, GitHub, GitLab, or sourcehut).

The editors will want to ensure consistency with the related SARIF schema set revision, the examples, as well as other terms and statements within the prose text of initially approx. ten thousand lines.

## Structure of this tree

In the `src` folder we keep the actual source content.

The `bin` and `etc` folders hold any tools and configuration files applicable as they become available.

Finally the `test` folder provides the tests we execute to ensure correctness of changes and minimize the occurrence of regressions.

**Note**: The `build` folder is local only and supports building user targeting document formats from the sources in `src`.
