---
id: adopcao-drp-bia
title: Alternativa — Classificação por Criticidade Operacional (DRP / BIA)
sidebar_position: 7
tags: [tipo:alternativa, drp, bia, classificacao, risco]
---
<!--template: sbdtoe-addon -->

# 📎 Classificação Alternativa via DRP / BIA

## 🎯 Objetivo

Permitir que **classificações já existentes** — nomeadamente **DRP (Disaster Recovery Plan)**, **BIA (Business Impact Analysis)** ou modelos equivalentes — sejam usadas **como mecanismo alternativo de classificação aplicacional**, quando o objetivo é **assegurar um nível de cuidado proporcional à criticidade operacional**, mesmo que isso resulte numa classificação conservadora.

Este modelo é especialmente útil quando:
- a organização já dispõe de classificações formais de continuidade;
- o custo de indisponibilidade é elevado;
- ou existe baixa tolerância a erro, falha ou downtime.

---

## 🧠 Princípio fundamental

No SbD-ToE, a classificação de risco serve primariamente para:

> **determinar o nível de rigor, controlo e validação a aplicar ao longo do SDLC**

Não para afirmar uma verdade absoluta sobre o risco “real”.

Assim, é **aceitável e deliberado** classificar uma aplicação como mais crítica do que a análise técnica estrita indicaria, quando:

- a aplicação tem de estar sempre disponível;
- o tempo de recuperação é muito reduzido (RTO/RPO baixos);
- o impacto operacional de falha é elevado;
- ou a organização decide aplicar uma postura conservadora.

---

## 📘 Enquadramento DRP / BIA

Modelos de DRP e BIA tipicamente classificam sistemas com base em:

- RTO (Recovery Time Objective)
- RPO (Recovery Point Objective)
- Impacto financeiro
- Impacto reputacional
- Impacto operacional
- Prioridade de recuperação

Embora não sejam modelos de segurança, estes critérios são **bons proxies de criticidade**, e justificam a aplicação de **controlos de segurança reforçados**.

---

## 🔁 Correspondência prática (proxy conservador)

| Classificação DRP / BIA | Classificação SbD-ToE adotada | Racional |
|------------------------|-------------------------------|----------|
| **Crítico**            | **L3 — Risco Elevado**        | Falha não tolerável ⇒ máximo rigor |
| **Importante / Médio** | **L2 — Risco Médio**          | Downtime limitado ⇒ controlos reforçados |
| **Baixo / Não essencial** | **L1 — Risco Baixo**      | Impacto reduzido ⇒ controlos mínimos |

> 📌 Esta correspondência **não implica que o risco técnico seja elevado**,  
> apenas que a aplicação **deve ser tratada como tal**.

---

## 📝 Exemplo típico

Aplicação classificada como **Crítica** no DRP:

- RTO < 2h  
- RPO ≈ 0  
- Processo core de negócio  
- Impacto imediato em clientes

Mesmo que:
- os dados não sejam sensíveis,
- a exposição seja controlada,

→ a aplicação é classificada como **L3**,  
para garantir:
- threat modeling formal,
- testes contínuos,
- validações reforçadas,
- e maior disciplina operacional.

Este *over-classification* é **intencional e aceitável**.

---

## ⚖️ Relação com o modelo E/D/I

Quando esta abordagem é usada:

- o modelo E/D/I **pode ser simplificado ou omitido**;
- ou usado apenas como **validação adicional**;
- a decisão deve ser registada como:
  > “Classificação por criticidade operacional (DRP/BIA)”.

Não é necessário provar que:
- exposição, dados e impacto técnico justificam L3;
- basta justificar que **o custo de falha o exige**.

---

## 🧩 Recomendações de governação

- Documentar explicitamente que a classificação foi feita por proxy DRP/BIA
- Garantir consistência entre DRP, BIA e inventário aplicacional
- Evitar rebaixar classificações críticas sem revisão formal
- Usar esta abordagem sobretudo em:
  - sistemas core,
  - plataformas transversais,
  - infraestruturas partilhadas,
  - serviços regulados

---

## 📌 Nota final

Esta abordagem **não substitui** o modelo de risco do SbD-ToE.  
Representa uma **decisão consciente de governação**, que privilegia:

> **segurança por excesso de cuidado,  
> em contextos onde errar para menos não é aceitável.**
