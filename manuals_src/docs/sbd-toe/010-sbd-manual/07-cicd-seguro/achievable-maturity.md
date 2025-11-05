---
id: achievable-maturity
title: Mapeamento de Maturidade – Capítulo 07
sidebar_position: 10
tags: [canon, maturidade, SAMM, BSIMM, SSDF, SLSA, DSOMM]
---

# 📈 Maturidade - CI/CD Seguro

Este documento apresenta o mapeamento entre as práticas descritas no Capítulo 07 do SbD-ToE - *CI/CD Seguro* - e os principais frameworks de segurança e maturidade:

- **OWASP SAMM**
- **BSIMM**
- **NIST SSDF**
- **SLSA**
- **OWASP DSOMM**

O capítulo define práticas para proteger pipelines CI/CD contra execução não autorizada, adulteração, perda de proveniência e outras ameaças à cadeia de fornecimento de software.

---

## 🎯 Como interpretar este mapeamento de maturidade

Este mapeamento **não mede a maturidade da organização**, mas sim o **nível de completude e rigor das práticas prescritas no capítulo**, face aos critérios dos frameworks reconhecidos.

| Framework        | Avaliação usada                     | Justificação                                      |
|------------------|-------------------------------------|--------------------------------------------------|
| OWASP SAMM       | `n / 3`                             | Framework prescritiva com 3 níveis por domínio   |
| OWASP DSOMM      | `n / m` (até 4)                     | Domínios com níveis formais                      |
| NIST SSDF        | Lista de controlos cobertos         | Modelo binário, sem níveis formais               |
| BSIMM            | Lista de práticas cobertas          | Modelo observacional, não prescritivo            |
| SLSA             | Nível máximo suportado (ex: 3 de 4) | Modelo acumulativo, objetivo e progressivo       |

---

## 🧭 Visão Geral de Alinhamento

| Framework         | Domínios Relevantes                              | Práticas ou Objetos Cobertos                                                  | Avaliação de Maturidade        |
|------------------|---------------------------------------------------|--------------------------------------------------------------------------------|--------------------------------|
| OWASP SAMM v2.1  | Implementation → Build & Deployment Automation    | Segurança integrada no pipeline, segregação de ambientes                      | **2 / 3**                      |
| OWASP DSOMM      | Build, Test, Release, Operate                     | Execução segura, validação de artefactos, assinaturas, rastreabilidade        | **3 / 4**                      |
| NIST SSDF v1.1   | PW.4–7, PS.3, RV.3, GV.2–3                        | Execução autenticada, revisões, provenance, configurações seguras             | **✔️ PW.4–7, PS.3, RV.3, GV.2–3** |
| BSIMM13          | Software Environment, Compliance & Policy         | Rastreabilidade, aprovação automática, segregação, repositórios de confiança  | Contributo direto              |
| SLSA v1.0        | Levels 1–3: Provenance, Policy, Isolation         | Proveniência, trusted builders, controlo de execução, hardening de pipelines  | **Nível 3 / 4**                |

---

## 🧱 OWASP SAMM – Build & Deployment Automation

| Nível | Descrição SAMM                                                  | Cobertura pelo Cap. 07                                  |
|-------|------------------------------------------------------------------|----------------------------------------------------------|
| 1     | Processos de build manuais e não auditáveis                     | ✅ Formalização mínima exigida                           |
| 2     | Pipelines automatizadas com validações e autenticação           | ✅ Execução autenticada e validada                       |
| 3     | Ambientes segregados com integração de controlos contínuos      | ❌ Parcial - depende de controlo externo à pipeline      |

**🧮 Maturidade atingida: 2 / 3**

---

## 🧱 OWASP DSOMM – Build, Test, Release, Operate

| Domínio  | Nível | Justificação técnica                                              |
|----------|-------|-------------------------------------------------------------------|
| Build    | 3 / 4 | Execução autenticada, trusted runners, proveniência               |
| Test     | 3 / 4 | Validação e rastreabilidade contínua dos resultados               |
| Release  | 3 / 4 | Assinatura e integridade do artefacto                             |
| Operate  | 3 / 4 | Logs, auditoria e controlo de fluxo CI/CD                         |

---

## 🧱 NIST SSDF – Pipeline e Proveniência

| Controlos NIST SSDF | Descrição                                           | Alinhamento com Cap. 07               |
|---------------------|-----------------------------------------------------|----------------------------------------|
| PW.4–PW.7           | Automatizar builds e gerir configurações seguras    | ✅ Pipelines seguras e controladas     |
| PS.3                | Validar proveniência e integridade de componentes   | ✅ Assinaturas e trusted sources        |
| RV.3                | Validar comportamento antes da publicação            | ✅ Etapas de validação formalizadas     |
| GV.2–GV.3           | Governação e rastreabilidade                        | ✅ Logs e segregação rastreável         |

---

## 🧱 BSIMM – Software Environment, Compliance

| Prática BSIMM   | Alinhamento com Cap. 07                                        |
|-----------------|----------------------------------------------------------------|
| CMVM1.3         | Automatizar enforcement de requisitos                          |
| SE2.5           | Rastreabilidade completa no ambiente CI/CD                     |
| CP1.2           | Política de segregação e isolamento                            |

---

## 🧱 SLSA – Provenance & CI/CD Control

| Nível | Requisitos principais                                  | Cobertura pelo Cap. 07                              |
|-------|---------------------------------------------------------|-----------------------------------------------------|
| 1     | Build controlado e rastreável                           | ✅ Execução autenticada com logs                    |
| 2     | Proveniência e controlo de configuração                 | ✅ Validação e assinatura de artefactos             |
| 3     | Builds reprodutíveis e trusted builders                 | ✅ Trusted environments e runners                   |
| 4     | Isolamento hermético e verificações externas            | ❌ Fora do escopo do capítulo (ver Cap. 08 e 09)    |

**🔐 Nível máximo suportado por este capítulo: SLSA 3 / 4**

---

## ✅ Conclusão

- O Capítulo 07 fornece práticas robustas para segurança de pipelines CI/CD;
- Está alinhado com maturidade **2/3** (SAMM), **3/4** (DSOMM e SLSA), e cobre integralmente controlos relevantes no **SSDF**;
- Ajuda a estabelecer rastreabilidade, integridade e governação em ambientes de automação contínua;
- Suporta organizações que pretendem atingir conformidade com práticas de *secure delivery pipeline* em DevSecOps.
