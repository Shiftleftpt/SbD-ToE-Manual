---
id: ameacas-mitigadas
title: Ameaças Mitigadas - Testes de Segurança
description: Visão bottom-up das ameaças mitigadas pelas práticas de testes de segurança deste capítulo.
tags: [ameaças, mitigação, segurança, testes, osc&r, stride, capec, ssdf]
sidebar_position: 50
---


# 🔐 Ameaças Mitigadas - Capítulo 10: Testes de Segurança

Este capítulo define a estratégia, técnicas e ferramentas de **validação contínua da segurança da aplicação**, incluindo testes estáticos, dinâmicos, interativos, fuzzing, validação de regressão e pentesting.

> ⚠️ As ameaças mitigadas por este capítulo são **técnicas e contextuais**, surgem na implementação e execução do software - e requerem **validação ativa e contínua para serem detetadas e corrigidas**.

---

## 🧪 Categoria 1 – Vulnerabilidades no código ou lógica de aplicação

| Ameaça                            | Fonte                              | Como surge                                            | Como a prática mitiga                                                  | Controlos associados                        | 🧹 Mitigada apenas por este capítulo? |
|-----------------------------------|-------------------------------------|-------------------------------------------------------|-------------------------------------------------------------------------|---------------------------------------------|----------------------------------------|
| Injeções (SQLi, OS Command, etc.) | OWASP Top 10 A01 / CAPEC-66        | Falta de sanitização ou validação                     | Detetadas por SAST + DAST com testes parametrizados                     | `addon/01-sast.md`, `addon/02-dast.md`      | ✅                                     |
| Falhas de controlo de acesso      | OWASP Top 10 A01 / ASVS V4 / STRIDE| Controlo de permissões mal implementado               | Validadas por DAST + IAST + testes manuais                              | `addon/02-dast.md`, `addon/03-iast.md`      | ✅                                     |
| Lógicas de negócio exploráveis    | OWASP Top 10 A04 / BSIMM           | Fluxos lógicos que permitem bypass ou fraude          | Requerem fuzzing, IAST e pentesting com contexto                        | `addon/04-fuzzing.md`, `addon/11-pen-testing.md` | ✅                              |

---

## 🔍 Categoria 2 – Defeitos regressivos e falhas reintroduzidas

| Ameaça                            | Fonte                              | Como surge                                         | Como a prática mitiga                                                    | Controlos associados                         | 🧹 Mitigada apenas por este capítulo? |
|-----------------------------------|-------------------------------------|----------------------------------------------------|----------------------------------------------------------------------------|----------------------------------------------|----------------------------------------|
| Regressão de segurança            | OWASP SAMM / SSDF PW.8 / DSOMM     | Código novo reintroduz falha previamente corrigida | Testes de regressão com critérios de cobertura e automação                | `addon/05-validacao-regressao.md`            | ✅                                     |
| Baixa cobertura dos testes        | OWASP SAMM / CAPEC / DSOMM         | Testes ignoram áreas críticas                      | Estratégia de cobertura baseada em risco + matriz de priorização          | `addon/06-cobertura-e-priorizacao.md`        | ✅                                     |
| Falhas conhecidas não testadas    | BSIMM / ISO 27034 / DSOMM          | Ausência de ligação entre findings e testes         | Integração com findings e feedback das equipas para aprendizagem contínua | `addon/08-gestao-findings.md`, `addon/09-feedback-equipa.md` | ✅                    |

---

## ⚠️ Categoria 3 – Falta de visibilidade sobre falhas de segurança

| Ameaça                               | Fonte                                | Como surge                                      | Como a prática mitiga                                                       | Controlos associados                          | 🧹 Mitigada apenas por este capítulo? |
|--------------------------------------|---------------------------------------|-------------------------------------------------|--------------------------------------------------------------------------------|------------------------------------------------|----------------------------------------|
| Falhas detetadas mas não resolvidas | SSDF RV.1 / BSIMM / OSC&R / DSOMM    | Findings ignorados ou mal atribuídos            | Processo de gestão de findings com owner, risco e rastreio                    | `addon/08-gestao-findings.md`                 | ✅                                     |
| Equipa sem feedback técnico          | BSIMM Intelligence / SAMM / DSOMM    | Falhas reportadas não chegam aos developers     | Integração sistemática de findings nos ciclos de feedback                     | `addon/09-feedback-equipa.md`                 | ✅                                     |
| Validações não repetíveis           | ISO 27034 / SSDF PW.7 / DSOMM        | Testes manuais sem base reutilizável            | Estratégia formal e automatização de testes                                  | `addon/00-estrategia-testes.md`, `addon/07-integracao-pipeline.md` | ✅                |

---

## 🛠️ Categoria 4 – Falta de integração no ciclo de vida

| Ameaça                                     | Fonte                             | Como surge                                          | Como a prática mitiga                                                           | Controlos associados                          | 🧹 Mitigada apenas por este capítulo? |
|--------------------------------------------|------------------------------------|-----------------------------------------------------|----------------------------------------------------------------------------------|------------------------------------------------|----------------------------------------|
| Testes manuais não escaláveis              | SSDF PW.5 / SLSA Build / DSOMM     | Não se testa a cada alteração                       | Integração em CI/CD com execução automática por tipo de alteração              | `addon/07-integracao-pipeline.md`             | ✅                                     |
| Falta de testes antes de go-live           | ISO 27034 / SSDF PW.7              | Deploy feito sem cobertura mínima validada         | Checklist com critérios de testes mínimos e rastreio de resultados             | `20-checklist-revisao.md`               | ❌ Cap. 01                             |
| Decisão de qualidade feita sem base        | BSIMM QA / SAMM / DSOMM            | Go/no-go baseado em perceção                        | Métricas de cobertura, findings, risco e histórico                              | `addon/06-cobertura-e-priorizacao.md`         | ✅                                     |

---

## 🧐 Categoria 5 – Incapacidade de detetar novas classes de vulnerabilidades

| Ameaça                                     | Fonte                              | Como surge                                           | Como a prática mitiga                                                              | Controlos associados                          | 🧹 Mitigada apenas por este capítulo? |
|--------------------------------------------|-------------------------------------|------------------------------------------------------|-------------------------------------------------------------------------------------|------------------------------------------------|----------------------------------------|
| Classes novas não detetadas por SAST/DAST  | ENISA DevSecOps / BSIMM PenTest    | Ferramentas automatizadas com dicionário fixo       | Pentesting com foco em comportamentos, fluxos e padrões anómalos                   | `addon/11-pen-testing.md`                     | ✅                                     |
| Testes superficiais sem contexto técnico   | STRIDE / CAPEC / ASVS              | Falta de compreensão da arquitetura ou risco         | Alinhamento dos testes com criticidade, arquitetura e ameaça                       | `addon/00-estrategia-testes.md`               | ✅                                     |
| Ferramentas não calibradas por contexto    | OWASP SAMM / OWASP Testing Guide / DSOMM | Testes genéricos sem adaptação                       | Estratégia por risco + integração de feedback de contexto                          | `addon/00-estrategia-testes.md`, `addon/09-feedback-equipa.md` | ✅               |

---

## ✅ Conclusão

O Capítulo 10 fornece a **última linha de defesa prática antes do go-live**, sendo o único capaz de:

- Detetar vulnerabilidades ativas e exploráveis;
- Prevenir regressões e assegurar a repetibilidade de validações;
- Garantir que findings se traduzem em melhoria real da aplicação.

> ✅ Este capítulo **mitiga pelo menos 12 ameaças que não são cobertas por nenhum outro**, com foco na **detecção ativa de falhas no código, arquitetura e execução da aplicação**.

> 📌 As práticas descritas respondem diretamente a requisitos de frameworks como **SSDF**, **OWASP SAMM**, **BSIMM**, **ISO 27034**, **CAPEC**, **ENISA DevSecOps** e **DSOMM**, integrando validação ativa, feedback, gates, cobertura proporcional ao risco e rastreabilidade objetiva.
