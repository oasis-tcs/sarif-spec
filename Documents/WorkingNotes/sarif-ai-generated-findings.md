# SARIF for AI-Generated Security Findings

**Version:** 0.2 (draft)  
**Status:** Proposal  
**Scope:** Conventions for representing AI/LLM-produced security findings as first-class SARIF 2.1.0

---

## Core Principle

In this scenario, AI is the originating tool — the primary source of findings, not a post-processor of another tool's output. Its findings are first-class `result` objects with CWE-based rule IDs.

---

## Tool Identity

`run.tool.driver` is the **scanning system** — prompt infrastructure, parsing logic, concern definition — versioned independently of the underlying model.

`run.tool.extensions[]` documents the **execution session components**: the LLM model, named skills, and optional orchestrator. Each is independently versioned. This is what makes the provenance of an AI production machine-readable — a consumer can identify which model and skill versions produced a given run without inspecting prose.

```json
"tool": {
  "driver": {
    "name": "MCP Security Analyzer",
    "organization": "Microsoft",
    "semanticVersion": "1.0.0",
    "informationUri": "https://dev.azure.com/my-org/my-project/_git/ai-security-tooling",
    "rules": [
      {
        "id": "CWE-78/mcp-server",
        "name": "CommandInjectionMcpServer",
        "shortDescription": { "text": "MCP tool parameter flows to a command execution sink" },
        "fullDescription": { "text": "An MCP server tool handler passes a caller-controlled parameter to a command execution API without sanitization, enabling arbitrary command execution by an unauthenticated caller." },
        "helpUri": "https://cwe.mitre.org/data/definitions/78.html",
        "defaultConfiguration": { "level": "error" }
      },
      {
        "id": "CWE-22/mcp-server",
        "name": "PathTraversalMcpServer",
        "shortDescription": { "text": "MCP tool parameter flows to a file system sink" },
        "helpUri": "https://cwe.mitre.org/data/definitions/22.html",
        "defaultConfiguration": { "level": "error" }
      },
      {
        "id": "CWE-306/mcp-server",
        "name": "MissingAuthenticationMcpServer",
        "shortDescription": { "text": "MCP server starts without requiring caller authentication" },
        "helpUri": "https://cwe.mitre.org/data/definitions/306.html",
        "defaultConfiguration": { "level": "error" }
      }
    ]
  },
  "extensions": [
    {
      "name": "GPT-4o",
      "version": "2024-11-20",
      "informationUri": "https://learn.microsoft.com/azure/ai-services/openai/concepts/models"
    },
    {
      "name": "mcp-detection-skill",
      "version": "1.0.0",
      "shortDescription": { "text": "Unauthenticated MCP server detection prompt and concern definition" }
    }
  ]
}
```

**Rule ID design:** CWE is the rule namespace. The sub-ID sub-classifies broad CWEs: `CWE-78` covers OS Command Injection across any context; `CWE-78/mcp-server` is an instance of it in MCP server tool handlers.

---

## Run Qualification

`run.automationDetails` qualifies how this particular run was produced — model version, prompt version, scan scope.

```json
"automationDetails": {
  "id": "mcp-security-scanner/2026-03-31/contoso/my-project/",
  "guid": "a3f2e917-4b1c-4d2e-8f3a-1234567890ab",
  "description": {
    "text": "MCP Security Analyzer v1.0.0 · GPT-4o 2024-11-20 · Concern: Unauthenticated MCP Servers · Repo: contoso/my-project/my-mcp-service"
  },
  "correlationGuid": "f7c3a041-9d2e-4b18-a765-0fedcba98765"
}
```

- `id` — hierarchical string; the `<scanner>/<date>/<org>/<project>/` structure enables grouping in result management systems.
- `guid` — stable identifier for this specific run (RFC 4122 UUID).
- `correlationGuid` — links all per-repo runs within a single fleet scan campaign. Enables campaign-level aggregation without coupling individual SARIF files.

`run.versionControlProvenance[]` optionally documents the scanned commit and branch; useful for systems that key on VCS provenance.

---

## Result Structure

```json
{
  "ruleId": "CWE-78/mcp-server",
  "kind": "fail",
  "level": "error",
  "message": {
    "text": "The 'command' parameter flows unsanitized to subprocess.run() in the 'run_shell' tool handler, enabling arbitrary command execution by an unauthenticated caller. No authentication middleware was detected in the call chain.",
    "markdown": "## Command Injection via MCP Tool Parameter\n\n**Rule:** CWE-78/mcp-server · **Severity:** Error · **Confidence:** High\n\nThe `command` parameter supplied by the MCP caller at `src/handler.py:42` is passed directly to `subprocess.run()` without validation or sanitization.\n\n### Evidence\n```python\n# src/handler.py:42\nsubprocess.run(command, shell=True)  # command is caller-supplied\n```\n\n### Mitigating factors checked\n- No authentication middleware found in `src/`\n- Server binds to a public interface (externally reachable)\n- No network-layer restriction found in deployment config\n\n### Recommended fix\nValidate and allowlist commands, or avoid `shell=True`:\n```python\nsubprocess.run(['/usr/bin/mytool', '--safe-arg', value], shell=False)\n```\n\n### References\n- [CWE-78](https://cwe.mitre.org/data/definitions/78.html)"
  },
  "locations": [
    {
      "physicalLocation": {
        "artifactLocation": { "uri": "src/handler.py", "uriBaseId": "%SRCROOT%" },
        "region": { "startLine": 42, "startColumn": 5 }
      }
    }
  ]
}
```

**`message.text`:** The first sentence must stand alone as a complete synopsis (§3.11.3) — specific enough to be useful when truncated in space-constrained UIs. Pattern: `<What flows where> in <handler/context>, enabling <attack>`.

**`message.markdown`:** Full AI analysis for human reviewers: evidence, mitigating factors checked, remediation, references. No `original.*` preservation in Scenario 1 — AI generates from scratch.

---

## Multi-Language Runs

A single rule `CWE-78/mcp-server` applies regardless of implementation language. The `artifactLocation.uri` file extension identifies the language context for each finding. For a finding that spans artifacts in different languages (e.g., a TypeScript MCP handler invoking a Python subprocess wrapper), use `result.relatedLocations[]` for the secondary artifact.

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
          "name": "MCP Security Analyzer",
          "organization": "Microsoft",
          "semanticVersion": "1.0.0",
          "rules": [
            {
              "id": "CWE-78/mcp-server",
              "shortDescription": { "text": "MCP tool parameter flows to a command execution sink" },
              "helpUri": "https://cwe.mitre.org/data/definitions/78.html",
              "defaultConfiguration": { "level": "error" }
            }
          ]
        },
        "extensions": [
          { "name": "GPT-4o", "version": "2024-11-20" },
          { "name": "mcp-detection-skill", "version": "1.0.0" }
        ]
      },
      "automationDetails": {
        "id": "mcp-security-scanner/2026-03-31/contoso/my-project/my-mcp-service/",
        "guid": "a3f2e917-4b1c-4d2e-8f3a-1234567890ab",
        "description": {
          "text": "MCP Security Analyzer v1.0.0 · GPT-4o 2024-11-20 · Unauthenticated MCP Servers concern"
        }
      },
      "results": [
        {
          "ruleId": "CWE-78/mcp-server",
          "kind": "fail",
          "level": "error",
          "message": {
            "text": "The 'command' parameter flows unsanitized to subprocess.run() in the 'run_shell' tool handler, enabling arbitrary command execution by an unauthenticated caller."
          },
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
    }
  ]
}
```

---

*See `sarif-ai-scenarios.md` for use case navigation. `sarif-ai-triage-annotation.md` covers Scenario 2 (single tool post-processing); `sarif-ai-multi-tool-synthesis.md` covers Scenario 3 (multi-tool synthesis).*
