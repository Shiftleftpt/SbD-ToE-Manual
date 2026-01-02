---
id: validacao-empirica-containers
title: Validação Empírica de Container CVEs
description: Framework de testes empíricos para validar exploitability de CVEs reportadas em container scanning
tags: [containers, validação, empirica, i2, invariantes, cve, exploit]
---

# ✅ Validação Empírica de Container CVEs

## 🌟 Objetivo

Implementar o Invariante **I2 (Evidência acima de plausibilidade)** de [agent.md](https://github.com/your-org/agent-spec) no contexto de container vulnerability scanning.

Scanners como `trivy`, `grype`, `clair` reportam CVEs baseadas em package versions, mas **não validam se CVE é realmente exploitável no runtime context**. A validação empírica confirma se CVE é **real threat** (exploitable, reachable) ou **false positive** (not exploitable due to hardening, network isolation, or non-usage of vulnerable function).

---

## 📋 Contexto normativo

**Problema:**
- **Falso Positivo (FP):** Scanner reporta "CRITICAL CVE in curl" mas application doesn't use curl at runtime
- **Falso Negativo (FN):** Scanner doesn't detect vulnerable library loaded dynamically at runtime
- **Sem validação empírica:** Teams suppress scanners (lose trust) OR block all CVEs without understanding (over-restrictive)

**Solução:**
Framework de validação empírica com:
- **Taxonomia:** 5 categorias de CVE types (OS packages, App dependencies, Dynamic libraries, Configuration, Runtime behavior)
- **Testes:** Deploy in staging + exploit PoC + reachability test + network isolation verification
- **FP Management:** Suppression with justification + VEX document + periodic review
- **FN Detection:** RCA + custom scanner rules + regression tests
- **Quality Metrics:** FP <20%, FN <5%, time-to-validation <4h

---

## 🧪 Taxonomia: 5 Categorias de Container CVEs

### 1️⃣ OS Package Vulnerabilities (Base Layer)

**Example CVE:**
```
Tool: Trivy
Finding: CVE-2024-1234 in glibc 2.35
Severity: HIGH (CVSS 7.5)
Package: glibc-2.35-r0 (Alpine base layer)
Vulnerability: Buffer overflow in DNS resolver
Status: ⛔ BLOCKED
```

**Empirical Validation Checklist:**

:::userstory
**História.**  
Como **DevOps Engineer ou AppSec Engineer**, quero **validar empiricamente se OS package CVE é exploitable**, para confirmar se bloquear deploy é justified.

**Procedimento T1: Validação de OS Package CVE**

1. **Verificar se package é usado:**
   - [ ] Is vulnerable package actually loaded by application?
   - [ ] Check running processes: `lsof -p <pid>` (list open libraries)
   - [ ] Check dynamic library dependencies: `ldd /app/binary`
   - [ ] If library not loaded → CVE not reachable → FALSE POSITIVE

   ```bash
   # Example: Check if glibc DNS resolver is used
   kubectl exec -it myapp-pod -- lsof -p 1 | grep libc
   # If application doesn't do DNS lookups → DNS resolver CVE not exploitable
   ```

2. **Testar reachability de vulnerable function:**
   - [ ] Is vulnerable function called by application?
   - [ ] Example: CVE in DNS resolver → test if app does DNS queries
   - [ ] If function not called → CVE not exploitable → FALSE POSITIVE

   ```bash
   # Example: Test DNS resolver usage
   kubectl exec -it myapp-pod -- strace -p 1 -e trace=getaddrinfo,gethostbyname
   # If no DNS calls → DNS resolver CVE not exploitable
   ```

3. **Verificar runtime hardening:**
   - [ ] Is vulnerable code path mitigated by runtime hardening?
   - [ ] Example: Buffer overflow → read-only FS, non-root, capabilities dropped
   - [ ] If hardening blocks exploit → risk REDUCED (not eliminated)

4. **Exploit PoC (if applicable):**
   - [ ] Deploy image in staging with vulnerable package
   - [ ] Run exploit PoC (if publicly available)
   - [ ] Monitor: Does exploit succeed? (RCE, crash, data exfiltration)
   - [ ] If exploit succeeds → CVE is EXPLOITABLE (TRUE POSITIVE)
   - [ ] If exploit blocked → CVE mitigated by hardening (ACCEPT RISK with documentation)

   ```bash
   # Example: Test buffer overflow exploit
   # 1. Deploy vulnerable image in staging
   kubectl run test-vuln --image=myapp:vulnerable --rm -it -- /bin/sh
   
   # 2. Run exploit PoC (hypothetical)
   ./exploit-cve-2024-1234.py --target localhost:8080
   
   # 3. Monitor for RCE
   # If exploit fails → hardening effective
   # If exploit succeeds → CVE confirmed exploitable
   ```

5. **Document result:**

   **If CVE is EXPLOITABLE:**
   - Severity: CONFIRMED
   - Impact: Buffer overflow allows RCE
   - Decision: REMEDIATE (upgrade glibc)
   - Remediation: FROM alpine:3.19.1 (includes patched glibc)

   **If CVE is FALSE POSITIVE:**
   - Reason: Application doesn't use DNS resolver function
   - Evidence: strace shows no DNS calls, lsof shows libc loaded but vulnerable function not called
   - Decision: SUPPRESS with justification
   - FP log: `falsos-positivos/FP-2026-01-23-CVE-2024-1234-glibc-dns-not-used.md`

:::

**Common FP Scenarios:**
- Package installed but not used (e.g., curl in base image but app uses httpx library)
- Vulnerable function not called (e.g., DNS resolver CVE but app uses static IPs)
- Runtime hardening blocks exploit (e.g., read-only FS prevents buffer overflow write)

**Common FN Scenarios:**
- Dynamic library loaded at runtime not scanned (e.g., plugin loaded via dlopen)
- Configuration vulnerability not detected by scanner (e.g., insecure JWT secret in env var)

---

### 2️⃣ Application Dependency Vulnerabilities (App Layer)

**Example CVE:**
```
Tool: Grype
Finding: CVE-2024-5678 in express 4.17.1 (Node.js)
Severity: CRITICAL (CVSS 9.1)
Package: express@4.17.1 (npm dependency)
Vulnerability: Prototype pollution leading to RCE
Status: ⛔ BLOCKED
```

**Empirical Validation Checklist:**

:::userstory
**História.**  
Como **Developer ou AppSec Engineer**, quero **validar empiricamente se application dependency CVE is exploitable**, para confirmar if remediation is necessary.

**Procedimento T2: Validação de App Dependency CVE**

1. **Verificar se vulnerable code path is reachable:**
   - [ ] Is vulnerable function/module used by application code?
   - [ ] Code search: grep for vulnerable function usage
   - [ ] If not used → CVE not reachable → FALSE POSITIVE

   ```bash
   # Example: Search for express vulnerable function
   grep -r "express.Router" src/
   # If not found → express router not used → CVE not exploitable
   ```

2. **Testar exploit in staging:**
   - [ ] Deploy vulnerable version in staging
   - [ ] Send malicious payload (exploit PoC)
   - [ ] Monitor: Does exploit succeed? (RCE, data leak, DoS)
   - [ ] If exploit fails → CVE not exploitable (hardening, input validation blocks exploit)

   ```bash
   # Example: Test prototype pollution exploit
   curl -X POST http://staging.example.com/api/user \
     -H "Content-Type: application/json" \
     -d '{"__proto__": {"isAdmin": true}}'
   
   # Check if prototype pollution occurred
   curl http://staging.example.com/api/admin
   # If admin access denied → exploit blocked (input validation works)
   # If admin access granted → CVE exploitable
   ```

3. **Verificar input validation:**
   - [ ] Does application validate input before passing to vulnerable function?
   - [ ] Example: Prototype pollution → does app sanitize JSON keys?
   - [ ] If validation blocks exploit → CVE mitigated (ACCEPT RISK with validation evidence)

4. **Document result:**

   **If CVE is EXPLOITABLE:**
   - Severity: CONFIRMED (prototype pollution leads to privilege escalation)
   - Impact: Attacker can gain admin access
   - Decision: REMEDIATE (upgrade express 4.17.1 → 4.18.0)
   - Remediation: npm update express@4.18.0

   **If CVE is FALSE POSITIVE:**
   - Reason: Input validation blocks exploit (JSON keys sanitized before parsing)
   - Evidence: Test shows exploit blocked, code review confirms validation
   - Decision: SUPPRESS with justification + monitor for bypass
   - FP log: `falsos-positivos/FP-2026-01-23-CVE-2024-5678-express-input-validation.md`

:::

**Common FP Scenarios:**
- Vulnerable function not called by application code
- Input validation blocks exploit (WAF, application-level sanitization)
- Vulnerable code path only reachable by admin users (reduced attack surface)

**Common FN Scenarios:**
- Vulnerability in custom code not detected by scanner (e.g., SQL injection in custom query builder)
- Transitive dependency vulnerability (scanner checks direct deps only)

---

### 3️⃣ Dynamic Library / Runtime Loaded Dependencies

**Example CVE:**
```
Tool: Trivy
Finding: CVE-2024-9999 in libxml2 2.9.10
Severity: HIGH (CVSS 7.8)
Package: libxml2-2.9.10 (loaded dynamically by Python lxml)
Vulnerability: XXE (XML External Entity) injection
Status: ⛔ BLOCKED
```

**Empirical Validation Checklist:**

:::userstory
**História.**  
Como **AppSec Engineer**, quero **validar empirically if dynamically loaded library CVE is exploitable**, para confirmar se risco é real.

**Procedimento T3: Validação de Dynamic Library CVE**

1. **Verificar se library is actually loaded:**
   - [ ] Check runtime library loading: `lsof -p <pid>` or `/proc/<pid>/maps`
   - [ ] If library not loaded → CVE not reachable → FALSE POSITIVE

   ```bash
   # Example: Check if libxml2 is loaded
   kubectl exec -it myapp-pod -- cat /proc/1/maps | grep libxml2
   # If libxml2 not found → CVE not exploitable
   ```

2. **Testar XXE exploit:**
   - [ ] Send malicious XML payload with external entity
   - [ ] Monitor: Does application parse external entity? (file read, SSRF)
   - [ ] If exploit succeeds → CVE exploitable

   ```bash
   # Example: Test XXE exploit
   curl -X POST http://staging.example.com/api/parse-xml \
     -H "Content-Type: application/xml" \
     -d '<?xml version="1.0"?>
          <!DOCTYPE foo [<!ENTITY xxe SYSTEM "file:///etc/passwd">]>
          <data>&xxe;</data>'
   
   # Check response for /etc/passwd content
   # If passwd exposed → XXE exploitable
   # If blocked → CVE mitigated (XML parser configured securely)
   ```

3. **Verificar XML parser configuration:**
   - [ ] Is XML parser configured to disable external entities?
   - [ ] Example: lxml with `resolve_entities=False`
   - [ ] If disabled → XXE blocked → ACCEPT RISK with config evidence

4. **Document result:**

   **If CVE is EXPLOITABLE:**
   - Severity: CONFIRMED (XXE allows file read)
   - Impact: Attacker can read /etc/passwd, env vars, secrets
   - Decision: REMEDIATE (upgrade libxml2 OR disable external entities)
   - Remediation: pip install lxml==4.9.3 (includes patched libxml2)

   **If CVE is FALSE POSITIVE:**
   - Reason: XML parser configured to disable external entities
   - Evidence: lxml initialized with `resolve_entities=False`, test confirms XXE blocked
   - Decision: SUPPRESS with config documentation
   - FP log: `falsos-positivos/FP-2026-01-23-CVE-2024-9999-libxml2-xxe-disabled.md`

:::

**Common FP Scenarios:**
- Library loaded but vulnerable function not called (e.g., libxml2 loaded but app doesn't parse XML)
- Secure configuration blocks exploit (e.g., XXE disabled in parser config)

**Common FN Scenarios:**
- Dynamic library loaded via plugin not scanned (scanner misses runtime-loaded libs)
- Library version misdetection (scanner checks package version, not actual library binary)

---

### 4️⃣ Configuration Vulnerabilities (Secrets, Permissions, Network)

**Example Finding:**
```
Tool: Trivy / Checkov
Finding: Hardcoded database password in Dockerfile ENV
Severity: CRITICAL
File: Dockerfile line 12 (ENV DB_PASS=secret123)
Status: ⛔ BLOCKED
```

**Empirical Validation Checklist:**

:::userstory
**História.**  
Como **AppSec Engineer**, quero **validar empiricamente se configuration vulnerability is exploitable**, para confirmar se secret is exposed.

**Procedimento T4: Validação de Configuration Vulnerability**

1. **Verificar se secret is exposed:**
   - [ ] Check running container env vars: `kubectl exec -it pod -- env`
   - [ ] Check image layers: `docker history --no-trunc myapp:v1.2.3`
   - [ ] If secret found → EXPLOITABLE (anyone with image access can read)

   ```bash
   # Example: Check for hardcoded secrets
   docker history --no-trunc myapp:v1.2.3 | grep -i password
   # If ENV DB_PASS found → secret exposed in image layer
   ```

2. **Testar secret accessibility:**
   - [ ] Can attacker extract secret? (image pull, container exec)
   - [ ] Test: docker pull myapp:v1.2.3 → docker inspect → read env vars
   - [ ] If accessible → CONFIRMED vulnerability

   ```bash
   # Example: Extract secret from image
   docker pull myapp:v1.2.3
   docker inspect myapp:v1.2.3 | grep -A 5 Env
   # If DB_PASS visible → secret compromised
   ```

3. **Assess impact:**
   - [ ] What can attacker do with exposed secret? (database access, API access)
   - [ ] Test: Use extracted secret to access resource
   - [ ] If successful → HIGH IMPACT (lateral movement, data exfiltration)

4. **Document result:**

   **If Configuration Vulnerability is EXPLOITABLE:**
   - Severity: CONFIRMED (database password exposed in image)
   - Impact: Anyone with image access (registry, Kubernetes nodes) can read password
   - Decision: REMEDIATE IMMEDIATELY (remove hardcoded password, use secrets manager)
   - Remediation: Remove ENV from Dockerfile, inject secret via Kubernetes Secret at runtime

   **If Configuration is SECURE:**
   - Reason: Secret injected via external secrets manager (not hardcoded)
   - Evidence: Dockerfile review shows no hardcoded secrets, runtime verification confirms secret from K8s Secret
   - Decision: NO ACTION NEEDED (secure configuration)

:::

**Common FP Scenarios:**
- False alarm (scanner detects "password" string but it's a placeholder, not real secret)
- Secret encrypted in image (not plaintext, requires decryption key)

**Common FN Scenarios:**
- Secret in non-standard location (e.g., custom config file not scanned by tool)
- Secret obfuscated (e.g., base64 encoded, scanner doesn't decode)

---

### 5️⃣ Runtime Behavior Vulnerabilities (Container Escape, Privilege Escalation)

**Example Finding:**
```
Tool: Falco / Tetragon
Finding: Container running as root with CAP_SYS_ADMIN
Severity: HIGH
Risk: Potential container escape
Status: ⚠️ ALERT
```

**Empirical Validation Checklist:**

:::userstory
**História.**  
Como **SRE ou AppSec Engineer**, quero **validar empiricamente se runtime configuration allows container escape**, para confirmar se hardening is adequate.

**Procedimento T5: Validação de Runtime Behavior Vulnerability**

1. **Verificar runtime security context:**
   - [ ] Is container running as root? `kubectl get pod -o yaml | grep runAsUser`
   - [ ] Are capabilities excessive? `kubectl get pod -o yaml | grep capabilities`
   - [ ] Is filesystem writable? `kubectl get pod -o yaml | grep readOnlyRootFilesystem`
   - [ ] If root + CAP_SYS_ADMIN + writable FS → HIGH RISK (potential escape)

   ```bash
   # Example: Check security context
   kubectl get pod myapp-pod -o yaml | grep -A 10 securityContext
   # If runAsUser: 0 (root) + capabilities: [SYS_ADMIN] → vulnerable to escape
   ```

2. **Testar container escape:**
   - [ ] Run known container escape exploit (e.g., cgroup release_agent exploit)
   - [ ] Monitor: Can attacker escape to host? (access host filesystem, processes)
   - [ ] If escape succeeds → CONFIRMED vulnerability

   ```bash
   # Example: Test cgroup escape (requires CAP_SYS_ADMIN)
   kubectl exec -it myapp-pod -- /bin/sh
   
   # Inside container (if running as root with CAP_SYS_ADMIN)
   mkdir /tmp/cgrp && mount -t cgroup -o memory cgroup /tmp/cgrp
   echo 1 > /tmp/cgrp/notify_on_release
   # ... (full exploit omitted for brevity)
   
   # If exploit succeeds → container escape confirmed
   ```

3. **Verificar hardening mitigations:**
   - [ ] Is seccomp profile restrictive? (blocks dangerous syscalls)
   - [ ] Is AppArmor/SELinux enforcing? (restricts file access)
   - [ ] Are network policies restrictive? (limits lateral movement)
   - [ ] If hardening blocks exploit → risk REDUCED (document mitigations)

4. **Document result:**

   **If Runtime Vulnerability is EXPLOITABLE:**
   - Severity: CONFIRMED (container escape possible with CAP_SYS_ADMIN)
   - Impact: Attacker can escape to host, compromise node, lateral movement to other pods
   - Decision: REMEDIATE (drop CAP_SYS_ADMIN, run as non-root, read-only FS)
   - Remediation: Update Deployment manifest with securityContext hardening

   **If Runtime is HARDENED:**
   - Reason: Seccomp profile blocks escape syscalls, non-root user, capabilities dropped
   - Evidence: Escape exploit blocked by seccomp, test confirms no host access
   - Decision: NO ACTION NEEDED (hardening adequate)

:::

**Common FP Scenarios:**
- Container runs as root but in isolated namespace (no host access)
- Capabilities present but not actually used by application

**Common FN Scenarios:**
- Zero-day container escape vulnerability (scanner doesn't know about it yet)
- Custom runtime configuration not validated (e.g., custom runc config)

---

## 📊 FP/FN Management

### Gestão de Falsos Positivos (FP)

**Workflow:**

```
1. Scanner Reports CVE
   ↓
2. DevOps/AppSec: Empirical Validation (T1-T5)
   - [ ] Is CVE exploitable? (exploit PoC, reachability test)
   - [ ] Run appropriate test for category
   - [ ] Document evidence
   ↓
3. Result: FP or TP (True Positive)?
   
   IF TP → Remediation required (see addon-11 Decision Framework)
   
   IF FP → Create Suppression Document & VEX
```

**FP Suppression Template (Template S1):**

```markdown
# Falso Positivo Report - Container CVE

**CVE ID:** CVE-2024-1234
**Tool:** Trivy v0.50.0
**Category:** OS Package (T1)
**Date:** 2026-01-23
**Reviewer:** DevOps Engineer + AppSec Engineer

## CVE Details
- Image: myapp:v1.2.3 (sha256:abc123...)
- Package: glibc 2.35-r0 (Alpine base layer)
- CVE: CVE-2024-1234 "Buffer overflow in DNS resolver"
- Severity: HIGH (CVSS 7.5)
- Fix: Upgrade to glibc 2.36

## Empirical Validation (T1 Procedure)

**Step 1: Verify package usage**
- Package loaded: YES (lsof shows libc.so loaded)
- Vulnerable function called: NO (strace shows no DNS calls: getaddrinfo, gethostbyname)
- Application architecture: Uses static IP addresses, no DNS lookups

**Step 2: Test reachability**
- Test command: `strace -p 1 -e trace=getaddrinfo,gethostbyname -f`
- Result: No DNS resolver calls detected in 24-hour monitoring period
- Conclusion: DNS resolver vulnerable function not reachable

**Step 3: Runtime hardening**
- Security context: runAsUser 1000 (non-root), readOnlyRootFilesystem: true
- Capabilities: All dropped except NET_BIND_SERVICE
- Network policy: Egress restricted to known endpoints only (no DNS port 53)

**Step 4: Exploit PoC**
- Exploit not applicable (DNS resolver not used)
- Network policy blocks DNS queries (port 53 egress denied)

## Why It's a False Positive

**Technical Justification:**
- DNS resolver vulnerability not exploitable because application doesn't use DNS
- Application uses static IP configuration (no dynamic host resolution)
- Network policy blocks DNS traffic (defense-in-depth)
- glibc present in base layer but vulnerable function not called

**Verification:**
- Tested: Application functions correctly without DNS resolver
- Monitoring: 7-day runtime trace confirms no DNS calls
- Architecture review: Static IPs documented in design, no DNS dependency

## Suppression

**Trivy suppression annotation:**
```yaml
# trivy-ignore:CVE-2024-1234:Application doesn't use DNS resolver; static IPs only; network policy blocks DNS
```

**VEX File:** `vex/FP-2026-01-23-CVE-2024-1234-glibc-dns-not-used.vex.json`
```json
{
  "component": {
    "name": "myapp",
    "version": "v1.2.3",
    "digest": "sha256:abc123..."
  },
  "vulnerabilities": [{
    "ref": "CVE-2024-1234",
    "state": "not_affected",
    "justification": "vulnerable_code_not_in_execute_path",
    "impact": "DNS resolver vulnerable function not called by application; static IP configuration; network policy blocks DNS traffic"
  }]
}
```

## Approval

- **Reviewed by:** João DevOps + Maria AppSec
- **Approved:** 2026-01-23 16:00 UTC
- **Signed:** joao.devops@company.com, maria.appsec@company.com
- **Next review:** 2026-07-23 (6-month cycle)
- **Review criteria:** If application architecture changes to use DNS, re-evaluate suppression

## Lessons Learned

**For scanning configuration:**
- Trivy should have reachability analysis (detect if vulnerable function called)
- Consider custom policy: "HIGH CVE in OS package + function not used = downgrade to MEDIUM"
- Add runtime monitoring: Alert if DNS calls appear (indicates architecture change)
```

### Gestão de Falsos Negativos (FN)

**Workflow:**

```
1. Security Issue Discovered (Pentest, incident, runtime alert)
   ↓
2. Check: Did scanner find this CVE?
   
   IF YES (TP detected) → Great, scanner working!
   
   IF NO → False Negative found
   ↓
3. Root Cause Analysis (RCA)
   - Why did scanner miss this?
   - Package version misdetection? Dynamic loading? Configuration issue?
   ↓
4. Improve Detection
   - Custom scanner rule
   - Update scanner database
   - Add runtime monitoring
```

**FN Root Cause Analysis Template (Template S2):**

```markdown
# Falso Negativo Report - Container CVE

**Finding ID:** FN-2026-01-24-001
**Vulnerability Type:** Dynamic Library (T3)
**Discovery Method:** Penetration Test (2026-01-24)
**Date:** 2026-01-24

## Vulnerability Details

**Discovered:** Prototype pollution in lodash 4.17.20 (dynamically loaded by plugin)
**Severity:** HIGH (CVSS 7.4)
**How discovered:** Pentester exploited prototype pollution to gain admin access

**Why scanner missed it:**
- Trivy scans package.json dependencies (lists lodash 4.17.21 - patched)
- But application loads lodash plugin dynamically at runtime (plugin bundles lodash 4.17.20 - vulnerable)
- Scanner doesn't scan plugin bundles (only top-level dependencies)

## Root Cause Analysis

### Why Detection Failed

1. **Gap 1: Dynamic plugin loading not scanned**
   - Application loads plugins from /app/plugins/ directory
   - Plugins bundle their own dependencies (separate node_modules)
   - Trivy scans /app/package-lock.json only (doesn't scan plugin bundles)

2. **Gap 2: No runtime dependency inventory**
   - No SBOM generated for runtime-loaded dependencies
   - Application loads plugins dynamically (require() at runtime)
   - Scanner has no visibility into runtime loaded libraries

3. **Configuration Issue:** Scanner config
   - Before: `trivy image --scanners vuln`
   - Missing: `--scanners vuln,secret,config` + custom paths for plugins

### Why It Matters

- Pentester exploited lodash prototype pollution via plugin API
- Gained admin access, modified application behavior
- Data exfiltration possible (access to customer PII)

## Mitigation

### Immediate (Fix the vulnerability)
- [ ] Update plugin to use lodash 4.17.21 (patched)
- [ ] Audit all plugins for vulnerable dependencies
- [ ] Implement plugin signature verification (prevent malicious plugins)
- [ ] Add runtime monitoring: Falco rule to detect prototype pollution attempts

### Improve Detection
- [ ] Update scanner: Add custom path for plugin scanning
  - Before: `trivy image myapp:v1.2.3`
  - After: `trivy image --scanners vuln --skip-dirs /app/cache --scan-all-files myapp:v1.2.3`
- [ ] Generate SBOM including plugin dependencies: `syft scan --scope all-layers myapp:v1.2.3`
- [ ] Add runtime dependency inventory: Monitor loaded libraries with `lsof` or eBPF

### Add Regression Test
- [ ] Create test: Image with plugin containing lodash 4.17.20 should fail scan
- [ ] Test SBOM generation: Verify plugin dependencies included
- [ ] Test in CI: Push sample vulnerable plugin, verify scanner detects

### Update Configuration
- [ ] Update Trivy config in `.trivyignore`:
  ```yaml
  # Scan all files including plugins
  scan-all-files: true
  skip-dirs:
    - /app/cache
    - /tmp
  ```
- [ ] Add SBOM generation step in pipeline: `syft scan --scope all-layers -o cyclonedx-json > sbom.json`

## Approval & Tracking

- **RCA Completed by:** AppSec team
- **Date:** 2026-01-24
- **Action Items:**
  - [ ] Fix plugin dependency — Due: 2026-01-25
  - [ ] Update scanner config — Due: 2026-01-25
  - [ ] Generate SBOM with plugins — Due: 2026-01-26
  - [ ] Team training on plugin security — Due: 2026-02-01
  - [ ] Audit all plugins — Due: 2026-02-07

## Lessons Learned

1. **Dynamic loading bypasses static scanners** (need runtime inventory)
2. **Plugins are high-risk** (bundle their own dependencies, hard to track)
3. **SBOM must include all layers** (not just top-level dependencies)
4. **Runtime monitoring essential** (detect exploits missed by scanners)
```

---

## 🎯 Quality Metrics & Thresholds

**Metric 1: False Positive Rate**
- **Target:** <20% (if >30%, scanner creates too much noise)
- **Definition:** (FPs / Total CVEs reported) × 100
- **Action:** If >30%, adjust scanner config or replace with alternative

**Metric 2: False Negative Rate**
- **Target:** <5% (if >10%, scanner inadequate)
- **Definition:** (FNs discovered / Total real vulnerabilities) × 100
- **Action:** If >10%, add runtime monitoring + enhance scanning

**Metric 3: Time-to-Validation**
- **Target:** <4h for HIGH, <2h for CRITICAL (L2/L3)
- **Definition:** Hours from CVE reported to validation complete
- **Action:** If > SLA, investigate bottlenecks (manual testing delays, exploit PoC unavailable)

**Metric 4: Proporcionalidade by Risk Level**

| Level | FP Rate Target | FN Rate Target | Time-to-Validation | Empirical Test Required |
|---|---|---|---|---|
| L1 | <25% | <10% | <8 hours | Optional (CRITICAL only) |
| L2 | <20% | <5% | <4 hours | CRITICAL+HIGH (empirical test mandatory) |
| L3 | <15% | <3% | <2 hours | ALL CVEs ≥MEDIUM (multi-method validation) |

---

## 🔗 Integração com Invariantes de agent.md

**I2 — Evidência acima de plausibilidade:**  
✅ Framework implementado (Taxonomia T1-T5, exploit PoCs, reachability tests, FP/FN management, quality metrics)

**I1 — Separação sugestão/decisão:**  
↔️ Cross-reference: Ver [addon-11](./11-scanner-decision-containers.md) para decision framework (Checklist C1, Decision Template T1)

**I3 — Reprodutibilidade:**  
✅ Tests versionadas (T1-T5 documented, reproducible commands + exploit PoCs)

**I4 — Proteção de ativos:**  
✅ Runtime hardening validation (T5) protects critical assets

**I5 — Rastreabilidade:**  
✅ FP/FN documents with approval trail (VEX, RCA, signed by AppSec)

---

## 📎 Referências Cruzadas

| Documento | Relação |
|---|---|
| [addon-11: Scanner Decision Framework](./11-scanner-decision-containers.md) | I1 decision framework (works with I2 empirical testing) |
| [Cap 07 — addon-12: Validação Empírica Gates](../../07-cicd-seguro/addon/12-validacao-empirica-gates.md) | Similar I2 framework for pipeline findings |
| [aplicacao-lifecycle.md](./aplicacao-lifecycle.md) | US-22 operationalizes este addon |
| [agent.md](https://github.com/your-org/agent-spec) | Invariantes I1-I5 normativas |

---

## ✅ Checklist de Implementação

- [ ] **Taxonomia & Procedures:**
  - [ ] Treinar DevOps/AppSec em T1-T5 (5 test procedures)
  - [ ] Documentar exploit PoCs por categoria
  - [ ] Setup staging environment para validation (isolated Kubernetes namespace)

- [ ] **FP/FN Management:**
  - [ ] Criar processo FP: CVE → Analysis → Suppression → VEX
  - [ ] Criar processo FN: Discovery → RCA → Custom rule → Regression test
  - [ ] Arquivo de FPs: `falsos-positivos/FP-YYYY-MM-DD-*.md`
  - [ ] Arquivo de FNs: `falsos-negativos/FN-YYYY-MM-DD-*.md`

- [ ] **Quality Metrics:**
  - [ ] Setup dashboard: FP rate, FN rate, time-to-validation
  - [ ] Define thresholds (scanner replacement if FP >30%)
  - [ ] Monthly review de métricas

- [ ] **Integration:**
  - [ ] Link addon-11 (Decision) com addon-12 (Evidence)
  - [ ] CVE policy: L2/L3 HIGH/CRITICAL CVEs require both C1 checklist + empirical test
  - [ ] Training: "How to validate a container CVE" (T1-T5 procedures)

---

> 📌 **Princípio central:** Evidence-driven CVE decisions.  
> Scanner reports, Empirical testing confirms.  
> FP/FN management ensures scanner quality and team trust.
