---
id: 06-dados
title: Gestão de Dados
description: O ativo inquieto que circula por todo o SDLC
sidebar_label: 6️⃣ Gestão de Dados
sidebar_position: 7
ai_generated: false
---

# Gestão de Dados como Cross-Cutting Concern

## O Ativo Inquieto

Os dados raramente ficam quietos. Circulam por:

- **Ambientes** — desenvolvimento, teste, staging, produção
- **Logs** — aplicacionais, infraestruturais, de segurança
- **Testes** — onde se usam dados reais ou sintéticos
- **Integrações** — fluxos entre sistemas
- **Fornecedores** — SaaS, APIs externas, terceiros

## Mais que Confidencialidade

A gestão de dados abrange:

- **Classificação** — Que dados existem e qual é a sua sensibilidade
- **Confidencialidade** — Quem pode ver os dados
- **Integridade** — Quem pode modificar os dados
- **Retenção** — Por quanto tempo os dados devem ser guardados
- **Localização** — Onde os dados residem (geograficamente, em que ambientes)
- **Linhagem** — Conhecer a origem e transformações dos dados

## Afetação Transversal

### Requisitos (Cap. 02)
- Classificar dados que a aplicação processa
- Definir fluxos permitidos
- Estabelecer limites de retenção

### Arquitetura (Cap. 04)
- Segregar dados por nível de sensibilidade
- Encriptar dados em trânsito e em repouso
- Implementar borders de privacidade

### Desenvolvimento (Cap. 06)
- Não usar dados reais em desenvolvimento
- Máscara de dados sensíveis em testes
- Validação de onde os dados fluem

### CI/CD (Cap. 07)
- Integração de testes sem expor dados reais
- Artefatos construídos sem informação sensível
- Logs de pipeline sem captura de secrets

### Observabilidade (Cap. 12)
- Logs estruturados sem dados sensíveis visíveis
- Monitoramento que detecta exfiltração
- Retenção de evidência sem desperdício

## Princípio Fundamental

> **Dados como propriedade**: Os dados devem ser tratados como o ativo crítico que são. A sua proteção é responsabilidade contínua, não um ponto de controlo.

Esta perspetiva garante que a segurança da informação não é uma função isolada, mas uma **disciplina contínua de intenção e contenção**.
