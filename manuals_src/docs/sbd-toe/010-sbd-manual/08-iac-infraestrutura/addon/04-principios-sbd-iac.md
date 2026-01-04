---

id: principios-sbd-iac
title: Princípios de Security by Design aplicados a IaC
sidebar_position: 4
description: Interpretação dos princípios de Security by Design no contexto específico de Infraestrutura como Código.
tags: [princípios, security by design, iac, fundamentos, arquitetura segura]
----------------------------------------------------------------------------

# 🛡️ Princípios de Security by Design aplicados a Projetos IaC

## 🌟 Objetivo

Garantir que todos os projetos IaC são desenhados e mantidos com base em princípios estruturais de **segurança por definição**, reforçando a fiabilidade e a resiliência da infraestrutura que provisionam.

> O projeto IaC é um ativo crítico e deve refletir, no próprio código e estrutura, os princípios de segurança aplicáveis a qualquer aplicação de risco.

---

## 📌 Princípios essenciais aplicáveis a projetos IaC

| Princípio                   | Aplicação prática no contexto IaC                                                                             |
| --------------------------- | ------------------------------------------------------------------------------------------------------------- |
| **Separação de ambientes**  | Diretórios, workspaces, pipelines e artefactos independentes para `dev`, `staging`, `prod`                    |
| **Privilégio mínimo**       | Os recursos provisionados (ex.: roles, buckets, keys) devem ter apenas as permissões estritamente necessárias |
| **Rastreabilidade**         | Todas as alterações devem ser versionadas, associadas a autor, ticket, ambiente e justificação                |
| **Imutabilidade**           | Recursos críticos devem ser redeployáveis, evitando alterações fora de band                                   |
| **Consistência**            | Naming conventions, tagging, layout de diretórios e outputs padronizados                                      |
| **Visibilidade controlada** | Outputs, logs e metadados suficientes para auditoria sem expor topologia, segredos ou permissões              |
| **Desacoplamento**          | Evitar hardcodes, dependências implícitas e sobreposição entre módulos e ambientes                            |
| **Fail securely**           | Defaults seguros (ex.: recursos só criados com tags e permissões restritivas por omissão)                     |
| **Minimização de contexto** | Reduzir ao mínimo a exposição de planos, outputs, topologia e metadados fora do domínio controlado            |

---

## ⚠️ Código não confiável por origem

Qualquer código IaC que seja:

* gerado automaticamente,
* sugerido por ferramentas assistidas,
* criado a partir de templates externos,

**deve ser tratado como código não confiável por origem**, independentemente da ferramenta utilizada.

A confiança resulta exclusivamente de:

* validação técnica automatizada;
* revisão humana qualificada;
* evidência explícita de aprovação;
* execução controlada em pipelines autorizados.

Este princípio evita que erros sistemáticos, defaults inseguros ou *hallucinations* se propaguem automaticamente entre ambientes.

---

## 📋 O que deve ser feito

1. Definir e aplicar um layout estruturado para o repositório, com separação lógica de ambientes;
2. Usar tags obrigatórias (ambiente, owner, tipo, criticidade) em todos os recursos provisionados;
3. Padronizar nomes e variáveis, evitando ambiguidades e erros por copy/paste;
4. Rever permissões criadas por IaC, com especial atenção a `iam_role`, `policy`, `security_group`, etc.;
5. Forçar uma estrutura comum entre projetos IaC, com templates base ou scaffolding aprovado;
6. Evitar dependências circulares ou implícitas entre módulos e ambientes;
7. Tratar *drift* e mudanças manuais como falha de segurança e não como exceção aceitável;
8. Garantir que qualquer alteração automatizada é validada e aprovada antes de execução.

---

## ⚙️ Técnicas e ferramentas

| Técnica / Ferramenta      | Aplicação prática                                                          |
| ------------------------- | -------------------------------------------------------------------------- |
| Layout de repositório IaC | `iac/ ├─ modules/ ├─ envs/ ├─ policies/ ├─ templates/`                     |
| Tagging obrigatório       | `tags = { Environment = "prod", Owner = "appsec", ... }`                   |
| Pre-commit hooks          | Validação de naming, presença de tags e estrutura de ficheiros             |
| Padrão de variáveis       | `variable "environment" { type = string }` obrigatório em todos os módulos |
| Testes semânticos         | OPA/Rego, Conftest para validar impacto real e políticas mínimas           |
| Policy-as-Code            | Bloqueio de permissões amplas, ausência de tags ou naming incorreto        |
| Reutilização controlada   | Templates base para `main.tf`, `variables.tf`, `outputs.tf` validados      |

---

## 🕒 Quando aplicar

| Fase do ciclo de vida   | Ação esperada                                                 |
| ----------------------- | ------------------------------------------------------------- |
| Criação do projeto IaC  | Definir layout e aplicar princípios estruturais               |
| Adição de novos módulos | Rever permissões, naming, outputs e tagging                   |
| Alterações críticas     | Revalidar aderência aos princípios antes de aprovação         |
| Auditoria / revisão     | Verificar rastreabilidade, tagging e minimização de exposição |

---

## 👥 Perfis envolvidos

| Perfil             | Responsabilidades                                                  |
| ------------------ | ------------------------------------------------------------------ |
| DevOps / Cloud     | Implementar estrutura, tagging, segregação e revisão de permissões |
| Segurança / AppSec | Definir políticas default e validar princípios SbD                 |
| Arquitetura        | Aprovar standards de layout, naming e outputs                      |
| Plataforma         | Fornecer scaffolds, templates e validações partilhadas             |

---

## 🧪 Exemplos práticos

* Diretório `envs/prod/` com ficheiro `main.tf`, onde `variable "environment"` é obrigatória;
* Tagging obrigatório em recursos como `aws_instance`, `aws_s3_bucket`, validado por OPA;
* Regra OPA de exemplo:

```rego
deny[msg] {
  input.resource_type == "aws_s3_bucket"
  not input.tags["Environment"]
  msg := "Missing Environment tag on S3 bucket"
}
```

---

## ✅ Benefícios diretos

* Redução do risco estrutural nos ambientes geridos por IaC;
* Prevenção de exposição involuntária de topologia e permissões;
* Consolidação de princípios SbD entre equipas e projetos;
* Capacidade de enforcement técnico consistente e auditável.

---

## 🔗 Referências cruzadas

| Documento                                       | Relação                                      |
| ----------------------------------------------- | -------------------------------------------- |
| `addon/02-validacoes-e-checks.md`               | Validações automáticas e evidência           |
| `addon/03-governanca-modulos.md`                | Governação e supply chain de módulos         |
| `addon/11-uso-ferramentas-automatizadas-iac.md` | Automação e ferramentas assistidas           |
| SAMM (AA2.1, CM1.3)                             | Padrões de arquitetura e controlo de mudança |
| SSDF (CM.5)                                     | Design seguro e separação de ambientes       |
| SLSA                                            | Proveniência e rastreabilidade de código     |
