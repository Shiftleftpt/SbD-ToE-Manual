---
id: aplicacao-lifecycle
title: Aplicação de Requisitos de Segurança no Ciclo de Vida
description: Integração das práticas de requisitos ao longo das fases do ciclo de desenvolvimento
tags: [tipo:aplicacao, ciclo-vida, requisitos, validacao, rastreabilidade, excecoes]
genia: us-format-normalization
---

# 🛠️ Aplicação de Requisitos de Segurança no Ciclo de Vida

Este documento prescreve **como aplicar sistematicamente os requisitos definidos no Capítulo 2** ao longo do ciclo de desenvolvimento, garantindo **rastreabilidade**, **proporcionalidade ao risco** e **validação contínua**.

Inclui modelos reutilizáveis de *user stories*, ações por papel, artefactos esperados e quadros de aplicação por nível de criticidade (L1–L3).

> **Nota de enquadramento:** L1–L3 classificam o **risco da aplicação** (impacto e exposição).  
> As características do processo (ex.: elevado grau de automação, geração de artefactos, dependência de terceiros) **não alteram a classificação**, mas podem exigir maior rigor de validação, evidência e controlo operacional.

---

## 📅 Quando aplicar os requisitos de segurança

| Fase / Evento                    | Ação esperada                                                                 | Artefacto principal                      |
| -------------------------------- | ----------------------------------------------------------------------------- | ---------------------------------------- |
| Início de projeto                | Seleção proporcional de requisitos com base na criticidade                    | `matriz-controlos-por-risco.md`          |
| Grooming / Planeamento           | Transformar requisitos em cartões rastreáveis                                 | Backlog (cards + tags `SEC-...`)         |
| Nova funcionalidade / refactor   | Revalidar requisitos aplicáveis à alteração (e, se aplicável, atualizar REQ)  | Story/tarefa técnica atualizada          |
| Integração ou exposição externa  | Rever requisitos de autenticação, logging, controlo de acesso e APIs          | Issue/checklist de integração            |
| Sprint review / Testes           | Verificar critérios de aceitação de segurança e recolher evidência            | Critérios + testes + evidências          |
| Preparação para go-live / release| Validar requisitos aplicados, exceções aprovadas, cobertura e evidência       | Checklist de release + evidência anexada |

---

## 👥 Quem faz o quê

| Papel / Função                      | Responsabilidades-chave                                                                 |
| ----------------------------------- | ---------------------------------------------------------------------------------------- |
| Product Owner / BA                  | Assegurar integração no backlog; garantir que requisitos relevantes existem como trabalho rastreável |
| Developer                           | Implementar controlos; aplicar tags; ligar mudanças a `SEC-Lx-*` e/ou `REQ-XXX`; propor exceções quando necessário |
| QA / Test Engineer                  | Definir critérios de aceitação e validação; garantir cobertura de testes e evidência     |
| Arquitetura / Tech Lead / DevSecOps | Rever requisitos em alterações críticas; assegurar coerência técnica e impacto no risco  |
| Equipa de Segurança / AppSec        | Validar aplicação; aprovar exceções; garantir alinhamento e consistência global          |
| GRC/Compliance (quando aplicável)   | Registar exceções e decisões; apoiar auditoria e rastreabilidade organizacional          |

> ✅ A rastreabilidade e a verificabilidade são responsabilidades partilhadas;  
> **a responsabilidade final sobre decisões de risco e exceções deve ser sempre explícita.**

---

## 📝 User Stories e Cartões Reutilizáveis

### US-01 — Seleção de requisitos por criticidade

**Contexto.**  
A seleção inicial de requisitos deve ser proporcional ao risco da aplicação (L1–L3).

:::userstory
**História.**  
Como **Product Owner**, quero selecionar os requisitos aplicáveis ao projeto, para garantir que a segurança é proporcional ao nível de risco.

**Critérios de aceitação (BDD).**
- **Dado** que a aplicação tem um nível de criticidade atribuído  
  **Quando** consulto a matriz de aplicação de requisitos adequada  
  **Então** marco no backlog os requisitos aplicáveis ao nível definido e registo a evidência da decisão

**Checklist.**
- [ ] Classificação de criticidade (L1–L3) atribuída  
- [ ] Matriz de aplicação usada (`SEC-Lx-...`)  
- [ ] Requisitos marcados no backlog  
- [ ] Evidência documentada no repositório do projeto

:::

**Artefactos & evidências.**
- Artefacto: `matriz-controlos-por-risco.md`  
- Evidência: backlog com tags `SEC-Lx-*` e referência ao nível Lx do projeto

**Proporcionalidade por risco.**
| Nível | Obrigatório? | Ajustes |
|---|---|---|
| L1 | Recomendado | Subconjunto essencial |
| L2 | Sim | Catálogo completo aplicável a L2 |
| L3 | Sim | Catálogo completo aplicável a L3 + reforços |

**Integração no SDLC.**
| Fase | Trigger | Responsável | SLA |
|---|---|---|---|
| Início | Kick-off do projeto | Product Owner | Antes do backlog inicial |

---

### US-02 — Revisão por alteração relevante

**Contexto.**  
Requisitos aplicáveis devem ser revistos sempre que exista alteração material do contexto técnico, superfície de exposição, dados tratados ou arquitetura.

:::userstory
**História.**  
Como **Arquitetura/Tech Lead** e **Scrum Master/Team Lead**, quero rever requisitos aplicáveis sempre que ocorra uma integração crítica ou mudança relevante, para garantir que os controlos e requisitos selecionados são atualizados, rastreados e validados.

**Critérios de aceitação (BDD).**
- **Dado** que ocorre uma alteração significativa (integração externa, mudança de dados, exposição, arquitetura)
  **Quando** a equipa analisa o impacto técnico e de risco
  **Então** atualiza a seleção de requisitos, cria/atualiza trabalho no backlog com tags `SEC-Lx-*` e, se aplicável, dispara novo Threat Modeling

**Critérios de aceitação (DoD).**
- [ ] Seleção/matriz atualizada e registada (incluindo novos requisitos aplicáveis)
- [ ] Se a alteração afeta risco: disparo de Threat Modeling registado
- [ ] Cartões no backlog marcados com `SEC-Lx-*` e owner definido
- [ ] Evidência: PR/issue com ligações relevantes (ex.: requisito ↔ alteração ↔ risco)
- [ ] Notificação a AppSec para validação (L2/L3 ou alterações críticas)

:::

**Artefactos & evidências.**
- `matriz-controlos-por-risco.md` atualizado; PR/issue; wiki/diagrama de arquitetura; registo de decisão e notificação

**Proporcionalidade.**
- L1: revisão ad-hoc; L2: revisão obrigatória; L3: revisão obrigatória + validação AppSec

**Integração no SDLC.**
| Fase | Trigger | Responsável | SLA |
|---|---|---|---|
| Design/Refactor | Alteração de arquitetura, dados ou exposição | Arquitetura + Tech Lead | Antes da release |

**Ligações úteis.**
- 🔗 [Validação e revisão de requisitos](./addon/validacao-requisitos)

---

### US-03 — Gestão de Exceções com TTL e Revalidação Obrigatória

**Contexto.**  
Nem todos os requisitos são aplicáveis. Exceções devem ser documentadas, justificadas, aprovadas e sujeitas a revalidação, evitando exceções permanentes.

:::userstory
**História.**  
Como **Developer** (proponente) e **GRC/Compliance** (regista), quero registar exceções com TTL e fluxo de aprovação por **AppSec** (técnica) e **Gestão Executiva/CISO** (quando aplicável), para garantir que todas as exceções são temporais, rastreáveis e revalidadas.

**Critérios de aceitação (BDD).**
- **Dado** que um requisito não pode ser aplicado
  **Quando** a equipa regista uma exceção (ID único) com justificação e TTL
  **Então** a exceção fica com owner definido, alerta configurado antes da expiração e reaprovação exigida para renovação

**Critérios de aceitação (DoD).**
- [ ] Exceção com ID e ligação ao requisito (`SEC-Lx-...` e/ou `REQ-XXX`) registada
- [ ] TTL definido consoante nível (L1=12m recomendado; L2=6m; L3=3m)
- [ ] Owner designado e destinatários de alertas definidos
- [ ] Aprovação técnica por AppSec documentada; aprovação executiva quando aplicável em L3
- [ ] Alertas automáticos configurados (ex.: 15 dias antes de expiração)
- [ ] Evidência de revalidação, mitigação ou encerramento anexada

:::

**Artefactos & evidências.**
- `excecoes/EXC-YYYY-N.md` (ou ticket GRC); logs de alerta; histórico de decisões e aprovadores

> **Referência:** Esta user story especializa o processo organizacional de exceções (Cap. 14) para o contexto de requisitos. TTL, alçadas de aprovação e revalidação devem seguir a política master definida nesse capítulo.

**Proporcionalidade.**
- L1: processo simplificado; L2: formalização obrigatória; L3: formal + mitigação exigida

**Integração no SDLC.**
| Fase | Trigger | Responsável | SLA |
|---|---|---|---|
| Planeamento/Release | Identificação da exceção | Developer + AppSec + GRC | Antes da release |

**Ligações úteis.**
- 🔗 [Gestão de exceções](./addon/gestao-excecoes)

---

### US-04 — Rastreabilidade de requisitos

**Contexto.**  
Todos os requisitos aplicados devem ser rastreáveis no backlog e auditáveis.

:::userstory
**História.**  
Como **QA / Test Engineer**, quero garantir que todos os requisitos aplicados têm rastreabilidade no backlog, para suportar auditoria e verificação.

**Critérios de aceitação (BDD).**
- **Dado** que os requisitos aplicáveis foram selecionados  
  **Quando** reviso backlog e PRs  
  **Então** encontro trabalho associado com tags `SEC-Lx-*` e referências rastreáveis às validações/evidências

**Checklist.**
- [ ] Todos os cartões relevantes têm tag `SEC-Lx-Tyy-ZZZ` (ou conforme taxonomia)
- [ ] Referência cruzada com o catálogo de requisitos aplicáveis
- [ ] Relatórios exportáveis (auditoria)
- [ ] Evidência de rastreabilidade arquivada

:::

**Artefactos & evidências.**
- Artefacto: board de desenvolvimento  
- Evidência: relatório/export de rastreabilidade e ligações para validações

**Proporcionalidade por risco.**
| Nível | Obrigatório? | Ajustes |
|---|---|---|
| L1 | Recomendado | Apenas requisitos críticos |
| L2 | Sim | Cobertura total dos requisitos selecionados |
| L3 | Sim | Cobertura total + rastreabilidade reforçada |

**Integração no SDLC.**
| Fase | Trigger | Responsável | SLA |
|---|---|---|---|
| Grooming | Revisão de backlog | QA | Por sprint |

**Ligações úteis.**
- 🔗 [Taxonomia de rastreabilidade](./addon/rastreabilidade-controlo)

---

### US-05 — Definição de critérios de validação

**Contexto.**  
Cada requisito selecionado deve ter critérios de aceitação/validação explícitos e verificáveis.

:::userstory
**História.**  
Como **Product Owner/QA**, quero garantir que cada requisito selecionado no backlog contém critérios de aceitação de segurança claros, para que possam ser validados e testados de forma consistente.

**Critérios de aceitação (BDD).**
- **Dado** que um requisito é selecionado  
  **Quando** o coloco no backlog  
  **Então** adiciono critérios de aceitação/validação formais e verificáveis

**Checklist.**
- [ ] Critérios definidos no cartão  
- [ ] Alinhamento com catálogo aplicável
- [ ] Validação prevista em testes e/ou revisões
- [ ] Evidência registada e rastreável

:::

**Artefactos & evidências.**
- Artefacto: backlog  
- Evidência: cartões/documentos com critérios e ligações a validações

**Proporcionalidade por risco.**
| Nível | Obrigatório? | Ajustes |
|---|---|---|
| L1 | Recomendado | Para requisitos críticos |
| L2 | Sim | Para todos os requisitos selecionados |
| L3 | Sim | Para todos + validação reforçada |

**Integração no SDLC.**
| Fase | Trigger | Responsável | SLA |
|---|---|---|---|
| Planeamento | Criação de cartões | PO + QA | Antes da sprint |

**Ligações úteis.**
- 🔗 [Validação de requisitos](./addon/validacao-requisitos)

---

### US-06 — Validação de cobertura de testes

**Contexto.**  
Requisitos devem ter validação associada para prevenir regressões e garantir eficácia.

:::userstory
**História.**  
Como **QA / Test Engineer**, quero garantir que os requisitos aplicáveis têm validação associada, para prevenir ausência de controlo e suportar evidência auditável.

**Critérios de aceitação (BDD).**
- **Dado** que requisitos foram aplicados  
  **Quando** executo os testes/revisões de validação  
  **Então** obtenho evidência documentada e rastreável do resultado

**Checklist.**
- [ ] Testes automáticos ou manuais documentados  
- [ ] Critérios de aceitação definidos  
- [ ] Evidência de execução por sprint/release  
- [ ] Logs/relatórios arquivados em CI/CD quando aplicável

:::

**Artefactos & evidências.**
- Artefacto: planos de teste/validação  
- Evidência: logs, relatórios, screenshots, revisões, resultados

**Proporcionalidade por risco.**
| Nível | Obrigatório? | Ajustes |
|---|---|---|
| L1 | Recomendado | Validação básica dos requisitos críticos |
| L2 | Sim | Cobertura integral dos requisitos selecionados |
| L3 | Sim | Cobertura integral + revisão independente |

**Integração no SDLC.**
| Fase | Trigger | Responsável | SLA |
|---|---|---|---|
| Sprint review | Execução de validações | QA | Por sprint |

**Ligações úteis.**
- 🔗 [Validação de requisitos](./addon/validacao-requisitos)

---

### US-07 — Validação e aprovação final

**Contexto.**  
A Equipa de Segurança deve validar a aplicação dos requisitos e aprovar exceções, controlando formalmente as decisões de risco.

:::userstory
**História.**  
Como **Equipa de Segurança / AppSec**, quero validar a aplicação dos requisitos e aprovar exceções, para garantir que as decisões de risco estão controladas e documentadas.

**Critérios de aceitação (BDD).**
- **Dado** que a release está pronta  
  **Quando** reviso requisitos aplicados e exceções  
  **Então** aprovo ou rejeito com base no risco e evidência disponível

**Checklist.**
- [ ] Requisitos aplicáveis verificados (evidência disponível)
- [ ] Exceções aprovadas/rejeitadas e registadas
- [ ] Evidência de decisão documentada
- [ ] Feedback registado no backlog/board

:::

**Artefactos & evidências.**
- Artefacto: registo de requisitos e exceções  
- Evidência: decisão registada em PR/issue e/ou ferramenta GRC

**Proporcionalidade por risco.**
| Nível | Obrigatório? | Ajustes |
|---|---|---|
| L1 | Recomendado | Revisão simplificada |
| L2 | Sim | Revisão formal |
| L3 | Sim | Revisão formal + mitigação exigida |

**Integração no SDLC.**
| Fase | Trigger | Responsável | SLA |
|---|---|---|---|
| Release | Aprovação final | AppSec | Antes do go-live |

**Ligações úteis.**
- 🔗 [Gestão de exceções](./addon/gestao-excecoes)

---

### US-08 — Catálogo de requisitos do projeto (criação e manutenção)

**Contexto.**  
No arranque do projeto e sempre que existam alterações de âmbito, deve existir um **catálogo versionado de requisitos do projeto**, derivado da baseline organizacional e filtrado pela criticidade.

:::userstory
**História.**  
Como **AppSec/PO/TL**, quero estabelecer e manter um catálogo de requisitos de segurança do projeto (REQ-XXX), para assegurar aplicação consistente, versionada e auditável ao longo do SDLC.

**Critérios de aceitação (BDD).**
- **Dado** que a aplicação tem criticidade L1–L3 definida  
  **Quando** derivo o catálogo do projeto a partir da baseline e filtro por nível  
  **Então** o catálogo fica versionado, com owner definido e ligação a critérios de validação

**Checklist.**
- [ ] Catálogo `REQ-XXX` criado/atualizado e versionado  
- [ ] Owner e periodicidade de revisão definidos  
- [ ] Mapeamento para critérios de validação e tags de backlog  
- [ ] Localização e link persistentes no repositório

:::

**Artefactos & evidências.**
- Artefacto: `catalogo-requisitos.md` (ou pasta `catalogo/`) + changelog  
- Evidência: MR/PR de criação/atualização e aprovação por AppSec

**Proporcionalidade por risco.**
| Nível | Obrigatório? | Ajustes |
|---|---|---|
| L1 | Sim | Subconjunto essencial pré-aprovado |
| L2 | Sim | Catálogo completo aplicável a L2 |
| L3 | Sim | Catálogo aplicável a L3 + reforços relevantes |

**Integração no SDLC.**
| Fase | Trigger | Responsável | SLA |
|---|---|---|---|
| Início | Kick-off / release major | AppSec + PO + TL | Antes do backlog inicial / antes da release |

**Ligações úteis.**
- 🔗 [Catálogo de requisitos](./addon/catalogo-requisitos)  
- 🔗 [Critérios de aceitação](./addon/criterios-aceitacao)

---

### US-09 — Validação por requisito/domínio (REQ-XXX → evidência)

**Contexto.**  
Cada requisito ativo deve ter validação e evidência associadas.

:::userstory
**História.**  
Como **QA/AppSec/TL**, quero validar cada requisito REQ-XXX segundo os critérios definidos, para assegurar evidência objetiva e rastreável do seu cumprimento.

**Critérios de aceitação (BDD).**
- **Dado** um requisito REQ-XXX com critérios definidos  
  **Quando** executo a validação associada  
  **Então** registo o resultado e anexo evidência ao requisito

**Checklist.**
- [ ] Método de validação definido por requisito  
- [ ] Execução registada por sprint/release  
- [ ] Resultado e evidência ligados ao REQ-XXX  
- [ ] Revisão e aprovação por AppSec quando aplicável

:::

**Artefactos & evidências.**
- Artefacto: `validacoes/REQ-XXX.md` (ou equivalente)  
- Evidência: logs CI/CD, relatórios (SAST/DAST/IAST), reviews, screenshots

**Proporcionalidade por risco.**
| Nível | Obrigatório? | Ajustes |
|---|---|---|
| L1 | Sim | Cobertura mínima dos requisitos críticos |
| L2 | Sim | Cobertura integral dos requisitos selecionados |
| L3 | Sim | Cobertura integral + revisão independente e gates automáticos |

**Integração no SDLC.**
| Fase | Trigger | Responsável | SLA |
|---|---|---|---|
| Testes/Review | Pipelines e checkpoints | QA + AppSec + TL | Por sprint e antes de release |

**Ligações úteis.**
- 🔗 [Validação de requisitos](./addon/validacao-requisitos)  
- 🔗 [Controlos por requisito](./addon/controlos-requisitos)

---

### US-10 — Gates automáticos em CI/CD para requisitos de segurança

**Contexto.**  
Pipelines devem impor verificações automáticas alinhadas com requisitos aplicáveis, bloqueando merge/release quando falham.

:::userstory
**História.**  
Como **DevOps/SRE** e **Developer**, quero que o pipeline CI/CD execute verificações de segurança e imponha *gates*, para que merges e releases só ocorram quando os requisitos de segurança forem satisfeitos.

**Critérios de aceitação (BDD).**
- **Dado** um PR/MR para a branch principal
  **Quando** o pipeline executa os jobs de segurança
  **Então** o merge é bloqueado se qualquer gate crítico falhar, e os relatórios ficam anexados ao PR

**Critérios de aceitação (DoD).**
- [ ] SAST executado com baseline e limiares configurados
- [ ] SCA executado; vulnerabilidades acima de limiar geram falha ou issue bloqueante
- [ ] DAST em staging quando aplicável (L2/L3 e alterações de exposição)
- [ ] Geração de SBOM (CycloneDX ou SPDX) anexada ao artefacto
- [ ] Assinatura do artefacto e armazenamento de assinatura/proveniência
- [ ] `policy-check` valida tags `SEC-Lx-*` e links `REQ-XXX` no PR
- [ ] Sumário do gate ligado ao PR/issue

:::

**Artefactos & evidências.**
- Logs CI, relatórios SAST/SCA/DAST, SBOM (`sbom.cdx.json`), assinatura (`artifact.sig`), relatório de gate

**Proporcionalidade por risco.**
| Nível | Obrigatório? | Ajustes |
|---|---|---|
| L1 | Recomendado | SAST básico; SCA recomendado |
| L2 | Sim | SAST + SCA obrigatórios; limiares configurados |
| L3 | Sim | SAST + SCA + DAST; gates rigorosos; SBOM + assinatura obrigatórios |

**Integração no SDLC.**
| Fase | Trigger | Responsável | SLA |
|---|---|---|---|
| Merge/Release | PR/MR targeting main/release | DevOps/SRE + AppSec | Bloqueio automático até resolução |

**Ligações úteis.**
- 🔗 [Gates de segurança em CI/CD](/sbd-toe/sbd-manual/cicd-seguro/addon/gates-seguranca)  
- 🔗 [SBOM e proveniência](/sbd-toe/sbd-manual/dependencias-sbom-sca/intro)

---

### US-11 — Geração de SBOM e assinatura de artefactos de build

**Contexto.**  
SBOMs e assinaturas suportam proveniência e auditoria.

:::userstory
**História.**  
Como **Developer** e **DevOps/SRE**, quero que a pipeline gere um SBOM e assine o artefacto final, para que possamos verificar origem, dependências e integridade no deployment.

**Critérios de aceitação (BDD).**
- **Dado** que é construído um artefacto de release
  **Quando** o job de build termina com sucesso
  **Então** é gerado um SBOM e o artefacto é assinado; ambos ficam armazenados com metadados de proveniência

**Critérios de aceitação (DoD).**
- [ ] SBOM gerado (CycloneDX/SPDX) e anexado ao build
- [ ] Artefacto assinado e assinatura armazenada no registo
- [ ] Metadados de proveniência (who/when/how) registados
- [ ] Job de verificação de assinatura disponível para deploy
- [ ] Procedimentos e rotação de chaves documentados em política interna

:::

**Artefactos & evidências.**
- `sbom.cyclonedx.json`, `artifact.sig`, attestations, build metadata

> **Referência:** Especializa o processo de SBOM e proveniência descrito no Cap. 05 para o contexto de requisitos.

**Integração no SDLC.**
| Fase | Trigger | Responsável | SLA |
|---|---|---|---|
| Build | Build de release | Developer + DevOps/SRE | Sempre na pipeline de release |

---

### US-12 — Validação de tags `SEC-Lx-*` e requisitos no pipeline

**Contexto.**  
Tags e referências devem estar presentes para garantir rastreabilidade.

:::userstory
**História.**  
Como **Developer** e **QA**, quero que o pipeline valide a presença e conformidade de tags `SEC-Lx-*` e referências a `REQ-XXX`, para garantir rastreabilidade e acionamento correto de checks automáticas.

**Critérios de aceitação (BDD).**
- **Dado** um PR com mudança funcional
  **Quando** o job `tag-check` executa
  **Então** o PR falha se não existir pelo menos uma tag válida e uma referência rastreável ao requisito aplicável; o comentário automático explica o que falta

**Critérios de aceitação (DoD).**
- [ ] Job `tag-check` presente e executável
- [ ] Validação de formato conforme taxonomia do capítulo
- [ ] Verificação de referência/ligação a `REQ-XXX` quando aplicável
- [ ] Comentário automático no PR com instruções quando falhar

:::

**Artefactos & evidências.**
- Logs do `tag-check`, templates de PR, exemplos de PRs conformes

**Integração no SDLC.**
| Fase | Trigger | Responsável | SLA |
|---|---|---|---|
| PR/MR | Criação de PR | Developer + DevOps | Antes de merge |

---

### US-13 — Política, Formação e Procedimentos Operacionais

**Contexto.**  
Para consistência, a organização deve publicar políticas, responsabilidades e formação.

:::userstory
**História.**  
Como **Gestão Executiva/CISO** e **GRC/Compliance**, quero publicar a política de aplicação de requisitos e providenciar formação, para que as equipas conheçam procedimentos, SLAs e operação dos controlos.

**Critérios de aceitação (BDD).**
- **Dado** que existem práticas de pipeline e gestão de exceções
  **Quando** a política e os guias operacionais são publicados
  **Então** as equipas recebem formação e checklist operacional, e a conformidade é avaliada num período definido (ex.: 3 meses)

**Critérios de aceitação (DoD).**
- [ ] Política publicada e versionada
- [ ] Playbooks operacionais documentados
- [ ] Sessões de formação realizadas e registadas
- [ ] Mecanismo de feedback/FAQ disponível
- [ ] Avaliação/auditoria interna após período definido

:::

**Artefactos & evidências.**
- Política publicada; materiais de formação; registos; checklist de conformidade

**Integração no SDLC.**
| Fase | Trigger | Responsável | SLA |
|---|---|---|---|
| Governança | Publicação de política/mudança de práticas | CISO + GRC | Política e formação em prazo definido |

---

### US-14 – Uso controlado de assistentes automatizados (incluindo IA) no desenvolvimento

**Contexto.**  
O uso de assistentes automatizados e ferramentas baseadas em IA pode acelerar o desenvolvimento, mas **não altera nem substitui** os requisitos de segurança aplicacionais. Todo o output gerado deve ser tratado como código de terceiros e sujeito a governação, validação e rastreabilidade explícitas.

:::userstory
**História.**  
Como **Developer**, **Tech Lead** e **AppSec Engineer**, quero garantir que qualquer código, configuração ou teste gerado com recurso a assistentes automatizados (incluindo IA) é explicitamente revisto, validado e rastreável, para assegurar que o cumprimento dos requisitos de segurança é verificável e que a responsabilidade permanece humana.

**Critérios de aceitação (BDD).**
- **Dado** que é utilizado um assistente automatizado para gerar código, configuração ou testes  
  **Quando** o output é integrado no repositório  
  **Então** o artefacto é sujeito a revisão humana, validação automática em CI/CD e ligado a requisitos `REQ-XXX` aplicáveis

**Critérios de aceitação (DoD).**
- [ ] Código/configuração gerada identificada no PR/MR (nota ou template de PR)
- [ ] Revisão humana efetuada e aprovada (code review formal)
- [ ] Gates de segurança em CI/CD executados (SAST, SCA e outros aplicáveis)
- [ ] Requisitos `REQ-XXX` e tags `SEC-Lx-*` referenciados no PR/MR
- [ ] Evidência de validação arquivada (logs de pipeline, relatórios, approvals)
- [ ] Nenhum segredo, credencial ou dado sensível incluído em prompts ou artefactos gerados

:::

**Artefactos & evidências.**
- PR/MR com referência a `REQ-XXX` e tags `SEC-Lx-*`
- Logs de CI/CD (SAST, SCA, testes)
- Aprovação de code review
- Relatório de gates de segurança

**Proporcionalidade por risco.**
| Nível | Obrigatório? | Ajustes |
|---|---|---|
| L1 | Recomendado | Revisão humana e SAST básico |
| L2 | Sim | Revisão + SAST/SCA obrigatórios |
| L3 | Sim | Revisão + SAST/SCA + validações reforçadas e AppSec review |

**Integração no SDLC.**
| Fase | Trigger | Responsável | SLA |
|---|---|---|---|
| PR/MR | Introdução de código/configuração gerada | Developer + Tech Lead | Antes do merge |
| Release | Gate final de segurança | AppSec | Antes do go-live |

**Ligações úteis.**
- 🔗 [Governação do uso de automatismos](./addon/governanca-automatismos)
- 🔗 [Gates automáticos em CI/CD](/sbd-toe/sbd-manual/cicd-seguro/addon/gates-seguranca)
- 🔗 [Validação de requisitos](./addon/validacao-requisitos)

---

## ⚖️ Aplicação proporcional por nível de risco (L1–L2–L3)

| Prática                    | L1 (baixo risco)               | L2 (médio risco)                          | L3 (alto risco)                                      |
| -------------------------- | ------------------------------ | ----------------------------------------- | ---------------------------------------------------- |
| Catálogo de requisitos     | Subconjunto essencial          | Catálogo completo aplicável a L2          | Catálogo completo aplicável a L3 + reforços relevantes |
| Rastreabilidade (tags)     | Recomendado                    | Obrigatória nos cartões de segurança      | Obrigatória em cartões técnicos e funcionais          |
| Exceções                   | Simplificado                   | Documentadas e aprovadas                  | Formalizadas com TTL curto e mitigação                |
| Validação de requisitos    | Revisão/validação básica        | Testes associados e evidência             | Testes + evidência + revisão independente             |
| Reavaliação por alterações | A pedido                        | A cada alteração crítica                   | Sempre que há mudança de exposição/arquitetura/controlo |

---

## 📄 Templates e artefactos esperados

| Artefacto                       | Formato sugerido           | Onde guardar / referenciar            |
| ------------------------------- | -------------------------- | ------------------------------------- |
| Matriz de requisitos por risco  | Markdown / tabela          | `docs/` ou Wiki de produto            |
| Cartões com tags `SEC-*`        | Board / GitHub / Jira      | Backlog da equipa                     |
| Catálogo do projeto (`REQ-XXX`) | Markdown / ficheiros       | `docs/req/` (ou equivalente)          |
| Justificação de exceções        | Markdown / issue template  | `excecoes/` ou ferramenta GRC         |
| Relatórios de rastreabilidade   | Export de board / CSV      | Arquivo de auditoria                  |
| Planos de teste e evidências    | YAML / Markdown / CI logs  | Repositório QA e/ou CI/CD             |
