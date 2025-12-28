---
id: 07-supply-chain
title: Supply Chain de Software
description: Rastreabilidade de tudo o que entra no sistema
sidebar_label: 7️⃣ Supply Chain
sidebar_position: 8
ai_generated: false
---

# Supply Chain de Software como Cross-Cutting Concern

## O Software que Não Escrevemos

Grande parte do software moderno não é escrita por quem a mantém. **É composto.**

Isso inclui:
- **Dependências de terceiros** — bibliotecas, frameworks, pacotes
- **Imagens e containers** — bases de SO, runtimes, camadas pré-construídas
- **Ferramentas** — compiladores, scanners, orquestradores
- **Código gerado** — templates, scaffolding, assistência de IA
- **Dados de configuração** — políticas, policies, regras externas

Cada um destes elementos traz consigo pressupostos invisíveis.

## Afetação Transversal

### Requisitos (Cap. 02)
- Requisito: Todas as dependências devem ter licenças conhecidas e compatíveis
- Requisito: Vulnerabilidades em dependências exigem plano de mitigação

### Arquitetura (Cap. 04)
- Decisão: Quais dependências são permitidas
- Decisão: Isolamento de dependências perigosas
- Decisão: Pinning de versões críticas

### Supply Chain (Cap. 05)
- SBOM completo (Software Bill of Materials)
- Rastreabilidade de origem (provenância)
- Verificação de integridade
- Resposta a vulnerabilidades

### CI/CD (Cap. 07)
- Scanning de dependências em build-time
- Bloqueio de versões vulneráveis
- Atualização contínua de patches
- Assinatura de artefatos produzidos

### Operações (Cap. 12)
- Monitoramento de vulnerabilidades em runtime
- Planos de resposta a incidentes em dependências
- Rastreabilidade de "quem introduziu isto"

## Princípio Fundamental

> **Confiança Verificada**: Nenhuma dependência é de confiança por defeito. Todas são verificadas quanto à origem, integridade e vulnerabilidades conhecidas.

A supply chain é a única perspetiva que permite à organização dizer "nós sabemos o que está em produção".
