---
name: guide
description: Generate secure coding prompts and guides for AI tools (Claude, ChatGPT, Cursor, Copilot). Creates copy-paste ready prompts for writing secure code following KISA CII guidelines, CWE-mapped patterns, and AI security best practices. Use when "generate security guide", "AI security prompt", "secure coding guide", "safe code request", "AI secure coding".
---

# KESE Secure Coding Prompt Generator

Generate secure coding prompts based on KISA guidelines and international standards (OWASP, CWE).

## Guideline Selection

| # | Guideline | Description |
|---|-----------|-------------|
| 1 | **CII Secure Coding** | Traditional vulnerabilities (SQLi, XSS, etc.) |
| 2 | **AI Security Coding** | AI-specific (Prompt Injection, Data Poisoning, etc.) |
| 3 | **Robot Security Coding** | Robot-specific (IEC 62443, firmware, protocols) |

## CII Branch

Reference `references/cii/webapp.md` for CWE-based patterns. Generate language-specific prompts (Python, JavaScript, Java, Go, etc.) and function-specific prompts (auth, file upload, API security).

## AI Security Branch

Reference `references/ai-security/developer.md` and `references/ai-security/overview.md`. Generate prompts for: Prompt Injection defense, Data Poisoning prevention, Model Extraction protection, LLM security, RAG pipeline security.

## Usage

Copy the generated prompt into your AI assistant conversation, then request code.
