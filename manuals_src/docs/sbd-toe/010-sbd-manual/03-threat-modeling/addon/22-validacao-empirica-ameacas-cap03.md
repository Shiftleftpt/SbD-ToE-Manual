---
id: addon-22-validacao-empirica-ameacas
title: "🧪 Addon-22 — Validação Empírica de Ameaças (I4: Empirical Validation)"
description: Framework de testes técnicos para confirmar existência de ameaças antes de exigir mitigação
tags: [I4, validacao-empirica, threat-modeling, SAST, DAST, testes, evidencia]
---

# 🧪 Addon-22 — Validação Empírica de Ameaças (I4)

## 🎯 Objetivo

Instituir um **framework de validação técnica** para confirmar se ameaças identificadas em threat modeling são **reais (VALIDADAS)**, **falsos positivos** ou **falsos negativos**, usando uma combinação de testes manuais, SAST, DAST e code review.

Este addon implementa a **Framework I4** (Empirical Validation and Evidence) para Cap 03, complementando:
- **US-05**: Validação manual e empírica de ameaças
- **Rastreabilidade**: Ligação entre ameaça → teste → evidência

---

## 📋 Problema e Contexto

### Problema
- ✗ Ameaças "plausíveis" são aceites sem validação técnica
- ✗ Ferramentas sugerem ameaças sem confirmação de exposição real
- ✗ Falsos positivos multiplicam-se, criando fadiga
- ✗ Falsos negativos (ameaças reais não detetadas) comprometem segurança
- ✗ Sem evidência técnica, é impossível priorizar mitigação

### Contexto (Proporcionalidade)

| Nível | Ameaças Validadas | Métodos | Cobertura |
|-------|-------------------|---------|-----------|
| **L1** | Opcional | Manual | ≥50% CRÍTICA |
| **L2** | Obrigatório | Manual + SAST | 100% CRÍTICA, ≥70% ALTA |
| **L3** | Obrigatório | Manual + SAST + DAST | 100% todas (multi-método) |

---

## 🧩 Estrutura: 6 Categorias de Ameaças + Métodos de Validação

### Fase 1: Categorizar Ameaça por Tipo de Validação

Antes de selecionar testes, classificar a ameaça:

```yaml
# threat-model/validation-roadmap/TM-GEN-XXX-validation-plan.md

threat_id: "TM-GEN-042"
title: "JWT com alg:none permite falsificação de sessão"
category: "A_Input_Validation"  # ← Determina métodos

# Mapa de categorias e métodos:
# A_Input_Validation: SAST (semgrep), Manual code review, DAST (fuzzing)
# B_Authentication: SAST (password rules), Manual test (bypass), DAST (brute force)
# C_Authorization: SAST (permission checks), Manual code review, DAST (privilege escalation)
# D_Cryptography: SAST (weak crypto), Manual code review, DAST (crypto attacks)
# E_Data_Handling: SAST (secrets), Manual code review, DAST (data exfiltration)
# F_Configuration: Manual review, DAST (misconfig detection)
```

**Mapa de Categorias e Métodos:**

| Categoria | Exemplo de Ameaça | SAST | Manual | DAST | Code Review |
|-----------|------|------|--------|------|-------------|
| **A — Input Validation** | SQL Injection, XSS, CSV Injection | ✅ Semgrep, SonarQube | ✅ Payload test | ✅ OWASP ZAP, Burp | ✅ Padrões |
| **B — Authentication** | Weak passwords, JWT bypass, Session fixation | ✅ Strength rules | ✅ Credential test | ✅ Brute force | ✅ Token handling |
| **C — Authorization** | Privilege escalation, IDOR, ACL bypass | ✅ Permission logic | ✅ Escalation test | ✅ Privilege check | ✅ RBAC logic |
| **D — Cryptography** | Weak crypto, hardcoded secrets, key exposure | ✅ Crypto libs | ✅ Key management | ✅ Encryption check | ✅ Secret scanning |
| **E — Data Handling** | Data exfiltration, privacy leaks, PII exposure | ✅ Data flow | ✅ Data access | ✅ Data interception | ✅ Field masking |
| **F — Configuration** | Insecure defaults, exposed configs, debug enabled | Manual only | ✅ Config scan | ✅ Misconfig detection | ✅ Settings review |

---

## Fase 2: Teste Empírico por Categoria

### Categoria A: Input Validation

#### A1. SAST (Semgrep)

```bash
# Instalar Semgrep
pip install semgrep

# Correr rules de input validation
semgrep --config=p/owasp-top-ten --config=p/cwe-top-25 \
  --config=p/security-audit \
  src/

# Output esperado:
# ✅ VULN: SQL Injection padrão detectado em queries.ts:42
# ✅ VULN: XSS padrão detectado em templates.ts:105
# ❌ No findings (false negative → investigar manualmente)
```

#### A2. Teste Manual: SQL Injection

```python
# Teste: JWT com payload especial (simula bypass)
import requests
import json
from datetime import datetime

API_URL = "http://localhost:8000/api/search"
HEADERS = {"Authorization": "Bearer <test_jwt>"}

# Payload de teste: SQL injection clássico
payloads = [
    "' OR '1'='1",
    "admin' --",
    "1'; DROP TABLE users; --",
    "1' UNION SELECT * FROM secrets --",
]

results = []
for payload in payloads:
    response = requests.post(
        API_URL,
        json={"query": payload},
        headers=HEADERS
    )
    
    results.append({
        "payload": payload,
        "status_code": response.status_code,
        "response_time": response.elapsed.total_seconds(),
        "error_message": response.text[:100],
        "vulnerability_detected": "error" in response.text.lower() or response.status_code == 500
    })

# Análise: Se vulnerability_detected=True para algum payload → VALIDADO
# Se todos status_code=400 (bad request) → controlo funciona → MITIGADO
```

#### A3. DAST: OWASP ZAP Scan

```bash
# Configurar e correr ZAP contra API
docker run --rm \
  -v $(pwd)/reports:/zap/wrk \
  ghcr.io/zaproxy/zaproxy:latest \
  zap-baseline.py \
  -t http://localhost:8000 \
  -r zap-report.html

# Análise: Procurar por:
# - Input Validation issues
# - SQL Injection
# - XSS findings
```

**Resultado Esperado:**
```
Threat: TM-GEN-042 (JWT alg:none)
- SAST Result: ✅ FOUND (Semgrep detecou uso de `alg:none` bypass)
- Manual Result: ✅ VALIDATED (Payload JWT sem assinatura aceito)
- DAST Result: ✅ CONFIRMED (ZAP escalou privilégios com JWT falso)

Conclusion: 🔴 VALIDADO — Ameaça é real e crítica
```

---

### Categoria B: Authentication

#### B1. SAST: Verificar regras de senha/token

```bash
# Exemplo: Verificar JWT com alg:none
semgrep -e 'PyJWT.*decode.*options.*verify_signature.*false' src/
semgrep -e 'jwt.*alg.*=.*none' src/
```

#### B2. Teste Manual: JWT Bypass

```python
# Teste: JWT com alg:none
import jwt
import json
from base64 import urlsafe_b64encode

# Criar JWT com alg:none (vulnerável)
header = {"alg": "none", "typ": "JWT"}
payload = {"sub": "admin", "role": "admin"}

# Encoding manual (sem assinatura)
header_encoded = urlsafe_b64encode(json.dumps(header).encode()).decode().rstrip('=')
payload_encoded = urlsafe_b64encode(json.dumps(payload).encode()).decode().rstrip('=')
signature = ""

jwt_token = f"{header_encoded}.{payload_encoded}.{signature}"

# Tentar usar token
headers = {"Authorization": f"Bearer {jwt_token}"}
response = requests.get("http://localhost:8000/api/admin", headers=headers)

print(f"Status: {response.status_code}")
print(f"Result: {'VULNERABILITY' if response.status_code == 200 else 'PROTECTED'}")
```

#### B3. DAST: Força Bruta (se aplicável)

```bash
# Teste: Brute force em /login (throttling check)
hydra -l admin -P /usr/share/wordlists/rockyou.txt \
  -e nsr \
  localhost http-post-form \
  "/login:username=^USER^&password=^PASS^:Login failed" \
  -t 4 -w 1 2>&1 | head -20

# Resultado esperado:
# - Rate limiting ativo (após 5 tentativas, IP bloqueado) → MITIGADO
# - Rate limiting inativo (múltiplas tentativas bem-sucedidas) → VULNERÁVEL
```

---

### Categoria C: Authorization

#### C1. SAST: Procurar por IDOR patterns

```bash
# Procurar padrões comuns de IDOR
semgrep -e 'req.params.id.*req.user.id' src/  # IDOR típico
semgrep -e 'findById.*req.params' src/        # Sem validação RBAC
```

#### C2. Teste Manual: IDOR (Insecure Direct Object Reference)

```python
# Teste: Aceder a recurso de outro utilizador
# Cenário: User A tenta aceder a dados de User B

def test_idor():
    # User A: ID=100
    # User B: ID=101
    
    # Login como User A
    auth_a = requests.post("http://localhost:8000/login",
        json={"username": "user_a", "password": "pass_a"}
    ).json()
    
    token_a = auth_a["token"]
    headers_a = {"Authorization": f"Bearer {token_a}"}
    
    # Tentar aceder a /api/users/101 (dados de User B)
    response = requests.get(
        "http://localhost:8000/api/users/101",
        headers=headers_a
    )
    
    if response.status_code == 200:
        print("🔴 IDOR VULNERÁVEL: User A pode ver dados de User B")
        return "VALIDATED"
    elif response.status_code == 403:
        print("✅ PROTECTED: User A não consegue ver User B")
        return "MITIGATED"
```

---

### Categoria D: Cryptography

#### D1. SAST: Procurar por criptografia fraca

```bash
# Procurar libs criptográficas fracas
semgrep --config=p/crypto-usage src/
```

#### D2. Manual: Verificar gestão de chaves

```bash
# Checklist manual
✓ Secrets não estão hardcoded?
✓ Chaves são rotacionadas?
✓ TLS v1.2+ é obrigatório?
✓ Algoritmos fraco (MD5, SHA1) não são usados?
```

---

### Categoria E: Data Handling

#### E1. SAST: Data flow analysis

```bash
semprep --config=p/data-flow-leaks src/
```

#### E2. Manual: Verificar PII exposure

```python
# Teste: Procurar PII em responses
def test_pii_exposure():
    response = requests.get("http://localhost:8000/api/users/100")
    data = response.json()
    
    # PII patterns
    pii_patterns = {
        "ssn": r"\d{3}-\d{2}-\d{4}",  # SSN
        "cc": r"\d{4}[-\s]?\d{4}[-\s]?\d{4}[-\s]?\d{4}",  # Credit card
        "email": r"[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}",  # Email
        "phone": r"\+?1?\d{9,15}",  # Phone
    }
    
    for field, pattern in pii_patterns.items():
        for key, value in data.items():
            if isinstance(value, str) and re.search(pattern, value):
                print(f"🔴 PII LEAK: {field} found in {key}")
                return "VALIDATED"
    
    return "PROTECTED"
```

---

### Categoria F: Configuration

#### F1. Manual: Configuration Review

```bash
# Checklist: Configuração segura
- [ ] Debug mode is disabled
- [ ] Error messages don't leak stack traces
- [ ] Default credentials removed
- [ ] HTTPS enforced
- [ ] CORS properly scoped
- [ ] CSP headers set
- [ ] HSTS enabled
```

#### F2. DAST: Misconfig scanning

```bash
# Usar ferramenta como Lynis ou custom script
curl -I http://localhost:8000/ | grep -i "x-frame-options\|x-content-type\|strict-transport"
```

---

## Fase 3: Documentar Resultado

### Template de Relatório

```markdown
# threat-model/validation-results/TM-GEN-042-validation.md

---
threat_id: "TM-GEN-042"
title: "JWT com alg:none"
validation_date: "2025-01-20"
validated_by: "QA Engineer + AppSec"
---

## Test Execution Summary

### A1. SAST (Semgrep)
- **Executed**: 2025-01-20 10:30 UTC
- **Tool**: Semgrep v1.45.0
- **Config**: owasp-top-ten + cwe-top-25
- **Result**: ✅ **FOUND**
- **Finding**: `jwt_decoder_alg_none` in src/auth/jwt-handler.ts:42
- **Evidence**: [semgrep-report.json](./evidence/semgrep-report.json)

### B2. Manual Test (JWT Bypass)
- **Executed**: 2025-01-20 11:00 UTC
- **Method**: Manual JWT crafting with `alg:none`
- **Result**: ✅ **VALIDATED**
- **Evidence**:
  ```
  POST /api/admin
  Bearer eyJhbGciOiJub25lIn0.eyJyb2xlIjoiYWRtaW4ifQ.
  
  Response: 200 OK (unauthorized access granted)
  ```
- **Screenshot**: [jwt-bypass.png](./evidence/jwt-bypass.png)

### B3. DAST (Rate Limiting)
- **Executed**: 2025-01-20 11:30 UTC
- **Tool**: Custom Python script (see below)
- **Result**: ✅ **MITIGATED**
- **Finding**: Rate limiting active after 5 attempts
- **Evidence**: [dast-report.log](./evidence/dast-report.log)

## Overall Conclusion

| Finding | Status |
|---------|--------|
| SAST Detection | ✅ FOUND |
| Manual Validation | ✅ REAL VULNERABILITY |
| DAST Confirmation | ✅ CONFIRMED |

**Result**: 🔴 **VALIDATED** — Ameaça é real e crítica

---

## Recommended Actions

1. **Immediate**: Fix JWT validation (REQ-AUT-003)
2. **Evidence**: Attach this report to Jira issue
3. **Escalation**: Escalate to CISO if not fixed within 3 days
```

---

## Fase 4: Gestão de Falsos Positivos e Falsos Negativos

### Falso Positivo (FP)

**Definição**: Ameaça sugerida mas não existe em contexto real.

**Exemplo**:
```
Ferramenta detecta: "SQL Injection pattern"
Manual test result: Query é parametrizada, SQL injection impossível
Classification: FALSE POSITIVE
```

**Gestão**:
```markdown
# threat-model/false-positives/FP-TM-042.md

---
threat_id: "TM-GEN-042"
original_threat: "SQL Injection"
classification_date: "2025-01-20"
---

## Why It's a False Positive

- Ferramenta detectou padrão `str + query` sem contexto
- Realidade: query usa parametrização (prepared statements)
- Não existe exposição a SQL injection neste código

## Action

- [ ] Suppress FP em Semgrep: semgrep --suppress-errors
- [ ] Documento FP em backlog (não criar issue)
- [ ] Tool refinement: Adicionar contexto para evitar FP similar

## Prevention

- Adicionar rule customizado em Semgrep para ignorar prepared statements
```

### Falso Negativo (FN)

**Definição**: Ameaça real não foi detetada por ferramenta ou modelo inicial.

**Exemplo**:
```
Manual penetration test descobre: "Timing attack on password validation"
Ferramenta não detetou: SAST não cobre timing attacks
Classification: FALSE NEGATIVE
```

**Gestão**:
```markdown
# threat-model/false-negatives/FN-TM-050.md

---
threat_id: "TM-NEW-050" (criada retroativamente)
original_threat: "Timing attack on password validation"
discovery_date: "2025-01-21"
discovered_by: "Penetration Tester"
---

## Why It's a False Negative

- DFD não incluía análise de timing attacks
- Semgrep não cobre timing attacks (fora do escopo)
- Manual penetration test descobriu: response time varia com password length

## Severity & Impact

- **Criticality**: ALTA
- **Impact**: Attacker pode reduzir password space by 30%
- **Business Impact**: Admin account compromise possível

## Remediation

- [ ] Add timing-safe password comparison in auth service
- [ ] Create issue: [PROJ-XXXX] Implement constant-time validation
- [ ] Add to next threat model review
- [ ] Update DFD: Include timing attack vectors
- [ ] Improve SAST rules: Add custom semgrep rule for timing

## Learning

- Manual testing is essential (SAST gaps detected)
- Next DFD review: Include attack timing vectors
- Team training: Timing attack awareness
```

---

## Integração com CI/CD

### Automação de Testes

```yaml
# threat-model/validate-empirically.yml

name: Empirical Threat Validation

on:
  pull_request:
    paths:
      - 'src/**'
      - 'threat-model/validation-roadmap/**'

jobs:
  sast:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Run Semgrep
        run: |
          pip install semgrep
          semgrep --config=p/owasp-top-ten \
            --config=p/security-audit \
            --json \
            --output=semgrep-report.json \
            src/
      
      - name: Upload Semgrep findings
        uses: actions/upload-artifact@v3
        with:
          name: semgrep-report
          path: semgrep-report.json
      
      - name: Fail on critical findings
        run: |
          critical_count=$(jq '.results[] | select(.extra.severity=="CRITICAL") | .id' semgrep-report.json | wc -l)
          if [ $critical_count -gt 0 ]; then
            echo "❌ CRITICAL findings detected. Please fix before merge."
            exit 1
          fi
  
  manual-tests:
    runs-on: ubuntu-latest
    services:
      app:
        image: myapp:test
        ports:
          - 8000:8000
    
    steps:
      - uses: actions/checkout@v3
      
      - name: Setup test environment
        run: |
          pip install requests pytest
      
      - name: Run manual validation tests
        run: |
          python -m pytest tests/security/validation_tests.py -v
      
      - name: Generate evidence
        if: failure()
        run: |
          echo "Validation failures detected. See artifacts."
          exit 1
  
  dast:
    runs-on: ubuntu-latest
    services:
      app:
        image: myapp:test
    
    steps:
      - name: Run OWASP ZAP baseline
        run: |
          docker run --rm \
            -v $(pwd)/reports:/zap/wrk \
            ghcr.io/zaproxy/zaproxy:latest \
            zap-baseline.py \
            -t http://localhost:8000 \
            -r zap-report.html
      
      - name: Upload DAST report
        uses: actions/upload-artifact@v3
        with:
          name: zap-report
          path: reports/zap-report.html
```

---

## Métricas de Sucesso (I4)

### Indicadores

| Métrica | Meta | Como Medir |
|---------|------|-----------|
| % Ameaças validadas empiricamente | 100% CRÍTICA, ≥70% ALTA (L2/L3) | Count validated_results/*.md |
| Tempo médio validação | <5 dias CRÍTICA, <10 dias ALTA | Timestamp em validation files |
| FP rate | <15% | Count FP / total findings |
| FN rate | <5% | Count FN descobertos / trimestre |
| Evidence completeness | 100% | Reports + screenshots + logs |

### Dashboard

```
📊 Threat Validation Dashboard

├─ Total Threats: 42
├─ Validation Status:
│  ├─ 🔴 VALIDATED: 28 (67%)
│  ├─ 🟡 FALSE_POSITIVE: 10 (24%)
│  ├─ ⚫ FALSE_NEGATIVE: 1 (2%)
│  └─ ⏳ Pending: 3 (7%)
├─ Avg Validation Time: 4.1 days
├─ Evidence Quality: 100%
└─ Status: 🟢 Compliant
```

---

## 📚 Referências

| Recurso | Descrição |
|---------|-----------|
| OWASP Testing Guide | Metodologia de testes | [owasp.org/WSTG] |
| NIST SP 800-115 | Testing and Assessment Framework | [nist.gov] |
| Semgrep Docs | SAST tool documentation | [semgrep.dev] |
| OWASP ZAP | DAST automation | [zaproxy.org] |
| MITRE ATT&CK | Ameaças conhecidas e técnicas | [attack.mitre.org] |

---

## 🎯 Checklist de Implementação (I4)

- [ ] Categorias A-F mapeadas a ameaças existentes
- [ ] SAST pipeline (Semgrep) configurado
- [ ] Testes manuais implementados (6 categorias)
- [ ] DAST (OWASP ZAP) integrado em CI/CD
- [ ] Primeiras 10 ameaças validadas com relatório completo
- [ ] FP/FN processes documentadas
- [ ] Métricas integradas no dashboard
- [ ] Feedback da equipa de QA incorporado

---

**Versão**: 1.0  
**Última Atualização**: Jan 2025  
**Mantido por**: QA + AppSec Team  
