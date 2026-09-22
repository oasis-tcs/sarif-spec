# SARIF v2.2 — Delivery Artifacts

This folder contains the publication-ready artifacts built from the sources in `../edit/`.

## Artifacts

| File | Description |
|------|-------------|
| `sarif-v2.2-draft.md` | GFM+ single-file Markdown |
| `sarif-v2.2-draft.html` | Self-contained HTML with OASIS styling |
| `sarif-v2.2-draft.ir.json` | Intermediate representation (nide IR) |
| `sarif-v2.2-draft.manifest.json` | Content manifest with per-channel hashes |
| `sarif-v2.2-draft.pdf` | PDF |
| `sarif-v2.2-draft.pdf.sha256` | SHA-256 checksum of the PDF |
| `sarif-v2.2-draft.pdf.blake3` | BLAKE3 checksum of the PDF |
| `sarif-v2.2-draft.typ` | Typst source (input used to produce the PDF) |

## Verifying checksums

```sh
# SHA-256
shasum -a 256 --check sarif-v2.2-draft.pdf.sha256

# BLAKE3 (requires b3sum)
b3sum --check sarif-v2.2-draft.pdf.blake3
```

## Building

Run from the `../edit/` directory:

```sh
make          # GFM+ and HTML
make pdf      # PDF
make release  # all channels + manifest + validate
```

## Comparing versions

```sh
# Prose diff of the HTML against the last committed version
nide diff --mode prose sarif-v2.2-draft.html

# Reproducibility diff of the PDF
nide diff --mode repro sarif-v2.2-draft.pdf
```
