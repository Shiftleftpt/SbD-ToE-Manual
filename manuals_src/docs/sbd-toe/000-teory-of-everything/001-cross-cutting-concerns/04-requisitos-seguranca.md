---
id: 04-requisitos-seguranca
title: Requisitos de Segurança
description: O contrato normativo entre intenção e execução
sidebar_label: 4️⃣ Requisitos de Segurança
sidebar_position: 5
ai_generated: false
---

# Requisitos de Segurança como Cross-Cutting Concern

## Requisitos como Promessas

Os requisitos de segurança representam o **contrato normativo entre intenção e execução**. Não são apenas listas — são promessas documentadas.

Promessas de que:
- Certos limites não serão ultrapassados
- Certas decisões terão sempre validação humana
- Certos erros não escalarão silenciosamente
- Certos dados seguirão fluxos conhecidos e auditáveis

## Independência de Tecnologia

Os requisitos de segurança são deliberadamente **independentes de tecnologia, tooling ou stack específica**.

Isto significa:
- Um requisito válido em 2024 continua válido em 2030
- Um requisito aplicável em Java é aplicável em Rust
- Um requisito do on-premises também vale para cloud

## Materialização Distribuída

Enquanto *cross-cutting concern*, os requisitos:

- **Aplicam-se simultaneamente** a código, infraestrutura, pipelines e organização
- **São reutilizados** e materializados em múltiplos capítulos técnicos
- **Permitem rastreabilidade top-down** (de normas para requisitos para práticas)
- **Permitem validação objetiva** — sabe-se quando um requisito é cumprido

## Exemplos de Requisitos Transversais

### "Outputs não são autoridade"
Aplicável a:
- Código gerado por IA (cap. 06)
- Configurações sugeridas (cap. 04)
- Padrões recomendados automaticamente (cap. 07)

**O requisito**: Qualquer output de sistema assistido requer validação e aprovação humana antes de integração.

### "Privilégios mínimos"
Aplicável a:
- Contas de serviço (cap. 04)
- Pipelines (cap. 07)
- Acesso a dados sensíveis (cap. 02, 12)
- Identidades de terceiros (cap. 05)

**O requisito**: Toda a identidade tem apenas as permissões mínimas para cumprir o seu papel.

### "Rastreabilidade contínua"
Aplicável a:
- Mudanças em código (cap. 06)
- Mutações de configuração (cap. 08)
- Acesso a ambientes (cap. 12)
- Decisões automatizadas (cap. 07)

**O requisito**: Cada ação significativa produz evidência auditável e imutável.
