---
id: policies-iac
title: Políticas Organizacionais sobre Infraestrutura como Código (IaC)
sidebar_position: 60
description: Políticas organizacionais formais que legitimam, reforçam e auditam a aplicação das práticas de segurança em projetos de IaC.
tags: [políticas, iac, infraestrutura como código, controlo organizacional, ssdf, slsa]
---


# 🏠 Políticas Organizacionais — Infraestrutura como Código (IaC) {iac-infraestrutura:canon:policies-iac}

A aplicação eficaz do Capítulo 08 — Infraestrutura como Código (IaC) — requer a existência de **políticas organizacionais formais** que regulem a forma como o código de infraestrutura é escrito, validado, aprovado, aplicado e auditado.

---

## 📌 Nota fundamental {iac-infraestrutura:canon:policies-iac#nota_fundamental}

> ⚠️ As práticas técnicas descritas neste capítulo (controlo de estado, validações automáticas, segregação de ambientes, controlo de origem e rastreabilidade) **devem estar legitimadas por políticas organizacionais aprovadas**.

Estas políticas:

* Tornam **obrigatória e auditável** a adoção das boas práticas de IaC;
* Regulam a **forma de aprovação e validação de alterações** a infraestrutura;
* Permitem a **automatização de controlo organizacional** sobre ambientes de execução.

> 📑 Este capítulo **executa as regras definidas nestas políticas**, que são a referência formal obrigatória para conformidade em ambientes de produção.

> 📁 A existência destas políticas é **recomendada por frameworks como SSDF, SLSA, OWASP IaC, SAMM e DSOMM**.

---

## 📄 Políticas recomendadas {iac-infraestrutura:canon:policies-iac#politicas_recomendadas}

| Nome da Política                                    | Obrigatória? | Aplicação                                   | Resumo do conteúdo necessário                       |
| --------------------------------------------------- | ------------ | ------------------------------------------- | --------------------------------------------------- |
| Política de Estado e Backend IaC                    | ✅ Sim        | Todos os repositórios Terraform e similares | Uso de backend remoto, locking, registo de estado.  |
| Política de Validação Automática de IaC             | ✅ Sim        | Todos os pipelines de IaC                   | Linters, scans, enforcement de OPA ou equivalente.  |
| Política de Origem e Aprovação de Módulos           | ✅ Sim        | Uso de módulos externos ou internos         | Origem validada, pinning, auditoria.                |
| Política de Segregação e Naming de Ambientes        | ⚠️ Opcional  | Ambientes partilhados, pipelines multi-env  | Diretórios, tags, prefixos, isolamento.             |
| Política de Rastreabilidade e Versionamento         | ✅ Sim        | Artefactos de aplicação IaC (plan, apply)   | Hash, assinatura, retenção, mapping PR → recurso.   |
| Política de Aprovação e Revisão de `terraform plan` | ✅ Sim        | Execução em ambientes produtivos            | Revisão obrigatória, logging, reviewers designados. |
| **Política de Gestão de Exceções IaC**              | ⚠️ Opcional  | Execuções com bypass, flags ou validações desativadas | Justificação formal, owner, prazo, reapreciação.     |

---

## 🔗 Correspondência com frameworks normativas {iac-infraestrutura:canon:policies-iac#correspondencia_com_frameworks_normativas}

| Framework      | Requisitos cobertos pelas políticas acima                                      |
| -------------- | ------------------------------------------------------------------------------ |
| **NIST SSDF**  | PW.5 (Automated Verification), CM.5 (Change Tracking), RV.3 (Vuln Management)  |
| **SLSA v1.0**  | Provenance enforcement, policy controls in CI/CD pipelines                     |
| **OWASP IaC**  | IaC Policy Management, Secret Management, Drift Detection                      |
| **SAMM v2.1**  | Implementation > Environment Hardening, Verification > Architecture Assessment |
| **OWASP DSOMM**| IaC Practices, Control Mapping, Governance Integration, Exception Management   |

---

## 📊 Estrutura sugerida de cada política {iac-infraestrutura:canon:policies-iac#estrutura_sugerida_de_cada_politica}

Cada política organizacional deve conter:

* **Objetivo e âmbito** claro (projetos, ambientes, ferramentas);
* **Critérios obrigatórios** (ex: tipos de scans, ferramentas exigidas, naming);
* **Papéis e responsabilidades** (DevOps, AppSec, Infra, Reviewer);
* **Exigência de documentação e validação** (PRs, pipelines);
* **Periodicidade de revisão** (anual ou por alteração de tooling);
* **Integração com evidências técnicas** (logs, artefactos, aplicação de controlos).

---

## ✅ Recomendações finais {iac-infraestrutura:canon:policies-iac#recomendacoes_finais}

* As políticas devem ser **formuladas em conjunto pelas equipas de segurança e operações**;
* Devem estar **documentadas e acessíveis** no repositório de conformidade ou governaça;
* A sua execução deve ser **validada e auditada regularmente**, como parte de revisões técnicas ou gates de release;
* Devem existir **KPIs de aplicação e conformidade** agregados por projeto, equipa e pipeline.

> 📍 Exemplos de templates poderão ser incluídos em ficheiros `60-*.md` complementares numa fase posterior.
