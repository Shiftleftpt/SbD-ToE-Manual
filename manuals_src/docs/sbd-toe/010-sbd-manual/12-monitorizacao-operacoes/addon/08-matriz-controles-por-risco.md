---
id: matriz-controles-por-risco
title: Matriz de Controles por Nível de Risco
sidebar_position: 8
description: Aplicação proporcional dos controlos de monitorização e resposta conforme a classificação de risco da aplicação.
tags: [L1, L2, L3, controles, matriz, proporcionalidade, risco]
---

# 📈 Matriz de Controlos por Nível de Risco - Monitorização e Operações

Esta matriz define os **requisitos mínimos obrigatórios de monitorização** para aplicações, consoante o seu nível de risco (L1 a L3). Serve como base para avaliação de conformidade e planeamento de controlos ao longo do ciclo de vida.

> ⚠️ Esta matriz aplica-se a **aplicações classificadas segundo o modelo de risco do Capítulo 1**.

---

## 📊 Matriz de cobertura

| Controlo / Requisito                           |  L1 |  L2 |  L3 |
| ---------------------------------------------- | :-: | :-: | :-: |
| Logging estruturado e persistente              |  ✔️ |  ✔️ |  ✔️ |
| Eventos críticos definidos (login, erro, etc.) |  ✔️ |  ✔️ |  ✔️ |
| Retenção mínima (>= 30 dias)                   |     |  ✔️ |  ✔️ |
| Logs enviados para sistema centralizado (SIEM) |     |  ✔️ |  ✔️ |
| Alertas automáticos configurados               |     |  ✔️ |  ✔️ |
| Simulações de trigger testadas                 |     |  ✔️ |  ✔️ |
| Correlação entre fontes                        |     |     |  ✔️ |
| Deteção comportamental / perfis adaptativos    |     |     |  ✔️ |
| Integração com resposta a incidentes (IRP)     |     |  ✔️ |  ✔️ |
| Métricas de MTTD / MTTR monitorizadas          |     |     |  ✔️ |

---

## ✅ Interpretação

* ✔️ = obrigatório para esse nível
* **L1**: logging local e básico para rastreabilidade
* **L2**: centralização de eventos e alertas operacionais fundamentais
* **L3**: deteção contextual, correlação, resposta integrada

> 🥉 Esta matriz deve ser cruzada com o catálogo de requisitos (Cap. 2) e os critérios de maturidade (`addon/achievable-maturity`).

---

## 📌 Recomendações adicionais

* Aplicações com exposição externa e dados sensíveis devem, mesmo sendo L1, cumprir requisitos de L2 ou L3;
* Utilizar esta matriz como **base de revisão em arquitetura, design e readiness para produção**;
* Incluir estes requisitos em definição de "Done" e critérios de aceitação de releases.

> 🔒 A matriz funciona como referencial de controlo mínimo e não como teto de ambição. Projetos maduros devem ir mais longe.
