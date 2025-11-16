---
id: checklist-revisao
title: Checklist - CI/CD Seguro
sidebar_label: Checklist de Revisão
description: Lista de verificação objetiva da adoção das práticas de segurança em pipelines CI/CD
tags: [checklist, auditoria, cicd, devsecops, pipelines]
sidebar_position: 20
---


# ✅ Checklist de Revisão Periódica de CI/CD Seguro

Este checklist aplica-se a todas as aplicações com pipelines de integração e entrega contínua, avaliadas segundo os critérios do **Capítulo 07 - CI/CD Seguro**.  
Serve como instrumento de verificação e auditoria da **conformidade com os controlos mínimos prescritos para segurança de pipelines, artefactos, segredos e ambientes de execução**.

Pode ser usado:

- Como tarefa técnica ou de segurança (ex: `[SEC] Rever conformidade CI/CD`)
- Em momentos formais de release, aprovação de exceções ou auditoria
- Como **KPI operativo** de maturidade em DevSecOps
- Como critério de promoção de aplicações para produção

> 🗓️ **Recomenda-se revisão no mínimo a cada 6 meses**, ou sempre que houver alterações relevantes ao pipeline, runners, segredos, políticas ou artefactos.

---

## 📋 Itens de verificação

| Item                                                                                           | Verificado? |
|------------------------------------------------------------------------------------------------|-------------|
| O pipeline está definido como código versionado e revisto por pull request?                   | ☐           |
| Os triggers do pipeline são restritos e controlados (ex: PRs autorizados, tags protegidas)?   | ☐           |
| Existem validações de segurança integradas (SAST, secrets, IaC, containers)?                  | ☐           |
| Os segredos são injetados de forma segura (vault ou variáveis protegidas)?                    | ☐           |
| O pipeline utiliza runners dedicados e descartáveis (pelo menos para L2/L3)?                   | ☐           |
| Os artefactos são gerados com proveniência verificável e, se aplicável, assinados?            | ☐           |
| Existem políticas CI/CD aplicadas por nível de risco (L1–L3)?                                 | ☐           |
| O pipeline aplica gates de segurança antes do deploy (ex: findings críticos bloqueiam)?        | ☐           |
| O deploy é rastreável até ao pipeline e commit de origem?                                     | ☐           |
| As exceções a políticas CI/CD estão registadas, aprovadas e com prazo de revisão definido?     | ☐           |

---

## 🔄 Notas finais

- Este checklist pode ser usado como base para **dashboards de maturidade CI/CD, formulários automatizados ou tarefas de backlog**.
- Pode ser integrado com ferramentas como GitHub, GitLab, Azure DevOps, Jira, Confluence ou plataformas GRC.
- A validação de todos os itens permite afirmar conformidade com o Capítulo 07 para efeitos de maturidade SbD-ToE.

