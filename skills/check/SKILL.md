---
name: check
description: Run a pre-deployment security compliance checklist based on KISA guidelines. Supports CII compliance (70 items covering accounts, access control, encryption, logging, hardening) and AI security checklists. Use when "pre-deploy check", "compliance checklist", "deployment ready", "security checklist", "AI security check".
---

# KESE Pre-Deployment Security Compliance Checklist

Run pre-deployment security checks. Auto-selects guideline based on user context.

## Guideline Selection

| # | Guideline | Description |
|---|-----------|-------------|
| 1 | **CII Compliance** | 70-item pre-deployment checklist |
| 2 | **AI Security Checklist** | AI developer/provider verification |
| 3 | **Robot Security Checklist** | Robot system 11 categories, 103 items |

Servers, infrastructure → **CII** / AI models, LLM → **AI Security**

---

## CII Branch

Load reference files from `references/cii/` based on detected environment. Check categories: Account Security (15), Access Control (15), Encryption (12), Logging (10), Service Hardening (12), Patch Management (6).

Severity: Critical (deployment blocker) → High → Medium → Low

## AI Security Branch

Load from `references/ai-security/`. Check developer (54 items), service provider, or user checklists by lifecycle phase.

---

## Rules
- Never skip Critical severity items
- Provide specific file paths and commands for fixes
- Block deployment if pass rate < 60%
