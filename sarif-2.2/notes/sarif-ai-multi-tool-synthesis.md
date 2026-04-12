# SARIF for AI-Synthesized Findings from Multiple Tool Outputs

**Version:** 0.1 (draft)  
**Status:** Proposal  
**Scope:** Conventions for a SARIF log where AI reads findings from multiple upstream tools and produces its own results by correlating across them

---

## Core Principle

When AI correlates findings across multiple tools, it adds its own run with its own `tool.driver`, `results[]`, and `automationDetails`. Upstream runs MAY be included in the same `runs[]` array — this enables structured cross-referencing to upstream results — but is not required.

SARIF provides a spec-defined mechanism for referencing any element within the same log file: the `sarif:` URI scheme (§3.10.3), used in embedded links within `message.text` or `message.markdown` (§3.11.6). The path component is a JSON Pointer (RFC 6901). When upstream runs are embedded, a message can link directly to a contributing result: `[CodeQL finding](sarif:/runs/0/results/42)`. The spec explicitly identifies cross-run result references as an intended use. These URIs are fragile to post-processing — if runs are reordered or results removed, all indices must be updated.

For structured (non-message) cross-referencing, `ai.synthesis.sourceResults` in `result.properties` records `{runIndex, resultIndex}` pairs; this is a property bag convention that applies only when upstream runs are embedded. When upstream runs are absent, upstream results can be identified by `result.guid` if GUIDs are available.

---

## Log Structure

```json
{
  "$schema": "https://schemastore.azurewebsites.net/schemas/json/sarif-2.1.0-rtm.5.json",
  "version": "2.1.0",
  "runs": [
    { /* run[0]: CodeQL */ },
    { /* run[1]: Semgrep */ },
    { /* run[2]: AI synthesis */ }
  ]
}
```

All runs share the same `correlationGuid` in their respective `automationDetails`, linking them as a coordinated analysis of the same codebase.

---

## AI Run Tool Identity

The AI synthesis run uses the same identity conventions as Scenario 1: `tool.driver` is the AI scanning system; `tool.extensions[]` records the model and skills.

```json
"tool": {
  "driver": {
    "name": "MCP Security Analyzer",
    "organization": "Microsoft",
    "semanticVersion": "1.0.0",
    "rules": [
      {
        "id": "CWE-78/mcp-server",
        "name": "CommandInjectionMcpServer",
        "shortDescription": { "text": "MCP tool parameter flows to a command execution sink" },
        "helpUri": "https://cwe.mitre.org/data/definitions/78.html",
        "defaultConfiguration": { "level": "error" },
        "relationships": [
          {
            "target": { "id": "78", "toolComponent": { "name": "CWE", "index": 0 } },
            "kinds": ["superset"]
          }
        ]
      }
    ]
  },
  "extensions": [
    { "name": "GPT-4o", "version": "2024-11-20" },
    { "name": "mcp-detection-skill", "version": "1.0.0" }
  ]
}
```

---

## Taxonomy

In a multi-tool context, a shared taxonomy lets consumers group findings from all runs by a common identifier regardless of tool-specific rule names. The AI run defines the taxonomy entry; upstream tool runs may reference it via their own `rule.relationships[]`.

```json
"taxonomies": [
  {
    "name": "CWE",
    "version": "4.14",
    "organization": "MITRE",
    "informationUri": "https://cwe.mitre.org/",
    "taxa": [
      { "id": "78",  "name": "Improper Neutralization of Special Elements used in an OS Command" },
      { "id": "306", "name": "Missing Authentication for Critical Function" }
    ]
  }
]
```

AI may also create taxa that map upstream tool rule IDs to the shared taxonomy, enabling downstream consumers to reason about cross-tool coverage without knowing tool-specific rule namespaces.

---

## Cross-Referencing Source Findings

### `relatedLocations[]` — source code locations

Point to the specific code locations in upstream runs that contributed to this finding. This is spec-defined per §3.27.22 and is the correct mechanism for code location references (physical and logical locations only — not result object references).

```json
"relatedLocations": [
  {
    "id": 1,
    "message": { "text": "Taint source: caller-controlled 'command' parameter (CodeQL)" },
    "physicalLocation": {
      "artifactLocation": { "uri": "src/handler.py", "uriBaseId": "%SRCROOT%" },
      "region": { "startLine": 15 }
    }
  },
  {
    "id": 2,
    "message": { "text": "Authentication gap: /internal/mcp endpoint lacks auth decorator (Semgrep)" },
    "physicalLocation": {
      "artifactLocation": { "uri": "src/routes/internal.py", "uriBaseId": "%SRCROOT%" },
      "region": { "startLine": 44 }
    }
  }
]
```

### `sarif:` URI embedded links — result references in message text

SARIF provides a spec-defined scheme for referencing any element within the same log file by JSON Pointer (§3.10.3). Embedded links in `message.text` or `message.markdown` MAY use this scheme (§3.11.6), and the spec explicitly cites cross-run result references as an intended use:

```
"There was [another result](sarif:/runs/0/results/42) found by this code flow."
```

In a synthesis message this becomes:

```
[CodeQL finding](sarif:/runs/0/results/0) — taint path to `subprocess.run()`
[Semgrep finding](sarif:/runs/1/results/0) — missing auth on `/internal/mcp`
```

> **Fragility note (spec §3.11.6):** These URIs are index-based. If a post-processor reorders runs or removes results, all `sarif:` URI indices must be updated. Use only when upstream runs are embedded in the same log and index stability can be maintained.

### `ai.synthesis.sourceResults` — structured result indices

For machine-readable cross-referencing (as opposed to in-message links), record the upstream `{runIndex, resultIndex}` pairs in `result.properties`. Applies only when upstream runs are embedded.

```json
"properties": {
  "ai.synthesis.sourceResults": [
    { "runIndex": 0, "resultIndex": 2 },
    { "runIndex": 1, "resultIndex": 7 }
  ],
  "ai.triage.confidence": 0.92,
  "ai.triage.model": "GPT-4o/2024-11-20",
  "ai.triage.promptVersion": "mcp-detection-skill/1.0.0",
  "ai.triage.timestamp": "2026-03-31T21:00:00Z"
}
```

---

## automationDetails and correlationGuid

```json
// CodeQL run (runs[0])
"automationDetails": {
  "id": "codeql/2026-03-31/contoso/my-project/my-mcp-service/",
  "guid": "b1c2d3e4-5678-90ab-cdef-1234567890ab",
  "correlationGuid": "f7c3a041-9d2e-4b18-a765-0fedcba98765"
}

// Semgrep run (runs[1])
"automationDetails": {
  "id": "semgrep/2026-03-31/contoso/my-project/my-mcp-service/",
  "guid": "c2d3e4f5-6789-0abc-def0-234567890abc",
  "correlationGuid": "f7c3a041-9d2e-4b18-a765-0fedcba98765"
}

// AI synthesis run (runs[2])
"automationDetails": {
  "id": "mcp-security-analyzer/2026-03-31/contoso/my-project/my-mcp-service/",
  "guid": "d3e4f5a6-789a-0bcd-ef01-34567890abcd",
  "description": {
    "text": "AI synthesis of CodeQL + Semgrep findings · GPT-4o 2024-11-20 · mcp-detection-skill v1.0.0"
  },
  "correlationGuid": "f7c3a041-9d2e-4b18-a765-0fedcba98765"
}
```

---

## Minimal Valid Example

```json
{
  "$schema": "https://schemastore.azurewebsites.net/schemas/json/sarif-2.1.0-rtm.5.json",
  "version": "2.1.0",
  "runs": [
    {
      "tool": {
        "driver": {
          "name": "CodeQL",
          "organization": "GitHub",
          "semanticVersion": "2.17.0",
          "rules": [
            {
              "id": "py/command-injection",
              "shortDescription": { "text": "Uncontrolled command line" }
            }
          ]
        }
      },
      "automationDetails": {
        "id": "codeql/2026-03-31/contoso/my-project/my-mcp-service/",
        "guid": "b1c2d3e4-5678-90ab-cdef-1234567890ab",
        "correlationGuid": "f7c3a041-9d2e-4b18-a765-0fedcba98765"
      },
      "results": [
        {
          "ruleId": "py/command-injection",
          "kind": "fail",
          "level": "error",
          "message": { "text": "This command depends on a user-provided value." },
          "locations": [
            {
              "physicalLocation": {
                "artifactLocation": { "uri": "src/handler.py", "uriBaseId": "%SRCROOT%" },
                "region": { "startLine": 42 }
              }
            }
          ]
        }
      ]
    },
    {
      "tool": {
        "driver": {
          "name": "Semgrep",
          "organization": "Semgrep",
          "semanticVersion": "1.60.0",
          "rules": [
            {
              "id": "python.flask.missing-auth",
              "shortDescription": { "text": "Flask route missing authentication decorator" }
            }
          ]
        }
      },
      "automationDetails": {
        "id": "semgrep/2026-03-31/contoso/my-project/my-mcp-service/",
        "guid": "c2d3e4f5-6789-0abc-def0-234567890abc",
        "correlationGuid": "f7c3a041-9d2e-4b18-a765-0fedcba98765"
      },
      "results": [
        {
          "ruleId": "python.flask.missing-auth",
          "kind": "fail",
          "level": "warning",
          "message": { "text": "Route /internal/mcp lacks authentication decorator." },
          "locations": [
            {
              "physicalLocation": {
                "artifactLocation": { "uri": "src/routes/internal.py", "uriBaseId": "%SRCROOT%" },
                "region": { "startLine": 44 }
              }
            }
          ]
        }
      ]
    },
    {
      "tool": {
        "driver": {
          "name": "MCP Security Analyzer",
          "organization": "Microsoft",
          "semanticVersion": "1.0.0",
          "rules": [
            {
              "id": "CWE-78/mcp-server",
              "shortDescription": { "text": "MCP tool parameter flows to a command execution sink" },
              "helpUri": "https://cwe.mitre.org/data/definitions/78.html",
              "defaultConfiguration": { "level": "error" },
              "relationships": [
                {
                  "target": { "id": "78", "toolComponent": { "name": "CWE", "index": 0 } },
                  "kinds": ["superset"]
                }
              ]
            }
          ]
        },
        "extensions": [
          { "name": "GPT-4o", "version": "2024-11-20" },
          { "name": "mcp-detection-skill", "version": "1.0.0" }
        ]
      },
      "taxonomies": [
        {
          "name": "CWE",
          "version": "4.14",
          "taxa": [
            { "id": "78", "name": "Improper Neutralization of Special Elements used in an OS Command" }
          ]
        }
      ],
      "automationDetails": {
        "id": "mcp-security-analyzer/2026-03-31/contoso/my-project/my-mcp-service/",
        "guid": "d3e4f5a6-789a-0bcd-ef01-34567890abcd",
        "description": {
          "text": "AI synthesis of CodeQL + Semgrep findings · GPT-4o 2024-11-20 · mcp-detection-skill v1.0.0"
        },
        "correlationGuid": "f7c3a041-9d2e-4b18-a765-0fedcba98765"
      },
      "results": [
        {
          "ruleId": "CWE-78/mcp-server",
          "kind": "fail",
          "level": "error",
          "message": {
            "text": "The 'command' parameter flows unsanitized to subprocess.run() in the 'run_shell' MCP handler via an unauthenticated route, enabling arbitrary command execution.",
            "markdown": "## Command Injection via Unauthenticated MCP Endpoint\n\n**Rule:** CWE-78/mcp-server · **Severity:** Error · **Confidence:** 0.92\n\nCodeQL detected a taint path from the caller-supplied `command` parameter to `subprocess.run()` at `src/handler.py:42`. Semgrep independently flagged the MCP route `/internal/mcp` at `src/routes/internal.py:44` as missing an authentication decorator. Together these confirm an unauthenticated caller can supply an arbitrary `command` value that reaches the `subprocess.run()` sink.\n\n### Source findings\n- [CodeQL result](sarif:/runs/0/results/0) — taint path to `subprocess.run()`\n- [Semgrep result](sarif:/runs/1/results/0) — missing auth on `/internal/mcp`"
          },
          "locations": [
            {
              "physicalLocation": {
                "artifactLocation": { "uri": "src/handler.py", "uriBaseId": "%SRCROOT%" },
                "region": { "startLine": 42 }
              }
            }
          ],
          "relatedLocations": [
            {
              "id": 1,
              "message": { "text": "Authentication gap: /internal/mcp lacks auth decorator (Semgrep)" },
              "physicalLocation": {
                "artifactLocation": { "uri": "src/routes/internal.py", "uriBaseId": "%SRCROOT%" },
                "region": { "startLine": 44 }
              }
            }
          ],
          "properties": {
            "ai.synthesis.sourceResults": [
              { "runIndex": 0, "resultIndex": 0 },
              { "runIndex": 1, "resultIndex": 0 }
            ],
            "ai.triage.confidence": 0.92,
            "ai.triage.model": "GPT-4o/2024-11-20",
            "ai.triage.promptVersion": "mcp-detection-skill/1.0.0",
            "ai.triage.timestamp": "2026-03-31T21:00:00Z"
          }
        }
      ]
    }
  ]
}
```

---

## Decision Summary

| Situation | Mechanism |
|---|---|
| Embed upstream tool runs | Include in `runs[]` before AI synthesis run |
| Link all runs as coordinated | Same `correlationGuid` in all `automationDetails` |
| Reference upstream code location | `result.relatedLocations[]` |
| Reference upstream result in message | `sarif:/runs/{n}/results/{m}` embedded link in `message.text`/`message.markdown` (§3.10.3, §3.11.6); fragile to post-processing |
| Reference upstream result (structured) | `ai.synthesis.sourceResults` `{runIndex, resultIndex}` in `result.properties`; requires upstream runs to be embedded |
| Map to shared taxonomy | `run.taxonomies[]` + `rule.relationships[]` |
| AI model and skill provenance | `run.tool.extensions[]` |
| Synthesis reasoning | `message.markdown` |

---

*See `sarif-ai-scenarios.md` for use case navigation. `sarif-ai-generated-findings.md` covers Scenario 1 (AI primary scanner); `sarif-ai-triage-annotation.md` covers Scenario 2 (single tool post-processing).*
