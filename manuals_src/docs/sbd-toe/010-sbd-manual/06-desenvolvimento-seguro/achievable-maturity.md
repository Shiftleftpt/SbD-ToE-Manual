---
id: achievable-maturity
<<<<<<< HEAD
=======
title: Mapeamento de Maturidade - Capítulo 06
>>>>>>> master
sidebar_position: 10
tags:
- DSOMM
- SAMM
- SLSA
- SSDF
- canon
- dsomm
- maturidade
title: Mapeamento de Maturidade - Capítulo 06
---


# 📈 Maturidade - Desenvolvimento Seguro

Este documento apresenta o grau de alinhamento entre as práticas descritas no Capítulo 06 do SbD-ToE - *Desenvolvimento Seguro* - e os principais frameworks de segurança e maturidade de software:

- **OWASP SAMM**
- **BSIMM**
- **NIST SSDF**
- **SLSA**
- **OWASP DSOMM**

O capítulo foca-se na adoção de práticas seguras no desenvolvimento, validação contínua do código, rastreabilidade de decisões técnicas e políticas formais de exceção e ownership, garantindo evidência auditável da aplicação das boas práticas.

---

## 🎯 Como interpretar este mapeamento de maturidade

Este mapeamento **não avalia equipas ou organizações**, mas sim o **grau de completude e maturidade das práticas descritas no capítulo**, com base em critérios de frameworks amplamente adotadas.

| Framework        | Avaliação usada                     | Justificação                                      |
|------------------|-------------------------------------|--------------------------------------------------|
| OWASP SAMM       | `n / 3`                             | Framework prescritiva com 3 níveis por domínio   |
| OWASP DSOMM      | `n / m` (até 4)                     | Domínios com níveis formais                      |
| NIST SSDF        | Lista de controlos cobertos         | Modelo binário, sem níveis formais               |
| BSIMM            | Lista de práticas cobertas          | Modelo observacional, não prescritivo            |
| SLSA             | Nível máximo suportado (ex: 2 de 4) | Modelo acumulativo, não gradual por domínio      |

---

## 🧭 Visão Geral de Alinhamento

| Framework         | Domínios Relevantes                             | Práticas ou Objetos Cobertos                                              | Avaliação de Maturidade        |
|------------------|--------------------------------------------------|---------------------------------------------------------------------------|--------------------------------|
| OWASP SAMM v2.1  | Implementation → Secure Build / Verification     | Linters, validação automática, rastreabilidade, PR validation             | **2 / 3**                      |
| OWASP DSOMM      | Design & Development, Tooling, Metrics           | Práticas estruturadas, validações automáticas, evidência e ownership      | **2 / 3**                      |
| NIST SSDF v1.1   | PS.1–2, RV.1–2, PO.2                             | Secure coding, validações, documentação e rastreabilidade                 | **✔️ PS.1, PS.2, RV.1, RV.2, PO.2** |
| BSIMM13          | Code Review, Compliance & Policy, SE2            | Revisão de código, exceções formais, ownership rastreável                 | Contributo direto              |
| SLSA v1.0        | Provenance, Build Integrity                      | Integração de validações e proveniência no build                          | **Nível 2 / 4**                |

---

## 🧱 OWASP SAMM - Implementation

| Nível | Descrição SAMM                                      | Cobertura pelo Cap. 06                           |
|-------|------------------------------------------------------|--------------------------------------------------|
| 1     | Práticas básicas de verificação manual              | ✅ Revisão de código e boas práticas             |
| 2     | Integração de validações automatizadas no pipeline  | ✅ SAST, linters, PR validation                  |
| 3     | Integração contínua e testes estruturados           | ❌ Parcial - Cap. foca-se em boas práticas, não test coverage |

**🧮 Maturidade atingida: 2 / 3**

---

## 🧱 OWASP DSOMM - Design & Development, Tooling, Metrics

| Domínio         | Nível | Justificação técnica                                              |
|------------------|-------|-------------------------------------------------------------------|
| Design & Dev     | 2 / 3 | Práticas estruturadas de desenvolvimento seguro                  |
| Tooling          | 2 / 3 | Linters, validações automáticas integráveis                      |
| Metrics          | 2 / 3 | Rastreabilidade, evidência, ownership e tratamento de exceções   |

---

## 🧱 NIST SSDF - Desenvolvimento e Verificação

| Controlos NIST SSDF | Descrição                                          | Alinhamento com Cap. 06 |
|---------------------|----------------------------------------------------|--------------------------|
| PS.1                | Estabelecer práticas seguras de codificação        | ✅ Checklists e validação formal     |
| PS.2                | Formar equipas em práticas seguras                 | ✅ Formação e documentação            |
| RV.1                | Verificar código continuamente                     | ✅ Linters e validação no pipeline    |
| RV.2                | Remediar vulnerabilidades identificadas            | ✅ Tracking de findings e exceções    |
| PO.2                | Governação e papéis de responsabilidade técnica    | ✅ Ownership rastreável               |

---

## 🧱 BSIMM - Code Review, Policy & Ownership

| Prática BSIMM   | Alinhamento com Cap. 06                                 |
|-----------------|---------------------------------------------------------|
| SE2.3           | Aplicar regras de revisão seguras                       |
| SE2.4           | Automatizar políticas de validação                      |
| CP1.1           | Definir papéis formais e exceções rastreáveis           |

---

## 🧱 SLSA - Build Validation & Provenance

| Nível | Requisitos principais                               | Cobertura pelo Cap. 06                       |
|-------|------------------------------------------------------|----------------------------------------------|
| 1     | Validações básicas no pipeline                       | ✅ Linters e PR validation                    |
| 2     | Proveniência e rastreabilidade de decisões           | ✅ Tracking de alterações e ownership         |
| 3–4   | Isolamento e builds reproduzíveis                    | ❌ Fora do escopo deste capítulo              |

**🔐 Nível máximo suportado por este capítulo: SLSA 2 / 4**

---

## ✅ Conclusão

- O Capítulo 06 fornece práticas sólidas de desenvolvimento seguro, com validação, evidência e governação;
- Atinge maturidade **2/3** em **SAMM** e **DSOMM**, e cobre diretamente os controlos críticos do **SSDF**;
- É aplicável a contextos regulados e ambientes que exigem *compliance auditável* e *rastreabilidade técnica*;
- Contribui para a adoção sistemática de boas práticas DevSecOps desde o primeiro commit.
