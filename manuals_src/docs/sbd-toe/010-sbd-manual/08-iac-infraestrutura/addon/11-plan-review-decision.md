---
id: plan-review-decision
title: Plan Review & Decisão de Apply
description: Framework de decisão para revisão de terraform plan com separação explícita sugestão/decisão
tags: [iac, plan, decisão, i1, invariantes, terraform]
---

# ✅ Plan Review & Decisão de Apply

## 🌟 Objetivo

Implementar o Invariante **I1 (Separação sugestão/decisão)** de [agent.md](https://github.com/your-org/agent-spec) no contexto de IaC (Infrastructure as Code).

Terraform `plan` gera **sugestões** de mudanças (create, update, destroy resources). Porém, a decisão de **aceitar, revisar ou rejeitar o plan** deve ser **explícita, documentada e auditável**, com papéis bem definidos baseados no impacto e classificação de risco (L1/L2/L3).

---

## 📋 Contexto normativo

**Problema:**
- Terraform plan reporta "Create S3 bucket, update security group, destroy old DB" sem contexto de negócio
- DevOps pressão para "just apply it" → Mudanças em prod sem análise de impacto
- Sem decisão documentada: "Who approved this?" in auditoria = impossível de responder
- Destroy operations especialmente perigosas (dados perdidos) mas aplicadas sem checklist

**Solução:**
Framework 4-fase que torna a decisão **explícita, documentada e auditável**:
1. Plan gerado com estimated changes reportado
2. Plan análisado com Checklist I1 (4 questões)
3. Documented decision (ACEITAR-apply / REVISAR-plan / REJEITAR-plan)
4. Escalation procedures para conflitos (timeline, policy, impact disputes)

---

## 🛠️ Framework 4-Fase

### Fase 1: Plan Gerado (Suggestions Reported)

**Entrada:** Terraform plan output:
```
Plan: 3 to add, 2 to change, 1 to destroy
Resource changes:
  + aws_s3_bucket.data (new resource)
  ~ aws_security_group.api (update in-place)
  - aws_db_instance.old (destroy)
```

**Análise automática:**
- Número de resources (impacto volume)
- Operações destrutivas presentes? (HIGH risk)
- Classificação: L1 changes (low impact) vs. L3 changes (critical data)
- Ambientes afetados: dev, staging, prod?

### Fase 2: Plan Análise com Checklist I1

**Responsável:** DevOps Engineer (inicial analysis) ou Architect (L2/L3 critical changes)

**Checklist I1 — 4 Questões de Validação:**

:::userstory
**História.**  
Como **DevOps Engineer ou Architect**, quero **validar se um terraform plan é justified**, para tomar decisão informada entre ACEITAR-apply, REVISAR-plan, ou REJEITAR-plan.

**Checklist C1: Validação de Plan**

- [ ] **C1.1 — Plan matches business intent?**
  - [ ] Was this plan change requested (issue, ticket, PR)?
  - [ ] Do the resources match the intended outcome?
  - [ ] Are any unexpected changes present?
  - [ ] Is number of create/update/destroy operations proportional to request?
  - **Evidence needed:** Issue/ticket linking plan, code review comments validating changes
  - **Example JUSTIFIED:** Issue "Add metrics S3 bucket" → Plan creates S3 bucket + IAM role (correct, proportional)
  - **Example UNJUSTIFIED:** Plan destroys "db_backup" but request was "add monitoring" (scope creep, plan rejected)

- [ ] **C1.2 — Resources are properly tagged?**
  - [ ] All resources have required tags (Environment, Application, Owner, Criticality)?
  - [ ] Tag values are correct for target environment?
  - [ ] Resource naming follows conventions (no typos or ambiguous names)?
  - **Evidence needed:** Plan output shows tags, naming validation passed
  - **Example GOOD:** Resource `aws_s3_bucket.prod_metrics_data` has tags `{Environment="prod", Application="metrics", Owner="data-team"}`
  - **Example BAD:** Resource `aws_s3_bucket.bucket1` has no tags or tag says `Environment="staging"` but being deployed to prod

- [ ] **C1.3 — Security configuration is appropriate for environment + classification?**
  - [ ] Is resource classification (L1/L2/L3) respected in plan?
  - [ ] Security group rules are restrictive (principle of least privilege)?
  - [ ] IAM policies grant minimum permissions needed?
  - [ ] Encryption, versioning, logging are enabled for L2/L3 resources?
  - **Evidence needed:** Security review, tfsec/checkov reports showing no critical violations
  - **Example GOOD:** L3 database has encryption enabled, backup configured, IAM access restricted to specific roles
  - **Example BAD:** L3 database created with default (unencrypted), all roles granted admin access

- [ ] **C1.4 — Resource dependencies and order are correct?**
  - [ ] Will resources be created in correct order (dependencies satisfied)?
  - [ ] Are there circular dependencies?
  - [ ] Are outputs from one resource used correctly in another?
  - [ ] Destroy operations: can resources be safely deleted without breaking dependencies?
  - **Evidence needed:** Terraform dependency graph (terraform graph), manual code review
  - **Example GOOD:** Database created before application with database endpoint passed via output
  - **Example BAD:** Application deployed before database exists, destroy order will break app

**Approval Criteria:**  
All 4 checklist items must have evidence for DevOps to proceed to Phase 3 (Documented Decision).
If any item has concerns, escalate to Architect or AppSec (see Phase 4: Escalation).
:::

**Output from Phase 2:**
- Completed Checklist C1 (all 4 questions answered with evidence)
- Risk assessment: Low/Medium/High based on answers
- Decision draft (ACEITAR / REVISAR / REJEITAR)
- Escalation flag (if conflict or high risk)

### Fase 3: Documented Decision com Decisores Explícitos

**Entrada:** Checklist C1 completado + decision draft

**Decisores por Plan Impact (Matriz Decisores):**

| Plan Impact | Analyzer | Reviewer | Approver | SLA |
|---|---|---|---|---|
| **Low** (L1, <5 resources, no destroy) | DevOps | — | — (auto-apply) | Immediate |
| **Medium** (L1-L2, 5-20 resources, minor destroy) | DevOps | Architect | — | 4 hours |
| **High** (L2-L3, >20 resources, critical destroy) | DevOps + Architect | AppSec | Release Manager | 2 hours |
| **Critical** (L3, database destroy, IAM policy changes) | DevOps + Architect | AppSec + Lead | Release Manager + CISO | 1 hour |

**Decision Template (Template T1):**

```markdown
# IaC Plan Review & Decision Log

**Plan ID:** TF-2026-01-20-001 (internal tracking)
**Terraform Environment:** prod-metrics
**Date:** 2026-01-20 14:30 UTC
**Triggered by:** PR #456 "Add metrics aggregation infrastructure"

## Plan Summary

- **Change type:** Create infrastructure
- **Resources:** 8 to add, 2 to change, 0 to destroy
- **Environments affected:** prod
- **Estimated cost increase:** +$450/month (compute + storage)
- **Risk level:** MEDIUM (new L2 infrastructure)

### Resources affected:
1. + aws_s3_bucket.metrics_data (L2, encryption enabled)
2. + aws_lambda_function.metrics_processor (L2, OIDC role)
3. + aws_dynamodb_table.metrics_cache (L2, backup enabled)
4. ~ aws_security_group.api (update: add port 443 ingress)
5. ~ aws_iam_policy.lambda_execution (add DynamoDB permissions)

## Checklist C1 Results

✅ **C1.1 — Plan matches business intent?**
- Request: Issue #123 "Implement metrics aggregation pipeline"
- Plan creates: S3 bucket (data storage), Lambda (processor), DynamoDB (cache)
- Expected? YES (all 3 components requested in issue)
- Unexpected changes? NO (only security group update for HTTPS, which is required)
- Proportional? YES (8 create, 2 update for 1 feature)
- **Conclusion:** Plan is JUSTIFIED and matches intent

✅ **C1.2 — Resources properly tagged?**
- All 8 new resources have tags:
  - Environment = prod
  - Application = metrics
  - Owner = data-eng-team
  - Criticality = L2
- Naming: `metrics_data`, `metrics_processor` (clear, follows convention)
- **Conclusion:** Tagging COMPLETE and CORRECT

✅ **C1.3 — Security appropriate for L2?**
- S3 bucket: Encryption enabled (AES-256), versioning enabled, public access blocked
- Lambda: OIDC role with minimum permissions (S3:GetObject, DynamoDB:PutItem), no wildcard permissions
- DynamoDB: Encryption enabled, point-in-time recovery enabled, backup configuration set
- Security group: Update adds HTTPS ingress (443) from ALB only, no overly permissive rules
- Checkov report: 0 critical, 1 warning (acceptable, remediation planned next sprint)
- **Conclusion:** Security configuration is APPROPRIATE for L2 resources

✅ **C1.4 — Dependencies and order correct?**
- Dependency graph: S3 bucket created first (independent), Lambda created second (depends on S3 for code), DynamoDB created parallel to Lambda
- Outputs: S3 bucket name passed to Lambda environment variable, DynamoDB table name passed to Lambda
- Destroy order: Lambda destroyed first (no data), then DynamoDB (backup created before destroy), then S3 (versioning allows recovery)
- No circular dependencies detected
- **Conclusion:** Dependencies are CORRECTLY ORDERED and SAFE to destroy

## Decision

**Decision Type:** ACEITAR-APPLY (Plan approved, ready for immediate apply)

**Decision Reasoning:**
- All 4 checklist items validated successfully
- Plan matches business intent (Issue #123)
- Security configuration appropriate for L2
- Dependencies and ordering correct
- Estimated cost within budget approval
- Risk level: MEDIUM (acceptable for this change type)
- Timeline: No urgency, standard review SLA met
- **Therefore:** Plan approved for apply to prod

**Decisores:**
- **Phase 2 (Analysis):** João Silva, DevOps Engineer (2026-01-20 14:30 UTC)
  - Checklist C1: ✅ Complete, all 4 items validated
  - Risk assessment: MEDIUM (acceptable)
  - Decision draft: ACEITAR-APPLY
  - Escalation flag: None
  
- **Phase 3 (Validation):** Carlos Architect, Senior Architect (2026-01-20 15:00 UTC)
  - Reviewed checklist C1: Agreed
  - Plan scope: Matches issue #123 correctly
  - Security review: L2 configuration appropriate
  - Cost impact: Within approved budget
  - Validation: APPROVED to apply
  
- **Phase 4 (Release Approval):** Maria Garcia, Release Manager (2026-01-20 15:30 UTC)
  - All approvals in place: ✅
  - Change window: Approved (maintenance window 2026-01-20 16:00 UTC)
  - Rollback plan: Reviewed and validated
  - Release approval: ✅ GRANTED

## Implementation

**Action Items:**
1. **Apply Plan:**
   - [ ] Execute `terraform apply` in prod-metrics workspace
   - [ ] Verify all 8 resources created successfully
   - [ ] Verify 2 security group + IAM updates applied correctly
   - Owner: João Silva + DevOps team
   - Timeline: 2026-01-20 16:00 UTC (within change window)

2. **Post-Apply Validation:**
   - [ ] Test S3 bucket access (upload/download test file)
   - [ ] Test Lambda function (invoke with sample metrics)
   - [ ] Test DynamoDB queries (insert/query operations)
   - [ ] Verify CloudWatch logs for errors
   - [ ] Check cost monitoring dashboard (compare with estimate)
   - Owner: QA + Data Engineering
   - Timeline: 30 minutes post-apply

3. **Rollback Readiness:**
   - [ ] Backup of DynamoDB created before apply (point-in-time recovery enabled)
   - [ ] Previous state saved in Terraform (terraform.tfstate.backup)
   - [ ] Rollback plan documented (restore from backup, destroy new resources)
   - Owner: DevOps team
   - Timeline: Pre-apply

## Traceability

- **Issue:** #123 (Implement metrics aggregation pipeline)
- **PR:** #456 (IaC changes)
- **Terraform state:** prod-metrics.tfstate (versioned, encrypted)
- **Plan file:** prod-metrics-2026-01-20-001.tfplan (signed, retained 30 days)
- **Approval chain:** João → Carlos → Maria
- **Change window:** 2026-01-20 16:00-17:00 UTC
- **Incident ticket:** (if issues arise post-apply)

## Follow-up & Prevention

- [ ] Update metrics pipeline documentation with new resources
- [ ] Add integration tests for Lambda + DynamoDB
- [ ] Cost monitoring: Alert if actual >20% of estimate
- [ ] Security scanning: Re-run checkov on monthly basis
- [ ] Lessons learned: Any deviations from checklist logged
```

**Key Decision Types:**

| Decision | Meaning | When Used | Impact |
|---|---|---|---|
| **ACEITAR-APPLY** | Accept plan as-is, apply immediately | Plan is sound, matches intent, security OK | Infrastructure deployed, changes in prod |
| **REVISAR-PLAN** | Plan has issues, revise and re-submit | Checklist item has concerns, dependencies wrong | Go back to dev, fix issues, re-create plan |
| **REJEITAR-PLAN** | Plan is fundamentally wrong, cancel | Plan doesn't match intent, security risks, critical errors | No changes deployed, issue re-triaged |

---

## 🔁 Escalation Procedures

**Escalation Triggers:**

1. **Conflict Type A: Timeline vs. Change Window**
   - **Scenario:** Plan requires 3 hours to apply, change window is 2 hours
   - **Escalation:** DevOps + Release Manager + Product Owner
   - **Resolution:** Extend change window OR defer plan to next window OR split plan into smaller chunks
   - **SLA:** 1 hour (decision must be made for continuity)

2. **Conflict Type B: Cost Impact Disputed**
   - **Scenario:** Plan shows +$450/month cost increase, budget approved only +$200/month
   - **Escalation:** DevOps + Finance + Product Owner
   - **Resolution:** Optimize resources (downsize instances) OR request budget exception OR defer feature
   - **SLA:** 4 hours (budget decisions are time-sensitive)

3. **Conflict Type C: Security Policy Mismatch**
   - **Scenario:** Plan creates S3 bucket without encryption, security policy requires encryption for L2
   - **Escalation:** DevOps + AppSec + Architect
   - **Resolution:** Modify plan to enable encryption OR document exception with compensating controls
   - **SLA:** 2 hours (security issues block apply)

**Escalation Workflow (Template T2):**

```markdown
# IaC Plan Escalation

**Plan ID:** TF-2026-01-21-002
**Escalation Type:** Type A (Timeline vs. Change Window)
**Initiated:** 2026-01-21 by João Silva (DevOps)
**Date:** 2026-01-21 09:00 UTC

## Conflict

**Situation:** Plan requires database migration (3-hour apply duration). Standard change window is 2 hours (weekend 02:00-04:00 UTC).

**DevOps Claim:** "Migration will take 3 hours. Current window only 2 hours. Need extended window."

**Change Manager Concern:** "Extended window costs extra. Need business justification."

**Product Owner Pressure:** "Need this migration done this weekend. Can't wait until next week."

## Investigation

**DevOps (João):** "DynamoDB migration involves: (1) Create new table (30min), (2) Copy 50GB data (90min), (3) Switch routing (30min), (4) Cleanup old table (30min). Total: 3 hours."

**Change Manager (Pedro):** "Extended windows cost $500 extra. Need approval from finance/product."

**Release Manager (Maria):** "Can we split plan? Apply creation on Friday, switch on Saturday?"

**Product Owner (Alex):** "Business needs this completed this weekend. Approve extended window."

**Finance (Rita):** "Approve $500 for extended window."

## Resolution

**Decision:** ACEITAR-APPLY with extended change window

1. **Extended Change Window Approved:**
   - [ ] Window extended to 4 hours (02:00-06:00 UTC on 2026-01-22)
   - [ ] Cost: $500 approved by finance
   - [ ] Communications sent to on-call team + monitoring

2. **Plan Adjustments:**
   - [ ] No changes to plan itself (already optimized)
   - [ ] Rollback plan updated: Can rollback table switching (30min) if migration fails

3. **Risk Mitigation:**
   - [ ] DynamoDB backup created pre-migration (point-in-time recovery)
   - [ ] Read replicas in standby mode (can switch if needed)
   - [ ] Monitoring alerts configured for migration (duplicate writes, replication lag)

**Approved by:** Pedro (Change Manager), Alex (Product Owner), Rita (Finance)
**Signed:** 2026-01-21 10:00 UTC
**Applied:** 2026-01-22 02:00-06:00 UTC (extended window)
```

---

## 📊 Matriz Decisores (por Plan Impact e Nível de Classificação)

**Objetivo:** Determinar quem decide em cada cenário, responsabilidade clara

### L1 (Baixo Risco)

| Plan Impact | Analyzer | Reviewer | Approver | Required Checklist | SLA |
|---|---|---|---|---|---|
| Low (<5 res, no destroy) | DevOps | — | — | C1.1, C1.2 | Immediate |
| Medium (5-20 res, minor destroy) | DevOps | Architect | — | Full C1 | 4 hours |

### L2 (Risco Médio)

| Plan Impact | Analyzer | Reviewer | Approver | Required Checklist | SLA |
|---|---|---|---|---|---|
| Low | DevOps | Architect | — | C1.1, C1.2 | 4 hours |
| Medium | DevOps | Architect | Release Manager | Full C1 + cost review | 4 hours |
| High (>20 res, critical destroy) | DevOps + Architect | AppSec | Release Manager | Full C1 + security scan | 2 hours |

### L3 (Risco Crítico)

| Plan Impact | Analyzer | Reviewer | Approver | Required Checklist | SLA |
|---|---|---|---|---|---|
| Medium | DevOps + Architect | AppSec | Release Manager | Full C1 + AppSec scan | 2 hours |
| High | DevOps + Architect | AppSec + Architect | Release Manager | Full C1 + AppSec scan + cost review | 2 hours |
| Critical (DB destroy, IAM policy change) | DevOps + Architect | AppSec + Lead | Release Manager + CISO | Full C1 + multiple scans + exception approval | 1 hour |

---

## 🎯 KPIs — Monitorização de Conformidade

**Métrica 1: Plan Review Documentation**
- **Definição:** % de plans (severity ≥ MEDIUM) com Checklist C1 documentado
- **Target:** 100% para L2/L3; ≥80% para L1
- **Cálculo:** (Plans com C1 / Total plans ≥ MEDIUM) × 100
- **Responsável:** DevOps Lead
- **Cadência:** Semanal

**Métrica 2: Plan Decision Time-to-Approval**
- **Definição:** Horas desde plan criado até decisão aprovada
- **Target:** <4h MEDIUM, <2h HIGH (L2/L3)
- **Cálculo:** Data/hora aprovação - Data/hora plan gerado
- **Responsável:** Release Manager
- **Cadência:** Semanal, P95 percentile

**Métrica 3: Plan Rejection Rate**
- **Definição:** % de plans rejeitados (decision = REJEITAR) vs. total
- **Target:** <5% (if >10%, planning phase inadequate)
- **Cálculo:** (Rejected plans / Total plans) × 100
- **Responsável:** Architect
- **Cadência:** Mensal

**Métrica 4: Destroy Operations Tracked**
- **Definição:** % de destroy operations com explicit approval documented
- **Target:** 100% para L2/L3; ≥95% para L1
- **Cálculo:** (Destroy ops approved / Total destroy ops) × 100
- **Responsável:** DevOps Lead
- **Cadência:** Semanal

**Métrica 5: Escalation Rate**
- **Definição:** % de plans requiring escalation (Type A, B, C conflicts)
- **Target:** <10% (if >20%, process has systemic issues)
- **Cálculo:** (Escalations / Total plans) × 100
- **Responsável:** Release Manager
- **Cadência:** Mensal

---

## 🔗 Integração com Invariantes de agent.md

**I1 — Separação sugestão/decisão:**  
✅ Framework implementado (Plan sugere → DevOps valida → Architect aprova → Release Manager autoriza)

**I2 — Evidência empírica:**  
↔️ Cross-reference: Ver [addon-12](./12-validacao-empirica-iac.md) para validação empírica de plan findings (tfsec, checkov reports)

**I3 — Reprodutibilidade:**  
✅ Plans versionadas em Git, decisões armazenadas em decision-logs/

**I4 — Proteção de ativos:**  
✅ Plan classification by L1/L2/L3 determina approval rigor

**I5 — Rastreabilidade:**  
✅ Audit trail completo (Plan → Checklist C1 → Decision T1 → Implementation → Rollback trail)

---

## 📎 Referências Cruzadas

| Documento | Relação |
|---|---|
| [addon-12: Validação Empírica de IaC](./12-validacao-empirica-iac.md) | I2 empirical testing de findings em plan |
| [Cap 07 — addon-11: Decisão Assistida em Gates](../../07-cicd-seguro/addon/11-decisao-gates-pipeline.md) | Similar I1 framework para pipeline gates |
| [aplicacao-lifecycle.md](./aplicacao-lifecycle.md) | US-19 operationalizes este addon |
| [agent.md](https://github.com/your-org/agent-spec) | Invariantes I1-I5 normativas |

---

## ✅ Checklist de Implementação

- [ ] **Onboarding:**
  - [ ] Treinar DevOps em Checklist C1 (4 questões)
  - [ ] Introduzir Decision Template T1 no fluxo de plans
  - [ ] Registar Escalation Workflow T2 em runbook

- [ ] **Processo:**
  - [ ] Criar policy: "All MEDIUM+ plans require Checklist C1 before apply"
  - [ ] Documentar Decisores por plan impact × level
  - [ ] Criar SLA para plan approval (Immediate/4h/2h/1h)

- [ ] **Tooling:**
  - [ ] Integrar terraform plan output com issue tracking
  - [ ] Criar workflow automático: "plan created" → "notify reviewers" → "create decision issue"
  - [ ] Setup dashboard: plans by status, approval time, rejection rate

- [ ] **Governance:**
  - [ ] Criar plan review board with defined roles
  - [ ] Estabelecer escalation procedures (Type A, B, C)
  - [ ] Implementar KPIs (dashboard + monthly review)

- [ ] **Validação:**
  - [ ] Teste com 3 plans reais (LOW, MEDIUM, HIGH impact)
  - [ ] Verificar tempos de decisão (vs. SLA)
  - [ ] Validar audit trail (Decision templates rastreáveis)

---

> 📌 **Princípio central:** Plans sugerem, HUMANS decidem.  
> A automação (checkov, tfsec) é facilitadora, não substitui julgamento sobre impacto de negócio.
