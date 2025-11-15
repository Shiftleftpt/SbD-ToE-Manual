---
id: case-study-anexo-tecnico
title: Anexo Técnico - Aplicação do SbD-ToE ao Pipeline CI/CD
sidebar_position: 9
description: Regras formais para permitir exceções no pipeline, com registo, aprovação, prazo de validade e visibilidade por função.
tags: [exceções, visibilidade, cicd, governação, auditoria, segurança]
---


# 📎 Anexo Técnico - Aplicação do SbD-ToE ao Pipeline CI/CD

Este anexo complementa o estudo de caso de aplicação do manual SbD-ToE ao pipeline CI/CD como projeto L3, fornecendo artefactos técnicos e operacionais reutilizáveis para equipas de engenharia, segurança e governance.

---

## ✅ Checkpoints de Validação por Fase

| Fase          | Validação                           | Ferramenta sugerida         | Capítulo SbD-ToE         |
| ------------- | ----------------------------------- | --------------------------- | ------------------------ |
| Planeamento   | Threat modeling documentado         | IriusRisk, Excel            | Cap. 03 – Threat Model   |
| Design        | Requisitos L3 atribuídos ao projeto | Catálogo do Cap. 02, 07     | Cap. 02, 07 – Requisitos |
| Implementação | Linters, revisão obrigatória        | Semgrep, ESLint, PRs        | Cap. 06 – Dev Seguro     |
| Build         | SBOM gerado para o pipeline         | `syft`, `cyclonedx`         | Cap. 05, 07              |
| Testes        | Validações de segurança ao pipeline | `trivy`, `semgrep`, CI      | Cap. 07, Cap. 10         |
| Deploy        | Proveniência e assinatura           | `cosign`, `slsa-provenance` | Cap. 07, 09              |
| Operações     | Logging, rastreabilidade, alertas   | AuditLogs, Kibana           | Cap. 12 – Monitorização  |

---

## 🧩 User Stories Relevantes

```markdown
**Como engenheiro de DevOps**,  

Quero que o pipeline da plataforma gere um SBOM próprio,  
Para garantir que todas as tasks, containers e SDKs usados estão inventariados e rastreados.

**Como responsável de segurança**,  

Quero aplicar threat modeling formal ao pipeline CI/CD,  
Para identificar vetores de ataque e definir controlos preventivos.

**Como gestor de conhecimento**,  

Quero que o processo de onboarding inclua formação sobre segurança do pipeline,  
Para garantir que todos os contribuidores compreendem o impacto da infraestrutura de entrega.

**Como auditor de segurança**,  

Quero validar se os runners utilizados estão isolados e corretamente configurados,  
Para mitigar riscos de execução maliciosa ou persistência de agentes externos.
```

---

## 📜 Requisitos Aplicáveis

| ID         | Descrição                                                           | Aplicável | Fonte       |
| ---------- | ------------------------------------------------------------------- | --------- | ----------- |
| REQ-L3-001 | O pipeline deve ter SBOM versionado por build                       | ✔         | Cap. 05, 07 |
| REQ-L3-014 | O runner usado deve ser segregado por função                        | ✔         | Cap. 09     |
| REQ-L3-019 | As tasks do pipeline devem ser analisadas quanto a vulnerabilidades | ✔         | Cap. 05, 07 |
| REQ-L3-027 | Toda alteração ao pipeline deve passar por revisão                  | ✔         | Cap. 06     |
| REQ-L3-038 | O pipeline deve ser sujeito a threat modeling explícito             | ✔         | Cap. 03, 07 |
| REQ-L3-045 | O pipeline deve passar por testes de segurança automatizados        | ✔         | Cap. 07, 10 |
| REQ-L3-048 | Deve existir logging e rastreabilidade de execuções                 | ✔         | Cap. 12     |
| REQ-L3-052 | Formação de equipas sobre segurança de CI/CD                        | ✔         | Cap. 13     |

---

## 📋 Checklist Operacional

| Item                                                              | Sim/Não |
| ----------------------------------------------------------------- | ------- |
| O pipeline foi formalmente classificado como ativo L3?            |         |
| Existe threat model documentado e revisto periodicamente?         |         |
| Os runners usados são segregados e controlados?                   |         |
| O próprio pipeline tem SBOM gerado e assinado?                    |         |
| As tasks usadas (ex: GitHub Actions, SDKs) são inventariadas?     |         |
| As dependências do pipeline são sujeitas a análise SCA?           |         |
| O `ci-pipeline.yml` é versionado e tem revisão obrigatória?       |         |
| Foram aplicadas práticas de desenvolvimento seguro ao pipeline?   |         |
| Existe processo formal de exceção e revisão para bypasses?        |         |
| Formação sobre CI/CD seguro foi ministrada às equipas relevantes? |         |
| Testes de segurança foram aplicados ao pipeline?                  |         |
| Rastreabilidade ponta-a-ponta está assegurada (build → deploy)?   |         |

---

## ✅ Considerações Finais

Este anexo traduz a prescrição narrativa do estudo de caso em elementos técnicos concretos e auditáveis, promovendo a **adoção eficaz e rastreável** do SbD-ToE no ciclo de vida dos próprios pipelines.

> 📌 O pipeline é um ativo crítico. Tratar o seu ciclo de vida como o de qualquer outro produto L3 é um passo fundamental para a maturidade em segurança da supply chain.
