---
id: addon-23-decisao-dependencias
title: "🎯 Addon-23 — Decisão Estruturada em Dependências (I3: Enhanced Decision-Making)"
description: Framework de decisão para aprovação e exceção de dependências com justificação documentada
tags: [I3, dependencias, sbom, governance, decisao-estruturada, matriz-decisores]
---

# 🎯 Addon-23 — Decisão Estruturada em Dependências (I3)

## 🎯 Objetivo

Instituir um **framework formal de decisão** para aprovação de novas dependências e formalização de exceções de SCA, garantindo que cada dependência (OSS, comercial, interna) é avaliada segundo critérios claros e aprovada por stakeholders apropriados.

Este addon implementa a **Framework I3** (Enhanced Decision-Making and Governance) para Cap 05, complementando:
- **Política de Dependências**: Critérios de aceitação
- **Exceções SCA**: Justificação formal de CVEs aceites
- **Governação**: Integração com compliance e supply chain

---

## 📋 Problema e Contexto

### Problema
- ✗ Dependências são adicionadas sem avaliação formal
- ✗ Sem matriz de decisores, aprovações são inconsistentes
- ✗ Exceções de CVE não são documentadas ou revisadas
- ✗ Falta rastreabilidade entre dependência e requisito técnico
- ✗ Dependências "shadow" (copiadas manualmente) escapam à governance

### Contexto (Proporcionalidade)

| Nível | Aprovação | Justificação | Auditoria |
|-------|-----------|-------------|-----------|
| **L1** | Informal | Simples | Anual |
| **L2** | Formal | Documentada | Trimestral |
| **L3** | Formal + Escalada | Completa | Mensal |

---

## 🧩 Estrutura: Matriz de Decisão para Dependências

### Fase 1: Avaliação de Nova Dependência

Antes de adicionar qualquer dependência, validar:

```yaml
# src/dependencies/decision-template.yaml

---
dependency:
  name: "lodash"
  version: "4.17.21"
  type: "npm"  # npm, python, maven, go, etc.
  source: "https://www.npmjs.com/package/lodash"
  
evaluation_date: "2025-01-15"
evaluated_by: "Developer (João) + Tech Lead (Ana)"

# Checklist de Aceitação
evaluation:
  
  # 1. Necessidade
  necessity:
    required: true
    rationale: "Utility library para manipulação de arrays/objects"
    alternative_evaluated: false
    comments: "Alternativa: usar array methods nativas (ES6+), mas lodash oferece mais garantias"
  
  # 2. Manutenção
  maintenance:
    actively_maintained: true
    last_release_date: "2024-12-10"
    release_frequency: "monthly"
    community_size: "large"
    bus_factor: "good"  # Múltiplos maintainers
    comments: "Projeto bem mantido, comunidade ativa"
  
  # 3. Segurança
  security:
    known_vulnerabilities: 0
    vulnerability_history: "low"
    security_audit_available: false
    license_compatible: true  # MIT
    license_type: "MIT"
    comments: "Sem CVEs conhecidas, MIT license compatível com projeto"
  
  # 4. Qualidade
  quality:
    test_coverage: "high"
    code_quality_score: 8.5  # e.g., CDNJS rating
    downloads_monthly: 150000000
    github_stars: 29000
    dependents_count: 3000000
    comments: "Excellent quality, widely adopted"
  
  # 5. Tamanho/Performance
  size:
    bundle_size_kb: 69  # gzip: 17KB
    acceptable: true
    comments: "Reasonable size, minimal impact"
  
  # 6. Supply Chain Risk
  supply_chain:
    npm_2fa_enabled: true
    published_by_verified_owner: true
    recent_owner_changes: false
    ownership_concentration: "good"
    comments: "Publisher is verified, 2FA enabled"

# Conclusão
decision:
  status: "APPROVED"
  approved_by:
    - name: "Ana Silva"
      role: "Tech Lead"
      date: "2025-01-15"
    - name: "AppSec Lead"
      role: "Security Review"
      date: "2025-01-15"
  
  conditions:
    - add_to_lock_file: true
    - regular_updates_required: true
    - monitor_vulnerabilities: true
  
  justification: |
    Lodash is a well-maintained, widely-adopted utility library with no known vulnerabilities.
    The security review and community adoption justify the decision to include it.
    Regular monitoring via automated SCA tools will be in place.
```

---

### Fase 2: Matriz de Decisão por Tipo de Dependência

```yaml
# src/dependencies/decision-matrix.yaml

decision_matrix:
  
  development_dependencies:
    # Jest, mocha, prettier, eslint, etc.
    approval_required: true
    who_approves: "Tech Lead"
    sla: "1 day"
    concerns:
      - "Don't compromise production bundle size"
      - "Security vulnerabilities in devDeps can still leak via source maps"
    example_criteria:
      - "No known CVEs"
      - "Actively maintained"
      - "If building production artifacts, must exclude from bundle"
  
  production_dependencies:
    # Core libraries, frameworks
    approval_required: true
    who_approves: "Tech Lead + AppSec Lead"
    sla: "2 days"
    concerns:
      - "Must be actively maintained"
      - "CVE risk management essential"
      - "License compatibility check"
      - "Pinning to exact version"
    example_criteria:
      - "No CRITICAL/HIGH CVEs without acceptable risk"
      - "Monthly+ release cadence"
      - ">1K GitHub stars (adoption indicator)"
      - "License compatible (MIT, Apache 2.0, BSD)"
  
  critical_dependencies:
    # Authentication, crypto, database drivers
    approval_required: true
    who_approves: "Tech Lead + AppSec Lead + CTO (if enterprise)"
    sla: "3 days"
    concerns:
      - "Security audit may be required"
      - "Direct impact on security posture"
      - "Supply chain risk elevated"
    example_criteria:
      - "Zero CVEs acceptable (no exceptions)"
      - "Active security maintenance program"
      - "Security audit available or budget allocated"
      - "Pinning to exact version with mandatory reviews for updates"
      - "Ownership verified (no typosquatting)"
  
  internal_dependencies:
    # Internal libraries, shared code
    approval_required: true
    who_approves: "Tech Lead"
    sla: "1 day"
    concerns:
      - "Source available in repository"
      - "Version control and tagging required"
    example_criteria:
      - "Code review completed"
      - "Version tagged in Git"
      - "SCA run on internal lib"
```

---

### Fase 3: Formalização de Exceções SCA

Quando uma vulnerabilidade é aceite (sem mitigação):

```markdown
# src/dependencies/exceptions/CVE-2024-12345-lodash.md

---
cve_id: "CVE-2024-12345"
severity: "HIGH"
library: "lodash"
version: "4.17.21"
affected_versions: "<=4.17.21"
exception_date: "2025-01-15"
exception_expires: "2025-04-15"  # 90 days
---

## Vulnerability Details

**CVE-2024-12345: Prototype Pollution in lodash**

- **CVSS Score**: 7.5
- **CWE**: CWE-1321 (Prototype Pollution)
- **Description**: Lodash versions <=4.17.21 vulnerable to prototype pollution via set() function

---

## Business Justification

| Factor | Assessment |
|--------|-----------|
| **Exploitability** | MÉDIA (requires specific data input) |
| **Attack Vector** | LOCAL_NETWORK (internal data only) |
| **Affected Components** | None in our usage (we use array utilities, not set()) |
| **Fix Available** | Yes, but requires major version upgrade (breaking changes) |
| **Upgrade Effort** | HIGH (3+ days, significant API changes) |
| **Business Impact of Downtime** | CRÍTICA (e-commerce order processing) |

---

## Risk Assessment

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|-----------|
| Exploitation via set() | LOW | CRÍTICA | Code review: ensure set() not used with user input |
| Supply chain attack | BAIXA | CRÍTICA | npm 2FA, dependency lock file |
| Cascade to dependent apps | BAIXA | ALTA | Internal SCA scans |

---

## Approved Mitigations

### Compensating Controls

1. **Code Review**: Audit all usage of lodash.set() to ensure no untrusted input
   - [ ] Review completed by AppSec
   - [ ] No untrusted set() calls found
   - [ ] Comments added to code with CVE reference

2. **Input Validation**: Strict validation of all user inputs before lodash operations
   - [ ] Schema validation (JSON Schema / Zod)
   - [ ] Type guards enabled in TypeScript

3. **Monitoring**: Alert on prototype pollution attack patterns
   - [ ] WAF rule: detect unusual property access patterns
   - [ ] SIEM: monitor for error patterns matching exploit

4. **Upgrade Plan**: Schedule migration to lodash 4.17.22+ (if no breaking changes)
   - [ ] Evaluate breaking changes
   - [ ] Plan migration for Q2 2025
   - [ ] Test in staging environment

---

## Approval and Escalation

### Approval Matrix

| Approver | Role | Status | Date | Notes |
|----------|------|--------|------|-------|
| Tech Lead | Decision | ✅ APPROVED | 2025-01-15 | Code review completed, mitigations in place |
| AppSec Lead | Security | ✅ APPROVED | 2025-01-15 | Compensating controls acceptable |
| CTO | Executive | ✅ APPROVED | 2025-01-16 | Escalated due to severity |

---

## Expiration and Rework

**Exception Expiration**: 2025-04-15 (90 days)

### Before Expiration, Must:
- [ ] Evaluate lodash 4.17.22+ (check breaking changes)
- [ ] Decide: upgrade or request extension
- [ ] If extension: re-justify with latest security data

### Mandatory Upgrade Triggers:
- [ ] Exploit published for CVE-2024-12345
- [ ] New related CVE in lodash
- [ ] Failing security audit or compliance check

---

## Traceability

- **JIRA Issue**: [PROJ-1234] Lodash CVE-2024-12345 exception + mitigation plan
- **Pull Request**: [#567] Add code review comments for lodash.set()
- **Commit**: `refs #1234 security: add lodash CVE mitigations`
- **Risk Register**: Registered in GRC system with approval scan

---
```

---

## Fase 4: Automação de Decisão em CI/CD

```yaml
# src/dependencies/decision-engine.yml

name: Dependency Decision Gate

on:
  pull_request:
    paths:
      - 'package.json'
      - 'requirements.txt'
      - 'Gemfile'
      - 'pom.xml'

jobs:
  dependency-decision:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Detect new dependencies
        run: |
          # Compare with main branch to find new deps
          git fetch origin main
          python scripts/detect_new_dependencies.py > new-deps.json
      
      - name: Check if decision records exist
        run: |
          python scripts/validate_decision_records.py \
            --input new-deps.json \
            --decision-dir src/dependencies/decisions/ \
            --output validation-report.json
          
          # Fail if any new dep lacks decision record
          if grep -q "missing_decision" validation-report.json; then
            echo "::error::New dependencies lack decision records"
            exit 1
          fi
      
      - name: Validate exception records
        run: |
          python scripts/validate_exceptions.py \
            --input new-deps.json \
            --exceptions-dir src/dependencies/exceptions/ \
            --output exception-report.json
          
          # Check if any exceptions are expired
          if grep -q "expired" exception-report.json; then
            echo "::warning::Some dependency exceptions have expired"
          fi
      
      - name: Comment PR with decision status
        uses: actions/github-script@v6
        with:
          script: |
            const fs = require('fs');
            const report = JSON.parse(fs.readFileSync('validation-report.json', 'utf8'));
            
            github.rest.issues.createComment({
              issue_number: context.issue.number,
              owner: context.repo.owner,
              repo: context.repo.repo,
              body: `## Dependency Decision Gate Report\n\n${JSON.stringify(report, null, 2)}`
            });
```

---

## Métricas de Sucesso (I3)

### Indicadores

| Métrica | Meta | Como Medir |
|---------|------|-----------|
| % Dependências com decision record | 100% | Count decisions / total deps |
| % Exceções documentadas | 100% | Count exception files / exceptions |
| % Exceções revistas antes expirarem | 100% | Monitor expiration dates |
| Tempo médio aprovação | <2 dias | Timestamp aprovação - data submissão |
| Taxa de rejeição (dependencies blocked) | 5-10% | Count rejected / total PRs |

### Dashboard

```
📊 Dependency Decision Dashboard

├─ Total Dependencies: 127
├─ With Decision Records: 127 (100%) ✅
├─ Active Exceptions: 3
│  ├─ Expiring in <30d: 1 ⚠️
│  └─ Expired: 0 ✅
├─ Approval SLA:
│  ├─ <1 day: 85%
│  ├─ 1-2 days: 12%
│  └─ >2 days: 3%
└─ Status: 🟢 Compliant
```

---

## 🎯 Checklist de Implementação (I3 - Cap 05)

- [ ] Matriz de decisão criada e comunicada
- [ ] Template de decision record implementado
- [ ] Template de exception record implementado
- [ ] Workflow de aprovação documentado
- [ ] Primeiras 20 dependências avaliadas com decision records
- [ ] Exceções SCA documentadas para CVEs conhecidas
- [ ] Gate de CI/CD implementado
- [ ] Dashboard de conformidade criado
- [ ] Feedback da equipa incorporado

---

**Versão**: 1.0  
**Última Atualização**: Jan 2025  
**Mantido por**: Architecture + Governance Team  
