# SW Supply Chain Security Self-Assessment Checklist

> Source: SW 공급망 보안 가이드라인 v1.0 (국정원·과기정통부·KISA, 2024.05)
> Standards: NIST SP 800-161r1, NIST SP 800-218
> Total: 29 items (Design 5 + Development 11 + Supply 3 + Operations 7 + Maintenance 3)

---

## 1. Design Phase (5 items)

| ID | Item | Detail | Severity |
|----|------|--------|----------|
| SC-01 | Roles & responsibilities for secure development defined | Organization notice with security roles and responsibilities | Low |
| SC-02 | Security training provided to developers | Supply chain security, secure coding training records | Medium |
| SC-03 | Supply chain security considered in design | Configuration management, SBOM generation & management plan | Low |
| SC-04 | Development environment security managed | OS/antivirus update status on dev endpoints | Low |
| SC-05 | Key security items identified and documented | Data protection level, encryption, authentication, access control specs | Medium |

---

## 2. Development Phase (11 items)

| ID | Item | Detail | Severity |
|----|------|--------|----------|
| SC-06 | Secure coding practices followed | Secure coding verification during source/build | Medium |
| SC-07 | Default security settings reviewed before deployment | SSL, access permissions, repository encryption enabled | High |
| SC-08 | External library security verified on import | Malware/integrity check for external libraries | High |
| SC-09 | Internal repository access restricted to authorized users | Source code management system access control | High |
| SC-10 | OSS and internal code continuously scanned for vulnerabilities | Vulnerability scan logs available | **Critical** |
| SC-11 | Automated security tests in build process | CI/CD pipeline includes security testing | Medium |
| SC-12 | Compiler/interpreter security options enabled | Build options with security features activated | Medium |
| SC-13 | Build artifacts preserved | Executables, compile logs, SBOM, test results archived | Medium |
| SC-14 | SBOM component vulnerabilities checked | Vulnerability identification from SBOM results | **Critical** |
| SC-15 | Severe vulnerabilities have validation process | CVSS 7.0+ components verified for exploitability | **Critical** |
| SC-16 | SBOM creation history maintained | SBOM generation records retained | Medium |

---

## 3. Supply/Distribution Phase (3 items)

| ID | Item | Detail | Severity |
|----|------|--------|----------|
| SC-17 | SW integrity verification data provided | Code signing, hash values delivered | High |
| SC-18 | Source code, libraries, OSS info securely archived | Secure storage of source materials | Medium |
| SC-19 | SBOM, vulnerability, license info shared with customer | SBOM utilization for transparency | Medium |

---

## 4. Deployment & Operations Phase (7 items)

| ID | Item | Detail | Severity |
|----|------|--------|----------|
| SC-20 | Supply chain security requirements manual exists | SBOM provision, vulnerability remediation, update requirements | Medium |
| SC-21 | Security requirements verified at contract | Compliance confirmation | Medium |
| SC-22 | SW integrity verified via code signing/hash | Code signature and hash validation | High |
| SC-23 | CVE monitoring for deployed SW | Known vulnerability alerts monitored | High |
| SC-24 | Severe vulnerability response process exists | Remediation request procedure to supplier | High |
| SC-25 | SBOM received for externally developed SW | SBOM review for outsourced SW | Medium |
| SC-26 | External code scanned for vulnerabilities | Security vulnerability check for outsourced code | High |

---

## 5. Maintenance Phase (3 items)

| ID | Item | Detail | Severity |
|----|------|--------|----------|
| SC-27 | Security updates regularly checked | Patch application status | High |
| SC-28 | Vulnerability remediation history maintained | Remediation action documentation | Medium |
| SC-29 | SBOM regularly updated | SBOM refreshed on SW changes | Medium |

---

## Scoring

| Pass Rate | Result |
|:---------:|--------|
| >= 80% | **PASS** - Supply chain security posture adequate |
| 60-79% | **CONDITIONAL** - Remediation plan required |
| < 60% | **FAIL** - Deployment blocked, critical gaps |

Critical items (SC-10, SC-14, SC-15) must ALL pass regardless of overall score.

---

## SBOM Validity Verification Checklist

| # | Check | Description |
|---|-------|-------------|
| V-1 | Developer confirmation | Compare SBOM data with actual product info (language, framework, OSS) |
| V-2 | Completeness check | Verify no missing fields per CycloneDX/SPDX standard |
| V-3 | Cross-validation | Compare results from 2+ SBOM tools |
| V-4 | Source vs Binary | Compare source-based and binary-based SBOM results |
| V-5 | Hidden components | Check for undiscovered OSS components post-installation |
