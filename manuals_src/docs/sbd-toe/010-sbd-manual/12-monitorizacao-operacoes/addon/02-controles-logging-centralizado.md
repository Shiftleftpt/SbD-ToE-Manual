---
description: Práticas para garantir logging estruturado, transporte seguro e centralização
  de eventos operacionais.
id: controles-logging-centralizado
sidebar_position: 2
tags:
- ECS
- centralização
- ciclo-vida
- deteccao
- estruturação
- logging
- transporte seguro
title: Controles de Logging Estruturado e Centralizado
---



# 🗃️ Logging Estruturado e Centralizado

## 🌟 Objetivo

Garantir que todas as aplicações registam eventos de forma estruturada, segura, rastreável e auditável, permitindo a deteção de anomalias, correlação entre sistemas e suporte à resposta a incidentes.

---

## 🧬 O que é logging estruturado

Logging estruturado consiste na **emissão de eventos com campos normalizados**, num formato legível por máquina (ex: JSON), transportado para um sistema centralizado e com garantias de integridade e retenção.

> 📌 A estrutura e consistência dos logs são essenciais para deteção, rastreabilidade e investigação eficaz.

---

## 🧱 Estrutura recomendada dos eventos

Adotar uma convenção como o Elastic Common Schema (ECS) ou formato próprio baseado em JSON com campos mínimos comuns.

| Campo            | Exemplo                                      | Observações                                   |
|------------------|----------------------------------------------|-----------------------------------------------|
| `timestamp`      | `2025-07-21T10:35:14Z`                        | ISO 8601 em UTC                               |
| `level`          | `INFO`, `ERROR`, `WARN`, `DEBUG`             | Níveis padronizados                           |
| `event.action`   | `user.login`, `file.upload`, `api.call`      | Taxonomia consistente                         |
| `user.id`        | `abcd-1234`                                   | ID interno do utilizador, se aplicável        |
| `src.ip`         | `192.168.1.20`                                | IP de origem                                  |
| `trace.id`       | `xyz-9876`                                    | Suporte a tracing distribuído                 |
| `application`    | `frontend-web`, `api-gateway`, `worker-job`  | Componente lógica da aplicação                |

---

## 📦 Transporte e centralização dos logs

- Usar **agentes de forwarding** (ex: Filebeat, Fluentbit, Vector)
- Garantir **transporte seguro (TLS)** e persistência temporária (buffers)
- Preferir **streaming contínuo** (ex: TCP, gRPC) a batch ou UDP
- Separar logging do processo principal (ex: sidecar container, logging driver)

### Destinos típicos:

| Categoria       | Exemplos                              |
|-----------------|----------------------------------------|
| SIEMs           | Splunk, Sentinel, QRadar              |
| Observabilidade | Elastic Stack, Loki, Datadog          |
| Híbridos        | OpenSearch, Graylog, Grafana Tempo    |

---

## 🔒 Segurança e integridade dos logs

| Controlo                          | Descrição                                                        |
|-----------------------------------|------------------------------------------------------------------|
| **Retenção protegida (WORM)**     | Impede alteração de logs após escrita                            |
| **Acesso restrito**               | Escrita apenas via aplicação; leitura auditada                   |
| **Assinatura ou hash**            | Verificação de integridade por lote ou ficheiro                  |
| **Isolamento de função**          | Logging separado da aplicação (ex: forwarder, sidecar, service)  |

> ⚠️ Logs apenas locais são aceitáveis apenas para aplicações L1 - com recolha periódica e justificação documentada.

---

## 📌 Eventos mínimos obrigatórios

| Tipo de evento        | Deve conter…                                    |
|-----------------------|--------------------------------------------------|
| Autenticação falhada  | IP, utilizador, timestamp, motivo                |
| Alterações sensíveis  | Quem, o quê, onde, antes e depois                |
| Exceções internas     | Stack trace (resumido), módulo, request ID       |
| Upload / download     | Nome, tamanho, utilizador, método                |
| Chamada API externa   | Endpoint, status, tempo de resposta              |

---

## ✅ Boas práticas

- Não registar dados sensíveis (ex: passwords, tokens), mesmo cifrados
- Separar logs por contexto funcional (ex: `app.log`, `auth.log`, `db.log`)
- Validar presença e formato de logs nos testes automatizados
- Incluir `request.id` e `trace.id` para rastreabilidade de pedidos distribuídos
- Emitir logs em todas as transições de estado de segurança

---

## 🧩 Ligação com deteção e resposta

O logging estruturado serve como **base para os mecanismos de deteção** definidos noutros documentos:

| Documento                      | Relação com este tópico                     |
|--------------------------------|----------------------------------------------|
| `03-alertas-eventos-criticos.md` | Geração de alertas a partir de eventos      |
| `06-correlacao-anomalias.md`    | Correlação entre eventos para deteção       |
| `08-matriz-controles-por-risco.md` | Requisitos de logging por nível L1–L3     |

---

> 🔐 Um sistema de logging bem estruturado e centralizado é pré-requisito para deteção eficaz, resposta a incidentes, e conformidade com frameworks como SSDF, SLSA, ISO 27001.
