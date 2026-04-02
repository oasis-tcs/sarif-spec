# Decorating Tool-Generated SARIF with AI Triage

**Version:** 0.3 (draft)  
**Status:** Proposal  
**Scope:** Conventions for annotating existing SARIF results with AI-supplied triage, without discarding the original tool's identity or findings structure

---

## Core Principle

When AI performs triage on findings produced by another tool, the original SARIF structure  tool identity, rule definitions, locations  is preserved intact. AI triage is expressed through:

1. **First-class SARIF mechanisms**  `suppressions[]` and `level` rewrites
2. **`original.*` property bag entries** to preserve any first-class field the AI overwrites
3. **`ai.triage.confidence`** per result, for audit and learning systems

The `ai.*` namespace prevents collision with upstream tool properties and signals AI provenance to consumers.

### Lossless Overlay

- A consumer ignoring `suppressions[]` and `properties` sees the raw tool output.
- A consumer applying `suppressions[]` and reading `result.level` sees the AI-triaged view.
- A consumer reading `original.*` can reconstruct the pre-annotation result.

---

## Run-Level Identity

The SARIF spec (§3.18.1) states that post-processing tools SHOULD NOT alter the `tool` object. AI provenance is therefore recorded entirely in `run.properties`, leaving the original tool identity untouched.

```json
"properties": {
  "ai.triaged": true,
  "ai.triage.model": "GPT-4o/2024-11-20",
  "ai.triage.promptVersion": "mcp-detection-skill/1.0.0",
  "ai.triage.timestamp": "2026-03-31T21:00:00Z"
}
```

---

## Result Management

### False positives  `result.suppressions[]`

`suppressions[]` is an additive array — in-source annotations, sidecar files, and external systems all contribute entries. AI appends its own entry and preserves all pre-existing ones unchanged.

```json
"suppressions": [
  {
    "kind": "inSource",
    "status": "accepted",
    "justification": "Reviewed by dev team; test fixture only."
  },
  {
    "kind": "external",
    "status": "accepted",
    "justification": "Server binds to 127.0.0.1 only; not externally reachable.",
    "guid": "a3f2e917-4b1c-4d2e-8f3a-1234567890ab",
    "properties": {
      "ai.triaged": true,
      "ai.triage.confidence": 0.95
    }
  }
]
```

- `kind: "external"`  AI is an external system relative to the tool run
- `status: "accepted"`  AI is confident; use `"underReview"` when human confirmation is required
- `ai.triaged: true`  marks this suppression as AI-originated; consumers can filter by this to distinguish AI suppressions from human or in-source ones
- `justification`  brief plain-text reason; full analysis in `message.markdown`

**Run-level constraint (§3.27.23):** Once any result carries a non-null `suppressions` array, all results in the run must too. Results with no prior suppressions and no AI suppression get `suppressions: []` (not suppressed, information available).

AI rewrites `message.text` and authors `message.markdown` with the full rationale. The original message is preserved in `message.properties["original.text"]`.

### Uncertain findings  `suppressions[].status = "underReview"`

When AI cannot determine exploitability, suppress with `"underReview"` to remove the result from active consideration pending human review. The `justification` states what AI could not determine.

### Severity calibration  `result.level` rewrite

When a finding is a confirmed TP but the tool's severity is wrong, rewrite `result.level` and preserve the original:

```json
"level": "warning",
"properties": {
  "original.level": "error",
  "ai.triage.confidence": 0.80
}
```

---

## Audit and Learning

`ai.triage.confidence` is the only per-result field — everything else (`model`, `promptVersion`, `timestamp`) is global on `run.properties`. For suppressed results, confidence lives on the suppression object's `properties` (already shown above). For non-suppressed results — confirmed TPs whether or not `level` changed — add it to `result.properties`:

```json
"properties": {
  "ai.triage.confidence": 0.91
}
```

---

## `original.*`  Preservation of Overwritten Properties

**At-level principle:** When AI overwrites any property on a SARIF object, `original.<propertyName>` goes into the property bag of that same object.

| Object rewritten | Property bag that receives `original.*` |
|---|---|
| `result.level` | `result.properties` |
| `result.message.text` | `result.message.properties` |
| `result.message.markdown` | `result.message.properties` |

Both namespaces use dot-separated flat keys.

---

## Message Authoring

For every triaged result, AI authors `message.text` and `message.markdown`. Original values are preserved in `message.properties["original.text"]` and `message.properties["original.markdown"]`.

### `message.text`

The first sentence must stand alone as a complete synopsis. For FP and uncertain results: state what AI determined and why. For TP with level change: state what the tool found and how AI calibrated the severity.

### `message.markdown`

Evidence, reasoning, mitigating factors checked, recommended action. This is the primary artifact for human reviewers.

`original.markdown` is `null` (or omitted) when the original tool produced no markdown.

---

## Combined Examples

### Confirmed FP

```json
{
  "ruleId": "CWE-306/mcp-server",
  "kind": "fail",
  "level": "error",
  "message": {
    "text": "False positive: MCP server at src/handler.py:88 binds to 127.0.0.1 only; no external caller can reach this process.",
    "markdown": "## False Positive  Loopback-Bound Server\n\n**Confidence:** 0.95\n\nThe missing-auth pattern is structurally present but the server binds to `127.0.0.1` only (`host='localhost'`, line 88). No external caller can reach this process.\n\n**No action required.**",
    "properties": {
      "original.text": "MCP server starts on port 8080 without authentication middleware.",
      "original.markdown": null
    }
  },
  "locations": [
    {
      "physicalLocation": {
        "artifactLocation": { "uri": "src/handler.py", "uriBaseId": "%SRCROOT%" },
        "region": { "startLine": 88 }
      }
    }
  ],
  "suppressions": [
    {
      "kind": "external",
      "status": "accepted",
      "justification": "Server binds to 127.0.0.1 only (host='localhost', line 88). Not externally reachable.",
      "guid": "a3f2e917-4b1c-4d2e-8f3a-1234567890ab"
    }
  ],
  "properties": {
    "ai.triage.confidence": 0.95
  }
}
```

### Uncertain — pending human review

```json
{
  "ruleId": "CWE-78/mcp-server",
  "kind": "fail",
  "level": "error",
  "message": {
    "text": "Auth status of secondary router at /internal/mcp could not be determined; taint path to subprocess.run() exists if the route is unguarded.",
    "markdown": "## Uncertain  Secondary Router Auth Status Unknown\n\n**Confidence:** 0.55\n\nAn `@auth_required` decorator is present on the primary endpoint. A secondary router is registered at `/internal/mcp` in `src/routes/internal.py:44`; its guard status could not be determined from the available code.\n\n**Recommend manual verification of router registration at `/internal/mcp`.**",
    "properties": {
      "original.text": "The 'args' parameter flows to subprocess.run() without sanitization.",
      "original.markdown": null
    }
  },
  "suppressions": [
    {
      "kind": "external",
      "status": "underReview",
      "justification": "Auth status of secondary router at /internal/mcp could not be determined.",
      "guid": "b2c3d4e5-6789-0abc-def0-234567890abc"
    }
  ],
  "properties": {
    "ai.triage.confidence": 0.55
  }
}
```

### Severity calibration (TP, overstated priority)

```json
{
  "ruleId": "CWE-306/mcp-server",
  "kind": "fail",
  "level": "warning",
  "message": {
    "text": "MCP server at src/app.ts starts without authentication middleware; server binds to an internal 10.x subnet, limiting exposure to internal callers.",
    "markdown": "## Missing Authentication  Internal Network Only\n\n**Confidence:** 0.80  Severity lowered from Error\n\nThe missing-auth pattern is real. Server binds to an internal 10.x subnet per deployment config; blast radius is limited to internal callers.",
    "properties": {
      "original.text": "MCP server starts without authentication middleware."
    }
  },
  "properties": {
    "original.level": "error",
    "ai.triage.confidence": 0.80
  }
}
```

### Confirmed TP, no changes

```json
{
  "ruleId": "CWE-78/mcp-server",
  "kind": "fail",
  "level": "error",
  "message": {
    "text": "The 'command' parameter flows unsanitized to subprocess.run() in the 'run_shell' MCP handler, enabling arbitrary command execution by an unauthenticated caller."
  },
  "properties": {
    "ai.triage.confidence": 0.97
  }
}
```

---

## Appendix: Rejected Conventions

### `kind = "open"` — not used

`"open"` was designed for proof-based and constraint-solving tools: the tool ran but could not close a constraint and cannot determine whether a violation exists. In practice `"open"` has near-zero consumer adoption — viewers, IDEs, and result management systems do not surface these results, making them invisible.

AI uncertainty is not an open constraint. When AI cannot determine exploitability it has evaluated the evidence and reached an uncertain conclusion — epistemic uncertainty, not an unclosed proof obligation. The correct expression is `"fail"` with calibrated `level`, or `"fail"` + `suppressions[].status = "underReview"` when human review is explicitly required. Both stay visible and well-supported.

### `kind = "review"` — not used

`"review"` is for rules where no automated check is possible at all — the tool surfaces a pattern and asks the user to inspect manually (the spec's example: an accessibility checker flagging "do not use color alone to highlight important information"). AI always performs an evaluation; it does not emit results for rules it cannot check. Uncertainty about a specific finding is an evaluation outcome, not a structural inability to evaluate.

---

*See `sarif-ai-scenarios.md` for use case navigation. `sarif-ai-generated-findings.md` covers Scenario 1 (AI primary scanner); `sarif-ai-multi-tool-synthesis.md` covers Scenario 3 (multi-tool synthesis).*
