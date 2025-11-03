---
id: achievable-maturity
title: Mapeamento de Maturidade – Capítulo 01
tags: [canon, maturidade, SAMM, SSDF, BSIMM, DSOMM]
---

# 📈 Maturidade — Classificação da Criticidade Aplicacional

Este documento estabelece o **grau de alinhamento entre as práticas descritas no Capítulo 01** do manual SbD-ToE e os requisitos de frameworks reconhecidas: **OWASP SAMM**, **BSIMM**, **NIST SSDF**, **SLSA** e **OWASP DSOMM**.

A prática de classificação da criticidade aplicacional é **fundacional para o modelo SbD-ToE**. Ela define **quando e com que intensidade os controlos de segurança devem ser aplicados**, suportando uma abordagem proporcional, rastreável e auditável.

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

| Framework         | Domínios Relevantes                         | Práticas ou Objetos Cobertos                                  | Avaliação de Maturidade             |
|------------------|----------------------------------------------|----------------------------------------------------------------|-------------------------------------|
| OWASP SAMM v2.1  | Governance → Risk Management                 | Classificação de risco por eixos, integração no SDLC           | **2 / 3**                           |
| OWASP DSOMM      | Risk, Security Requirements, Compliance      | Derivação de requisitos, rastreabilidade, decisão proporcional | **2 / 3** (média dos domínios)      |
| NIST SSDF v1.1   | RM.1, RM.2                                   | Classificação e avaliação de risco                             | **✔️ RM.1, RM.2**                   |
| BSIMM13          | Strategy and Metrics                         | SR1.1, SR1.5: decisão por criticidade                          | Contributo parcial, SR2 fora do escopo |
| SLSA v1.0        | Supply Chain Risk Awareness                  | Definição proporcional de requisitos à criticidade             | **Nível 1 / 4**                     |

---

## 🧱 OWASP SAMM – Governance → Risk Management

| Nível | Descrição SAMM                                                           | Cobertura pelo Cap. 01                  |
|-------|--------------------------------------------------------------------------|------------------------------------------|
| 1     | Realiza-se classificação básica dos riscos das aplicações                | ✅ Modelo de eixos aplicável             |
| 2     | Integração com processos organizacionais e rastreabilidade               | ✅ Com suporte a versão e auditoria      |
| 3     | Análise quantitativa e retroalimentação contínua                         | ❌ Fora do escopo do capítulo            |

**🧮 Maturidade atingida: 2 / 3**

---

## 🧱 OWASP DSOMM – Governance, Risk Management, Requirements

| Domínio                  | Níveis cobertos | Justificação técnica                                                   |
|--------------------------|----------------|------------------------------------------------------------------------|
| Risk Management          | 2 / 3          | Modelo de classificação estruturado e aplicado sistematicamente       |
| Security Requirements    | 2 / 3          | Permite derivação proporcional baseada em risco                       |
| Compliance Mapping       | 2 / 3          | Rastreabilidade a frameworks de referência presente                    |
| Governance & Metrics     | 1 / 3          | Não define KPIs quantitativos nem reporting formal                     |

> A estrutura proposta é compatível com práticas DevSecOps guiadas por risco.

---

## 🧱 NIST SSDF – Risk Management (RM)

| Controlos NIST SSDF | Descrição                                             | Alinhamento com Cap. 01 |
|---------------------|--------------------------------------------------------|--------------------------|
| RM.1                | Classificar software por criticidade                   | ✅ Totalmente coberto    |
| RM.2                | Avaliar o risco de segurança associado ao software     | ✅ Coberto               |
| RM.3                | Gerir riscos identificados                             | ❌ Fora do escopo        |

> O capítulo cobre os primeiros passos (classificação e avaliação), deixando a gestão para outros capítulos (ex: mitigação).

---

## 🧱 BSIMM – Strategy and Metrics

| Prática BSIMM       | Alinhamento com Cap. 01                                |
|---------------------|--------------------------------------------------------|
| SR1.1               | ✅ Classificação suporta decisões de segurança          |
| SR1.5               | ✅ Avaliação de criticidade incorporada                 |
| SR2.x               | ❌ Não são cobertas práticas de medição/benchmarking    |

> A abordagem SbD-ToE foca-se em práticas operacionais integradas no ciclo de vida, não em métricas organizacionais agregadas.

---

## 🧱 SLSA – Supply Chain Levels for Software Artifacts

| Nível | Requisitos principais                   | Cobertura pelo Cap. 01         |
|-------|------------------------------------------|--------------------------------|
| 1     | Consciência de risco                     | ✅ Classificação por eixos      |
| 2     | Proveniência do software                 | ❌ Fora do escopo               |
| 3     | Build controlado                         | ❌ Coberto noutros capítulos    |
| 4     | Cadeia totalmente verificável            | ❌ Coberto noutros capítulos    |

**🔐 Nível máximo suportado por este capítulo: SLSA 1 / 4**

---

## ✅ Conclusão

- O Capítulo 01 atinge **nível 2/3 em SAMM e DSOMM**, e **alinha-se diretamente com RM.1 e RM.2 do SSDF**;
- A prática de classificação **é pré-condição para controlos proporcionais e justificados** nos restantes capítulos;
- Constitui um mecanismo de rastreabilidade entre risco, requisitos, validações e políticas;
- Não substitui frameworks formais de análise de risco regulada, mas é compatível com **ISO 27005, NIST 800-30**, entre outras.
