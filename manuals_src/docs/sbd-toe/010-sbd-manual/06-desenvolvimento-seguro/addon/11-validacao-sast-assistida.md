---
id: validacao-sast-assistida
title: Validação Assistida de Findings SAST
description: Framework de decisão para findings de ferramentas SAST/Linters com separação explícita sugestão/decisão
tags: [sast, linters, decisão, validação, i1, invariantes]
---

# ✅ Validação Assistida de Findings SAST

## 🌟 Objetivo

Implementar o Invariante **I1 (Separação sugestão/decisão)** de [agent.md](https://github.com/your-org/agent-spec) no contexto de validação de findings de ferramentas SAST (Semgrep, SonarQube, Snyk Code, Bandit).

Ferramentas SAST sugerem correções automáticas, mas **a decisão de aceitar, adaptar ou rejeitar a sugestão deve ser explícita, documentada e rastreável**, com papéis bem definidos e escalação clara para conflitos.

---

## 📋 Contexto normativo

**Problema:**  
Quando SAST reporta "SQL Injection na linha 42" com sugestão de fix automático, o Developer enfrenta dilema:
- **Aceitar cegamente** → Fix pode estar incorrecto ou incompleto (ex: sanitização em lugar errado)
- **Rejeitar sem justificação** → Vulnerabilidade permanece não-mitigada, auditoria impossível
- **Adaptar sem rastreabilidade** → Difícil auditar se decisão foi técnica ou política

**Solução:**  
Framework 4-fase que torna a decisão **explícita, fundamentada e auditável**:
1. SAST sugere finding + fix
2. Developer valida com checklist I1
3. Documented decision com decisores explícitos
4. Escalation procedures para conflitos

---

## 🛠️ Framework 4-Fase

### Fase 1: SAST Sugere Finding + Fix

**Entrada:** Ferramenta SAST reporta:
- Vulnerability type (SQLi, XSS, CSRF, Hardcoded Secret, etc.)
- Location (ficheiro, linha, função)
- Severity (LOW, MEDIUM, HIGH, CRITICAL)
- Suggested fix (automático ou manual)
- CWE/CVE referência (se aplicável)

**Exemplo:**
```
Tool: Semgrep
Rule: java.lang.security.audit.sql-injection
Severity: HIGH
File: src/main/java/com/app/controller/UserController.java:42
Code: String query = "SELECT * FROM users WHERE id = " + userId;
Fix: Use PreparedStatement instead of string concatenation
CWE: CWE-89 (SQL Injection)
```

### Fase 2: Developer Valida com Checklist I1

**Responsável:** Developer (código owner ou quem conhece contexto)

**Checklist I1 — 5 Questões de Validação:**

:::userstory
**História.**  
Como **Developer**, quero **validar se um finding de SAST é real, relevante e corretamente fixado**, para tomar decisão informada entre ACEITAR, ADAPTAR ou REJEITAR.

**Checklist C1: Validação de Finding SAST**

- [ ] **C1.1 — Vulnerability Real?**
  - [ ] Code path is reachable? (Is function called? Is variable user-controlled?)
  - [ ] Attack vector exists? (Can attacker inject malicious input to this parameter?)
  - [ ] Context applicable? (Is this code exposed externally, or internal-only?)
  - **Evidence needed:** Code trace, execution flow diagram, or attestation
  - **Example VALID:** `userId` comes from HTTP request parameter, query executes with user input
  - **Example INVALID (FP):** `userId` is internal variable, already validated upstream, no injection possible

- [ ] **C1.2 — Severity Assessment Correct?**
  - [ ] CVSS score or internal severity matches finding? (Is HIGH justified? Or overestimated?)
  - [ ] Business impact matches CVSS? (Can attacker steal data? Modify transactions? DoS service?)
  - [ ] Exploitability realistic? (Requires admin access? Or unauthenticated?)
  - **Evidence needed:** CVSS calculation (if CVSS not provided), attack difficulty assessment, CVE comparison
  - **Example VALID:** SQLi with data access = HIGH (attacker reads user PII)
  - **Example INVALID (FP):** SQLi in comment field without data access = LOW (noise, attacker only sees own comments)

- [ ] **C1.3 — Suggested Fix Adequate?**
  - [ ] Fix resolves root cause? (Does PreparedStatement stop SQLi? Or only partially?)
  - [ ] Fix is correct technique? (Parameterization > escaping > input validation order)
  - [ ] Fix has no side effects? (Does it break functionality? Performance? Compatibility?)
  - [ ] Fix is complete? (All similar code paths fixed? Or only this one location?)
  - **Evidence needed:** Code review, security testing, regression testing
  - **Example VALID:** PreparedStatement with parameterized query (correct, complete)
  - **Example INVALID:** String escaping for SQLi (partial, incomplete defense-in-depth)

- [ ] **C1.4 — Context & Defense-in-Depth?**
  - [ ] Mitigating controls exist downstream? (Input validation, WAF, output encoding, authorization?)
  - [ ] Defense-in-depth justified? (Can we skip fix if WAF blocks SQLi?)
  - [ ] Risk acceptable if not fixed? (Is this low-risk domain or security-critical?)
  - **Evidence needed:** Architecture diagram, control inventory, threat model
  - **Example VALID:** Microservice with egress validation, WAF, and parameterized queries (defense-in-depth)
  - **Example INVALID:** Claim "WAF will block it" without WAF in architecture or WAF not active in prod

- [ ] **C1.5 — Requirement Mapping?**
  - [ ] Maps to existing requirement? (REQ-AUTH-001, REQ-DATA-001, etc.?)
  - [ ] Creates new requirement? (If yes, must be documented separately as REQ-NEWDOMAIN-001-v1.0)
  - [ ] Complies with policies? (Organizational standards, industry regulations?)
  - **Evidence needed:** REQ-XXX-v1.0 documentation, policy checklist
  - **Example VALID:** SQLi finding maps to REQ-INPUT-VALID-001-v1.0 (input validation)
  - **Example NEW:** Hardcoded API key creates new REQ-SECRETS-MGMT-001-v1.0

**Approval Criteria:**  
All 5 checklist items must have evidence for Developer to proceed to Phase 3 (Documented Decision).
If any item has low confidence, escalate to AppSec Engineer (see Phase 4: Escalation).
:::

**Output from Phase 2:**
- Completed Checklist C1 (all 5 questions answered with evidence)
- Decision draft (ACEITAR / ADAPTAR / REJEITAR)
- Escalation flag (if conflict or high severity)

### Fase 3: Documented Decision com Decisores Explícitos

**Entrada:** Checklist C1 completado + decision draft

**Decisores por Nível de Severidade (Matriz Decisores):**

| Severity | Phase 2: Analysis | Phase 3: Validation | Phase 4: Approval | SLA |
|---|---|---|---|---|
| **LOW** | Developer (optional) | — (skip) | Reviewer (merge gate) | 7 days |
| **MEDIUM** | Developer (mandatory) | Reviewer (code review) | — | 5 days |
| **HIGH** | Developer (mandatory) | AppSec Engineer (security review) | Reviewer (merge gate) | 3 days |
| **CRITICAL** | Developer (mandatory) | AppSec Engineer + AppSec Lead (senior review) | Reviewer (merge gate) | 48 hours |

**Decision Template (Template T1):**

```markdown
# SAST Finding Decision Log

**Finding ID:** SEMGREP-SQL-001 (internal tracking)
**Tool:** Semgrep
**Rule:** java.lang.security.audit.sql-injection
**Severity:** HIGH
**Date:** 2026-01-15

## Location
- **File:** src/main/java/com/app/controller/UserController.java
- **Line:** 42
- **Function:** getUserById(String userId)
- **Code:** `String query = "SELECT * FROM users WHERE id = " + userId;`

## Checklist C1 Results

✅ **C1.1 Vulnerability Real?**
- Code path reachable: YES (public REST endpoint /api/users/{id})
- User-controlled input: YES (userId from HTTP path parameter)
- Evidence: Code trace in PR #789, endpoint spec in OpenAPI document
- **Conclusion:** Vulnerability is REAL

✅ **C1.2 Severity Correct?**
- CVSS Score: 8.6 (HIGH) — Unauthenticated data access
- Business impact: User can read other users' PII (emails, addresses, phone numbers)
- Exploitability: Direct (no auth required, simple SQL payload)
- **Conclusion:** Severity HIGH is JUSTIFIED

✅ **C1.3 Fix Adequate?**
- Root cause: String concatenation in SQL query
- Suggested fix: Use PreparedStatement with parameter binding
- Analysis: PreparedStatement prevents SQLi entirely (SQL parsing happens before parameter substitution)
- Side effects: None (method signature unchanged, performance improved)
- Coverage: Similar code in getAllUsers() also fixed (same PR)
- **Conclusion:** Fix ADEQUATE and COMPLETE

✅ **C1.4 Defense-in-Depth?**
- Mitigating controls: WAF (AWS WAF rules for SQLi) + Parameterized queries (fix) + Egress validation (database whitelist)
- Defense-in-depth: Justified (WAF first line, parameterization second, DB whitelist third)
- Risk if unfixed: UNACCEPTABLE (no WAF in development environment, missing parameterization)
- **Conclusion:** Defense-in-depth ADEQUATE with fix

✅ **C1.5 Requirement Mapping?**
- Existing requirement: REQ-INPUT-VALID-001-v1.0 (Validate and sanitize all external inputs)
- New requirement: None (SQLi already covered by REQ-INPUT-VALID-001)
- Compliance: Satisfies OWASP Top 10 A03:2021 (Injection), GDPR Art. 5 (Integrity/Confidentiality)
- **Conclusion:** Maps to REQ-INPUT-VALID-001-v1.0

## Decision

**Decision Type:** ACEITAR (Apply fix as suggested)

**Decisores:**
- **Phase 2 (Analysis):** João Silva, Developer (2026-01-15 14:30 UTC)
  - Checklist C1: ✅ Complete, all 5 items validated
  - Decision draft: ACEITAR
  - Escalation: None (no conflict, straightforward fix)
  
- **Phase 3 (Validation):** Maria Santos, AppSec Engineer (2026-01-16 10:00 UTC)
  - Reviewed checklist C1: Agreed
  - Severity assessment: Confirmed HIGH
  - Fix technique: Parameterized query is CORRECT
  - Validation: APPROVED
  
- **Phase 4 (Approval):** Pedro Costa, Code Reviewer (2026-01-16 15:45 UTC)
  - Merge approval: ✅ Granted (all security criteria met)
  - Testing: All tests pass, regression testing completed
  - Merge gate: PASSED

## Justification

Vulnerability is real (direct SQL injection in public endpoint), severity is high (unauthenticated data access), and suggested fix (PreparedStatement) is the correct, complete solution. Defense-in-depth adds WAF layer. Decision aligns with REQ-INPUT-VALID-001-v1.0.

## Implementation

- **PR:** #789 (`fix/sql-injection-UserController`)
- **Commit:** abc123def456 ("Fix: Use PreparedStatement in getUserById() to prevent SQL injection")
- **Tests:** Added test case `testSQLiPayloadBlocked()` with malicious input `userId=1' OR '1'='1`
- **Result:** Test passes, payload blocked, legitimate queries work

## Evidence & Traceability

- Checklist C1 validation: See attached evidence file `C1-validation-PR789.md`
- Code review: PR #789 comments (2026-01-16)
- Test evidence: CI/CD logs, test report `test-results-sql-injection.xml`
- Approval: Signed by Maria Santos (AppSec) & Pedro Costa (Reviewer)

## Follow-up

- [ ] Merge PR #789 (ready for merge)
- [ ] Deploy to staging for integration testing (2026-01-17)
- [ ] Production deployment (2026-01-18 after sign-off)
- [ ] Add custom Semgrep rule for similar patterns to catch future instances
```

**Key Decision Types:**

| Decision | When? | Impact | Escalation? |
|---|---|---|---|
| **ACEITAR** | Fix correct, complete, no side effects | Apply fix as-is | Only if conflict on severity |
| **ADAPTAR** | Fix correct but incomplete, needs modification | Apply modified fix + additional testing | AppSec validates modification |
| **REJEITAR** | False positive OR risk accepted after analysis | Suppress with VEX document | AppSec Lead approves suppression |

### Fase 4: Escalation Procedures

**Escalation Triggers:**

1. **Conflict Type A: Fix Breaks Functionality**
   - **Scenario:** PreparedStatement fix requires API refactor, breaks backward compatibility
   - **Escalation:** Developer + Reviewer + Product Owner
   - **Resolution:** ADAPTAR (modify fix) OR REJEITAR (suppress + mitigate in architecture)
   - **Example:** Original code: `GET /api/users?id=1,2,3` (CSV list), Fix breaks this → Adapt to parameterized array or array binding
   - **SLA:** 3 days

2. **Conflict Type B: Fix Doesn't Resolve Vulnerability**
   - **Scenario:** Suggested fix is incomplete (string escaping instead of parameterization), AppSec identifies gap
   - **Escalation:** Developer + AppSec Engineer
   - **Resolution:** ADAPTAR (correct the fix) OR seek second opinion on risk
   - **Example:** SAST suggests escaping quotes, but SQLi still possible with comment syntax → Escalate to parameterization
   - **SLA:** 2 days (must resolve before merge)

3. **Conflict Type C: Critical Finding Disputed**
   - **Scenario:** Developer claims "not exploitable in our context" (e.g., "WAF blocks it"), AppSec disagrees
   - **Escalation:** Developer + AppSec Engineer + AppSec Lead + Architect
   - **Resolution:** Joint review + evidence gathering (WAF logs, threat model, test)
   - **Example:** "Hardcoded API key in code is OK because we run behind WAF" → Dispute: WAF not in dev/test, code reviews expose secret
   - **SLA:** 48 hours (must resolve before go-live)

**Escalation Workflow (Template T2):**

```markdown
# SAST Finding Escalation

**Finding ID:** SEMGREP-HARDCODED-SECRET-001
**Escalation Type:** Type C (Critical Finding Disputed)
**Initiated:** 2026-01-16 by João Silva (Developer)
**Date:** 2026-01-16 14:00 UTC

## Dispute

**Developer Claim:** "Hardcoded AWS API key in `config.py` is acceptable because code is not exposed to public (internal-only service)."

**AppSec Concern:** "Code repositories are often compromised or exposed; hardcoded secrets represent supply chain risk."

**Evidence Needed:**
- [ ] Developer: Justification + threat model (where is secret exposed? who has access?)
- [ ] AppSec: Assessment of secret exploitability (can anyone with repo access use secret? in what environments?)
- [ ] Architect: Alternative solutions (Secrets Manager, environment variables, KMS)

## Investigation

**Developer (João):** "Code only runs on internal staging server, GitHub repo is private, only 5 engineers have access. Risk is minimal."

**AppSec (Maria):** "GitHub private repos can be exposed (misconfiguration, social engineering, insider threat). Supply chain risk assessment shows API keys are 'crown jewels' for AWS access. Recommend rotating secret immediately and using AWS Secrets Manager."

**Architect (Fernando):** "We have AWS Secrets Manager in prod but not in dev/staging. Recommend patching dev/staging with Secrets Manager + rotating any exposed keys."

## Resolution

**Decision:** ADAPTAR + IMMEDIATE ACTION

1. **Immediate (within 24h):**
   - Rotate compromised AWS API key in production
   - Remove hardcoded key from code (replace with Secrets Manager reference)
   - Add pre-commit hook to detect hardcoded secrets (e.g., `detect-secrets`)

2. **Short-term (within 1 week):**
   - Deploy AWS Secrets Manager to dev/staging environments
   - Migrate all hardcoded secrets to Secrets Manager
   - Update security guidelines (REQ-SECRETS-001-v1.1) to mandate Secrets Manager

3. **Long-term:**
   - Audit all existing repos for similar issues
   - Add SCA scan to CI/CD pipeline with failure threshold

**Approved by:** Maria Santos (AppSec Lead), Fernando Oliveira (Architect), Pedro Costa (CTO)
**Signed:** 2026-01-16 16:00 UTC
```

---

## 📊 Matriz Decisores (por Severity e Nível de Classificação)

**Objetivo:** Determinar quem decide em cada cenário

### L1 (Baixo Risco)

| Severity | Analyzer | Validator | Approver | Required Checklist | SLA |
|---|---|---|---|---|---|
| LOW | Developer (optional) | — | — | C1.1, C1.2 (summary) | 7 days |
| MEDIUM | Developer (mandatory) | Reviewer (code review) | — | Full C1 | 5 days |

### L2 (Risco Médio)

| Severity | Analyzer | Validator | Approver | Required Checklist | SLA |
|---|---|---|---|---|---|
| LOW | Developer | — | — | C1.1, C1.2 | 5 days |
| MEDIUM | Developer | Reviewer | — | Full C1 | 3 days |
| HIGH | Developer | AppSec Engineer | Reviewer | Full C1 + empirical test (addon-12) | 3 days |

### L3 (Risco Crítico)

| Severity | Analyzer | Validator | Approver | Required Checklist | SLA |
|---|---|---|---|---|---|
| MEDIUM | Developer | AppSec Engineer | Reviewer | Full C1 + empirical test | 2 days |
| HIGH | Developer | AppSec Engineer + Code Reviewer | AppSec Lead | Full C1 + empirical test | 48 hours |
| CRITICAL | Developer | AppSec Engineer + AppSec Lead | CTO/CISO | Full C1 + empirical test + threat model review | 24 hours |

---

## 🎯 KPIs — Monitorização de Conformidade

**Métrica 1: Coverage of SAST Findings**
- **Definição:** % de findings (severidade ≥ MEDIUM) com Checklist C1 completado antes de merge
- **Target:** 100% para L2/L3; ≥80% para L1
- **Cálculo:** (Findings com C1 / Total findings ≥ MEDIUM) × 100
- **Responsável:** AppSec Engineer
- **Cadência:** Semanal (por release sprint)

**Métrica 2: Decision Time (Time-to-Decision)**
- **Definição:** Dias desde SAST finding reportado até decisão aprovada (Phase 3 completo)
- **Target:** <3 dias para HIGH, <48 horas para CRITICAL
- **Cálculo:** Data aprovação AppSec - Data finding reportado
- **Responsável:** Development Manager
- **Cadência:** Semanal, P95 percentile

**Métrica 3: Suppression Rate & Justification**
- **Definição:** % de findings REJEITAR (suppressed with VEX) vs. total findings
- **Target:** 10-20% healthy ratio (if >30%, tools may have high false positive rate)
- **Cálculo:** (Suppressed findings / Total findings) × 100
- **Responsável:** AppSec Engineer
- **Cadência:** Mensal

**Métrica 4: Escalation Rate**
- **Definição:** % de findings que triggered escalation (Type A, B, C)
- **Target:** <5% (if >10%, decision framework may be unclear)
- **Cálculo:** (Escalated findings / Total findings) × 100
- **Responsável:** AppSec Lead
- **Cadência:** Mensal

**Métrica 5: Approval Compliance**
- **Definição:** % de findings aprovados por correto decisor (AppSec para HIGH/CRITICAL, Reviewer para merge)
- **Target:** 100% para L3; ≥95% para L2
- **Cálculo:** (Findings aprovados por decisor correto / Total findings) × 100
- **Responsável:** AppSec Engineer
- **Cadência:** Trimestral

---

## 🔗 Integração com Invariantes de agent.md

**I1 — Separação sugestão/decisão:**  
✅ Framework implementado (SAST sugere → Developer valida → AppSec aprova → Reviewer merges)

**I2 — Evidência empírica:**  
↔️ Cross-reference: Ver [addon-12](./12-validacao-manual-findings.md) para validação empírica de findings (CRITICAL/HIGH em L3 requerem teste manual)

**I3 — Reprodutibilidade:**  
✅ Decisões versionadas e rastreadas em Git (Decision Template T1 pode ser armazenado em `decisions/sast-findings/YYYY-MM-DD-XXX.md`)

**I4 — Proteção de ativos:**  
↔️ Hardcoded secrets escalados automaticamente (Conflict Type: Secrets Management)

**I5 — Rastreabilidade:**  
✅ Audit trail completo (Checklist C1 → Decision T1 → PR comments → Commit message → Test evidence)

---

## 📎 Referências Cruzadas

| Documento | Relação |
|---|---|
| [addon-12: Validação Manual de Findings](./12-validacao-manual-findings.md) | I2 empirical testing de findings SAST |
| [addon-05: Gestão de Exceções](./05-excecoes-e-justificacoes.md) | VEX (Vulnerability Exceptions) para FPs |
| [addon-07: Guidelines da Equipa](./07-guidelines-equipa.md) | Versionamento de guidelines mapeadas para requisitos |
| [Cap 05 — addon-21: Validação Manual de CVEs](../../05-dependencias-sbom-sca/addon/21-validacao-manual-cves.md) | Similar framework para dependency vulnerabilities |
| [agent.md](https://github.com/your-org/agent-spec) | Invariantes I1-I5 normativas |

---

## ✅ Checklist de Implementação

- [ ] **Onboarding:**
  - [ ] Treinar team em Checklist C1 (5 questões de validação)
  - [ ] Introduzir Decision Template T1 no fluxo de PR
  - [ ] Registar Escalation Workflow T2 em runbook

- [ ] **Tooling:**
  - [ ] Integrar SAST output com issue tracking (ex: Jira, GitHub Issues)
  - [ ] Adicionar template de PR com Checklist C1
  - [ ] Configurar merge gate: Exigir aprovação AppSec para MEDIUM+ antes de merge

- [ ] **Governance:**
  - [ ] Definir Decisores por project + Severity (usar Matriz Decisores)
  - [ ] Estabelecer SLAs por level (L1/L2/L3)
  - [ ] Implementar KPIs (monitorização mensal)

- [ ] **Processo:**
  - [ ] Mapear findings SAST para requisitos (REQ-XXX-v1.0)
  - [ ] Criar policy: "All MEDIUM+ findings require Checklist C1 before merge"
  - [ ] Criar runbook para Escalation (Type A, B, C)

- [ ] **Validação:**
  - [ ] Teste com 3 findings reais (LOW, MEDIUM, HIGH)
  - [ ] Verificar tempos de decisão (vs. SLA)
  - [ ] Validar audit trail (Decision templates rastreáveis)

---

> 📌 **Princípio central:** SAST sugere, HUMANS decidem.  
> A automação é facilitadora, não substitui julgamento técnico.
