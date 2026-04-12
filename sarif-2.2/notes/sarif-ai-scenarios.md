# SARIF for AI Security Findings — Scenario Guide

**Version:** 0.1 (draft)  
**Status:** Proposal

---

## Use Cases

| Dimension | [S1: AI Primary Scanner](sarif-ai-generated-findings.md) | [S2: AI Triages Single Tool](sarif-ai-triage-annotation.md) | [S3: AI Synthesizes Multiple Tools](sarif-ai-multi-tool-synthesis.md) |
|---|---|---|---|
| Upstream SARIF | None | One run | Multiple runs |
| AI's results | New `results[]` in its own run | Rewrites existing results; originals preserved in `original.*` property bag | New `results[]` from synthesis |
| Tool identity | AI is `driver` | Original `tool` untouched; AI provenance in `run.properties` | All originals preserved; AI has its own run |
| Rule IDs | AI's own (CWE-based) | Upstream tool's | AI's own (CWE-based) |
| Taxonomy (`taxa`) | Rarely needed | Optional — AI may add CWE refs to upstream results | Recommended — maps multiple tool rule namespaces to shared taxonomy |
| Source cross-references | N/A | `suppressions[]`, `level` rewrites, `ai.triage.confidence` | `relatedLocations` + `ai.synthesis.sourceResults` |
| `runs[]` count | 1 | 1 | 3+ |

---

## Scenario 1: AI Primary Scanner

AI scans source code directly with no upstream tool output. AI is `run.tool.driver`. The LLM model and named skills are recorded in `run.tool.extensions[]`. Findings are first-class `result` objects with CWE-based rule IDs (`CWE-78/mcp-server`). `CWE-78` covers OS Command Injection across any context; `CWE-78/mcp-server` is an instance of it in MCP server tool handlers.

→ [sarif-ai-generated-findings.md](sarif-ai-generated-findings.md)

---

## Scenario 2: AI Triages Single Tool Output

One upstream tool (CodeQL, Semgrep, a custom scanner) has produced SARIF. AI evaluates each finding and issues a verdict: false positive, true positive, or reprioritization. The original tool's identity and results are preserved. AI verdicts are expressed as a lossless overlay: `result.suppressions[]` for FPs, `result.level` rewrites with `original.level` preservation for reprioritization, and `ai.triage.*` property bag fields for machine-readable triage metadata supporting automated re-triage pipelines.

→ [sarif-ai-triage-annotation.md](sarif-ai-triage-annotation.md)

---

## Scenario 3: AI Synthesizes Multiple Tool Outputs

Multiple upstream tools have produced SARIF. AI reads across all runs, correlates patterns that no single tool may have detected alone, and issues its own findings in a new `run`. Upstream runs MAY be embedded in the same `runs[]` array when high-fidelity cross-referencing is needed — this enables both structured `ai.synthesis.sourceResults` property bag references and spec-defined `sarif:` URI embedded links (§3.10.3) in message text that point directly to upstream result objects by JSON Pointer. These URIs are fragile to post-processing. When upstream runs are absent, contributing code locations are referenced via `relatedLocations[]` and upstream results by `result.guid` if available. A `taxonomies` entry in the AI run maps across upstream tool rule namespaces to a shared CWE taxonomy. AI may also create taxa that map individual upstream tool rules to CWE entries, enabling cross-tool grouping for downstream consumers.

→ [sarif-ai-multi-tool-synthesis.md](sarif-ai-multi-tool-synthesis.md)
