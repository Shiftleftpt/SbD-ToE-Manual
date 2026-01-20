---

id: exemplos-praticas-boas
title: Exemplos de Boas Práticas de IaC Seguro
sidebar_position: 5
description: Exemplos comentados de código e práticas seguras para aplicar em repositórios de Infraestrutura como Código.
tags: [exemplos, boas práticas, iac, código seguro, repositórios]
-----------------------------------------------------------------

# 🛠️ Exemplos de Estrutura e Práticas Seguras em Projetos IaC

## 🌟 Objetivo

Apresentar **exemplos concretos, reutilizáveis e auditáveis** de como estruturar e operar projetos de Infraestrutura como Código (IaC) de forma segura, coerente e alinhada com as práticas prescritas neste capítulo.

Este ficheiro tem natureza **ilustrativa e operacional**: não introduz novos requisitos, mas demonstra **como aplicar corretamente** os existentes.

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

**Propriedades de segurança asseguradas:**

* Separação física e lógica de ambientes;
* Modularização controlada e reutilizável;
* Integração nativa de *policy-as-code*;
* Suporte direto a rastreabilidade e auditoria.

---

## 🏷️ Exemplo de tagging obrigatório

```hcl
tags = {
  Environment = var.environment
  Owner       = var.owner
  Application = var.application
  Criticality = var.criticality
  ManagedBy   = "Terraform"
}
```

* As *tags* são aplicadas **por omissão** em todos os recursos;
* A ausência de qualquer *tag* obrigatória deve resultar em **falha bloqueante** via OPA/Rego.

---

## 🔐 Exemplo de controlo de permissões (privilégio mínimo)

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

  managed_policy_arns = [aws_iam_policy.least_privilege.arn]
}
```

**Notas de segurança:**

* Nenhuma política ampla (`*`) é permitida por omissão;
* Permissões são explicitamente associadas e validadas em *policy-as-code*;
* Revisão obrigatória para qualquer alteração em IAM.

---

## 🔄 Exemplo de uso seguro de módulos externos

```hcl
module "vpc" {
  source = "git::https://github.com/org/vpc-module.git?ref=v1.2.3"

  cidr_block  = "10.0.0.0/16"
  environment = var.environment
}
```

**Boas práticas evidenciadas:**

* Referência explícita a *tag* imutável (`ref=vX.Y.Z`);
* Origem verificável;
* Compatível com validação de *digest* e *attestation* em pipeline.

---

## 💪 Exemplo de workflow CI para validação IaC

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

**Garantias fornecidas pelo pipeline:**

* Validação sintática e estrutural;
* Deteção precoce de más configurações;
* Bloqueio automático de não conformidades;
* Evidência auditável por PR/MR.

---

## 🧷 Template de *pre-commit hooks*

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

**Objetivo:**

* Reduzir *feedback loop*;
* Eliminar erros triviais antes de CI;
* Normalizar qualidade entre contribuidores.

---

## 🔗 Ligação a requisitos

| Exemplo aplicado                 | Requisitos relacionados   |
| -------------------------------- | ------------------------- |
| Estrutura modular de repositório | IAC-002, IAC-005, REQ-004 |
| Tagging obrigatório              | IAC-002, IAC-008, REQ-006 |
| Uso de módulos versionados       | IAC-004, REQ-007          |
| Workflow CI com scanners         | IAC-003, REQ-005, REQ-006 |
| Pre-commit hooks                 | IAC-003, REQ-006          |

---

## ✅ Benefícios diretos

* Acelera a adoção consistente de IaC seguro;
* Reduz variação entre projetos e equipas;
* Facilita auditoria e *onboarding* técnico;
* Transforma segurança em *default operacional*.

---

> 🔗 Estes exemplos estão alinhados com as práticas de **SSDF (PW.6)**, **SLSA (Build L2)** e **OWASP SAMM (AA2.1, CM1.1)**, funcionando como material de referência operacional para equipas técnicas.
