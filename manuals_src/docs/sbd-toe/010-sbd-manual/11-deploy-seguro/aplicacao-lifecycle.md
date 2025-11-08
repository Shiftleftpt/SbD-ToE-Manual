---
id: aplicacao-lifecycle
title: Como Fazer
description: Integração prática das práticas de release e deploy seguro no ciclo de vida de software
tags: [ciclo de vida, deploy, release, rollback, gates, produção]
sidebar_position: 15
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
- Dado um pipeline de deploy  
- Quando um artefacto não está assinado  
- Então o deploy é bloqueado  

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

**Ligações úteis.** xref:sbd-toe:cap07:intro ; xref:sbd-toe:cap11:intro  

---

### US-02 - Validação em staging antes da promoção

Staging é o “ensaio geral”: sem ele, a produção torna-se campo de teste.  

**Contexto.** Promover diretamente à produção aumenta risco de incidentes.  

:::userstory
**História.**   
Como **QA/Testes**, quero **validar releases em staging com testes funcionais e de segurança**, para **detetar falhas antes da promoção**.  

**Critérios de aceitação (BDD).**  
- Dado ambiente staging ativo  
- Quando executo validações  
- Então só versões aprovadas seguem para produção  

**Checklist.**  
- [ ] Testes funcionais executados  
- [ ] DAST autenticado concluído  
- [ ] Relatório anexado à release  

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

**Ligações úteis.** xref:sbd-toe:cap10:intro  

---

### US-03 - Gates de aprovação no deploy

Sem gates, a promoção a produção torna-se uma aposta: e a segurança não pode ser um jogo de sorte.  

**Contexto.** Releases sem gates podem promover código inseguro.  

:::userstory
**História.**   
Como **AppSec**, quero **definir gates automáticos e thresholds no deploy**, para **bloquear releases inseguras**.  

**Critérios de aceitação (BDD).**  
- Dado uma release candidata  
- Quando findings críticos não estão resolvidos  
- Então o deploy é bloqueado até aprovação formal  

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

**Ligações úteis.** xref:sbd-toe:cap07:intro ; xref:sbd-toe:cap10:intro  

---

### US-04 - Rollback rápido e testado

Falhas acontecem. A diferença entre crise e resiliência está em quão rápido conseguimos voltar atrás.  

**Contexto.** Sem rollback seguro, falhas em produção ampliam impacto.  

:::userstory
**História.**   
Como **DevOps/SRE**, quero **rollback rápido e testado periodicamente**, para **reverter releases problemáticas**.  

**Critérios de aceitação (BDD).**  
- Dado um incidente em produção  
- Quando aciono rollback  
- Então a versão anterior é restaurada automaticamente  

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

**Ligações úteis.** xref:sbd-toe:cap12:intro  

---

### US-05 - Rastreabilidade end-to-end

Se não for possível reconstituir o caminho desde o commit até ao deploy, não existe governação real.  

**Contexto.** Sem rastreabilidade, não é possível auditar incidentes.  

:::userstory
**História.**   
Como **Gestão de Produto**, quero **garantir rastreabilidade entre commit → build → release → deploy**, para **auditar e justificar decisões de risco**.  

**Critérios de aceitação (BDD).**  
- Dado incidente pós-release  
- Quando audito histórico  
- Então consigo traçar origem até commit inicial  

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

**Ligações úteis.** xref:sbd-toe:cap02:intro ; xref:sbd-toe:cap07:intro  

---

### US-06 - Monitorização pós-deploy

Um deploy não termina no *merge*: só se considera concluído quando a versão está estável e visível em produção.  

**Contexto.** Deploys inseguros podem originar falhas não detetadas.  

:::userstory
**História.**   
Como **DevOps/SRE**, quero **ativar monitorização pós-deploy**, para **detetar anomalias e regressões em tempo real**.  

**Critérios de aceitação (BDD).**  
- Dado nova versão em produção  
- Quando ocorre anomalia  
- Então alertas são gerados automaticamente  

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

**Ligações úteis.** xref:sbd-toe:cap12:intro  

---

## 📦 Artefactos esperados

Cada prática deve deixar um **rasto verificável**.  
Estes artefactos constituem a evidência objetiva necessária para auditorias e conformidade:

| Artefacto | Evidência |
|-----------|-----------|
| Artefacto assinado + SBOM | Proveniência validada |
| Relatórios staging | Testes funcionais + DAST |
| Configuração de gates | Pipeline versionado |
| Logs de rollback | Evidência de reversão |
| Rastreabilidade end-to-end | Commit → release |
| Monitorização pós-deploy | Dashboards + alertas |

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

---

## 🏁 Recomendações finais

- **Nunca promover diretamente** para produção sem staging.  
- **Automatizar deploys, rastrear e reverter** sempre que necessário.  
- **Rollback testado regularmente** assegura resiliência.  
- **Monitorização pós-deploy** deve estar integrada com resposta a incidentes (Cap. 12).  
- **Aplicar proporcionalidade L1–L3** garante equilíbrio entre custo e risco.  
