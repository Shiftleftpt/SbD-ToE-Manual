---
id: metricas-indicadores
title: Métricas, Indicadores e KPIs de Deteção e Resposta
sidebar_position: 7
description: Definição e cálculo de indicadores como MTTD e MTTR, e sua aplicação em dashboards operacionais.
tags: [métricas, indicadores, mttd, mttr, dashboards, kpi]
---

# 📈 Métricas, Indicadores e Cobertura {monitorizacao-operacoes:addon:metricas-indicadores}

## 🌟 Objetivo {monitorizacao-operacoes:addon:metricas-indicadores#objetivo}

Definir métricas e indicadores para avaliar a **eficácia, cobertura e maturidade** dos controlos de monitorização, deteção e resposta, permitindo melhoria contínua com base em dados operacionais.

---

## 📏 Indicadores de cobertura {monitorizacao-operacoes:addon:metricas-indicadores#indicadores_de_cobertura}

| Métrica                             | Objetivo                                              |
| ----------------------------------- | ----------------------------------------------------- |
| % de fluxos críticos com logging    | Avaliar visibilidade mínima sobre operações sensíveis |
| % de logs enviados para SIEM        | Medir aderência à centralização                       |
| % de alertas com trigger testado    | Validação da eficácia dos alertas                     |
| % de componentes com tagging ECS    | Avaliar consistência e normalização                   |
| % de pipelines que produzem eventos | Cobertura CI/CD na deteção de eventos suspeitos       |

---

## ⏱️ Indicadores operacionais {monitorizacao-operacoes:addon:metricas-indicadores#indicadores_operacionais}

| Métrica                        | Significado                                      | Exemplo de cálculo                   |
| ------------------------------ | ------------------------------------------------ | ------------------------------------ |
| **MTTD** (Time to Detect)      | Tempo médio desde evento até alerta              | timestamp\_alert - timestamp\_event  |
| **MTTR** (Time to Respond)     | Tempo médio até início da mitigação              | timestamp\_action - timestamp\_alert |
| **Falso positivo rate**        | % de alertas não relevantes                      | alertas inválidos / total alertas    |
| **Eventos por utilizador/dia** | Atividade média normal para perfil base          | baseline comparativo                 |
| **Incidentes por categoria**   | Classificação de casos por tipo (acesso, fraude) | logs ou tickets IR                   |

> 🌟 **MTTD e MTTR** são indicadores-chave de maturidade operacional.

---

## 📊 Dashboards e relatórios sugeridos {monitorizacao-operacoes:addon:metricas-indicadores#dashboards_e_relatorios_sugeridos}

| Tipo de painel           | Dados incluídos                                   |
| ------------------------ | ------------------------------------------------- |
| **Cobertura de logging** | Apps sem logs estruturados, por criticidade       |
| **Qualidade de alertas** | Triggers ativos/testados, % falsos positivos      |
| **Eventos e contexto**   | Eventos por tipo, IP, user, sistema               |
| **Deteção e resposta**   | MTTD, MTTR, por severidade, em histórico temporal |
| **Padrões anómalos**     | Outliers por role, geografia, hora, device        |

---

## 🌄 Integração com maturidade {monitorizacao-operacoes:addon:metricas-indicadores#integracao_com_maturidade}

| Nível de maturidade | Indicadores esperados                                              |
| ------------------- | ------------------------------------------------------------------ |
| **L1 (mínimo)**     | Logging ativo local, análise manual ocasional                      |
| **L2 (moderado)**   | Alertas automáticos com tuning, dashboards de operação básicos     |
| **L3 (avçado)**     | Correlação de fontes, detecção comportamental, KPIs como MTTD/MTTR |

> 📊 Estas métricas contribuem também para os Capítulos 10 (Testes de Segurança) e 11 (Controlo de Execução).

---

## ✅ Recomendações finais {monitorizacao-operacoes:addon:metricas-indicadores#recomendacoes_finais}

* Medir e publicar métricas **pelo menos mensalmente**
* Estabelecer metas de melhoria (ex: -20% MTTD em 3 meses)
* Correlacionar métricas com eventos reais e exercícios simulados
* Priorizar visibilidade e cobertura sobre ativos críticos

> 💡 *Sem medição, não há melhoria.* A visibilidade quantitativa é essencial à maturidade em segurança.
