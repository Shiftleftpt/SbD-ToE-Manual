---
id: governanca-modulos
title: Governação de Módulos e Reutilização Segura
sidebar_position: 3
description: Práticas de gestão e aprovação de módulos reutilizáveis em projetos IaC, garantindo rastreabilidade e segurança.
tags: [governação, módulos, iac, reutilização, segurança, rastreabilidade]
---


# 🛡️ Governação de Módulos Reutilizáveis em IaC

## 🌟 Objetivo

Assegurar que os módulos reutilizados em projetos de Infraestrutura como Código (IaC) — sejam internos ou externos — são:

* Provenientes de fontes confiáveis;
* Versionados e rastreáveis;
* Aprovados e auditáveis;
* Documentados e mantidos com política de ciclo de vida definida.

> A reutilização sem governação formal de módulos representa um **risco sistémico**: uma única má prática pode propagar-se por múltiplos projetos e ambientes.

---

## 📌 O que deve ser feito

1. Catalogar os módulos internos com informação sobre origem, responsável e versão;
2. Verificar a proveniência e integridade de módulos externos antes da adoção;
3. Impedir o uso de módulos não validados em ambientes críticos (ex: produção);
4. Controlar versões e reforçar imutabilidade — evitar `main`, `latest` ou referências flutuantes;
5. Documentar uso, parâmetros, dependências e outputs esperados por módulo;
6. Aplicar validações automáticas a módulos internos antes de os disponibilizar publicamente;
7. Rever e atualizar periodicamente os módulos críticos em uso ativo.

---

## ⚙️ Como aplicar

| Ação                       | Prescrição                                                                  |
| -------------------------- | --------------------------------------------------------------------------- |
| **Módulos internos**       | Repositório central versionado, com CI/CD, tagging semântico e documentação |
| **Módulos externos**       | Validar manualmente ou usar `source` com hash/versão fixa (`?ref=v1.2.0`)   |
| **Trusted sources**        | Definir whitelist: `registry.terraform.io`, `github.com/org/`, etc.         |
| **Controlo de versões**    | Impedir `main`, `latest`; definir `>=`, `~>` com precisão                   |
| **Registo de aprovação**   | Associar cada módulo a análise de risco e aprovação explícita               |
| **Validação automatizada** | Linters, testes e `terraform-docs` antes de `publish`                       |
| **SBOM / inventário**      | Incluir lista de módulos nos artefactos de deploy                           |

---

## 🕒 Quando aplicar

| Momento                               | Ação esperada                                                           |
| ------------------------------------- | ----------------------------------------------------------------------- |
| Inclusão de novo módulo externo       | Validar fonte, versionamento e conformidade                             |
| Criação/atualização de módulo interno | Validar sintaxe, segurança e outputs antes de release                   |
| Revisão de segurança                  | Verificar se módulos em uso são suportados e livres de vulnerabilidades |
| Pipeline de build                     | Confirmar que os módulos referenciados são aprovados e atualizados      |

---

## 👥 Perfis envolvidos

| Papel              | Responsabilidade técnica                                                 |
| ------------------ | ------------------------------------------------------------------------ |
| DevOps             | Integração dos módulos e verificação de conformidade técnica             |
| Arquitetura        | Aprovação de padrões modulares e repositórios autorizados                |
| Segurança          | Validação de origem, integridade e manutenção dos módulos externos       |
| Cloud / Plataforma | Gestão do repositório interno e da política de ciclo de vida dos módulos |

---

## 🧪 Exemplos práticos

* Utilização segura de módulo externo:

  ```hcl
  source = "git::https://github.com/org/vpc-module.git?ref=v1.2.3"
  ```
* Definição de fontes confiáveis no pipeline:

  ```bash
  ALLOW_MODULES_FROM = ["registry.terraform.io/org/", "github.com/org/"]
  ```
* Pipeline de CI que publica módulo apenas após:

  * `tflint` (linting)
  * `checkov` (segurança)
  * `terraform-docs` (documentação atualizada)
* Tabela interna de inventário:

  * Nome do módulo, owner, versão, última atualização, ambientes afetados

---

## ✅ Boas práticas

* Centralizar módulos internos num repositório com regras de publicação;
* Evitar dependência de módulos com manutenção descontinuada ou sem histórico confiável;
* Estabelecer uma política formal de revisão e aprovação de módulos;
* Monitorizar periodicamente o uso de módulos externos e a sua manutenção *upstream*;
* Garantir que as equipas conhecem os critérios para uso e criação de módulos reutilizáveis.

---

## 🔗 Referências cruzadas

| Documento                     | Relação com esta prática                         |
| ----------------------------- | ------------------------------------------------ |
| `02-matriz-requisitos-iac.md` | Requisitos `IAC-004`, `REQ-006`, `REQ-007`       |
| SSDF (PW\.4, CM.3)            | Governação de componentes reutilizados           |
| SLSA (Source L2)              | Controlo de integridade e proveniência de código |
| CIS Controls (2.3, 2.5, 8.6)  | Gestão segura de software e código reutilizado   |

---

> 📌 A governação de módulos é um **elemento crítico de segurança em IaC**. Módulos inseguros, obsoletos ou mal mantidos podem comprometer múltiplos ambientes de forma transversal — exigindo políticas claras, validação contínua e rastreabilidade.
