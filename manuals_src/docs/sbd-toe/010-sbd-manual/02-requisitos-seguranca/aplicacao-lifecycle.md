---
id: aplicacao-lifecycle
title: Como Fazer
description: Integração das práticas de requisitos ao longo das fases do ciclo de desenvolvimento
tags: [tipo:aplicacao, ciclo-vida, requisitos, validacao, rastreabilidade, excecoes]
genia: us-format-normalization
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

### US-02 – Revisão por alteração relevante

**Contexto.**  
A classificação e os requisitos aplicados devem ser revistos sempre que ocorra uma integração crítica, mudança de exposição, dados ou arquitetura que possa alterar o perfil de risco.

:::userstory
**História.**   
Como **Arquitetos de Software** e **Team Lead / Scrum Master**, quero rever a classificação e os requisitos sempre que ocorra uma integração crítica ou mudança relevante, para garantir que os controlos e REQ-XXX aplicáveis são atualizados e rastreados.

**Critérios de aceitação (BDD).**
- Dado que ocorre uma alteração significativa (integração externa, mudança de dados/escalabilidade, exposição)
- Quando os **Arquitetos de Software** analisam o impacto técnico
- Então atualizam a matriz de requisitos (mapeando REQ-XXX), disparam nova análise de ameaças se aplicável, e criam/atualizam tarefas no backlog com tags `SEC-Lx-*`

**DoD.**
- [ ] Matriz de requisitos atualizada com REQ-XXX vinculados
- [ ] Se alteração afecta risco: disparo de novo Threat Modeling registado
- [ ] Cartões no backlog marcados com `SEC-Lx-*` e owner definido (Developer / Team Lead)
- [ ] Evidência: PR/issue com link para `REQ-XXX` e `RSK-XXX`
- [ ] Notificação a **AppSec Engineer** para validação (em L2/L3)

:::

**Artefactos & evidências.**
- `matriz-controlos-por-risco.md` atualizado, PR/issue, wiki de arquitetura, log de notificação para AppSec Engineer

**Proporcionalidade.**
- L1: revisão ad-hoc; L2: revisão obrigatória; L3: revisão obrigatória + validação AppSec Engineer

**Integração no SDLC.**
| Fase | Trigger | Responsável | SLA |
|---|---|---|---|
| Refactor/Design | Alteração da arquitetura ou de dados | Arquitetos de Software + Team Lead | Antes da release |

**Ligações úteis.**
- 🔗 [Validação e revisão de requisitos](./addon/validacao-requisitos)

---

### US-03 – Gestão de Exceções com TTL e Revalidação Obrigatória

**Contexto.**  
Nem todos os requisitos são aplicáveis; exceções devem ser formalmente documentadas, justificadas, aprovadas e sujeitas a revalidação periódica para evitar excepções permanentes.

:::userstory
**História.**   
Como **Developer** (proponente) e **GRC/Compliance** (regista), quero registar exceções com TTL e fluxo de aprovação por **AppSec Engineer** (técnica) e **Gestão Executiva/CISO** (para L3), para garantir que todas as excepções são temporais, rastreáveis e sujeitas a revalidação.

**BDD.**
- Dado que um requisito não pode ser aplicado
- Quando a equipa regista uma excepção (ID único) com justificação e TTL (ex: 6m / 3m)
- Então a excepção fica com owner definido, alerta automático configurado 15 dias antes da expiração, e fluxo de re-aprovação exigido para renovação

**DoD.**
- [ ] Excepção com ID e ligação ao `SEC-Lx-...` registada em ferramenta (Jira/GRC)
- [ ] TTL definido consoante nível (L1=12m rec.; L2=6m; L3=3m)
- [ ] Owner designado (Developer / Team Lead) e receptor de alertas (GRC/Compliance)
- [ ] Aprovação técnica por **AppSec Engineer** documentada; **Gestão Executiva/CISO** aprova renovações L3
- [ ] Alertas automáticos configurados 15 dias antes de expiração
- [ ] Evidência de revalidação ou encerramento anexada

:::

**Artefactos & evidências.**
- `excecoes/EXC-YYYY-N.md` ou ticket em GRC; logs de alerta; histórico de decisões com approver

> **Referência:** Este US implementa [Cap 14-US-01: Processo formal de exceções]
> no contexto de requisitos de segurança. TTL, alçadas de aprovação e revalidação devem seguir a política master de exceções definida em Cap 14.

**Proporcionalidade.**
- L1: processo simplificado; L2: formalização obrigatória; L3: formal + mitigação requisitada

**Integração no SDLC.**
| Fase | Trigger | Responsável | SLA |
|---|---|---|---|
| Planeamento | Identificação da excepção | Developer + AppSec + GRC/Compliance | Antes da release |

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

### US-10 – Gates automáticos em CI/CD para requisitos de segurança

**Contexto.**
As pipelines devem impor verificações automáticas que assegurem que requisitos seleccionados (REQ-XXX) são validados antes de merge/release.

:::userstory
**História.**
Como **DevOps/SRE** e **Developer**, quero que o pipeline CI/CD verifique automaticamente SAST, SCA, DAST (quando aplicável), presença de SBOM e assinatura de artefactos, para que merges e releases só ocorram quando os requisitos de segurança forem satisfeitos.

**BDD.**
- Dado um Pull Request/MR para a branch principal
- Quando o pipeline executa os jobs de segurança (SAST, SCA, policy-check, sbom-gen, sign-artifact)
- Então o merge é bloqueado se qualquer job crítico falhar; logs e relatórios são anexados ao PR

**DoD.**
- [ ] Job SAST executado com baseline de severidade e limiares configurados
- [ ] SCA executado; dependências com CVSS > configurable_fail_threshold falham a build ou geram issue bloqueante
- [ ] DAST executado em ambiente de staging para alterações que mexem na superfície de rede/exposição (L2/L3)
- [ ] Job `sbom-gen` produz CycloneDX ou SPDX e anexa ao artefacto gerado
- [ ] Artefacto assinado (detached signature) e assinatura armazenada em registry/provenance store
- [ ] Job `policy-check` valida tags `SEC-Lx-*` e a existência de REQ-XXX linkados no PR description
- [ ] Gate report sumarizado e ligado ao PR/issue

:::

**Artefactos & evidências.**
- Logs de CI, relatórios SAST/SCA/DAST, ficheiro SBOM (`sbom.cdx.json`), assinatura (`artifact.sig`), relatório de gate

**Proporcionalidade por risco.**
| Nível | Obrigatório? | Ajustes |
|---|---|---|
| L1 | Recomendado | SAST básico, SCA recomendado |
| L2 | Sim | SAST + SCA obrigatório; gates com limiares configurados |
| L3 | Sim | SAST + SCA + DAST; gates rigorosos; SBOM + assinatura obrigatória |

**Integração no SDLC.**
| Fase | Trigger | Responsável | SLA |
|---|---|---|---|
| Merge/Release | PR/MR targeting main/release | DevOps/SRE + AppSec | Bloqueio automático até resolução |

**Ligações úteis.**
- 🔗 [Gates de segurança em CI/CD](/sbd-toe/sbd-manual/cicd-seguro/addon/gates-seguranca)  
- 🔗 [SBOM e proveniência](/sbd-toe/sbd-manual/dependencias-sbom-sca/intro)

---

### US-11 – Geração de SBOM e assinatura de artefactos de build

**Contexto.**
SBOMs e assinaturas provam a proveniência dos artefactos e são necessárias para auditoria e para gates de cadeia de fornecimento.

:::userstory
**História.**
Como **Developer** e **DevOps/SRE**, quero que a pipeline gere um SBOM (CycloneDX/SPDX) e assine o artefacto final (imagem/container/package), para que possamos verificar origem, dependências e integridade no deployment.

**BDD.**
- Dado que é construído um artefacto de release (container/image/package)
- Quando o job de build termina com sucesso
- Então é gerado um SBOM e o artefacto é assinado; ambos ficam armazenados no repositório/registo de artefactos com metadados de proveniência

**DoD.**
- [ ] SBOM gerado em formato CycloneDX (JSON) ou SPDX e anexo ao build
- [ ] Artefacto assinado com chave do projecto/organization (cosign/Notary/PKI) e assinatura armazenada no registo
- [ ] Metadados de proveniência (who/when/how) registados no registro (ou attestation store)
- [ ] Job de verificação de assinatura disponível para pipelines de deploy
- [ ] Documentação do processo e chaves/rotas de rotação em política interna

:::

**Artefactos & evidências.**
- `sbom.cyclonedx.json`, `artifact.sig`, attestations, build metadata

> **Referência:** Este US especializa [Cap 05-US-02: SBOM em cada build]
> para o contexto de requisitos de proveniência e assinatura. Para detalhes técnicos de geração e armazenamento de SBOM, consulte Cap 05.

**Integração no SDLC.**
| Fase | Trigger | Responsável | SLA |
|---|---|---|---|
| Build | Build de release | Developer + DevOps/SRE | Sempre na pipeline de release |

---

### US-12 – Validação de tags `SEC-Lx-*` e requisitos no pipeline

**Contexto.**
Tags `SEC-Lx-*` e referências a `REQ-XXX` devem estar presentes nos cartões/PRs para garantir rastreabilidade e cobertura automática.

:::userstory
**História.**
Como **Developer** e **QA**, quero que o pipeline valide a presença e conformidade das tags `SEC-Lx-*` e referências a REQ-XXX no PR, para garantir que o trabalho é rastreável e que as checks automáticas sabem que requisitos foram acionados.

**BDD.**
- Dado um PR que implementa uma mudança funcional
- Quando o job `tag-check` executa no pipeline
- Então o PR falha se não existir pelo menos uma tag `SEC-Lx-*` válida ou um link para `REQ-XXX`; o comentário automático explica a necessidade

**DoD.**
- [ ] Job `tag-check` presente e executável no CI
- [ ] Validação de formato `SEC-L[1-3]-[T|C]-[0-9]{3}` ou conforme taxonomia do capítulo
- [ ] Verificação de link REQ-XXX no corpo do PR ou issue associado
- [ ] Mensagem automática de pull request com instruções quando falhar

:::

**Artefactos & evidências.**
- Logs de `tag-check`, exemplos de PRs conformes, templates de PR com checklist

**Integração no SDLC.**
| Fase | Trigger | Responsável | SLA |
|---|---|---|---|
| PR/MR | Criação de PR | Developer + DevOps | Antes de merge |

---

### US-13 – Política, Formação e Publicação de Procedimentos Operacionais

**Contexto.**
Para que as práticas acima sejam aplicadas de forma consistente, a organização deve publicar políticas, definir responsabilidades e conduzir formação para os papéis relevantes.

:::userstory
**História.**
Como **Gestão Executiva/CISO** e **GRC/Compliance**, quero publicar a política de aplicação de requisitos e providenciar formação para Developers, AppSec e DevOps, para que as equipas saibam procedimentos, SLAs e como operar os pipelines de segurança.

**BDD.**
- Dado que existem novas práticas de pipeline e gestão de exceções
- Quando a política e os guias operacionais são publicados
- Então as equipas recebem formação e um checklist operacional, e a conformidade é avaliada num período de 3 meses

**DoD.**
- [ ] Política de aplicação de requisitos publicada e versionada
- [ ] Playbooks operacionais (pipeline, SBOM, assinatura, exceções) documentados
- [ ] Sessões de formação realizadas para Developers, DevOps e AppSec (registo de presenças)
- [ ] Mecanismo de feedback e FAQs disponível para clarificação
- [ ] Auditoria interna/avaliação de conformidade 3 meses após publicação

:::

**Artefactos & evidências.**
- Política publicada (doc/MD), slides e gravações de formação, registos de presença, checklist de conformidade

**Integração no SDLC.**
| Fase | Trigger | Responsável | SLA |
|---|---|---|---|
| Governança | Publicação de política ou mudança de tooling | CISO + GRC/Compliance | Política publicada e formação em 30 dias |

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
