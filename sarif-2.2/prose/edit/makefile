.POSIX:
.SILENT:
.DEFAULT_GOAL = build

pyversion = py314
linelength = 120
black = black -S -l $(linelength) --target-version $(pyversion) --quiet bin
lint = ruff check bin
types = mypy bin
OPEN ?= open

shared = ../share/
artifact_stem = sarif-v2.2-draft

target_gfm_plus = gfm-plus

out_html          = $(shared)$(artifact_stem).html
out_gfm_plus      = $(shared)$(artifact_stem).md
out_ir            = $(shared)$(artifact_stem).ir.json
out_manifest      = $(shared)$(artifact_stem).manifest.json
out_pdf           = $(shared)$(artifact_stem).pdf
out_pdf_sha256    = $(shared)$(artifact_stem).pdf.sha256
out_pdf_blake3    = $(shared)$(artifact_stem).pdf.blake3
out_typst         = $(shared)$(artifact_stem).typ

.PHONY: all
all: lint types build

.PHONY: format
format:
	command -v ruff >/dev/null 2>&1 || { echo >&2 "make format requires ruff but it's not installed - you can install with: 'pip install ruff'.  Aborting."; exit 1; }
	$(lint) --fix
	command -v black >/dev/null 2>&1 || { echo >&2 "make format requires black but it's not installed - you can install with: 'pip install black'.  Aborting."; exit 1; }
	$(black)

.PHONY: lint
lint:
	$(lint) --diff
	$(black) --check --diff
	command -v unmake >/dev/null 2>&1 || { echo >&2 "make lint requires unmake but it's not installed - you can install with: 'cargo install unmake'.  Aborting."; exit 1; }
	-unmake makefile

.PHONY: types
types:
	command -v mypy >/dev/null 2>&1 || { echo >&2 "make types requires mypy but it's not installed - you can install with: 'pip install mypy'.  Aborting."; exit 1; }
	$(types)

.PHONY: render
render: html

.PHONY: sections
sections:
	command -v nide >/dev/null 2>&1 || { echo >&2 "make sections requires nide but it's not installed - you can install with: 'pip install nide'.  Aborting."; exit 1; }
	nide harvest

.PHONY: gfm-plus
gfm-plus: sections
	nide assemble && \
	  cp -p build/ir.json $(out_ir) && \
	  nide render -t $(target_gfm_plus) && \
	  cp -p build/gfm-plus.md $(out_gfm_plus) && \
	  printf "Rendered markdown:\n" && \
	  ls -l $(out_gfm_plus)

.PHONY: html
html: gfm-plus
	command -v pandoc >/dev/null 2>&1 || { echo >&2 "make html requires pandoc but it's not installed - you can get help on installing at https://pandoc.org.  Aborting."; exit 1; }
	nide render -t html && \
	  pandoc -f gfm+definition_lists -t html build/html.md --columns=345 \
	  --css style/base.css --css style/skin.css --standalone -o build/pandoc.html && \
	  nide inject && \
	  cp -p build/injected.html $(out_html) && \
	  printf "Rendered html:\n" && \
	  ls -l $(out_html)

.PHONY: pdf
pdf:
	nide assemble && nide render -t typst
	mkdir -p build/images
	cp ../media/OASISLogo-v3.0.png build/images/
	pandoc -f markdown+definition_lists -t typst --standalone \
	  --template etc/sarif.typ --lua-filter build/nide-columns.lua \
	  build/typst.md -o build/typst.typ
	typst compile --root . build/typst.typ build/sarif-typst.pdf
	cp -p build/sarif-typst.pdf $(out_pdf)
	cp -p build/typst.typ $(out_typst)
	shasum -a 256 $(out_pdf) > $(out_pdf_sha256)
	{ command -v b3sum >/dev/null 2>&1 && b3sum $(out_pdf) > $(out_pdf_blake3); } || \
	  printf "b3sum not found — skipping blake3 checksum\n"
	$(OPEN) $(out_pdf)

.PHONY: release
release: html pdf
	nide manifest && nide validate
	cp -p build/manifest.json $(out_manifest)
	ls -l $(shared)$(artifact_stem).*

.PHONY: quality
quality:
	nide quality

.PHONY: diff
diff:
	nide diff --mode prose $(out_html) || true

.PHONY: diff-repro
diff-repro:
	nide diff --mode repro $(out_pdf) || true

.PHONY: build
build: render status

.PHONY: status
status:
	printf "Current version control status:\n"; \
	git status || true

.PHONY: clean
clean:
	rm -rf `find . -name __pycache__`
	rm -f `find . -type f -name '*.py[co]' `
	rm -f `find . -type f -name '*~' `
	rm -f `find . -type f -name '.*~' `
	rm -rf .cache .*_cache
	rm -f .DS_Store
	rm -fr build/
	mkdir -p build/

.PHONY: distclean
distclean: clean
	rm -fr build/



.PHONY: context
context:
	printf "Clone-info:\n"
	printf "%s name.is(): '%s'\n" "-" "$$(basename `git rev-parse --show-toplevel`)"
	printf "%s branch.is(): '%s'\n" "-" "$$(git branch --show-current)"
	printf "%s revision.is(): sha1:%s\n" "-" "$$(git rev-parse HEAD)"
	printf "%s location.is(): %s\n" "-" "$$(python -c "(lambda _Y: (lambda _mod: (lambda Path: (lambda g: [(lambda x: [(lambda c, p: (lambda _loop1: _loop1(c, p))(_Y(lambda _loop1: (lambda c, p: ([_loop1(c, p) for (p, c) in [x(p, c, g)]][0]) if (c != p) and (str(c) != '/') else print((f\"(orga/repo='{c.parent.name}/{c.name}', rel-path='{o.relative_to(c)}')\" if (c == p) else \"(orga/repo='?/?', rel-path='?')\"))))))(c if 'c' in dir() else None, p if 'p' in dir() else None) for (_, c) in [x(p, c, g)]][0])(lambda p, c, g: (c, c.parent if not (c / g).is_dir() else c)) for o, p, c in [[Path().resolve()] * 3]][0])('.git'))(_mod.Path))(__import__('pathlib', {}, {}, ['Path'])))((lambda f: (lambda x: x(x))(lambda y: f(lambda *args: y(y)(*args)))))")"
	printf "%s node.id(): '%s'\n" "-" "$$(python -c 'import platform; import uuid; print(str(uuid.uuid3(uuid.NAMESPACE_DNS, platform.node())))')"

.PHONY: name  # Deprecated - backwards compatibility target
name: context

.PHONY: whoami  # Deprecated - backwards compatibility target
whoami: context

.PHONY: typst  # Deprecated - use pdf
typst: pdf

.PHONY: render-html  # Deprecated - backwards compatibility target
render-html: html

.PHONY: render-markdown  # Deprecated - backwards compatibility target
render-markdown: gfm-plus

.PHONY: render-pdf  # Deprecated - backwards compatibility target
render-pdf: pdf
