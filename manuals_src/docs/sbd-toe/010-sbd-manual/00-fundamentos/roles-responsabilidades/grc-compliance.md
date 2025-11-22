---
description: Responsabilidades de GRC/Compliance no SbD-ToE
id: grc-compliance
sidebar_label: 📑 GRC / Compliance
sidebar_position: 11
tags:
- auditores
- auditoria
- cicd
- compliance
- governance
- grc
- responsabilidades
title: GRC / Compliance
---


# 📑 GRC / Compliance

## Visão Geral

GRC assegura que **práticas internas estão alinhadas com normas e regulamentos externos**.  
Coordena auditorias, mantém documentação de risco residual, gere exceções e fornece prova documental exigida por NIS2, DORA, GDPR.

### Responsabilidades Principais
- Asseguram rastreabilidade com normas (SSDF, ISO) e regulamentos (NIS2, DORA, GDPR, AI Act)
- Monitorizam exceções e garantem documentação de risco residual
- Coordenam auditorias internas e externas
- Ligam requisitos técnicos a obrigações legais

### Contexto Organizacional
É o garante da **prova documental** exigida por NIS2 (auditoria, reporte) e DORA (resiliência operacional e gestão de terceiros). Sem GRC, não há demonstração de conformidade.

## Enquadramento Regulatório

Fornece prova documental exigida em:
- **NIS2**: Auditorias, reporting, rastreabilidade
- **DORA**: Resiliência, governação de terceiros, testes
- **GDPR**: Demonstração de conformidade (*accountability*)

---

## Atividades por Capítulo

### Cap. 01 - Classificação de Aplicações
Registar **risco residual** após aplicar controlos, registar aceitações com TTL explícito, consolidar KPIs mensais/trimestrais sobre classificação e exceções.

**User Stories:**
- [US-04: Registro de risco residual](/sbd-toe/sbd-manual/classificacao-aplicacoes/aplicacao-lifecycle#us-04--registro-de-risco-residual) — Fundamentar decisões de aceitação
- [US-05: Aceitações com TTL e re-aprovação](/sbd-toe/sbd-manual/classificacao-aplicacoes/aplicacao-lifecycle#us-05--aceitações-com-ttl-e-alerta-de-re-aprovação) — Evitar exceções permanentes
- [US-08: KPIs de governação da classificação](/sbd-toe/sbd-manual/classificacao-aplicacoes/aplicacao-lifecycle#us-08--kpis-de-governação-da-classificação) — Demonstrar maturidade

### Cap. 02 - Requisitos de Segurança
Publicar política de aplicação e providenciar formação (com Gestão/CISO).

**User Stories:**
- [US-07: Política de aplicação de requisitos](/sbd-toe/sbd-manual/requisitos-seguranca/aplicacao-lifecycle#us-07--publicação-de-política-de-aplicação-de-requisitos) — Procedimentos claros (com Gestão Executiva/CISO)

### Cap. 07 - CI/CD Seguro
Rastrear **commit → pipeline → release** para suportar auditorias. Garantir exceções registadas, aprovadas e temporárias.

**User Stories:**
- [US-09: Rastreabilidade ponta-a-ponta](/sbd-toe/sbd-manual/cicd-seguro/aplicacao-lifecycle#us-09--rastreabilidade-ponta-a-ponta) — Suportar auditorias
- [US-10: Gestão de exceções](/sbd-toe/sbd-manual/cicd-seguro/aplicacao-lifecycle#us-10--gestão-de-exceções) — Evitar dívida técnica

### Cap. 08 - IaC e Infraestrutura
Mapear **ficheiro IaC → recurso → ambiente** para validar impacto e rastreabilidade. Garantir janelas de mudança e aprovações por papel. Registar exceções com prazo e contramedidas.

**User Stories:**
- [US-07: Rastreabilidade ficheiro → recurso → ambiente](/sbd-toe/sbd-manual/iac-infraestrutura/aplicacao-lifecycle#us-07--rastreabilidade-ficheiro--recurso--ambiente) — Validar impacto (com Auditores)
- [US-13: Janela de mudança e aprovações](/sbd-toe/sbd-manual/iac-infraestrutura/aplicacao-lifecycle#us-13--janela-de-mudança-e-aprovações-por-papel) — Reduzir risco operacional (com Auditores)
- [US-14: Exceções formais em IaC](/sbd-toe/sbd-manual/iac-infraestrutura/aplicacao-lifecycle#us-14--exceções-formais-em-iac) — Evitar dívida estrutural (com AppSec)

### Cap. 12 - Monitorização e Operações
Medir **MTTD e MTTR de incidentes**. Documentar conformidade entre controlos e requisitos regulatórios (SSDF, NIS2, ISO 27001).

**User Stories:**
- [US-11: MTTD e MTTR de incidentes](/sbd-toe/sbd-manual/monitorizacao-operacoes/aplicacao-lifecycle#us-11--mttd-e-mttr-de-incidentes) — Avaliar eficácia
- [US-12: Documentação de conformidade regulatória](/sbd-toe/sbd-manual/monitorizacao-operacoes/aplicacao-lifecycle#us-12--documentação-de-conformidade-regulatória) — Demonstrar alinhamento (com Auditoria)

### Cap. 13 - Formação e Onboarding
Medir **KPIs de capacitação**, executar simulações de incidentes, garantir formação mínima para terceiros, definir e recolher KPIs.

**User Stories:**
- [US-03: KPIs de capacitação](/sbd-toe/sbd-manual/formacao-onboarding/aplicacao-lifecycle#us-03--kpis-de-capacitação) — Avaliar impacto em auditoria
- [US-04: Simulações de incidentes](/sbd-toe/sbd-manual/formacao-onboarding/aplicacao-lifecycle#us-04--simulações-de-incidentes-war-room) — Validar processos (com Gestão)
- [US-11: KPIs detalhados de capacitação](/sbd-toe/sbd-manual/formacao-onboarding/aplicacao-lifecycle#us-11--kpis-de-capacitação) — Reportar conformidade (com Gestão)
- [US-12: Formação mínima para terceiros](/sbd-toe/sbd-manual/formacao-onboarding/aplicacao-lifecycle#us-12--formação-mínima-obrigatória-para-terceiros) — NIS2/DORA (com Gestão)

### Cap. 14 - Governança e Contratação
Validar **fornecedores de forma contínua**, executar validações periódicas de conformidade, validar formalmente onboarding de colaboradores.

**User Stories:**
- [US-01: Validação contínua de fornecedores](/sbd-toe/sbd-manual/governanca-contratacao/aplicacao-lifecycle#us-01--validação-contínua-de-fornecedores) — Conformidade contratual
- [US-07: Validações periódicas de conformidade](/sbd-toe/sbd-manual/governanca-contratacao/aplicacao-lifecycle#us-07--validações-periódicas-de-conformidade) — Detetar desvios (com AppSec)

### Transversal - Todos os Capítulos
Ligar **requisitos técnicos a obrigações legais** (NIS2, DORA, GDPR, AI Act). Coordenar auditorias e manter rastreabilidade documental.

---

## Referências aos Capítulos

Para contexto e enquadramento completo:

- [Cap. 01 - Classificação de Aplicações](/sbd-toe/sbd-manual/classificacao-aplicacoes/intro)
- [Cap. 02 - Requisitos de Segurança](/sbd-toe/sbd-manual/requisitos-seguranca/intro)
- [Cap. 04 - Arquitetura Segura](/sbd-toe/sbd-manual/arquitetura-segura/intro)
- [Cap. 07 - CI/CD Seguro](/sbd-toe/sbd-manual/cicd-seguro/intro)
- [Cap. 08 - IaC e Infraestrutura](/sbd-toe/sbd-manual/iac-infraestrutura/intro)
- [Cap. 09 - Containers e Imagens](/sbd-toe/sbd-manual/containers-imagens/intro)
- [Cap. 12 - Monitorização e Operações](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro)
- [Cap. 13 - Formação e Onboarding](/sbd-toe/sbd-manual/formacao-onboarding/intro)
- [Cap. 14 - Governança e Contratação](/sbd-toe/sbd-manual/governanca-contratacao/intro)
