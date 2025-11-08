---
id: aplicacao-lifecycle
title: Como Fazer
description: Integração prática das prescrições de gestão de dependências, geração de SBOM e execução de SCA ao longo do ciclo de vida da aplicação
tags: [dependencias, sbom, sca, supply-chain, cicd, excecoes, governance, updates]
sidebar_position: 15
---

# 🔄 Aplicação no Ciclo de Vida - Dependências, SBOM e SCA

## 🧭 Quando aplicar

As práticas acompanham a aplicação desde o arranque até ao *post‑release*.  
Cada evento é um **gatilho** que deve produzir evidências objetivas.

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
- Dado que pretendo incluir uma dependência
- Quando submeto pedido de aprovação
- Então a dependência é validada segundo a política (origem, licença, manutenção, CVEs)

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
| Fase | Trigger | Responsável |
|---|---|---|
| Design/Dev | Inclusão de dependência | Developer + AppSec

**Ligações úteis.**  
- Política de Dependências (cap05:intro#politicas)

---

### US-02 - SBOM em cada build

**Contexto.**  
Sem SBOM atualizado não é possível determinar rapidamente exposição a CVEs e cumprir requisitos de auditoria.

:::userstory
**História.**   
Como **DevOps**, quero **gerar SBOM em cada build**, para **rastreabilidade completa de componentes**.

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
- CycloneDX/SPDX (normas de SBOM)

---

### US-03 - SCA automático com *gates*

**Contexto.**  
SCA identifica vulnerabilidades conhecidas em dependências (diretas e transitivas) e deve bloquear risco inaceitável.

:::userstory
**História.**   
Como **AppSec**, quero **executar SCA automático nos pipelines**, para **detetar CVEs antes de produção**.

**Critérios de aceitação (BDD).**
- Dado um build
- Quando o SBOM é gerado
- Então o SCA corre e **bloqueia** findings que excedam o threshold por Lx

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
| Fase | Trigger | Responsável |
|---|---|---|
| CI | Geração de SBOM | DevOps + AppSec

**Ligações úteis.**  
- Guia de thresholds por L1–L3 (cap05:intro#proporcionalidade)

---

### US-04 - Exceções a CVEs formais e temporárias

**Contexto.**  
Nem todos os findings podem ser resolvidos de imediato; exceções devem ser **formais, justificadas e temporárias**.

:::userstory
**História.**   
Como **AppSec**, quero **formalizar exceções a CVEs**, para **manter governação e justificar risco residual**.

**Checklist.**
- [ ] `excecoes.yaml` com justificativa técnica e de negócio  
- [ ] Aprovador e prazo definidos  
- [ ] Controlo compensatório especificado  
- [ ] Revisão periódica agendada

:::

**Artefactos & evidências.**
- `excecoes.yaml` (versionado)
- Aprovação registada no backlog

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
- Template de exceções (Cap. 05 - anexos)

---

### US-05 - Validação de release (*go/no-go*)

**Contexto.**  
Cada release é uma decisão de risco que deve ser **explícita e rastreável**.

:::userstory
**História.**   
Como **Product Owner**, quero **validar findings e exceções antes do go‑live**, para **tomar decisão informada de *go/no-go***.

**Critérios de aceitação (BDD).**
- Dado uma release candidata
- Quando verifico critérios de segurança e risco residual
- Então documento a decisão e condicionantes (se existirem)

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
| Fase | Trigger | Responsável |
|---|---|---|
| Pré‑release | RC pronta | Product Owner + QA + AppSec

**Ligações úteis.**  
- Checklist de release segura (Cap. 05 - anexos)

---

### US-06 - Repositórios internos como fonte única

**Contexto.**  
Sem repositórios internos, dependências podem ser resolvidas de fontes não controladas (*typosquatting*, *confusion*, malícia).

:::userstory
**História.**   
Como **DevOps**, quero **forçar repositórios internos aprovados**, para **garantir proveniência e consistência**.

**Critérios de aceitação (BDD).**
- Dado que o *package manager* resolve dependências
- Quando a build ocorre
- Então só aceita fontes do repositório interno aprovado

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
| Fase | Trigger | Responsável |
|---|---|---|
| Build | Resolução de dependências | DevOps/CI

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
- Dado que preciso de uma biblioteca externa
- Quando a adiciono ao projeto
- Então é gerida via *package manager* e **não** por cópia manual

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
| Fase | Trigger | Responsável |
|---|---|---|
| Dev | Inclusão de nova lib | Developer + AppSec

**Ligações úteis.**  
- Guia “Bibliotecas locais: riscos e substituição”

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
- Dado que é publicada nova versão
- Quando o bot executa **impact analysis**
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
| Fase | Trigger | Responsável |
|---|---|---|
| Dev/CI | Nova versão publicada | DevOps + Developer + QA

**Ligações úteis.**  
- Guia de operação de bots (labels, *auto‑merge*, *canary*)

---

### US-10 – Inventário e SBOM por Build

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

---

### US-11 – Alertas sobre Vulnerabilidades em Componentes Usados

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
| **PRs de bots** | *Labels* de impacto, logs e testes |
| **Relatórios de drift** | Diferenças entre SBOM e runtime |
| **Tickets ITSM / Incidentes** | Evidência de tratamento de CVE e SLA cumprido |

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
| Bots / automação de patching | Opcional | Ativos + *auto-merge patch* | Ativos + *impact analysis*, *canary* e rollback |
| Integração com Cap. 12 | Opcional | Alertas SIEM básicos | Total: SOAR, métricas MTTR/MTTA e escalonamento |

---

## 🏁 Recomendações finais

- **SBOM** deve ser tratado como documento vivo, com assinatura e proveniência verificável por build e por ambiente.  
- **Inventário contínuo** em produção é essencial: deteta *drift* e vulnerabilidades em versões efetivamente implantadas.  
- **SCA automatizado** com *gates* proporcionais ao risco e integração com alertas CVE em runtime.  
- **Repositórios internos** e *attestations* são a base da confiança na supply chain.  
- **Exceções formais e temporárias** (VEX) devem ser reavaliadas automaticamente quando muda o risco ou surge *exploit ativo*.  
- **Eliminar bibliotecas copiadas manualmente** e reforçar *pinning* de versões e proveniência.  
- **Bots com avaliação de impacto**:  
  - PRs de *patches triviais* → *auto-merge*;  
  - PRs com impacto → revisão humana, *canary* e promoção por estágios (sobretudo em L3).  
- **Integração com Cap. 12** deve garantir visibilidade total, alertas em tempo real e métricas operacionais de resposta (MTTA/MTTR) por severidade e ambiente.
