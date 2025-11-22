---
description: Estratégias de planeamento e controlo para garantir uma adoção eficaz
  e auditável das práticas de segurança em Infraestrutura como Código.
id: planeamento-e-controle
sidebar_position: 1
tags:
- adoção
- cicd
- controlo
- governanca
- iac
- planeamento
- seguranca
title: Planeamento e Controlo da Aplicação de IaC Seguro
---


# 🧭 Planeamento de Execução e Controlo de Estado

## 🌟 Objetivo

Garantir que todos os projetos de Infraestrutura como Código (IaC) mantêm um **controlo consistente, seguro e rastreável** do **estado da infraestrutura** e dos **planos de execução** (`plan`) gerados antes de qualquer alteração.

Esta prática permite:

- Prevenir *drift* e alterações não autorizadas;
- Evitar concorrência e conflitos entre múltiplos operadores;
- Permitir auditoria e rollback seguros;
- Viabilizar integração com pipelines CI/CD e processos de aprovação;
- Assegurar integridade e conformidade com políticas de execução.

---

## 📌 O que deve ser feito

1. **Configurar backend remoto autenticado** para armazenar o estado (`terraform.tfstate`, ou equivalente);
2. **Ativar mecanismo de locking** para evitar concorrência durante o `apply`;
3. **Gerar e versionar planos de execução (`plan`)** antes de aplicar alterações;
4. **Associar os `plans` a mecanismos de aprovação** (ex: Pull Request, Change Request);
5. **Armazenar artefactos de plano e logs de execução com integridade verificável**;
6. **Detetar e alertar sobre *drift*** (diferença entre estado real e esperado);
7. **Proibir execuções locais manuais** fora de contexto validado e controlado.

---

## ⚙️ Como aplicar

| Ação                | Prescrição                                                                 |
|---------------------|----------------------------------------------------------------------------|
| **Backend remoto**  | S3 + DynamoDB (AWS), Azure Blob + CosmosDB, ou GCS, com autenticação forte |
| **Locking**         | `lock = true` + mecanismo como DynamoDB, Consul ou equivalente              |
| **Execução CI/CD**  | Proibir `apply` manual; `plan` gerado e versionado no pipeline              |
| **Rastreabilidade** | Tags, branches, PR/MR ID, nome de release e output legível no diff          |
| **Auditoria**       | Guardar `plan` e logs com hashes e metadados (timestamp, hash, autor)       |
| **Drift detection** | `terraform plan -detailed-exitcode`, `driftctl`, `tfsec`, ou CI agendado    |

---

## 🕒 Quando aplicar

| Momento                       | Ação esperada                                                        |
|-------------------------------|-----------------------------------------------------------------------|
| Início do projeto IaC         | Definir e documentar backend, ambiente e locking                     |
| Novo `apply` em produção      | Gerar `plan`, submeter a aprovação, versionar artefacto              |
| Após rollback, erro ou patch  | Validar estado atual e corrigir divergência                          |
| Periodicamente (ex: CI agendado) | Verificar *drift* entre estado esperado e realidade               |

---

## 👥 Perfis envolvidos

| Papel            | Responsabilidade                                               |
|------------------|---------------------------------------------------------------|
| DevOps/Cloud     | Configuração de backend, execução via pipeline                |
| Segurança        | Definição de política de execução controlada                  |
| Arquitetura      | Aprovação de ambientes e mecanismos de isolamento             |
| GRC/Compliance   | Verificação da rastreabilidade e mecanismos de auditoria      |

---

## 🧪 Exemplos práticos

- `terraform backend "s3"` com `encrypt = true`, `lock_table` e versionamento;
- Pipeline com job que faz `terraform plan`, armazena o `.plan` e aguarda aprovação para `apply`;
- Tabela DynamoDB configurada para locking, com TTL e tags por projeto;
- Armazenamento de planos e logs num bucket versionado (`branch + timestamp + PR` como nome do artefacto).

---

## ✅ Boas práticas

- Nunca executar `terraform apply` localmente em ambientes de produção;
- Validar e registar `plan` antes de qualquer alteração significativa;
- Usar artefactos com hashes de integridade e rastreabilidade cruzada com PR ou release;
- Monitorizar divergências entre o estado real e o esperado (**drift detection**) periodicamente;
- Estabelecer uma política organizacional formal sobre execução controlada de infraestrutura.

---

## 🔗 Referências cruzadas

| Documento                      | Relação com esta prática                            |
|--------------------------------|-----------------------------------------------------|
| `08-rastreabilidade-vulnerabilidades.md` | Reforça auditoria e rastreabilidade               |
| `04-integracao-ci-cd.md`       | Execução automatizada e validação de planos         |
| `02-matriz-requisitos-iac.md`  | Requisitos `IAC-001`, `REQ-004`, `REQ-005`          |
| SSDF (PW.5) / SLSA (Build L2)  | Requisitos normativos sobre execução controlada     |

---

> 🔐 Este controlo é essencial para garantir integridade, rastreabilidade e conformidade no ciclo de vida de infraestrutura como código - sendo um dos pilares de maturidade em IaC seguro segundo o modelo SbD-ToE.
