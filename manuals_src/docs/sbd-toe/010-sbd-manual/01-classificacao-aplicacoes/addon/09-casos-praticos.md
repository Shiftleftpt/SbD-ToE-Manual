---
id: casos-praticos
title: Exemplos de Aplicação da Classificação de Risco
sidebar_position: 9
tags: [tipo:exemplo, tema:classificacao, risco, aplicacao]
---

# 🧪 Casos Práticos de Classificação de Risco

Os exemplos seguintes ilustram **diferentes formas legítimas de classificar aplicações** no SbD-ToE, demonstrando:

- aplicação direta do modelo **E/D/I**;
- impacto de **dados e contexto regulatório**;
- uso de **classificação conservadora por criticidade operacional**;
- influência de **automação avançada (incl. IA)** quando relevante.

O objetivo não é encontrar a “classificação perfeita”,  
mas **assegurar o nível adequado de cuidado e controlo**.

---

## 📝 Caso 1 — Plataforma de E-commerce Pública

**Contexto**  
Plataforma de vendas online, com pagamentos diretos e integração com terceiros.

- **Exposição (E)**: Pública (web + app móvel) → **3**  
- **Tipo de Dados (D)**: Dados pessoais + dados de pagamento → **3**  
- **Impacto (I)**: Financeiro, reputacional e legal → **3**

**Classificação:**  
**E + D + I = 9 → L3 (Risco Elevado)**

**Racional**  
Mesmo sem considerar incidentes passados, a combinação de exposição pública, dados sensíveis e impacto direto no negócio justifica **máximo rigor**.

**Implicações práticas**:
- Requisitos de segurança completos e rastreáveis  
- Threat modeling formal  
- SBOM e SCA contínuo  
- DAST contínuo, fuzzing e validação de regressões  

---

## 📝 Caso 2 — Portal Interno de RH Hospitalar

**Contexto**  
Aplicação interna, acessível apenas na rede hospitalar, usada para gestão de RH.

- **Exposição (E)**: Interna → **1**  
- **Tipo de Dados (D)**: Dados clínicos e financeiros de colaboradores → **3**  
- **Impacto (I)**: Legal (RGPD), confidencialidade sensível → **3**

**Classificação:**  
**E + D + I = 7 → L3 (Risco Elevado)**

**Racional**  
A baixa exposição **não compensa** a natureza dos dados nem o impacto legal.  
Este é um exemplo clássico de erro comum evitado pelo modelo SbD-ToE.

**Nota importante**  
Este caso demonstra que:
> *“interno” não significa “baixo risco”*.

---

## 📝 Caso 3 — Sistema de Faturação B2B

**Contexto**  
Sistema usado por clientes empresariais autenticados, com integração ERP.

- **Exposição (E)**: Acesso externo autenticado → **2**  
- **Tipo de Dados (D)**: Dados financeiros e de clientes → **2**  
- **Impacto (I)**: Operacional e financeiro → **2**

**Classificação:**  
**E + D + I = 6 → L2 (Risco Médio)**

**Racional**  
Sistema relevante, mas com impacto controlável e sem dados regulados críticos.

**Implicações práticas**:
- Requisitos de segurança formais, mas proporcionais  
- Threat modeling simplificado  
- SCA com política de severidade  
- Testes de segurança regulares, não contínuos  

---

## 📝 Caso 4 — Ferramenta Interna de Gestão de Tarefas

**Contexto**  
Aplicação simples, usada internamente para gestão de tarefas.

- **Exposição (E)**: Interna → **1**  
- **Tipo de Dados (D)**: Não sensíveis → **1**  
- **Impacto (I)**: Baixo → **1**

**Classificação:**  
**E + D + I = 3 → L1 (Risco Baixo)**

**Racional**  
Baixa exposição, baixo impacto e ausência de dados sensíveis justificam controlos mínimos.

**Implicações práticas**:
- Linters e revisão básica de código  
- Boas práticas gerais de segurança  
- Sem exigência de testes avançados  

---

## 📝 Caso 5 — Serviço Core com DRP Crítico (Classificação Conservadora)

**Contexto**  
Serviço central de negócio, classificado como **Crítico no DRP**:

- RTO < 1h  
- RPO ≈ 0  
- Interrupção paralisa operações da organização  

**Análise técnica estrita**:
- Exposição controlada  
- Dados moderadamente sensíveis  

**Decisão adotada**:
- **Classificação direta como L3**, por criticidade operacional

**Racional**  
Mesmo que o risco técnico pudesse ser L2, o custo de falha justifica  
**tratamento como aplicação de risco elevado**.

> Este é um exemplo explícito de *over-classification deliberada*,  
> aceite e recomendada no SbD-ToE.

---

## 📝 Caso 6 — Aplicação com Automação Avançada (incl. IA)

**Contexto**  
Aplicação interna que utiliza automação assistiva para:
- gerar código,
- aprovar alterações de configuração,
- executar ações com impacto real.

- **Exposição (E)**: Interna, mas com integrações externas → **2**  
- **Tipo de Dados (D)**: Código, configurações, segredos ocasionais → **2**  
- **Impacto (I)**: Alterações automáticas com efeito real → **3**

**Classificação:**  
**E + D + I = 7 → L3 (Risco Elevado)**

**Racional**  
A classificação **não é elevada por “usar IA”**,  
mas porque existe:
- delegação,
- velocidade,
- e impacto sem validação humana obrigatória.

---

## 📌 Conclusão

Estes exemplos demonstram que:

- a classificação de risco **não é mecânica**;
- o SbD-ToE aceita decisões conservadoras e pragmáticas;
- o objetivo final é sempre:
  > **aplicar o nível certo de cuidado, controlo e validação**.

A coerência do modelo está na **proporcionalidade**,  
não na obsessão pela pontuação perfeita.
