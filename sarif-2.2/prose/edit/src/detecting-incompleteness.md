<!--
---
toc:
  auto: false
  label: (Informative) Detecting incomplete result sets
  enumerate: Appendix I.
---
-->
# (Informative) Detecting incomplete result sets

This document describes three conditions that inform the SARIF consumer that the tool has failed to produce a comprehensive set of results. For convenience, this Appendix gathers those conditions together in one place:

- If any `invocation` object ([§3.20](#invocation-object)) in `theRun.invocations` ([§3.14.11](#invocations-property)) has a value of `false` for its `executionSuccessful` property ([§3.20.14](#executionsuccessful-property)), the tool either failed to start, terminated with an exit code that denotes failure, or terminated with an unhandled exception or signal.

- If any `notification` object ([§3.58](#notification-object)) in `invocation.toolExecutionNotifications` ([§3.20.21](#toolexecutionnotifications-property)) or `toolConfigurationNotifications` ([§3.20.22](#toolconfigurationnotifications-property)) has a value of `"error"` for its `level` property ([§3.58.6](#notification-object--level-property)), it is possible that the tool was unable to execute every analysis rule on every analysis target. Therefore, the results cannot be assumed to be complete.

- If `theRun.results` ([§3.14.23](#results-property)) is `null`, the tool either failed to start or failed to begin its analysis.

These conditions apply separately to each run in the log file.
