---
id: addon-23-melhoria-continua-ameacas
title: "📈 Addon-23 — Melhoria Contínua em Threat Modeling (I5: Continuous Improvement)"
description: Framework para análise pós-incidente, lições aprendidas e evolução do modelo de ameaças
tags: [I5, melhoria-continua, threat-modeling, lições-aprendidas, RCA, post-mortem, evolucao]
---

# 📈 Addon-23 — Melhoria Contínua em Threat Modeling (I5)

## 🎯 Objetivo

Instituir um **framework de aprendizagem contínua** para capturar lições aprendidas de incidentes reais, falsos negativos, e evolução do threat landscape, realimentando o modelo de ameaças de forma sistemática.

Este addon implementa a **Framework I5** (Continuous Improvement and Lessons Learned) para Cap 03, complementando:
- **US-06**: Post-incident threat analysis e RCA
- **US-07**: Atualização contínua da baseline de ameaças
- **Governação**: Integração com GRC e compliance

---

## 📋 Problema e Contexto

### Problema
- ✗ Modelos de ameaça envelhecem e perdem relevância
- ✗ Incidentes reais não realimentam o threat model
- ✗ Falsos negativos ocorrem repetidamente
- ✗ Sem sistematização, aprendizagem fica dispersa
- ✗ Threat landscape evolui mas modelos ficam estáticos

### Contexto (Proporcionalidade)

| Nível | Frequência Review | Escalada Incidentes | Documentação |
|-------|-------------------|-------------------|--------------|
| **L1** | Anual | Informal | Checklist |
| **L2** | Trimestral | Formal (AppSec) | Documentada (Markdown) |
| **L3** | Mensal | Formal + CISO | Documentada + Auditada |

---

## 🧩 Estrutura: 4 Pilares de Melhoria Contínua

### Pilar 1: Análise Pós-Incidente (Post-Mortem)

#### 1.1 Trigger: Incidente ocorreu

Sempre que um **incidente de segurança** ocorre, realizar análise imediata:

```markdown
# threat-model/incidents/INC-2025-001-post-mortem.md

---
incident_id: "INC-2025-001"
date_detected: "2025-01-18"
date_resolved: "2025-01-18 14:30 UTC"
severity: "ALTA"
---

## 1. Resumo Executivo

**O que**: Conta de admin comprometida via JWT `alg:none`  
**Quando**: 2025-01-18, 09:30 UTC  
**Impacto**: 500 registos de cliente acedidos  
**Duração**: 5 horas  
**Causa Raiz**: JWT validation não rejeita `alg:none`

---

## 2. Linha Temporal (Timeline)

| Hora | Evento |
|------|--------|
| 09:30 | Alertas de acesso administrativo anómalo |
| 09:45 | Escalação a AppSec |
| 10:15 | Confirmação: JWT falso com `alg:none` |
| 12:00 | Conta de admin desativada, investigação iniciada |
| 14:30 | Fix deployed (JWT validation rejeita `alg:none`) |

---

## 3. Investigação Técnica (RCA — Root Cause Analysis)

### 3.1 Como o ataque aconteceu?

```
1. Atacante consegue JWT via social engineering / leak
2. Cria novo JWT com payload {"role":"admin", "alg":"none"}
3. API não valida algoritmo JWT, aceita `alg:none`
4. Atacante consegue acesso admin sem conhecer secret
```

### 3.2 Por que não foi previsto?

| Check | Status | Razão |
|-------|--------|-------|
| DFD incluía JWT? | ✅ Sim | Mas não especificava validação de alg |
| STRIDE aplicado? | ✅ Sim | Mas focou em "expiração" não em alg validation |
| Código review apanhou? | ❌ Não | Padrão jwt.decode() uses default (alg validation ativo em v2+) |
| SAST detetou? | ⚠️ Regra missing | Semgrep não tem rule para alg:none bypass |
| Teste manual? | ❌ Não | Não estava em validação roadmap |

### 3.3 Conclusão RCA

**Root Cause**: Validação de JWT `alg` não foi expl ícita  
**Contributing Factors**: Sem testes manuais, sem regra SAST específica  
**Why Not Caught Earlier**: Threat model focou em expiração, não em algoritmo

---

## 4. Lições Aprendidas (Lessons Learned)

### 4.1 O que saiu bem?

- ✅ Alertas funcionaram (detecção em 15 min)
- ✅ Resposta rápida (1h para fix deployed)
- ✅ Comunicação clara com clientes

### 4.2 O que não saiu bem?

- ❌ JWT validation não era explícita (assumed default)
- ❌ Sem teste manual de JWT bypass
- ❌ DFD não especificava "alg validation required"
- ❌ Semgrep rule missing para alg:none

### 4.3 Ações de Melhoria (Improvements)

| ID | Ação | Responsável | Prazo | Status |
|----|------|-------------|-------|--------|
| A1 | Adicionar ameaça TM-JWT-ALG ao modelo | AppSec | Imediato | ✅ Done |
| A2 | Criar Semgrep rule: jwt-alg-validation | AppSec | 1 semana | In Progress |
| A3 | Adicionar teste manual: JWT bypass em CI | QA | 2 semanas | Backlog |
| A4 | Revisar todas as libs JWT (3 serviços) | Dev | 3 semanas | Backlog |
| A5 | Atualizar DFD: explicitar validação JWT | Arch | 1 semana | In Progress |

---

## 5. Rastreabilidade e Escalação

### 5.1 Requisitos Gerados

- REQ-AUT-003: Validação de algoritmo JWT obrigatória
- REQ-AUT-015: Apenas algoritmos asimétricos (RS256, ES256)

### 5.2 Issues Criadas

- [PROJ-1234] Fix JWT alg:none validation (P0, 1d)
- [PROJ-1235] Add Semgrep rule jwt-alg-validation (P2, 3d)
- [PROJ-1236] Add JWT bypass test to CI (P1, 5d)

### 5.3 Integração com GRC

- Risk Register: Incidente registado, mitigação em progresso
- Compliance: GDPR incident notification (se aplicável)
- Insurance: Notificação obrigatória de incidente

---

## 6. Aprovações

| Papel | Aprovação | Data |
|-------|-----------|------|
| Security Lead | ✅ Approved | 2025-01-18 16:00 |
| Product Owner | ✅ Approved | 2025-01-18 16:30 |
| CISO (escalada L3) | ✅ Approved | 2025-01-19 09:00 |

---
```

---

### Pilar 2: Falsos Negativos como Feedback Loop

#### 2.1 Quando FN é descoberto

Toda vez que uma ameaça real não foi prevista:

```markdown
# threat-model/false-negatives/FN-2025-001-rca.md

---
threat_id: "TM-NEW-042" (created retroactively)
fn_discovery_date: "2025-01-18"
discovery_method: "Incident response"
severity: "CRÍTICA"
---

## Problem

**What**: Timing attack on password validation  
**Expected**: Threat model should have included this  
**Actual**: Not in DFD, not tested

## Analysis

### Why it wasn't caught?

1. **Threat Model Gap**: DFD focou em fluxo, não em timing attacks
2. **SAST Limitation**: Semgrep não cobre timing attacks
3. **Manual Testing Gap**: Teste de timing não estava em plano

### Severity Assessment

| Factor | Impact |
|--------|--------|
| Exploitability | ALTA: passível de automação |
| Business Impact | ALTA: admin password compromise |
| Detectability | BAIXA: sem logging de timing |

---

## Improvements

### Immediate (< 1 week)

1. **Code Fix**: Implementar constant-time password comparison
   ```python
   # BEFORE (vulnerable to timing attack)
   if password == stored_hash:
       return True
   
   # AFTER (constant-time comparison)
   return hmac.compare_digest(password, stored_hash)
   ```

2. **Threat Model Update**: Adicionar timing attack threat
   ```yaml
   - id: TM-TIM-001
     title: "Timing attack on password validation"
     category: "Cryptography"
     severity: "ALTA"
     mitigation: "Constant-time comparison required"
     test_method: "Manual timing analysis + code review"
   ```

### Medium-term (< 1 month)

3. **SAST Rule**: Criar rule Semgrep para timing attacks
   ```yaml
   rules:
     - id: timing-attack-comparison
       pattern: |
         $X == $Y
       message: "Direct comparison may be vulnerable to timing attacks"
       languages: [python, javascript]
   ```

4. **Manual Test**: Adicionar teste de timing ao plano
   ```python
   import time
   
   correct_pass = "admin123"
   test_passes = [
       "a" * len(correct_pass),  # Wrong length
       "wrong_password",          # Wrong content
       correct_pass               # Correct
   ]
   
   timings = []
   for pwd in test_passes:
       start = time.perf_counter()
       validate_password(pwd)  # Function under test
       elapsed = time.perf_counter() - start
       timings.append((pwd, elapsed))
   
   # If timing differs significantly → VULNERABLE
   ```

### Long-term (< 3 months)

5. **Process Improvement**: Integrar timing attacks na DFD
6. **Training**: Workshop sobre ameaças criptográficas

---

## Integration Points

- **Threat Model**: Add TM-TIM-001 with `test_method: "manual_timing"`
- **CI/CD**: Validação de constant-time comparison em código
- **Training**: Casestory de timing attack no onboarding
```

---

### Pilar 3: Revisão Periódica de Threat Model

#### 3.1 Gatilho: Revisão mensal/trimestral

```markdown
# threat-model/reviews/REVIEW-2025-Q1.md

---
review_date: "2025-01-31"
reviewer: "AppSec Lead + Security Architect"
period: "January 2025"
---

## Executive Summary

- **Total Threats**: 42
- **New Threats Identified**: 3 (timing attacks, data exfiltration via logs)
- **Threats Mitigated**: 8
- **Threats Residual**: 5 (escalada a CISO)
- **Falsos Negativos**: 1 (timing attack)
- **Model Health Score**: 8.2/10 (↑ from 7.8 in Dec)

---

## Threat Landscape Changes

### External Threats (Q1 2025)

| Source | Finding | Impact | Action |
|--------|---------|--------|--------|
| MITRE ATT&CK | Supply chain attacks (SCA updates) | ALTA | Add to DFD: dependency scanning |
| OWASP Top 10 2024 | AI/LLM injection attacks | ALTA | Create new threat category |
| CWE Top 25 | CWE-434 Upload of Dangerous File | MÉDIA | Review file upload logic |
| Industry Reports | Prompt injection in AI apps | CRÍTICA | Plan AI security submodule |

### Internal Threats (Q1 2025)

| Source | Finding | Impact | Action |
|--------|---------|--------|--------|
| Incident Analysis | Timing attack on auth | CRÍTICA | Add FN-2025-001 |
| Pentesting | Weak CORS policy | ALTA | Fix in v1.2 |
| Code Review | Hardcoded API key in config | CRÍTICA | Rotate keys + use secrets manager |

---

## Threat Model Updates

### Added Threats
- TM-TIM-001: Timing attack on password validation
- TM-LLM-001: Prompt injection in AI integration
- TM-FILE-001: Upload of dangerous file types

### Updated Threats
- TM-JWT-001: Enhanced validation checks
- TM-CORS-001: Scope reduction

### Removed/Obsoleted
- TM-LEGACY-001: (technology deprecated in v1.0)

---

## Metrics and KPIs

| Metric | Jan | Feb | Target |
|--------|-----|-----|--------|
| Threat Identification Rate | 42 | +3 | ↑ 10% per quarter |
| Mitigation Rate | 8/10 = 80% | 85% | ≥90% |
| FN Discovery Rate | 1 | 0 | <1 per quarter |
| Model Age (days) | 31 | | <60 days |
| Coverage (L3 apps) | 95% | | 100% |

---

## Recommendations for Next Quarter

1. **Urgent**: Implement AI/LLM threat submodule
2. **High**: Enhance SCA integration in threat model
3. **Medium**: Conduct pentesting for timing attacks
4. **Training**: Security team briefing on OWASP 2024

---

## Sign-off

- **Reviewed by**: João Silva (AppSec Lead) ✅
- **Approved by**: Maria Santos (Product Owner) ✅
- **Archived**: threat-model/reviews/REVIEW-2025-Q1.md
```

---

### Pilar 4: Evolução Automática da Baseline

#### 4.1 Automação: Atualização de regras SAST

```python
# threat-model/scripts/update_sast_rules.py

import requests
import yaml
from datetime import datetime

def fetch_latest_cwe_top_25():
    """Buscar Top 25 CWE mais recente"""
    # MITRE CWE API
    response = requests.get("https://cwe.mitre.org/top25/latest.json")
    return response.json()

def fetch_owasp_top_10():
    """Buscar Top 10 OWASP 2024"""
    # (implementar fetch)
    pass

def generate_semgrep_rules(cwe_list, owasp_list):
    """Gerar rules Semgrep baseadas em CWE/OWASP"""
    rules = []
    
    for cwe in cwe_list:
        rule = {
            "id": f"custom-{cwe['id'].lower()}",
            "title": cwe['name'],
            "severity": map_severity(cwe['severity']),
            "pattern": generate_pattern(cwe['id']),  # placeholder
            "message": f"Potential {cwe['name']} vulnerability",
            "languages": ["python", "javascript"]
        }
        rules.append(rule)
    
    return rules

def update_baseline():
    """Atualizar baseline automaticamente"""
    cwe_list = fetch_latest_cwe_top_25()
    owasp_list = fetch_owasp_top_10()
    
    new_rules = generate_semgrep_rules(cwe_list, owasp_list)
    
    # Atualizar ficheiro
    with open("threat-model/baselines/semgrep-cwe-top-25.yaml", "w") as f:
        yaml.dump(new_rules, f)
    
    # Commit automático
    os.system(f"git add threat-model/baselines/")
    os.system(f"git commit -m 'chore: update SAST rules from CWE Top 25 ({datetime.now().date()})'")
    os.system(f"git push")
    
    print(f"✅ Updated {len(new_rules)} rules")

if __name__ == "__main__":
    update_baseline()
```

#### 4.2 CI/CD Trigger: Monthly rule update

```yaml
# .github/workflows/update-threat-baseline.yml

name: Update Threat Modeling Baseline

on:
  schedule:
    # Run monthly
    - cron: '0 9 1 * *'
  workflow_dispatch:

jobs:
  update-baseline:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Fetch latest CWE Top 25
        run: |
          python threat-model/scripts/update_sast_rules.py
      
      - name: Run validation
        run: |
          semgrep --validate threat-model/baselines/
      
      - name: Create PR with updates
        uses: peter-evans/create-pull-request@v5
        with:
          commit-message: 'chore: update threat baseline from latest CWE/OWASP'
          title: '[Automated] Update threat baseline'
          body: |
            Updated threat modeling baseline from latest MITRE CWE Top 25 and OWASP Top 10.
            
            Please review and merge if changes are relevant to your application.
          branch: threat-model-baseline-update
          labels: 'threat-modeling'
```

---

## 📊 Estrutura de Armazenamento

```
threat-model/
├── incidents/
│   ├── INC-2025-001-post-mortem.md
│   └── INC-2025-002-post-mortem.md
├── false-negatives/
│   ├── FN-2025-001-rca.md
│   └── FN-2025-002-rca.md
├── reviews/
│   ├── REVIEW-2025-Q1.md
│   ├── REVIEW-2025-Q2.md
│   └── REVIEW-2025-ANNUAL.md
├── baselines/
│   ├── semgrep-cwe-top-25.yaml (auto-updated)
│   └── dfd-patterns/<arch-type>.yaml
├── lessons-learned/
│   ├── LL-2025-001-jwt-validation.md
│   ├── LL-2025-002-timing-attacks.md
│   └── LESSONS-LEARNED-2025.md
└── metrics/
    ├── threat-modeling-metrics.csv
    └── dashboard-data.json
```

---

## Métricas de Sucesso (I5)

### Indicadores

| Métrica | Meta | Frequência |
|---------|------|-----------|
| Incidentes relacionados a threat model | 0 (L3), <2/ano (L2) | Trimestral |
| Tempo meio entre falso negativo descoberta | >6 meses | Trimestral |
| Taxa de atualização do threat model | ≥1x/trimestre | Mensal |
| Ações de melhoria implementadas | ≥75% | Mensal |
| Cobertura de OWASP Top 10 | 100% | Trimestral |
| Cobertura de CWE Top 25 | ≥80% | Trimestral |

### Dashboard

```
📈 Threat Modeling Improvement Dashboard

├─ Model Health Score: 8.2/10
├─ Incidents (YTD): 1 (resolved)
├─ FN Discovered: 1 (RCA done)
├─ Recent Updates: 3 (Jan 2025)
├─ Coverage:
│  ├─ OWASP Top 10: 100% ✅
│  ├─ CWE Top 25: 92%
│  ├─ MITRE ATT&CK: 78%
│  └─ Industry-specific: 85%
└─ Status: 🟢 Healthy
```

---

## Integração com Processos Existentes

### Ligação com GRC

- **Risk Register**: Incidentes escalados automaticamente
- **Compliance**: Post-mortems são evidência auditável
- **Insurance**: Relatórios RCA para documentação

### Ligação com Desenvolvimento

- **Backlog**: Ações de melhoria criadas como issues
- **CI/CD**: Validação de threat model em cada release
- **Runbooks**: Lições aprendidas integradas em playbooks

### Ligação com Treinamento

- **Casestories**: Incidentes reais usados no onboarding
- **Security Workshops**: Lições aprendidas apresentadas trimestralmente
- **Knowledge Base**: Documentação pública de ameaças descobertas

---

## 📚 Referências

| Recurso | Descrição |
|---------|-----------|
| NIST SP 800-61 | Computer Security Incident Handling Guide |
| Google SRE Book - Postmortems | Blameless postmortem culture |
| OWASP Risk Assessment | Metodologia de priorização |
| MITRE ATT&CK Framework | Ameaças e técnicas de ataque |

---

## 🎯 Checklist de Implementação (I5)

- [ ] Post-mortem template criado e comunicado
- [ ] False negative RCA process implementado
- [ ] Revisão mensal de threat model agendada
- [ ] Automação de baseline SAST configurada
- [ ] Dashboard de métricas integrado
- [ ] Primeiros 3 post-mortems completos
- [ ] Lições aprendidas comunicadas à equipa
- [ ] Feedback integrado na próxima iteração do threat model

---

**Versão**: 1.0  
**Última Atualização**: Jan 2025  
**Mantido por**: AppSec + DevSecOps Team  
