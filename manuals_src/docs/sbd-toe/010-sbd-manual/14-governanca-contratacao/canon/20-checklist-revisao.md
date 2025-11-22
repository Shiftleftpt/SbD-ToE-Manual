---
id: checklist-revisao
title: ✅ Checklist SbD-ToE - Governança e Contratação
sidebar_position: 20
description: Checklist binário de controlo da aplicação das práticas de governação por projeto
tags: [aprovacao, checklist, contratacao, controlo, excecoes, projeto, revisao]
---


# ✅ Checklist de Revisão Periódica - Governança e Contratação

Este checklist aplica-se a **projetos, aplicações ou contratos** com impacto técnico e visa validar a aplicação prática das práticas prescritas no Capítulo 14 - Governança e Contratação.

> 📌 Deve ser usado em revisões formais, auditorias internas, milestones de projeto ou ciclos de revalidação técnica.

---

## 📋 Itens de Verificação

| Item                                                                                                                   | Verificado? |
|------------------------------------------------------------------------------------------------------------------------|-------------|
| Existe owner de segurança formalmente designado para o projeto ou aplicação?                                          | ☐           |
| O nível de criticidade (L1–L3) está documentado e justificado?                                                         | ☐           |
| Os requisitos mínimos proporcionais ao risco estão identificados e aplicados?                                         | ☐           |
| Existem exceções aprovadas com owner, validade, compensação e rastreabilidade formal (`excecoes.yaml`, contratos)?    | ☐           |
| Foram incluídas cláusulas de segurança nos contratos ou acordos com terceiros?                                         | ☐           |
| Os fornecedores com acesso técnico foram validados com base em checklist/questionário definidos?                      | ☐           |
| A aplicação ou sistema está incluída na matriz de controlo das práticas SbD-ToE (ex: `09-controle-praticas-sbd.md`)?  | ☐           |
| Existe evidência formal (ficheiros, issues, wiki) de revisão da conformidade técnica e contratual?                    | ☐           |
| As políticas organizacionais relacionadas com segurança, contratação e exceções estão formalmente aprovadas e auditadas (`60`)? | ☐           |
| Existem KPIs definidos e reportados relacionados com exceções, cobertura de práticas e conformidade?                  | ☐           |
| Está definida uma revisão programada (libertação, recontratação, auditoria) com base nestes dados?                    | ☐           |
| Todos os decisores (owners, aprovadores, reviewers) têm formação SbD válida nos últimos 12 meses (Cap. 13)?           | ☐           |

---

## 🔄 Integração Operacional

- Pode ser usado como **template de revisão recorrente** em Jira, Confluence, SharePoint ou Forms;
- Deve ter validação conjunta por **AppSec, GRC e gestão de produto**;
- Cada item exige **evidência rastreável e versionada**, conforme práticas do Cap. 14.

---

## 🎯 Conformidade e Indicadores

- A validação positiva deste checklist permite declarar **conformidade com o Capítulo 14 - Governança e Contratação**.
- Os resultados podem ser integrados em **dashboards, ciclos de auditoria e métricas de maturidade**.
- Permite derivar **KPIs objetivos** como:
  - % de aplicações com exceções formalmente aprovadas;
  - % de fornecedores validados;
  - % de contratos com cláusulas de segurança;
  - % de projetos com matriz de controlo SbD-ToE atualizada.

---

## 🔗 Ligações cruzadas

- **Cap. 01** - Classificação de risco (base para aplicação proporcional)
- **Cap. 02** - Requisitos de segurança (alvo de exceções, rastreabilidade)
- **Cap. 05** - Dependências e SBOM (cláusulas e validações contratuais)
- **Cap. 10** - Testes de segurança (validação prática de controlos)
- **Cap. 13** - Formação (validação obrigatória de funções críticas)
- **Cap. 14.08** - Governação Integral
- **Cap. 14.09** - Controlo Consolidado das Práticas SbD-ToE

> ✅ Este checklist é um mecanismo central de controlo contínuo, proporcional e rastreável da adoção do modelo SbD-ToE em contextos reais de governação e contratação.
