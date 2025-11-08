---
id: aplicacao-lifecycle
title: Como Fazer
description: Como aplicar as práticas de CI/CD seguro ao longo do ciclo de vida da aplicação, com proporcionalidade por risco, user stories normalizadas e evidências auditáveis
tags: [cicd, devsecops, pipelines, segurança, proveniência, risco, rastreabilidade]
sidebar_position: 15
---

# 📅 Aplicação no Ciclo de Vida - CI/CD Seguro

Enquanto o `intro.md` explica **porque os pipelines são críticos** e que práticas devem ser aplicadas, este documento mostra **como transformar essas prescrições em ações concretas** dentro do ciclo de vida de desenvolvimento e entrega.  
A lógica é simples mas poderosa: cada controlo deve ter um momento certo, um responsável definido, uma user story clara e uma evidência verificável.  
Só assim a segurança em CI/CD deixa de ser teórica e passa a ser **prática operacional auditável**.

---

## 🧭 Quando aplicar

A segurança em pipelines não acontece apenas quando algo corre mal - ela é parte do seu ADN desde o primeiro commit.  
Cada vez que se cria, altera ou promove um pipeline, existem triggers que exigem controlos específicos:

| Momento gatilho                                   | Objetivo de segurança                                | Papéis principais        |
|--------------------------------------------------|------------------------------------------------------|--------------------------|
| Criação ou refactor do pipeline                   | Introduzir controlos base (proteção, scanners)       | Dev Team, DevOps         |
| Alteração de tooling/infra (runners, secrets)     | Rever isolamento, injeção de segredos e permissões   | DevOps, AppSec           |
| Introdução/atualização de scanners                | Aumentar cobertura e gates proporcionais ao risco    | Dev Team, AppSec         |
| Preparação de release / promoção a produção       | Validar assinatura e proveniência dos artefactos     | DevOps, AppSec           |
| Registo de exceção (bypass de gate)               | Aprovação formal, prazos e compensações              | GRC/Auditoria, AppSec    |
| Auditoria ou revisão periódica                    | Demonstrar rastreabilidade ponta-a-ponta             | GRC/Auditoria, DevOps    |

---

## 👥 Quem executa cada ação

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

## 🧾 User Stories normalizadas

Para que a segurança não se perca em generalidades, cada prática é expressa como **user story reutilizável**, com:

- Contexto → porque importa  
- Rationale científico → evidência e referência a frameworks  
- História → a perspetiva de quem executa  
- Critérios BDD → comportamento esperado  
- Checklist binária → prova objetiva  
- Artefactos → evidências concretas

---

### US-01 – Gestão segura de código fonte

**Contexto.**  
Sem controlo sobre o repositório, qualquer pipeline é vulnerável.

:::userstory
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

:::

**Artefactos & evidências.** Políticas de branch protection, logs de revisão  

---

### US-02 – Design seguro dos pipelines

**Contexto.**  
Pipelines inseguros são alvos privilegiados de ataque.

:::userstory
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

:::

**Artefactos & evidências.** Histórico de commits  

---

### US-03 – Scanners integrados

**Contexto.**  
Detetar cedo é mais barato e eficaz.

:::userstory
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

:::

**Artefactos & evidências.** Relatórios de scanners  

---

### US-04 – Gestão de segredos

**Contexto.**  
Segredos estáticos expõem a organização.

:::userstory
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

:::

**Artefactos & evidências.** Políticas de segredos, logs de acesso  

---

### US-05 – Isolamento de runners

**Contexto.**  
Runners inseguros comprometem todo o ecossistema.

:::userstory
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

:::

**Artefactos & evidências.** Config de runners, logs  

---

### US-06 – Assinatura e proveniência

**Contexto.**  
Artefactos não assinados perdem legitimidade.

:::userstory
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

:::

**Artefactos & evidências.** Assinaturas, ficheiros de proveniência  

---

### US-07 – Gates por risco

**Contexto.**  
Nem todas as apps exigem o mesmo rigor.

:::userstory
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

:::

**Artefactos & evidências.** Políticas de gates  

---

### US-08 – Cobertura ampliada

**Contexto.**  
Cobertura limitada cria pontos cegos.

:::userstory
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

:::

**Artefactos & evidências.** Relatórios, SBOM  

---

### US-09 – Rastreabilidade ponta-a-ponta

**Contexto.**  
Sem rastreio, auditoria é impossível.

:::userstory
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

:::

**Artefactos & evidências.** Logs, dashboards  

---

### US-10 – Gestão de exceções

**Contexto.**  
Exceções mal geridas tornam-se risco estrutural.

:::userstory
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

:::

**Artefactos & evidências.** Registo de exceções  

---

## 📦 Artefactos esperados

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

## ⚖️ Matriz de proporcionalidade L1–L3

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

## 🏁 Recomendações finais

A segurança de pipelines não é opcional: é **o coração da segurança por design**.  
Um CI/CD seguro multiplica a confiança em todo o ciclo de vida, permitindo releases rápidas e auditáveis.

- **Prefere OIDC a segredos estáticos** - elimina chaves long-lived.  
- **Usa runners ephemerais e segregados** - reduz persistência de ataque.  
- **Assina artefactos e regista proveniência** - cada release deve ser verificável.  
- **Aplica gates proporcionais ao risco** - evita tanto o excesso como a negligência.  
- **Controla exceções** - com prazo, dono e compensações, nunca em aberto.  
- **Investe em rastreabilidade total** - commit→pipeline→release como linha de confiança.

Em suma: um pipeline seguro é **o garante silencioso** de que todo o trabalho de desenvolvimento chega a produção de forma íntegra, confiável e auditável.
