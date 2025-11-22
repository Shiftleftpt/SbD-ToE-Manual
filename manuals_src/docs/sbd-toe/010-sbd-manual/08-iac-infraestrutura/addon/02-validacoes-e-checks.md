---
description: Estratégias de planeamento e controlo para garantir uma adoção eficaz
  e auditável das práticas de segurança em Infraestrutura como Código.
id: validacoes-e-checks
sidebar_position: 1
tags:
- adoção
- cicd
- controlo
- governanca
- iac
- planeamento
- seguranca
title: Validações Automáticas e Controlo de Qualidade no Projeto IaC
---



# 🧪 Validações Automáticas e Controlo de Qualidade no Projeto IaC

## 🌟 Objetivo

Garantir que todas as alterações em projetos de Infraestrutura como Código (IaC) são sujeitas a **validações automáticas**, assegurando:

- Correção sintática e semântica do código;
- Conformidade com políticas internas e boas práticas de segurança;
- Ausência de erros lógicos, *drift* ou configurações perigosas;
- Integração confiável no pipeline CI/CD.

> A validação automatizada é um dos pilares do controlo de qualidade e segurança do próprio projeto IaC, aplicando o princípio de *"shift-left"* ao controlo da infraestrutura.

---

## 📌 O que deve ser feito

1. Executar **linters e validadores sintáticos** (ex: `terraform validate`, `tflint`, `yamllint`);
2. Aplicar **ferramentas de segurança específicas para IaC** (ex: `tfsec`, `checkov`, `kics`);
3. Validar **aderência a convenções internas** (naming, tags, módulos permitidos);
4. Integrar todas as validações no **pipeline CI/CD**, com falha obrigatória em caso de não conformidade;
5. Validar **`terraform plan` ou equivalente antes do `apply`**;
6. Verificar **ausência de alterações inesperadas (drift)**;
7. Bloquear alterações caso **requisitos críticos não sejam cumpridos**.

---

## ⚙️ Como aplicar

| Tipo de Validação        | Ferramentas ou Técnicas                                                                 |
|--------------------------|------------------------------------------------------------------------------------------|
| **Sintática / Semântica**    | `terraform fmt`, `terraform validate`, `yamllint`, `jsonlint`                           |
| **Linting estruturado**      | `tflint` (Terraform), `actionlint` (GitHub Actions), `ansible-lint`                     |
| **Segurança e conformidade** | `tfsec`, `checkov`, `kics`, `terrascan`, `inspec`                                       |
| **Políticas internas**       | OPA/Rego, Sentinel (HashiCorp), Conftest, validações customizadas                       |
| **CI/CD**                    | Jobs automáticos em PR/MR, gates com bloqueio em falha, badges de conformidade          |
| **Testes de `plan`**         | Verificação de que as alterações planeadas são esperadas e autorizadas                  |
| **Pre-commit hooks**         | Execução local obrigatória de checks antes de `git push`                                |

---

## 🕒 Quando aplicar

| Momento                           | Validações esperadas                                           |
|-----------------------------------|----------------------------------------------------------------|
| Commit / Push                     | Linters, testes locais, pré-commit hooks                       |
| Pull Request                      | Execução completa de linters, scanners de segurança e policies |
| Merge para branch de release      | Validação reforçada, `plan` validado, conformidade forçada     |
| Pré-`apply`                       | Verificação final com `plan`, hashes e validação de ambiente   |
| Periodicamente (agendado)         | Verificação de drift, revalidação de módulos e dependências    |

---

## 👥 Perfis envolvidos

| Papel             | Responsabilidade técnica                                                   |
|-------------------|-----------------------------------------------------------------------------|
| DevOps            | Integração dos checks no pipeline e execução em PRs                        |
| Segurança         | Definição das regras de política e validação dos scanners                  |
| Desenvolvimento   | Adaptação do código às regras e correção de findings                       |
| Cloud / Infra      | Validação de permissões, tags e outputs esperados                         |

---

## 🧪 Exemplos práticos

- `terraform validate` e `tflint` executados via GitHub Actions ou Azure Pipelines;
- `tfsec` com severidade mínima configurada: `--minimum-severity=high`;
- `checkov` com baseline para ignorar findings previamente aceites;
- Política OPA a bloquear `aws_s3_bucket` sem `versioning` ativo;
- Job `validate-iac` como pré-requisito obrigatório ao `apply`.

---

## ✅ Boas práticas

- Definir um **conjunto mínimo obrigatório de validações** por tipo de projeto;
- Executar todos os validadores de forma **automática e bloqueante** no pipeline;
- Envolver segurança e equipas de infraestrutura na **definição contínua das regras**;
- Usar **pre-commit hooks** para evitar erros antes do push;
- Integrar **badges de conformidade** visíveis nos repositórios como incentivo e controlo;
- Versionar as configurações dos validadores e políticas em repositórios comuns.

---

## 🔗 Referências cruzadas

| Documento                     | Relação com esta prática                              |
|-------------------------------|--------------------------------------------------------|
| `01-planeamento-e-controle.md` | Validação do `plan` como pré-condição ao `apply`      |
| `02-matriz-requisitos-iac.md` | Requisitos `IAC-003`, `REQ-005`                        |


---

> ⚠️ A ausência de validações automáticas abre a porta a más práticas, riscos de segurança, configurações perigosas e erros difíceis de rastrear - comprometendo todo o ciclo de vida da infraestrutura como código.
