---
id: matriz-requisitos-iac
title: Matriz de Requisitos Técnicos para Projetos IaC
description: Requisitos específicos para garantir segurança em projetos de Infraestrutura como Código
sidebar_position: 8
---

# 📘 Matriz de Requisitos Técnicos para Projetos IaC

Este catálogo define requisitos de segurança **específicos para projetos de Infraestrutura como Código (IaC)**, que complementam os requisitos aplicacionais definidos no Capítulo 02.  

Estes requisitos são aplicáveis diretamente ao **código, estrutura e práticas dos próprios projetos IaC**, e incluem aspetos tanto **aplicacionais** (ex: versionamento, validação) como **infraestruturais** (ex: controlo de estado, segregação de ambientes, enforcement de políticas).

---

## 📊 Requisitos por nível de risco

| ID       | Requisito                                                                                              | L1 | L2 | L3 | Cap. 2? | Referências                 | Justificação                                                                 |
|----------|---------------------------------------------------------------------------------------------------------|----|----|----|---------|-----------------------------|--------------------------------------------------------------------------------|
| IAC-001  | O projeto IaC deve usar backend remoto autenticado com locking ativado para controlo de estado         |    | X  | X  | -       | SSDF PW.5, Terraform Docs   | Evita concorrência e drift em ambientes críticos                              |
| IAC-002  | Ambientes (dev, QA, prod) devem ser definidos de forma segregada e versionada                           | X  | X  | X  | REQ-004 | CIS 4.5, SSDF PM.2          | Impede alterações acidentais e permite revisão por ambiente                   |
| IAC-003  | Todas as alterações devem ser sujeitas a validações automáticas (syntax, lint, policy, segurança)      | X  | X  | X  | REQ-005 | SSDF PS.2, SLSA Build L2    | Reforça integridade e conformidade contínua                                   |
| IAC-004  | Módulos reutilizados devem ter origem confiável (repositório interno, hash ou verificação manual)      |    | X  | X  | -       | SLSA Source L2, Terraform   | Protege contra código externo malicioso ou obsoleto                           |
| IAC-005  | O histórico de alterações deve ser completo, com tagging e releases rastreáveis                         | X  | X  | X  | REQ-002 | GitOps, SSDF CM.1           | Suporta rollback e auditoria                                                  |
| IAC-006  | Devem existir convenções formais de nomeação, tagging e estrutura de diretórios                         |    | X  | X  | -       | Terraform Best Practices    | Facilita automação, rastreabilidade e revisão                                 |
| IAC-007  | O plano (`terraform plan` ou equivalente) deve ser rastreado e aprovado antes do `apply`               |    | X  | X  | -       | SSDF PW.6                   | Garante controlo de alterações aplicadas                                      |
| IAC-008  | O projeto IaC deve ter rastreabilidade entre ficheiros e os ambientes/recursos que afetam              |    | X  | X  | -       | SSDF CM.5                   | Permite accountability e avaliação de impacto                                 |
| IAC-009  | Devem existir políticas de enforcement aplicadas automaticamente (ex: OPA, Sentinel, Rego, Conftest)   |    |    | X  | -       | SSDF PW.5, SLSA L3          | Reduz risco de erro humano e aplica controlo em pipelines                     |
| IAC-010  | Os artefactos gerados (ex: `plan`, `apply`, manifests) devem ser armazenados com versionamento e hash  |    | X  | X  | -       | SLSA Provenance, SSDF PW.4  | Garante integridade e auditoria de mudanças em tempo                         |

---

## 📎 Notas explicativas

- **IAC-001**: aplica-se a projetos com múltiplos colaboradores e ambientes partilhados.
- **IAC-004**: módulos não verificados podem conter configurações perigosas ou vulnerabilidades.
- **IAC-007**: permite validar *o que será alterado* antes da execução e associar a change request.
- **IAC-009**: enforcement automatizado evita drift organizacional e violações de política.
- **IAC-010**: necessário para rastrear o impacto real do IaC aplicado em ambientes produtivos.

---

## 🧾 Exemplos de evidência

| Requisito   | Evidência sugerida                                                                      |
|-------------|------------------------------------------------------------------------------------------|
| IAC-001     | Configuração de backend remoto (`backend.tf`) com locking ativado                        |
| IAC-003     | Log de execução de linter + scanner (ex: TFLint, tfsec, Checkov)                         |
| IAC-005     | Histórico Git com tags, releases e convenções de commits                                 |
| IAC-007     | Aprovação manual ou automática do `plan` via Pull Request com diff visível               |
| IAC-009     | Política OPA/Rego em CI/CD + resultados visíveis e bloqueio se não conforme              |

---

## 🔗 Relacionado com outros capítulos

<!-- - [Capítulo 02 – Requisitos de Segurança (REQ-XXX)](../../02-requisitos-seguranca) -->
- [Capítulo 06 – Desenvolvimento Seguro](/sbd-toe/sbd-manual/desenvolvimento-seguro/intro)
- [Capítulo 07 – CI/CD Seguro](/sbd-toe/sbd-manual/cicd-seguro/intro)
- [Capítulo 11 – Deploy e Controlo de Execução](/sbd-toe/sbd-manual/deploy-seguro/intro)

