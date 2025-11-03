---
id: manual-formacao-capitulos
title: Manual de Formação por Capítulo do SbD-ToE
description: Guia técnico de formação contínua com ligação direta a cada capítulo do manual.
tags: [formacao, manual, por capitulo, sbdtoe, referencia cruzada]
---


# 👥 Manual de Formação por Perfil

## 🌟 Objetivo

Organizar os conteúdos formativos sugeridos pelo manual SbD-ToE por **perfil funcional técnico**.  
Este documento serve de base para:

- Construção de **trilhos práticos por função**
- **Onboarding técnico estruturado**
- Planos de **retenção e rotação de conhecimento**

> 📌 Alinhado com o Capítulo 01 — Gestão de Risco, a aplicação proporcional por nível de risco deve modular a profundidade dos conteúdos.

---

## 🧬 Conteúdos sugeridos por função

### 👤 Dev (Desenvolvedores)

| Tópico                                    | Formato recomendado                   |
|-------------------------------------------|----------------------------------------|
| Secure coding                             | Labs com falhas reais (ex: Juice Shop) |
| Pull Requests seguros                     | Templates + Code Clinics quinzenais    |
| Threat Modeling por feature               | Sessões peer-led                       |
| Gestão de dependências                    | Labs com lockfiles, SCA, SBOM          |
| Pipelines com scanners                    | Oficina de integração                  |
| Controlo de tokens                        | Simulação de abuso + revisão de scope  |
| Uso seguro de imagens Docker              | Hardening prático                      |

---

### 👤 QA (Testers / Quality Assurance)

| Tópico                                    | Formato recomendado                   |
|-------------------------------------------|----------------------------------------|
| Critérios de aceitação com segurança      | Revisão cruzada + exemplos reais       |
| Testes de segurança (SAST, DAST, fuzzing) | Labs dirigidos + simulação             |
| Participação em Threat Modeling           | Sessões por épico                      |
| Validação de requisitos                   | Checklist + labs funcionais            |
| Análise de alertas e falsos positivos     | War Room + tuning de deteção           |
| Revisão de bugs com causa de segurança    | Estudo de caso interno                 |

---

### 👤 PO (Product Owners)

| Tópico                                    | Formato recomendado                   |
|-------------------------------------------|----------------------------------------|
| Classificação de risco                    | Workshop + exercício guiado            |
| Priorização de requisitos de segurança    | Sessão prática + exemplos históricos   |
| Gestão de exceções justificadas           | Revisão rotativa + análise de impacto  |
| Implicações legais (NIS2, DORA)           | Formação executiva                     |
| Storytelling de falhas reais              | Repositório interno + partilha em retro|

---

### 👤 DevOps / Engenharia de Plataforma

| Tópico                                    | Formato recomendado                   |
|-------------------------------------------|----------------------------------------|
| Pipelines CI/CD com segurança             | Oficina de stages com scanners         |
| Gestão de segredos                        | Lab com Vault e escopos                |
| Hardening de imagens                      | PR review + análise com Trivy          |
| Scanners de IaC e validação               | Hands-on com Checkov/TFSec             |
| Deploy com rollback e feature flags       | Simulação de rollout                   |
| Alertas e tuning                          | War Room + dashboards operacionais     |

---

### 👤 AppSec (Segurança Aplicacional)

| Tópico                                    | Formato recomendado                   |
|-------------------------------------------|----------------------------------------|
| Facilitação de Threat Modeling            | Formação + sessões reais               |
| Criação de trilhos formativos             | Alinhamento com Cap. 13 e Cap. 1       |
| Análise de dependências e vulnerabilidades| Casos práticos com SBOM + SCA          |
| Revisão de PRs + pairing                  | Sessões regulares com equipas          |
| Operação de CTFs, quizzes, war rooms      | Plano de atividades rotativas          |
| Governação de métricas                    | Dashboard + follow-up                  |

---

### 👤 Gestão (Team Leads, Executivos, Segurança Organizacional)

| Tópico                                    | Formato recomendado                   |
|-------------------------------------------|----------------------------------------|
| Governança da formação e rastreabilidade  | Relatórios + auditoria de trilhos      |
| Requisitos contratuais (terceiros)        | Sessões jurídicas + cláusulas padrão   |
| Métricas de maturidade                    | Análise de KPIs de segurança/formação  |
| Promoção de Champions                     | Plano de visibilidade interna          |
| Participação em post-mortems              | Ações corretivas com reforço cultural  |

---

## ✅ Boas práticas

- Definir **trilhos por perfil + risco (L1–L3)** com base neste mapeamento
- Incluir ações no **backlog, LMS, ou planos de onboarding**
- Medir **retenção e eficácia** com quizzes, labs, shadowing ou PRs reais
- Envolver **Champions** na curadoria e facilitação da formação contínua

---

## 📎 Referências cruzadas

| Documento                          | Relação direta                        |
|------------------------------------|----------------------------------------|
| `02-trilho-formativo.md`           | Matriz formal por perfil e risco       |
| `01-catalogo-formativo.md`         | Mapeamento por capítulo e formato      |
| `03-programa-champions.md`         | Multiplicadores na disseminação        |
| `90-indicadores-metricas.md`       | KPIs por perfil e por conteúdo         |

---

> 🎯 A formação por perfil é a base prática da aplicação proporcional do SbD-ToE.  
> A sua eficácia depende da **relevância contextual, repetição prática e validação por pares**.
