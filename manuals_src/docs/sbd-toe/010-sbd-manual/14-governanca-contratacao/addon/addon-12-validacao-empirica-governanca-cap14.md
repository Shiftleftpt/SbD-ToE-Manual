# 🔍 Validação Empírica da Eficácia de Governação

> **Invariante I2 (agent.md):** Evidência acima de plausibilidade → Empirical validation que exceções realmente reduzem risco & compensações funcionam

---

## 📋 Objetivo

Implementar um **framework de validação empírica** para confirmar que exceções de risco, com suas compensações, realmente funcionam em produção (compensações mitigam, incidentes não exploram lacunas, auditoria passa).

Problema central: "Exceção aprovada com compensação SIEM" ≠ "SIEM alert realmente funciona em produção"  
Solução: 5 fases para **testar compensações com cenários reais**, medir **eficácia**, e identificar **compensações inefetivas** (aprovadas mas não funcionam) ou **false negatives** (exceção sem risco real).

---

## 🚨 Problema: Risco & Cenários

**Cenário 1 — Compensação aprovada, não implementada:**
- L2 app: "Exceção REQ-LOG-005 (sem logs 90d), compensada por SIEM anomaly alerts"
- Exceção aprovada em Feb, SIEM alert supostamente ativo
- Maio: Incidente em app → Logs não existem (retenção 7d), SIEM alerta não disparou
- **Risco:** Compensação não estava operacional; exceção oferecia risco nu

**Cenário 2 — Compensação inadequada (aprovada mas fraca):**
- L3 app (crítico): "Exceção REQ-CRYPT-002 (sem criptografia), compensada por 'SLA resposta 4h'"
- Aprovada (erro de avaliação em D1)
- Seis meses depois: "SLA resposta 4h" é mero SLA operacional, não mitiga exposição dados em trânsito
- **Risco:** Compensação é fraca para L3, exceção oferece risco inaceitável

**Cenário 3 — Revalidação não ocorre:**
- Exception: "Logs 90d por 6 meses, roadmap Q3 infraestrutura"
- Junho chega: Infraestrutura ainda não orçada, deadline passa sem renovação formal
- Sistema não marca como "violação", continua em vigor indefinidamente
- **Risco:** Exceção "temporária" torna-se permanente sem decisão consciente

---

## 🔄 Framework: 5 Fases de Validação

```
┌──────────────────────────────────────────────────────────────┐
│ FASE 1: P1 — BASELINE (Pré-exceção)                          │
│ └─ Recolher dados: incidentes, audit results, métrica saúde  │
├──────────────────────────────────────────────────────────────┤
│ FASE 2: P2 — COMPENSATION TESTING (Lab/Staging)              │
│ └─ Validar compensação funciona: SIEM rule dispara, logs     │
├──────────────────────────────────────────────────────────────┤
│ FASE 3: P3 — PRODUCTION MONITORING (Canary)                  │
│ └─ Executar testes em produção real, medir eficácia          │
├──────────────────────────────────────────────────────────────┤
│ FASE 4: P4 — INCIDENT RCA (Validação empírica)               │
│ └─ Classificar: compensação funcionou? ou falhou?            │
├──────────────────────────────────────────────────────────────┤
│ FASE 5: P5 — CONTINUOUS REVIEW (Trimestral)                  │
│ └─ Revisar exceções, RCA, reanalisar risco, renovar/negar    │
└──────────────────────────────────────────────────────────────┘
```

---

## 🎯 FASE 1 — P1: Baseline Establishment (Pré-exceção)

**Objetivo:** Antes de qualquer exceção, documentar estado atual de risco & controlo.

**Duração:** 1-2 semanas antes de aprovar exceção

### P1-1: Métricas de Risco Baseline

Recolher de produção (últimas 4 semanas):

**Métrica A1: Incidentes Relacionados ao Requisito**
```
Exceção: REQ-LOG-005 (retenção logs 90d)
App: app-inventario

Incidentes nos últimos 4 semanas:
- 2025-02-10: "Access anomaly, didn't find logs" (severity: MÉDIA, resolved: 2 dias)
- 2025-01-15: "Audit finding: logs not 90d" (severity: BAIXA, finding aberto)

Baseline:
- # Incidentes relacionados a logs: 2
- MTTR médio: 2 dias
- Audit findings: 1 aberto
```

**Métrica A2: Cobertura de Controlos Atuais**
```
Exceção: REQ-CRYPT-002 (criptografia em trânsito)
App: api-core

Status atual:
- Está TLS implementado? SIM (parcial, 80% tráfico, 20% legacy clients)
- Está monitorizado? SIM (SIEM regista erro TLS)
- Quem tem visibilidade? SOC (1 pessoa, part-time)

Baseline:
- % tráfico criptografado: 80%
- MTTR se falha: ~4 horas (SOC disponibilidade)
- Cobertura monitorização: Básica
```

### P1-2: Documentação de Baseline

**Arquivo:** `baseline_pre_excecao_[app]_[requisito]_[data].md`

```markdown
# Baseline — app-inventario — REQ-LOG-005 — 2025-02-15

## Período de observação
- Data início: 2025-01-15
- Data fim: 2025-02-15
- Duração: 4 semanas

## Amostra
- Aplicação: app-inventario (L2, inventory management)
- Requisito: REQ-LOG-005 (retenção logs 90 dias)
- Risco sem requisito: **Alto** (compliance issue, audit trail gap)

## Resultados

### Incidentes
- 2 incidentes em 4 semanas relacionados a logs
- MTTR: 2 dias (pois logs não retidos 90d, investigação lenta)
- Audit finding: 1 aberto (logs retention não cumprido)

### Controlos atuais
- Logs retidos: 7 dias (atual), 90 dias (alvo, não implementado)
- Monitorização: SIEM basic (anomaly detection ativo)
- SLA resposta: 4 horas (por SOC)

### Compensação proposta
- SIEM alert anomalies
- Manual audit trimestral
- Roadmap infraestrutura Q3 2025

## Próxima fase
P2 — Compensation testing, data: 2025-02-20
```

---

## 🧬 FASE 2 — P2: Compensation Testing (Lab/Staging)

**Objetivo:** Validar que compensação proposta realmente funciona.

**Duração:** 1-2 semanas de testes

### P2-1: Definir Cenários de Teste

**Baseado em baseline (P1):** Selecionar compensações propostas e validar

| # | Compensação | Tipo Teste | Esperado | Duração |
|---|-------------|-----------|----------|---------|
| C1 | SIEM alert anomalies | Injetar anomalia, alert dispara? | SIM em <1 min | 1h |
| C2 | Manual audit trimestral | Executar audit, encontrar gaps? | SIM, formato correto | 4h |
| C3 | Redução retenção 7d | Implementar, logs expiram? | SIM, timely | 2h |

### P2-2: Procedimento P2

**Por cada compensação C1-C3:**

1. **Setup:** Lab/staging com dados reais da app
2. **Execução:** Simular cenário que dispara necessidade de compensação
3. **Medição:**
   - ✅ Compensação funciona (alert dispara, audit encontra)
   - ⏱️ Tempo para funcionar (segundos? minutos?)
   - 📝 Dados/formatos corretos
   - ⚙️ Automação ou manual?

4. **Resultado por Compensação:**
```
P2 Results — app-inventario — Compensations (2025-02-20)

┌──────────────────┬────────┬──────────┬────────────────┐
│ Compensação      │ Funciona│ Tempo    │ Status         │
├──────────────────┼────────┼──────────┼────────────────┤
│ SIEM alert       │ ✅ SIM │ 45 sec   │ Pronto         │
│ Manual audit     │ ✅ SIM │ 4 horas  │ Pronto (manual)│
│ Retention 7d     │ ✅ SIM │ Auto     │ Pronto         │
├──────────────────┼────────┼──────────┼────────────────┤
│ Overall          │ ✅ 100%│ Avg 1h   │ Ready for P3   │
└──────────────────┴────────┴──────────┴────────────────┘
```

---

## 🌍 FASE 3 — P3: Production Monitoring (Canary)

**Objetivo:** Executar compensações em produção (1-5% tráfico) e medir eficácia real.

**Duração:** 2-4 semanas de produção

### P3-1: Setup Canary

**Selecionar feature/app "in scope" for exceção:**
- Ex: app-inventario, REQ-LOG-005 exceção
- Canary: SIEM alerts + audit process ativos em produção

**Monitorização:**
```
Production traffic (100%):
  - 95% com compensações (SIEM + audit já existem)
  - 5% nova aplicação exceção (validar compensações em produção)
  
Métrica: Alert rate, false positive rate, audit time, risco detetado
```

### P3-2: Procedimento P3

**Semana 1-2: Baseline em produção**
1. Ativar SIEM alerts em produção
2. Medir: false positive rate, false negative rate (anomalia real não detectada)
3. Medir: tempo médio alert-to-response

**Métricas P3 (semana 1-2):**

| Métrica | Target | Resultado | Status |
|---------|--------|-----------|--------|
| FP rate | <10% | 8% | ✅ OK |
| FN rate | <5% | 3% | ✅ OK |
| Alert latency p95 | <5 min | 3 min | ✅ OK |
| SOC response | <4h | 2h avg | ✅ OK |

**Semana 3-4: Validação prática**
1. Executar synthetic threat (anomaly) em produção (1% tráfico)
2. Medir: SIEM detects? Quantos false positives?
3. Medir: Audit process consegue classificar corretamente?

---

## 📊 FASE 4 — P4: Incident RCA (Validação Empírica)

**Objetivo:** Após meses em produção, analisar incidentes reais para validar se compensação funcionou.

**Duração:** 1 semana de análise

### P4-1: Recolher Amostra de Incidentes

**Caso 1: Compensação Efetiva**

```markdown
## Case C1 — Compensation Effective

**Exceção:** app-inventario, REQ-LOG-005 (logs 90d)
**Compensação:** SIEM alert + manual audit
**Incidente:** 2025-04-10 - Unauthorized access tentative

### What happened
- 2025-04-10 14:00: Unauthorized attempt to access user_id=123
- 2025-04-10 14:05: SIEM alert dispara (anomaly detected)
- 2025-04-10 14:15: SOC responde, bloqueia access
- 2025-04-10 15:00: AppSec investigates (logs 7d retenção suficiente)

### Classification
- **Compensação Efectiva:** ✅ SIM
  - SIEM alerta funcionou (5 min latency)
  - Resposta rápida (10 min)
  - Logs 7d foram suficientes para investigação
  - Risco mitigado

### Métrica de eficácia
- Detection latency: 5 min ✅
- Response time: 10 min ✅
- Investigation success: SIM ✅
- Resultado: **Compensação FUNCIONA**

```

**Caso 2: Compensação Falha**

```markdown
## Case C2 — Compensation Failed

**Exceção:** api-core, REQ-CRYPT-002 (criptografia)
**Compensação:** "SLA 4h response"
**Incidente:** 2025-05-22 - Data exposed in transit

### What happened
- 2025-05-22 09:00: Attacker intercepts unencrypted data (legacy client, TLS bypass)
- 2025-05-22 12:00: Customer reports suspicious activity (data accessed?)
- 2025-05-22 13:00: SIEM detecta anomalia (belatedly, dados já exfiltrados)
- 2025-05-22 14:30: SOC responde

### Classification
- **Compensação Inefectiva:** ❌ NÃO
  - SLA "4h response" não é mitigação técnica, apenas procedural
  - Dados já exfiltrados quando SLA de 4h disparado
  - Risco **NÃO foi mitigado** por compensação

### Métrica de eficácia
- Detection latency: 3h (dados já expostos) ❌
- Response time: 1.5h (vs SLA 4h) (irrelevante, tarde)
- Damage: Data exposição confirmada ❌
- Resultado: **Compensação FALHOU, exceção deve ser NEGADA**

### RCA & Ação
- Exceção foi mal avaliada em D1 (Q2 checklist falhou)
- Necessário: Implantar criptografia REAL, negar exceção
- Timing: Implementar até [data], ou app offlining

```

### P4-2: V1 & V2 Templates

#### Template V1: Compensação Efetiva

```markdown
## V1 — Compensation Effective Analysis

**Caso ID:** EFF-2025-Q2-001
**Data:** 2025-04-10
**Exceção:** app-inventario, REQ-LOG-005
**Compensação:** SIEM alert + manual audit

---

### Validação
- ✅ SIEM alert disparou (latency: 5 min)
- ✅ SOC respondeu em SLA (2h vs 4h)
- ✅ Logs 7d foram suficientes para RCA
- ✅ Incidente foi mitigado sem escalação

---

### Resultado
**Compensação FUNCIONA** para este requisito/app

---

### KPI Contribution
- Efetividade: 1 (out of 1)
- Latency: 5 min (target <10 min)
- Impacto: Incidente resolvido rápido

```

#### Template V2: Compensação Falha (RCA)

```markdown
## V2 — Compensation Failed / RCA

**Caso ID:** FAIL-2025-Q2-001
**Data:** 2025-05-22
**Exceção:** api-core, REQ-CRYPT-002
**Compensação proposta:** "SLA 4h response" (inadequada)

---

### Root Cause Analysis

**O que aconteceu:**
- Legacy client sem TLS, dados em plaintext
- Attacker intercepts traffic (SLA de 4h não mitiga isso)
- Dados exfiltrados antes de SOC responder

**Raiz problema:**
- Compensação foi procedural (SLA response), não técnica
- Não há mitigação REAL da exposição em trânsito
- D1 checklist falhou (Q2 avaliação incorreta de suficiência)

---

### Remediation

1. **Imediato:** Bloquear legacy clients sem TLS
2. **Urgente:** Implementar criptografia REAL (não apenas SLA)
3. **Timing:** Até [data concreta]
4. **Resultado:** Exceção NEGADA, requisito deve ser cumprido

---

### Lição aprendida
- Compensações procedurais (SLA response) são insuficientes para L3 apps
- D1 Q2 ("Compensações adequadas?") deve questionar: "É TÉCNICA ou apenas SLA?"
- Revisar todas exceções L3 com compensação "SLA response" → possível upgrade para técnica

```

### P4-3: KPIs de Eficácia

Após análise de 10-20 incidentes reais (3-6 meses de dados):

| Métrica | Target | Resultado | Status |
|---------|--------|-----------|--------|
| **Compensation effectiveness** | >80% | 85% | ✅ Acceptable |
| **Detection latency (P50)** | <10 min | 7 min | ✅ Good |
| **Falsos positivos** | <15% | 12% | ✅ Good |
| **Falsos negativos** | <5% | 3% | ✅ Good |
| **Incidentes mitigados** | >75% | 78% | ✅ Good |

---

## 📈 FASE 5 — P5: Continuous Review

**Objetivo:** Após validação (P1-P4), implementar ciclo de melhoria contínua.

**Frequência:** Trimestral (L1), Mensal (L2), Contínuo (L3)

### P5-1: Trimestral Review Cycle (L2/L3)

**Agenda Trimestral:**

```
WEEK 1: Coleta de dados
  - Incidentes últimos 3 meses em exceções L2/L3
  - Análise de compensações (funcionam? não funcionam?)
  - Audit results (acharam gaps?)
  
WEEK 2: RCA & análise
  - Por cada incidente: V1 (efetiva) ou V2 (falha)?
  - Calcular KPIs (effectiveness %, latency, etc.)
  - Identificar patterns (ex: "SIEM alerts sempre falham para X")
  
WEEK 3: Decisão
  - Exceção permanece? (Sim, compensação funciona)
  - Exceção negada? (Não, compensação falhou, requisito obrigatório)
  - Exceção modificada? (Sim, mudar compensação para mais forte)
  
WEEK 4: Revalidação
  - Se compensação modificada, executar P2-P3 novamente
  - Comunicar decisão (aprove, negar, modify)
  - Atualizar GRC system, comunicar stakeholders
```

### P5-2: Proporcionalidade L1/L2/L3

| Nível | P1 Baseline | P2 Test | P3 Monit | P4 RCA | P5 Review |
|-------|------------|--------|---------|--------|-----------|
| **L1** | Yearly | Yearly | 3-month | Quarterly | Quarterly |
| **L2** | Quarterly | Quarterly | Monthly | Monthly | Monthly |
| **L3** | Monthly | Monthly | Monthly | Weekly | Weekly |

### P5-3: Checklist de Revisão

Se P4 identifica compensação ineficaz (>20% falhas):

```markdown
## Exceção Review — app-core — REQ-ENC-002 — Q2 2025

### P4 Analysis Result
- Effectiveness: 75% (target 80%+) ⚠️
- 3 dos 12 incidentes: compensação falhou (SLA response, não técnica)

---

### Decisão necessária

**☐ RENEW (Compensação funciona adequadamente)**
- Sim, 75% é aceitável para L2
- Revalidação: 2025-06-30
- Continue monitorização

**☐ MODIFY (Cambiar compensação por mais forte)**
- Não, SLA response é insuficiente
- Compensação nova: Implementar rate limiting + WAF alerts
- Revalidação: 2025-06-30 (após implementação)

**☐ DENY (Compensação não funciona, requisito obrigatório)**
- Não, 75% é inadequado para L3 (seria necessário >95%)
- Ação: Implementar requisito ou offlining
- Deadline: 2025-08-30

---

### Decision Selected
**☑ MODIFY**
- Razão: 3 dos 12 incidentes = "SLA response não mitiga"
- Nova compensação: Rate limiting (técnica) + WAF alerts + SLA response (backup)
- Timeline: Implementar até 2025-06-15
- Retest: P2-P3 após implementação

---

## Retest Result (2025-06-20)
- Effectiveness: 95% (target 80%+) ✅ PASS
- Pronto para renovação trimestral
```

### P5-4: KPIs Continuidade

**KPI-1: Efetividade de Compensação**
- **Target:** >80% (L1/L2), >95% (L3)
- **Frequência:** Trimestral
- **Owner:** AppSec + GRC
- **Métrica:** # Compensações efetivas / # Total incidentes em exceções × 100

**KPI-2: Tempo de Detecção**
- **Target:** <10 min (L1/L2), <5 min (L3)
- **Frequência:** Trimestral
- **Owner:** SOC
- **Métrica:** Percentil 50 latency para alert (desde incidente até disparo)

**KPI-3: Taxa de Falsos Positivos**
- **Target:** <15% (L1/L2), <5% (L3)
- **Frequência:** Mensal
- **Owner:** SOC
- **Métrica:** # False positive alerts / # Total alerts × 100

**KPI-4: Taxa de Falsos Negativos**
- **Target:** <5% (L1/L2), <2% (L3)
- **Frequência:** Trimestral
- **Owner:** AppSec
- **Métrica:** # Incidentes não detectados / # Total incidentes × 100

**KPI-5: Exceções Mantidas vs Removidas**
- **Target:** >30% exceções removidas em revalidação
- **Frequência:** Trimestral
- **Owner:** GRC
- **Métrica:** # Exceções removidas / # Total revalidadas × 100

---

## 📚 Integração com Cap 14 — Aplicação Lifecycle

| Fase SDLC | P1-P5 Trigger | Responsável | Ação |
|-----------|--------------|-------------|------|
| **Planning** | P1: Baseline se exceção prevista | AppSec | Recolher dados pré-exceção |
| **Approval** | P2: Compensation testing antes R1 | DevOps | Validar compensação em lab |
| **Deployment** | P3: Canary com monitorização | SOC + AppSec | Deploy com alerts ativados |
| **Operations** | P4: RCA mensal/trimestral | AppSec + GRC | Análise incidentes, V1/V2 |
| **Audit** | P5: Review trimestral | GRC | Renovação/denial exceção |

---

## 🔗 Cenário Real: P1-P5 Completo

**Exceção:** app-inventario, REQ-LOG-005 | **Período:** 2025-02 a 2025-05

---

### ✅ P1 — Baseline (2025-02-15)
```
Resultado:
- 2 incidentes relacionados a logs no mês anterior
- MTTR: 2 dias (lento, por falta de logs 90d)
- Audit finding: 1 aberto
```

---

### ✅ P2 — Compensation Testing (2025-02-20)
```
Resultado:
- SIEM alert: Funciona (45 sec latency) ✅
- Manual audit: Funciona (4h execution) ✅
- Retention 7d: Funciona (auto) ✅
- Overall effectiveness: 100%
```

---

### ✅ P3 — Production Monitoring (2025-03-01 a 03-30)
```
Resultado (primeira semana):
- FP rate: 8% (target <10%) ✅
- FN rate: 3% (target <5%) ✅
- Alert latency p95: 3 min (target <5 min) ✅
- Pronto para continuar
```

---

### ✅ P4 — Incident RCA (2025-04-15)
```
Resultado (amostra 8 incidentes em 3 meses):
- 7 incidentes: Compensação efetiva (V1)
- 1 incidente: Compensação falhou (V2 — logs 7d insuficiente para RCA)

Effectiveness: 7/8 = 87.5% (target >80%) ✅
Ação: V2 RCA → "Aumentar retenção 14d para L2 crítica"
```

---

### ✅ P5 — Continuous Review (2025-05-15)
```
Resultado:
- Compensation effectiveness: 87.5% ✅
- KPIs all met
- Decision: RENEW exceção por mais 6 meses
- Ação: Atualizar retenção 14d, revalidação 2025-11-15
```

---

## 📋 Checklist Final de Implementação

- [ ] P1 baseline procedure documentada (métricas: incidentes, controlo status, compensação)
- [ ] P1 baseline recolhido para cada exceção L2+ (registro em GRC)
- [ ] P2 compensation test procedure definida (lab/staging validation)
- [ ] P2 tests executados antes aprovação R1
- [ ] P3 production canary framework setup (monitorização + alerts)
- [ ] P3 metrics recolhidos (FP%, FN%, latency)
- [ ] P4 V1 template (compensação efetiva) documentado
- [ ] P4 V2 template (RCA falha) documentado
- [ ] P4 RCA procedure (mensal/trimestral) definida
- [ ] P5 review cycle agenda fixa (trimestral)
- [ ] P5 decisão framework (RENEW/MODIFY/DENY) implementado
- [ ] 5 KPIs rastreados em dashboard (effectiveness, latency, FP%, FN%, removal rate)
- [ ] Proporcionalidade L1/L2/L3 aplicada (frequência diferente)
- [ ] Training para AppSec/GRC em P1-P5 — 2h workshop

