---
id: ameacas-mitigadas
title: Ameaças Mitigadas pelas Práticas de Monitorização e Operações
sidebar_position: 50
description: Tabela de ameaças mitigadas pelas práticas de logging, correlação e resposta descritas neste capítulo.
tags: [ameacas, deteccao, resposta, logging, osc&r, ameaças, mitigação, visibilidade]
---


# ⚡️ Ameaças Mitigadas pelas Práticas de Monitorização e Operações

Este documento apresenta uma visão consolidada das **ameaças técnicas e operacionais mitigadas pelas práticas descritas no Capítulo 12 - Monitorização, Logging e Resposta a Incidentes**.

A referência principal é o modelo **OWASP OSC&R** (Open Software Supply Chain Attack Reference), complementado com taxonomias como **MITRE ATT&CK**, **STRIDE**, **CAPEC**, **SSDF**, **BSIMM**, **CIS Controls** e o **OWASP DSOMM** (*Operations*).

> ⚠️ Este capítulo não mitiga vulnerabilidades diretamente, mas **é essencial para detetar falhas, reagir a eventos de segurança e garantir visibilidade runtime**, funcionando como **segunda linha de defesa ativa**.

---

## 🔍 Categoria 1 - Ausência de logging e visibilidade operacional

| Ameaça                            | Fonte                        | Como surge                                    | Como a prática mitiga                                                | Controlos associados                       |
|----------------------------------|-------------------------------|-----------------------------------------------|------------------------------------------------------------------------|--------------------------------------------|
| Eventos críticos não registados  | SSDF PW.8 / ISO 27001 A.12   | Logging desestruturado ou ausente             | Logging estruturado, obrigatório e centralizado                        | `addon/02-controles-logging-centralizado.md` |
| Logs voláteis ou truncados       | STRIDE (Repudiation) / CAPEC-233 | Logs locais não persistidos ou sem ACL       | Retenção ≥30 dias, envio seguro, controle de formato e destino        | `addon/02-controles-logging-centralizado.md` |
| Falta de rastreabilidade de execução | DSOMM → Operations / MITRE T1562 | Ausência de contexto e origem em logs     | Tagging e correlação por aplicação, domínio e pipeline                | `addon/06-correlacao-anomalias.md`         |

---

## 🚨 Categoria 2 - Alertas inexistentes ou ineficazes

| Ameaça                         | Fonte                           | Como surge                                  | Como a prática mitiga                                                   | Controlos associados                    |
|--------------------------------|----------------------------------|---------------------------------------------|--------------------------------------------------------------------------|-----------------------------------------|
| Incidentes sem alerta          | MITRE T1609 / SSDF RV.1         | Falta de alertas automáticos                | Alertas baseados em eventos críticos, integração com SIEM                | `addon/03-alertas-eventos-criticos.md` |
| Alertas ignorados por ruído    | OWASP Logging / BSIMM           | Volume elevado sem priorização              | Filtros por criticidade, canais apropriados, tuning contínuo            | `addon/03-alertas-eventos-criticos.md`, `addon/07-metricas-indicadores.md` |
| Falta de correlação de alertas | CAPEC-310 / STRIDE              | Alertas isolados, sem contexto de origem    | Correlação entre fontes com perfil comportamental e deduplicação        | `addon/06-correlacao-anomalias.md`     |

---

## 🧯 Categoria 3 - Resposta ineficaz ou descoordenada

| Ameaça                         | Fonte                              | Como surge                                | Como a prática mitiga                                                   | Controlos associados                    |
|--------------------------------|-------------------------------------|-------------------------------------------|--------------------------------------------------------------------------|-----------------------------------------|
| Incidentes sem owner definido  | SSDF RM.3 / ISO 27001 A.16         | Sem responsáveis definidos                | Tabelas de owners e canais de escalamento automatizado                   | `addon/05-monitorizacao-operacoes.md`   |
| Reação ad-hoc ou tardia        | ENISA DevSecOps / BSIMM Ops        | Falta de processo de resposta             | Integração com IRP, uso de playbooks e simulações regulares              | `addon/05-monitorizacao-operacoes.md`   |
| Eventos sem acionamento de ação| MITRE / OSC&R                      | Logs ignorados após deteção               | Integração com workflows e mecanismos de correção (chatops, SOAR)        | `addon/05-monitorizacao-operacoes.md`   |

---

## 📊 Categoria 4 - Falta de métricas e capacidade de medição

| Ameaça                             | Fonte                              | Como surge                                | Como a prática mitiga                                                   | Controlos associados                    |
|------------------------------------|-------------------------------------|-------------------------------------------|--------------------------------------------------------------------------|-----------------------------------------|
| Ausência de métricas de postura    | SSDF PW.5 / ISO 27034              | Sem indicadores de cobertura ou impacto   | KPIs de segurança: MTTD, MTTR, % de logs, alertas por severidade        | `addon/07-metricas-indicadores.md`     |
| Impossibilidade de priorizar riscos| NIST 800-137 / ISO 27005           | Sem visão integrada de exposição          | Matriz de controlos por risco, dashboards operacionais                   | `addon/08-matriz-controles-por-risco.md`|
| Dados sem granularidade ou visão   | BSIMM / OWASP                      | Visão agregada e não segmentada           | Visualização por aplicação, domínio, origem de evento                    | `addon/07-metricas-indicadores.md`     |

---

## 🔄 Categoria 5 - Integração deficiente no ciclo de vida

| Ameaça                                  | Fonte                            | Como surge                              | Como a prática mitiga                                                   | Controlos associados                    |
|-----------------------------------------|-----------------------------------|-----------------------------------------|--------------------------------------------------------------------------|-----------------------------------------|
| Novos sistemas sem monitorização        | SSDF PW.1 / ISO 27001 A.14       | Ciclo de vida sem requisitos de logging | Inclusão formal nos critérios de aceitação e Definition of Done          | `15-aplicacao-lifecycle.md`      |
| Equipas ignoram alertas operacionais    | OWASP / BSIMM Ops                | Alertas fora dos canais de decisão      | Integração com ferramentas operacionais e turnos on-call                 | `addon/05-monitorizacao-operacoes.md`   |
| Dados não usados para melhoria contínua | DSOMM / SSDF RM.2                | Logs não geram ações corretivas         | Integração com KPIs, backlog de segurança, validação contínua           | `addon/07-metricas-indicadores.md`, `20-checklist-revisao.md` |

---

## ✅ Conclusão

O Capítulo 12 constitui o **eixo central da visibilidade runtime**, permitindo:

- Detetar falhas e abusos em tempo útil;
- Reduzir o tempo de exposição (MTTD/MTTR);
- Correlacionar sinais dispersos em eventos acionáveis;
- Reagir com coordenação e eficácia operacional.

> 📌 Estas práticas mitigam **mais de 15 ameaças operacionais conhecidas** e são pré-requisito para modelos de resposta modernos como SOAR, IRP e auditoria contínua.

> ⚙️ São exigidas direta ou indiretamente por **SSDF**, **BSIMM**, **ISO 27001**, **CIS v8**, **ENISA**, **MITRE ATT&CK**, **OSC&R** e **DSOMM** (domínio *Operations*), sendo a fundação da **segurança como sistema vivo**.
