.POSIX:
.SILENT:
.DEFAULT_GOAL = check

# SARIF vision: the schema and records/ are authored, views/ are derived from them (see VISION.md).
#   make derive   write views/ (findings, examples against the schema, statements per role), the constraint sentences,
#                 and (nide derive) the snippets of the twins
#   make check    fail when a view differs from what the sources give, or a record is incomplete
#   make prose    check, then build the specification as before (prose/edit, needs nide)
# The Python environment is the one of the repository (pyenv local in sarif-spec/): jsonschema and PyYAML.

python ?= python

.PHONY: derive check prose
derive:
	$(python) -I bin/vision.py derive
	cd prose/edit && nide derive

check:
	$(python) -I bin/vision.py check
	cd prose/edit && nide derive --check

prose: check
	$(MAKE) -C prose/edit
