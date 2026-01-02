# 🧪 Validação Empírica de Eficácia de Formação

> **Invariante I2 (agent.md):** Evidência acima de plausibilidade → Empirical validation que formação realmente melhora competência & previne vulnerabilidades

---

## 📋 Objetivo

Implementar um **framework de validação empírica** para confirmar que formação não apenas aumenta conhecimento (quiz score), mas **muda comportamento real** e **reduz vulnerabilidades** em produção.

Problema central: "85% aprovação em quiz" ≠ "Dev escreve código seguro"  
Solução: 5 fases para **testar aprendizado com cenários reais**, medir **eficácia**, e identificar **false positives** (altos scores, fraco desempenho) ou **false negatives** (baixos scores, bom desempenho).

---

## 🚨 Problema: Risco & Cenários

**Cenário 1 — False Positive (quiz sim, code não):**
- Dev completa "OWASP Top 10" (quiz 92%), recebe certificado
- 2 semanas depois: PR review mostra múltiplas falhas OWASP (SQL injection, XSS simples)
- **Risco:** Quiz mede memorização, não competência aplicada
- **Consequência:** Formação consumida sem benefício real, vulnerabilidade não remediada

**Cenário 2 — False Negative (quiz não, code sim):**
- QA falha "Testes de Segurança" (quiz 68%, reprovado)
- Mas em prática com app vulnerável, encontra 5 falhas complexas em 30min
- **Risco:** Quiz inadequado para medir competência real (muito teórico, pouco prático)
- **Consequência:** Talento retido, competência não reconhecida

**Cenário 3 — Sem correlação com redução de vulns:**
- Equipa L2 completou "Secure Coding 101" (2024)
- 2025: Mesmo número de vulnerabilidades em code reviews, CI/CD ainda passa 3 falhas/mês
- **Risco:** Formação sem impacto real; investimento desperdiçado
- **Consequência:** Confiança perdida em programa de formação

---

## 🔄 Framework: 5 Fases de Validação

```
┌──────────────────────────────────────────────────────────────┐
│ FASE 1: P1 — BASELINE (2-4 semanas pré-formação)            │
│ └─ Recolher p50/p95/p99 de métricas sem intervenção         │
├──────────────────────────────────────────────────────────────┤
│ FASE 2: P2 — SYNTHETIC THREAT GENERATION (lab)              │
│ └─ Criar cenários reais de ataque em staging                │
├──────────────────────────────────────────────────────────────┤
│ FASE 3: P3 — PRODUCTION VALIDATION (canary)                 │
│ └─ Executar testes em 1-5% tráfico real, medir latência     │
├──────────────────────────────────────────────────────────────┤
│ FASE 4: P4 — FALSE POSITIVE/NEGATIVE MEASUREMENT (1 semana)  │
│ └─ Classificar alerts reais: TP/FP/FN, calcular accuracy    │
├──────────────────────────────────────────────────────────────┤
│ FASE 5: P5 — CONTINUOUS IMPROVEMENT (mensal/trimestral)     │
│ └─ Revisar resultados, ajustar conteúdo, retestar           │
└──────────────────────────────────────────────────────────────┘
```

---

## 🎯 FASE 1 — P1: Baseline Establishment

**Objetivo:** Antes de qualquer formação, documentar estado atual de competência & vulnerabilidade.

**Duração:** 2-4 semanas de observação (não intervém)

### P1-1: Métricas de Código (Baseline)

Recolher de produção (últimos 2-4 semanas):

**Métrica A1: Vulnerabilidade por Dev**
```
┌──────────────────┬────────────┬────────────┬─────────┐
│ Dev Name         │ # Vulns P3 │ # Vulns P2 │ # Vulns │
│                  │ (Crítica)  │ (Alta)     │ P1 (Med)│
├──────────────────┼────────────┼────────────┼─────────┤
│ João Silva       │ 0          │ 1          │ 2       │
│ Maria Costa      │ 0          │ 2          │ 3       │
│ Pedro Oliveira   │ 0          │ 0          │ 1       │
│ Avg (L1)         │ 0.0        │ 1.0        │ 2.0     │
└──────────────────┴────────────┴────────────┴─────────┘
```
- **p50:** Mediana vulnerabilidades por Dev
- **p95:** Percentil 95 (pior quartil)
- **p99:** Máximo

**Métrica A2: Tipos de Vulnerabilidades (Distribuição)**
```
OWASP Top 10 Distribution (baseline):
- SQL Injection: 15%
- XSS: 25%
- Insecure Deserialization: 10%
- Authentication Bypass: 20%
- Information Disclosure: 15%
- Other: 15%
```

**Métrica A3: Tempo médio para Fix (MTTR por Dev)**
- João: 3 dias (p50), 7 dias (p95)
- Maria: 5 dias (p50), 12 dias (p95)
- Avg L1: 4 dias (p50), 10 dias (p95)

### P1-2: Métricas de Processo (Baseline)

**Métrica B1: Taxa de aprovação em Code Review**
- % PRs aprovadas de 1ª (sem rework)
- % PRs com feedback "security concern"
- Avg dias de PR review

**Métrica B2: Incidentes Relacionados a Código**
- # Incidentes por Dev (últimas 4 semanas)
- % Incidentes causados por padrão de código (vs. configuração, operação)

### P1-3: Documentação de Baseline

**Arquivo:** `baseline_pre_formacao_[trilho]_[data].md`

```markdown
# Baseline — Secure Coding L1 — 2025-01-15

## Período de observação
- Data início: 2024-12-15
- Data fim: 2025-01-15
- Duração: 4 semanas

## Amostra
- Devs testados: 12 (L1)
- PINs analisados: 125
- Incidentes: 3

## Resultados

### Vulnerabilidades
- p50: 2 vulns/dev
- p95: 5 vulns/dev
- p99: 8 vulns/dev (1 dev outlier)
- Distribuição: 60% XSS+SQLi, 40% outras

### MTTR
- Média: 4.2 dias
- Mediana: 3 dias
- p95: 10 dias

### Code Review
- Taxa aprovação 1ª: 65%
- Feedback "security": 18%

## Exceções documentadas
- Dev X teve 8 vulns (outlier), mas em código novo (legacy app rewrite) — contexto especial
- Dev Y teve 0 vulns (expertise segurança prévia) — baseline pode estar enviado

## Próxima fase
P2 — Synthetic threats, data: 2025-01-20
```

---

## 🧬 FASE 2 — P2: Synthetic Threat Generation

**Objetivo:** Criar cenários de ataque reais em lab/staging, confirmar que formação permite detecção.

**Duração:** 1-2 semanas de testes

### P2-1: Definir 5-10 Threat Types (Cenários)

**Baseado em baseline (P1):** Selecionar top vulnerabilidades encontradas

| # | Threat Type | OWASP | Contexto | Dificuldade |
|---|------------|-------|---------|------------|
| T1 | SQL Injection (UNION-based) | A9 | Login form | Fácil (3 min detect) |
| T2 | XSS (Stored) | A7 | Comment field | Fácil (2 min detect) |
| T3 | Authentication Bypass (JWT) | A7 | Token manipulation | Médio (5 min detect) |
| T4 | Insecure Direct Object Reference | A4 | User profile (id=N) | Médio (8 min detect) |
| T5 | API rate limit bypass | A4 | Registration endpoint | Difícil (15 min detect) |
| T6 | XXE injection | A4 | File upload XML | Difícil (20 min detect) |
| T7 | Command Injection | A9 | Backup script | Médio (10 min detect) |
| T8 | Insecure deserialization | A8 | Cache poisoning | Difícil (25 min detect) |

### P2-2: Implementar Cenários em Staging

**Staging App Setup:** Clone de produção com vulnerabilidades **injetadas propositalmente**

```yaml
# staging/vulnerable-app-config.yaml
vulnerabilities:
  - id: T1
    type: SQLi
    location: /login?user=X&pass=Y
    payload: "' OR '1'='1"
    detection_method: "query in logs shows UNION SELECT"
    
  - id: T2
    type: XSS
    location: /comments endpoint
    payload: "<img src=x onerror=alert(1)>"
    detection_method: "script tags in response, WAF alert"
    
  - id: T3
    type: JWT_bypass
    location: /api/profile
    payload: "JWT with alg=none or expired token with modified claims"
    detection_method: "audit log shows unexpected elevation"
```

### P2-3: Procedimento de Teste P2

**Por cada threat T1-T8:**

1. **Setup:** Ativar vulnerabilidade em staging
2. **Execução:** "Dê a um Dev 30 minutos para encontrar a vulnerabilidade"
3. **Medição:**
   - ✅ Detecção correta (Dev encontrou vulnerabilidade)
   - ⏱️ Tempo para detecção (min:sec)
   - 📝 Método usado (manual code review, scanner, fuzzing, etc.)
   - ❌ Não detectado em 30 min

4. **Resultado por Dev:**
```
P2 Results — Secure Coding L1 — Staging (2025-01-20 a 01-27)

┌──────────────┬──────┬──────┬──────┬──────┬──────┬──────┬──────┬──────┐
│ Dev          │ T1   │ T2   │ T3   │ T4   │ T5   │ T6   │ T7   │ T8   │
│              │ (SQLi│ (XSS)│ (JWT)│ (IDOR│ (Rate│ (XXE)│ (Cmd)│ (Deser
├──────────────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┤
│ João Silva   │ 3m   │ 2m   │ 5m   │ ✗    │ ✗    │ ✗    │ 12m  │ ✗    │
│ Maria Costa  │ 5m   │ 8m   │ ✗    │ 15m  │ ✗    │ ✗    │ ✗    │ ✗    │
│ Pedro Oliv.  │ 2m   │ 1m   │ 3m   │ 8m   │ ✗    │ ✗    │ 10m  │ ✗    │
│ Avg L1       │ 3.3m │ 3.7m │ 4m   │ 11.5m│ ✗    │ ✗    │ 11m  │ ✗    │
│ Threshold    │ ≤10m │ ≤10m │ ≤15m │ ≤20m │ ≤30m │ ≤30m │ ≤30m │ ≤30m │
└──────────────┴──────┴──────┴──────┴──────┴──────┴──────┴──────┴──────┘

Detection rate (baseline P2):
- T1-T4: 100% detection (fácil-médio)
- T5-T8: 0% detection (difícil) → Formação necessária em XXE, rate limiting, deserialization
```

---

## 🌍 FASE 3 — P3: Production Validation (Canary)

**Objetivo:** Se formação foi eficaz em staging, confirmar em produção com risco controlado.

**Duração:** 1-2 semanas (canary 1-5% tráfico)

### P3-1: Setup Canary

**Selecionar feature/app "in scope" for formação:**
- Ex: Payment API (L3), que recebeu "Secure API Design" training
- Canary: Ativar novas regras de validação/segurança em 1% dos requests

**Tráfico canary:**
```
Production traffic:
  - 99% old rules (baseline)
  - 1% new rules (post-training improvements)
  
Métrica: Erro rate, latência, security alerts
```

### P3-2: Procedimento P3

**Semana 1:**
1. Implementar melhorias de segurança recomendadas pela formação (ex: Input validation aprimorado)
2. Rodar em canary 1% tráfico
3. Medir: erro rate, latência, security alerts

**Métricas P3:**

| Métrica | Baseline (99% old) | Canary (1% new) | Aceitável | Resultado |
|---------|------------------|-----------------|-----------|-----------|
| Error rate | 0.5% | 0.5% | ≤0.7% | ✅ PASS |
| Latência p95 | 150ms | 155ms | ≤200ms | ✅ PASS |
| CPU/Memory | 45%/60% | 45%/62% | ≤60%/70% | ✅ PASS |
| Security alerts | 3/hora | 2/hora | ≤5/hora | ✅ PASS |

**Se PASS:** Expandir para 5% → 10% → 50% → 100%  
**Se FAIL:** Investigar, ajustar, reverter se necessário

### P3-3: Validação de Latência de Detecção

Se formação inclui "detecção de anomalias em real-time":

```
Latência de detecção pós-formação:
- Anomalia ocorre: 14:00:00
- Alert gerado: 14:00:05 (5 segundos)
- Resposta iniciada: 14:00:45 (45 segundos)
- Target: ≤1 min

p50 latência: 30 sec
p95 latência: 2 min
p99 latência: 5 min
```

---

## 📊 FASE 4 — P4: False Positive & False Negative Measurement

**Objetivo:** Após 1 semana pós-formação, classificar resultados reais.

**Duração:** 1 semana de análise

### P4-1: Recolher Amostra de Casos Reais

**Caso 1: Code Review com Security Feedback**

```markdown
## Case A1 — False Positive (Quiz high, Code issue)

**Dev:** João Silva
**Quiz Score:** 92% ("OWASP Top 10")
**Context:** PR para Payment processing, 250 linhas Java

### Code Review Feedback
- [ ] Line 45: SQL query with string concatenation → SQL Injection risk
- [ ] Line 78: Deserialization of untrusted data → Insecure Deserialization
- [ ] Line 120: Missing authentication check → Access Control

### Classificação
- **FP (False Positive):** Quiz score 92%, mas 3 security issues em código novo
- **Root cause:** Quiz mede OWASP Top 10 theory, não aplicação prática
- **Action:** Adicionar "lab hands-on" ao trilho, com code review feedback loop

### Métrica de correção
- **Pré-formação:** 2 issues/PR (avg)
- **Pós-formação:** Esperado 0.5 issues/PR
- **P4 resultado:** 1.8 issues/PR → Still high, formação inadequada

```

**Caso 2: False Negative (Quiz low, Code quality ok)**

```markdown
## Case B1 — False Negative (Quiz low, Code OK)

**Dev:** Maria Costa
**Quiz Score:** 68% (reproved) — "Secure API Design"
**Context:** PR para API rate limiting, 180 linhas Python

### Code Review Feedback
- [ ] Rate limit implementation: Correct exponential backoff
- [ ] Token validation: Proper JWT checks with expiration
- [ ] Error handling: No information disclosure in error messages
- [ ] Logging: Appropriate security event logging

### Classificação
- **FN (False Negative):** Quiz score 68%, mas código implementa práticas corretamente
- **Root cause:** Quiz é muito teórico (memorização), Maria tem experiência prática anterior
- **Action:** Reconhecer competência prévia, ajustar quiz para prático (code review de exemplo real)

### Métrica de reconhecimento
- **Maria:** Approved by exception para L2 despite 68% score
- **Quiz update:** Incluir practical scenario em vez de theory-only
```

### P4-2: V1 & V2 Templates de Classificação

#### Template V1: False Positive Handling

```markdown
## V1 — False Positive Analysis

**Caso ID:** FP-2025-Q1-001
**Data:** 2025-02-15
**Dev:** João Silva
**Formação:** OWASP Top 10 (Quiz 92%)

---

### Identificação de FP
- **Evidência:** High quiz score (92%) BUT 3 security issues em PR
- **Issue tipo:** SQL Injection (não coberto adequadamente em quiz)
- **Impacto:** Risco real em produção, formação ineficaz para SQL Injection context

---

### Root Cause Analysis
- [ ] Quiz inadequado (muito teórico, não prático)
- [ ] Formação não cobria contexto específico (SQL em Java + ORM)
- [ ] Falta de labs hands-on
- [ ] Feedback loop ausente (quiz result não conecta com code reality)

---

### Remediation Plan
1. **Imediato:** 1:1 pair programming com AppSec (SQL Injection fixes, 2h)
2. **Semana seguinte:** Lab prático "SQLi em Java" (2h)
3. **Feedback:** Code review de próximo SQL code com AppSec
4. **Retest:** Quiz revisado + code scenario em 2 semanas

**Owner:** AppSec Lead  
**SLA:** Remediation concluído em 30 dias (by 2025-03-15)

---

### Prevention (para evitar FPs futuros)
- [ ] Adicionar scenario-based questions ao quiz (ex: "Este código Java tem SQLi?")
- [ ] Incluir 2h labs em "SQL Injection em Java" no trilho
- [ ] Conectar quiz feedback com code review feedback (dev recebe score + link a PR issues)
- [ ] Retest formação: Labs + code review de caso real (não quiz apenas)

```

#### Template V2: False Negative / RCA Handling

```markdown
## V2 — False Negative Analysis & Root Cause

**Caso ID:** FN-2025-Q1-001
**Data:** 2025-02-20
**Dev:** Maria Costa
**Formação:** Secure API Design (Quiz 68% — reprovada)

---

### Identificação de FN
- **Evidência:** Low quiz score (68%, threshold 75%) BUT código implementa práticas corretamente
- **Competência:** Rate limiting, token validation, error handling, logging — all correct
- **Impacto:** False signal de incompetência, dev restringida de progression

---

### Root Cause Analysis

**RCA 1: Quiz inadequado?**
- Quiz questions: Múltipla escolha sobre OWASP API Top 10
- Contexto: Teórico, não prático
- Maria's knowledge: Experiência prévia (5 anos API security), consegue aplicar mesmo sem evocar teoria

**RCA 2: Experiência prévia não reconhecida?**
- ✅ Maria tem 2 anos projectos API-heavy
- ✅ Code reviews anteriores mostram "rate limiting correct" padrão
- ❌ Quiz not weighted para experiência prévia

---

### Remediation Plan
1. **Imediato:** Reconhecer competência prévia, aprove por exceção
2. **Feedback:** Explicar à Maria que quiz score baixo não reflete competência (quiz inadequado)
3. **Quiz update:** Converter para scenario-based (review code example, encontrar issues)
4. **Retest:** Maria toma quiz revisado (esperado 85%+)

**Owner:** AppSec + RH  
**SLA:** Resolução em 10 dias (by 2025-03-01)

---

### Prevention
- [ ] Pre-assessment: Verificar experiência prévia antes de quiz mandatory
- [ ] Quiz design: Incluir scenario-based questions (não theory-only)
- [ ] Bypass mechanism: If code review + incident history demonstram competência, waive quiz
- [ ] Feedback loop: Conectar quiz result com actual performance data

```

### P4-3: Métricas de Qualidade

Após análise de amostra (20-30 casos reais):

| Métrica | Target | P4 Resultado | Status |
|---------|--------|------------|--------|
| **FP Rate** | <20% (L1), <10% (L2), <5% (L3) | 18% | ✅ Acceptable |
| **FN Rate** | <15% (L1), <10% (L2), <5% (L3) | 12% | ✅ Acceptable |
| **Quiz-Code Correlation** | >0.7 | 0.65 | ⚠️ Weak (quiz needs update) |
| **Remedy Time (avg)** | <30 days | 25 days | ✅ Good |
| **Competency Confirmation** | >80% code quality post-training | 82% | ✅ Confirmed |

---

## 📈 FASE 5 — P5: Continuous Improvement

**Objetivo:** Após validação (P1-P4), implementar ciclo de melhoria contínua.

**Frequência:** Mensal (L1), Semanal (L2), Diária (L3)

### P5-1: Monthly Review Cycle (L1)

**Agenda Mensal:**

```
WEEK 1: Coleta de dados
  - Recolher vulnerabilidades encontradas (último mês)
  - Recolher quiz scores, code review feedback
  - Recolher incidentes relacionados a código
  
WEEK 2: Análise (GRC + AppSec)
  - Identificar FP/FN (templates V1/V2)
  - Calcular KPIs (taxa FP, FN, vulnerabilidade média)
  - Identificar gaps no trilho (ex: "XXE não é coberto, encontramos 2 casos")
  
WEEK 3: Decisão de melhoria
  - Atualizar conteúdo do trilho (adicionar, remover, resequenciar)
  - Atualizar quiz (adicionar scenario-based questions)
  - Atualizar labs (novo lab se gap identificado)
  
WEEK 4: Retest
  - Testar trilho atualizado com novo cohort de devs
  - Executar P2-P3-P4 novamente (synthetic + validation)
```

### P5-2: Proporcionalidade L1/L2/L3

| Nível | Baseline (P1) | Synthetic (P2) | Validation (P3) | FP/FN (P4) | Review Cycle |
|-------|---------------|----------------|-----------------|-----------|--------------|
| **L1** | Quarterly | Quarterly | Quarterly | Monthly | Monthly |
| **L2** | Biweekly | Monthly | Monthly | Weekly | Weekly |
| **L3** | Weekly | Weekly | Weekly | Daily | Daily |

### P5-3: Checklist de Atualização de Trilho

Se P4 identifica FP/FN > target:

```markdown
## Trilho Update Checklist — Secure Coding L1 — 2025-02

### FP/FN Analysis Result
- FP Rate: 18% (target <20%) — ACCEPTABLE
- FN Rate: 12% (target <15%) — ACCEPTABLE
- Gap identificado: XXE handling (encontradas 2 vulns, 0 antes) → ADD CONTENT

### Trilho Updates
- [ ] Content: Adicionar módulo "XXE Prevention" (30 min video + 15 min lab)
- [ ] Quiz: Adicionar 3 questions sobre XXE (scenario-based)
- [ ] Lab: Criar lab XXE attack/defense em DVWA
- [ ] Code example: Adicionar exemplo Java XML parsing seguro
- [ ] Test: Executar P2 scenario T8 (XXE) com novo trilho (target: 80%+ detection)

### Timeline
- Content prep: 2025-02-28
- Lab setup: 2025-03-07
- Pilot with 2 devs: 2025-03-10
- P2 validation: 2025-03-17
- Rollout: 2025-04-01

### Owner
- Content: AppSec (Maria)
- Lab: DevOps (Pedro)
- P2 Pilot: AppSec + QA (João)

---

## Retest Result (2025-03-17)
- [ ] P2 XXE detection rate: 85% (target 80%+) ✅ PASS
- [ ] Quiz FN rate: 8% (target <15%) ✅ GOOD
- [ ] Ready for rollout: YES

---

## Post-Rollout (April)
- [ ] Measure: 0 XXE vulns in April code reviews (vs. 2 in Feb)
- [ ] User satisfaction: 8/10+ from devs
- [ ] MTTR for XXE issues: <1 day (vs. 3 days avg pre-training)
```

### P5-4: KPIs Continuidade

**KPI-1: Eficácia de Formação (Reduction in Vulns)**
- **Target:** 30% redução em vulnerabilidades pós-formação (vs. baseline P1)
- **Frequência:** Mensal
- **Owner:** AppSec
- **Métrica:** (Vulns pré-formação - Vulns pós-formação) / Vulns pré-formação × 100

**KPI-2: FP/FN Rate**
- **Target:** FP <20% (L1), <10% (L2), <5% (L3); FN <15% (L1), <10% (L2), <5% (L3)
- **Frequência:** Semanal
- **Owner:** AppSec
- **Métrica:** Classificação manual de 20-30 casos reais/mês

**KPI-3: Quiz-Code Correlation**
- **Target:** >0.7 (high correlation = quiz predicts code quality)
- **Frequência:** Mensal
- **Owner:** AppSec
- **Métrica:** Pearson correlation coefficient (quiz score vs. code review issues)

**KPI-4: MTTR Improvement**
- **Target:** -30% MTTR (faster fixes pós-formação)
- **Frequência:** Mensal
- **Owner:** DevOps
- **Métrica:** Avg dias para fix (antes vs. depois formação)

**KPI-5: Incident Rate (Security)**
- **Target:** -25% security incidents causados por código
- **Frequência:** Trimestral
- **Owner:** GRC
- **Métrica:** # Incidentes /mês relacionados a code (pré vs. pós-formação)

---

## 📚 Integração com Cap 13 — Aplicação Lifecycle

| Fase SDLC | P1-P5 Trigger | Responsável | Ação |
|-----------|--------------|-------------|------|
| **Onboarding** | P1: Baseline incluído em plano onboarding | RH + AppSec | Recolher baseline pré-formação (vulnerabilidades, MTTR) |
| **Development** | P2-P4: Code review feedback loop | AppSec | Usar code review findings para corrigir FP/FN em trilho |
| **CI/CD** | P3: Canary + metrics | DevOps | Setup canary para validação pós-formação em staging/prod |
| **Audit** | P5: Monthly/quarterly review | GRC | Auditoria de P1-P5 execução, KPIs compliance |
| **Training Update** | P5: Trilho improvement | AppSec | Atualizar trilho baseado em P4 findings |

---

## 🔗 Cenário Real: P1-P5 Completo

**Trilho:** "Secure Coding L1" | **Cohort:** 12 Devs | **Período:** 2025-01-15 a 2025-03-31

---

### ✅ P1 — Baseline (2025-01-15 a 01-29)

```
Resultado:
- Avg vulnerabilidades: 2.1/dev
- Distribuição: 40% XSS, 35% SQLi, 25% outras
- MTTR: 4.2 dias
- Code review approval 1ª: 65%
```

---

### ✅ P2 — Synthetic (2025-02-01 a 02-14)

```
Resultado:
- T1 (SQLi): 100% detected (avg 3.2 min)
- T2 (XSS): 95% detected (avg 2.8 min)
- T3-T8: 0% detected (advanced topics)
- Recomendação: Trilho covers T1-T4, add labs para T5-T8
```

---

### ✅ P3 — Canary (2025-02-15 a 02-28)

```
Canary setup: 2% traffic with improved input validation
Resultado:
- Error rate: 0.5% (same as baseline) ✅
- Latência: 2ms overhead (acceptable) ✅
- Security alerts: 1.5/hora (vs. 3/hora baseline) ✅
- Expand to 10% → 50% → 100% (by 2025-03-10)
```

---

### ✅ P4 — FP/FN (2025-03-01 a 03-07)

```
Resultado (amostra 25 casos):
- FP: 4 casos (16%, target <20%) ✅ Acceptable
- FN: 3 casos (12%, target <15%) ✅ Acceptable
- Quiz-code correlation: 0.72 (target >0.7) ✅ Good
- KPI status: GREEN

Ações remediação:
- 2 FP cases: Pair programming + labs (pair-prog-2025-03.md)
- 1 FN case: Reconhecer competência prévia
```

---

### ✅ P5 — Continuous (2025-03-08+)

```
Monthly reviews:
- 2025-03-31: Vulnerabilidade 1.8/dev (vs. 2.1 baseline) → -14% ✅
- 2025-04-30: Vulnerabilidade 1.5/dev → -28% (approaching target -30%)
- 2025-05-31: Vulnerabilidade 1.4/dev → -33% ✅ TARGET MET

Trilho updates:
- Added XXE lab (February gap found)
- Updated quiz with scenario-based questions (March improvement)

Proposta ciclo: Continuar monitoramento + trimestral retest (synthetic P2)
```

---

## 📋 Checklist Final de Implementação

- [ ] P1 baseline recolhida e documentada para cada trilho L1/L2/L3
- [ ] P2 synthetic test scenarios documentados (T1-T8 ou equivalent)
- [ ] P2 staging environment com vulnerabilidades injetadas pronto
- [ ] P3 canary framework setup (1-5% traffic staging)
- [ ] P4 V1/V2 templates para FP/FN analysis documentados
- [ ] P4 manual classification procedure definida (20-30 casos/mês)
- [ ] P5 monthly review cycle agendado (data fixa, participantes, template)
- [ ] KPI dashboard criado (5 métricas tracked)
- [ ] Training para AppSec/GRC em P1-P5 framework — 2h workshop
- [ ] Audit trimestral de P1-P5 execução programado

---

## 🎯 Referências & Ligações

- [Decisão Estruturada em Atribuição](addon/addon-11-decisao-estruturada-formacao-cap13.md) ← I1 framework
- [Trilhos Formativos por Função](addon/02-trilho-formativo)
- [KPIs de Capacitação](aplicacao-lifecycle.md#US-14) — Reporte de formação
- [Papéis e Responsabilidades](/sbd-toe/000-teory-of-everything/07-roles) — Cap 13

