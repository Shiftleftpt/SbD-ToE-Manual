---
id: validacao-manual-ameacas
title: Validação Manual de Ameaças — Empirismo vs. Plausibilidade
description: Garantir que ameaças sugeridas por ferramentas são validadas tecnicamente antes de implementação
tags: [addon, validacao-manual, i2, empirismo, testes-seguranca, ameacas]
---

# 🧪 Validação Manual de Ameaças — Empirismo vs. Plausibilidade

## 🎯 Objetivo

Este addon estabelece o **Invariante I2 (Evidência acima de Plausibilidade)** no contexto de Threat Modeling, garantindo que:

- **Ameaças não são aceites apenas porque "parecem plausíveis"** — Requerem validação técnica
- **Testes empíricos obrigatórios** para ameaças CRÍTICA/ALTA em L2/L3
- **Falsos positivos (FP) e Falsos Negativos (FN) são detectados e registados**
- **Qualidade da ferramenta é medida** (FP rate, FN rate, tempo de validação)

**Contexto normativo:**  
Este addon implementa o **Invariante I2 (Evidência acima de Plausibilidade)** de [agent.md](https://github.com/your-org/agent-spec). Complementa [addon-14](./14-validacao-ameacas-assistida) (I1 separação) e [addon-07](./07-mapeamento-threats-requisitos) (mapeamento threats→requisitos).

---

## 🚨 Cenários de Risco — Quando I2 é Violado

### Cenário 1: Ameaça "Plausível" Mas Falsa

**Exemplo crítico:**
```yaml
# Ferramenta: "SQL Injection em /api/search endpoint"
# Severidade: CRÍTICA
# DFD sugere: "User input → Database query"

# Realidade: Aplicação usa Sequelize ORM com prepared statements
# Input nunca é concatenado diretamente em SQL
# Teste: Manual SQL injection attempt → BLOQUEADO ✅

# Resultado: FALSO POSITIVO — ferramenta enganou
```

**Risco:**
- Desenvolvedor consome tempo implementando proteção contra falso positivo
- Confiança na ferramenta reduz (cry wolf effect)
- Recursos desviados para falsos positivos = menos testes de ameaças reais

---

### Cenário 2: Ameaça Real Não Detectada

**Exemplo crítico:**
```yaml
# Aplicação: Serviço de autenticação
# Ameaça real não detectada por ferramenta: "JWT expirado não é validado"
# Teste manual: Modifiquei JWT expirado, servidor aceitou ✅ VULNERÁVEL
# Ferramenta não sugeriu porque modelo DFD não incluía "validação de expiração"

# Resultado: FALSO NEGATIVO — ferramenta perdeu ameaça real
```

**Risco:**
- Vulnerabilidade real não é mitigada
- Descobre-se apenas em produção ou em test manual
- Impacto: Unauthorized access, session hijacking

---

### Cenário 3: Validação Incompleta

**Exemplo crítico:**
```yaml
# Ameaça: "Sensitive data exposure via logs"
# Ferramenta sugeriu: Ameaça real
# Decisor diz: "Logs estão em /var/log/app.log, protegido (permissões 600)"
# Validação realizada: NENHUMA (sem teste, sem evidence)

# Risco verdadeiro:
# - /var/log/app.log pode ser lido por root, container escape, etc.
# - Logs são enviados para ELK Stack (senha de database exposta em logs)
# - Validação empírica nunca foi feita

# Resultado: Ameaça aceite mas não realmente mitigada
```

---

## 🔐 Procedimento de Validação Manual — Framework I2

### Fase 1: Categorizar Ameaça por Tipo de Validação

**Entrada:** Ameaça aceita por I1 (addon-14) → Precisa validação empírica?

**Taxonomia de ameaças:**

| Categoria | Tipo de Ameaça | Validação Necessária | Teste Típico |
|---|---|---|---|
| **A: Input Validation** | SQL injection, command injection, XSS, XXE | ✅ TESTE MANUAL + SAST | Payload injection (sqlmap, XSStrike) |
| **B: Authentication/Session** | JWT bypass, session fixation, weak password policy | ✅ TESTE MANUAL + DAST | Modificar JWT, reuse sessionid, brute force |
| **C: Authorization** | IDOR, privilege escalation, broken access control | ✅ TESTE MANUAL + DAST | Aceder recurso de outro user, /admin sem role |
| **D: Cryptography** | Weak algorithm, small key size, hardcoded secrets | ✅ TESTE MANUAL + code review | Inspecionar certificados, key material, algorithms |
| **E: Data Protection** | Sensitive data in logs, plaintext storage, backup exposure | ✅ TESTE MANUAL + audit | Dump database, read logs, aceder backup |
| **F: Configuration** | Debug mode enabled, default credentials, open ports | ✅ TESTE AUTOMÁTICO + SAST | Scan ports, test default creds, check config files |

---

### Fase 2: Teste Empírico por Categoria

**Papéis:** QA Engineer ou AppSec Engineer (executor), AppSec Lead (validador)

**Para cada ameaça CRÍTICA/ALTA, executar teste correspondente:**

:::userstory
**História.**  
Como **AppSec Engineer**, quero **validar manualmente ameaça com teste técnico**, para confirmar que é real antes de exigir mitigação.

**Critérios de aceitação (BDD).**
- **Dado** que ameaça foi aceita em I1  
  **Quando** executo teste empírico  
  **Então** confirmo ou refuto se vulnerabilidade é real

**Checklist I2 — Validação Empírica por Categoria.**

#### **A. Input Validation (SQL Injection, XSS, Command Injection)**

```yaml
Ameaça: "SQL Injection em /api/search?q=<input>"
Validação:
  - [ ] Teste manual: curl "http://app/api/search?q='; DROP TABLE users; --"
    Resultado esperado: ERROR (query fails) ou OK (parameterized query, injection blocked)
    Evidência: Screenshot de erro ou SAST detects parameterized query
  - [ ] SAST (Semgrep, SonarQube): Deteta concatenação de SQL direto?
    Resultado: PASSING (query.execute(sql, [param])) ou FAILING (query.execute(sql + param))
  - [ ] DAST (OWASP ZAP): Tenta injeções automáticas
    Resultado: Vulnerável ou Seguro
```

#### **B. Authentication/Session (JWT Bypass, Session Fixation)**

```yaml
Ameaça: "JWT token com alg:none aceito pelo servidor"
Validação:
  - [ ] Teste manual: Criar JWT com alg:none e tentar acesso
    Comando: curl -H "Authorization: Bearer <jwt_none>" http://app/api/me
    Resultado esperado: 401 Unauthorized ou error
    Evidência: Response screenshot mostrando rejeição
  - [ ] Code review: Função de validação JWT verifica alg?
    Verificar: `if (header.alg === 'none') { reject() }`
  - [ ] SAST: Detecta hardcoded JWT secrets ou missing validation?
    Resultado: No findings (seguro) ou Critical (inseguro)
```

#### **C. Authorization (IDOR, Privilege Escalation)**

```yaml
Ameaça: "IDOR em /api/users/<id>/profile — Acesso a perfis de outros users"
Validação:
  - [ ] Teste manual: Login como User A, tentar GET /api/users/<id_user_b>/profile
    Resultado esperado: 403 Forbidden
    Evidência: Teste com 2 contas diferentes, screenshot de rejeição
  - [ ] DAST (Burp Suite): Teste de IDOR automático (compare responses)
    Resultado: Vulnerable (respostas diferentes) ou Secure (erro, ou mesmo dados anónimos)
  - [ ] Code review: Check se endpoint valida `currentUser.id == requestedUser.id`?
```

#### **D. Cryptography (Weak Algorithms, Small Keys)**

```yaml
Ameaça: "Certificado TLS com algoritmo SHA1 (deprecado)"
Validação:
  - [ ] Teste manual: openssl s_client -connect app:443 | grep "Signature Algorithm"
    Resultado esperado: sha256WithRSAEncryption
    Resultado inseguro: sha1WithRSAEncryption (rejeitado)
  - [ ] Code review: Verificar key size
    Comando: openssl x509 -in cert.pem -text | grep "Public-Key"
    Esperado: RSA 2048+ ou EC 256+
  - [ ] SAST (cryptographic checks): Detecta weak keys ou algorithms?
```

#### **E. Data Protection (Sensitive Data in Logs, Plaintext Storage)**

```yaml
Ameaça: "Passwords armazenadas em plaintext na database"
Validação:
  - [ ] Teste manual: Dump da database, verificar coluna passwords
    SELECT user_id, password FROM users LIMIT 1;
    Resultado esperado: bcrypt hash (começa com $2y$) ou similar
    Resultado inseguro: plaintext ou MD5 (vulnerável)
  - [ ] Code review: Onde é hash gerado?
    Verificar: bcrypt.hash(password, 10) ou similar
  - [ ] Logs: Grep logs para PII exposure
    Comando: grep -r "password=" logs/ | head -10
    Resultado esperado: Nenhuma exposição
    Resultado inseguro: Passwords ou tokens em plaintext nos logs
```

#### **F. Configuration (Debug Mode, Default Credentials, Open Ports)**

```yaml
Ameaça: "Debug mode ativo (stack traces expostas)"
Validação:
  - [ ] Teste manual: Trigger error, ver se stack trace é exposto
    Teste: GET /api/invalid-endpoint
    Resultado esperado: Generic "500 Internal Server Error"
    Resultado inseguro: Stack trace com caminhos de arquivo, versões de libs
  - [ ] SAST: Detecta debug mode ativo em código?
    Procurar: DEBUG=true, logger.debug() exposed, etc.
  - [ ] Port scanning: nmap app.com -p 1-10000
    Resultado esperado: 2 ports open (80, 443)
    Resultado inseguro: 8080 (debug), 5432 (postgres direct access), 6379 (redis)
```

:::

---

### Fase 3: Registar Resultado — Validado ou Falso Positivo/Negativo

**Artefato:** `threat-model/validation-results/TM-GEN-XXX-validation.md`

```yaml
---
threat_id: TM-GEN-001
titulo: "JWT token com alg:none aceito"
data_teste: "2026-01-16"
executor_teste: "João QA Engineer"
validador: "Maria AppSec Engineer"

# Resultado
resultado: "VALIDADO" # [VALIDADO | FALSO_POSITIVO | FALSO_NEGATIVO]
evidencia: |
  **Teste manual:**
  1. Criei JWT com alg:none usando jwt.io
  2. Enviei: GET /api/me -H "Authorization: Bearer eyJhbGc..."
  3. Servidor respondeu: 401 Unauthorized ✅
  4. Conclusão: Aplicação rejeita JWT com alg:none
  
  **SAST (Semgrep):**
  - Função validateJWT em auth.ts linha 23 valida header.alg
  - Rejeita alg:none explicitamente
  - Resultado: PASSING ✅
  
  **Code Review:**
  - JWT validation implementado correto (asymmetric signature com RS256)
  - Nunca aceita alg:none
  
# Decisão pós-validação
decisao_final: "FALSO_POSITIVO" # Ameaça não existe, validação passou
risco_residual: "MUITO BAIXO"
acao: "Descartar ameaça, documentar FP para evitar sugestão futura"

# Se fosse VALIDADO:
# requisito_associado: "REQ-AUT-003"
# prazo_mitigacao: "2026-02-28"

# KPI
severidade_original: "CRÍTICA"
severidade_ajustada: "NENHUMA" # Se FP
tempo_validacao_horas: 2
metodo_validacao: "Manual teste + SAST + Code review"

---
```

---

### Fase 4: Gestão de Falsos Positivos e Falsos Negativos

#### **Falsos Positivos (FP) — Ameaça sugerida mas não existe**

**Procedimento:**
1. **Análise técnica** — Documentar por que é FP (controlo existe, configuração correta)
2. **Aprovação AppSec** — AppSec Lead valida análise
3. **Suppression em ferramenta** — Marcar em IriusRisk/SonarQube para não sugerir novamente
4. **Registro em catalog** — `threat-model/falsos-positivos/FP-TM-GEN-XXX.md`
5. **Revisão periódica** — 6 meses, reavaliar se FP continua válido

**Template FP:**
```markdown
# Falso Positivo — TM-GEN-XXX

## Descrição
Ferramenta sugeriu: "SQL Injection em /api/search"
Validação provou: Aplicação usa ORM com prepared statements, SQL injection é impossível

## Análise técnica
- ORM: Sequelize v6.21
- Função: `db.query('SELECT * FROM users WHERE name = ?', [searchTerm])`
- Prepared statement garante que searchTerm nunca é interpretado como código SQL
- Teste manual de injeção: `?q='; DROP TABLE users; --` → Sem efeito, tratado como string literal

## AppSec aprovação
Validado por: Maria AppSec Engineer, 2026-01-16
Conclusão: FP confirmado, sem risco real

## Suppression
- IriusRisk: Suppressed rule SQL-001 in /api/search endpoint
- Motivo: "ORM prevents SQL injection"
- Revisão: 2026-07-16 (6 meses)

```

#### **Falsos Negativos (FN) — Ameaça real não foi sugerida**

**Procedimento:**
1. **Registo de incidente** — Quem descobriu (teste manual, auditor, incident post-mortem)?
2. **Análise de causa raiz** — Por que ferramenta não detectou?
3. **Ação imediata** — PR crítico, mitigação manual até tool fix
4. **Ajuste de ferramenta** — Custom rule, update versão, ou documento limitação
5. **Validação contínua** — Adicionar à suite de testes

**Template FN:**
```markdown
# Falso Negativo — FN-2026-001

## Descrição
Vulnerabilidade descoberta: "JWT expirado não é validado em renovação"
Ameaça real, não detectada por ferramenta de threat modeling

## Como foi descoberto
- Teste manual de segurança em 2026-01-20
- QA Engineer tentou usar token expirado
- Servidor aceitou token expirado (vulnerabilidade)

## Análise de causa raiz
- Modelo DFD não incluía "token renewal endpoint" (/auth/refresh)
- Ferramenta não sugeriu ameaça porque endpoint não estava no modelo
- Gap: Documentação de arquitetura estava desatualizada

## Ação imediata
- PR crítico #1567 criado: "Add token expiration check"
- Fix: Função validateJWT agora checa `exp` claim
- Teste: Todos os endpoints com token expirado rejeitam (401)
- Mitigação temporal: Manual security tests até fix deployado

## Ajuste da ferramenta
- IriusRisk: Adicionar novo nó no DFD para /auth/refresh
- Custom rule (Semgrep): "JWT exp claim must be checked before use"
- Versão: IriusRisk atualizar para v2024.02 (melhor detecção de refresh tokens)

## Validação contínua
- Adicionar teste de segurança automatizado: "Expired JWT is rejected"
- Incluir em regression suite de CI/CD
- Próxima revisão: 2026-04-20 (validar se FN foi coberto)

```

---

## 📊 KPIs de Validação Manual — Qualidade de Ameaças

| KPI | Fórmula | Meta | Ação |
|---|---|---|---|
| **FP Rate** | (FP confirmados / Total ameaças sugeridas) × 100 | <15% | Se >30%: avaliar/trocar ferramenta |
| **FN Rate** | (FN descobertos / Total vulnerabilidades reais) × 100 | <5% | Se >10%: melhorar modelo DFD, adicionar custom rules |
| **Tempo validação** | Dias entre sugestão e decisão final | <5 dias (CRÍTICA) | Se >7 dias: gargalo de processo |
| **Validação coverage** | % ameaças CRÍTICA/ALTA com teste técnico | 100% (L2/L3) | Se <80%: bloquear release |
| **Teste methods diversity** | % ameaças testadas com >1 método (manual + SAST + DAST) | >70% | Se <50%: adicionar DAST/SAST tools |

**Decision thresholds:**
- **FP rate >30%** → Ferramenta gera ruído excessivo, considerar desativar ou trocar
- **FN rate >10%** → Ferramenta inadequada para cobertura de ameaças reais
- **Validação coverage <80%** → Cultura de "trusting ferramenta" vs. "verifying empirically"

---

## 📐 Proporcionalidade por Nível

| Aspecto | L1 | L2 | L3 |
|---|---|---|---|
| **Validação manual obrigatória?** | Recomendado (ameaças CRÍTICA) | Obrigatório (CRÍTICA, ALTA) | Obrigatório (todas) |
| **Tipos de teste** | Manual | Manual + SAST | Manual + SAST + DAST + Code Review |
| **Cobertura de ameaça** | ≥50% CRÍTICA | 100% CRÍTICA, ≥70% ALTA | 100% todas ameaças |
| **FP rate aceitável** | <30% | <20% | <15% |
| **FN rate aceitável** | <15% | <10% | <5% |
| **Tempo validação** | Flexível | <5 dias CRÍTICA | <2 dias CRÍTICA |

---

## ✅ Checklist de Implementação

- [ ] Taxonomia de ameaças (6 categorias) comunicada a equipa
- [ ] Ferramentas de teste disponíveis (Burp Suite, OWASP ZAP, Semgrep, sqlmap)
- [ ] Templates de validação criados por categoria (A-F)
- [ ] Dashboard de KPIs configurado (FP rate, FN rate, coverage %)
- [ ] Processo de escalação para FN (como reportar, RCA, fix tracking)
- [ ] Documentação: onde registar FP/FN e histórico
- [ ] Formação: QA Engineers e AppSec sabem testar cada categoria
- [ ] Integração CI/CD: Testes de segurança executam em cada commit
- [ ] SLA de validação definido e comunicado
- [ ] Revisão periódica de FP/FN (trimestral, avaliar qualidade ferramenta)

---

**Última atualização**: 2026-01-01  
**Versão do addon**: 1.0.0  
**Autores**: AppSec Team + QA Engineers + Arquitetos de Software  
**Aprovação**: [Nome do AppSec Lead/CISO] — [Data]
