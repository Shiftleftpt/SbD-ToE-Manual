---
id: risco-residual
title: Análise de Risco Residual e Decisão de Aceitação
sidebar_position: 4
tags: [tipo:analise, risco-residual, aceitacao, excecao]
---

<!--template: sbdtoe-core -->

# 🛠️ Análise de Risco Residual

O **risco residual** representa o risco que **permanece após a aplicação efetiva dos controlos definidos**, e constitui a base factual para qualquer decisão consciente de aceitação, mitigação adicional ou rejeição.

No *Security by Design – Theory of Everything (SbD-ToE)*, o risco residual **não é um valor abstrato**, mas o resultado de uma avaliação contextual que considera:
- o nível de criticidade da aplicação (L1–L3),
- os **atributos do risco**,
- a **eficácia real dos controlos**,
- e a **evidência disponível**.

Este ficheiro complementa o modelo de classificação e aceitação de risco, introduzindo a lógica de **“antes e depois dos controlos”**, de forma operacional e auditável.

---

## 🔢 Definições fundamentais

- **Risco Bruto (inerente)**  
  Risco identificado **antes da aplicação de controlos**, resultante da combinação de exposição, dados e impacto.

- **Risco Residual**  
  Risco remanescente **após a aplicação efetiva dos controlos**, considerando:
  - redução real de impacto,
  - aumento de detetabilidade,
  - melhoria de evidenciabilidade,
  - e limitação de alcance ou superfície.

- **Risco Aceitável**  
  Limite máximo de risco residual tolerado pela organização, dependente do nível da aplicação (L1–L3).

> 📌 No SbD-ToE, o risco residual **não resulta de uma subtração matemática simples**, mas de uma **reavaliação consciente dos atributos do risco após controlo**.

---

## 🧠 Relação com o modelo E/D/I

A análise de risco residual deve ser sempre coerente com a classificação **E/D/I** da aplicação:

- os controlos **não alteram retroativamente a exposição ou os dados tratados**;
- os controlos podem:
  - reduzir impacto,
  - limitar probabilidade de exploração,
  - aumentar deteção,
  - e melhorar evidência.

Sempre que a aplicação de controlos **não altere materialmente os atributos relevantes do risco**, o risco residual **permanece elevado**, mesmo que existam controlos “teóricos”.

---

## 🧩 Avaliação prática do risco residual

A avaliação do risco residual deve responder explicitamente às seguintes perguntas:

- Os controlos estão **implementados e ativos**?
- A sua eficácia é **verificável e evidenciável**?
- Existe **validação humana efetiva**, quando aplicável?
- O comportamento residual é **determinístico e reproduzível**?
- O impacto residual é **compatível com o nível da aplicação**?

A ausência de resposta positiva a qualquer uma destas questões **impede a aceitação válida do risco**.

---

## 📝 Exemplo ilustrativo (não normativo)

**Cenário:** API exposta com autenticação forte

| Dimensão avaliada            | Antes dos controlos | Após controlos efetivos                  |
|-----------------------------|---------------------|------------------------------------------|
| Exposição (E)               | 3                   | 3 (permanece exposta)                    |
| Tipo de Dados (D)           | 2                   | 2                                        |
| Impacto (I)                 | 3                   | 2 (limitação de abuso, rate limiting)    |
| Detetabilidade              | Baixa               | Alta (alertas, logging)                  |
| Evidenciabilidade           | Limitada            | Elevada (logs, métricas)                 |

👉 O risco residual é **reduzido**, mas **não eliminado**.  
A sua aceitação depende do nível da aplicação e da evidência disponível.

---

## ⚖️ Papel do risco residual na decisão

O risco residual deve ser comparado com os **limiares de aceitação definidos por nível de aplicação**:

| Nível da Aplicação         | Risco Residual Máximo Aceitável |
|---------------------------|----------------------------------|
| **L1** (baixa criticidade) | até 9                            |
| **L2** (média criticidade) | até 6                            |
| **L3** (alta criticidade)  | até 4                            |

> 📌 Estes valores **assumem evidência adequada e controlo efetivo**.  
> Sem evidência suficiente, o risco residual **não pode ser considerado baixo**, independentemente do valor estimado.

---

## ❌ Situações em que o risco residual **não é aceitável**

Não é aceitável considerar risco residual como tolerável quando:

- os controlos não estão comprovadamente ativos;
- a decisão depende exclusivamente de confiança implícita em automação ou tooling;
- os resultados não são reprodutíveis ou verificáveis;
- existe impacto legal, regulatório ou reputacional significativo;
- a aplicação é **L3** e o risco residual depende de validação não determinística.

---

## 🔄 Integração com o ciclo de vida e com GRC

- O risco residual deve ser **reavaliado sempre que ocorra alteração relevante**:
  - arquitetura,
  - dados,
  - exposição,
  - automação ou processo.
- Deve integrar:
  - gates de release,
  - artefactos de revisão de segurança,
  - e sistemas de GRC com thresholds explícitos.
- O risco residual **não é permanente**: tem prazo, contexto e responsáveis.

---

## 📌 Recomendação final

Toda a decisão de aceitação de risco residual deve ser:

- **formalmente registada**;
- **justificada com evidência técnica**;
- **compatível com o nível da aplicação**;
- **limitada no tempo e sujeita a reavaliação**.

> O risco residual não é um “resto inevitável”,  
> é uma **decisão consciente sobre o que a organização está disposta a assumir, aqui e agora**.
