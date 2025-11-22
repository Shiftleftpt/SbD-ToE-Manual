---
id: exemplo-raci-governance
title: "Exemplo: RACI e Governança"
description: Template exemplar de RACI (Responsible, Accountable, Consulted, Informed) para implementação SbD
tags: [exemplos, governanca, organizacao, raci, responsabilidades]
---

# Exemplo: RACI de Governança

## Enquadramento

O SbD-ToE prescreve ([Cap. 14](/sbd-toe/sbd-manual/governanca-contratacao/intro)):
- ✓ Estrutura de governança
- ✓ RACI claro
- ✓ Aprovações formais
- ✓ Segregação de responsabilidades

O SbD-ToE **NÃO prescreve** qual organigrama (varia por setor, tamanho, geografia).

Este documento apresenta **exemplos de RACI para diferentes contextos**.

---

## Modelo de Governo

O governo de segurança deve ter **três níveis**:

```
┌──────────────────────────────────────────────────┐
│ NÍVEL EXECUTIVO: Board + Executive Committee    │
│ Função: Aprovação política, governance, risk    │
│ Frequência: Trimestral                          │
├──────────────────────────────────────────────────┤
│ NÍVEL TÁTICO: Segurança + Operações             │
│ Função: Execução, metriques, escalations        │
│ Frequência: Mensal                              │
├──────────────────────────────────────────────────┤
│ NÍVEL OPERACIONAL: Devs + SRE + Segurança      │
│ Função: Implementação diária, code review       │
│ Frequência: Contínua                            │
└──────────────────────────────────────────────────┘
```

---

## Exemplo 1: Fintech Pequena (10-20 devs)

### Organigrama Simplificado
```
CEO
├─ CTO (Chief Technology Officer)
│  ├─ Tech Lead (1 person)
│  │  └─ Developers (8-15)
│  ├─ SRE/DevOps (1-2)
│  └─ Security Champion (part-time, 0.5 FTE)
├─ Head of Compliance/GRC
│  └─ Compliance Officer
└─ CFO (Budget)
```

### RACI por Atividade

| Atividade | CTO | Tech Lead | Security Champion | Compliance | CFO | Board |
|-----------|-----|-----------|------------------|-----------|-----|-------|
| **Governança** | | | | | | |
| Definir política SbD | A | R | C | C | I | A |
| Approvar política board | I | - | - | C | I | **A** |
| Definir RACI | R | A | C | - | - | I |
| **Planejamento** | | | | | | |
| Classificar apps (L1-L3) | R | A | C | I | - | - |
| Alocar budget para segurança | I | I | I | C | **A** | I |
| **Desenvolvimento** | | | | | | |
| Code review (security gates) | I | R | C | - | - | - |
| Threat modeling | R | A | R | C | - | - |
| Testes de segurança | R | A | R | - | - | - |
| **Operações** | | | | | | |
| Monitorização de incidentes | I | I | R | - | - | - |
| Resposta a incidentes | I | A | R | C | I | I |
| **Compliance** | | | | | | |
| Auditoria interna | I | C | I | R | - | A |
| Reporte DORA | - | - | C | R | - | A |

**Legenda:**
- **R (Responsible):** Faz o trabalho
- **A (Accountable):** Aprova, é responsável
- **C (Consulted):** Opinião importante
- **I (Informed):** Informado do resultado

### Reuniões de Governo

**Comissão de Segurança (Quinzenal, 1h)**
- Presentes: CTO, Tech Lead, Security Champion, Compliance Officer
- Agenda: Incidentes, vulnerabilidades, progress roadmap
- Output: Atas, escalations, decisões

**Board Report (Trimestral, 30min)**
- Presentes: CEO, CTO, CFO, Compliance Officer, Board
- Agenda: KPIs, conformidade DORA, riscos, budget
- Output: Decisões estratégicas, aprovações

---

## Exemplo 2: Banco Regional (100-200 devs)

### Organigrama Estruturado
```
Conselho/Board
├─ Comissão de Risco
│  └─ Chief Risk Officer (CRO)
│
CEO
├─ CTO (Chief Technology Officer)
│  ├─ VP Development
│  │  ├─ Tech Leads (múltiplos)
│  │  └─ Development Squads (30-50 devs)
│  ├─ VP Operations/SRE
│  │  ├─ SRE Lead
│  │  ├─ SRE Team (3-5)
│  │  └─ Infrastructure
│  └─ CISO (Chief Information Security Officer)
│     ├─ Security Architect
│     ├─ Incident Response Manager
│     ├─ Security Engineers (2-3)
│     └─ Security Champions (embed em squads)
├─ Chief Compliance Officer (CCO)
│  ├─ Compliance Manager
│  ├─ GRC Team
│  └─ Internal Audit Lead
└─ CFO
```

### RACI Expandida

| Atividade | CTO | CISO | VP Dev | Tech Lead | Dev/SRE | Compliance | CRO | Board |
|-----------|-----|------|--------|-----------|---------|-----------|-----|-------|
| **Governança Executiva** | | | | | | | | |
| Estratégia de segurança (3 anos) | R | A | C | - | - | C | C | **A** |
| Política de segurança aplicacional | C | R | A | C | - | C | I | A |
| Aprovação Board de políticas | I | I | I | - | - | C | I | **A** |
| Orçamento de segurança | I | A | C | - | - | I | C | **A** |
| **Classificação & Risk** | | | | | | | | |
| Classificar apps (L1-L3) | I | R | A | **R** | - | C | - | I |
| Threat modeling (apps L3) | - | R | C | A | - | I | - | - |
| Risk assessment (fornecedores) | I | C | - | - | - | R | I | I |
| **Development Lifecycle** | | | | | | | | |
| Code review (security gates) | I | C | I | A | **R** | - | - | - |
| SAST/SCA scanning | I | A | I | I | **R** | - | - | - |
| Pull request approval (sec) | I | C | - | A | **R** | - | - | - |
| **Operações & Monitorização** | | | | | | | | |
| Centralizar logs (SIEM) | A | R | C | - | A | I | - | - |
| Alertas de segurança | I | A | - | - | R | - | - | - |
| Deteção de incidentes | - | **R** | I | - | C | - | - | - |
| **Incidentes & Resposta** | | | | | | | | |
| Classificação de incidentes | - | A | - | - | C | C | - | - |
| Resposta P0/P1 | C | **A** | C | - | R | I | I | I |
| Reporte incidentes DORA | - | C | - | - | - | **R** | A | A |
| **Conformidade & Auditoria** | | | | | | | | |
| Auditoria interna (SbD) | I | C | I | - | - | **R** | I | A |
| Readiness DORA | C | A | C | - | - | **R** | A | **A** |
| Testagem TLPT | C | **A** | C | - | - | I | I | I |

### Estrutura de Reuniões

**Steering Committee (Executivo) - Mensal, 1.5h**
- Presentes: CTO, CISO, CCO, CFO, CRO
- Agenda: Risk dashboard, budget, conformidade, escalations
- Output: Decisões estratégicas

**Security & Risk Committee - Semanal, 1h**
- Presentes: CISO, VP Operations, VP Dev Lead, Compliance Lead, Incident Response Manager
- Agenda: Incidentes, vulnerabilidades, roadmap, blockers
- Output: Decisions, task assignments

**Development Security Review - Bi-weekly, 1h**
- Presentes: Tech Leads, Security Engineers, SRE Lead
- Agenda: Code review findings, SAST/SCA results, threat modeling progress
- Output: Escalations, guidance, exemptions

**Squad Security Standup - Weekly (per squad), 15min**
- Presentes: Squad, Security Champion (embedded)
- Agenda: Security tasks, blockers, questions
- Output: Real-time support

**Board Governance - Quarterly, 1h**
- Presentes: Board, CTO, CISO, CCO, CFO, CRO
- Agenda: Strategic risk, compliance posture, DORA readiness, budget
- Output: Board decisions, strategic guidance

---

## Exemplo 3: PME Distribuída (30-50 devs, múltiplas localizações)

### Desafio
- Múltiplas localizações (Lisboa, Porto, remoto)
- Recursos limitados
- Expertise distribuída

### Solução: Modelo Híbrido

**Estrutura Enxuta:**
```
CEO (Lisboa)
├─ CTO/Tech Lead (Lisboa)
│  ├─ Security Champion (0.5 FTE, Lisboa)
│  ├─ SRE/DevOps (0.5 FTE, Porto)
│  └─ Developers (5-8 por squad, distribuído)
├─ CFO (remoto)
└─ Compliance Officer (Lisboa, part-time)
```

**RACI Simplificada:**

| Atividade | CTO | Sec Champion | SRE | Dev Lead | Compliance | CEO |
|-----------|-----|-------------|-----|----------|-----------|-----|
| Política | R | C | - | - | C | A |
| Classificar apps | R | A | - | C | - | I |
| Code review sec | I | A | - | R | - | - |
| SAST/SCA | I | R | I | I | - | - |
| Incidentes | - | R | A | C | I | I |
| DORA audit | I | C | C | - | R | A |

**Reuniões (Lean):**
- **Semanal, 30min:** CTO + Security Champion + SRE (standup remoto)
- **Bi-weekly, 1h:** CTO + All Tech Leads (code review highlights)
- **Mensal, 1h:** CTO + Compliance + CEO (KPIs + DORA progress)

---

## Responsabilidades Chave por Papel

### CISO (Chief Information Security Officer)

**Accountable For:**
- ✓ Conformidade DORA e regulamentações
- ✓ Política de segurança
- ✓ Trilho auditoria (logs)
- ✓ Resposta a incidentes
- ✓ TLPT eligibility e execução
- ✓ Risk dashboard accuracy

**Reporta a:** CRO ou CEO (depende governance)

**Escalações típicas:**
- Incidente P0 (dentro de 30 min)
- Vuln crítica não resolvida (within 48h)
- Conformidade DORA em risco (weekly)

---

### Tech Lead (Development Squads)

**Responsible For:**
- ✓ Threat modeling (apps próprias)
- ✓ Code review (security gates)
- ✓ Testes de segurança
- ✓ Documentação de requisitos

**Consulted:**
- Policy changes
- New tools / frameworks
- Security exceptions

**Reports a:** VP Development ou CTO

---

### Security Champion (Embedded)

**Role:** "Security voice" dentro da squad

**Responsible For:**
- ✓ Advocacia de práticas seguras
- ✓ Code review (segurança)
- ✓ Training & awareness
- ✓ Liaison com CISO team

**Tempo:** 20-30% da semana

**Reports a:** CISO (dotted line), Squad Lead (solid line)

---

### Compliance Officer / GRC

**Accountable For:**
- ✓ Conformidade regulatória (DORA, GDPR, etc.)
- ✓ Relatórios supervisor
- ✓ Audit trail
- ✓ Policy approval coordination

**Reports a:** Chief Compliance Officer ou CRO

---

## Aprovações Formais (Trilho de Decisão)

### Política de Segurança
```
Draft (CISO)
  ↓
Review (Security team + Compliance)
  ↓
Approval (CTO + CISO)
  ↓
Board vote
  ↓
Implementation + Communication
  ↓
Annual review
```

### Exceção de Segurança (ex: deploy com vuln alta)
```
Request (Tech Lead)
  ↓
Justificação de risco (Squad + CISO)
  ↓
Approval (CISO + CTO)
    OR Escalate (Board decision)
  ↓
Approval + SLA remediação
  ↓
Log em audit trail + notify CRO
```

### Fornecedor Crítico
```
Request (VP Procurement/Tech)
  ↓
Risk assessment (CISO team)
  ↓
Security requirements (CISO + Compliance)
  ↓
Contrato (Jurídico + CISO review)
  ↓
Approval (CTO + CISO + Compliance)
  ↓
Onboarding (Security Champion + SRE)
```

---

## Matriz de Comunicação

| Grupo | Frequência | Formato | Owner |
|-------|-----------|---------|-------|
| **Board** | Trimestral | Report formal | CISO/Compliance |
| **Steering Committee** | Mensal | Reunião + slides | CTO/CISO |
| **Security Committee** | Semanal | Reunião | CISO |
| **Dev Leads** | Bi-weekly | Reunião | CISO |
| **All Staff** | Anual | All-hands | CEO/CISO |
| **Security Champions** | Quinzenal | Reunião + Slack | CISO |
| **On-call (incidents)** | On-demand | Pagerduty + Slack | On-call lead |

---

## Documentação Essencial

Cada organização deve documentar:

```
📋 GOVERNANCE DOCUMENTATION

├─ Charter of Governance
│  ├─ Estrutura (organigrama)
│  ├─ Roles & responsibilities (RACI)
│  ├─ Escalation paths
│  └─ Approval workflows
│
├─ Security Policies
│  ├─ Policy de Segurança Aplicacional
│  ├─ Policy de Incidentes
│  ├─ Policy de Fornecedores
│  └─ Code of Conduct (security)
│
├─ Procedures
│  ├─ Code review procedure
│  ├─ Incident response playbook
│  ├─ Exception approval process
│  └─ Audit trail requirements
│
└─ Training Materials
   ├─ Role-based training (CISO, Tech Lead, Dev, QA)
   ├─ Onboarding security checklist
   ├─ Annual refresher modules
   └─ Incident response drills
```

---

## Checklist de Implementação

- [ ] **Organigrama definido** - Roles claros, reporting lines
- [ ] **RACI documentada** - Aprovada e comunicada
- [ ] **Reuniões agendadas** - Calendário confirmado
- [ ] **Escalation paths claros** - Documentado (ex: P0 → CISO → CTO → CEO)
- [ ] **Aprovações assinadas** - Board signature on policies
- [ ] **Training** - Todos conhecem seu role
- [ ] **Audit trail ativo** - Logs de quem decidiu o quê, quando

---

## Notas Importantes

1. **Não existe tamanho único** - Adaptar ao contexto
2. **Evolução:** Estrutura pode mudar conforme maturidade
3. **Simplicidade:** Evitar bureaucracia excessiva
4. **Clareza:** RACI ambígua = problemas
5. **Documentação:** Tudo escrito, nada "implícito"
6. **Revisão:** Anually, após grandes mudanças

---

**Versão:** 1.0  
**Data:** Novembro 2025  
**Review:** Anual ou pós-mudança organizacional
