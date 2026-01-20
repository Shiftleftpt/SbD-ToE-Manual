---
id: uso-ferramentas-automatizadas-iac
title: 🛠️ Uso de Ferramentas Automatizadas e Assistidas na Autoria de IaC
description: Regras prescritivas para uso seguro de automação/assistência na escrita e alteração de IaC, com validações e evidência por nível de risco
tags: [tipo:addon, iac, automacao, assistencia, validacao, evidencias, supply-chain]
---

# 🛠️ Uso de Ferramentas Automatizadas e Assistidas na Autoria de IaC

A escrita e alteração de Infraestrutura como Código é frequentemente suportada por **automação** (templates, geradores, normalizadores, snippets, scripts) e por **mecanismos assistidos** (sugestões e composição).  
Estas ferramentas aumentam produtividade, mas introduzem riscos específicos: alterações de baixa explicabilidade, defaults inseguros, permissões excessivas, recursos inesperados e exposição involuntária de informação sensível.

Este documento define **o que é aceitável**, **o que é proibido**, e **que validações e evidências são obrigatórias** para garantir que automação/assistência não reduz controlo, rastreabilidade e auditabilidade.

---

## 1) Princípio base: sugestão ≠ decisão

Independentemente da origem, **o IaC proposto é sempre tratado como entrada não confiável**.  
A decisão de executar (`apply`) é sempre humana e formalizada por gates e aprovações (proporcional ao risco).

---

## 2) Padrões aceitáveis vs proibidos

### ✅ Aceitável (com controlo)

- Gerar **rascunhos** de IaC (skeletons) para posterior revisão humana.
- Normalizar formatação/estrutura (ex.: reorganização de ficheiros) desde que haja `plan` e validações.
- Gerar documentação e comentários (não executáveis) a partir do código.
- Criar propostas de mudança em branches/PRs com execução obrigatória de `plan` e scanners.

### ❌ Proibido (por defeito)

- Qualquer mecanismo que execute `apply` em produção sem gates e aprovação formal.
- Alterações automáticas “em massa” sem explicabilidade e sem correlação com risco/impacto.
- Publicar `plan`, logs detalhados ou diffs sensíveis em sistemas externos sem minimização/redaction.
- Introduzir dependências/módulos/providers novos sem governança (allowlist + pinning + revisão).

> Exceções só são aceitáveis com registo formal (TTL, owner, compensações) e aprovação conforme criticidade.

---

## 3) Classes de erro típicas em IaC automatizado/assistido

Estas classes devem ser assumidas como risco de base e cobertas por validação semântica:

1. **Recursos “alucinatórios” / inesperados**: criação de recursos não pretendidos (serviços, endpoints, regras).
2. **Defaults inseguros**: cifragem desligada, logging ausente, permissões “abertas”.
3. **IAM demasiado amplo**: wildcards, admin roles, cross-account indevido.
4. **Exposição de rede**: security groups permissivos, portas públicas, redes planas.
5. **Destruição acidental**: `destroy` implícito, recreações, substituições destrutivas.
6. **Drift mascarado**: alterações indiretas por providers/módulos, upgrades não controlados.
7. **Exfiltração por logs/artefactos**: publicação indevida de topologia, IDs, endpoints e segredos.

---

## 4) Validações obrigatórias (gates) e evidência mínima

### 4.1 Gates mínimos (sempre aplicáveis)

- **Lint/sintaxe**: validação de formato e consistência.
- **Scanning de segurança**: misconfigurations, exposições e padrões perigosos.
- **Policy-as-code**: bloqueio de violações críticas.
- **Secret scanning**: impedir segredos em repo/logs/artefactos.

### 4.2 Validação semântica do `plan` (obrigatória quando aplicável)

- Impacto do `plan`: criação/alteração/destruição por recurso e ambiente.
- Permissões efetivas: aumento de privileges, wildcards, admin roles.
- Exposição: endpoints públicos, regras de rede permissivas, storage público.
- Cifragem/logging: recursos críticos sem garantias mínimas.
- Diffs inesperados: upgrades e mudanças indiretas.

### 4.3 Evidência mínima (auditável)

- `plan` associado ao PR/MR + commit + ambiente.
- Relatórios de scanners/policies associados ao mesmo PR/MR.
- Registo de aprovações antes de `apply` (quem, quando, porquê).
- Retenção dos artefactos proporcional ao risco.

---

## 5) Tratamento de sistemas externos

Qualquer sistema externo que processe:
- conteúdo do repositório,
- `plan`,
- logs,
- diffs,
- outputs,

deve ser tratado como **dependência de segurança**:

- classificado e autorizado organizacionalmente;
- sujeito a requisitos de logging/retenção e isolamento;
- sujeito a regras de minimização de contexto (**no secrets / no infra topology**);
- sujeito a obrigações contratuais quando aplicável.

---

## ⚖️ Proporcionalidade L1–L3

| Dimensão | L1 | L2 | L3 |
|---|---|---|---|
| Uso de automação/assistência | Permitido com revisão | Permitido com gates bloqueantes | Permitido com gates + SoD reforçada |
| Validação semântica do `plan` | Recomendado | Obrigatório | Obrigatório (reforçado) |
| Aprovação antes de `apply` | Simples | 2º revisor | Dupla aprovação + janela de mudança |
| Evidência e retenção | Básica | Obrigatória | Obrigatória + retenção reforçada |
| Integrações externas | Restringir | Minimizar e redigir | Minimizar+redigir + controlo reforçado |

---

## ✅ Checklist de controlo por projeto

- [ ] Automação/assistência é usada apenas para proposta (não para execução não controlada)
- [ ] Gates mínimos ativos (lint, scanning, policies, secret scanning)
- [ ] Validação semântica do `plan` aplicada quando relevante
- [ ] `plan` e relatórios correlacionados com PR/MR + aprovação
- [ ] Integrações externas seguem minimização de contexto e redaction
- [ ] Exceções são formais, temporárias e com compensações
