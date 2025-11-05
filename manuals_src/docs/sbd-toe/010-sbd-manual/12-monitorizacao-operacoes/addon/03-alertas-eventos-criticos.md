---
id: alertas-eventos-criticos
title: Geração e Gestão de Alertas para Eventos Críticos
sidebar_position: 3
description: Regras, thresholds e melhores práticas para alertas eficazes baseados em eventos sensíveis.
tags: [alertas, eventos críticos, deteção, thresholds, severidade]
---

# 🚨 Alertas baseados em Eventos Críticos

## 🌟 Objetivo

Prescrever práticas para a definição, ativação e validação de **alertas automáticos baseados em eventos críticos**, com foco em deteção atempada, redução de falsos positivos e integração eficaz com as equipas de resposta.

---

## 🧬 O que são alertas críticos

Alertas críticos são **notificações geradas automaticamente** com base em padrões de eventos que indicam anomalias, falhas de segurança ou comportamentos indesejados — exigindo validação humana ou resposta imediata.

> 🌟 Um bom alerta é oportuno, acionável, e baseado em eventos rastreáveis e estruturados.

---

## 📌 Tipos de eventos que devem gerar alertas

| Tipo de evento              | Exemplos práticos                                 | Severidade sugerida |
| --------------------------- | ------------------------------------------------- | ------------------- |
| **Autenticação falhada**    | Várias falhas consecutivas de um IP ou utilizador | Alta / Média        |
| **Elevação de privilégios** | Mudança de perfil sem processo formal             | Alta                |
| **Alterações críticas**     | Configuração de permissões, API keys              | Alta / Média        |
| **Falhas repetidas**        | Erros 5xx contínuos numa API ou microserviço      | Média               |
| **Inatividade incomum**     | Queda de logs de um módulo ativo                  | Média / Baixa       |
| **Chamadas anómalas**       | Acesso fora do horário, geolocalização incomum    | Alta / Média        |

> ⚠️ O conjunto de alertas deve ser proporcional à **criticidade da aplicação** e à **sensibilidade dos dados tratados**.

---

## 🛠️ Como definir um alerta eficaz

Cada regra de alerta deve conter:

* **Condição**: ex. 5 falhas de login num intervalo de 3 minutos;
* **Fonte de dados**: ficheiro de log ou índice no SIEM (ex: `auth.log`);
* **Severidade**: Alta, Média, Baixa — de acordo com o impacto e urgência;
* **Canal de notificação**: e-mail, Slack, webhook, PagerDuty, etc.;
* **Runbook (opcional)**: link para resposta padronizada.

### Exemplo (YAML genérico):

```yaml
alert_name: login_failures_high
condition: count(auth.event == "login_failed") by ip > 5 in 3m
severity: high
notify: slack_channel_security
runbook: https://wiki.exemplo.org/runbooks/login-failures
```

---

## 🧪 Validação de alertas

| Técnica                    | Descrição                                        |
| -------------------------- | ------------------------------------------------ |
| **Simulação ativa**        | Forçar evento em ambiente de staging             |
| **Unit test de regra**     | Testes automáticos à lógica de condição          |
| **Replay com dados reais** | Aplicar regra retroativamente a dados históricos |
| **Playbooks de triagem**   | Associar alerta ações operacionais               |

> ✅ Apenas alertas validados devem ser considerados ativos em produção.

---

## 📊 Tuning e gestão de falsos positivos

Alertas mal calibrados causam ruído e descredibilizam o sistema. Práticas recomendadas:

* Definir limiares com base em dados reais e contexto
* Usar mecanismos de silenciamento (ex: snooze, threshold decay)
* Documentar falsos positivos e causas
* Rever condições periodicamente

> 💡 Estatísticas por alerta ajudam a priorizar (ex: sinal/ruído).

---

## 🧹 Integração com outros controlos

| Documento                          | Ligação com este tópico                          |
| ---------------------------------- | ------------------------------------------------ |
| `02-logging-centralizado.md`       | Define eventos de origem para geração de alertas |
| `06-correlacao-anomalias.md`       | Correlação de múltiplos eventos e domínios       |
| `05-monitorizacao-operacoes.md`     | Utiliza alertas como gatilho de resposta         |
| `08-matriz-controles-por-risco.md` | Aponta requisitos de alerta por criticidade      |

---

## ✅ Recomendações finais

* Iniciar com 5 a 10 alertas de alto valor (impacto + frequência)
* Priorizar alertas ligados a fluxos críticos ou dados sensíveis
* Documentar todas as regras, parâmetros e validações
* Integrar alertas em pipelines de observabilidade e resposta

> 🔒 A capacidade de alerta eficaz é um dos pilares da maturidade operacional em segurança. Deve evoluir com base em feedback, deteção real e resposta a incidentes.
