---
id: maturidade
title: Mapeamento de Maturidade – Capítulo 12
sidebar_position: 10
tags: [canon, maturidade, SAMM, BSIMM, SSDF, SLSA, DSOMM]
---

# 📈 Maturidade — Monitorização e Operações {monitorizacao-operacoes:canon:maturidade}

Este documento apresenta o **mapeamento de maturidade das práticas descritas no Capítulo 12 — Monitorização e Operações**, com base nos principais frameworks de referência:

- **OWASP SAMM**
- **BSIMM**
- **NIST SSDF**
- **SLSA**
- **OWASP DSOMM**

As práticas abordam logging estruturado, métricas de segurança, alertas, integração com resposta a incidentes, correlação de eventos e observabilidade contínua.

---

## 🎯 Como interpretar este mapeamento de maturidade {monitorizacao-operacoes:canon:maturidade#como_interpretar_este_mapeamento_de_maturidade}

Este mapeamento avalia o **grau de completude e sofisticação** das práticas prescritas, de acordo com os mecanismos nativos de cada framework:

| Framework        | Avaliação usada                     | Justificação                                      |
|------------------|-------------------------------------|--------------------------------------------------|
| OWASP SAMM       | `n / 3`                             | Três níveis por domínio                          |
| OWASP DSOMM      | `n / m`                             | Níveis de maturidade por domínio técnico         |
| NIST SSDF        | Lista de controlos cobertos         | Avaliação binária (completo/incompleto)          |
| BSIMM            | Práticas observadas                 | Enfoque empírico                                 |
| SLSA             | Nível acumulativo (1–4)             | Requisitos progressivos                          |

---

## 🧭 Visão Geral de Alinhamento {monitorizacao-operacoes:canon:maturidade#visao_geral_de_alinhamento}

| Framework     | Domínios Relevantes                  | Práticas Cobertas                                              | Avaliação de Maturidade        |
|---------------|---------------------------------------|------------------------------------------------------------------|--------------------------------|
| **SAMM v2.1** | Operations → Incident Management      | Logging, alertas, KPIs, integração com resposta                 | **3 / 3**                      |
| **BSIMM13**   | Deployment → TDI1.1, TDI2.2, IR1.4    | Telemetria, correlação, resposta                                | Contributo direto              |
| **SSDF**      | DE.1.2, RV.1.2, RV.1.3                | Logging seguro, correlação, métricas operacionais               | **✔️ DE.1.2, RV.1.2, RV.1.3** |
| **SLSA v1.0** | Observability                         | Logging e métricas integradas                                   | **Nível 2 / 4**                |
| **DSOMM**     | Operations                            | Monitorização, deteção, alertas, IR, correlação                 | **5 / 5**                      |

---

## 🧱 OWASP SAMM – Operations → Incident Management {monitorizacao-operacoes:canon:maturidade#owasp_samm__operations__incident_management}

| Nível | Descrição SAMM                                  | Implementação no Cap. 12                          |
|-------|--------------------------------------------------|---------------------------------------------------|
| 1     | Logging básico e manual                          | ✅ Logging estruturado                             |
| 2     | Monitorização contínua e alertas                 | ✅ Alertas automatizados e dashboards              |
| 3     | Integração com resposta a incidentes             | ✅ Correlação e canal de resposta definido         |

**🧮 Maturidade atingida: 3 / 3**

---

## 🧱 OWASP DSOMM – Operations {monitorizacao-operacoes:canon:maturidade#owasp_dsomm__operations}

| Domínio     | Nível | Justificação técnica                                              |
|-------------|-------|-------------------------------------------------------------------|
| Operations  | 5 / 5 | Cobertura completa: logging, deteção, correlação, integração IR   |

---

## 🧱 NIST SSDF – Controlos de Monitorização {monitorizacao-operacoes:canon:maturidade#nist_ssdf__controlos_de_monitorizacao}

| Controlos NIST SSDF | Descrição                                       | Alinhamento com Cap. 12                  |
|---------------------|--------------------------------------------------|------------------------------------------|
| DE.1.2              | Deteção ativa de eventos                         | ✅ Regras de deteção e correlação         |
| RV.1.2              | Logging seguro e audível                         | ✅ Logging estruturado                    |
| RV.1.3              | Avaliação contínua da integridade                | ✅ Métricas, KPIs e evidência             |

---

## 🧱 BSIMM – Práticas Observadas {monitorizacao-operacoes:canon:maturidade#bsimm__praticas_observadas}

| Prática BSIMM | Alinhamento com Cap. 12                                  |
|---------------|-----------------------------------------------------------|
| TDI1.1        | Coleta estruturada de telemetria                          |
| TDI2.2        | Correlacionar eventos para deteção de ataques             |
| IR1.4         | Ativação de planos de resposta a incidentes               |

---

## 🧱 SLSA – Observabilidade {monitorizacao-operacoes:canon:maturidade#slsa__observabilidade}

| Nível | Requisitos principais                                | Cobertura pelo Cap. 12                             |
|-------|------------------------------------------------------|----------------------------------------------------|
| 1     | Logging básico de build/test                         | ✅ Logging mínimo em pipelines                     |
| 2     | Logging com métricas e alertas                       | ✅ KPIs operacionais e deteção automatizada        |
| 3     | Observabilidade com integridade garantida            | ❌ Parcial — não aborda verificação criptográfica  |
| 4     | Telemetria auditável e controlada externamente       | ❌ Não aplicável neste contexto                    |

**🔐 Nível máximo suportado por este capítulo: SLSA 2 / 4**

---

## ✅ Conclusão {monitorizacao-operacoes:canon:maturidade#conclusao}

- As práticas prescritas permitem atingir **maturidade elevada e completa em SAMM, DSOMM e SSDF**;
- Os controlos cobrem os principais requisitos de deteção, rastreabilidade e resposta técnica;
- A integração com resposta a incidentes e métricas de operação reforça o ciclo de segurança contínua.
