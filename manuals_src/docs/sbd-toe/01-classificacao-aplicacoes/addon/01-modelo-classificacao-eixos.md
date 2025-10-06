---
id: modelo-classificacao-eixos
title: Modelo de Classificação
sidebar_position: 1
tags: [tipo:modelo, tema:criticidade, eixo, risco]
---
<!--template: sbdtoe-core -->

# 📎 Modelo de Classificação por Eixos de Risco {classificacao-aplicacoes:addon:modelo-classificacao-eixos}

## 🎯 Objetivo {classificacao-aplicacoes:addon:modelo-classificacao-eixos#objetivo}

Fornecer um modelo **prático, proporcional e aplicável** ao contexto do desenvolvimento de software, para avaliar o **nível de risco de uma aplicação** com base em três eixos fundamentais:

- **Exposição (E)**
- **Tipo de Dados (D)**
- **Impacto Potencial (I)**

Este modelo permite decisões rápidas e documentadas sobre os controlos mínimos de segurança a aplicar, com rastreabilidade ao longo do ciclo de vida.

---

## 🧮 Fórmula do Modelo Simplificado {classificacao-aplicacoes:addon:modelo-classificacao-eixos#formula_do_modelo_simplificado}

A classificação de risco é feita com base na soma dos três eixos:

**Risco Total (R) = E + D + I**

**Onde:**

- **E (Exposição)**: Grau de acessibilidade da aplicação ou sistema
- **D (Tipo de Dados)**: Sensibilidade e regulamentação dos dados processados
- **I (Impacto Potencial)**: Consequência esperada de uma violação ou falha

### Classificação por Pontuação {classificacao-aplicacoes:addon:modelo-classificacao-eixos#classificacao_por_pontuacao}

| Soma Total | Classificação de Risco | Código |
|------------|------------------------|--------|
| 3–4        | **Baixo**              | L1     |
| 5–6        | **Médio**              | L2     |
| 7–9        | **Elevado**            | L3     |

---

## 🧱 Detalhe dos Eixos {classificacao-aplicacoes:addon:modelo-classificacao-eixos#detalhe_dos_eixos}

### 🧭 Exposição (E) {classificacao-aplicacoes:addon:modelo-classificacao-eixos#exposicao_e}

Avalia quão acessível está a aplicação ou sistema, com base no seu contexto de rede e interface.

| Nível | Descrição                                          | Pontos |
|-------|----------------------------------------------------|--------|
| 1     | Apenas acessível internamente (sem acesso externo) | 1      |
| 2     | Acessível externamente, mas com autenticação       | 2      |
| 3     | Público (acesso aberto ou não autenticado)         | 3      |

---

### 📑 Tipo de Dados (D) {classificacao-aplicacoes:addon:modelo-classificacao-eixos#tipo_de_dados_d}

Classifica a natureza e criticidade da informação processada.

| Nível | Descrição                                                              | Pontos |
|-------|------------------------------------------------------------------------|--------|
| 1     | Dados públicos, sem sensibilidade ou impacto legal                     | 1      |
| 2     | Dados pessoais, identificáveis, ou confidenciais internos              | 2      |
| 3     | Dados regulados ou altamente sensíveis (bancários, saúde, localização) | 3      |

---

### ⚠️ Impacto Potencial (I) {classificacao-aplicacoes:addon:modelo-classificacao-eixos#impacto_potencial_i}

Avalia o impacto que uma violação teria para a organização.

| Nível | Descrição                                                             | Pontos |
|-------|----------------------------------------------------------------------|--------|
| 1     | Impacto nulo ou irrelevante                                          | 1      |
| 2     | Impacto limitado, reversível ou com pouco alcance                    | 2      |
| 3     | Impacto elevado: reputacional, regulatório ou financeiro significativo | 3      |

---

## 🔎 Porquê somar os eixos? {classificacao-aplicacoes:addon:modelo-classificacao-eixos#porque_somar_os_eixos}

Ao optar pela **soma simples dos eixos**, este modelo privilegia a **facilidade de uso e interpretação**, permitindo que equipas técnicas apliquem a lógica sem cálculos complexos.

Alternativas como multiplicação ponderada (ex: \( R = E × I \)) foram consideradas, mas:

- **Aumentam a variância desnecessariamente**
- Dificultam a padronização entre equipas
- Tornam o racional menos explícito em auditorias

Este modelo é empírico e prescritivo, alinhado com a realidade de projetos ágeis e contextos de DevSecOps, mantendo proporcionalidade e rastreabilidade.

---

## ⚠️ Considerações finais {classificacao-aplicacoes:addon:modelo-classificacao-eixos#consideracoes_finais}

- Este modelo **não substitui análises de threat modeling ou risco regulatório formal**
- Deve ser usado como **componente rápida de classificação** e input para priorização, na ausência de práticas mais formais em uso
- Deve ser revisto a cada alteração relevante: funcionalidades, dados, exposição ou contexto

---

## 🔗 Ligações úteis {classificacao-aplicacoes:addon:modelo-classificacao-eixos#ligacoes_uteis}

- [Ver adoção de classificações existentes (DRP/BIA)](xref:sbd-toe:toe:01-classificacao-aplicacoes:adopcao-drp-bia) <!-- Precisa revisão manual -->
- [Ver Capítulo 1 — Gestão de Risco](xref:sbd-toe:toe:intro:intro)
