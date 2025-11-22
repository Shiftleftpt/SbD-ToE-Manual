---
description: Responsabilidades dos Arquitetos de Software no SbD-ToE
id: arquitetos-software
sidebar_label: 🏗️ Arquitetos de Software
sidebar_position: 6
tags:
- arquitetura
- containers
- dependencias
- design
- responsabilidades
- seguranca
- segurança
title: Arquitetos de Software
---


# 🏗️ Arquitetos de Software

## Visão Geral

Arquitetos desenham soluções que **resistem ao tempo e às ameaças**.  
Garantem que princípios de segurança estão embutidos nas decisões estruturais desde o início. Aplicam **padrões seguros desde a fundação**.

### Responsabilidades Principais
- Desenham soluções com padrões seguros (Cap. 04)
- Antecipam implicações de risco em integrações e fluxos de dados
- Garantem consistência da arquitetura em pipelines, IaC e deploys
- Tomam decisões arquiteturais documentadas (ADR)

### Contexto Organizacional
O trabalho dos arquitetos suporta princípios de *security by design* previstos em **GDPR**, **AI Act** e também obrigações de **NIS2** relacionadas com planeamento de medidas técnicas adequadas. Sem arquitetura segura, correções posteriores são caras e ineficazes.

## Enquadramento Regulatório

Concretizam:
- **GDPR** e **AI Act**: *Security by design* e *privacy by design*
- **NIS2**: Medidas técnicas estruturais adequadas

---

## Atividades por Capítulo

### Cap. 02 - Requisitos de Segurança
Rever **classificação e requisitos** sempre que ocorra integração crítica ou mudança estrutural relevante.

**User Stories:**
- [US-02: Revisão em alterações críticas](/sbd-toe/sbd-manual/requisitos-seguranca/aplicacao-lifecycle#us-02--revisão-em-integração-crítica-ou-mudança-relevante) — Atualizar controlos e rastreabilidade

### Cap. 03 - Threat Modeling
Criar **modelo de ameaça inicial** com DFDs e STRIDE/LINDDUN, validar arquitetura identificando ameaças críticas antes do design, atualizar modelo em alterações significativas, aplicar LINDDUN quando há tratamento de dados pessoais.

**User Stories:**
- [US-01: Modelo de ameaça inicial](/sbd-toe/sbd-manual/threat-modeling/aplicacao-lifecycle#us-01--criação-de-modelo-de-ameaça-inicial) — Riscos visíveis desde o início
- [US-02: Validação de arquitetura via threat modeling](/sbd-toe/sbd-manual/threat-modeling/aplicacao-lifecycle#us-02--validação-de-arquitetura-através-de-threat-modeling) — Identificar ameaças antes do design
- [US-03: Atualização em alterações significativas](/sbd-toe/sbd-manual/threat-modeling/aplicacao-lifecycle#us-03--atualização-em-alterações-significativas) — Manter modelo válido
- [US-06: Aplicação de LINDDUN para privacidade](/sbd-toe/sbd-manual/threat-modeling/aplicacao-lifecycle#us-06--aplicação-de-linddun-para-privacidade) — Cobertura de ameaças GDPR

### Cap. 04 - Arquitetura Segura
Definir **princípios de arquitetura segura**, produzir ficha de arquitetura com controlos, registar decisões (ADR) com racional de segurança, rever trust boundaries e integrações, sincronizar modelo de ameaças com decisões, manter triggers de revisão, catálogo de padrões seguros, especificar controlos de isolamento, executar threat modeling no design inicial L2-L3.

**User Stories:**
- [US-01: Princípios de arquitetura segura](/sbd-toe/sbd-manual/arquitetura-segura/aplicacao-lifecycle#us-01--definição-de-princípios-de-arquitetura-segura) — Orientar decisões técnicas
- [US-02: Ficha de arquitetura com controlos](/sbd-toe/sbd-manual/arquitetura-segura/aplicacao-lifecycle#us-02--produção-de-ficha-de-arquitetura) — Solução segura e escalável
- [US-07: Registro de decisões (ADR)](/sbd-toe/sbd-manual/arquitetura-segura/aplicacao-lifecycle#us-07--registro-de-decisões-de-arquitetura-adr) — Rastreabilidade e consistência
- [US-08: Revisão de trust boundaries](/sbd-toe/sbd-manual/arquitetura-segura/aplicacao-lifecycle#us-08--revisão-de-trust-boundaries-e-integrações) — Validar autenticação, autorização, isolamento
- [US-09: Sincronização threat model ↔ arquitetura](/sbd-toe/sbd-manual/arquitetura-segura/aplicacao-lifecycle#us-09--sincronização-entre-modelo-de-ameaças-e-decisões-de-arquitetura) — Controlos cobrem ameaças
- [US-10: Triggers de revisão de arquitetura](/sbd-toe/sbd-manual/arquitetura-segura/aplicacao-lifecycle#us-10--triggers-de-revisão-de-arquitetura) — Documentação atualizada
- [US-11: Catálogo de padrões seguros](/sbd-toe/sbd-manual/arquitetura-segura/aplicacao-lifecycle#us-11--catálogo-de-padrões-de-arquitetura-segura) — Reutilização de designs validados
- [US-12: Controlos de isolamento técnico](/sbd-toe/sbd-manual/arquitetura-segura/aplicacao-lifecycle#us-12--controlos-técnicos-de-isolamento) — Resiliência a sobre-carga e falhas
- [US-14: Threat Modeling no design inicial](/sbd-toe/sbd-manual/arquitetura-segura/aplicacao-lifecycle#us-14--threat-modeling-no-design-inicial-l2l3) — Especificar controlos proporcionais

### Cap. 08 - IaC e Infraestrutura
Colaborar na **segregação de ambientes** com tagging e permissões mínimas, governar módulos IaC com origem confiável.

**User Stories:**
- [US-02: Segregação de ambientes com tagging](/sbd-toe/sbd-manual/iac-infraestrutura/aplicacao-lifecycle#us-02--segregação-de-ambientes-tagging-e-permissões-mínimas) — Isolamento e rastreabilidade
- [US-04: Governança de módulos IaC](/sbd-toe/sbd-manual/iac-infraestrutura/aplicacao-lifecycle#us-04--governança-e-origem-confiável-de-módulos) — Evitar propagação de más práticas

### Cap. 11-12 - Deploy e Operações
Apoiar desenho **resiliente de ambientes** de produção com padrões de disponibilidade e recuperação.

---

## Referências aos Capítulos

Para contexto e enquadramento completo:

- [Cap. 02 - Requisitos de Segurança](/sbd-toe/sbd-manual/requisitos-seguranca/intro)
- [Cap. 03 - Threat Modeling](/sbd-toe/sbd-manual/threat-modeling/intro)
- [Cap. 04 - Arquitetura Segura](/sbd-toe/sbd-manual/arquitetura-segura/intro)
- [Cap. 07 - CI/CD Seguro](/sbd-toe/sbd-manual/cicd-seguro/intro)
- [Cap. 08 - IaC e Infraestrutura](/sbd-toe/sbd-manual/iac-infraestrutura/intro)
- [Cap. 11 - Deploy Seguro](/sbd-toe/sbd-manual/deploy-seguro/intro)
- [Cap. 12 - Monitorização e Operações](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro)
