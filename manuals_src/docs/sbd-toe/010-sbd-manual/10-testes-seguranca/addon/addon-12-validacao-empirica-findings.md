---
id: validacao-empirica-findings
title: Framework de Validação Empírica de Findings de Testes
description: Framework para testar exploitabilidade real de findings, documentar falsos positivos/negativos com evidência reproduzível
tags: [I2, evidência empírica, exploração, false positives, false negatives, PoC, testing]
---

# 🔬 Framework de Validação Empírica de Findings de Testes

## 🌟 Objetivo

Implementar **Invariante I2 (Evidência Acima de Plausibilidade)** de agent.md no contexto de testes de segurança aplicacional.

Ferramentas de teste (SAST, DAST, IAST, fuzzing) reportam findings baseados em **padrões heurísticos**, não em **exploração empírica**.

**Problemas observados:**
- **Falsos Positivos (FP):** Ferramenta reporta SQL injection mas query é parametrizada (detector triggered por string concatenation em contexto seguro)
- **Falsos Negativos (FN):** SAST não deteta XSS em template engine dinâmico, vulnerabilidade explorada em produção
- **Findings plausíveis mas não-exploitáveis:** DAST reporta "IDOR possível" mas autorização bloqueia todos os testes
- **Falta de evidência:** "É vulnerável?" → "Ferramenta disse que sim" (não há PoC, não há teste de exploração)

Este addon prescreve **framework de validação empírica** que:
1. Define taxonomia T1-T5 de tipos de findings por ferramenta
2. Prescreve procedimentos de teste de exploração para cada tipo
3. Define templates de documentação de FP (Template S1) e FN (Template S2)
4. Estabelece métricas de qualidade (FP rate, FN rate, time-to-validation)
5. Integra validação empírica no workflow de decisão (addon-11)

---

## 🎯 Contexto normativo

**Risco de não-conformidade com I2:**
- Equipas bloqueiam pipelines por FP (SQL injection em log statement, XSS em dead code)
- Vulnerabilidades reais não-detectadas explodem em produção (FN)
- Decisions de ACEITAR-RISCO baseadas em "achismo" ("parece seguro") sem teste empírico
- Ferramentas não são otimizadas (FP rate >50%, equipas ignoram alertas)
- Auditoria rejeita evidência ("where is the proof?")

**Consequências observadas:**
- L1/L2: Fadiga de alertas (FP excessivos), equipas desativam scanners
- L3: Vulnerabilidade CRITICAL não-detectada por SAST, exploited in production, breach GDPR
- Compliance: Auditor exige "empirical evidence of exploitability" — não existe

---

## 📋 Taxonomia T1-T5 — Tipos de Findings por Ferramenta

### T1: SAST Findings (Análise Estática)

**Características:**
- Deteta padrões no código-fonte sem executar aplicação
- Alta taxa de FP (30-50%) em configurações default
- Não valida runtime context (autenticação, autorização, input validation)

**Exemplos comuns:**
- SQL Injection (string concatenation em queries)
- XSS (output sem encoding)
- Path Traversal (user input em file paths)
- Hardcoded secrets (passwords em código)
- Insecure crypto (MD5, DES, weak keys)

**Validação empírica necessária:**
- ✅ CRITICAL/HIGH: Testar exploração em staging (confirmar que payload funciona)
- ✅ L3: Todos findings ≥MEDIUM requerem teste manual
- ❌ L1: Opcional (aceitar output de ferramenta)

---

### T2: DAST Findings (Análise Dinâmica)

**Características:**
- Testa aplicação em execução (black-box)
- Envia payloads maliciosos e analisa respostas
- FP rate moderado (15-30%), mas pode gerar muitos "informativos"

**Exemplos comuns:**
- SQL Injection (payload: `' OR 1=1--`)
- XSS (payload: `<script>alert(1)</script>`)
- IDOR (tentar aceder a `/api/users/456` sem autorização)
- Authentication bypass (tentar aceder a `/admin` sem login)
- SSRF (payload: `http://169.254.169.254/latest/meta-data/`)

**Validação empírica necessária:**
- ✅ CRITICAL/HIGH: Confirmar exploração com payloads mais sofisticados (não apenas payload básico da ferramenta)
- ✅ L3: Testar bypasses (WAF evasion, encoding variations)
- ❌ L1/L2: Aceitar findings HIGH+ sem revalidação

---

### T3: IAST Findings (Análise Interativa)

**Características:**
- Instrumenta aplicação (agent no runtime)
- Deteta vulnerabilidades durante testes funcionais
- FP rate baixo (5-15%), mas FN rate pode ser elevado se cobertura de testes é baixa

**Exemplos comuns:**
- SQL Injection detetado durante teste funcional (agent vê query com input não-sanitizado)
- XSS detetado em output rendering
- Command Injection em system call
- Deserialization vulnerabilities

**Validação empírica necessária:**
- ✅ CRITICAL: Revalidar com PoC manual (IAST pode detectar mas não testar full exploit)
- ⚠️ HIGH/MEDIUM: Opcional se IAST tem alta confiança (confidence score ≥80%)
- ❌ L1: Aceitar findings sem revalidação

---

### T4: Fuzzing Findings

**Características:**
- Envia inputs aleatórios/semi-aleatórios para quebrar aplicação
- Deteta crashes, exceptions, comportamento inesperado
- FP rate muito baixo (<5%), mas findings requerem triagem (nem todo crash é vulnerabilidade)

**Exemplos comuns:**
- Buffer overflow (crash com input grande)
- Null pointer dereference
- Regex DoS (ReDoS)
- Integer overflow
- Unhandled exceptions revelando stack traces

**Validação empírica necessária:**
- ✅ Todos findings: Reproduzir crash, analisar root cause, confirmar se é exploitável (crash ≠ vulnerabilidade)
- ✅ L3: Desenvolver PoC completo para crashes que podem levar a RCE

---

### T5: Pentesting Findings (Teste Manual Ofensivo)

**Características:**
- Pentester humano testa aplicação com criatividade e contexto
- FP rate muito baixo (<5%), findings são geralmente reais
- Cobre lógica de negócio, race conditions, fluxos complexos

**Exemplos comuns:**
- Business logic flaws (ex: negative price, duplicate transactions)
- Race conditions (ex: double-spend, concurrent session hijacking)
- Authentication bypasses não-óbvios (ex: session fixation via subdomain)
- Authorization bypasses complexos (ex: IDOR via indirect reference)

**Validação empírica necessária:**
- ✅ CRITICAL/HIGH: Reproduzir com PoC documentado (pentester deve fornecer)
- ⚠️ MEDIUM/LOW: Opcional se pentester fornece evidência clara
- ❌ Geralmente não requer revalidação (pentester já testou empiricamente)

---

## 🧪 Procedimentos de Teste de Exploração

### Procedimento T1 — SAST Findings

**Objetivo:** Confirmar se padrão de código detectado é exploitável no contexto real.

**Passo 1: Análise de Code Path**
```bash
# Exemplo: SAST reporta SQL injection em src/api/users.ts:142
# Confirmar se código é reachable

# 1. Verificar call graph (quem chama esta função?)
grep -r "getUserById" src/
# Resultado: Chamada em 3 endpoints: GET /api/users/:id, POST /api/admin/users, GET /api/reports

# 2. Verificar se endpoints estão expostos
curl https://staging.example.com/api/users/123
# Se retorna 200 → endpoint público, código é reachable
# Se retorna 404 → código pode estar em dead code
```

**Passo 2: Análise de Input Validation**
```bash
# Verificar se input é validado antes de chegar ao código vulnerável
grep -A 10 -B 10 "getUserById" src/api/users.ts

# Exemplo de código:
# function getUserById(id: string) {
#   const query = `SELECT * FROM users WHERE id = ${id}`; // SAST deteta aqui
#   return db.query(query);
# }

# Verificar se existe validação upstream:
grep -B 20 "getUserById" src/api/users.ts | grep -E "(validate|sanitize|parseInt)"

# Se não existe validação → vulnerabilidade real
# Se existe validação (ex: parseInt(id)) → pode ser FP
```

**Passo 3: Teste de Exploração em Staging**
```bash
# Enviar payload SQL injection
curl "https://staging.example.com/api/users/123' OR 1=1--"

# Analisar resposta:
# - Retorna todos os users? → Vulnerabilidade confirmada
# - Retorna erro 500 "Invalid input"? → Validação bloqueia (FP ou mitigado)
# - Retorna erro 400 "Bad request"? → WAF bloqueia (mitigado, mas código ainda vulnerável)
```

**Passo 4: Documentar Resultado**
```markdown
# Validação Empírica — SAST-2026-01-16-001

**Finding:** SQL Injection em src/api/users.ts:142
**Ferramenta:** Semgrep SAST

**Teste 1: Code Path Analysis**
- Resultado: ✅ Código é reachable via GET /api/users/:id (endpoint público)

**Teste 2: Input Validation**
- Resultado: ❌ Nenhuma validação detectada upstream
- Código: `const query = \`SELECT * FROM users WHERE id = ${id}\`;` (string concatenation)

**Teste 3: Exploração em Staging**
- Payload: `123' OR 1=1--`
- Resultado: ✅ Retorna todos os users (1.234 registos), vulnerabilidade confirmada
- Evidência: Screenshot + HTTP response (anexo: screenshot-001.png)

**Conclusão: VULNERABILIDADE REAL (não é FP)**
**Decisão:** CORRIGIR-IMEDIATO (parametrized query)
```

---

### Procedimento T2 — DAST Findings

**Objetivo:** Confirmar se finding reportado por DAST é exploitável com payloads mais sofisticados.

**Passo 1: Reproduzir Finding da Ferramenta**
```bash
# DAST reporta XSS em GET /search?q=
# Payload usado pela ferramenta: <script>alert(1)</script>

curl "https://staging.example.com/search?q=<script>alert(1)</script>"

# Analisar resposta:
# - HTML contém <script>alert(1)</script> sem encoding? → Vulnerabilidade confirmada
# - HTML contém &lt;script&gt;alert(1)&lt;/script&gt;? → Output encoding correto (FP)
# - WAF bloqueia com 403? → Mitigado, mas código pode estar vulnerável
```

**Passo 2: Testar Bypasses (se WAF bloqueia)**
```bash
# Testar encoding variations
curl "https://staging.example.com/search?q=%3Cscript%3Ealert(1)%3C/script%3E"
curl "https://staging.example.com/search?q=<scr<script>ipt>alert(1)</script>"
curl "https://staging.example.com/search?q=<img src=x onerror=alert(1)>"

# Se algum bypass funciona → vulnerabilidade real, WAF é insuficiente
# Se todos bloqueados → mitigado (mas código ainda vulnerável, decisão: CORRIGIR-PLANEJADO)
```

**Passo 3: Testar Contextos Alternativos**
```bash
# XSS pode existir em outros contextos (JSON, JavaScript, HTML attribute)
curl "https://staging.example.com/search?q=\"-alert(1)-\"" # JSON context
curl "https://staging.example.com/search?q=' onmouseover='alert(1)" # HTML attribute

# Testar com ferramenta especializada
dalfox url "https://staging.example.com/search?q=FUZZ"
```

**Passo 4: Documentar Resultado**
```markdown
# Validação Empírica — DAST-2026-01-16-042

**Finding:** XSS Refletido em GET /search?q=
**Ferramenta:** OWASP ZAP DAST

**Teste 1: Reprodução de Payload Básico**
- Payload: `<script>alert(1)</script>`
- Resultado: ❌ WAF bloqueia com 403 Forbidden

**Teste 2: Bypass WAF**
- Payload 1: `<img src=x onerror=alert(1)>` → ❌ Bloqueado
- Payload 2: `<svg/onload=alert(1)>` → ❌ Bloqueado
- Payload 3: `<iframe src=javascript:alert(1)>` → ✅ Passou WAF, XSS confirmado
- Evidência: Screenshot (anexo: xss-bypass-iframe.png)

**Teste 3: Análise de Código**
- Código: `<h1>Search results for: ${req.query.q}</h1>` (template literal sem encoding)
- Conclusão: Código está vulnerável, WAF é bypassable

**Conclusão: VULNERABILIDADE REAL (WAF insuficiente)**
**Decisão:** CORRIGIR-IMEDIATO (output encoding) + Melhorar WAF rule
```

---

### Procedimento T3 — IAST Findings

**Objetivo:** Validar findings de IAST com PoC manual (IAST deteta mas não explora).

**Passo 1: Analisar Stack Trace de IAST**
```json
// IAST report
{
  "finding_id": "IAST-2026-01-16-099",
  "type": "SQL Injection",
  "confidence": 85,
  "location": "src/database/queries.js:56",
  "stack_trace": [
    "executeQuery (queries.js:56)",
    "getUserByEmail (users.js:142)",
    "login (auth.controller.js:89)",
    "POST /api/auth/login"
  ],
  "tainted_input": "req.body.email",
  "sink": "db.query(sql)"
}
```

**Passo 2: Reproduzir com PoC Manual**
```bash
# IAST detetou SQL injection em POST /api/auth/login
# Testar com payload real

curl -X POST https://staging.example.com/api/auth/login \
  -H "Content-Type: application/json" \
  -d '{"email": "admin@example.com\" OR 1=1--", "password": "dummy"}'

# Analisar resposta:
# - Login bem-sucedido sem password correto? → SQL injection confirmado
# - Erro "Invalid email format"? → Validação bloqueia (FP ou mitigado)
```

**Passo 3: Testar Exploração Completa**
```bash
# Testar extração de dados (SQL injection com UNION)
curl -X POST https://staging.example.com/api/auth/login \
  -H "Content-Type: application/json" \
  -d '{"email": "admin@example.com\" UNION SELECT null,password,null FROM users--", "password": "dummy"}'

# Se retorna passwords → SQL injection permite data exfiltration (CRITICAL)
```

**Passo 4: Documentar Resultado**
```markdown
# Validação Empírica — IAST-2026-01-16-099

**Finding:** SQL Injection em POST /api/auth/login
**Ferramenta:** Contrast IAST
**Confidence Score:** 85%

**Teste 1: Reprodução de Detecção**
- Payload: `admin@example.com" OR 1=1--`
- Resultado: ✅ Login bem-sucedido sem password (vulnerabilidade confirmada)

**Teste 2: Exploração Completa (Data Exfiltration)**
- Payload: `admin@example.com" UNION SELECT null,password,null FROM users--`
- Resultado: ✅ Retorna hash de passwords de todos os users
- Evidência: HTTP response (anexo: sqli-data-exfiltration.json)

**Conclusão: VULNERABILIDADE CRITICAL (data exfiltration confirmada)**
**Decisão:** CORRIGIR-IMEDIATO (parametrized query + rate limiting)
```

---

### Procedimento T4 — Fuzzing Findings

**Objetivo:** Analisar crashes/exceptions de fuzzing, confirmar se são exploitáveis.

**Passo 1: Reproduzir Crash**
```bash
# Fuzzer reporta crash com input específico
# Input: GET /api/parse?data=AAAAAA...(10000 A's)

# Reproduzir localmente
curl "https://staging.example.com/api/parse?data=$(python3 -c 'print("A"*10000)')"

# Analisar logs:
# - Exception "OutOfMemoryError"? → DoS confirmado
# - Crash com segfault? → Possível buffer overflow (RCE?)
# - Exception handled gracefully? → Não é vulnerabilidade (apenas edge case)
```

**Passo 2: Root Cause Analysis**
```bash
# Analisar código para identificar causa do crash
grep -A 20 "/api/parse" src/

# Exemplo:
# function parseData(data: string) {
#   const buffer = Buffer.alloc(1024); // Buffer fixo de 1KB
#   buffer.write(data); // Sem validação de tamanho → buffer overflow
# }

# Confirmar vulnerabilidade: Input >1024 bytes causa overflow
```

**Passo 3: Testar Exploitabilidade**
```bash
# Buffer overflow pode levar a RCE?
# Testar com payloads de exploit development

# Payload com shellcode (exemplo simplificado)
curl "https://staging.example.com/api/parse?data=$(python3 exploit.py)"

# Se consegue executar código → CRITICAL (RCE)
# Se apenas crash/DoS → HIGH (DoS)
# Se exception handled → LOW (edge case)
```

**Passo 4: Documentar Resultado**
```markdown
# Validação Empírica — FUZZ-2026-01-16-234

**Finding:** Crash com input >10000 bytes em GET /api/parse
**Ferramenta:** AFL Fuzzer

**Teste 1: Reprodução de Crash**
- Input: 10.000 caracteres 'A'
- Resultado: ✅ Exception "OutOfMemoryError", serviço reinicia

**Teste 2: Root Cause Analysis**
- Código: `Buffer.alloc(1024)` com `buffer.write(data)` sem validação
- Conclusão: Buffer overflow quando input >1KB

**Teste 3: Exploitabilidade**
- Tentativa de RCE: ❌ Node.js managed memory impede RCE
- Resultado: DoS confirmado (serviço reinicia, downtime de 5s)

**Conclusão: VULNERABILIDADE HIGH (DoS exploitável)**
**Decisão:** CORRIGIR-IMEDIATO (validar tamanho de input, max 1KB)
```

---

### Procedimento T5 — Pentesting Findings

**Objetivo:** Reproduzir findings de pentesting com PoC fornecido, validar severidade.

**Passo 1: Analisar Relatório de Pentesting**
```markdown
# Pentesting Report — Finding PT-2026-01-15-007

**Title:** IDOR in User Profile API
**Severity:** HIGH
**Description:** Endpoint GET /api/users/:id returns user profile without authorization check. Authenticated user can access any user's profile by changing :id parameter.

**PoC:**
1. Login as user A (id=123)
2. Get auth token: `Authorization: Bearer eyJhbGc...`
3. Request GET /api/users/456 with token
4. Response: User B's profile (email, phone, address)

**Impact:** Privacy breach, GDPR violation
```

**Passo 2: Reproduzir PoC**
```bash
# Login as user A
curl -X POST https://staging.example.com/api/auth/login \
  -d '{"email": "userA@example.com", "password": "password123"}' \
  | jq -r '.token'
# Token: eyJhbGc...

# Tentar aceder ao perfil de user B (id=456)
curl https://staging.example.com/api/users/456 \
  -H "Authorization: Bearer eyJhbGc..."

# Resultado esperado (vulnerável): Retorna perfil de user B
# Resultado seguro: 403 Forbidden "Not authorized"
```

**Passo 3: Validar Severidade**
```bash
# Confirmar dados sensíveis expostos
# Resposta:
{
  "id": 456,
  "email": "userB@example.com", # PII
  "phone": "+351912345678",     # PII
  "address": "Rua X, Lisboa",   # PII
  "ssn": "123456789"            # CRITICAL PII
}

# Severidade confirmada: HIGH → CRITICAL (SSN exposto)
```

**Passo 4: Documentar Resultado**
```markdown
# Validação Empírica — PT-2026-01-15-007

**Finding:** IDOR in GET /api/users/:id
**Pentester:** João Martins (external pentest)

**Teste 1: Reprodução de PoC**
- Resultado: ✅ IDOR confirmado, user A acede a perfil de user B

**Teste 2: Análise de Dados Expostos**
- Dados: Email, phone, address, **SSN** (PII crítico)
- Conclusão: Impacto maior que reportado (SSN não foi mencionado em relatório)

**Severidade ajustada: HIGH → CRITICAL**

**Conclusão: VULNERABILIDADE CRITICAL (GDPR breach)**
**Decisão:** CORRIGIR-IMEDIATO (adicionar authorization check)
```

---

## 📋 Template S1 — Supressão de False Positive

```markdown
# Supressão de False Positive — FP-2026-01-16-001

**Finding Original:**
- Finding ID: SAST-2026-01-16-123
- Ferramenta: SonarQube
- Severidade: HIGH
- Tipo: SQL Injection
- Localização: src/logging/audit.ts:89
- Descrição: String concatenation em SQL query

**Análise Técnica:**

**Razão do False Positive:**
Ferramenta deteta string concatenation em query SQL:
```typescript
const sql = `INSERT INTO audit_logs (timestamp, message) VALUES (${Date.now()}, '${sanitize(message)}')`;
db.execute(sql);
```

**Por que é FP:**
1. **Timestamp não é user input:** `Date.now()` retorna integer, não pode conter SQL injection
2. **Message é sanitizado:** Função `sanitize()` faz escaping de caracteres especiais (', ", \)
3. **Validação empírica:** Teste com payloads SQL injection confirmou que escaping funciona
   - Payload: `'; DROP TABLE users--` → Escapado para `\'; DROP TABLE users--`
   - Resultado: Query insere literal string, não executa comando SQL

**Evidência:**
- Código da função `sanitize()`: [link para código](src/utils/sanitize.ts)
- Teste de exploração: [anexo: fp-test-sqli.md]
- Screenshot de query executada: [anexo: query-log.png]

**Decisão: SUPRIMIR (False Positive)**

**Ação de Supressão:**
```typescript
// nosemgrep: sql-injection
// Justificação: Date.now() é integer, message é sanitizado com sanitize()
// Ver: FP-2026-01-16-001
const sql = `INSERT INTO audit_logs (timestamp, message) VALUES (${Date.now()}, '${sanitize(message)}')`;
```

**Aprovação:**
- Developer: João Silva (2026-01-16)
- AppSec Engineer: Maria Costa (2026-01-16)

**Revisão periódica:** 2026-07-16 (6 meses)
```

---

## 📋 Template S2 — Root Cause Analysis de False Negative

```markdown
# False Negative RCA — FN-2026-01-18-001

**Incidente:**
- Data: 2026-01-18
- Tipo: XSS explorado em produção
- Impacto: 50 users tiveram sessões hijacked, 3 contas comprometidas
- CVE: N/A (vulnerabilidade interna)

**Vulnerabilidade:**
- Localização: src/templates/search-results.ejs:34
- Código vulnerável:
```html
<h2>Search results for: <%= query %></h2>
```
- Tipo: XSS Refletido (user input em HTML sem encoding)

**Por que não foi detetado?**

**Ferramentas que falharam:**
1. **SAST (SonarQube):** ❌ Não deteta XSS em templates EJS (apenas em JavaScript)
2. **DAST (OWASP ZAP):** ❌ Endpoint /search não foi crawled (requer autenticação, scanner não tinha credenciais)
3. **IAST (Contrast):** ❌ Não estava instrumentado em staging (apenas em produção após incidente)

**Root Cause:**
- **SAST limitation:** Regras de SAST não cobrem template engines EJS (apenas Handlebars, Pug)
- **DAST configuration:** Scanner DAST não tinha credenciais de autenticação, não testou endpoints autenticados
- **IAST deployment:** IAST não estava deployado em staging, apenas habilitado em produção após incidente
- **Manual testing:** Não existia checklist de testes manuais para XSS em templates

**Correção Imediata:**
- PR #5678: Output encoding em EJS (`<%- escapeHtml(query) %>`)
- Deploy hotfix v2.1.1 em 2h após deteção
- Revalidação DAST: XSS não mais detetável

**Prevenção Futura:**

**1. Ajuste de SAST:**
- Adicionar regra custom para EJS templates:
```yaml
# semgrep rule
rules:
  - id: ejs-xss
    pattern: <%= $VAR %>
    message: "Potential XSS in EJS template. Use <%- escapeHtml($VAR) %>"
    severity: HIGH
```
- Validação: Regra deteta vulnerabilidade em código histórico ✅

**2. Ajuste de DAST:**
- Configurar credenciais de autenticação em scanner ZAP
- Adicionar endpoint /search ao scope explícito
- Validação: DAST agora testa endpoint /search ✅

**3. Deploy de IAST em Staging:**
- Instrumentar staging com Contrast agent
- Executar testes funcionais com IAST ativo
- Validação: IAST deteta XSS em testes funcionais ✅

**4. Teste Manual:**
- Adicionar checklist de XSS para templates:
  - [ ] Testar XSS em todos os parâmetros de query
  - [ ] Validar output encoding em EJS, Handlebars, Pug
  - [ ] Testar com payloads diversos (<script>, <img>, <svg>)

**5. Regressão Automatizada:**
```javascript
// test/security/xss.test.js
test('Search query must be HTML-encoded', async () => {
  const response = await request(app)
    .get('/search?query=<script>alert(1)</script>')
    .expect(200);
  
  // HTML must NOT contain unencoded <script> tag
  expect(response.text).not.toContain('<script>alert(1)</script>');
  expect(response.text).toContain('&lt;script&gt;alert(1)&lt;/script&gt;');
});
```

**Lições Aprendidas:**
- ❌ SAST não é suficiente para templates (limitação de cobertura)
- ❌ DAST sem autenticação não testa endpoints críticos
- ❌ IAST deve estar em staging, não apenas produção
- ✅ Validação empírica manual é essencial em L3
- ✅ Regressão automatizada previne reincidência

**Aprovação RCA:**
- AppSec Engineer: Maria Costa (2026-01-19)
- Tech Lead: Pedro Santos (2026-01-19)
- CISO: Ana Ferreira (2026-01-19)

**Follow-up:** 2026-02-19 (revisão de eficácia de medidas)
```

---

## 📊 Métricas de Qualidade

**Objetivo:** Monitorizar eficácia das ferramentas e processo de validação empírica.

### Métrica 1: Taxa de False Positives

**Definição:**
```
FP Rate = (Findings suprimidos como FP / Total findings reportados) × 100
```

**Meta:**
- L1: <30% (ferramentas podem ter mais FP)
- L2: <20%
- L3: <15% (ferramentas devem ser bem configuradas)

**Ação se meta não cumprida:**
- FP rate >30%: Reconfigurar ferramenta (ajustar regras, reducir sensibilidade)
- FP rate >50%: Substituir ferramenta (gera ruído excessivo, equipas ignoram alertas)

---

### Métrica 2: Taxa de False Negatives

**Definição:**
```
FN Rate = (Vulnerabilidades não-detetadas / Total vulnerabilidades reais) × 100
```

**Meta:**
- L1: <10% (aceitável ter alguns FN)
- L2: <5%
- L3: <2% (cobertura deve ser quase total)

**Como medir:**
- FN identificados por: Pentesting externo, incidentes de produção, testes manuais
- Total vulnerabilidades = FN identificados + Vulnerabilidades detetadas por ferramentas

**Ação se meta não cumprida:**
- FN rate >10%: Adicionar ferramenta complementar (ex: SAST + IAST + DAST)
- FN rate >15%: Reforçar validação manual (L3: obrigatória)

---

### Métrica 3: Tempo de Validação Empírica

**Definição:**
```
Time-to-Validation = Tempo desde finding reportado até validação empírica completa
```

**Meta:**
- CRITICAL: <2h (L3), <4h (L2), <8h (L1)
- HIGH: <4h (L3), <8h (L2), <24h (L1)
- MEDIUM: <8h (L3), <24h (L2), <48h (L1)

**Ação se meta não cumprida:**
- Adicionar recursos (mais AppSec Engineers)
- Automatizar testes de exploração (scripts de PoC)
- Priorizar findings por risco real (não apenas severidade reportada)

---

### Métrica 4: Cobertura de Validação Empírica

**Definição:**
```
Validation Coverage = (Findings com teste empírico / Total findings CRITICAL+HIGH) × 100
```

**Meta:**
- L1: >50% (testar pelo menos metade dos CRITICAL+HIGH)
- L2: >80%
- L3: 100% (todos CRITICAL+HIGH devem ser testados empiricamente)

**Ação se meta não cumprida:**
- <80% em L2/L3: Processo de validação não está a ser seguido → Training de equipas
- <50% em L1: Considerar aumentar maturidade para L2

---

### Métrica 5: Taxa de Confirmação de Vulnerabilidades

**Definição:**
```
Confirmation Rate = (Findings confirmados como vulnerabilidade real / Total findings validados) × 100
```

**Insight:**
- Confirmation rate alto (>80%): Ferramentas são precisas, poucos FP
- Confirmation rate baixo (<50%): Ferramentas reportam muitos FP, precisam ajuste

**Meta:**
- L1/L2/L3: >70% (70% dos findings testados são vulnerabilidades reais)

---

## ⚖️ Proporcionalidade L1–L3

| Nível | Validação Empírica Obrigatória? | Tipos de Findings | Templates S1/S2? | Métricas? |
|---|---|---|---|---|
| **L1** | CRITICAL apenas | T1 (SAST), T2 (DAST) | Recomendado | FP rate, FN rate (anual) |
| **L2** | CRITICAL + HIGH | T1, T2, T3 (IAST), T4 (Fuzzing) | Obrigatório | FP/FN rate, Time-to-Validation (mensal) |
| **L3** | CRITICAL + HIGH + MEDIUM | T1, T2, T3, T4, T5 (Pentesting) | Obrigatório | Todas métricas (semanal) |

---

## 🔗 Integração com Outros Capítulos

- **Cap 02 (Requisitos):** Validação empírica de requisitos críticos (addon-07 de Cap 02 já implementa I2)
- **Cap 06 (Desenvolvimento):** SAST findings seguem procedimento T1 (addon-12 de Cap 06)
- **Cap 07 (CI/CD):** Gates baseados em findings validados empiricamente
- **Cap 09 (Containers):** Scanner findings seguem procedimento similar (addon-12 de Cap 09)
- **Cap 10 (Testes):** Este addon é core para Cap 10
- **addon-11 (Decisão):** Validação empírica alimenta checklist C1.1 (exploitável?)

---

## 📎 Referências Cruzadas

| Documento | Relação |
|---|---|
| [addon-11: Framework de Decisão](./addon-11-decisao-findings-testes) | Validação empírica alimenta decisão (C1.1) |
| [addon-08: Gestão de Findings](./08-gestao-findings) | Findings validados são registados em plataforma |
| [US-10: Gestão Centralizada](../aplicacao-lifecycle#us-10) | Integração de validação empírica em workflow |
| [Cap 02 addon-07: Validação de Requisitos](../../02-requisitos-seguranca/addon/07-validacao-requisitos) | FP/FN management para requisitos |
| [agent.md: Invariante I2](https://github.com/your-org/agent-spec) | Fundamento normativo |

---

## 🔄 Revisão e Melhoria Contínua

**Triggers de revisão:**
- FN identificado em produção → RCA obrigatório (Template S2)
- FP rate >30% → Reconfiguração de ferramenta
- Incidente de segurança → Análise de por que ferramentas não detetaram

**Frequência de revisão:**
- Mensal (L2/L3): Análise de métricas FP/FN rate, ajuste de ferramentas
- Trimestral (L1): Revisão de Templates S1, validação de supressões
- Após incidentes: RCA obrigatório com Template S2

---

> 📌 Plausibilidade não é suficiente — evidência empírica é mandatória.  
> Ferramentas sugerem, humanos testam, vulnerabilidades são confirmadas com PoC reproduzível.
