# SBOM Vulnerability Scanning & Remediation

> Source: SW 공급망 보안 가이드라인 v1.0 (KISA)
> Checklist refs: SC-10, SC-14, SC-15, SC-23, SC-24, SC-27

---

## 1. Vulnerability Scanning with Grype (SC-14)

```bash
# Scan from SBOM file
grype sbom:sbom.json

# Scan with severity threshold (fail on high+)
grype sbom:sbom.json --fail-on high

# Output as JSON for processing
grype sbom:sbom.json -o json > vuln-report.json

# Scan source directory directly
grype dir:. --fail-on critical
```

---

## 2. Package Manager Built-in Audit (SC-10)

### Node.js

```bash
# npm audit
npm audit
npm audit --json > npm-audit.json

# Fix automatically
npm audit fix
npm audit fix --force  # including breaking changes
```

### Python

```bash
# pip-audit
pip install pip-audit
pip-audit
pip-audit -f json -o pip-audit.json

# safety
pip install safety
safety check
```

### Java

```bash
# OWASP Dependency-Check
mvn org.owasp:dependency-check-maven:check
```

### .NET

```bash
dotnet list package --vulnerable
dotnet list package --vulnerable --include-transitive
```

### Go

```bash
# govulncheck
go install golang.org/x/vuln/cmd/govulncheck@latest
govulncheck ./...
```

---

## 3. NVD/CVE Lookup (SC-15, SC-23)

```bash
# Search NVD for specific CVE
curl -s "https://services.nvd.nist.gov/rest/json/cves/2.0?cveId=CVE-2021-44228" | python -m json.tool

# Search by keyword
curl -s "https://services.nvd.nist.gov/rest/json/cves/2.0?keywordSearch=log4j" | python -m json.tool | head -50

# Check CISA KEV (Known Exploited Vulnerabilities)
curl -s "https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json" | python -c "
import json, sys
data = json.load(sys.stdin)
for v in data['vulnerabilities'][:5]:
    print(f\"{v['cveID']} | {v['vendorProject']} | {v['product']} | Due: {v['dueDate']}\")
"
```

---

## 4. CVSS Severity Assessment (SC-15)

| CVSS Score | Severity | Required Action | SLA |
|:----------:|----------|----------------|:---:|
| 9.0-10.0 | Critical | Immediate patch/mitigation | 24h |
| 7.0-8.9 | High | Urgent remediation | 7d |
| 4.0-6.9 | Medium | Planned remediation | 30d |
| 0.1-3.9 | Low | Monitor, next release | 90d |

---

## 5. Vulnerability Response Record (SC-24, SC-28)

| Field | Description |
|-------|-------------|
| CVE ID | Vulnerability identifier (e.g., CVE-2021-44228) |
| Component | Affected component name and version |
| CVSS Score | Severity score (0.0-10.0) |
| KEV Status | Whether listed in CISA KEV |
| Business Impact | Affected services/data/operations |
| EoS Status | End-of-Support status of component |
| Priority | P0 (Critical) / P1 (High) / P2 (Medium) / P3 (Low) |
| Remediation | Patch / Upgrade / Virtual patch / Isolate / Accept risk |
| SLA | Target remediation date |
| Owner | Responsible team and person |
| Verification | Re-scan result, regression test link |
| Status | Planned / In Progress / Completed / Exception (approved) |

---

## 6. License Scanning (SC-19)

```bash
# License check with Syft + Grype
syft dir:. -o cyclonedx-json | python -c "
import json, sys
data = json.load(sys.stdin)
for c in data.get('components', []):
    licenses = c.get('licenses', [])
    lic_names = [l.get('license', {}).get('id', 'Unknown') for l in licenses]
    print(f\"{c['name']}@{c.get('version','?')} : {', '.join(lic_names) or 'No license'}\")
"

# Check for copyleft licenses (GPL risk)
syft dir:. -o cyclonedx-json | python -c "
import json, sys
data = json.load(sys.stdin)
copyleft = ['GPL', 'LGPL', 'AGPL', 'MPL']
for c in data.get('components', []):
    for l in c.get('licenses', []):
        lid = l.get('license', {}).get('id', '')
        if any(cl in lid.upper() for cl in copyleft):
            print(f'WARNING: {c[\"name\"]}@{c.get(\"version\",\"?\")} uses {lid}')
"
```
