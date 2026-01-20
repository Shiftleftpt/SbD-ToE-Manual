---
id: rationale-catalogo
title: ℹ️ Fundamentação
description: Fundamentação e estrutura lógica dos temas de requisitos usados no catálogo
tags: [estrutura, requisitos, temas, asvs, rastreabilidade, ia]
sidebar_position: 2
---

## Rationale para a Estrutura dos Requisitos Aplicacionais

A definição dos requisitos aplicacionais neste manual segue uma estrutura em **20 temas principais**, criada com o objetivo de oferecer uma abordagem **abrangente, prática e proporcional ao risco**, adequada à aplicação dos princípios de *Security by Design* ao longo de todo o ciclo de vida do software.

Esta estrutura procura equilibrar **rigor normativo**, **aplicabilidade prática** e **neutralidade tecnológica**, permitindo a sua utilização consistente em contextos de desenvolvimento tradicionais, cloud-native, altamente automatizados ou assistidos por ferramentas de geração automática.

---

## 🧩 Origem e Fundamento

A estrutura adotada tem como base principal a framework **OWASP ASVS v5.0 (Application Security Verification Standard)**, reconhecida como uma referência global para a definição e verificação de requisitos de segurança aplicacional.

Contudo, a versão aqui apresentada:

- **Incorpora e cruza requisitos** inspirados noutras frameworks de maturidade e segurança, nomeadamente:
  - **NIST SP 800-53 Rev. 5**
  - **OWASP SAMM v2.1**
  - **BSIMM13** (por inferência a partir de fontes públicas)
  - **SLSA v1.0**
  - **CIS Controls v8**
- **Agrupa e adapta domínios do ASVS** para refletir melhor a forma como os sistemas são efetivamente concebidos, desenvolvidos, integrados e operados em ambientes modernos.

Desta forma, os temas cobrem não apenas preocupações clássicas de segurança funcional e técnica (ex.: autenticação, encriptação, controlo de acesso), mas também domínios relacionados com **práticas de desenvolvimento**, **automação**, **auditoria**, **cadeia de fornecimento** e **integração contínua**.

Não obstante esta consolidação — que pode e deve ser adaptada a cada organização — o manual inclui noutros capítulos **requisitos específicos por domínio técnico**, como Arquitetura Segura, CI/CD, Supply Chain, Infraestrutura como Código ou Containers.

Neste capítulo são tratados, de forma deliberada, os requisitos que podem ser classificados como **requisitos de segurança aplicacionais transversais**, aplicáveis a uma aplicação concreta e proporcionais ao seu nível de risco.

---

## 🧠 Motivações para Ajustes e Consolidação

A estrutura dos 20 temas foi desenvolvida com base nas seguintes motivações fundamentais:

- **Clareza funcional**  
  Os temas são nomeados de forma a permitir que qualquer equipa técnica compreenda rapidamente o seu âmbito e aplicação.

- **Proporcionalidade ao risco**  
  Todos os requisitos são classificáveis por níveis de risco da aplicação (L1, L2, L3), permitindo uma aplicação graduada e justificável.

- **Alinhamento com práticas reais de engenharia**  
  Os agrupamentos refletem a forma como as organizações estruturam equipas, processos, pipelines e responsabilidades técnicas.

- **Cobertura de lacunas identificadas em frameworks base**  
  Domínios como *Threat Modeling*, *SBOM/SCA*, *CI/CD Seguro*, *Testes de Segurança* e *Governação* são tradicionalmente pouco ou mal cobertos em frameworks exclusivamente aplicacionais como o ASVS, mas são críticos na prática — razão pela qual surgem como temas autónomos.

---

## 🤖 Nota sobre Automação e Uso de IA no Desenvolvimento

A estrutura por temas **não assume um modelo de desenvolvimento manual**, nem ignora a adoção crescente de **automação, pipelines avançados ou assistentes baseados em IA** no processo de engenharia de software.

No entanto, essa pervasividade **não justifica a criação de novos temas de requisitos aplicacionais**, uma vez que:

- a automação **não altera a natureza dos riscos aplicacionais**;
- os requisitos de segurança mantêm-se válidos independentemente da forma como o código é produzido;
- o impacto da automação manifesta-se sobretudo ao nível da **governação**, **validação**, **rastreabilidade** e **evidência**.

Por esse motivo, o manual opta por:
- manter o catálogo T01–T20 **estável e tecnologicamente neutro**;
- tratar explicitamente o uso de automatismos e IA através de **prescrições transversais** e **regras de aplicação**, documentadas em anexos e no ciclo de vida (ex.: governação do uso de automatismos, gates de CI/CD, revisão humana obrigatória).

Esta decisão preserva a longevidade e a coerência do modelo, evitando dependência de tecnologias específicas.

---

## 🧷 Ligação aos Capítulos do Manual

Os 20 temas de requisitos funcionam como **base comum** para a aplicação prática dos capítulos seguintes do manual, permitindo:

- **Ancorar decisões de arquitetura e desenvolvimento em requisitos de segurança concretos e verificáveis**;
- **Definir níveis mínimos de segurança esperados por tipo de aplicação**, com base na sua classificação de risco;
- **Reforçar a rastreabilidade entre requisitos, práticas, testes e controlo de qualidade**;
- **Suportar modelos de threat modeling, onboarding, verificação contínua e checklists operacionais** apresentados nos capítulos seguintes.

Cada tema pode ser diretamente associado a um ou mais capítulos técnicos do manual (por exemplo, *Gestão de Dependências* com o Capítulo 5, *CI/CD Seguro* com o Capítulo 7, etc.).

> A estrutura por temas é também reutilizada nos **checklists práticos**, nas **matrizes de rastreabilidade** e na **cobertura de frameworks normativas** que acompanham este manual.

---
