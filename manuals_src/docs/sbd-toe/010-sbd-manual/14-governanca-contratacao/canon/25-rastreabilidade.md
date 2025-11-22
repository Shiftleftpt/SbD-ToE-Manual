---
id: rastreabilidade
title: Rastreabilidade Top-Down - Capítulo 14
sidebar_position: 25
description: Evidência de conformidade entre as práticas de governança e os requisitos dos principais frameworks de segurança
tags: [conformidade, contratos, exceções, fornecedores, frameworks, rastreabilidade]
---


# 📎 Rastreabilidade contra Frameworks - Capítulo 14: Governança e Contratação Segura

Este documento estabelece a **rastreabilidade top-down entre os requisitos dos principais frameworks e normas de segurança** e as práticas prescritas no Capítulo 14 - Governança e Contratação.

> 📌 Esta rastreabilidade permite demonstrar que as práticas de validação de exceções, cláusulas contratuais, ownership formal, onboarding de terceiros e rastreabilidade organizacional descritas neste capítulo **respondem de forma sistemática e completa às exigências técnicas e normativas reconhecidas**.

---

## 📌 Tabela de Rastreabilidade

| Framework           | Requisito / Domínio                           | Prática do Cap. 14 que responde                             | Cobertura |
|---------------------|-----------------------------------------------|-------------------------------------------------------------|-----------|
| **NIST SSDF**       | PO.1 / PO.3 / RV.2                            | Governação sobre risco, exceções, métricas, validação       | ✅ Completo |
| **OWASP SAMM v2.1** | Strategy & Metrics / Supplier Management      | Modelo de rastreabilidade, KPIs, revalidação de fornecedores| ✅ Nível 3 |
| **BSIMM13**         | SM1–SM3 / CP1                                 | Governação, exceções, ações corretivas                      | ✅ Nível 2 |
| **ISO/IEC 27001**   | A.5.1 / A.15.1–15.2                           | Cláusulas contratuais, políticas de segurança               | ✅ Completo |
| **CIS v8**          | 15.1 / 15.6 / 17.1                            | Política de terceiros, rastreabilidade, auditoria           | ✅ Completo |
| **ENISA**           | Supply Chain / DevSecOps - Governance Layer  | Validação de fornecedores, exceções auditáveis              | ✅ Completo |
| **OWASP DSOMM**     | Governance / Third-Party / Verification / Policies & Standards | Owners, onboarding, auditoria contínua, exceções formalizadas | ✅ 4–5/5   |

---

## 🧠 Notas explicativas por framework

### 🛠️ NIST SSDF

O capítulo cobre integralmente:
- **PO.1 / PO.3**: governação de exceções, processos formais, ciclos de revalidação (`addon/01`, `06`);
- **RV.2**: ações corretivas, auditoria, revisão de métricas por domínio (`addon/04`, `07`).

---

### 🧱 OWASP SAMM v2.1

Atinge **nível 3** em:
- *Strategy & Metrics*: governação formal, KPIs, modelo de maturidade;
- *Supplier Management*: controlo contratual, checklist de validação, revalidação contínua de fornecedores (`addon/02`, `03`, `06`).

---

### 📊 BSIMM13

Cobertura sólida em:
- **SM1–SM3**: governação formal, owners de segurança, rastreabilidade;
- **CP1**: gestão de terceiros com cláusulas contratuais e reavaliação periódica.

---

### 🏛️ ISO/IEC 27001

Cobertura direta de:
- **A.15.1.1–A.15.2.1**: segurança na contratação e relacionamento com fornecedores;
- **A.5.1.1**: definição clara de política de segurança aplicável a contratos.

---

### 📐 CIS Controls v8

Controlos contemplados:
- **15.1 / 15.6**: validação e gestão contínua de fornecedores;
- **17.1**: auditoria interna da função de segurança e conformidade de controlos.

---

### 🔄 ENISA Supply Chain / DevSecOps

Cobertura integral dos domínios:
- Política formal de relacionamento com fornecedores;
- Governação estruturada sobre risco e decisões de exceção;
- Verificação periódica e rastreável do cumprimento dos controlos.

---

### 🧮 OWASP DSOMM

O Capítulo 14 responde aos seguintes domínios do OWASP DSOMM:

| Domínio DSOMM         | Práticas SbD-ToE (Cap. 14)                                              | Nível |
|------------------------|------------------------------------------------------------------------|--------|
| **Governance**          | Modelo formal de decisões, owners, exceções auditáveis (`addon/01`, `07`) | 5 / 5  |
| **Third-Party Management** | Onboarding seguro, contratos com cláusulas, revalidação de fornecedores (`02`, `03`, `06`) | 5 / 5  |
| **Verification**         | Revalidações, métricas de conformidade, KPIs (`addon/06`, `90`)      | 4 / 5  |
| **Policies & Standards** | Políticas formais aplicáveis a terceiros e fornecedores (`60`, `addon/02`) | 5 / 5  |

> ✅ O modelo prescrito neste capítulo permite alcançar **nível elevado de maturidade organizacional segundo o DSOMM**, com rastreabilidade total entre controlo, execução e evidência de conformidade.

---

## 🔗 Ligações com outros capítulos

Este capítulo é transversal e complementa todos os outros:

- **Capítulo 01** - aplica critérios de risco para decisões de exceção;
- **Capítulo 02** - rastreabilidade e validação de requisitos implementados;
- **Capítulo 05** - aplica cláusulas de dependências e gestão SCA;
- **Capítulo 07 e 09** - contratualiza práticas seguras de CI/CD e execução;
- **Capítulo 13** - aplica controlo de formação a terceiros e fornecedores.

> 📌 Esta rastreabilidade comprova que o modelo de governação e contratação descrito neste capítulo funciona como **mecanismo organizacional de enforcement, controlo e maturidade da adoção do SbD-ToE**.
