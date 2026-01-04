---
id: achievable-maturity
title: Mapeamento de Maturidade - Capítulo 02
sidebar_position: 10
tags: [canon, maturidade, SAMM, SSDF, DSOMM, SLSA]
---

# 📈 Maturidade - Requisitos de Segurança

Este documento estabelece o **grau de alinhamento entre as práticas descritas no Capítulo 02** do manual SbD-ToE e os requisitos de frameworks reconhecidas: **OWASP SAMM**, **BSIMM**, **NIST SSDF**, **SLSA** e **OWASP DSOMM**.

A definição e validação de requisitos de segurança é um **pilar central na engenharia de software seguro**. Este capítulo fornece os mecanismos para garantir que os requisitos são proporcionais ao risco, rastreáveis, testáveis e auditáveis.

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
| SLSA             | Nível máximo suportado (ex: 1 de 4) | Modelo acumulativo, não gradual por domínio      |

As avaliações aqui descritas foram realizadas com base numa leitura técnico-científica de cada fonte original.

## 🧭 Visão Geral de Alinhamento

| Framework         | Domínios Relevantes                            | Práticas ou Objetos Cobertos                                        | Avaliação de Maturidade             |
|------------------|--------------------------------------------------|----------------------------------------------------------------------|-------------------------------------|
| OWASP SAMM v2.1  | Design → Security Requirements                  | Requisitos proporcionais, rastreáveis, com validação formal         | **2 / 3**                           |
| OWASP DSOMM      | Requirements, Architecture, Verification        | Catálogo validado, derivação por risco, critérios de aceitação      | **2 / 3** (média dos domínios)      |
| NIST SSDF v1.1   | PW.1, PW.4, RV.1                                 | Documentação, revisão e validação de requisitos                     | **✔️ PW.1, PW.4, RV.1**             |
| BSIMM13          | Requirements and Attack Models                  | Integração no backlog, rastreabilidade, critérios                   | Contributo parcial                  |
| SLSA v1.0        | Build, Verification, Criteria Definition         | Definição de critérios de aceitação com base em requisitos          | **Nível 1 / 4**                     |

---

## 🧱 OWASP SAMM - Design → Security Requirements

| Nível | Descrição SAMM                                                                 | Cobertura pelo Cap. 02                      |
|-------|----------------------------------------------------------------------------------|----------------------------------------------|
| 1     | Definir requisitos de segurança mínimos                                         | ✅ Catálogo estruturado por domínio          |
| 2     | Requisitos definidos com base em riscos                                         | ✅ Derivação por níveis L1–L3                |
| 3     | Requisitos ligados a métricas e controlos de eficácia                          | ❌ Fora do âmbito imediato                   |

**🧮 Maturidade atingida: 2 / 3**

---

## 🧱 OWASP DSOMM - Requirements, Architecture, Verification

| Domínio                  | Níveis cobertos | Justificação técnica                                                    |
|--------------------------|----------------|-------------------------------------------------------------------------|
| Requirements             | 2 / 3          | Requisitos testáveis, rastreáveis e validados                          |
| Architecture             | 2 / 3          | Mapeamento por risco e dependência com arquitetura                     |
| Verification             | 2 / 3          | Critérios definidos para validação dos requisitos                      |

> O capítulo fornece os alicerces para práticas maduras de definição e teste de requisitos, reutilizáveis por produto.

---

## 🧱 NIST SSDF - Produce Well-Secured Software & Review (PW, RV)

| Controlos NIST SSDF | Descrição                                     | Alinhamento com Cap. 02 |
|---------------------|-----------------------------------------------|--------------------------|
| PW.1                | Documentar requisitos de segurança            | ✅ Totalmente coberto    |
| PW.4                | Estabelecer critérios de segurança            | ✅ Coberto               |
| RV.1                | Rever requisitos com intervenientes técnicos  | ✅ Coberto               |
| RV.2                | Rever requisitos com partes interessadas      | ❌ Fora do âmbito        |

> A testabilidade e rastreabilidade dos requisitos são suportadas por práticas prescritivas com validação contínua.

---

## 🧱 BSIMM - Intelligence → Requirements and Attack Models

| Prática BSIMM       | Alinhamento com Cap. 02                                |
|---------------------|--------------------------------------------------------|
| AM1.1               | ✅ Requisitos baseados em análise de risco             |
| AM2.1               | ⚠️ Integração parcial com modelos de ameaça            |
| AM3.x               | ❌ Fora do âmbito técnico atual                         |

> A prática de requisitos integra-se diretamente no ciclo de backlog, suportando histórias e aceitação baseada em risco.

---

## 🧱 SLSA - Build & Verification Requirements

| Nível | Requisitos principais                     | Cobertura pelo Cap. 02              |
|-------|--------------------------------------------|-------------------------------------|
| 1     | Definição de critérios de validação        | ✅ Aplicação explícita de critérios |
| 2     | Proveniência e rastreabilidade             | ❌ Fora do âmbito                   |
| 3     | Verificação reforçada no pipeline          | ❌ Implementado noutros capítulos   |

**🔐 Nível máximo suportado por este capítulo: SLSA 1 / 4**

---

## ✅ Conclusão

- Este capítulo estabelece práticas **fundacionais de requisitos seguros**, rastreáveis e testáveis;
- Suporta **rastreabilidade completa entre risco, requisito, validação e aceitação**;
- Está alinhado com **SAMM 2/3**, **DSOMM média 2/3**, e **controlos SSDF PW.1, PW.4 e RV.1**;
- Permite às equipas integrar requisitos de segurança no backlog, testes e aceitação de produto.

---

## 📊 Sumário Consolidado de Alinhamento por Framework

| Framework         | Domínios Relevantes                            | Práticas ou Objetos Cobertos                                        | Avaliação de Maturidade             |
|------------------|--------------------------------------------------|----------------------------------------------------------------------|-------------------------------------|
| OWASP SAMM v2.1  | Design → Security Requirements                  | Requisitos proporcionais, rastreáveis, com validação formal         | **2 / 3**                           |
| OWASP DSOMM      | Requirements, Architecture, Verification        | Catálogo validado, derivação por risco, critérios de aceitação      | **2 / 3** (média dos domínios)      |
| NIST SSDF v1.1   | PW.1, PW.4, RV.1                                 | Documentação, revisão e validação de requisitos                     | **✔️ PW.1, PW.4, RV.1**             |
| BSIMM13          | Requirements and Attack Models                  | Integração no backlog, rastreabilidade, critérios                   | Contributo parcial                  |
| SLSA v1.0        | Build, Verification, Criteria Definition         | Definição de critérios de aceitação com base em requisitos          | **Nível 1 / 4**                     |
