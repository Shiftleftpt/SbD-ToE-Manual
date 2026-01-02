# Addon 12: Framework de Validação Empírica de Deployment — Evidência acima de Plausibilidade

## Objetivo

Estabelecer procedimentos empíricos para validar que um deployment em produção é seguro, saudável e reversível, **sem confiar apenas em staging passing**. Este addon implementa o invariante I2 (Evidência acima de plausibilidade) no contexto operacional de deployment, garantindo que decisions sobre go-live (canary → GA) se baseiam em observação real de produção, não apenas extrapolação de staging.

## Problema

Staging validation pode passar completamente e produção falhar por razões que staging não reproduz:
- **Diferenças de infraestrutura:** Staging tem 1% da capacidade, produção tem 100% + autoscaling
- **Padrões de tráfego:** Staging tem tráfego sintético previsível, produção tem padrões caóticos
- **Dependências externas:** Staging usa stubs, produção usa APIs reais que podem estar lentas
- **Efeitos de escala:** Caching funciona bem em staging (todos os usuários são 10), mas falha em produção (10k usuários)
- **Fenômenos emergentes:** Race conditions, deadlocks, cascading failures não visíveis em staging

### Cenários de Risco

**Cenário 1 — Falso positivo (staging pass, production safe):**
- DAST em staging: Passou (0 críticas, 0 alerta de segurança)
- Deploy para produção com confiança
- 1h depois: Nada de extraordinário, métricas nominais
- **Problema:** Nenhum alarme tocou, confiança aumenta, mas como saber se staging estava representativo?

**Cenário 2 — Falso negativo (staging pass, production breaks):**
- Testes em staging: Latência média 50ms, erro rate < 0.5%, carga simulada 1k RPS
- Deploy para produção esperando performance similar
- 15 min depois: Latência spike para 2s, erro rate sobe para 5%, cascata de timeouts
- **Problema:** Staging não reproduziu pico de carga real (5k RPS), não capturou comportamento sob stress
- **Resposta:** Rollback executado em 4 min, mas 200 clientes já viram erros

**Cenário 3 — Smoke test incompleto:**
- Deployment iniciado, canary 1% ativo
- App health check passa (responds to /health), app inicia OK
- Mas: Dependência de database está Down (não mapeada em health check)
- Feature usa database, 100% de falha na canary, não notado por 10 minutos
- **Problema:** Health check é superficial, não testa happy path

**Cenário 4 — Monitorização cega:**
- Deploy em produção, canary 1% ativo
- Dashboards parecem OK (avg latência, avg erro rate)
- Mas: 5% dos usuários experenciam erro (tail latency de 95th percentile está em 5s)
- Não notado porque média é 200ms
- **Problema:** Monitorização não é granular, miss de anomalias em cauda

## Solução: Framework de Validação Empírica em 5 Categorias

### T1: Pre-Deploy Health Checks (Antes de Go-Live)

**Objetivo:** Verificação rápida de que infraestrutura crítica está respondendo (5-10 minutos antes de canary)

**Procedimento:**

```bash
# T1.1: Verificar conectividade de dependências principais
Verificações (execute cada uma, registre resultado):
  [ ] Database: Conexão + query simples (SELECT 1) responde em < 1 segundo
  [ ] Cache (Redis/Memcached): Conexão + SET + GET funciona, resposta < 100ms
  [ ] API externas: GET /health em cada API (pagamento, auth, etc) responde 200 OK
  [ ] Message queue: Produce + consume mensagem de teste, latência < 500ms
  [ ] File storage: Write + read arquivo de teste (10KB), latência < 1 segundo

# T1.2: Verificar alerting pipeline
  [ ] Logs estão fluindo para SIEM (últimas 5 entradas visíveis em console)
  [ ] Métricas estão sendo coletadas (Prometheus/Grafana mostra últimas entradas)
  [ ] Email/Slack alertas estão funcionando (teste: enviar alerta de teste, confirmar recebido em <1 min)

# T1.3: Verificar baseline de métricas pré-deploy
  [ ] Latência baseline em ambiente: Registre média atual (ex: p50=100ms, p99=300ms)
  [ ] Error rate baseline: Registre taxa atual (ex: 0.1%)
  [ ] CPU/Memory utilização: Registre baseline por servidor (ex: 35% CPU, 60% mem)
  [ ] Throughput (RPS): Registre taxa de requisições atual (ex: 500 RPS)

Saída T1: Tudo OK? Procede para Canary. Algo falhou? BLOCK—investigate antes de go-live.
```

**Responsável:** On-call engineer (5-10 min antes de canary)

**Template T1.1: Log Pré-Deploy**

```
Data: 15 Jan 2026, 10:50 AM
Versão: 2.4.1
Executado por: Bob (On-call)

T1.1 Conectividade:
  [ ✅ ] Database query responde 150ms
  [ ✅ ] Redis SET/GET responde 45ms
  [ ✅ ] Payment API /health 200 OK (130ms)
  [ ✅ ] Messaging SQS Put/Get 250ms
  [ ✅ ] S3 Write/Read 800ms (OK, slowish but normal)

T1.2 Alerting:
  [ ✅ ] Logs fluindo (tail -f SIEM mostra eventos live)
  [ ✅ ] Métricas visíveis (Grafana mostra últimas 10 data points)
  [ ✅ ] Alerta de teste enviado, Slack recebeu em 2s

T1.3 Baselines:
  Latência pré-deploy: p50=95ms, p99=280ms, p999=450ms
  Error rate pré-deploy: 0.12%
  CPU median: 32%, tail: 45%
  Memory median: 58%, tail: 72%
  Throughput: 520 RPS (nominal)

RESULTADO: ✅ GREEN—Procede para canary (11:00 AM)

Assinado: Bob [sig] 10:50 AM
```

---

### T2: Smoke Tests em Canary (1% Traffic, 15-30 minutos)

**Objetivo:** Executar happy-path funcional em canary (1% traffic) para validar que funcionalidade crítica funciona

**Procedimento:**

```bash
# T2.1: Iniciar canary (1% traffic)
Timestamp: [registro quando canary inicia]
Feature-flag: Ativar para 1% de usuários (ou 1% de tráfego por proxy)
Monitorização: Iniciaste dashboards de canary em background

# T2.2: Smoke tests funcionais (executar 5-10 happy-path scenarios)
Cada teste:
  1. Executar ação (ex: POST /user/login)
  2. Registrar latência (ex: 150ms)
  3. Registrar status (2xx / 4xx / 5xx)
  4. Repetir 5x, calcular média e desvio padrão

Teste 1 — Login:
  [ ] POST /auth/login (credentials válidas) → 200 OK
  [ ] Latência: 5 execuções: [130ms, 145ms, 125ms, 140ms, 135ms] → avg=135ms, σ=8ms
  [ ] Comparar com baseline pré-deploy (150ms): -10% (FASTER—ok, pode ser cache)
  [ ] Status: ✅ PASS

Teste 2 — Create resource:
  [ ] POST /api/v1/resource (payload válido) → 201 CREATED
  [ ] Latência: 5 execuções: [200ms, 210ms, 190ms, 205ms, 215ms] → avg=204ms, σ=10ms
  [ ] Baseline pré-deploy: 180ms. Atual: +12% (SLOWER—investigate, mas dentro de tolerância)
  [ ] Status: ✅ PASS

Teste 3 — Query resource:
  [ ] GET /api/v1/resource/123 → 200 OK
  [ ] Latência: 5 exec: [45ms, 48ms, 42ms, 46ms, 44ms] → avg=45ms, σ=2ms
  [ ] Baseline: 40ms. Atual: +12.5% (NORMAL)
  [ ] Status: ✅ PASS

Teste 4 — Logout:
  [ ] POST /auth/logout (valid session) → 200 OK
  [ ] Latência: 5 exec: [80ms, 78ms, 82ms, 79ms, 81ms] → avg=80ms, σ=1.6ms
  [ ] Baseline: 75ms. Atual: +6.7% (OK)
  [ ] Status: ✅ PASS

Teste 5 — Error handling (invalid input):
  [ ] POST /api/v1/resource (payload INVÁLIDO) → 400 BAD REQUEST
  [ ] Latência: 5 exec: [35ms, 36ms, 34ms, 37ms, 35ms] → avg=35.4ms
  [ ] Baseline: 30ms. Atual: +18% (OK, validation overhead expected)
  [ ] Status: ✅ PASS

# T2.3: Monitorização de canary (durante 15-30 min)
Registrar a cada 5 minutos:
  - Latência observada em canary: [p50, p99, p999]
  - Error rate em canary: [%, número de erros]
  - CPU/Memory de canary instances
  - Qualquer alerta acionado

Timeline exemplo:
  11:00 AM — Canary inicia, 1% traffic routed
  11:05 AM — Smoke tests completados, all PASS
  11:05-11:10 — Monitor canary: p50=100ms (+5% vs baseline 95ms—OK), error=0.08% (baseline 0.12%—BETTER!)
  11:10-11:15 — Monitor: p50=105ms, error=0.09%—nominal variation
  11:15-11:20 — Monitor: p50=98ms, error=0.11%—nominal, approaching baseline
  11:20-11:25 — Monitor: p50=102ms, error=0.10%—stable, canary healthy
  11:25-11:30 — Monitor: p50=100ms, error=0.09%—very stable, confidence high

# T2.4: Decisão canary → GA
Se latência/error rate em canary são within expected range:
  → APPROVE GA (ampliar feature-flag de 1% para 100%)
  
Se anomalia detected (ex: error spike, latency 2x):
  → Activate feature-flag kill-switch (manual or auto)
  → Rollback canary → Investigate
```

**Responsável:** On-call engineer + automated monitoring

**Template T2.2: Smoke Test Log**

```
Data: 15 Jan 2026, 11:00 AM
Versão: 2.4.1
Executado por: Bob (On-call)

CANARY INICIADO: 11:00 AM, 1% traffic routed via feature-flag

Smoke Tests Funcionais:

Test 1 — /auth/login:
  Execuções: 130ms, 145ms, 125ms, 140ms, 135ms
  Avg: 135ms, σ: 8ms
  Baseline pré-deploy: 150ms
  Resultado: ✅ PASS (-10% vs baseline, dentro de tolerância)

Test 2 — POST /api/v1/resource:
  Execuções: 200ms, 210ms, 190ms, 205ms, 215ms
  Avg: 204ms, σ: 10ms
  Baseline pré-deploy: 180ms
  Resultado: ✅ PASS (+12% vs baseline, aceitável)

Test 3 — GET /api/v1/resource:
  Execuções: 45ms, 48ms, 42ms, 46ms, 44ms
  Avg: 45ms, σ: 2ms
  Baseline pré-deploy: 40ms
  Resultado: ✅ PASS (+12.5%, normal)

Test 4 — /auth/logout:
  Execuções: 80ms, 78ms, 82ms, 79ms, 81ms
  Avg: 80ms, σ: 1.6ms
  Baseline pré-deploy: 75ms
  Resultado: ✅ PASS (+6.7%, OK)

Test 5 — Error handling:
  Execuções: 35ms, 36ms, 34ms, 37ms, 35ms
  Avg: 35.4ms, σ: 1.4ms
  Baseline pré-deploy: 30ms
  Resultado: ✅ PASS (+18%, validation overhead expected)

SÍNTESE SMOKE TESTS: ✅ ALL PASS

Monitorização de Canary (5-min snapshots):
  11:05 — p50=100ms (baseline 95ms, +5%), p99=290ms (baseline 280ms, +3.5%), error=0.08% (baseline 0.12%, BETTER)
  11:10 — p50=105ms, p99=305ms, error=0.09%
  11:15 — p50=98ms, p99=275ms, error=0.11%
  11:20 — p50=102ms, p99=300ms, error=0.10%
  11:25 — p50=100ms, p99=290ms, error=0.09%
  11:30 — p50=99ms, p99=285ms, error=0.08%

ANÁLISE:
  Latência canary está dentro de ±10% de baseline (OK)
  Error rate em canary está MELHOR que baseline (confidence UP)
  Nenhum alerta disparado
  Canary é estável e saudável por 30 min consecutivos

RESULTADO: ✅ GREEN—Aprovado para GA (ampliar para 100%)

Assinado: Bob [sig] 11:30 AM
```

---

### T3: Post-Deploy Health Validation (Imediatamente após GA)

**Objetivo:** Verificação imediata de que todas as instâncias estão saudáveis após go-live GA (100% traffic)

**Procedimento:**

```bash
# T3.1: Verificar all instances healthy (5 minutos após GA)
Health check:
  [ ] All app instances reporting healthy (HTTP 200 /health)
  [ ] No instances are crashing or restarting (zero restarts in last 5 min)
  [ ] Load balancer sees all instances as ACTIVE
  [ ] Database connections OK (no connection pool exhaustion)
  [ ] Cache utilization normal (no evictions)

# T3.2: Monitorar p50/p99 latência (10 minutos após GA)
Esperado: Latência não piora > 15% vs baseline pré-deploy
  [ ] p50 latência no range [baseline * 0.85, baseline * 1.15]
  [ ] p99 latência no range [baseline * 0.85, baseline * 1.15]
  [ ] p999 latência no range [baseline * 0.85, baseline * 1.2] (tail pode ter mais variação)
  
Exemplo:
  Baseline pré-deploy: p50=95ms, p99=280ms, p999=450ms
  5 min após GA: p50=100ms (✅ within range), p99=300ms (✅ OK), p999=480ms (✅ OK)

# T3.3: Monitorar error rate (10 minutos após GA)
Esperado: Error rate não aumenta > 2x baseline, ou absolute < 0.5%
  [ ] Error rate no range [0, min(baseline * 2, 0.5%)]
  
Exemplo:
  Baseline: 0.12%
  5 min após GA: 0.15% (✅ within range)
  10 min após GA: 0.11% (✅ OK, within range)

# T3.4: Verificar business metrics (15-20 minutos após GA)
  [ ] Transaction success rate: > 99.5% (ou baseline - 0.5%)
  [ ] User conversion funnel: No drop-off anomalies (step-by-step conversão rate)
  [ ] Revenue impact: No spike in refunds/chargebacks (monitor over 2-4h)

SAÍDA: Se tudo OK → Deployment validado, marca como "GA healthy". 
Se anomalia → Ativa rollback immediately.
```

**Responsável:** On-call engineer + automated monitoring

**Template T3.1: Post-GA Health Check**

```
Data: 15 Jan 2026, 11:35 AM (5 min após GA iniciado)
Versão: 2.4.1
Executado por: Bob (On-call)

GA INICIADO: 11:30 AM, feature-flag ampliado de 1% para 100%

T3.1 Instance Health:
  [ ✅ ] App instances (10 total):
    Server 1: healthy, 0 restarts, load 45%
    Server 2: healthy, 0 restarts, load 42%
    Server 3: healthy, 0 restarts, load 48%
    ... (7 mais, all healthy)
  [ ✅ ] Load balancer: All instances ACTIVE
  [ ✅ ] Database connections: 45/100 (normal)
  [ ✅ ] Cache hit rate: 87% (normal, was 88% baseline)

T3.2 Latência (10 min após GA, agregada últimas 10 min):
  p50: 102ms (baseline 95ms, +7.4%—✅ OK, within ±15%)
  p99: 305ms (baseline 280ms, +8.9%—✅ OK, within ±15%)
  p999: 485ms (baseline 450ms, +7.8%—✅ OK, within ±20%)

T3.3 Error Rate (10 min após GA):
  Current: 0.13% (baseline 0.12%)
  Δ: +0.01pp (✅ OK, within limits)
  Breakdown:
    - 4xx client errors: 0.08% (normal, same as baseline)
    - 5xx server errors: 0.05% (baseline 0.04%—slightly up, but <limit)

T3.4 Business Metrics (15 min após GA):
  [ ✅ ] Transaction success: 99.87% (baseline 99.85%, +0.02pp—excellent)
  [ ✅ ] Conversion funnel: No anomalies
    Step 1 (browse): 89.2% → Step 2 (add-to-cart): 42.1% (baseline 42.0%—✅)
    Step 2 → Step 3 (checkout): 87.3% (baseline 87.5%—-0.2pp, normal variation)
    Step 3 → Step 4 (complete): 98.1% (baseline 98.0%—✅)
  [ ✅ ] Revenue: $2,340 in last 15 min (on-pace for $10k/day, normal)

RESULTADO: ✅ GREEN—GA deployment is HEALTHY

CONCLUSÃO: 2.4.1 deployment validated in production. No anomalies. 
Proceed with monitoring (continue T5 below).

Assinado: Bob [sig] 11:35 AM
```

---

### T4: Rollback Verification (Teste de Rollback antes de Go-Live)

**Objetivo:** Verificar que rollback do deployment é possível, rápido (<5 min), e completo

**Procedimento:**

```bash
# T4.1: Executar rollback dry-run em staging (ANTES de canary, preferivelmente)
Objetivo: Validar que rollback procedure funciona
  [ ] Checkout versão anterior (N-1)
  [ ] Execute schema migration rollback (if any DB changes)
  [ ] Deploy N-1 to staging
  [ ] Verificar staging está saudável (health checks pass)
  [ ] Tempo total: Registre (target < 3 min em staging)

Exemplo (Staging):
  11:20 AM — Inicia rollback dry-run
  11:21 AM — Schema rollback completo (1 min)
  11:22 AM — App deploy N-1 (1 min)
  11:22:30 — Health checks pass, staging healthy
  11:23 AM — Rollback dry-run completo (3 min total)
  ✅ PASS: Rollback is possible, fast, and complete

# T4.2: Documentar rollback procedure em Produção
Procedure (a ser executado em produção if needed):
  Step 1: Disable feature-flag (1 min) — Routes 100% to old code
  Step 2: Database rollback (if needed) — Depends on schema change
    - If just code deploy: 0 min (feature-flag is sufficient)
    - If schema migration: Execute migration rollback (time varies)
  Step 3: Redeploy N-1 app (2-3 min)
  Step 4: Health checks (1 min)
  Total time: ~5 min (feature-flag routing) to ~10 min (if schema rollback)

# T4.3: Validar rollback trigger
Quem pode executar rollback?
  [ ] On-call engineer (Bob, Charlie) — can execute any time
  [ ] Escalation: Líder Técnico or CTO if on-call is unavailable
  
When to rollback?
  [ ] If error rate > 2% for > 5 min
  [ ] If latência p99 > baseline * 2 for > 5 min
  [ ] If any critical alerta (CRITICAL severity) triggered
  [ ] If business metric anomaly (ex: transaction success < 95%)

SAÍDA: Rollback é possível, documentado, e team sabe quando/como executar.
```

**Responsável:** Infrastructure/DevOps team (teste before canary)

**Template T4.1: Rollback Verification Log**

```
Data: 15 Jan 2026, 11:20 AM (dry-run em staging antes de canary)
Versão: 2.4.1 → Rollback para 2.4.0
Executado por: Bob (On-call) + Charlie (DevOps)

STAGING ROLLBACK DRY-RUN:

T4.1 Execute dry-run:
  11:20 AM — Initiate rollback procedure
  11:20:30 — Stop 2.4.1 instances in staging
  11:21:00 — Execute schema migration rollback (new table created in 2.4.1 is removed)
    - Migration script: DOWN_001_add_feature_table.sql
    - Duration: 30 seconds
    - Verification: Table "feature_data" is deleted, data preserved in backup
  11:21:30 — Start 2.4.0 instances with old app code
  11:22:00 — Instances started, health checks initiated
  11:22:20 — Health check /health → 200 OK
  11:22:25 — Health check /health → 200 OK (all instances healthy)
  11:22:30 — Database connections OK, cache OK, all services responding

  Total time: 2 min 30 sec (✅ within 3 min target)

T4.2 Validate rollback completeness:
  [ ✅ ] Feature from 2.4.1 is disabled (table dropped)
  [ ✅ ] Staging is fully functional on 2.4.0
  [ ✅ ] No data loss (backup intact)
  [ ✅ ] Performance nominal (latency ~95ms, error rate 0.12%)

T4.3 Production rollback procedure:
  Step 1: Disable feature-flag in 2.4.1 deployment (routes to 2.4.0) → 1 min
  Step 2: Execute schema migration rollback (same as staging) → 1 min
  Step 3: Redeploy 2.4.0 app container (if needed) → 2 min
  Step 4: Health checks + validation → 1 min
  Total estimated: 5 min (if feature-flag + code rollback)

T4.4 Rollback authorization:
  [ ✅ ] On-call: Bob, Charlie (authorized to execute without approval)
  [ ✅ ] Escalation: Alice (L2 Lead) if on-call unavailable
  [ ✅ ] Trigger: Automated alerta > CRITICAL or manual decision

RESULTADO: ✅ GREEN—Rollback is verified, documented, and team is trained

Assinado: Bob, Charlie [sig] 11:22 AM
```

---

### T5: Monitoring Validation (Continuous, 4h-24h post-GA)

**Objetivo:** Monitorar deployment continuously após GA para detectar anomalias latentes (que não aparecem nos primeiros 30 min)

**Procedimento:**

```bash
# T5.1: Verificar SIEM e logging está coletando dados
SIEM/Logging checks (continuous):
  [ ] Logs estão fluindo em tempo real (tail mostra eventos live)
  [ ] Log volume é normal (não há spike ou drop-off)
  [ ] Parsing está correto (fields extraídos corretamente)
  [ ] Alertas baseados em logs estão funcionando (ex: "5xx error spike")

# T5.2: Verificar Observability (Metrics, Traces, Logs)
Golden signals (monitor continuamente):
  [ ] Latência: p50, p99, p999 dentro de range esperado (±15% baseline)
  [ ] Traffic: RPS normal, não há drops ou spikes de >20%
  [ ] Errors: Error rate < baseline * 2, breakdown clear (4xx vs 5xx)
  [ ] Saturation: CPU, memory, disk < 80%, no resource exhaustion

# T5.3: Verificar dashboards e alertas
Dashboards:
  [ ] Main deployment dashboard mostra all green
  [ ] Business metrics dashboard mostra trends nominals
  [ ] Infrastructure dashboard mostra resource utilization normal
  
Alertas:
  [ ] High error rate alerta está ativo e testado
  [ ] High latência alerta está ativo
  [ ] Critical business metric alerta está ativo (ex: transaction success < 95%)
  [ ] Nenhum alerta crítico disparado (se disparou, investigar immediately)

# T5.4: Validar rollback readiness (continuous)
  [ ] Feature-flag kill-switch está pronto (can disable in < 1 min)
  [ ] Rollback procedure é still valid (no schema changes since GA)
  [ ] On-call team é contactable (phone/Slack active)

SAÍDA: Monitorização contínua garante que deployment continua saudável por 4-24h.
Sem anomalias detectadas após esse período → Deploy é "produção-stable".
```

**Responsável:** On-call engineer + automated dashboards

**Template T5.1: Monitoring Validation (4h post-GA)**

```
Data: 15 Jan 2026, 15:30 (4h após GA iniciado)
Versão: 2.4.1
Executado por: Bob (On-call, observou dashboards continuamente)

T5.1 SIEM / Logging:
  [ ✅ ] Logs fluindo: tail -f mostra 50+ events/sec (normal)
  [ ✅ ] Volume estável: 10.2M logs em últimas 4h (avg 2.5M/h—normal)
  [ ✅ ] Parsing OK: All fields extraídos corretamente
  [ ✅ ] Alertas: "5xx spike" alerta não disparou (error rate stable)

T5.2 Golden Signals (última 4h):
  Latência:
    p50: 99ms (baseline 95ms, +4%—✅)
    p99: 295ms (baseline 280ms, +5%—✅)
    p999: 475ms (baseline 450ms, +5.5%—✅)
  Traffic:
    Avg RPS: 515 RPS (baseline 500 RPS, +3%—✅ normal growth)
    Peak RPS: 620 RPS (1 min, at 12:45 PM—within expected)
  Errors:
    Error rate: 0.14% (baseline 0.12%, +0.02pp—✅)
    4xx: 0.09% (client errors)
    5xx: 0.05% (server errors, slightly up from 0.04%, but OK)
  Saturation:
    CPU: 42% median, 58% peak (baseline 40%/50%—✅)
    Memory: 62% median, 74% peak (baseline 60%/72%—✅)
    Disk: 35% (normal, well below 80%)

T5.3 Dashboards & Alertes:
  [ ✅ ] Main deployment dashboard: All GREEN
  [ ✅ ] Business metrics: Conversion rate 87.5% (baseline 87.4%—✅)
  [ ✅ ] Infrastructure: All resources normal
  [ ✅ ] Alertes: No critical alerts triggered (one minor "5xx dip" at 13:42, auto-recovered)

T5.4 Rollback Readiness:
  [ ✅ ] Feature-flag kill-switch: Ready, tested at 13:15 (disabled/enabled in 30s)
  [ ✅ ] Rollback procedure: Still valid, no new schema changes since GA
  [ ✅ ] On-call team: Bob online, Slack responsive, phone reachable

ANÁLISE (4h post-GA):
  Deployment 2.4.1 está SAUDÁVEL e ESTÁVEL
  Todas as métricas dentro de range esperado
  Nenhuma anomalia latente detectada
  Confiança ALTA na stability de 2.4.1

PRÓXIMOS PASSOS:
  - Continuar monitorando por mais 20h (até total de 24h post-GA)
  - Alice (L2 Lead) fará revisão final a 15:30 AM amanhã (24h post-GA)
  - Se nada acontecer em 24h, deploy 2.4.1 é "production-stable"
  - Feature-flag pode ficar ativado permanentemente ou ser removido em 2.4.2

ASSINADO: Bob [sig] 15:30 PM
```

---

## Falsos Positivos & Negativos: Handling

### Falso Positivo (S1): Staging Pass, Production Safe, Nada Aconteceu

**Cenário:** Todas as validações T1-T5 passam, nenhuma anomalia, 24h post-GA deployment está perfeitamente saudável.

**Pergunta:** Como sabemos se staging foi representativo, ou deployment só foi "lucky"?

**Procedimento S1:**

```markdown
## Template S1 — Análise de Falso Positivo (ou "Lucky Deployment")

Data: 16 Jan 2026, 15:30 (24h após GA)
Versão: 2.4.1 (been production-stable for 24h)

### Questões para Documentar

Q1: O staging era representative da produção em termos de dados e carga?
  [ ] Sim: Staging had > 80% of production data schema and patterns
  [ ] Parcial: Staging tinha ~50% de coverage, alguns padrões missing
  [ ] Não: Staging era synthetic, production data patterns unknown

Q2: Que testes foram executados em staging vs produção?
  Staging: [lista]
  Produção T1-T5: [lista]
  Diferenças: [o que foi diferente]

Q3: Houve anomalias esperadas que não se materializaram?
  [ ] Nenhuma: Tudo funcionou como esperado
  [ ] Menores: Latência era 5% mais alta (expected), error rate menor (good luck)
  [ ] Maiores: [alguma anomalia significante não se materializou]

### Conclusões

Se staging foi representative e não há diferenças significantes entre T1-T5 e staging:
  ✅ Não é falso positivo, staging foi valid + deployment foi bom

Se staging era synthetic ou tinham diferenças:
  ⚠️ Deployment pode ter sido lucky—aumentar rigor de staging para próxima iteração
  - Action: [Expandir staging data, adicionar padrões missing, aumentar carga simulada]

### Learning (Retrospectiva)

Para próxima release 2.4.2:
  - Staging data: [Se era synthetic, tornar mais realistic]
  - Staging load: [Se era baixo, aumentar para 50% de production peak]
  - T1-T5 rigor: [Se algo ficou faltando, adicionar checks]
  - Feature-flag: [Kill-switch manual deve virar automático baseado em alerta]

Assinado: Alice (L2 Lead), Bob (On-call) [sig] 16 Jan, 15:30
```

---

### Falso Negativo (S2): Production Anomalies Not Caught in Staging

**Cenário:** Staging validation passou, deployment passou T1-T4, mas em T5 (ou no dia seguinte) uma anomalia emerges que staging não capturou.

**Exemplos reais:**
- Staging: Latência 50ms
- Produção: Latência 500ms (10x slower—why?)
  - Causa: Prod database replica é mais lenta que staging
  - Staging não testa contra replica
- Staging: 0 errors em 1h synthetic test
- Produção: 2% error rate after 2h de real traffic
  - Causa: Race condition em alta concorrência
  - Staging não simula 5k concurrent users

**Procedimento S2:**

```markdown
## Template S2 — Análise de Falso Negativo (Production Anomaly Not in Staging)

Data: 16 Jan 2026, 03:45 (12h após GA)
Versão: 2.4.1

### Anomalia Detectada

Métrica: Latência p99
Observado em staging: 280ms
Observado em produção (T5): 900ms
Diferença: 3.2x (CRITICAL—rollback necessário)

Tempo de detecção: 5h após GA (via automated alerta de latência high)
Ação: Feature-flag kill-switch ativado em 2 min, rollback iniciado

### Root Cause Analysis (RCA)

Questão 1: Por que a anomalia não foi capturada em staging?
  Causa identificada: Staging database replica é em-memory (fast), 
                     produção replica está em remote region (slow, 200ms latency)
  Staging config: DB_REPLICA_MODE=in_memory
  Produção config: DB_REPLICA_MODE=remote_async

Questão 2: O código em 2.4.1 causa problema, ou infra?
  Análise: 2.4.1 adicionou 3 chamadas a DB replica (feature-flag checks)
           Em-memory replica: 3 * 1ms = 3ms overhead (not visible)
           Remote replica: 3 * 200ms = 600ms overhead (CRITICAL)
  Conclusão: Código assumiu replica era fast (como em staging)

Questão 3: Como isso passou em code review?
  Review note: "Replica calls are optimized" (mas didn't test on remote replica)

### Remediação

Immediate (já feito):
  [ ✅ ] Feature-flag kill-switch ativado, rollback to 2.4.0 em 2 min
  [ ✅ ] Produção restored: Latência back to 280ms, error rate normal
  [ ✅ ] RCA iniciado, findings documentados

Short-term (próximos dias):
  [ ] Fix código 2.4.1: Cache replica results, reduce calls from 3 to 1
  [ ] Fix staging: Setup remote replica simulator to match production
  [ ] Fix testing: Add latency injection (remote replica = +200ms delay)

Medium-term (próximo sprint):
  [ ] Staging infrastructure: Mirror produção mais closely (remote replica real)
  [ ] Integration testing: Test contra replica, não just main DB
  [ ] Load testing: Incluir latência de remote calls

### Learning (Retrospectiva)

Gaps identificados:
  1. Staging infra não era representative (missing remote replica effect)
  2. Code review não perguntou "como isso escala com remote calls?"
  3. T5 (Monitoring Validation) capturou bem (latência alerta em 5 min)—bom!

Melhorias para 2.4.2:
  [ ] Staging será setup com remote replica simulator
  [ ] Code review terá checklist: "Does this scale with network latency?"
  [ ] T1-T5 terão "latency injection" teste (simulate remote replica)
  [ ] Canary será aumentado para 5% (maior probabilidade de catching issues)

Assinado: Alice (L2 Lead), Bob (On-call), DevOps [sig] 16 Jan, 04:00
```

---

## Qualidade Metrics (Validação T1-T5)

| Métrica | Alvo L1 | Alvo L2 | Alvo L3 | Propósito |
|---|---|---|---|---|
| **Pre-Deploy Health Check (T1)** | — | — | — | |
| T1 health checks passing | 100% | 100% | 100% | Crítico: if fails, block go-live |
| T1 execution time | < 30 min | < 15 min | < 10 min | Velocidade de pré-validação |
| **Smoke Tests in Canary (T2)** | — | — | — | |
| Canary health (p50 latência) | ±20% baseline | ±15% baseline | ±10% baseline | Detecção rápida de regressão |
| Canary health (error rate) | < 2x baseline | < 1.5x baseline | < 1.2x baseline | Tolerância menor para L3 (maior confiança) |
| Canary duration before GA | 30 min | 20 min | 10 min | L3 pode ir mais rápido (mais testado) |
| **Post-Deploy Health (T3)** | — | — | — | |
| Post-GA latência (p50) | ±20% baseline | ±15% baseline | ±10% baseline | Sem regressão após GA |
| Post-GA error rate | < 1% absolute | < 0.5% absolute | < 0.3% absolute | Threshold mais rigoroso para L3 |
| Post-GA business success | > 95% | > 98% | > 99% | Business continuity metric |
| **Rollback Verification (T4)** | — | — | — | |
| Rollback execution time | < 15 min | < 10 min | < 5 min | L3 apps change more frequently, faster rollback required |
| Rollback success rate | > 95% | > 98% | > 99% | Must be reliable |
| **Monitoring Validation (T5)** | — | — | — | |
| Monitoring uptime | > 99% | > 99.5% | > 99.9% | Must detect issues |
| Alerta latency (issue → detection) | < 5 min | < 2 min | < 1 min | Faster response for L3 |
| Dashboard uptime | > 95% | > 98% | > 99% | Visibility is critical |

---

## Implementação Checklist

- [ ] **T1 Procedure:** Documentar pré-deploy health checks, listar dependências críticas
- [ ] **T2 Procedure:** Criar smoke test scripts (5-10 happy paths), parametrizar latência tolerância
- [ ] **T3 Procedure:** Configurar dashboards (latência, error rate, business metrics), alertas
- [ ] **T4 Procedure:** Testar rollback dry-run em staging, documentar steps em produção
- [ ] **T5 Procedure:** Continuous monitoring setup, SLA definitions, on-call escalation
- [ ] **S1 Template:** Documentar quando "falso positivo" ocorre, learning session
- [ ] **S2 Template:** RCA procedure para when production anomalies appear
- [ ] **Métricas:** Setup tracking de T1-T5 quality metrics, monthly review
- [ ] **Training:** Treinar on-call engineers em T1-T5, templates S1/S2

---

## Referências

- **NIST SSDF PO.5:** Production readiness, deployment validation
- **OWASP SAMM** (PO): Production operations, monitoring
- **SLSA Framework:** Framework integrity L2/L3 (deployment security)
- **Observability:** Golden Signals (latência, traffic, errors, saturation)

