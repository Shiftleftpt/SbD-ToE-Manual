---
id: aplicacao-lifecycle
title: Como Fazer
description: Integração prática das práticas de segurança IaC no SDLC, com proporcionalidade por risco, user stories reutilizáveis e evidência auditável
tags: [tipo:aplicacao, ciclo-vida, iac, infraestrutura, seguranca, pipelines]
genia: us-format-normalization
---

# 📅 Aplicação no Ciclo de Vida - Infraestrutura como Código (IaC)

Este documento operacionaliza as práticas prescritas para **Infraestrutura como Código (IaC)**.  
Enquanto o `intro.md` define o “quê” e o “porquê”, aqui mostramos o “como”: em que fases do ciclo de vida cada requisito se aplica, quem é responsável por executá-lo, como traduzi-lo em user stories reutilizáveis e quais as evidências que asseguram rastreabilidade e auditabilidade.  
A intenção é clara: transformar prescrições em **ações verificáveis**, com proporcionalidade por risco e rastreabilidade completa.

---

## 🧭 Quando aplicar

A segurança em IaC deve ser aplicada **desde o planeamento até à operação**, garantindo que qualquer alteração em infraestrutura é controlada, auditável e reversível.

| Momento *trigger* | Objetivo de segurança | Papéis principais |
|------------------|-----------------------|------------------|
| Criação de módulo IaC | Garantir origem confiável e *pinning* | DevOps / SRE, AppSec Engineers |
| Execução de `plan` | Validar alterações e simulações seguras | DevOps / SRE, Developers |
| Execução de `apply` | Executar apenas alterações aprovadas e assinadas | DevOps / SRE, GRC / Compliance |
| Auditorias de *drift* | Detetar divergências entre IaC e ambiente real | DevOps / SRE, AppSec Engineers |
| Atualização de módulos | Rever proveniência e *attestations* | AppSec Engineers, Auditores Internos |
| Revisão de exceções | Reavaliar riscos e prazos de compensação | GRC / Compliance, AppSec Engineers |

---

## 👥 Quem executa cada ação

| Ação operacional | Responsável | Apoio | Evidência/Artefactos |
|-------------------|--------------|--------|----------------------|
| Versionar módulos e backends remotos | DevOps / SRE | AppSec Engineers | `backend.tf`, `state.tf`, logs de locking |
| Validar formato e sintaxe de IaC | Developers | Quality Assurance | Relatórios de validação automática |
| Aplicar *policy-as-code* nos *pipelines* | AppSec Engineers | DevOps / SRE | Relatórios OPA/Sentinel |
| Assinar *plans* e gerar *attestations* | DevOps / SRE | AppSec Engineers | Assinaturas digitais e `attestation.json` |
| Detetar e corrigir *drift* | DevOps / SRE | AppSec Engineers | Relatórios de `plan -refresh-only` |
| Gerir exceções e revisões | GRC / Compliance | AppSec Engineers | `excecoes-iac.json`, logs de aprovação |

---

## 🧾 User Stories normalizadas

Cada prática é expressa como **user story reutilizável**, com critérios verificáveis, artefactos concretos e proporcionalidade por nível de risco (L1–L3).

---

### US-01 – Backend remoto, locking e rastreabilidade

**Contexto.**  
O estado de infraestrutura deve estar centralizado, protegido e versionado. Sem backend remoto, os riscos incluem perda de estado, conflitos de concorrência e impossibilidade de auditoria.

:::userstory
**História.**  
Como **DevOps / SRE**, quero **armazenar o estado em backend remoto com locking e encriptação**, para evitar *drift*, conflitos e perda de integridade.

**Critérios de aceitação (BDD).**
- **Dado** um projeto IaC novo  
  **Quando** é inicializado  
  **Então** usa **backend remoto** (S3+DynamoDB, Azure Blob, GCS) com **locking** ativo e **encriptação KMS**.  
- **Dado** um `terraform apply` em execução  
  **Quando** outro operador tenta executar  
  **Então** é bloqueado até **release do lock**.  
- **Dado** um plano de execução  
  **Quando** é gerado  
  **Então** é armazenado versionado com **metadados** (timestamp, autor, PR/MR ID).

**Checklist.**
- [ ] Backend remoto configurado e auditado  
- [ ] Locking ativo (DynamoDB, Consul, ou equivalente)  
- [ ] Encriptação em trânsito e em repouso  
- [ ] Histórico de planos versionado  
:::

**🧾 Artefactos & evidências.**  
`backend.tf`, logs de locking, hash de estado, metadados de plano.

**⚖️ Proporcionalidade.**
| Nível | Obrigatório? | Ajustes |
|---|---:|---|
| L1 | Sim | Backend remoto + locking básico |
| L2 | Sim | Backend + locking + encriptação KMS |
| L3 | Sim | Backend + locking + encriptação + MFA + auditoria |

---

### US-02 – Segregação de ambientes, tagging e permissões mínimas

**Contexto.**  
Ambientes (dev, staging, prod) devem ser isolados, com tags obrigatórias e permissões restritivas por princípio. O "fail securely" começa aqui: recursos criados sem permissões, apenas adicionadas conforme necessário.

:::userstory
**História.**  
Como **DevOps / SRE** e **Arquitetos de Software**, quero **ambientes segregados com tagging obrigatório e permissões mínimas por default**, para evitar alterações acidentais e garantir rastreabilidade.

**Critérios de aceitação (BDD).**
- **Dado** um novo projeto IaC  
  **Quando** é inicializado  
  **Então** tem diretórios segregados (`envs/dev/`, `envs/staging/`, `envs/prod/`) e `variable "environment"` obrigatória.  
- **Dado** um recurso criado (ex: S3 bucket, security group)  
  **Quando** é provisionado  
  **Então** possui **tags obrigatórias**: Environment, Owner, Application, Criticality, ManagedBy.  
- **Dado** uma role ou permissão  
  **Quando** é criada  
  **Então** tem **scope mínimo** (ex: `s3:GetObject` para apenas um bucket, não `s3:*`).

**Checklist.**
- [ ] Diretórios de ambiente segregados  
- [ ] Tags obrigatórias em todos os recursos  
- [ ] Permissões com princípio de privilégio mínimo  
- [ ] Validação de tagging + permissões em policy-as-code  
:::

**🧾 Artefactos & evidências.**  
Estrutura de repositório (`envs/`), código de módulo com `tags` obrigatórias, política OPA/Rego validando presença de tags, output de `terraform plan` mostrando permissões.

**⚖️ Proporcionalidade.**
| Nível | Obrigatório? | Ajustes |
|---|---:|---|
| L1 | Sim | Segregação básica + tags simples |
| L2 | Sim | Segregação + tags completas + validação de permissões |
| L3 | Sim | Segregação + tags + permissões mínimas + enforcement em OPA |

---

### US-03 – Validações automáticas integradas

**Contexto.**  
Erros de sintaxe, configurações inseguras e violações de políticas devem ser detetadas **antes** de qualquer aplicação em ambiente real.

:::userstory
**História.**  
Como **Developers** e **AppSec Engineers**, quero **validações automáticas obrigatórias no pipeline** (lint, segurança, policies), para bloquear erros e configurações perigosas.

**Critérios de aceitação (BDD).**
- **Dado** um commit com IaC  
  **Quando** é feito push  
  **Então** **linters** (`terraform fmt`, `tflint`) e **scanners de segurança** (`tfsec`, `checkov`) correm automaticamente.  
- **Dado** uma violação de política crítica  
  **Quando** é detetada  
  **Então** o pipeline **bloqueia o merge** e reporta em PR.  
- **Dado** um `plan` falhado  
  **Quando** não passa validação mínima  
  **Então** é impedido o `apply`.

**Checklist.**
- [ ] Linters (`terraform validate`, `tflint`) no CI/CD  
- [ ] Scanners de segurança (`tfsec`, `checkov`)  
- [ ] Policy-as-code (OPA/Rego, Sentinel)  
- [ ] Pre-commit hooks obrigatórios  
:::

**🧾 Artefactos & evidências.**  
Relatórios de lint, outputs de scanners, logs de pipeline, badges de conformidade.

**⚖️ Proporcionalidade.**
| Nível | Obrigatório? | Ajustes |
|---|---:|---|
| L1 | Sim | Linters + aviso |
| L2 | Sim | Linters + scanners + bloqueio severo |
| L3 | Sim | Linters + scanners + policies + cobertura 100% |

---

### US-04 – Governança e origem confiável de módulos

**Contexto.**  
Módulos mal mantidos ou não verificados propagam riscos na cadeia de fornecimento. É necessário validar origem, versão, conformidade e proveniência antes de permitir uso.

:::userstory
**História.**  
Como **AppSec Engineers**, **Arquitetos de Software** e **DevOps / SRE**, quero **governança formal de módulos com verificação de origem confiável**, para evitar propagação de má prática e reduzir risco de supply chain.

**Critérios de aceitação (BDD).**

**Fase 1: Governança & Aprovação**
- **Dado** um módulo externo novo  
  **Quando** é referenciado no projeto  
  **Então** deve constar de **allowlist** e estar **pinned a versão exata** (sem `main`, `latest`).  
- **Dado** um módulo interno  
  **Quando** é publicado  
  **Então** passou por **testes automatizados**, **linting** e **revisão explícita**.  
- **Dado** uma atualização de módulo  
  **Quando** tem vulnerabilidade reportada  
  **Então** é marcada e revisão de uso é **obrigatória**.

**Fase 2: Origem Confiável & Verificação**
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
- [ ] Repositório central de módulos internos versionado  
- [ ] **Whitelist/allowlist** de fontes externas publicada  
- [ ] **Pinning de versão** verificado em pipeline  
- [ ] **SBOM** de módulos em cada deploy  
- [ ] Política de **allowlist/denylist** publicada  
- [ ] **Digest/SHA256** verificado em *pipeline*  
- [ ] **Attestation** exigida para fontes externas  
:::

**🧾 Artefactos & evidências.**  
Registry de módulos, policy de whitelist, SBOM, registos de aprovação, histórico de updates, verificação de digest/attestation, logs de pipeline com gate de origem.

**⚖️ Proporcionalidade.**
| Nível | Obrigatório? | Ajustes |
|---|---:|---|
| L1 | Sim | Whitelist simples + versionamento + pinning |
| L2 | Sim | Whitelist + validação automática + SBOM + digest verificado |
| L3 | Sim | Whitelist + validação + SBOM + attestation e revisão AppSec; denylist ativa |

---

### US-05 – Rastreabilidade, versionamento e naming

**Contexto.**  
Alterações devem ser rastreáveis via Git com convenções formais de commit, tagging e releases. Nomes de recursos devem seguir padrão consistente.

:::userstory
**História.**  
Como **DevOps / SRE** e **GRC / Compliance**, quero **histórico completo de alterações com naming conventions, tags git e releases versionadas**, para suportar rollback e auditoria.

**Critérios de aceitação (BDD).**
- **Dado** uma alteração de infraestrutura  
  **Quando** é comitada  
  **Então** segue padrão: `[IaC] Tipo de mudança em ambiente Y (issue-XXX)` e liga a ticket.  
- **Dado** uma release pronta  
  **Quando** é promovida para produção  
  **Então** é criada tag git com formato semântico (`iac-prod-v2025.07.10`, hash, timestamp).  
- **Dado** uma convenção de naming  
  **Quando** é violada  
  **Então** é rejeitada por pre-commit hook ou linter.

**Checklist.**
- [ ] Convenções de naming definidas (`app-env-resource-counter`)  
- [ ] Pre-commit hooks validam padrão  
- [ ] Tagging semântico em releases  
- [ ] Documentação de changelog  
:::

**🧾 Artefactos & evidências.**  
Ficheiro `NAMING.md`, logs de Git com commits estruturados, tags e releases no repositório, output de pre-commit validação.

**⚖️ Proporcionalidade.**
| Nível | Obrigatório? | Ajustes |
|---|---:|---|
| L1 | Recomendado | Naming simples + git básico |
| L2 | Sim | Naming + convenções commit + tagging |
| L3 | Sim | Naming + convenções + tagging semântico + CHANGELOG |

---

### US-06 – Revisão formal de plan antes de apply

**Contexto.**  
O `terraform plan` (ou equivalente) deve ser revisto e aprovado antes de qualquer aplicação. Isso permite validar impacto, detectar alterações inesperadas e associar a change request.

:::userstory
**História.**  
Como **DevOps / SRE** e **AppSec Engineers**, quero **aprovação formal de `terraform plan` em PR antes de `apply`**, para validar impacto e associar a change control.

**Critérios de aceitação (BDD).**
- **Dado** um PR com mudança de IaC  
  **Quando** é submetida  
  **Então** o pipeline executa `terraform plan` e anexa output legível no comentário do PR.  
- **Dado** o plan é revisto  
  **Quando** não há alterações inesperadas  
  **Então** recebe aprovação explicit (co-sign de no mínimo 2 roles: DevOps + AppSec).  
- **Dado** um `apply` agendado  
  **Quando** corresponde a ambiente crítico (staging/prod)  
  **Então** requer **dupla aprovação** e **janela de mudança**.

**Checklist.**
- [ ] Pipeline executa `terraform plan` em PR  
- [ ] Plan output anexado legível  
- [ ] Aprovação requerida (no mínimo 2 roles)  
- [ ] Auditoria de aprovação registada  
:::

**🧾 Artefactos & evidências.**  
PR com plan anexado, comentários de aprovação, logs de gate em pipeline, trilha de aprovações.

**⚖️ Proporcionalidade.**
| Nível | Obrigatório? | Ajustes |
|---|---:|---|
| L1 | Recomendado | Plan anexado em PR |
| L2 | Sim | Plan + aprovação simples |
| L3 | Sim | Plan + dupla aprovação + janela de mudança |

---

### US-07 – Rastreabilidade ficheiro → recurso → ambiente

**Contexto.**  
Deve haver mapeamento claro entre alterações em ficheiros IaC, recursos criados e ambientes afetados. Isso suporta accountability e avaliação de impacto.

:::userstory
**História.**  
Como **GRC / Compliance** e **Auditores Internos**, quero **mapeamento documentado de ficheiro IaC → recurso → ambiente**, para validar impacto e rastreabilidade.

**Critérios de aceitação (BDD).**
- **Dado** um recurso em produção  
  **Quando** preciso identificar origem  
  **Então** consigo mapear: ficheiro `.tf` (branch + commit) → recurso (ID, nome) → ambiente (prod).  
- **Dado** uma auditoria de conformidade  
  **Quando** é executada  
  **Então** consigo gerar relatório de "recurso criado em ambiente X por quem, quando, com que código".  
- **Dado** metadata em código  
  **Quando** é preservada (ex: `locals { application = "..." }`, tags com aplicação)  
  **Então** facilita rastreabilidade automática.

**Checklist.**
- [ ] Metadata em `locals` com aplicação, owner, versão  
- [ ] Tags incluem aplicação e team  
- [ ] Dashboard/script que mapeia recurso → ficheiro → commit  
- [ ] Documentação de relações entre módulos  
:::

**🧾 Artefactos & evidências.**  
Metadata em código, tags em recursos, dashboard de rastreabilidade, script de mapeamento, logs de `terraform apply` com artefactos.

**⚖️ Proporcionalidade.**
| Nível | Obrigatório? | Ajustes |
|---|---:|---|
| L1 | Recomendado | Metadata em locals |
| L2 | Sim | Metadata + tags + documentação |
| L3 | Sim | Metadata + tags + dashboard automático de rastreabilidade |

---

### US-08 – Enforcement automático de políticas

**Contexto.**  
Políticas de segurança devem ser aplicadas automaticamente via OPA/Sentinel/Rego no pipeline, sem depender exclusivamente de revisão manual.

:::userstory
**História.**  
Como **AppSec Engineers** e **DevOps / SRE**, quero **enforcement automático de políticas em pipeline** (bloqueio de permissões amplas, ausência de tags, etc.), para aplicar conformidade sistemática.

**Critérios de aceitação (BDD).**
- **Dado** um recurso com permissões amplas (ex: `s3:*`)  
  **Quando** é validado em `conftest` ou OPA  
  **Então** é **rejeitado automaticamente** com mensagem clara.  
- **Dado** uma política configurada (ex: "todos buckets S3 devem ter versionamento")  
  **Quando** é executada no pipeline  
  **Então** bloqueia `apply` se não for cumprida.  
- **Dado** uma exceção justificada  
  **Quando** é registada (ex: comentário `# opa-exception: IAC-003`)  
  **Então** é auditada e contabilizada em métricas de conformidade.

**Checklist.**
- [ ] Regras OPA/Rego/Sentinel definidas e versionadas  
- [ ] Integração em pipeline (pre-merge, pre-apply)  
- [ ] Mecanismo de exceção rastreável  
- [ ] Métricas de conformidade (% bloqueios, exceções ativas)  
:::

**🧾 Artefactos & evidências.**  
Regras OPA em repositório, output de execução, logs de bloqueios, exceções registadas, métricas de conformidade.

**⚖️ Proporcionalidade.**
| Nível | Obrigatório? | Ajustes |
|---|---:|---|
| L1 | Recomendado | Validação básica em pipeline |
| L2 | Sim | OPA/Rego com enforcement, logs de bloqueios |
| L3 | Sim | OPA/Rego + exceções formais + métricas + revisão trimestral |

---

### US-09 – Assinatura e Proveniência de artefactos IaC

**Contexto.**  
Sem proveniência verificável, *plans* e *applies* podem ser adulterados. Assinaturas e **attestations** devem ser verificadas **antes da promoção**.

:::userstory
**História.**  
Como **DevOps / SRE** e **AppSec Engineers**, quero **assinar *plans* e registar *attestations* de *pipeline***, para garantir integridade ponta-a-ponta até ao *apply* em ambiente crítico.

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

> **Padrão Comum:** Assinatura e verificação de proveniência ocorrem em **múltiplos contextos** (CI/CD, IaC, imagens, deploy).
> Este US foca o contexto de **módulos e *plans* de IaC**; ver também **Cap 07-US-06** (CI/CD),
> **Cap 09-US-03** (imagens), **Cap 11-US-01** (deploy). Todos aplicam o **mesmo princípio** (sign → validate → use).

---

### US-10 – Gestão de segredos e identidades para IaC

**Contexto.**  
Chaves estáticas em *providers* ou *runners* representam risco elevado. Preferir **OIDC / workload identity**, *scopes* mínimos e **TTL curto**.

:::userstory
**História.**  
Como **DevOps / SRE** e **AppSec Engineers**, quero **emitir credenciais temporárias via OIDC/workload identity** com **permissões mínimas**, para eliminar chaves long-lived e reduzir abuso.

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

### US-11 – Deteção e correção de *drift*

**Contexto.**  
Mudanças manuais no *runtime* criam **desalinhamento** (*drift*) com o IaC. É necessário **auditar** e **corrigir** de forma controlada.

:::userstory
**História.**  
Como **AppSec Engineers** e **DevOps / SRE**, quero **auditorias periódicas de *drift*** e **correção controlada**, para manter coerência entre IaC e infraestrutura.

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

### US-12 – *Rollback* e salvaguarda de *destroy*

**Contexto.**  
Falhas de *apply* e *destroy* acidentais têm impacto elevado. É necessária **estratégia de *rollback*** e *guardrails*.

:::userstory
**História.**  
Como **DevOps / SRE**, quero **pontos de restauração**, **confirmações explícitas** para *destroy* e **procedimento de *rollback***, para reduzir *downtime* e evitar perda de dados.

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

### US-13 – Janela de mudança e aprovações por papel

**Contexto.**  
Alterações em ambientes críticos exigem **janela de mudança** e **aprovação multinível**.

:::userstory
**História.**  
Como **GRC / Compliance**, **AppSec Engineers** e **Auditores Internos**, quero **janelas de mudança definidas** e **aprovações por papel** antes do *apply* em `prod`, para reduzir risco operacional.

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

### US-14 – Exceções formais em IaC

**Contexto.**  
Nem todas as políticas podem ser cumpridas em todas as circunstâncias. Exceções devem ser **temporárias**, **justificadas** e com **compensações** (addon/09).

:::userstory
**História.**  
Como **GRC / Compliance** e **AppSec Engineers**, quero **exceções registadas** com **prazo** e **contramedidas**, para evitar dívida estrutural.

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

> **Referência:** Este US implementa [Cap 14-US-01: Processo formal de exceções]
> no contexto de Infrastructure-as-Code. Aprovação dupla, TTL e compensações devem seguir a política master de exceções em Cap 14.

**⚖️ Proporcionalidade.**
| Nível | Obrigatório? | Ajustes |
|---|---:|---|
| L1 | Sim | Aprovação única |
| L2 | Sim | Aprovação dupla (AppSec+PO) |
| L3 | Sim | Aprovação AppSec+GRC e *review* por sprint |

---

## 🛡️ Princípios de SbD Reforçados em IaC

### Fail Securely (Falhar com Segurança)

O princípio de **fail securely** em IaC estabelece que recursos e permissões devem ter **defaults seguros** por omissão, com **recusa explícita** em vez de permissão ampla:

**Implementação prática (US-02, US-06, US-09):**
- Recursos criados **sem permissões**; permissões são adicionadas explicitamente após justificação
- Exemplo: `aws_s3_bucket` com `block_public_acls = true` como default automático
- Policy-as-code rejeita qualquer S3 bucket **sem** *server-side encryption* ativada
- Regra Rego: `deny[msg] { input.resource == "aws_s3_bucket" }`  com ausência de encriptação

**Checklist de validação (reforço em US-03, US-09):**
- [ ] Validação de defaults seguros em **policy-as-code** (OPA/Sentinel)
- [ ] Rejeição automática de recursos sem conformidade mínima
- [ ] Documentação de exceções a defaults (rastreáveis e temporárias)

---

### Desacoplamento entre Módulos e Ambientes

O princípio de **desacoplamento** previne dependências circulares ou implícitas que comprometem a reutilização e criatividade:

**Implementação prática (US-02, US-04, US-05):**
- Módulos IaC não contêm **hardcodes** de outputs de outros módulos
- Exemplo ERRADO: `security_group_id = module.network.security_group_id` hardcoded
- Exemplo CERTO: `security_group_id = var.security_group_id` (passado como variável)
- Ambientes segregados não contêm referências cruzadas entre backend states

**Checklist de validação (reforço em US-03, US-06):**
- [ ] Linter detecta hardcodes e interdependências inválidas
- [ ] Módulos publicados com outputs documentados e tipados
- [ ] Testes automatizados validam independência de módulos

---

## 📦 Artefactos & Evidências Esperadas

Cada prática deixa uma pegada objetiva.  
Sem evidência, não há conformidade. A tabela abaixo resume os outputs esperados.

| Artefacto/Evidência                   | Origem / US | Observações                         |
|---------------------------------------|-------------|-------------------------------------|
| `backend.tf` + logs de locking        | US-01       | Prova de locking e encriptação KMS  |
| Estrutura de diretórios por ambiente  | US-01       | `dev/`, `staging/`, `prod/`         |
| Relatórios de lint/security/policies  | US-02       | Arquivados em pipeline              |
| Configuração de validações em CI/CD   | US-02       | Pré-commit hooks + pipeline jobs    |
| Lista de módulos aprovados            | US-03       | Allowlist de fontes externas + SBOM |
| Registry de módulos internos          | US-03       | Versionado e com documentação       |
| Diretórios `envs/dev`, `envs/staging`, `envs/prod` | US-05 | Segregação física |
| Tags obrigatórias em recursos         | US-05       | Environment, Owner, Application, Criticality, ManagedBy |
| Política de permissões mínimas (OPA)  | US-05       | Regras de validação de IAM |
| `NAMING.md` + pre-commit hooks        | US-06       | Convenções de nomeação |
| Histórico Git com padrão de commits   | US-06       | `[IaC] Tipo em ambiente (issue-XXX)` |
| Tags git semânticas e releases        | US-06       | `iac-prod-v2025.07.10` |
| PR com `terraform plan` anexado       | US-07       | Aprovação formal antes do apply     |
| Trilha de aprovações multinível       | US-07       | DevOps + AppSec |
| Dashboard/script de rastreabilidade   | US-08       | Mapas ficheiro→recurso→ambiente     |
| Metadata em `locals` (app, owner)     | US-08       | Aplicação e equipa associadas       |
| Regras OPA/Rego/Sentinel versionadas  | US-09       | Enforcement policy-as-code |
| Logs de bloqueios e conformidade      | US-09       | Métricas de enforcement, exceções ativas |
| Lista de módulos aprovados (origem)   | US-04       | Origem + hash/version               |
| `CHANGELOG`, tags, releases           | US-05       | Evidência de change control         |
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
| Validações automáticas              | Aviso           | Bloqueio falhas severas   | Bloqueio total + cobertura completa      |
| Governança de módulos               | Whitelist simples | Whitelist + validação automática | Whitelist + validação + SBOM + aprovação |
| **Segregação ambientes + tagging**  | **Recomendado** | **Obrigatório + tagging completo** | **Obrigatório + tags + validação OPA** |
| **Rastreabilidade e naming**        | **Recomendado** | **Obrigatório + convenções formais** | **Obrigatório + pre-commit + CHANGELOG** |
| **Revisão formal de plan**          | **Recomendado** | **Obrigatório** | **Obrigatório + dupla aprovação** |
| **Rastreabilidade ficheiro→recurso**| **Recomendado** | **Obrigatório + documentação** | **Obrigatório + dashboard automático** |
| **Enforcement de políticas**        | **Recomendado** | **OPA/Rego obrigatório** | **OPA + exceções formais + métricas** |
| Origem confiável de módulos         | Recomendado     | Obrigatório + pinagem     | Obrigatório + proveniência formal        |
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