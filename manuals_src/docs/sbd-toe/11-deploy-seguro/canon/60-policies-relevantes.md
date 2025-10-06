---
id: policies-deploy-seguro
title: Políticas Organizacionais sobre Deploy Seguro
description: Políticas formais necessárias para garantir a segurança, reversibilidade e rastreabilidade de deploys em produção.
tags: [policy, organizacional, deploy, rollback, validação, rastreabilidade]
sidebar_position: 60
---


# 🏠 Políticas Organizacionais — Deploy Seguro {deploy-seguro:canon:policies-deploy-seguro}

A aplicação consistente e eficaz do Capítulo 11 — **Deploy Seguro** — exige a existência de **políticas organizacionais formais** que regulem as condições técnicas e operacionais para execução de código em produção, com foco em:

- Validação pré-deploy (readiness);
- Gating e aprovação formal;
- Logging, rastreabilidade e reversibilidade;
- Requisitos para rollback testado e documentado.

---

## 📌 Nota fundamental {deploy-seguro:canon:policies-deploy-seguro#nota_fundamental}

> ⚠️ A execução segura de software em produção **depende de critérios técnicos e operacionais bem definidos e formalizados**.

Estas políticas devem:

- Estabelecer regras para aprovação de releases e gates de deploy;
- Tornar obrigatória a existência de plano de rollback testado;
- Definir papéis e responsabilidades para autorização, validação e execução do deploy;
- Estipular como garantir rastreabilidade e reversibilidade.

> 📑 Estas políticas devem estar alinhadas com os processos definidos no capítulo e ser auditáveis.

> 🔹 Frameworks como **SSDF**, **SAMM**, **SLSA** e **BSIMM** recomendam explicitamente a existência destas políticas.

---

## 📓 Políticas recomendadas {deploy-seguro:canon:policies-deploy-seguro#politicas_recomendadas}

| Nome da Política                                  | Obrigatória? | Aplicação                                     | Resumo do conteúdo necessário                                             |
|---------------------------------------------------|--------------|--------------------------------------------------|-------------------------------------------------------------------------|
| Política de Aprovação de Releases              | ✅ Sim      | Todas as releases para produção                | Critérios de readiness, checklist obrigatória, owners e aprovação formal |
| Política de Rollback e Reversibilidade           | ✅ Sim      | Todas as releases com impacto operacional        | Exigência de plano de rollback, teste prévio, execução documentada        |
| Política de Logging e Rastreabilidade            | ✅ Sim      | Todos os ambientes de produção e staging       | Requisitos de logging, versionamento, toggles e auditabilidade           |
| Política de Gating e Automatis\-mo de Deploy      | ⚠ Opcional | Pipelines com deploy automatizado               | Definição de gates, aprovação automática, bloqueio por findings         |
| Política de Validação em Ambiente de Staging    | ✅ Sim      | Projetos com staging ou pre-prod                | Validação funcional, métricas e readiness com evidência                   |
| Política de Autonomia e Responsabilidade de Deploy | ⚠ Opcional | Equipas com deploy self-service ou continuo     | Quem pode autorizar, requisitos mínimos, registo de decisões             |

---

## 📆 Correspondência com frameworks normativas {deploy-seguro:canon:policies-deploy-seguro#correspondencia_com_frameworks_normativas}

| Framework        | Requisitos cobertos pelas políticas acima                                                            |
|-----------------|------------------------------------------------------------------------------------------------------------------|
| **NIST SSDF**    | PS.2 (Release authorization), RV.4 (Rollback), RV.5 (Logging), PO.1 (Release Readiness)                         |
| **SLSA v1.0**    | Requirements for provenance, versioning, release policies, tamper resistance                                    |
| **OWASP SAMM**   | Operations > Environment Management / Release Management                                                       |
| **BSIMM13**      | SE2.5 (Operate securely in production), CMVM2.3 (Audit logging), TVM3.2 (Automate release gates)               |
| **CIS Controls** | Control 6 (Access Control), Control 8 (Audit Log Management), Control 16 (Application Software Security)        |

---

## 📄 Estrutura sugerida de cada política {deploy-seguro:canon:policies-deploy-seguro#estrutura_sugerida_de_cada_politica}

Cada política organizacional deve conter:

- Objetivo e âmbito;
- Regras obrigatórias e condicionantes (ex: não há deploy sem rollback testado);
- Papéis e responsabilidades (Dev, QA, AppSec, Produto);
- Requisitos de rastreabilidade, logging e evidências;
- Modo de integração com pipelines (automático, manual, gated);
- Periodicidade de revisão e auditoria.

---

## ✅ Recomendações finais {deploy-seguro:canon:policies-deploy-seguro#recomendacoes_finais}

- Estas políticas devem ser aprovadas pelas áreas de **segurança, QA e produto**;
- Devem estar **acessíveis, versionadas e conhecidas** por todas as equipas envolvidas em deploy;
- Devem ser **implementadas via CI/CD sempre que possível**, com gates, validadores e logs integrados;
- A sua existência é um requisito essencial para deploy seguro, auditável e reversível.

> 📁 Templates de política poderão ser incluídos em ficheiros `60-*.md` adicionais em futuras versões do manual.
