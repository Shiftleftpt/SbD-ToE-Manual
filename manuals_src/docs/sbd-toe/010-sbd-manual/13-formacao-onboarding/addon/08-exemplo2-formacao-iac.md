---
id: formacao-iac
title: Módulo Formativo - Infraestrutura como Código (IaC) Seguro
sidebar_position: 8
description: Capacitação prática para equipas técnicas que desenvolvem, revêm ou operam projetos IaC de forma segura
tags: [checkov, devops, formacao, iac, pipelines, requisitos, terraform, tfsec, validacao]
---


# 🧱 Módulo Formativo - Infraestrutura como Código (IaC) Seguro

## 🎯 Objetivo

Capacitar as equipas técnicas para:

- Compreender os principais riscos de segurança em projetos de IaC;
- Aplicar os requisitos `IAC-001` a `IAC-013` definidos no Capítulo 08 do SbD-ToE;
- Integrar validações e boas práticas de segurança no ciclo de vida de desenvolvimento e operação de infraestrutura;
- Reduzir o risco de exposição, erro de configuração e drift.

---

## 📋 Pré-requisitos

- Familiaridade com linguagens de IaC (ex: Terraform, Bicep, YAML/K8s)
- Experiência prévia com pipelines de CI/CD (execução, revisão ou configuração)
- Conhecimento básico sobre segregação de ambientes e gestão de credenciais

---

## 🧪 Formato da sessão

| Bloco                     | Duração | Objetivo                                                              |
|--------------------------|---------|-----------------------------------------------------------------------|
| Introdução               | 10 min  | Contexto e importância de segurança em IaC                            |
| Requisitos `IAC-XXX`     | 20 min  | Apresentação dos requisitos normativos e ligação a más práticas reais|
| Revisão de PR inseguro   | 20 min  | Exercício prático com deteção de falhas e discussão em grupo         |
| Integração com CI/CD     | 15 min  | Demonstração de pipelines com validações automáticas (tfsec, OPA, etc.) |
| Quiz + validação         | 10 min  | Questionário com feedback imediato                                    |

> 🔍 Este módulo pode ser adaptado a workshops hands-on com labs reais ou simulações por stack.

---

## 📦 Materiais necessários

- Repositório com exemplos reais e simulados (Terraform, Bicep, K8s)
- Cheatsheet de ferramentas e comandos (tfsec, checkov, driftctl, opa)
- Templates de PR com secções obrigatórias de validação
- Referência rápida dos requisitos `IAC-001` a `IAC-013`
- Diagrama de fluxo de validação e gestão de exceções

---

## ✅ Critérios de conclusão

- Participação ativa na sessão ou revisão assistida de PR
- Aprovação no quiz final (mínimo 80%)
- Entrega de evidência de integração de validações no pipeline do projeto (ex: PR com config de tfsec/checkov)

---

## 🔁 Integração no ciclo de vida

- Inclusão do módulo na **formação obrigatória de onboarding DevOps**
- Tarefas de backlog técnico: `[SEC] Validar plano Terraform com tfsec` / `[SEC] Adicionar tagging obrigatório`
- Associar ao **processo de exceções formais** descrito no capítulo
- Criar cartão ou história do tipo:  
  `Como DevOps quero validar todos os PRs de IaC com tfsec e driftctl, para garantir conformidade com os requisitos IAC-XXX.`

---

## 🔗 Referências cruzadas no SbD-ToE

| Capítulo                       | Relevância                                                 |
|--------------------------------|------------------------------------------------------------|
| Capítulo 08 - IaC Seguro       | Fonte principal de requisitos e práticas (IAC-001 a IAC-013) |
| Capítulo 07 - CI/CD Seguro     | Integração com pipelines e execuções isoladas             |
| Capítulo 04 - Arquitetura      | Impacto estrutural das configurações e módulos reutilizáveis|
| Capítulo 02 - Requisitos       | Correspondência com REQ-XXX relacionados com segredos, permissões, segregação |

---

## 📊 Boas práticas operacionais

- Incluir este módulo como **pré-requisito para acesso a ambientes cloud** ou pipelines críticos
- Realizar sessões trimestrais com análise de erros reais de IaC da organização
- Reforçar o uso de PR Clinics com foco em infraestrutura
- Manter repositório interno com *IaC patterns* seguros e inseguros
- Acompanhar mudanças em ferramentas e adaptar continuamente o conteúdo

---

> 📌 Este módulo é essencial para qualquer equipa que atue sobre infraestrutura como código - seja em contexto de provisionamento, pipelines ou operações. A sua aplicação reduz riscos sistémicos e aumenta a maturidade da organização na gestão de ambientes e permissões.
