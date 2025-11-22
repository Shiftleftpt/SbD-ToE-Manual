---
id: product-owner
title: Product Owner (PO)
sidebar_label: 📋 Product Owner (PO)
description: Responsabilidades do Product Owner no SbD-ToE
tags: [po, product-owner, produto, responsabilidades]
sidebar_position: 8
---

# 📋 Product Owner (PO)

## Visão Geral

Product Owner **equilibra negócio e segurança**, garantindo que esta não é vista como custo, mas como **valor intrínseco ao produto**.  
Responsável por priorizar requisitos de segurança, validar impacto de decisões arquiteturais e autorizar releases apenas quando critérios são cumpridos.

### Responsabilidades Principais
- Equilibram prioridades de negócio com requisitos de segurança
- Garantem que as histórias de segurança entram e permanecem no backlog
- Aprovam critérios de aceitação que incluem segurança
- Tomam decisões go/no-go informadas por análise de risco

### Contexto Organizacional
O PO suporta obrigações de **DORA** (integração de segurança e continuidade digital em todos os produtos) e de **NIS2** (integração da gestão de risco nos processos de negócio).

## Enquadramento Regulatório

Apoia:
- **DORA**: Integração da resiliência digital no ciclo de vida
- **NIS2**: Incorporação da gestão de risco no negócio

---

## Atividades por Capítulo

### Cap. 01 - Classificação de Aplicações
Validar **classificações de risco** em função dos objetivos estratégicos do produto.

### Cap. 02 - Requisitos de Segurança
Selecionar **requisitos aplicáveis ao projeto** proporcionais ao risco. Garantir que cada requisito no backlog contém critérios de aceitação de segurança claros e testáveis.

**User Stories:**
- [US-01: Seleção de requisitos aplicáveis](/sbd-toe/sbd-manual/requisitos-seguranca/aplicacao-lifecycle#us-01--seleção-de-requisitos-aplicáveis-ao-projeto) — Segurança proporcional ao risco
- [US-03: Critérios de aceitação de segurança](/sbd-toe/sbd-manual/requisitos-seguranca/aplicacao-lifecycle#us-03--critérios-de-aceitação-de-segurança-claros) — Validação consistente

### Cap. 03 - Threat Modeling
Priorizar **ameaças identificadas** de acordo com impacto no negócio, otimizando mitigação e investimento.

**User Stories:**
- [US-05: Priorização de ameaças por impacto](/sbd-toe/sbd-manual/threat-modeling/aplicacao-lifecycle#us-05--priorização-de-ameaças-por-impacto-no-negócio) — Otimizar recursos de mitigação

### Cap. 04 - Arquitetura Segura
Validar **impacto de requisitos de arquitetura** para priorizar mitigação. Gerir exceções com aprovação e controlos compensatórios.

**User Stories:**
- [US-06: Validação de impacto de requisitos](/sbd-toe/sbd-manual/arquitetura-segura/aplicacao-lifecycle#us-06--validação-de-impacto-de-requisitos-de-arquitetura) — Priorizar mitigação
- [US-10: Gestão de exceções de arquitetura](/sbd-toe/sbd-manual/arquitetura-segura/aplicacao-lifecycle#us-10--gestão-de-exceções-de-arquitetura) — Equilibrar risco e entrega (com AppSec)

### Cap. 05 - Dependências e SBOM
Validar **findings e exceções antes do go-live**, tomando decisão informada de go/no-go baseada em análise de risco.

**User Stories:**
- [US-05: Validação de release (go/no-go)](/sbd-toe/sbd-manual/dependencias-sbom-sca/aplicacao-lifecycle#us-05--validação-de-release-gono-go) — Decisão informada antes do go-live

### Cap. 07 - CI/CD Seguro
Definir **gates de release** que bloqueiam versões inseguras, garantindo conformidade com thresholds estabelecidos.

### Cap. 11 - Deploy Seguro
Autorizar apenas **releases com critérios de segurança cumpridos**, validando que controlos estão aplicados.

### Cap. 13-14 - Formação e Governança
Assegurar que **formação e cláusulas contratuais** refletem práticas seguras e apoiam decisões de produto.

---

## Referências aos Capítulos

Para contexto e enquadramento completo:

- [Cap. 01 - Classificação de Aplicações](/sbd-toe/sbd-manual/classificacao-aplicacoes/intro)
- [Cap. 02 - Requisitos de Segurança](/sbd-toe/sbd-manual/requisitos-seguranca/intro)
- [Cap. 03 - Threat Modeling](/sbd-toe/sbd-manual/threat-modeling/intro)
- [Cap. 04 - Arquitetura Segura](/sbd-toe/sbd-manual/arquitetura-segura/intro)
- [Cap. 05 - Dependências e SBOM](/sbd-toe/sbd-manual/dependencias-sbom-sca/intro)
- [Cap. 07 - CI/CD Seguro](/sbd-toe/sbd-manual/cicd-seguro/intro)
- [Cap. 11 - Deploy Seguro](/sbd-toe/sbd-manual/deploy-seguro/intro)
- [Cap. 13 - Formação e Onboarding](/sbd-toe/sbd-manual/formacao-onboarding/intro)
- [Cap. 14 - Governança e Contratação](/sbd-toe/sbd-manual/governanca-contratacao/intro)
