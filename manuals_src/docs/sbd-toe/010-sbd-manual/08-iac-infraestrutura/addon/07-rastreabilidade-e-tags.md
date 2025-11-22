---
description: Técnicas para garantir a rastreabilidade de alterações, uso de tagging
  e gestão de versões seguras em IaC.
id: rastreabilidade-e-tags
sidebar_position: 7
tags:
- git
- iac
- rastreabilidade
- seguranca
- segurança
- tags
- versionamento
title: Rastreabilidade e Versionamento com Tags em IaC
---



# 🔍 Rastreabilidade e Uso de Tags em Projetos IaC

## 🌟 Objetivo

Garantir que todas as alterações, recursos e ambientes definidos via Infraestrutura como Código (IaC) sejam **rastreáveis, auditáveis e identificáveis**, através de convenções de tagging, metadados e controlo de alterações versionadas.

> A rastreabilidade é um pilar de segurança organizacional: permite compreender "quem alterou o quê, quando, com que justificação, e com que impacto".

---

## 🔖 O que deve ser feito

1. **Aplicar tags obrigatórias em todos os recursos criados via IaC**, incluindo ambiente, owner, criticidade e origem;
2. **Manter convenções formais de nomeação** para recursos, ficheiros, ambientes e releases;
3. **Registar todas as alterações em sistema de controlo de versões**, com commit messages legíveis e ligadas a tickets;
4. **Incluir metadados no código** que permitam mapear alterações com recurso e contexto afetado;
5. **Documentar as relações entre ficheiros, módulos e ambientes impactados**;
6. **Incluir identificação de aplicação, equipa e finalidade** nos manifestos IaC, outputs ou logs.

---

## ⚖️ Como deve ser feito

| Elemento                 | Prática recomendada                                                           |
| ------------------------ | ----------------------------------------------------------------------------- |
| Tags em recursos         | `Environment`, `Owner`, `Application`, `Criticality`, `ManagedBy`             |
| Comentários informativos | Indicar ID da tarefa, contexto e objetivo da alteração                        |
| Commit messages          | Padrão: `[IaC] Alterar recurso X em ambiente Y (issue-123)`                   |
| Metadata nos manifests   | `locals` com aplicação, equipa, versão e data                                 |
| Tracking de releases     | Tags git: `iac-prod-v2025.07.10`, artefactos versionados com hash e timestamp |
| Output de execução       | Logs com autor, data, PR, plano executado, ambiente alvo                      |

---

## 🗓️ Quando aplicar

| Momento                           | Ação esperada                                                     |
| --------------------------------- | ----------------------------------------------------------------- |
| Criação de novo recurso           | Aplicar tags obrigatórias                                         |
| Alteração significativa           | Registar justificação, ambiente e ticket associado                |
| Execução de `plan/apply`          | Guardar output com hash, data e identidade do autor               |
| Auditoria ou revisão de segurança | Verificar metadados, naming, tagging e rastreabilidade por versão |

---

## 💼 Exemplos práticos

### 🌍 Tags em Terraform

```hcl
resource "aws_s3_bucket" "logs" {
  bucket = "app-logs-prod"

  tags = {
    Environment = "prod"
    Owner       = "devops-team"
    Criticality = "high"
    Application = "web-api"
    ManagedBy   = "Terraform"
  }
}
```

### 🔍 Metadata local

```hcl
locals {
  app_name    = "billing-service"
  maintainer  = "infra-team@org"
  version     = "v1.3.2"
  last_update = "2025-07-10"
}
```

### 💪 Commit message com rastreabilidade

```
[IaC] Corrigir timeout no ALB do ambiente staging (ISSUE-8723)
```

---

## ✅ Benefícios diretos

* Permite auditoria e investigação de incidentes de forma objetiva;
* Aumenta visibilidade sobre impacto e autoria de alterações;
* Suporta decisões de reversão ou aprovação com base em contexto documentado;
* Reduz risco de inconsistências e facilita controlo de qualidade.

---

> 🔗 Alinhado com os requisitos `IAC-002`, `IAC-005`, `IAC-008`, `REQ-004`, `REQ-006`, SSDF (CM.5), SAMM (AA2.1), CIS Controls (8.3, 4.6).
