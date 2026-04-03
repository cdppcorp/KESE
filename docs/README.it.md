🌐 [한국어](../README.md) | [English](../README.md#english) | [Français](README.fr.md) | [日本語](README.ja.md) | [中文](README.zh.md) | [Русский](README.ru.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Português](README.pt.md) | [Italiano](README.it.md) | [العربية](README.ar.md) | [हिन्दी](README.hi.md) | [Türkçe](README.tr.md) | [Tiếng Việt](README.vi.md) | [ภาษาไทย](README.th.md) | [Bahasa Indonesia](README.id.md) | [Polski](README.pl.md) | [Nederlands](README.nl.md) | [Svenska](README.sv.md) | [Українська](README.uk.md)

---

# KESE - KISA Enhanced Security Evaluation Kit

Plugin per Claude Code dedicato alla valutazione delle vulnerabilita delle Infrastrutture Critiche Informatiche (CII), alla valutazione della sicurezza dell'IA, alla sicurezza robotica, alla sicurezza spaziale, alla guida alla codifica sicura e alla valutazione della sicurezza Zero Trust, basato sulle linee guida della KISA (Agenzia Coreana per Internet e la Sicurezza).

---

## Panoramica

KESE (KISA Enhanced Security Evaluation Kit) e un plugin per Claude Code che fornisce funzionalita complete di valutazione delle vulnerabilita di sicurezza basate sulle linee guida della KISA (Agenzia Coreana per Internet e la Sicurezza). Supporta le valutazioni delle Infrastrutture Critiche Informatiche (CII), della Sicurezza dell'IA, della Sicurezza Robotica, della Sicurezza Spaziale, della Codifica Sicura e della Sicurezza Zero Trust.

## Funzionalita

| Skill | Descrizione |
|-------|-------------|
| `/kesekit-start` | Eseguire la valutazione completa delle vulnerabilita di sicurezza (CII 560+ / Sicurezza IA / Sicurezza Robotica / Sicurezza Spaziale / Codifica Sicura / Zero Trust) |
| `/kesekit-check` | Checklist di conformita di sicurezza pre-distribuzione (CII / IA / Robot / Spazio / Codifica Sicura / Zero Trust) |
| `/kesekit-fix` | Generare automaticamente script di hardening e correzioni di sicurezza (CII / IA / Robot / Spazio / Codifica Sicura / Zero Trust) |
| `/kesekit-guide` | Generare prompt di codifica sicura per strumenti di IA (CII / IA / Robot / Spazio / JS·Python·Generico / Zero Trust) |

## Linee Guida Supportate

### 1. CII (Infrastrutture Critiche Informatiche) — 560+ elementi

**Valutazione Tecnica**
| Sistema | Codice | Elementi |
|---------|--------|:--------:|
| Server Unix/Linux | U-01~U-67 | 67 |
| Server Windows | W-01~W-64 | 64 |
| Servizio Web | WEB-01~WEB-26 | 26 |
| Apparecchiature di Sicurezza | S-01~S-23 | 23 |
| Apparecchiature di Rete | N-01~N-38 | 38 |
| Sistema di Controllo | C-01~C-51 | 46 |
| PC | PC-01~PC-18 | 18 |
| DBMS | D-01~D-26 | 26 |
| Dispositivo Mobile | M-01~M-04 | 4 |
| Applicazione Web | 21 codici | 21 |
| Virtualizzazione | HV-01~HV-25 | 25 |
| Cloud | CA-01~CA-19 | 19 |

**Valutazione Amministrativa**: A-1~A-127 (127 elementi, 14 domini)
**Valutazione Fisica**: P-1~P-18 (18 elementi)

### 2. Guida alla Sicurezza dell'IA — 54+ elementi

| Destinatari | Elementi | Ciclo di Vita |
|-------------|:--------:|---------------|
| Sviluppatore IA | 54 | 6 fasi (Pianificazione→Dati→Modello→Distribuzione→Monitoraggio→Dismissione) |
| Fornitore di Servizi | ~43 | 6 fasi (Pianificazione→Sviluppo→Operazioni→Manutenzione→Feedback→Dismissione) |
| Utente | 7 | Best practice di sicurezza |

### 3. Sicurezza Robotica — ~103 elementi

| Categoria | Codice | Elementi | Standard di Riferimento |
|-----------|--------|:--------:|------------------------|
| Sviluppo SW sicuro (SSDF) | SSDF-01~19 | 19 | NIST SP 800-218 |
| Sicurezza della catena di fornitura | SC-01~07 | 7 | NIST SP 800-161 |
| Identificazione e autenticazione | IA-01~11 | 11 | IEC 62443 |
| Controllo d'uso | UC-01~11 | 11 | IEC 62443 |
| Integrita del sistema | SI-01~11 | 11 | IEC 62443 |
| Protezione dei dati | DP-01~04 | 4 | IEC 62443 |
| Limitazione del flusso dati | DFR-01~02 | 2 | IEC 62443 |
| Risposta agli eventi | ER-01~03 | 3 | IEC 62443 |
| Disponibilita delle risorse | RA-01~08 | 8 | IEC 62443 |
| Resilienza informatica | CR-01~13 | 13 | EU CRA |
| Sicurezza wireless | WS-01~14 | 14 | EU RED |

Destinatari: Robot industriali / di servizio / medici (ISO 8373)

### 4. Sicurezza Spaziale — 53 elementi

| Area | Codice | Elementi | Standard di Riferimento |
|------|--------|:--------:|------------------------|
| Controllo accessi | AC-01~12 | 12 | CMMC, K-RMF |
| Identificazione e autenticazione | IA-01~02 | 2 | CMMC, NIS2 |
| Sicurezza sistemi e comunicazioni | SC-01~07 | 7 | NIST IR 8401 |
| Integrita sistemi e informazioni | SI-01~04 | 4 | NIST CSF |
| Gestione operativa sistemi/servizi | SO-01~09 | 9 | ISMS-P |
| Risposta agli incidenti | IR-01~02 | 2 | NIS2 |
| Sicurezza del personale | PS-01~02 | 2 | CMMC |
| Sicurezza fisica | PE-01~03 | 3 | K-RMF |
| Valutazione dei rischi e della sicurezza | RA-01~02 | 2 | NIST CSF |
| Governance della sicurezza | SG-01~04 | 4 | ISMS-P |
| Piani di emergenza | CP-01~02 | 2 | NIST IR 8270 |
| Gestione della catena di fornitura | SM-01~04 | 4 | CMMC, NIS2 |

Destinatari: Operatori satellitari, fornitori GSaaS, operatori di stazioni di terra, aziende della catena di fornitura spaziale

### 5. Guida alla Codifica Sicura — 46 elementi

| Categoria | Elementi | CWE | Standard di Riferimento |
|-----------|:--------:|:---:|------------------------|
| Validazione e rappresentazione dati di input | 16 | 18 | CWE/SANS Top 25, OWASP Top 10 |
| Funzionalita di sicurezza | 16 | 16 | CWE/SANS Top 25 |
| Tempo e stato | 2 | 3 | CWE |
| Gestione errori | 3 | 3 | CWE |
| Errori di codice | 3 | 3 | CWE |
| Incapsulamento | 4 | 5 | CWE |
| Uso improprio delle API | 2 | 1 | CWE |

**Linguaggi supportati:**
| Linguaggio | Elementi | Framework |
|------------|:--------:|-----------|
| Pseudo Code (generico) | 46 | Pattern indipendenti dal linguaggio |
| JavaScript | 42 | Express.js, Sequelize, Mongoose, Node.js crypto |
| Python | 46 | Django, Flask, SQLAlchemy, cryptography |

Destinatari: Sviluppatori web JavaScript/Python, utenti di strumenti IA (Claude, Cursor, Copilot), sviluppatori vibe coding

### 6. Sicurezza Zero Trust — ~421 elementi

| Elemento Fondamentale | Codice | Elementi | Maturita |
|-----------------------|--------|:--------:|----------|
| Identita | ZT-ID-01~53 | 53 | Tradizionale/Iniziale/Avanzato/Ottimale |
| Dispositivi ed Endpoint | ZT-DV-01~36 | 36 | Tradizionale/Iniziale/Avanzato/Ottimale |
| Rete | ZT-NW-01~54 | 54 | Tradizionale/Iniziale/Avanzato/Ottimale |
| Sistema | ZT-SY-01~49 | 49 | Tradizionale/Iniziale/Avanzato/Ottimale |
| Applicazioni e Carichi di Lavoro | ZT-AP-01~60 | 60 | Tradizionale/Iniziale/Avanzato/Ottimale |
| Dati | ZT-DA-01~58 | 58 | Tradizionale/Iniziale/Avanzato/Ottimale |
| Visibilita e Analisi | ZT-VA-01~43 | 43 | Tradizionale/Iniziale/Avanzato/Ottimale |
| Automazione e Orchestrazione | ZT-AU-01~43 | 43 | Tradizionale/Iniziale/Avanzato/Ottimale |
| Specifico OT/ICS | ZT-OT-01~25 | 25 | Tradizionale/Iniziale/Avanzato/Ottimale |

**4 livelli di maturita**: Tradizionale → Iniziale → Avanzato → Ottimale
**Standard di riferimento**: KISA Zero Trust Guideline 2.0, NIST SP 800-207, CISA ZT Maturity Model

Destinatari: Aziende che adottano Zero Trust, ambienti OT/ICS, organizzazioni in migrazione cloud, responsabili della valutazione della maturita della sicurezza

## Installazione

```
/plugin marketplace add cdppcorp/KESE-KIT
/plugin install kesekit@cdppcorp-KESE-KIT
```

## Utilizzo

```bash
# Avviare la valutazione completa di sicurezza
/kesekit-start

# Eseguire la checklist pre-distribuzione
/kesekit-check

# Generare script di hardening
/kesekit-fix

# Ottenere prompt di codifica sicura
/kesekit-guide
```

---

## Struttura del Progetto

```
KESE-KIT/
├── .claude-plugin/
│   └── marketplace.json              ← Metadati del plugin
├── skills/                            ← Skill in inglese
│   ├── start/
│   │   ├── SKILL.md                  ← Router (~80 righe)
│   │   ├── references/               ← Documenti descrittivi/normativi
│   │   │   ├── ai-security/          ← Panoramica, fornitori, guida utente
│   │   │   └── space-security/       ← Panoramica, scenari di minaccia
│   │   ├── templates/                ← Moduli, tabelle checklist
│   │   │   ├── cii/                  ← 14 tabelle di verifica CII
│   │   │   ├── ai-security/          ← Verifica sviluppatore IA, checklist utente
│   │   │   ├── robot-security/       ← 6 checklist sicurezza robotica
│   │   │   ├── space-security/       ← 4 tabelle verifica sicurezza spaziale
│   │   │   └── zero-trust/           ← Tabelle verifica Zero Trust
│   │   └── scripts/                  ← Script di verifica/correzione eseguibili
│   │       ├── cii/                  ← Script bash, PowerShell, SQL
│   │       └── robot-security/       ← Script firewall, SBOM, certificati
│   ├── check/
│   ├── fix/
│   └── guide/
├── skills-ko/                         ← Skill in coreano (stessa struttura)
├── 문서/                              ← PDF originali
├── authorkit/                         ← Documenti originali e artefatti di lavoro
├── docs/                              ← README in 20 lingue
├── CONTRIBUTING.md                    ← Come aggiungere linee guida
└── README.md
```

---

## Registro delle Modifiche

### v4.0.0 (2026-04-03)

**Nuova Linea Guida Aggiunta: Sicurezza Zero Trust**
- Fonte: KISA Zero Trust Guideline 2.0 (245p) + Modello di Maturita Zero Trust (182p) + Guida Zero Trust per OT (67p)
- 9 elementi fondamentali, ~421 voci di verifica, 4 livelli di maturita
- Supporto OT/ICS specifico (ZT-OT-01~25)
- Standard: KISA Zero Trust Guideline 2.0, NIST SP 800-207, CISA ZT Maturity Model

### v3.2.0 (2026-04-02)

**Nuova Linea Guida Aggiunta: Guida alla Codifica Sicura**
- Fonte: KISA Javascript Secure Coding Guide 159p + Python Secure Coding Guide 176p (revisione 2023)
- 7 categorie, 46 elementi, 49 CWE mappati
- Guida Pseudo Code generica di nuova creazione (pattern UNSAFE/SAFE indipendenti dal linguaggio)
- Esempi di codice per framework JavaScript (Express.js, Sequelize, Node.js) / Python (Django, Flask, SQLAlchemy)

### v3.0.0 (2026-04-02)

**Modifica incompatibile: formato dei comandi aggiornato**
- Tutti gli skill unificati sotto il namespace `kesekit`
- Formato comandi: `/start` → `/kesekit-start` (prefisso namespace aggiunto)

**Nuova Linea Guida Aggiunta: Sicurezza Spaziale**
- Fonte: Modello di Sicurezza Spaziale Part1 134p + Part2 223p + Guida Esplicativa 218p (MSIT/KISA)
- 12 aree, 53 voci di checklist
- Destinatari: Operatori satellitari, fornitori GSaaS, operatori stazioni di terra

### v2.0.0 (2026-03-30)

**Refactoring della Struttura — Applicazione del pattern Progressive Disclosure**

| Modifica | Prima (v1.0) | Dopo (v2.0) |
|----------|-------------|------------|
| SKILL.md | Tutta la conoscenza inline (270~465 righe) | Solo router (~50~80 righe) |
| Linee guida | Solo CII | CII + Sicurezza IA |
| Archiviazione conoscenze | Hardcoded in SKILL.md | Separato in `references/` (18 file) |
| Codici elementi | Solo alcuni elementi inclusi | Tutti gli elementi basati sulla guida 2026 |
| Estensibilita | L'aggiunta di nuove linee guida aumentava il numero di skill | 4 skill fissi, si aggiungono solo riferimenti |

**Nuova Linea Guida Aggiunta: Guida alla Sicurezza dell'IA**
- Fonte: Ministero della Scienza e delle TIC / KISA "Guida alla Sicurezza dell'Intelligenza Artificiale (IA)"
- 54 elementi di verifica per sviluppatori IA (ciclo di vita a 6 fasi)
- Requisiti di sicurezza per fornitori di servizi IA
- 7 pratiche di sicurezza per utenti IA

**Aggiornamento delle Linee Guida CII**
- Riestratta la totalita degli elementi sulla base della guida dettagliata 2026
- Integrazione del sistema di codifica degli elementi (nuovi codici come WEB, HV, CA)

### v1.0.0 (2026-03-29)

- Rilascio iniziale
- 4 skill di valutazione delle vulnerabilita CII (coreano/inglese)
- Elementi tecnici (424) + amministrativi (127) + fisici (9)

---

## Base Giuridica

- **Legge sulla Protezione delle Infrastrutture di Informazione e Comunicazione** (정보통신기반 보호법)
- **Legge sull'e-Government** (전자정부법)
- **Legge sulla Protezione dei Dati Personali** (개인정보 보호법)
- **Legge Fondamentale sull'Intelligenza Artificiale** (인공지능 기본법, in vigore dal 22/01/2026)

---

## Risorse Correlate

- [Guida Dettagliata alla Valutazione delle Vulnerabilita Tecniche della KISA](https://www.kisa.or.kr)
- [Guida alla Sicurezza dell'Intelligenza Artificiale (IA)](https://www.kisa.or.kr)
- [OWASP Top 10](https://owasp.org/Top10/)
- [OWASP Top 10 per LLM](https://owasp.org/www-project-top-10-for-large-language-model-applications/)
- [CWE/SANS Top 25](https://cwe.mitre.org/top25/)

---

## Realizzato Con

| Plugin | Descrizione |
|--------|-------------|
| [authorkit-ko](https://github.com/cdppcorp/authorkit) | Skill di supporto alla scrittura di libri - analisi PDF, estrazione struttura, revisione/riscrittura |
| [win-hooks](https://github.com/anthropics/claude-code-plugins) | Compatibilita degli hook dei plugin Claude Code per ambiente Windows |

---

## Licenza

MIT License

## Autore

CDPP Corp (https://github.com/cdppcorp)
