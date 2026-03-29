---
name: fix
description: Auto-fix security vulnerabilities found in CII and AI systems. Generates hardening scripts for Unix/Linux, Windows, web servers, databases, and AI systems. Applies secure configurations based on KISA guidelines. Use when "fix vulnerabilities", "secure the system", "apply hardening", "server hardening", "AI security fix".
---

# KESE Vulnerability Auto-Fix

Generate and apply fixes based on vulnerability assessment results. Auto-selects guideline.

## Guideline Selection

| # | Guideline | Description |
|---|-----------|-------------|
| 1 | **CII Hardening** | Platform-specific hardening scripts |
| 2 | **AI Security Fixes** | AI system security hardening |
| 3 | **Robot Security Fixes** | Robot system hardening (IEC 62443, CRA, RED) |

## CII Branch

Load reference from `references/cii/` → generate hardening scripts saved to `scripts/kese-hardening/`.

## AI Security Branch

Load from `references/ai-security/` → generate security hardening code for AI pipelines, model security, API protection, LLM guardrails.

## Notes
- Always backup before applying fixes
- Test in non-production first
- Document all changes for compliance audit
