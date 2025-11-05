---
id: integracao-siem
title: Integração com SIEM e Plataformas de Correlação
sidebar_position: 4
description: Integração com sistemas SIEM para parsing, visualização e correlação de eventos.
tags: [siem, integração, parsing, dashboards, correlação]
---


# 📉 Integração com Sistemas de Deteção (SIEM)

## 🌟 Objetivo

Garantir uma **integração fiável, segura e auditável** entre as fontes de eventos (aplicações, infraestruturas, pipelines) e o sistema de análise e correlação (SIEM), assegurando suporte a deteção eficaz, resposta e rastreabilidade.

---

## 🧬 O que é a integração com SIEM

Trata-se da cadeia de **coleta, transporte, transformação e ingestão** dos eventos relevantes num SIEM, garantindo:

* Formato adequado e compatível com parsing;
* Latência reduzida e resiliência a falhas;
* Capacidade de correlação eficaz entre fontes.

> 🧑‍💻 A aplicação nunca deve comunicar diretamente com o SIEM - usar sempre um forwarder como camada de isolamento.

---

## 📀 Arquitetura típica de integração

```
[Aplicação] → [Logger] → [Forwarder/Agent] → [Parser] → [SIEM]
```

| Componente          | Função principal                                      |
| ------------------- | ----------------------------------------------------- |
| **Logger**          | Emissão de logs estruturados (ex: JSON, ECS)          |
| **Forwarder**       | Coleta local, buffering e envio seguro                |
| **Parser/Ingester** | Transformar logs para formato normalizado e indexável |
| **SIEM**            | Análise, correlação, visualização e alerta            |

---

## 🛠️ Requisitos funcionais da integração

| Requisito                            | Descrição                                      |
| ------------------------------------ | ---------------------------------------------- |
| **Formato suportado**                | JSON, CEF, LEEF, ECS, Syslog estruturado       |
| **Canal seguro**                     | TLS 1.2+ com autenticação (chave, token, mTLS) |
| **Buffering local**                  | Forwarder deve tolerar falhas de rede          |
| **Tagging por aplicação / ambiente** | Facilita filtros e dashboards                  |
| **Timestamps normalizados**          | UTC, ISO 8601, sincronizado via NTP            |

---

## 🔧 Ferramentas comuns

| Categoria           | Exemplos                                            |
| ------------------- | --------------------------------------------------- |
| **Forwarders**      | Filebeat, Fluentbit, Vector, rsyslog                |
| **SIEMs**           | Splunk, Azure Sentinel, Elastic SIEM, QRadar        |
| **Normalizadores**  | Logstash, Cribl, ingest pipelines (OpenSearch, ELK) |
| **Observabilidade** | Grafana, Loki, Datadog, Prometheus                  |

---

## ✅ Boas práticas de integração

* Validar logs com `tcpdump`, `wireshark` ou dashboards de ingesão;
* Usar **filtros de enriquecimento** (ex: geolocalização, `user-agent`, `env`);
* Evitar redundância (mesmo evento enviado para vários destinos);
* Testar envio com `logger`, `curl`, replay de logs reais;
* Garantir reversão segura (rollback de versão de forwarder, tags, etc.).

---

## 🔍 Validação da integração

| Verificação                         | Método sugerido                               |
| ----------------------------------- | --------------------------------------------- |
| Evento chegou ao SIEM               | Confirmar via index ou forwarder log          |
| Campos foram parseados corretamente | Ver em dashboard ou query de inspeção         |
| Latência entre geração e ingesão    | Medida com timestamp vs ingest time           |
| Duplicados ou perdas                | Verificação por hash / ID / contagem esperada |

---

## 🔒 Considerações de segurança

* Isolar rede de forwarders da rede do SIEM;
* Monitorizar falhas de envio ou parsing com alertas;
* Proteger configurações dos agentes (tokens, paths, endpoints);
* Validar que os eventos não contêm dados sensíveis em claro.

---

## 📂 Integrações avançadas

* Logging de execução de pipelines (CI/CD, DevOps);
* Envio de eventos diretamente via API gateways e proxies;
* Correlação com sessão, utilizador, `trace.id`, etc.;
* Dashboards por aplicação, ambiente, componente.

---

## 🧹 Ligação com outros controlos

| Documento                          | Relação com este tópico                        |
| ---------------------------------- | ---------------------------------------------- |
| `02-logging-centralizado.md`       | Define as fontes e formatos dos eventos        |
| `06-correlacao-anomalias.md`       | Utiliza os eventos para deteção e correlação   |
| `09-ameacas-mitigadas.md`          | Mostra como a integração suporta resposta      |
| `08-matriz-controles-por-risco.md` | Determina se integração com SIEM é obrigatória |

> 🧠 A qualidade da integração com o SIEM determina diretamente a eficácia da resposta e rastreabilidade dos sistemas.
