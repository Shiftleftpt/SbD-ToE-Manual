---
id: modelo-classificacao-eixos
title: Modelo de Classificação
sidebar_position: 1
tags: [tipo:modelo, tema:criticidade, eixo, risco]
---
<!--template: sbdtoe-core -->

# 📎 Modelo de Classificação por Eixos de Risco

## 🎯 Objetivo

Fornecer um modelo **prático, proporcional e aplicável** ao contexto do desenvolvimento de software, para avaliar o **nível de risco de uma aplicação** com base em três eixos fundamentais:

- **Exposição (E)**
- **Tipo de Dados (D)**
- **Impacto Potencial (I)**

Este modelo permite decisões rápidas e documentadas sobre os controlos mínimos de segurança a aplicar, com rastreabilidade ao longo do ciclo de vida.

---

## 🧮 Fórmula do Modelo Simplificado

A classificação de risco é feita com base na soma dos três eixos:

**Risco Total (R) = E + D + I**

**Onde:**

- **E (Exposição)**: Grau de acessibilidade da aplicação ou sistema
- **D (Tipo de Dados)**: Sensibilidade e regulamentação dos dados processados
- **I (Impacto Potencial)**: Consequência esperada de uma violação ou falha

### Classificação por Pontuação

| Soma Total | Classificação de Risco | Código |
|------------|------------------------|--------|
| 3–4        | **Baixo**              | L1     |
| 5–6        | **Médio**              | L2     |
| 7–9        | **Elevado**            | L3     |

---

## 🧱 Detalhe dos Eixos

### 🧭 Exposição (E)

Avalia quão acessível está a aplicação ou sistema, com base no seu contexto de rede e interface.

| Nível | Descrição                                          | Pontos |
|-------|----------------------------------------------------|--------|
| 1     | Apenas acessível internamente (sem acesso externo) | 1      |
| 2     | Acessível externamente, mas com autenticação       | 2      |
| 3     | Público (acesso aberto ou não autenticado)         | 3      |

---

### 📑 Tipo de Dados (D)

Classifica a natureza e criticidade da informação processada.

| Nível | Descrição                                                              | Pontos |
|-------|------------------------------------------------------------------------|--------|
| 1     | Dados públicos, sem sensibilidade ou impacto legal                     | 1      |
| 2     | Dados pessoais, identificáveis, ou confidenciais internos              | 2      |
| 3     | Dados regulados ou altamente sensíveis (bancários, saúde, localização) | 3      |

---

### ⚠️ Impacto Potencial (I)

Avalia o impacto que uma violação teria para a organização.

| Nível | Descrição                                                             | Pontos |
|-------|----------------------------------------------------------------------|--------|
| 1     | Impacto nulo ou irrelevante                                          | 1      |
| 2     | Impacto limitado, reversível ou com pouco alcance                    | 2      |
| 3     | Impacto elevado: reputacional, regulatório ou financeiro significativo | 3      |

---

## 🔎 Porquê somar os eixos?

Ao optar pela **soma simples dos eixos**, este modelo privilegia a **facilidade de uso e interpretação**, permitindo que equipas técnicas apliquem a lógica sem cálculos complexos.

Alternativas como multiplicação ponderada (ex: \( R = E × I \)) foram consideradas, mas:

- **Aumentam a variância desnecessariamente**
- Dificultam a padronização entre equipas
- Tornam o racional menos explícito em auditorias

Este modelo é empírico e prescritivo, alinhado com a realidade de projetos ágeis e contextos de DevSecOps, mantendo proporcionalidade e rastreabilidade.

---

## ⚠️ Considerações finais

- Este modelo **não substitui análises de threat modeling ou risco regulatório formal**
- Deve ser usado como **componente rápida de classificação** e input para priorização, na ausência de práticas mais formais em uso
- Deve ser revisto a cada alteração relevante: funcionalidades, dados, exposição ou contexto

Não obstante permite de forma extremamente rápida, e assente no conhecimento intriseco dos elementos participantes da equipa, numa determinação impirica do grau de segurança a aplicar à aplicação.
---

## 🔗 Ligações úteis

- Modelo alternativo: [Ver adoção de classificações existentes (DRP/BIA)](/sbd-toe/sbd-manual/classificacao-aplicacoes/addon/adopcao-drp-bia) <!-- Precisa revisão manual -->
- [Ver Capítulo 1 — Gestão de Risco](/sbd-toe/sbd-manual/classificacao-aplicacoes/intro)
