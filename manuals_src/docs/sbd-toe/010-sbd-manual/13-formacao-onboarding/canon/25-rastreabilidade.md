---
id: Rastreabilidade
title: Rastreabilidade contra Frameworks
sidebar_label: Checklist de Revisão
description: Lista de verificação binária e rastreável da adoção das práticas do Capítulo 13.
tags: [checklist, formacao, onboarding, controlo, validacao, auditoria]
sidebar_position: 20
---


# 📎 Rastreabilidade contra Frameworks — Capítulo 13: Formação e Onboarding Seguro

Este ficheiro estabelece a **rastreabilidade entre as práticas prescritas neste capítulo** e os requisitos dos principais frameworks e normas internacionais associados à qualificação de acesso, cultura de segurança e educação contínua.

> A rastreabilidade é feita de forma **top-down**, demonstrando como o SbD-ToE cobre sistematicamente os requisitos normativos e de maturidade técnica associados à formação, onboarding e segurança comportamental — incluindo domínios como **Education & Training do OWASP DSOMM** e controlos organizacionais de ISO 27001, SSDF e CIS.

---

## 📌 Tabela de Rastreabilidade

| Requisito / Domínio (Framework)                          | Prática do Capítulo 13 que responde                            | Nível de Cobertura |
|----------------------------------------------------------|----------------------------------------------------------------|--------------------|
| **NIST SSDF** – PO.2.1 / PO.2.2                          | Formação mínima por função, validação de conhecimento          | ✅ Completo         |
| **NIST SSDF** – PW.1 / RV.1                              | Formação ligada à definição e validação de requisitos          | ✅ Parcial          |
| **OWASP SAMM v2.1** – Governance → Education & Guidance  | Programas de formação contínua, champions, onboarding seguro   | ✅ Nível 3          |
| **OWASP DSOMM** – Education & Training                   | Formação adaptativa, rastreável, com feedback e KPIs           | ✅ Nível 3          |
| **BSIMM13** – Training & Culture (T1–T3)                 | Formação estruturada, gamificação, rastreabilidade             | ✅ Práticas-chave   |
| **ISO/IEC 27001** – A.7.2.x / A.8.2.2 / A.13.2.4          | Qualificação para acesso, onboarding de terceiros              | ✅ Completo         |
| **CIS Controls v8** – Control 14.1 / 14.2 / 14.3          | Formação proporcional ao risco, validação de acesso            | ✅ Completo         |
| **ENISA DevSecOps** – Awareness & Security Culture        | Programas formais, integração com ciclo de vida, educação por papel | ✅ Completo    |

---

## 🧠 Notas explicativas por framework

### 🛠️ NIST SSDF

Cobertura direta de:
- **PO.2.1**: formação obrigatória por função com rastreabilidade (Addon 01, 02);
- **PO.2.2**: validação de conhecimento antes de acesso (Addon 10, 11, 20);
- Ligação parcial a PW.1 / RV.1 quando a formação reforça definição de requisitos e identificação de falhas.

---

### 🧱 OWASP SAMM v2.1

Atinge **nível 3** em *Education & Guidance*:
- Programas estruturados (Addon 01, 02);
- Formação contínua com Security Champions (Addon 03);
- Integração com práticas organizacionais por capítulo (Addon 05, 06).

---

### 🧱 OWASP DSOMM

Cobertura completa do domínio **Education & Training**:
- Formação estruturada por perfil técnico e nível de risco (Addon 01, 02);
- Validação formal com quizzes e permissões condicionadas (Addon 10, 11);
- Feedback contínuo com KPIs, atualização pós-incidente, integração com ciclos DevSecOps (Addon 90);
- Cultura de champions e curadoria contínua como reforço organizacional (Addon 03).

> ✅ Atinge **nível 3** no domínio DSOMM – Education & Training.

---

### 📊 BSIMM13

Cobertura dos domínios de *Training & Culture*:
- **T1–T3**: formação adaptada ao papel, quizzes e validação de onboarding;
- CTFs, labs e técnicas imersivas (Addon 04) reforçam maturidade.

---

### 🏛️ ISO/IEC 27001

Cobertura direta de:
- **A.7.2.2**: formação de segurança antes de atribuição de funções;
- **A.8.2.2**: onboarding seguro e proporcional;
- **A.13.2.4**: políticas de formação para terceiros (Addon 20, 21).

---

### 📐 CIS Controls v8

Controlos cobertos:
- **14.1**: políticas formais de formação baseadas em risco;
- **14.2**: validação antes de atribuir privilégios;
- **14.3**: formação contínua, gamificação, champions.

---

### 🔄 ENISA DevSecOps

Cobertura completa dos domínios:
- Security culture transversal a SDLC;
- Formação como parte do backlog e do ciclo de desenvolvimento (Addon 05);
- Rastreabilidade e reforço contínuo via KPIs e planos por capítulo.

---

## 🔗 Ligações com outros capítulos

As práticas descritas neste capítulo são complementares e estruturantes para:

- Capítulo 01 — Formação obrigatória com base na classificação de risco;
- Capítulo 02 — Formação sobre requisitos, ameaças e validação;
- Capítulo 03 — Formação sobre threat modeling e artefactos críticos;
- Capítulo 05 / 07 / 09 — Integração com práticas técnicas de dependências, CI/CD e containers;
- Todos os capítulos — formação por capítulo via Addon 06 e indicadores do Addon 90.

> 📌 Esta rastreabilidade comprova que a formação prescrita no SbD-ToE **não é genérica nem informal**, mas uma componente crítica de segurança organizacional, rastreável e verificável por projeto, pessoa e função.
