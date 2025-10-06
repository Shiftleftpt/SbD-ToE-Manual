---
id: aplicacao-lifecycle
title: Aplicação no Ciclo de Vida — Dependências, SBOM e SCA
description: Integração prática das prescrições de gestão de dependências, geração de SBOM e execução de SCA ao longo do ciclo de vida da aplicação
tags: [dependencias, sbom, sca, supply-chain, cicd, excecoes, governance, updates]
sidebar_position: 15
---

# 🔄 Aplicação no Ciclo de Vida — Dependências, SBOM e SCA {cap05:aplicacao-lifecycle}

## 🧭 Quando aplicar {cap05:aplicacao-lifecycle#quando-aplicar}

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

## 👥 Quem executa cada ação {cap05:aplicacao-lifecycle#quem-executa}

A governação é **coletiva** — papéis e responsabilidades consistentes com o intro.md.

| Papel | Responsabilidade |
|------|-------------------|
| **Developer / Lead** | Incluir dependências, triagem inicial, *pinning*, correções |
| **AppSec** | Políticas, *tuning* de *gates*, gestão de exceções e risco |
| **DevOps / CI/CD** | SBOM, SCA, repositórios internos, bots de atualização e *impact analysis* |
| **QA / Test Engineer** | Evidências, testes de regressão, validação de PRs de bots |
| **Product Owner** | Decisão *go/no-go* e aceitação de risco residual |
| **GRC / Gestão** | Auditoria, conformidade, retenção de evidências |

---

## 📖 User Stories Reutilizáveis {cap05:aplicacao-lifecycle#user-stories}

Cada US transforma a prescrição em backlog acionável, com **contexto, rationale científico, BDD/checklist, artefactos, proporcionalidade L1–L3 e integração no SDLC**.

---

### US-01 — Gestão de dependências seguras {#us-01}

**Contexto.**  
Dependências externas sem validação introduzem risco invisível (componentes abandonados, origem duvidosa, licenças incompatíveis).

**📖 Rationale científico.**  
Frameworks como **SSDF PW.4**, **SAMM Implementation** e **BSIMM CMVM1.1** exigem políticas explícitas de dependências.  
Relatórios da **Sonatype** mostram que mais de 90% das vulnerabilidades em bibliotecas usadas em incidentes poderiam ter sido evitadas escolhendo versões mantidas e auditadas.  
Casos como o *LeftPad incident* (npm, 2016) lembram-nos de como um único pacote pode parar milhares de builds — a disciplina aqui não é opcional, é sobrevivência organizacional.

**História.**  
Como **Developer**, quero **usar apenas dependências aprovadas**, para **reduzir risco de vulnerabilidades herdadas e conflitos de licença**.

**Critérios de aceitação (BDD).**
- Dado que pretendo incluir uma dependência
- Quando submeto pedido de aprovação
- Então a dependência é validada segundo a política (origem, licença, manutenção, CVEs)

**Checklist (binária, auditável).**
- [ ] Dependência aprovada formalmente  
- [ ] Licença validada / compatível  
- [ ] Sem CVEs críticos conhecidos  
- [ ] Proveniência confirmada (repositório interno)

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
| Fase | Gatilho | Responsável |
|---|---|---|
| Design/Dev | Inclusão de dependência | Developer + AppSec

**Ligações úteis.**  
- Política de Dependências (cap05:intro#politicas)

---

### US-02 — SBOM em cada build {#us-02}

**Contexto.**  
Sem SBOM atualizado não é possível determinar rapidamente exposição a CVEs e cumprir requisitos de auditoria.

### US-02 — SBOM em cada build {#us-02}

**📖 Rationale científico.**  
Um SBOM não é “papelada extra”: é o mapa que permite saber onde estamos quando surge um CVE crítico.  
Normativos como **SSDF PS.3**, **SLSA v1.0** e **BSIMM CMVM2.1** colocam a proveniência como elemento essencial.  
O **Executive Order 14028 (EUA)** tornou SBOM mandatário em software crítico, e a prática já provou valor em incidentes reais: equipas com SBOM atualizado responderam a log4j em horas; sem SBOM, outras ficaram semanas às cegas.

**História.**  
Como **DevOps**, quero **gerar SBOM em cada build**, para **rastreabilidade completa de componentes**.

**Checklist.**
- [ ] SBOM no formato CycloneDX ou SPDX  
- [ ] SBOM versionado e associado à release  
- [ ] Acessível para auditoria

**Artefactos.**
- `sbom.json` / `sbom.xml`

**Proporcionalidade por risco.**
| Nível | Obrigatório? | Ajustes |
|---|---|---|
| L1 | Sim | SBOM básico |
| L2 | Sim | SBOM completo, incluído na release |
| L3 | Sim | SBOM assinado + verificação de integridade

**Integração no SDLC.**
| Fase | Gatilho | Responsável |
|---|---|---|
| CI | Execução de build | DevOps

**Ligações úteis.**  
- CycloneDX/SPDX (normas de SBOM)

---

### US-03 — SCA automático com *gates* {#us-03}

**Contexto.**  
SCA identifica vulnerabilidades conhecidas em dependências (diretas e transitivas) e deve bloquear risco inaceitável.

**📖 Rationale científico.**  
Executar SCA não é luxo — é o alarme de incêndio no pipeline.  
**SSDF RV.2**, **SAMM Verification** e **BSIMM CMVM3.1** destacam-no como essencial.  
Dados do **Verizon DBIR** confirmam: 40% das vulnerabilidades exploradas em 2023 estavam em bibliotecas de terceiros não atualizadas.  
Sem gates, relatórios de SCA viram “ruído de fundo” e não mudam comportamentos; com gates, transformam-se em barreiras objetivas que previnem regressões.

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

**Artefactos.**
- `sca-report.html` / JSON
- Logs de pipeline com *gates*

**Proporcionalidade por risco.**
| Nível | Política |
|---|---|
| L1 | Alerta |
| L2 | Bloqueio High/Critical |
| L3 | Bloqueio Medium+

**Integração no SDLC.**
| Fase | Gatilho | Responsável |
|---|---|---|
| CI | Geração de SBOM | DevOps + AppSec

**Ligações úteis.**  
- Guia de thresholds por L1–L3 (cap05:intro#proporcionalidade)

---

### US-04 — Exceções a CVEs formais e temporárias {#us-04}

**Contexto.**  
Nem todos os findings podem ser resolvidos de imediato; exceções devem ser **formais, justificadas e temporárias**.

**📖 Rationale científico.**  
Exceções são inevitáveis, mas se não forem governadas tornam-se bombas-relógio.  
**SSDF RV.1**, **SAMM Governance** e **BSIMM CP1.2** prescrevem processos formais, com prazo e mitigação.  
A **ENISA** alerta: riscos acumulados por exceções não revistas são uma das maiores causas de falhas de auditoria.  
Aqui, a diferença é simples: exceções informais escondem riscos; exceções formais iluminam-nos e permitem geri-los.

**História.**  
Como **AppSec**, quero **formalizar exceções a CVEs**, para **manter governação e justificar risco residual**.

**Checklist.**
- [ ] `excecoes.yaml` com justificativa técnica e de negócio  
- [ ] Aprovador e prazo definidos  
- [ ] Controlo compensatório especificado  
- [ ] Revisão periódica agendada

**Artefactos.**
- `excecoes.yaml` (versionado)
- Aprovação registada no backlog

**Proporcionalidade por risco.**
| Nível | Obrigatório? | Ajustes |
|---|---|---|
| L1 | Opcional | Justificação simples |
| L2 | Sim | Revisão periódica (30–90 dias) |
| L3 | Sim | Validação executiva + métricas de risco

**Integração no SDLC.**
| Fase | Gatilho | Responsável |
|---|---|---|
| Release | Findings pendentes | AppSec + Product Owner

**Ligações úteis.**  
- Template de exceções (Cap. 05 — anexos)

---

### US-05 — Validação de release (*go/no-go*) {#us-05}

**Contexto.**  
Cada release é uma decisão de risco que deve ser **explícita e rastreável**.

**📖 Rationale científico.**  
Cada release é também uma decisão de risco.  
**SSDF RV.4**, **SAMM Verification** e **BSIMM CR3.2** defendem que essa decisão seja informada e documentada.  
Estudos do **DBIR** mostram que revisões finais reduzem em ~30% a probabilidade de vulnerabilidades conhecidas chegarem à produção.  
A prática não é burocracia: é a diferença entre “lançámos porque estava na sprint” e “lançámos porque sabemos o que estamos a aceitar”.

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

**Artefactos.**
- `releases.md` com histórico e justificações

**Proporcionalidade por risco.**
| Nível | Obrigatório? | Ajustes |
|---|---|---|
| L1 | Opcional | Decisão simples |
| L2 | Sim | Revisão formal |
| L3 | Sim | Revisão formal + AppSec envolvido

**Integração no SDLC.**
| Fase | Gatilho | Responsável |
|---|---|---|
| Pré‑release | RC pronta | Product Owner + QA + AppSec

**Ligações úteis.**  
- Checklist de release segura (Cap. 05 — anexos)

---

### US-06 — Repositórios internos como fonte única {#us-06}

**Contexto.**  
Sem repositórios internos, dependências podem ser resolvidas de fontes não controladas (*typosquatting*, *confusion*, malícia).

### US-06 — Repositórios internos como fonte única {#us-06}

**📖 Rationale científico.**  
Usar apenas repositórios internos é um dos controlos mais eficazes contra ataques de cadeia de fornecimento.  
**SLSA v1.0**, **SSDF PW.4** e **BSIMM CMVM1.1** prescrevem-no explicitamente.  
Incidentes de *dependency confusion* mostraram como basta publicar pacotes maliciosos com o mesmo nome para comprometer builds inteiros.  
Organizações que centralizam dependências em repositórios internos reduzem drasticamente esta superfície de ataque.

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

**Artefactos.**
- `repo-config.yaml`  
- Logs de CI/CD com origem validada

**Proporcionalidade por risco.**
| Nível | Obrigatório? | Ajustes |
|---|---|---|
| L1 | Opcional | Recomendado |
| L2 | Sim | Obrigatório |
| L3 | Sim | Obrigatório + assinatura/verificação de pacotes

**Integração no SDLC.**
| Fase | Gatilho | Responsável |
|---|---|---|
| Build | Resolução de dependências | DevOps/CI

**Ligações úteis.**  
- SLSA Provenance (conceitos)

---

### US-07 — Proibir bibliotecas copiadas manualmente {#us-07}

**Contexto.**  
JS, PHP, DLLs, JARs copiados diretamente para o repo escapam ao SBOM e ao SCA, criando *shadow dependencies*.

**📖 Rationale científico.**  
Ainda é comum encontrar JS, DLLs ou PHP copiados diretamente para o repositório.  
Este “atalho” mina completamente SBOM e SCA, criando *shadow dependencies*.  
**SSDF PW.4**, **SAMM Governance** e **BSIMM CMVM1.1** classificam esta prática como falha grave.  
Além do risco de segurança, há o custo: sem package manager não há atualização automática, nem gestão de licenças. O resultado é dívida técnica e riscos ocultos.

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

**Artefactos.**
- `package.json` / `pom.xml` / `composer.json`  
- Logs de build (resolução via repos internos)

**Proporcionalidade por risco.**
| Nível | Obrigatório? | Ajustes |
|---|---|---|
| L1 | Sim | Política documentada |
| L2 | Sim | Auditorias periódicas |
| L3 | Sim | Enforcement automático em CI/CD

**Integração no SDLC.**
| Fase | Gatilho | Responsável |
|---|---|---|
| Dev | Inclusão de nova lib | Developer + AppSec

**Ligações úteis.**  
- Guia “Bibliotecas locais: riscos e substituição”

---

### US-08 — Automação da atualização com avaliação de impacto {#us-08}

**Contexto.**  
Dependências degradam com o tempo; é necessário atualizar **com segurança e rapidez**.  
Ferramentas modernas avaliam **impacto** (semver, *release notes*, *diffs*, cobertura de testes) e:
- **abrem PRs automáticos** com *auto‑merge* quando a alteração é segura (*patch/minor* sem impacto, testes verdes, *gates* OK);
- **marcam como requires‑human** quando há impacto (API quebrada, *major*), anexando *guidelines* de *refactor*.

**📖 Rationale científico.**  
Atualizar não é apenas “ficar na última versão”: é equilibrar rapidez com segurança.  
**SSDF PW.7/RV.3**, **BSIMM CMVM4.2** e práticas DSOMM apontam para automação com *impact analysis*.  
Ferramentas modernas (Renovate, Dependabot, Xygeni etc.) conseguem abrir PRs automáticos quando não há impacto, e pedir ajuda humana quando há *breaking changes*.  
Estudos da GitHub e Sonatype mostram que estas práticas reduzem o *time-to-fix* em mais de 40%, sem sacrificar estabilidade.  
Na prática, isto transforma o dilema “atualizamos já ou esperamos?” num processo contínuo, transparente e auditável.

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
| Fase | Gatilho | Responsável |
|---|---|---|
| Dev/CI | Nova versão publicada | DevOps + Developer + QA

**Ligações úteis.**  
- Guia de operação de bots (labels, *auto‑merge*, *canary*)

---

## 📦 Artefactos esperados {cap05:aplicacao-lifecycle#artefactos}

| Artefacto | Evidência |
|-----------|-----------|
| `dependencies-approval.md` | Lista aprovada |
| `sbom.json` / `sbom.xml` | Inventário por build |
| `sca-report.html/json` | Vulnerabilidades e *gates* |
| `excecoes.yaml` | Exceções formais |
| `releases.md` | Decisões *go/no-go* |
| `repo-config.yaml` | Repos internos configurados |
| **PRs de bots** | *Labels* de impacto, logs e testes |

---

## ⚖️ Matriz de proporcionalidade L1–L3 {cap05:aplicacao-lifecycle#proporcionalidade}

| Prática | L1 | L2 | L3 |
|---------|----|----|----|
| SBOM | Básico | Completo por release | Assinado + integridade |
| SCA | Aviso | Bloqueio High/Critical | Bloqueio Medium+ |
| Pinning | Recomendado | Obrigatório | Obrigatório + proveniência |
| Exceções | Simples | Formais + revisão | Formais + validação executiva |
| Repositório interno | Recomendado | Obrigatório | Obrigatório + assinatura |
| Bibliotecas copiadas | Proibidas (política) | Auditoria periódica | Enforcement CI/CD |
| Bots + impacto | Opcional | Ativos + *auto‑merge patch* | Ativos + *impact analysis* + *canary* |

---

## 🏁 Recomendações finais {cap05:aplicacao-lifecycle#recomendacoes}

- **SBOM** como documento vivo (por build).  
- **SCA automatizado** com *gates* proporcionais ao risco.  
- **Repositórios internos** como fonte única de confiança.  
- **Exceções formais** e temporárias com mitigação.  
- **Eliminar bibliotecas copiadas manualmente** do repo.  
- **Bots com avaliação de impacto**: PRs seguros *auto‑merge*; alterações com impacto ⇒ **revisão humana**, *canary* e promoção por estágios (sobretudo em L3).

