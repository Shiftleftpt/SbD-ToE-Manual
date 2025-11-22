---
id: achievable-maturity
title: Mapeamento de Maturidade - Capítulo 11
sidebar_position: 10
tags: [DSOMM, SAMM, SLSA, SSDF, canon, maturidade]
---

# 📈 Maturidade - Deploy Seguro

Este documento apresenta o **mapeamento de maturidade das práticas descritas no Capítulo 11 - Deploy Seguro**, com base nos principais frameworks de referência:

- **OWASP SAMM**
- **BSIMM**
- **NIST SSDF**
- **SLSA**
- **OWASP DSOMM**

As práticas cobrem: validação de readiness, controlo de triggers de deploy, rollback seguro, registo de decisões, gates automatizados e rastreabilidade organizacional em ambientes de produção.

---

## 🎯 Como interpretar este mapeamento de maturidade

Este mapeamento avalia o **grau de completude e sofisticação prática** face aos requisitos de cada framework. As métricas aplicadas seguem a estrutura nativa de cada referência:

| Framework        | Avaliação usada                     | Justificação                                      |
|------------------|-------------------------------------|--------------------------------------------------|
| OWASP SAMM       | `n / 3`                             | Três níveis por domínio                          |
| OWASP DSOMM      | `n / m`                             | Níveis de maturidade por domínio técnico         |
| NIST SSDF        | Lista de controlos cobertos         | Avaliação objetiva e não graduada                |
| BSIMM            | Práticas observadas                 | Abordagem empírica                               |
| SLSA             | Nível acumulativo (1–4)             | Requisitos progressivos                          |

---

## 🧭 Visão Geral de Alinhamento

| Framework     | Domínios Relevantes                  | Práticas Cobertas                                                  | Avaliação de Maturidade        |
|---------------|---------------------------------------|----------------------------------------------------------------------|--------------------------------|
| **SAMM v2.1** | Verification → Security Testing       | Gates, validação final, rollback                                    | **3 / 3**                      |
| **BSIMM13**   | Deployment → CMVM, SE2.5              | Controlo de promoção, exceções, logging                             | Contributo direto              |
| **SSDF**      | RV.1.2, RV.2.3, RV.3.3                | Execução autorizada, rollback, logging e reversibilidade            | **✔️ RV.1.2, RV.2.3, RV.3.3** |
| **SLSA v1.0** | Provenance, Build Triggers            | Controlos de promoção e artefactos, validações                      | **Nível 2 / 4**                |
| **DSOMM**     | Design & Development                  | Deploy seguro, rastreabilidade, controlo formal de produção         | **4 / 5**                      |

---

## 🧱 OWASP SAMM - Verification → Security Testing

| Nível | Descrição SAMM                                | Implementação no Cap. 11                           |
|-------|------------------------------------------------|----------------------------------------------------|
| 1     | Validação manual antes de produção             | ✅ Checklist e gates de readiness                  |
| 2     | Automatização e rollback validado              | ✅ Rollback com validação integrada                |
| 3     | Controlo formalizado e política de exceções    | ✅ Justificação de deploy, bloqueio e auditoria    |

**🧮 Maturidade atingida: 3 / 3**

---

## 🧱 OWASP DSOMM - Deploy Seguro como Domínio Técnico

| Domínio               | Nível | Justificação técnica                                              |
|-----------------------|-------|-------------------------------------------------------------------|
| Design & Development  | 4 / 5 | Deploy seguro, rollback rastreável, controlo de exceções          |

---

## 🧱 NIST SSDF - Requisitos de Execução Autorizada

| Controlos NIST SSDF | Descrição                                      | Alinhamento com Cap. 11                  |
|---------------------|------------------------------------------------|------------------------------------------|
| RV.1.2              | Autorizar a execução                           | ✅ Validação de readiness e triggers      |
| RV.2.3              | Validar artefactos antes de produção           | ✅ Gates técnicos e revisão               |
| RV.3.3              | Controlar rollback e revalidação               | ✅ Processo reversível documentado        |

---

## 🧱 BSIMM - Práticas de Governança de Deployment

| Prática BSIMM | Alinhamento com Cap. 11                                         |
|---------------|------------------------------------------------------------------|
| SE2.5         | Exceções formais e registo de decisões                          |
| CMVM1.5       | Logging e auditoria do processo de deploy                       |
| CMVM2.4       | Aprovação e validação automatizada                              |

---

## 🧱 SLSA - Controlo de Build e Proveniência

| Nível | Requisitos principais                                      | Cobertura pelo Cap. 11                                |
|-------|------------------------------------------------------------|--------------------------------------------------------|
| 1     | Deploy controlado manualmente                              | ✅ Pré-condições e triggers definidos                  |
| 2     | Controlo de promoção e validação de artefactos             | ✅ Validação de release e rollback rastreável          |
| 3     | Validação de proveniência e runtime                        | ❌ Parcial - depende de integração com Cap. 07 e 12    |
| 4     | Controlo externo e sandboxing                              | ❌ Não abordado                                         |

**🔐 Nível máximo suportado por este capítulo: SLSA 2 / 4**

---

## ✅ Conclusão

- Este capítulo atinge **nível elevado de maturidade em SAMM, SSDF, DSOMM e BSIMM**, abordando formalização, rollback, controlo de promoção e rastreabilidade;
- A integração com Capítulos 07 (CI/CD) e 12 (Monitorização) pode reforçar o alinhamento com SLSA 3 e 4;
- A maturidade obtida é suficiente para ambientes produtivos de elevada exigência.
