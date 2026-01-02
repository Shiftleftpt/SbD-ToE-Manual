---
id: scanner-decision-containers
title: Decisão Assistida para Findings de Container Scanning
description: Framework de decisão para validar findings de vulnerability scanners (Trivy, Grype) com separação sugestão/decisão
tags: [containers, scanner, decisão, i1, invariantes, trivy, grype]
---

# ✅ Decisão Assistida para Findings de Container Scanning

## 🌟 Objetivo

Implementar o Invariante **I1 (Separação sugestão/decisão)** de [agent.md](https://github.com/your-org/agent-spec) no contexto de container vulnerability scanning.

Scanners como `trivy`, `grype`, `clair`, `anchore` reportam **sugestões** (CVEs encontradas em imagens). Porém, a decisão de **bloquear deploy, remediar, ou aceitar risco** deve ser **explícita, contextual e auditável**, com papéis bem definidos baseados em severidade e classificação L1/L2/L3.

---

## 📋 Contexto normativo

**Problema:**
- Scanner reporta "HIGH: CVE-2024-1234 in nginx:1.25.3" → blocks pipeline automatically
- Sem contexto: CVE is exploitable? Mitigated by network policy? Alternative remediation available?
- Sem decisão documentada: Deploy blocked indefinitely OR risk accepted without justification
- Example real: CVE in base layer (OS package) but application doesn't use affected function → blocked unnecessarily

**Solução:**
Framework 4-fase que torna a decisão **explícita, contextual e auditável**:
1. Scanner reports finding with severity + CVSS score
2. Finding analyzed with Checklist I1 (4 questions: exploitability, mitigation, remediation, business impact)
3. Documented decision (BLOQUEAR-deploy / REMEDIAR-imagem / ACEITAR-risco / DEFER-com-mitigação)
4. Escalation procedures para conflicts (timeline vs. security, false positive disputes, compensating control debates)

---

## 🛠️ Framework 4-Fase

### Fase 1: Scanner Reports Finding (Suggestions Generated)

**Entrada:** Container scanner output:
```
Trivy scan report for myapp:v1.2.3
CRITICAL: CVE-2024-5678 in openssl 3.0.1
- CVSS: 9.8 (Network, Low Complexity, No Auth Required)
- Description: Remote code execution via malformed certificate
- Fixed in: openssl 3.0.2
- Affected: openssl-libs 3.0.1-r0 (Alpine base layer)
```

**Análise automática:**
- Severity: CRITICAL (CVSS 9.8)
- Package type: Base layer (OS dependency, not app dependency)
- Fix available: Yes (upgrade to 3.0.2)
- Reachability: Unknown (requires analysis)

### Fase 2: Finding Analysis com Checklist I1

**Responsável:** DevOps Engineer (initial) + AppSec Engineer (L2/L3 critical)

**Checklist I1 — 4 Questões de Validação:**

:::userstory
**História.**  
Como **DevOps Engineer** ou **AppSec Engineer**, quero **validar se CVE reportado é real threat**, para tomar decisão informada entre BLOQUEAR-deploy, REMEDIAR-imagem, ACEITAR-risco, ou DEFER-com-mitigação.

**Checklist C1: Validação de Container CVE**

- [ ] **C1.1 — CVE is exploitable in runtime context?**
  - [ ] Is vulnerable package actually used by application?
  - [ ] Is vulnerable function/module loaded or called?
  - [ ] Are attack vectors present (network exposed, user input reaches vulnerable code)?
  - [ ] Is runtime configuration hardened (network policies, seccomp, capabilities dropped)?
  - **Evidence needed:** Reachability analysis, runtime behavior test, network policy review
  - **Example EXPLOITABLE:** Web app uses openssl for HTTPS → CVE exploitable via malicious cert → REMEDIATE
  - **Example NOT EXPLOITABLE:** openssl in base layer but app uses boringssl instead → CVE not exploitable → ACCEPT RISK

- [ ] **C1.2 — Existing mitigations reduce exploitability?**
  - [ ] Network policies restrict ingress/egress (attack vector blocked)?
  - [ ] Pod security policies enforce non-root, drop capabilities, read-only FS?
  - [ ] WAF or ingress controller filters malicious input?
  - [ ] Runtime security (Falco, Tetragon) detects exploitation attempts?
  - **Evidence needed:** Network policy manifests, PSP/PSA config, WAF rules, runtime detections
  - **Example MITIGATED:** CVE requires network access but pod has no ingress → risk LOW
  - **Example NOT MITIGATED:** CVE in publicly exposed service with no WAF → risk HIGH

- [ ] **C1.3 — Remediation is feasible and timely?**
  - [ ] Fix available (patch exists, alternative base image, package upgrade)?
  - [ ] Breaking changes if remediated (API changes, config incompatibility)?
  - [ ] SLA for remediation (how long to rebuild + test + deploy)?
  - [ ] Business impact if deployment blocked (feature delay, service outage)?
  - **Evidence needed:** Fix availability check, compatibility test, business priority
  - **Example FEASIBLE:** Upgrade openssl 3.0.1 → 3.0.2 (no breaking changes, 2h rebuild) → REMEDIATE
  - **Example NOT FEASIBLE:** Upgrade requires OS major version change (breaking, 2 weeks work) → DEFER with mitigation

- [ ] **C1.4 — Business context justifies risk acceptance or deferral?**
  - [ ] Is this critical deployment (production outage recovery, security patch)?
  - [ ] Is timeline acceptable (can wait for remediation, or must deploy now)?
  - [ ] Compensating controls available (temporary firewall rule, manual monitoring)?
  - [ ] Risk owner approval if accepting risk (Product Owner, CISO sign-off)?
  - **Evidence needed:** Business justification, compensating controls plan, risk owner approval
  - **Example JUSTIFIED DEFERRAL:** Production outage, deploy critical fix, CVE mitigated by network policy → ACCEPT RISK with monitoring
  - **Example UNJUSTIFIED:** Feature deployment, no urgency, CVE exploitable → BLOQUEAR deploy until remediated

**Approval Criteria:**  
All 4 checklist items must have evidence for decision to proceed to Phase 3 (Documented Decision).
If any item has concerns, escalate to AppSec or Architect (see Phase 4: Escalation).
:::

**Output from Phase 2:**
- Completed Checklist C1 (all 4 questions answered with evidence)
- Risk assessment: Exploitability (HIGH/MEDIUM/LOW) × Mitigation (GOOD/PARTIAL/NONE)
- Decision draft (BLOQUEAR / REMEDIAR / ACEITAR-RISCO / DEFER-COM-MITIGAÇÃO)
- Escalation flag (if conflict or ambiguity)

### Fase 3: Documented Decision com Decisores Explícitos

**Entrada:** Checklist C1 completado + decision draft

**Decisores por CVE Severity × Classification Level (Matriz Decisores):**

| CVE Severity | Analyzer | Reviewer | Approver | SLA |
|---|---|---|---|---|
| **LOW** (CVSS <4.0) | DevOps | — | — (auto-accept with review) | 24 hours |
| **MEDIUM** (CVSS 4.0-6.9) | DevOps | AppSec | — | 8 hours |
| **HIGH** (CVSS 7.0-8.9) | DevOps | AppSec | Product Owner (L2/L3) | 4 hours |
| **CRITICAL** (CVSS 9.0-10.0) | DevOps + AppSec | Lead AppSec | Product Owner + CISO (L3) | 2 hours |

**Proporcionalidade by Level:**

| Level | LOW CVE | MEDIUM CVE | HIGH CVE | CRITICAL CVE |
|---|---|---|---|---|
| **L1** | Auto-accept | Review + remediate within 30 days | Remediate within 7 days | Block deploy, remediate immediately |
| **L2** | Auto-accept | Review + remediate within 14 days | Block deploy OR compensating controls | Block deploy, remediate immediately |
| **L3** | Review + track | Block deploy OR compensating controls + approval | Block deploy, remediate immediately | Block deploy, no exceptions |

**Decision Template (Template T1):**

```markdown
# Container CVE Decision Log

**Finding ID:** TRIVY-CVE-2024-5678-001
**Image:** myapp:v1.2.3 (sha256:abc123...)
**Date:** 2026-01-22 10:00 UTC
**Triggered by:** Pipeline build #456 (commit abc123, PR #789)

## CVE Summary

- **CVE ID:** CVE-2024-5678
- **Severity:** CRITICAL (CVSS 9.8)
- **Package:** openssl 3.0.1 (Alpine base layer: openssl-libs 3.0.1-r0)
- **Vulnerability:** Remote code execution via malformed certificate
- **Fix available:** Yes (upgrade to openssl 3.0.2)
- **Scanner:** Trivy v0.50.0
- **Classification:** L2 (production application)

## Checklist C1 Results

✅ **C1.1 — CVE is exploitable in runtime context?**
- Application: Web API using openssl for HTTPS connections
- Vulnerable function: X509 certificate parsing (used by nginx ingress)
- Attack vector: PRESENT (public-facing HTTPS endpoint)
- Runtime hardening: Network policies allow ingress on port 443 (required for API)
- **Conclusion:** CVE is EXPLOITABLE via malicious certificate presented to HTTPS endpoint

⚠️ **C1.2 — Existing mitigations reduce exploitability?**
- Network policies: Ingress allowed (required for API), egress restricted
- PSP: Non-root user, capabilities dropped, read-only FS
- WAF: No certificate validation at WAF layer (vulnerability reachable)
- Runtime security: Falco rules monitor process execution, but cannot block exploit before execution
- **Conclusion:** Partial mitigation (hardened runtime) but vulnerability STILL EXPLOITABLE

✅ **C1.3 — Remediation is feasible and timely?**
- Fix: Upgrade openssl 3.0.1 → 3.0.2 (available in Alpine 3.19.1)
- Breaking changes: None (patch version, API compatible)
- Rebuild time: 30 minutes (rebuild image + run tests)
- Test coverage: Integration tests pass with new openssl version (verified in staging)
- **Conclusion:** Remediation is FEASIBLE and TIMELY (30 min)

⚠️ **C1.4 — Business context justifies risk acceptance or deferral?**
- Business priority: Feature deployment (new metrics API)
- Timeline: Can defer deployment for 1 hour (not critical)
- Compensating controls: Temporary network policy to restrict ingress to known IPs only (reduce attack surface)
- Risk owner: Product Owner willing to accept temporary deployment with mitigation
- **Conclusion:** Business can WAIT for remediation (1 hour acceptable delay)

## Decision

**Decision Type:** REMEDIAR-IMAGEM (Remediate image before deploy)

**Decision Reasoning:**
- CVE is CRITICAL (CVSS 9.8) and EXPLOITABLE in production context
- Remediation is FEASIBLE (30 min rebuild) and TIMELY (no breaking changes)
- Business can WAIT 1 hour (deployment not critical)
- L2 classification requires REMEDIATION for CRITICAL CVEs
- **Therefore:** Rebuild image with patched openssl, re-scan, deploy patched version

**Alternative Considered (REJECTED):**
- Deploy with compensating control (restrict ingress to known IPs)
- **Why rejected:** L2 policy prohibits deploying CRITICAL CVEs even with compensating controls (defense-in-depth principle)

**Decisores:**
- **Phase 2 (Analysis):** João DevOps Engineer (2026-01-22 10:00 UTC)
  - Checklist C1: ✅ Complete
  - Risk assessment: Exploitability HIGH, Mitigation PARTIAL
  - Decision draft: REMEDIAR-IMAGEM
  - Escalation flag: None
  
- **Phase 3 (Validation):** Maria AppSec Engineer (2026-01-22 10:15 UTC)
  - Reviewed checklist C1: Agreed
  - CVE exploitability: Confirmed HIGH
  - Remediation plan: Approved (rebuild with openssl 3.0.2)
  - Validation: APPROVED to remediate

- **Phase 4 (Release Approval):** Carlos Product Owner (2026-01-22 10:30 UTC)
  - Deployment delayed by 1 hour: Acceptable
  - Remediation approach: Approved
  - Release approval: ✅ GRANTED (for patched image only)

## Implementation

**Action Items:**
1. **Rebuild Image:**
   - [ ] Update Dockerfile: FROM alpine:3.19.1 (includes openssl 3.0.2)
   - [ ] Rebuild: docker build -t myapp:v1.2.3-patched
   - [ ] Re-scan: trivy image myapp:v1.2.3-patched (verify CVE-2024-5678 resolved)
   - Owner: João DevOps + Build team
   - Timeline: 30 minutes

2. **Verification:**
   - [ ] Verify CVE-2024-5678 not present in new scan
   - [ ] Run integration tests in staging (API endpoints functional)
   - [ ] Sign patched image: cosign sign myapp:v1.2.3-patched
   - Owner: QA + AppSec
   - Timeline: 20 minutes

3. **Deploy:**
   - [ ] Deploy patched image to production: kubectl set image deployment/myapp myapp=myapp:v1.2.3-patched
   - [ ] Monitor for errors (5 min)
   - [ ] Confirm metrics API functional
   - Owner: DevOps + SRE
   - Timeline: 10 minutes

4. **Post-Deploy Monitoring:**
   - [ ] Falco alerts monitored for 24 hours (detect any runtime anomalies)
   - [ ] No incidents: Mark CVE as RESOLVED
   - Owner: SRE + AppSec
   - Timeline: 24 hours post-deploy

## Traceability

- **CVE:** CVE-2024-5678 (NIST NVD link)
- **Scanner:** Trivy v0.50.0 (scan report: trivy-scan-myapp-v1.2.3.json)
- **Image:** myapp:v1.2.3 → myapp:v1.2.3-patched
- **Dockerfile:** commit abc123 → def456 (upgrade Alpine 3.19.0 → 3.19.1)
- **PR:** #789 (CVE remediation)
- **Decision chain:** João → Maria → Carlos
- **Deployment:** 2026-01-22 11:00 UTC (patched version)
```

**Key Decision Types:**

| Decision | Meaning | When Used | Impact |
|---|---|---|---|
| **BLOQUEAR-DEPLOY** | Block deployment until remediated | CVE CRITICAL + exploitable + L2/L3 | Deploy blocked, feature delayed |
| **REMEDIAR-IMAGEM** | Rebuild image with fix, re-scan, deploy | Fix available + feasible + timely | Image rebuilt, delay acceptable |
| **ACEITAR-RISCO** | Accept CVE with documented justification | CVE not exploitable OR mitigated OR L1 + LOW severity | Deploy proceeds, CVE tracked |
| **DEFER-COM-MITIGAÇÃO** | Deploy with compensating controls, remediate later | CVE exploitable but urgent deployment + compensating controls | Deploy with mitigation, remediate within SLA |

---

## 🔁 Escalation Procedures

**Escalation Triggers:**

1. **Conflict Type A: Timeline vs. Security**
   - **Scenario:** CRITICAL CVE found, remediation takes 2 days, business needs deploy today
   - **Escalation:** DevOps + AppSec + Product Owner + CISO (L3 only)
   - **Resolution:** Deploy with compensating controls (network isolation, monitoring) OR defer deployment
   - **SLA:** 2 hours (critical timeline decision)

2. **Conflict Type B: False Positive Dispute**
   - **Scenario:** Scanner reports CRITICAL but DevOps claims "not exploitable in our context"
   - **Escalation:** DevOps + AppSec + Security Architect
   - **Resolution:** Empirical validation (see addon-12 for testing procedures) OR accept DevOps analysis with documented evidence
   - **SLA:** 4 hours (requires testing/analysis)

3. **Conflict Type C: Compensating Control Adequacy**
   - **Scenario:** HIGH CVE, fix not available, DevOps proposes network policy as mitigation
   - **Escalation:** DevOps + AppSec + Architect
   - **Resolution:** Validate compensating control effectiveness (penetration test, threat model review) OR block deploy
   - **SLA:** 4 hours (requires technical validation)

**Escalation Workflow (Template T2):**

```markdown
# Container CVE Escalation

**Finding ID:** TRIVY-CVE-2024-9999-002
**Escalation Type:** Type A (Timeline vs. Security)
**Initiated:** 2026-01-23 by Maria AppSec (2026-01-23 14:00 UTC)
**Date:** 2026-01-23 14:00 UTC

## Conflict

**Situation:** CRITICAL CVE (CVSS 9.1) in postgresql client library. Production database migration scheduled for today (2026-01-23 18:00 UTC). Remediation requires upgrading postgresql 14 → 15 (2-day effort: testing, config migration, compatibility validation).

**AppSec Claim:** "CRITICAL CVE must be remediated before deploy. Cannot accept risk for L3 database."

**Product Owner Pressure:** "Database migration is contractually committed. Delay costs $50K/day penalty. Must deploy today."

**DevOps Proposal:** "Deploy with compensating control: Database not publicly exposed, network policy restricts access to app pods only. CVE requires network access from internet."

## Investigation

**AppSec (Maria):** "CVE-2024-9999 allows remote code execution via malformed SQL query. Even if database not public, compromised app pod could exploit."

**DevOps (João):** "App pods run with read-only FS, non-root, capabilities dropped. Exploit requires write access to /tmp. Network policy blocks egress from database pod."

**Product Owner (Carlos):** "Business cannot accept $50K penalty. Deploy with mitigation, remediate within 7 days."

**Security Architect (Pedro):** "Compromised app pod is realistic threat (past incidents: SSRF in web app). Compensating controls reduce but do not eliminate risk."

**CISO (Rita, L3 only):** "Risk acceptance for CRITICAL CVE in L3 requires board approval. Not feasible for today's timeline."

## Resolution

**Decision:** DEFER-COM-MITIGAÇÃO (Deploy with compensating controls, remediate within 7 days)

1. **Deploy Today with Enhanced Mitigations:**
   - [ ] Network policy: Database pod egress blocked (cannot exfiltrate data)
   - [ ] App pod: Upgrade to latest version (no known SSRF vulnerabilities)
   - [ ] Runtime monitoring: Falco rules detect SQL injection attempts + unusual database queries
   - [ ] Manual review: DBA monitors database logs for suspicious activity (24/7 for 7 days)
   
2. **Remediation Plan (7-day SLA):**
   - [ ] Upgrade postgresql 14 → 15 (testing + migration)
   - [ ] Re-scan image with upgraded postgresql
   - [ ] Deploy patched version within 7 days (2026-01-30)

3. **Risk Acceptance:**
   - [ ] Product Owner accepts risk: Documented in risk register
   - [ ] Compensating controls validated: Penetration test confirms exploit blocked by network policy + runtime monitoring
   - [ ] AppSec approves: Conditional on 7-day remediation SLA

**Approved by:** Maria (AppSec), Carlos (Product Owner), Rita (CISO - L3 sign-off)
**Signed:** 2026-01-23 15:00 UTC
**Deploy Window:** 2026-01-23 18:00 UTC (with mitigations)
**Remediation Deadline:** 2026-01-30 (7 days)
```

---

## 📊 Matriz Decisores (por CVE Severity e Nível de Classificação)

**Objetivo:** Determinar quem decide em cada cenário, responsabilidade clara

### L1 (Baixo Risco)

| CVE Severity | Analyzer | Reviewer | Approver | Required Checklist | SLA |
|---|---|---|---|---|---|
| LOW (CVSS <4.0) | DevOps | — | — | C1.1, C1.3 | 24 hours |
| MEDIUM (CVSS 4.0-6.9) | DevOps | — | — | C1.1, C1.3 | 8 hours |
| HIGH (CVSS 7.0-8.9) | DevOps | AppSec | — | Full C1 | 4 hours |
| CRITICAL (CVSS 9.0-10.0) | DevOps | AppSec | Product Owner | Full C1 + risk acceptance | 2 hours |

### L2 (Risco Médio)

| CVE Severity | Analyzer | Reviewer | Approver | Required Checklist | SLA |
|---|---|---|---|---|---|
| LOW | DevOps | — | — | C1.1, C1.3 | 24 hours |
| MEDIUM | DevOps | AppSec | — | Full C1 | 8 hours |
| HIGH | DevOps | AppSec | Product Owner | Full C1 + compensating controls | 4 hours |
| CRITICAL | DevOps + AppSec | Lead AppSec | Product Owner | Full C1 + risk acceptance + mitigation plan | 2 hours |

### L3 (Risco Crítico)

| CVE Severity | Analyzer | Reviewer | Approver | Required Checklist | SLA |
|---|---|---|---|---|---|
| MEDIUM | DevOps | AppSec | — | Full C1 | 8 hours |
| HIGH | DevOps + AppSec | Lead AppSec | Product Owner | Full C1 + compensating controls + penetration test | 4 hours |
| CRITICAL | DevOps + AppSec | Lead AppSec + Security Architect | Product Owner + CISO | Full C1 + risk acceptance + board approval (if accepting risk) | 1 hour |

---

## 🎯 KPIs — Monitorização de Conformidade

**Métrica 1: CVE Decision Documentation**
- **Definição:** % de CVEs (severity ≥ MEDIUM) com Checklist C1 documentado
- **Target:** 100% para L2/L3; ≥80% para L1
- **Cálculo:** (CVEs com C1 / Total CVEs ≥ MEDIUM) × 100
- **Responsável:** DevOps Lead
- **Cadência:** Semanal

**Métrica 2: CVE Decision Time-to-Resolution**
- **Definição:** Horas desde CVE reportado até decisão aprovada
- **Target:** <2h CRITICAL, <4h HIGH (L2/L3)
- **Cálculo:** Data/hora aprovação - Data/hora CVE reportado
- **Responsável:** AppSec Lead
- **Cadência:** Semanal, P95 percentile

**Métrica 3: Deploy Block Rate**
- **Definição:** % de deploys bloqueados por CVEs vs. total
- **Target:** <10% (if >20%, scanner tuning needed or remediation process inadequate)
- **Cálculo:** (Deploys blocked / Total deploy attempts) × 100
- **Responsável:** Release Manager
- **Cadência:** Mensal

**Métrica 4: Risk Acceptance Rate**
- **Definição:** % de CRITICAL CVEs accepted with risk vs. remediated
- **Target:** <5% for L2/L3 (most CRITICAL CVEs should be remediated, not accepted)
- **Cálculo:** (CRITICAL CVEs accepted / Total CRITICAL CVEs) × 100
- **Responsável:** CISO (L3) / AppSec Lead (L2)
- **Cadência:** Mensal

**Métrica 5: Remediation SLA Compliance**
- **Definição:** % of CVEs remediated within SLA (7 days HIGH, 14 days MEDIUM)
- **Target:** ≥90%
- **Cálculo:** (CVEs remediated within SLA / Total CVEs requiring remediation) × 100
- **Responsável:** DevOps Lead
- **Cadência:** Mensal

---

## 🔗 Integração com Invariantes de agent.md

**I1 — Separação sugestão/decisão:**  
✅ Framework implementado (Scanner sugere → DevOps valida → AppSec aprova → Product Owner autoriza)

**I2 — Evidência empírica:**  
↔️ Cross-reference: Ver [addon-12](./12-validacao-empirica-containers.md) para validação empírica de CVE exploitability

**I3 — Reprodutibilidade:**  
✅ CVEs documentadas com scan reports, imagens versionadas (digest), decisões em decision-logs/

**I4 — Proteção de ativos:**  
✅ CVE decision by severity × L1/L2/L3 classification

**I5 — Rastreabilidade:**  
✅ Audit trail completo (CVE → Checklist C1 → Decision T1 → Remediation → Deploy)

---

## 📎 Referências Cruzadas

| Documento | Relação |
|---|---|
| [addon-12: Validação Empírica de Container CVEs](./12-validacao-empirica-containers.md) | I2 empirical testing de CVE exploitability |
| [Cap 07 — addon-11: Decisão Assistida em Gates](../../07-cicd-seguro/addon/11-decisao-gates-pipeline.md) | Similar I1 framework para pipeline gates |
| [aplicacao-lifecycle.md](./aplicacao-lifecycle.md) | US-21 operationalizes este addon |
| [agent.md](https://github.com/your-org/agent-spec) | Invariantes I1-I5 normativas |

---

## ✅ Checklist de Implementação

- [ ] **Onboarding:**
  - [ ] Treinar DevOps em Checklist C1 (4 questões)
  - [ ] Introduzir Decision Template T1 no fluxo de scanning
  - [ ] Registar Escalation Workflow T2 em runbook

- [ ] **Processo:**
  - [ ] Criar policy: "All MEDIUM+ CVEs require Checklist C1 before deploy"
  - [ ] Documentar Decisores por CVE severity × level
  - [ ] Criar SLA para CVE decision (2h/4h/8h/24h)

- [ ] **Tooling:**
  - [ ] Integrar scanner output com issue tracking
  - [ ] Criar workflow automático: "CVE found" → "notify reviewers" → "create decision issue"
  - [ ] Setup dashboard: CVEs by status, decision time, block rate

- [ ] **Governance:**
  - [ ] Criar CVE review board with defined roles
  - [ ] Estabelecer escalation procedures (Type A, B, C)
  - [ ] Implementar KPIs (dashboard + monthly review)

- [ ] **Validação:**
  - [ ] Teste com 3 CVEs reais (LOW, HIGH, CRITICAL)
  - [ ] Verificar tempos de decisão (vs. SLA)
  - [ ] Validar audit trail (Decision templates rastreáveis)

---

> 📌 **Princípio central:** Scanners suggest, HUMANS decide with context.  
> CVE severity alone is insufficient — exploitability, mitigations, and business context determine the right decision.
