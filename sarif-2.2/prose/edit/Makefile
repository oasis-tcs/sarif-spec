.DEFAULT_GOAL := build
.PHONY: build
build:
	bin/futile.py
	pandoc -f gfm+definition_lists -t html build/tmp.md --columns=345  --css style/base.css --css style/skin.css --standalone -o build/tmp.html --metadata title="Static Analysis Results Interchange Format (SARIF) Version 2.2 CSD01"
	bin/toccata.py
	timeout 2 tidy -config etc/tidy-config.txt build/injected.html -ashtml | sed 's/<!\[CDATA\[//g; s/\]\]>//g;' > ../share/sarif-v2.2-draft.html
	git status
