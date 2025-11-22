---
id: achievable-maturity
title: Mapeamento de Maturidade - Capítulo 05
sidebar_position: 10
tags: [DSOMM, SAMM, SLSA, SSDF, canon, maturidade]
---

# 📈 Maturidade - Dependências, SBOM e SCA

Este documento apresenta o mapeamento entre as práticas descritas no Capítulo 05 do SbD-ToE - *Gestão de Dependências, SBOM e SCA* - e os principais frameworks de segurança e maturidade:

- **OWASP SAMM**
- **BSIMM**
- **NIST SSDF**
- **SLSA**
- **OWASP DSOMM**

O capítulo prescreve práticas formais para identificação, validação e governação contínua de dependências externas e componentes de terceiros, com integração de SBOM, políticas e SCA.

---

## 🎯 Como interpretar este mapeamento de maturidade

Este ficheiro **não avalia organizações**, mas sim o grau de maturidade e completude das **práticas prescritas no capítulo** face a frameworks amplamente reconhecidos.

| Framework        | Avaliação usada                     | Justificação                                      |
|------------------|-------------------------------------|--------------------------------------------------|
| OWASP SAMM       | `n / 3`                             | Framework prescritiva com 3 níveis por domínio   |
| OWASP DSOMM      | `n / m` (até 4)                     | Domínios com níveis formais                      |
| NIST SSDF        | Lista de controlos cobertos         | Modelo binário, sem níveis formais               |
| BSIMM            | Lista de práticas cobertas          | Modelo observacional, não prescritivo            |
| SLSA             | Nível máximo suportado (ex: 2 de 4) | Modelo acumulativo, não gradual por domínio      |

---

## 🧭 Visão Geral de Alinhamento

| Framework         | Domínios Relevantes                              | Práticas ou Objetos Cobertos                                              | Avaliação de Maturidade        |
|------------------|---------------------------------------------------|---------------------------------------------------------------------------|--------------------------------|
| OWASP SAMM v2.1  | Construction → Dependency Management              | SBOM, políticas de aceitação, exceções, validação e bloqueio              | **2 / 3**                      |
| OWASP DSOMM      | Policy, Build & Deploy, Tooling                   | Políticas de risco, hardening, bloqueios CI/CD, rastreabilidade SCA       | **2 / 3** (média dos domínios) |
| NIST SSDF v1.1   | PS.3.2, RV.1.1, RV.1.3                             | Gestão de dependências, findings, análise contínua                        | **✔️ PS.3.2, RV.1.1, RV.1.3**  |
| BSIMM13          | CMVM1.1, SR1.2, SE2.4                              | Inventário, aceitação de risco, governação de exceções                    | Contributo direto              |
| SLSA v1.0        | Provenance, Build Integrity, Dependency Control   | SBOM, pinning, proveniência de dependências                               | **Nível 2 / 4**                |

---

## 🧱 OWASP SAMM - Construction → Dependency Management

| Nível | Descrição SAMM                                                     | Cobertura pelo Cap. 05                                |
|-------|--------------------------------------------------------------------|--------------------------------------------------------|
| 1     | Identificação e listagem manual de dependências                    | ✅ SBOM obrigatória por build                          |
| 2     | Processo formal de aceitação, rastreio e controlo de risco         | ✅ Políticas, exceções e integração com SCA            |
| 3     | Automação e integração contínua                                    | ❌ Parcial - ferramentas integráveis, mas não automatizado no core |

**🧮 Maturidade atingida: 2 / 3**

---

## 🧱 OWASP DSOMM - Policy, Build & Deploy, Tooling

| Domínio        | Nível | Justificação técnica                                               |
|----------------|-------|--------------------------------------------------------------------|
| Policy         | 2 / 3 | Definição formal de critérios de aceitação e exceções              |
| Build & Deploy | 2 / 3 | Geração e publicação de SBOM com integração na pipeline            |
| Tooling        | 2 / 3 | Ferramentas recomendadas para SCA, validação de findings           |

---

## 🧱 NIST SSDF - Dependências e Validação

| Controlos NIST SSDF | Descrição                                        | Alinhamento com Cap. 05 |
|---------------------|--------------------------------------------------|--------------------------|
| PS.3.2              | Validar integridade de componentes                | ✅ SBOM e critérios de aceitação       |
| RV.1.1              | Rever código e componentes                        | ✅ Validação de dependências e findings |
| RV.1.3              | Corrigir vulnerabilidades identificadas           | ✅ Integração com gestão de findings   |

---

## 🧱 BSIMM - Software Environment e Segurança Operacional

| Prática BSIMM   | Alinhamento com Cap. 05                                |
|-----------------|--------------------------------------------------------|
| CMVM1.1         | Inventário formal e atualizado                         |
| SR1.2           | Rastreio de vulnerabilidades em bibliotecas            |
| SE2.4           | Revisão e aceitação de componentes por política        |

---

## 🧱 SLSA - Provenance & Dependency Control

| Nível | Requisitos principais                                  | Cobertura pelo Cap. 05                    |
|-------|---------------------------------------------------------|-------------------------------------------|
| 1     | Listagem e rastreio básico de dependências              | ✅ SBOM gerado por build                   |
| 2     | Proveniência e pinning de versões                       | ✅ Critérios de controlo formal            |
| 3+    | Builds verificáveis e reprodutibilidade                 | ❌ Fora do escopo (ver Cap. 06 e 08)       |

**🔐 Nível máximo suportado por este capítulo: SLSA 2 / 4**

---

## ✅ Conclusão

- O Capítulo 05 define práticas robustas para controlo de dependências e componentes de terceiros;
- Alinha-se com **SAMM (2/3)**, **DSOMM (2/3)**, **SSDF (3 controlos)**, **BSIMM (3 práticas)** e **SLSA (nível 2/4)**;
- Permite implementação prática e proporcional de políticas de aceitação, SBOM e validação contínua;
- Serve de base para segurança em pipelines e hardening de cadeia de fornecimento de software.
