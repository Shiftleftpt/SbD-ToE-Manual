---
id: aplicacao-lifecycle
title: Aplicação de Desenvolvimento Seguro no Ciclo de Vida
description: Como aplicar práticas de desenvolvimento seguro em cada fase do SDLC, com user stories reutilizáveis, artefactos auditáveis e matriz proporcional L1–L3
tags: [tipo:aplicacao, ciclo-vida, desenvolvimento, codificacao-segura, validacao, user-stories]
genia: us-format-normalization
---

# ⚙️ Aplicação no Ciclo de Vida - Desenvolvimento Seguro

O desenvolvimento seguro não é um exercício teórico nem uma “boa prática” vaga: exige aplicação consistente em cada fase do ciclo de vida do software.  
Neste documento mostramos **como transformar as prescrições do capítulo em prática diária**, detalhando quando aplicar, quem executa, que user stories devem entrar no backlog e quais as evidências que permitem auditoria e governação.  
O objetivo é simples mas ambicioso: fazer do desenvolvimento seguro um hábito mensurável, rastreável e parte intrínseca da qualidade do produto.

---

## 🧭 Quando aplicar

A segurança acompanha o projeto desde o início e não pode ser relegada para fases finais.  
O quadro seguinte mostra **em que momentos concretos do SDLC** cada prática deve ser aplicada e qual a ação esperada em cada um deles.

| Fase do SDLC          | Momento específico                          | Ação esperada                                       |
|-----------------------|----------------------------------------------|-----------------------------------------------------|
| Planeamento           | Definição de stack, dependências, guidelines | Criar/adaptar guidelines seguras                    |
| Desenvolvimento       | Ao escrever/refatorar código                 | Aplicar linters, validações locais                  |
| Revisão de Código     | Em cada PR / merge                           | Checklist e validação formal                        |
| Integração Contínua   | Execução do pipeline                         | SAST, validação de dependências e *rulesets*        |
| Pré-produção          | Go-live / release                            | Validação de exceções, checklist final              |
| Operação / Manutenção | Atualizações, patches, refatorizações        | Revisão de guidelines, dependências e exceções      |

---

## 🧱 Gates de desenvolvimento seguro (proposto → revisto → validado → aceite)

Para escalar em frequência de entrega e diversidade de contribuições, o desenvolvimento seguro não pode depender de “confiança” na origem do código.  
O SbD-ToE assume que **todo o código é entrada não confiável** até existir validação suficiente e evidência verificável.

Por isso, a aceitação de código deve ser tratada como um processo com estados explícitos:

- **Proposto**: mudança criada, ainda não compreendida nem validada (risco máximo).  
- **Revisto**: entendimento técnico humano confirmado (risco reduzido).  
- **Validado**: validação empírica concluída (testes + validações automáticas relevantes).  
- **Aceite**: decisão explícita de incorporação, atribuída a role identificável, com evidência registada.

Estes estados não são “burocracia”; são mecanismos práticos para reduzir o risco introduzido pelo processo de desenvolvimento.

| Gate | Estado de entrada | Ação obrigatória | Evidência mínima | Role responsável |
|-----|-------------------|------------------|------------------|------------------|
| G1 | Proposto | Revisão humana estruturada com checklist | Aprovação registada no PR + checklist | **Scrum Master / Team Lead** (com execução por **Developer** / **Quality Assurance (QA)**) |
| G2 | Revisto | Validação técnica automatizada | Relatórios CI/CD + logs + testes | **DevOps / SRE** + **Developer** |
| G3 | Validado | Decisão final de aceitação | Aprovação final + referência a exceções | **Scrum Master / Team Lead** (L1) · **AppSec Engineer** (L2/L3) · **Gestão Executiva** (L3 quando aplicável) |

> Falhar um gate implica correção ou rejeição.  
> Um PR não deve ser “aceite” sem atravessar G1–G3 com evidência.

---

## 👥 Quem executa cada ação

A segurança no desenvolvimento é um **esforço coletivo**: diferentes papéis contribuem de forma complementar, formando uma cadeia de confiança.  
A tabela seguinte explicita estas responsabilidades, usando **apenas os roles definidos no SbD-ToE**.

| Role (SbD-ToE) | Responsabilidades principais |
|---|---|
| **Developer** | Aplicar guidelines, linters e validações locais; registar desvios e propor *tailoring* quando necessário |
| **Quality Assurance (QA)** | Validar critérios de qualidade e segurança em PRs; confirmar critérios e exceções; suportar evidência e rastreabilidade |
| **Scrum Master / Team Lead** | Garantir execução de G1/G3; confirmar checklists; assegurar integração no ciclo ágil; bloquear merges sem evidência |
| **DevOps / SRE** | Automatizar linters/SAST; versionar e distribuir *rulesets* organizacionais; aplicar enforcement e *quality gates* em pipelines |
| **AppSec Engineer** | Definir critérios mínimos; aprovar exceções; validar dependências críticas; mapear requisitos e findings a OWASP/ASVS/CWE; definir perfis L1–L3 |
| **Arquitetos de Software** | Definir padrões por stack, decisões estruturais e guidelines base; aprovar curadoria técnica de guidelines/rulesets; assegurar consistência arquitetural |
| **Product Owner (PO)** | Priorizar trabalho (incluindo dívida e exceções); assegurar que requisitos de segurança entram no backlog e são aceites com critérios objetivos |

> Nota: ferramentas podem apoiar e automatizar, mas **não assumem responsabilidade**.  
> A responsabilidade de aceitar código é sempre atribuída a roles humanos identificáveis.

---

## 📖 User Stories reutilizáveis

### US-01 - Guidelines de Desenvolvimento Seguro

**Contexto.**  
Guidelines claras e versionadas por *stack* evitam decisões ad-hoc e asseguram consistência. Mais do que um documento estático, são um **mecanismo vivo** de governação: atualizadas, revistas e aplicadas diariamente. A existência de *rulesets* derivadas de linters e analisadores automáticos, com *tailoring* documentado, reduz significativamente riscos de interpretação subjetiva.

:::userstory
**História.**   
Como **Developer**, quero aplicar as guidelines de código seguro aprovadas, para garantir consistência e reduzir vulnerabilidades desde o início.

**Critérios de aceitação (BDD).**
- **Dado** que inicio desenvolvimento numa *stack* definida  
  **Quando** consulto as guidelines aprovadas  
  **Então** aplico as regras mínimas obrigatórias e registo qualquer desvio justificado

**Checklist.**
- [ ] `guidelines-stack.md` referenciado no README do projeto  
- [ ] Ficheiros de configuração de linters/analisadores presentes e versionados  
- [ ] Regras mínimas aplicadas  
- [ ] *Tailoring* documentado (`rules/README.md`) e aprovado (por **Arquitetos de Software** / **AppSec Engineer** conforme aplicável)  
- [ ] Desvios registados em `excecoes-seguranca.md`  
- [ ] Evidência de revisão do PR
:::

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
| Fase        | Trigger            | Responsável                                   | SLA              |
|-------------|--------------------|-----------------------------------------------|------------------|
| Planeamento | Definição de stack | **Arquitetos de Software** + **Developer**    | Antes do 1.º sprint |

**Ligações úteis.**  
[Desenvolvimento Seguro](/sbd-toe/sbd-manual/desenvolvimento-seguro)

---

### US-02 - Revisão de Código Segura

**Contexto.**  
Revisões de código não são apenas uma prática de qualidade, mas um **ponto de controlo de segurança**. Quando sistematizadas com checklist, previnem vulnerabilidades, promovem partilha de conhecimento e criam registo formal de conformidade.

:::userstory
**História.**   
Como **Scrum Master / Team Lead**, quero garantir que cada PR é revisto com checklist de segurança obrigatória, para prevenir vulnerabilidades e manter registo de conformidade.

*(Executa: **Developer** / **Quality Assurance (QA)** com governação do **Scrum Master / Team Lead**)*

**Critérios de aceitação (BDD).**
- **Dado** que um PR é criado  
  **Quando** é submetido à revisão  
  **Então** a checklist de segurança é preenchida e o PR apenas é aceite após validação

**Checklist.**
- [ ] `checklist-pr.md` incluído no **template de PR**  
- [ ] Itens críticos validados (autenticação, entradas, dependências)  
- [ ] Comentários de segurança registados quando aplicável  
- [ ] **PR rejeitado automaticamente se checklist não estiver completa**  
- [ ] O PR só progride quando existe aprovação humana registada (estado “revisto”)
:::

**Artefactos & evidências.**  
`checklist-pr.md` (PR template), histórico e comentários no PR

**Proporcionalidade por risco.**
| Nível | Obrigatório? | Ajustes |
|-------|--------------|---------|
| L1    | Sim          | Checklist básica |
| L2    | Sim          | Checklist completa + dupla revisão |
| L3    | Sim          | Revisão dedicada com foco em segurança (inclui **AppSec Engineer** quando aplicável) |

**Integração no SDLC.**
| Fase              | Trigger  | Responsável                                                     | SLA          |
|-------------------|----------|------------------------------------------------------------------|--------------|
| Revisão de Código | PR aberto | **Developer** / **Quality Assurance (QA)** + **Scrum Master / Team Lead** | Antes do merge |

---

### US-03 - Gestão de Dependências no Código

**Contexto.**  
Cada dependência externa adicionada ao projeto é uma potencial porta de entrada para riscos de cadeia de fornecimento. A gestão rigorosa destas dependências garante que não se introduz software obsoleto, vulnerável ou malicioso.

:::userstory
**História.**   
Como **AppSec Engineer**, quero validar e justificar dependências externas, para reduzir riscos de supply chain e garantir compliance.

**Critérios de aceitação (BDD).**
- **Dado** que foi proposta uma nova dependência  
  **Quando** avalio licença, manutenção e CVEs associados  
  **Então** aprovo ou recuso com decisão registada

**Checklist.**
- [ ] Dependência listada em `sbom-deps.json`  
- [ ] Licença compatível com política da organização  
- [ ] Sem CVEs críticos (ou exceção formal aprovada)  
- [ ] Decisão documentada em ticket
:::

**Artefactos & evidências.**
- Artefacto: `sbom-deps.json`  
- Evidência: ticket de aprovação com justificação

**Proporcionalidade por risco.**
| Nível | Obrigatório? | Ajustes |
|-------|--------------|---------|
| L1    | Sim          | Aprovação simplificada |
| L2    | Sim          | Aprovação formal + proveniência registada |
| L3    | Sim          | Política de pinning/lockfile obrigatório |

**Integração no SDLC.**
| Fase            | Trigger              | Responsável                         | SLA            |
|-----------------|----------------------|-------------------------------------|----------------|
| Desenvolvimento | Inclusão dependência | **Developer** + **AppSec Engineer** | Antes do merge |

**Nota - cruza com outras práticas**  
Esta user story cruza com práticas como [Dependências, SBOM e SCA](/sbd-toe/sbd-manual/dependencias-sbom-sca) e, de certa forma, permite a monitorização de *drift* como indicado em [Monitorização & Operações](/sbd-toe/sbd-manual/monitorizacao-operacoes).

---

### US-04 - Automatização em CI/CD (Linters & SAST)

**Contexto.**  
A automatização de validações em pipelines CI/CD garante consistência, acelera a deteção de falhas e cria evidência contínua. Automatizar significa **remover o fator humano de distração ou esquecimento** em controlos repetitivos.

:::userstory
**História.**   
Como **DevOps / SRE**, quero integrar linters e SAST no pipeline, para detetar falhas precocemente e gerar evidência contínua.

**Critérios de aceitação (BDD).**
- **Dado** que o pipeline é executado  
  **Quando** correm linters e SAST  
  **Então** relatórios são arquivados e a build falha em findings críticos

**Checklist.**
- [ ] Jobs configurados no pipeline  
- [ ] Limiares (*thresholds*) de severidade definidos  
- [ ] Relatórios arquivados de forma imutável  
- [ ] Build falha em findings críticos  
- [ ] O PR só progride para “validado” quando G2 é satisfeito (evidência CI/CD)
:::

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
| Fase | Trigger            | Responsável       | SLA        |
|------|--------------------|-------------------|------------|
| CI/CD| Execução pipeline  | **DevOps / SRE**  | Cada build |

**Ligações úteis.**  
[CI/CD Seguro](/sbd-toe/sbd-manual/cicd-seguro)

---

### US-05 - Gestão de Exceções Técnicas

**Contexto.**  
Nem sempre todos os controlos podem ser aplicados em tempo útil. É inevitável lidar com exceções técnicas — mas se estas não forem **formalmente registadas, aprovadas e temporárias**, tornam-se dívida de risco e criam vulnerabilidades persistentes.

:::userstory
**História.**   
Como **AppSec Engineer**, quero registar e aprovar exceções técnicas, para garantir rastreabilidade, mitigação e revisão futura.

**Critérios de aceitação (BDD).**
- **Dado** que uma exceção é solicitada  
  **Quando** avalio justificação e mitigação propostas  
  **Então** aprovo ou recuso e defino prazo de validade

**Checklist.**
- [ ] Exceção registada em `excecoes-seguranca.md`  
- [ ] Mitigação alternativa definida  
- [ ] Prazo de validade atribuído  
- [ ] Reavaliação agendada
:::

**Artefactos & evidências.**
- Artefacto: `excecoes-seguranca.md`  
- Evidência: aprovação formal em issue/PR

> **Referência:** Este US implementa [Cap 14-US-01: Processo formal de exceções]  
> no contexto de desenvolvimento seguro. Todas as exceções técnicas devem ser geridas conforme a política master de exceções em Cap 14, incluindo TTL e revalidação periódica.

**Proporcionalidade por risco.**
| Nível | Obrigatório? | Ajustes |
|-------|--------------|---------|
| L1    | Sim          | Exceções simples e raras |
| L2    | Sim          | Revalidação por sprint |
| L3    | Sim          | Aprovação executiva + plano compensatório |

**Integração no SDLC.**
| Fase    | Trigger            | Responsável                                  | SLA              |
|---------|--------------------|-----------------------------------------------|------------------|
| Release | Exceção solicitada | **AppSec Engineer** + **Product Owner (PO)** | Antes do go-live |

**Ligações úteis.**  
[Requisitos de Segurança](/sbd-toe/sbd-manual/requisitos-seguranca)

---

### US-06 - Uso Validado de GenIA

**Contexto.**  
Ferramentas de IA generativa (GenIA) aceleram a escrita de código, mas podem introduzir **vulnerabilidades, violações de licença e desalinhamento com regras técnicas obrigatórias**.  
O seu uso deve ser rastreável, validado e sempre sujeito a revisão técnica humana.

:::userstory
**História.**   
Como **Developer**, quero usar IA generativa com revisão obrigatória e constrangimentos técnicos explícitos, para acelerar produtividade sem comprometer segurança.

**Critérios de aceitação (BDD).**
- **Dado** que gero código com GenIA  
  **Quando** registo o uso e submeto a revisão  
  **Então** só é aceite se cumprir guidelines, constrangimentos técnicos do projeto e licenciamento
- E o PR não progride sem evidência de revisão humana (G1) e validação (G2)

**Checklist.**
- [ ] Uso registado em `uso-genia.md`  
- [ ] Constrangimentos técnicos versionados e aplicáveis ao projeto (`constrangimentos-dev.md`)  
- [ ] Revisão técnica aplicada (por **Developer** / **Quality Assurance (QA)**, com escalonamento a **AppSec Engineer** quando aplicável)  
- [ ] Conformidade de licença verificada  
- [ ] Evidência anexada ao PR (inclui ligações a validações e ao constrangimento relevante)
:::

**Artefactos & evidências.**
- Artefactos: `uso-genia.md`, `constrangimentos-dev.md`  
- Evidência: comentários de revisão + validações no PR

**Proporcionalidade por risco.**
| Nível | Obrigatório? | Ajustes |
|-------|--------------|---------|
| L1    | Opcional     | Registo simples |
| L2    | Sim          | Registo + revisão técnica + constrangimentos obrigatórios |
| L3    | Sim          | Revisão formal + validações adicionais + evidência reforçada |

**Integração no SDLC.**
| Fase            | Trigger   | Responsável                         | SLA           |
|-----------------|-----------|--------------------------------------|---------------|
| Desenvolvimento | Uso GenIA  | **Developer** + **Quality Assurance (QA)** | Antes do merge |

**Ligações úteis.**  
[Desenvolvimento Seguro](/sbd-toe/sbd-manual/desenvolvimento-seguro)

---

### US-07 - Governação e Curadoria de Guidelines

**Contexto.**  
A governação ativa das guidelines assegura que estas evoluem com as tecnologias e com as vulnerabilidades emergentes.  
A publicação formal e a revisão periódica são mecanismos de controlo e conformidade.

:::userstory
**História.**  
Como **AppSec Engineer**, quero rever e publicar guidelines curadas trimestralmente, para garantir atualização contínua e governação formal das práticas de desenvolvimento seguro.

**Critérios de aceitação (BDD).**
- **Dado** que decorre o ciclo de revisão ou surge nova *stack*  
  **Quando** as *rulesets* são atualizadas  
  **Então** é publicada uma **release/tag** aprovada por **Arquitetos de Software** e **AppSec Engineer** (e, quando aplicável, operacionalizada por **DevOps / SRE**)

**Checklist.**
- [ ] *Rulesets* avaliados e documentados  
- [ ] *Tailoring* validado  
- [ ] Configurações versionadas e publicadas  
- [ ] Changelog incluído na release  
- [ ] Revisão periódica registada  
- [ ] Mapeamento atualizado para ASVS/CWE
:::

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
| Fase       | Trigger               | Responsável                                                     | SLA       |
|------------|-----------------------|------------------------------------------------------------------|-----------|
| Governação | Nova stack ou revisão | **Arquitetos de Software** + **AppSec Engineer** + **DevOps / SRE** | Até 2 sem. |

---

### US-08 - Rastreabilidade com Anotações de Segurança

**Contexto.**  
Validações de segurança devem ser rastreáveis até aos requisitos originais. Anotações padronizadas (`@sec:*`) no código e nos testes permitem **ligar implementação, requisitos e evidência de auditoria** de forma inequívoca.

:::userstory
**História.**   
Como **Developer**, quero anotar validações de segurança com `@sec:*`, para garantir rastreabilidade ponta-a-ponta até ao backlog.

**Critérios de aceitação (BDD).**
- **Dado** que implemento requisito de segurança  
  **Quando** adiciono anotação `@sec:*`  
  **Então** o requisito fica rastreável até ao backlog e relatórios de CI/CD

**Checklist.**
- [ ] Anotações incluídas em código/testes  
- [ ] Referência cruzada a requisitos (`SEC-*`)  
- [ ] Relatórios exportam anotações  
- [ ] Evidência arquivada
:::

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
| Fase            | Trigger                    | Responsável                         | SLA        |
|-----------------|----------------------------|--------------------------------------|------------|
| Desenvolvimento | Implementação de requisito | **Developer** + **Quality Assurance (QA)** | Até ao merge |

---

### US-09 - Gate de Segurança Pré-release

**Contexto.**  
Antes de cada *release* deve existir um ponto de controlo objetivo que consolide todas as evidências de segurança — relatórios SAST, SBOM, exceções, checklists e aprovações.

:::userstory
**História.**  
Como **DevOps / SRE**, quero executar um **gate de segurança pré-release** que agregue todas as evidências de validação, para só permitir publicações conformes com os requisitos de segurança.

**Critérios de aceitação (BDD).**
- **Dado** que existe uma *release* candidata  
- E o nível de risco L1–L3 foi atribuído  
  **Quando** o *security gate* é executado  
  **Então** o resultado é binário (Aprovado/Rejeitado) e é registado como artefacto da release

**Checklist.**
- [ ] *Job* `release-security-gate` configurado no pipeline  
- [ ] Relatório agregado anexado à *tag/release*  
- [ ] Ligações a SAST, SBOM, exceções e checklist de PR  
- [ ] Bloqueio automático em caso de falha  
- [ ] Aprovação final por **AppSec Engineer** (e, em L3 quando aplicável, por **Gestão Executiva**)
:::

**Artefactos & evidências.** `gate-relatorio.md`, anexos CI/CD, *tag/release* assinada

**Proporcionalidade.**
| Nível | Obrigatório? | Ajustes |
|-------|---------------|---------|
| L1 | Sim | Gate básico (SAST + SBOM + checklist) |
| L2 | Sim | Gate reforçado com política de exceções |
| L3 | Sim | *Policy-as-code* e dupla aprovação formal |

---

### US-10 - Perfis de Validação por Nível de Risco (L1–L3)

**Contexto.**  
A aplicação proporcional dos controlos é essencial para garantir eficiência e consistência.  
Cada aplicação deve herdar um perfil técnico de validação compatível com a sua classificação de risco.

:::userstory
**História.**  
Como **AppSec Engineer**, quero definir e aplicar **perfis de validação L1–L3** que determinem regras, limiares e *quality gates* adequados ao risco, para uniformizar a execução e auditoria.

**Critérios de aceitação (BDD).**
- **Dado** que a aplicação tem classificação L1/L2/L3  
  **Quando** é executado o pipeline  
  **Então** são aplicadas as regras e limiares correspondentes ao perfil definido

**Checklist.**
- [ ] Perfis L1–L3 documentados e aprovados  
- [ ] *Rulesets* correspondentes no pipeline  
- [ ] Métricas de severidade e cobertura definidas  
- [ ] Gates G1–G3 parametrizados por perfil (thresholds e exceções)  
- [ ] Auditoria trimestral aos perfis e thresholds
:::

**Artefactos & evidências.** `matriz-proporcionalidade-dev.md`, `ci/pipeline.yml`, relatórios de auditoria

**Proporcionalidade.**
| Nível | Obrigatório? | Ajustes |
|-------|---------------|---------|
| L1 | Sim | Perfil com linters + SAST leve + checklist básica |
| L2 | Sim | Perfil com SAST completo + thresholds + dupla revisão quando aplicável |
| L3 | Sim | Perfil com *policy-as-code* + gates reforçados + retenção auditável |

---

### US-11 - Arquivo Central de Evidências de Validação

**Contexto.**  
A retenção controlada de evidências é requisito de auditoria e conformidade.  
As provas de execução dos controlos devem ser exportadas e arquivadas de forma segura, imutável e auditável.

:::userstory
**História.**  
Como **Quality Assurance (QA)** e **DevOps / SRE**, quero **arquivar centralmente todas as evidências de validação** (relatórios SAST, SBOM, exceções, `@sec:*`), para garantir rastreabilidade e cumprimento de requisitos de auditoria.

**Critérios de aceitação (BDD).**
- **Dado** que o pipeline executa validações  
  **Quando** conclui a execução  
  **Então** exporta e arquiva relatórios e evidências num repositório controlado e versionado

**Checklist.**
- [ ] Repositório de evidências definido (preferencialmente WORM)  
- [ ] Export automático por *build/release*  
- [ ] Índice de evidências por aplicação e *commit*  
- [ ] Política de retenção definida (≥ 2 anos; L3 ≥ 5 anos)  
- [ ] Acesso auditado e controlado
:::

**Artefactos & evidências.**  
diretório `evidencias/`, `evidencias-index.json`, registos de acesso

**Proporcionalidade.**
| Nível | Obrigatório? | Ajustes |
|-------|---------------|---------|
| L1 | Sim | Retenção mínima e export básico |
| L2 | Sim | Export assinado + índice por componente |
| L3 | Sim | Armazenamento imutável e verificação periódica de integridade |

---

### US-12 - Validações Locais Obrigatórias (Pre-commit)

**Contexto.**  
Validações executadas localmente antes de qualquer push reduzem ciclos de feedback, aumentam consistência de código e diminuem carga no pipeline. Git hooks e linters locais são a primeira linha de defesa.

:::userstory
**História.**  
Como **Developer**, quero executar **linters e validações de segurança localmente** antes de fazer commit, para detetar erros triviais e vulnerabilidades facilmente corrigíveis sem depender do pipeline CI/CD.

**Critérios de aceitação (BDD).**
- **Dado** que uso um IDE ou terminal no projeto  
  **Quando** executo `make lint` ou hook pre-commit (automático)  
  **Então** recebo feedback imediato de erros de linting e vulnerabilidades detetáveis localmente  
- E falhas críticas bloqueiam o commit

**Checklist.**
- [ ] Git hooks configurados (`.husky/pre-commit` ou `.git/hooks/`)  
- [ ] Targets `make lint` e `make check-security` funcionais  
- [ ] Regras mínimas locais alinhadas com CI/CD  
- [ ] Falhas críticas bloqueiam commit; avisos permitem *bypass* com flag  
- [ ] Documentação em `README.md` com comandos de setup e uso  
- [ ] *Bypass* seguro (`SKIP_HOOKS=1`) disponível com rastreabilidade
:::

**Artefactos & evidências.**
- Artefatos: `.husky/pre-commit`, `Makefile` (targets `lint`, `check-security`), `.eslintrc.json` (ou equivalente por stack)  
- Evidência: logs de execução pre-commit em histórico de commits, output em PR

**Proporcionalidade.**
| Nível | Obrigatório? | Ajustes |
|-------|---------------|---------|
| L1 | Recomendado | Linters básicos (style, typos) |
| L2 | Sim | Linters obrigatórios + *secrets scanning* |
| L3 | Sim | Pre-commit + SAST leve local + validação de padrões |

**Integração no SDLC.**
| Fase       | Trigger           | Responsável   | SLA |
|------------|-------------------|---------------|-----|
| Dev (Local)| Preparação commit | **Developer** | Imediato (execução local) |

**Ligações úteis.**
- US-01 (Guidelines de Desenvolvimento)
- US-04 (Automatização em CI/CD)
- Cap. 06, addon 02 (Linters e Validações)

---

### US-13 - Validação de Padrões Perigosos e Anti-patterns

**Contexto.**  
Padrões de código inseguro (eval, concatenação SQL, *hardcoded secrets*, XSS, etc.) devem ser detetados automaticamente e bloqueados, com educação sobre alternativas seguras.

:::userstory
**História.**  
Como **AppSec Engineer**, quero que o pipeline **detete automaticamente padrões perigosos** (eval, innerHTML sem sanitização, concatenação SQL, secrets, etc.) e bloqueie a build, com mensagem educativa e ligação para corrigir.

**Critérios de aceitação (BDD).**
- **Dado** que um PR introduz um padrão de código perigoso  
  **Quando** SAST/linters/semgrep executam  
  **Então** a build falha com mensagem explicativa, referência a CWE e alternativa segura  
- E o encontro é registado para mensuração de tendências

**Checklist.**
- [ ] Regras SAST/Semgrep configuradas para padrões perigosos por stack (Python, JS, Java, etc.)  
- [ ] Mensagens de erro educativas com exemplos inseguro vs. seguro  
- [ ] Referência cruzada com Cap. 06, addon 01 (Boas Práticas) e com OWASP/CWE  
- [ ] Escala de severidade clara: **critical** (eval, exec), **high** (SQL concat, XSS), **medium** (hardcoded secrets)  
- [ ] Template em PR com "Como corrigir este padrão" por categoria  
- [ ] Métricas de deteções e resoluções reportadas em dashboard
:::

**Artefactos & evidências.**
- Artefatos: `.semgrep.yml`, `sonar-project.properties`, regras SAST (SonarQube, Checkmarx, Snyk)  
- Evidência: relatórios do PR com findings + educação, histórico de resoluções

**Proporcionalidade.**
| Nível | Obrigatório? | Ajustes |
|-------|---------------|---------|
| L1 | Sim | Deteção de padrões **críticos** apenas (eval, exec) |
| L2 | Sim | Deteção expandida (**críticos** + **high**: SQL, XSS) |
| L3 | Sim | Deteção completa + contexto e reforço educativo |

**Integração no SDLC.**
| Fase              | Trigger                  | Responsável                         | SLA |
|-------------------|--------------------------|--------------------------------------|-----|
| CI/CD (Analysis)  | PR aberto ou commit em dev | **DevOps / SRE** + **AppSec Engineer** | Cada build (~5–10 min) |

**Ligações úteis.**
- US-01, addon 01 (Boas Práticas de Código)
- US-04 (Automatização em CI/CD)
- US-08 (Anotações para Rastreabilidade)
- Cap. 06, addon 01 (Boas Práticas)

---

### US-14 - Monitorização de Conformidade e Métricas de Segurança

**Contexto.**  
Métricas contínuas de segurança (cobertura de linters, exceções ativas, findings resolvidos, compliance L1–L3) permitem governação informada e identificação rápida de desvios.

:::userstory
**História.**  
Como **Scrum Master / Team Lead** e **AppSec Engineer**, quero **visualizar dashboard de métricas de segurança** (cobertura SAST, exceções ativas/expiradas, findings resolvidos, compliance por nível L1–L3) para decisão informada e ação corretiva rápida.

**Critérios de aceitação (BDD).**
- **Dado** que decorrem múltiplas releases e sprints  
  **Quando** acedo ao dashboard de conformidade  
  **Então** visualizo: trend de compliance, exceções pendentes, ações recomendadas  
- E recebo alertas automáticos para desvios críticos (ex: exceção expirada sem reavaliação)

**Checklist.**
- [ ] Dashboard centralizado (ex: Grafana, Kibana, painel interno) com dados de Cap. 06  
- [ ] Métricas-chave: cobertura SAST, exceções ativas/expiradas, findings resolvidos, compliance L1–L3  
- [ ] Agregação por aplicação, stack, nível de risco e sprint  
- [ ] Alertas automáticos para desvios (ex: exceção expirada, queda de compliance)  
- [ ] Export mensal/trimestral para auditoria interna e regulatória  
- [ ] Ligação com US-11 (Arquivo de Evidências) para rastreabilidade completa
:::

**Artefactos & evidências.**
- Artefatos: Configs dashboard (Grafana JSON, queries Elasticsearch), scripts de agregação  
- Evidência: capturas mensais/trimestrais de dashboard, relatórios de tendência, alertas gerados

**Proporcionalidade.**
| Nível | Obrigatório? | Ajustes |
|-------|---------------|---------|
| L1 | Recomendado | Métricas básicas (cobertura SAST, exceções) |
| L2 | Sim | Dashboard com alertas para desvios |
| L3 | Sim | Dashboard contínuo + auditoria automática + SLA de remediação |

**Integração no SDLC.**
| Fase                     | Trigger                     | Responsável                                              | SLA |
|--------------------------|-----------------------------|----------------------------------------------------------|-----|
| Governação (Trimestral +)| Conforme procura / agenda   | **AppSec Engineer** + **DevOps / SRE** + **GRC / Compliance** (quando aplicável) | Relatório mensal |

**Ligações úteis.**
- US-07 (Governação e Curadoria de Guidelines)
- US-09 (Gate de Segurança Pré-release)
- US-11 (Arquivo Central de Evidências)
- Cap. 12 (Monitorização e Operação)

---

## 📦 Artefactos Esperados

| Artefacto                  | Evidência auditável                                      |
|---------------------------|----------------------------------------------------------|
| `guidelines-stack.md`     | Guidelines curadas e aprovadas, com *changelog*          |
| `rules/`                  | *Rulesets* versionados e aprovados                       |
| `checklist-pr.md`         | Checklist formal integrada em PRs                        |
| `sbom-deps.json`          | SBOM validado e aprovado                                 |
| `gate-relatorio.md`       | Relatório consolidado do *security gate*                 |
| `excecoes-seguranca.md`   | Registo de exceções e aprovações                         |
| `uso-genia.md`            | Registo e revisão de uso de GenIA                        |
| `constrangimentos-dev.md` | Constrangimentos técnicos versionados (inclui GenIA)     |
| `.husky/pre-commit`       | Git hooks configurados e funcionais (US-12)              |
| `Makefile` (lint targets) | Validações locais disponíveis (US-12)                    |
| `.semgrep.yml`            | Regras de deteção de padrões perigosos (US-13)           |
| `sonar-rules.txt`         | Configuração de padrões perigosos em SAST (US-13)        |
| `evidencias/`             | Arquivo centralizado e indexado de evidências            |
| `dashboard-metrics.json`  | Config de dashboard de conformidade (US-14)              |
| `compliance-report.md`    | Relatório mensal/trimestral de métricas (US-14)          |

---

## ⚖️ Matriz de Proporcionalidade L1–L3

| Prática / Controlo | L1 (baixo) | L2 (médio) | L3 (crítico) |
|--------------------|------------|-------------|--------------|
| Guidelines | Regras upstream | Curadas por stack | Auditadas e *policy-as-code* |
| Revisão de código | Checklist básica | Dupla revisão | Revisão dedicada (inclui AppSec quando aplicável) |
| Dependências | Validação simples | Validação formal | SBOM rastreável |
| CI/CD | Linters básicos | SAST obrigatório | SAST + IaC/DAST + políticas |
| Exceções | Registo simples | Revalidação por sprint | Dupla aprovação |
| GenIA | Registo opcional | Revisão + constrangimentos obrigatórios | Revisão formal, licenças e evidência reforçada |
| Governação | Curadoria anual | Trimestral | Contínua e automatizada |
| Evidências | Export manual | Export automático | Arquivo imutável e auditado |
| Security Gate | Básico | Completo | Reforçado e automatizado |
| Validações Locais (US-12) | Recomendado | Obrigatório | Obrigatório + SAST leve |
| Padrões Perigosos (US-13) | Críticos apenas | Críticos + High | Completo + educação |
| Métricas & Conformidade (US-14) | Recomendado | Com alertas | Contínuo + SLA |

---

## 🏁 Recomendações Finais

O desenvolvimento seguro deve ser tratado como um **processo contínuo e mensurável**.  
As *user stories* deste capítulo operacionalizam as prescrições normativas, assegurando que cada prática deixa rasto verificável e que o grau de aplicação é proporcional ao risco.  
A integração destas ações no backlog e no pipeline transforma a segurança de software em disciplina diária e auditável.

Em síntese: o capítulo demonstra que **desenvolvimento seguro é a fundação sobre a qual o resto do ciclo de vida assenta**.  
Sem ele, nenhuma prática subsequente — seja CI/CD, IaC ou runtime — consegue oferecer confiança total.
