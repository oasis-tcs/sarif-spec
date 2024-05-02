# The SARIF 2.2 Prose Folder

This place offers access to the editable sources of the v2.2 SARIF specification (to be).

In the `share` folder there are the user facing delivery items that offer layout and navigation
optimized for online viewing per 

- a typical web interface of a version control server (like Codeberg, GitHub, GitLab, or SourceHut) - the Markdown file
- any typical browser (like Brave, Chrome, Edge, Firefox, or Safari) - the HTML file

Inside the `edit` folder we build these delivery items from the source files (also in Markdown format, but
split by concerns, verifiable per syntax, and offering clean structural constructs for definition lists etc.
instead of the specific idioms mixed in for ease of use in specific reading tools).

The `sarif-v2.2-editor-draft.md` in this folder is an intermediate file and may vanish at any point in time.

In general, we try to keep this file identical to the `share/sarif-v2.2-draft.md` file.

The latter is generated from the source files below `edit/src/` as collected per `edit/etc/bind.txt` through
the `edit/bin/volatile.py` script (for now).

The way to the HTML is a three-step process:

First calling pandoc (inside the `edit` folder) as:

```console
% pandoc -f gfm+definition_lists -t html build/tmp.md --columns=345  --css style/base.css --css style/skin.css  \
  --standalone -o build/tmp.html \
  --metadata title="Static Analysis Results Interchange Format (SARIF) Version 2.1.0 Plus Errata 01"
```

Second, swapping the hacked-up table of contents (for Markdown web-rendered views) with a real HTML one,
and connecting the skin styles to the elements (reading from the `build/tmp.html` file of the previous step):

```console
% bin/toccata.py
```

Rewrites the `build/tmp.html` pandoc auto-generated HTML file into a more OASIS alike one at `build/injected.html`. 

The third step uses tidy-html5 to cleanse the file from non-conforming content and formats.
```console
% tidy -config etc/tidy-config.txt build/injected.html -ashtml | \
  sed 's/<!\[CDATA\[//g; s/\]\]>//g;' > ../share/sarif-v2.2-draft.html
```

Note: Currently we still have 17 warnings in the third step, as the generated HTML is not conforming.
