---
id: policies-relevantes
title: Policies
description: Políticas organizacionais necessárias para enquadrar e reforçar a governação e segurança na utilização de Infrastructure as Code (IaC)
tags: [políticas, infraestrutura como código, cloud, devsecops, pipelines, configuração segura]
sidebar_position: 60
---

# 🏠 Políticas Organizacionais — IaC e Infraestrutura como Código

A aplicação eficaz do **Capítulo 08 – IaC e Infraestrutura como Código** exige a existência de **políticas organizacionais formais** que enquadrem, reforcem e legitimem as práticas de governação técnica, segurança e validação associadas à automatização da infraestrutura.

Estas políticas asseguram que:

- A infraestrutura é tratada como **artefacto de software**, sujeita às mesmas regras de controlo, qualidade e rastreabilidade do código-fonte;
- A gestão de ambientes e recursos é **determinística, auditável e reversível**;
- A segurança e a conformidade são **validadas antes da aplicação** de qualquer alteração de infraestrutura.

---

## 📄 Políticas Organizacionais Relevantes

| Nome da Política | Obrigatória? | Aplicação | Resumo do Conteúdo Necessário |
|------------------|--------------|------------|--------------------------------|
| **Política de Governação de IaC** | ✅ Sim | Todos os repositórios e pipelines que definem ou aplicam infraestrutura | Define princípios, papéis e responsabilidades; requer *code review*, segregação de ambientes, controlo de acesso e aprovação formal antes de *apply*. |
| **Política de Gestão de Segredos e Credenciais em IaC** | ✅ Sim | Repositórios IaC, pipelines e ferramentas de orquestração | Proíbe inclusão de segredos em código; obriga uso de *secret managers*; estabelece *rotation policy*, *scopes* mínimos e monitorização de acessos. |
| **Política de Validação e Testes de Segurança IaC** | ✅ Sim | Pipelines CI/CD e módulos partilhados | Requer execução de *IaC scanning* e *policy-as-code* (tfsec, Checkov, KICS, OPA); validações obrigatórias antes do *merge* e *deploy*. |
| **Política de Hardening e Configuração Segura de Recursos Cloud** | ✅ Sim | Ambientes Cloud, híbridos e on-premises automatizados | Define controlos mínimos (IAM, rede, storage, logging); impõe linhas de base (CIS, ENISA Cloud); obriga detecção e mitigação de *drift*. |
| **Política de Gestão de Módulos e Reutilização de IaC** | ⚠️ Recomendável | Registos internos de módulos e templates | Estabelece critérios de aprovação, versionamento semântico, revisão de segurança e ciclo de vida de módulos reutilizáveis. |
| **Política de Rollback e Recuperação Automatizada** | ⚠️ Reforçada | Ambientes críticos e de produção | Define mecanismos de reversão automatizada e testes periódicos de restauração de configuração e estado; estabelece requisitos de consistência. |
| **Política de Observabilidade e Auditoria de Alterações de Infraestrutura** | ⚠️ Reforçada | Todos os ambientes geridos via IaC | Determina que todas as alterações (automáticas ou manuais) sejam registadas com *commit ID*, *pipeline run* e evidências de aprovação. |

---

## 📈 Correspondência com frameworks normativos

| Framework | Requisitos cobertos pelas políticas acima |
|------------|--------------------------------------------|
| **NIST SSDF v1.1** | PW.5 (build integrity), RV.1 (verification), PS.1 (review of changes). |
| **OWASP SAMM v2.1** | Governance (GOV 1.1–1.2), Deployment (DEP 1.2) — governação, aprovações e rastreabilidade de *deploys*. |
| **BSIMM 13** | CMVM 1.3, SE 2.2, ST 1.1 — conformidade, *config scanning* e validação automatizada. |
| **SLSA v1.0** | L2–L3 (Source & Build Integrity) — rastreabilidade e proveniência de artefactos de infraestrutura. |
| **DSOMM v2** | IaC Security & Configuration Management — governação, validação e segurança de módulos. |
| **CIS Controls v8** | Control 4 (Secure Configurations), Control 16 (Application Security). |
| **ENISA Cloud Security Baseline** | Secção 3 (Cloud Configuration and Change Management). |

---

## 📃 Estrutura mínima de cada política

Cada política deve conter, no mínimo:

- **Objetivo e âmbito** (tecnologias, ambientes, equipas abrangidas);  
- **Papéis e responsabilidades** (DevOps, Cloud Engineer, AppSec, Auditoria);  
- **Critérios obrigatórios e controlos técnicos** (validações automáticas, *gates*, segregação);  
- **Integração CI/CD** (momentos de verificação, *policy-as-code*, aprovação);  
- **Evidências rastreáveis** (logs, relatórios, *pull requests*);  
- **Frequência de revisão e auditoria de conformidade.**

---

## ✅ Recomendações finais

- As políticas devem ser **publicadas e geridas centralmente** no repositório de políticas técnicas da organização.  
- Devem estar **integradas nos pipelines CI/CD** como mecanismos automáticos de conformidade (*policy enforcement*).  
- A sua aplicação deve ser **avaliada nos checklists de revisão por projeto** do capítulo e em auditorias de segurança.  
- Recomenda-se alinhamento contínuo com **benchmarks CIS/ENISA** e com práticas dos *cloud providers*.  
- A conformidade com estas políticas é **critério formal de maturidade** em segurança de infraestrutura e DevSecOps.

> 📁 Templates ou exemplos detalhados destas políticas poderão ser incluídos em versões futuras como ficheiros complementares `60-*.md` do manual.
