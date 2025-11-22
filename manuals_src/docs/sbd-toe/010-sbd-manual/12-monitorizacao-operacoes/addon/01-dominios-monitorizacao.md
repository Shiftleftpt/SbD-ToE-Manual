---
description: Identificação e definição dos domínios técnicos e operacionais a monitorizar
  em sistemas modernos.
id: dominios-monitorizacao
sidebar_position: 1
tags:
- infraestrutura
- logging
- monitorização
- observabilidade
- runtime
- seguranca
- segurança
title: Domínios de Monitorização e Observabilidade
---


# 🧭 Domínios e Abrangência da Monitorização

## 🌟 Objetivo

Definir uma taxonomia prática dos **domínios de monitorização** aplicáveis a aplicações e sistemas, permitindo estruturar controlos de deteção, operação, rastreabilidade e segurança, com proporcionalidade ao nível de risco e aos fluxos críticos.

---

## 🧬 O que são domínios de monitorização

A monitorização aplicacional e infraestrutural pode ser classificada em domínios específicos consoante o tipo de dados observados e os objetivos de deteção, análise ou rastreabilidade. Cada domínio foca-se num subconjunto distinto do comportamento do sistema, e exige ferramentas e abordagens próprias.

---

## 🗂️ Tipos de monitorização

| Tipo                        | Finalidade principal                                  | Exemplos práticos                                     |
|-----------------------------|--------------------------------------------------------|--------------------------------------------------------|
| **Técnica (runtime)**       | Deteção de falhas, exceções, problemas de performance | Logs de erro, métricas de CPU/memória, tracebacks     |
| **Segurança (SIEM)**        | Deteção de eventos suspeitos ou abusivos              | Logins falhados, alteração de permissões, DoS         |
| **Negócio / funcional**     | Visibilidade sobre fluxos críticos                    | Eventos de checkout, acessos a áreas sensíveis        |
| **Conformidade / auditoria**| Rastreabilidade e prova de conformidade               | Quem acedeu a quê, quando, com que perfil              |
| **Infraestrutura / CI/CD**  | Monitorização do ambiente e do pipeline               | Alterações de config, builds, uso de secrets           |

> 🌐 A correta classificação permite aplicar requisitos de forma proporcional, com foco em deteção, rastreabilidade ou otimização operacional.

---

## 🔎 Como aplicar

1. **Identificar fluxos críticos** da aplicação e do sistema;
2. **Mapear domínios aplicáveis** a cada fluxo (ex: funcional, segurança, CI/CD);
3. **Selecionar fontes de dados** compatíveis com cada domínio (ver abaixo);
4. **Integrar ferramentas de observabilidade** adaptadas ao contexto (ex: Prometheus, ELK, Splunk, Datadog);
5. **Correlacionar eventos entre domínios**, sempre que possível, para deteção mais eficaz.

---

## 📘 Fontes típicas de dados para cada domínio

| Origem              | Tipo de dados                         | Ferramentas comuns                    |
|---------------------|----------------------------------------|----------------------------------------|
| Aplicação           | Logs estruturados (JSON, ECS...)       | Logback, Winston, Serilog              |
| Infraestrutura      | Syslog, métricas, eventos               | Filebeat, Fluentbit, Prometheus        |
| CI/CD               | Saída de pipelines, rastos de build    | GitHub Actions, GitLab, Azure DevOps   |
| API Gateway / WAF   | Requests, erros, bloqueios             | Kong, NGINX, AWS WAF, Azure Frontdoor  |
| SIEM                | Eventos agregados                      | Splunk, Sentinel, Elastic, QRadar      |

---

## 📊 Proporcionalidade por nível de risco

A seleção de domínios e profundidade de monitorização deve ser proporcional à criticidade da aplicação:

- **Aplicações L3**: cobertura completa dos domínios, com integração com SIEM e alertas ativos.
- **Aplicações L2**: foco em runtime, infraestrutura e segurança; logging centralizado obrigatório.
- **Aplicações L1**: podem limitar-se a métricas técnicas, desde que justificado e aceite por segurança.

> 📌 A `addon/08-matriz-controles-por-risco.md` detalha os mínimos por nível de risco.

---

## ✅ Boas práticas

- Aplicar logging estruturado (ex: JSON, ECS) com enriquecimento de contexto;
- Priorizar domínios que suportam deteção ativa e resposta (ex: segurança, CI/CD);
- Rever cobertura de domínios ao longo do SDLC;
- Integrar com plataforma de observabilidade comum (ex: stack ELK, Datadog, Grafana/Loki);
- Correlacionar eventos entre domínios para deteção de ataques ou falhas encadeadas.

---

## 📎 Referências cruzadas

| Documento                           | Relação com este tópico                         |
|-------------------------------------|--------------------------------------------------|
| `08-matriz-controles-por-risco.md` | Define mínimos por domínio e por criticidade     |
| `04-integracao-siem.md`            | Integração de eventos com plataformas de deteção |
| `05-monitorizacao-operacoes.md`     | Resposta a eventos e alertas                     |
| `06-correlacao-anomalias.md`       | Estratégias de correlação entre domínios         |

---

> 🔍 A classificação clara dos domínios de monitorização é essencial para uma abordagem eficaz, auditável e proporcional à deteção de anomalias e à operação segura de sistemas modernos.
