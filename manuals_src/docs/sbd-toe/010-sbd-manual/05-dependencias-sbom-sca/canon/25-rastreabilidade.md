---
id: rastreabilidade
title: Rastreabilidade Top-Down - Capítulo 05
description: Análise de rastreabilidade das práticas deste capítulo face aos principais frameworks normativos
tags: [rastreabilidade, frameworks, dependencias, sbom, sca, supply-chain, dsomm]
sidebar_position: 25

---

# 📎 Rastreabilidade contra Frameworks - Capítulo 05: Dependências, SBOM e SCA

Este ficheiro estabelece a **rastreabilidade entre as práticas prescritas neste capítulo** e os requisitos dos principais frameworks relacionados com gestão segura de dependências, SBOM (Software Bill of Materials) e análise de composição de software (SCA).

> A rastreabilidade é feita de forma **top-down**, demonstrando como o SbD-ToE cobre sistematicamente os requisitos normativos e de maturidade técnica associados à gestão segura de dependências e supply chain.

---

## 📌 Tabela de Rastreabilidade

| Requisito / Domínio (Framework)                                 | Prática do Capítulo 05 que responde                          | Nível de Cobertura |
|-----------------------------------------------------------------|--------------------------------------------------------------|--------------------|
| **NIST SSDF** - PW.3 (Componentes de terceiros seguros)         | Inventário sistemático (SBOM), análise SCA, critérios de aceitação | ✅ Completo         |
| **NIST SSDF** - RV.1 (Identificação de vulnerabilidades)        | Análise contínua de composição (SCA), rastreabilidade        | ✅ Completo         |
| **OWASP SAMM** - Operations → Component Management              | Inventário completo (Addon 01), análise contínua, governança (Addon 02, 03, 05) | ✅ Nível 3          |
| **BSIMM13** - SFD (Software Dependency Management)              | Inventário, política formal de aceitação e atualização, análise periódica | ✅ Nível 3          |
| **SLSA v1.0** - Provenance & Dependencies (Nível 3)             | SBOM formal, controlo de registos de origem, validação contínua (Addon 01, 07) | ✅ Completo         |
| **OWASP DSOMM** - Build & Deploy, Governance, Verification      | SCA contínua, SBOM integrado no pipeline, políticas e controlo de findings | ✅ Nível 2/3        |
| **ISO/IEC 27001** - A.12.6.2 (Gestão Técnica de Vulnerabilidades)| Análise SCA contínua, rastreabilidade de vulnerabilidades (Addon 02, 08) | ✅ Completo         |
| **ISO/IEC 27001** - A.15.1.3 (Supply Chain Security)            | Avaliação contínua do risco de supply chain (Addon 06)       | ✅ Completo         |
| **CIS Controls v8** - Control 16.2 (Software Inventory)         | Inventário e SBOM completo, rastreabilidade                  | ✅ Completo         |
| **CIS Controls v8** - Control 16.5 (Patch Management)           | Política formal de atualizações e aceitação de risco (Addon 05, 09) | ✅ Completo         |
| **ENISA DevSecOps** - Dependency Management & SBOM              | Integração em pipelines CI/CD, geração contínua de SBOM (Addon 04) | ✅ Completo         |

---

## 🧠 Notas explicativas por framework

### 🛠️ NIST SSDF

Cobertura integral dos controlos:
- PW.3: Inventário formal (SBOM), critérios de aceitação e análise SCA contínua.
- RV.1: Identificação e gestão de vulnerabilidades via SCA e rastreabilidade automatizada.

---

### 🧱 OWASP SAMM

Nível 3 alcançado em Component Management:
- Inventário formal e completo (Addon 01)
- Análise sistemática (Addon 02)
- Governação e atualização (Addon 03, 05, 09)

---

### 📊 BSIMM13

Domínio **SFD** plenamente atendido:
- Gestão sistemática de bibliotecas externas
- Critérios de aceitação e atualização formalizados

---

### 🔐 SLSA v1.0

Cumprimento até Nível 3:
- SBOM formal gerado por build
- Proveniência de artefactos e integração CI/CD

---

### 📦 OWASP DSOMM

As práticas do capítulo respondem a quatro domínios fundamentais do DSOMM:

| Domínio                 | Práticas relevantes no Capítulo 05                                 |
|-------------------------|---------------------------------------------------------------------|
| **Build & Deploy**      | SBOM e SCA automatizados no CI/CD (Addon 02, 03)                    |
| **Governance & Policy** | Políticas formais de aceitação e atualização (Addon 05, 09)         |
| **Verification**        | Rejeição de findings críticos sem exceções não justificadas         |
| **Design & Dev**        | Escolha consciente e rastreável de bibliotecas (Addon 01)           |

> O **nível de cobertura 2/3** é coerente com o atingido nos demais frameworks e demonstra integração prática das recomendações DSOMM.

---

### 🏛️ ISO/IEC 27001

Cobertura completa:
- A.12.6.2: Gestão técnica contínua de vulnerabilidades
- A.15.1.3: Gestão de risco em cadeia de fornecimento

---

### 📐 CIS Controls v8

Cobertura total:
- 16.2: Inventário formal de software (SBOM)
- 16.5: Política de atualização e aceitação de risco

---

### 🔄 ENISA DevSecOps

Cumprimento integral:
- Geração e validação de SBOM automatizada em pipelines (Addon 04)

---

## 🔗 Ligações com outros capítulos

As práticas relativas à gestão segura de dependências, SBOM e SCA descritas neste capítulo:

- **Dependem da classificação de risco** das aplicações (Capítulo 01)
- **Apoiam a definição e validação de requisitos** (Capítulo 02)
- **Constituem base técnica para segurança na cadeia CI/CD** (Capítulo 07)
- **Suportam controlos contínuos de vulnerabilidades e validações** (Capítulo 10)

> 📌 Esta rastreabilidade comprova que as práticas do Capítulo 05 respondem de forma estruturada e proporcional aos principais frameworks e normas, permitindo **auditoria, melhoria contínua e gestão de risco técnica e organizacional**.
