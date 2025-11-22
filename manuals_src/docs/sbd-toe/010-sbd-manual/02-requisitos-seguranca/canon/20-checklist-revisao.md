---
description: Verificações obrigatórias por projeto para garantir a aplicação dos requisitos
  definidos
id: checklist-revisao
sidebar_position: 20
tags:
- auditoria
- checklist
- desenvolvimento
- rastreabilidade
- requisitos
- validacao
- validação
title: Checklist de Revisão - Requisitos de Segurança
---


# ✅ Checklist de Verificação - Requisitos de Segurança

Este ficheiro fornece uma lista objetiva e auditável para avaliar se os requisitos de segurança foram devidamente definidos, aplicados e rastreados ao longo do ciclo de vida da aplicação, conforme prescrito neste capítulo.

> Pode ser utilizado como instrumento de controlo por projeto, por sprint ou por tipo de risco.

---

## 📋 Estrutura da Checklist

| Nº | Verificação                                                                 | Risco | Referência                                | Aplicado? (✔/✘) |
|----|------------------------------------------------------------------------------|-------|-------------------------------------------|-----------------|
| 1  | Existe **catálogo de requisitos de segurança** adaptado à organização?      | L1    | `addon/01-catalogo-requisitos.md`         |                 |
| 2  | Foram atribuídas **tags de rastreabilidade normalizadas** (SEC-Lx-TEMA-XXX) aos requisitos definidos? | L1–L3 | `addon/09-taxonomia-rastreabilidade.md`    |                 |
| 3  | A seleção de requisitos por projeto é feita com base na **classificação de risco**? | L1–L3 | `addon/06-matriz-controlos-por-risco.md`  |                 |
| 4  | Foram identificados e registados os requisitos aplicáveis ao projeto?       | L1–L3 | `addon/01`, `addon/06`                     |                 |
| 5  | Os requisitos estão **integrados no backlog ou artefactos de arquitetura**? | L1–L3 | `15-aplicacao-lifecycle.md`          |                 |
| 6  | Existem **user stories ou tasks** que implementam requisitos de segurança?  | L2    | `15-aplicacao-lifecycle.md`          |                 |
| 7  | Os requisitos estão **rastreáveis a controlos técnicos ou processuais**?    | L2/L3 | `addon/06`, `25-rastreabilidade.md`  |                 |
| 8  | Existem **critérios de aceitação de segurança** definidos por requisito?    | L2/L3 | `15-aplicacao-lifecycle.md`          |                 |
| 9  | Os requisitos são **validados em testes ou revisões de código**?            | L2/L3 | `achievable-maturity`, `15`       |                 |
| 10 | Foram consideradas **restrições legais, normativas ou contratuais**?        | L1–L3 | `25-rastreabilidade.md`              |                 |
| 11 | Existe processo para **atualização de requisitos em função de alterações**? | L1–L3 | `addon/06`, `15-aplicacao-lifecycle.md` |             |

---

## 📌 Utilização recomendada

- Esta checklist pode ser utilizada como instrumento de verificação por projeto, sprint ou release.
- Os resultados podem servir como **indicador de controlo operacional** e **KPI de maturidade de aplicação do modelo SbD-ToE**.
- A existência de um catálogo de requisitos (`item 1`) e a sua seleção proporcional (`item 3`) devem ser consideradas **pré-condições obrigatórias** para a adoção das restantes práticas.
- O alinhamento com frameworks como OWASP SAMM, SSDF e DSOMM reforça o valor destas verificações, especialmente nos domínios de **Security Requirements** e **Reusable Controls** (ver `achievable-maturity`).

