---
description: Mapeamento das práticas deste capítulo face a frameworks normativos e
  requisitos de segurança reconhecidos
id: rastreabilidade
sidebar_position: 25
tags:
- arquitetura
- dsomm
- frameworks
- iso
- rastreabilidade
- samm
- slsa
title: Rastreabilidade Top-Down - Capítulo 04
---


# 📎 Rastreabilidade contra Frameworks - Capítulo 04: Arquitetura Segura

Este documento estabelece a **rastreabilidade entre as práticas prescritas neste capítulo** e os requisitos dos principais frameworks e normas de segurança aplicacional no que diz respeito à conceção, validação e governação da arquitetura.

> A rastreabilidade é feita de forma **top-down**, demonstrando como o SbD-ToE cobre sistematicamente os requisitos técnicos e normativos associados à arquitetura de software segura.

---

## 📌 Tabela de Rastreabilidade

| Requisito / Domínio (Framework)                                | Prática do Capítulo 04 que responde                              | Nível de Cobertura |
|----------------------------------------------------------------|------------------------------------------------------------------|--------------------|
| **NIST SSDF** - PW.1 / PW.4 / RV.1                             | Requisitos de arquitetura, validação formal e rastreabilidade     | ✅ Completo         |
| **OWASP SAMM v2.1** - Design → Architecture & Design           | Zonas de confiança, padrões, validação técnica                   | ✅ Nível 3          |
| **BSIMM13** - Architecture Analysis (AA1–AA3)                  | Modelação, validação formal e documentação de arquitetura         | ✅ Nível 2          |
| **ISO/IEC 27001** - A.14.2.1 / A.14.2.5                        | Definição, revisão e validação técnica da arquitetura             | ✅ Completo         |
| **ISO/IEC 27034** - Application Security Architecture          | Referenciais, práticas e rastreabilidade de controlos de arquitetura | ✅ Completo       |
| **SLSA v1.0** - Build Design Integrity (Nível 2–3)             | Segmentação e isolamento por design, definição da arquitetura segura| ✅ Parcial          |
| **CIS Controls v8** - Control 4.1 / 4.3 / 16.1                 | Definição da arquitetura, separação de funções e controlo de execução| ✅ Completo         |
| **ENISA SDLC / DevSecOps** - Secure Architecture & Review      | Validação formal, zonas de risco, diagramas e documentação        | ✅ Completo         |
| **OWASP DSOMM** - Design & Development                         | Práticas formais de arquitetura, validações, rastreabilidade      | ✅ Nível 3          |

---

## 🧠 Notas Explicativas por Framework

### 🛠️ NIST SSDF

- **PW.1**: Requisitos de arquitetura definidos com base na análise de risco (`ARC-001` a `ARC-011`);
- **PW.4**: Validação da arquitetura antes de desenvolvimento e entrega, com documentação formal;
- **RV.1**: Existência de rastreabilidade entre os requisitos, artefactos de arquitetura e decisões técnicas.

---

### 🧱 OWASP SAMM v2.1

Permite atingir **nível 3** no domínio *Architecture & Design*:
- Zonas de confiança bem definidas;
- Padrões de arquitetura aprovados e reutilizados;
- Validações formais com critérios proporcionais ao risco;
- Rastreabilidade entre requisitos e componentes técnicos.

---

### 📊 BSIMM13

Cobertura dos domínios:
- **AA1**: Mapeamento da arquitetura com base em zonas, fluxos e ativos;
- **AA2**: Validações técnicas com critérios definidos, recorrência e rastreio;
- **AA3**: Documentação formal e versionada das decisões e diagramas.

---

### 🏛️ ISO/IEC 27001

- **A.14.2.1**: Integração da arquitetura segura como parte do processo de desenvolvimento seguro;
- **A.14.2.5**: Validação da arquitetura e dos controlos antes da entrega do sistema.

---

### 🔐 ISO/IEC 27034

- Tratamento da arquitetura como artefacto formal e verificável;
- Integração de controlos de segurança diretamente na estrutura da arquitetura;
- Rastreabilidade entre requisitos, ameaças, controlos e documentação técnica.

---

### 🧬 SLSA v1.0

- Contribuição parcial para **Build Design Integrity**:
  - Diagrama da arquitetura claro com delimitação de zonas;
  - Isolamento lógico proposto, mas dependente da camada infraestrutural;
- Cobertura plena exige articulação com práticas do Capítulo 07 (CI/CD Seguro).

---

### 🧱 CIS Controls v8

- **4.1 / 4.3**: Separação lógica de ativos com base na função e risco;
- **16.1**: Estrutura da arquitetura como mecanismo de controlo da superfície de ataque e configuração segura.

---

### 🛰️ ENISA SDLC / DevSecOps

- Práticas recomendadas de conceção segura formalmente representadas;
- Revisão da arquitetura com critérios de exposição, impacto e risco;
- Reutilização de modelos referenciais e documentação versionada.

---

### 🧩 OWASP DSOMM - Design & Development

- Definição formal da arquitetura, zonas de confiança e fronteiras
- Validações de arquitetura proporcionais ao risco 
- Rastreabilidade entre requisitos e componentes
- Uso da arquitetura como base para identificação de ameaças 
- Diagramas versionados, ADRs, exceções formais 

---

## 🔗 Ligações com Outros Capítulos

Este capítulo articula-se diretamente com:

- **Capítulo 01 - Gestão de Risco**: as zonas de confiança e validações são proporcionais ao risco.
- **Capítulo 02 - Requisitos de Segurança**: os requisitos `REQ-XXX` são rastreados até `ARC-XXX`.
- **Capítulo 03 - Threat Modeling**: a arquitetura segura é a base para identificação de ameaças.
- **Capítulo 09 - Containers e Zonas**: a arquitetura lógica sustenta o modelo de segmentação.
- **Capítulo 10 - Testes de Validação**: a arquitetura é a entrada principal dos testes estruturais.

---

## ✅ Conclusão

A rastreabilidade demonstrada neste capítulo comprova que as práticas de arquitetura segura prescritas:

- **Cumprem na íntegra os principais frameworks de segurança e normas internacionais**;
- Funcionam como **estrutura de controlo técnico verificável, rastreável e auditável**;
- São indispensáveis para **atingir níveis de maturidade elevados (nível 3)** em SAMM, SSDF, DSOMM e outros referenciais;
- Constituem a base sobre a qual se constroem os restantes pilares do modelo SbD-ToE.

> 🧱 **Este capítulo é fundacional**: sem arquitetura segura, nenhuma prática de threat modeling, validação, rastreabilidade ou exceção pode ser corretamente aplicada.
