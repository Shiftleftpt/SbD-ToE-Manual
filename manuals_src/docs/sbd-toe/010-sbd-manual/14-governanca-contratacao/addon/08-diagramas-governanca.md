---
id: diagramas-governanca
title: Diagramas de Governação de Segurança
sidebar_position: 8
description: Diagramas visuais dos fluxos de governação, exceções e validações formais
tags: [diagramas, excecoes, fluxo, validacao]
---


# 🗾️ Diagramas de Apoio à Governança

Este anexo inclui diagramas que representam os principais fluxos de decisão, rastreabilidade e validação descritos no Capítulo 14 — Governança e Contratação.

---

## 📌 1. Fluxo de aprovação de exceção

```mermaid
flowchart TD
  A[Requisito não aplicável] --> B[Justificação técnica documentada]
  B --> C[Proposta de compensação]
  C --> D[Avaliação AppSec]
  D --> E{Aprovação formal?}
  E -- Sim --> F[Exceção registada com owner e validade]
  E -- Não --> G[Controlo obrigatório aplica-se]
```

---

## 📅 2. Onboarding de fornecedor externo

```mermaid
flowchart TD
  A[Pedido de integração de fornecedor] --> B[Classificação de risco do sistema]
  B --> C[Checklist e questionário de segurança]
  C --> D[Análise AppSec + Procurement]
  D --> E{Requisitos cumpridos?}
  E -- Sim --> F[Aprovação de onboarding]
  E -- Não --> G[Negociação / Compensação / Rejeição]
```

---

## 🔗 3. Rastreabilidade organizacional

```mermaid
flowchart LR
  R[Risco: L1/L2/L3] --> Q[Requisitos do Catálogo SbD-ToE]
  Q --> C[Contrato com cláusulas]
  C --> V[Validação: testes, auditoria, evidência]
  V --> E[Registo de exceções (se aplicável)]
  E --> O[Owner e prazo de revisão]
```

---

## 🔄 4. Ciclo de revisão e validação continuada

```mermaid
flowchart TD
  A[Release / Evento crítico] --> B[Reavaliação do risco]
  B --> C[Revisão dos requisitos aplicados]
  C --> D[Validação de conformidade + evidência]
  D --> E{Alterou-se o risco ou requisitos?}
  E -- Sim --> F[Atualização do registo / exceção]
  E -- Não --> G[Confirmação e encerramento do ciclo]
```

---

## 📆 5. Escalonamento de decisão de risco

```mermaid
flowchart TD
  A[Controlo não aplicado] --> B[Análise pelo Owner de Projeto]
  B --> C[Revisão AppSec / Arquiteto]
  C --> D{Impacto organizacional?}
  D -- Elevado --> E[Aprovação por CISO / Direção]
  D -- Moderado --> F[Aprovação por Equipa Técnica]
```

---

## 🧩 6. Governação de sistemas legados ou não conformes

```mermaid
flowchart TD
  A[Sistema legado identificado] --> B[Classificação de risco atual]
  B --> C[Mapeamento de requisitos aplicáveis]
  C --> D{Controlo técnico viável?}
  D -- Sim --> E[Plano de remediação técnica]
  D -- Não --> F[Registo de exceção organizacional]
  F --> G[Definição de compensações e reavaliação periódica]
```

> 🔍 Este fluxo articula-se com o Capítulo 09 (*containers* e Execução Isolada) e Capítulo 08 (IaC), nos casos de infraestruturas antigas ou pipelines herdados.

---

## 🎓 7. Validação de formação obrigatória por função crítica

```mermaid
flowchart TD
  A[Owner / Aprovador designado] --> B[Verificação de formação SbD (Cap. 13)]
  B --> C{Formação válida (\<12 meses)?}
  C -- Sim --> D[Validação formal autorizada]
  C -- Não --> E[Formação obrigatória antes de validação]
```

> 📚 Este fluxo aplica-se a qualquer capítulo que requeira owners, validadores ou aprovadores formais, e deve ser integrado com o Cap. 13 — Formação e Onboarding.

---

> 📄 Estes diagramas simples podem ser incluídos em relatórios, formação ou documentação de processos. A sua utilização facilita a adoção organizacional e o alinhamento entre equipas técnicas, GRC e gestão executiva.

---
