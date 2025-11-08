---
id: aplicacao-lifecycle
title: Como Fazer
description: Integração das práticas de requisitos ao longo das fases do ciclo de desenvolvimento
tags: [tipo:aplicacao, execucao, ciclo de vida, requisitos, validação, rastreabilidade, exceções]
sidebar_position: 15
---

# 🛠️ Aplicação de Requisitos de Segurança no Ciclo de Vida

Este anexo prescreve **como aplicar sistematicamente os requisitos definidos no Capítulo 2** ao longo do ciclo de desenvolvimento, garantindo rastreabilidade, proporcionalidade ao risco e validação contínua.

Inclui modelos reutilizáveis de user stories, ações por papel, artefactos esperados e quadros de aplicação por nível de criticidade (L1–L3).

---

## 📅 Quando aplicar os requisitos de segurança

| Fase / Evento                   | Ação esperada                                                 | Artefacto principal              |
| ------------------------------- | ------------------------------------------------------------- | -------------------------------- |
| Início de projeto               | Seleção proporcional de requisitos com base na criticidade    | `matriz-controlos-por-risco.md`  |
| Grooming / Planeamento          | Transformar requisitos em cartões rastreáveis                 | Backlog (cards + tags `SEC-...`) |
| Nova funcionalidade / refactor  | Revalidar requisitos aplicáveis à alteração                   | Tarefa técnica / story revisada  |
| Integração ou exposição externa | Rever requisitos de autenticação, logging, controlo de acesso | Issue ou checklist de integração |
| Sprint review ou testes         | Verificar critérios de aceitação de segurança                 | Critérios + testes associados    |
| Preparação para go-live         | Validar requisitos aplicados, exceções aprovadas, coverage    | Checklist de release             |

---

## 👥 Quem faz o quê

| Papel / Função                        | Responsabilidades-chave                                      |
| ------------------------------------- | ------------------------------------------------------------ |
| Product Owner                         | Selecionar requisitos conforme risco e integrá-los no backlog|
| Developer                             | Implementar requisitos, aplicar tags e registar exceções      |
| QA / Test Engineer                    | Garantir critérios de aceitação, rastreabilidade e cobertura de testes |
| Arquitetura / Tech Lead / DevSecOps   | Rever requisitos em refactors, integrações e alterações críticas |
| Equipa de Segurança / AppSec          | Validar requisitos aplicados, aprovar exceções e garantir alinhamento global |

---

## 📝 User Stories e Cartões Reutilizáveis

### US-01 – Seleção de requisitos por criticidade

**Contexto.**  
A seleção inicial de requisitos deve ser proporcional ao risco da aplicação (L1–L3).

:::userstory
**História.**   
Como **Product Owner**, quero selecionar os requisitos aplicáveis ao projeto, para garantir que a segurança é proporcional ao nível de risco.

**Critérios de aceitação (BDD).**
- Dado que a aplicação tem um nível de criticidade atribuído  
- Quando consulto a matriz de requisitos adequada  
- Então marco no backlog apenas os aplicáveis ao nível definido

**Checklist.**
- [ ] Classificação de criticidade (L1–L3) atribuída  
- [ ] Matriz de aplicação usada (`SEC-Lx-...`)  
- [ ] Requisitos marcados no backlog  
- [ ] Evidência documentada no repositório do projeto

:::

**Artefactos & evidências.**
- Artefacto: `matriz-controlos-por-risco.md`  
- Evidência: backlog com tags `SEC-Lx-*`

**Proporcionalidade por risco.**
| Nível | Obrigatório? | Ajustes |
|---|---|---|
| L1 | Opcional | Catálogo reduzido |
| L2 | Sim | Catálogo completo L2 |
| L3 | Sim | Catálogo completo L3 + reforços |

**Integração no SDLC.**
| Fase | Trigger | Responsável | SLA |
|---|---|---|---|
| Início | Kick-off do projeto | Product Owner | Antes do backlog inicial |

---

### US-02 – Revisão periódica e após alterações

**Contexto.**  
A classificação e os requisitos aplicados devem ser revistos periodicamente e sempre que houver alterações significativas de exposição, dados, integrações ou arquitetura.

:::userstory
**História.**   
Como **Arquitetura / Tech Lead / DevSecOps**, quero rever a classificação e os requisitos aplicáveis sempre que uma integração crítica ou mudança relevante ocorre, para garantir que os controlos se mantêm adequados.

**Critérios de aceitação (BDD).**
- Dado que ocorre uma alteração significativa  
- Quando reviso a classificação e a matriz de requisitos  
- Então ajusto ou acrescento requisitos conforme necessário

**Checklist.**
- [ ] Mudança relevante identificada  
- [ ] Revisão de classificação realizada  
- [ ] Requisitos ajustados ou acrescentados  
- [ ] Evidência arquivada em repositório de arquitetura

:::

**Artefactos & evidências.**
- Artefacto: registo de arquitetura  
- Evidência: issue de revisão ou PR de atualização

**Proporcionalidade por risco.**
| Nível | Obrigatório? | Ajustes |
|---|---|---|
| L1 | Opcional | Apenas em alterações críticas  |
| L2 | Sim | Em todas as mudanças críticas    |
| L3 | Sim | Em qualquer alteração da arquitetura |

**Integração no SDLC.**
| Fase | Trigger | Responsável | SLA |
|---|---|---|---|
| Refactor/Design | Alteração da arquitetura ou de dados | Tech Lead | Antes da release |

**Ligações úteis.**
- 🔗 [Validação e revisão de requisitos](./addon/validacao-requisitos)

---

### US-03 – Gestão de exceções

**Contexto.**  
Nem todos os requisitos são aplicáveis; exceções devem ser formalmente documentadas, justificadas e aprovadas.

:::userstory
**História.**   
Como **Developer**, quero registar uma exceção a um requisito não aplicável, para que a decisão seja rastreável e validada.

**Critérios de aceitação (BDD).**
- Dado que identifico um requisito não aplicável  
- Quando registo uma exceção formal  
- Então o pedido é avaliado e aprovado/rejeitado pela equipa de segurança

**Checklist.**
- [ ] Justificação documentada  
- [ ] Avaliação de risco residual realizada  
- [ ] Prazo de validade definido  
- [ ] Aprovação formal pela equipa de segurança  
- [ ] Evidência anexada ao backlog

:::

**Artefactos & evidências.**
- Artefacto: `excecoes/*.md`  
- Evidência: issue ou PR com decisão

**Proporcionalidade por risco.**
| Nível | Obrigatório? | Ajustes |
|---|---|---|
| L1 | Opcional | Registo simplificado |
| L2 | Sim | Exceção formalizada |
| L3 | Sim | Exceção formal + mitigação definida |

**Integração no SDLC.**
| Fase | Trigger | Responsável | SLA |
|---|---|---|---|
| Planeamento | Identificação da exceção | Developer + AppSec | Antes da release |

**Ligações úteis.**
- 🔗 [Gestão de exceções](./addon/gestao-excecoes)

---

### US-04 – Rastreabilidade de requisitos

**Contexto.**  
Todos os requisitos aplicados devem ser rastreáveis no backlog e auditáveis.

:::userstory
**História.**   
Como **QA / Test Engineer**, quero garantir que todos os requisitos aplicados têm rastreabilidade no backlog, para suportar auditoria e verificação.

**Critérios de aceitação (BDD).**
- Dado que os requisitos estão definidos  
- Quando reviso o backlog  
- Então encontro todos com tags `SEC-Lx-*`

**Checklist.**
- [ ] Todos os cartões têm tag `SEC-Lx-Tyy-ZZZ`  
- [ ] Referência cruzada com catálogo de requisitos  
- [ ] Relatórios exportáveis  
- [ ] Evidência de rastreabilidade arquivada

:::

**Artefactos & evidências.**
- Artefacto: board de desenvolvimento  
- Evidência: relatório de rastreabilidade

**Proporcionalidade por risco.**
| Nível | Obrigatório? | Ajustes |
|---|---|---|
| L1 | Opcional | Apenas requisitos críticos |
| L2 | Sim | Requisitos completos L2 |
| L3 | Sim | Todos os requisitos L3 |

**Integração no SDLC.**
| Fase | Trigger | Responsável | SLA |
|---|---|---|---|
| Grooming | Revisão de backlog | QA | Por sprint |

**Ligações úteis.**
- 🔗 [Taxonomia de rastreabilidade](./addon/rastreabilidade-controlo)

---

### US-05 – Definição de critérios de validação

**Contexto.**  
Cada requisito selecionado deve ter critérios de aceitação e validação definidos de forma explícita, para garantir verificabilidade e testes eficazes.


:::userstory
**História.**   
Como **Product Owner/QA**, quero garantir que cada requisito selecionado no backlog contém critérios de aceitação de segurança claros, para que possam ser validados e testados de forma consistente.

**Critérios de aceitação (BDD).**
- Dado que um requisito é selecionado  
- Quando o coloco no backlog  
- Então adiciono critérios de aceitação/validação formais

**Checklist.**
- [ ] Critérios definidos no cartão  
- [ ] Alinhamento com catálogo de requisitos  
- [ ] Validação prevista em testes  
- [ ] Evidência registada

:::

**Artefactos & evidências.**
- Artefacto: backlog  
- Evidência: cartões/documentos de critérios

**Proporcionalidade por risco.**
| Nível | Obrigatório? | Ajustes |
|---|---|---|
| L1 | Opcional | Apenas para requisitos críticos |
| L2 | Sim | Para todos os requisitos selecionados |
| L3 | Sim | Para todos + validação reforçada |

**Integração no SDLC.**
| Fase | Trigger | Responsável | SLA |
|---|---|---|---|
| Planeamento | Criação de cartões | PO + QA | Antes da sprint |

**Ligações úteis.**
- 🔗 [Validação de requisitos](./addon/validacao-requisitos)

---

### US-06 – Validação de cobertura de testes

**Contexto.**  
Requisitos devem ter sempre cobertura de testes para garantir eficácia e prevenir regressões.

:::userstory
**História.**   
Como **QA / Test Engineer**, quero garantir que todos os requisitos têm validação associada, para prevenir falsos positivos ou ausência de controlo.

**Critérios de aceitação (BDD).**
- Dado que requisitos foram aplicados  
- Quando executo os testes  
- Então obtenho evidência documentada da validação

**Checklist.**
- [ ] Testes automáticos ou manuais documentados  
- [ ] Critérios de aceitação definidos  
- [ ] Evidência de execução por sprint  
- [ ] Logs arquivados em pipeline CI/CD

:::

**Artefactos & evidências.**
- Artefacto: planos de teste  
- Evidência: logs ou screenshots em pipeline

**Proporcionalidade por risco.**
| Nível | Obrigatório? | Ajustes |
|---|---|---|
| L1 | Opcional | Testes básicos |
| L2 | Sim | Testes completos |
| L3 | Sim | Testes completos + revisão independente |

**Integração no SDLC.**
| Fase | Trigger | Responsável | SLA |
|---|---|---|---|
| Sprint review | Execução de testes | QA | Por sprint |

**Ligações úteis.**
- 🔗 [Validação de requisitos](./addon/validacao-requisitos)

---

### US-07 – Validação e aprovação final

**Contexto.**  
A Equipa de Segurança deve validar requisitos aplicados e aprovar exceções, garantindo que as decisões de risco são formalmente controladas.

:::userstory
**História.**   
Como **Equipa de Segurança / AppSec**, quero validar a aplicação dos requisitos e aprovar eventuais exceções, para garantir que as decisões de risco estão formalmente controladas e documentadas.

**Critérios de aceitação (BDD).**
- Dado que os requisitos foram aplicados  
- Quando reviso backlog e exceções  
- Então aprovo ou rejeito com base no risco

**Checklist.**
- [ ] Verificação de requisitos aplicados  
- [ ] Aprovação/rejeição de exceções registadas  
- [ ] Evidência de decisão documentada  
- [ ] Feedback registado no board de projeto

:::

**Artefactos & evidências.**
- Artefacto: ficheiro de exceções  
- Evidência: decisão registada em PR ou issue

**Proporcionalidade por risco.**
| Nível | Obrigatório? | Ajustes |
|---|---|---|
| L1 | Opcional | Revisão simplificada |
| L2 | Sim | Revisão formal |
| L3 | Sim | Revisão formal + mitigação exigida |

**Integração no SDLC.**
| Fase | Trigger | Responsável | SLA |
|---|---|---|---|
| Release | Aprovação final | AppSec | Antes do go-live |

**Ligações úteis.**
- 🔗 [Gestão de exceções](./addon/gestao-excecoes)

---

### US-08 – Catálogo de requisitos do projeto (criação e manutenção)

**Contexto.**  
No arranque do projeto e sempre que existam alterações de âmbito, deve existir um **catálogo versionado de requisitos (REQ-XXX)**, derivado da baseline organizacional e filtrado pela criticidade.

:::userstory
**História.**  
Como **AppSec/PO/TL**, quero estabelecer e manter um catálogo de requisitos de segurança do projeto (REQ-XXX), para assegurar aplicação consistente, versionada e auditável ao longo do SDLC.

**Critérios de aceitação (BDD).**
- Dado que a aplicação tem criticidade L1–L3 definida  
- Quando gero o catálogo a partir da baseline e filtro por nível  
- Então o catálogo fica versionado, com owner definido e ligação a critérios de validação

**Checklist.**
- [ ] Catálogo `REQ-XXX` criado/atualizado e versionado  
- [ ] Owner e periodicidade de revisão definidos  
- [ ] Mapeamento para critérios de validação e tags de backlog  
- [ ] Localização e link persistentes no repositório

:::

**Artefactos & evidências.**
- Artefacto: `catalogo-requisitos.md` (ou pasta `catalogo/`) + CHANGELOG do catálogo  
- Evidência: MR/PR de criação/atualização e aprovação por AppSec

**Proporcionalidade por risco.**
| Nível | Obrigatório? | Ajustes |
|---|---|---|
| L1 | Sim | Subconjunto essencial pré-aprovado |
| L2 | Sim | Catálogo completo L2 |
| L3 | Sim | Catálogo L3 + reforços (p.ex., supply-chain, hardening) |

**Integração no SDLC.**
| Fase | Trigger | Responsável | SLA |
|---|---|---|---|
| Início | Kick-off / nova release major | AppSec + PO + TL | Antes do backlog inicial / antes da release |

**Ligações úteis.**
- 🔗 [Catálogo de requisitos](./addon/catalogo-requisitos)  
- 🔗 [Critérios de aceitação](./addon/criterios-aceitacao)

---

### US-09 – Validação por requisito/domínio (REQ-XXX → evidência)

**Contexto.**  
Cada requisito ativo **deve** ter uma forma de validação associada (teste, revisão, scanner, evidência manual), com **resultado e prova** ligados ao requisito.

:::userstory
**História.**  
Como **QA/AppSec/TL**, quero validar cada requisito REQ-XXX segundo os critérios definidos, para assegurar que existe evidência objetiva e rastreável do seu cumprimento.

**Critérios de aceitação (BDD).**
- Dado um requisito REQ-XXX com critérios definidos  
- Quando executo a validação associada (teste/revisão/scan)  
- Então registo o resultado “pass/fail” e anexo a evidência ao requisito

**Checklist.**
- [ ] Método de validação definido por requisito  
- [ ] Execução registada por sprint/release  
- [ ] Resultado e evidência ligados ao REQ-XXX  
- [ ] Revisão e aprovação por AppSec quando aplicável

:::

**Artefactos & evidências.**
- Artefacto: plano de validação por requisito (p.ex., `validacoes/REQ-XXX.md`)  
- Evidência: logs de CI/CD, relatórios (SAST/DAST/IAST), reviews, screenshots

**Proporcionalidade por risco.**
| Nível | Obrigatório? | Ajustes |
|---|---|---|
| L1 | Sim | Amostragem mínima de requisitos críticos |
| L2 | Sim | Cobertura integral dos requisitos selecionados |
| L3 | Sim | Cobertura integral + revisão independente e gates automáticos |

**Integração no SDLC.**
| Fase | Trigger | Responsável | SLA |
|---|---|---|---|
| Testes/Code Review | Execução de pipelines ou checkpoints de qualidade | QA + AppSec + TL | Por sprint e antes de release |

**Ligações úteis.**
- 🔗 [Validação de requisitos](./addon/validacao-requisitos)  
- 🔗 [Controlos por requisito](./addon/controlos-requisitos)

---

## ⚖️ Aplicação proporcional por nível de risco (L1–L2–L3)

| Prática                    | L1 (baixo risco)          | L2 (médio risco)                     | L3 (alto risco)                                  |
| -------------------------- | ------------------------- | ------------------------------------ | ------------------------------------------------ |
| Catálogo de requisitos     | Básico (10–15 requisitos) | Catálogo completo L2                 | Catálogo completo L3 + reforços adicionais       |
| Rastreabilidade (tags)     | Opcional                  | Obrigatória nos cartões de segurança | Todos os cartões técnicos e funcionais           |
| Exceções                   | Ad hoc                    | Documentadas e aprovadas             | Formalizadas com prazo e mitigação               |
| Validação de requisitos    | Revisão manual            | Testes associados                    | Testes + cobertura + revisão independente        |
| Reavaliação por alterações | Parcial / a pedido        | A cada funcionalidade crítica        | Sempre que há mudança de controlo ou arquitetura |

---

## 📄 Templates e artefactos esperados

| Artefacto                       | Formato sugerido           | Onde guardar / referenciar           |
| ------------------------------- | -------------------------- | ------------------------------------ |
| Matriz de requisitos por risco  | Markdown / tabela          | Diretório `docs/` ou Wiki de produto |
| Cartões com tags `SEC-*`        | Board / GitHub / Jira      | Backlog de equipa                    |
| Justificação de exceções        | Markdown / issue template  | Diretório `excecoes/` ou board       |
| Relatórios de rastreabilidade   | Export de board / CSV      | Arquivo de auditoria                 |
| Planos de teste e evidências    | YAML / Markdown / CI logs  | Repositório QA ou CI/CD              |
