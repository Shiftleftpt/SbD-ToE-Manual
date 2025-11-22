---
id: gestao-codigo-fonte
title: Gestão Segura de Código-Fonte
sidebar_position: 0
description: Práticas para proteger branches, controlar alterações e garantir versionamento rastreável do código usado em pipelines.
tags: [branches, cicd, código-fonte, pipelines, revisão, scm]
---


# 📁 Gestão segura de código fonte

A segurança do pipeline começa **antes da execução automatizada** - começa no repositório. A gestão segura de código fonte é o **primeiro elo da cadeia CI/CD**, e garante que só código legítimo, revisto e rastreável chega à build.

> Um pipeline bem protegido não serve de nada se o repositório puder ser manipulado diretamente, silenciosamente ou sem validação.

---

## 🎯 Objetivos

- Garantir que **todo o código incluído no pipeline é legítimo e autorizado**;
- Prevenir alterações maliciosas ou acidentais aos branches de produção;
- Assegurar rastreabilidade, revisão e integridade do histórico de commits e tags.

---

## 🛠️ Práticas

1. **Proteção de branches principais (`main`, `release`, `prod`)**  
   - Impedir `push` direto: só permitir alterações via pull/merge request;
   - Exigir revisores (ex: dois olhos para L1, quatro olhos para L3).

2. **Revisão obrigatória com histórico auditável**  
   - Todas as alterações devem passar por revisão técnica;
   - Revisão deve ser rastreável, com logs preservados.

3. **Assinatura de commits ou tags em aplicações críticas**  
   - Para L3, é obrigatória a assinatura digital de commits ou pelo menos de tags de release;
   - Ex: GPG, Sigstore, SSH verified.

4. **Proibição de alteração de histórico (`force push`, `rebase` retroativo)**  
   - Repositórios devem bloquear `push --force` em branches protegidos;
   - A política de alterações deve ser claramente documentada.

5. **Gestão de permissões granular e com base em funções**  
   - Acesso de escrita restrito por branch ou projeto;
   - Integração com mecanismos de identidade empresarial (SSO, RBAC, etc.).

6. **Ciclo de vida de branches controlado**  
   - Branches devem ser limpos, com naming padronizado e tempo de vida conhecido;
   - Branches de curto prazo (feature/bugfix) não devem ter acesso a segredos.

---

## ⚖️ Aplicação proporcional por nível de risco

| Nível | Requisitos obrigatórios                     | Requisitos reforçados                             |
|-------|----------------------------------------------|---------------------------------------------------|
| **L1** | Proteção de branches; revisão mínima         | Naming padrão; sem `force push`                   |
| **L2** | Revisão obrigatória; bloqueio de histórico   | Política de merge e naming padronizada            |
| **L3** | Assinaturas digitais; acesso segregado       | Auditoria formal de alterações e tags protegidas  |

---

## 📌 Exemplos práticos

- **GitHub**  
  - Branch protection rules: impedir `force push`, exigir PR com aprovação;
  - Commits `verified` com GPG ou Sigstore (OIDC).

- **GitLab**  
  - Protected branches: controlo de escrita por membro;
  - Merge request rules com code owner approval.

- **Azure Repos**  
  - Branch policies: reviewers obrigatórios, build validation;
  - Proibição de squash ou rebase em branches críticos.

- **Bitbucket**  
  - Merge checks, branch restrictions, commit signature enforcement.

---

## 📉 Riscos mitigados

- Introdução de código malicioso diretamente no repositório (OSC&R: SC0001);
- Substituição silenciosa de código (OSC&R: CI0004);
- Publicações não autorizadas por tag ou branch à margem do processo;
- Manipulação do histórico para ocultar atividades maliciosas.

---
