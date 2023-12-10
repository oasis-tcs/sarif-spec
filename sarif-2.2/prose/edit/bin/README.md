# Notes on tools

Before committing changes to the python files in here, please ensure the following commands succeed:

  + mypy $FILE (for type verification)
  + ruff --ignore E501 $FILE (for general linting)
  + black -S -l120 $FILE (for 120 lines and single quotes preferred format)
  + vale --config ../etc/vale.ini $FILE (developer documentation spell check)

Also processing the test fixtures in the adhoc subtree shall align with use and abuse accordingly:

```console
❯ {for f in $(find test/fixtures/adhoc/use | grep "\.md$"); do bin/adhoc-align-table-columns.py $f; done} 2>&1 | cut -f2- -d ' '
INFO [tabla]: document with aligned tables written to build/empty-header-single-gfm-table.md
INFO [tabla]: document with aligned tables written to build/misaligned-single-gfm-table.md
INFO [tabla]: document with aligned tables written to build/misaligned-two-gfm-tables.md
```

```console
❯ {for f in $(find test/fixtures/adhoc/abuse | grep "\.md$"); do bin/adhoc-align-table-columns.py $f; done} 2>&1 | cut -f2- -d ' '
ERROR [tabla]: expected either table, blank line, or end of file but found non-blank line in location(missing-post-table-blank-line-single-gfm-table.md:4@table[4]) -> (       some text and no blank line following the table lines.)
ERROR [tabla]: expected either table, blank line, or end of file but found column separator (|) in location(misplaced-table-line-single-gfm-table.md:6@table[6]) -> ( | 46|)
ERROR [tabla]: expected cols(2) but found cols(1) in location(mismatch-columns-too-few-two-gfm-tables.md:5@table[4]) -> (| one too few|)
ERROR [tabla]: expected cols(2) but found cols(1) in location(mismatch-columns-too-few-single-gfm-table.md:5@table[4]) -> (| one too few|)
ERROR [tabla]: expected 1 separator line but found 0 in location(missing-separator-line-single-gfm-table.md:3@table[2]) -> (no separator line detected)
ERROR [tabla]: expected cols(1) but found cols(2) in location(mismatch-columns-too-many-two-gfm-tables.md:5@table[4]) -> (|| one too many|)
ERROR [tabla]: expected 1 separator line but found 2 in location(too-many-separator-lines-single-gfm-table.md:5@table[4]) -> (ambiguous separator lines detected)
ERROR [tabla]: expected cols(1) but found cols(2) in location(mismatch-columns-too-many-single-gfm-table.md:5@table[4]) -> (|| one too many|)
```

Last, but not least, the source files for the prose shall pass (if they do not, the error might be in the markdown files).

As of 2023-AUG-01 all source markdown files do pass the table test:

```console
❯ {for f in src/*.md; do bin/adhoc-align-table-columns.py $f; done} 2>&1 | cut -f2- -d ' '
INFO [tabla]: document with aligned tables written to build/acknowledgements.md
INFO [tabla]: document with aligned tables written to build/changelog.md
INFO [tabla]: document with aligned tables written to build/conformance.md
INFO [tabla]: document with aligned tables written to build/conventions.md
INFO [tabla]: document with aligned tables written to build/converters.md
INFO [tabla]: document with aligned tables written to build/detecting-incompleteness.md
INFO [tabla]: document with aligned tables written to build/deterministic.md
INFO [tabla]: document with aligned tables written to build/diagnosing-results.md
INFO [tabla]: document with aligned tables written to build/endnotes.md
INFO [tabla]: document with aligned tables written to build/examples.md
INFO [tabla]: document with aligned tables written to build/external-property-file-format.md
INFO [tabla]: document with aligned tables written to build/file-format-00.md
INFO [tabla]: document with aligned tables written to build/file-format-01-general.md
INFO [tabla]: document with aligned tables written to build/file-format-02-sarif-file-naming-convention.md
INFO [tabla]: document with aligned tables written to build/file-format-03-artifactcontent-object.md
INFO [tabla]: document with aligned tables written to build/file-format-04-artifactlocation-object.md
INFO [tabla]: document with aligned tables written to build/file-format-05-string-properties.md
INFO [tabla]: document with aligned tables written to build/file-format-06-object-properties.md
INFO [tabla]: document with aligned tables written to build/file-format-07-array-properties.md
INFO [tabla]: document with aligned tables written to build/file-format-08-property-bags.md
INFO [tabla]: document with aligned tables written to build/file-format-09-datetime-properties.md
INFO [tabla]: document with aligned tables written to build/file-format-10-uri-valued-properties.md
INFO [tabla]: document with aligned tables written to build/file-format-11-message-object.md
INFO [tabla]: document with aligned tables written to build/file-format-12-multiformatmessagestring-object.md
INFO [tabla]: document with aligned tables written to build/file-format-13-sariflog-object.md
INFO [tabla]: document with aligned tables written to build/file-format-14-run-object.md
INFO [tabla]: document with aligned tables written to build/file-format-15-externalpropertyfilereferences-object.md
INFO [tabla]: document with aligned tables written to build/file-format-16-externalpropertyfilereference-object.md
INFO [tabla]: document with aligned tables written to build/file-format-17-runautomationdetails-object.md
INFO [tabla]: document with aligned tables written to build/file-format-18-tool-object.md
INFO [tabla]: document with aligned tables written to build/file-format-19-toolcomponent-object.md
INFO [tabla]: document with aligned tables written to build/file-format-20-invocation-object.md
INFO [tabla]: document with aligned tables written to build/file-format-21-attachment-object.md
INFO [tabla]: document with aligned tables written to build/file-format-22-conversion-object.md
INFO [tabla]: document with aligned tables written to build/file-format-23-versioncontroldetails-object.md
INFO [tabla]: document with aligned tables written to build/file-format-24-artifact-object.md
INFO [tabla]: document with aligned tables written to build/file-format-25-speciallocations-object.md
INFO [tabla]: document with aligned tables written to build/file-format-26-translationmetadata-object.md
INFO [tabla]: document with aligned tables written to build/file-format-27-result-object.md
INFO [tabla]: document with aligned tables written to build/file-format-28-location-object.md
INFO [tabla]: document with aligned tables written to build/file-format-29-physicallocation-object.md
INFO [tabla]: document with aligned tables written to build/file-format-30-region-object.md
INFO [tabla]: document with aligned tables written to build/file-format-31-rectangle-object.md
INFO [tabla]: document with aligned tables written to build/file-format-32-address-object.md
INFO [tabla]: document with aligned tables written to build/file-format-33-logicallocation-object.md
INFO [tabla]: document with aligned tables written to build/file-format-34-locationrelationship-object.md
INFO [tabla]: document with aligned tables written to build/file-format-35-suppression-object.md
INFO [tabla]: document with aligned tables written to build/file-format-36-codeflow-object.md
INFO [tabla]: document with aligned tables written to build/file-format-37-threadflow-object.md
INFO [tabla]: document with aligned tables written to build/file-format-38-threadflowlocation-object.md
INFO [tabla]: document with aligned tables written to build/file-format-39-graph-object.md
INFO [tabla]: document with aligned tables written to build/file-format-40-node-object.md
INFO [tabla]: document with aligned tables written to build/file-format-41-edge-object.md
INFO [tabla]: document with aligned tables written to build/file-format-42-graphtraversal-object.md
INFO [tabla]: document with aligned tables written to build/file-format-43-edgetraversal-object.md
INFO [tabla]: document with aligned tables written to build/file-format-44-stack-object.md
INFO [tabla]: document with aligned tables written to build/file-format-45-stackframe-object.md
INFO [tabla]: document with aligned tables written to build/file-format-46-webrequest-object.md
INFO [tabla]: document with aligned tables written to build/file-format-47-webresponse-object.md
INFO [tabla]: document with aligned tables written to build/file-format-48-resultprovenance-object.md
INFO [tabla]: document with aligned tables written to build/file-format-49-reportingdescriptor-object.md
INFO [tabla]: document with aligned tables written to build/file-format-50-reportingconfiguration-object.md
INFO [tabla]: document with aligned tables written to build/file-format-51-configurationoverride-object.md
INFO [tabla]: document with aligned tables written to build/file-format-52-reportingdescriptorreference-object.md
INFO [tabla]: document with aligned tables written to build/file-format-53-reportingdescriptorrelationship-object.md
INFO [tabla]: document with aligned tables written to build/file-format-54-toolcomponentreference-object.md
INFO [tabla]: document with aligned tables written to build/file-format-55-fix-object.md
INFO [tabla]: document with aligned tables written to build/file-format-56-artifactchange-object.md
INFO [tabla]: document with aligned tables written to build/file-format-57-replacement-object.md
INFO [tabla]: document with aligned tables written to build/file-format-58-notification-object.md
INFO [tabla]: document with aligned tables written to build/file-format-59-exception-object.md
INFO [tabla]: document with aligned tables written to build/fingerprints.md
INFO [tabla]: document with aligned tables written to build/fixes.md
INFO [tabla]: document with aligned tables written to build/frontmatter.md
INFO [tabla]: document with aligned tables written to build/introduction-00.md
INFO [tabla]: document with aligned tables written to build/introduction-01-ipr-policy.md
INFO [tabla]: document with aligned tables written to build/introduction-02-terminology.md
INFO [tabla]: document with aligned tables written to build/introduction-03-normative-references.md
INFO [tabla]: document with aligned tables written to build/introduction-04-informative-references.md
INFO [tabla]: document with aligned tables written to build/introduction-05-trademarks.md
INFO [tabla]: document with aligned tables written to build/locating-metadata.md
INFO [tabla]: document with aligned tables written to build/mime-types.md
INFO [tabla]: document with aligned tables written to build/source-language-examples.md
INFO [tabla]: document with aligned tables written to build/viewers.md
```
