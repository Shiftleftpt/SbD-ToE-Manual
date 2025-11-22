---
id: achievable-maturity
sidebar_position: 10
tags:
- DSOMM
- SAMM
- SLSA
- SSDF
- canon
- dsomm
- maturidade
title: Mapeamento de Maturidade - Capítulo 08
---


# 📈 Maturidade - Infraestrutura como Código (IaC)

Este documento estabelece o **alinhamento entre as práticas descritas no Capítulo 08** do manual SbD-ToE e os domínios equivalentes nos principais frameworks de segurança e maturidade de software:

- **OWASP SAMM**
- **BSIMM**
- **NIST SSDF**
- **SLSA**
- **OWASP DSOMM**

As práticas visam garantir que projetos IaC sejam tratados como **produtos de software seguros**, com requisitos, validações, rastreabilidade e governação - totalmente integrados no ciclo de desenvolvimento e operação.

---

## 🎯 Como interpretar este mapeamento de maturidade

O objetivo deste mapeamento é demonstrar **completude e maturidade das práticas prescritas no capítulo**, e não avaliar a organização em si. Cada framework é interpretado segundo o seu modelo nativo:

| Framework        | Avaliação usada                     | Justificação                                      |
|------------------|-------------------------------------|--------------------------------------------------|
| OWASP SAMM       | `n / 3`                             | Níveis por domínio (modelo prescritivo)          |
| OWASP DSOMM      | `n / m`                             | Níveis formais por domínio técnico               |
| NIST SSDF        | Lista de controlos cobertos         | Controlo binário (não gradativo)                 |
| BSIMM            | Lista de práticas observadas        | Framework observacional, não prescritivo         |
| SLSA             | Nível acumulativo (1–4)             | Modelo progressivo por artefacto                 |

---

## 🧭 Visão Geral de Alinhamento

| Framework         | Domínios Relevantes                               | Práticas ou Objetos Cobertos                                                    | Avaliação de Maturidade        |
|------------------|----------------------------------------------------|----------------------------------------------------------------------------------|--------------------------------|
| OWASP SAMM v2.1  | Implementation → Secure Build                      | Controlo de pipelines IaC, linting, enforcement                                | **2 / 3**                      |
| OWASP DSOMM      | Design & Development, Build & Test, Tooling        | Validação, segregação de ambientes, controlo de estado                          | **3 / 4**                      |
| NIST SSDF v1.1   | PW.5, CM.1, PS.2, PW.6                              | Configuração segura, validação, rastreabilidade e enforcement                   | **✔️ PW.5, CM.1, PS.2, PW.6** |
| BSIMM13          | Configuration Management, Compliance               | Versionamento, gestão de ambientes, controlo de exceções                       | Contributo relevante           |
| SLSA v1.0        | Source L2, Build L2, Provenance, Policy Enforcement| Validação de planos, proveniência, segregação, controlo de builds               | **Nível 2 / 4**                |

---

## 🧱 OWASP SAMM - Secure Build para IaC

| Nível | Descrição SAMM                                       | Cobertura pelo Cap. 08                              |
|-------|-------------------------------------------------------|-----------------------------------------------------|
| 1     | Configuração manual, sem rastreabilidade              | ❌ Fora do escopo - prática não recomendada         |
| 2     | Uso de linters, controlo automatizado e pipelines     | ✅ Validadores de IaC e enforcement automatizado    |
| 3     | Integração contínua com artefactos rastreáveis        | ❌ Parcial - depende do ecossistema DevOps          |

**🧮 Maturidade atingida: 2 / 3**

---

## 🧱 OWASP DSOMM - Aplicação a Projetos IaC

| Domínio             | Nível | Justificação técnica                                               |
|---------------------|-------|--------------------------------------------------------------------|
| Design & Dev        | 3 / 4 | Requisitos IaC, separação de ambientes, arquitetura segura         |
| Build & Test        | 3 / 4 | Linting, validação de planos, pipelines de teste                   |
| Tooling             | 3 / 4 | Ferramentas de análise estática e validação automatizada           |

---

## 🧱 NIST SSDF - Validação e Governação de IaC

| Controlos NIST SSDF | Descrição                                         | Alinhamento com Cap. 08         |
|---------------------|---------------------------------------------------|----------------------------------|
| PW.5                | Gestão segura de ficheiros e versões IaC          | ✅ Repositórios versionados      |
| PW.6                | Definição de configurações seguras                | ✅ Separação de ambientes         |
| CM.1                | Controlo e revisão de alterações                  | ✅ Validação de planos e deltas   |
| PS.2                | Práticas seguras de escrita de código             | ✅ Enforcement e linting          |

---

## 🧱 BSIMM - Gestão de Configuração e Compliance

| Prática BSIMM   | Alinhamento com Cap. 08                                      |
|-----------------|--------------------------------------------------------------|
| CMVM1.1         | Versionamento e gestão formal de ficheiros IaC               |
| CMVM2.3         | Validação automática de alterações de infraestrutura         |
| CP1.2           | Rastreabilidade e controlo de exceções em ambientes          |

---

## 🧱 SLSA - Fonte, Build e Proveniência

| Nível | Requisitos principais                                      | Cobertura pelo Cap. 08                              |
|-------|-------------------------------------------------------------|-----------------------------------------------------|
| 1     | Proveniência básica e controle manual                      | ✅ Validadores e aprovação manual formal             |
| 2     | Proveniência verificável e trusted source control          | ✅ Controlo de planos e ambientes                    |
| 3     | Build reprodutível, assinaturas, isolamento de ambiente    | ❌ Fora do escopo deste capítulo                     |
| 4     | Reprovação por auditor externo e sandboxing total          | ❌ Fora do escopo deste capítulo                     |

**🔐 Nível máximo suportado por este capítulo: SLSA 2 / 4**

---

## ✅ Conclusão

- Este capítulo posiciona os projetos IaC como objetos de segurança equivalentes a software;
- Cobre integralmente práticas de versionamento, validação, segregação e enforcement;
- Alinha-se com maturidade **2/3 (SAMM)**, **3/4 (DSOMM)** e **2/4 (SLSA)**;
- As práticas são compatíveis com pipelines modernos de DevOps e compliance regulatório (SSDF).
