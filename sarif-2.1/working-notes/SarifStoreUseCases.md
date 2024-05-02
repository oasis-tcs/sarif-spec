
## General Queries/Filters
* Filter by severity (error, warning, info)
* Filter by specific rule(s) (which comprise policies)
* Filter by scan targets paths/type/etc.
* Retrieve results by owner (see below)
* Retrieve new results by timestamp
  * New results since point-in-time
  * New results within start/end-time window
* Distinguish by critical categories:
  * Shipping vs. non-shipping code
* Filter verbose/non-essential information
  * Code flows, graphs, etc. (for detailed debugging)
  * Fixes
* Retrieve for specific UX, IDE, console, etc.

## Fixes
* Retrieve specific result instance(s)
* Show results in IDE scoped to:
  * Files opened in editor
  * Project/Solution
  * Repository/Branch/Commit

## Reporting
* Correlate with responsible developer(s)
  * Dev who checked in the vulnerability
  * Dev who is assigned the clean-up
* Correlate with literal code owners
  * Actual project code
  * 3rd-party/other checked in dependencies
* Correlate with accountable leaders
* Correlate with logical project definition
* Generate SAST evidence for compliance
  * Tool + plugin(s) version details
  * Comprehensive description of enabled rules
  * Invocation details (command-line, etc.)
  * Hashes/etc. of all scanned targets
