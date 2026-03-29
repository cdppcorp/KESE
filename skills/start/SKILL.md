---
name: start
description: Run a security vulnerability assessment based on KISA guidelines. Supports CII (Critical Information Infrastructure) with 560+ technical/administrative/physical items, and AI Security Guide (developer/provider/user). Use when "security assessment", "vulnerability scan", "CII audit", "KISA assessment", "AI security assessment", "infrastructure security review".
---

# KESE Security Vulnerability Assessment

Perform comprehensive security vulnerability assessment based on KISA guidelines. Automatically selects the appropriate guideline based on user context.

## Guideline Selection

| # | Guideline | Description | Items |
|---|-----------|-------------|:-----:|
| 1 | **CII (Critical Information Infrastructure)** | Technical(424)+Administrative(127)+Physical(18) | ~560 |
| 2 | **AI Security** | AI Developer/Service Provider/User requirements | ~54 |
| 3 | **Robot Security** | Industrial/Service/Medical robot checklist (11 categories) | ~103 |

### Auto-detection
- Servers, networks, databases, web services, firewalls → **CII**
- AI models, LLM, generative AI, machine learning, prompts → **AI Security**

---

## CII Branch

Read the appropriate reference file from `references/cii/` based on the target system.

| System | Reference File | Items |
|--------|---------------|:-----:|
| Unix/Linux | `references/cii/unix.md` | 67 |
| Windows Server | `references/cii/windows.md` | 64 |
| Web Service | `references/cii/web-service.md` | 26 |
| Security Equipment | `references/cii/security-equip.md` | 23 |
| Network Equipment | `references/cii/network.md` | 38 |
| Control System | `references/cii/control-system.md` | 46 |
| PC | `references/cii/pc.md` | 18 |
| DBMS | `references/cii/database.md` | 26 |
| Mobile | `references/cii/mobile.md` | 4 |
| Web Application | `references/cii/webapp.md` | 21 |
| Virtualization | `references/cii/virtualization.md` | 25 |
| Cloud | `references/cii/cloud.md` | 19 |
| Administrative | `references/cii/admin.md` | 127 |
| Physical | `references/cii/physical.md` | 18 |

### Judgment Criteria
- **Pass**: Security settings properly applied
- **Partial**: Partially implemented, improvement needed
- **Fail**: Vulnerability exists
- **N/A**: Not applicable to the environment

---

## AI Security Branch

Read from `references/ai-security/` based on target audience.

| Target | Reference File |
|--------|---------------|
| Overview | `references/ai-security/overview.md` |
| AI Developer | `references/ai-security/developer.md` |
| Service Provider | `references/ai-security/service-provider.md` |
| User | `references/ai-security/user-guide.md` |

6-stage lifecycle: Planning → Data → Model Dev → Deploy → Monitoring → Decommission

---

## Notes
- Do not modify files during assessment — read-only
- Mark N/A for technologies not present
- Provide specific remediation for each finding
