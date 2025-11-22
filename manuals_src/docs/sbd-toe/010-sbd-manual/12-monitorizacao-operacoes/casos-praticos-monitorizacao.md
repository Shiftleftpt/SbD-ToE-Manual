---
id: casos-praticos-monitorizacao
title: Casos Práticos de Monitorização e Deteção
description: Exemplos aplicados de logging, alertas e correlação em contextos reais
tags: [alertas, caso de estudo, correlação, deteção, exemplos, logging, sbd-toe, telemetria]
---

# 📊 Casos Práticos de Monitorização e Deteção

Este anexo apresenta **exemplos práticos** de aplicação das recomendações de monitorização, logging, alertas e correlação. Os cenários aqui descritos ajudam a compreender como aplicar as prescrições deste capítulo a casos concretos.

---

## 🚀 Caso 1 - API Gateway com logging estruturado e alertas

> 🛡️ **Classificação de risco: L3 - Aplicação com exposição pública e operações críticas**

**Contexto:** Aplicativo exposto com API Gateway, autenticação via token, com endpoints críticos (checkout, transferências).

**Controlos aplicados:**

- Logging JSON com ECS via NGINX customizado
- Campos incluídos: `user.id`, `request.path`, `status`, `latency`, `geo.country`
- Alertas:
  - 5xx consecutivos por IP num intervalo de 5 minutos
  - Acesso a `/checkout` fora do horário 06:00–22:00
- Logs enviados para Elastic Stack via Filebeat
- Dashboards com métricas de endpoint, erros, geo, por perfil

**Resultado:** Redução de MTTD para anomalias de login e abuso por script automatizado.

---

## 💰 Caso 2 - Monitorização de uploads em aplicação de gestão documental

> 🛡️ **Classificação de risco: L3 - Aplicação com dados sensíveis e risco de exfiltração**

**Contexto:** Plataforma interna de gestão de documentos sensíveis com workflow de revisão.

**Controlos aplicados:**

- Logging de eventos de `upload`, `download`, `delete`, com user ID e checksum
- Tabela de eventos replicada para SIEM (QRadar) via syslog estruturado
- Correlação ativa: upload de >100MB + IP não habitual + user role "editor"
- Gera alerta de "potencial exfiltração interna"
- Playbook dispara investigação com tagging de logs e isolamento temporário

**Resultado:** Deteção de movimentação não autorizada em contexto de turnover de equipa.

---

## 👨‍💼 Caso 3 - Monitorização de pipelines CI/CD e deteção de execução invulgar

> 🛡️ **Classificação de risco: L2 - Pipeline interno com impacto em cadeia de fornecimento**

**Contexto:** Pipelines com execução automática via GitHub Actions + Kubernetes. Equipa quer rastrear alterações de comportamento.

**Controlos aplicados:**

- Logging estruturado de jobs, com evento `pipeline.start`, `pipeline.command`, `pipeline.result`
- Logs enviados para Loki + Grafana Tempo com `trace.id`
- Alertas:
  - Execução de comandos shell fora dos habituais (`curl`, `rm`, `base64`)
  - Job que dura >2x tempo médio histórico
  - Pipeline executado por branch "legacy/" + user não habitual
- Correlação com imagem usada no job (ex: `ubuntu:latest` fora do baseline)

**Resultado:** Um incidente de build corrompido foi detetado e bloqueado antes de chegar à release.

---

## 🔎 Caso 4 - Correlação de logs de autenticação com movimentos de sessão

> 🛡️ **Classificação de risco: L3 - Aplicação multiuser com perfis sensíveis e risco de hijack**

**Contexto:** Aplicativo com users internos e externos, com sessões longas. Foi reportado uso indevido.

**Controlos aplicados:**

- Sessão identificada por `session.id` + `trace.id`
- Logs de login, refresh de token, logout e chamadas de API agregados por sessão
- Correlação:
  - Login via token antigo com origem IP/UA diferente
  - Refresh de token disparado sem uso normal da sessão
- Triggera alerta por "sessão fantasma / hijacked"
- Validação cruzada com logs do load balancer e WAF

**Resultado:** Bloqueio de sessão e revogação em tempo real. Reforço de timeout e alerta antecipado.

---

## 🧪 Caso 5 - Aplicação interna de baixa criticidade com logging local e validação manual

> 🛡️ **Classificação de risco: L1 - Aplicação de suporte técnico, uso limitado**

**Contexto:** Aplicação interna utilizada apenas por equipa de suporte técnico, sem acesso externo nem dados sensíveis.

**Controlos aplicados:**

- Logging local em ficheiro rotativo com formato estruturado (JSON)
- Eventos registados: `login`, `erro`, `config.change`
- Retenção de 15 dias em disco local com backups semanais
- Validação manual do funcionamento do logging nas revisões de release
- Sem SIEM, sem correlação automática nem alertas em tempo real

**Resultado:** Cumprimento dos requisitos mínimos do nível L1, com visibilidade básica e rastreabilidade suficiente para auditorias internas.

> ✅ Exemplo de aplicação **proporcional ao risco**, sem sobreengenharia.

---

## 📊 Tabela Resumo dos Casos

| Caso | Risco | Contexto Principal                      | Controlos-chave aplicados                           |
|------|-------|------------------------------------------|-----------------------------------------------------|
| 1    | L3    | API Gateway com endpoints críticos       | ECS logging, alertas fora de horário, Elastic Stack |
| 2    | L3    | Gestão documental com risco de fuga      | Syslog, correlação, isolamento, SOAR                |
| 3    | L2    | CI/CD com execução anómala               | Logs de pipeline, correlação por comando e branch   |
| 4    | L3    | Multiuser com sessões hijack             | trace.id, correlação de login/token/sessão          |
| 5    | L1    | Aplicação interna de suporte             | Logging local, sem SIEM, revisão manual             |

---

> Estes casos práticos demonstram como a aplicação integrada dos controlos de logging, alerta e correlação permite **detetar comportamentos que seriam invisíveis isoladamente**.

> ✅ Para aplicações de risco elevado (L3), recomenda-se manter um repositório validado de exemplos reais e simulados, com validação de trigger e resposta.
