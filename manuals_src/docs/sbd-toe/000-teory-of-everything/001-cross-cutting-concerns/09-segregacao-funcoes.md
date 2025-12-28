---
id: 09-segregacao-funcoes
title: Segregação de Funções e Responsabilidades
description: Proteção contra auto-aprovação e escalada descontrolada
sidebar_label: 9️⃣ Segregação de Funções
sidebar_position: 10
ai_generated: false
---

# Segregação de Funções e Responsabilidades

## O Princípio Clássico, Moderno

A segregação de funções é um princípio de segurança clássico: não deixar que a mesma pessoa decida, execute e aprove.

Mas em ambientes altamente automatizados, este princípio assume particular relevância:

- Quem escreve a política pode configurá-la?
- Quem faz deploy pode aprovação do deploy?
- Quem tem acesso aos logs pode apagar os seus próprios erros?

## Proteção Cognitiva e Processual

A segregação funciona em dois níveis:

### Cognitivo
Diferentes pessoas trazem perspetivas diferentes:
- O desenvolvedor vê "como fazer funcionar"
- O revisor vê "estamos dispostos a aceitar isto?"
- O operador vê "conseguimos isto em produção?"

Estas perspetivas revelam problemas que uma única pessoa não consegue ver.

### Processual
A segregação força a criação de processos:
- Requisições formais de acesso
- Aprovação documentada
- Auditoria da concessão

## Afetação Transversal

### Arquitetura (Cap. 04)
- Diferentes papéis no desenho de arquitetura
- Separação entre design e review
- Validação arquitetural independente

### Desenvolvimento (Cap. 06)
- Desenvolvedor vs. Revisor (code review obrigatório)
- Revisor vs. Integrador (merge em branch protegida)
- Diferentes acesso a ambientes

### CI/CD (Cap. 07)
- Pipeline vs. Aprovação humana
- Deploy em produção requer step separado
- Rollback autorizado apenas por certos papéis

### Operações (Cap. 12)
- Monitores vs. Responders
- Alertas vs. Ação manual
- Logs centralizados, acesso segregado

### Governação (Cap. 14)
- Approval workflows formais
- Segregação entre pedir, aprovar e auditar
- Impossibilidade de auto-aprovação

## Caso de Estudo: Deploy

Uma mudança de código envolve múltiplos papéis:

1. **Desenvolvedor** — escreve código
2. **Revisor (peer)** — valida qualidade e segurança
3. **Revisor (arquitetura)** — valida padrões
4. **Aprovador (produção)** — autoriza deploy
5. **Executor (CI/CD)** — executa deployment
6. **Auditor** — regista quem fez o quê e quando

Nenhum destes papéis substitui outro. Todos são essenciais.

## Princípio Fundamental

> **Distribuição de Poder**: Nenhuma entidade (pessoa ou sistema) deve poder decidir, executar e validar sozinha. O poder deve ser distribuído.

Isto não reduz eficiência — aumenta confiança.
