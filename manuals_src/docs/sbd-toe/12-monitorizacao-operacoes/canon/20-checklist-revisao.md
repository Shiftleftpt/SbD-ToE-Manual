---
id: checklist-revisao
title: Checklist – Monitorização e Operações
sidebar_label: Checklist de Revisão
sidebar_position: 20
description: Checklist de controlo binário da adoção das práticas de monitorização, alerta e resposta a incidentes.
tags: [checklist, controlo, validacao, monitorizacao, deteccao, resposta]
---


# ✅ Checklist de Revisão — Capítulo 12: Monitorização e Operações {monitorizacao-operacoes:canon:checklist-revisao}

Este checklist aplica-se a todas as aplicações que requeiram capacidade de **logging estruturado, alertas automáticos, correlação de eventos e resposta a incidentes**.  
Serve como instrumento de verificação binária e auditável da **adoção prática das prescrições do Capítulo 12**, permitindo:

- Controlo contínuo da aplicação proporcional das práticas de monitorização;
- Verificação sistemática por projeto ou aplicação;
- Geração de indicadores operacionais e de maturidade organizacional.

> 🗓️ **Recomenda-se a sua execução por release, por alteração de domínios monitorizados ou após incidentes relevantes.**

---

## 📋 Itens de Verificação {monitorizacao-operacoes:canon:checklist-revisao#itens_de_verificacao}

| Item de controlo                                                                 | Verificado? |
|----------------------------------------------------------------------------------|-------------|
| Foram definidos os eventos críticos a monitorizar                               | ☑           |
| Existe logging estruturado com formato consistente (ex: JSON, ECS)              | ☑           |
| Os eventos críticos são emitidos e contêm os campos mínimos (timestamp, user)   | ☑           |
| Os logs são transmitidos por forwarder seguro para sistema centralizado (SIEM)  | ☑           |
| A configuração de envio garante segurança (TLS, autenticação, buffer local)     | ☑           |
| Existem regras de alerta automáticas para eventos críticos                      | ☑           |
| As regras de alerta foram testadas com eventos simulados                        | ☑           |
| Os alertas são correlacionados entre múltiplas fontes (app, infra, CI/CD)       | ☑           |
| Existe integração com sistema de resposta (IRP, SOAR, tickets automáticos)      | ☑           |
| Estão definidas e monitorizadas métricas de MTTD e MTTR                         | ☑           |
| Existem dashboards operacionais atualizados e acessíveis                        | ☑           |
| A cobertura de logging é validada periodicamente (amostragem ou rastreio)       | ☑           |
| As exceções à monitorização são justificadas, aprovadas e documentadas          | ☑           |
| As práticas estão ajustadas ao nível de risco da aplicação (L1–L3)              | ☑           |
| As práticas estão integradas no ciclo de vida (pipeline, PR, release)           | ☑           |

---

## 🔄 Integração Operacional {monitorizacao-operacoes:canon:checklist-revisao#integracao_operacional}

- Este checklist pode ser usado em **auditorias técnicas, gates de release ou revisões de segurança**;
- Cada resposta afirmativa deve ser suportada por **evidência objetiva**: regras, dashboards, tickets, configs, capturas de teste;
- A proporcionalidade deve seguir a [matriz de controlo por risco](xref:sbd-toe:toe:12-monitorizacao-operacoes:matriz-controles-por-risco).

> ⚠️ **Respostas negativas exigem exceção formal aprovada e justificada.**

---

## 📊 Conformidade e Governação {monitorizacao-operacoes:canon:checklist-revisao#conformidade_e_governacao}

- Este instrumento valida a **conformidade com o Capítulo 12 — Monitorização e Operações**;
- Pode ser integrado em **ciclos de revisão regulares ou como KPI organizacional**;
- A evolução das métricas (ex: % com alertas testados, cobertura de logs, MTTD médio) reflete a **maturidade da equipa**.

> 📅 Este checklist é parte integrante do modelo canónico de controlo SbD-ToE, e suporta a governaça por evidência.
