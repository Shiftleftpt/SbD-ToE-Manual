---
id: 10-automacao
title: Automação e Execução Delegada
description: Decisões executadas à velocidade da máquina
sidebar_label: 🔟 Automação
sidebar_position: 11
ai_generated: false
---

# Automação e Execução Delegada

## Decisões à Escala

A automação não substitui decisões humanas — **executa-as à escala e à velocidade de máquinas**.

Um script que antes levava uma hora e era executado manualmente por uma pessoa agora executa em segundos, talvez centenas de vezes por dia, sem intervenção.

Isto é poderoso. E perigoso.

## O Que é Automação?

No contexto do SbD-ToE, automação inclui:

- **Pipelines CI/CD** — automatizam build, test, deploy
- **Scripts de infraestrutura** — automatizam provisionamento
- **Bots e orquestradores** — automatizam tarefas operacionais
- **Assistentes inteligentes** — automatizam sugestões e recomendações
- **Políticas e regras** — automatizam tomadas de decisão

## O Risco da Automação Inconsciente

Sem governação proporcional, a automação amplifica erros:

- Uma falha manual afeta 1 utilizador
- Uma falha automatizada afeta milhões
- Uma decisão manual é revista e questionada
- Uma decisão automatizada é executada sem questionamento

## Afetação Transversal

### CI/CD (Cap. 07)
- Gates automáticos (passar testes = deploy?)
- Políticas de merge automatizadas
- Rollback automático em caso de falha

### IaC (Cap. 08)
- Provisioning automático de infraestrutura
- Aplicação de políticas de compliance
- Rollback de alterações perigosas

### Testes (Cap. 10)
- Testes automatizados vs. validação manual
- Cobertura automática vs. caso crítico não testado

### Operações (Cap. 12)
- Alertas automáticos vs. confirmação humana
- Remediation automática com auditoria
- Escalation quando bots não conseguem

### Governação (Cap. 14)
- Limites claros do que pode ser automatizado
- Governação proporcional ao impacto
- Rastreabilidade de decisões automatizadas

## Governação de Automação

A regra de ouro:

> **Automação proporcional ao impacto**: Quanto maior o impacto potencial, maior o número de validações e gates humanos antes de execução.

**Exemplos:**

- L3 (baixo impacto): Pode ser 100% automatizado com logs
- L2 (médio impacto): Automático com pós-validação
- L1 (alto impacto): Automático com pré-aprovação humana

## Responsabilidade Distribuída

Quem é responsável pelo erro de um bot?

No SbD-ToE, responsabilidade é distribuída:

- **Quem desenhou o bot** — responsável pela lógica
- **Quem aprovou o bot** — responsável pela autorização
- **Quem o deixou executar sozinho** — responsável pelo controlo
- **Quem o monitora** — responsável pela detecção de anomalias

Isto garante que a automação nunca é "invisível".

## Princípio Fundamental

> **Automação Consciente**: Tudo o que é automatizado deve ser monitorado, auditado e, se necessário, reversível em tempo real.
