---
id: criterios-validacao
title: 📋 Critérios de Validação Arquitetural
description: Validação por requisito (ARC-001 a ARC-011) com foco em risco, ciclo de vida e responsabilidade
sidebar_position: 5
---

# 📋 Validação Arquitetural - Critérios por Requisito

Este documento define como validar os requisitos de arquitetura segura (ARC-001 a ARC-011), com base no:

- **nível de risco da aplicação** (L1–L3),
- **ciclo de vida da arquitetura** (design, alteração, exceção),
- **papel responsável pela validação** (Arquiteto, AppSec, Revisor técnico).

---

## ✅ Validação por Requisito

| Requisito | O que validar | Como validar | Quando | Responsável |
|-----------|----------------|---------------|--------|-------------|
| ARC-001 | Zonas de confiança identificadas | Diagrama com zonas assinaladas e justificadas | Design inicial | Arquiteto técnico |
| ARC-002 | Fronteiras técnicas claras (ex: proxies, gateways, ACLs) | Análise de isolamento entre componentes | Revisão de segurança | AppSec |
| ARC-003 | Fluxos críticos representados | DFD ou diagrama de arquitetura que cubra entrada/saída de dados | Design inicial + atualizações | Dev + Revisor técnico |
| ARC-004 | Versão auditável do diagrama | Repositório controlado + hash/versionamento | Submissão à aprovação | DevOps / Arquiteto |
| ARC-005 | Aplicação de critérios formais | Checklist técnico por nível de risco | Antes da aprovação | Revisor AppSec |
| ARC-006 | Avaliação de impacto arquitetónico | Análise da alteração + plano de mitigação | Em alterações estruturais | Arquiteto + PO |
| ARC-007 | Validação de padrões internos | Aprovação formal do padrão usado | Antes de reutilização | Equipa de arquitetura |
| ARC-008 | Rastreabilidade requisitos ↔ arquitetura | Mapeamento entre requisitos e componentes | Final do design | Arquiteto + Segurança |
| ARC-009 | Reutilização de modelos validados | Verificação da conformidade do projeto com o modelo | Início do projeto | Equipa técnica |
| ARC-010 | Threat modeling incluído | Registo de modelação STRIDE ou DFD com marcações | Projetos L2 e L3 | AppSec + Arquitetura |
| ARC-011 | Exceções justificadas e aprovadas | Formulário de exceção aprovado, data de revisão definida | Sempre que aplicável | Arquiteto + Segurança |

---

## 🎯 Aplicação prática por nível de risco

| Critério / Nível de risco | L1 | L2 | L3 |
|---------------------------|:--:|:--:|:--:|
| Validação informal por Arquiteto técnico | ✔️ | ✔️ | ✔️ |
| Validação formal por AppSec |   | ✔️ | ✔️ |
| Revisão por comité técnico |   |   | ✔️ |
| Evidência arquivada com a release |   | ✔️ | ✔️ |
| Atualização após alteração relevante | ✔️ | ✔️ | ✔️ |

---

## 📎 Notas de apoio

- Estes critérios devem ser integrados nos eventos de entrega técnica e ciclos de planeamento de arquitetura.
- Validações podem ser incluídas em workflows de pull requests, aprovações de infraestrutura ou documentação técnica.
- Os requisitos e validações estão alinhados com [`addon/01-catalogo-requisitos.md`](/sbd-toe/sbd-manual/requisitos-seguranca/addon/catalogo-requisitos).

> A validação não é um ato pontual: é uma **atividade contínua que acompanha a arquitetura ao longo da vida da aplicação**.

> 📌 Este anexo complementa o `20-checklist-revisao.md` com critérios formais para contextos de maior criticidade.
