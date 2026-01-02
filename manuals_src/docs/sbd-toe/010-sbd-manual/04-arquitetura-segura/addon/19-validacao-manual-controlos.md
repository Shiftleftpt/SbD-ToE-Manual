---
id: validacao-manual-controlos
title: Validação Manual de Controlos de Arquitetura — Empirismo vs. Plausibilidade
description: Garantir que controlos arquiteturais (rate limiting, circuit breakers) são validados tecnicamente antes de go-live
tags: [addon, validacao-manual, i2, empirismo, controlos-arquitetura, testes]
---

# 🧪 Validação Manual de Controlos de Arquitetura — Empirismo vs. Plausibilidade

## 🎯 Objetivo

Este addon estabelece o **Invariante I2 (Evidência acima de Plausibilidade)** no contexto de Arquitetura Segura, garantindo que:

- **Controlos não são aceites apenas porque "parecem adequados"** — Requerem validação técnica
- **Testes empíricos obrigatórios** para controlos CRÍTICOS em L2/L3
- **Falsos positivos (FP) e Falsos Negativos (FN) são detectados e registados**
- **Qualidade da implementação é medida** (FP rate, FN rate, tempo de validação)

**Contexto normativo:**  
Este addon implementa o **Invariante I2 (Evidência acima de Plausibilidade)** de [agent.md](https://github.com/your-org/agent-spec). Complementa [addon-18](./18-validacao-decisoes-arquitetura) (I1 separação) e [addon-05](./05-validacao) (validação de arquitetura).

---

## 🚨 Cenários de Risco — Quando I2 é Violado

### Cenário 1: Controlo "Plausível" Mas Não Testado

**Exemplo crítico:**
```yaml
# ADR-042: "API Gateway implementa rate limiting: 100 req/s per IP"
# Requisito: ARC-RL-001 v1.0
# Implementação: Configuração em nginx.conf
  limit_req_zone $binary_remote_addr zone=api_limit:10m rate=100r/s;
  
# Validação: <nenhuma>
# Teste de carga: <não executado>

# Realidade: Rate limiting não funciona em prod (configuração aplicada apenas a /api/v1, mas /api/v2 sem proteção)
```

**Risco:**
- Controlo especificado mas ineficaz
- Ataque DDoS passa porque `/api/v2` não tem rate limit
- Confiança falsa no controlo

---

### Cenário 2: Controlo Implementado com Falsos Positivos

**Exemplo crítico:**
```yaml
# ADR-055: "Circuit breaker protege serviço de DB outage"
# Implementação: Hystrix circuit breaker com threshold 50% error rate
# Problema: Threshold muito baixo, circuit abre durante deploy normal (5% errors por 2s = abre circuit)

# Resultado: Falso Positivo
# Impacto: Service indisponível mesmo com DB saudável
# Root cause: Circuit breaker mal configurado
```

**Risco:**
- Controlo gera mais problemas que resolve
- SLA degradado por falsos positivos
- Operações perde confiança no controlo

---

### Cenário 3: Controlo Ausente (Falso Negativo)

**Exemplo crítico:**
```yaml
# ADR-048: "mTLS entre microservices garante autenticação mútua"
# Documentação: "Istio service mesh configurado"
# Realidade: Istio instalado mas PeerAuthentication policy não aplicada
# Teste: curl de Service A → Service B sem certificado → SUCESSO ❌

# Resultado: Falso Negativo — controlo especificado mas não implementado
```

**Risco:**
- Lateral movement possível entre services
- Controlo documentado mas não eficaz

---

## 🔐 Procedimento de Validação Manual — Framework I2

### Fase 1: Categorizar Controlo por Tipo de Validação

**Entrada:** Controlo aceito por I1 (addon-18) → Precisa validação empírica?

**Taxonomia de controlos arquiteturais:**

| Categoria | Tipo de Controlo | Validação Necessária | Teste Típico |
|---|---|---|---|
| **A: Rate Limiting** | Limite de requests por IP/user/global | ✅ TESTE CARGA + logs | Curl 1000× rapidamente, verificar 429 |
| **B: Circuit Breaker** | Proteção contra cascading failures | ✅ TESTE CHAOS + observabilidade | Derrubar dependência, verificar fallback |
| **C: Authentication** | mTLS, API keys, OAuth flows | ✅ TESTE MANUAL + DAST | Tentar acesso sem credentials, com credentials inválidos |
| **D: Authorization** | RBAC, ABAC, policy enforcement | ✅ TESTE MANUAL + DAST | Tentar acessar endpoint restrito com role insuficiente |
| **E: Encryption in Transit** | TLS, mTLS entre services | ✅ TESTE MANUAL + scan | openssl s_client, verificar cipher suite |
| **F: Logging & Observability** | Correlation IDs, centralized logs | ✅ TESTE MANUAL + query | Gerar evento crítico, verificar se aparece em logs |
| **G: Isolation** | Network policies, namespaces | ✅ TESTE MANUAL + scan | Tentar lateral movement entre services |
| **H: Input Validation** | Schema validation, sanitização | ✅ TESTE MANUAL + fuzzing | Enviar payloads malformados, verificar rejeição |

---

### Fase 2: Teste Empírico por Categoria

**Papéis:** QA Engineer ou AppSec Engineer (executor), Arquiteto (validador)

**Para cada controlo CRÍTICO/ALTA, executar teste correspondente:**

:::userstory
**História.**  
Como **QA Engineer**, quero **validar empiricamente controlo de arquitetura com teste técnico**, para confirmar que funciona antes de go-live.

**Critérios de aceitação (BDD).**
- **Dado** que controlo foi especificado em ADR  
  **Quando** executo teste empírico  
  **Então** confirmo ou refuto se controlo é eficaz

**Checklist I2 — Validação Empírica por Categoria.**

#### **A. Rate Limiting (Limite de Requests)**

```yaml
Controlo: "API Gateway rate limit 100 req/s per IP"
Validação:
  - [ ] Teste de carga: ab -n 10000 -c 100 http://api.example.com/v1/resource
    Resultado esperado: Após 100 req, retorna 429 Too Many Requests
    Evidência: Screenshot de logs mostrando 429s
  - [ ] Teste de bypass: Trocar IP (proxy/VPN), verificar se reset contador
    Resultado: Cada IP tem contador independente
  - [ ] Logs: Verificar se rate limit events são logados
    Comando: grep "rate_limit_exceeded" logs/api-gateway.log
    Resultado esperado: Eventos registados com IP, timestamp, endpoint
```

#### **B. Circuit Breaker (Proteção Cascading Failures)**

```yaml
Controlo: "Circuit breaker protege Service A de DB outage"
Validação:
  - [ ] Teste chaos: Derrubar database container (docker stop postgres-db)
    Resultado esperado: Circuit abre após X errors, retorna fallback response
    Evidência: Logs "circuit_open" + metrics Prometheus
  - [ ] Half-open state: Aguardar timeout, verificar se circuit tenta reabrir
    Resultado esperado: Após 30s, circuit half-open, próximo request testa DB
  - [ ] False positive test: Trigger 5% errors (normal), verificar se circuit não abre
    Resultado esperado: Circuit permanece fechado (threshold = 50%)
  - [ ] Observabilidade: Dashboard Grafana mostra circuit state
```

#### **C. Authentication (mTLS, OAuth, API Keys)**

```yaml
Controlo: "mTLS entre Service A e Service B"
Validação:
  - [ ] Teste sem certificado: curl http://service-b/api/data (sem client cert)
    Resultado esperado: 401 Unauthorized ou TLS handshake failure
    Evidência: Response "client certificate required"
  - [ ] Teste com certificado inválido: curl --cert invalid.pem http://service-b/api/data
    Resultado esperado: TLS handshake failure
  - [ ] Teste com certificado válido: curl --cert client.pem --key client-key.pem https://service-b/api/data
    Resultado esperado: 200 OK
  - [ ] Scan TLS: openssl s_client -connect service-b:443 -showcerts
    Resultado esperado: Cipher suite forte (TLS 1.3, ECDHE-RSA-AES256-GCM-SHA384)
```

#### **D. Authorization (RBAC, Policy Enforcement)**

```yaml
Controlo: "RBAC: apenas role 'admin' pode DELETE /api/users"
Validação:
  - [ ] Teste role 'user': curl -X DELETE http://api/users/123 -H "Authorization: Bearer <user_token>"
    Resultado esperado: 403 Forbidden
    Evidência: Response "insufficient permissions"
  - [ ] Teste role 'admin': curl -X DELETE http://api/users/123 -H "Authorization: Bearer <admin_token>"
    Resultado esperado: 200 OK (user deleted)
  - [ ] Teste sem token: curl -X DELETE http://api/users/123
    Resultado esperado: 401 Unauthorized
  - [ ] DAST (Burp Suite): Teste de privilege escalation (user → admin)
```

#### **E. Encryption in Transit (TLS, mTLS)**

```yaml
Controlo: "TLS 1.3 obrigatório em API externa"
Validação:
  - [ ] Scan TLS: nmap --script ssl-enum-ciphers -p 443 api.example.com
    Resultado esperado: TLS 1.3, cipher suites fortes
    Resultado inseguro: TLS 1.0, SSLv3, cipher RC4
  - [ ] Teste downgrade: openssl s_client -tls1_2 -connect api.example.com:443
    Resultado esperado: TLS 1.2 rejeitado (se TLS 1.3 é obrigatório)
  - [ ] Certificate validation: openssl x509 -in cert.pem -text -noout
    Verificar: Subject, Issuer, Validity, Key size (≥2048)
```

#### **F. Logging & Observability (Correlation IDs, Centralized)**

```yaml
Controlo: "Todos os requests têm correlation ID em logs centralizados"
Validação:
  - [ ] Gerar request: curl http://api/resource -H "X-Correlation-ID: test-12345"
    Resultado esperado: Response inclui X-Correlation-ID header
  - [ ] Query logs: grep "test-12345" logs/api-service.log
    Resultado esperado: Todos os logs do request têm correlation_id=test-12345
  - [ ] Logs centralizados: Query ELK Stack: correlation_id:"test-12345"
    Resultado esperado: Logs de todos os services (API, DB, Auth) com mesmo ID
  - [ ] Evento crítico: Trigger 500 error, verificar se log inclui stack trace + correlation ID
```

#### **G. Isolation (Network Policies, Namespaces)**

```yaml
Controlo: "Network policy: Service A não pode aceder Service B (different namespace)"
Validação:
  - [ ] Teste lateral movement: kubectl exec -it pod-service-a -- curl http://service-b.namespace-b/api
    Resultado esperado: Connection timeout ou "Network policy denied"
    Evidência: kubectl logs pod-service-a | grep "connection refused"
  - [ ] Teste allowed connection: Service A → Service C (same namespace, allowed)
    Resultado esperado: 200 OK
  - [ ] Scan network: nmap -p 1-65535 <service-b-ip> (from Service A pod)
    Resultado esperado: All ports filtered (network policy blocks)
```

#### **H. Input Validation (Schema Validation, Sanitização)**

```yaml
Controlo: "API valida JSON schema antes de processar"
Validação:
  - [ ] Teste payload malformado: curl -X POST http://api/resource -d '{"name": 123}'
    Schema espera: {"name": "string"}
    Resultado esperado: 400 Bad Request "name must be string"
  - [ ] Teste payload com XSS: curl -X POST http://api/resource -d '{"name": "<script>alert(1)</script>"}'
    Resultado esperado: 400 Bad Request (sanitized) ou armazenado escapado
  - [ ] Fuzzing: wfuzz -z file,payloads.txt http://api/resource -d '{"name": "FUZZ"}'
    Resultado esperado: Todos payloads maliciosos rejeitados (400)
```

:::

---

### Fase 3: Registar Resultado — Validado ou Falso Positivo/Negativo

**Artefato:** `architecture/validation-results/CTRL-XXX-validation.md`

```yaml
---
control_id: CTRL-RL-001
titulo: "API Gateway rate limiting 100 req/s"
data_teste: "2026-01-16"
executor_teste: "João QA Engineer"
validador: "Maria Arquiteta"

# Resultado
resultado: "VALIDADO" # [VALIDADO | FALSO_POSITIVO | FALSO_NEGATIVO]
evidencia: |
  **Teste de carga:**
  1. Executei ab -n 10000 -c 100 http://api/v1/resource
  2. Após 100 requests, servidor retornou 429 Too Many Requests
  3. Logs confirmam: "rate_limit_exceeded ip=192.168.1.100"
  4. Conclusão: Rate limiting eficaz ✅
  
  **Teste de bypass:**
  - Tentei trocar IP (proxy), contador reset corretamente
  - Cada IP tem limite independente
  
  **Logs centralizados:**
  - Events registados em ELK Stack com severity=WARNING
  
# Decisão pós-validação
decisao_final: "VALIDADO"
risco_residual: "BAIXO"
acao: "Controlo eficaz, manter configuração"

# Se fosse FALSO_POSITIVO:
# problema: "Rate limit muito restritivo, bloqueia users legítimos"
# acao: "Aumentar threshold para 200 req/s"

# Se fosse FALSO_NEGATIVO:
# problema: "/api/v2 não tem rate limit (configuração missing)"
# acao: "PR crítico #789 para adicionar rate limit a /api/v2"

# KPI
severidade_original: "CRÍTICA"
tempo_validacao_horas: 3
metodo_validacao: "Load testing + log analysis + chaos testing"

---
```

---

### Fase 4: Gestão de Falsos Positivos e Falsos Negativos

#### **Falsos Positivos (FP) — Controlo bloqueia tráfego legítimo**

**Procedimento:**
1. **Análise técnica** — Documentar por que é FP (threshold muito baixo, false alarm)
2. **Aprovação Arquiteto** — Arquiteto valida análise
3. **Ajuste de configuração** — Tuning (ex: rate limit 100→200 req/s)
4. **Registro em catalog** — `architecture/falsos-positivos/FP-CTRL-XXX.md`
5. **Revisão periódica** — 6 meses, reavaliar se FP continua válido

**Template FP:**
```markdown
# Falso Positivo — CTRL-RL-001

## Descrição
Controlo: "Rate limiting 100 req/s"
Problema: Users legítimos bloqueados durante picos de carga (ex: Black Friday)

## Análise técnica
- Threshold 100 req/s muito restritivo para API pública
- Durante Black Friday, 200 req/s por user é normal
- Logs confirmam: 80% dos 429s foram false positives (users legítimos)

## Arquiteto aprovação
Validado por: Maria Arquiteta, 2026-01-17
Conclusão: FP confirmado, threshold precisa ajuste

## Ajuste
- Aumentar rate limit para 200 req/s
- Adicionar burst allowance (300 req/s por 10s)
- Monitorar durante próximo pico
- Revisão: 2026-07-17 (6 meses)
```

#### **Falsos Negativos (FN) — Controlo não implementado/eficaz**

**Procedimento:**
1. **Registo de incidente** — Quem descobriu (teste manual, incident post-mortem)?
2. **Análise de causa raiz** — Por que controlo não funciona?
3. **Ação imediata** — PR crítico, mitigação manual até fix
4. **Ajuste de configuração** — Corrigir implementação
5. **Validação contínua** — Adicionar à suite de testes

**Template FN:**
```markdown
# Falso Negativo — FN-2026-002

## Descrição
Controlo especificado: "mTLS entre Service A e Service B"
Realidade: mTLS não configurado, comunicação em HTTP plaintext

## Como foi descoberto
- Teste manual de segurança em 2026-01-20
- QA Engineer tentou curl HTTP (sem cert) → Sucesso ❌
- Esperava TLS handshake failure

## Análise de causa raiz
- Istio service mesh instalado mas PeerAuthentication policy não aplicada
- ConfigMap mTLS configurado mas não aplicado ao namespace correto
- Gap: Documentação de arquitetura não validada em prod

## Ação imediata
- PR crítico #890 criado: "Apply PeerAuthentication policy to namespace prod"
- Fix: kubectl apply -f peer-auth-strict.yaml
- Teste: Todos os requests HTTP rejeitados (connection refused) ✅
- Mitigação temporal: Network policy bloqueia HTTP port 80

## Ajuste de implementação
- Automatizar validação de mTLS em CI/CD
- Script: `validate-mtls.sh` testa comunicação service-to-service
- Teste de regressão: Adicionar a CI pipeline (daily)

## Validação contínua
- Adicionar teste de segurança automatizado: "mTLS enforcement check"
- Incluir em regression suite de CI/CD
- Próxima revisão: 2026-04-20 (validar se FN foi coberto)
```

---

## 📊 KPIs de Validação Manual — Qualidade de Controlos

| KPI | Fórmula | Meta | Ação |
|---|---|---|---|
| **FP Rate** | (FP confirmados / Total controlos) × 100 | <15% | Se >30%: tuning de configuração |
| **FN Rate** | (FN descobertos / Total controlos críticos) × 100 | <5% | Se >10%: melhorar validação CI/CD |
| **Tempo validação** | Dias entre especificação e validação | <7 dias (CRÍTICA) | Se >10 dias: gargalo de processo |
| **Validação coverage** | % controlos CRÍTICA/ALTA com teste técnico | 100% (L2/L3) | Se <80%: bloquear release |
| **Teste methods diversity** | % controlos testados com >1 método (load + chaos + manual) | >70% | Se <50%: adicionar ferramentas |

**Decision thresholds:**
- **FP rate >30%** → Configuração inadequada, tunning necessário
- **FN rate >10%** → Implementação inadequada, validação CI/CD insuficiente
- **Validação coverage <80%** → Cultura de "confiar" vs. "verificar"

---

## 📐 Proporcionalidade por Nível

| Aspecto | L1 | L2 | L3 |
|---|---|---|---|
| **Validação manual obrigatória?** | Recomendado (controlos CRÍTICA) | Obrigatório (CRÍTICA, ALTA) | Obrigatório (todas) |
| **Tipos de teste** | Manual | Manual + load testing | Manual + load + chaos + fuzzing |
| **Cobertura de controlo** | ≥50% CRÍTICA | 100% CRÍTICA, ≥70% ALTA | 100% todas controlos |
| **FP rate aceitável** | <30% | <20% | <15% |
| **FN rate aceitável** | <15% | <10% | <5% |
| **Tempo validação** | Flexível | <7 dias CRÍTICA | <5 dias CRÍTICA |

---

## ✅ Checklist de Implementação

- [ ] Taxonomia de controlos (8 categorias) comunicada a equipa
- [ ] Ferramentas de teste disponíveis (ab, curl, openssl, nmap, kubectl, wfuzz)
- [ ] Templates de validação criados por categoria (A-H)
- [ ] Dashboard de KPIs configurado (FP rate, FN rate, coverage %)
- [ ] Processo de escalação para FN (como reportar, RCA, fix tracking)
- [ ] Documentação: onde registar FP/FN e histórico
- [ ] Formação: QA Engineers e Arquitetos sabem testar cada categoria
- [ ] Integração CI/CD: Testes de controlos executam em cada deploy
- [ ] SLA de validação definido e comunicado
- [ ] Revisão periódica de FP/FN (trimestral, avaliar qualidade implementação)

---

**Última atualização**: 2026-01-01  
**Versão do addon**: 1.0.0  
**Autores**: QA Engineers + Arquitetos de Software + AppSec Team  
**Aprovação**: [Nome do Arquiteto Lead/CISO] — [Data]
