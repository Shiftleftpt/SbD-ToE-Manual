---
id: 08-evidencia-rastreabilidade
title: Evidência, Rastreabilidade e Auditoria
description: A memória e governabilidade da segurança
sidebar_label: 8️⃣ Evidência e Rastreabilidade
sidebar_position: 9
ai_generated: false
---

# Evidência, Rastreabilidade e Auditoria

## A Memória da Segurança

Sem memória não há governação. Sem evidência não há confiança.

A rastreabilidade liga:
- **Decisões** → Práticas (porque fazemos isto?)
- **Práticas** → Artefactos (que prova temos?)
- **Artefactos** → Responsabilidades (quem é responsável?)

## O que é Rastreabilidade?

Rastreabilidade é a capacidade de:

1. **Demonstrar conformidade** — "Nós cumprimos este requisito"
2. **Auditar decisões** — "Isto foi decidido assim por esta razão"
3. **Justificar excepções** — "Isto não foi cumprido mas temos plano"
4. **Investigar incidentes** — "Como é que isto chegou aqui?"
5. **Melhorar continuamente** — "O que aprendemos com isto?"

## Afetação Transversal

### Requisitos (Cap. 02)
- Cada requisito é rastreável a normas e regulações
- Cada requisito tem critérios de aceitação mensuráveis

### Desenvolvimento (Cap. 06)
- Commits linkados a requisitos
- Code reviews documentados
- Mudanças rastreadas a approvals

### Testes (Cap. 10)
- Testes linkados a requisitos
- Cobertura medida e rastreada
- Falhas investigadas

### Operações (Cap. 12)
- Logs imutáveis e auditáveis
- Mudanças rastreadas
- Incidentes investigáveis

### Governação (Cap. 14)
- Policies documentadas
- Exceções formalmente aprovadas
- Revisões periódicas com evidência

## Artefatos Mínimos

O SbD-ToE define artefatos mínimos para cada capítulo:

- **Código** — commits, PRs, reviews, builds
- **Testes** — cobertura, resultados, artefatos
- **Infraestrutura** — IaC com versionamento, change logs
- **Operações** — logs estruturados, alertas, métricas
- **Governação** — políticas, aprovações, exceções

## Princípio Fundamental

> **Verificabilidade**: Se não consegues demonstrar que algo foi feito, é como se não tivesse sido feito.

A evidência não é burocracia — é a única forma de saber se a segurança é real ou apenas teórica.
