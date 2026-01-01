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

## 🧠 Enquadramento conceptual

No *Security by Design – Theory of Everything (SbD-ToE)*, o risco é tratado como um **conceito único**, caracterizado por múltiplos **atributos internos** (origem, mecanismo, detetabilidade, evidenciabilidade, reprodutibilidade, entre outros).

O modelo **E/D/I** constitui uma **projeção simplificada e operacional** desse risco, focada nos fatores que mais diretamente influenciam:
- a exposição técnica do sistema,
- a natureza dos dados tratados,
- e o impacto potencial de uma falha ou abuso.

Este modelo **não pretende capturar a totalidade do risco**, mas fornecer uma base consistente e suficiente para classificação aplicacional e aplicação proporcional de controlos.

---

## 🧮 Fórmula do Modelo Simplificado

A classificação de risco é feita com base na soma dos três eixos:

**Risco Classificado (R) = E + D + I**

**Onde:**

- **E (Exposição)**: Grau de acessibilidade técnica e operacional da aplicação
- **D (Tipo de Dados)**: Sensibilidade, valor e enquadramento legal dos dados processados
- **I (Impacto Potencial)**: Consequência expectável de uma falha, violação ou decisão incorreta

### Classificação por Pontuação

| Soma Total | Classificação de Risco | Código |
|------------|------------------------|--------|
| 3–4        | **Baixo**              | L1     |
| 5–6        | **Médio**              | L2     |
| 7–9        | **Elevado**            | L3     |

Esta classificação representa o **nível mínimo de rigor** a aplicar em requisitos, controlos, validações e evidência.

---

## 🧱 Detalhe dos Eixos

### 🧭 Exposição (E)

Avalia quão acessível está a aplicação ou sistema, considerando superfícies de ataque, interfaces e contexto de rede.

| Nível | Descrição                                          | Pontos |
|-------|----------------------------------------------------|--------|
| 1     | Apenas acessível internamente (sem acesso externo) | 1      |
| 2     | Acessível externamente, com autenticação           | 2      |
| 3     | Público ou amplamente exposto (acesso aberto ou não autenticado) | 3 |

---

### 📑 Tipo de Dados (D)

Classifica a natureza, sensibilidade e enquadramento legal dos dados processados.

| Nível | Descrição                                                              | Pontos |
|-------|------------------------------------------------------------------------|--------|
| 1     | Dados públicos ou sem sensibilidade                                    | 1      |
| 2     | Dados pessoais, identificáveis ou confidenciais internos               | 2      |
| 3     | Dados regulados ou altamente sensíveis (ex.: saúde, financeiros, localização) | 3 |

---

### ⚠️ Impacto Potencial (I)

Avalia o impacto expectável para a organização caso o risco se materialize.

| Nível | Descrição                                                                  | Pontos |
|-------|----------------------------------------------------------------------------|--------|
| 1     | Impacto nulo ou irrelevante                                                 | 1      |
| 2     | Impacto limitado, localizado ou reversível                                 | 2      |
| 3     | Impacto elevado: financeiro, regulatório, operacional ou reputacional significativo | 3 |

---

## 🧩 Critérios complementares em contextos de automação e apoio à decisão

A utilização de mecanismos de automação ou apoio à decisão (incluindo IA) **não cria novos eixos de risco**, nem implica, por si só, alteração da criticidade da aplicação.

Esses mecanismos devem ser considerados **exclusivamente quando modificam atributos relevantes do risco**, nomeadamente exposição, tipo de dados tratados ou impacto efetivo das decisões e ações realizadas.

### 🧭 Regra de aplicação obrigatória

A reavaliação dos eixos **E**, **D** e **I** é **obrigatória** sempre que a automação ou apoio à decisão:

- introduza nova superfície de exposição ou integração externa;
- envolva tratamento adicional de dados pessoais, regulados, segredos ou informação confidencial;
- aumente delegação, alcance ou velocidade de decisões com impacto real no sistema, nos dados ou no negócio.

Sempre que **qualquer uma destas condições se verifique**, a equipa **deve** ajustar os eixos afetados e **registar explicitamente o racional da decisão**.

A manutenção da classificação original **só é aceitável** quando exista:
- validação humana obrigatória e efetiva;
- controlo explícito dos outputs automatizados;
- evidência suficiente de que os atributos do risco não foram alterados.

### 🔎 Orientação prática mínima

| Situação observada                                                                 | Ajuste esperado |
|-----------------------------------------------------------------------------------|-----------------|
| Integração com serviços externos de automação ou IA                                | Avaliar E       |
| Envio de dados pessoais, regulados ou IP em prompts, contexto ou artefactos        | D ≥ 2           |
| Execução automática de código, infraestrutura ou decisões sem revisão humana       | I = 3           |
| Resultados não determinísticos aceites como evidência final                        | I = 3           |

> 📌 Esta orientação é prescritiva quanto à necessidade de avaliação, não quanto ao resultado final, que deve ser sempre contextual e documentado.

---

## 🔎 Porquê somar os eixos?

A opção pela **soma simples** dos eixos privilegia:

- simplicidade operacional;
- facilidade de adoção por equipas técnicas;
- consistência entre projetos;
- clareza e transparência em auditorias.

Modelos mais complexos foram considerados, mas tendem a introduzir variabilidade excessiva e dificultar a padronização organizacional.

Este modelo é empírico e prescritivo, adequado a contextos ágeis e DevSecOps, mantendo proporcionalidade e rastreabilidade.

---

## ⚠️ Considerações finais

- Este modelo **não substitui** threat modeling nem análises de risco formais;
- Deve ser usado como **mecanismo rápido de classificação** e ponto de partida para decisões;
- Deve ser revisto sempre que ocorram alterações relevantes a funcionalidades, dados, exposição ou pressupostos de processo.

Apesar da sua simplicidade, o modelo permite determinar, de forma rápida e fundamentada, **o nível de rigor de segurança a aplicar**, assegurando coerência ao longo do ciclo de vida.

---

## 🔗 Ligações úteis

- Modelo alternativo: [Adoção de classificações existentes (DRP/BIA)](/sbd-toe/sbd-manual/classificacao-aplicacoes/addon/adopcao-drp-bia)
- [Capítulo 01 – Classificação da Criticidade Aplicacional](/sbd-toe/sbd-manual/classificacao-aplicacoes/intro)
