# SW Supply Chain Security Assessment Overview

> Domain: SW Supply Chain Security (6 categories, 29 items)
> Source: SW 공급망 보안 가이드라인 v1.0 (국정원·과기정통부·KISA, 2024.05)
> Standards: NIST SP 800-161r1, NIST SP 800-218, NTIA SBOM

---

## Assessment Categories

| # | Category | Items | Scope |
|---|----------|:-----:|-------|
| 1 | Design Phase | 5 | Roles, training, SBOM planning, environment, security specs |
| 2 | Development Phase | 11 | Secure coding, libraries, build security, SBOM management |
| 3 | Supply/Distribution Phase | 3 | Integrity, archival, SBOM delivery |
| 4 | Deployment & Operations Phase | 7 | Requirements, verification, monitoring, SBOM review |
| 5 | Maintenance Phase | 3 | Updates, history, SBOM refresh |
| **Total** | | **29** | |

## Judgment Criteria

| Result | Condition |
|--------|-----------|
| **Pass** | Item requirement fully met with evidence |
| **Partial** | Partially implemented or missing documentation |
| **Fail** | Not implemented or no evidence |
| **N/A** | Not applicable to this environment |

## Severity Classification

| Severity | Description | Items |
|----------|-------------|:-----:|
| **Critical** | SBOM not generated, no vulnerability scanning | SC-10, SC-14, SC-15 |
| **High** | No integrity verification, no access control | SC-07, SC-08, SC-09, SC-17, SC-22 |
| **Medium** | Missing training, incomplete documentation | SC-02, SC-05, SC-13, SC-16 |
| **Low** | Process improvement opportunities | SC-01, SC-03, SC-04 |

## Assessment Scope Detection

| Context | Indicators |
|---------|-----------|
| SBOM Required | npm/pip/maven project, government/public sector delivery |
| Supply Chain Risk | External libraries, OSS components, 3rd-party dependencies |
| Regulatory | US federal SW, EU digital product, Korean public sector |
| Vibe Coding | AI-generated code with auto-imported dependencies |

Load `templates/supply-chain/sbom-checklist.md` for the full 29-item assessment.
