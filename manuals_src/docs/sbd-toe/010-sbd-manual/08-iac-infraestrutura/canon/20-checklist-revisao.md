---
id: checklist-revisao
title: Checklist de Revisão - Infraestrutura como Código (IaC)
sidebar_position: 20
sidebar_label: Checklist de Revisão
description: Checklist binário e auditável para verificar a aplicação prática das prescrições de segurança para IaC.
tags: [checklist, validação, revisão, iac, infraestrutura como código, controlo]
---


# ✅ Checklist de Revisão Periódica de Práticas de IaC

Este checklist aplica-se a todos os projetos de **Infraestrutura como Código (IaC)** desenvolvidos ou mantidos internamente. Serve como instrumento de verificação binária e auditável da **adoção prática das prescrições do Capítulo 08**, permitindo:

* Controlo objetivo da aplicação dos requisitos `IAC-001` a `IAC-010`;
* Integração com processos de PR, release, auditoria e onboarding;
* Geração de indicadores operacionais e de conformidade.

> 🗓️ **Recomenda-se revisão a cada nova release, PR relevante ou alteração em ambiente crítico.**

---

## 📋 Itens de Verificação

| Item                                                                             | Verificado? |
| -------------------------------------------------------------------------------- | ----------- |
| O backend remoto está configurado com locking e encriptação (`IAC-001`)          | ☐           |
| Os ambientes são segregados e versionados (`IAC-002`)                            | ☐           |
| Existe validação automática no CI/CD (lint, policy, tfsec, etc.) (`IAC-003`)     | ☐           |
| Todos os módulos são confiáveis, pinados ou revistos manualmente (`IAC-004`)     | ☐           |
| Existe histórico de alterações, tagging e releases (`IAC-005`)                   | ☐           |
| As convenções de naming e diretórios são aplicadas e documentadas (`IAC-006`)    | ☐           |
| Cada `plan` é revisto e aprovado antes de `apply` (`IAC-007`)                    | ☐           |
| Existe rastreabilidade entre ficheiros e recursos/ambientes afetados (`IAC-008`) | ☐           |
| O pipeline aplica enforcement automático de políticas (`IAC-009`)                | ☐           |
| Os artefactos `plan`, `apply`, manifests são versionados com hash (`IAC-010`)    | ☐           |

---

## 🔄 Integração Operacional

* Este checklist pode ser aplicado manualmente (ex: revisão de PR) ou integrado no CI/CD como gate.
* Pode ser usado em revisões formais de arquitetura, releases ou onboarding de novos repositórios.
* Cada item deve ser validado com **evidência objetiva**:

  * Ficheiros `backend.tf`, logs de `tfsec`, screenshots de CI, hashes em releases, etc.

> ⚠️ Respostas negativas requerem exceção formal, aprovada e documentada (ver modelo de governação).

---

## 📊 Conformidade e KPI

* A validação deste checklist permite declarar **conformidade com o Capítulo 08 - Infraestrutura como Código**.
* A contagem de itens verificados pode ser usada para **KPIs operacionais de adoção e maturidade**.
* Pode ser incluído como evidência em auditorias, processos de exceção ou gates de release.

> 📌 Este mecanismo está alinhado com o modelo de **controlo contínuo e rastreabilidade** definido no SbD-ToE.
