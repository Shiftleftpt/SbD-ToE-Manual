---
id: decisao-gates-pipeline
title: Decisão Assistida em Gates de Pipeline
description: Framework de decisão para gate failures em CI/CD com separação explícita sugestão/decisão
tags: [pipeline, gates, decisão, i1, invariantes, policy]
---

# ✅ Decisão Assistida em Gates de Pipeline

## 🌟 Objetivo

Implementar o Invariante **I1 (Separação sugestão/decisão)** de [agent.md](https://github.com/your-org/agent-spec) no contexto de gates de segurança em pipelines CI/CD.

Pipelines aplicam **políticas automáticas** (SAST findings, container vulnerabilities, policy violations), bloqueando builds que não cumprem thresholds. Porém, a decisão de aceitar, remediar ou contornar essas políticas deve ser **explícita, documentada e rastreável**, com papéis bem definidos e escalação clara para conflitos.

---

## 📋 Contexto normativo

**Problema:**
Quando gate bloqueia uma build (ex: "SAST encontrou 3 HIGH findings"), o time enfrenta dilema:
- **Aceitar bloqueio** → Release atrasada, pressão para "fix rápido"
- **Contornar gate sem justificativa** → Vulnerabilidades em produção, auditoria impossível
- **Adaptar política** → Sem rastreabilidade de "por quem" e "por quê"

**Solução:**
Framework 4-fase que torna a decisão **explícita, documentada e auditável**:
1. Gate bloqueia (policy violation reportado)
2. Developer/AppSec analisa com checklist I1
3. Documented decision (ACEITAR-bloqueio / REMEDIAR / CONTORNAR-com-justificativa)
4. Escalation procedures para conflitos críticos

---

## 🛠️ Framework 4-Fase

### Fase 1: Gate Bloqueia (Policy Violation Reportado)

**Entrada:** Pipeline gate reporta violation:
- Gate name (ex: SAST findings threshold, container scan, policy violation)
- Severity (LOW, MEDIUM, HIGH, CRITICAL)
- Details (3 HIGH findings, CVE-2024-XXXXX in base image, etc.)
- Current policy threshold (ex: CRITICAL=0, HIGH ≤5, MEDIUM ≤20)
- Suggested action (remediate finding, update base image, override policy)

**Exemplo:**
```
Gate: SAST Threshold
Severity: HIGH
Status: ⛔ BLOCKED
Details: 3 HIGH findings (SQLi, XSS, Hardcoded Secret)
Threshold: CRITICAL=0, HIGH=0 (zero-tolerance policy)
Suggested: Fix before merge OR review & suppress findings
Current Action: Build failed, PR blocked
```

### Fase 2: Developer/AppSec Valida com Checklist I1

**Responsável:** Developer (initial analysis) ou AppSec Engineer (L2/L3 critical gates)

**Checklist I1 — 4 Questões de Validação:**

:::userstory
**História.**  
Como **Developer ou AppSec Engineer**, quero **validar se um gate block é justified**, para tomar decisão informada entre ACEITAR-bloqueio, REMEDIAR, ou CONTORNAR-com-justificativa.

**Checklist C1: Validação de Gate Block**

- [ ] **C1.1 — Policy Justified?**
  - [ ] Is current threshold appropriate for app classification (L1/L2/L3)?
  - [ ] Does threshold balance security vs. false positives?
  - [ ] Are there organizational policies that support this threshold?
  - **Evidence needed:** Policy document, threat model, historical FP data
  - **Example JUSTIFIED:** L3 app with zero-tolerance for CRITICAL findings (policy matches risk)
  - **Example UNJUSTIFIED:** L1 app with MEDIUM findings block (too strict, kills release velocity)

- [ ] **C1.2 — Findings Real or False Positives?**
  - [ ] Are reported findings real vulnerabilities? (Not FP from tool misconfiguration?)
  - [ ] Can findings be exploited in this context?
  - [ ] Are findings in reachable code paths?
  - **Evidence needed:** Code review, threat model analysis, manual testing (empirical validation from addon-12)
  - **Example REAL:** SAST reports hardcoded AWS key in source code (confirmed real secret, exploitable)
  - **Example FP:** SAST reports SQLi but query uses PreparedStatement (FP, already safe)

- [ ] **C1.3 — Remediation Feasible?**
  - [ ] Can findings be fixed quickly (hours/days)?
  - [ ] Does fix require architecture changes (weeks/months)?
  - [ ] Are there acceptable mitigating controls if fix is deferred?
  - **Evidence needed:** Effort estimation, mitigation analysis, timeline
  - **Example FEASIBLE:** Hardcoded secret → Move to secrets manager (1-2 hours)
  - **Example DEFERRED:** Architectural redesign for multitenant isolation → 6 weeks, needs risk acceptance

- [ ] **C1.4 — Risk Acceptance Documented?**
  - [ ] If not fixing now, are residual risks documented?
  - [ ] Is compensation control in place (WAF rule, monitoring, incident response plan)?
  - [ ] Who approves risk acceptance (Developer alone vs. AppSec vs. CISO)?
  - **Evidence needed:** Risk acceptance form, compensating controls, approval chain
  - **Example GOOD:** High finding with WAF rule blocking attack pattern + monitoring
  - **Example BAD:** "We'll fix this later" without risk acceptance document or controls

**Approval Criteria:**  
All 4 checklist items must have evidence for Developer to proceed to Phase 3 (Documented Decision).
If any item has low confidence or high risk, escalate to AppSec Engineer (see Phase 4: Escalation).
:::

**Output from Phase 2:**
- Completed Checklist C1 (all 4 questions answered with evidence)
- Decision draft (ACEITAR / REMEDIAR / CONTORNAR)
- Escalation flag (if conflict or high severity)

### Fase 3: Documented Decision com Decisores Explícitos

**Entrada:** Checklist C1 completado + decision draft

**Decisores por Gate Severity (Matriz Decisores):**

| Severity | Developer Analysis | AppSec Review | Release Manager Approval | SLA |
|---|---|---|---|---|
| **LOW** | Optional | — | — (auto-pass) | Immediate |
| **MEDIUM** | Mandatory | Reviewer judgment call | — | 1 day |
| **HIGH** | Mandatory | Mandatory | Reviewer | 8 hours |
| **CRITICAL** | Mandatory | Mandatory + AppSec Lead | Release Manager | 4 hours |

**Decision Template (Template T1):**

```markdown
# CI/CD Gate Decision Log

**Gate ID:** SAST-2026-01-16-001 (internal tracking)
**Gate Name:** SAST Findings Threshold
**Date:** 2026-01-16 14:30 UTC
**Triggered by:** Automated CI/CD pipeline

## Gate Details

- **Pipeline:** build/main/PR-789
- **Application:** PaymentService (L3 classification)
- **Severity:** HIGH
- **Status:** ⛔ BLOCKED
- **Findings:**
  - 1 CRITICAL (Hardcoded AWS secret in config.py:42)
  - 2 HIGH (SQLi in UserController, XSS in search)
- **Current Policy:** CRITICAL=0, HIGH=0 (zero-tolerance)
- **Threshold Status:** Exceeded (CRITICAL: 1 > 0, HIGH: 2 > 0)

## Checklist C1 Results

✅ **C1.1 — Policy Justified?**
- Current threshold (zero-tolerance HIGH): YES, justified for L3 payment service
- Risk profile: CRITICAL financial data, PCI-DSS compliance
- Historical FP rate: 5% (acceptable)
- **Conclusion:** Policy is JUSTIFIED and appropriate

✅ **C1.2 — Findings Real?**
- CRITICAL (Hardcoded secret): CONFIRMED REAL
  - Evidence: Manual code review, secret pattern matches AWS key format
  - Exploitability: Confirmed (test: AWS SDK authentication succeeded)
  - Risk: Full access to production S3 buckets, RDS databases
- HIGH (SQLi in UserController): CONFIRMED REAL
  - Evidence: Code uses string concatenation in SQL query
  - Exploitability: Test with sqlmap confirms injection possible
  - Risk: Unauthorized database access, data exfiltration
- HIGH (XSS in search): FALSE POSITIVE (FP)
  - Evidence: Output is HTML-encoded by template engine
  - Template: Jinja2 with auto-escape enabled
  - Test: Payload `<script>alert(1)</script>` rendered as `&lt;script&gt;...&lt;/script&gt;`
  - **Conclusion:** 1 CRITICAL + 1 HIGH real findings, 1 HIGH is FP

✅ **C1.3 — Remediation Feasible?**
- CRITICAL (Hardcoded secret):
  - Feasibility: Immediate (move to AWS Secrets Manager)
  - Timeline: 2-4 hours (secret rotation + code update + tests)
  - Effort: Low (1 developer, 1 DevOps engineer)
- HIGH (SQLi in UserController):
  - Feasibility: Immediate (convert to PreparedStatement)
  - Timeline: 4-8 hours (code change + tests + review)
  - Effort: Low (1 developer, 1 reviewer)
- HIGH (XSS - FP):
  - Feasibility: Suppress with justification
  - Timeline: <30 minutes (add suppression comment, create VEX)
- **Conclusion:** All findings REMEDIATION FEASIBLE immediately

✅ **C1.4 — Risk Acceptance?**
- For CRITICAL: No risk acceptance (must remediate NOW)
- For HIGH: No risk acceptance (must remediate NOW)
- For FP: Suppress with VEX document
- **Compensating controls:** None needed (findings will be fixed)
- **Conclusion:** No residual risk acceptance required

## Decision

**Decision Type:** REMEDIAR (Fix before merge, gate remains active)

**Decision Reasoning:**
- All findings are real (2 confirmed, 1 FP)
- All findings are remediable immediately (2-8 hours)
- Policy (zero-tolerance HIGH/CRITICAL) is appropriate for L3 app
- Risk acceptance not acceptable (no compensating controls justify deferring)
- **Therefore:** Remediate all findings, then re-run gate

**Decisores:**
- **Phase 2 (Analysis):** João Silva, Developer (2026-01-16 14:30 UTC)
  - Checklist C1: ✅ Complete, all 4 items validated
  - Decision draft: REMEDIAR
  - Escalation: None (straightforward remediation path)
  
- **Phase 3 (Validation):** Maria Santos, AppSec Engineer (2026-01-16 15:00 UTC)
  - Reviewed checklist C1: Agreed
  - Severity assessment: Confirmed CRITICAL + HIGH real findings
  - Remediation assessment: Feasible and appropriate
  - Risk: No residual risk (all findings fixable)
  - Validation: APPROVED to remediate
  
- **Phase 4 (Release Approval):** Pedro Costa, Release Manager (2026-01-17 10:00 UTC)
  - Gate re-run after fixes: ✅ PASSED (all findings resolved)
  - Merge approval: ✅ Granted
  - Release readiness: APPROVED

## Implementation

**Action Items:**
1. **CRITICAL - Hardcoded Secret:**
   - [ ] Create AWS Secrets Manager secret
   - [ ] Update code: `config.py` to use `boto3.client('secretsmanager')`
   - [ ] Rotate AWS key in production immediately
   - [ ] Verify: Secrets scan passes on re-run
   - Owner: João Silva + DevOps team
   - Timeline: 2-4 hours

2. **HIGH - SQLi:**
   - [ ] Convert string concatenation to PreparedStatement
   - [ ] Test: sqlmap confirms no injection possible after fix
   - [ ] Code review: Verify fix is correct and complete
   - [ ] Verify: SAST scan passes on re-run
   - Owner: João Silva + Reviewer
   - Timeline: 4-8 hours

3. **HIGH - XSS (FP):**
   - [ ] Add suppression annotation: `# nosemgrep: xss-output-encoding`
   - [ ] Create VEX document: `vex/FP-2026-01-16-XSS-Search.vex.json`
   - [ ] Verify: SAST scan suppresses this finding on re-run
   - Owner: João Silva
   - Timeline: <30 minutes

4. **Gate Re-run:**
   - [ ] Commit all fixes with message: "Fix: CRITICAL hardcoded secret, HIGH SQLi, suppress FP XSS per SAST-2026-01-16-001"
   - [ ] Push and trigger pipeline
   - [ ] Confirm gate passes (zero violations)
   - Owner: João Silva
   - Timeline: After fixes complete

## Traceability

- **PR:** #789 (`fix/critical-findings-SAST-2026-01-16`)
- **Commits:** 
  - abc123 - Fix: Move AWS secret to Secrets Manager
  - def456 - Fix: Use PreparedStatement in UserController.getUserById()
  - ghi789 - Suppress: XSS FP in search component with VEX
- **Gate Logs:** CI/CD pipeline run #1234 (initial block), run #1235 (re-run after fixes, PASS)
- **Evidence:** SAST reports (before/after), empirical test logs (SQLi + hardcoded secret confirmation), VEX document
- **Approval Chain:** João (Developer) → Maria (AppSec) → Pedro (Release Manager)

## Follow-up & Prevention

- [ ] Security training: Team training on "Hardcoded secrets prevention" (next sprint)
- [ ] Custom rule: Add Semgrep custom rule to detect AWS secret patterns earlier in dev
- [ ] Process improvement: Add pre-commit hook to detect secrets before push
- [ ] Metrics: Log this incident for "findings by category" trend analysis
```

**Key Decision Types:**

| Decision | Meaning | When Used | Impact |
|---|---|---|---|
| **ACEITAR-bloqueio** | Accept that gate blocks release | Finding is unacceptable risk, release cannot proceed | Release delayed until remediation complete |
| **REMEDIAR** | Fix findings before merge | Findings real but fixable quickly | Development resumes after remediation |
| **CONTORNAR-com-justificativa** | Override gate with documented reason | Risk is acceptable with compensating controls OR finding is known FP | Release proceeds, but with audit trail |

---

## 🔁 Escalation Procedures

**Escalation Triggers:**

1. **Conflict Type A: Remediation Timeline vs. Release Deadline**
   - **Scenario:** Gate blocks CRITICAL finding, but fix takes 2 weeks and release deadline is 2 days
   - **Escalation:** Developer + AppSec Engineer + Release Manager + Product Owner
   - **Resolution:** CONTORNAR-com-justificativa (risk acceptance with compensating controls) OR defer release
   - **Example:** Payment processing down → CRITICAL bug fix needed urgently, security finding deferred with risk acceptance
   - **SLA:** 4 hours (decision must be made for continuity)

2. **Conflict Type B: Policy Appropriateness Disputed**
   - **Scenario:** Developer claims gate is too strict ("no HIGH findings for L2 app is excessive"), AppSec disagrees
   - **Escalation:** Developer + AppSec Engineer + Team Lead
   - **Resolution:** Joint policy review → Adjust threshold OR clarify justification for current threshold
   - **Example:** L2 app with strict policy designed for mature team → Review if policy should be relaxed for early-stage apps
   - **SLA:** 2 days (policy adjustment, if needed)

3. **Conflict Type C: False Positive Disputed**
   - **Scenario:** Developer claims finding is FP ("output is already encoded"), AppSec wants empirical proof
   - **Escalation:** Developer + AppSec Engineer + Security Architect
   - **Resolution:** Manual testing + code review to confirm FP status (see addon-12)
   - **Example:** SAST reports XSS, but application uses framework with auto-escaping
   - **SLA:** 1 day (empirical validation must complete)

**Escalation Workflow (Template T2):**

```markdown
# CI/CD Gate Escalation

**Gate ID:** SAST-2026-01-17-002
**Escalation Type:** Type A (Timeline vs. Deadline)
**Initiated:** 2026-01-17 by João Silva (Developer)
**Date:** 2026-01-17 09:00 UTC

## Conflict

**Situation:** Payment processing L3 app has CRITICAL hardcoded secret finding. Timeline to fix: 4-6 hours. Release deadline: 2 hours (production incident response).

**Developer Claim:** "We need to override gate for emergency hotfix. Secret will be rotated post-release."

**AppSec Concern:** "CRITICAL secrets in code should never reach production. Needs proper remediation before release, not after."

**Product Owner Pressure:** "Payment system down = revenue impact. Need release NOW."

## Investigation

**Developer (João):** "The secret was accidentally committed. We know which resources it accesses (S3 bucket for transaction logs). We'll rotate immediately post-release."

**AppSec (Maria):** "The risk here is: (1) Secret exposed in prod code/history, (2) Attacker could use secret to access S3 before rotation, (3) No audit of what attacker accessed. We need to remediate properly."

**Release Manager (Pedro):** "Emergency releases have happened before. We have process for this - escalate to CTO, document risk, get sign-off."

**CTO (Carlos):** "Security is right. We can't compromise on secrets in prod. However, business-critical incident acknowledged. Decision: We hotfix the code+secret locally, rotate ASAP, then release. Full RCA post-incident."

## Resolution

**Decision:** REMEDIAR (Fix before merge, accept tight timeline with CTO approval)

1. **Immediate (Next 2 hours):**
   - [ ] Implement Secrets Manager fix locally
   - [ ] Rotate AWS secret in production NOW
   - [ ] Test locally that code works with new secret
   - [ ] Skip SAST gate (CTO approved emergency override)
   - [ ] Deploy with audit trail: PR, commits, CTO approval document

2. **Post-Release (Next 24 hours):**
   - [ ] RCA meeting: Why secret was committed? How to prevent?
   - [ ] Code review of fix
   - [ ] Confirm SAST gate passes on next release
   - [ ] Update secrets management policy/tooling

3. **Long-term (Next sprint):**
   - [ ] Pre-commit hook to prevent secret commits
   - [ ] Secret scanning in all repos
   - [ ] Training on secret management

**Approved by:** Carlos Martinez (CTO), Maria Santos (AppSec Lead), Pedro Costa (Release Manager)
**Signed:** 2026-01-17 09:30 UTC
**Emergency Override:** Documented in incident ticket INC-2026-001
```

---

## 📊 Matriz Decisores (por Gate Severity e Nível de Classificação)

**Objetivo:** Determinar quem decide em cada cenário, responsabilidade clara

### L1 (Baixo Risco)

| Gate Severity | Analyzer | Validator | Approver | Required Checklist | SLA |
|---|---|---|---|---|---|
| LOW | Developer (optional) | — | — | C1.1 (policy justified?) | Immediate |
| MEDIUM | Developer | Reviewer | — | Full C1 | 1 day |

### L2 (Risco Médio)

| Gate Severity | Analyzer | Validator | Approver | Required Checklist | SLA |
|---|---|---|---|---|---|
| LOW | Developer | — | — | C1.1, C1.2 | 1 day |
| MEDIUM | Developer | Reviewer | — | Full C1 | 8 hours |
| HIGH | Developer | AppSec Engineer | Release Manager | Full C1 + empirical test (addon-12) | 8 hours |

### L3 (Risco Crítico)

| Gate Severity | Analyzer | Validator | Approver | Required Checklist | SLA |
|---|---|---|---|---|---|
| MEDIUM | Developer | AppSec Engineer | Release Manager | Full C1 + empirical test | 4 hours |
| HIGH | Developer | AppSec Engineer + Code Reviewer | Release Manager | Full C1 + empirical test | 4 hours |
| CRITICAL | Developer | AppSec Engineer + AppSec Lead | CTO/CISO | Full C1 + empirical test + risk assessment | 2 hours |

---

## 🎯 KPIs — Monitorização de Conformidade

**Métrica 1: Gate Decision Documentation**
- **Definição:** % de gate blocks (severidade ≥ MEDIUM) com Checklist C1 documentado
- **Target:** 100% para L2/L3; ≥80% para L1
- **Cálculo:** (Gates com C1 / Total gates ≥ MEDIUM) × 100
- **Responsável:** AppSec Engineer
- **Cadência:** Semanal

**Métrica 2: Decision Time-to-Resolution**
- **Definição:** Horas desde gate bloqueia até decisão aprovada
- **Target:** <8h para HIGH, <4h para CRITICAL (L2/L3)
- **Cálculo:** Data/hora aprovação - Data/hora gate block
- **Responsável:** Release Manager
- **Cadência:** Semanal, P95 percentile

**Métrica 3: False Positive Rate in Gates**
- **Definição:** % de gate blocks que eram FP (finding not real)
- **Target:** <15% (if >25%, gate configuration has too many FPs)
- **Cálculo:** (FP gates approved / Total gates blocked) × 100
- **Responsável:** AppSec Engineer
- **Cadência:** Mensal

**Métrica 4: Override Rate (Contornar-com-justificativa)**
- **Definição:** % de gate blocks overridden vs. total blocks
- **Target:** <5% (if >10%, gate policy may be too strict OR risk acceptance too common)
- **Cálculo:** (Overrides / Total blocks) × 100
- **Responsável:** Release Manager
- **Cadência:** Mensal

**Métrica 5: Release Impact**
- **Definição:** % of releases delayed by gate blocks vs. total releases
- **Target:** <10% (if >20%, gates may be blocking legitimate releases)
- **Cálculo:** (Releases delayed by gates / Total releases) × 100
- **Responsável:** Release Manager
- **Cadência:** Mensal

---

## 🔗 Integração com Invariantes de agent.md

**I1 — Separação sugestão/decisão:**  
✅ Framework implementado (Gate sugere → Developer valida → AppSec aprova → Release Manager merges)

**I2 — Evidência empírica:**  
↔️ Cross-reference: Ver [addon-12](./12-validacao-empirica-gates.md) para validação empírica de findings bloqueados (CRITICAL/HIGH em L3 requerem teste manual)

**I3 — Reprodutibilidade:**  
✅ Decisões versionadas em Git (Decision Template T1 pode ser armazenado em `decisions/gates/YYYY-MM-DD-XXX.md`)

**I4 — Proteção de ativos:**  
✅ Pipeline classificação determina gate policy (L3 pipeline = mais rigoroso)

**I5 — Rastreabilidade:**  
✅ Audit trail completo (Gate block → Checklist C1 → Decision T1 → Implementation → Gate re-run → Approval)

---

## 📎 Referências Cruzadas

| Documento | Relação |
|---|---|
| [addon-12: Validação Empírica de Gates](./12-validacao-empirica-gates.md) | I2 empirical testing de findings bloqueados |
| [Cap 06 — addon-11: Validação SAST Assistida](../../06-desenvolvimento-seguro/addon/11-validacao-sast-assistida.md) | Similar I1 framework para code-level findings |
| [aplicacao-lifecycle.md](./aplicacao-lifecycle.md) | US-17 operationalizes este addon |
| [agent.md](https://github.com/your-org/agent-spec) | Invariantes I1-I5 normativas |

---

## ✅ Checklist de Implementação

- [ ] **Onboarding:**
  - [ ] Treinar team em Checklist C1 (4 questões de validação)
  - [ ] Introduzir Decision Template T1 no fluxo de gate blocks
  - [ ] Registar Escalation Workflow T2 em runbook

- [ ] **Tooling:**
  - [ ] Integrar gate block reports com issue tracking (ex: Jira, GitHub Issues)
  - [ ] Criar workflow automático: "gate blocked" → "notify developer" → "create decision issue"
  - [ ] Setup dashboard: gate blocks by severity, decision time, FP rate

- [ ] **Governance:**
  - [ ] Definir Decisores por Application Classification (L1/L2/L3) + Gate Severity
  - [ ] Estabelecer SLAs por level
  - [ ] Implementar KPIs (dashboard + monthly review)

- [ ] **Processo:**
  - [ ] Criar policy: "All MEDIUM+ gate blocks require Checklist C1 before override"
  - [ ] Criar runbook para Escalation (Type A, B, C)
  - [ ] Documentar quando CONTORNAR-com-justificativa é acceptable (rare, documented)

- [ ] **Validação:**
  - [ ] Teste com 3 gate blocks reais (LOW, MEDIUM, HIGH)
  - [ ] Verificar tempos de decisão (vs. SLA)
  - [ ] Validar audit trail (Decision templates rastreáveis)

---

> 📌 **Princípio central:** Gates sugerem, HUMANS decidem.  
> A automação é facilitadora, não substitui julgamento técnico sobre quando bloqueio é apropriado.
