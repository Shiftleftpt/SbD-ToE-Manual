---
description: Listagem de conteúdos formativos mínimos por perfil técnico para onboarding
  e capacitação contínua.
id: catalogo-formativo
tags:
- catalogo
- conteudos
- formacao
- manual
- onboarding
- perfis
- por capitulo
title: Catálogo de Formação por Perfil Técnico
---



# 🗺️ Catálogo de Conteúdos Formativos SbD-ToE

## 🌟 Objetivo

Cruzar os **14 capítulos técnicos do manual SbD-ToE** com os **conteúdos de formação essenciais**, de forma a orientar:

- A criação de **trilhos formativos** por função e criticidade;
- A atribuição proporcional de conteúdos a **níveis de risco (L1–L3)**;
- A escolha de **formatos pedagógicos adequados** por perfil e contexto.

Este catálogo serve de base para programas de formação, onboarding, labs e CTFs internos - e pode ser instanciado como estrutura curricular num LMS.

---

## 🧬 O que contém

A matriz define, por capítulo técnico do manual:

- Os **tópicos a ensinar**
- O **público-alvo** (funções)
- O **nível de risco mínimo** aplicável
- O **formato de aprendizagem sugerido**

> 📌 Serve como referência para trilhos, formação por contexto (ex: incidente), e como base para o manual expandido de formação.

---

## 📋 Estrutura da Tabela

| Capítulo | Tópico a ensinar                   | Público-alvo       | Nível de risco | Formato sugerido                         |
|----------|------------------------------------|---------------------|----------------|------------------------------------------|

---

## 📘 Mapa por Capítulo

| Capítulo | Tópico a ensinar                              | Público-alvo       | Nível | Formato sugerido                    |
|----------|-----------------------------------------------|---------------------|--------|-------------------------------------|
| 1. Gestão de Risco         | Classificação de aplicações             | PO, Dev, QA         | Médio  | Exercício prático + template       |
|                            | Avaliação de risco técnico              | PO, AppSec          | Elevado| Workshop + simulação               |
| 2. Requisitos de Segurança | Especificação segura de user stories   | PO, QA              | Médio  | Lab + revisão cruzada              |
|                            | Uso de catálogo interno de requisitos  | Dev, PO             | Médio  | Quiz + aplicação prática           |
| 3. Threat Modeling         | Modelação por funcionalidade real      | Dev, QA, PO         | Médio  | Sessão prática + rotação de lead   |
|                            | Uso de checklists em design            | QA, AppSec          | Baixo  | Template + explicação peer-led     |
| 4. Arquitetura Segura      | Padrões e antipadrões de arquitetura    | Dev, Tech Leads      | Elevado| Oficina comparativa + pairing      |
| 5. Controlo de Dependências| SBOM, lockfiles e controlo de SCA      | Dev, DevOps         | Médio  | PR clinic + lab com scanner        |
|                            | Triagem de alertas                     | AppSec, Dev          | Elevado| Revisão rotativa + lab interno     |
| 6. Desenvolvimento Seguro  | PR seguro e validação de código        | Dev, QA             | Médio  | Revisão pública + guia comentado   |
|                            | Common mistakes / top 5 falhas         | Dev                 | Baixo  | Quiz + exemplo de PR real          |
| 7. CI/CD Seguro            | Pipelines com scanners                 | DevOps              | Médio  | Oficina prática + checklist        |
|                            | âmbitos de permissões em tokens        | DevOps              | Elevado| Lab + simulação de abuso           |
| 8. IaC Seguro              | Uso de scanners (ex: TFSec)            | DevOps, CloudEng    | Médio  | Lab com Terraform inseguro         |
|                            | Boas práticas em pipelines IaC         | DevOps              | Médio  | PR review + clinic                 |
| 9. *containers* & Imagens   | Dockerfiles seguros                    | Dev, DevOps         | Médio  | Lab + análise de imagem real       |
|                            | Imagens base e hardening               | DevOps              | Elevado| Checklist de validação + pairing   |
| 10. Testes de Segurança    | Uso de DAST em staging                 | QA, Testers         | Médio  | Lab hands-on + template de bug     |
|                            | Introdução ao fuzzing                  | QA, AppSec          | Elevado| Demo + exercício dirigido          |
| 11. Deploy Seguro          | Configuração segura e rollback         | DevOps              | Médio  | Simulação + pós-mortem educativo   |
| 12. Monitorização          | Alertas relevantes e falsos positivos | DevOps, QA          | Médio  | Jogo de deteção + dashboard        |
| 13. Formação & Onboarding  | Labs rotativos, PR clinics, CTF        | Todos               | Todos  | Sessões regulares + rotação        |
| 14. Governança & Contratação | Cláusulas de segurança em contratos | Gestão, Procurement | Elevado| Estudo de caso + checklist legal   |

---

## 🛠️ Como aplicar

- Instanciar como matriz de referência em:
  - Programas de onboarding por função
  - Estrutura curricular num LMS
  - Planos anuais de capacitação
- Relacionar com:
  - Checklists de entrada (ex: `10-checklist-onboarding.md`)
  - Políticas de contratação de terceiros (ex: `21-plano-formacao-terceiros.md`)
  - Métricas e indicadores (ex: `90-indicadores-metricas.md`)

---

## ✅ Boas práticas

- Rever anualmente os tópicos por capítulo e função
- Usar a matriz como base para criação de labs e workshops internos
- Validar aprendizagem com quizzes, clinics ou simulações realistas
- Usar na formação derivada de incidentes reais

---

## 📎 Referências cruzadas

| Documento                           | Relação                                     |
|-------------------------------------|---------------------------------------------|
| `02-trilho-formativo.md`            | Define a aplicação da matriz por risco      |
| `03-programa-champions.md`          | Suporte à disseminação                      |
| `10-checklist-onboarding.md`        | Verificação do conteúdo aprendido           |
| `20-modelo-inclusao-terceiros.md`   | Aplicação adaptada a fornecedores externos  |
| `90-indicadores-metricas.md`        | Medição da adoção e eficácia da formação    |

---

> 📚 Este catálogo pode evoluir para o **Volume II - Manual de Formação SbD-ToE**, com conteúdos, exercícios e labs por capítulo, função e nível de risco.
