---
id: policies-relevantes
title: Policies
description: Políticas formais necessárias para legitimar e operacionalizar a validação contínua da segurança das aplicações.
tags: [policy, organizacional, testes, segurança, validação, dsoom, ssdf, samm]
sidebar_position: 60
---


# 🏛️ Políticas Organizacionais — Testes de Segurança

A aplicação eficaz do **Capítulo 10 — Testes de Segurança** exige que existam **políticas organizacionais formais** que definam:

- O **que testar**, **quando testar** e **como validar** a segurança das aplicações;
- Os **níveis mínimos exigidos** de cobertura e proporcionalidade por criticidade (L1–L2–L3);
- A **gestão de findings**, **exceções**, **revalidações** e **mecanismos de rastreabilidade**;
- A **execução periódica de testes ofensivos (PenTesting)** como reforço e validação complementar a mecanismos automatizados.

---

## 📌 Nota fundamental

> ⚠️ A validação de segurança eficaz não depende apenas de ferramentas — depende de **políticas claras que estabeleçam critérios, responsabilidades e controlo contínuo**.

Estas políticas:

- **Formalizam os requisitos mínimos de validação por tipo de aplicação** e risco;
- **Definem critérios de aprovação e rejeição de releases com base em segurança**;
- **Obrigam à rastreabilidade entre findings, exceções, decisões e releases**;
- **Estabelecem o uso de validação ofensiva manual (PenTesting) como reforço complementar onde aplicável**;
- **Facilitam auditorias externas, conformidade normativa e melhoria contínua**.

> 🧩 Este capítulo **executa e operacionaliza políticas organizacionais** relativas à validação contínua e testes de segurança.

> 📎 Estas políticas são recomendadas por **SSDF**, **OWASP SAMM**, **SLSA**, **BSIMM**, **ENISA** e **OWASP DSOMM** como base para maturidade em AppSec.

---

## 🧾 Políticas recomendadas

| Nome da Política                                       | Obrigatória? | Aplicação                                 | Resumo do conteúdo necessário |
|--------------------------------------------------------|--------------|--------------------------------------------|-------------------------------|
| Política de Validação de Segurança Aplicacional       | ✅ Sim       | Todas as aplicações com entrega contínua   | Tipos de testes exigidos (SAST, DAST, fuzzing), níveis mínimos por criticidade, ferramentas aprovadas. |
| Política de Gestão de Findings de Segurança            | ✅ Sim       | Todos os produtos com scanner ativo        | Processo de triagem, classificação, priorização, tracking, ownership e reporte de findings. |
| Política de Exceções a Vulnerabilidades Identificadas  | ✅ Sim       | Quando um finding não é corrigido          | Justificação técnica, prazo de validade, revisão periódica, mitigação compensatória. |
| Política de Execução de PenTesting Ofensivo            | ⚠️ Opcional  | Aplicações L2/L3, APIs externas, produtos críticos | Periodicidade definida (ex: semestral), escopo, metodologia, objetivos (black-box/grey-box), reporte e follow-up obrigatório. |
| Política de Cobertura de Testes de Segurança           | ⚠️ Opcional  | Aplicações críticas (L2–L3)                | Definição de métricas de cobertura esperada, fuzzing dirigido, teste de regressões. |
| Política de Integração de Testes com Ciclo de Vida     | ⚠️ Opcional  | Equipas com integração DevSecOps           | Definição de critérios BDD, integração com pipelines, PRs, e processos de release. |
| Política de Revalidação e Observabilidade de Testes    | ⚠️ Opcional  | Ambientes com requisitos de auditoria      | Revalidação de findings, logging dos testes, análise de falhas de execução. |

---

## 📎 Correspondência com frameworks normativas

| Framework           | Requisitos cobertos pelas políticas acima                                                  |
|--------------------|---------------------------------------------------------------------------------------------|
| **NIST SSDF**       | RV.1 (Security Testing), RV.3 (Vulnerability Resolution), PO.2 (Validation Criteria)       |
| **OWASP SAMM**      | Verification > Security Testing, Governance > Metrics & Feedback                          |
| **SLSA v1.0**        | Build/test requirements for provenance and reproducibility                                 |
| **BSIMM13**         | SE2.3 (Fix recurring bugs), SR2.1 (Track AppSec results), CMVM2 (Test result visibility)   |
| **ENISA SDLC**      | Validation and testing phase; integration of testing in secure SDLC                        |
| **OWASP DSOMM**     | Design & Development > Security Testing, Vulnerability Management, Release & Sign-off      |

---

## 📋 Estrutura sugerida de cada política

Cada política deve incluir, pelo menos:

- **Objetivo e âmbito** (ex: validação de segurança por tipo de aplicação ou contexto);
- **Critérios obrigatórios por nível de criticidade (L1–L3)**;
- **Requisitos técnicos por tipo de teste** (ex: ferramentas permitidas, formatos, thresholds, escopos);
- **Papéis e responsabilidades** (ex: QA, AppSec, produto, equipa Dev, equipa Red Team ou externa);
- **Formato de evidência exigida** (ex: relatórios, logs, dashboards, issues, SBOM);
- **Processos de exceção, follow-up e revalidação periódica**;
- **Ciclo de revisão e melhoria da política**.

---

## ✅ Recomendações finais

- Estas políticas devem ser **aprovadas em conjunto pelas áreas de Segurança, Qualidade e Desenvolvimento**;
- Devem ser **documentadas, acessíveis e integradas no ciclo de vida de software**;
- A sua aplicação deve ser **auditável, baseada em evidência objetiva e alinhada com pipelines automatizados e testes ofensivos planeados**;
- A maturidade da organização em validação de segurança depende **não apenas da execução dos testes, mas da existência de critérios formais e consistentes**.

> 📌 Políticas bem definidas são a **garantia de que os testes — automáticos ou manuais — têm impacto real, visível e contínuo na segurança da organização**.
