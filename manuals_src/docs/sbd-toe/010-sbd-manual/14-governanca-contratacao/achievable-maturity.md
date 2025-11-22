---
id: achievable-maturity
title: Mapeamento de Maturidade - Capítulo 14
sidebar_position: 10
tags: [canon, maturidade, SAMM, SSDF, SLSA, DSOMM]
---

# 📈 Maturidade - Governança e Contratação

Este documento apresenta o **mapeamento de maturidade das práticas descritas no Capítulo 14 - Governança e Contratação**, com base nos principais frameworks de referência:

- **OWASP SAMM**
- **BSIMM**
- **NIST SSDF**
- **SLSA**
- **OWASP DSOMM**

As práticas cobrem papéis críticos, exceções, contratos, rastreabilidade organizacional, onboarding e validação de fornecedores, métricas e integração com modelos de maturidade.

---

## 🎯 Como interpretar este mapeamento de maturidade

| Framework        | Avaliação usada                     | Justificação                                      |
|------------------|-------------------------------------|--------------------------------------------------|
| OWASP SAMM       | `n / 3`                             | Níveis progressivos por domínio                  |
| OWASP DSOMM      | `n / m`                             | Maturidade por domínio técnico                   |
| NIST SSDF        | Lista de controlos cumpridos        | Avaliação objetiva e cumulativa                  |
| BSIMM            | Práticas observadas                 | Foco empírico nas atividades                     |
| SLSA             | Nível cumulativo (1–4)              | Aplicável à cadeia de fornecimento               |

---

## 🧭 Visão Geral de Alinhamento

| Framework     | Domínios Relevantes                      | Práticas Cobertas                                          | Avaliação de Maturidade                          |
|---------------|-------------------------------------------|-------------------------------------------------------------|--------------------------------------------------|
| **SAMM v2.1** | Governance, Education, Incident Management | Ownership, exceções, rastreabilidade, formação             | **2 / 3**                                        |
| **BSIMM13**   | Governance & Compliance                   | Formalização de exceções, cláusulas contratuais, reviewers  | **SE2, CP1**                                     |
| **SSDF**      | PO.1, PO.3, RV.1, RV.2                    | Papéis críticos, requisitos formais, onboarding, validação | **Completamente coberto**                        |
| **SLSA v1.0** | Supply Chain Governance                   | Requisitos contratuais, aceitação de risco, rastreabilidade| **Contributo indireto - Nível 2 / 4**            |
| **DSOMM**     | Governance, 3rd Party, Tooling, Training, Metrics | Exceções, KPIs, onboarding, validação, maturidade       | **4 / 5**                                        |

---

## 🧱 OWASP SAMM - Governance e Education

| Domínio               | Nível | Implementação no Cap. 14                                 |
|-----------------------|-------|----------------------------------------------------------|
| Governance            | 2 / 3 | Papéis definidos, exceções formais, contratos seguros    |
| Education & Guidance  | 2 / 3 | Formação de fornecedores e rastreio organizacional       |
| Incident Management   | 1 / 3 | Parciais - rastreabilidade e canais de reporte definidos |

---

## 🧱 OWASP DSOMM

| Domínio         | Nível | Justificação técnica                                               |
|------------------|-------|--------------------------------------------------------------------|
| Governance       | 3 / 3 | Definição clara de ownership, políticas, controlo contínuo         |
| 3rd Party        | 4 / 4 | Validação de fornecedores, requisitos contratuais, rastreabilidade |
| Tooling & Metrics| 4 / 5 | KPIs de governação e feedback contínuo                             |
| Training         | 3 / 3 | Onboarding formal de stakeholders                                 |

---

## 🧱 NIST SSDF - Controlos Cumpridos

| Controlos NIST SSDF | Descrição                                       | Alinhamento com Cap. 14                    |
|---------------------|--------------------------------------------------|--------------------------------------------|
| PO.1.1              | Definir responsabilidades                        | ✅ Ownership por perfil                     |
| PO.3.1              | Estabelecer critérios de aceitação               | ✅ Exceções e cláusulas contratuais         |
| RV.1.1              | Verificar conformidade de terceiros              | ✅ Validação de fornecedores                |
| RV.2.2              | Rastrear decisões de risco                       | ✅ Processo de exceções e aceitação formal  |

---

## 🧱 BSIMM - Governance & Compliance

| Prática BSIMM | Alinhamento com Cap. 14                                       |
|---------------|---------------------------------------------------------------|
| SE2           | Processo formal de exceções e aceitação de risco              |
| CP1           | Inclusão de requisitos e cláusulas nos contratos de software  |

---

## 🧱 SLSA - Supply Chain

| Nível | Requisitos principais                            | Cobertura pelo Cap. 14                       |
|-------|--------------------------------------------------|----------------------------------------------|
| 1     | Cadeia de fornecimento minimamente identificada  | ✅ Papéis e terceiros registados              |
| 2     | Requisitos contratuais definidos                 | ✅ Cláusulas de segurança formais             |
| 3     | Verificação independente                         | ❌ Parcial - validações sem atestado externo |
| 4     | Governação contínua e auditável                  | ❌ Não aplicável                             |

**🔐 Nível suportado por este capítulo: SLSA 2 / 4**

---

## ✅ Conclusão

- As práticas descritas posicionam a organização com **maturidade elevada em SAMM, SSDF e DSOMM**, com forte contributo para BSIMM e SLSA;
- O modelo prescrito é diretamente aplicável a ambientes com fornecedores críticos, contratos sensíveis e requisitos regulatórios;
- Serve de alicerce para suportar a segurança organizacional e a rastreabilidade de decisões estratégicas.
