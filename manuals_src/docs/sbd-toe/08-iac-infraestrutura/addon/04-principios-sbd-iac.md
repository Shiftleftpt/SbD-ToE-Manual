---
id: principios-sbd-iac
title: Princípios de Security by Design aplicados a IaC
sidebar_position: 4
description: Interpretação dos princípios de Security by Design no contexto específico de Infraestrutura como Código.
tags: [princípios, security by design, iac, fundamentos, arquitetura segura]
---

# 🛡️ Princípios de Security by Design aplicados a Projetos IaC {iac-infraestrutura:addon:principios-sbd-iac}

## 🌟 Objetivo {iac-infraestrutura:addon:principios-sbd-iac#objetivo}

Garantir que todos os projetos IaC são desenhados e mantidos com base em princípios estruturais de **segurança por definição**, reforçando a fiabilidade e a resiliência da infraestrutura que provisionam.

> O projeto IaC é um ativo crítico e deve refletir, no próprio código e estrutura, os princípios de segurança aplicáveis a qualquer aplicação de risco.

---

## 📌 Princípios essenciais aplicáveis a projetos IaC {iac-infraestrutura:addon:principios-sbd-iac#principios_essenciais_aplicaveis_a_projetos_iac}

| Princípio                  | Aplicação prática no contexto IaC                                                              |
| -------------------------- | ---------------------------------------------------------------------------------------------- |
| **Separação de ambientes** | Diretórios, workspaces, pipelines e artefactos independentes para `dev`, `staging`, `prod`     |
| **Privilégio mínimo**      | Os recursos provisionados (ex: roles, buckets, keys) devem ter permissões mínimas necessárias  |
| **Rastreabilidade**        | Todas as alterações devem ser versionadas, associadas a autor, ticket, ambiente e justificação |
| **Imutabilidade**          | Recursos críticos devem ser redeployáveis sem alteração fora de band                           |
| **Consistência**           | Naming conventions, tagging, layout de diretórios e outputs padronizados                       |
| **Visibilidade**           | Outputs e logs claros; tagging e metainformação para debugging e auditoria                     |
| **Desacoplamento**         | Evitar hardcodes, dependências implícitas e sobreposição entre módulos/ambientes               |
| **Fail securely**          | Defaults seguros (ex: recurso só criado com tags, permissões restritivas por omissão)          |

---

## 📋 O que deve ser feito {iac-infraestrutura:addon:principios-sbd-iac#o_que_deve_ser_feito}

1. Definir e aplicar um layout estruturado para o repositório, com separação lógica de ambientes;
2. Usar tags obrigatórias (ambiente, owner, tipo, criticidade) em todos os recursos provisionados;
3. Padronizar nomes e variáveis, evitando ambiguidades e erros por copy/paste;
4. Rever permissões criadas por IaC, com especial atenção a `iam_role`, `policy`, `security_group`, etc.;
5. Forçar estrutura comum entre projetos IaC, com template base ou scaffolding;
6. Evitar dependências circulares ou indiretas entre módulos e ambientes;
7. Tratar *drift* e mudanças manuais como falha de segurança, e não como exceção aceitável.

---

## ⚙️ Técnicas e ferramentas {iac-infraestrutura:addon:principios-sbd-iac#tecnicas_e_ferramentas}

| Técnica/Ferramenta      | Aplicação prática                                                              |
| ----------------------- | ------------------------------------------------------------------------------ |
| Layout repositório IaC  | `iac/ ├─ modules/ ├─ envs/ ├─ policies/ ├─ templates/`                         |
| Tagging                 | `tags = { Environment = "prod", Owner = "appsec", ... }`                       |
| Pre-commit hooks        | Validação de naming, presença de tags, padrão de ficheiros                     |
| Padrão de variáveis     | `variable "environment" { type = string ... }` obrigatório em todos os módulos |
| Testes semânticos       | OPA/Rego, Conftest para garantir políticas mínimas aplicadas                   |
| Policy-as-Code          | Bloquear permissões amplas, ausência de tags ou naming incorreto               |
| Reutilização controlada | Templates para `main.tf`, `variables.tf`, `outputs.tf` validados e aprovados   |

---

## 🕒 Quando aplicar {iac-infraestrutura:addon:principios-sbd-iac#quando_aplicar}

| Fase do ciclo de vida                | Ação esperada                                            |
| ------------------------------------ | -------------------------------------------------------- |
| Criação do projeto IaC               | Definir layout e aplicar princípios a nível estrutural   |
| Adição de novos módulos              | Rever permissões, naming, outputs, tagging               |
| Alterações críticas                  | Revalidar aderência a princípios antes de aprovação      |
| Auditoria ou revisão de conformidade | Verificar tagging, rastreabilidade e outputs previsíveis |

---

## 👥 Perfis envolvidos {iac-infraestrutura:addon:principios-sbd-iac#perfis_envolvidos}

| Perfil         | Responsabilidades relacionadas ao tema                                    |
| -------------- | ------------------------------------------------------------------------- |
| DevOps / Cloud | Implementar estrutura, tagging, segregação e revisão de permissões        |
| Segurança      | Validar aplicação dos princípios, definir políticas default e enforcement |
| Arquitetura    | Aprovar standards de layout, naming, tagging e estrutura de outputs       |
| Plataforma     | Disponibilizar scaffolds e validações partilhadas entre equipas           |

---

## 🧪 Exemplos práticos {iac-infraestrutura:addon:principios-sbd-iac#exemplos_praticos}

* Diretório `envs/prod/` com ficheiro `main.tf`, onde `variable "environment"` é obrigatória;
* Tagging obrigatório em `aws_instance`, `aws_s3_bucket`, etc., validado por `terraform validate` + OPA;
* Regra OPA:

  ```rego
  deny[msg] {
    input.resource_type == "aws_s3_bucket"
    not input.tags["Environment"]
    msg := "Missing Environment tag on S3 bucket"
  }
  ```

---

## ✅ Benefícios diretos {iac-infraestrutura:addon:principios-sbd-iac#beneficios_diretos}

* Redução do risco estrutural nos ambientes geridos por IaC;
* Consolidação de boas práticas entre equipas;
* Aumento da previsibilidade, auditoria e debugging das alterações;
* Capacidade de enforcement técnico automatizado.

---

## 🔗 Referências cruzadas {iac-infraestrutura:addon:principios-sbd-iac#referencias_cruzadas}

| Documento                     | Relação com esta prática                                      |
| ----------------------------- | ------------------------------------------------------------- |
| `02-matriz-requisitos-iac.md` | Requisitos `IAC-002`, `IAC-005`, `REQ-004`, `REQ-006`         |
| SAMM (AA2.1, CM1.3)           | Padrões arquiteturais e controlo de mudança                   |
| SSDF (CM.5)                   | Design seguro e separação de ambientes                        |
| SLSA (Source & Provenance)    | Fiabilidade de origem e rastreabilidade no controlo de código |
