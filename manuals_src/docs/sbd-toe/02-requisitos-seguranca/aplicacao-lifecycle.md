---
id: aplicacao-lifecycle
title: Aplicação de Requisitos de Segurança no Ciclo de Vida
description: Integração das práticas de requisitos ao longo das fases do ciclo de desenvolvimento
tags: [tipo:aplicacao, execucao, ciclo de vida, requisitos, validação, rastreabilidade, exceções]
sidebar_position: 15
---

<!--template: sbdtoe-usage -->

# 🛠️ Aplicação de Requisitos de Segurança no Ciclo de Vida {requisitos-seguranca:aplicacao-lifecycle}

Este anexo prescreve **como aplicar sistematicamente os requisitos definidos no Capítulo 2** ao longo do ciclo de desenvolvimento, garantindo rastreabilidade, proporcionalidade ao risco e validação contínua.

Inclui modelos reutilizáveis de user stories, ações por papel, artefactos esperados e quadros de aplicação por nível de criticidade (L1–L3).

---

## 📅 Quando aplicar os requisitos de segurança {requisitos-seguranca:aplicacao-lifecycle#quando_aplicar_os_requisitos_de_seguranca}

| Fase / Evento                   | Ação esperada                                                 | Artefacto principal              |
| ------------------------------- | ------------------------------------------------------------- | -------------------------------- |
| Início de projeto               | Seleção proporcional de requisitos com base na criticidade    | `matriz-controlos-por-risco.md`  |
| Grooming / Planeamento          | Transformar requisitos em cartões rastreáveis                 | Backlog (cards + tags `SEC-...`) |
| Nova funcionalidade / refactor  | Revalidar requisitos aplicáveis à alteração                   | Tarefa técnica / story revisada  |
| Integração ou exposição externa | Rever requisitos de autenticação, logging, controlo de acesso | Issue ou checklist de integração |
| Sprint review ou testes         | Verificar critérios de aceitação de segurança                 | Critérios + testes associados    |
| Preparação para go-live         | Validar requisitos aplicados, exceções aprovadas, coverage    | Checklist de release             |

---

## 👥 Quem faz o quê {requisitos-seguranca:aplicacao-lifecycle#quem_faz_o_que}

| Papel / Função                        | Responsabilidades-chave                                      |
| ------------------------------------- | ------------------------------------------------------------ |
| Product Owner                         | Selecionar requisitos conforme risco e integrá-los no backlog|
| Developer                             | Implementar requisitos, aplicar tags e registar exceções      |
| QA / Test Engineer                    | Garantir critérios de aceitação, rastreabilidade e cobertura de testes |
| Arquitetura / Tech Lead / DevSecOps   | Rever requisitos em refactors, integrações e alterações críticas |
| Equipa de Segurança / AppSec          | Validar requisitos aplicados, aprovar exceções e garantir alinhamento global |

---

## 📝 User Stories e Cartões Reutilizáveis {requisitos-seguranca:aplicacao-lifecycle#user_stories_e_cartoes_reutilizaveis}

### US-01 – Seleção de requisitos por criticidade {#us-01}

**Contexto.**  
A seleção inicial de requisitos deve ser proporcional ao risco da aplicação (L1–L3).

**📖 Rationale científico.**  
Alinhado com **OWASP SAMM Governance/Strategy & Metrics**, **BSIMM SR1.1**, **NIST SSDF RM.1** e **ISO/IEC 27005** (gestão de risco).  
Mitiga riscos de desajuste entre controlos e risco real, reduzindo **CWE-693 (Protection Mechanism Failure)**, **CWE-1039 (Automated Discovery—Incorrect Assumptions)** e lacunas de **OSC&R – Requirements Coverage Gaps**.  
Valor empírico: o **Verizon DBIR** e estudos **BSIMM** mostram que uma seleção proporcional reduz custos de implementação e diminui “janela de exposição” para classes de falhas recorrentes (p.ex., **OWASP Top 10**), mantendo a eficácia operacional.

**História.**  
Como **Product Owner**, quero selecionar os requisitos aplicáveis ao projeto, para garantir que a segurança é proporcional ao nível de risco.

**Critérios de aceitação (BDD).**
- Dado que a aplicação tem um nível de criticidade atribuído  
- Quando consulto a matriz de requisitos adequada  
- Então marco no backlog apenas os aplicáveis ao nível definido

**Checklist (binária, auditável).**
- [ ] Classificação de criticidade (L1–L3) atribuída  
- [ ] Matriz de aplicação usada (`SEC-Lx-...`)  
- [ ] Requisitos marcados no backlog  
- [ ] Evidência documentada no repositório do projeto

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
| Fase | Gatilho | Responsável | SLA |
|---|---|---|---|
| Início | Kick-off do projeto | Product Owner | Antes do backlog inicial |

**Ligações úteis.**
- 🔗 [Matriz de controlos por risco](xref:sbd-toe:toe:01-classificacao-aplicacoes:matriz-controlos-por-risco)

---

### US-02 – Revisão periódica e após alterações {#us-02}

**Contexto.**  
A classificação e os requisitos aplicados devem ser revistos periodicamente e sempre que houver alterações significativas de exposição, dados, integrações ou arquitetura.

**📖 Rationale científico.**  
Baseado em **SSDF PS.3** (Review and Update Security Requirements), **SAMM Design/Threat Assessment**, **BSIMM AM2.4** (análise de arquitetura) e práticas de cadeia de fornecimento **SLSA** (gestão de mudanças).  
Mitiga riscos de **OSC&R – Surface Expansion**, **CWE-16 (Configuration Issues)** e **CWE-710 (Improper Adherence to Coding Standards)**, frequentes após mudanças.  
Valor empírico: o **NIST SP 800-160** e o **DBIR** correlacionam incidentes críticos a mudanças não acompanhadas por reavaliação proporcional de controlos.

**História.**  
Como **Arquitetura / Tech Lead / DevSecOps**, quero rever a classificação e os requisitos aplicáveis sempre que uma integração crítica ou mudança relevante ocorre, para garantir que os controlos se mantêm adequados.

**Critérios de aceitação (BDD).**
- Dado que ocorre uma alteração significativa  
- Quando reviso a classificação e a matriz de requisitos  
- Então ajusto ou acrescento requisitos conforme necessário

**Checklist (binária, auditável).**
- [ ] Mudança relevante identificada  
- [ ] Revisão de classificação realizada  
- [ ] Requisitos ajustados ou acrescentados  
- [ ] Evidência arquivada em repositório de arquitetura

**Artefactos & evidências.**
- Artefacto: registo de arquitetura  
- Evidência: issue de revisão ou PR de atualização

**Proporcionalidade por risco.**
| Nível | Obrigatório? | Ajustes |
|---|---|---|
| L1 | Opcional | Apenas em alterações críticas  |
| L2 | Sim | Em todas as mudanças críticas    |
| L3 | Sim | Em qualquer alteração arquitetural |

**Integração no SDLC.**
| Fase | Gatilho | Responsável | SLA |
|---|---|---|---|
| Refactor/Design | Alteração arquitetural ou de dados | Tech Lead | Antes da release |

**Ligações úteis.**
- 🔗 [Validação e revisão de requisitos](xref:sbd-toe:toe:02-requisitos-seguranca:validacao-requisitos)

---

### US-03 – Gestão de exceções {#us-03}

**Contexto.**  
Nem todos os requisitos são aplicáveis; exceções devem ser formalmente documentadas, justificadas e aprovadas.

**📖 Rationale científico.**  
Processo descrito em **OWASP SAMM Governance/Policy & Compliance**, **BSIMM CP1.2** (documentação de riscos e exceções), **NIST SSDF RV.1** e **ISO/IEC 27005** (tratamento do risco residual).  
Mitiga riscos de **CWE-285 (Improper Authorization)**, **CWE-732 (Incorrect Permission Assignment)** e **CAPEC-220 (Disabling Security Controls)**, prevenindo bypass indevido de controlos.  
Valor empírico: **ENISA Threat Landscape** e **DBIR** mostram que exceções ad hoc aumentam dívida de risco e dificultam auditoria.

**História.**  
Como **Developer**, quero registar uma exceção a um requisito não aplicável, para que a decisão seja rastreável e validada.

**Critérios de aceitação (BDD).**
- Dado que identifico um requisito não aplicável  
- Quando registo uma exceção formal  
- Então o pedido é avaliado e aprovado/rejeitado pela equipa de segurança

**Checklist (binária, auditável).**
- [ ] Justificação documentada  
- [ ] Avaliação de risco residual realizada  
- [ ] Prazo de validade definido  
- [ ] Aprovação formal pela equipa de segurança  
- [ ] Evidência anexada ao backlog

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
| Fase | Gatilho | Responsável | SLA |
|---|---|---|---|
| Planeamento | Identificação da exceção | Developer + AppSec | Antes da release |

**Ligações úteis.**
- 🔗 [Gestão de exceções](xref:sbd-toe:toe:02-requisitos-seguranca:gestao-excecoes)

---

### US-04 – Rastreabilidade de requisitos {#us-04}

**Contexto.**  
Todos os requisitos aplicados devem ser rastreáveis no backlog e auditáveis.

**📖 Rationale científico.**  
Prescrito por **NIST SSDF RV.2** (document and maintain traceability), **OWASP SAMM Design/Threat Assessment** e **BSIMM SR1.5** (ligar requisitos à implementação), com reforço de **DSOMM** (governance & metrics) e **SLSA** (proveniência).  
Mitiga **CWE-1079 (Inconsistent Tagging)** e lacunas de **OSC&R – Requirements Coverage Gaps**, permitindo auditoria e accountability (ver **ISO/IEC 27034**).  
Valor empírico: dados **BSIMM** indicam que equipas com rastreabilidade fraca têm tempo médio de correção 3× superior e maior taxa de regressões.

**História.**  
Como **QA / Test Engineer**, quero garantir que todos os requisitos aplicados têm rastreabilidade no backlog, para suportar auditoria e verificação.

**Critérios de aceitação (BDD).**
- Dado que os requisitos estão definidos  
- Quando reviso o backlog  
- Então encontro todos com tags `SEC-Lx-*`

**Checklist (binária, auditável).**
- [ ] Todos os cartões têm tag `SEC-Lx-Tyy-ZZZ`  
- [ ] Referência cruzada com catálogo de requisitos  
- [ ] Relatórios exportáveis  
- [ ] Evidência de rastreabilidade arquivada

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
| Fase | Gatilho | Responsável | SLA |
|---|---|---|---|
| Grooming | Revisão de backlog | QA | Por sprint |

**Ligações úteis.**
- 🔗 [Taxonomia de rastreabilidade](xref:sbd-toe:toe:01-classificacao-aplicacoes:rastreabilidade)

---

### US-05 – Definição de critérios de validação {#us-05}

**Contexto.**  
Cada requisito selecionado deve ter critérios de aceitação e validação definidos de forma explícita, para garantir verificabilidade e testes eficazes.

**📖 Rationale científico.**  
Recomendado por **NIST SSDF RV.3** (define and verify acceptance criteria), **OWASP SAMM Verification/Testing**, **BSIMM PT3.1** e **ISO/IEC 25010** (qualidade).  
Mitiga **CWE-20 (Improper Input Validation)**, **CWE-693 (Protection Mechanism Failure)** e padrões **CAPEC-112 (Brute Force Input)**, além de reduzir ambiguidades de teste que levam a falsos negativos.  
Valor empírico: estudos **BSIMM** e o **DBIR** indicam que critérios de validação claros reduzem defeitos escapados para produção em ~30–40% e aceleram a triagem.

**História.**  
Como **Product Owner/QA**, quero garantir que cada requisito selecionado no backlog contém critérios de aceitação de segurança claros, para que possam ser validados e testados de forma consistente.

**Critérios de aceitação (BDD).**
- Dado que um requisito é selecionado  
- Quando o coloco no backlog  
- Então adiciono critérios de aceitação/validação formais

**Checklist (binária, auditável).**
- [ ] Critérios definidos no cartão  
- [ ] Alinhamento com catálogo de requisitos  
- [ ] Validação prevista em testes  
- [ ] Evidência registada

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
| Fase | Gatilho | Responsável | SLA |
|---|---|---|---|
| Planeamento | Criação de cartões | PO + QA | Antes da sprint |

**Ligações úteis.**
- 🔗 [Validação de requisitos](xref:sbd-toe:toe:02-requisitos-seguranca:validacao-requisitos)

---

### US-06 – Validação de cobertura de testes {#us-06}

**Contexto.**  
Requisitos devem ter sempre cobertura de testes para garantir eficácia e prevenir regressões.

**📖 Rationale científico.**  
Prática prevista por **NIST SSDF RV.3**, **OWASP SAMM Verification/Testing**, **BSIMM PT3.x** e **DSOMM** (continuidade de validação).  
Mitiga falhas de **CWE-693 (Protection Mechanism Failure)** e deteta padrões **CAPEC-112**, **CAPEC-66 (SQL Injection)** e **CAPEC-242 (Code Injection)** quando os requisitos mapeiam para controles do **OWASP Top 10**.  
Valor empírico: **BSIMM** associa maior cobertura a menor taxa de incidentes em produção; o **DBIR** destaca que ausência de testes sistemáticos aumenta dwell time e impacto.

**História.**  
Como **QA / Test Engineer**, quero garantir que todos os requisitos têm validação associada, para prevenir falsos positivos ou ausência de controlo.

**Critérios de aceitação (BDD).**
- Dado que requisitos foram aplicados  
- Quando executo os testes  
- Então obtenho evidência documentada da validação

**Checklist (binária, auditável).**
- [ ] Testes automáticos ou manuais documentados  
- [ ] Critérios de aceitação definidos  
- [ ] Evidência de execução por sprint  
- [ ] Logs arquivados em pipeline CI/CD

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
| Fase | Gatilho | Responsável | SLA |
|---|---|---|---|
| Sprint review | Execução de testes | QA | Por sprint |

**Ligações úteis.**
- 🔗 [Validação de requisitos](xref:sbd-toe:toe:02-requisitos-seguranca:validacao-requisitos)

---

### US-07 – Validação e aprovação final {#us-07}

**Contexto.**  
A Equipa de Segurança deve validar requisitos aplicados e aprovar exceções, garantindo que as decisões de risco são formalmente controladas.

**📖 Rationale científico.**  
Alinhado com **OWASP SAMM Governance/Policy & Compliance**, **BSIMM CR3.2** (auditoria de controlos), **NIST SSDF RV.4** (formal approval of residual risk) e **ISO/IEC 27005** (aceitação de risco).  
Mitiga riscos de **CWE-1191 (Improper Restriction of Control Operations)**, abuso de privilégios **CAPEC-233** e decisões não documentadas que fragilizam accountability.  
Valor empírico: revisões independentes (dados **ENISA** e **DBIR**) reduzem falhas não detetadas e reforçam conformidade.

**História.**  
Como **Equipa de Segurança / AppSec**, quero validar a aplicação dos requisitos e aprovar eventuais exceções, para garantir que as decisões de risco estão formalmente controladas e documentadas.

**Critérios de aceitação (BDD).**
- Dado que os requisitos foram aplicados  
- Quando reviso backlog e exceções  
- Então aprovo ou rejeito com base no risco

**Checklist (binária, auditável).**
- [ ] Verificação de requisitos aplicados  
- [ ] Aprovação/rejeição de exceções registadas  
- [ ] Evidência de decisão documentada  
- [ ] Feedback registado no board de projeto

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
| Fase | Gatilho | Responsável | SLA |
|---|---|---|---|
| Release | Aprovação final | AppSec | Antes do go-live |

**Ligações úteis.**
- 🔗 [Gestão de exceções](xref:sbd-toe:toe:02-requisitos-seguranca:gestao-excecoes)

---

## ⚖️ Aplicação proporcional por nível de risco (L1–L2–L3) {requisitos-seguranca:aplicacao-lifecycle#aplicacao_proporcional_por_nivel_de_risco_l1l2l3}

| Prática                    | L1 (baixo risco)          | L2 (médio risco)                     | L3 (alto risco)                                  |
| -------------------------- | ------------------------- | ------------------------------------ | ------------------------------------------------ |
| Catálogo de requisitos     | Básico (10–15 requisitos) | Catálogo completo L2                 | Catálogo completo L3 + reforços adicionais       |
| Rastreabilidade (tags)     | Opcional                  | Obrigatória nos cartões de segurança | Todos os cartões técnicos e funcionais           |
| Exceções                   | Ad hoc                    | Documentadas e aprovadas             | Formalizadas com prazo e mitigação               |
| Validação de requisitos    | Revisão manual            | Testes associados                    | Testes + cobertura + revisão independente        |
| Reavaliação por alterações | Parcial / a pedido        | A cada funcionalidade crítica        | Sempre que há mudança de controlo ou arquitetura |

---

## 📄 Templates e artefactos esperados {requisitos-seguranca:aplicacao-lifecycle#templates_e_artefactos_esperados}

| Artefacto                       | Formato sugerido           | Onde guardar / referenciar           |
| ------------------------------- | -------------------------- | ------------------------------------ |
| Matriz de requisitos por risco  | Markdown / tabela          | Diretório `docs/` ou Wiki de produto |
| Cartões com tags `SEC-*`        | Board / GitHub / Jira      | Backlog de equipa                    |
| Justificação de exceções        | Markdown / issue template  | Diretório `excecoes/` ou board       |
| Relatórios de rastreabilidade   | Export de board / CSV      | Arquivo de auditoria                 |
| Planos de teste e evidências    | YAML / Markdown / CI logs  | Repositório QA ou CI/CD              |
