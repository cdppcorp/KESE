🌐 [한국어](../README.md) | [English](../README.md#english) | [Français](README.fr.md) | [日本語](README.ja.md) | [中文](README.zh.md) | [Русский](README.ru.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [Português](README.pt.md) | [Italiano](README.it.md) | [العربية](README.ar.md) | [हिन्दी](README.hi.md) | [Türkçe](README.tr.md) | [Tiếng Việt](README.vi.md) | [ภาษาไทย](README.th.md) | [Bahasa Indonesia](README.id.md) | [Polski](README.pl.md) | [Nederlands](README.nl.md) | [Svenska](README.sv.md) | [Українська](README.uk.md)

---

# KESE - KISA Enhanced Security Evaluation Kit

Plugin de Claude Code para el analisis y evaluacion de vulnerabilidades en Infraestructuras Criticas de Informacion (CII), evaluacion de seguridad de IA, inspeccion de seguridad de robots, inspeccion de seguridad espacial, guia de codificacion segura y evaluacion de seguridad Zero Trust.

---

## Descripcion general

KESE (KISA Enhanced Security Evaluation Kit) es un plugin de Claude Code que ofrece capacidades integrales de evaluacion de vulnerabilidades basadas en las directrices de KISA (Agencia de Internet y Seguridad de Corea). Soporta evaluaciones CII, seguridad de IA, seguridad de robots, seguridad espacial, codificacion segura y evaluacion de seguridad Zero Trust.

## Funcionalidades

| Skill | Descripcion |
|-------|-------------|
| `/kesekit-start` | Ejecutar evaluacion completa de vulnerabilidades de seguridad (CII 560+ / Seguridad IA / Seguridad de robots / Seguridad espacial / Codificacion segura / Zero Trust) |
| `/kesekit-check` | Lista de verificacion de cumplimiento de seguridad previo al despliegue (CII / IA / Robots / Espacio / Codificacion segura / Zero Trust) |
| `/kesekit-fix` | Generacion automatica de scripts de hardening y correcciones de seguridad (CII / IA / Robots / Espacio / Codificacion segura / Zero Trust) |
| `/kesekit-guide` | Generar prompts de codificacion segura para herramientas de IA (CII / IA / Robots / Espacio / JS·Python·Generico / Zero Trust) |

## Directrices soportadas

### 1. CII (Infraestructura Critica de Informacion) — 560+ elementos

**Evaluacion tecnica**
| Sistema | Codigo | Elementos |
|---------|--------|:---------:|
| Servidores Unix/Linux | U-01~U-67 | 67 |
| Servidores Windows | W-01~W-64 | 64 |
| Servicios web | WEB-01~WEB-26 | 26 |
| Equipos de seguridad | S-01~S-23 | 23 |
| Equipos de red | N-01~N-38 | 38 |
| Sistemas de control | C-01~C-51 | 46 |
| PC | PC-01~PC-18 | 18 |
| SGBD | D-01~D-26 | 26 |
| Dispositivos moviles | M-01~M-04 | 4 |
| Aplicaciones web | 21 codigos | 21 |
| Virtualizacion | HV-01~HV-25 | 25 |
| Nube | CA-01~CA-19 | 19 |

**Evaluacion administrativa**: A-1~A-127 (127 elementos, 14 dominios)
**Evaluacion fisica**: P-1~P-18 (18 elementos)

### 2. Guia de seguridad de IA — 54+ elementos

| Destinatario | Elementos | Ciclo de vida |
|--------------|:---------:|---------------|
| Desarrollador de IA | 54 | 6 etapas (Planificacion→Datos→Modelo→Despliegue→Monitoreo→Desmantelamiento) |
| Proveedor de servicios | ~43 | 6 etapas (Planificacion→Desarrollo→Operaciones→Mantenimiento→Retroalimentacion→Desmantelamiento) |
| Usuario | 7 | Mejores practicas de seguridad |

### 3. Seguridad de robots — ~103 elementos

| Categoria | Codigo | Elementos | Estandares de referencia |
|-----------|--------|:---------:|--------------------------|
| Desarrollo SW seguro (SSDF) | SSDF-01~19 | 19 | NIST SP 800-218 |
| Seguridad de la cadena de suministro | SC-01~07 | 7 | NIST SP 800-161 |
| Identificacion y autenticacion | IA-01~11 | 11 | IEC 62443 |
| Control de uso | UC-01~11 | 11 | IEC 62443 |
| Integridad del sistema | SI-01~11 | 11 | IEC 62443 |
| Proteccion de datos | DP-01~04 | 4 | IEC 62443 |
| Restriccion de flujo de datos | DFR-01~02 | 2 | IEC 62443 |
| Respuesta a eventos | ER-01~03 | 3 | IEC 62443 |
| Disponibilidad de recursos | RA-01~08 | 8 | IEC 62443 |
| Ciber-resiliencia | CR-01~13 | 13 | EU CRA |
| Seguridad inalambrica | WS-01~14 | 14 | EU RED |

Destinatarios: robots industriales / de servicio / medicos (ISO 8373)

### 4. Seguridad espacial — 53 elementos

| Area | Codigo | Elementos | Estandares de referencia |
|------|--------|:---------:|--------------------------|
| Control de acceso | AC-01~12 | 12 | CMMC, K-RMF |
| Identificacion y autenticacion | IA-01~02 | 2 | CMMC, NIS2 |
| Seguridad de sistemas y comunicaciones | SC-01~07 | 7 | NIST IR 8401 |
| Integridad de sistemas e informacion | SI-01~04 | 4 | NIST CSF |
| Gestion de operaciones de sistema/servicio | SO-01~09 | 9 | ISMS-P |
| Respuesta a incidentes | IR-01~02 | 2 | NIS2 |
| Seguridad del personal | PS-01~02 | 2 | CMMC |
| Seguridad fisica | PE-01~03 | 3 | K-RMF |
| Evaluacion de riesgos y seguridad | RA-01~02 | 2 | NIST CSF |
| Gobernanza de seguridad | SG-01~04 | 4 | ISMS-P |
| Plan de contingencia | CP-01~02 | 2 | NIST IR 8270 |
| Gestion de la cadena de suministro | SM-01~04 | 4 | CMMC, NIS2 |

Destinatarios: operadores de satelites, proveedores GSaaS, operadores de estaciones terrestres, empresas de la cadena de suministro espacial

### 5. Guia de codificacion segura — 46 elementos

| Categoria | Elementos | CWE | Estandares de referencia |
|-----------|:---------:|:---:|--------------------------|
| Validacion de datos de entrada y representacion | 16 | 18 | CWE/SANS Top 25, OWASP Top 10 |
| Funciones de seguridad | 16 | 16 | CWE/SANS Top 25 |
| Tiempo y estado | 2 | 3 | CWE |
| Manejo de errores | 3 | 3 | CWE |
| Errores de codigo | 3 | 3 | CWE |
| Encapsulacion | 4 | 5 | CWE |
| Uso incorrecto de API | 2 | 1 | CWE |

**Lenguajes soportados:**
| Lenguaje | Elementos | Frameworks |
|----------|:---------:|-----------|
| Pseudo Code (generico) | 46 | Patrones independientes del lenguaje |
| JavaScript | 42 | Express.js, Sequelize, Mongoose, Node.js crypto |
| Python | 46 | Django, Flask, SQLAlchemy, cryptography |

Destinatarios: desarrolladores web JavaScript/Python, usuarios de herramientas IA (Claude, Cursor, Copilot), desarrolladores de vibe coding

### 6. Seguridad Zero Trust — ~421 elementos

| Elemento central | Codigo | Elementos | Madurez |
|------------------|--------|:---------:|---------|
| Identidad | ZT-ID-01~53 | 53 | Tradicional/Inicial/Avanzado/Optimo |
| Dispositivo y punto final | ZT-DV-01~36 | 36 | Tradicional/Inicial/Avanzado/Optimo |
| Red | ZT-NW-01~54 | 54 | Tradicional/Inicial/Avanzado/Optimo |
| Sistema | ZT-SY-01~49 | 49 | Tradicional/Inicial/Avanzado/Optimo |
| Aplicacion y carga de trabajo | ZT-AP-01~60 | 60 | Tradicional/Inicial/Avanzado/Optimo |
| Datos | ZT-DA-01~58 | 58 | Tradicional/Inicial/Avanzado/Optimo |
| Visibilidad y analisis | ZT-VA-01~43 | 43 | Tradicional/Inicial/Avanzado/Optimo |
| Automatizacion y orquestacion | ZT-AU-01~43 | 43 | Tradicional/Inicial/Avanzado/Optimo |
| OT/ICS especifico | ZT-OT-01~25 | 25 | Tradicional/Inicial/Avanzado/Optimo |

**4 niveles de madurez**: Tradicional (Traditional) → Inicial (Initial) → Avanzado (Advanced) → Optimo (Optimal)
**Estandares de referencia**: KISA Zero Trust Guideline 2.0, NIST SP 800-207, CISA ZT Maturity Model

Destinatarios: empresas que adoptan Zero Trust, entornos OT/ICS, organizaciones en migracion a la nube, responsables de evaluacion de madurez de seguridad

## Instalacion

```
/plugin marketplace add cdppcorp/KESE-KIT
/plugin install kesekit@cdppcorp-KESE-KIT
```

> **Para actualizar:**
> ```
> /plugin marketplace update cdppcorp-KESE-KIT
> /plugin update kesekit@cdppcorp-KESE-KIT
> /reload-plugins
> ```

## Uso

```bash
# Iniciar evaluacion completa de seguridad
/kesekit-start

# Ejecutar lista de verificacion previa al despliegue
/kesekit-check

# Generar scripts de hardening
/kesekit-fix

# Obtener prompts de codificacion segura
/kesekit-guide
```

---

## Estructura del proyecto

```
KESE-KIT/
├── .claude-plugin/
│   └── marketplace.json              ← Metadatos del plugin
├── skills/                            ← Skills en ingles
│   ├── start/
│   │   ├── SKILL.md                  ← Enrutador (~80 lineas)
│   │   ├── references/               ← Documentos de descripcion/criterios
│   │   │   ├── ai-security/          ← Descripcion, proveedor de servicios, guia de usuario
│   │   │   ├── space-security/       ← Descripcion, escenarios de amenazas de la cadena de suministro
│   │   │   └── zero-trust/           ← Madurez Zero Trust, OT/ICS
│   │   ├── templates/                ← Formularios anexos, tablas de checklists
│   │   │   ├── cii/                  ← 14 tablas de verificacion CII
│   │   │   ├── ai-security/          ← Verificacion de desarrollador IA, checklist de usuario
│   │   │   ├── robot-security/       ← 6 checklists de seguridad de robots
│   │   │   ├── space-security/       ← 4 tablas de verificacion de seguridad espacial
│   │   │   └── zero-trust/           ← 9 checklists de elementos centrales Zero Trust
│   │   └── scripts/                  ← Scripts de verificacion/correccion ejecutables
│   │       ├── cii/                  ← Scripts bash, PowerShell, SQL
│   │       └── robot-security/       ← Scripts de firewall, SBOM, certificados
│   ├── check/
│   ├── fix/
│   └── guide/
├── skills-ko/                         ← Skills en coreano (misma estructura)
├── 문서/                              ← PDFs originales (14)
├── authorkit/                         ← Documentos originales y materiales de trabajo
│   ├── converted/
│   │   ├── ref-001/                  ← Guia administrativa/fisica (full.md)
│   │   ├── ref-002/                  ← Guia tecnica (full.md)
│   │   ├── ref-003/                  ← Guia de seguridad IA (full.md)
│   │   ├── ...
│   │   ├── ref-013/                  ← Zero Trust Guideline 2.0 (full.md)
│   │   ├── ref-014/                  ← Guia del modelo de madurez Zero Trust (full.md)
│   │   └── ref-015/                  ← Guia de aplicacion Zero Trust para OT (full.md)
│   └── ...
├── docs/                              ← README en 20 idiomas
├── CONTRIBUTING.md
└── README.md
```

---

## Historial de cambios

### v4.0.0 (2026-04-03)

**Nueva directriz: Seguridad Zero Trust**
- Fuente: KISA Zero Trust Guideline 2.0 (245p) + Guia del modelo de madurez Zero Trust (182p) + Guia de aplicacion Zero Trust para OT (67p)
- 9 elementos centrales, ~421 elementos de checklist
- 4 niveles de madurez: Traditional → Initial → Advanced → Optimal
- Estandares de referencia: KISA Zero Trust Guideline 2.0, NIST SP 800-207, CISA ZT Maturity Model
- 25 elementos especificos de OT/ICS incluidos

### v3.2.0 (2026-04-02)

**Nueva directriz: Guia de codificacion segura**
- Fuente: KISA Javascript Secure Coding Guide 159p + Python Secure Coding Guide 176p (edicion revisada 2023)
- 7 categorias, 46 elementos, 49 correspondencias CWE
- Nueva guia generica Pseudo Code (patrones UNSAFE/SAFE independientes del lenguaje)
- Ejemplos de codigo por framework: JavaScript (Express.js, Sequelize, Node.js) / Python (Django, Flask, SQLAlchemy)
- `references/secure-coding/` + `templates/secure-coding/` desplegados en los 8 skills (EN/KO)

### v3.0.0 (2026-04-02)

**Breaking Change: Cambio de formato de comandos**
- Todos los skills unificados bajo el namespace `kesekit`
- Formato de comandos: `/start` → `/kesekit-start` (prefijo de namespace agregado)

**Nueva directriz: Seguridad espacial**
- Fuente: Modelo de seguridad espacial Part1 134p + Part2 223p + Guia explicativa 218p
- 12 areas, 53 elementos de checklist
- Estandares de referencia: CMMC, K-RMF, NIS2, ISMS-P, NIST IR 8401/8270, CCSDS

**Nueva directriz: Seguridad de robots** (v2.1)
- Fuente: Modelo de seguridad de robots (avanzado) 156p + Guia de checklist de seguridad de robots 225p
- 11 categorias, ~103 elementos de checklist
- Estandares de referencia: NIST SP 800-218, IEC 62443, EU CRA, EU RED, NIS2

### v2.0.0 (2026-03-30)

**Refactorizacion de estructura — Aplicacion del patron Progressive Disclosure**

| Cambio | Antes (v1.0) | Despues (v2.0) |
|--------|--------------|----------------|
| SKILL.md | Todo el conocimiento en linea (270~465 lineas) | Solo enrutador (~50~80 lineas) |
| Directrices | Solo CII | CII + seguridad IA |
| Almacenamiento de conocimiento | Codificado en SKILL.md | Separado en `references/` (18 archivos) |
| Codigos de elementos | Solo algunos elementos incluidos | Todos los elementos basados en la guia 2026 |
| Escalabilidad | Agregar directrices aumenta el numero de skills | 4 skills fijos, solo se agregan references |

**Nueva directriz: Guia de seguridad de IA**
- Fuente: Ministerio de Ciencia y TIC · KISA «Guia de seguridad de Inteligencia Artificial (IA)»
- 54 elementos de verificacion para desarrolladores de IA (ciclo de vida de 6 etapas)
- Requisitos de seguridad para proveedores de servicios de IA
- 7 reglas de seguridad para usuarios de IA

**Actualizacion de la directriz CII**
- Reextraccion completa de elementos basada en la guia detallada 2026
- Incorporacion del sistema de codigos de elementos (nuevos codigos: WEB, HV, CA, etc.)

### v1.0.0 (2026-03-29)

- Lanzamiento inicial
- 4 skills de evaluacion de vulnerabilidades CII (coreano/ingles)
- Elementos tecnicos (424) + administrativos (127) + fisicos (9)

---

## Base legal

- **Ley de proteccion de infraestructuras de informacion y comunicaciones** (Act on Protection of Information and Communications Infrastructure)
- **Ley de gobierno electronico** (e-Government Act)
- **Ley de proteccion de datos personales** (Personal Information Protection Act)
- **Ley basica de inteligencia artificial** (AI Basic Act, en vigor desde el 22.01.2026)

---

## Recursos relacionados

- [Guia detallada de KISA para evaluacion tecnica de vulnerabilidades](https://www.kisa.or.kr)
- [Guia de seguridad de Inteligencia Artificial (IA)](https://www.kisa.or.kr)
- [OWASP Top 10](https://owasp.org/Top10/)
- [OWASP Top 10 for LLM](https://owasp.org/www-project-top-10-for-large-language-model-applications/)
- [CWE/SANS Top 25](https://cwe.mitre.org/top25/)

---

## Construido con

| Plugin | Descripcion |
|--------|-------------|
| [authorkit-ko](https://github.com/cdppcorp/authorkit) | Skill de apoyo a la redaccion de libros — analisis de PDF, extraccion de estructura, revision/reescritura |
| [win-hooks](https://github.com/anthropics/claude-code-plugins) | Compatibilidad de hooks de plugins de Claude Code en entornos Windows |

---

## Licencia

MIT License

## Autor

CDPP Corp (https://github.com/cdppcorp)
