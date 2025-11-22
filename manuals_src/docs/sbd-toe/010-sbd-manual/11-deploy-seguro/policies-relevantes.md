---
description: Políticas formais necessárias para garantir a segurança, reversibilidade
  e rastreabilidade de deploys em produção.
id: policies-relevantes
sidebar_position: 60
tags:
- deploy
- organizacional
- policy
- políticas
- rastreabilidade
- rollback
- validacao
title: Policies
---



# 🏠 Políticas Organizacionais - Deploy Seguro

A aplicação consistente e eficaz do Capítulo 11 - **Deploy Seguro** - exige a existência de **políticas organizacionais formais** que regulem as condições técnicas e operacionais para execução de código em produção, com foco em:

- Validação pré-deploy (readiness);
- Gating e aprovação formal;
- Logging, rastreabilidade e reversibilidade;
- Requisitos para rollback testado e documentado.

---

## 📌 Nota fundamental

> ⚠️ A execução segura de software em produção **depende de critérios técnicos e operacionais bem definidos e formalizados**.

Estas políticas devem:

- Estabelecer regras para aprovação de releases e gates de deploy;
- Tornar obrigatória a existência de plano de rollback testado;
- Definir papéis e responsabilidades para autorização, validação e execução do deploy;
- Estipular como garantir rastreabilidade e reversibilidade.

> 📑 Estas políticas devem estar alinhadas com os processos definidos no capítulo e ser auditáveis.

---

## 📓 Políticas recomendadas

| Nome da Política                                  | Obrigatória? | Aplicação                                     | Resumo do conteúdo necessário                                             |
|---------------------------------------------------|--------------|--------------------------------------------------|-------------------------------------------------------------------------|
| Política de Aprovação de Releases              | ✅ Sim      | Todas as releases para produção                | Critérios de readiness, checklist obrigatória, owners e aprovação formal |
| Política de Rollback e Reversibilidade           | ✅ Sim      | Todas as releases com impacto operacional        | Exigência de plano de rollback, teste prévio, execução documentada        |
| Política de Logging e Rastreabilidade            | ✅ Sim      | Todos os ambientes de produção e staging       | Requisitos de logging, versionamento, toggles e auditabilidade           |
| Política de Gating e Automatis\-mo de Deploy      | ⚠ Opcional | Pipelines com deploy automatizado               | Definição de gates, aprovação automática, bloqueio por findings         |
| Política de Validação em Ambiente de Staging    | ✅ Sim      | Projetos com staging ou pre-prod                | Validação funcional, métricas e readiness com evidência                   |
| Política de Autonomia e Responsabilidade de Deploy | ⚠ Opcional | Equipas com deploy self-service ou continuo     | Quem pode autorizar, requisitos mínimos, registo de decisões             |

---

## 📄 Estrutura sugerida de cada política

Cada política organizacional deve conter:

- Objetivo e âmbito;
- Regras obrigatórias e condicionantes (ex: não há deploy sem rollback testado);
- Papéis e responsabilidades (Dev, QA, AppSec, Produto);
- Requisitos de rastreabilidade, logging e evidências;
- Modo de integração com pipelines (automático, manual, gated);
- Periodicidade de revisão e auditoria.

---

## ✅ Recomendações finais

- Estas políticas devem ser aprovadas pelas áreas de **segurança, QA e produto**;
- Devem estar **acessíveis, versionadas e conhecidas** por todas as equipas envolvidas em deploy;
- Devem ser **implementadas via CI/CD sempre que possível**, com gates, validadores e logs integrados;
- A sua existência é um requisito essencial para deploy seguro, auditável e reversível.

> 📁 Templates de política poderão ser incluídos em ficheiros `60-*.md` adicionais em futuras versões do manual.
