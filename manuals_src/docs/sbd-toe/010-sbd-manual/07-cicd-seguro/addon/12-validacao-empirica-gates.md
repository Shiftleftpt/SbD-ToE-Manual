---
id: validacao-empirica-gates
title: Validação Empírica de Findings Bloqueados
description: Taxonomia de 5 categorias com testes empíricos para validar gate findings, FP/FN management
tags: [gates, validação empírica, i2, invariantes, testes, pipeline]
---

# ✅ Validação Empírica de Findings Bloqueados

## 🌟 Objetivo

Implementar o Invariante **I2 (Evidência acima de plausibilidade)** de [agent.md](https://github.com/your-org/agent-spec) no contexto de validação empírica de findings que bloqueiam gates em CI/CD.

Ferramentas de scanning (SAST, container scanning, policy checks) produzem **falsos positivos** (alertam quando não há risco) e **falsos negativos** (não alertam quando há risco real). A validação empírica confirma se gate blocks são justified ou FPs que podem ser suprimidos.

---

## 📋 Contexto normativo

**Problema:**
- **Falso Positivo (FP):** Gate bloqueia "hardcoded secret" mas é dummy value de testes (FP) → Bloqueia release sem razão
- **Falso Negativo (FN):** Gate não detecta vulnerability que pentesting encontra depois → Production risk
- **Sem validação:** Team gasta tempo fixando não-issues OR ignora legítimos findings, perdendo confiança em ferramentas

**Solução:**
Framework de validação empírica com:
- **Taxonomia:** 5 categorias de gate violations (Container vulns, Policy violations, Hardcoded secrets, IaC misconfigs, SBOM gaps)
- **Testes:** Exploit PoC ou reachability test para cada categoria
- **FP Management:** Suppression com justificativa técnica + VEX document
- **FN Detection:** RCA + custom rules + regression tests
- **Quality Metrics:** FP <20%, FN <5%, time-to-validation <24h CRITICAL

---

## 🧪 Taxonomia: 5 Categorias de Gate Violations

### 1️⃣ Container Vulnerabilities (Base Image Scan)

**Gate Block Example:**
```
Tool: Trivy (Container Scanning)
Type: Critical Vulnerability in Base Image
Severity: CRITICAL
Location: Dockerfile base image
Base: node:18-alpine (CVE-2024-12345: RCE in npm)
Status: ⛔ BLOCKED
Policy: No CRITICAL vulnerabilities allowed in L2/L3
```

**Empirical Validation Checklist:**

:::userstory
**História.**  
Como **DevOps Engineer ou AppSec Engineer**, quero **validar empiricamente se vulnerability em container base image é realmente exploitável**, para confirmar se bloquear deploy é justified.

**Procedimento T1: Validação de Container Vulnerability**

1. **Identificar vulnerabilidade:**
   - [ ] CVE ID + description (ex: CVE-2024-12345 RCE in npm)
   - [ ] Affected component (npm version x.y.z)
   - [ ] Is component used in application? (pode estar em base image mas nunca invocado)
   - [ ] Is component reachable from external input?

2. **Verificar exploitabilidade:**
   - [ ] Build container locally with vulnerable base
   - [ ] Attempt to exploit vulnerability (RCE if possible)
   - [ ] Can attacker trigger the vulnerable code path?
   - [ ] What privileges would attacker have?

   **Example - npm RCE test:**
   ```bash
   # Build image locally
   docker build -t test:vuln -f Dockerfile .
   
   # Attempt to trigger npm vulnerability
   docker run --rm test:vuln npm --version
   # Check if version is vulnerable
   
   # Or use CVSS/EPSS data
   # If EPSS >80%, vulnerability is likely exploitable in real-world
   ```

3. **Assess real-world risk:**
   - [ ] Is npm executed with attacker input? (package.json install, npm run?)
   - [ ] Is vulnerability in runtime code or build-time only?
   - [ ] What's the blast radius if exploited?

4. **Document result:**

   **If EXPLOITABLE:**
   - Severity: CONFIRMED
   - Risk: RCE in container with application privileges
   - Decision: BLOQUEAR release (gate block is justified)
   - Fix: Update base image to patched version (node:18-alpine-X.X.X-patch)

   **If NOT EXPLOITABLE (FP):**
   - Reason: Vulnerable component not invoked in application
   - Evidence: Code audit shows npm not executed during runtime
   - Decision: SUPPRESS with VEX (gate block can be overridden)
   - FP log: `falsos-positivos/FP-2026-01-16-Container-npm.md`

:::

**Common FP Scenarios:**
- Vulnerable component in base image but never invoked (ex: npm vulnerability but app uses pnpm)
- Vulnerability requires specific environment/configuration not present
- CVE patched in newer versions of base image
- CVSS/EPSS score high but real-world exploitability low (PoC doesn't work)

**Common FN Scenarios:**
- Supply chain vulnerability (compromised dependency not detected by CVE databases)
- Container hardening bypass (e.g., escape from container runtime)
- Multi-stage build vulnerability (vulnerability in builder stage leaks to runtime)

---

### 2️⃣ Policy Violations (OPA/Kyverno)

**Gate Block Example:**
```
Tool: Kyverno (Policy Engine)
Type: Pod Security Violation
Severity: HIGH
Violation: Container running as root (UID 0)
Policy: "All containers must run as non-root"
Status: ⛔ BLOCKED
```

**Empirical Validation Checklist:**

:::userstory
**História.**  
Como **DevOps Engineer**, quero **validar empiricamente se policy violation é real security risk**, para saber se permitir exceção.

**Procedimento T2: Validação de Policy Violation**

1. **Understand policy intent:**
   - [ ] Why was this policy created? (Defense-in-depth, compliance, best practice?)
   - [ ] What's the security goal? (ex: prevent privilege escalation via container escape)
   - [ ] Is policy appropriate for this application? (L3 critical app vs. L1 internal tool)

2. **Assess real-world risk if exception granted:**
   - [ ] If running as root, can attacker escape to host?
   - [ ] What's the likelihood of container escape in this environment?
   - [ ] Are there compensating controls? (seccomp, AppArmor, network isolation?)

   **Example - root container assessment:**
   ```bash
   # Test container security
   docker run --rm my-image
   # Check user: id
   # If UID=0 (root):
   #   - Can attacker escape to host OS? (depends on kernel, container runtime)
   #   - Is there seccomp profile blocking dangerous syscalls?
   #   - Are there AppArmor/SELinux rules?
   ```

3. **Check for legitimate reasons:**
   - [ ] Does application REQUIRE root? (rare, usually no)
   - [ ] Can application functionality be preserved with non-root?
   - [ ] Is there a technical limitation preventing non-root?

4. **Document result:**

   **If VIOLATION IS REAL SECURITY RISK:**
   - Policy: KEEP ENFORCED
   - Decision: Fix application to comply (run as non-root user)
   - Remediation: `Dockerfile: USER appuser` (non-root)

   **If VIOLATION IS FALSE SECURITY CONCERN (FP):**
   - Reason: Root not actually exploitable OR compensating controls present
   - Evidence: seccomp profile blocks container escape syscalls
   - Decision: OVERRIDE policy with documented risk acceptance
   - Risk acceptance: `policy-exceptions/PEX-2026-01-16-root-container.md`

:::

**Common FP Scenarios:**
- Policy too strict for application needs (root required for legitimate reasons)
- Compensating controls mitigate policy violation (seccomp, AppArmor, network isolation)
- Policy rule has false positives (security scanning misconfiguration)

**Common FN Scenarios:**
- Policy doesn't cover all attack vectors (allows root but misses privileged capabilities)
- Policy bypass via workarounds (ex: policy checks only Kubernetes, but Docker CLI bypasses it)

---

### 3️⃣ Hardcoded Secrets in Code/Config

**Gate Block Example:**
```
Tool: TruffleHog (Secret Scanning)
Type: Hardcoded Secret Detected
Severity: CRITICAL
Location: src/config.py:42
Secret: AWS_SECRET_ACCESS_KEY=AKIA...
Status: ⛔ BLOCKED
Policy: No secrets allowed in code
```

**Empirical Validation Checklist:**

:::userstory
**História.**  
Como **AppSec Engineer**, quero **validar empiricamente se hardcoded secret é realmente exploitável**, para confirmar se bloquear merge é justified.

**Procedimento T3: Validação de Hardcoded Secret**

1. **Classify secret type:**
   - [ ] Real secret (production key) vs. dummy/test value?
   - [ ] Can secret be used to access real resources?
   - [ ] How many people have access to code repository?

2. **Attempt to use secret:**
   - [ ] Extract secret from code
   - [ ] Try to authenticate with secret (AWS CLI, API call, database connection)
   - [ ] Does secret grant access? Or revoked/invalid?

   ```bash
   # Example: AWS API key
   export AWS_ACCESS_KEY_ID="AKIA..."
   export AWS_SECRET_ACCESS_KEY="..."
   aws s3 ls
   
   # If returns S3 buckets → Secret is VALID (EXPLOITABLE)
   # If access denied → Secret is INVALID/REVOKED (lower risk, but still exposed)
   ```

3. **Assess blast radius:**
   - [ ] What resources can be accessed with this secret?
   - [ ] Is it a production key or test/dev key?
   - [ ] Can attacker modify/delete resources?

4. **Document result:**

   **If SECRET IS VALID & EXPLOITABLE:**
   - Severity: CRITICAL (confirmed working secret)
   - Decision: BLOQUEAR merge (gate block is justified)
   - Action: Rotate secret IMMEDIATELY in production
   - Fix: Remove from code, use Secrets Manager

   **If SECRET IS INVALID/TEST VALUE (FP):**
   - Reason: Dummy value (sk_test_xxx), not real secret
   - Evidence: Attempted to use secret → Access denied
   - Decision: SUPPRESS with technical justification
   - FP log: `falsos-positivos/FP-2026-01-16-Secret-test-key.md`

:::

**Common FP Scenarios:**
- Test/dummy credentials (sk_test_xxx, not sk_live_xxx)
- Credentials already rotated (secret is revoked)
- Public API keys (intentionally shared, not secrets)
- Example/documentation keys (clearly marked as example)

**Common FN Scenarios:**
- Secret obfuscated/encoded (base64, ROT13)
- Multi-part secret split across multiple variables
- Secrets in environment variables (harder to detect)
- Legacy secret formats not recognized by scanner

---

### 4️⃣ IaC Misconfigurations (Terraform/Helm Scanning)

**Gate Block Example:**
```
Tool: Checkov (IaC Scanning)
Type: IaC Misconfiguration
Severity: HIGH
Issue: S3 bucket has public read access (ACL=public-read)
Location: terraform/s3.tf:15
Policy: All data buckets must be private
Status: ⛔ BLOCKED
```

**Empirical Validation Checklist:**

:::userstory
**História.**  
Como **DevOps Engineer ou Cloud Architect**, quero **validar empiricamente se IaC misconfiguration é real security risk**, para saber se remediation é justified.

**Procedimento T4: Validação de IaC Misconfiguration**

1. **Understand configuration intent:**
   - [ ] Why is S3 bucket public? (intentional for public website vs. accident?)
   - [ ] Is public access appropriate for this data?
   - [ ] What kind of data is stored (public info vs. sensitive)?

2. **Assess real-world impact:**
   - [ ] Can attacker read bucket contents?
   - [ ] Can attacker modify/delete files?
   - [ ] Can attacker perform actions on resources?
   - [ ] Are there compensating controls? (VPC endpoint, bucket policy restrictions?)

   ```bash
   # Example: Test S3 bucket accessibility
   aws s3 ls s3://my-bucket --no-sign-request
   # If returns contents → Public read CONFIRMED
   # If access denied → Bucket is protected (misconfiguration warning only)
   ```

3. **Check business requirements:**
   - [ ] Must this resource be public for application to work?
   - [ ] Can we add bucket policy to restrict access more granularly?
   - [ ] Are there compliance requirements (GDPR, PCI) preventing public access?

4. **Document result:**

   **If MISCONFIGURATION IS REAL SECURITY RISK:**
   - Severity: CONFIRMED
   - Decision: FIX configuration (make S3 bucket private)
   - Remediation: `terraform: acl = "private"`

   **If MISCONFIGURATION IS INTENTIONAL/NECESSARY (FP):**
   - Reason: S3 bucket hosts public website content (legitimate public access)
   - Evidence: Bucket policy restricts read to CloudFront distribution only, not true "public-read"
   - Decision: Suppress with documented justification
   - FP log: `falsos-positivos/FP-2026-01-16-S3-public-website.md`

:::

**Common FP Scenarios:**
- Configuration intentionally public (public website hosting)
- Compensation controls in place (bucket policy restricts access to specific principals)
- Configuration warning overly strict (best practice but not required for this data)

**Common FN Scenarios:**
- Implicit public access (via IAM policy, not bucket ACL)
- Combination of configurations creating unintended exposure
- Legacy resource not covered by IaC scanning

---

### 5️⃣ SBOM Gaps / Supply Chain Risk

**Gate Block Example:**
```
Tool: CycloneDX SBOM Validation
Type: SBOM Gap Detected
Severity: MEDIUM
Issue: Dependency com.example:library:1.0 missing from SBOM
Location: Container image myapp:latest
Status: ⛔ BLOCKED
Policy: All dependencies must be included in SBOM (for supply chain visibility)
```

**Empirical Validation Checklist:**

:::userstory
**História.**  
Como **AppSec Engineer ou DevSecOps**, quero **validar empiricamente se SBOM gap é indicativo de supply chain risk**, para saber se gate block é justified.

**Procedimento T5: Validação de SBOM Gap**

1. **Identify missing dependency:**
   - [ ] What's the missing component? (name, version)
   - [ ] Is it a direct dependency or transitive?
   - [ ] Is it actually present in built artifact?

2. **Assess supply chain risk:**
   - [ ] Can the missing dependency be exploited?
   - [ ] Is dependency from trusted source?
   - [ ] Are there known CVEs for this version?
   - [ ] Is dependency signed/verified?

   ```bash
   # Example: Check if dependency is actually in image
   docker inspect myapp:latest | grep com.example.library
   
   # Or use SBOM tools to find discrepancies
   syft myapp:latest --output json | grep library
   ```

3. **Determine root cause:**
   - [ ] Why is SBOM missing dependency? (tool limitation, build configuration issue, or legitimate override?)
   - [ ] Is SBOM generation broken or component intentionally excluded?

4. **Document result:**

   **If SBOM GAP IS REAL SUPPLY CHAIN RISK:**
   - Decision: FIX SBOM generation (ensure all dependencies captured)
   - Action: Update SBOM generation tooling or build configuration

   **If SBOM GAP IS ACCEPTABLE:**
   - Reason: Dependency is transitive and already captured by parent (not risk)
   - Evidence: SBOM tool misconfiguration, not missing dependency
   - Decision: SUPPRESS with documented justification
   - SBOM gap log: `sbom-gaps/GAP-2026-01-16-transitive-dependency.md`

:::

**Common FP Scenarios:**
- SBOM tool doesn't recognize all dependency formats (gradle, npm, etc.)
- Transitive dependency appears as gap but is captured via parent
- Tool configuration incomplete (missing scanners for some languages)

**Common FN Scenarios:**
- Supply chain attack via compromised package (not detected by SBOM as "missing")
- Embedded binaries or vendored code not in SBOM
- Dynamic dependencies loaded at runtime (static tools can't detect)

---

## 📊 FP/FN Management

### Gestão de Falsos Positivos (FP)

**Workflow:**

```
1. Gate Bloqueia
   ↓
2. Developer/AppSec: Empirical Validation (T1-T5)
   - [ ] Is finding real? (exploit PoC, reachability test)
   - [ ] Run appropriate test for category
   - [ ] Document evidence
   ↓
3. Result: FP or TP (True Positive)?
   
   IF TP → Remediation required (see addon-11 Decision Framework)
   
   IF FP → Create Suppression Document & VEX
```

**FP Suppression Template (Template S1):**

```markdown
# Falso Positivo Report - Gate Block

**Gate ID:** TRIVY-CONTAINER-2026-01-16-001
**Tool:** Trivy (Container Scanning)
**Category:** Container Vulnerability (T1)
**Date:** 2026-01-16
**Reviewer:** DevOps Engineer + AppSec Engineer

## Finding Details
- Container: myapp:latest
- Vulnerability: CVE-2024-12345 (RCE in npm)
- Base Image: node:18-alpine
- Severity: CRITICAL (reported)

## Empirical Validation (T1 Procedure)

**Step 1: Identify Vulnerability**
- CVE: CVE-2024-12345 - RCE vulnerability in npm module X
- Affected: npm < 10.5.0
- Current version in image: npm 10.4.0 (VULNERABLE version)

**Step 2: Verify Exploitability**
- Is npm executed in application runtime?
  - Answer: NO - npm is only in base image for build-time dependency management
  - Evidence: Application uses pnpm (not npm) for dependency management
  - npm binary is not executed during runtime
  
**Step 3: Real-World Risk Assessment**
- Can attacker trigger vulnerable code path? NO
- npm is not invoked at runtime, vulnerability unreachable
- Blast radius if exploited: NONE (component not in runtime path)

## Why It's a False Positive

**Technical Justification:**
- npm vulnerable version is in base image (build-time tool)
- Application uses pnpm for dependency management (not npm)
- npm binary is never invoked at runtime
- Vulnerability is present but unreachable

**Verification:**
- Code audit: Confirmed npm not used in application code
- Dockerfile analysis: npm only used for build-stage dependencies
- Runtime testing: strace shows npm not executed during app runtime

## VEX (Vulnerability Exception) Document

**Status:** NOT_AFFECTED (Code is not vulnerable because component not used in runtime)
**Justification:** npm vulnerability exists in base image, but npm is not invoked during application runtime
**Impact Statement:** Unreachable vulnerability; application uses pnpm instead
**Expiration:** 2026-07-16 (6 months review cycle)

## Suppression

**Kyverno suppression annotation:**
```yaml
# kyverno.io/ignore: CVE-2024-12345-npm-not-runtime
# Reason: npm is build-time only, not executed at runtime
# Application uses pnpm instead
# VEX: FP-2026-01-16-npm-build-only
```

**VEX File:** `vex/FP-2026-01-16-npm-build-only.vex.json`
```json
{
  "bom-ref": "myapp:latest",
  "vulnerabilities": [{
    "ref": "CVE-2024-12345",
    "state": "not_affected",
    "justification": "component_not_used",
    "impact": "npm is build-time dependency, not invoked at runtime"
  }]
}
```

## Approval

- **Reviewed by:** Pedro Garcia, DevOps Engineer + Maria Santos, AppSec Engineer
- **Approved:** 2026-01-16 16:00 UTC
- **Signed:** pedro.garcia@company.com, maria.santos@company.com
- **Next review:** 2026-07-16 (6-month cycle)

## Lessons Learned

**For scanning configuration:**
- Trivy should have context about which npm is build-time vs. runtime
- Could add Dockerfile analysis to suppress build-stage vulnerabilities automatically
- Consider multi-stage build scanning to distinguish build vs. runtime components
```

### Gestão de Falsos Negativos (FN)

**Workflow:**

```
1. Vulnerability Discovered (Pentest, incident, etc.)
   ↓
2. Check: Did gate find this?
   
   IF YES (TP detected) → Great, gate working!
   
   IF NO → False Negative found
   ↓
3. Root Cause Analysis (RCA)
   - Why did gate miss this?
   - Tool limitation? Configuration issue?
   ↓
4. Improve Detection
   - Custom rule creation
   - Tool configuration update
   - Add manual testing
```

**FN Root Cause Analysis Template (Template S2):**

```markdown
# Falso Negativo Report - Gate Block

**Finding ID:** FN-2026-01-17-001
**Vulnerability Type:** Container Image Supply Chain Attack
**Discovery Method:** Security Pentest (2026-01-17)
**Date:** 2026-01-17

## Vulnerability Details

**Discovered:** Compromised base image (attacker pushed malware to quay.io/sneaky-base:latest)
**Severity:** CRITICAL (malware in all deployments)
**How discovered:** Pentest detected unexpected outbound connections to C&C server

**Why gate missed it:**
- Gate uses image digest for reproducibility: `quay.io/sneaky-base@sha256:abc123...`
- Image with sha256:abc123 passed Trivy scan (clean at time of build)
- 2 days later, attacker re-tagged :latest to push malware (same tag, different digest)
- Gate checked image by tag (:latest), not by digest
- Team pulled new image (with malware) without re-scanning

## Root Cause Analysis

### Why Gate Failed

1. **Gap 1: Gate checks by tag, not digest**
   - Policy: `FROM quay.io/sneaky-base:latest` (mutable tag)
   - Gate scans at build-time, but :latest can change anytime
   - Attacker re-tags :latest to point to compromised image
   - Gate doesn't re-verify at deployment time

2. **Gap 2: No supply chain verification**
   - Gate doesn't check image signature (unsigned image from registry)
   - Gate doesn't verify image source (could be from untrusted registry)
   - No cosign/notary verification of image provenance

3. **Configuration Issue:** Image pull policy allows latest
   - `imagePullPolicy: Always` in K8s manifests
   - Pulls latest version (with malware) without re-scan

## Mitigation

### Immediate (Fix the vulnerability)
- [ ] Rotate compromised image
- [ ] Audit what malware did in prod (network logs, file system changes)
- [ ] Update all running deployments with known-good image digest

### Improve Detection
- [ ] Require image digest (immutable) instead of tag
  - Before: `FROM quay.io/sneaky-base:latest`
  - After: `FROM quay.io/sneaky-base@sha256:known-good-digest`
- [ ] Add image signing requirement (cosign, notary)
  - Gate must verify image signature before deployment
- [ ] Add runtime image verification
  - Verify image hasn't changed between gate scan and deployment

### Add Regression Test
- [ ] Create test: Detect if image changes after gate scan
- [ ] Test unsigned images are blocked
- [ ] Test pull-from-malicious-registry is blocked

### Update SBOM/SCA
- [ ] Include base image digest in SBOM
- [ ] Track image signature/provenance
- [ ] Alert on image re-tagging

## Approval & Tracking

- **RCA Completed by:** AppSec team
- **Date:** 2026-01-17
- **Action Items:**
  - [ ] Update gate to verify image signatures — Due: 2026-01-18
  - [ ] Require image digest (not tag) — Due: 2026-01-19
  - [ ] Add supply chain verification (cosign) — Due: 2026-01-25
  - [ ] Team training on image security — Due: 2026-01-23

## Lessons Learned

1. **Mutable tags are risky** in CI/CD (can hide supply chain attacks)
2. **Image scanning is point-in-time** (need re-verification at deployment)
3. **Supply chain verification** (signatures, provenance) is essential for base images
4. **Multiple defense layers** needed (gate scan + deployment verification + runtime monitoring)
```

---

## 🎯 Quality Metrics & Thresholds

**Metric 1: False Positive Rate**
- **Target:** <20% (if >30%, gate creates too much noise)
- **Definition:** (FPs / Total gate blocks) × 100
- **Action:** If >30%, adjust gate policy or tool configuration

**Metric 2: False Negative Rate**
- **Target:** <5% (if >10%, gate inadequate)
- **Definition:** (FNs discovered / Total real vulnerabilities) × 100
- **Action:** If >10%, add custom rules + enhance scanning

**Metric 3: Time-to-Validation**
- **Target:** <24h for CRITICAL, <48h for HIGH
- **Definition:** Hours from gate block to validation complete
- **Action:** If > SLA, investigate bottlenecks (tool slowness, manual testing delays)

**Metric 4: Proporcionalidade by Risk Level**

| Level | FP Rate Target | FN Rate Target | Time-to-Validation | Empirical Test Required |
|---|---|---|---|---|
| L1 | <25% | <10% | <48 hours | Optional (CRITICAL only) |
| L2 | <20% | <5% | <24 hours | CRITICAL+HIGH (empirical test mandatory) |
| L3 | <15% | <3% | <12 hours | ALL blocks (multi-method validation) |

---

## 🔗 Integração com Invariantes de agent.md

**I2 — Evidência acima de plausibilidade:**  
✅ Framework implementado (Taxonomia T1-T5, empirical tests, FP/FN management, quality metrics)

**I1 — Separação sugestão/decisão:**  
↔️ Cross-reference: Ver [addon-11](./11-decisao-gates-pipeline.md) para decision framework (Checklist C1, Decision Template T1, escalation)

**I3 — Reprodutibilidade:**  
✅ Tests versionadas (T1-T5 documented, reproducible commands)

**I4 — Proteção de ativos:**  
✅ Supply chain vulnerability (T5) detection protects critical assets

**I5 — Rastreabilidade:**  
✅ FP/FN documents with approval trail (VEX, RCA, signed by AppSec)

---

## 📎 Referências Cruzadas

| Documento | Relação |
|---|---|
| [addon-11: Decisão Assistida em Gates](./11-decisao-gates-pipeline.md) | I1 decision framework (works with I2 empirical testing) |
| [Cap 06 — addon-12: Validação Manual Findings](../../06-desenvolvimento-seguro/addon/12-validacao-manual-findings.md) | Similar I2 framework for code-level findings (6 categories) |
| [Cap 05 — addon-21: Validação Manual CVEs](../../05-dependencias-sbom-sca/addon/21-validacao-manual-cves.md) | Similar I2 framework for dependency vulnerabilities |
| [agent.md](https://github.com/your-org/agent-spec) | Invariantes I1-I5 normativas |

---

## ✅ Checklist de Implementação

- [ ] **Taxonomia & Procedures:**
  - [ ] Treinar team em T1-T5 (5 test procedures)
  - [ ] Definir tools usados (docker, kubectl, aws, terraform, sbom tools)
  - [ ] Documentar PoC por categoria

- [ ] **FP/FN Management:**
  - [ ] Criar processo FP: Block → Analysis → Suppression → VEX
  - [ ] Criar processo FN: Discovery → RCA → Custom rule → Regression test
  - [ ] Arquivo de FPs: `falsos-positivos/FP-YYYY-MM-DD-*.md`
  - [ ] Arquivo de FNs: `falsos-negativos/FN-YYYY-MM-DD-*.md`

- [ ] **Quality Metrics:**
  - [ ] Setup dashboard: FP rate, FN rate, time-to-validation
  - [ ] Define thresholds (gate replacement if FP >30%)
  - [ ] Monthly review de métricas

- [ ] **Integration:**
  - [ ] Link addon-11 (Decision) com addon-12 (Evidence)
  - [ ] Gate policy: L2/L3 blocks require both C1 checklist + empirical test
  - [ ] Training: "How to validate a gate block" (T1-T5 procedures)

---

> 📌 **Princípio central:** Evidence-driven decisions.  
> Gate suggests, Empirical testing confirms.  
> FP/FN management ensures gate quality.
