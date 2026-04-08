# SBOM Generation Scripts

> Source: SW 공급망 보안 가이드라인 v1.0 (KISA)
> Checklist refs: SC-03, SC-10, SC-13, SC-14, SC-16

---

## 1. SBOM Generation with Syft (SC-10, SC-14)

```bash
# Source code directory scan
syft dir:. -o cyclonedx-json > sbom-cyclonedx.json
syft dir:. -o spdx-json > sbom-spdx.json

# Container image scan
syft <image-name>:<tag> -o cyclonedx-json > sbom-container.json

# Specific package manager lockfile
syft file:package-lock.json -o cyclonedx-json > sbom.json
```

---

## 2. Language-Specific SBOM Tools (SC-10)

### Node.js (npm/yarn)

```bash
# CycloneDX npm plugin
npm install -g @cyclonedx/cyclonedx-npm
cyclonedx-npm --output-file sbom.json

# yarn
npm install -g @cyclonedx/cyclonedx-npm
cyclonedx-npm --package-lock-only --output-file sbom.json
```

### Python (pip/poetry)

```bash
# CycloneDX Python
pip install cyclonedx-bom
cyclonedx-py requirements -i requirements.txt -o sbom.json --format json

# Poetry
cyclonedx-py poetry -o sbom.json --format json
```

### Java (Maven/Gradle)

```bash
# Maven CycloneDX plugin
mvn org.cyclonedx:cyclonedx-maven-plugin:makeBom

# Gradle
gradle cyclonedxBom
```

### .NET (NuGet)

```bash
dotnet tool install --global CycloneDX
dotnet CycloneDX <project>.csproj -o sbom.json -j
```

### Go

```bash
# CycloneDX Go module
cyclonedx-gomod mod -json -output sbom.json
```

---

## 3. SBOM Validation (SC-16, V-1~V-5)

```bash
# Validate CycloneDX format
npm install -g @cyclonedx/cyclonedx-cli
cyclonedx validate --input-file sbom.json --input-format json

# Check component count
cat sbom.json | python -c "
import json, sys
data = json.load(sys.stdin)
comps = data.get('components', [])
print(f'Components: {len(comps)}')
for c in comps[:10]:
    print(f'  {c.get(\"name\", \"?\")}@{c.get(\"version\", \"?\")} [{c.get(\"licenses\", [{}])}]')
"
```

---

## 4. Cross-Validation with Multiple Tools (V-3)

```bash
# Generate SBOM with two different tools
syft dir:. -o cyclonedx-json > sbom-syft.json
cyclonedx-npm --output-file sbom-cdx.json

# Compare component counts
echo "Syft components:"
cat sbom-syft.json | python -c "import json,sys; print(len(json.load(sys.stdin).get('components',[])))"
echo "CycloneDX-npm components:"
cat sbom-cdx.json | python -c "import json,sys; print(len(json.load(sys.stdin).get('components',[])))"
```

---

## 5. CI/CD Integration (SC-11, SC-13)

### GitHub Actions

```yaml
name: SBOM & Security
on: [push, pull_request]
jobs:
  sbom:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Generate SBOM
        uses: anchore/sbom-action@v0
        with:
          format: cyclonedx-json
          output-file: sbom.json
      - name: Scan Vulnerabilities
        uses: anchore/scan-action@v4
        with:
          sbom: sbom.json
          fail-build: true
          severity-cutoff: high
      - name: Archive SBOM
        uses: actions/upload-artifact@v4
        with:
          name: sbom
          path: sbom.json
```

### GitLab CI/CD

```yaml
sbom-scan:
  stage: test
  image: anchore/syft:latest
  script:
    - syft dir:. -o cyclonedx-json > sbom.json
    - grype sbom:sbom.json --fail-on high
  artifacts:
    paths:
      - sbom.json
```
