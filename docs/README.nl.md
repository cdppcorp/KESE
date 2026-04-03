🌐 [한국어](../README.md) | [English](../README.md#english) | [Français](README.fr.md) | [日本語](README.ja.md) | [中文](README.zh.md) | [Русский](README.ru.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Português](README.pt.md) | [Italiano](README.it.md) | [العربية](README.ar.md) | [हिन्दी](README.hi.md) | [Türkçe](README.tr.md) | [Tiếng Việt](README.vi.md) | [ภาษาไทย](README.th.md) | [Bahasa Indonesia](README.id.md) | [Polski](README.pl.md) | [Nederlands](README.nl.md) | [Svenska](README.sv.md) | [Українська](README.uk.md)

---

# KESE - KISA Enhanced Security Evaluation Kit

Een Claude Code skill-plugin voor kwetsbaarheidsanalyse van kritieke informatie-infrastructuur (CII), AI-beveiligingsevaluatie, robotbeveiliging, ruimtevaartbeveiliging, secure coding en Zero Trust-evaluatie.

---

## Overzicht

KESE (KISA Enhanced Security Evaluation Kit) is een Claude Code-plugin die uitgebreide mogelijkheden biedt voor kwetsbaarheidsanalyse op basis van de richtlijnen van KISA (Korea Internet & Security Agency). Het ondersteunt evaluaties van kritieke informatie-infrastructuur (CII), AI-beveiliging, robotbeveiliging, ruimtevaartbeveiliging, secure coding en Zero Trust-evaluatie.

## Functies

| Skill | Beschrijving |
|-------|-------------|
| `/kesekit-start` | Volledige beveiligingskwetsbaarheidsanalyse uitvoeren (CII 560+ / AI / Robot / Ruimtevaart / Secure Coding / Zero Trust) |
| `/kesekit-check` | Beveiligingschecklist voor compliance voor implementatie (CII / AI / Robot / Ruimtevaart / Secure Coding / Zero Trust) |
| `/kesekit-fix` | Automatisch hardening-scripts en beveiligingsoplossingen genereren (CII / AI / Robot / Ruimtevaart / Secure Coding / Zero Trust) |
| `/kesekit-guide` | Secure coding-prompts genereren voor AI-tools (CII / AI / Robot / Ruimtevaart / JS·Python·Algemeen / Zero Trust) |

## Ondersteunde richtlijnen

### 1. CII (Kritieke Informatie-Infrastructuur) — 560+ items

**Technische kwetsbaarheidsevaluatie**
| Systeem | Code | Aantal items |
|---------|------|:------:|
| Unix/Linux-server | U-01~U-67 | 67 |
| Windows-server | W-01~W-64 | 64 |
| Webservice | WEB-01~WEB-26 | 26 |
| Beveiligingsapparatuur | S-01~S-23 | 23 |
| Netwerkapparatuur | N-01~N-38 | 38 |
| Besturingssysteem | C-01~C-51 | 46 |
| PC | PC-01~PC-18 | 18 |
| DBMS | D-01~D-26 | 26 |
| Mobiel | M-01~M-04 | 4 |
| Web Application | 21 codes | 21 |
| Virtualisatie | HV-01~HV-25 | 25 |
| Cloud | CA-01~CA-19 | 19 |

**Organisatorische kwetsbaarheidsevaluatie**: A-1~A-127 (127 items, 14 domeinen)
**Fysieke kwetsbaarheidsevaluatie**: P-1~P-18 (18 items)

### 2. AI-beveiligingsgids — 54+ items

| Doelgroep | Aantal items | Levenscyclus |
|-----------|:------:|---------|
| AI-ontwikkelaar | 54 | 6 fasen (Planning→Data→Modelontwikkeling→Implementatie→Monitoring→Buitengebruikstelling) |
| AI-serviceprovider | ~43 | 6 fasen (Planning→Ontwikkeling→Beheer→Onderhoud→Feedback→Buitengebruikstelling) |
| AI-gebruiker | 7 | Beveiligingsrichtlijnen |

### 3. Robotbeveiliging — ~103 items

| Categorie | Code | Aantal items | Referentiestandaard |
|-----------|------|:------:|---------------------|
| Veilige SW-ontwikkeling (SSDF) | SSDF-01~19 | 19 | NIST SP 800-218 |
| Toeleveringsketenbeveiliging | SC-01~07 | 7 | NIST SP 800-161 |
| Identificatie en authenticatie | IA-01~11 | 11 | IEC 62443 |
| Gebruikscontrole | UC-01~11 | 11 | IEC 62443 |
| Systeemintegriteit | SI-01~11 | 11 | IEC 62443 |
| Gegevensbescherming | DP-01~04 | 4 | IEC 62443 |
| Beperking gegevensstromen | DFR-01~02 | 2 | IEC 62443 |
| Incidentrespons | ER-01~03 | 3 | IEC 62443 |
| Beschikbaarheid van middelen | RA-01~08 | 8 | IEC 62443 |
| Cyberweerbaarheid | CR-01~13 | 13 | EU CRA |
| Draadloze beveiliging | WS-01~14 | 14 | EU RED |

Doelgroep: Industriele robots / Servicerobot / Medische robots (ISO 8373)

### 4. Ruimtevaartbeveiliging — 53 items

| Domein | Code | Aantal items | Referentiestandaard |
|--------|------|:------:|---------------------|
| Toegangscontrole | AC-01~12 | 12 | CMMC, K-RMF |
| Identificatie en authenticatie | IA-01~02 | 2 | CMMC, NIS2 |
| Systeem- en communicatiebeveiliging | SC-01~07 | 7 | NIST IR 8401 |
| Systeem- en informatie-integriteit | SI-01~04 | 4 | NIST CSF |
| Systeem-/dienstoperatiebeheer | SO-01~09 | 9 | ISMS-P |
| Incidentrespons | IR-01~02 | 2 | NIS2 |
| Personeelsbeveiliging | PS-01~02 | 2 | CMMC |
| Fysieke beveiliging | PE-01~03 | 3 | K-RMF |
| Risico- en beveiligingsevaluatie | RA-01~02 | 2 | NIST CSF |
| Beveiligingsgovernance | SG-01~04 | 4 | ISMS-P |
| Noodplan | CP-01~02 | 2 | NIST IR 8270 |
| Toeleveringsketenbeheer | SM-01~04 | 4 | CMMC, NIS2 |

Doelgroep: Satellietoperators, GSaaS-providers, Grondstationoperators, Bedrijven in de ruimtevaarttoeleveringsketen

### 5. Secure coding-gids — 46 items

| Categorie | Aantal items | Aantal CWE | Referentiestandaard |
|-----------|:------:|:------:|---------------------|
| Invoervalidatie en -representatie | 16 | 18 | CWE/SANS Top 25, OWASP Top 10 |
| Beveiligingsfuncties | 16 | 16 | CWE/SANS Top 25 |
| Tijd en status | 2 | 3 | CWE |
| Foutafhandeling | 3 | 3 | CWE |
| Codefouten | 3 | 3 | CWE |
| Inkapseling | 4 | 5 | CWE |
| API-misbruik | 2 | 1 | CWE |

**Ondersteunde talen:**
| Taal | Aantal items | Framework |
|------|:------:|-----------|
| Pseudo Code (Algemeen) | 46 | Taalonafhankelijke patronen |
| JavaScript | 42 | Express.js, Sequelize, Mongoose, Node.js crypto |
| Python | 46 | Django, Flask, SQLAlchemy, cryptography |

Doelgroep: JavaScript/Python-webontwikkelaars, AI-toolgebruikers (Claude, Cursor, Copilot), Vibe Coding-ontwikkelaars

### 6. Zero Trust-beveiliging — ~421 items

| Kernelement | Code | Aantal items | Volwassenheid |
|-------------|------|:------:|-------------|
| Identiteit | ZT-ID-01~53 | 53 | Traditioneel/Initieel/Geavanceerd/Optimaal |
| Apparaat & Eindpunt | ZT-DV-01~36 | 36 | Traditioneel/Initieel/Geavanceerd/Optimaal |
| Netwerk | ZT-NW-01~54 | 54 | Traditioneel/Initieel/Geavanceerd/Optimaal |
| Systeem | ZT-SY-01~49 | 49 | Traditioneel/Initieel/Geavanceerd/Optimaal |
| Applicatie & Workload | ZT-AP-01~60 | 60 | Traditioneel/Initieel/Geavanceerd/Optimaal |
| Data | ZT-DA-01~58 | 58 | Traditioneel/Initieel/Geavanceerd/Optimaal |
| Zichtbaarheid & Analyse | ZT-VA-01~43 | 43 | Traditioneel/Initieel/Geavanceerd/Optimaal |
| Automatisering & Orkestratie | ZT-AU-01~43 | 43 | Traditioneel/Initieel/Geavanceerd/Optimaal |
| OT/ICS-specifiek | ZT-OT-01~25 | 25 | Traditioneel/Initieel/Geavanceerd/Optimaal |

**4 volwassenheidsniveaus**: Traditioneel (Traditional) → Initieel (Initial) → Geavanceerd (Advanced) → Optimaal (Optimal)
**Referentiestandaarden**: KISA Zero Trust Guideline 2.0, NIST SP 800-207, CISA ZT Maturity Model

Doelgroep: Organisaties die Zero Trust implementeren, OT/ICS-omgevingen, Organisaties die naar de cloud migreren, Verantwoordelijken voor beveiligingsvolwassenheidsevaluatie

## Installatie

```
/plugin marketplace add cdppcorp/KESE-KIT
/plugin install kesekit@cdppcorp-KESE-KIT
```

## Gebruik

```bash
# Volledige beveiligingsevaluatie starten
/kesekit-start

# Checklist voor implementatie uitvoeren
/kesekit-check

# Hardening-scripts genereren
/kesekit-fix

# Secure coding-prompts ophalen
/kesekit-guide
```

---

## Projectstructuur

```
KESE-KIT/
├── .claude-plugin/
│   └── marketplace.json              ← Plugin-metadata
├── skills/                            ← Engelstalige skills
│   ├── start/
│   │   ├── SKILL.md                  ← Router (~80 regels)
│   │   ├── references/               ← Beschrijvings-/criteriadocumenten
│   │   │   ├── ai-security/          ← Overzicht, serviceproviders, gebruikersgids
│   │   │   └── space-security/       ← Overzicht, bedreigingsscenario's toeleveringsketen
│   │   ├── templates/                ← Formulieren, checklisttabellen
│   │   │   ├── cii/                  ← CII 14 inspectietabellen
│   │   │   ├── ai-security/          ← AI-ontwikkelaar, gebruikerchecklists
│   │   │   ├── robot-security/       ← 6 robotbeveiligingschecklists
│   │   │   ├── space-security/       ← 4 ruimtevaarttabellen
│   │   │   └── zero-trust/           ← Zero Trust-checklisttabellen
│   │   └── scripts/                  ← Inspectie-/herstelscripts
│   │       ├── cii/                  ← bash, PowerShell, SQL
│   │       └── robot-security/       ← Firewall, SBOM, certificaten
│   ├── check/
│   ├── fix/
│   └── guide/
├── skills-ko/                         ← Koreaanse skills (zelfde structuur)
├── 문서/                              ← Originele PDF's
├── authorkit/                         ← Brondocumenten en werkproducten
├── docs/                              ← README's in 20 talen
└── README.md
```

---

## Wijzigingsgeschiedenis

### v4.0.0 (2026-04-03)

**Nieuwe richtlijn: Zero Trust-beveiliging — ~421 items**
- Bron: KISA Zero Trust Guideline 2.0 (245 pag.) + Volwassenheidsmodel-gids (182 pag.) + OT-implementatiegids (67 pag.)
- 9 kernelementen, ~421 checklistitems, 4 volwassenheidsniveaus
- Standaarden: KISA Zero Trust Guideline 2.0, NIST SP 800-207, CISA ZT Maturity Model

### v3.2.0 (2026-04-02)

**Nieuwe richtlijn: Secure Coding**
- Bron: KISA Javascript Secure Coding Guide 159 pag. + Python Secure Coding Guide 176 pag. (herziene editie 2023)
- 7 categorieen, 46 items, 49 CWE
- JavaScript / Python / Pseudo Code (algemeen)

### v3.0.0 (2026-04-02)

**Breaking Change: Opdrachtformaat gewijzigd**
- Alle skills samengevoegd in enkele `kesekit`-namespace
- Opdrachtformaat: `/start` → `/kesekit-start`

**Nieuwe richtlijn: Ruimtevaartbeveiliging**
- Bron: Space Security Model Part1 134 pag. + Part2 223 pag. + Toelichting 218 pag.
- 12 domeinen, 53 checklistitems

### v2.0.0 (2026-03-30)

**Structuurherziening — Progressive Disclosure-patroon toegepast**

| Wijziging | Vorige versie (v1.0) | Huidige versie (v2.0) |
|-----------|------------|------------|
| SKILL.md | Alle kennis inline (270~465 regels) | Alleen router (~50~80 regels) |
| Richtlijnen | Alleen CII ondersteund | CII + AI-beveiliging ondersteund |
| Kennisopslag | Hardcoded in SKILL.md | Gescheiden in `references/` (18 bestanden) |
| Itemcodes | Slechts enkele items opgenomen | Alle items op basis van de gids van 2026 |
| Uitbreidbaarheid | Meer skills nodig bij nieuwe richtlijnen | 4 skills vast, alleen references toevoegen |

**Nieuwe richtlijn toegevoegd: AI-beveiligingsgids**
- Bron: Ministerie van Wetenschap en ICT / KISA "Artificial Intelligence (AI) Security Guide"
- 54 verificatie-items voor AI-ontwikkelaars (6-fasen levenscyclus)
- Beveiligingsvereisten voor AI-serviceproviders
- 7 beveiligingsrichtlijnen voor AI-gebruikers

**CII-richtlijnupdate**
- Alle items opnieuw geextraheerd op basis van de gedetailleerde gids van 2026
- Nieuw codesysteem weergegeven (WEB, HV, CA en andere nieuwe codes)

### v1.0.0 (2026-03-29)

- Eerste release
- 4 CII-kwetsbaarheidsanalyse-skills (Koreaans/Engels)
- Technisch (424) + Organisatorisch (127) + Fysiek (9) items

---

## Juridische grondslag

- **Wet op de bescherming van informatie- en communicatie-infrastructuur** (Act on Protection of Information and Communications Infrastructure)
- **Wet op elektronisch bestuur** (e-Government Act)
- **Wet op de bescherming van persoonsgegevens** (Personal Information Protection Act)
- **AI-basiswet** (AI Basic Act, in werking getreden op 22-01-2026)

---

## Gerelateerde bronnen

- [KISA Gedetailleerde gids voor technische kwetsbaarheidsanalyse](https://www.kisa.or.kr)
- [Artificial Intelligence (AI) Security Guide](https://www.kisa.or.kr)
- [OWASP Top 10](https://owasp.org/Top10/)
- [OWASP Top 10 for LLM](https://owasp.org/www-project-top-10-for-large-language-model-applications/)
- [CWE/SANS Top 25](https://cwe.mitre.org/top25/)

---

## Gebouwd met

| Plugin | Beschrijving |
|--------|-------------|
| [authorkit-ko](https://github.com/cdppcorp/authorkit) | Skill voor ondersteuning bij het schrijven van boeken - PDF-analyse, structuurextractie, revisie/herschrijving |
| [win-hooks](https://github.com/anthropics/claude-code-plugins) | Compatibiliteit met Claude Code plugin-hooks in Windows-omgeving |

---

## Licentie

MIT License

## Auteur

CDPP Corp (https://github.com/cdppcorp)
