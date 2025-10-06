---
id: risco-residual
title: Análise de Risco Residual e Decisão de Aceitação
sidebar_position: 6
tags: [tipo:analise, risco-residual, aceitacao, excecao]
---

<!--template: sbdtoe-core -->

# 🛠️ Análise de Risco Residual {classificacao-aplicacoes:addon:risco-residual}

O conceito de **risco residual** é essencial para a tomada de decisão consciente e justificada sobre a segurança de uma aplicação ou sistema. Representa o risco que **permanece após a aplicação de controlos**, e deve ser sempre comparado com os limites de tolerância da organização.

Este ficheiro complementa o modelo de avaliação semiquantitativa apresentado anteriormente, introduzindo a lógica de "antes e depois dos controlos".

## 🔢 Definições e Relações {classificacao-aplicacoes:addon:risco-residual#definicoes_e_relacoes}

* **Risco Bruto (Inerente)**: Valor do risco antes da aplicação de qualquer controlo.
* **Risco Residual**: Valor do risco remanescente após a aplicação efetiva dos controlos.
* **Risco Aceitável**: Limite máximo de risco residual tolerado pela organização.

> Risco Residual = Risco Bruto - Eficácia dos Controlos Aplicados

Na prática, esta subtração é avaliada qualitativamente ou reavaliando os fatores de impacto e probabilidade após os controlos.

---

## 📝 Exemplo Prático {classificacao-aplicacoes:addon:risco-residual#exemplo_pratico}

**Cenário:** API de autenticação exposta

| Fator                  | Valor Inicial | Valor Após Controlos           |
| ---------------------- | ------------- | ------------------------------ |
| Impacto (I)            | 5             | 4 (uso de MFA e rate limiting) |
| Probabilidade (P)      | 4             | 2 (hardening, WAF, alertas)    |
| Risco Bruto = 5x4 = 20 |               | Risco Residual = 4x2 = 8       |

> Neste caso, o risco é reduzido de "Crítico" para "Médio", o que pode ser aceitável para aplicações L1 ou L2.

---

## 🏛️ Papel do Risco Residual na Tomada de Decisão {classificacao-aplicacoes:addon:risco-residual#papel_do_risco_residual_na_tomada_de_decisao}

O risco residual deve ser sempre comparado com os **limiares definidos por nível de aplicação (L1–L3)**:

* **Se inferior ao limiar de aceitação**: Pode ser aceite, com registo formal.
* **Se igual ou superior**: Deve ser mitigado adicionalmente ou sujeito a tratamento (exceção, transferência, etc).

### Tabela exemplo de decisão por nível: {classificacao-aplicacoes:addon:risco-residual#tabela_exemplo_de_decisao_por_nivel}

| Nível da Aplicação         | Risco Residual Aceitável (exemplo) |
| -------------------------- | ---------------------------------- |
| **L1** (baixa criticidade) | até 9                              |
| **L2** (média criticidade) | até 6                              |
| **L3** (alta criticidade)  | até 4                              |

---

## ✅ Benefícios da Análise de Risco Residual {classificacao-aplicacoes:addon:risco-residual#beneficios_da_analise_de_risco_residual}

* Permite validação da **eficácia dos controlos** implementados.
* Apoia decisões de "go/no-go" em deploys.
* Proporciona base documental para justificar aceitação de risco.
* Promove cultura de responsabilização e gestão consciente do risco.

---

## ⚠️ Riscos de Má Utilização {classificacao-aplicacoes:addon:risco-residual#riscos_de_ma_utilizacao}

* Considerar o risco residual como "valor fixo" em vez de dinâmico.
* Não validar se os controlos foram **efetivamente aplicados**.
* Aceitar riscos sem registo formal ou sem envolvimento de decisores.

---

## 🔄 Integração com o Ciclo de Vida e com o GRC {classificacao-aplicacoes:addon:risco-residual#integracao_com_o_ciclo_de_vida_e_com_o_grc}

* O risco residual deve ser **revisto a cada alteração de arquitetura ou funcionalidade relevante**.
* Pode ser integrado em sistemas de GRC com thresholds automáticos.
* Deve ser parte dos artefactos de revisão de segurança antes de releases.

---

## 📌 Recomendação Final {classificacao-aplicacoes:addon:risco-residual#recomendacao_final}

Todas as decisões sobre aceitação de risco residual devem ser:

* Formalmente registadas
* Justificadas com base em evidência técnica e impacto
* Coerentes com os limiares definidos por nível da aplicação
* Sujeitas a reavaliação periódica
