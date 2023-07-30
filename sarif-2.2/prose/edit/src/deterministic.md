<!--
---
toc:
  auto: false
  label: (Informative) Producing deterministic SARIF log files
  enumerate: Appendix F.
  children:
  - label: General
    enumerate: F.1
  - label: Non-deterministic file format elements
    enumerate: F.2
  - label: Array and dictionary element ordering
    enumerate: F.3
  - label: Absolute paths
    enumerate: F.4
  - label: Inherently non-deterministic tools
    enumerate: F.5
  - label: Compensating for non-deterministic output
    enumerate: F.6
  - label: Interaction between determinism and baselining
    enumerate: F.7
---
-->
# (Informative) Producing deterministic SARIF log files <a id='informative-producing-deterministic-sarif-log-files'></a>

## General{#informative-producing-deterministic-sarif-log-files--general}

In certain circumstances, it is desirable for an analysis tool to produce deterministic output; that is, for it to produce identical output when run repeatedly with identical inputs.

For example, this is useful in a build system that caches the output from each build step. If the build is rerun and the inputs to a given step are identical (which the build system might determine, for example, by comparing timestamps, or by computing a hash of the inputs to the step and storing it along with the output from the step), then the build system can save time by not re-running the step, and simply using the existing outputs.

Consider this sequence of build steps:

1.  A binary analysis tool analyzes A.dll and produces A.sarif.

2.  A bug database ingestion tool reads A.sarif and files bugs for any new results.

If A.sarif has not changed between this build and the previous one, the build system does not have to execute Step 2.

Authors of analysis tools are encouraged to provide a mechanism (for example, a command line option such as `--deterministic`) which instructs the tool to produce deterministic output.

There are several issues to consider when producing deterministic output:

- Avoiding elements of the SARIF file format whose values are non-deterministic.

- Emitting array and dictionary elements in a deterministic order.

- Avoiding absolute paths.

- Handling baseline information

## Non-deterministic file format elements

Certain optional elements of the SARIF format are non-deterministic in most situations. A log file that includes these elements will not be deterministic except under special circumstances. For example:

- If a build system always runs on the same machine under the same account, `invocation.machine` and `invocation.account` is deterministic.

- If a binary analysis tool runs in an environment that guarantees the same memory layout from run to run (for example, an environment that allows a binary to be loaded at a fixed address and that does not use address space layout randomization (ASLR)), then `physicalLocation.address` and `run.addresses` are deterministic.

Authors of analysis tools are encouraged to provide a mechanism (for example, a command line option such as `--known-deterministic-properties:<property name>…`) which allows the tool to emit specified properties even when producing deterministic output.

Avoiding these elements, in conjunction with the techniques described in subsequent sections of this Appendix, makes it more likely that the analysis tool will produce deterministic output:

- Non-deterministic elements in property bag properties.

- Non-deterministic elements in user-facing messages, for example, a timestamp in a result message.

- The trailing component of `run.automationDetails.id`

- `run.automationDetails.guid`

- `run.baselineGuid`

- `run.originalUriBaseIds`

- `run.addresses`, because security measures such as address space layout randomization (ASLR) might place the same code at different addresses from run to run.

- `invocation.commandLine`, because it might specify non-deterministic absolute file paths or other non-deterministic elements.

- `invocation.arguments`, for the same reason.

- `invocation.processId`

- `invocation.startTimeUtc`

- `invocation.endTimeUtc`

- `invocation.machine`

- `invocation.account`

- `invocation.workingDirectory`, because the tool might be launched from different directories on different machines.

- `invocation.environmentVariables`

- `invocation.stdin`, `stdout`, `stderr`, or `stdoutStderr`, because the tool’s console output might include non-deterministic elements such as timestamps.

- `versionControlDetails.revisionId`

- `versionControlDetails.asOfTimeUtc`

- `versionControlDetails.mappedTo`, because a repository might be downloaded to different directories on different machines.

- `threadFlow.threadId`

- `threadFlowLocation.executionTimeUtc`

- `notification.threadId`

- `notification.timeUtc`

- `result.guid`

- `stackFrame.threadId`

- `physicalLocation.address`, for the same reason as `run.addresses`.

## Array and dictionary element ordering

One obstacle to determinism in SARIF log files is the ordering of array elements and object properties.

For some arrays, SARIF requires a specific ordering. For example, within `stack.frames`, SARIF requires the `location` object representing the most deeply nested function call to appear first.

For other arrays, for example `properties.tags`, SARIF does not require a specific ordering. For such arrays, a tool can ensure the order by sorting the array elements before writing them to the log file. For example, it might sort the tags in locale-insensitive alphabetical order.

The array of `result` objects in the `run.results` array presents more of a problem. A multi-threaded analysis tool analyzing multiple artifacts in parallel might produce results in any order, and there is no natural order for the results. A tool might choose to order them, for example, first alphabetically by analysis target URI, then numerically by line number, then by column number, then alphabetically by rule id.

For dictionaries such as the `artifact.hashes` object, a tool might order the property names alphabetically, using a locale-insensitive ordering.

## Absolute paths

Another obstacle to determinism is the use of absolute paths which might differ from machine to machine. For example:

- Different build machines might be configured to use different source directories.

- A single build machine might use a different directory for each build.

Tools can avoid the use of absolute file paths by emitting URIs that are relative to one or more root directories (for example, a source root directory and an output root directory), and accompanying each `artifactLocation.uri` property with the corresponding `artifactLocation.uriBaseId` property.

## Inherently non-deterministic tools

The algorithms used by some tools are inherently non-deterministic because, for example, they perform random sampling or random traversals of the graphs that represent the code. Generally, these tools produce mostly the same result set, but there might be small differences between runs.

Such tools can avoid this source of non-determinism by, for example, providing a command-line argument to specify the random number generator seed.

## Compensating for non-deterministic output <a id='compensating-for-non-deterministic-output'></a>

If an analysis tool does not produce deterministic output, a build system can add additional processing steps to compensate.

There are two scenarios to consider:

- Log equality is determined by a simple comparison of file contents, or by comparing file hashes.

- Log equality is determined by an "intelligent" comparison.

In the first scenario, a post-processing step could produce deterministic output by creating a new file that omits non-deterministic elements, reorders array elements and object properties, removes file path prefixes, and introduces `artifactLocation.uriBaseId` properties.

In the second scenario, a post-processing step could intelligently compare the newly produced log to the log from a previous build by ignoring non-deterministic elements, ensuring that arrays have the same elements regardless of order, and ignoring file path prefixes.

## Interaction between determinism and baselining

SARIF's baselining feature poses a particular challenge for determinism. We illustrate the problem with the following scenario:

On a particular date, a project's nightly build runs an analysis tool ToolX, which produces a log file, say, `log_20170914.sarif`. The next day, a developer modifies one of the files scanned by the tool in a way that introduces a new problem. That night, the nightly build tool runs again, this time producing a log file which compares the current set of results to those that appeared in the previous run:

    ToolX --input a.c b.c --baseline log_20170914.sarif --output log_20170915.sarif

Because a new problem has been introduced, `log_20170614.sarif` will contain a result object whose `baselineState` is `"new"`. The next night, without any further changes to the source files, the tool is run yet again:

    ToolX --input a.c b.c --baseline log_20170915.sarif --output log_20170916.sarif

The result object that first appeared in `log_20160615.sarif` still appears in `log_20160616.sarif`, but since it existed in the baseline, its baselineState will now be `"unchanged"` or `"updated"` as appropriate (see [§3.27.24](#baselinestate-property)).

The result is that even though none of the analysis target files have changed, the log file has changed, or at least, a simple file comparison (such as comparing the hash of the new log with the hash of the baseline) will report that it has changed.

Strictly speaking, this does not violate determinism. After all, the baseline file has changed, and the baseline file is one of the inputs to the analysis. But from a practical standpoint, this is still a problem, albeit a small one.

If the build uses a simple mechanism such as hash value comparison to determine if a file has changed, then on those occasions when the only difference between the newest log and the baseline is that some results that were previously "new" are now "unchanged", subsequent build steps which consume the SARIF log file will run, even if they might not actually be necessary. For example, a build step which automatically files bugs for new results will run, even though the log contains no new results. Or a build step which tracks the number of open issues will run, even though the number of open issues has not actually changed.

If the build engineers for a project wish to absolutely minimize the execution of unnecessary build steps, they have various options. They might perform an "intelligent" comparison between the baseline and the new log, treating "new" results in the baseline as equivalent to "unchanged" results. Or they might rewrite the baseline (marking all "new" results as "unchanged") before performing the comparison. Of course, there is no guarantee that such an "intelligent" comparison or baseline rewriting process will actually take less time than the unnecessary build steps it is intended to avoid.
