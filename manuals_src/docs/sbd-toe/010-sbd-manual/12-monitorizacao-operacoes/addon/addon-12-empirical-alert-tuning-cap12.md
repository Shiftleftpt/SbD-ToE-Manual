# Addon 12: Framework de Tuning Empírico de Alertas — Evidência acima de Plausibilidade

## Objetivo

Estabelecer procedimentos empíricos para validar que alertas **detectam ameaças reais**, não apenas disparam baseado em thresholds estáticos. Este addon implementa o invariante I2 (Evidência acima de plausibilidade) no contexto operacional de monitorização, garantindo que decisões sobre resposta a incidentes se baseiam em observação real de produção, não apenas regras configuradas sem validação.

## Problema

Alertas podem ser configurados teoricamente mas falhar em produção de duas formas críticas:
- **Falsos Positivos (FP):** Alerta dispara mas não é ameaça (noise → alert fatigue → ignorados)
- **Falsos Negativos (FN):** Ameaça real ocorre mas alerta não dispara (threat passes undetected)

### Cenários de Risco

**Cenário 1 — Falso Positivo crônico:**
- Alerta: "Acesso a recurso crítico de IP novo"
- Configuração: IP não em whitelist → trigger
- Realidade: 50% dos acessos são de VPN de clientes legítimos (novos IPs por session)
- Resultado: Alerta dispara 20x/dia, Ops ignora (alert fatigue), ameaça real passa despercebida

**Cenário 2 — Falso Negativo silencioso:**
- Alerta: "Database connections > 100"
- Threshold: 100 connections
- Realidade: Ataque lento aumenta connections para 110 durante 30 min (apenas +10%)
- Resultado: Alerta não dispara (below threshold), attack completes sem detecção

**Cenário 3 — Falta de correlação:**
- Alerta 1: "Login fail > 5 per IP" → Fires
- Alerta 2: "Database unusual access pattern" → Fires (separately)
- Reality: Ambas são parte do mesmo ataque multi-stage (brute-force → DB exfil)
- Resultado: Alertas disparam isoladamente, correlação é manual, resposta é lenta

## Solução: Framework de Tuning Empírico em 5 Fases

### P1: Estabelecer Baseline de Produção

**Objetivo:** Entender padrão normal de produção sem ameaças ativas

**Procedimento:**

```bash
# P1.1: Recolher dados de 2-4 semanas de produção "clean" (sem ameaças conhecidas)
Baseline period: [data_início] a [data_fim] (2-4 semanas)
Exemplos de métricas a recolher:
  - Latência de requisições: p50, p95, p99, p999
  - Taxa de erro por endpoint: % de 4xx, % de 5xx
  - Failed login attempts: por minuto, por IP, por utilizador
  - Database connections: número ativo, tempo de espera
  - CPU/Memory: por servidor, agregado
  - Network traffic: inbound, outbound, por protocolo
  - Event volume: logs por segundo, por tipo

# P1.2: Normalizar e documentar baseline
Para cada métrica:
  - Valores normais: Registar p50, p95, p99 (não apenas média)
  - Variação natural: Padrões por hora (pico 9-17h), por dia (pico segunda-sexta)
  - Contexto: Quando baseline muda legitimamente (release, horário, sazonalidade)

Exemplo baseline (Login Failures):
  Métrica: Failed auth attempts per minute per IP
  Normal range: 0-2 attempts/min
  Peak (office hours): 2-5 attempts/min (legitimate failed login retry)
  Off-hours: 0-1 attempts/min
  Known spikes: Mondays 9-10am (1 in 5 users forgot password over weekend)
  
  Threshold para alerta: > 10 attempts/min OU > 5 attempts/min from known-bad IP

# P1.3: Documentar exceções
Legítimo padrões que parecem anómalos:
  - Batch jobs que geram traffic spike às 2 da manhã
  - Sincronização de dados que causa latência 2x por hora
  - Testes de penetração programados (sempre 3ª-feira 14-16h)

Saída P1: Documento de baseline com p50/p95/p99 por métrica, padrões conhecidos, exceções
```

**Responsável:** AppSec + DevOps (recolha conjunta)

---

### P2: Gerar Incidentes de Teste (Synthetic Threats)

**Objetivo:** Criar ameaças controladas e validar que alertas disparam

**Procedimento:**

```bash
# P2.1: Definir 5-10 tipos de ameaça para testar
Ameaças a simular (exemplos):
  1. Brute-force auth: 20 failed attempts em 1 minuto (known bad IP)
  2. DoS/Rate limit: 1000 RPS de single IP para endpoint (vs. normal 50 RPS)
  3. Privilege escalation: User A tenta aceder a recursos de User B (unauthorized)
  4. Data exfiltration: Large dataset é exportado (ex: 10GB em 10 min)
  5. Config change: Database connection string é alterada (security implication)
  6. Credential spray: 5 diferentes usernames attempted (vs. 1 per session)
  7. Lateral movement: Login de mesmo user de 5 different IPs em 10 min
  8. Resource abuse: Single user cria 100 jobs in parallel (DoS via resource depletion)

# P2.2: Executar simulação em staging ou canary
Environment: Staging or Low-Impact Canary (1% traffic)
Para cada ameaça:
  1. Execute simulação (script, tool, manual)
  2. Registre: hora exata, IP/user afetado, duração, intensidade
  3. Observe: Quais alertas disparam? Quantos minutos de delay?
  4. Comparar com baseline: Quão anómala é métrica?

Exemplo: Brute-force simulation
  Setup: Ativa SSH fail2ban test (20 failed login attempts de IP 10.0.0.50)
  Expected: Alerta "Login fail > 10" dispara em < 1 minuto
  Result: Alerta dispara em 42 segundos (✅ within tolerance)
  Metric: Failed attempts: 0 → 20 (2000% spike vs. baseline)

# P2.3: Iterar se alerta não dispara
Se alerta não foi acionado:
  - Por quê? Threshold é muito alto? Rule não captura esse padrão?
  - Ajusta threshold ou rule
  - Re-executa simulação
  - Valida que alerta agora dispara

# P2.4: Documentar cenário + baseline para referência futura
Template:
  Ameaça: [tipo]
  Simulação: [como foi criada]
  Baseline afectada: [métrica, valor normal, valor durante ataque]
  Alerta esperado: [nome do alerta]
  Latência de detecção: [tempo até alerta disparou]
  Falso Positivo histórico: [este padrão já foi visto legitimamente?]

Saída P2: Document com 5-10 cenários testados, alertas validados, latências registadas
```

**Responsável:** AppSec (design de testes) + Ops (execução)

---

### P3: Validar Alertas Disparam Corretamente

**Objetivo:** Confirmar que alertas detectam ameaças reais (testing real production)

**Procedimento:**

```bash
# P3.1: Executar P2 em produção com 1% traffic canary (low-risk)
Environment: Production Canary (1% traffic ou low-impact)
Importante: Usar feature flags para limitar impacto
  - Simule ataque em canary/staging ANTES de produção
  - OU simule com 1% real traffic e rollback rápido

# P3.2: Monitorizar alertas em tempo real
Durante simulação:
  [ ] Alerta é acionado? (SIM/NÃO)
  [ ] Em quanto tempo? (tempo de latência)
  [ ] É o alerta esperado? (correto ou falso positivo?)
  [ ] Contexto completo é capturado? (user, IP, resource, severity)

Exemplo: DoS simulation em produção canary (1% traffic)
  Simulação: Generate 500 RPS de single IP (vs. normal 50 RPS average)
  Expected alert: "Rate limit exceeded" or "DDoS detected"
  Actual: Alerta dispara após 15 segundos ✅
  Contexto: Source IP capturado, RPS registado (515), duration = 5 min
  Ação: Feature flag desativado, traffic retornou ao normal

# P3.3: Analisar latência de detecção
Métrica crítica: Quanto tempo desde "ataque começou" até "alerta disparou"?
  - IDEAL: < 1 min (detecção rápida)
  - BELA: 1-5 min (aceitável para MEDIUM ameaças)
  - POBRE: > 5 min (CRITICAL ameaças deveriam ser detectadas mais rápido)

Saída P3: Log de testes em produção, latências medidas, validação que alertas funcionam
```

**Responsável:** Ops + Security (execução coordenada)

---

### P4: Medir Taxa de Falsos Positivos

**Objetivo:** Quantificar e aceitar FP rate, identificar tuning necessário

**Procedimento:**

```bash
# P4.1: Recolher alertas de 1 semana de produção normal
Período: 1 semana de produção normal (sem ataques conhecidos)
Recolher: Lista de todos os alertas disparados

# P4.2: Classificar manualmente cada alerta
Para cada alerta:
  [ ] Verdadeiro Positivo (TP): Alerta é válido, ameaça é real
  [ ] Falso Positivo (FP): Alerta dispara, mas não é ameaça
  
Exemplo lista:
  Alerta ID 001: "Login fail > 10" → FP (QA testing, whitelist IP)
  Alerta ID 002: "DDoS pattern detected" → TP (real attack from 203.45.67.x)
  Alerta ID 003: "Unusual resource access" → FP (known batch job timing)
  Alerta ID 004: "Config change detected" → TP (unauthorized change attempt)

# P4.3: Calcular FP rate
FP rate = # of FPs / (# TPs + # FPs)

Target FP rates by alert type:
  - High confidence alerts (brute-force, known-bad IP): Target FP rate < 5%
  - Medium confidence (unusual access): Target FP rate < 15%
  - Low confidence (anomaly-based): Target FP rate < 25%

Example result:
  Week 1 alerts: 50 total (40 TP, 10 FP)
  FP rate = 10 / 50 = 20%
  If target is 10%, tuning is needed

# P4.4: Analisa FP patterns
Quais tipos de FP ocorrem frequentemente?
  - Timing: Todas as 3 AM (batch job)
  - Source: Sempre de IP 10.0.1.x (internal network)
  - User: Sempre user "admin" (authorized)
  - Action: Sempre create (not delete, more dangerous)

Action: Whitelist, add context, adjust threshold

Saída P4: FP rate report, patterns identified, tuning recommendations
```

**Responsável:** AppSec (classificação) + Ops (whitelist/tuning)

---

### P5: Continuous Tuning e Validação

**Objetivo:** Manter alertas afinados contra mudanças de produção

**Procedimento:**

```bash
# P5.1: Monthly alert review
Frequência: Uma vez por mês
Para cada alerta:
  - FP rate this month (target < target%)
  - Mean time to alert (latência média)
  - TP rate (how many real threats were caught)
  - Rules are still valid? (alguma mudança em produção?)

# P5.2: Tune based on observations
Se FP rate > target:
  - Aumentar threshold (menos sensível)
  - Adicionar whitelist de known-false positives
  - Refinar rule (ex: "7+ failed logins from non-known-good IPs")
  - Aumentar janela de time (ex: 5 failed in 1 min → 10 failed in 5 min)

Se FN detectado (threat que não foi alerted):
  - Reduzir threshold (mais sensível)
  - Adicionar contexto ao rule (ex: failed logins + resource access attempt = ataque)
  - Criar novo alerta para preencher a lacuna

# P5.3: A/B testing (opcional para L3)
Para L3 apps com high threat surface:
  - Versão A: Current alert rule
  - Versão B: Candidate improved rule
  - Executa ambas em production com metrics
  - Compara FP/FN, latência, coverage
  - Deploy winning version

# P5.4: Quarterly synthetic test re-run
Frequência: Uma vez por trimestre
Repete P2+P3 (gera ameaças teste, valida alertas disparam)
Objetivo: Confirmar que alertas continuam a funcionar após mudanças

Saída P5: Monthly alert metrics, tuning log, quarterly synthetic test results
```

**Responsável:** Ops + AppSec (continuous collaboration)

---

## Falso Positivo & Negativo: Handling Templates

### Falso Positivo (V1): Alerta Dispara, Não é Ameaça

**Cenário:** Alerta é acionado, mas investigação mostra que não é ameaça real.

**Procedimento V1:**

```markdown
## Template V1 — Análise de Falso Positivo

Data: [data]
Alerta ID: [alerta]
Investigador: [nome]

### Alerta Disparado
- Nome: [ex: Login fail > 10]
- IP/User/Resource: [contexto]
- Hora: [timestamp]
- Métrica: [ex: 12 failed logins em 2 minutos]

### Investigação
- Por quê é FP? [ex: QA testing, batch job retry, legitimate user confusion]
- Qual é a evidência? [ex: IP é da rede interna, user é QA team]
- Como sabemos que não é ataque? [ex: contexto temporal + known legitimate activity]

### Ação Tomada
Opção A: Whitelist
  - Adicionar IP/user/resource a whitelist do alerta
  - Implementado em [data]
  - Teste: Regra foi re-testada com mesmo padrão → alerta não dispara ✅

Opção B: Aumentar Threshold
  - Mudar threshold de "10" para "15" failed logins em 2 min
  - Rationale: Legitimate activity ocasionalmente atinge 10-12, ataque começa >15
  - Teste: Recolheram dados históricos, zero FP com novo threshold, bons TPs mantidos ✅

Opção C: Adicionar Contexto
  - Refinar rule de "failed logins > 10" para "failed logins > 10 AND IP não em whitelist"
  - Rationale: Context reduz FP sem perder detecção

### Learning
- Por que a rule foi configurada sem este contexto?
- Como evitamos FP similar no futuro?

Assinado: [Investigador] [data]
```

---

### Falso Negativo (V2): Ameaça Real, Alerta Não Disparou

**Cenário:** Ameaça real ocorreu, mas alerta não foi acionado (detection miss).

**Procedimento V2:**

```markdown
## Template V2 — Análise de Falso Negativo / RCA

Data: [data incidente descoberto]
Ameaça: [descrição, ex: Unauthorized database export]
Descoberta: [como foi descoberta se não por alerta]

### Análise Causa Raiz (RCA)

Pergunta 1: Por que alerta não disparou?
  - Métrica não estava sendo recolhida? (ex: export log não era centralizado)
  - Threshold era muito alto? (ex: alerta só disparava em >1GB export, ataque foi 500MB)
  - Rule não capturava padrão? (ex: export via API, rule só monitorizava UI)
  - Alerta estava silenciado/disabled? (ex: tuning anterior desativou regra)

Análise para nossa ameaça: Database export não era monitorizado
  - Log source: Database não tinha audit logging de exports ❌
  - Descoberta: Observado via network monitoring (alta data transfer), não alerta

Pergunta 2: Qual é a criticidade desta lacuna?
  - Ameaça: Confidencialidade comprometida (dados foram exfiltrados)
  - Detecção: Totalmente missed até descoberta manual
  - Impacto: [X] dias desde exfil até descoberta

Pergunta 3: Qual é a remediação?
  - Habilitado: Audit logging em database (todos os exports registados)
  - Novo alerta: "Database export > 100MB" criado e testado
  - Validação: Synthetic test de export, alerta dispara em <1 min ✅

### Learning & Melhoria
- Gap identificado: Database auditing não estava habilitado
- Root cause: Configuração foi skipped como "not yet needed"
- Prevenção: Audit logging agora é parte de deployment checklist
- Teste futuro: P2/P3 incluem data export scenario

Assinado: [Investigador] [data]
```

---

## Qualidade Metrics (Validação P1-P5)

| Métrica | Alvo L1 | Alvo L2 | Alvo L3 | Propósito |
|---|---|---|---|---|
| **Baseline Establishment (P1)** | — | — | — | |
| Baseline period | 2 semanas | 2 semanas | 2 semanas | Dados suficientes para padrão |
| Métricas recolhidas | 5+ | 10+ | 15+ | Cobertura proporcional |
| Baseline documentation | Básico | Completo | Completo + context |Reprodutibilidade |
| **Synthetic Testing (P2)** | — | — | — | |
| Ameaças simuladas | 3 tipos | 5 tipos | 8+ tipos | Cobertura de threat types |
| Teste frequency | Quarterly | Monthly | Monthly | Validação regular |
| Alert detection rate (P2 passa) | > 90% | > 95% | > 98% | Alertas funcionam |
| Mean detection latency | < 5 min | < 2 min | < 1 min | Rapidez de detecção |
| **FP Measurement (P4)** | — | — | — | |
| FP rate (max acceptable) | 20% | 10% | 5% | Menos noise para L3 |
| FN rate (max acceptable) | 15% | 10% | 5% | Cobertura maior para L3 |
| Alert accuracy (TP / total) | > 80% | > 90% | > 95% | Qualidade geral |
| **Continuous Tuning (P5)** | — | — | — | |
| Tuning review frequency | Quarterly | Monthly | Continuous | Manutenção proporcional |
| Alerta rule changes per month | 0-2 | 2-4 | 5+ | Evolução baseada em dados |
| Whitelist items maintained | Basic | Documented | Auto-validated | Conhecido e rastreável |

---

## Implementação Checklist

- [ ] **P1:** Recolher baseline de 2-4 semanas de produção clean
- [ ] **P1:** Documentar p50/p95/p99 por métrica, padrões conhecidos, exceções
- [ ] **P2:** Definir 5-10 tipos de ameaça para testar
- [ ] **P2:** Executar simulações em staging, registar alertas disparados
- [ ] **P3:** Executar P2 em production canary (1% traffic), medir latências
- [ ] **P4:** Recolher alertas de 1 semana produção, classificar TP/FP
- [ ] **P4:** Calcular FP rate, comparar contra targets, identificar padrões
- [ ] **P5:** Setup monthly alert review process
- [ ] **P5:** Implementar tuning (whitelists, thresholds, rules)
- [ ] **P5:** Quarterly synthetic test re-run (P2+P3 repetido)
- [ ] **V1/V2:** Template process para FP/FN handling quando descobertos
- [ ] **Métricas:** Setup KPI tracking (FP rate, alert accuracy, detection latency)

---

## Proporcionalidade L1/L2/L3

### L1 — Manual, Low Automation
- **P1:** Baseline manual (simple p50 value, no percentiles)
- **P2/P3:** Synthetic tests quarterly, manual execution
- **P4:** FP rate measured monthly via manual review
- **P5:** Tuning quarterly, whitelist maintained in spreadsheet
- **Frequency:** Slow (quarterly), mais labor-intensive

### L2 — Automated + Gated
- **P1:** Baseline automated recolha, p50/p95/p99 calculados
- **P2/P3:** Synthetic tests monthly, semi-automated scripts
- **P4:** FP rate automated tracking, dashboards
- **P5:** Tuning monthly, regras versioned em Git
- **Frequency:** Regular (monthly), mais automated

### L3 — Automated + Tested + Continuous
- **P1:** Baseline continuous recolha, real-time dashboards
- **P2/P3:** Synthetic tests weekly/continuous, fully automated chaos engineering
- **P4:** FP rate real-time tracking, automated tuning suggestions
- **P5:** Continuous tuning via ML/anomaly detection, auto-whitelisting
- **Frequency:** Continuous, mostly automated with human oversight

---

## Referências

- **NIST SSDF PO.5:** Alert tuning, false positive management
- **OWASP SAMM** (O&U—Operations & Maintenance): Alert monitoring and tuning
- **Observability best practices:** Reducing alert fatigue, alert quality metrics

