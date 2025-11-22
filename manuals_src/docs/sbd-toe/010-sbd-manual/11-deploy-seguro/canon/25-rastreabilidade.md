---
id: rastreabilidade
title: Rastreabilidade - Deploy Seguro
description: Mapeamento top-down entre frameworks normativas e as práticas de segurança na entrega de código em produção.
tags: [deploy, frameworks, rastreabilidade, samm, ssdf]
sidebar_position: 25
---


# 📎 Rastreabilidade contra Frameworks - Capítulo 11: Deploy Seguro e Controlo de Execução

Este documento estabelece a **rastreabilidade entre as práticas prescritas neste capítulo** e os requisitos definidos pelas principais frameworks, normas e modelos de maturidade que regulam a entrega, ativação e execução segura de software.

> A análise é feita de forma **top-down**, demonstrando como o Capítulo 11 responde sistematicamente aos requisitos técnicos e organizacionais aplicáveis ao runtime seguro.

---

## 📌 Tabela de Rastreabilidade

| Requisito / Domínio (Framework)                                    | Prática do Capítulo 11 que responde                          | Cobertura |
|--------------------------------------------------------------------|----------------------------------------------------------------|-----------|
| **NIST SSDF v1.1** - PW.6, PW.7                                    | Validações formais antes do deploy, readiness gates            | ✅        |
| **NIST SSDF v1.1** - RV.3                                          | Monitorização pós-deploy, rollback automatizado                | ✅        |
| **OWASP SAMM v2.1** - Release → Release Management                 | Gestão de releases, toggles, rollback                          | ✅ (N3)   |
| **OWASP SAMM v2.1** - Release → Environment Management             | Segregação de ambientes, autorização de execução               | ✅ (N3)   |
| **BSIMM13** - Deployment → DR1–DR3, SE2.5                          | Feature toggles, rastreabilidade, aprovação formal             | ✅        |
| **SLSA v1.0** - Provenance Enforcement (L1–L3)                     | Deploy automatizado, rollback parcial, proveniência assinada   | 🔹 (L2)  |
| **ISO/IEC 27001** - A.14.2.2, A.14.2.4                             | Transição controlada, segregação de ambientes                  | ✅        |
| **CIS Controls v8** - 4.8, 6.8, 16.13                              | Deploy seguro, auditoria runtime, rollback                     | ✅        |
| **ENISA DevSecOps** - Secure Deployment, Runtime Enforcement       | Deploy progressivo, validação pré-execução, runtime controlado | ✅        |
| **OWASP DSOMM** - Design & Development (5 práticas)               | Validação formal, rollback, toggles rastreáveis                | ✅ (4/5) |

---

## 🧠 Notas explicativas por framework

### 🔹 NIST SSDF v1.1

- **PW.6–PW.7**: critérios objetivos de aceitação e validação automatizada (Addon 04);
- **RV.3**: monitorização ativa e triggers de rollback (Addon 05, 07);
- Todas as execuções são rastreáveis com owners e artefactos versionados.

### 🔹 OWASP SAMM v2.1

- **Release Management (N3)**: deploy controlado, toggles com expiração, rollback formal (Addon 03, 06, 07);
- **Environment Management (N3)**: segregação de execução, gates formais e autorização dual (Addon 08).

### 🔹 BSIMM13

- **DR1–DR3**: reversibilidade de execução, rastreabilidade de artefactos e eventos de release;
- **SE2.5**: aprovação formal com critérios AppSec e validação pré-produção (Addon 04, 06).

### 🔹 SLSA v1.0

- Cumprimento até **nível 2**:
  - L1: pipelines automatizados (Cap. 07);
  - L2: proveniência assinada antes da promoção (Addon 06);
  - 🔹 L3 (observabilidade ativa) depende de práticas do Capítulo 12.

### 🔹 ISO/IEC 27001

- **A.14.2.2**: procedimentos formais de transição e deploy controlado;
- **A.14.2.4**: ambientes segregados, execução rastreável e auditável.

### 🔹 CIS Controls v8

- **4.8**: deploy controlado com mecanismos de rollback definidos;
- **6.8**: segregação e autorização de execução;
- **16.13**: execução segura com observabilidade e resposta.

### 🔹 ENISA DevSecOps

- Pipeline de deploy com validações explícitas antes da execução (Addon 04);
- Runtime controlado com mecanismos como kill switch, OPA ou equivalent (Addon 06, 07);
- Execução progressiva e baseada em risco (Addon 07).

### 🔹 OWASP DSOMM

- Domínio **Design & Development**:
  - 4 das 5 práticas cobertas: validação formal, rollback, toggles rastreáveis, readiness gates;
  - Observabilidade contínua parcial - aprofundada no Cap. 12.

---

## 🔗 Ligações com outros capítulos

As práticas aqui prescritas articulam-se diretamente com:

- **Cap. 01 - Gestão de Risco**: identifica onde execução controlada é mandatória;
- **Cap. 02 - Requisitos de Segurança**: define critérios técnicos de deploy seguro;
- **Cap. 07 - CI/CD Seguro**: automatiza gates, rollback e validações no pipeline;
- **Cap. 09 - Containers e Execução em Produção**: extensões runtime;
- **Cap. 10 - Testes de Segurança**: integra os critérios de aceitação e regressão;
- **Cap. 12 - Monitorização e Resposta**: reforça a observabilidade ativa do runtime.

> 📌 Esta rastreabilidade demonstra que o Capítulo 11 constitui uma **resposta prescritiva e integrada às exigências operacionais e normativas** de execução segura, validada e reversível em ambientes de produção.
