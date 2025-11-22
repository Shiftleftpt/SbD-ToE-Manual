---
id: achievable-maturity
title: Mapeamento de Maturidade - Capítulo 04
sidebar_position: 10
tags: [DSOMM, SAMM, SLSA, SSDF, canon, maturidade]
---

# 📈 Maturidade - Arquitetura Segura

Este documento estabelece o **grau de alinhamento entre as práticas descritas no Capítulo 04** do manual SbD-ToE e os requisitos das principais frameworks de segurança e maturidade:

- **OWASP SAMM**
- **BSIMM**
- **NIST SSDF**
- **SLSA**
- **OWASP DSOMM**

O capítulo propõe uma abordagem prescritiva à definição e validação de arquiteturas seguras, com base em requisitos formais (`ARC-001` a `ARC-011`), segmentação por zonas de confiança, princípios de defesa em profundidade e critérios de rastreabilidade e exceção.

---

## 🎯 Como interpretar este mapeamento de maturidade

Este documento **não mede a maturidade de uma organização**, mas sim o **grau de cobertura que as práticas deste capítulo oferecem relativamente às frameworks de referência**.

### Tipos de Avaliação Utilizados

| Framework        | Avaliação usada                     | Justificação                                      |
|------------------|-------------------------------------|--------------------------------------------------|
| OWASP SAMM       | `n / 3`                             | Framework prescritiva com 3 níveis por domínio   |
| OWASP DSOMM      | `n / m` (até 4)                     | Domínios com níveis formais                      |
| NIST SSDF        | Lista de controlos cobertos         | Modelo binário, sem níveis formais               |
| BSIMM            | Lista de práticas cobertas          | Modelo observacional, não prescritivo            |
| SLSA             | Nível máximo suportado (ex: 2 de 4) | Modelo acumulativo, não gradual por domínio      |

---

## 🧭 Visão Geral de Alinhamento

| Framework         | Domínios Relevantes                    | Práticas ou Objetos Cobertos                                       | Avaliação de Maturidade          |
|------------------|-----------------------------------------|--------------------------------------------------------------------|----------------------------------|
| OWASP SAMM v2.1  | Design → Architecture & Design          | Princípios formais, validação e documentação da arquitetura          | **2 / 3**                        |
| OWASP DSOMM      | Architecture, Risk, Requirements         | Requisitos `ARC-XXX`, rastreabilidade, zonas de confiança          | **3 / 4** (média dos domínios)   |
| NIST SSDF v1.1   | PW.4, PW.7                              | Revisão da arquitetura formal, validação de segurança                | **✔️ PW.4, PW.7**                |
| BSIMM13          | Architecture Analysis (AA1, AA2), CMVM  | Validação da arquitetura, gestão de exceções                         | Contributo relevante             |
| SLSA v1.0        | Build System, Provenance                | Segmentação e isolamento da arquitetura                              | **Nível 2 / 4**                  |

---

## 🧱 OWASP SAMM - Design → Architecture & Design

| Nível | Descrição SAMM                                             | Cobertura pelo Cap. 04                              |
|-------|------------------------------------------------------------|-----------------------------------------------------|
| 1     | Arquitetura definida informalmente                         | ✅ Requisitos mínimos `ARC-001` a `ARC-004`         |
| 2     | Documentação com validação proporcional                    | ✅ Validação rastreável, zonas de confiança         |
| 3     | Integração contínua e revisão automatizada                 | ❌ Fora do escopo (requer automação e pipelines)    |

**🧮 Maturidade atingida: 2 / 3**

---

## 🧱 OWASP DSOMM - Architecture, Requirements, Risk

| Domínio       | Níveis cobertos | Justificação técnica                                               |
|---------------|----------------|----------------------------------------------------------------------|
| Architecture  | 3 / 4          | Segmentação, zonas de confiança, tratamento explícito               |
| Requirements  | 3 / 4          | Requisitos formais por tipo de componente (`ARC-XXX`)               |
| Risk Analysis | 3 / 4          | Integração com threat modeling e aceitação de risco por exceção     |

> O capítulo cobre a maioria dos aspetos de arquitetura relevantes à segurança em ambientes modernos.

---

## 🧱 NIST SSDF - Design Review and Architecture

| Controlos NIST SSDF | Descrição                                         | Alinhamento com Cap. 04 |
|---------------------|---------------------------------------------------|--------------------------|
| PW.4                | Rever design quanto à segurança                   | ✅ Com base nos requisitos `ARC` |
| PW.7                | Avaliar riscos associados à arquitetura           | ✅ Via threat modeling + zonas de confiança |

---

## 🧱 BSIMM - Architecture & CMVM

| Prática BSIMM   | Alinhamento com Cap. 04                                         |
|-----------------|-----------------------------------------------------------------|
| AA1.2           | Técnicas de arquitetura para reduzir risco                       |
| AA2.1           | Avaliação formal da arquitetura                                 |
| CMVM1.1         | Definição de zonas de confiança e exceções                      |

> O capítulo fornece práticas que contribuem diretamente para análise da arquitetura e gestão de exceções.

---

## 🧱 SLSA - Provenance & Isolation

| Nível | Requisitos principais                          | Cobertura pelo Cap. 04                  |
|-------|-------------------------------------------------|-----------------------------------------|
| 1     | Princípios básicos de isolamento                | ✅ Segmentação e zonas de confiança      |
| 2     | Arquitetura formal com proveniência             | ✅ Requisitos documentados               |
| 3–4   | Cadeias verificáveis, builds isolados           | ❌ Fora do escopo (ver Cap. 06 e 08)     |

**🔐 Nível máximo suportado por este capítulo: SLSA 2 / 4**

---

## ✅ Conclusão

- O Capítulo 04 estabelece uma base sólida para a arquitetura segura, com requisitos formais, rastreabilidade e validação;
- Alinha-se fortemente com **SAMM (2/3)**, **DSOMM (3/4)**, **SSDF (PW.4, PW.7)** e **BSIMM (AA, CMVM)**;
- Permite decisões justificadas com base em princípios de arquitetura reconhecidos e aplicáveis a diferentes domínios de risco;
- Suporta práticas modernas de segurança por design com aplicabilidade direta a ambientes regulados ou críticos.

---

## 📊 Sumário Consolidado de Alinhamento por Framework

| Framework         | Domínios Relevantes                    | Práticas ou Objetos Cobertos                                       | Avaliação de Maturidade          |
|------------------|-----------------------------------------|--------------------------------------------------------------------|----------------------------------|
| OWASP SAMM v2.1  | Design → Architecture & Design          | Princípios formais, validação e documentação da arquitetura          | **2 / 3**                        |
| OWASP DSOMM      | Architecture, Risk, Requirements         | Requisitos `ARC-XXX`, rastreabilidade, zonas de confiança          | **3 / 4** (média dos domínios)   |
| NIST SSDF v1.1   | PW.4, PW.7                              | Revisão da arquitetura formal, validação de segurança                | **✔️ PW.4, PW.7**                |
| BSIMM13          | Architecture Analysis (AA1, AA2), CMVM  | Validação da arquitetura, gestão de exceções                         | Contributo relevante             |
| SLSA v1.0        | Build System, Provenance                | Segmentação e isolamento da arquitetura                              | **Nível 2 / 4**                  |
