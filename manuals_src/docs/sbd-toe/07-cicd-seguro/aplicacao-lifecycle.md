---
id: aplicacao-lifecycle
title: Aplicação no Ciclo de Vida — CI/CD Seguro
description: Como aplicar as práticas de CI/CD seguro ao longo do ciclo de vida da aplicação, com proporcionalidade por risco, user stories normalizadas e evidências auditáveis
tags: [cicd, devsecops, pipelines, segurança, proveniência, risco, rastreabilidade]
sidebar_position: 15
---

# 📅 Aplicação no Ciclo de Vida — CI/CD Seguro {cicd-seguro:aplicacao-lifecycle}

Enquanto o `intro.md` explica **porque os pipelines são críticos** e que práticas devem ser aplicadas, este documento mostra **como transformar essas prescrições em ações concretas** dentro do ciclo de vida de desenvolvimento e entrega.  
A lógica é simples mas poderosa: cada controlo deve ter um momento certo, um responsável definido, uma user story clara e uma evidência verificável.  
Só assim a segurança em CI/CD deixa de ser teórica e passa a ser **prática operacional auditável**.

---

## 🧭 Quando aplicar {cicd-seguro:aplicacao-lifecycle#quando_aplicar}

A segurança em pipelines não acontece apenas quando algo corre mal — ela é parte do seu ADN desde o primeiro commit.  
Cada vez que se cria, altera ou promove um pipeline, existem gatilhos que exigem controlos específicos:

| Momento gatilho                                   | Objetivo de segurança                                | Papéis principais        |
|--------------------------------------------------|------------------------------------------------------|--------------------------|
| Criação ou refactor do pipeline                   | Introduzir controlos base (proteção, scanners)       | Dev Team, DevOps         |
| Alteração de tooling/infra (runners, secrets)     | Rever isolamento, injeção de segredos e permissões   | DevOps, AppSec           |
| Introdução/atualização de scanners                | Aumentar cobertura e gates proporcionais ao risco    | Dev Team, AppSec         |
| Preparação de release / promoção a produção       | Validar assinatura e proveniência dos artefactos     | DevOps, AppSec           |
| Registo de exceção (bypass de gate)               | Aprovação formal, prazos e compensações              | GRC/Auditoria, AppSec    |
| Auditoria ou revisão periódica                    | Demonstrar rastreabilidade ponta-a-ponta             | GRC/Auditoria, DevOps    |

---

## 👥 Quem executa cada ação {cicd-seguro:aplicacao-lifecycle#quem_executa}

A responsabilidade em CI/CD é **partilhada**.  
Um pipeline seguro resulta da soma de esforços: do programador que submete código com scanners ativos, ao DevOps que endurece runners, até ao GRC que valida exceções.

| Ação operacional                                                      | Responsável  | Apoio                | Evidência/Artefactos                          |
|-----------------------------------------------------------------------|--------------|----------------------|-----------------------------------------------|
| Definir/alterar pipeline versionado via PR                            | Dev Team     | DevOps               | `ci-pipeline.yml`, histórico de revisão       |
| Endurecer runners (ephemerais, não-privilegiados, segregados)         | DevOps       | AppSec               | Configuração de runners, imagens base         |
| Integrar scanners (SAST, secrets, IaC, containers, SBOM)              | Dev Team     | AppSec, DevOps       | Relatórios de scanners, configs no pipeline   |
| Injeção segura de segredos (OIDC, TTL curto, masked logs)             | DevOps       | AppSec               | Políticas de segredos, logs de acesso         |
| Assinar artefactos e gerar proveniência                               | DevOps       | AppSec               | Assinaturas, ficheiros de proveniência        |
| Definir políticas/gates por risco (L1–L3)                             | AppSec       | DevOps, GRC          | Regras de gates, thresholds                   |
| Registar e aprovar exceções                                           | GRC/Auditoria| AppSec               | Registo formal de exceções e aprovações       |
| Garantir rastreabilidade ponta-a-ponta                                | DevOps       | GRC/Auditoria        | Logs correlacionados commit→pipeline→release  |

---

## 🧾 User Stories normalizadas {cicd-seguro:aplicacao-lifecycle#user_stories}

Para que a segurança não se perca em generalidades, cada prática é expressa como **user story reutilizável**, com:

- Contexto → porque importa  
- Rationale científico → evidência e referência a frameworks  
- História → a perspetiva de quem executa  
- Critérios BDD → comportamento esperado  
- Checklist binária → prova objetiva  
- Artefactos → evidências concretas

---

### US-01 – Gestão segura de código fonte {#us-01}

**Contexto.**  
Sem controlo sobre o repositório, qualquer pipeline é vulnerável.

**📖 Rationale científico.**  
Alinhado com **SSDF PS.3** e **BSIMM SE2.5**.  
Mitiga riscos de **CWE-494** e **OSC&R: Source Code Tampering**.  
Estudos (DBIR 2023) mostram que falhas no controlo de branches estiveram na origem de 62% dos incidentes investigados.

**História.**  
Como **Dev Team**, quero que todas as alterações ao repositório sejam protegidas por PR e revisão obrigatória, para garantir integridade.

**BDD.**
- Dado que existe um repositório  
- Quando submeto PR para `main`  
- Então só é aceite com revisão e checks ativos  

**Checklist.**
- [ ] Branch protection ativa  
- [ ] Reviewer obrigatório  
- [ ] Status checks configurados  
- [ ] Proibido `force push`  

**Artefactos.** Políticas de branch protection, logs de revisão  

---

### US-02 – Design seguro dos pipelines {#us-02}

**Contexto.**  
Pipelines inseguros são alvos privilegiados de ataque.

**📖 Rationale científico.**  
Coberto por **DSOMM Build Security**, **SSDF PW.4** e **BSIMM CP1.2**.  
Mitiga **CAPEC-438 (Pipeline Poisoning)**.  
A **ENISA** alerta que adulteração de pipelines é vetor dominante em supply chain.

**História.**  
Como **DevOps**, quero pipelines versionados e aprovados por PR, para evitar alterações não auditadas.

**BDD.**
- Dado que altero pipeline  
- Quando submeto PR  
- Então só é aceite após revisão  

**Checklist.**
- [ ] `ci-pipeline.yml` versionado  
- [ ] PR obrigatório  
- [ ] Triggers explícitos  

**Artefactos.** Histórico de commits  

---

### US-03 – Scanners integrados {#us-03}

**Contexto.**  
Detetar cedo é mais barato e eficaz.

**📖 Rationale científico.**  
Referências: **SSDF RV.3**, **SAMM Verification**.  
Mitiga **CWE-89, CWE-798, CWE-77**.  
Estudos da **Veracode** apontam redução de 80% nos custos de correção quando deteção é feita em CI.

**História.**  
Como **Dev Team**, quero que o pipeline execute scanners de segurança, para impedir falhas graves em produção.

**BDD.**
- Dado que submeto código  
- Quando corre pipeline  
- Então falhas críticas bloqueiam merge  

**Checklist.**
- [ ] SAST ativo  
- [ ] Secrets scanning ativo  
- [ ] IaC scanning (quando aplicável)  

**Artefactos.** Relatórios de scanners  

---

### US-04 – Gestão de segredos {#us-04}

**Contexto.**  
Segredos estáticos expõem a organização.

**📖 Rationale científico.**  
Baseado em **SSDF PW.7**, **BSIMM CMVM1.3**.  
Mitiga **CWE-798** e **OSC&R: Credential Leakage**.  
A GitGuardian (2023) reportou >10M segredos expostos em repositórios públicos.

**História.**  
Como **DevOps**, quero segredos injetados por OIDC com TTL curto, para reduzir risco de abuso.

**BDD.**
- Dado que pipeline arranca  
- Quando credenciais são necessárias  
- Então são emitidas JIT e mascaradas em logs  

**Checklist.**
- [ ] OIDC configurado  
- [ ] TTL curto  
- [ ] Variáveis mascaradas  

**Artefactos.** Políticas de segredos, logs de acesso  

---

### US-05 – Isolamento de runners {#us-05}

**Contexto.**  
Runners inseguros comprometem todo o ecossistema.

**📖 Rationale científico.**  
Centrado em **SLSA Provenance** e **SSDF GV.2**.  
Mitiga **CWE-250** e **CAPEC-664**.  
Casos como **Codecov 2021** provam a necessidade de runners ephemerais.

**História.**  
Como **DevOps**, quero runners ephemerais e segregados, para reduzir persistência pós-compromisso.

**BDD.**
- Dado que job termina  
- Quando runner encerra  
- Então é destruído sem manter estado  

**Checklist.**
- [ ] Ephemerais  
- [ ] Sem privilégios excessivos  
- [ ] Segmentação de rede  

**Artefactos.** Config de runners, logs  

---

### US-06 – Assinatura e proveniência {#us-06}

**Contexto.**  
Artefactos não assinados perdem legitimidade.

**📖 Rationale científico.**  
Central em **SLSA v1.0**, **SSDF RV.3**.  
Mitiga **CWE-353** e ataques como SolarWinds.  
A **Linux Foundation** (2022) coloca proveniência como prioridade #1.

**História.**  
Como **DevOps**, quero que todos os artefactos sejam assinados e tenham proveniência validada, para garantir confiança.

**BDD.**
- Dado que artefacto é produzido  
- Quando é promovido  
- Então assinatura e proveniência são verificadas  

**Checklist.**
- [ ] Assinatura automática  
- [ ] Proveniência SLSA  
- [ ] Verificação antes de release  

**Artefactos.** Assinaturas, ficheiros de proveniência  

---

### US-07 – Gates por risco {#us-07}

**Contexto.**  
Nem todas as apps exigem o mesmo rigor.

**📖 Rationale científico.**  
Alinhado com **SSDF GV.2**, **SAMM Governance**.  
Mitiga **OSC&R: Weak Enforcement**.  
Segundo o DBIR, gates proporcionais reduzem em 50% falhas críticas.

**História.**  
Como **AppSec**, quero gates distintos por L1–L3, para aplicar segurança proporcional.

**BDD.**
- Dado que app é L3  
- Quando há falha High  
- Então gate bloqueia promoção  

**Checklist.**
- [ ] Política publicada  
- [ ] Gates configurados  
- [ ] Thresholds definidos  

**Artefactos.** Políticas de gates  

---

### US-08 – Cobertura ampliada {#us-08}

**Contexto.**  
Cobertura limitada cria pontos cegos.

**📖 Rationale científico.**  
Referências: **SSDF PW.5**, **BSIMM SE3.5**.  
Mitiga **CWE-1104**.  
A **ENISA 2023** indica que 45% das organizações não monitorizam containers sem SBOM.

**História.**  
Como **AppSec**, quero scanners de containers e SBOM em pipelines, para cobrir supply chain.

**BDD.**
- Dado que imagem é construída  
- Quando corre pipeline  
- Então SBOM é gerado e anexado  

**Checklist.**
- [ ] Container scanning ativo  
- [ ] SBOM gerado  
- [ ] Base images validadas  

**Artefactos.** Relatórios, SBOM  

---

### US-09 – Rastreabilidade ponta-a-ponta {#us-09}

**Contexto.**  
Sem rastreio, auditoria é impossível.

**📖 Rationale científico.**  
Baseado em **SSDF RV.3**, **BSIMM CMVM1.3**.  
Mitiga **CWE-778**.  
Organizações sem rastreabilidade têm 2x maior MTTR (DBIR).

**História.**  
Como **GRC**, quero rastrear commit→pipeline→release, para suportar auditorias.

**BDD.**
- Dado que ocorre incidente  
- Quando analiso release  
- Então consigo traçar origem  

**Checklist.**
- [ ] IDs de correlação  
- [ ] Logs retidos  
- [ ] Export imutável  

**Artefactos.** Logs, dashboards  

---

### US-10 – Gestão de exceções {#us-10}

**Contexto.**  
Exceções mal geridas tornam-se risco estrutural.

**📖 Rationale científico.**  
Referências: **SSDF GV.3**, **BSIMM CP1.2**.  
Mitiga **CAPEC-220**.  
O DBIR 2023 reporta 35% de incidentes graves associados a bypass sem registo.

**História.**  
Como **GRC**, quero exceções registadas, aprovadas e temporárias, para não acumular dívida técnica.

**BDD.**
- Dado que exceção é pedida  
- Quando analisada  
- Então só aprovada com prazo e compensações  

**Checklist.**
- [ ] Owner registado  
- [ ] Prazo definido  
- [ ] Aprovação dupla (L3)  

**Artefactos.** Registo de exceções  

---

## 📦 Artefactos esperados {cicd-seguro:aplicacao-lifecycle#artefactos}

Cada prática deixa pegadas técnicas. Sem elas, não há prova de conformidade:

| Artefacto / Evidência                | Dono          | Observações                        |
|-------------------------------------|---------------|------------------------------------|
| `ci-pipeline.yml`                    | Dev Team      | Versionado via PR                  |
| Assinaturas + Proveniência (SLSA)    | DevOps        | Validadas como gate                |
| Relatórios de scanners               | Dev Team/AppSec | Thresholds definidos             |
| SBOM por build                       | AppSec        | Anexado ao artefacto              |
| Registo de exceções                  | GRC/Auditoria | Inclui prazo e compensações        |
| Logs de execuções/releases           | DevOps        | IDs de correlação armazenados      |

---

## ⚖️ Matriz de proporcionalidade L1–L3 {cicd-seguro:aplicacao-lifecycle#matriz}

Nem todas as apps exigem o mesmo nível de rigor.  
A matriz assegura que **o esforço é proporcional ao risco**:

| Categoria                 | L1 (baixo)                  | L2 (médio)                           | L3 (crítico)                           |
|---------------------------|-----------------------------|--------------------------------------|----------------------------------------|
| Branches/PR               | 1 reviewer + build check    | Reviewer + segurança                 | ≥2 reviewers + code owners             |
| Scanners                  | SAST + secrets              | + IaC                                | + Containers + SBOM                     |
| Segredos                  | Variáveis mascaradas        | OIDC preferido                       | OIDC obrigatório + TTL curto            |
| Runners                   | Partilhados com guardrails  | Segregados                           | Ephemerais + segmentação de rede        |
| Artefactos                | Assinatura recomendada      | Assinatura + proveniência obrigatória| Rejeição automática se inválido         |
| Gates por risco            | Aviso                       | Bloqueio High/Critical               | Bloqueio Medium+                        |
| Exceções                  | Registo simples             | Aprovação AppSec                     | Dupla aprovação + prazo curto           |
| Rastreabilidade           | Logs básicos                | IDs correlacionados                  | Export imutável + dashboards            |

---

## 🏁 Recomendações finais {cicd-seguro:aplicacao-lifecycle#recomendacoes}

A segurança de pipelines não é opcional: é **o coração da segurança por design**.  
Um CI/CD seguro multiplica a confiança em todo o ciclo de vida, permitindo releases rápidas e auditáveis.

- **Prefere OIDC a segredos estáticos** — elimina chaves long-lived.  
- **Usa runners ephemerais e segregados** — reduz persistência de ataque.  
- **Assina artefactos e regista proveniência** — cada release deve ser verificável.  
- **Aplica gates proporcionais ao risco** — evita tanto o excesso como a negligência.  
- **Controla exceções** — com prazo, dono e compensações, nunca em aberto.  
- **Investe em rastreabilidade total** — commit→pipeline→release como linha de confiança.

Em suma: um pipeline seguro é **o garante silencioso** de que todo o trabalho de desenvolvimento chega a produção de forma íntegra, confiável e auditável.
