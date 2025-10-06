---
id: aplicacao-lifecycle
title: Aplicação no Ciclo de Vida — Infraestrutura como Código (IaC)
description: Integração prática das práticas de segurança IaC no SDLC, com proporcionalidade por risco, user stories reutilizáveis e evidência auditável
tags: [iac, infraestrutura, segurança, ciclo de vida, user stories, pipelines]
sidebar_position: 15
---

# 📅 Aplicação no Ciclo de Vida — Infraestrutura como Código (IaC) {iac-infraestrutura:aplicacao-lifecycle}

Este documento operacionaliza as práticas prescritas para **Infraestrutura como Código (IaC)**.  
Enquanto o `intro.md` define o “quê” e o “porquê”, aqui mostramos o “como”: em que fases do ciclo de vida cada requisito se aplica, quem é responsável por executá-lo, como traduzi-lo em user stories reutilizáveis e quais as evidências que asseguram rastreabilidade e auditabilidade.  
A intenção é clara: transformar prescrições em prática concreta e verificável.

---

## 🧭 Quando aplicar {iac-infraestrutura:aplicacao-lifecycle#quando_aplicar}

Como vimos no `pre-intro`, cada requisito `IAC-XXX` foi concebido para ter **um momento certo de aplicação** no ciclo de vida.  
Não basta aplicar controlos no fim: é preciso integrá-los desde o arranque do projeto, acompanhando cada alteração de recursos, a adoção de módulos, a preparação de releases e até as auditorias periódicas.  
A tabela seguinte sintetiza esse alinhamento, ajudando a equipa a saber **quando ativar cada prática e quem deve estar envolvido**.

| Momento de aplicação             | Prática aplicada                 | Papéis principais         |
|----------------------------------|----------------------------------|---------------------------|
| Início do projeto IaC            | Backend remoto, naming conventions| DevOps/Infra, Arquitetura |
| Configuração de ambientes        | Segregação, versionamento         | DevOps/Infra              |
| Alteração de recursos            | PR com validações automáticas     | DevOps/Infra, AppSec      |
| Adoção de módulos                | Origem confiável de módulos       | DevOps/Infra, AppSec      |
| Preparação de release            | Versionamento, tagging, assinatura| DevOps/Infra              |
| Antes do `apply`                 | Revisão de `plan`                 | DevOps/Infra, AppSec      |
| Auditorias e revisões periódicas | Rastreabilidade, enforcement      | GRC, AppSec               |

---

## 👥 Quem executa cada ação {iac-infraestrutura:aplicacao-lifecycle#quem_executa}

Garantir segurança em IaC não é responsabilidade de uma única equipa.  
Cada papel desempenha uma função específica, e só a articulação entre todos mantém a cadeia de confiança íntegra.

| Ação operacional                              | Responsável   | Apoio        | Evidência/Artefactos                        |
|-----------------------------------------------|---------------|--------------|---------------------------------------------|
| Configurar backend remoto com locking         | DevOps/Infra  | Arquitetura  | Config `backend.tf` + logs de locking       |
| Definir segregação/versionamento              | DevOps/Infra  | Arquitetura  | Estrutura de diretórios e branches          |
| Ativar validações automáticas (lint/policies) | DevOps/Infra  | AppSec       | Logs de execução no pipeline                |
| Aprovar `plan` antes de `apply`               | AppSec        | DevOps/Infra | PR com output `plan` anexado                |
| Controlar origem de módulos                   | DevOps/Infra  | AppSec       | Lista de módulos aprovados                  |
| Garantir rastreabilidade ficheiro→recurso     | GRC           | DevOps/Infra | Mapeamento automático em dashboard          |
| Versionar e assinar artefactos                | DevOps/Infra  | AppSec       | Tags, hashes, assinaturas, proveniência     |
| Monitorizar exceções ativas                   | GRC           | AppSec       | Registo de exceções com prazo               |

---

## 🧾 User Stories por requisito {iac-infraestrutura:aplicacao-lifecycle#user_stories}

Aqui cada requisito `IAC-XXX` se traduz numa **user story reutilizável**, com contexto, racional científico, critérios de aceitação, checklist binária e artefactos.  
Este formato permite integração direta em backlogs, assegurando que cada requisito é tratado como item de trabalho verificável.

---

### US-01 – Backend remoto com locking (IAC-001)

**Contexto.**  
O estado da infraestrutura deve ser protegido contra alterações concorrentes.

**📖 Rationale científico.**  
Referências: **SSDF PW.4 / PS.3**, **SAMM Implementation/Operations**, **BSIMM SE2.5**, **ISO/IEC 27005**.  
Mitiga: **CWE-362**, **CWE-667**, **OSC&R: State Tampering**, **CAPEC-172**.  
Evidência: relatórios **DBIR/ENISA** mostram que estados sem locking causam drift e indisponibilidade; *remote state + locking + KMS* reduz incidentes operacionais.

**História.**  
Como **DevOps/Infra**, quero configurar o backend remoto com locking, para garantir consistência do estado e evitar corrupção concorrente.

**BDD.**  
- Dado que vários utilizadores trabalham no mesmo projeto  
- Quando executam operações simultâneas  
- Então o backend bloqueia o estado e impede corrupção  

**Checklist (binária, auditável).**  
- [ ] Backend remoto configurado (`S3+DynamoDB`, `KMS`)  
- [ ] Teste de concorrência documentado  
- [ ] Validação incluída em CI/CD  

**Artefactos.** `backend.tf`, logs de locking  

**Proporcionalidade.**  
- L1: Recomendado  
- L2: Obrigatório  
- L3: Obrigatório + monitorização  

**Integração SDLC.** Início do projeto — **Responsável:** DevOps/Infra  

**Ligações úteis.**  
xref:sbd-toe:cap02:intro  

---

### US-02 – Segregação e versionamento de ambientes (IAC-002)

**Contexto.**  
Ambientes mal segregados aumentam risco de fuga ou alteração acidental.

**📖 Rationale científico.**  
Referências: **SSDF PS.1/PS.2**, **BSIMM SE2.3**, **ISO/IEC 27001** (segregação de ambientes).  
Mitiga: **CWE-284**, **OSC&R: Environment Promotion Bypass**, **CAPEC-17**.  
Evidência: **DBIR** mostra que contaminação entre ambientes é causa recorrente de incidentes.

**História.**  
Como **Arquitetura**, quero ambientes definidos e versionados separadamente, para garantir isolamento e rollback.

**BDD.**  
- Dado que existem múltiplos ambientes  
- Quando aplico alterações  
- Então apenas o ambiente alvo é afetado  

**Checklist (binária, auditável).**  
- [ ] Diretórios por ambiente (`dev/`, `prod/`)  
- [ ] Branches ou tags dedicadas  
- [ ] Rollback documentado  

**Artefactos.** Estrutura de repositório, tags/releases  

**Proporcionalidade.**  
- L1: Recomendado  
- L2: Obrigatório  
- L3: Obrigatório + auditoria  

**Integração SDLC.** Configuração inicial — **Responsável:** DevOps/Infra  

**Ligações úteis.**  
xref:sbd-toe:cap14:intro  

---

### US-03 – Validações automáticas (IAC-003)

**Contexto.**  
Erros manuais em IaC são fonte comum de falhas.

**📖 Rationale científico.**  
Referências: **SSDF RV.2/RV.3**, **SAMM Verification**, **BSIMM SE3.x**, **DSOMM Automation**.  
Mitiga: **CWE-16**, **CWE-79**, **CWE-89**, **CAPEC-175**.  
Evidência: **ENISA** indica redução de até 80% de misconfigs quando validações ocorrem em PR.

**História.**  
Como **DevOps/Infra**, quero que todas as alterações passem por validações automáticas, para evitar más práticas.

**BDD.**  
- Dado que submeto PR de IaC  
- Quando corre o pipeline  
- Então falha se não estiver conforme às policies  

**Checklist (binária, auditável).**  
- [ ] Lint (`tflint`)  
- [ ] Segurança (`tfsec`, `checkov`)  
- [ ] Policies (`OPA`, `Sentinel`)  

**Artefactos.** Relatórios pipeline  

**Proporcionalidade.**  
- L1: Aviso  
- L2: Bloqueio falhas severas  
- L3: Bloqueio total  

**Integração SDLC.** Pull request — **Responsável:** DevOps/Infra + AppSec  

**Ligações úteis.**  
xref:sbd-toe:cap07:intro  

---

### US-04 – Origem confiável de módulos (IAC-004)

**Contexto.**  
Módulos não verificados podem introduzir código malicioso.

**📖 Rationale científico.**  
Referências: **SLSA v1.0**, **SSDF PW.4**, **BSIMM CMVM1.1**.  
Mitiga: **CWE-829**, **CWE-494**, **OSC&R: Dependency Confusion**.  
Evidência: relatórios **Sonatype** mostram que pinagem reduz risco de supply chain.

**História.**  
Como **AppSec**, quero garantir que apenas módulos confiáveis são utilizados, para prevenir código malicioso.

**BDD.**  
- Dado que um módulo externo é adicionado  
- Quando submeto PR  
- Então apenas módulos aprovados podem ser usados  

**Checklist (binária, auditável).**  
- [ ] Módulos pinados por versão  
- [ ] Validados internamente  
- [ ] Evidência anexada ao PR  

**Artefactos.** Lista de módulos aprovados  

**Proporcionalidade.**  
- L1: Recomendado  
- L2: Obrigatório  
- L3: Obrigatório + proveniência  

**Integração SDLC.** Adoção de módulos — **Responsável:** DevOps/Infra + AppSec  

**Ligações úteis.**  
xref:sbd-toe:cap05:intro  

---

### US-05 – Histórico de alterações e tagging (IAC-005)

**Contexto.**  
Alterações não versionadas impedem auditoria.

**📖 Rationale científico.**  
Referências: **SSDF PS.3**, **ISO/IEC 27001 A.12**, **BSIMM SE2.5**.  
Mitiga: **OSC&R: Insufficient Traceability**, **CWE-778**, **CAPEC-116**.  
Evidência: **DBIR** mostra que tagging acelera rollback seguro.

**História.**  
Como **DevOps/Infra**, quero garantir que todas as alterações têm histórico auditável, para suportar auditoria.

**BDD.**  
- Dado que publico alteração  
- Quando gero release  
- Então existe tag e relatório associado  

**Checklist (binária, auditável).**  
- [ ] Git tags semânticas  
- [ ] Releases formais  
- [ ] Relatório de mudanças  

**Artefactos.** `CHANGELOG`, tags  

**Proporcionalidade.**  
- L1: Recomendado  
- L2: Obrigatório  
- L3: Obrigatório + validação externa  

**Integração SDLC.** Release — **Responsável:** DevOps/Infra  

**Ligações úteis.**  
xref:sbd-toe:cap14:intro  

---

### US-06 – Convenções de naming e diretórios (IAC-006)

**Contexto.**  
Inconsistência no naming dificulta automação.

**📖 Rationale científico.**  
Referências: **SAMM Governance**, **SSDF PS.1/PS.2**, **BSIMM SE2.3**.  
Mitiga: **CWE-710**, **OSC&R: Misconfiguration via Layout**.  
Evidência: padrões de naming reduzem falsos-negativos em scanners.

**História.**  
Como **Arquitetura**, quero aplicar convenções de naming e diretórios, para garantir legibilidade e automação.

**BDD.**  
- Dado que crio recurso  
- Quando aplico naming conventions  
- Então validações automáticas passam  

**Checklist (binária, auditável).**  
- [ ] Convenções documentadas  
- [ ] Linter configurado  
- [ ] Validação em pipeline  

**Artefactos.** `naming.md`, logs  

**Proporcionalidade.**  
- L1: Recomendado  
- L2: Obrigatório  
- L3: Obrigatório + enforcement  

**Integração SDLC.** Setup inicial — **Responsável:** Arquitetura  

**Ligações úteis.**  
xref:sbd-toe:cap06:intro  

---

### US-07 – Revisão de `plan` antes de `apply` (IAC-007)

**Contexto.**  
Aplicar sem revisão pode introduzir falhas graves.

**📖 Rationale científico.**  
Referências: **SSDF RV.3**, **SAMM Verification**, **BSIMM CP1.2**.  
Mitiga: **CWE-284**, **CWE-732**, **OSC&R: Risky Changes**.  
Evidência: **ENISA** relaciona incidentes críticos a `apply` sem revisão.

**História.**  
Como **AppSec**, quero rever o `plan` antes de `apply`, para garantir impactos claros e validados.

**BDD.**  
- Dado que executo `terraform plan`  
- Quando submeto PR  
- Então aplicação só avança após aprovação  

**Checklist (binária, auditável).**  
- [ ] Output `plan` anexado ao PR  
- [ ] Aprovação formal antes de `apply`  
- [ ] Bloqueio automático se não aprovado  

**Artefactos.** Output `plan`, logs  

**Proporcionalidade.**  
- L1: Recomendado  
- L2: Obrigatório  
- L3: Obrigatório + dupla aprovação  

**Integração SDLC.** Antes do deploy — **Responsável:** AppSec + DevOps/Infra  

**Ligações úteis.**  
xref:sbd-toe:cap14:intro  

---

### US-08 – Rastreabilidade ficheiros→recursos (IAC-008)

**Contexto.**  
Falta de rastreio dificulta auditoria.

**📖 Rationale científico.**  
Referências: **SSDF RV.2**, **DSOMM Evidence**, **BSIMM CMVM1.3**.  
Mitiga: **CWE-778**, **OSC&R: Lack of Traceability**, **CAPEC-59**.  
Evidência: dashboards de rastreio reduzem *MTTR* e melhoram análise forense.

**História.**  
Como **GRC**, quero rastrear ficheiro→recurso→ambiente, para suportar accountability.

**BDD.**  
- Dado que analiso repositório  
- Quando consulto dashboard  
- Então consigo mapear ficheiro→recurso  

**Checklist (binária, auditável).**  
- [ ] Mapeamento automático  
- [ ] Dashboard acessível  
- [ ] Logs arquivados  

**Artefactos.** Dashboard  

**Proporcionalidade.**  
- L1: Recomendado  
- L2: Obrigatório  
- L3: Obrigatório + auditoria externa  

**Integração SDLC.** Auditoria — **Responsável:** GRC  

**Ligações úteis.**  
xref:sbd-toe:cap12:intro  

---

### US-09 – *Policy-as-code* com enforcement (IAC-009)

**Contexto.**  
Sem enforcement, violações podem passar despercebidas.

**📖 Rationale científico.**  
Referências: **SSDF RV.2/RV.3**, **SAMM Governance**, **BSIMM SE3.x**, **SLSA**.  
Mitiga: **CWE-16**, **CWE-284**, **OSC&R: Policy Bypass**.  
Evidência: *policy-as-code* (OPA/Sentinel) reduz *config drift* e erros manuais.

**História.**  
Como **AppSec**, quero enforcement automático de policies no pipeline, para evitar violações manuais.

**BDD.**  
- Dado que executo pipeline  
- Quando policies são aplicadas  
- Então falha se não conforme  

**Checklist (binária, auditável).**  
- [ ] Policies definidas em OPA/Sentinel  
- [ ] Enforcement ativo em pipeline  
- [ ] Logs arquivados  

**Artefactos.** Policies, logs  

**Proporcionalidade.**  
- L1: Aviso  
- L2: Bloqueio falhas severas  
- L3: Bloqueio total  

**Integração SDLC.** CI/CD — **Responsável:** AppSec + DevOps/Infra  

**Ligações úteis.**  
xref:sbd-toe:cap07:intro  

---

### US-10 – Assinatura e Proveniência de artefactos IaC (IAC-010)

**Contexto.**  
Artefactos IaC sem assinatura ou proveniência validada podem ser adulterados.

**📖 Rationale científico.**  
Referências: **SLSA v1.0**, **SSDF RV.3**, **SAMM Implementation**, **BSIMM CP1.2**, **ISO/IEC 27001 A.12**.  
Mitiga: **CWE-353**, **CWE-494**, **OSC&R: Artifact Tampering**, **CAPEC-440**.  
Evidência: casos SolarWinds e Codecov mostram a importância de assinatura/proveniência.

**História.**  
Como **DevOps/Infra**, quero assinar e gerar proveniência para artefactos IaC, para garantir integridade e permitir verificação antes de `apply`.

**BDD.**  
- Dado que um artefacto IaC é produzido  
- Quando é promovido ou aplicado  
- Então a assinatura e a proveniência SLSA são verificadas  

**Checklist (binária, auditável).**  
- [ ] Assinatura automática dos artefactos  
- [ ] Proveniência gerada e arquivada  
- [ ] Gate de verificação antes de `apply`  
- [ ] SBOM de módulos/providers  

**Artefactos.** Assinaturas, proveniência, SBOM  

**Proporcionalidade.**  
- L1: Recomendado  
- L2: Obrigatório  
- L3: Obrigatório + rejeição automática  

**Integração SDLC.** Release — **Responsável:** DevOps/Infra + AppSec  

**Ligações úteis.**  
xref:sbd-toe:cap05:intro  

---

## 📦 Artefactos & Evidências Esperadas {iac-infraestrutura:aplicacao-lifecycle#artefactos}

Cada prática deixa uma pegada objetiva.  
Sem evidência, não há conformidade. A tabela abaixo resume os outputs esperados.

| Artefacto/Evidência                   | Origem / US | Observações                         |
|---------------------------------------|-------------|-------------------------------------|
| `backend.tf` + logs de locking        | US-01       | Prova de locking e encriptação KMS  |
| Estrutura de diretórios por ambiente  | US-02       | `dev/`, `staging/`, `prod/`         |
| Relatórios de lint/security/policies  | US-03       | Arquivados em pipeline              |
| Lista de módulos aprovados            | US-04       | Origem + hash/version               |
| `CHANGELOG`, tags, releases           | US-05       | Evidência de change control         |
| `naming.md` + logs de lint            | US-06       | Naming conventions aplicadas        |
| PR com `terraform plan` anexado       | US-07       | Aprovação formal antes do apply     |
| Dashboard de rastreabilidade          | US-08       | Mapas ficheiro→recurso→ambiente     |
| Logs de enforcement                   | US-09       | Bloqueios e métricas de conformidade|
| Assinaturas + Proveniência (SLSA)     | US-10       | Gate obrigatório em L2/L3           |
| SBOM de módulos/providers             | US-10       | CycloneDX/SPDX                      |

---

## ⚖️ Matriz de proporcionalidade L1–L3 {iac-infraestrutura:aplicacao-lifecycle#matriz_l1_l3}

Nem todas as aplicações exigem o mesmo rigor.  
A proporcionalidade permite equilibrar custo, risco e controlo.

| Prática                             | L1 (baixo)      | L2 (médio)                | L3 (alto/crítico)                        |
|-------------------------------------|-----------------|---------------------------|------------------------------------------|
| Backend remoto + locking            | Recomendado     | Obrigatório               | Obrigatório + monitorização              |
| Segregação/versionamento            | Recomendado     | Obrigatório               | Obrigatório + auditoria                  |
| Validações automáticas              | Aviso           | Bloqueio falhas severas   | Bloqueio total + cobertura completa      |
| Origem confiável de módulos         | Recomendado     | Obrigatório + pinagem     | Obrigatório + proveniência formal        |
| Histórico, tags e releases          | Recomendado     | Obrigatório               | Obrigatório + validação externa          |
| Naming e diretórios                 | Recomendado     | Obrigatório               | Obrigatório + enforcement automático     |
| Revisão de `plan`                   | Recomendado     | Obrigatório               | Obrigatório + dupla aprovação            |
| Rastreabilidade ficheiro→recurso    | Recomendado     | Obrigatório               | Obrigatório + auditoria externa          |
| Policy-as-code                      | Aviso           | Bloqueio falhas severas   | Bloqueio total + métricas conformidade   |
| Assinatura + proveniência artefactos| Recomendado     | Obrigatório (gate críticos)| Obrigatório + rejeição automática        |

---

## 🏁 Recomendações finais {iac-infraestrutura:aplicacao-lifecycle#recomendacoes}

A segurança de IaC deve ser entendida como **disciplina contínua**.  
Não basta aplicar controlos isolados: é preciso garantir que todos se reforçam mutuamente, formando uma rede de confiança.

- **Padronizar backends e providers** para reduzir drift.  
- **Adotar policy-as-code** como prática central, versionada e testada.  
- **Assinar artefactos** e aplicar proveniência SLSA como gates obrigatórios.  
- **Automatizar o ciclo plan→review→apply** em pipelines com aprovação formal.  
- **Medir conformidade** com métricas (drift, bloqueios, exceções) e reportar por L1–L3.  
- **Rever exceções periodicamente**, garantindo que não se eternizam como riscos ocultos.  

Em síntese, **IaC é software** — e deve ser tratado com o mesmo rigor, visibilidade e proporcionalidade que qualquer outra peça crítica do ciclo de vida.
