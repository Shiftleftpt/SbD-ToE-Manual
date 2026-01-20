---
id: aplicacao-lifecycle
title: Como Fazer
description: Integração prática das práticas de release e deploy seguro no ciclo de vida de software
tags: [tipo:aplicacao, ciclo-vida, deploy, release, rollback, gates, producao]
genia: us-format-normalization
---

# 🚀 Aplicação de Deploy Seguro no Ciclo de Vida

## 🧭 Quando aplicar

Um *deploy* seguro não acontece de repente: é o culminar de várias etapas críticas, desde a construção do artefacto até à auditoria pós-*release*.  
Cada fase tem riscos específicos e, por isso, exige controlos próprios e evidências claras.

A tabela seguinte mostra onde cada prática deve ser aplicada e como comprovar a sua execução:

| Fase SDLC / Evento | Ação | Evidência |
|--------------------|------|-----------|
| Build | Garantir artefacto assinado e versionado | Assinatura + SBOM |
| Pré-release | Validação em *staging* + *gates* | Relatórios de validação |
| Deploy | Execução de pipeline com *rollback* preparado | Logs de deploy |
| Pós-release | Monitorização de saúde e integridade | Métricas + alertas |
| Auditoria | Revisão de rastreabilidade *end-to-end* | Relatórios de auditoria |

---

## 👥 Quem executa cada ação

A responsabilidade por um *deploy* seguro é necessariamente partilhada.  
Não existe um “dono único”: cada papel contribui com uma parte da garantia de integridade.  
O quadro seguinte clarifica esta divisão:

| Papel | Responsabilidade |
|-------|------------------|
| **Dev** | Produzir artefactos prontos a *deploy* |
| **QA/Testes** | Validar *staging*, critérios de aceitação |
| **AppSec** | Aprovar *gates* e gerir exceções |
| **DevOps/SRE** | Executar pipelines, *rollback* e monitorização |
| **Gestão de Produto** | Decidir *go/no-go*, aceitar risco residual |

---

## 📖 User Stories Reutilizáveis

As histórias seguintes descrevem cenários típicos de risco no *deploy* e como devem ser tratados de forma consistente.  
Ao formalizá-las em *backlog*, a organização consegue alinhar papéis, práticas e evidências de forma auditável.

---

### US-01 - Deploy apenas de artefactos assinados

A integridade começa pela proveniência: se não controlarmos a origem, todo o processo fica vulnerável.

**Contexto.** *Deploys* de artefactos não confiáveis comprometem todo o sistema.

:::userstory
**História.**  
Como **DevOps/SRE**, quero **executar *deploy* apenas de artefactos assinados e versionados**, para **assegurar integridade e rastreabilidade**.

**Critérios de aceitação (BDD).**  
- **Dado** um pipeline de *deploy*  
  **Quando** um artefacto não está assinado  
  **Então** o *deploy* é bloqueado

**Checklist.**  
- [ ] Assinatura validada (ex.: cosign / in-toto)  
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

> **Padrão comum:** assinatura e verificação de proveniência ocorrem em múltiplos contextos (CI/CD, IaC, imagens *container*, *deploy*).  
> Este US foca o contexto de validação no *deploy*, onde artefactos são verificados antes de serem promovidos; ver também os US equivalentes nos capítulos 07, 08 e 09 (mesmo princípio: *sign → validate → use*).

---

### US-02 - Validação em *staging* antes da promoção

*Staging* é o “ensaio geral”: sem ele, a produção torna-se campo de teste.

**Contexto.** Promover diretamente à produção aumenta o risco de incidentes.

:::userstory
**História.**  
Como **QA/Testes**, quero **validar *releases* em *staging* com ambiente segregado, dados controlados e testes funcionais + segurança**, para **garantir *readiness* sem expor dados reais**.

**Critérios de aceitação (BDD).**  
- **Dado** um ambiente de *staging* equivalente a produção (mesmas versões e configuração)  
  **Quando** executo validações (funcionais + DAST + verificação de SBOM)  
  **Então** apenas *releases* aprovadas por QA e AppSec seguem para produção

- **Dado** que *staging* é usado para validar *releases*  
  **Quando** preparo o ambiente e os dados  
  **Então** são usados apenas dados fictícios/mascarados (nunca dados reais)

- **Dado** que o ambiente de *staging* contém dados de teste e credenciais  
  **Quando** concedo acessos  
  **Então** o acesso é segregado (MFA + RBAC) e auditável

**Checklist.**  
- [ ] Ambiente de *staging* com infraestrutura equivalente a produção  
- [ ] Dados de teste (sem dados reais; mascarados/fictícios)  
- [ ] Testes funcionais e regressivos executados  
- [ ] DAST autenticado concluído  
- [ ] SBOM validado (sem dependências maliciosas / não conformes)  
- [ ] Acesso segregado (MFA, permissões por papel)  
- [ ] Relatório de validação anexado à *release*  
- [ ] Aprovação formal registada (QA + AppSec)
:::

**Artefactos & evidências.** Relatórios de *staging*.

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

### US-03 - *Gates* de aprovação no *deploy*

Sem *gates*, a promoção a produção torna-se uma aposta — e a segurança não pode ser um jogo de sorte.

**Contexto.** *Releases* sem *gates* podem promover código inseguro.

:::userstory
**História.**  
Como **AppSec**, quero **definir *gates* automáticos e *thresholds* no *deploy***, para **bloquear *releases* inseguras**.

**Critérios de aceitação (BDD).**  
- **Dado** uma *release* candidata  
  **Quando** existem *findings* críticos não resolvidos  
  **Então** o *deploy* é bloqueado até decisão formal (correção ou exceção aprovada)

**Checklist.**  
- [ ] *Gates* automáticos configurados  
- [ ] *Thresholds* documentados  
- [ ] Exceções registadas e aprovadas
:::

**Artefactos & evidências.** Configuração de pipeline + registo de exceções.

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

### US-04 - *Rollback* rápido e testado

Falhas acontecem. A diferença entre crise e resiliência está em quão rápido conseguimos voltar atrás.

**Contexto.** Sem *rollback* seguro, falhas em produção ampliam o impacto.

:::userstory
**História.**  
Como **DevOps/SRE**, quero **ter *rollback* rápido e testado periodicamente**, para **reverter *releases* problemáticas**.

**Critérios de aceitação (BDD).**  
- **Dado** um incidente em produção  
  **Quando** aciono *rollback*  
  **Então** a versão anterior é restaurada de forma controlada e com evidência registada

**Checklist.**  
- [ ] *Rollback* automatizado configurado  
- [ ] Testes de *rollback* trimestrais  
- [ ] Evidência documentada
:::

**Artefactos & evidências.** Logs de *rollback* + relatórios.

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

### US-05 - Rastreabilidade *end-to-end*

Se não for possível reconstituir o caminho desde o *commit* até ao *deploy*, não existe governação real.

**Contexto.** Sem rastreabilidade, não é possível auditar incidentes com rigor.

:::userstory
**História.**  
Como **Gestão de Produto**, quero **garantir rastreabilidade entre *commit* → build → release → deploy**, para **auditar e justificar decisões de risco**.

**Critérios de aceitação (BDD).**  
- **Dado** um incidente pós-release  
  **Quando** audito o histórico  
  **Então** consigo traçar a origem até ao *commit* inicial e aos artefactos produzidos

**Checklist.**  
- [ ] Logs preservados e correlacionáveis (build/release/deploy)  
- [ ] Relatórios anexados à *release*  
- [ ] Auditoria concluída e registada
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

Um *deploy* não termina no *merge*: só se considera concluído quando a versão está estável e visível em produção.

**Contexto.** *Deploys* inseguros podem originar falhas não detetadas.

:::userstory
**História.**  
Como **DevOps/SRE**, quero **ativar monitorização pós-deploy**, para **detetar anomalias e regressões em tempo real**.

**Critérios de aceitação (BDD).**  
- **Dado** uma nova versão em produção  
  **Quando** ocorre uma anomalia relevante (erros, latência, integridade)  
  **Então** são gerados alertas automáticos com encaminhamento para resposta

**Checklist.**  
- [ ] *Dashboards* atualizados  
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

### US-07 - Controlo de execução com *feature flags*

A capacidade de ativar ou desativar funcionalidades em produção sem novo *deploy* é essencial para mitigar riscos e responder rapidamente a incidentes.

**Contexto.** Sem controlo dinâmico, cada problema exige novo *deploy* ou *rollback*, amplificando o impacto.

:::userstory
**História.**  
Como **DevOps/AppSec**, quero **implementar *feature flags* com metadados, *owner* e expiração**, para **permitir ativação/desativação dinâmica de funcionalidades sem novo *deploy* e com rastreabilidade completa**.

**Critérios de aceitação (BDD).**  
- **Dado** que uma funcionalidade nova é entregue  
  **Quando** a *flag* está ativa  
  **Então** a funcionalidade é controlada por regras de âmbito (ambiente, grupo, geo) e registada em auditoria

- **Dado** que uma *flag* é alterada  
  **Quando** a alteração é aplicada  
  **Então** é registado quem alterou, quando e porquê

- **Dado** que uma *flag* tem expiração definida  
  **Quando** a expiração é atingida  
  **Então** a *flag* é automaticamente desativada e reportada

**Checklist.**  
- [ ] *Flags* com metadados (owner, expiração, justificação)  
- [ ] *Flags* versionadas como código (YAML/JSON)  
- [ ] Validação de PRs com aprovação para *flags* críticas  
- [ ] Logs de ativação/desativação em sistema de auditoria  
- [ ] *Kill switch* configurado para funcionalidades sensíveis  
- [ ] Testes de *fallback* para cada *toggle* crítico
:::

**Artefactos & evidências.** Configuração de *flags* (versionada), logs de auditoria, relatório de *flags* expiradas.

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

### US-08 - Gestão segura de segredos no *deploy*

Segredos embebidos em artefactos criam exposição difícil de revogar e amplificam risco de *supply chain*.

**Contexto.** Credenciais em imagens/artefactos aumentam o impacto de um vazamento e complicam rotação.

:::userstory
**História.**  
Como **DevOps/AppSec**, quero **garantir que segredos nunca são embebidos em artefactos de *deploy***, para **reduzir exposição e permitir rotação dinâmica sem novo *deploy***.

**Critérios de aceitação (BDD).**  
- **Dado** um pipeline de *deploy*  
  **Quando** o artefacto é construído  
  **Então** *secret scanning* bloqueia credenciais embebidas

- **Dado** que uma credencial é necessária em execução  
  **Quando** a aplicação é iniciada  
  **Então** a credencial é injetada apenas em *runtime* via cofre de segredos e com auditoria

- **Dado** que a plataforma suporta identidades de curta duração  
  **Quando** autenticamos para obter segredos  
  **Então** é usado OIDC / *workload identity* (sem chaves de longa duração)

**Checklist.**  
- [ ] *Secret scanning* ativo em CI (ex.: trivy, gitleaks, truffleHog)  
- [ ] Pipeline falha se credenciais forem detetadas  
- [ ] Segredos injetados via mecanismo seguro (*secrets manager*, volumes, env restritas)  
- [ ] OIDC / *workload identity* configurado (sem chaves persistentes)  
- [ ] Rotação de segredos documentada (TTL, política de expiração)  
- [ ] Auditoria de acesso a segredos centralizada
:::

**Artefactos & evidências.** Logs de *secret scanning*, configuração de injeção de segredos, relatório de auditoria de acesso.

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

### US-09 - Versionamento semântico e *changelog* técnico

A comunicação clara das alterações em cada *release* é essencial para decisões informadas sobre aceitação de risco e para auditorias pós-incidente.

**Contexto.** Sem *changelog* estruturado, não há forma fiável de comunicar riscos de compatibilidade ou vulnerabilidades corrigidas.

:::userstory
**História.**  
Como **Dev/Gestão**, quero **manter versionamento semântico com *changelog* técnico e de segurança**, para **comunicar claramente alterações, riscos e compatibilidade de cada *release***.

**Critérios de aceitação (BDD).**  
- **Dado** uma *release* nova  
  **Quando** é criada uma *tag* de versão  
  **Então** a versão segue semântico (MAJOR.MINOR.PATCH) e referencia o *commit* exato

- **Dado** a publicação da *release*  
  **Quando** atualizo o *changelog*  
  **Então** são registadas alterações técnicas (breaking changes, dependências, CVEs corrigidas) e notas de segurança

**Checklist.**  
- [ ] Versionamento semântico aplicado (vX.Y.Z)  
- [ ] `CHANGELOG.md` atualizado por *release*  
- [ ] Secção de segurança com CVEs/mitigações e severidade  
- [ ] *Owner* da *release* definido e registado  
- [ ] Hash de *commit* e data associados à versão  
- [ ] Documento de compatibilidade / breaking changes quando aplicável
:::

**Artefactos & evidências.** `CHANGELOG.md` versionado, *tags* Git com metadata, relatório de breaking changes (se aplicável).

**Proporcionalidade L1–L3.**  
| L1 | L2 | L3 |
|----|----|----|
| Básico | Completo + segurança | Completo + segurança + compatibilidade |

**Integração no SDLC.**  
| Fase | Trigger | Responsável | SLA |
|------|---------|-------------|-----|
| Release | Criação de *release* | Dev + Gestão | Cada versão |

**Ligações úteis.** [Requisitos de Segurança](/sbd-toe/sbd-manual/requisitos-seguranca/intro)

---

### US-10 - *Deploy* progressivo com estratégias *canary*/*blue-green*

Promover para 100% dos utilizadores simultaneamente amplifica o impacto de qualquer falha. Progressividade permite detetar regressões com risco controlado.

**Contexto.** *Deploy* imediato para 100% aumenta a probabilidade de incidente generalizado.

:::userstory
**História.**  
Como **DevOps/Gestão**, quero **implementar *deploy* progressivo (*canary*, *blue/green*, regras por etapas)**, para **mitigar risco e permitir *rollback* rápido com impacto minimizado**.

**Critérios de aceitação (BDD).**  
- **Dado** uma *release* candidata com plano de *rollout*  
  **Quando** inicio o *deploy*  
  **Então** a versão é promovida gradualmente (ex.: 1% → 5% → 20% → 100%)

- **Dado** que estou numa etapa de *rollout*  
  **Quando** avalio métricas de sucesso (erros, latência, segurança)  
  **Então** a promoção para a etapa seguinte só ocorre se critérios forem cumpridos; caso contrário, bloqueia ou reverte

- **Dado** um critério de bloqueio acionado  
  **Quando** o *threshold* é ultrapassado  
  **Então** ocorre *rollback* automático ou é exigida decisão humana conforme criticidade

**Checklist.**  
- [ ] Estratégia de *rollout* documentada (*canary* por percentagem ou *blue/green* por validação)  
- [ ] Métricas de sucesso por etapa definidas (baseline vs *canary*)  
- [ ] Critérios de bloqueio parametrizados (ex.: erro 5xx, latência, alertas)  
- [ ] Testes em *canary* validados antes de promoção geral  
- [ ] *Rollback* automático por *threshold* ou manual por *owner*  
- [ ] *Dashboard* de estado do *rollout* em tempo real  
- [ ] Papéis de decisão claros (quem aprova promoção entre etapas)
:::

**Artefactos & evidências.** Configuração de *rollout*, métricas baseline vs *canary*, logs de eventos, *dashboard* com estado.

**Proporcionalidade L1–L3.**  
| L1 | L2 | L3 |
|----|----|----|
| Recomendado (manual por etapas) | Automatizado com métricas | Automatizado + *rollback* por *threshold* |

**Integração no SDLC.**  
| Fase | Trigger | Responsável | SLA |
|------|---------|-------------|-----|
| Deploy | Promoção a produção | DevOps + QA | Por etapa ≤ 30 min |

**Ligações úteis.** [Monitorização & Operações](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro)

---

### US-11 - Validações técnicas pré-deploy com *gates* condicionais

Sem validações estruturadas antes do *deploy*, código inseguro ou não funcional pode chegar a produção.

**Contexto.** Validações inadequadas comprometem a integridade e elevam o risco operacional.

:::userstory
**História.**  
Como **AppSec/QA**, quero **executar validações técnicas (SAST, DAST, SBOM, análise de *findings*) com *gates* condicionais por risco**, para **bloquear automaticamente *releases* inseguras**.

**Critérios de aceitação (BDD).**  
- **Dado** uma *release* candidata  
  **Quando** o pipeline de *deploy* inicia  
  **Então** são executadas validações mínimas (SAST, DAST em *staging*, verificação de SBOM/dependências) e é produzido um relatório

- **Dado** o resultado das validações  
  **Quando** existem *findings* acima do limiar definido para Lx  
  **Então** o *deploy* é bloqueado, exceto se existir exceção formal aprovada

**Checklist.**  
- [ ] SAST configurado (ex.: SonarQube, Semgrep ou equivalente)  
- [ ] DAST autenticado em *staging*  
- [ ] SBOM gerado (CycloneDX/SPDX) e validado  
- [ ] Análise de dependências (CVE/licenciamento/políticas)  
- [ ] *Findings* com decisão justificada (aceite/mitigado/falso positivo)  
- [ ] *Gates* parametrizados por risco L1–L3  
- [ ] Exceções registadas com *owner*, justificação e data de revisão/expiração  
- [ ] Relatório de validação anexado a cada *release*
:::

**Artefactos & evidências.** Relatórios SAST/DAST, SBOM, lista de *findings* com estado, logs de *gates* (bloqueios, aprovações, exceções), configuração de pipeline versionada.

**Proporcionalidade L1–L3.**  
| L1 | L2 | L3 |
|----|----|----|
| SAST + aviso | SAST + DAST + bloqueio High/Critical | SAST + DAST + bloqueio Medium+ |

**Integração no SDLC.**  
| Fase | Trigger | Responsável | SLA |
|------|---------|-------------|-----|
| Pré-release | Validação antes de produção | AppSec + DevOps | ≤ 30 min |

**Ligações úteis.** [Testes de Segurança](/sbd-toe/sbd-manual/testes-seguranca/intro)

---

### US-12 - *Rollback* estruturado por tipo (binário, configuração, BD, infra)

Nem todos os *rollbacks* são iguais. Sem plano específico por tipo, a reversão tende a ser manual, lenta e arriscada.

**Contexto.** *Rollbacks* não planeados amplificam o tempo de recuperação e o risco de inconsistência.

:::userstory
**História.**  
Como **DevOps/SRE**, quero **documentar e testar *rollback* para cada tipo de alteração (binário, configuração, BD, infraestrutura)**, para **reverter incidentes rapidamente com confiança**.

**Critérios de aceitação (BDD).**  
- **Dado** um incidente em produção  
  **Quando** aciono *rollback*  
  **Então** existe um procedimento aplicável ao tipo de alteração e fica evidência registada (quem, quando, versão alvo)

- **Dado** uma alteração de BD ou infraestrutura  
  **Quando** ocorre reversão  
  **Então** existe controlo de consistência (migrações reversíveis/snapshots; estado IaC conhecido) e validação pós-*rollback*

**Checklist.**  
- [ ] Plano de *rollback* por tipo documentado e revisto  
- [ ] *Rollback* binário: *tag* Git anterior identificada + testada  
- [ ] *Rollback* de configuração: *feature flags* / variáveis revertíveis  
- [ ] *Rollback* de BD: migração reversa ou *snapshot* testado  
- [ ] *Rollback* de infra: Terraform/Helm com estado conhecido e procedimento seguro  
- [ ] Testes de *rollback* executados trimestralmente (evidência)  
- [ ] SLA por tipo definido e comunicado  
- [ ] Processo de aprovação e auditoria de *rollback*
:::

**Artefactos & evidências.** Procedimentos (1 por tipo), logs de testes trimestrais, evidência de reversão de BD, configuração IaC com reversão, auditoria de *rollbacks* executados.

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

### US-13 - Validação humana obrigatória após deploy automatizado

Um deploy automático bem-sucedido não é sinónimo de operação segura.
Esta US garante que qualquer promoção automática para produção é validada por um responsável humano.

:::userstory
**História.**  
Como **Ops/AppSec**, quero **validar explicitamente o estado de segurança após deploy automático**, para **assegurar que não existem impactos inesperados antes de considerar a release concluída**.

**Critérios de aceitação (BDD).**  
- **Dado** que um deploy automático para produção é concluído  
  **Quando** o sistema entra em estado operacional  
  **Então** existe validação humana documentada antes de fechar a release

- **Dado** que métricas ou alertas indicam comportamento anómalo  
  **Quando** a validação ocorre  
  **Então** o deploy é marcado como pendente ou revertido até análise concluída
:::

**Artefactos & evidências.** Registo de validação pós-deploy, métricas observadas, decisão final.

**Proporcionalidade.**  
L1: validação amostral  
L2: validação obrigatória  
L3: validação + aprovação dupla

**Integração no SDLC.**  
Produção | Pós-deploy | Ops/AppSec | `<`24h

---

### US-14 - Controlo e validação de drift operacional

Automação contínua introduz risco de drift silencioso entre estado desejado e real.

:::userstory
**História.**  
Como **Ops**, quero **detetar e validar drift operacional**, para **garantir que alterações automáticas ou manuais não introduzem desvios inseguros**.

**Critérios de aceitação (BDD).**  
- **Dado** um estado desejado definido  
  **Quando** ocorre drift em produção  
  **Então** o desvio é registado, analisado e validado antes de correção automática
:::

**Artefactos & evidências.** Relatórios de drift, decisão humana, histórico de correções.

**Proporcionalidade.**  
L1: alerta  
L2: validação obrigatória  
L3: bloqueio até validação

**Integração no SDLC.**  
Operação contínua | Deteção de drift | Ops | `<48h`

---

### US-15 - Reprodutibilidade de incidentes em runtime

Sem reprodutibilidade, não existe auditoria nem melhoria.

:::userstory
**História.**  
Como **Ops/AppSec**, quero **garantir que incidentes em produção são reprodutíveis**, para **validar causas raiz e eficácia das correções**.

**Critérios de aceitação (BDD).**  
- **Dado** um incidente operacional  
  **Quando** é analisado  
  **Então** existe contexto suficiente para reproduzir o comportamento observado
:::

**Artefactos & evidências.** Logs versionados, snapshots de configuração, relatório de RCA.

**Proporcionalidade.**  
L1: reprodutibilidade básica  
L2: reprodutibilidade documentada  
L3: reprodutibilidade completa e auditável

**Integração no SDLC.**  
Produção | Incidente | Ops/AppSec | SLA definido

---
## 📦 Artefactos esperados

Cada prática deve deixar um rasto verificável.  
Estes artefactos constituem a evidência objetiva necessária para auditorias e conformidade:

| Artefacto | Evidência |
|-----------|-----------|
| Artefacto assinado + SBOM | Proveniência validada |
| Relatórios de *staging* | Testes funcionais + DAST + segregação de dados |
| Configuração de *gates* | Pipeline versionado |
| Logs de *rollback* | Evidência de reversão |
| Rastreabilidade *end-to-end* | *Commit* → *release* → *deploy* |
| Monitorização pós-deploy | *Dashboards* + alertas |
| Configuração de *feature flags* | Versionada (YAML/JSON) + logs de auditoria |
| Logs de *secret scanning* | Bloqueios em CI + artefactos limpos |
| `CHANGELOG.md` e *tags* Git | Versionamento + metadata de *release* |
| Configuração de *rollout* progressivo | Configuração + métricas por etapa |
| Validações técnicas pré-deploy | Relatórios + decisões de *findings* + evidência |
| Procedimentos de *rollback* por tipo | Documentos + testes trimestrais |

---

### US-16 - Separação entre ação automática e autorização irreversível

Ferramentas podem agir, mas não decidir impactos irreversíveis.

:::userstory
**História.**  
Como **Ops**, quero **separar execução automática de ações irreversíveis da autorização humana**, para **garantir controlo e responsabilidade explícita**.

**Critérios de aceitação (BDD).**  
- **Dado** que uma ação irreversível é proposta automaticamente  
  **Quando** é executada  
  **Então** existe autorização humana registada previamente
:::

**Artefactos & evidências.** Registo de autorização, logs de execução, identidade do decisor.

**Proporcionalidade.**  
L1: registo simples  
L2: autorização formal  
L3: dupla aprovação

**Integração no SDLC.**  
Produção | Ação crítica | Ops | Antes da execução

---

### US-17 - Evidência operacional auditável

Logs e métricas só têm valor quando tratados como evidência.

:::userstory
**História.**  
Como **GRC/AppSec**, quero **tratar evidência operacional como artefacto auditável**, para **demonstrar controlo efetivo em operação**.

**Critérios de aceitação (BDD).**  
- **Dado** um evento relevante (deploy, rollback, incidente)  
  **Quando** ocorre  
  **Então** a evidência é preservada, versionada e acessível para auditoria
:::

**Artefactos & evidências.** Logs imutáveis, retenção definida, trilhos de auditoria.

**Proporcionalidade.**  
L1: retenção curta  
L2: retenção definida  
L3: retenção + revisão periódica

**Integração no SDLC.**  
Operação contínua | Evento | Ops/GRC | Imediato

---

## ⚖️ Matriz de proporcionalidade L1–L3

Nem todas as aplicações exigem o mesmo nível de controlo.  
A proporcionalidade permite adaptar rigor sem comprometer segurança:

| Prática | L1 | L2 | L3 |
|---------|----|----|----|
| Deploy de artefactos assinados | Recomendado | Obrigatório | Obrigatório + rejeição automática |
| Validação em *staging* | Opcional | Recomendado | Obrigatório |
| *Gates* de aprovação | Aviso | Bloqueio High/Critical | Bloqueio Medium+ |
| *Rollback* | Manual | Automatizado | Automatizado + testado |
| Rastreabilidade | Básica | Completa | Completa + auditoria |
| Monitorização | Básica | Crítica
