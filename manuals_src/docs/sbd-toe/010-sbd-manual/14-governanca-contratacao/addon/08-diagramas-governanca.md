---
description: Diagramas visuais dos fluxos de governação, exceções e validações formais
id: diagramas-governanca
sidebar_position: 8
tags:
- contratacao
- diagramas
- excecoes
- fluxo
- fornecedores
- validacao
- validação
title: Diagramas de Governação de Segurança
---



# 🗾️ Diagramas de Apoio à Governança

Este anexo inclui diagramas que representam os principais fluxos de decisão, rastreabilidade e validação descritos no Capítulo 14 - Governança e Contratação.

---

## 📌 1. Fluxo de aprovação de exceção

```mermaid
flowchart TD
  A[Requisito não aplicável] --> B[Justificação técnica documentada]
  B --> C[Proposta de compensação]
  C --> D[Avaliação AppSec]
  D --> E{Aprovação formal?}
  E -->|Sim| F[Exceção registada com owner e validade]
  E -->|Não| G[Controlo obrigatório aplica-se]
```

---

## 📅 2. Onboarding de fornecedor externo

```mermaid
flowchart TD
  A[Pedido de integração de fornecedor] --> B[Classificação de risco do sistema]
  B --> C[Checklist e questionário de segurança]
  C --> D[Análise AppSec + Procurement]
  D --> E{Requisitos cumpridos?}
  E -->|Sim| F[Aprovação de onboarding]
  E -->|Não| G[Negociação / Compensação / Rejeição]
```

---

## 🔗 3. Rastreabilidade organizacional

```mermaid
flowchart LR
  R[Risco: L1/L2/L3] --> Q[Requisitos do Catálogo SbD-ToE]
  Q --> C[Contrato com cláusulas]
  C --> V[Validação: testes, auditoria, evidência]
  V --> E[Registo de exceções se aplicável]
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
  E -->|Sim| F[Atualização do registo / exceção]
  E -->|Não| G[Confirmação e encerramento do ciclo]
```
