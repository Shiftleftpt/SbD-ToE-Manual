---
id: rationale-catalogo
title: ℹ️ Fundamentação
description: Fundamentação e estrutura lógica dos temas de requisitos usados no catálogo
tags: [estrutura, requisitos, temas, asvs, rastreabilidade]
sidebar_position: 2
---

## Rationale para a Estrutura dos Requisitos Aplicacionais

A definição dos requisitos aplicacionais neste manual segue uma estrutura em **20 temas principais**, criada com o objetivo de oferecer uma abordagem **abrangente, prática e proporcional ao risco**, adequada à aplicação dos princípios de *Security by Design* ao longo do ciclo de vida do software.

### 🧩 Origem e Fundamento

A estrutura adotada tem como base principal a framework **OWASP ASVS v5.0 (Application Security Verification Standard)**, reconhecida como uma referência global para verificação de segurança aplicacional. Contudo, a versão aqui apresentada:

- **Agrupa e adapta domínios** do ASVS para refletir melhor o modo como os sistemas são realmente desenvolvidos e mantidos;
- **Incorpora requisitos adicionais** inspirados noutras frameworks de maturidade e segurança, como:
  - **NIST SP 800-53 Rev. 5**
  - **OWASP SAMM v2.1**
  - **BSIMM13**
  - **SLSA v1.0**
  - **CIS Controls v8**

Estes temas permitem cobrir não só as preocupações clássicas de segurança funcional e técnica (ex: autenticação, encriptação, controlo de acesso), mas também tópicos relacionados com práticas de desenvolvimento, automação, auditoria e integração em pipelines modernos.
Não obstante desta compilação, que pode ser adotada e obviamente adaptada a cada projeto, existem ao longo do manual outras práticas que incluem os seus proprios requisitos especificos, e.g., Arquitetuera segura, Requisitos CI/CD, Requisitos Supply Chain. 
Neste capitulo, tentativamente, cobrimos os requisitos que podem ser classificados tradicionalmente como requisitos para a aplicação, e para um dado nivel de classificação.

### 🧠 Motivações para Ajustes

A estrutura dos 20 temas foi desenvolvida com base nas seguintes motivações:

- **Clareza funcional**: os temas são nomeados para que qualquer equipa técnica consiga perceber rapidamente a que se referem;
- **Proporcionalidade ao risco**: todos os requisitos são classificáveis por níveis de risco da aplicação (L1, L2, L3), o que permite a sua aplicação proporcional;
- **Alinhamento com práticas reais**: os agrupamentos refletem a forma como as organizações estruturam equipas, processos e ferramentas;
- **Cobertura de lacunas identificadas**: áreas como *Threat Modeling*, *SBOM/SCA*, *CI/CD seguro*, *Testes de segurança* e *Governança* são pouco ou mal cobertas em frameworks como o ASVS, mas essenciais na prática - por isso, são tratadas como temas autónomos.

### 🧷 Ligação aos Capítulos do Manual

Os 20 temas de requisitos funcionam como **base comum para a aplicação prática dos capítulos seguintes do manual**, permitindo:

- **Ancorar as decisões de arquitetura e desenvolvimento nos requisitos de segurança concretos**;
- **Definir níveis mínimos de segurança esperados por tipo de aplicação (com base na sua classificação de risco)**;
- **Reforçar a rastreabilidade entre requisitos, práticas, testes, e controlo de qualidade**;
- **Suportar os modelos de threat modeling, onboarding, verificação e checklist operacional** apresentados nos capítulos seguintes.

Cada um dos temas pode, assim, ser diretamente associado a um ou mais capítulos técnicos do manual (*ex: "Controlo de Dependências"* com o Capítulo 5, *"CI/CD Seguro"* com o Capítulo 7, etc.).

> A estrutura por temas também será usada nos **checklists práticos** e na **matriz de cobertura de frameworks** que acompanha este manual.

---

