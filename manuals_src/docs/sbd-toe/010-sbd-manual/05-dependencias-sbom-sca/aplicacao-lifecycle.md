---
id: aplicacao-lifecycle
title: Como Fazer
description: Integração prática das prescrições de gestão de dependências, geração de SBOM e execução de SCA ao longo do ciclo de vida da aplicação
tags: [tipo:aplicacao, ciclo-vida, dependencias, sbom, sca, supply-chain, governance]
genia: us-format-normalization
---

# 🔄 Aplicação no Ciclo de Vida - Dependências, SBOM e SCA

## 🧭 Quando aplicar

As práticas acompanham a aplicação desde o arranque até ao *post‑release*.  
Cada evento é um **trigger** que deve produzir evidências objetivas.

| Fase SDLC / Evento | Ação esperada | Artefacto/Evidência |
|--------------------|---------------|---------------------|
| Início de projeto  | Publicar política e configurar repositórios internos | Documento de política + `repo-config.yaml` |
| Nova dependência   | Rever origem, licença, manutenção e CVEs | Ticket de aprovação + registo |
| Build / CI         | Gerar SBOM e executar SCA com *gates* | `sbom.*` + `sca-report.*` + logs |
| Release            | Rever findings/exceções e decidir *go/no-go* | `releases.md` + `excecoes.yaml` |
| Ciclo regular      | **Bots** abrem PRs de atualização com **avaliação de impacto** | PRs automáticos + testes/logs |
| CVE crítico público| Análise de impacto + *backport/fix* | Issue de resposta + plano de mitigação |

---

## 👥 Quem executa cada ação

A governação é **coletiva** - papéis e responsabilidades consistentes com o intro.md.

| Papel | Responsabilidade |
|------|-------------------|
| **Developer / Lead** | Incluir dependências, triagem inicial, *pinning*, correções |
| **AppSec** | Políticas, *tuning* de *gates*, gestão de exceções e risco |
| **DevOps / CI/CD** | SBOM, SCA, repositórios internos, bots de atualização e *impact analysis* |
| **QA / Test Engineer** | Evidências, testes de regressão, validação de PRs de bots |
| **Product Owner** | Decisão *go/no-go* e aceitação de risco residual |
| **GRC / Gestão** | Auditoria, conformidade, retenção de evidências |

---

## 📖 User Stories Reutilizáveis

Cada US transforma a prescrição em backlog acionável, com **contexto, rationale científico, BDD/checklist, artefactos, proporcionalidade L1–L3 e integração no SDLC**.

---

### US-01 - Gestão de dependências seguras

**Contexto.**  
Dependências externas sem validação introduzem risco invisível (componentes abandonados, origem duvidosa, licenças incompatíveis).

:::userstory
**História.**   
Como **Developer**, quero **usar apenas dependências aprovadas**, para **reduzir risco de vulnerabilidades herdadas e conflitos de licença**.

**Critérios de aceitação (BDD).**
- **Dado** que pretendo incluir uma dependência
  **Quando** submeto pedido de aprovação
  **Então** a dependência é validada segundo a política (origem, licença, manutenção, CVEs)

**Checklist.**
- [ ] Dependência aprovada formalmente  
- [ ] Licença validada / compatível  
- [ ] Sem CVEs críticos conhecidos  
- [ ] Proveniência confirmada (repositório interno)

:::

**Artefactos & evidências.**
- `dependencies-approval.md`  
- Ticket de validação no backlog

**Proporcionalidade por risco.**
| Nível | Obrigatório? | Ajustes |
|---|---|---|
| L1 | Opcional | Aprovação simplificada |
| L2 | Sim | Validação formal + licença |
| L3 | Sim | Revisão AppSec + proveniência

**Integração no SDLC.**
| Fase | Trigger | Responsável | SLA |
|---|---|---|---|
| Design/Dev | Inclusão de dependência | Developer + AppSec | Na aprovação da dependência |

**Ligações úteis.**  
- [Pilares de governação](/sbd-toe/sbd-manual/dependencias-sbom-sca/intro#pilares-de-governação)

---

### US-02 - SBOM em cada build

**Contexto.**  
Sem SBOM atualizado não é possível determinar rapidamente exposição a CVEs e cumprir requisitos de auditoria.

:::userstory
**História.**   
Como **DevOps**, quero **gerar SBOM em cada build**, para **rastreabilidade completa de componentes**.

**Critérios de aceitação (BDD).**
- **Dado** que um build é acionado
  **Quando** o artefacto é produzido
  **Então** é gerado um SBOM em formato CycloneDX ou SPDX

- **Dado** um SBOM gerado
- **Quando** é associado à release
- **Então** é armazenado e acessível para auditoria

**Checklist.**
- [ ] SBOM no formato CycloneDX ou SPDX  
- [ ] SBOM versionado e associado à release  
- [ ] Acessível para auditoria

:::

**Artefactos & evidências.**
- `sbom.json` / `sbom.xml`

**Proporcionalidade por risco.**
| Nível | Obrigatório? | Ajustes |
|---|---|---|
| L1 | Sim | SBOM básico |
| L2 | Sim | SBOM completo, incluído na release |
| L3 | Sim | SBOM assinado + verificação de integridade

**Integração no SDLC.**
| Fase | Trigger | Responsável |
|---|---|---|
| CI | Execução de build | DevOps

**Ligações úteis.**  
- [SBOM - Normas CycloneDX e SPDX](https://www.cyclonedx.org)
- [US-10 - Inventário e SBOM por Build](#us-10--inventário-e-sbom-por-build)

---

### US-03 - SCA automático com *gates*

**Contexto.**  
SCA identifica vulnerabilidades conhecidas em dependências (diretas e transitivas) e deve bloquear risco inaceitável.

:::userstory
**História.**   
Como **AppSec**, quero **executar SCA automático nos pipelines**, para **detetar CVEs antes de produção**.

**Critérios de aceitação (BDD).**
- **Dado** um build
  **Quando** o SBOM é gerado
  **Então** o SCA corre e **bloqueia** findings que excedam o threshold por Lx

**Checklist.**
- [ ] Scanner SCA integrado (ex.: Dependency‑Check/Trivy/Grype)  
- [ ] Findings documentados e triados  
- [ ] Bloqueio automático para CVEs críticos (L2) e médios+ (L3)

:::

**Artefactos & evidências.**
- `sca-report.html` / JSON
- Logs de pipeline com *gates*

**Proporcionalidade por risco.**
| Nível | Política |
|---|---|
| L1 | Alerta |
| L2 | Bloqueio High/Critical |
| L3 | Bloqueio Medium+

**Integração no SDLC.**
| Fase | Trigger | Responsável | SLA |
|---|---|---|---|
| CI | Geração de SBOM | DevOps + AppSec | Durante o build (bloqueio imediato) |

**Ligações úteis.**  
- [Guia de thresholds por L1–L3](/sbd-toe/sbd-manual/dependencias-sbom-sca/aplicacao-lifecycle#matriz-de-proporcionalidade-l1l3)

---

### US-04 - Exceções a CVEs formais e temporárias

**Contexto.**  
Nem todos os findings podem ser resolvidos de imediato; exceções devem ser **formais, justificadas e temporárias**.

:::userstory
**História.**   
Como **AppSec**, quero **formalizar exceções a CVEs**, para **manter governação e justificar risco residual**.

**Critérios de aceitação (BDD).**
- **Dado** que existe um CVE não resolvido
  **Quando** é solicitada uma exceção
  **Então** a exceção é formalizada em `excecoes.yaml` com justificativa técnica e de negócio, aprovador e prazo

- **Dado** uma exceção com prazo definido
- **Quando** passa o prazo
- **Então** é acionada revisão periódica com reavaliação do risco

**Checklist.**
- [ ] `excecoes.yaml` com justificativa técnica e de negócio  
- [ ] Aprovador e prazo definidos  
- [ ] Controlo compensatório especificado  
- [ ] Revisão periódica agendada

:::

**Artefactos & evidências.**
- `excecoes.yaml` (versionado)
- Aprovação registada no backlog

> **Referência:** Este US implementa [Cap 14-US-01: Processo formal de exceções]
> no contexto de vulnerabilidades em dependências (CVEs). O processo de aprovação, TTL e revalidação devem seguir a política master de exceções em Cap 14.

**Proporcionalidade por risco.**
| Nível | Obrigatório? | Ajustes |
|---|---|---|
| L1 | Opcional | Justificação simples |
| L2 | Sim | Revisão periódica (30–90 dias) |
| L3 | Sim | Validação executiva + métricas de risco

**Integração no SDLC.**
| Fase | Trigger | Responsável |
|---|---|---|
| Release | Findings pendentes | AppSec + Product Owner

**Ligações úteis.**  
- [Exceções e Aceitação de Risco em Vulnerabilidades](/sbd-toe/sbd-manual/dependencias-sbom-sca/addon/excecoes-e-aceitacao-risco)

---

### US-05 - Validação de release (*go/no-go*)

**Contexto.**  
Cada release é uma decisão de risco que deve ser **explícita e rastreável**.

:::userstory
**História.**   
Como **Product Owner**, quero **validar findings e exceções antes do go‑live**, para **tomar decisão informada de *go/no-go***.

**Critérios de aceitação (BDD).**
- **Dado** uma release candidata
  **Quando** verifico critérios de segurança e risco residual
  **Então** documento a decisão e condicionantes (se existirem)

**Checklist.**
- [ ] Lista de findings e estado  
- [ ] Exceções aprovadas e válidas  
- [ ] Decisão *go/no-go* documentada

:::

**Artefactos & evidências.**
- `releases.md` com histórico e justificações

**Proporcionalidade por risco.**
| Nível | Obrigatório? | Ajustes |
|---|---|---|
| L1 | Opcional | Decisão simples |
| L2 | Sim | Revisão formal |
| L3 | Sim | Revisão formal + AppSec envolvido

**Integração no SDLC.**
| Fase | Trigger | Responsável | SLA |
|---|---|---|---|
| Pré‑release | RC pronta | Product Owner + QA + AppSec | Antes do deploy a produção |

**Ligações úteis.**  
<!-- genia_suggest: Criar addon/10-checklist-release-segura.md com checklist de validação de release por L1-L3 -->
- [Artefactos esperados](/sbd-toe/sbd-manual/dependencias-sbom-sca/aplicacao-lifecycle#-artefactos-esperados)

---

### US-06 - Repositórios internos como fonte única

**Contexto.**  
Sem repositórios internos, dependências podem ser resolvidas de fontes não controladas (*typosquatting*, *confusion*, malícia).

:::userstory
**História.**   
Como **DevOps**, quero ***enforce* repositórios internos aprovados**, para **garantir proveniência e consistência**.

**Critérios de aceitação (BDD).**
- **Dado** que o *package manager* resolve dependências
  **Quando** a build ocorre
  **Então** só aceita fontes do repositório interno aprovado

**Checklist.**
- [ ] `repo-config.yaml` ativo (proxy/registry interno)  
- [ ] Bloqueio a fontes externas (allowlist)  
- [ ] Logs de acesso monitorizados e retidos

:::

**Artefactos & evidências.**
- `repo-config.yaml`  
- Logs de CI/CD com origem validada

**Proporcionalidade por risco.**
| Nível | Obrigatório? | Ajustes |
|---|---|---|
| L1 | Opcional | Recomendado |
| L2 | Sim | Obrigatório |
| L3 | Sim | Obrigatório + assinatura/verificação de pacotes

**Integração no SDLC.**
| Fase | Trigger | Responsável | SLA |
|---|---|---|---|
| Build | Resolução de dependências | DevOps/CI | Imediato (bloqueio em tempo real) |

**Ligações úteis.**  
- SLSA Provenance (conceitos)

---

### US-07 - Proibir bibliotecas copiadas manualmente

**Contexto.**  
JS, PHP, DLLs, JARs copiados diretamente para o repo escapam ao SBOM e ao SCA, criando *shadow dependencies*.

:::userstory
**História.**   
Como **Developer**, quero **usar apenas *package managers*/repositórios internos**, **nunca** copiar bibliotecas para o repo.

**Critérios de aceitação (BDD).**
- **Dado** que preciso de uma biblioteca externa
  **Quando** a adiciono ao projeto
  **Então** é gerida via *package manager* e **não** por cópia manual

**Checklist.**
- [ ] Zero libs copiadas manualmente  
- [ ] Todas via *package manager*  
- [ ] Auditoria periódica confirma ausência

:::

**Artefactos & evidências.**
- `package.json` / `pom.xml` / `composer.json`  
- Logs de build (resolução via repos internos)

**Proporcionalidade por risco.**
| Nível | Obrigatório? | Ajustes |
|---|---|---|
| L1 | Sim | Política documentada |
| L2 | Sim | Auditorias periódicas |
| L3 | Sim | Enforcement automático em CI/CD

**Integração no SDLC.**
| Fase | Trigger | Responsável | SLA |
|---|---|---|---|
| Dev | Inclusão de nova lib | Developer + AppSec | Na aprovação da dependência |

**Ligações úteis.**  
<!-- genia_suggest: Criar addon/11-bibliotecas-locais-migracao.md com padrões de migração por stack (npm, maven, composer, etc) -->
- [Governança de Bibliotecas de Terceiros](/sbd-toe/sbd-manual/dependencias-sbom-sca/addon/governanca-libs-terceiros)

---

### US-08 - Automação da atualização com avaliação de impacto

**Contexto.**  
Dependências degradam com o tempo; é necessário atualizar **com segurança e rapidez**.  
Ferramentas modernas avaliam **impacto** (semver, *release notes*, *diffs*, cobertura de testes) e:
- **abrem PRs automáticos** com *auto‑merge* quando a alteração é segura (*patch/minor* sem impacto, testes verdes, *gates* OK);
- **marcam como requires‑human** quando há impacto (API quebrada, *major*), anexando *guidelines* de *refactor*.

:::userstory
**História.**   
Como **DevOps/Developer**, quero **bots de atualização com avaliação de impacto**, para **receber PRs seguros automaticamente e *handoff* humano quando necessário**.

**Critérios de aceitação (BDD).**
- **Dado** que é publicada nova versão
  **Quando** o bot executa **impact analysis**
- Então:
  - Se **no‑impact** ⇒ PR com **auto‑merge** condicionado a CI verde e *gates* ok  
  - Se **impact** ⇒ PR **requires‑human** com *diff*, *breaking notes*, *refactor hints*, ou mesmo *GenAI com a alteração* adequada.

**Checklist.**
- [ ] Bot ativo (Renovate/Dependabot/afins)  
- [ ] **Impact analysis** configurado (semver + testes + changelog)  
- [ ] Critérios de **auto‑merge seguro** por L1–L3  
- [ ] Etiquetas (`no-impact`, `requires-human`) e *routing* para revisores  
- [ ] *Canary/rollout* definido (L3)

:::

**Artefactos & evidências.**
- PRs automáticos com labels e logs  
- Relatórios de testes e *gates* do CI/CD

**Proporcionalidade por risco.**
| Nível | Política |
|---|---|
| L1 | Bots opcionais; *auto‑PR* para *patch/minor* |
| L2 | Bots obrigatórios; *auto‑merge* para *patch* com CI verde |
| L3 | Bots obrigatórios; *impact analysis* + *canary*; *auto‑merge* apenas *patch*; *minor/major* requer aprovação humana e promoção por estágios |

**Integração no SDLC.**
| Fase | Trigger | Responsável | SLA |
|---|---|---|---|
| Dev/CI | Nova versão publicada | DevOps + Developer + QA | Automático (PR aberto e processado por bot) |

**Ligações úteis.**  
- [Política de Atualizações Automáticas](/sbd-toe/sbd-manual/dependencias-sbom-sca/addon/politica-atualizacoes)
- [Integração CI/CD](/sbd-toe/sbd-manual/dependencias-sbom-sca/addon/integracao-ci-cd)

---

### US-09 - Auditoria Periódica de Bibliotecas Copiadas Manualmente

**Contexto.**  
Bibliotecas copiadas manualmente escapam ao SBOM e ao SCA. É necessário **automação periódica** para detetar estas dependências ocultas e ***enforce* substituição** via package manager ou bloqueio em CI/CD.

:::userstory
**História.**   
Como **AppSec Engineer**, quero **executar auditoria periódica automatizada** para detetar bibliotecas copiadas manualmente (JS, PHP, DLL, JAR, etc.), para **bloquear a sua utilização em CI/CD e garantir SBOM e SCA completos**.

**Critérios de aceitação (BDD).**
- **Dado** que é executada auditoria periódica (semanal/mensal conforme Lx)
  **Quando** encontradas bibliotecas copiadas não via package manager
  **Então** é criada issue no backlog com prazo de substituição via repositório/package manager

**Checklist.**
- [ ] Scanner automático configurado (ex: busca de padrões de libs copiadas, extensões JS/PHP/DLL/JAR)
- [ ] Frequência de auditoria definida por Lx (L1: mensal, L2: quinzenal, L3: semanal)
- [ ] Resultados versionados no repositório (`.audit-libs.json`)
- [ ] Bloqueio em CI/CD para L2–L3 quando detectadas libs copiadas
- [ ] Zero libs detectadas como meta

:::

**Artefactos & evidências.**
- `.audit-libs.json` / `.audit-libs.yaml` (versionado)
- Logs de auditoria e scanner
- Issues de correção no backlog

**Proporcionalidade por risco.**
| Nível | Obrigatório? | Ajustes |
|---|---|---|
| L1 | Sim | Política documentada; auditoria manual mensal |
| L2 | Sim | Scanner automático quinzenal; alerta em pipeline |
| L3 | Sim | Scanner automático semanal; bloqueio em CI/CD |

**Integração no SDLC.**
| Fase | Trigger | Responsável | SLA |
|---|---|---|---|
| Ciclo regular | Auditoria periódica (cronograma) | AppSec Engineer + DevOps | L1: mensal, L2: quinzenal, L3: semanal |
| Build | Detecção em CI/CD (L2–L3) | DevOps (bloqueio) | Imediato (bloqueio em tempo real) |
| Backlog | Libs detectadas | Developer (remediação)

**Ligações úteis.**  
- [US-07 - Proibir bibliotecas copiadas manualmente](#us-07---proibir-bibliotecas-copiadas-manualmente)
<!-- genia_suggest: Criar addon/12-padroes-deteccao-libs.md com padrões regex e ferramentas por stack (npm, Python, Java, PHP, etc) -->
- [Governança de Bibliotecas de Terceiros](/sbd-toe/sbd-manual/dependencias-sbom-sca/addon/governanca-libs-terceiros)

---

### US-10 - Inventário e SBOM por Build

**Contexto.**  
Cada build deve produzir uma **Software Bill of Materials (SBOM)** assinada e rastreável, identificando todas as dependências utilizadas (diretas e transitivas).  
Esta SBOM deve poder ser **correlacionada com o artefacto implantado** e servir de base à deteção de desvios (“drift”) entre o que foi construído e o que está efetivamente a executar.

:::userstory
**História.**  
Como **DevOps Engineer**, quero gerar automaticamente um **SBOM assinado por build**, que se mantenha associado a cada imagem, pacote ou artefacto implantado, permitindo identificar todos os componentes e as suas versões.

**Critérios de aceitação (BDD).**
- **Dado** um pipeline de build  
  **Quando** o artefacto é produzido  
  **Então** é gerado um **SBOM CycloneDX ou SPDX** assinado e arquivado com metadados de commit, versão e hash.  
  
- **Dado** um SBOM assinado no build  
  **Quando** o serviço é implantado em `stage` ou `prod`  
  **Então** o orquestrador mantém **etiquetas de proveniência** (commit, build-id, imagem) que associam cada instância ao SBOM correto. 

- **Dado** telemetria de runtime  
  **Quando** é detetado um componente carregado que não existe no SBOM  
  **Então** é aberto **incidente de drift** com correção requerida.  

- **Dado** um pedido de auditoria ou compliance  
  **Quando** o auditor solicita o inventário de componentes  
  **Então** é possível exportar a SBOM e proveniência por versão.

**Checklist.**
- [ ] SBOM gerado por build (standard SPDX ou CycloneDX).  
- [ ] Assinatura e armazenamento seguro do SBOM.  
- [ ] Proveniência do deploy (attestations e labels por ambiente).  
- [ ] Comparação runtime vs SBOM e deteção de drift.  
- [ ] Exportação de inventário para CMDB ou data-lake de compliance.  
- [ ] Integração com alertas de vulnerabilidade e com Cap. 12 (Monitorização & Operação Segura).

:::

**Artefactos & evidências.**  
`sbom-<build>.json`, `attestation-<build>.json`, `proveniencia-<deploy>.json`, relatórios de drift e logs de build.

**Proporcionalidade.**
| Nível | Obrigatório? | Cobertura |
|---|---:|---|
| L1 | Sim | SBOM por build e associação básica por imagem. |
| L2 | Sim | Attestations + labels por ambiente, deteção de drift básica. |
| L3 | Sim | Drift contínuo + bloqueio de execuções não atestadas. |

**Integração no SDLC.**
| Fase | Trigger | Responsável | SLA |
|---|---|---|---|
| CI | Execução de build | DevOps Engineer | No build (geração automática) |
| Deploy | Implantação em ambiente | DevOps Engineer | Imediato (associação com metadados) |
| Operação | Monitorização contínua | DevOps + AppSec | Contínuo (deteção de drift) |

**Ligações úteis.**
- [SLSA Provenance - Conceitos e Implementação](https://slsa.dev)
- [Inventário e SBOM](/sbd-toe/sbd-manual/dependencias-sbom-sca/addon/inventario-sbom)
- [US-11 - Alertas sobre Vulnerabilidades](#us-11--alertas-sobre-vulnerabilidades-em-componentes-usados)

---

### US-11 - Alertas sobre Vulnerabilidades em Componentes Usados

**Contexto.**  
Os sistemas devem **detetar automaticamente vulnerabilidades conhecidas (CVEs)** nas dependências utilizadas.  
Além dos alertas durante o build, devem existir **alertas em produção**, correlacionando as versões efetivamente implantadas e os ambientes onde se encontram.  
O sistema deve conhecer **onde corre cada versão** para avaliar impacto real e priorizar correção.

:::userstory
**História.**  
Como **Gestor de Aplicação** e **AppSec**, quero **receber alertas correlacionados por ambiente** quando surgir uma CVE que afete versões em execução, para priorizar a correção e reduzir o MTTR.

**Critérios de aceitação (BDD).**
- **Dado** um inventário por serviço/ambiente com SBOM associado  
  **Quando** é publicada uma CVE que afeta uma versão implantada  
  **Então** é gerado um **alerta único** com componente, versão, serviços/ambientes impactados, *exploitability*, exposição e SLA recomendado.  
- **Dado** um alerta com SLA L2/L3  
  **Quando** passa o tempo de triagem sem ação  
  **Então** é **escalado automaticamente** (Cap. 12) e criado incidente no sistema de ITSM.  
- **Dado** uma exceção de risco aceite (VEX/justificativa)  
  **Quando** passa a existir *exploit ativo*  
  **Então** a exceção é reavaliada e o alerta reativado.  
- **Dado** o ciclo de vida de patch management  
  **Quando** a correção é implantada  
  **Então** o alerta é fechado automaticamente e registado como *resolved CVE*.  

**Checklist.**
- [ ] Inventário contínuo por serviço e ambiente com SBOM associado.  
- [ ] Correlação de CVEs e advisories para versões implantadas.  
- [ ] Enriquecimento de risco (exploit disponível, exposição, dados sensíveis).  
- [ ] Integração com Cap. 12 (SIEM/SOAR/alerting) e ITSM (incidentes/tarefas).  
- [ ] Processo de exceções com VEX e reavaliação automática.  
- [ ] KPIs: MTTA/MTTR por severidade e ambiente; % cobertura inventário vs deploys.

:::

**Artefactos & evidências.**  
`sbom-<build>.json` assinado; `inventario-runtime-<servico>-<ambiente>.json`; feed de CVEs correlacionadas; tickets/incidentes; decisões VEX.

**Proporcionalidade.**
| Nível | Obrigatório? | SLA triagem | SLA mitigação | Ajustes |
|---|---:|---:|---:|---|
| L1 | Sim | 5 dias úteis | 30 dias | Alertar apenas *high/critical* implantadas sem compensações. |
| L2 | Sim | 2 dias úteis | 14 dias | Incluir *medium* em serviços expostos; escalonamento automático. |
| L3 | Sim | 1 dia útil | 7 dias | *Blockers* com auto-rollback/kill-switch quando aplicável. |

**Integração no SDLC.**
| Fase | Trigger | Responsável | SLA |
|---|---|---|---|
| Publicação CVE | Nova vulnerabilidade pública | Automático (feed) | Detecção automática (1–6h) |
| Triagem | CVE correlacionada com versão implantada | AppSec + DevOps | L1: 5d, L2: 2d, L3: 1d |
| Mitigação | Plano de correção ou exceção | DevOps + AppSec | L1: 30d, L2: 14d, L3: 7d |

**Ligações úteis.**
- [US-02 - SBOM em cada build](#us-02---sbom-em-cada-build)
- [US-10 - Inventário e SBOM por Build](#us-10--inventário-e-sbom-por-build)
- [Cap. 12 - Monitorização & Operação Segura](/sbd-toe/sbd-manual/monitorizacao-operacoes/aplicacao-lifecycle)


---

### US-12 - Validação Automática de Compatibilidade de Licenças

**Contexto.**  
Dependências com licenças incompatíveis (GPL, AGPL, etc.) podem introduzir obrigações legais inesperadas. É necessário **validar automaticamente a compatibilidade** contra lista branca organizacional.

:::userstory
**História.**   
Como **Developer**, quero **validar automaticamente a compatibilidade de licenças** de novas dependências, para **garantir conformidade legal e evitar conflitos**.

**Critérios de aceitação (BDD).**
- **Dado** que é adicionada nova dependência
  **Quando** o build executa
  **Então** validador de licenças avalia compatibilidade contra lista branca organizacional

- **Dado** que uma licença é incompatível
- **Quando** o build tenta resolver a dependência
- **Então** o pipeline bloqueia com mensagem clara (L2–L3) ou avisa (L1)

**Checklist.**
- [ ] Lista branca de licenças aprovadas definida (ex: MIT, Apache 2.0, BSD)
- [ ] Validador automático de licenças integrado no CI/CD
- [ ] Bloqueio para licenças proibidas/incompatíveis (L2–L3)
- [ ] Alerta para licenças não reconhecidas (para revisão manual)
- [ ] Documentação do critério de aprovação por licença

:::

**Artefactos & evidências.**
- `licenses-whitelist.yaml` / `.licenseignore` (versionado)
- Logs de CI/CD com validação de licenças
- Issues de remediação (trocar dependência ou requerer exceção formal)

**Proporcionalidade por risco.**
| Nível | Obrigatório? | Ajustes |
|---|---|---|
| L1 | Opcional | Validação manual, ad hoc |
| L2 | Sim | Automática com alerta; bloqueio para GPL/AGPL |
| L3 | Sim | Automática com bloqueio; exceções requerem aprovação formal |

**Integração no SDLC.**
| Fase | Trigger | Responsável | SLA |
|---|---|---|---|
| Design/Dev | Inclusão de dependência | Developer | Na aprovação da dependência |
| Build | Resolução de dependências | CI/CD (bloqueio/alerta) | Durante o build (imediato) |
| Exceção | Licença incompatível com business case | AppSec + Legal (se necessário) | Antes do go-live |

**Ligações úteis.**  
- [US-01 - Gestão de dependências seguras](#us-01---gestão-de-dependências-seguras)
- [SPDX License List](https://spdx.org/licenses/)

---

### US-13 - Validação assistida de atualizações de dependências (I1)
**Contexto.**  
Bots de atualização (Dependabot, Renovate) sugerem updates mas requerem validação humana antes de merge, especialmente para breaking changes ou CVEs críticos.

:::userstory
**História.**   
Como **Developer**, quero validar propostas de atualização de bots com checklist I1 e decisores explícitos, para garantir separação entre sugestão e decisão (Invariante I1).

**Critérios de aceitação (BDD).**
- **Dado** que bot abre PR de atualização  
  **Quando** executo Checklist I1  
  **Então** decisão é registada com decisores explícitos (Developer, AppSec, Product Owner) e justificação documentada

**Checklist I1 — Validação de Proposta de Atualização.**
- [ ] **Relevância:** Breaking changes? Team expertise? Custos aceitáveis?
- [ ] **Evidência empírica:** Testes cobrem? PoC/staging validado? Rollback plan?
- [ ] **Controlo existente:** Se CVE, vulnerabilidade real? Exploitável no contexto?
- [ ] **Novos requisitos:** Mapeia a DEP-XXX ou cria novo?
- [ ] **Decisão:** ACEITAR (auto-merge) / ADAPTAR (migration plan) / REJEITAR (postpone com VEX)

**Decisão documentada em PR:**
- Decisores: Proponente (Bot), Validador técnico (Developer, data), Validador segurança (AppSec, data), Aprovador impacto (Product Owner, data)
- Justificação: Breaking changes, CVE severity, esforço migration, risco residual
- Plano: Migration steps, staging validation, rollback plan, SLA completion
- Evidências: PoC logs, tests added, approval emails

**Escalation para conflitos:**
- Segurança (CVE CRITICAL) vs. Estabilidade (Breaking) → Product Owner + AppSec + CTO (L3)
- Update vs. Freeze de produção → AppSec Lead + Product Owner (deploy emergencial?)
- Supply chain risk → Arquiteto + AppSec + Product Owner (fork interno? alternativa?)

:::

**Artefactos & evidências.**  
- PR comment com template decisão I1 completo
- `dependencies/proposals/proposal-XXX.md` (sugestão bot)
- Checklist I1 preenchido
- VEX document (se postpone)

**Proporcionalidade.**
| Nível | Obrigatório? | Ajustes |
|---|---|---|
| L1 | Recomendado | Checklist para MAJOR/CVE HIGH+, auto-merge PATCH |
| L2 | Sim | Checklist obrigatório MINOR+, decisores explícitos CVE MEDIUM+ |
| L3 | Sim | Checklist obrigatório todas atualizações, PoC para MAJOR/CVE CRITICAL |

**Matriz de decisores.**
| Severidade Update | Decisor Técnico | Validador Segurança | Aprovador Impacto | SLA |
|---|---|---|---|---|
| PATCH (bug fix) | Developer | - | - | Auto-merge (CI green) |
| MINOR sem breaking | Developer | - | - | 2 dias |
| MINOR com hints breaking | Developer | AppSec (deps críticas) | - | 5 dias |
| MAJOR (breaking) | Developer + Arquiteto | AppSec | Product Owner | 10 dias |
| CVE CRITICAL | Developer | AppSec Lead | Product Owner | 48h (L3) |
| CVE HIGH | Developer | AppSec | - | 7 dias (L2) |

**KPIs.**
- % PRs com decisor explícito: 100% (L2/L3)
- Tempo médio decisão: <5d (MINOR), <48h (CVE CRITICAL)
- % auto-merge seguros: >95%
- % CVE com SLA cumprido: >90%

**Integração no SDLC.**
| Fase | Trigger | Responsável | SLA |
|---|---|---|---|
| Continuous | Bot detecta nova versão | Developer + AppSec | <7 dias (ALTA) |
| Go-live | Validação ADR completo | QA + AppSec | Antes release |

**Ligações úteis.**
- 🔗 [Addon 20 - Framework I1 para Bots](addon/20-validacao-atualizacoes-assistida.md)
- 🔗 [US-04 - Exceções a CVEs](#us-04---exceções-a-cves-formais-e-temporárias)

---

### US-14 - Validação manual e empírica de CVEs (I2)
**Contexto.**  
CVEs reportados por SCA devem ser validados tecnicamente para confirmar exploitabilidade antes de priorizar mitigação (evitar FP, detectar FN).

:::userstory
**História.**   
Como **AppSec Engineer**, quero validar empiricamente CVEs reportados por SCA com testes técnicos, para confirmar exploitabilidade real antes de priorizar mitigação (Invariante I2).

**Critérios de aceitação (BDD).**
- **Dado** que CVE foi reportado por scanner  
  **Quando** executo teste empírico por categoria  
  **Então** confirmo ou refuto exploitabilidade, registo FP/FN, e priorizo mitigação

**Taxonomia de CVEs (6 categorias com testes):**
- **A. RCE (Remote Code Execution):** Exploit PoC + code analysis (input deserializado?)
- **B. SQLi (SQL Injection):** SQL payloads + sqlmap (query dinâmica com user input?)
- **C. XSS (Cross-Site Scripting):** XSS payloads + Burp Suite (output escapado?)
- **D. Authentication Bypass:** JWT manipulation + replay attacks (algoritmo "none" aceite?)
- **E. Path Traversal:** ../ payloads + file read (whitelist existe?)
- **F. DoS (Denial of Service):** ReDoS payloads + load test (rate limiting adequado?)

**Gestão de Falsos Positivos/Negativos:**
- **FP (CVE não exploitável):** Análise técnica → VEX "not_affected" → Suppressão temporária → Revisão 6 meses
- **FN (CVE não detectado):** Discovery manual → Root cause (DB outdated?) → Mitigação imediata → Adicionar custom check

**Qualidade de validação:**
- FP rate: <20% (se >30% → scanner mal configurado)
- FN rate: <3% (se >10% → scanner inadequado)
- Tempo validação: <24h (CRITICAL)
- Cobertura: 100% CVEs CRITICAL (L2/L3)
- EPSS prioritization: >90% CVEs com EPSS >0.5 priorizados

:::

**Artefactos & evidências.**  
- `dependencies/validation-results/CVE-2023-XXXX-validation.md` (resultado EXPLOITÁVEL/NÃO_APLICÁVEL/MITIGADO)
- Evidência técnica: Exploit PoC logs, screenshots, comandos executados
- VEX document (se FP)
- `dependencies/falsos-negativos/FN-2026-XXX.md` (se FN descoberto)

**Proporcionalidade.**
| Nível | Obrigatório? | Ajustes |
|---|---|---|
| L1 | Recomendado | Validação manual ≥50% CVEs CRITICAL, teste manual |
| L2 | Sim | Validação obrigatória 100% CRITICAL + ≥70% HIGH, manual + exploit PoC |
| L3 | Sim | Validação obrigatória 100% MEDIUM+, manual + PoC + automated regression |

**KPIs.**
- FP rate: <20%
- FN rate: <3%
- % CVEs CRITICAL testados: 100% (L2/L3)
- Tempo validação: <24h (CRITICAL)
- EPSS correlation: >90%

**Integração no SDLC.**
| Fase | Trigger | Responsável | SLA |
|---|---|---|---|
| SCA scan | CVE reportado | AppSec + Developer | <24h (CRITICAL) |
| Post-incident | FN descoberto | AppSec + QA | 48h para mitigação |
| Quarterly | Revisão FP/FN | AppSec Lead | Trimestral |

**Ligações úteis.**
- 🔗 [Addon 21 - Taxonomia e Testes de CVEs](addon/21-validacao-manual-cves.md)
- 🔗 [Addon 02 - Análise SCA](addon/02-analise-sca.md)

---

## 🧩 Nota complementar — Inventário contínuo de componentes e alertas em produção

A gestão de dependências não termina no build.  
Deve existir um **inventário contínuo de componentes de 3.ºs** por projeto e ambiente (dev/test/stage/prod), com **alertas automáticos** quando são publicadas vulnerabilidades que afetem versões implantadas.  

Isto complementa o SCA no pipeline ao:  
- Fechar o ciclo *build → deploy → run*;  
- Priorizar pelo risco real (exposição e exploitability);  
- Acionar resposta operacional via Cap. 12 (Monitorização & Operação Segura).

**Prática recomendada.**
1. Gerar SBOM no build e assinar.  
2. Etiquetar por ambiente no registo/orquestrador.  
3. Descoberta contínua em runtime (inventário por deploy) e comparação com SBOM.  
4. Correlação de CVEs e alertas quando: versão implantada afetada / exploit ativo / caminho crítico.  
5. Abertura automática de incidente/tarefa com SLA proporcional L1–L3.  
6. Evidência: SBOM, inventário, alertas, VEX, histórico de patching.

**Integração com Cap. 12 — Monitorização & Operação Segura.**

Os user stories 10 e 11 estão muito relacionados com o exposto no **Cap. 12 — Monitorização & Operação Segura.**, evidenciando o aspeto critico de monitorização além da execução de um qualquer pipeline de build. É fácil implementar medidas de segurança durante o build, mas, depois de entrar em produção uma aplicação pode estar um longo periodo de tempo sem voltar ao pipeline de desenvolvimento, é portanto essencial rever periodicamente, ou espontaneamente, o SBOM das aplicações em produção. É mais grave uma nova vulnerabilidade ser encontrada numa aplicação em produção do que durante o processo de desenvolvimento, principalmente sem medidas de alarmistica ou periodicas de deteção.
Ums dos aspetos fundamentais no  **Cap. 12 — Monitorização & Operação Segura.** é exatamente esse controlo, definindo:

- Eventos: criação/fecho de alerta, mudança de exploitability, violação de SLA, drift.  
- Métricas: MTTA, MTTR, ativos afetados, % exceções ativas, *patch latency*.  
- Automação: enriquecimento, priorização, escalonamento, playbooks SOAR.  
- Relato executivo: compliance Cap. 05 + Cap. 12, visão por L1–L3.

---
## 📦 Artefactos esperados

| Artefacto | Evidência |
|-----------|-----------|
| `dependencies-approval.md` | Lista aprovada de dependências |
| `sbom.json` / `sbom.xml` | Inventário por build (CycloneDX/SPDX) |
| `attestation-<build>.json` | Proveniência e assinatura do build |
| `inventario-runtime-<servico>-<ambiente>.json` | Inventário de componentes efetivamente implantados |
| `sca-report.html/json` | Vulnerabilidades detetadas e *gates* aplicados |
| `cve-alerts.json` | Alertas correlacionados por ambiente e severidade |
| `vex.yaml` | Exceções justificadas e estado de reavaliação |
| `excecoes.yaml` | Exceções formais aprovadas |
| `releases.md` | Decisões *go/no-go* e histórico de *patching* |
| `repo-config.yaml` | Repositórios internos configurados |
| `.audit-libs.json` / `.audit-libs.yaml` | Resultados de auditoria periódica de libs copiadas |
| `licenses-whitelist.yaml` | Lista branca de licenças aprovadas |
| **PRs de bots** | *Labels* de impacto, logs e testes + comentário decisão I1 |
| **Relatórios de drift** | Diferenças entre SBOM e runtime |
| **Tickets ITSM / Incidentes** | Evidência de tratamento de CVE e SLA cumprido |
| `dependencies/proposals/proposal-XXX.md` | Proposta bot para validação I1 (US-13) |
| `dependencies/validation-results/CVE-XXX-validation.md` | Resultado validação empírica (EXPLOITÁVEL/FP/FN) (US-14) |
| `dependencies/falsos-positivos/FP-CVE-XXX.md` | VEX + análise técnica FP (US-14) |
| `dependencies/falsos-negativos/FN-2026-XXX.md` | RCA + mitigação FN (US-14) |

---

## ⚖️ Matriz de proporcionalidade L1–L3

| Prática | L1 | L2 | L3 |
|---------|----|----|----|
| SBOM | Básico por build | Completo por release | Assinado + integridade + proveniência |
| Inventário runtime | Recomendado | Obrigatório | Contínuo + deteção de *drift* |
| SCA | Aviso | Bloqueio High/Critical | Bloqueio Medium+ + feed CVE ativo |
| Alertas CVE implantadas | Manual / ad hoc | Automático por ambiente | Automático + correlação e escalonamento |
| Pinning de versões | Recomendado | Obrigatório | Obrigatório + validação de proveniência |
| Exceções / VEX | Simples | Formais + revisão periódica | Formais + revalidação automática |
| Repositório interno | Recomendado | Obrigatório | Obrigatório + assinatura e *provenance attestation* |
| Bibliotecas copiadas | Proibidas (política) | Auditoria periódica | Enforcement CI/CD + bloqueio |
| Auditoria de libs copiadas | Política documentada; mensal | Scanner automático; quinzenal | Scanner automático; semanal + bloqueio CI/CD |
| Validação de licenças | Manual, ad hoc | Automática com alerta | Automática com bloqueio (exceto exceções formais) |
| Bots / automação de patching | Opcional | Ativos + *auto-merge patch* | Ativos + *impact analysis*, *canary* e rollback |
| Integração com Cap. 12 | Opcional | Alertas SIEM básicos | Total: SOAR, métricas MTTR/MTTA e escalonamento |

---

## 🏁 Recomendações finais

- **SBOM** deve ser tratado como documento vivo, com assinatura e proveniência verificável por build e por ambiente.  
- **Inventário contínuo** em produção é essencial: deteta *drift* e vulnerabilidades em versões efetivamente implantadas.  
- **SCA automatizado** com *gates* proporcionais ao risco e integração com alertas CVE em runtime.  
- **Repositórios internos** e *attestations* são a base da confiança na supply chain.  
- **Exceções formais e temporárias** (VEX) devem ser reavaliadas automaticamente quando muda o risco ou surge *exploit ativo*.  
- **Eliminar bibliotecas copiadas manualmente** (US-07) com **auditoria periódica automatizada** (US-09) e bloqueio em CI/CD para L2–L3.  
- **Validar compatibilidade de licenças** (US-12) contra lista branca, bloqueando ou alertando conforme criticidade.  
- **Bots com avaliação de impacto** (US-08):  
  - PRs de *patches triviais* → *auto-merge*;  
  - PRs com impacto → revisão humana, *canary* e promoção por estágios (sobretudo em L3).  
- **Integração com Cap. 12** deve garantir visibilidade total, alertas em tempo real e métricas operacionais de resposta (MTTA/MTTR) por severidade e ambiente.

