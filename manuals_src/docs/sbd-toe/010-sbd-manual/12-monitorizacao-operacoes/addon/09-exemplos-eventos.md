---
id: exemplos-eventos
title: Exemplos de Eventos Relevantes para Monitorização
sidebar_position: 9
description: Catálogo de eventos típicos a monitorizar para fins operacionais e de segurança.
tags: [eventos, logging, segurança, observabilidade, catálogo]
---


# 🪨 Ameaças Mitigadas por Monitorização e Operações

## 🌟 Objetivo

Mapear os vetores de ataque que podem ser **detetados, antecipados ou correlacionados** pelas práticas descritas neste capítulo, contribuindo para a capacidade de resposta e melhoria da postura de segurança.

---

## 📊 Categorias de ameaça abordadas

| Categoria (OSC\&R / ATT\&CK)         | Descrição resumida                             |
| ------------------------------------ | ---------------------------------------------- |
| **Abuso de credenciais**             | Uso de senhas ou tokens comprometidos          |
| **Brute force / guessing**           | Tentativas repetidas de autenticação           |
| **Privilege escalation / tampering** | Elevação ou alteração indevida de permissões   |
| **Access abuse / insider misuse**    | Uso ilegítimo de acessos válidos               |
| **Data exfiltration**                | Saída não autorizada de dados                  |
| **Pipeline compromise**              | Execução indevida em pipelines CI/CD           |
| **Configuration tampering**          | Modificação de parâmetros ou secrets           |
| **Availability sabotage (DoS)**      | Inatividade suspeita, perda de logs, sabotagem |

---

## 🔍 Mapeamento práticas → ameaças mitigadas

| Prática de monitorização                 | Ameaças mitigadas                    |
| ---------------------------------------- | ------------------------------------ |
| Logging de autenticações e falhas        | Brute force, abuso de credenciais    |
| Alertas por login fora de perfil         | Insider misuse, uso indevido         |
| Correlação: role change + config change  | Privilege escalation, tampering      |
| Monitorização de uploads/downloads       | Exfiltração, movimento lateral       |
| Detetar execuções invulgares em pipeline | Comprometimento em CI/CD             |
| Logging de exceções estruturadas         | Reconhecimento, probing, caça a bugs |
| Alerta de perda de logs ou inatividade   | Sabotagem, tampering de forwarding   |

---

## 📄 Exemplos de cobertura prática

| Ameaça identificada        | Evento(s) indicativos                            | Prática associada                     |
| -------------------------- | ------------------------------------------------ | ------------------------------------- |
| **Brute force**            | >10 falhas em 3min de um IP                      | Alertas threshold, logs auth          |
| **Token comprometido**     | Login com token válido fora do país habitual     | Correlação com IP/geolocalização      |
| **Privilege abuse**        | Criação de user + alteração de secret            | Logging + correlação entre fontes     |
| **Exfiltração silenciosa** | Transferência alta de dados off-hour             | Detecção comportamental               |
| **Sabotagem de logs**      | Perda de logs + alteração de config do forwarder | Alertas de inatividade + logs sistema |

---

## ✅ Recomendações finais

* Utilizar este mapeamento como base para **justificação de controlos de monitorização**;
* Relacionar diretamente com OSC\&R / MITRE ATT\&CK nos planos de cobertura e threat modeling;
* Priorizar ameaças com **impacto elevado e baixa visibilidade sem logging ativo**.

> 🧠 Monitorizar não é bloquear — é **detetar e reagir a tempo**. A visibilidade é o primeiro passo da resiliência.
