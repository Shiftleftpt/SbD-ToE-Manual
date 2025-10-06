---
id: aplicacao-lifecycle
title: Aplicação no Ciclo de Vida — Desenvolvimento Seguro
description: Como aplicar práticas de desenvolvimento seguro em cada fase do SDLC, com user stories reutilizáveis, artefactos auditáveis e matriz proporcional L1–L3
tags: [desenvolvimento, ciclo-de-vida, codificação-segura, validação, user-stories]
sidebar_position: 15
---

# ⚙️ Aplicação no Ciclo de Vida — Desenvolvimento Seguro {desenvolvimento-seguro:aplicacao-lifecycle}

O desenvolvimento seguro não é um exercício teórico ou uma “boa prática” vaga: exige aplicação consistente em cada fase do ciclo de vida do software.  
Neste documento mostramos **como transformar as prescrições do capítulo em prática diária**, detalhando quando aplicar, quem executa, que user stories devem entrar no backlog e quais as evidências que permitem auditoria e governação.  
O objetivo é simples mas ambicioso: fazer do desenvolvimento seguro um hábito mensurável, rastreável e parte intrínseca da qualidade do produto.

---

## 🧭 Quando aplicar {desenvolvimento-seguro:aplicacao-lifecycle#quando}

A segurança acompanha o projeto desde o início e não pode ser relegada para fases finais.  
O quadro seguinte mostra **em que momentos concretos do SDLC** cada prática deve ser aplicada e qual a ação esperada em cada um deles.

| Fase do SDLC          | Momento específico                         | Ação esperada                                       |
|-----------------------|---------------------------------------------|-----------------------------------------------------|
| Planeamento           | Definição de stack, dependências, guidelines| Criar/adaptar guidelines seguras                    |
| Desenvolvimento       | Ao escrever/refatorar código                | Aplicar linters, validações locais                  |
| Revisão de Código     | Em cada PR / merge                         | Checklist e validação formal                        |
| Integração Contínua   | Execução do pipeline                        | SAST, validação de dependências e *rulesets*        |
| Pré-produção          | Go-live / release                          | Validação de exceções, checklist final              |
| Operação / Manutenção | Atualizações, patches, refatorizações       | Revisão de guidelines, dependências e exceções      |

---

## 👥 Quem executa cada ação {desenvolvimento-seguro:aplicacao-lifecycle#quem}

A segurança no desenvolvimento é um **esforço coletivo**: diferentes papéis contribuem de forma complementar, formando uma cadeia de confiança.  
A tabela seguinte explicita estas responsabilidades.

| Papel/Função                      | Responsabilidades principais |
|-----------------------------------|------------------------------|
| **Desenvolvedor**                 | Aplicar guidelines, linters e validações locais; propor *tailoring* de regras quando necessário |
| **Revisor Técnico**               | Validar PRs, confirmar critérios de segurança e exceções; aplicar checklist formal |
| **Equipa AppSec**                 | Definir critérios mínimos, aprovar exceções, validar dependências críticas; mapear ASVS/CWE |
| **DevSecOps / CI/CD**             | Automatizar linters/SAST, versionar e distribuir *rulesets* organizacionais; aplicar enforcement |
| **Gestor Técnico / Lead de Stack**| Criar/selecionar guidelines base por stack; aprovar derivadas de linters/analisadores; assegurar revisão periódica |

---

## 📖 User Stories reutilizáveis {desenvolvimento-seguro:aplicacao-lifecycle#user-stories}
### US-01 — Guidelines de Desenvolvimento Seguro {#us-01}

**Contexto.**  
Guidelines claras e versionadas por *stack* evitam decisões ad-hoc e asseguram consistência. Mais do que um documento estático, são um **mecanismo vivo** de governação: atualizadas, revistas e aplicadas diariamente. A existência de *rulesets* derivadas de linters e analisadores automáticos, com *tailoring* documentado, reduz significativamente riscos de interpretação subjetiva.

**📖 Rationale científico.**  
Alinhado com **SSDF PS.1** (definição de requisitos), **SAMM Implementation** e **BSIMM SE2.3** (guidelines de codificação).  
Mitiga falhas como **CWE-657 (Violation of Secure Design Principles)** e **CWE-20 (Improper Input Validation)**.  
Segundo o **Verizon DBIR 2023**, cerca de 27% das falhas exploradas têm origem em práticas de codificação deficientes.  
Estudos da Microsoft SDL e investigações independentes demonstram que *guidelines* versionadas e aplicadas com linters reduzem em 40% a reincidência de vulnerabilidades.

**História.**  
Como **Desenvolvedor**, quero aplicar as guidelines de código seguro aprovadas, para garantir consistência e reduzir vulnerabilidades desde o início.

**Critérios de aceitação (BDD).**
- Dado que inicio desenvolvimento numa *stack* definida  
- Quando consulto as guidelines aprovadas  
- Então aplico as regras mínimas obrigatórias e registo qualquer desvio justificado

**Checklist (binária, auditável).**
- [ ] `guidelines-stack.md` referenciado no README do projeto  
- [ ] Ficheiros de configuração de linters/analisadores presentes e versionados  
- [ ] Regras mínimas aplicadas  
- [ ] *Tailoring* documentado (`rules/README.md`) e aprovado  
- [ ] Desvios registados em `excecoes-seguranca.md`  
- [ ] Evidência de revisão do PR

**Artefactos & evidências.**
- Artefactos: `guidelines-stack.md`, diretório `rules/`  
- Evidência: commit IDs + histórico do PR

**Proporcionalidade por risco.**
| Nível | Obrigatório? | Ajustes |
|-------|--------------|---------|
| L1    | Sim          | Regras upstream com ajustes mínimos |
| L2    | Sim          | Conjunto organizacional curado |
| L3    | Sim          | Auditoria periódica e *policy-as-code* |

**Integração no SDLC.**
| Fase        | Gatilho           | Responsável              | SLA             |
|-------------|-------------------|--------------------------|-----------------|
| Planeamento | Definição de stack| Gestor Técnico + Dev     | Antes do 1.º sprint |

**Ligações úteis.**  
xref:sbd-toe:cap06:intro

---

### US-02 — Revisão de Código Segura {#us-02}

**Contexto.**  
Revisões de código não são apenas uma prática de qualidade, mas um **ponto de controlo de segurança**. Quando sistematizadas com checklist, previnem vulnerabilidades, promovem partilha de conhecimento e criam registo formal de conformidade.

**📖 Rationale científico.**  
Baseado em **SAMM Verification (Code Review)**, **BSIMM SE2.4** e **SSDF RV.1**.  
Mitiga riscos como **CWE-22 (Path Traversal)** e **CWE-89 (SQL Injection)**.  
Segundo o **SmartBear 2022 State of Code Review**, equipas que utilizam checklists formais reduzem em 60% a taxa de vulnerabilidades que chegam a produção.

**História.**  
Como **Revisor Técnico**, quero aplicar uma checklist de segurança em cada PR, para prevenir a entrada de vulnerabilidades no repositório.

**Critérios de aceitação (BDD).**
- Dado que abro um PR  
- Quando aplico a checklist formal  
- Então confirmo controlos críticos e registo evidência da revisão

**Checklist (binária, auditável).**
- [ ] `checklist-pr.md` marcado no PR  
- [ ] Itens críticos verificados  
- [ ] Comentários registados quando aplicável  
- [ ] Aprovação formal no histórico

**Artefactos & evidências.**
- Artefacto: `checklist-pr.md`  
- Evidência: histórico do PR e comentários de revisão

**Proporcionalidade por risco.**
| Nível | Obrigatório? | Ajustes |
|-------|--------------|---------|
| L1    | Sim          | Checklist básica |
| L2    | Sim          | Checklist completa + dupla revisão |
| L3    | Sim          | Revisão dedicada com foco em segurança |

**Integração no SDLC.**
| Fase            | Gatilho   | Responsável      | SLA          |
|-----------------|-----------|------------------|--------------|
| Revisão de Código| PR aberto| Revisor Técnico  | Antes do merge |

**Ligações úteis.**  
xref:sbd-toe:cap06:intro

---

### US-03 — Gestão de Dependências no Código {#us-03}

**Contexto.**  
Cada dependência externa adicionada ao projeto é uma potencial porta de entrada para riscos de cadeia de fornecimento. A gestão rigorosa destas dependências garante que não se introduz software obsoleto, vulnerável ou malicioso.

**📖 Rationale científico.**  
Relacionada com **SSDF PW.4**, **SAMM Implementation**, e **BSIMM CMVM1.1**.  
Mitiga riscos como **CWE-829 (Use of Untrusted Components)** e ataques de *dependency confusion*.  
Segundo o **Sonatype 2023 Supply Chain Report**, 1 em cada 10 pacotes descarregados contém uma vulnerabilidade crítica — prova da necessidade de validação formal e contínua.

**História.**  
Como **AppSec**, quero validar e justificar dependências externas, para reduzir riscos de supply chain e garantir compliance.

**Critérios de aceitação (BDD).**
- Dado que foi proposta uma nova dependência  
- Quando avalio licença, manutenção e CVEs associados  
- Então aprovo ou recuso com decisão registada

**Checklist (binária, auditável).**
- [ ] Dependência listada em `sbom-deps.json`  
- [ ] Licença compatível com política da organização  
- [ ] Sem CVEs críticos (ou exceção formal aprovada)  
- [ ] Decisão documentada em ticket

**Artefactos & evidências.**
- Artefacto: `sbom-deps.json`  
- Evidência: ticket de aprovação com justificativa

**Proporcionalidade por risco.**
| Nível | Obrigatório? | Ajustes |
|-------|--------------|---------|
| L1    | Sim          | Aprovação simplificada |
| L2    | Sim          | Aprovação formal + proveniência registada |
| L3    | Sim          | Política de pinning/lockfile obrigatório |

**Integração no SDLC.**
| Fase          | Gatilho             | Responsável        | SLA            |
|---------------|---------------------|--------------------|----------------|
| Desenvolvimento | Inclusão dependência | Dev + AppSec       | Antes do merge |

**Ligações úteis.**  
xref:sbd-toe:cap05:intro

---

### US-04 — Automatização em CI/CD (Linters & SAST) {#us-04}

**Contexto.**  
A automatização de validações em pipelines CI/CD garante consistência, acelera a deteção de falhas e cria evidência contínua. Automatizar significa **remover o fator humano de distração ou esquecimento** em controlos repetitivos.

**📖 Rationale científico.**  
Previsto em **DSOMM – Automation**, **SSDF RV.2** e **BSIMM SE3.3**.  
Mitiga riscos como **CWE-117 (Improper Logging)** e **CWE-693 (Protection Mechanism Failure)**.  
Relatórios da **ENISA** e do **DBIR** demonstram que equipas que integram SAST reduzem o tempo médio de deteção em 27%.

**História.**  
Como **DevSecOps**, quero integrar linters e SAST no pipeline, para detetar falhas precocemente e gerar evidência contínua.

**Critérios de aceitação (BDD).**
- Dado que o pipeline é executado  
- Quando correm linters e SAST  
- Então relatórios são arquivados e a build falha em findings críticos

**Checklist (binária, auditável).**
- [ ] Jobs configurados no pipeline  
- [ ] Thresholds de severidade definidos  
- [ ] Relatórios arquivados de forma imutável  
- [ ] Build falha em findings críticos

**Artefactos & evidências.**
- Artefacto: `ci/pipeline.yml`  
- Evidência: relatórios SARIF/JSON arquivados

**Proporcionalidade por risco.**
| Nível | Obrigatório? | Ajustes |
|-------|--------------|---------|
| L1    | Sim          | Linters básicos + SAST leve |
| L2    | Sim          | SAST completo + *gating* de severidade |
| L3    | Sim          | SAST + validações adicionais (IaC/DAST) |

**Integração no SDLC.**
| Fase | Gatilho           | Responsável | SLA       |
|------|-------------------|-------------|-----------|
| CI/CD| Execução pipeline | DevSecOps   | Cada build|

**Ligações úteis.**  
xref:sbd-toe:cap07:intro

---
### US-05 — Gestão de Exceções Técnicas {#us-05}

**Contexto.**  
Nem sempre todos os controlos podem ser aplicados em tempo útil. É inevitável lidar com exceções técnicas — mas se estas não forem **formalmente registadas, aprovadas e temporárias**, tornam-se dívida de risco e criam vulnerabilidades persistentes.

**📖 Rationale científico.**  
Baseado em **SSDF RV.1** (gestão de exceções), **SAMM Governance/Policy**, e **BSIMM CP1.2**.  
Mitiga riscos como **CAPEC-220 (Disabling Security Features)** e falhas de governação.  
Segundo o **DBIR 2023**, exceções mal geridas estão entre as principais causas de reincidência de vulnerabilidades críticas.

**História.**  
Como **AppSec**, quero registar e aprovar exceções técnicas, para garantir rastreabilidade, mitigação e revisão futura.

**Critérios de aceitação (BDD).**
- Dado que uma exceção é solicitada  
- Quando avalio justificação e mitigação propostas  
- Então aprovo ou recuso e defino prazo de validade

**Checklist (binária, auditável).**
- [ ] Exceção registada em `excecoes-seguranca.md`  
- [ ] Mitigação alternativa definida  
- [ ] Prazo de validade atribuído  
- [ ] Reavaliação agendada  

**Artefactos & evidências.**
- Artefacto: `excecoes-seguranca.md`  
- Evidência: aprovação formal em issue/PR

**Proporcionalidade por risco.**
| Nível | Obrigatório? | Ajustes |
|-------|--------------|---------|
| L1    | Sim          | Exceções simples e raras |
| L2    | Sim          | Revalidação por sprint |
| L3    | Sim          | Aprovação executiva + plano compensatório |

**Integração no SDLC.**
| Fase   | Gatilho          | Responsável     | SLA             |
|--------|------------------|-----------------|-----------------|
| Release| Exceção solicitada| AppSec + PO     | Antes do go-live|

**Ligações úteis.**  
xref:sbd-toe:cap02:intro

---

### US-06 — Uso Validado de GenIA {#us-06}

**Contexto.**  
Ferramentas de IA generativa (GenIA) aceleram a escrita de código, mas podem introduzir **vulnerabilidades ou violações de licença**. O seu uso deve ser rastreável, validado e sempre sujeito a revisão técnica humana.

**📖 Rationale científico.**  
Emergente em **NIST AI Risk Management Framework**, alinhado com **SSDF PO.2** (gestão de ferramentas) e princípios de **OWASP Top 10 for LLMs**.  
Mitiga riscos como **CWE-676 (Use of Potentially Dangerous Function)** e problemas de licenciamento.  
Segundo estudos da **Stanford 2023** e relatórios da **GitHub Copilot**, até 40% do código gerado por IA contém falhas de segurança quando não revisto.

**História.**  
Como **Desenvolvedor**, quero usar IA generativa com revisão obrigatória, para acelerar produtividade sem comprometer segurança.

**Critérios de aceitação (BDD).**
- Dado que gero código com GenIA  
- Quando anoto origem e submeto a revisão  
- Então só é aceite se cumprir guidelines e licenciamento

**Checklist (binária, auditável).**
- [ ] Uso registado em `uso-genia.md`  
- [ ] Revisão técnica aplicada  
- [ ] Conformidade de licença verificada  
- [ ] Evidência anexada ao PR  

**Artefactos & evidências.**
- Artefacto: `uso-genia.md`  
- Evidência: comentários de revisão + validações no PR

**Proporcionalidade por risco.**
| Nível | Obrigatório? | Ajustes |
|-------|--------------|---------|
| L1    | Opcional     | Registo simples |
| L2    | Sim          | Registo + revisão técnica |
| L3    | Sim          | Revisão formal + validações adicionais |

**Integração no SDLC.**
| Fase          | Gatilho  | Responsável        | SLA           |
|---------------|----------|--------------------|---------------|
| Desenvolvimento| Uso GenIA| Dev + Revisor Técnico| Antes do merge|

**Ligações úteis.**  
xref:sbd-toe:cap06:intro

---

### US-07 — Governação e Curadoria de Guidelines {#us-07}

**Contexto.**  
Sem governação ativa, guidelines estagnam e perdem relevância. A curadoria regular e a delegação de validação a linters com *rulesets* curados garantem adoção prática e atualizada.

**📖 Rationale científico.**  
Alinhado com **SAMM Governance**, **SSDF PS.2** (processo de revisão de requisitos) e **BSIMM CP1.1**.  
Mitiga riscos como **CWE-710 (Improper Adherence to Coding Standards)**.  
Segundo o **BSIMM13**, organizações que fazem curadoria trimestral de regras aumentam em média 2 níveis de maturidade.

**História.**  
Como **Gestor Técnico**, quero rever e publicar guidelines curadas periodicamente, para assegurar que estão atualizadas, versionadas e aprovadas.

**Critérios de aceitação (BDD).**
- Dado que existe nova stack ou revisão trimestral  
- Quando seleciono *rulesets* de referência e aplico *tailoring*  
- Então publico versão aprovada por AppSec

**Checklist (binária, auditável).**
- [ ] *Rulesets* avaliados e documentados  
- [ ] *Tailoring* aprovado por AppSec  
- [ ] Configurações versionadas em `rules/`  
- [ ] Release/tag publicada com changelog  
- [ ] Mapeamento ASVS/CWE atualizado  

**Artefactos & evidências.**
- Artefacto: diretório `rules/`  
- Evidência: release/tag + changelog

**Proporcionalidade por risco.**
| Nível | Obrigatório? | Ajustes |
|-------|--------------|---------|
| L1    | Opcional     | Uso de regras upstream *default* |
| L2    | Sim          | Curadoria organizacional obrigatória |
| L3    | Sim          | *Policy-as-code* + distribuição controlada |

**Integração no SDLC.**
| Fase      | Gatilho             | Responsável           | SLA     |
|-----------|---------------------|-----------------------|---------|
| Governação| Nova stack ou revisão| Gestor Técnico + AppSec| Até 2 sem.|

**Ligações úteis.**  
xref:sbd-toe:cap06:intro

---

### US-08 — Rastreabilidade com Anotações de Segurança {#us-08}

**Contexto.**  
Validações de segurança devem ser rastreáveis até aos requisitos originais. Anotações padronizadas (`@sec:*`) no código e nos testes permitem **ligar implementação, requisitos e evidência de auditoria** de forma inequívoca.

**📖 Rationale científico.**  
Alinhado com **SSDF RV.2** (capture evidence), **BSIMM SE2.4**, e práticas de **DSOMM – Evidence**.  
Mitiga riscos como **CWE-1059 (Incomplete Documentation of Data Flow)** e falhas em auditorias.  
Segundo o **DBIR 2023**, a ausência de rastreabilidade aumenta em 40% o tempo médio de resposta a incidentes.

**História.**  
Como **Desenvolvedor**, quero anotar validações de segurança com `@sec:*`, para garantir rastreabilidade ponta-a-ponta até ao backlog.

**Critérios de aceitação (BDD).**
- Dado que implemento requisito de segurança  
- Quando adiciono anotação `@sec:*`  
- Então o requisito fica rastreável até ao backlog e relatórios de CI/CD

**Checklist (binária, auditável).**
- [ ] Anotações incluídas em código/testes  
- [ ] Referência cruzada a requisitos (`SEC-*`)  
- [ ] Relatórios exportam anotações  
- [ ] Evidência arquivada  

**Artefactos & evidências.**
- Artefacto: código comentado, testes anotados  
- Evidência: relatórios de CI/CD

**Proporcionalidade por risco.**
| Nível | Obrigatório? | Ajustes |
|-------|--------------|---------|
| L1    | Opcional     | Apenas em módulos críticos |
| L2    | Sim          | Todas as validações de segurança |
| L3    | Sim          | Anotações + validação automática |

**Integração no SDLC.**
| Fase              | Gatilho                | Responsável | SLA        |
|-------------------|------------------------|-------------|------------|
| Desenvolvimento   | Implementação de requisito | Dev + QA   | Até ao merge|

**Ligações úteis.**  
xref:sbd-toe:cap06:intro

---
## 📦 Artefactos esperados {desenvolvimento-seguro:aplicacao-lifecycle#artefactos}

A aplicação prática do desenvolvimento seguro deixa sempre **pegadas objetivas** — ficheiros, relatórios e registos que podem ser auditados.  
Sem evidência, não existe conformidade. Esta tabela resume os principais artefactos esperados:

| Artefacto               | Evidência auditável                                                |
|--------------------------|--------------------------------------------------------------------|
| `guidelines-stack.md`    | Regras de codificação segura por stack, com *mapping* para ASVS/CWE|
| `rules/` versionado      | Configurações partilhadas de linters/SAST (`.eslintrc.*`, `.semgrep.yml`), com release/tag e changelog |
| Pacote `@org/eslint-sec` | *Shareable config* interno (ex.: NPM/Artifactory) com controlo de versões |
| `checklist-pr.md`        | Checklist formal preenchida e arquivada em PRs                    |
| `sbom-deps.json`         | Lista de dependências externas com validação formal               |
| Relatórios SAST/linters  | Saídas automatizadas (SARIF/JSON) arquivadas no pipeline           |
| `excecoes-seguranca.md`  | Registo formal de exceções técnicas aprovadas e prazos definidos  |
| `uso-genia.md`           | Registo de utilização de GenIA, revisão associada e decisão de aceitação |

---

## ⚖️ Matriz de proporcionalidade L1–L3 {desenvolvimento-seguro:aplicacao-lifecycle#matriz}

Nem todas as aplicações exigem o mesmo grau de controlo.  
A matriz abaixo traduz a lógica de proporcionalidade: **quanto maior o risco (L3), mais rigor na aplicação e governação**.

| Prática                    | L1 (baixo)             | L2 (médio)                   | L3 (alto/crítico)                       |
|-----------------------------|------------------------|------------------------------|-----------------------------------------|
| Guidelines de código        | Mínimas, upstream      | Curadas por stack            | Auditadas + *policy-as-code*            |
| Revisão de código           | Checklist básica       | Checklist completa           | Revisor dedicado com foco em segurança  |
| Gestão de dependências      | Justificação simples   | Validação formal             | Validação + SBOM rastreável             |
| Automatização CI/CD         | Linters básicos        | SAST obrigatório             | SAST + validações adicionais (IaC/DAST) |
| Gestão de exceções          | Registo simples        | Revisão obrigatória          | Dupla aprovação + prazo curto           |
| Uso de GenIA                | Registo opcional       | Revisão obrigatória          | Revisão formal + validação de licenças  |
| Governação de guidelines    | Regras *default*       | Curadoria organizacional     | Revisão periódica + distribuição controlada |

---

## 🏁 Recomendações finais {desenvolvimento-seguro:aplicacao-lifecycle#recomendacoes}

O desenvolvimento seguro deve ser visto como **um hábito quotidiano**, não como um esforço extraordinário.  
As práticas tornam-se naturais quando estão integradas no fluxo de trabalho e apoiadas por governação clara.  

- **Versionar e publicar guidelines** como artefactos formais (com releases e changelogs), não como “notas avulsas”.  
- **Automatizar ao máximo** — linters, SAST e scanners eliminam variações manuais e produzem evidência contínua.  
- **Exceções são a exceção**: devem ser raras, temporárias e sempre justificadas.  
- **GenIA pode ser usada**, mas sob registo e revisão técnica, nunca como substituto de disciplina humana.  
- **KPIs de adoção** devem ser medidos: % de PRs com checklist aplicada, % de dependências validadas, % de findings resolvidos no SLA.  
- **Revisão periódica** das práticas garante que regras não se tornam obsoletas.  

Em síntese: o capítulo demonstra que **desenvolvimento seguro é a fundação sobre a qual o resto do ciclo de vida assenta**.  
Sem ele, nenhuma prática subsequente — seja CI/CD, IaC ou runtime — consegue oferecer confiança total.
