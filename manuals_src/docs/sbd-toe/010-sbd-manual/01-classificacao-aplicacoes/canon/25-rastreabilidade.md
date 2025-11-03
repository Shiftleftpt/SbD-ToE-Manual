---
id: rastreabilidade
title: Rastreabilidade Top-Down – Capítulo 01
sidebar_position: 25
tags: [canon, rastreabilidade, frameworks, alinhamento]
---

# 📎 Rastreabilidade contra Frameworks — Capítulo 01: Classificação do Risco

Este ficheiro estabelece a **rastreabilidade entre as práticas de classificação do risco prescritas neste capítulo** e os requisitos dos principais frameworks de segurança, governação e gestão do ciclo de vida aplicacional.

> A rastreabilidade é feita de forma **top-down**, demonstrando como o SbD-ToE cobre sistematicamente os requisitos de avaliação, decisão e governação de risco nas práticas de segurança aplicacional.

---

## 📌 Tabela de Rastreabilidade

| Requisito / Domínio (Framework)                       | Prática do Capítulo 01 que responde                             | Nível de Cobertura |
|-------------------------------------------------------|------------------------------------------------------------------|--------------------|
| **NIST SSDF** – PO.1.1 / PO.1.2 / PO.3.2              | Classificação de risco, tratamento proporcional, risco residual | ✅ Completo         |
| **OWASP SAMM v2.1** – Governance → Risk Management    | Avaliação formal, aplicação por tipo de aplicação, ciclo de vida| ✅ Nível 3          |
| **OWASP DSOMM** – Governance / Risk / Requirements    | Classificação e priorização, rastreabilidade, aceitação formal  | ✅ Nível 2          |
| **BSIMM13** – Strategy & Metrics (SM1–SM3)            | Classificação formal, exceções justificadas, rastreabilidade    | ✅ Nível 2          |
| **ISO/IEC 27001** – A.6.1.2 / A.8.2.1 / A.18.2.3       | Avaliação de risco de ativos, aceitação formal, exceções        | ✅ Completo         |
| **CIS Controls v8** – Control 4.1 / 4.3 / 17.1         | Classificação de sistemas, priorização de controlos, auditoria   | ✅ Completo         |
| **ENISA SDLC / Risk** – Risk Profiling & Governance   | Aplicação de criticidade, decisão de segurança proporcional     | ✅ Completo         |

---

## 🧠 Notas explicativas por framework

### 🛠️ NIST SSDF

Cobertura integral de:
- **PO.1.1**: identificação e categorização dos ativos (Addon 01, 02);
- **PO.3.2**: decisões documentadas sobre exceções e risco residual (Addon 06, 09);
- Integração com o ciclo de vida via critérios de aceitação (Addon 07).

---

### 🧱 OWASP SAMM v2.1

Atinge **nível 3** em *Risk Management*:
- Classificação sistemática (Addon 01, 02);
- Matriz de aplicação proporcional de práticas (Addon 04);
- Rastreabilidade organizacional com base em risco (Addon 08).

---

### 🧭 OWASP DSOMM

Cobre domínios centrais de:
- **Governance / Risk Management**: modelo de classificação aplicável no SDLC (Addon 01, 02);
- **Security Requirements**: definição e aplicação proporcional com base na criticidade (link com Cap. 2);
- **Compliance Mapping**: decisão justificada sobre controlo, exceção ou aceitação (Addon 06);
- Atinge **maturidade 2** nos domínios de governança e requisitos.

> O Capítulo 01 estabelece as fundações exigidas no DSOMM para aplicar segurança em pipelines DevSecOps com proporcionalidade, rastreabilidade e autonomia.

---

### 📊 BSIMM13

Cobre práticas de:
- Classificação de aplicações por impacto (SM1);
- Justificação e registo de exceções de segurança (SM2);
- Governação contínua da aplicação do modelo (SM3).

---

### 🏛️ ISO/IEC 27001

Controlos cobertos:
- **A.6.1.2**: avaliação de riscos e tratamento;
- **A.8.2.1**: classificação da informação e ativos por impacto;
- **A.18.2.3**: registo e aprovação de exceções de segurança.

---

### 📐 CIS Controls v8

Contempla:
- **4.1**: classificação de aplicações e ativos críticos;
- **4.3**: alinhamento de controlos com o nível de risco;
- **17.1**: governança contínua e auditoria sobre decisões de segurança.

---

### 🔄 ENISA SDLC / Risk

Cobre integralmente:
- Risk profiling aplicado ao SDLC;
- Avaliação proporcional por tipo de aplicação;
- Registo e auditoria de decisões sobre risco e controlos.

---

## 🔗 Ligações com outros capítulos

O Capítulo 01 é a base de aplicação proporcional dos restantes:

- Capítulo 02 — seleção de requisitos baseada no nível de risco;
- Capítulo 03 — exigência de threat modeling consoante criticidade;
- Capítulo 05 a 14 — aplicação seletiva de práticas com base em L1–L3;
- Capítulo 13 / 14 — exceções, aceitação formal e rastreabilidade organizacional.

> 📌 Esta rastreabilidade comprova que a classificação do risco no SbD-ToE é **o mecanismo central de governação e proporcionalidade**, assegurando segurança com eficiência operacional e cobertura normativa.
