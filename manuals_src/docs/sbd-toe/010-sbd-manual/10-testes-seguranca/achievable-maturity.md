---
id: achievable-maturity
title: Mapeamento de Maturidade – Capítulo 10
sidebar_position: 10
tags: [canon, maturidade, SAMM, BSIMM, SSDF, SLSA, DSOMM]
---

# 📈 Maturidade — Testes de Segurança

Este documento apresenta o **mapeamento de maturidade das práticas descritas no Capítulo 10 — Testes de Segurança**, com base nos principais frameworks de referência:

- **OWASP SAMM**
- **BSIMM**
- **NIST SSDF**
- **SLSA**
- **OWASP DSOMM**

As práticas abrangem testes automatizados (SAST, DAST, IAST), fuzzing, análise de resultados, rastreabilidade, gestão de findings, testes manuais (ex: PenTesting) e integração contínua no SDLC.

---

## 🎯 Como interpretar este mapeamento de maturidade

Este mapeamento avalia o **nível de completude e integração** das práticas prescritas no capítulo relativamente aos frameworks de referência. Cada avaliação segue o modelo próprio de maturidade da framework:

| Framework        | Avaliação usada                     | Justificação                                      |
|------------------|-------------------------------------|--------------------------------------------------|
| OWASP SAMM       | `n / 3`                             | Três níveis crescentes por domínio               |
| OWASP DSOMM      | `n / m`                             | Níveis por domínio técnico                       |
| NIST SSDF        | Lista de controlos cobertos         | Modelo binário e objetivo                        |
| BSIMM            | Lista de práticas observadas        | Modelo observacional, não prescritivo            |
| SLSA             | Nível acumulativo (1–4)             | Requisitos progressivos em cadeia de build/test  |

---

## 🧭 Visão Geral de Alinhamento

| Framework     | Domínios Relevantes                  | Práticas Cobertas                                                     | Avaliação de Maturidade        |
|---------------|---------------------------------------|------------------------------------------------------------------------|--------------------------------|
| **SAMM v2.1** | Verification → Security Testing       | Testes automatizados, gates de validação, gestão de findings          | **2 / 3**                      |
| **BSIMM13**   | SFD1, SE1, T1.3, T2.4, SE3.5          | Feedback automático, rastreabilidade, pentests                        | Contributo direto              |
| **SSDF**      | RV.1, RV.3, RV.6, PS.2                | Validação automatizada, fuzzing, evidência e análise                  | **✔️ RV.1, RV.3, RV.6, PS.2** |
| **SLSA v1.0** | Build/Test Coverage                   | Cobertura limitada, validação de artefactos antes de deploy           | **Nível 2 / 4**                |
| **DSOMM**     | Testing, Design & Development         | Integração contínua, rastreabilidade por release, gates automáticos   | **2 / 3**                      |

---

## 🧱 OWASP SAMM – Verification → Security Testing

| Nível | Descrição SAMM                                  | Cobertura pelo Cap. 10                                 |
|-------|--------------------------------------------------|--------------------------------------------------------|
| 1     | Testes manuais básicos de segurança              | ✅ Inclui Pentesting e casos adversariais manuais      |
| 2     | Integração de testes automatizados no pipeline   | ✅ SAST, DAST, fuzzing, cobertura e regressão          |
| 3     | Gestão ativa de findings e feedback contínuo     | ❌ Parcial — não garante formalização organizacional   |

**🧮 Maturidade atingida: 2 / 3**

---

## 🧱 OWASP DSOMM – Domínios Testing + Design & Development

| Domínio               | Nível | Justificação técnica                                              |
|-----------------------|-------|-------------------------------------------------------------------|
| Testing               | 2 / 3 | SAST/DAST integrados, fuzzing, feedback, gates                    |
| Design & Development  | 2 / 3 | Validação por release, controlo de findings, reporting técnico    |

---

## 🧱 NIST SSDF – Requisitos de Validação

| Controlos NIST SSDF | Descrição                                        | Alinhamento com Cap. 10                       |
|---------------------|--------------------------------------------------|-----------------------------------------------|
| RV.1                | Validar código e artefactos                      | ✅ Com SAST/DAST automáticos e análise manual |
| RV.3                | Gerir resultados e rastrear correções            | ✅ Via rastreabilidade e evidência             |
| RV.6                | Fuzzing, testes dinâmicos                        | ✅ Inclui fuzzing contínuo e testes adversariais |
| PS.2                | Planear e executar testes                        | ✅ Planeamento formal e rastreável             |

---

## 🧱 BSIMM – Práticas Observadas em Organizações Reais

| Prática BSIMM | Alinhamento com Cap. 10                                               |
|---------------|------------------------------------------------------------------------|
| SFD1.2        | Integração de SAST no ciclo de vida                                    |
| SE1.1         | Geração automática de resultados                                        |
| T1.3          | Validação ofensiva com objetivos definidos                             |
| T2.4          | Acompanhamento de findings e regressão                                 |
| SE3.5         | Feedback técnico a equipas de desenvolvimento                          |

---

## 🧱 SLSA – Build/Test Coverage

| Nível | Requisitos principais                                             | Cobertura pelo Cap. 10                                 |
|-------|------------------------------------------------------------------|--------------------------------------------------------|
| 1     | Execução de testes em CI                                         | ✅ Cobertura mínima via pipelines                      |
| 2     | Cobertura definida e evidência de testes                         | ✅ Evidência e análise rastreável                      |
| 3     | Cobertura exigida e enforcement                                  | ❌ Parcial — depende de governance                     |
| 4     | Testes e resultados com garantia de integridade                  | ❌ Não abrangido pelo capítulo                         |

**🔐 Nível máximo suportado por este capítulo: SLSA 2 / 4**

---

## ✅ Conclusão

- As práticas deste capítulo permitem atingir um **nível elevado de maturidade técnica** em segurança da validação;
- Existe uma forte integração no SDLC com evidência, feedback e rastreabilidade contínua;
- O capítulo serve de base robusta para ambientes CI/CD com validação automatizada e gestão de riscos técnicos.
