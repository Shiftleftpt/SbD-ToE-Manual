---
id: exemplos-praticas-boas
title: Exemplos de Boas Práticas de IaC Seguro
sidebar_position: 5
description: Exemplos comentados de código e práticas seguras para aplicar em repositórios de Infraestrutura como Código.
tags: [exemplos, boas práticas, iac, código seguro, repositórios]
---


# 🛠️ Exemplos de Estrutura e Práticas Seguras em Projetos IaC

## 🌟 Objetivo

Apresentar **exemplos concretos e reutilizáveis** de como estruturar e operar projetos de Infraestrutura como Código de forma segura, de acordo com os princípios, requisitos e validações definidos neste capítulo.

---

## 📁 Estrutura recomendada de repositório

```text
iac/
├── modules/
│   └── networking/
│       ├── main.tf
│       ├── variables.tf
│       ├── outputs.tf
│       └── README.md
├── envs/
│   ├── dev/
│   │   ├── main.tf
│   │   └── backend.tf
│   ├── staging/
│   └── prod/
├── policies/
│   ├── opa/
│   └── conftest/
├── .github/workflows/
│   └── validate.yaml
├── .pre-commit-config.yaml
├── LICENSE
└── README.md
```

> Esta estrutura separa ambientes, permite modularização segura e suporte a enforcement automatizado.

---

## 🏷️ Exemplo de tagging obrigatório

```hcl
tags = {
  Environment = var.environment
  Owner       = var.owner
  Criticality = var.criticality
  ManagedBy   = "Terraform"
}
```

Incluído automaticamente por módulo ou imposto por política (ex: regra Rego).

---

## 🔐 Exemplo de controlo de permissões

```hcl
resource "aws_iam_role" "example" {
  name = "app-deploy-role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect = "Allow"
        Principal = {
          Service = "ec2.amazonaws.com"
        }
        Action = "sts:AssumeRole"
      }
    ]
  })

# Aplicação de política mínima
  managed_policy_arns = [aws_iam_policy.least_privilege.arn]
}
```

---

## 🔄 Exemplo de uso seguro de módulos externos

```hcl
module "vpc" {
  source  = "git::https://github.com/org/vpc-module.git?ref=v1.2.3"

  cidr_block = "10.0.0.0/16"
  environment = var.environment
}
```

> A referência a `ref=tag` impede alterações inesperadas e permite validação de proveniência.

---

## 💪 Exemplo de workflow CI para validação

```yaml
name: Validate IaC

on:
  pull_request:
    paths:
      - 'iac/**'

jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Terraform Format
        run: terraform fmt -check -recursive
      - name: Terraform Validate
        run: terraform validate
      - name: TFLint
        uses: terraform-linters/setup-tflint@v1
      - name: tfsec
        run: tfsec ./iac
      - name: Checkov
        run: checkov -d ./iac
```

> O pipeline executa validações sintáticas, lint e segurança com scanners reconhecidos.

---

## 🏠 Template de pre-commit hook

```yaml
repos:
  - repo: https://github.com/antonbabenko/pre-commit-terraform
    rev: v1.66.1
    hooks:
      - id: terraform_fmt
      - id: terraform_validate
      - id: terraform_tflint
      - id: terraform_tfsec
```

> Aplicado automaticamente antes do `git commit`, reduz erros antes de PR.

---

## 🔗 Ligação a requisitos

| Exemplo aplicado                 | Requisitos relacionados         |
| -------------------------------- | ------------------------------- |
| Estrutura de repositório modular | `IAC-002`, `IAC-005`, `REQ-004` |
| Tagging obrigatório              | `IAC-002`, `IAC-008`, `REQ-006` |
| Uso de módulo versionado         | `IAC-004`, `REQ-007`            |
| Workflow CI com scanners         | `IAC-003`, `REQ-005`, `REQ-006` |
| Pre-commit hooks                 | `IAC-003`, `REQ-006`            |

---

## ✅ Benefícios

* Acelera adoção segura de práticas por novas equipas;
* Promove consistência entre projetos e ambientes;
* Reduz esforço manual de revisão e validação;
* Permite escalar segurança como padrão.

---

> 🔗 Todos os exemplos foram alinhados com os ficheiros anteriores deste capítulo e com as práticas de SSDF (PW\.6), SLSA (Build L2), SAMM (AA2.1), BSIMM (CMVM1.1).
