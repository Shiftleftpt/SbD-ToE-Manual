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

Este ficheiro funciona como:

- Instrumento de **controlo binário** (sim / não) por projeto
- **Mecanismo de auditoria** técnica e organizacional
- **KPI operativo** de maturidade em DevSecOps
- Critério objetivo para **promoção de aplicações** para produção

> 🗓️ **Recomenda-se revisão no mínimo a cada 6 meses**, ou sempre que existam alterações relevantes ao pipeline, runners, segredos, políticas, integrações externas ou modelo de promoção.

---

## 📋 Itens de verificação

| Item                                                                                                               | Verificado? |
|--------------------------------------------------------------------------------------------------------------------|-------------|
| O pipeline está definido como código, versionado e sujeito a revisão por *pull request*?                           | ☐           |
| A configuração efetiva do pipeline executado (excluindo segredos) é rastreável e preservada para auditoria?       | ☐           |
| Os *triggers* do pipeline são restritos e controlados (ex: PRs autorizados, tags protegidas)?                     | ☐           |
| Existem validações de segurança integradas com execução observável (SAST, secrets, IaC, containers, etc.)?       | ☐           |
| Os resultados dos scanners correspondem a execução real (logs, *run id*, *exit code*) e não apenas a relatórios? | ☐           |
| Os segredos são injetados de forma segura, temporária e sem exposição em logs ou artefactos?                      | ☐           |
| O pipeline utiliza runners dedicados, isolados e descartáveis (obrigatório para L2/L3)?                           | ☐           |
| Os artefactos são gerados com proveniência verificável e, quando aplicável, assinados antes de promoção?          | ☐           |
| Existem políticas CI/CD formalizadas e aplicadas por nível de risco (L1–L3)?                                      | ☐           |
| Os *gates* de segurança são explícitos, binários e aplicados antes de qualquer ação irreversível (deploy)?        | ☐           |
| As decisões de promoção ou bypass de *gates* têm responsável humano identificado e registado?                    | ☐           |
| O deploy é rastreável até ao pipeline e *commit* de origem (commit → pipeline → artefacto → release)?             | ☐           |
| As exceções a políticas CI/CD estão registadas, aprovadas, temporárias e com compensações definidas?              | ☐           |
| Integrações externas do pipeline são conhecidas, aprovadas e tratadas como dependências de supply chain?          | ☐           |
| Existe retenção adequada de logs, metadados e evidências para investigação e auditoria?                           | ☐           |

---

## 🔄 Notas finais

- Este checklist deve ser aplicado **por pipeline e por aplicação**, não apenas de forma genérica.
- O resultado pode ser usado diretamente como:
  - tarefa técnica (`[SEC] Revisão CI/CD Seguro`);
  - evidência de auditoria;
  - input para dashboards de maturidade;
  - critério objetivo de aprovação de *release*.
- Um item assinalado como **não conforme** implica:
  - correção técnica,
  - registo de exceção formal,
  - ou bloqueio de promoção, conforme o nível de risco da aplicação.

A validação completa deste checklist permite afirmar **conformidade prática e auditável** com o Capítulo 07 do SbD-ToE.
