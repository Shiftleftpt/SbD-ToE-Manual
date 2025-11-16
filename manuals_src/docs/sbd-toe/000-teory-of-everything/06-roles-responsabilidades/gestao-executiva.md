---
id: gestao-executiva
title: Gestão Executiva / CISO
sidebar_label: 🏛️ Gestão Executiva / CISO
description: Responsabilidades da Gestão Executiva no SbD-ToE
tags: [gestao-executiva, ciso, governance, responsabilidades]
sidebar_position: 10
---

# 🏛️ Gestão Executiva / CISO

## Visão Geral

Gestão Executiva **dá direção e garante condições de aplicação**.  
Sem patrocínio ao mais alto nível, segurança perde prioridade e recursos. CISO traduz estratégia em programas executáveis.

### Responsabilidades Principais
- Patrocinam e asseguram condições de aplicação do SbD-ToE
- Definem orçamento e apoiam a escolha de ferramentas e formação
- Assumem responsabilidade final pela governação da segurança
- Tomam decisões estratégicas sobre risco residual

### Contexto Organizacional
Este papel é **central em NIS2 e DORA**, que explicitamente atribuem ao órgão de gestão a **responsabilidade pela supervisão e execução** de medidas de cibersegurança e resiliência operacional digital.

## Enquadramento Regulatório

**NIS2** e **DORA** atribuem **responsabilidade explícita ao órgão de gestão** pela segurança digital e resiliência operacional.

---

## Atividades por Capítulo

### Cap. 01 - Classificação de Aplicações
Publicar **políticas organizacionais formais** (Classificação de Risco, Aceitação de Risco, Revisão Periódica, Rastreabilidade/Auditoria) para assegurar critérios uniformes.

**User Stories:**
- [US-09: Políticas organizacionais formais](/sbd-toe/sbd-manual/classificacao-aplicacoes/aplicacao-lifecycle#us-09--políticas-organizacionais-formais) — Operação uniforme e auditável

### Cap. 02 - Requisitos de Segurança
Aprovar **modelos de requisitos mínimos** e publicar política de aplicação com formação para equipas técnicas.

**User Stories:**
- [US-07: Publicação de política de aplicação](/sbd-toe/sbd-manual/requisitos-seguranca/aplicacao-lifecycle#us-07--publicação-de-política-de-aplicação-de-requisitos) — Procedimentos e SLAs claros (com GRC)

### Cap. 04 - Arquitetura Segura
Estabelecer **processo formal de aprovação de arquitetura para L3**, com comité técnico ou governance review.

**User Stories:**
- [US-15: Aprovação formal de arquitetura L3](/sbd-toe/sbd-manual/arquitetura-segura/aplicacao-lifecycle#us-15--aprovação-formal-de-arquitetura-para-l3) — Mitigar riscos estruturais antes do go-live (com Arquitetos)

### Cap. 05-09 - Tooling e Infraestrutura
Apoiar **investimento em ferramentas** (SCA, SAST, DAST, SBOM, policy engines) e processos automatizados.

### Cap. 07 - CI/CD Seguro
Visualizar **dashboard de métricas de CI/CD** (cobertura, exceções, gate blocks, tempo remediação) para decisão informada.

**User Stories:**
- [US-12: Dashboard de métricas CI/CD](/sbd-toe/sbd-manual/cicd-seguro/aplicacao-lifecycle#us-12--métricas-e-conformidade-organizacional) — Ação corretiva estratégica

### Cap. 10 - Testes de Segurança
Estabelecer **critérios de aceitação de segurança por release** e processo de aceitação de risco residual.

**User Stories:**
- [US-07: Critérios de aceitação por release](/sbd-toe/sbd-manual/testes-seguranca/aplicacao-lifecycle#us-07---critérios-de-aceitação-de-segurança-por-release) — Decisões go/no-go informadas

### Cap. 11 - Deploy e Operações
Decidir sobre **riscos elevados em produção**, garantir rastreabilidade commit → build → release → deploy.

**User Stories:**
- [US-07: Rastreabilidade ponta-a-ponta](/sbd-toe/sbd-manual/deploy-seguro/aplicacao-lifecycle#us-07--rastreabilidade-ponta-a-ponta) — Auditar decisões de risco

### Cap. 13 - Formação e Onboarding
Executar **simulações de incidentes** (war room) regularmente, definir KPIs de capacitação, garantir formação mínima para terceiros, definir trilho obrigatório por perfil de contractor.

**User Stories:**
- [US-04: Simulações de incidentes (war room)](/sbd-toe/sbd-manual/formacao-onboarding/aplicacao-lifecycle#us-04--simulações-de-incidentes-war-room) — Validar processos de resposta (com GRC)
- [US-11: KPIs de capacitação](/sbd-toe/sbd-manual/formacao-onboarding/aplicacao-lifecycle#us-11--kpis-de-capacitação) — Avaliar impacto real (com GRC)
- [US-12: Formação mínima para terceiros](/sbd-toe/sbd-manual/formacao-onboarding/aplicacao-lifecycle#us-12--formação-mínima-obrigatória-para-terceiros) — Cumprir NIS2/DORA (com GRC)
- [US-13: Trilho formativo para contractors](/sbd-toe/sbd-manual/formacao-onboarding/aplicacao-lifecycle#us-13--trilho-formativo-obrigatório-para-contractors) — SLA antes de acesso técnico (com Training Manager)

### Cap. 14 - Governança e Contratação
Definir e monitorizar **KPIs de governação**, designar Security Champion por aplicação crítica, consolidar e reportar KPIs, formalizar modelo de governação com alçadas.

**User Stories:**
- [US-01: KPIs de governação](/sbd-toe/sbd-manual/governanca-contratacao/aplicacao-lifecycle#us-01--kpis-de-governação) — Avaliar eficácia SbD-ToE
- [US-05: Designação de Security Champion](/sbd-toe/sbd-manual/governanca-contratacao/aplicacao-lifecycle#us-05--designação-formal-de-security-champion) — Responsabilização clara
- [US-08: Consolidação e reporte de KPIs](/sbd-toe/sbd-manual/governanca-contratacao/aplicacao-lifecycle#us-08--consolidação-e-reporte-de-kpis) — Avaliar maturidade organizacional
- [US-09: Modelo de governação formal](/sbd-toe/sbd-manual/governanca-contratacao/aplicacao-lifecycle#us-09--modelo-de-governação-formal-com-alçadas) — Autoridade apropriada (com AppSec)

---

## Referências aos Capítulos

Para contexto e enquadramento completo:

- [Cap. 01 - Classificação de Aplicações](/sbd-toe/sbd-manual/classificacao-aplicacoes/intro)
- [Cap. 02 - Requisitos de Segurança](/sbd-toe/sbd-manual/requisitos-seguranca/intro)
- [Cap. 04 - Arquitetura Segura](/sbd-toe/sbd-manual/arquitetura-segura/intro)
- [Cap. 05 - Dependências e SBOM](/sbd-toe/sbd-manual/dependencias-sbom-sca/intro)
- [Cap. 07 - CI/CD Seguro](/sbd-toe/sbd-manual/cicd-seguro/intro)
- [Cap. 09 - Containers e Imagens](/sbd-toe/sbd-manual/containers-imagens/intro)
- [Cap. 10 - Testes de Segurança](/sbd-toe/sbd-manual/testes-seguranca/intro)
- [Cap. 11 - Deploy Seguro](/sbd-toe/sbd-manual/deploy-seguro/intro)
- [Cap. 12 - Monitorização e Operações](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro)
- [Cap. 13 - Formação e Onboarding](/sbd-toe/sbd-manual/formacao-onboarding/intro)
- [Cap. 14 - Governança e Contratação](/sbd-toe/sbd-manual/governanca-contratacao/intro)
