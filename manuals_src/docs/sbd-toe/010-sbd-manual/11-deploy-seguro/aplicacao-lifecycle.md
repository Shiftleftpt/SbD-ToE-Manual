---
id: aplicacao-lifecycle
title: Como Fazer
description: Integração prática das práticas de release e deploy seguro no ciclo de vida de software
tags: [tipo:aplicacao, ciclo-vida, deploy, release, rollback, gates, producao]
genia: us-format-normalization
---

# 🚀 Aplicação de Deploy Seguro no Ciclo de Vida

## 🧭 Quando aplicar

Um deploy seguro não acontece de repente: é o culminar de várias etapas críticas que vão desde a construção do artefacto até à auditoria pós-release.  
Cada fase tem riscos específicos e, por isso, precisa de controlos próprios e evidências claras.  

A tabela seguinte mostra onde cada prática deve ser aplicada e como comprovar a sua execução:

| Fase SDLC / Evento | Ação | Evidência |
|--------------------|------|-----------|
| Build | Garantir artefacto assinado e versionado | Assinatura + SBOM |
| Pré-release | Validação em staging + gates | Relatórios de validação |
| Deploy | Execução de pipeline com rollback preparado | Logs de deploy |
| Pós-release | Monitorização de saúde e integridade | Métricas + alertas |
| Auditoria | Revisão de rastreabilidade end-to-end | Relatórios de auditoria |

---

## 👥 Quem executa cada ação

A responsabilidade por um deploy seguro é necessariamente partilhada.  
Não existe um “dono único”: cada papel contribui com uma parte da garantia de integridade.  
O quadro seguinte clarifica esta divisão:

| Papel | Responsabilidade |
|-------|------------------|
| **Dev** | Produzir artefactos prontos a deploy |
| **QA/Testes** | Validar staging, critérios de aceitação |
| **AppSec** | Aprovar gates e gerir exceções |
| **DevOps/SRE** | Executar pipelines, rollback e monitorização |
| **Gestão de Produto** | Decidir go/no-go, aceitar risco residual |

---

## 📖 User Stories Reutilizáveis

As histórias seguintes descrevem **cenários típicos de risco no deploy** e como devem ser tratados de forma consistente.  
Ao formalizá-las em backlog, a organização consegue alinhar papéis, práticas e evidências de forma auditável.

### US-01 - Deploy apenas de artefactos assinados

A integridade começa pela proveniência: se não controlarmos a origem, todo o processo é vulnerável.  

**Contexto.** Deploys de artefactos não confiáveis comprometem todo o sistema.  

:::userstory
**História.**   
Como **DevOps/SRE**, quero **executar deploy apenas de artefactos assinados e versionados**, para **assegurar integridade e rastreabilidade**.  

**Critérios de aceitação (BDD).**  
- **Dado** um pipeline de deploy  
  **Quando** um artefacto não está assinado  
  **Então** o deploy é bloqueado  

**Checklist.**  
- [ ] Assinatura validada (cosign/in-toto)  
- [ ] SBOM anexo ao artefacto  
- [ ] Proveniência verificada  

:::

**Artefactos & evidências.** Artefacto assinado + SBOM.  

**Proporcionalidade L1–L3.**  
| L1 | L2 | L3 |
|----|----|----|
| Recomendado | Obrigatório | Obrigatório + rejeição automática |

**Integração no SDLC.**  
| Fase | Trigger | Responsável | SLA |
|------|---------|-------------|-----|
| Build/Release | Produção de artefacto | DevOps/SRE | Cada release |

**Ligações úteis.** [CI/CD Seguro](/sbd-toe/sbd-manual/cicd-seguro/intro) ; [Deploy Seguro](/sbd-toe/sbd-manual/deploy-seguro/intro)  

> **Padrão Comum:** Assinatura e verificação de proveniência ocorrem em **múltiplos contextos** 
> (CI/CD, IaC, imagens container, deploy). Este US foca o contexto de **validação no deploy** onde 
> artefactos são verificados antes de serem promovidos; ver também [Cap 07-US-06: Assinatura e 
> proveniência em artefactos CI/CD], [Cap 08-US-09: Assinatura de módulos IaC], e [Cap 09-US-03: 
> Assinatura de imagens container]. Todos aplicam o **mesmo princípio** (sign → validate → use).

---

### US-02 - Validação em staging antes da promoção

Staging é o "ensaio geral": sem ele, a produção torna-se campo de teste.  

**Contexto.** Promover diretamente à produção aumenta risco de incidentes.  

:::userstory
**História.**   
Como **QA/Testes**, quero **validar releases em staging com ambiente segregado, dados controlados e testes funcionais + segurança**, para **garantir readiness sem expor dados reais**.  

**Critérios de aceitação (BDD).**  
- **Dado** environment staging idêntico a produção (mesmas versões, configuração)  
  **Quando** executo validações (funcionais + DAST + SBOM check)  
  **Então** apenas releases aprovadas por QA e AppSec seguem para produção  
- E staging tem dados mascarados/fictícios (nunca dados reais)  
- E acesso a staging é segregado (MFA, RBAC)

**Checklist.**  
- [ ] Ambiente staging com infraestrutura equivalente a produção  
- [ ] Dados de teste (sem dados reais, mascarados)  
- [ ] Testes funcionais regressivos executados  
- [ ] DAST autenticado concluído  
- [ ] SBOM validado (sem dependências maliciosas)  
- [ ] Acesso segregado (MFA, permissões por papel)  
- [ ] Relatório de validação anexado à release  
- [ ] Aprovação formal registada (QA + AppSec)

:::

**Artefactos & evidências.** Relatórios de staging.  

**Proporcionalidade L1–L3.**  
| L1 | L2 | L3 |
|----|----|----|
| Opcional | Recomendado | Obrigatório |

**Integração no SDLC.**  
| Fase | Trigger | Responsável | SLA |
|------|---------|-------------|-----|
| Pré-release | Preparação para produção | QA/Testes | Cada release |

**Ligações úteis.** [Testes de Segurança](/sbd-toe/sbd-manual/testes-seguranca/intro)  

---

### US-03 - Gates de aprovação no deploy

Sem gates, a promoção a produção torna-se uma aposta: e a segurança não pode ser um jogo de sorte.  

**Contexto.** Releases sem gates podem promover código inseguro.  

:::userstory
**História.**   
Como **AppSec**, quero **definir gates automáticos e thresholds no deploy**, para **bloquear releases inseguras**.  

**Critérios de aceitação (BDD).**  
- **Dado** uma release candidata  
  **Quando** findings críticos não estão resolvidos  
  **Então** o deploy é bloqueado até aprovação formal  

**Checklist.**  
- [ ] Gates automáticos configurados  
- [ ] Thresholds documentados  
- [ ] Exceções registadas e aprovadas  

:::

**Artefactos & evidências.** Configuração pipeline + registo de exceções.  

**Proporcionalidade L1–L3.**  
| L1 | L2 | L3 |
|----|----|----|
| Aviso | Bloqueio High/Critical | Bloqueio Medium+ |

**Integração no SDLC.**  
| Fase | Trigger | Responsável | SLA |
|------|---------|-------------|-----|
| Release | Promoção a produção | AppSec + DevOps | Cada release |

**Ligações úteis.** [CI/CD Seguro](/sbd-toe/sbd-manual/cicd-seguro/intro) ; [Testes de Segurança](/sbd-toe/sbd-manual/testes-seguranca/intro)  

---

### US-04 - Rollback rápido e testado

Falhas acontecem. A diferença entre crise e resiliência está em quão rápido conseguimos voltar atrás.  

**Contexto.** Sem rollback seguro, falhas em produção ampliam impacto.  

:::userstory
**História.**   
Como **DevOps/SRE**, quero **rollback rápido e testado periodicamente**, para **reverter releases problemáticas**.  

**Critérios de aceitação (BDD).**  
- **Dado** um incidente em produção  
  **Quando** aciono rollback  
  **Então** a versão anterior é restaurada automaticamente  

**Checklist.**  
- [ ] Rollback automatizado configurado  
- [ ] Testes de rollback trimestrais  
- [ ] Evidência documentada  

:::

**Artefactos & evidências.** Logs de rollback + relatórios.  

**Proporcionalidade L1–L3.**  
| L1 | L2 | L3 |
|----|----|----|
| Manual | Automatizado | Automatizado + testado periodicamente |

**Integração no SDLC.**  
| Fase | Trigger | Responsável | SLA |
|------|---------|-------------|-----|
| Produção | Incidente ou falha | DevOps/SRE | ≤ 1h |

**Ligações úteis.** [Monitorização & Operações](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro)

---

### US-05 - Rastreabilidade end-to-endSe não for possível reconstituir o caminho desde o commit até ao deploy, não existe governação real.  

**Contexto.** Sem rastreabilidade, não é possível auditar incidentes.  

:::userstory
**História.**   
Como **Gestão de Produto**, quero **garantir rastreabilidade entre commit → build → release → deploy**, para **auditar e justificar decisões de risco**.  

**Critérios de aceitação (BDD).**  
- **Dado** incidente pós-release  
  **Quando** audito histórico  
  **Então** consigo traçar origem até commit inicial  

**Checklist.**  
- [ ] Logs versionados  
- [ ] Relatórios anexados  
- [ ] Auditoria concluída  

:::

**Artefactos & evidências.** Registo de rastreabilidade, logs CI/CD.  

**Proporcionalidade L1–L3.**  
| L1 | L2 | L3 |
|----|----|----|
| Básica | Completa | Completa + auditoria contínua |

**Integração no SDLC.**  
| Fase | Trigger | Responsável | SLA |
|------|---------|-------------|-----|
| Auditoria | Incidente ou revisão periódica | Gestão + AppSec | Anual |

**Ligações úteis.** [Requisitos de Segurança](/sbd-toe/sbd-manual/requisitos-seguranca/intro) ; [CI/CD Seguro](/sbd-toe/sbd-manual/cicd-seguro/intro)  

---

### US-06 - Monitorização pós-deploy

Um deploy não termina no *merge*: só se considera concluído quando a versão está estável e visível em produção.  

**Contexto.** Deploys inseguros podem originar falhas não detetadas.  

:::userstory
**História.**   
Como **DevOps/SRE**, quero **ativar monitorização pós-deploy**, para **detetar anomalias e regressões em tempo real**.  

**Critérios de aceitação (BDD).**  
- **Dado** nova versão em produção  
  **Quando** ocorre anomalia  
  **Então** alertas são gerados automaticamente  

**Checklist.**  
- [ ] Dashboards atualizados  
- [ ] Alertas configurados  
- [ ] Processo de resposta definido  

:::

**Artefactos & evidências.** Logs + métricas de saúde.  

**Proporcionalidade L1–L3.**  
| L1 | L2 | L3 |
|----|----|----|
| Básica | Crítica | Completa + resposta automática |

**Integração no SDLC.**  
| Fase | Trigger | Responsável | SLA |
|------|---------|-------------|-----|
| Pós-release | Entrada em produção | DevOps/SRE | ≤ 15 min |

**Ligações úteis.** [Monitorização & Operações](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro)

---

### US-07 - Controlo de Execução com Feature FlagsA capacidade de ativar ou desativar funcionalidades em produção sem novo deploy é essencial para mitigar riscos e responder rapidamente a incidentes.

**Contexto.** Sem controlo dinâmico, cada problema requer novo deploy e rollback, amplificando impacto.

:::userstory
**História.**  
Como **DevOps/AppSec**, quero **implementar feature flags com metadados, owner e expiração**, para **permitir ativação/desativação dinâmica de funcionalidades sem novo deploy e com rastreabilidade completa**.

**Critérios de aceitação (BDD).**  
- **Dado** que uma funcionalidade nova é entregue  
  **Quando** a flag está ativa  
  **Então** a funcionalidade é visível e controlada por regras de âmbito (ambiente, grupo, geo)  
- E cada alteração de flag é auditada (quem, quando, porquê)  
- E flags expiradas são automaticamente desativadas

**Checklist.**  
- [ ] Flags com metadados (owner, expiração, justificação)  
- [ ] Flags versionadas como código (YAML/JSON)  
- [ ] Validação de PRs com aprovação para flags críticas  
- [ ] Logs de ativação/desativação em sistema de auditoria  
- [ ] Kill switch configurado para funcionalidades sensíveis  
- [ ] Testes de fallback para cada toggle crítico  

:::

**Artefactos & evidências.** Configuração de flags (versionada no repo), logs de auditoria, relatório de flags expiradas.

**Proporcionalidade L1–L3.**  
| L1 | L2 | L3 |
|----|----|----|
| Opcional | Recomendado | Obrigatório |

**Integração no SDLC.**  
| Fase | Trigger | Responsável | SLA |
|------|---------|-------------|-----|
| Deploy/Produção | Ativação de funcionalidade | DevOps + AppSec | Imediato |

**Ligações úteis.** [Monitorização & Operações](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro)

---

### US-08 - Gestão Segura de Segredos no DeploySegredos embebidos em artefactos criam exposição que é difícil revogar e reforçam risco de supply chain.

**Contexto.** Credenciais em imagens amplificam impacto de vazamento e complicam rotação.

:::userstory
**História.**  
Como **DevOps/AppSec**, quero **garantir que segredos nunca são embebidos em artefactos de deploy**, para **reduzir exposição e permitir rotação dinâmica sem novo deploy**.

**Critérios de aceitação (BDD).**  
- **Dado** um pipeline de deploy  
  **Quando** artefacto é construído  
  **Então** secret scanning bloqueia credenciais embebidas  
- E credenciais são injetadas apenas em runtime via cofre de segredos  
- E acesso a segredos é auditado com OIDC/Workload Identity  

**Checklist.**  
- [ ] Secret scanning ativo em CI (trivy, gitleaks, truffleHog)  
- [ ] Pipeline falha se credenciais detectadas  
- [ ] Segredos injetados via variáveis de ambiente/volumes seguros  
- [ ] OIDC ou Workload Identity configurado (sem chaves de longa duração)  
- [ ] Rotação de segredos documentada (TTL, política de expiração)  
- [ ] Auditoria de acesso a segredos centralizada  

:::

**Artefactos & evidências.** Logs de secret scanning, configuração de injeção de segredos, relatório de auditoria de acesso.

**Proporcionalidade L1–L3.**  
| L1 | L2 | L3 |
|----|----|----|
| Recomendado | Obrigatório | Obrigatório + rotação automática |

**Integração no SDLC.**  
| Fase | Trigger | Responsável | SLA |
|------|---------|-------------|-----|
| Build/Deploy | Build de artefacto | DevOps + AppSec | Cada build |

**Ligações úteis.** [CI/CD Seguro](/sbd-toe/sbd-manual/cicd-seguro/intro)  

---

### US-09 - Versionamento Semântico e Changelog Técnico

A comunicação clara das alterações em cada release é essencial para decisões informadas sobre aceitação de risco e para auditorias pós-incidente.

**Contexto.** Sem changelog estruturado, não há forma de comunicar riscos de compatibilidade ou vulnerabilidades corrigidas.

:::userstory
**História.**  
Como **Dev/Gestão**, quero **manter versionamento semântico com changelog técnico e de segurança**, para **comunicar claramente as alterações, riscos e compatibilidade de cada release**.

**Critérios de aceitação (BDD).**  
- **Dado** uma release nova  
  **Quando** é criada tag de versão  
  **Então** versão segue semântico (MAJOR.MINOR.PATCH)  
- E changelog lista alterações técnicas (breaking changes, CVEs corrigidas, dependências)  
- E changelog de segurança destaca problemas resolvidos com severidade  

**Checklist.**  
- [ ] Versionamento semântico aplicado (vX.Y.Z)  
- [ ] Changelog técnico atualizado por release  
- [ ] Changelog de segurança destacando CVEs e mitigações  
- [ ] Owner de release definido e registado  
- [ ] Hash de commit e data associados à versão  
- [ ] Documento de compatibilidade / breaking changes se aplicável  

:::

**Artefactos & evidências.** `CHANGELOG.md` versionado, Git tags com metadata, relatório de breaking changes.

**Proporcionalidade L1–L3.**  
| L1 | L2 | L3 |
|----|----|----|
| Básico | Completo + segurança | Completo + segurança + compatibilidade |

**Integração no SDLC.**  
| Fase | Trigger | Responsável | SLA |
|------|---------|-------------|-----|
| Release | Criação de release | Dev + Gestão | Cada versão |

**Ligações úteis.** [Requisitos de Segurança](/sbd-toe/sbd-manual/requisitos-seguranca/intro)  

---

### US-10 - Deploy Progressivo com Estratégias Canary/Blue-Green

O deploy para 100% de utilizadores simultaneamente aumenta risco de incidente generalizado. Progressividade permite detetar falhas com impacto reduzido.

**Contexto.** Deploy para 100% simultaneamente amplifica impacto de qualquer falha ou regressão.

:::userstory
**História.**  
Como **DevOps/Gestão**, quero **implementar deploy progressivo (canary, blue/green, staging rules)**, para **mitigar risco e permitir rollback rápido com impacto minimizado**.

**Critérios de aceitação (BDD).**  
- **Dado** uma release candidata com plano de rollout  
  **Quando** inicia deploy  
  **Então** a versão é promovida gradualmente (ex: 1% → 5% → 20% → 100%)  
- E cada etapa é monitorizada antes da promoção automática ou manual  
- E existe critério de bloqueio (latência, erros 5xx, alertas segurança)  
- E rollback é possível em cada etapa sem impacto generalizado  

**Checklist.**  
- [ ] Estratégia de rollout documentada (Canary % ou Blue/Green com validação)  
- [ ] Métricas de sucesso por etapa definidas (baseline vs canary)  
- [ ] Critérios de bloqueio parametrizados (e.g., latência > 500ms = rollback automático)  
- [ ] Testes em canary validados antes promoção para general availability  
- [ ] Rollback automático ativado por threshold ou manual por owner  
- [ ] Comunicação de estado de rollout em dashboard (ex: Spinnaker, Argo)  
- [ ] Papéis de decisão claros (who approves promoção entre etapas)  

:::

**Artefactos & evidências.**  
Configuração de rollout (Spinnaker, Argo Rollouts, Flagger, ou documentação manual), métricas baseline vs canary, logs de eventos de rollout, dashboard com estado em tempo real.

**Proporcionalidade L1–L3.**  
| L1 | L2 | L3 |
|----|----|----|
| Recomendado (manual por etapas) | Automatizado com métricas | Automatizado + threshold-triggered rollback |

**Integração no SDLC.**  
| Fase | Trigger | Responsável | SLA |
|------|---------|-------------|-----|
| Deploy | Promoção a produção | DevOps + QA | Per etapa ≤ 30 min |

**Ligações úteis.** [Monitorização & Operações](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro)

---

### US-11 - Validações Técnicas Pré-Deploy com Gates CondicionaisSem validações estruturadas antes de deploy, código inseguro ou não-funcional pode alcançar produção.

**Contexto.** Validações inadequadas comprometem integridade de produção.

:::userstory
**História.**  
Como **AppSec/QA**, quero **executar validações técnicas (SAST, DAST, SBOM, análise de findings) com gates condicionais por risco**, para **bloquear automaticamente releases inseguras**.

**Critérios de aceitação (BDD).**  
- **Dado** uma release candidata  
  **Quando** pipeline de deploy inicia  
  **Então** executa SAST + DAST + verificação de dependências (Semgrep, trivy, CycloneDX)  
- E gera relatório de findings com severidade  
- E bloqueia deploy se:
  - L1: Críticos abertos
  - L2: High/Critical abertos  
  - L3: Medium+ abertos
- E exceptuando com aprovação formal de AppSec

**Checklist.**  
- [ ] SAST configurado (SonarQube, Semgrep ou similar)  
- [ ] DAST autenticado em staging  
- [ ] SBOM gerado (CycloneDX, Syft) + validado  
- [ ] Análise de dependências (OWASP Dependency Check)  
- [ ] Findings com decisão justificada (accepted, mitigated, false positive)  
- [ ] Gates parametrizados por risco L1–L3  
- [ ] Exceções registadas com owner + justificativa + data de revisão  
- [ ] Relatório de validação anexado a cada release  

:::

**Artefactos & evidências.**  
Relatório SAST + DAST, SBOM (CycloneDX XML/JSON), lista de findings com status, logs de gates (bloqueios, aprovações, exceções), configuração de pipeline (versionada).

**Proporcionalidade L1–L3.**  
| L1 | L2 | L3 |
|----|----|----|
| SAST + Aviso | SAST + DAST + bloqueio High/Critical | SAST + DAST + bloqueio Medium+ |

**Integração no SDLC.**  
| Fase | Trigger | Responsável | SLA |
|------|---------|-------------|-----|
| Pre-release | Validação staging/produção | AppSec + DevOps | ≤ 30 min |

**Ligações úteis.** [Testes de Segurança](/sbd-toe/sbd-manual/testes-seguranca/intro)  

---

### US-12 - Rollback Estruturado por Tipo (Binário, Config, BD, Infra)

Nem todos os rollbacks são iguais. Sem plano específico por tipo, reversão fica manual e arriscada.

**Contexto.** Rollbacks não planeados amplificam tempo de recuperação e risco de inconsistência.

:::userstory
**História.**  
Como **DevOps/SRE**, quero **documentar e testar rollback para cada tipo de alteração (binário, config, BD, infraestrutura)**, para **reverter incidentes rapidamente com confiança**.

**Critérios de aceitação (BDD).**  
- **Dado** incidente em produção  
  **Quando** aciono rollback  
- Então:
  - Se é binário: versão anterior restaurada (segundos)
  - Se é config: feature flag desativada ou variável revertida (< 1 min)
  - Se é BD: migração revertida ou snapshot restaurado (minutos)
  - Se é infra: Terraform/Helm rollback ativado (minutos)
- E rastreio de rollback registado (quem, quando, versão anterior, versão alvo)

**Checklist.**  
- [ ] Plano de rollback por tipo documentado e revisado  
- [ ] Rollback binário: tag Git anterior identificada + testada  
- [ ] Rollback config: feature flags ou secrets manager para revert rápido  
- [ ] Rollback BD: script reverso ou snapshot testado  
- [ ] Rollback infra: Terraform/Helm com estado conhecido e testado  
- [ ] Testes de rollback executados trimestrais (evidência documentada)  
- [ ] SLA por tipo definido e comunicado  
- [ ] Processo de aprovação e auditoria de rollback  

:::

**Artefactos & evidências.**  
Procedimentos de rollback (1 por tipo), logs de testes trimestrais, evidência de reversão em BD (migrações reversas), configuração IaC com rollback (Terraform/Helm), auditoria de rollbacks executados.

**Proporcionalidade L1–L3.**  
| L1 | L2 | L3 |
|----|----|----|
| Manual documentado | Automatizado (binário + config) | Automatizado todos os tipos + testado |

**Integração no SDLC.**  
| Fase | Trigger | Responsável | SLA |
|------|---------|-------------|-----|
| Incidente | Falha em produção | DevOps/SRE | ≤ 15 min |

**Ligações úteis.** [Monitorização & Operações](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro)

---

## 📦 Artefactos esperadosCada prática deve deixar um **rasto verificável**.  
Estes artefactos constituem a evidência objetiva necessária para auditorias e conformidade:

| Artefacto | Evidência |
|-----------|-----------|
| Artefacto assinado + SBOM | Proveniência validada |
| Relatórios staging | Testes funcionais + DAST + segregação de dados |
| Configuração de gates | Pipeline versionado |
| Logs de rollback | Evidência de reversão |
| Rastreabilidade end-to-end | Commit → release |
| Monitorização pós-deploy | Dashboards + alertas |
| Configuração de feature flags | Versionada (YAML/JSON) + logs de auditoria |
| Logs de secret scanning | Bloqueios em CI + artefactos limpos |
| CHANGELOG.md e Git tags | Versionamento + metadata de release |
| Configuração de rollout progressivo | Spinnaker, Argo, Flagger ou documentação com métricas |
| Validações técnicas pré-deploy | SAST, DAST, SBOM, findings com decisão + relatório |
| Procedimentos rollback por tipo | Manual ou IaC (Terraform/Helm) + testes trimestrais |

---

## ⚖️ Matriz de proporcionalidade L1–L3

Nem todas as aplicações exigem o mesmo nível de controlo.  
A proporcionalidade permite adaptar rigor sem comprometer segurança:  

| Prática | L1 | L2 | L3 |
|---------|----|----|----|
| Deploy de artefactos assinados | Recomendado | Obrigatório | Obrigatório + rejeição automática |
| Validação em staging | Opcional | Recomendado | Obrigatório |
| Gates de aprovação | Aviso | Bloqueio High/Critical | Bloqueio Medium+ |
| Rollback | Manual | Automatizado | Automatizado + testado |
| Rastreabilidade | Básica | Completa | Completa + auditoria |
| Monitorização | Básica | Crítica | Completa + resposta automática |
| Feature flags e toggles | Opcional | Recomendado | Obrigatório |
| Gestão de segredos (OIDC/Workload Identity) | Recomendado | Obrigatório | Obrigatório + rotação automática |
| Versionamento semântico e changelog | Básico | Completo + segurança | Completo + segurança + compatibilidade |
| Deploy progressivo (Canary/Blue-Green) | Recomendado (manual) | Automatizado com métricas | Automatizado + threshold-triggered rollback |
| Validações técnicas pré-deploy | SAST + Aviso | SAST + DAST + bloqueio High/Critical | SAST + DAST + bloqueio Medium+ |
| Rollback por tipo (binário, config, BD, infra) | Manual documentado | Automatizado (binário + config) | Automatizado todos os tipos + testado |

---

## 🏁 Recomendações finais

- **Nunca promover diretamente** para produção sem staging.  
- **Automatizar deploys, rastrear e reverter** sempre que necessário.  
- **Rollback testado regularmente** assegura resiliência.  
- **Monitorização pós-deploy** deve estar integrada com resposta a incidentes (Cap. 12).  
- **Aplicar proporcionalidade L1–L3** garante equilíbrio entre custo e risco.  
