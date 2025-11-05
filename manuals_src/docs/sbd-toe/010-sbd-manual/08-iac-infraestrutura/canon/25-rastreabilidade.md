---
id: rastreabilidade
title: Rastreabilidade - Infraestrutura como Código (IaC)
sidebar_position: 25
description: Mapeamento entre as práticas de segurança prescritas no capítulo e os requisitos de frameworks e normas reconhecidas.
tags: [rastreabilidade, normas, frameworks, iac, infraestrutura como código]
---

# 📎 Rastreabilidade contra Frameworks - Capítulo 08: IaC e Infraestrutura como Código

Este ficheiro estabelece a **rastreabilidade entre as práticas prescritas neste capítulo** e os requisitos dos principais frameworks e normas de segurança associados à definição, controlo e governação segura de infraestrutura como código (IaC).

> A rastreabilidade é feita de forma **top-down**, demonstrando como o SbD-ToE cobre sistematicamente os requisitos normativos e técnicos exigidos à IaC, com ênfase em **proporcionalidade, enforcement e validação automatizada**.

---

## 📌 Tabela de Rastreabilidade

| Requisito / Domínio (Framework)                             | Prática do Capítulo 08 que responde                              | Nível de Cobertura |
|-------------------------------------------------------------|------------------------------------------------------------------|--------------------|
| **NIST SSDF** – PW.3 / PW.6 / RV.3                          | Validação IaC, controlo de risco, rastreabilidade e exceções     | ✅ Completo         |
| **OWASP SAMM v2.1** – Implementation → Environment Hardening | Templates validados, segregação de ambientes, enforcement político | ✅ Nível 3          |
| **BSIMM13** – Configuration & Deployment (CD1–CD3)          | IaC versionado, revisão formal, tagging e rastreabilidade         | ✅ Nível 2          |
| **SLSA v1.0** – Provenance, Build Policies                  | IaC auditável, tagging de versões, enforcement e controlo         | ✅ Completo         |
| **ISO/IEC 27001** – A.12.1.2 / A.14.2.5 / A.14.2.7           | Validação técnica da infraestrutura e gestão de ambientes         | ✅ Completo         |
| **CIS Controls v8** – Control 4.4 / 11.1 / 16.11             | Gestão segura de configuração e validação automatizada            | ✅ Completo         |
| **ENISA DevSecOps** – IaC Security & Governance              | Rastreabilidade, requisitos IaC, segregação de ambientes, automação | ✅ Completo         |
| **OWASP DSOMM** – Design & Development / Build & Test       | Política como código, enforcement, validação, gestão de segredos | ✅ Nível 2 / 3      |

---

## 🧠 Notas explicativas por framework

### 🛠️ NIST SSDF

Cobre integralmente:
- **PW.3**: definição e documentação de requisitos de segurança para componentes IaC (`addon/08`);
- **PW.6**: execução de validações automáticas antes do `apply`, com PR reviews (`addon/02`, `addon/06`);
- **RV.3**: tratamento formal de exceções técnicas (`addon/09`).

---

### 🧱 OWASP SAMM v2.1

Atinge **nível 3** em *Environment Hardening*:
- Templates reutilizáveis com segurança por design (`addon/04`);
- Enforcement político automatizado com OPA/Conftest (`addon/06`);
- Validação e segregação de ambientes (`addon/03`, `addon/07`).

---

### 📊 BSIMM13

Cobertura sólida dos domínios **CD1–CD3**:
- IaC tratado como artefacto auditável;
- Versionamento com tagging explícito (`addon/01`, `addon/07`);
- Revisão de alterações à infraestrutura por PR (`addon/06`).

---

### 🔐 SLSA v1.0

Capítulo suporta:
- Proveniência de planos e artefactos (`addon/07`);
- Controlo de alterações com assinatura e enforcement (`addon/06`);
- Modularização e controlo por políticas internas (`60`).

---

### 🏛️ ISO/IEC 27001

Controlos abordados:
- **A.12.1.2**: separação lógica de ambientes (`addon/03`);
- **A.14.2.5**: validação técnica de configuração e deployment (`addon/02`);
- **A.14.2.7**: controlo de alterações rastreável e com aceitação formal (`addon/06`, `addon/09`).

---

### 📐 CIS Controls v8

Cobertura completa de:
- **4.4**: infraestrutura definida como código e validada (`addon/01`);
- **11.1**: aprovação de configurações e ambientes (`addon/06`);
- **16.11**: monitorização e validação contínua (`addon/02`, `addon/30`).

---

### 🔄 ENISA DevSecOps

Capítulo responde a:
- Validação contínua de configurações (`addon/02`);
- Rastreabilidade entre risco, requisitos e configuração (`addon/08`);
- Gestão formal de exceções e governação de ambientes (`addon/09`).

---

### 🧬 OWASP DSOMM

O Capítulo 08 cobre diretamente os subdomínios de **Design & Development** e **Build & Test**:

| Subdomínio DSOMM                | Prática no Capítulo 08 que responde                     | Cobertura |
|--------------------------------|----------------------------------------------------------|-----------|
| **IaC Practices**              | Estrutura modular, pipelines IaC, requisitos `IAC-XXX`   | ✅ Completo |
| **Control Mapping**           | Enforcement com OPA/Conftest + políticas (`60`)    | ✅ Completo |
| **Secrets Management**        | Segregação e injeção de segredos (`addon/06`)            | ✅ Completo |
| **Validation & Linting**      | Linters e enforcement automático (`addon/02`, `addon/06`) | ✅ Completo |
| **Threat Modeling Integration**| Menção implícita à análise de risco (`addon/08`)          | ⚠️ Parcial |
| **Infrastructure Testing**    | Sugerido no `30`, mas não obrigatório                    | ⚠️ Parcial |
| **Drift Detection**           | Não abordado diretamente                                 | ❌        |

> ⚠️ A cobertura DSOMM é elevada, mas recomenda-se reforço formal na integração com threat modeling e testes automáticos da infraestrutura para atingir o **nível 3 de maturidade**.

---

## 🔗 Ligações com outros capítulos

Este capítulo complementa e depende de:

- **Capítulo 01 - Classificação de Risco**: define a exigência proporcional de validação para ambientes e infraestrutura;
- **Capítulo 02 - Requisitos de Segurança**: define os requisitos `IAC-XXX`, validados pelas práticas deste capítulo;
- **Capítulo 07 - Pipelines CI/CD**: onde os controlos deste capítulo são aplicados e orquestrados;
- **Capítulo 09 - Containers**: que dependem diretamente da infraestrutura provisionada para garantir isolamento e segurança;
- **Capítulo 14 - Governação e Exceções Técnicas**: que legitima as práticas de aceitação e rastreabilidade descritas em `addon/09`.

> 📌 Esta rastreabilidade comprova que o Capítulo 08 **opera como camada crítica de enforcement de segurança no ciclo de vida da infraestrutura**, garantindo que ambientes são definidos, auditados, testados e aplicados com controlo técnico e organizacional.
