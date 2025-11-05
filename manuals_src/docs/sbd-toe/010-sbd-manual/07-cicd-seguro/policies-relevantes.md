---
id: policies-relevantes
title: Policies
description: Conjunto de políticas recomendadas para sustentar e legitimar as práticas de segurança CI/CD descritas no capítulo
tags: [políticas, cicd, pipelines, governança, segurança organizacional]
sidebar_position: 60
---


# 🏛️ Políticas Organizacionais - Segurança em Pipelines CI/CD

A adoção eficaz do Capítulo 07 - CI/CD Seguro - exige a existência de **políticas organizacionais formais** que **regulem, legitimem e sustentem as práticas de segurança aplicáveis à cadeia de integração e entrega contínua**.

---

## 📌 Nota fundamental

> ⚠️ As práticas técnicas prescritas neste capítulo (ex: controlo de execução, injeção de segredos, validação de artefactos, segregação de pipelines) **devem ser legitimadas formalmente por políticas organizacionais aprovadas e auditáveis**.

Estas políticas:

- Tornam **obrigatória a aplicação proporcional de controlos de segurança por nível de risco**;
- Estabelecem **regras claras para a execução segura dos pipelines**, evitando decisões ad hoc;
- Permitem auditoria da **proveniência de artefactos e validação das etapas críticas de build e deploy**.

> 🧩 Este capítulo implementa as práticas; as políticas fornecem **a base normativa e vinculativa** para garantir que são corretamente aplicadas.

> 📎 A existência de políticas sobre segurança CI/CD é uma **exigência explícita** ou **recomendação forte** em frameworks como **SLSA**, **SSDF**, **OWASP CI/CD Project**, **BSIMM** e guias da **ENISA**.

---

## 🧾 Políticas recomendadas

| Nome da Política                              | Obrigatória? | Aplicação                                | Resumo do conteúdo necessário |
|-----------------------------------------------|--------------|-------------------------------------------|-------------------------------|
| Política de Execução Segura de Pipelines      | ✅ Sim       | Todas as pipelines de CI/CD               | Regras de execução autorizada; runners permitidos; controlo por branch/contexto; eventos que disparam builds. |
| Política de Segregação de Ambientes e Runners | ✅ Sim       | Equipas DevOps, Segurança, Cloud          | Regras de isolamento por projeto/confiança; runners dedicados; proibição de execução cruzada sem aprovação. |
| Política de Injeção e Proteção de Segredos    | ✅ Sim       | Toda a organização                        | Origem e gestão de segredos; proibição de hardcoded; mascaramento em logs; integração com vaults. |
| Política de Validação de Artefactos e Proveniência | ✅ Sim   | Repositórios, pipelines, ambientes de staging/prod | Geração e verificação de proveniência; hash e assinatura; regras para promoção entre ambientes. |
| Política de Revisão de Pipelines              | ⚠️ Opcional | Organizações com pipelines partilhadas    | Peer review obrigatória; controlo de alterações; aprovação técnica de templates. |
| Política de Aplicação Proporcional por Risco  | ⚠️ Opcional | Organizações com classificação formal     | Mapeamento entre nível de risco e controlos mínimos exigidos no pipeline. |

---

## 📎 Correspondência com frameworks normativas

| Framework              | Requisitos cobertos pelas políticas acima                                                                 |
|------------------------|------------------------------------------------------------------------------------------------------------|
| **SLSA**               | Build Integrity, Provenance Generation, Isolation of Build Environment                                     |
| **NIST SSDF**          | PW.4 (Protect Build Infrastructure), RV.1 (Verify Integrity of Artifacts), DE.1 (Define Build Process)     |
| **OWASP CI/CD Project**| Secure Execution, Secrets Management, Job Isolation, Artifact Control                                     |
| **BSIMM13**            | SE2.1 (Review CI/CD), SE3.x (Automation of Control Gates), CMVM Practices                                 |
| **ENISA DevSecOps**    | Sec. 3.3–3.6 - validação, build seguro, segregação, gestão de segredos                                    |
| **ISO/IEC 27001/27034**| A.12.1.2, A.14.2.1 - controlo de alterações, validação de software antes de produção                       |
| **CIS Controls v8**    | 2.1, 4.6, 16.4 - gestão de ativos, segregação e validação de software                                      |

---

## 📋 Estrutura sugerida de cada política

Cada política organizacional deve conter, no mínimo:

- **Objetivo e âmbito** (aplicação a pipelines, ambientes, equipas, tipos de artefactos);
- **Critérios obrigatórios e permissões explícitas** (ex: runners autorizados, fontes de segredos, regras de deploy);
- **Papéis e responsabilidades** (DevOps, Segurança, AppSec, donos de produto);
- **Mecanismos de registo, validação e rastreabilidade** (ex: proveniência, logs de execução, aprovação de exceções);
- **Regras de revisão periódica da política** (ex: revisão anual, ou após incidentes).

---

## ✅ Recomendações finais

- As políticas devem ser **oficialmente aprovadas pela gestão técnica e de segurança**;
- Devem estar **acessíveis a todas as equipas envolvidas nos pipelines e entregas**;
- A sua existência é **condição necessária para garantir maturidade e auditabilidade do ciclo CI/CD**;
- A sua aplicação deve ser visível nas práticas definidas neste capítulo, com **ligação direta a controlos e validações no pipeline**.

> 📌 Templates para estas políticas poderão ser disponibilizados como ficheiros `60-*.md` em futuras versões do manual.
