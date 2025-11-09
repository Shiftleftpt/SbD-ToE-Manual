---
id: aplicacao-lifecycle
title: Como Fazer
description: Integração prática das práticas de segurança IaC no SDLC, com proporcionalidade por risco, user stories reutilizáveis e evidência auditável
tags: [iac, infraestrutura, segurança, ciclo de vida, user stories, pipelines]
sidebar_position: 15
---

# 📅 Aplicação no Ciclo de Vida - Infraestrutura como Código (IaC)

Este documento operacionaliza as práticas prescritas para **Infraestrutura como Código (IaC)**.  
Enquanto o `intro.md` define o “quê” e o “porquê”, aqui mostramos o “como”: em que fases do ciclo de vida cada requisito se aplica, quem é responsável por executá-lo, como traduzi-lo em user stories reutilizáveis e quais as evidências que asseguram rastreabilidade e auditabilidade.  
A intenção é clara: transformar prescrições em **ações verificáveis**, com proporcionalidade por risco e rastreabilidade completa.

---

## 🧭 Quando aplicar

A segurança em IaC deve ser aplicada **desde o planeamento até à operação**, garantindo que qualquer alteração em infraestrutura é controlada, auditável e reversível.

| Momento gatilho | Objetivo de segurança | Papéis principais |
|------------------|-----------------------|------------------|
| Criação de módulo IaC | Garantir origem confiável e *pinning* | ⚙️ DevOps, 🔐 AppSec |
| Execução de `plan` | Validar alterações e simulações seguras | ⚙️ DevOps, 👨‍💻 Developers |
| Execução de `apply` | Executar apenas alterações aprovadas e assinadas | ⚙️ DevOps, 📑 GRC |
| Auditorias de *drift* | Detetar divergências entre IaC e ambiente real | ⚙️ DevOps, 🔐 AppSec |
| Atualização de módulos | Rever proveniência e *attestations* | 🔐 AppSec, 📋 Auditoria |
| Revisão de exceções | Reavaliar riscos e prazos de compensação | 📑 GRC, 🔐 AppSec |

---

## 👥 Quem executa cada ação

| Ação operacional | Responsável | Apoio | Evidência/Artefactos |
|-------------------|--------------|--------|----------------------|
| Versionar módulos e backends remotos | ⚙️ DevOps | 🔐 AppSec | `backend.tf`, `state.tf`, logs de locking |
| Validar formato e sintaxe de IaC | 👨‍💻 Developers | 🧪 QA | Relatórios de validação automática |
| Aplicar *policy-as-code* nos *pipelines* | 🔐 AppSec | ⚙️ DevOps | Relatórios OPA/Sentinel |
| Assinar *plans* e gerar *attestations* | ⚙️ DevOps | 🔐 AppSec | Assinaturas digitais e `attestation.json` |
| Detetar e corrigir *drift* | ⚙️ DevOps | 🔐 AppSec | Relatórios de `plan -refresh-only` |
| Gerir exceções e revisões | 📑 GRC | 🔐 AppSec | `excecoes-iac.json`, logs de aprovação |

---

## 🧾 User Stories normalizadas

Cada prática é expressa como **user story reutilizável**, com critérios verificáveis, artefactos concretos e proporcionalidade por nível de risco (L1–L3).

---

### US-04 – Origem confiável de módulos (IAC-004)

**Contexto.**  
Dependências de IaC são vetor de *supply chain*. A origem deve ser confiável, com *pinning* estrito, *digest* verificável e política de *allowlist/denylist*.

:::userstory
**História.**  
Como **🔐 AppSec** e **⚙️ DevOps**, quero **permitir apenas módulos de repositórios aprovados, com versão *pinned* e *digest/attestation***, para reduzir risco de comprometimento de *supply chain*.

**Critérios de aceitação (BDD).**
- **Dado** um módulo novo  
  **Quando** é referenciado no repositório  
  **Então** deve constar da **allowlist** e estar **versionado** (sem *ranges*) com **digest** verificado.  
- **Dado** atualização de módulo  
  **Quando** o *pipeline* corre  
  **Então** valida **attestation** e recusa se a origem não cumprir a política.  
- **Dado** um módulo *private*  
  **Quando** é consumido  
  **Então** é exigida **assinatura** do produtor interno e revisão por **AppSec**.

**Checklist.**
- [ ] Política de **allowlist/denylist** publicada  
- [ ] **Pinning semântico** (sem *wildcards*)  
- [ ] **Digest**/SHA256 verificado em *pipeline*  
- [ ] **Attestation** exigida para fontes externas  
:::

**🧾 Artefactos & evidências.**  
`policy-modulos.md`; registos de verificação de *digest*/attestation; *logs* de *pipeline* com gate de origem.

**⚖️ Proporcionalidade.**
| Nível | Obrigatório? | Ajustes |
|---|---:|---|
| L1 | Sim | *Pinning* de versão + allowlist simples |
| L2 | Sim | *Pinning* + **digest** obrigatório |
| L3 | Sim | **Attestation** e revisão AppSec; *denylist* ativa |

---

### US-10 – Assinatura e Proveniência de artefactos IaC (IAC-010)

**Contexto.**  
Sem proveniência verificável, *plans* e *applies* podem ser adulterados. Assinaturas e **attestations** devem ser verificadas **antes da promoção**.

:::userstory
**História.**  
Como **⚙️ DevOps** e **🔐 AppSec**, quero **assinar *plans* e registar *attestations* de *pipeline***, para garantir integridade ponta-a-ponta até ao *apply* em ambiente crítico.

**Critérios de aceitação (BDD).**
- **Dado** um `terraform plan` gerado  
  **Quando** é submetido a revisão  
  **Então** deve estar **assinado** e possuir **attestation** do *pipeline*.  
- **Dado** uma promoção para `prod`  
  **Quando** o *gate* valida artefactos  
  **Então** rejeita *plan/apply* **sem assinatura válida** ou **attestation**.

**Checklist.**
- [ ] Assinatura de `plan` e *apply logs*  
- [ ] **Attestation** (SLSA-like) do *pipeline*  
- [ ] Gate de verificação antes de `prod`  
:::

**🧾 Artefactos & evidências.**  
Ficheiros de assinatura; `attestation.json`; *logs* de *gate*; trilha de aprovação.

**⚖️ Proporcionalidade.**
| Nível | Obrigatório? | Ajustes |
|---|---:|---|
| L1 | Recomendado | Assinatura de `plan` |
| L2 | Sim | Assinatura + verificação automática |
| L3 | Sim | Assinatura + **attestation** e *gate* bloqueante |

---

### US-11 – Gestão de segredos e identidades para IaC (IAC-011)

**Contexto.**  
Chaves estáticas em *providers* ou *runners* representam risco elevado. Preferir **OIDC / workload identity**, *scopes* mínimos e **TTL curto**.

:::userstory
**História.**  
Como **⚙️ DevOps** e **🔐 AppSec**, quero **emitir credenciais temporárias via OIDC/workload identity** com **permissões mínimas**, para eliminar chaves long-lived e reduzir abuso.

**Critérios de aceitação (BDD).**
- **Dado** um *pipeline* de IaC  
  **Quando** necessita aceder ao *provider*  
  **Então** obtém **token efémero** via OIDC, com *scope* mínimo e **TTL ≤ 1h**.  
- **Dado** um *runner* comprometido  
  **Quando** o token expira  
  **Então** **não** é possível reutilização ou escalada.

**Checklist.**
- [ ] OIDC/workload identity configurado  
- [ ] *Scopes* mínimos e *boundaries* por ambiente  
- [ ] Proibição de chaves estáticas no repositório  
:::

**🧾 Artefactos & evidências.**  
Política de segredos; configuração OIDC; *logs* de emissão/expiração.

**⚖️ Proporcionalidade.**
| Nível | Obrigatório? | Ajustes |
|---|---:|---|
| L1 | Sim | Segredos cifrados e rotacionados |
| L2 | Sim | OIDC obrigatório com TTL curto |
| L3 | Sim | OIDC + *Just-In-Time* + *break-glass* auditado |

---

### US-12 – Deteção e correção de *drift* (IAC-012)

**Contexto.**  
Mudanças manuais no *runtime* criam **desalinhamento** (*drift*) com o IaC. É necessário **auditar** e **corrigir** de forma controlada.

:::userstory
**História.**  
Como **🔐 AppSec** e **⚙️ DevOps**, quero **auditorias periódicas de *drift*** e **correção controlada**, para manter coerência entre IaC e infraestrutura.

**Critérios de aceitação (BDD).**
- **Dado** um ciclo quinzenal  
  **Quando** corre `terraform plan -refresh-only`  
  **Então** são gerados **relatórios de *drift*** por ambiente.  
- **Dado** *drift* crítico em `prod`  
  **Quando** é confirmado  
  **Então** é criada tarefa de correção com **aprovação** antes de *apply*.

**Checklist.**
- [ ] Job agendado de *drift* por ambiente  
- [ ] Relatórios versionados  
- [ ] Correções via PR + revisão  
:::

**🧾 Artefactos & evidências.**  
Relatórios de *drift*; PRs de correção; aprovações.

**⚖️ Proporcionalidade.**
| Nível | Obrigatório? | Ajustes |
|---|---:|---|
| L1 | Sim | Auditoria mensal |
| L2 | Sim | Quinzenal + alertas |
| L3 | Sim | Semanal + *gate* para *drift* crítico |

---

### US-13 – *Rollback* e salvaguarda de *destroy* (IAC-013)

**Contexto.**  
Falhas de *apply* e *destroy* acidentais têm impacto elevado. É necessária **estratégia de *rollback*** e *guardrails*.

:::userstory
**História.**  
Como **⚙️ DevOps**, quero **pontos de restauração**, **confirmações explícitas** para *destroy* e **procedimento de *rollback***, para reduzir *downtime* e evitar perda de dados.

**Critérios de aceitação (BDD).**
- **Dado** um *apply* falhado  
  **Quando** é acionado *rollback*  
  **Então** recursos críticos regressam ao estado anterior.  
- **Dado** uma operação `destroy`  
  **Quando** corre em `prod`  
  **Então** requer **dupla confirmação** e **janela de mudança**.

**Checklist.**
- [ ] *Snapshots* de estado/recursos críticos  
- [ ] Procedimento de *rollback* testado  
- [ ] *Kill-switch* para *destroy* em `prod`  
:::

**🧾 Artefactos & evidências.**  
Procedimento `rollback.md`; *snapshots*; *logs* de confirmação dupla.

**⚖️ Proporcionalidade.**
| Nível | Obrigatório? | Ajustes |
|---|---:|---|
| L1 | Sim | *Rollback* manual documentado |
| L2 | Sim | *Snapshots* automáticos |
| L3 | Sim | *Rollback* automatizado e *kill-switch* |

---

### US-14 – Janela de mudança e aprovações por papel (IAC-014)

**Contexto.**  
Alterações em ambientes críticos exigem **janela de mudança** e **aprovação multinível**.

:::userstory
**História.**  
Como **📑 GRC**, **🔐 AppSec** e **📋 Auditoria**, quero **janelas de mudança definidas** e **aprovações por papel** antes do *apply* em `prod`, para reduzir risco operacional.

**Critérios de aceitação (BDD).**
- **Dado** uma alteração a `prod`  
  **Quando** o *plan* é aprovado  
  **Então** o *apply* ocorre **apenas** na janela autorizada e com aprovações **PO/AppSec/GRC**.

**Checklist.**
- [ ] Janelas de mudança publicadas  
- [ ] Fluxo de aprovação multinível  
- [ ] Trilha de auditoria completa  
:::

**🧾 Artefactos & evidências.**  
Calendário de mudança; registos de aprovação; *logs* de *apply*.

**⚖️ Proporcionalidade.**
| Nível | Obrigatório? | Ajustes |
|---|---:|---|
| L1 | Opcional | Aprovação simples |
| L2 | Sim | Aprov. PO + AppSec |
| L3 | Sim | Aprov. PO + AppSec + GRC |

---

### US-15 – Exceções formais em IaC (IAC-015)

**Contexto.**  
Nem todas as políticas podem ser cumpridas em todas as circunstâncias. Exceções devem ser **temporárias**, **justificadas** e com **compensações** (addon/09).

:::userstory
**História.**  
Como **📑 GRC** e **🔐 AppSec**, quero **exceções registadas** com **prazo** e **contramedidas**, para evitar dívida estrutural.

**Critérios de aceitação (BDD).**
- **Dado** um pedido de exceção  
  **Quando** é analisado  
  **Então** só é aprovado com **prazo** e **compensações**; **expirado** → **revogar** e restaurar política.

**Checklist.**
- [ ] Registo de exceção com dono  
- [ ] Prazo e contramedidas  
- [ ] Revisão periódica automatizada  
:::

**🧾 Artefactos & evidências.**  
`excecoes-iac.json`; decisões; *logs* de revisão e expiração.

**⚖️ Proporcionalidade.**
| Nível | Obrigatório? | Ajustes |
|---|---:|---|
| L1 | Sim | Aprovação única |
| L2 | Sim | Aprovação dupla (AppSec+PO) |
| L3 | Sim | Aprovação AppSec+GRC e *review* por sprint |

## 📦 Artefactos & Evidências Esperadas

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
| Política de segredos OIDC/workload    | US-11       | Tokens efémeros e permissões mínimas|
| Relatórios de drift e correção        | US-12       | Auditorias periódicas de infraestrutura|
| Snapshots e logs de rollback          | US-13       | Recuperação após falha              |

---

## ⚖️ Matriz de proporcionalidade L1–L3

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
| Gestão de segredos IaC              | Recomendado     | Obrigatório (OIDC/TTL curto) | Obrigatório + JIT + auditoria           |
| Rollback e contingência             | Recomendado     | Obrigatório (snapshots automáticos) | Obrigatório + rollback automatizado     |
| Assinatura + proveniência artefactos| Recomendado     | Obrigatório (gate críticos)| Obrigatório + rejeição automática        |

---

## 🏁 Recomendações finais

A segurança de IaC deve ser entendida como **disciplina contínua**.  
Não basta aplicar controlos isolados: é preciso garantir que todos se reforçam mutuamente, formando uma rede de confiança.

- **Padronizar backends e providers** para reduzir drift.  
- **Adotar policy-as-code** como prática central, versionada e testada.  
- **Assinar artefactos** e aplicar proveniência SLSA como gates obrigatórios.  
- **Automatizar o ciclo plan→review→apply** em pipelines com aprovação formal.  
- **Medir conformidade** com métricas (drift, bloqueios, exceções) e reportar por L1–L3.  
- **Rever exceções periodicamente**, garantindo que não se eternizam como riscos ocultos.  

Em síntese, **IaC é software** - e deve ser tratado com o mesmo rigor, visibilidade e proporcionalidade que qualquer outra peça crítica do ciclo de vida.