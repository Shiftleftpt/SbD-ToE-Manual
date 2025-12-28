---
id: intro
title: Cross-Cutting Concerns
description: Preocupações de segurança que atravessam transversalmente todos os domínios e fases do SDLC
sidebar_label: 📋 Visão Geral
sidebar_position: 1
ai_generated: false
---

# 🔗 Cross-Cutting Concerns no SbD-ToE

## O que são Cross-Cutting Concerns?

No **Security by Design – Theory of Everything**, um *cross-cutting concern* é uma preocupação de segurança que:

- **atravessa múltiplos domínios técnicos** (desenvolvimento, arquitetura, CI/CD, operações, governação)
- **reaparece em várias fases do SDLC** — não é um ponto de controlo isolado
- **afeta tanto o produto como o processo** que o cria
- **é definida de forma normativa** — independentemente de tecnologia ou stack
- **materializa-se através de múltiplas práticas especializadas** descritas em capítulos distintos do manual

Enquanto um capítulo técnico (ex.: CI/CD) responde a uma pergunta específica — *"como fazer deploy seguro?"* — os cross-cutting concerns respondem a perguntas que **atravessam todo o SDLC**: *"como gerimos identidades em todos os capítulos?"*, *"como rastreamos evidência de segurança?"*.

---

## Porquê são críticos?

Sem explicitação formal de cross-cutting concerns, acontece uma de duas coisas:

1. **Fragmentação** — cada equipa resolve o mesmo problema de formas diferentes, criando inconsistência
2. **Lacunas** — ninguém assume responsabilidade porque "aquilo devia estar noutro lado"

O SbD-ToE torna-os **explícitos, normativos e rastreáveis** — permitindo que:

- Práticas sejam consistentes em todos os capítulos
- Responsabilidades sejam claramente distribuídas
- Conformidade seja verificável top-down e bottom-up

---

## Conjunto Canónico do SbD-ToE

O SbD-ToE identifica **12 cross-cutting concerns** fundamentais:

| Concern | Descrição |
|---------|-----------|
| **🎯 Gestão de Risco** | Eixo estruturante — proporcionalidade ao risco em todas as decisões de segurança |
| **📋 Requisitos de Segurança** | Contrato normativo entre intenção e execução — aplicados em todos os domínios |
| **🔐 Identidade, Autenticação e Autorização** | Gestão de identidades humanas, técnicas, pipelines e agentes |
| **💾 Gestão de Dados** | Classificação, confidencialidade, integridade, retenção — atravessa todo o SDLC |
| **🔗 Supply Chain de Software** | Dependências, imagens, código gerado — rastreabilidade contínua |
| **📊 Evidência, Rastreabilidade e Auditoria** | Ligação entre prescrição normativa e realidade operacional |
| **✂️ Segregação de Funções e Responsabilidades** | Proteção contra auto-aprovação e escalada não controlada de erros |
| **⚙️ Automação e Execução Delegada** | Pipelines, scripts, bots, agentes — executam decisões humanas à escala |
| **🤝 Gestão de Terceiros e Fornecedores** | Dependências operacionais e legais — confiança por extensão |
| **👥 Competência, Formação e Consciência** | Literacia de segurança — determina eficácia real de qualquer controlo |
| **📈 IA como Stress Test** | IA expõe fragilidades latentes nos princípios de segurança existentes |
| **🧭 Princípios Organizacionais** | Proporcionalidade, modularidade, prescritividade, responsabilidade partilhada, rastreabilidade |

---

## Como são integrados no manual?

Os cross-cutting concerns são **definidos uma única vez, de forma abstrata**, na camada normativa. Depois:

- **Capítulos técnicos** (01-14) materializam cada concern em práticas concretas
- **Ficheiros de rastreabilidade** (`canon/`) demonstram alinhamento top-down
- **Checklists e evidência** suportam validação bottom-up
- **Modelos de maturidade** permitem avaliar adoção organizacional

Esta arquitetura evita redundância, reduz ambiguidade e permite evolução contínua.

---

## Próximas secções

Selecione um concern abaixo para explorar definição formal, contexto histórico e aplicação prática no SbD-ToE:
