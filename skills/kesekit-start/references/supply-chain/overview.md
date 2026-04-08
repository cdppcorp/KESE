# SW Supply Chain Security Overview

> Source: SW 공급망 보안 가이드라인 v1.0 (2024.05, 국가정보원·과기정통부·디플정위·KISA)
> Domain: SW Supply Chain Risk Management, SBOM-based Security
> Standards: NIST SP 800-161r1 (C-SCRM), NIST SP 800-218 (SSDF), NTIA SBOM Minimum Elements

---

## 1. Supply Chain Attack Types (7 Categories)

| # | Attack Type | Description | Example |
|---|------------|-------------|---------|
| 1 | **Open Source Vulnerability** | Exploiting known CVEs in widely used OSS | Log4Shell (CVE-2021-44228) |
| 2 | **Third-party Dependency** | Compromised 3rd-party libraries/modules | event-stream malicious injection |
| 3 | **Public Repository** | Malicious packages via npm/PyPI/Maven | Typosquatting attacks |
| 4 | **Build System** | CI/CD pipeline compromise | SolarWinds Orion |
| 5 | **Update Hijacking** | Intercepting legitimate update channels | Kaseya VSA ransomware |
| 6 | **Internal Repository** | Enterprise code repository breach | Codecov credential leak |
| 7 | **Supplier/Partner** | Trusted vendor as attack vector | NotPetya via M.E.Doc |

---

## 2. C-SCRM Framework (NIST SP 800-161r1)

```
┌────────────────────────────────────────┐
│ Level 1 - Enterprise                    │
│ C-SCRM strategy, policy, governance    │
├────────────────────────────────────────┤
│ Level 2 - Mission/Business Process     │
│ Process-specific risk management       │
├────────────────────────────────────────┤
│ Level 3 - Operational                  │
│ System-level SCRM in SDLC             │
└────────────────────────────────────────┘
```

### Supply Chain Participants

| Role | Responsibilities |
|------|-----------------|
| **Developer** | Secure coding, SBOM generation, vulnerability patching |
| **Supplier** | Security verification, integrity validation, customer notification |
| **Operator** | Security requirements, acceptance testing, lifecycle management |

---

## 3. SBOM (Software Bill of Materials)

### NTIA Minimum Elements (7 Data Fields)

| Field | Description |
|-------|-------------|
| Supplier Name | Entity that created/identified the component |
| Timestamp | Date/time of SBOM assembly |
| Author Name | Entity creating the SBOM data |
| Component Name | Name assigned to the SW unit |
| Version String | Version identifier |
| Unique Identifier | Lookup key for component identification |
| Relationship | Dependency relationship (X included in Y) |

### SBOM Standards

| Standard | Organization | Focus | International |
|----------|-------------|-------|:------------:|
| SPDX | Linux Foundation | License management | ISO/IEC 5962 |
| CycloneDX | OWASP | Supply chain security | - |
| SWID | NIST/US Commerce | SW asset management | ISO/IEC 19770-2 |

### NIS-SBOM (Korea, 20 Fields)

Extended from NTIA 7 fields to 20 fields for Korean government/public sector:
- SBOM Standard, SBOM Type, CycloneDX No, SPDX Doc. ID
- SBOM ID, Product Name/Version, Component Name/Alias/Version
- Component Supplier Name, Hash, Path
- SBOM Author Name, Unique Identifier, Dependency Relationship
- Timestamp, License Name Version, Vul. DB, Vul. Info

---

## 4. Vulnerability Management Flow

```
SBOM Generate → CVE Lookup (NVD) → CVSS Scoring → Remediation Plan
     │                │                  │                │
  SCA tools      nvd.nist.gov      0.0~10.0 scale    Priority action
```

### CVSS Severity Levels

| Score | Severity | Action |
|:-----:|----------|--------|
| 9.0-10.0 | Critical | Immediate remediation |
| 7.0-8.9 | High | Urgent remediation |
| 4.0-6.9 | Medium | Planned remediation |
| 0.1-3.9 | Low | Monitor |

---

## 5. Regulatory Landscape

| Country | Regulation | SBOM Requirement | Timeline |
|---------|-----------|------------------|----------|
| USA | EO 14028 + OMB M-22-18 | SBOM submission for federal SW | Active |
| EU | Cyber Resilience Act (CRA) | SBOM for all digital products | 2026 H2 |
| Japan | METI SBOM Roadmap | Industry-specific SBOM adoption | Phased |
| Korea | NIS-SBOM | 20-field SBOM for public sector | In progress |

---

Total assessment items: **29 self-check items** (Design: 5, Development: 11, Supply: 3, Operations: 7, Maintenance: 3)
