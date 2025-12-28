---
id: 03-gestao-risco
title: Gestão de Risco
description: O eixo estruturante que proporciona todas as decisões de segurança
sidebar_label: 3️⃣ Gestão de Risco
sidebar_position: 4
ai_generated: false
---

# Gestão de Risco como Cross-Cutting Concern

## O Eixo Estruturante

A gestão de risco constitui o **eixo estruturante do SbD-ToE**. Todas as decisões de segurança são proporcionais ao risco, incluindo:

- **Seleção de requisitos aplicáveis** — Nem todo o requisito se aplica igualmente a todos os sistemas
- **Profundidade de validação e teste** — L1 exige mais rigor que L3
- **Nível de evidência exigido** — A criticidade determina o volume de artefatos
- **Mecanismos de governação e aprovação** — Sistemas críticos exigem gates mais rigorosos

## Uma perspetiva crítica

No SbD-ToE, o risco não se limita ao produto final. **Abrange explicitamente o processo de engenharia**, incluindo:

- Fluxos de desenvolvimento
- Ferramentas utilizadas
- Automatismos em pipelines
- Decisões de arquitetura
- Acesso a ambientes

## Proporcionalidade em Prática

A proporcionalidade manifesta-se através da **matriz L1-L3**:

| Nível | Criticidade | Validação Esperada | Evidência | Aprovação |
|-------|-------------|-------------------|-----------|-----------|
| **L1** | Crítica | Máxima | Completa e auditável | Multi-gate, formal |
| **L2** | Média | Moderada | Essencial, rastreável | Dupla validação |
| **L3** | Baixa | Básica | Verificada | Self-service com logs |

## Implicação para outros concerns

Todos os outros cross-cutting concerns são **proporcionais ao risco**:

- IAM mais rigoroso em L1, relaxado em L3
- Supply chain mais intensamente auditada em L1
- Requisitos mais explícitos e testados em L1
- Rastreabilidade mais granular em L1

Isto garante eficiência sem sacrificar segurança.
