---
id: design-seguro-pipelines
title: Design Seguro dos Pipelines
sidebar_position: 1
description: Regras de construção e revisão segura de pipelines como código, com triggers controlados e ambientes previsíveis.
tags: [cicd, pipelines, yaml, triggers, revisão, automação]
---


# 🧱 Design seguro dos pipelines

O design seguro dos pipelines CI/CD é um controlo fundamental para garantir que apenas alterações **legítimas, autorizadas e rastreáveis** são processadas automaticamente. O pipeline deve ser tratado como **infraestrutura sensível**, com as mesmas precauções de segurança aplicáveis a código fonte, scripts de infraestrutura ou configurações privilegiadas.

> A integridade da entrega contínua depende diretamente da integridade dos próprios pipelines.

---

## 🎯 Objetivos

- Garantir que **apenas alterações autorizadas** desencadeiam execuções;
- Assegurar que o **fluxo de execução está controlado e é previsível**;
- Proteger contra **manipulação maliciosa do pipeline** (ex: substituição de scripts, bypass de etapas);
- Permitir **rastreabilidade e revisão independente** de tudo o que o pipeline faz.

---

## 🛠️ Práticas

1. **Pipelines como código (PaC)**  
   - Pipelines devem ser definidos como ficheiros versionados (ex: YAML, JSON, HCL), em repositórios controlados;
   - Todas as alterações devem ser rastreáveis e sujeitas a revisão formal via pull/merge request.

2. **Triggers controlados e explícitos**  
   - Só devem ser aceites triggers de fontes autorizadas (ex: merge em branch principal, push em branch monitorizada, tag assinada);
   - Execuções em forks ou branches externos devem ser desativadas ou mediadas.

3. **Revisão obrigatória de alterações ao pipeline**  
   - Alterações a ficheiros de pipeline (ex: `.github/workflows/*.yml`) devem requerer revisão técnica e/ou de segurança;
   - Deve aplicar-se política de "4-olhos" (mínimo dois revisores).

4. **Separação de pipelines por função ou criticidade**  
   - CI e CD devem ser pipelines distintos, com controlos e permissões diferenciadas;
   - Aplicações classificadas como L3 devem ter pipelines dedicados, segregados de pipelines genéricos.

5. **Templates reutilizáveis e centralizados**  
   - Utilização de templates permite validação centralizada e reduz riscos de erro ou manipulação;
   - Templates devem ser versionados, auditáveis e revistos periodicamente.

---

## ⚖️ Aplicação proporcional por nível de risco

| Nível | Requisitos obrigatórios                         | Requisitos reforçados                                 |
|-------|--------------------------------------------------|--------------------------------------------------------|
| **L1** | Pipelines versionados; triggers controlados      | -                                                      |
| **L2** | Revisão obrigatória; CI/CD separados             | Templates reutilizáveis; validação automática          |
| **L3** | Revisão por segurança; pipelines isolados        | Aprovação formal de alterações ao pipeline             |

---

## 📌 Exemplos práticos

- **GitHub Actions**  
  - `required reviewers` para `.github/workflows`;
  - Desativar execuções automáticas em forks (`pull_request_target`).

- **GitLab CI**  
  - Uso de `rules:` e `only:` para controlar triggers;
  - Regras de aprovação obrigatória para `.gitlab-ci.yml`.

- **Azure DevOps**  
  - Política de branch protection e PR gates para `azure-pipelines.yml`;
  - Templates YAML em repositório separado com acesso controlado.

- **Jenkins**  
  - Pipelines declarativos versionados em Git;
  - Proteção de scripts com *Script Approval Plugin*.

---

## 📉 Riscos mitigados

- Execuções não autorizadas (OSC&R: CI0001, CI0004);
- Substituição maliciosa de scripts (OSC&R: CI0011);
- Manipulação do fluxo de build (OSC&R: CI0002);
- Abuso de triggers automáticos (OSC&R: CI0006, CI0015).

---
