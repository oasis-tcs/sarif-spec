# Examples: the twins against the schema

Derived by `bin/vision.py derive` from `records/examples.yaml`, the twins and the schema; do not edit.
Each twin is validated as its host definition after its markers are removed and the context the schema
requires is injected (`injected` counts those members). What remains is what the example says about SARIF.

101 of 120 twins are valid this way.
81 of 120 twins say the same as a JSON code block of their prose file
(layout, commas, margin notes and markers aside): those snippets can be derived from their twins without a
change of content. The others differ: one of the two drifted, or a notation is not yet normalised.

| Twin | Host | Injected | Result | Prose snippet |
|---|---|---:|---|---|
| `diagnosing-results_example-1.json` | run | 1 | valid | same |
| `diagnosing-results_example-2.json` | run | 1 | valid | same |
| `diagnosing-results_example-3.json` | run | 1 | valid | same |
| `examples_comprehensive-sarif-file_codeblock-json-1.sarif.json` | sarifLog | 1 | 2 error(s), see findings | differs |
| `examples_minimal-recommended-sarif-log-file-with-source-information_codeblock-json-1.sarif.json` | sarifLog | 0 | valid | same |
| `examples_minimal-recommended-sarif-log-file-without-source-information_codeblock-json-1.sarif.json` | sarifLog | 0 | valid | same |
| `examples_minimal-valid-sarif-log-file_codeblock-json-1.sarif.json` | sarifLog | 0 | valid | same |
| `external-property-file-format_externalproperties-object_general_example-1.json` | externalProperties | 0 | 1 error(s), see findings | same |
| `file-format-03-artifactcontent-object_rendered-property_example-1.json` | physicalLocation | 1 | 1 error(s), see findings | same |
| `file-format-04-artifactlocation-object_description-property_example-1.json` | run | 1 | valid | same |
| `file-format-04-artifactlocation-object_guidance-on-the-use-of-artifactlocation-objects_example-1.json` | run | 2 | valid | same |
| `file-format-04-artifactlocation-object_index-property_example-1.json` | run | 2 | valid | same |
| `file-format-04-artifactlocation-object_uribaseid-property_example-2.json` | artifactChange | 1 | valid | differs |
| `file-format-05-string-properties_versioned-hierarchical-strings_example-1.json` | result | 1 | valid | same |
| `file-format-08-property-bags_tags_general_example-2.json` | run | 1 | valid | same |
| `file-format-08-property-bags_tags_tag-metadata_example-1.json` | artifact | 0 | valid | same |
| `file-format-08-property-bags_tags_tag-metadata_example-2.json` | run | 1 | valid | same |
| `file-format-11-message-object_messages-with-embedded-links_example-2.json` | result | 2 | 2 error(s), see findings | same |
| `file-format-11-message-object_messages-with-placeholders_example-2.json` | run | 1 | valid | same |
| `file-format-13-sariflog-object_general_example-1.json` | sarifLog | 0 | valid | differs |
| `file-format-13-sariflog-object_inlineexternalproperties-property_example-1.json` | sarifLog | 0 | valid | differs |
| `file-format-14-run-object_artifacts-property_example-1.json` | run | 1 | valid | differs |
| `file-format-14-run-object_general_example-1.json` | run | 1 | valid | differs |
| `file-format-14-run-object_logicallocations-property_example-1.json` | run | 1 | valid | differs |
| `file-format-14-run-object_newlinesequences-property_example-2.json` | run | 1 | valid | differs |
| `file-format-14-run-object_originaluribaseIds-property_example-1.json` | run | 1 | valid | differs |
| `file-format-14-run-object_originaluribaseIds-property_example-2.json` | run | 2 | valid | same |
| `file-format-14-run-object_redactiontokens-property_example-1.json` | run | 1 | 1 error(s), see findings | same |
| `file-format-14-run-object_versioncontrolprovenance-property_example-1.json` | run | 1 | valid | same |
| `file-format-15-externalpropertyfilereferences-object_properties_example-1.json` | run | 1 | valid | same |
| `file-format-15-externalpropertyfilereferences-object_properties_example-2.json` | run | 1 | valid | same |
| `file-format-15-externalpropertyfilereferences-object_properties_example-3.json` | run | 1 | valid | same |
| `file-format-17-runautomationdetails-object_general_example-1.json` | run | 1 | valid | same |
| `file-format-18-tool-object_general_example-1.json` | tool | 0 | valid | same |
| `file-format-19-toolcomponent-object_globalmessagestrings-property_example-1.json` | tool | 1 | valid | differs |
| `file-format-19-toolcomponent-object_minimumrequiredlocalizeddatasemanticversion-property_example-1.json` | run | 1 | valid | same |
| `file-format-19-toolcomponent-object_notifications-property_example-1.json` | tool | 1 | 4 error(s), see findings | differs |
| `file-format-19-toolcomponent-object_policies_example-1.json` | run | 0 | valid | same |
| `file-format-19-toolcomponent-object_rules-property_example-1.json` | tool | 0 | valid | differs |
| `file-format-19-toolcomponent-object_supportedtaxonomies-property_example-1.json` | run | 0 | valid | same |
| `file-format-19-toolcomponent-object_taxa-property_example-1.json` | toolComponent | 0 | valid | same |
| `file-format-19-toolcomponent-object_taxonomies_example-1.json` | run | 0 | malformed marker: `member-insert`, `member-inject` | differs |
| `file-format-19-toolcomponent-object_translations_example-1.json` | run | 0 | valid | same |
| `file-format-20-invocation-object_executionsuccessful-property_example-1.json` | invocation | 0 | valid | same |
| `file-format-20-invocation-object_exitcodedescription-property_example-1.json` | invocation | 1 | valid | same |
| `file-format-20-invocation-object_exitcodedescription-property_example-2.json` | invocation | 1 | valid | same |
| `file-format-20-invocation-object_exitsignalnumber-property_example-1.json` | invocation | 1 | valid | same |
| `file-format-20-invocation-object_processstartfailuremessage-property_example-1.json` | invocation | 1 | valid | same |
| `file-format-20-invocation-object_responsefiles-property_example-1.json` | invocation | 1 | valid | same |
| `file-format-20-invocation-object_toolconfigurationnotifications-property_example-1.json` | invocation | 2 | 1 error(s), see findings | differs |
| `file-format-20-invocation-object_toolconfigurationnotifications-property_example-2.json` | invocation | 1 | valid | differs |
| `file-format-20-invocation-object_toolconfigurationnotifications-property_example-3.json` | invocation | 1 | valid | differs |
| `file-format-21-attachment-object_general_example-1.json` | result | 2 | 1 error(s), see findings | same |
| `file-format-22-conversion-object_general_example-1.json` | sarifLog | 1 | malformed marker: `...item-inject` | differs |
| `file-format-23-versioncontroldetails-object_mappedto-property_example-1.json` | run | 2 | valid | same |
| `file-format-24-artifact-object_encoding-property_example-1.json` | run | 1 | valid | same |
| `file-format-24-artifact-object_hashes-property_example-1.json` | artifact | 0 | valid | same |
| `file-format-24-artifact-object_parentindex-property_example-1.json` | run | 1 | valid | differs |
| `file-format-25-speciallocations-object_displaybase-property_example-1.json` | run | 1 | valid | same |
| `file-format-26-translationmetadata-object_general_example-1.json` | toolComponent | 0 | valid | same |
| `file-format-27-result-object_analysistarget-property_example-1.json` | result | 1 | valid | same |
| `file-format-27-result-object_fingerprints-property_example-1.json` | result | 1 | valid | same |
| `file-format-27-result-object_fingerprints-property_example-2.json` | run | 3 | valid | same |
| `file-format-27-result-object_kind-property_example-1.json` | run | 3 | 2 error(s), see findings | differs |
| `file-format-27-result-object_level-property_example-1.json` | run | 2 | 1 error(s), see findings | differs |
| `file-format-27-result-object_message-property_example-1.json` | run | 1 | valid | differs |
| `file-format-27-result-object_message-property_example-2.json` | run | 0 | valid | same |
| `file-format-27-result-object_partialfingerprints-property_example-1.json` | result | 1 | valid | same |
| `file-format-27-result-object_partialfingerprints-property_example-2.json` | run | 3 | valid | same |
| `file-format-27-result-object_partialfingerprints-property_example-3.json` | result | 1 | valid | same |
| `file-format-27-result-object_partialfingerprints-property_example-4.json` | result | 1 | valid | same |
| `file-format-27-result-object_relatedlocations-property_example-1.json` | run | 3 | 6 error(s), see findings | differs |
| `file-format-27-result-object_ruleid-property_example-1.json` | run | 3 | valid | same |
| `file-format-27-result-object_taxa-property_example-1.json` | run | 1 | malformed marker: `...member-inkect`, `...member-inkect`, `...member-inkect`, `...member-inkect`, `...member-inkect` | same |
| `file-format-28-location-object_annotations-property_example-1.json` | location | 0 | valid | differs |
| `file-format-29-physicallocation-object_contextregion-property_example-1.json` | result | 1 | valid | same |
| `file-format-29-physicallocation-object_region-property_example-1.json` | result | 1 | valid | same |
| `file-format-32-address-object_parent-child-relationships_example-1.json` | run | 1 | valid | same |
| `file-format-33-logicallocation-object_decoratedname-property_example-1.json` | logicalLocation | 0 | valid | same |
| `file-format-33-logicallocation-object_fullyqualifiedname-property_example-1.json` | run | 1 | valid | differs |
| `file-format-33-logicallocation-object_kind-property_example-1.json` | run | 3 | valid | differs |
| `file-format-33-logicallocation-object_kind-property_example-2.json` | run | 3 | 2 error(s), see findings | differs |
| `file-format-33-logicallocation-object_name-property_example-1.json` | logicalLocation | 0 | valid | same |
| `file-format-33-logicallocation-object_parentindex-property_example-1.json` | run | 1 | valid | same |
| `file-format-34-locationrelationship-object_general_example-1.json` | result | 1 | valid | same |
| `file-format-36-codeflow-object_general_example-1.json` | result | 1 | valid | same |
| `file-format-37-threadflow-object_immutablestate-property_example-1.json` | threadFlow | 1 | valid | same |
| `file-format-38-threadflowlocation-object_index-property_example-1.json` | run | 1 | valid | differs |
| `file-format-38-threadflowlocation-object_index-property_example-2.json` | run | 2 | valid | differs |
| `file-format-38-threadflowlocation-object_index-property_example-3.json` | run | 2 | valid | differs |
| `file-format-38-threadflowlocation-object_kinds-property_example-1.json` | threadFlowLocation | 0 | valid | differs |
| `file-format-38-threadflowlocation-object_kinds-property_example-2.json` | threadFlowLocation | 0 | valid | differs |
| `file-format-38-threadflowlocation-object_kinds-property_example-3.json` | threadFlowLocation | 0 | valid | differs |
| `file-format-38-threadflowlocation-object_location-property_example-1.json` | codeFlow | 0 | valid | same |
| `file-format-38-threadflowlocation-object_state-property_example-1.json` | threadFlowLocation | 0 | valid | same |
| `file-format-38-threadflowlocation-object_taxa-property_example-1.json` | run | 1 | valid | same |
| `file-format-40-node-object_id-property_example-1.json` | graph | 0 | valid | same |
| `file-format-41-edge-object_sourcenodeid-property_example-1.json` | graph | 1 | valid | same |
| `file-format-42-graphtraversal-object_edgetraversals-property_example-1.json` | result | 1 | valid | same |
| `file-format-42-graphtraversal-object_immutablestate-property_example-1.json` | graphTraversal | 1 | valid | same |
| `file-format-43-edgetraversal-object_stepoveredgecount-property_example-1.json` | result | 1 | 2 error(s), see findings | same |
| `file-format-48-resultprovenance-object_conversionsources-property_example-1.json` | sarifLog | 2 | valid | differs |
| `file-format-49-reportingdescriptor-object_deprecatedids-property_example-1.json` | run | 2 | valid | same |
| `file-format-49-reportingdescriptor-object_messagestrings-property_example-1.json` | reportingDescriptor | 1 | valid | same |
| `file-format-49-reportingdescriptor-object_shortdescription-property_example-1.json` | reportingDescriptor | 1 | valid | same |
| `file-format-50-reportingconfiguration-object_parameters-property_example-1.json` | reportingDescriptor | 0 | 1 error(s), see findings | same |
| `file-format-51-configurationoverride-object_general_example-1.json` | run | 1 | valid | same |
| `file-format-52-reportingdescriptorreference-object_general_example-1.json` | invocation | 1 | valid | same |
| `file-format-52-reportingdescriptorreference-object_id-property_example-1.json` | run | 4 | valid | same |
| `file-format-52-reportingdescriptorreference-object_index-property_example-1.json` | run | 1 | valid | same |
| `file-format-53-reportingdescriptorrelationship-object_general_example-1.json` | run | 0 | valid | same |
| `file-format-53-reportingdescriptorrelationship-object_general_example-2.json` | run | 0 | valid | differs |
| `file-format-55-fix-object_artifactchanges-property_example-1.json` | fix | 0 | valid | same |
| `file-format-55-fix-object_artifactchanges-property_example-2.json` | fix | 0 | valid | same |
| `file-format-55-fix-object_description-property_example-1.json` | - | 0 | no host: the fix is shown under a label key `fix`, which no SARIF object has; the twin should hold the fix itself | differs |
| `file-format-55-fix-object_general_example-1.json` | result | 2 | valid | differs |
| `file-format-56-artifactchange-object_general_example-1.json` | fix | 1 | valid | differs |
| `file-format-57-replacement-object_general_example-1.json` | fix | 6 | 3 error(s), see findings | differs |
| `file-format-57-replacement-object_general_example-2.json` | artifactChange | 1 | valid | differs |
| `file-format-58-notification-object_associatedrule-property_example-1.json` | run | 1 | valid | same |
