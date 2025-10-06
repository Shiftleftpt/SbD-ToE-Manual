---
id: correlacao-anomalias
title: Correlação de Eventos e Deteção de Anomalias
sidebar_position: 6
description: Estratégias para correlação de logs entre fontes e deteção de comportamentos suspeitos.
tags: [correlação, anomalias, eventos, deteção, multi-sistema]
---


# 🧬 Correlação e Deteção de Anomalias {monitorizacao-operacoes:addon:correlacao-anomalias}

## 🌟 Objetivo {monitorizacao-operacoes:addon:correlacao-anomalias#objetivo}

Aplicar técnicas de correlação de eventos e deteção de anomalias para identificar padrões de comportamento que, embora inofensivos de forma isolada, possam indicar risco significativo quando analisados em conjunto.

---

## 🎯 Objetivos da aplicação de correlação {monitorizacao-operacoes:addon:correlacao-anomalias#objetivos_da_aplicacao_de_correlacao}

* Detetar **comportamentos suspeitos** emergentes de padrões discretos
* Reduzir **falsos positivos** através de contexto cruzado
* Priorizar **incidentes reais** com base em múltiplas evidências
* Suportar **deteção proativa e adaptativa**

---

## 🥁 Tipos de correlação {monitorizacao-operacoes:addon:correlacao-anomalias#tipos_de_correlacao}

| Tipo               | Exemplo prático                               |
| ------------------ | --------------------------------------------- |
| **Temporal**       | Ações suspeitas em curto intervalo            |
| **Contextual**     | Login fora de horas + IP incomum              |
| **Comportamental** | Desvio do padrão do utilizador                |
| **Cross-source**   | Evento em app seguido de firewall ou SIEM     |
| **Sessão / fluxo** | Eventos com mesmo `trace.id` ou session token |

---

## 🛠️ Técnicas e ferramentas de suporte {monitorizacao-operacoes:addon:correlacao-anomalias#tecnicas_e_ferramentas_de_suporte}

| Técnica                 | Aplicação / exemplo                           |
| ----------------------- | --------------------------------------------- |
| **Regras no SIEM**      | Splunk, Sentinel, QRadar                      |
| **Chaining / grafos**   | Grafos de identidade e sessão                 |
| **Modelos de baseline** | Desvios por IP, endpoint, hora                |
| **Threshold composto**  | Múltiplas condições acumuladas                |
| **Score agregado**      | Pontuação por utilizador, device ou aplicação |

> ⚠️ A correlação baseada em regras é o melhor ponto de partida para maioria das organizações.

---

## 🧠 Exemplos de padrões correlacionados {monitorizacao-operacoes:addon:correlacao-anomalias#exemplos_de_padroes_correlacionados}

| Padrão identificado                | Interpretação             |
| ---------------------------------- | ------------------------- |
| Login + download massivo           | Abuso de credenciais      |
| Falhas repetidas + sucesso         | Brute force bem-sucedido  |
| Mudança de role + alteração config | Escalada de privilégios   |
| API key + acesso fora do horário   | Uso indevido              |
| Commit + execução atípica CI/CD    | Comprometimento na cadeia |

---

## 🪧 Boas práticas {monitorizacao-operacoes:addon:correlacao-anomalias#boas_praticas}

* Normalizar eventos antes da correlação (formatos, campos)
* Usar janelas temporais limitadas (ex: 5m, 15m)
* Corrigir falsos negativos com novos fatores de correlação
* Usar IDs persistentes: `user.id`, `session.id`, `trace.id`
* Avaliar severidade do conjunto, não dos eventos isolados

---

## 📊 Deteção baseada em comportamento {monitorizacao-operacoes:addon:correlacao-anomalias#detecao_baseada_em_comportamento}

| Técnica                     | Finalidade                                    |
| --------------------------- | --------------------------------------------- |
| **Baseline por utilizador** | Desvios individuais (tempo, volume, endpoint) |
| **Perfil por role**         | Ações não previstas para determinado perfil   |
| **Métricas agregadas**      | Chamada de APIs, latência, variação no padrão |
| **Feedback supervisionado** | Reforço de regras com base em casos reais     |

> 💡 Requer tuning progressivo e participação ativa das equipas.

---

## 🧹 Integração com outros controlos {monitorizacao-operacoes:addon:correlacao-anomalias#integracao_com_outros_controlos}

| Documento                        | Relação com este tópico                      |
| -------------------------------- | -------------------------------------------- |
| `02-logging-centralizado.md`     | Fonte dos eventos para correlação            |
| `04-integracao-siem.md`          | Canal e formato da ingesão                   |
| `03-alertas-eventos-criticos.md` | Geração de alertas baseada em padrões        |
| `09-ameacas-mitigadas.md`        | Mapeia deteção a cenários de ameaça (OSC\&R) |

---

## ✅ Recomendações finais {monitorizacao-operacoes:addon:correlacao-anomalias#recomendacoes_finais}

* Começar com correlação simples, baseada em eventos de alto impacto
* Testar com dados reais, simulados e logs antigos
* Acompanhar métricas de qualidade (sinal/ruído, tempo de triagem)
* Evoluir para scoring, baseline dinâmico e detecção assistida

> 🌟 A correlação eficaz reduz falsos positivos e revela padrões complexos que de outro modo passariam despercebidos.
