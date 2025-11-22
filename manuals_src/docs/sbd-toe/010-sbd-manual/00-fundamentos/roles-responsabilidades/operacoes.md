---
id: operacoes
title: Operações (Ops)
sidebar_label: 🔧 Operações (Ops)
description: Responsabilidades de Operações no SbD-ToE
tags: [incident-response, operacoes, ops, responsabilidades, runtime]
sidebar_position: 7
---

# 🔧 Operações (Ops)

## Visão Geral

Ops mantém **integridade em runtime**, garantindo disponibilidade, aplicação de patches e resposta coordenada a incidentes.  
Responsável por **monitorização contínua**, configuração de alertas e execução de playbooks de resposta.

### Responsabilidades Principais
- Asseguram execução segura em runtime
- Implementam patches e atualizações regulares
- Coordenam resposta a incidentes (Cap. 12)
- Mantêm disponibilidade e resiliência operacional

### Contexto Organizacional
As Ops são **linha da frente no cumprimento de NIS2** (resposta a incidentes, notificação em 24h) e **DORA** (continuidade operacional e gestão de eventos críticos).

## Enquadramento Regulatório

Linha da frente em:
- **NIS2**: Notificação de incidentes em 24h
- **DORA**: Continuidade operacional e resiliência

---

## Atividades por Capítulo

### Cap. 09 - Containers e Imagens
Manter **baseline de containers** atualizado, aplicar patches de segurança em imagens base de forma sistemática.

### Cap. 11 - Deploy Seguro
Assegurar **resiliência em deploys**, coordenar rollback quando necessário, validar procedimentos de recuperação.

### Cap. 12 - Monitorização e Operações
Configurar **alertas críticos com SLAs**, integrar alertas com playbooks de incident response, correlacionar eventos multi-fonte, afinar alertas para reduzir falsos positivos, coordenar resposta a incidentes, trabalhar com métricas e manter disponibilidade.

**User Stories:**
- [US-03: Alertas críticos com SLAs](/sbd-toe/sbd-manual/monitorizacao-operacoes/aplicacao-lifecycle#us-03--alertas-críticos-com-slas-definidos) — Resposta atempada a incidentes
- [US-10: Playbooks de resposta a incidentes](/sbd-toe/sbd-manual/monitorizacao-operacoes/aplicacao-lifecycle#us-10--integração-de-alertas-com-playbooks-de-resposta-a-incidentes) — Ação rápida e coordenada
- [US-05: Correlação de eventos](/sbd-toe/sbd-manual/monitorizacao-operacoes/aplicacao-lifecycle#us-05--correlação-de-eventos-entre-múltiplas-fontes) — Deteção de padrões suspeitos (com AppSec)
- [US-06: Validação e afinação de alertas](/sbd-toe/sbd-manual/monitorizacao-operacoes/aplicacao-lifecycle#us-06--validação-e-afinação-de-alertas) — Reduzir falsos positivos (com AppSec)

### Cap. 13 - Formação e Onboarding
Participar em **simulações de incidentes** (war room, tabletop exercises) para validar processos de resposta.

### Cap. 14 - Governança e Contratação
Documentar **incidentes e lições aprendidas**, garantindo melhoria contínua dos processos de resposta.

---

## Referências aos Capítulos

Para contexto e enquadramento completo:

- [Cap. 09 - Containers e Imagens](/sbd-toe/sbd-manual/containers-imagens/intro)
- [Cap. 11 - Deploy Seguro](/sbd-toe/sbd-manual/deploy-seguro/intro)
- [Cap. 12 - Monitorização e Operações](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro)
- [Cap. 13 - Formação e Onboarding](/sbd-toe/sbd-manual/formacao-onboarding/intro)
- [Cap. 14 - Governança e Contratação](/sbd-toe/sbd-manual/governanca-contratacao/intro)
