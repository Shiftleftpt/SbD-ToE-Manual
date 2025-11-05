---
id: rastreabilidade
title: Rastreabilidade Top-Down – Capítulo 07
description: Mapeamento entre as práticas do capítulo e os requisitos normativos de segurança em CI/CD
tags: [rastreabilidade, normativo, cicd, pipelines, frameworks, dsomm, ssdf]
sidebar_position: 25
---


# 📎 Rastreabilidade contra Frameworks - Capítulo 07: CI/CD Seguro

Este ficheiro estabelece a **rastreabilidade entre as práticas prescritas neste capítulo** e os requisitos dos principais frameworks e normas de segurança para cadeias de integração e entrega contínua (CI/CD), proteção de pipelines e validação automatizada.

> A rastreabilidade é feita de forma **top-down**, demonstrando como o SbD-ToE cobre sistematicamente os requisitos técnicos e normativos de segurança em pipelines de software.

---

## 📌 Tabela de Rastreabilidade

| Requisito / Domínio (Framework)                           | Prática do Capítulo 07 que responde                             | Nível de Cobertura |
|-----------------------------------------------------------|------------------------------------------------------------------|--------------------|
| **NIST SSDF** – PW.7 / RV.3 / RV.4                        | Validações automáticas, gates, rastreabilidade de artefactos     | ✅ Completo         |
| **OWASP SAMM v2.1** – Implementation → Secure Build       | Design seguro do pipeline, runners isolados, controlo de execução| ✅ Nível 3          |
| **BSIMM13** – Deployment & Build (SE1–SE3, CM1)           | Proteção do pipeline, execução rastreável e controlada           | ✅ Nível 2          |
| **SLSA v1.0** – Levels 1–3 (Build Integrity & Provenance) | Proveniência, isolamento de execução, assinatura de artefactos   | ✅ Completo         |
| **DSOMM** – Build, Test, Release, Govern, Operate         | Segurança automatizada ponta-a-ponta em pipelines CI/CD          | ✅ Nível 3–4        |
| **ISO/IEC 27001** – A.12.1.2 / A.14.2.2 / A.14.2.5         | Gestão segura de pipelines e validação antes de entrega          | ✅ Completo         |
| **CIS Controls v8** – Control 16.4 / 16.5 / 16.8           | Controlo de execução e validações de segurança contínuas         | ✅ Completo         |
| **ENISA DevSecOps** – Pipeline Security & Enforcement     | Validações CI/CD, gates, segregação de runners, rastreabilidade  | ✅ Completo         |

---

## 🧠 Notas explicativas por framework

### 🛠️ NIST SSDF

Cobertura integral de:
- **PW.7**: validações de segurança antes de release (Addon 07);
- **RV.3 / RV.4**: rastreabilidade de ações, proveniência de builds e assinatura de artefactos (Addon 08).

---

### 🧱 OWASP SAMM v2.1

Atinge **nível 3** em *Secure Build*:
- Runners dedicados e isolamento (Addon 04);
- Segredos protegidos e controlos de execução (Addon 03, 06);
- Design formal da cadeia de CI/CD (Addon 01).

---

### 📊 BSIMM13

Cobre:
- **SE1–SE3**: validações de segurança, rastreabilidade e execução auditável;
- **CM1**: controlo de alterações de pipeline com aprovação formal.

---

### 🔐 SLSA v1.0

Cobertura de:
- **Level 1–3**: isolamento de ambientes, proveniência, assinatura e validação contínua de artefactos (Addon 05, 08).

---

### 🧪 DSOMM - DevSecOps Maturity Model

Cobertura nos domínios principais:

| Domínio DSOMM | Prática SbD-ToE                                |
|---------------|--------------------------------------------------|
| **Build**     | Pipelines como código, controlo SCM, runners dedicados (`addon/01`, `04`) |
| **Test**      | Execução automatizada de validações (SAST, secrets, IaC) (`addon/07`)     |
| **Release**   | Assinatura e proveniência dos artefactos (`addon/05`, `08`)              |
| **Govern**    | Políticas de segurança CI/CD e scorecards de conformidade (`addon/06`, `60`) |
| **Operate**   | Logging de execução, controlo de exceções, deploy auditável (`addon/09`)  |

> A maturidade descrita neste capítulo permite implementar práticas DSOMM em todos os domínios operacionais e de governação técnica da cadeia CI/CD, com rastreabilidade e enforcement automatizado.

---

### 🏛️ ISO/IEC 27001

Contempla:
- **A.12.1.2**: segregação de ambientes e controlo de execução;
- **A.14.2.2**: transferência segura entre ambientes (CI → entrega);
- **A.14.2.5**: validação técnica pré-release.

---

### 📐 CIS Controls v8

Práticas implementadas:
- **16.4 / 16.5**: controlo automatizado da execução e segregação de ambientes;
- **16.8**: validações contínuas integradas no pipeline (Addon 07).

---

### 🔄 ENISA DevSecOps

Cobertura total:
- Validações técnicas de segurança integradas;
- Proteção contra execução não autorizada;
- Rastreabilidade de builds e registos de auditoria.

---

## 🔗 Ligações com outros capítulos

O Capítulo 07 está diretamente interligado com:

- **Capítulo 01** - classificação de risco determina exigência de validações no CI/CD;
- **Capítulo 02 / 06** - requisitos REQ-XXX e práticas de desenvolvimento são validados aqui;
- **Capítulo 09** - execução segura de containers depende do pipeline;
- **Capítulo 10** - testes de segurança automáticos acionados no pipeline.

> 📌 Esta rastreabilidade comprova que o Capítulo 07 fornece um modelo técnico e auditável de proteção da cadeia de desenvolvimento, com validações contínuas e rastreabilidade de execução.
