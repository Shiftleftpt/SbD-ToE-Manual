---
id: rastreabilidade
title: Rastreabilidade Top-Down – Capítulo 12
sidebar_position: 25
description: Mapeamento das práticas de monitorização e resposta face a frameworks como NIST SSDF, SAMM, BSIMM, ISO e CIS Controls.
tags: [rastreabilidade, frameworks, normativo, monitorizacao, resposta, deteccao]
---


# 📎 Rastreabilidade contra Frameworks — Capítulo 12: Monitorização, Operações e Telemetria {monitorizacao-operacoes:canon:rastreabilidade}

Este documento estabelece a **rastreabilidade entre as práticas de monitorização, logging e resposta prescritas neste capítulo** e os requisitos dos principais frameworks e normas de segurança operacional e deteção de ameaças.

> A rastreabilidade é feita de forma **top-down**, demonstrando como o SbD-ToE cobre os requisitos normativos e técnicos associados à telemetria, visibilidade contínua e resposta coordenada.

---

## 📌 Tabela de Rastreabilidade {monitorizacao-operacoes:canon:rastreabilidade#tabela_de_rastreabilidade}

| Framework / Requisito                                     | Prática do Capítulo 12 que responde                          | Avaliação         |
|-----------------------------------------------------------|--------------------------------------------------------------|--------------------|
| **NIST SSDF v1.1** – RV.1.2 / RV.1.3 / DE.1.2              | Logging estruturado, alertas, correlação e resposta           | ✅ Completo         |
| **OWASP SAMM v2.1** – Operations → Incident Management     | Logging técnico, deteção, métricas operacionais               | ✅ Nível 3          |
| **BSIMM13** – Deployment → TDI1.1 / TDI2.2 / IR1.4         | Logging, alertas, integração com IRP                          | ✅ 3 práticas        |
| **SLSA v1.0** – Observability                              | Logging e alertas em runtime, sem proveniência completa       | ⚠️ Parcial (2/4)    |
| **OWASP DSOMM** – Operations (5 práticas)                  | Logging seguro, alertas, correlação, IR e métricas            | ✅ 5/5              |
| **ISO/IEC 27001** – A.12.4.x / A.16.1.x                    | Logging, deteção, resposta a incidentes                       | ✅ Completo         |
| **CIS Controls v8** – Controlos 8, 17, 18                  | Logs protegidos, deteção e resposta automatizada              | ✅ Completo         |
| **ENISA DevSecOps** – Logging / Observabilidade / IR       | Integração contínua com telemetria e resposta                 | ✅ Completo         |

---

## 🧠 Notas explicativas por framework {monitorizacao-operacoes:canon:rastreabilidade#notas_explicativas_por_framework}

### 🛠️ NIST SSDF v1.1 {monitorizacao-operacoes:canon:rastreabilidade#nist_ssdf_v11}

Cobertura de:
- **RV.1.2**: logging estruturado e seguro (Addon 02);
- **RV.1.3**: uso de logs para análise e melhoria contínua (Addons 07, 05);
- **DE.1.2**: mecanismos de deteção ativa com base em alertas (Addon 03).

---

### 🧱 OWASP SAMM v2.1 {monitorizacao-operacoes:canon:rastreabilidade#owasp_samm_v21}

Alinhamento com *Incident Management*:
- Nível 1: logging de eventos críticos (Addon 01, 02);
- Nível 2: alertas e deteção de anomalias (Addon 03, 06);
- Nível 3: métricas como MTTD/MTTR e tuning (Addon 07).

---

### 📊 BSIMM13 {monitorizacao-operacoes:canon:rastreabilidade#bsimm13}

Domínio Deployment:
- **TDI1.1**: logging técnico e de segurança com tagging (Addon 02);
- **TDI2.2**: deteção baseada em eventos e comportamentos (Addon 03, 06);
- **IR1.4**: integração com processos de resposta (Addon 05, 04).

---

### 🔍 SLSA v1.0 {monitorizacao-operacoes:canon:rastreabilidade#slsa_v10}

Domínio Observability:
- Cobre níveis 1 e 2: runtime logs e alertas (Addon 02, 03);
- Níveis 3 e 4 (proveniência auditável e verificação automática) requerem Cap. 07.

---

### 🧠 OWASP DSOMM {monitorizacao-operacoes:canon:rastreabilidade#owasp_dsomm}

Domínio **Operations**:
- **Logging**: estruturado, com ACLs e retenção (Addon 02);
- **Monitoring**: alertas com base em severidade e comportamento (Addon 03);
- **Alert Tuning**: métricas e tuning periódico (Addon 07);
- **Incident Response Integration**: resposta e playbooks (Addon 05);
- **Security Metrics & KPIs**: MTTD/MTTR operacionais (Addon 07).

---

### 🏛️ ISO/IEC 27001 {monitorizacao-operacoes:canon:rastreabilidade#isoiec_27001}

- **A.12.4.x**: logging técnico, retenção e acesso controlado (Addon 02);
- **A.16.1.x**: deteção de incidentes, resposta e registos (Addon 05).

---

### 📐 CIS Controls v8 {monitorizacao-operacoes:canon:rastreabilidade#cis_controls_v8}

- **Control 8**: logging estruturado e seguro (Addon 02);
- **Control 17**: alertas e correlação (Addon 03, 06);
- **Control 18**: resposta automatizada e playbooks (Addon 05).

---

### 🔄 ENISA DevSecOps {monitorizacao-operacoes:canon:rastreabilidade#enisa_devsecops}

- Logging como parte da pipeline (Addon 02);
- Observabilidade contínua (Addon 03, 04, 06);
- Integração com processos de IR e controlo operacional (Addon 05, 07).

---

## 🔗 Ligações com outros capítulos {monitorizacao-operacoes:canon:rastreabilidade#ligacoes_com_outros_capitulos}

Este capítulo complementa:

- **Capítulo 01** — classificação de risco determina escopo de monitorização;
- **Capítulo 02 / 03** — requisitos e ameaças que devem ser detetáveis via logging;
- **Capítulo 07** — geração de logs e rastreabilidade nos pipelines CI/CD;
- **Capítulo 09** — observabilidade e execução segura em ambientes containerizados;
- **Capítulo 14** — suporte à auditoria e validação contínua de exceções operacionais.

> 📌 Esta rastreabilidade demonstra que o Capítulo 12 estabelece a fundação da **segurança contínua e operacional**, com visibilidade, correlação e resposta integradas em todo o ciclo de vida.
