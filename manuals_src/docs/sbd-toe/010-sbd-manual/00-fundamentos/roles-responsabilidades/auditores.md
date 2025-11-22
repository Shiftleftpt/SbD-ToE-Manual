---
description: Responsabilidades dos Auditores no SbD-ToE
id: auditores
sidebar_label: 📋 Auditores Internos e Externos
sidebar_position: 14
tags:
- auditores
- auditoria
- compliance
- organizacional
- políticas
- responsabilidades
- validação
title: Auditores Internos e Externos
---


# 📋 Auditores Internos e Externos

## Visão Geral

Auditores **validam a aplicação efetiva das práticas** descritas no SbD-ToE.  
Verificam classificações de risco, rastreabilidade, evidência de aplicação, e alinhamento com requisitos regulatórios em todos os capítulos.

### Responsabilidades Principais
- Validam a aplicação efetiva das práticas prescritas
- Avaliam classificações de risco, requisitos, rastreabilidade e evidências
- Produzem relatórios independentes e recomendações de melhoria
- Comprovam conformidade perante autoridades

### Contexto Organizacional
São instrumentos essenciais para comprovar conformidade perante autoridades de supervisão, tal como requerido em **NIS2**, **DORA**, **GDPR** e **ISO 27001**.

## Enquadramento Regulatório

São instrumentos formais para comprovar cumprimento perante autoridades:
- **NIS2**: Auditorias de segurança e conformidade
- **DORA**: Testes de resiliência e auditorias de terceiros
- **GDPR**: Auditorias de proteção de dados
- **ISO 27001/27002**: Auditorias de SGSI

---

## Atividades por Capítulo

### Transversal - Todos os Capítulos
Validar **evidência de aplicação de práticas**, verificar **rastreabilidade de decisões** (ADR, exceções, aceitações de risco), confirmar **alinhamento com requisitos regulatórios** (NIS2, DORA, GDPR, SSDF, ISO 27001).

**Requisitos associados:**
- [US-12: Documentação de conformidade regulatória](/sbd-toe/sbd-manual/monitorizacao-operacoes/aplicacao-lifecycle#us-12--documentação-de-conformidade-regulatória) — GRC documenta, Auditores validam

### Cap. 01 - Classificação de Aplicações
Verificar **classificações de risco** e sua adequação ao contexto técnico e negócio. Validar KPIs de governação.

**Requisitos associados:**
- [US-08: KPIs de governação da classificação](/sbd-toe/sbd-manual/classificacao-aplicacoes/aplicacao-lifecycle#us-08--kpis-de-governação-da-classificação) — GRC consolida, Auditores validam
- [US-09: Políticas organizacionais formais](/sbd-toe/sbd-manual/classificacao-aplicacoes/aplicacao-lifecycle#us-09--políticas-organizacionais-formais) — Gestão publica, Auditores validam aplicação

### Cap. 02 - Requisitos de Segurança
Validar **implementação de requisitos por nível** (L1/L2/L3), verificar rastreabilidade requisitos → controlos → evidência.

### Cap. 07 - CI/CD Seguro
Validar **rastreabilidade commit → pipeline → release**, verificar gestão de exceções.

**Requisitos associados:**
- [US-09: Rastreabilidade ponta-a-ponta](/sbd-toe/sbd-manual/cicd-seguro/aplicacao-lifecycle#us-09--rastreabilidade-ponta-a-ponta) — GRC rastreia, Auditores validam
- [US-10: Gestão de exceções](/sbd-toe/sbd-manual/cicd-seguro/aplicacao-lifecycle#us-10--gestão-de-exceções) — GRC gere, Auditores validam

### Cap. 08 - IaC e Infraestrutura
Validar **rastreabilidade ficheiro → recurso → ambiente**, verificar janelas de mudança e aprovações, validar exceções formais.

**Requisitos associados:**
- [US-07: Rastreabilidade ficheiro → recurso → ambiente](/sbd-toe/sbd-manual/iac-infraestrutura/aplicacao-lifecycle#us-07--rastreabilidade-ficheiro--recurso--ambiente) — GRC documenta, Auditores validam
- [US-13: Janela de mudança e aprovações](/sbd-toe/sbd-manual/iac-infraestrutura/aplicacao-lifecycle#us-13--janela-de-mudança-e-aprovações-por-papel) — GRC define, Auditores validam
- [US-14: Exceções formais em IaC](/sbd-toe/sbd-manual/iac-infraestrutura/aplicacao-lifecycle#us-14--exceções-formais-em-iac) — GRC/AppSec gerem, Auditores validam

### Cap. 14 - Governança e Contratação
Auditar **documentação de exceções**, verificar **aprovações formais**, validar **conformidade contratual com fornecedores**, verificar rastreabilidade completa.

**Requisitos associados:**
- [US-06: Repositório de conformidade](/sbd-toe/sbd-manual/governanca-contratacao/aplicacao-lifecycle#us-06--repositório-de-conformidade-por-aplicação) — AppSec/Dev Lead mantêm, Auditores validam
- [US-07: Validações periódicas de conformidade](/sbd-toe/sbd-manual/governanca-contratacao/aplicacao-lifecycle#us-07--validações-periódicas-de-conformidade) — AppSec/GRC executam, Auditores validam
- [US-10: Checklist centralizado de conformidade](/sbd-toe/sbd-manual/governanca-contratacao/aplicacao-lifecycle#us-10--checklist-centralizado-de-conformidade-sbd-toe) — AppSec/Dev Lead mantêm, Auditores usam

---

## Referências aos Capítulos

Auditores utilizam todos os capítulos como fonte de evidência:

- [Cap. 01 - Classificação de Aplicações](/sbd-toe/sbd-manual/classificacao-aplicacoes/intro)
- [Cap. 02 - Requisitos de Segurança](/sbd-toe/sbd-manual/requisitos-seguranca/intro)
- [Cap. 03 - Threat Modeling](/sbd-toe/sbd-manual/threat-modeling/intro)
- [Cap. 04 - Arquitetura Segura](/sbd-toe/sbd-manual/arquitetura-segura/intro)
- [Cap. 05 - Dependências e SBOM](/sbd-toe/sbd-manual/dependencias-sbom-sca/intro)
- [Cap. 06 - Desenvolvimento Seguro](/sbd-toe/sbd-manual/desenvolvimento-seguro/intro)
- [Cap. 07 - CI/CD Seguro](/sbd-toe/sbd-manual/cicd-seguro/intro)
- [Cap. 08 - IaC e Infraestrutura](/sbd-toe/sbd-manual/iac-infraestrutura/intro)
- [Cap. 09 - Containers e Imagens](/sbd-toe/sbd-manual/containers-imagens/intro)
- [Cap. 10 - Testes de Segurança](/sbd-toe/sbd-manual/testes-seguranca/intro)
- [Cap. 11 - Deploy Seguro](/sbd-toe/sbd-manual/deploy-seguro/intro)
- [Cap. 12 - Monitorização e Operações](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro)
- [Cap. 13 - Formação e Onboarding](/sbd-toe/sbd-manual/formacao-onboarding/intro)
- [Cap. 14 - Governança e Contratação](/sbd-toe/sbd-manual/governanca-contratacao/intro)
