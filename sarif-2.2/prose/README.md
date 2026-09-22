# SARIF Version 2.2 — Prose

The `prose` folder holds the editable source and the publication-ready delivery items
for the Static Analysis Results Interchange Format (SARIF) v2.2 specification.

## Delivery channels

The `share/` folder contains four rendered artifacts:

| Channel | File | Description |
|---------|------|-------------|
| GFM+ | `sarif-v2.2-draft.md` | Single-file GitHub-flavored Markdown; renders on Codeberg, GitHub, and GitLab |
| HTML | `sarif-v2.2-draft.html` | Self-contained HTML with OASIS styling; open in any browser |
| PDF | `sarif-v2.2-draft.pdf` | Print-ready PDF via nide + pandoc + typst |
| IR | `sarif-v2.2-draft.ir.json` | Intermediate representation; input for downstream tooling |

## Building

All targets are defined in `edit/makefile`.
Run commands from the `edit/` directory.

```
make          # GFM+ and HTML (default)
make pdf      # PDF via typst
make release  # all channels + manifest + validation
make quality  # run spec and OASIS baseline quality checks
```

## Source layout

The source lives in `edit/src/` assembled per `edit/etc/bind.txt`.
See `edit/README.md` for the full authoring reference.
