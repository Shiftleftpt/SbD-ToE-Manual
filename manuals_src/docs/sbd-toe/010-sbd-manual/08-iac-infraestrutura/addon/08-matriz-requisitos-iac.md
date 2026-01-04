---

id: matriz-requisitos-iac
title: Matriz de Requisitos Técnicos para Infraestrutura como Código
sidebar_position: 8
description: Mapeamento detalhado dos requisitos IAC-001 a IAC-013 com orientação prática para validação, evidência e aplicação proporcional ao risco.
tags: [matriz, requisitos, iac, validacao, controlo, auditoria]
---------------------------------------------------------------

# 📘 Matriz de Requisitos Técnicos para Projetos IaC

Este catálogo define **requisitos de segurança específicos para projetos de Infraestrutura como Código (IaC)**, complementando os requisitos aplicacionais definidos no **Capítulo 02 — Requisitos de Segurança**.

Os requisitos aqui descritos aplicam-se **ao próprio projeto IaC como produto de software**, incluindo:

* código e estrutura do repositório;
* pipelines CI/CD associados;
* módulos, templates e dependências;
* mecanismos de controlo, validação e enforcement.

Esta matriz é **normativa**: cada requisito deve poder ser **validado objetivamente** e gerar **evidência auditável**.

---

## 📊 Requisitos por nível de risco

| ID      | Requisito                                                              |  L1 |  L2 |  L3 | Rel. Cap. 2 | Referências                | Justificação                                         |
| ------- | ---------------------------------------------------------------------- | :-: | :-: | :-: | :---------: | -------------------------- | ---------------------------------------------------- |
| IAC-001 | Backend remoto autenticado com *locking* ativo para controlo de estado |     |  ✓  |  ✓  |      –      | SSDF PW.5, Terraform Docs  | Evita concorrência, corrupção de estado e *drift*    |
| IAC-002 | Ambientes (`dev`, `staging`, `prod`) segregados e versionados          |  ✓  |  ✓  |  ✓  |   REQ-004   | CIS 4.5, SSDF PM.2         | Reduz impacto de erro e permite revisão por ambiente |
| IAC-003 | Validações automáticas obrigatórias (syntax, lint, segurança, policy)  |  ✓  |  ✓  |  ✓  |   REQ-005   | SSDF PS.2, SLSA Build L2   | Garante integridade e bloqueia erro precoce          |
| IAC-004 | Módulos reutilizados com origem confiável e versão imutável            |     |  ✓  |  ✓  |      –      | SLSA Source L2             | Mitiga risco de *supply chain*                       |
| IAC-005 | Histórico completo com versionamento, *tags* e *releases*              |  ✓  |  ✓  |  ✓  |   REQ-002   | GitOps, SSDF CM.1          | Suporta rollback e auditoria                         |
| IAC-006 | Convenções formais de naming, tagging e layout de diretórios           |     |  ✓  |  ✓  |      –      | Terraform Best Practices   | Facilita automação e revisão                         |
| IAC-007 | *Plan* rastreável e aprovado antes de qualquer *apply*                 |     |  ✓  |  ✓  |      –      | SSDF PW.6                  | Garante controlo explícito de mudanças               |
| IAC-008 | Rastreabilidade ficheiro → recurso → ambiente                          |     |  ✓  |  ✓  |      –      | SSDF CM.5                  | Permite avaliação de impacto e accountability        |
| IAC-009 | Enforcement automático de políticas em pipeline                        |     |     |  ✓  |      –      | SSDF PW.5, SLSA L3         | Reduz dependência de revisão manual                  |
| IAC-010 | Artefactos (`plan`, `apply`, manifests) versionados e com hash         |     |  ✓  |  ✓  |      –      | SLSA Provenance, SSDF PW.4 | Garante integridade e evidência                      |
| IAC-011 | Gestão segura de segredos (sem *hardcoding*)                           |  ✓  |  ✓  |  ✓  |   REQ-008   | SSDF PW.6                  | Previne exfiltração e abuso de credenciais           |
| IAC-012 | Deteção automatizada de *drift* entre IaC e estado real                |     |  ✓  |  ✓  |      –      | SSDF CM.5                  | Mantém coerência entre intenção e realidade          |
| IAC-013 | Revisão periódica formal de módulos e templates IaC                    |     |     |  ✓  |      –      | SAMM AA2.2, SR2.2          | Evita propagação de práticas obsoletas               |

---

## 📌 Notas explicativas

* **IAC-001** aplica-se sempre que exista colaboração, *pipelines partilhados* ou múltiplos ambientes.
* **IAC-004** considera qualquer dependência externa como **código não confiável por origem** até validação.
* **IAC-007** materializa o princípio de *change control* técnico em IaC.
* **IAC-009** é requisito estrutural para ambientes de risco elevado (L3).
* **IAC-012** trata *drift* como falha de segurança, não exceção operacional.

---

## 🧾 Exemplos de evidência

| Requisito | Evidência objetiva                               |
| --------- | ------------------------------------------------ |
| IAC-001   | `backend.tf` com *locking* + logs de lock        |
| IAC-003   | Logs de CI com lint, scanners e policies         |
| IAC-005   | Histórico Git com *tags* e *releases*            |
| IAC-007   | PR com *plan* anexado e aprovações               |
| IAC-009   | Regras OPA/Rego + logs de bloqueio               |
| IAC-011   | Integração Vault/KMS/OIDC sem segredos em código |
| IAC-012   | Relatórios periódicos de *drift*                 |
| IAC-013   | Registos de revisão AppSec/DevSecOps             |

---

## 🔗 Relação com outros capítulos

* Cap. 02 — Requisitos de Segurança (REQ-XXX)
* Cap. 06 — Desenvolvimento Seguro
* Cap. 07 — CI/CD Seguro
* Cap. 11 — Deploy e Controlo de Execução
