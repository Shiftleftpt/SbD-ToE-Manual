---
id: addon-20-decisao-arquitetura
title: "🎯 Addon-20 — Decisão Estruturada em Arquitetura (I3: Enhanced Decision-Making)"
description: Framework de decisão para ADRs (Architecture Decision Records) com aprovação e rastreabilidade
tags: [I3, arquitetura, ADR, decisao-estruturada, governance, trade-offs]
---

# 🎯 Addon-20 — Decisão Estruturada em Arquitetura (I3)

## 🎯 Objetivo

Instituir um **framework formal de decisão arquitetónica** baseado em **Architecture Decision Records (ADRs)** para documentar, avaliar e aprovar decisões de segurança na arquitetura, garantindo rastreabilidade, análise de trade-offs e conformidade com padrões.

Este addon implementa a **Framework I3** (Enhanced Decision-Making and Governance) para Cap 04, complementando:
- **US-08**: Decisões de arquitetura com análise de segurança
- **US-09**: Sincronização threat model ↔ arquitetura
- **Governação**: Integração com strategy e compliance

---

## 📋 Problema e Contexto

### Problema
- ✗ Decisões de arquitetura são tomadas informalmente ou sem documentação
- ✗ Sem rastreabilidade, é impossível justificar trade-offs posteriores
- ✗ Segurança é consideração tardia, não parte da decisão
- ✗ Sem matriz de decisores, aprovações são inconsistentes
- ✗ Decisões antigas não são revisitadas (arquitetura envelhece)

### Contexto (Proporcionalidade)

| Nível | Documentação | Aprovações | Review Freq |
|-------|-------------|-----------|-------------|
| **L1** | ADR simplificado | Informal | Anual |
| **L2** | ADR formal | Formal (Arch) | Trimestral |
| **L3** | ADR detalhado com RCA | Formal (Arch + CTO) | Mensal |

---

## 🧩 Estrutura: ADR com Segurança

### Template ADR (Architecture Decision Record)

```markdown
# ADR-001: Escolher API Gateway como Control Point de Autenticação

**Status**: DECIDED (ACCEPTED / REJECTED / DEPRECATED)  
**Date**: 2025-01-15  
**Decision Maker**: Arquiteto Lead + AppSec Lead  

---

## Context

Aplicação tem 8 microserviços com diferentes requisitos de autenticação.  
Necessitamos de um **ponto centralizado** para validação de JWT, rate limiting e logging.

### Current Architecture
```
┌─────────────────────────────────────┐
│        Client Apps                  │
└──┬──────┬──────┬─────────┬──────────┘
   │      │      │         │
   ▼      ▼      ▼         ▼
┌─────┐┌─────┐┌─────┐ ┌──────┐
│ MS1 ││ MS2 ││ MS3 │ │ MS4  │
└─────┘└─────┘└─────┘ └──────┘
   (Each validates JWT independently)
   ❌ Redundant, inconsistent, hard to audit
```

---

## Decision

### Options Evaluated

| Option | Pros | Cons | Security | Effort | Cost |
|--------|------|------|----------|--------|------|
| **A: API Gateway (Nginx/Kong)** | Centralized, reusable, audit trail | Added latency | ⭐⭐⭐⭐⭐ | 1w | Low |
| **B: Service Mesh (Istio/Linkerd)** | Decentralized, resilient, mTLS | Complex, learning curve | ⭐⭐⭐⭐ | 3w | Medium |
| **C: Each Service (status quo)** | Simple, minimal latency | Inconsistent, audit gap | ⭐⭐ | 0 | 0 |
| **D: API Gateway + Service Mesh** | Best of both | Expensive, overhead | ⭐⭐⭐⭐⭐ | 4w | High |

### Selected Option

**✅ DECISION: A — API Gateway (Kong)**

### Rationale

1. **Security**: Centralized JWT validation + rate limiting
2. **Audit Trail**: All authentication attempts logged in one place
3. **Cost/Effort**: Manageable, ROI within 1 quarter
4. **Operational**: Familiar technology, less learning curve
5. **Threat Model**: Aligns with threat modeling (centralized control point)

---

## Security Analysis

### Threat Mitigations

| Threat | Current | With API GW | Mitigation Status |
|--------|---------|------------|------------------|
| Unauthorized access | Each service | API GW validates JWT | ✅ IMPROVED |
| JWT bypass | Inconsistent | Centralized validation | ✅ IMPROVED |
| Rate limiting | None | API GW enforces | ✅ NEW |
| Audit trail | Fragmented | Centralized logging | ✅ IMPROVED |
| Service-to-service auth | mTLS per pair | mTLS via service mesh (future) | ⏳ FUTURE |

### Security Decisions (Linked to Requirements)

- **REQ-AUT-001**: JWT validation mandatory → API GW enforces
- **REQ-AC-015**: Rate limiting 100 req/min → API GW enforces
- **REQ-LOG-005**: All auth attempts logged → API GW writes to centralized log

### Trade-offs

| Trade-off | Impact | Mitigation |
|-----------|--------|-----------|
| Added latency (5-10ms) | Acceptable (< 1% overhead) | Cache responses for public endpoints |
| Single point of failure | Risk escalated to CRÍTICA | Deploy HA (3x replicas, auto-failover) |
| New attack surface | Risk of misconfig | Security hardening checklist + IaC validation |

---

## Consequences

### Positive
- ✅ Centralized authentication control
- ✅ Audit trail for compliance (GDPR, SOC2)
- ✅ Faster onboarding of new microservices
- ✅ Rate limiting protects backend services

### Negative
- ❌ Additional latency (mitigated by cache)
- ❌ New operational component to manage
- ❌ Kong licensing cost (mitigated by open-source)

### Risks

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|-----------|
| API GW misconfiguration | ALTA | CRÍTICA | Security hardening checklist + IaC |
| API GW compromise | BAIXA | CRÍTICA | Harden, monitor, rate limit attack traffic |
| Performance degradation | MÉDIA | ALTA | Load testing, cache tuning |

---

## Implementation Roadmap

### Phase 1: Design (Week 1)
- [ ] DFD updated with API GW
- [ ] Security hardening checklist created
- [ ] Threat model updated (API GW as control point)
- [ ] Estimated effort: 3 days

### Phase 2: Development & Testing (Weeks 2-3)
- [ ] Kong deployment (dev/staging)
- [ ] JWT validation rules configured
- [ ] Rate limiting policies defined
- [ ] Security tests written
- [ ] Estimated effort: 10 days

### Phase 3: Hardening (Week 4)
- [ ] Security review & penetration testing
- [ ] Compliance validation (GDPR, SOC2)
- [ ] Documentation updated
- [ ] Estimated effort: 5 days

### Phase 4: Production Rollout (Week 5)
- [ ] Canary deployment (10% traffic)
- [ ] Monitoring active
- [ ] Rollback plan tested
- [ ] Estimated effort: 2 days

---

## Approvals & Governance

### Approval Matrix

| Approver | Role | Approval | Date | Comments |
|----------|------|----------|------|----------|
| João Silva | Architecture Lead | ✅ APPROVED | 2025-01-15 | Aligns with strategy |
| Ana Martins | Security Lead | ✅ APPROVED | 2025-01-15 | Mitigates TM-AUTH-001 |
| Miguel Santos | DevOps Lead | ✅ APPROVED | 2025-01-16 | Operationally feasible |
| Carlos Neves | Product Lead | ✅ APPROVED | 2025-01-16 | Acceptable timeline |
| CEO/CISO (if needed) | — | — | — | Not escalated (non-critical) |

### Sign-off
- **ADR Status**: ACCEPTED
- **Decision Date**: 2025-01-15
- **Effective Date**: 2025-02-15 (after Phase 3 testing)
- **Review Date**: 2025-04-15 (3-month post-implementation review)

---

## Traceability

### Linked to Threat Model
- Threat TM-AUTH-001: "Unauthorized access via JWT bypass"
  - Mitigation: API GW centralizes JWT validation
  - Status: MITIGATED via this decision

### Linked to Requirements
- REQ-AUT-001: JWT validation mandatory
- REQ-AC-015: Rate limiting enforcement
- REQ-LOG-005: Centralized auth logging
- REQ-OP-012: High availability requirement

### Linked to Architecture
- Service A (User Service): Uses API GW
- Service B (Order Service): Uses API GW
- Service C (Payment Service): Uses API GW

### Linked to Implementation
- Jira Epic: [PROJ-500] API Gateway Implementation
- Jira Task: [PROJ-501] Kong deployment
- Jira Task: [PROJ-502] Security hardening
- GitHub: [Feature Branch] api-gateway-integration

---

## Governance & Monitoring

### Post-Implementation Review

Scheduled for 2025-04-15 (3 months after implementation):

- [ ] Latency impact < 1% (measure)
- [ ] Availability 99.99% uptime
- [ ] Zero security incidents related to API GW
- [ ] All threat model mitigations verified
- [ ] Cost within budget

### Superseded Decisions

This ADR supersedes:
- ADR-001 (deprecated): Per-service authentication (2024-06)

### Related ADRs

- ADR-002: Service Mesh Evaluation (future)
- ADR-003: Secret Management Strategy
- ADR-004: Observability & Logging

---

## References

- [OWASP API Security Top 10](https://owasp.org/www-project-api-security/)
- [Kong Security Best Practices](https://docs.konghq.com/)
- [Threat Model: TM-AUTH-001](../../threat-modeling/canon/50-ameacas-mitigadas.md)
- [TOGAF Architecture Decision Records](https://www.opengroup.org/togaf)
```

---

## Estrutura de Diretórios ADRs

```
src/architecture/adr/
├── 001-api-gateway-selection.md
├── 002-database-encryption-at-rest.md
├── 003-zero-trust-networking.md
├── 004-service-to-service-authentication.md
├── 005-audit-logging-strategy.md
├── _index.md  (lista de todas ADRs)
└── README.md  (guia de criação)
```

---

## Matriz de Decisores por Tipo de Decisão

| Tipo de Decisão | Exemplos | Aprovadores | SLA |
|------------------|----------|------------|-----|
| **Crítica** (segurança) | Zero-trust, mTLS, encryption | Arch + AppSec + CTO | <24h |
| **Alta** (performance) | Caching, DB sharding, load balancing | Arch + DevOps | <48h |
| **Média** (funcional) | API design, pattern selection | Arch | <5 dias |
| **Baixa** (técnica) | Library choice, tool adoption | Arch + Dev | <10 dias |

---

## Métricas de Sucesso (I3)

### Indicadores

| Métrica | Meta | Como Medir |
|---------|------|-----------|
| % Decisões documentadas em ADR | 100% (L2/L3) | Count ADRs / total architectural decisions |
| Tempo médio aprovação ADR | <5 dias (crítica), <10 dias (alta) | Timestamp aprovação - data submissão |
| % ADRs com análise de segurança | 100% | Count "Security Analysis" section |
| % ADRs com aprovação formal | 100% | Count approvals em ADR |
| Taxa de revisão ADRs | ≥1x/trimestre | Count ADRs revistos / trimestre |

---

## 🎯 Checklist de Implementação (I3 - Cap 04)

- [ ] Template ADR criado e comunicado
- [ ] Matriz de decisores definida
- [ ] Primeiras 10 ADRs documentadas retroativamente
- [ ] Workflow de aprovação configurado
- [ ] ADRs integradas em CI/CD (validação de referência)
- [ ] Relatório mensal de ADRs gerado
- [ ] Treinamento para arquitetos realizado
- [ ] Feedback do time incorporado

---

**Versão**: 1.0  
**Última Atualização**: Jan 2025  
**Mantido por**: Architecture Team  
