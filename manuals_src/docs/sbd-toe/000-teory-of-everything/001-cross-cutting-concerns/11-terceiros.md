---
id: 11-terceiros
title: Gestão de Terceiros e Fornecedores
description: Confiança por extensão através de dependências operacionais
sidebar_label: 1️⃣1️⃣ Terceiros
sidebar_position: 12
ai_generated: false
---

# Gestão de Terceiros e Fornecedores

## Confiança por Extensão

Cada serviço externo é uma **extensão implícita do sistema**.

Quando um software utiliza SaaS, APIs externas ou serviços especializados, a fronteira de segurança da organização expande-se. A segurança do sistema é agora afetada por:

- Conformidade do fornecedor
- Práticas de segurança dele
- Vulnerabilidades nos seus sistemas
- Acesso deles aos nossos dados

## Tipos de Terceiros

### SaaS e Plataformas Cloud
- Processamento de dados
- Hospedagem de infraestrutura
- Serviços especializados

### APIs Externas
- Pagamentos
- Comunicações
- Integrações de dados

### Fornecedores de Ferramentas
- Ferramentas de desenvolvimento
- Plataformas de CI/CD
- Sistemas de monitorização

### Provedores de Dados
- APIs de dados públicos
- Feeds de inteligência de ameaças
- Datasets para ML

## Afetação Transversal

### Requisitos (Cap. 02)
- Requisito: Fornecedores devem estar conformes a normas
- Requisito: Contrato define responsabilidades de segurança

### Arquitetura (Cap. 04)
- Isolamento de serviços críticos
- Fallbacks em caso de falha de terceiro
- Redundância geográfica

### Supply Chain (Cap. 05)
- SBOM de terceiros (quem fornece o quê?)
- Rastreabilidade de acesso
- Verificação de integridade

### Dados (Cap. 02, 06)
- Classificação de dados compartilhados
- Criptografia em trânsito
- Limite de dados processados

### Operações (Cap. 12)
- Monitoramento de disponibilidade de terceiro
- Alertas de anomalias
- Planos de contingência

### Governação (Cap. 14)
- Avaliação de risco de terceiros
- Contracts com SLAs e requisitos de segurança
- Auditoria periódica

## Responsabilidade Partilhada

No modelo de responsabilidade partilhada:

- **Fornecedor é responsável por**: Segurança da sua plataforma, compliance da sua infraestrutura
- **Organização é responsável por**: Como usa o serviço, proteção de dados antes de enviar, acesso concedido ao serviço
- **Ambos são responsáveis por**: Resposta a incidentes, comunicação de vulnerabilidades

## Princípio Fundamental

> **Verificação Contínua**: Nenhum terceiro é confiável por defeito. Todos são avaliados, auditados e monitorados continuamente.

A confiança em terceiros é uma decisão de risco, não um facto.
