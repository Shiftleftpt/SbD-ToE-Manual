---
id: 05-identidade-privilegios
title: Identidade, Autenticação e Autorização
description: Quem tem permissão para fazer acontecer em cada contexto
sidebar_label: 5️⃣ Identidade e Privilégios
sidebar_position: 6
ai_generated: false
---

# Identidade, Autenticação e Autorização (IAM)

## O Espaço Compartilhado de Decisão

A gestão de identidades e privilégios atravessa todos os domínios do SDLC, incluindo:

- Utilizadores humanos (desenvolvedores, DevOps, administradores)
- Contas técnicas (serviços, aplicações, funções)
- Pipelines automatizados e orquestradores
- Agentes de software (bots, assistentes, monitores)

## A Pergunta Crítica

À medida que a automação cresce, a pergunta sobre segurança muda:

- **Antes**: "Quem fez isto?"
- **Agora**: "Quem tinha permissão para isto acontecer?"

Esta mudança reflete a realidade: nem todas as ações são explicadas por intenção humana direta.

## Afetação Transversal

O IAM como cross-cutting concern afeta:

### Arquitetura (Cap. 04)
- Desenho de fronteiras entre domínios
- Isolamento de componentes críticos
- Separação entre contextos de execução

### Desenvolvimento (Cap. 06)
- Permissões para acesso a código-fonte
- Quem pode fazer merge em branches protegidas
- Quem pode alterar configurações sensíveis

### CI/CD (Cap. 07)
- Identidade dos pipelines
- Escopo de permissões de deploy
- Assinatura de artefatos

### Operações (Cap. 12)
- Acesso a ambientes produtivos
- Quem pode executar operações críticas
- Rotação de credenciais

### Governação (Cap. 14)
- Aprovação centralizada de privilégios
- Segregação de funções entre papéis
- Auditoria de mudanças de permissões

## Princípio Fundamental

> **Privilégios mínimos**: Toda a identidade (humana ou técnica) tem apenas as permissões estritamente necessárias para cumprir o seu papel.

Este princípio, aplicado consistentemente, previne que erros isolados se tornem sistémicos.
