---
id: validacao-empirica-iac
title: Validação Empírica de Findings em IaC
description: Taxonomia com testes empíricos para validar IaC misconfigurations, FP/FN management
tags: [iac, validação, empirica, i2, invariantes, terraform, checkov]
---

# ✅ Validação Empírica de Findings em IaC

## 🌟 Objetivo

Implementar o Invariante **I2 (Evidência acima de plausibilidade)** de [agent.md](https://github.com/your-org/agent-spec) no contexto de validação de findings reportados por ferramentas de IaC scanning.

Ferramentas como `tfsec`, `checkov`, `kics` e `OPA` produzem **falsos positivos** (alertam quando não há risco) e **falsos negativos** (não alertam quando há risco real). A validação empírica confirma se plan violations são justified ou FPs que podem ser suprimidos.

---

## 📋 Contexto normativo

**Problema:**
- **Falso Positivo (FP):** Checkov reporta "S3 bucket must be encrypted" mas é data lake (encryption not required per policy)
- **Falso Negativo (FN):** Checker não detecta "RDS database has public access enabled" mas network rules allow external connections
- **Sem validação:** Team suppresses checkers (loses trust) OR applies all checks without understanding (over-restrictive, blocks deployments)

**Solução:**
Framework de validação empírica com:
- **Taxonomia:** 5 categorias de IaC violations (Security config, Policy violations, Tagging gaps, IAM permissions, Resource limits)
- **Testes:** Deploy in staging + verify if misconfiguration actually exploitable
- **FP Management:** Suppression com justificativa + VEX document
- **FN Detection:** RCA + custom rules + regression tests
- **Quality Metrics:** FP <20%, FN <5%, time-to-validation <2h

---

## 🧪 Taxonomia: 5 Categorias de IaC Violations

### 1️⃣ Security Configuration Gaps (Encryption, Logging, Versioning)

**Example Violation:**
```
Tool: checkov
Finding: S3 bucket does not have versioning enabled
Severity: MEDIUM
Resource: aws_s3_bucket.data_lake
Status: ⛔ BLOCKED
```

**Empirical Validation Checklist:**

:::userstory
**História.**  
Como **DevOps Engineer ou AppSec Engineer**, quero **validar empiricamente se security configuration gap é real risk**, para confirmar se bloquear apply é justified.

**Procedimento T1: Validação de Security Configuration**

1. **Entender intent da policy:**
   - [ ] Por quê versioning é obrigatório? (Data recovery? Audit trail? Compliance?)
   - [ ] É aplicável para este recurso? (backup S3 vs. versioned data?)
   - [ ] Existem compensating controls? (manual backups, snapshots, replication?)

2. **Testar impacto real:**
   - [ ] Fazer deploy sem versioning
   - [ ] Simular: delete object → can it be recovered?
   - [ ] Verificar: consegui recuperar dados sem versioning? (não = risk real)

   ```bash
   # Example: Test S3 versioning absence
   aws s3 cp s3://my-bucket/important.txt . # download file
   aws s3 rm s3://my-bucket/important.txt    # delete file
   aws s3 cp s3://my-bucket/important.txt . # try to recover
   
   # If no-versioning: file gone forever (RISK CONFIRMED)
   # If versioning existed: could recover from version history (RISK MITIGATED)
   ```

3. **Assess business context:**
   - [ ] É data lake (append-only, immutable?) → versioning not critical
   - [ ] É transient cache (temporary, ephemeral?) → versioning not needed
   - [ ] É critical production data (PCI, HIPAA?) → versioning mandatory

4. **Document result:**

   **If risk is REAL:**
   - Severity: CONFIRMED
   - Impact: Data loss risk without versioning
   - Decision: BLOQUEAR plan (enable versioning)
   - Fix: `versioning = { enabled = true }`

   **If risk is FALSE POSITIVE (FP):**
   - Reason: Data lake is append-only, versioning unnecessary
   - Evidence: Architecture review confirms immutability
   - Decision: SUPPRESS with justification
   - FP log: `falsos-positivos/FP-2026-01-20-S3-versioning-datalake.md`

:::

**Common FP Scenarios:**
- Versioning disabled for ephemeral/temporary data (cache, temporary processing)
- Encryption not required for public data (non-sensitive, already encrypted in transit)
- Logging disabled for non-critical resources (dev environment, test buckets)
- Backup not configured for data that's replicated elsewhere

**Common FN Scenarios:**
- Security group allows "0.0.0.0" but intended for load balancer (rule specific but overly permissive in appearance)
- Database not encrypted at rest, but encryption handled at application level (tool doesn't understand app context)
- No MFA on admin account, but MFA enforced by identity provider (tool checks IAM only)

---

### 2️⃣ Policy Violations (OPA/Sentinel Rules)

**Example Violation:**
```
Tool: OPA/Conftest
Finding: Resource created without required Environment tag
Severity: HIGH
Resource: aws_instance.web
Status: ⛔ BLOCKED
Message: "All resources must have Environment tag"
```

**Empirical Validation Checklist:**

:::userstory
**História.**  
Como **DevOps Engineer**, quero **validar empiricamente se policy violation é real enforcement issue**, para saber se permitir exceção.

**Procedimento T2: Validação de Policy Violations**

1. **Understand policy intent:**
   - [ ] Por quê Environment tag é obrigatório? (Cost center? Billing? Operational segregation?)
   - [ ] O que acontece sem tag? (Untrackable costs? Wrong environment?)
   - [ ] Existem resources que legitimamente não têm ambiente? (shared services?)

2. **Test impact of violation:**
   - [ ] Deploy resource sem tag
   - [ ] Simular: Como isso afeta operações? Monitoring? Cost tracking?
   - [ ] Consegui segregar recursos por ambiente sem tag? (não = policy essential)

   ```bash
   # Example: Test Environment tag enforcement
   # Deploy without Environment tag
   aws ec2 describe-instances --filters "Name=tag:Environment,Values=" 
   # If returns 0 → tag is tracked, policy working
   
   # Cost allocation test
   aws ce get-cost-and-usage --filter Environment=prod
   # If resource missing tag, costs unallocated (audit risk)
   ```

3. **Check for exceptions:**
   - [ ] Are there resources that legitimately don't need Environment tag?
   - [ ] Shared services (CI/CD runners, central logging) might not fit "prod/staging/dev"
   - [ ] Can we use different tag name for shared resources?

4. **Document result:**

   **If policy enforcement is REAL:**
   - Severity: CONFIRMED
   - Impact: Cost allocation broken, environment segregation fails
   - Decision: BLOQUEAR plan (add Environment tag)
   - Fix: `tags = { Environment = "prod", ... }`

   **If policy is FALSE POSITIVE (FP):**
   - Reason: Shared service doesn't fit Environment taxonomy
   - Evidence: Resource is cross-environment (managed infrastructure)
   - Decision: Document exception with alternative tagging
   - FP log: `falsos-positivos/FP-2026-01-20-OPA-environment-shared-service.md`

:::

**Common FP Scenarios:**
- Shared infrastructure (monitoring, logging, DNS) doesn't fit Environment tagging
- Third-party managed resources (where we don't control tagging)
- Temporary resources created for testing (short-lived, don't need full tagging)

**Common FN Scenarios:**
- Policy allows tag override without justification (policy too permissive)
- Policy checks only IAM tags but not resource tags (incomplete coverage)
- Policy enforced in some pipelines but not others (inconsistent application)

---

### 3️⃣ Tagging Gaps & Metadata Issues

**Example Violation:**
```
Tool: Checkov
Finding: Resource missing Owner tag
Severity: MEDIUM
Resource: aws_lambda_function.processor
Status: ⛔ BLOCKED
```

**Empirical Validation Checklist:**

:::userstory
**História.**  
Como **DevOps Engineer ou Architect**, quero **validar empiricamente se missing Owner tag impacta operações**, para confirmar se rejeitar plan.

**Procedimento T3: Validação de Tagging Gaps**

1. **Assess operational impact:**
   - [ ] Consegui identificar team responsável sem Owner tag? (não = operational risk)
   - [ ] Consegui escalate security issue? (sem owner = can't notify urgently)
   - [ ] Consegui fazer cost chargeback? (sem owner = unallocated costs)

2. **Test scenarios:**
   ```bash
   # Example: Test missing Owner tag impact
   # Query resources without Owner tag
   aws ec2 describe-instances --filters "Name=tag-key,Values=!Owner" --query 'Reservations[*].Instances[*].[InstanceId,Tags]'
   
   # If many unowned resources, tag is important
   # If none, tag might be redundant
   ```

3. **Check if tag is actually used:**
   - [ ] Are tags queried for automation? (cost allocation, access control, inventory)
   - [ ] Or just for documentation? (lower priority)

4. **Document result:**

   **If tag is REQUIRED:**
   - Decision: BLOQUEAR plan (add Owner tag)
   - Fix: `tags = { Owner = "data-eng-team", ... }`

   **If tag is OPTIONAL (FP):**
   - Reason: Resource is auto-managed (Terraform ownership is obvious)
   - Decision: SUPPRESS with documentation
   - FP log: `falsos-positivos/FP-2026-01-20-Owner-tag-terraform-managed.md`

:::

**Common FP Scenarios:**
- Tags are inherited from module (tool doesn't detect inheritance)
- Tags set via Terraform locals, not inline (tool expects inline)
- Multiple owners (team-managed, not single person)

**Common FN Scenarios:**
- Tags are set but with wrong values (policy doesn't validate values, only presence)
- Tags inherited from parent resource but tool checks only current resource

---

### 4️⃣ IAM Permissions (Over-Privileged Roles)

**Example Violation:**
```
Tool: tfsec / checkov
Finding: Lambda execution role has Admin permission
Severity: CRITICAL
Resource: aws_iam_role.lambda_exec
Status: ⛔ BLOCKED
```

**Empirical Validation Checklist:**

:::userstory
**História.**  
Como **AppSec Engineer**, quero **validar empiricamente se IAM permissions são realmente over-privileged**, para confirmar se bloquear é justified.

**Procedimento T4: Validação de IAM Permissions**

1. **Analyze actual needs:**
   - [ ] What does Lambda actually need? (S3:GetObject only? or PutObject too?)
   - [ ] Is admin permission accidental? (copy/paste from template?)
   - [ ] Or intentional design? (documented and approved?)

2. **Test with minimal permissions:**
   - [ ] Apply plan with minimal role (S3:GetObject only)
   - [ ] Test Lambda function: does it work?
   - [ ] If it fails → minimal role insufficient → need more permissions
   - [ ] If it works → admin was over-privileged

   ```bash
   # Example: Test minimal IAM permissions
   # Create role with S3:GetObject only
   aws iam create-role --role-name lambda-minimal
   aws iam attach-role-policy --role-name lambda-minimal \
     --policy-arn arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess
   
   # Test Lambda with this role
   aws lambda create-function --runtime python3.11 --role lambda-minimal ...
   # Try to read S3: SUCCESS
   # Try to delete S3 object: FAILS (as expected, permission denied)
   ```

3. **Check for legacy reasons:**
   - [ ] Is admin permission inherited from old app? (could be reduced now)
   - [ ] Or legitimately needed? (multi-service access, complex operations)

4. **Document result:**

   **If permissions are OVER-PRIVILEGED:**
   - Severity: CONFIRMED
   - Risk: Lateral movement if Lambda compromised
   - Decision: REVISAR-PLAN (reduce to minimum needed)
   - Fix: Replace admin with specific permissions (S3:GetObject, DynamoDB:Query, etc.)

   **If admin IS NECESSARY (rare):**
   - Reason: Lambda needs complex, multi-service access
   - Evidence: Architecture review confirms need
   - Decision: Document exception with compensating controls
   - Mitigations: MFA before assume role, audit all actions, network isolation
   - Exception: `iam-exceptions/EXC-2026-01-20-Lambda-Admin.md`

:::

**Common FP Scenarios:**
- Role is for Lambda that needs to orchestrate multiple services (legitimately needs broad permissions)
- Role is for admin/operational tool (intended to have broad permissions)
- Copy of existing admin role, but in prod context might not need all permissions

**Common FN Scenarios:**
- Policy is permissive but narrowed by resource-based restrictions (tool doesn't see full picture)
- Permissions granted via multiple small policies, not obvious when combined

---

### 5️⃣ Resource Limits & Capacity Planning

**Example Violation:**
```
Tool: Custom policy
Finding: DynamoDB table created without capacity reservation
Severity: MEDIUM
Resource: aws_dynamodb_table.metrics
Status: ⛔ BLOCKED
Message: "L2+ resources must have provisioned capacity or auto-scaling configured"
```

**Empirical Validation Checklist:**

:::userstory
**História.**  
Como **DevOps Engineer**, quero **validar empiricamente se resource limits are adequate**, para confirmar se plan design is correct.

**Procedimento T5: Validação de Resource Limits**

1. **Assess workload requirements:**
   - [ ] What's the expected throughput? (requests/sec, data volume)
   - [ ] Peak vs. average? (spiky vs. continuous)
   - [ ] SLA for performance? (99.9% latency? 99.99%?)

2. **Test with actual load:**
   - [ ] Deploy resource with limits in test environment
   - [ ] Generate realistic load (load test)
   - [ ] Monitor: Does it meet SLA? Throttling? Timeouts?
   - [ ] If SLA missed → limits insufficient → need increase
   - [ ] If SLA met → limits adequate

   ```bash
   # Example: Test DynamoDB capacity
   # Deploy table with low capacity
   aws dynamodb create-table --table-name test-metrics \
     --attribute-definitions AttributeName=id,AttributeType=S \
     --key-schema AttributeName=id,KeyType=HASH \
     --billing-mode PROVISIONED \
     --provisioned-throughput ReadCapacityUnits=10,WriteCapacityUnits=10
   
   # Load test: insert 1000 records/sec
   # Monitor: CloudWatch metrics for throttling
   # If throttled: capacity insufficient
   # If no throttling: capacity adequate
   ```

3. **Consider cost trade-offs:**
   - [ ] High capacity = higher cost but better performance
   - [ ] Low capacity = lower cost but risk of throttling
   - [ ] What's acceptable trade-off for this app?

4. **Document result:**

   **If limits are INADEQUATE:**
   - Severity: CONFIRMED (will cause SLA breach)
   - Impact: Performance degradation, errors under load
   - Decision: REVISAR-PLAN (increase capacity)
   - Fix: Increase provisioned throughput OR enable auto-scaling

   **If limits are ADEQUATE:**
   - Reason: Load test confirms capacity is sufficient
   - Evidence: Metrics show no throttling even at peak
   - Decision: ACEITAR-PLAN (limits are correct)

:::

**Common FP Scenarios:**
- Resource is for development/test (doesn't need production-grade capacity)
- Workload is predictable and low volume (minimal capacity needed)
- Application handles backpressure gracefully (throttling is acceptable)

**Common FN Scenarios:**
- Capacity planned for current load, not accounting for future growth
- Auto-scaling not configured, so no elasticity (sudden spike causes failure)

---

## 📊 FP/FN Management

### Gestão de Falsos Positivos (FP)

**Workflow:**

```
1. Plan Checker Reporta Violation
   ↓
2. DevOps/AppSec: Empirical Validation (T1-T5)
   - [ ] Is violation real? (exploit PoC, reachability test)
   - [ ] Run appropriate test for category
   - [ ] Document evidence
   ↓
3. Result: FP or TP (True Positive)?
   
   IF TP → Remediation required (see addon-11 Decision Framework)
   
   IF FP → Create Suppression Document & VEX
```

**FP Suppression Template (Template S1):**

```markdown
# Falso Positivo Report - IaC Violation

**Violation ID:** CHECKOV-CKV-S3-001-2026-01-20
**Tool:** Checkov (Infrastructure Code Scanner)
**Category:** Security Configuration (T1)
**Date:** 2026-01-20
**Reviewer:** DevOps Engineer + AppSec Engineer

## Violation Details
- Resource: aws_s3_bucket.data_lake
- Violation: "S3 bucket versioning not enabled"
- Severity: MEDIUM (reported)
- Policy: "All S3 buckets must have versioning enabled"

## Empirical Validation (T1 Procedure)

**Step 1: Understand intent**
- Policy intent: Protect against accidental deletion
- Applicability: YES (data lake contains important data)
- Compensating controls: Weekly snapshots to backup S3 bucket (immutable)

**Step 2: Test impact**
- Deployed bucket without versioning in test environment
- Simulated deletion: `aws s3 rm s3://test-datalake/file.txt`
- Recovery attempt: Could NOT recover from versioning (as expected, versioning disabled)
- Backup recovery: Could recover from weekly snapshot (backup works, latency 7 days)

**Step 3: Assess business context**
- Data lake is append-only (new data added daily, never updated)
- Retention: Data kept for 90 days, then deleted per policy
- Recovery need: If file accidentally deleted, can restore from 7-day-old snapshot
- Cost impact: Versioning adds ~20% to storage costs ($500/month extra)

## Why It's a False Positive

**Technical Justification:**
- Versioning not needed because data is append-only and immutable
- Weekly backups provide recovery path (latency acceptable for data lake)
- Cost of versioning ($500/month) exceeds benefit for this use case
- Data is non-critical (can be re-generated from source if needed)

**Verification:**
- Tested: Bucket functions correctly without versioning
- Backup procedure: Verified weekly snapshots capture all data
- Recovery test: Confirmed snapshot can restore all data
- Cost analysis: Versioning would cost $6000/year unnecessarily

## Suppression

**Checkov suppression annotation:**
```hcl
# checkov:skip=CKV_AWS_21:Versioning not needed for append-only data lake; weekly backups provide recovery
resource "aws_s3_bucket" "data_lake" {
  bucket = "company-data-lake"
  # versioning intentionally disabled to reduce costs
  # weekly backups in separate account ensure recovery capability
}
```

**VEX File:** `vex/FP-2026-01-20-S3-versioning-datalake.vex.json`
```json
{
  "component": {
    "name": "data_lake_infrastructure",
    "version": "1.0.0"
  },
  "vulnerabilities": [{
    "ref": "CKV_AWS_21",
    "state": "not_affected",
    "justification": "component_not_vulnerable",
    "impact": "Versioning not needed for append-only data lake; weekly snapshots provide recovery"
  }]
}
```

## Approval

- **Reviewed by:** João DevOps + Maria AppSec
- **Approved:** 2026-01-20 14:30 UTC
- **Signed:** joao.devops@company.com, maria.appsec@company.com
- **Next review:** 2026-07-20 (6-month cycle)
- **Review criteria:** If data lake becomes mutable or retention changes, re-evaluate suppression

## Lessons Learned

**For scanning configuration:**
- Checkov should have context about data lake patterns (append-only, immutable)
- Could add custom policy: "Versioning required except for append-only buckets with backup"
- Consider cost of violations (not all high-severity = must-fix)
```

### Gestão de Falsos Negativos (FN)

**Workflow:**

```
1. Security Issue Discovered (Pentest, incident, etc.)
   ↓
2. Check: Did plan checker find this?
   
   IF YES (TP detected) → Great, checker working!
   
   IF NO → False Negative found
   ↓
3. Root Cause Analysis (RCA)
   - Why did checker miss this?
   - Tool limitation? Configuration issue?
   ↓
4. Improve Detection
   - Custom rule creation
   - Tool configuration update
   - Add manual testing
```

**FN Root Cause Analysis Template (Template S2):**

```markdown
# Falso Negativo Report - IaC Violation

**Finding ID:** FN-2026-01-21-001
**Vulnerability Type:** IAM Over-Privilege
**Discovery Method:** Security Pentest (2026-01-21)
**Date:** 2026-01-21

## Vulnerability Details

**Discovered:** Lambda execution role has `iam:*` permission (admin)
**Severity:** CRITICAL (privilege escalation risk)
**How discovered:** Pentester assumed Lambda role and created new admin account

**Why checker missed it:**
- Checkov has rule CKV_IAM_62 "Ensure IAM policies contain no statements that allow all actions"
- Rule exists but was NOT ENABLED in pipeline configuration
- Plan checker was running with default config (not security-focused config)

## Root Cause Analysis

### Why Detection Failed

1. **Gap 1: Checker not configured for security profile**
   - Policy: Use `checkov:skip=CKV_IAM_62` to suppress policy warnings
   - But: Pipeline runs Checkov with default config (permissive)
   - Result: Rule not applied to plan

2. **Gap 2: No enforcement of IAM best practices**
   - Configuration allows `iam:*` because no policy restricts it
   - No automated code review to catch admin permissions

3. **Configuration Issue:** Pipeline Checkov config
   - Before: `checkov --framework terraform`
   - Missing: `--check CKV_IAM_62` (explicit enable security checks)

### Why It Matters

- Pentester used Lambda role to create admin IAM account
- Then used admin account to delete logs, modify security groups
- Application compromised, data exfiltrated

## Mitigation

### Immediate (Fix the vulnerability)
- [ ] Remove `iam:*` from Lambda role
- [ ] Replace with minimum needed: `s3:GetObject`, `dynamodb:Query`
- [ ] Audit other Lambda roles for same issue
- [ ] Revoke admin account created by pentester

### Improve Detection
- [ ] Update pipeline: Enable security-focused Checkov config
  - Before: `checkov --framework terraform`
  - After: `checkov --framework terraform --check CKV_IAM_62,CKV_IAM_63,CKV_IAM_64`
- [ ] Add custom OPA rule: Reject any role with `Action: "*"` or `iam:*`
- [ ] Add manual code review: Any IAM policy change requires AppSec review

### Add Regression Test
- [ ] Create test: Terraform with `iam:*` policy should fail Checkov
- [ ] Test OPA rule: Custom policy blocks admin permissions
- [ ] Test in CI: Push sample bad policy, verify it's blocked

### Update Configuration
- [ ] Update Checkov config in `.checkov.yml`:
  ```yaml
  framework:
    - terraform
  checks:
    - CKV_IAM_62  # Ensure IAM policies don't allow all actions
    - CKV_IAM_63  # Ensure IAM policy doesn't allow * on resources
    - CKV_IAM_64  # Ensure IAM policy doesn't allow full access to Lambda
  ```

## Approval & Tracking

- **RCA Completed by:** AppSec team
- **Date:** 2026-01-21
- **Action Items:**
  - [ ] Fix Lambda role permissions — Due: 2026-01-22
  - [ ] Update Checkov config — Due: 2026-01-22
  - [ ] Deploy OPA rule — Due: 2026-01-23
  - [ ] Team training on IAM best practices — Due: 2026-01-30
  - [ ] Audit all Lambda roles — Due: 2026-02-04

## Lessons Learned

1. **Checker configuration is critical** (default config is permissive, not secure)
2. **IAM permissions need manual review** (automation not sufficient for complex policies)
3. **Regression tests are essential** (once found, prevent reoccurrence)
4. **Multiple defense layers needed** (Checkov + OPA + manual review)
```

---

## 🎯 Quality Metrics & Thresholds

**Metric 1: False Positive Rate**
- **Target:** <20% (if >30%, checker creates too much noise)
- **Definition:** (FPs / Total violations reported) × 100
- **Action:** If >30%, adjust checker config or replace with alternative

**Metric 2: False Negative Rate**
- **Target:** <5% (if >10%, checker inadequate)
- **Definition:** (FNs discovered / Total real violations) × 100
- **Action:** If >10%, add custom rules + enhance scanning

**Metric 3: Time-to-Validation**
- **Target:** <2h for CRITICAL, <4h for HIGH (L2/L3)
- **Definition:** Hours from plan violation reported to validation complete
- **Action:** If > SLA, investigate bottlenecks (tool slowness, manual testing delays)

**Metric 4: Proporcionalidade by Risk Level**

| Level | FP Rate Target | FN Rate Target | Time-to-Validation | Empirical Test Required |
|---|---|---|---|---|
| L1 | <25% | <10% | <4 hours | Optional (CRITICAL only) |
| L2 | <20% | <5% | <2 hours | CRITICAL+HIGH (empirical test mandatory) |
| L3 | <15% | <3% | <1 hour | ALL violations (multi-method validation) |

---

## 🔗 Integração com Invariantes de agent.md

**I2 — Evidência acima de plausibilidade:**  
✅ Framework implementado (Taxonomia T1-T5, empirical tests, FP/FN management, quality metrics)

**I1 — Separação sugestão/decisão:**  
↔️ Cross-reference: Ver [addon-11](./11-plan-review-decision.md) para decision framework (Checklist C1, Decision Template T1)

**I3 — Reprodutibilidade:**  
✅ Tests versionadas (T1-T5 documented, reproducible commands)

**I4 — Proteção de ativos:**  
✅ IAM validation (T4) protects critical assets

**I5 — Rastreabilidade:**  
✅ FP/FN documents with approval trail (VEX, RCA, signed by AppSec)

---

## 📎 Referências Cruzadas

| Documento | Relação |
|---|---|
| [addon-11: Plan Review Decision](./11-plan-review-decision.md) | I1 decision framework (works with I2 empirical testing) |
| [Cap 07 — addon-12: Validação Empírica Gates](../../07-cicd-seguro/addon/12-validacao-empirica-gates.md) | Similar I2 framework for pipeline findings |
| [aplicacao-lifecycle.md](./aplicacao-lifecycle.md) | US-20 operationalizes este addon |
| [agent.md](https://github.com/your-org/agent-spec) | Invariantes I1-I5 normativas |

---

## ✅ Checklist de Implementação

- [ ] **Taxonomia & Procedures:**
  - [ ] Treinar DevOps em T1-T5 (5 test procedures)
  - [ ] Documentar PoC por categoria
  - [ ] Setup test environment para validação (staging IaC)

- [ ] **FP/FN Management:**
  - [ ] Criar processo FP: Violation → Analysis → Suppression → VEX
  - [ ] Criar processo FN: Discovery → RCA → Custom rule → Regression test
  - [ ] Arquivo de FPs: `falsos-positivos/FP-YYYY-MM-DD-*.md`
  - [ ] Arquivo de FNs: `falsos-negativos/FN-YYYY-MM-DD-*.md`

- [ ] **Quality Metrics:**
  - [ ] Setup dashboard: FP rate, FN rate, time-to-validation
  - [ ] Define thresholds (checker replacement if FP >30%)
  - [ ] Monthly review de métricas

- [ ] **Integration:**
  - [ ] Link addon-11 (Decision) com addon-12 (Evidence)
  - [ ] Plan policy: L2/L3 violations require both C1 checklist + empirical test
  - [ ] Training: "How to validate an IaC violation" (T1-T5 procedures)

---

> 📌 **Princípio central:** Evidence-driven decisions.  
> Plan suggests, Empirical testing confirms.  
> FP/FN management ensures checker quality.
