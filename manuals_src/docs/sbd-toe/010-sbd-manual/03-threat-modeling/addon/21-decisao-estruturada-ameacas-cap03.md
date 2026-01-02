---
id: addon-21-decisao-ameacas
title: "🎯 Addon-21 — Decisão Estruturada em Threat Modeling (I3: Enhanced Decision-Making)"
description: Framework de decisão documentada e governada para aceitar, adaptar ou rejeitar ameaças
tags: [I3, decisao-estruturada, threat-modeling, governance, matriz-decisores, rastreabilidade]
---

# 🎯 Addon-21 — Decisão Estruturada em Threat Modeling (I3)

## 🎯 Objetivo

Instituir um **framework formal de decisão** para avaliação sistemática de ameaças derivadas de threat modeling, garantindo que cada ameaça é **aceita, adaptada ou rejeitada com justificação documentada** e aprovação apropriada.

Este addon implementa a **Framework I3** (Enhanced Decision-Making and Governance) para Cap 03, complementando:
- **US-04**: Validação assistida de ameaças com decisão documentada
- **US-06**: Justificação formal de risco aceite

---

## 📋 Problema e Contexto

### Problema
- ✗ Ferramentas sugerem ameaças em massa, gerando fadiga de decisão
- ✗ Decisões não documentadas criam conflitos: "Por que este risco foi aceite?"
- ✗ Sem matriz de decisores, aprovações são inconsistentes
- ✗ Ameaças rejeitadas não são rastreadas, multiplicam-se discussões

### Contexto (Proporcionalidade)

| Nível | Urgência | Necessidade de Matriz | Aprovações |
|-------|----------|----------------------|------------|
| **L1** | I1-I2 | Simplificada | Informal (Arquiteto) |
| **L2** | I1-I3 | Completa | Formal (AppSec + PO) |
| **L3** | I1-I5 | Completa + Escalada | Formal + CTO/CISO |

---

## 🧩 Estrutura: Matriz de Decisão para Ameaças

### Fase 1: Avaliação Inicial (Critérios de Aceitação)

Antes de aceitar uma ameaça, validar:

| Critério | Questão | Impacto |
|----------|---------|--------|
| **Relevância** | Esta ameaça é aplicável ao contexto desta app? | Rejeitar se: contexto diferente ou tecnologia não usada |
| **Exposição** | Existe fluxo de dados que expõe este componente? | Rejeitar se: DFD não contém fluxo mencionado |
| **Detetabilidade** | É possível detetar tentativa de exploração? | Adaptar: com logging/monitorização |
| **Impacto Real** | Qual é o impacto se explorada? | Rejeitar se: impacto < L1 classification |
| **Controlo Existente** | Há controlo mitigador já implementado? | Adaptar: se parcial; Aceitar: se completo |
| **Urgência** | Quando este risco deve ser mitigado? | Rejeitar: se nenhuma exposição atual |

### Fase 2: Matriz de Decisão Contextualizada

**Template de decisão por ameaça:**

```yaml
# threat-model/decisions/TM-GEN-XXX-decision.md

---
threat_id: "TM-GEN-042"
title: "JWT com alg:none permite falsificação de sessão"
source: "IriusRisk / Ferramenta"
severity: "CRÍTICA"
components_affected:
  - API Gateway
  - Auth Service
date_raised: "2025-01-15"
---

## 1. Avaliação Inicial

### 1.1 Critérios de Aceitação

| Critério | Pergunta | Resposta | Evidência |
|----------|----------|----------|-----------|
| **Relevância** | Usamos JWT nesta app? | ✅ Sim | api/auth/jwt-handler.ts |
| **Exposição** | DFD contém API → Auth → DB? | ✅ Sim | ameacas/dfd-api-flow.drawio |
| **Detetabilidade** | Podemos detetar `alg:none`? | ✅ Sim (SAST) | Semgrep rule: jwt-alg-validation |
| **Impacto Real** | Qual impacto se falsa sessão? | 🔴 CRÍTICA | Acesso a dados sensíveis |
| **Controlo Existente** | JWT validation já existe? | ⚠️ Parcial | Verifica assinatura, mas não nega `alg:none` |
| **Urgência** | Deve ser mitigado agora? | ✅ Sim | Exposição de API pública |

**Conclusão**: ✅ **ACEITAR** — Ameaça é real, relevante, e necessita mitigação imediata.

### 1.2 Decisão (ACEITAR/ADAPTAR/REJEITAR)

- **Decisão**: `ACEITAR`
- **Justificação**: Ameaça é aplicável, exponibilidade real e impacto crítico.
- **Controlo Proposto**: Rejeitar explicitamente `alg:none` em validação JWT.

---

## 2. Mapeamento para Requisitos

| Requisito Gerado | Categoria (Cap.2) | Prioridade | Status | Ligação |
|------------------|-------------------|-----------|--------|---------|
| `REQ-AUT-003` | Autenticação e Sessões | P0 | Em Design | [Link Jira] |
| `REQ-AUT-015` | Assinatura JWT obrigatória | Autenticação e Sessões | P0 | [Link Backlog] |

---

## 3. Caminho de Mitigação

### Opção A: Implementação de Controlo
- Código: Validação de `alg` em JWT parser
- Teste: Teste unitário com JWT `alg:none` → rejeitado
- Release: Na próxima sprint (P0)

### Opção B: Aceitar Risco (se não mitigado)
- Risco residual: Escalado a CISO por criticidade
- Compensador: WAF regex + IP whitelisting (mitigation menor)
- Prazo: Máx 30 dias para mitigação

**Opção escolhida**: A (Implementação obrigatória)

---

## 4. Aprovações e Rastreabilidade

### Matriz de Decisores

| Decisor | Papel | Aprovação | Data | Observações |
|---------|-------|-----------|------|-------------|
| João Silva | AppSec Lead | ✅ Aprova | 2025-01-15 | Risco crítico, implementação obrigatória |
| Maria Santos | Product Owner | ✅ Aprova | 2025-01-15 | Alinhado com roadmap segurança Q1 |
| CTO (se escalado) | — | — | — | Não necessário (< 30 dias) |

### Rastreabilidade

- **Decision File**: `threat-model/decisions/TM-GEN-042-decision.md`
- **Jira Issue**: [PROJ-1234] JWT alg:none validation
- **Commit**: `refs #1234 feat(auth): add JWT alg validation`
- **Pull Request**: [#567] https://github.com/...

---

## 5. Gestão de Exceções e Riscos Residuais

### Se Risco Aceite (Sem Mitigação)

Documentar em `threat-model/risk-acceptance/ACCEPT-TM-042.md`:

```yaml
---
threat_id: "TM-042"
acceptance_date: "2025-01-15"
accepted_by: "CTO/CISO"
expiration_date: "2025-04-15" # 90 dias
---

### Justificação de Aceitação
- Mitigação requer refactor da arquitetura auth (alto esforço)
- Compensador implementado: WAF + rate limiting
- Aplicação tem uso interno (baixa exposição)
- Risco revisitado em Q2 2025

### Compensadores
- WAF regex blocks payloads com `none`
- Rate limiting: 5 requests/min por IP
- Monitorização: Alert se falha validação JWT

### Escalada
- Registada em GRC risk register
- Comunicada a stakeholders
- Revisão trimestral obrigatória
```

---

## 6. Implementação Prática: Template Reutilizável

### 6.1 Decision Template (Markdown)

```markdown
# TM-[THREAT_ID] Decision Template

## Threat Information
- **ID**: TM-GEN-XXX
- **Title**: [ameaça_descricao]
- **Source**: [ferramenta_ou_manual]
- **Severity**: [CRÍTICA|ALTA|MÉDIA|BAIXA]

## Evaluation

| Criterion | Question | Answer | Evidence |
|-----------|----------|--------|----------|
| Relevance | ? | ☐ Yes / ☐ No | |
| Exposure | ? | ☐ Yes / ☐ No | |
| Detectability | ? | ☐ Yes / ☐ Partial / ☐ No | |
| Business Impact | ? | ☐ Critical / ☐ High | |
| Existing Control | ? | ☐ Complete / ☐ Partial / ☐ None | |

## Decision

**Decision**: ☐ ACCEPT / ☐ ADAPT / ☐ REJECT

**Justification**: [razão]

**Mapped Requirements**: 
- REQ-XXX: [descrição]

**Mitigations**:
- [ ] Control A
- [ ] Control B

## Approvals

| Approver | Role | Status | Date |
|----------|------|--------|------|
| | AppSec Lead | ☐ Approved | |
| | Product Owner | ☐ Approved | |

## Traceability

- **Decision File**: threat-model/decisions/TM-GEN-XXX-decision.md
- **Jira**: [PROJ-XXXX]
- **Commit**: [hash]
```

### 6.2 Governance Workflow

```
Threat Detected
    ↓
Initial Evaluation (Criteria 1-6)
    ↓
    ├─→ REJECT: Document in rejections.md
    ├─→ ADAPT: Adjust threat, re-evaluate
    └─→ ACCEPT:
           ↓
           Map to Requirements (Cap.2)
           ↓
           Propose Mitigation Path (A/B/C)
           ↓
           Route to Approvers:
           - AppSec Lead (always)
           - Product Owner (if medium+ effort)
           - CTO/CISO (if residual risk → GRC)
           ↓
           Document Decision + Approvals
           ↓
           Backlog Card Created → Jira
           ↓
           Tracked via CI/CD in threat-model-validation.yml
```

---

## 7. Matriz de Decisores por Tipo de Ameaça

Pré-configurar aprovadores conforme gravidade e categoria:

| Ameaça | Severidade | Esforço | Aprovadores | SLA |
|--------|-----------|--------|------------|-----|
| Auth/Sessions | CRÍTICA | >3d | AppSec, PO | <24h |
| Access Control | ALTA | >2d | AppSec, PO | <48h |
| Data/Privacy | CRÍTICA | <5d | AppSec, CISO | <24h |
| Configuration | MÉDIA | <1d | AppSec | <5d |
| Denial of Service | ALTA | <2d | AppSec, DevOps | <48h |

---

## 8. Métricas de Sucesso (I3)

### Indicadores

| Métrica | Meta | Como Medir |
|---------|------|-----------|
| % Ameaças com decisão documentada | 100% (L2/L3) | Relatório: `decisions/*.md` count |
| Tempo médio decisão | <5 dias (CRÍTICA), <10 dias (ALTA) | Timestamp em decision file |
| % Decisões com aprovação formal | 100% (L2/L3) | Count approvers in YAML |
| % Ameaças rastreáveis a Jira | 100% | Link count em decision files |
| Taxa de escalada (→ GRC) | <20% (L2) | Count ACCEPT com prazo revisão |

### Dashboard Sugerido

```
📊 Threat Modeling Decision Dashboard

├─ Total Threats Managed: 42
├─ Status Distribution:
│  ├─ ✅ Accepted: 25 (59%)
│  ├─ 🔄 Adapted: 10 (24%)
│  ├─ ❌ Rejected: 7 (17%)
│  └─ ⏳ Pending: 0 (0%)
├─ Avg Decision Time: 4.2 days
├─ Approval Rate: 100%
├─ Escalated to GRC: 3
└─ Status: 🟢 Compliant
```

---

## 9. Integração com CI/CD

### Validação Automática

Adicionar em `threat-model/validate-decisions.yml`:

```yaml
name: Threat Modeling Decision Validation

on:
  pull_request:
    paths:
      - 'threat-model/decisions/**'
      - 'threat-model/risk-acceptance/**'

jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Check decision completeness
        run: |
          for file in threat-model/decisions/*.md; do
            # Validate structure:
            # - Contains threat_id, decision, justification, approvals
            grep -q "threat_id:" "$file" || exit 1
            grep -q "Decision:" "$file" || exit 1
            grep -q "Justification:" "$file" || exit 1
            grep -q "Approvals" "$file" || exit 1
          done
      
      - name: Check GRC escalations
        run: |
          # Count decisions with >90d acceptance
          # Flag for CISO review
          python scripts/check_grc_escalations.py
      
      - name: Generate decision report
        run: |
          python scripts/generate_decision_report.py > threat-decisions-report.txt
      
      - name: Comment PR with summary
        uses: actions/github-script@v6
        with:
          script: |
            fs.readFileSync('threat-decisions-report.txt', 'utf8')
```

---

## 10. Exemplo Completo: JWT alg:none

[Veja exemplo acima na Fase 2]

---

## 📚 Referências e Ligações

| Recurso | Descrição | Link |
|---------|-----------|------|
| OWASP Risk Rating Methodology | Como priorizar ameaças | [owasp.org/...risk...] |
| ISO 27005 Risk Assessment | Standard de avaliação de risco | [iso.org] |
| SAMM 2.0 - Threat Assessment | Practices de threat modeling | [samm.owasp.org] |
| Cap. 02 - Requisitos Segurança | Catálogo de requisitos | [/sbd-toe/sbd-manual/requisitos] |
| US-04: Validação Assistida | User story desta framework | [aplicacao-lifecycle#us-04] |
| US-06: Risco Aceite | Formalização de exceções | [aplicacao-lifecycle#us-06] |

---

## 🎯 Checklist de Implementação (I3)

- [ ] Matriz de decisão comunicada a DevSecOps/AppSec
- [ ] Template de decision file criado em repositório
- [ ] Matriz de decisores definida e publicada
- [ ] Workflow CI/CD configurado para validar decisions
- [ ] Primeiras 10 ameaças processadas com template
- [ ] Relatório mensal de decisões gerado automaticamente
- [ ] Métricas de sucesso integradas no dashboard de segurança
- [ ] Feedback do AppSec coletado e incorporado

---

**Versão**: 1.0  
**Última Atualização**: Jan 2025  
**Mantido por**: AppSec Team  
