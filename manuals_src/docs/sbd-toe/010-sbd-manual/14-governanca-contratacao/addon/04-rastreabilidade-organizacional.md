---
id: rastreabilidade-organizacional
title: Rastreabilidade Organizacional de Segurança
sidebar_position: 4
description: Modelo de registo e justificação formal de decisões e entregáveis de segurança
tags: [rastreabilidade, evidencias, compliance, auditoria]
---



# 🔗 Modelo de Rastreabilidade Organizacional

## 🌟 Objetivo

Garantir que existe uma **ligação clara, documentada e auditável** entre:

* A **classificação de risco** atribuída a cada aplicação ou sistema;
* Os **requisitos de segurança aplicados** (Cap. 2);
* As **cláusulas contratuais e exigências a terceiros** (Cap. 14.2);
* Os **mecanismos de validação** (testes, revisões, evidência);
* A **documentação de exceções ou compensações** (Cap. 14.1);
* E os **responsáveis nomeados** por cada decisão.

---

## 📈 Estrutura de rastreabilidade recomendada

| Aplicativo / Projeto | Risco (L1-L3) | Requisitos aplicados | Exceções aprovadas  | Fornecedor / Serviço | Evidência existente | Owner de segurança  |
| -------------------- | ------------- | -------------------- | ------------------- | -------------------- | ------------------- | ------------------- |
| Ex: Portal RH        | L3            | REQ-001, REQ-002...  | REQ-017 justificada | Fornecedor ABC       | Teste CI + cláusula | joao.silva\@empresa |

> 🔹 Esta estrutura pode ser mantida em Excel, SharePoint, Jira ou outra ferramenta ALM com suporte a traçabilidade.

---

## 🔄 Mecanismos de atualização

* A tabela deve ser atualizada:

  * Em cada release relevante;
  * Sempre que haja alterações de risco, fornecedor ou requisitos;
  * Na aprovação de exceções ou onboarding de novos terceiros.

* A responsabilidade pela atualização deve ser atribuída ao **owner de segurança do projeto**.

---

## 🔢 Integração com GRC, auditorias e conformidade

* Este modelo pode ser usado como **fonte de verdade** para:

  * Avaliação de conformidade com ISO 27001, NIS2, PCI-DSS;
  * Revisões internas de GRC;
  * Análise de exceções e compensações por parte da equipa AppSec.

* Pode ser consolidado com **dashboards trimestrais ou semestrais**, tais como:

  * % de aplicações com rastreabilidade completa;
  * % de aplicações com exceções aprovadas;
  * % de aplicações com evidência validada.

---

## 📊 Sugestão de visualização

```mermaid
flowchart LR
  R[Risco Classificado (L1/L2/L3)] --> Q[Requisitos Selecionados]
  Q --> C[Contrato com Cláusulas Alinhadas]
  C --> V[Validação: testes, revisões, SBOM, etc.]
  V --> E[Evidência Documentada]
  E --> D[Decisões de exceção se aplicável]
  D --> O[Owner nomeado / revalidação futura]
```

---

## ✅ Recomendações finais

* Esta tabela deve ser usada como **base para governação técnica** e decisão executiva;
* Deve integrar os dados provenientes dos **checklists por capítulo SbD-ToE**;
* Pode ser usada para **construir KPIs de maturidade e visibilidade** (ver Cap. 14.30).

---

## 🔗 Ligações cruzadas

* Cap. 1 — Classificação de risco
* Cap. 2 — Requisitos e matriz de aplicação
* Cap. 14.1 — Governação e exceções
* Cap. 14.2 — Cláusulas contratuais
* Cap. 14.3 — Validação de fornecedores
* Cap. 14.30 — KPIs de governação

---
