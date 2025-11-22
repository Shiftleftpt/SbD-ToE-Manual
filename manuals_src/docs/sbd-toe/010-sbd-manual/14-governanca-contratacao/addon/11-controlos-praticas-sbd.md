---
description: Formas de validar, reforçar e governar a aplicação dos controlos definidos
  noutros capítulos do SbD-ToE
id: controlos-praticas-sbd
sidebar_position: 11
tags:
- cat_operacional
- controlo
- enforcement
- governanca
- governação
- validacao
- validação
title: Controlos de Governança sobre as Práticas do SbD-ToE
---



# 🧮 Controlo Sistemático das Práticas do SbD-ToE

Este documento define o modelo de **controlo sistemático e contínuo** da aplicação das práticas prescritas ao longo de todos os capítulos do manual *Security by Design - Theory of Everything (SbD-ToE)*.

> 📌 O objetivo é assegurar que **todas as práticas de segurança são efetivamente aplicadas, rastreadas, validadas e auditadas** por aplicação, ao longo do tempo.

---

## 🧭 Governação das práticas por domínio técnico

| Capítulo / Domínio Técnico             | Mecanismos de Governação Esperados                                               | Exemplos de Evidência / KPI                         |
|----------------------------------------|----------------------------------------------------------------------------------|-----------------------------------------------------|
| **Cap. 02 - Requisitos**               | Validação da aplicação por L1–L3, gestão de exceções, evidência de rastreabilidade | Checklist aplicado, % de REQ aplicados / justificados |
| **Cap. 03 - Threat Modeling**          | Execução por milestone, owner definido, atualização periódica                   | Modelos por aplicação, histórico de revisões        |
| **Cap. 05 - Dependências e SBOM**      | Geração automática de SBOM, análise SCA, registo de findings                    | Relatórios de findings, % resolvidos e justificados |
| **Cap. 07 - CI/CD Seguro**             | Validação de pipelines, rastreio de execuções, controlo de bypass               | Execuções auditadas, aprovações formais de bypass   |
| **Cap. 08 - IaC Seguro**               | Validação contínua de módulos, owners por ambiente, rastreabilidade             | Issues + owners por recurso, % de módulos validados |
| **Cap. 09 - Containers e Imagens**     | Aplicação de políticas de imagem, validações de origem e assinatura             | Catálogo validado, evidência de scanner             |
| **Cap. 10 - Testes de Segurança**      | Execução por L1–L3, gestão de findings, revalidação periódica                   | Evidência de testes, plano de resolução             |
| **Cap. 11 - Deploy e Execução**        | Validação de runtime, isolamento, execuções controladas                         | Controlo de execuções, logs versionados             |
| **Cap. 13 - Formação e Terceiros**     | Verificação de formação por perfil, onboarding com validação                    | Lista de formação por função, checklist onboarding  |

---

## 🧩 Formato do controlo por aplicação

Cada aplicação deve ter um **repositório de conformidade**, com:

- Checklist binário por capítulo (`20-checklist-revisao.md`)
- Estado de aplicação por prática (sim / exceção / não se aplica)
- Evidência de validação e aprovação
- Histórico de alterações e decisões

> ⚠️ Devem existir ficheiros rastreáveis e versionados (ex: `.yaml`, `.md`, dashboards GRC).

---

## 🔁 Ciclo de validação contínua

| Fase                      | Ação esperada                                    |
|---------------------------|--------------------------------------------------|
| 🧱 Início de projeto       | Ativar mecanismos de controlo e owners por prática |
| 📥 Integração de mudanças  | Rever estado dos controlos impactados            |
| 🚀 Pré-release             | Verificar conformidade e exceções justificadas   |
| 📊 Auditoria / revisão     | Validar estado geral por capítulo e domínio       |

---

## 📡 Supervisão, KPIs e Escalonamento

- O estado das práticas deve ser **consolidado em dashboards operacionais** com:

  - % de práticas cumpridas por aplicação / equipa
  - Exceções abertas por capítulo
  - Ciclo médio de revalidação

- As falhas persistentes devem ser **reportadas à gestão de risco ou GRC** com plano de ação.

---

## ✅ Conclusão

Este modelo permite:

- Governar a adoção do SbD-ToE de forma contínua, transparente e auditável
- Consolidar informação de segurança de todas as aplicações num ponto único
- Sustentar decisões, auditorias e evolução da maturidade com base em evidência

> 📌 Este controlo é a base da **governação integral da segurança aplicacional**, e deve ser ativado por todas as equipas que adotem o SbD-ToE.
