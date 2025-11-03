---
id: 05-monitorizacao-e-reacao
title: Monitorização Pós-Deploy e Ações de Reação
description: Práticas de observabilidade, métricas de runtime e mecanismos automáticos de rollback após o deploy.
tags: [tipo:anexo, grupo:execucao, tema:monitorizacao, rollback, observabilidade]
---

# 📊 Monitorização e Reação a Incidentes de Runtime

A fase de execução de uma aplicação em produção exige **observabilidade adequada e capacidade de reação rápida** a falhas ou anomalias. Este documento define os mecanismos essenciais para detetar, analisar e responder a problemas de segurança ou estabilidade em runtime.

---

## 🔍 Domínios de observabilidade

| Domínio               | Descrição                                                             | Exemplos de ferramenta       |
|------------------------|----------------------------------------------------------------------|------------------------------|
| **Logging estruturado**| Registos de eventos com contexto (user, request, IP, erro)            | ELK, Loki, Datadog Logs      |
| **Métricas de execução** | Indicadores de desempenho e estabilidade                              | Prometheus, New Relic, App Insights |
| **Alertas de segurança** | Triggers automáticos por padrões anómalos ou violações de regras     | SIEM, Sentry, Azure Defender  |
| **Tracing distribuído**| Rastreio de chamadas entre serviços, com tempos e erros               | Jaeger, OpenTelemetry        |

---

## 🚨 Exemplos de eventos que devem gerar alertas

- Aumento anormal de erros 5xx
- Timeout em chamadas para dependências críticas
- Ativação de kill switch
- Acesso a funcionalidades desativadas por toggle
- Logs com mensagens de exceção não tratadas
- Detetação de padrões anómalos (ex: spikes de login)

---

## 🚒 Reação a incidentes

| Tipo de resposta          | Exemplo                                                          |
|---------------------------|------------------------------------------------------------------|
| **Rollback automático**   | Reverter deploy se nível de erro ou métricas ultrapassarem limiar |
| **Ativação de toggles**   | Kill switch ativa funcionalidade de contenção                 |
| **Escalonamento humano**  | Alerta em canal de incidentes (ex: Slack, PagerDuty)             |
| **Análise posterior**      | Gerar timeline e registos para post-mortem                      |

> 🔊 A reação não deve ser exclusivamente humana: deve ser suportada por automação e playbooks claros.

---

## 📊 Métricas de rastreabilidade pós-deploy

- Latência média por funcionalidade
- Erros por endpoint / método
- Nº de toggles ativados em runtime
- Incidentes com resolução por rollback
- Utilizadores impactados por falha

Estas métricas devem ser ligadas a:
- Versão da release
- Owner funcional e técnico
- Eventos de ativação/desativação de controlos de execução

---

## 💼 Requisitos para auditoria e rastreabilidade

- Logs devem conter:
  - ID da release
  - Identificador de funcionalidade
  - Timestamp + contexto
- Alteracões de configuração devem ser:
  - Versionadas
  - Auditadas por perfil autorizado
  - Ligadas a um motivo/documentação

---

## ✅ Checklist de monitorização

- [ ] Estão definidos alertas para eventos de segurança?
- [ ] Todos os toggles críticos geram eventos no sistema de logs?
- [ ] Estão configuradas métricas por funcionalidade?
- [ ] Existe dashboard ou painel de execução em runtime?
- [ ] Estão definidos limites que disparam rollback automático?
- [ ] Existe playbook de reação por tipo de incidente?

> 🗓️ Estas práticas devem ser validadas em cada release e mantidas durante o ciclo de vida da versão ativa.
