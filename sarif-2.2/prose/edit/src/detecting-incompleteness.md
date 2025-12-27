<!--
---
toc:
  auto: false
  label: (Informative) Detecting incomplete result sets
  enumerate: Appendix I.
---
-->
# (Informative) Detecting Incomplete Result Sets

This document describes three conditions that inform the SARIF consumer that the tool has failed to produce a comprehensive set of results. For convenience, this Appendix gathers those conditions together in one place:

- If any `invocation` object ([sec](#invocation-object)) in `theRun.invocations` ([sec](#invocations-property)) has a value of `false` for its `executionSuccessful` property ([sec](#executionsuccessful-property)), the tool either failed to start, terminated with an exit code that denotes failure, or terminated with an unhandled exception or signal.

- If any `notification` object ([sec](#notification-object)) in `invocation.toolExecutionNotifications` ([sec](#toolexecutionnotifications-property)) or `toolConfigurationNotifications` ([sec](#toolconfigurationnotifications-property)) has a value of `"error"` for its `level` property ([sec](#notification-object--level-property)), it is possible that the tool was unable to execute every analysis rule on every analysis target. Therefore, the results cannot be assumed to be complete.

- If `theRun.results` ([sec](#results-property)) is `null`, the tool either failed to start or failed to begin its analysis.

These conditions apply separately to each run in the log file.
