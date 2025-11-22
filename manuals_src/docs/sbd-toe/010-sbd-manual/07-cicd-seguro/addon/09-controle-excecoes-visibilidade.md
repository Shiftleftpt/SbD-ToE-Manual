---
description: Regras formais para permitir exceções no pipeline, com registo, aprovação,
  prazo de validade e visibilidade por função.
id: controle-excecoes-visibilidade
sidebar_position: 9
tags:
- auditoria
- cicd
- excecoes
- exceções
- governanca
- seguranca
- visibilidade
title: Controlo de Exceções e Visibilidade Organizacional
---



# 🧭 Controlo de exceções e visibilidade organizacional

Mesmo com pipelines bem definidos, é inevitável que ocorram exceções - falhas temporárias, necessidades urgentes, aplicações legadas ou contextos específicos.

Esta prática define como gerir **exceções de forma controlada, rastreável e aprovada**, e como garantir **visibilidade organizacional sobre conformidade, desvios e evolução das práticas** no CI/CD.

> Exceções inevitáveis não podem ser invisíveis nem permanentes.

---

## 🎯 Objetivos

- Permitir exceções justificadas, com controlo e responsabilização;
- Detetar incumprimentos sistemáticos ou acidentais das políticas de pipeline;
- Fornecer visibilidade técnica e executiva sobre o estado de segurança e maturidade CI/CD.

---

## 🛠️ Práticas

1. **Gestão formal de exceções**  
   - Toda exceção deve ser registada com motivo, impacto, responsável e prazo de validade;
   - A aprovação deve ser formal (ex: ticket, comentário com reviewer, label `bypass-*`).

2. **Exceções visíveis no pipeline e nos relatórios**  
   - Devem ser **explicitamente assinaladas** em logs, artefactos ou metadados de execução;
   - Exceções devem ter expiração e estar sujeitas a revisão.

3. **Métricas agregadas de conformidade e exceções**  
   - Exemplos de indicadores:  
     - % de pipelines com SAST ativo;  
     - Nº de exceções por categoria;  
     - Aplicações L3 sem enforcement ativo.

4. **Alertas de desvios críticos ou repetidos**  
   - Detetar e sinalizar situações como:  
     - Uso recorrente de `--force`;  
     - Deploys sem gates;  
     - Builds sem proveniência ou sem validações.

5. **Reporting técnico e executivo**  
   - Relatórios e dashboards periódicos com:  
     - Ações corretivas para equipas técnicas;  
     - Indicadores de risco e maturidade para gestão.

---

## ⚖️ Aplicação proporcional por nível de risco

| Nível | Exceções permitidas                         | Controlo esperado                                           |
|-------|----------------------------------------------|-------------------------------------------------------------|
| **L1** | Exceções técnicas justificadas               | Registo simples (ex: label, comentário)                     |
| **L2** | Aprovadas por lead técnico ou segurança      | Registo + data de expiração + plano de revisão              |
| **L3** | Exceções mínimas e temporárias               | Aprovadas formalmente; obrigam mitigação paralela ou compensatória |

---

## 📌 Exemplos práticos

- **GitHub Actions**  
  - Labels como `bypass-security-gate`; aprovação visível no PR;  
  - Métricas com GitHub Insights + Scorecard.

- **GitLab CI**  
  - Ficheiro `exception.yaml` no MR; revisão por `Security Approval`;  
  - Dashboards com % de políticas aplicadas por projeto.

- **Azure DevOps**  
  - Exceções em `release override`, associadas a Work Items;  
  - Dashboards (nativos ou Power BI) com KPIs por pipeline.

- **Jenkins**  
  - Comentários manuais no `Jenkinsfile`; uso de flags `bypass=true`;  
  - Integração com Jira ou ServiceNow para controlo formal.

---

## 📉 Riscos mitigados

- Bypass silencioso de políticas de segurança (OSC&R: CI0002);
- Ausência de rastreabilidade em falhas intencionais ou técnicas;
- Incapacidade de avaliar a maturidade global de CI/CD;
- Repetição sistemática de exceções sem ação corretiva.

---

