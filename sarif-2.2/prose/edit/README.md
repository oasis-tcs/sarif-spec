# SARIF v2.2 — Authoring Reference

This is the working directory for editing and building the SARIF Version 2.2 specification.

## Folder layout

| Path | Purpose |
|------|---------|
| `bin/` | Project-specific utility scripts (do not modify without review) |
| `etc/` | Build configuration — nide.yaml, typst template, rules, LUTs |
| `src/` | Markdown source files; assembled per `etc/bind.txt` |
| `test/` | Test code for example correctness (leave as-is) |
| `build/` | Local-only build artifacts; not tracked in VCS |
| `../share/` | Publication-ready output artifacts |
| `../media/` | Shared images (OASIS logo, etc.) |

## Configuration files (`etc/`)

| File | Purpose |
|------|---------|
| `bind.txt` | Ordered list of source files for assembly |
| `nide.yaml` | nide pipeline configuration (channels, enumerations, quality) |
| `sarif.typ` | Typst template for PDF rendering |
| `oasis.typ` | Shared OASIS Typst base template |
| `tidy-config.txt` | HTML tidy configuration |
| `vale.ini` | Vale prose-linting configuration |
| `markdownlint.json` | Markdownlint configuration |
| `rules/oasis.rules.yaml` | Shared OASIS TC baseline quality rules (14 rules) |
| `rules/spec.rules.yaml` | SARIF-specific quality rules; extends oasis |
| `section-display-to-label.json` | Section display-number → label LUT |
| `section-label-to-display.json` | Section label → display-number LUT (derived) |
| `section-display-to-text.json` | Section display-number → heading text LUT |
| `example-global-to-local.json` | Example global → local number LUT |
| `example-local-to-global.json` | Example local → global number LUT (derived) |

## Utility scripts (`bin/`)

| Script | Purpose |
|--------|---------|
| `bump.py` | Bump version strings in source files |
| `png-logo-to-data-url.sh` | Convert OASIS logo PNG to inline data-URL for HTML |
| `adhoc-align-table-columns.py` | One-off: align markdown table column widths |
| `adhoc-code-block-sem-sec-refs.py` | One-off: add semantic section references in code blocks |
| `adhoc-fix-toc-labels.py` | One-off: fix ToC label anchors |
| `adhoc-semantic-cite-refs.py` | One-off: convert bare citations to semantic cite refs |
| `adhoc-semantic-sec-refs.py` | One-off: convert bare section numbers to semantic sec refs |

## Authoring loop

1. Edit source files in `src/`.
2. Run `make` to render GFM+ and HTML; check `../share/sarif-v2.2-draft.html` in a browser.
3. Run `make quality` to check spec and OASIS baseline rules.
4. Run `make pdf` to render the PDF; it opens automatically.
5. Run `make diff` to compare HTML prose against the last committed version.
6. Run `make release` when ready to publish all channels with manifest and validation.

## Build targets

### Primary targets

| Target | What it does |
|--------|-------------|
| `make` | GFM+ and HTML (default: `make build`) |
| `make gfm-plus` | Assemble IR and render GFM+ Markdown |
| `make html` | Render HTML (depends on `gfm-plus`) |
| `make pdf` | Render PDF via typst |
| `make release` | All channels + `nide manifest` + `nide validate` |

### Quality and diff targets

| Target | What it does |
|--------|-------------|
| `make quality` | Run `nide quality` against `etc/rules/spec.rules.yaml` |
| `make diff` | Prose diff of HTML against HEAD (`nide diff --mode prose`) |
| `make diff-repro` | Reproducibility diff of PDF against HEAD (`nide diff --mode repro`) |

### Utility targets

| Target | What it does |
|--------|-------------|
| `make status` | Show fossil VCS status |
| `make tree` | Show file tree, VCS changes, and verify fossil DB hash |
| `make hash` | Update BLAKE3 hash of the fossil database |
| `make dist-scm` | Hash and distribute the fossil repository |
| `make context` | Print environment and tool version info |
| `make clean` | Remove `build/` and caches |
| `make distclean` | Full clean including `build/` |

### Deprecated aliases

| Alias | Canonical |
|-------|-----------|
| `make typst` | `make pdf` |
| `make render-html` | `make html` |
| `make render-markdown` | `make gfm-plus` |
| `make render-pdf` | `make pdf` |

## Using nide quality directly

```sh
# Run with the default rules path configured in nide.yaml
nide quality

# Run with an explicit rules file
nide quality --rules etc/rules/spec.rules.yaml

# Check only OASIS baseline rules
nide quality --rules etc/rules/oasis.rules.yaml
```

## Using nide diff directly

```sh
# Prose diff (compares rendered text)
nide diff --mode prose ../share/sarif-v2.2-draft.html

# Reproducibility diff (compares binary PDF checksums)
nide diff --mode repro ../share/sarif-v2.2-draft.pdf

# Full diff (prose + meta + repro)
nide diff --mode full ../share/sarif-v2.2-draft.html
```

## Tool prerequisites

| Tool | Install | Purpose |
|------|---------|---------|
| `nide` | `pip install nide` | Spec assembly, rendering, quality, diff |
| `pandoc` | [pandoc.org](https://pandoc.org) | Markdown → HTML / Markdown → typst |
| `typst` | [typst.app](https://typst.app) | typst → PDF |
| `fossil` | [fossil-scm.org](https://fossil-scm.org) | Version control |
| `b3sum` | `cargo install b3sum` | BLAKE3 checksums |
