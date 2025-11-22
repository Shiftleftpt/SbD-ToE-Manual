---
description: Template exemplar de reporte de incidentes alinhado com DORA RTS/ITS
id: exemplo-relatorio-incidentes
tags:
- dora
- exemplos
- implementacao
- incidentes
- playbook
- reporte
- template
title: 'Exemplo: Reporte de Incidentes'
---


# Exemplo: Relatório de Incidentes

## Enquadramento

O SbD-ToE prescreve ([Cap. 12](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro)):
- ✓ Processos de deteção de incidentes
- ✓ Registre, classifique e documente
- ✓ Trilho auditoria completo

O SbD-ToE **NÃO prescreve** templates específicos DORA (ITS - Implementing Technical Standards).

Este documento apresenta um **template exemplar** de como estruturar reporte de incidentes.

---

## ⚠️ Aviso Importante

**Este é um exemplo** - não é o template oficial DORA.

Os reguladores (EBA, BCB, ESMA) publicarão templates ITS oficiais. Este exemplo:
- Ilustra **princípios** de estruturação
- Pode servir como **base interna**
- Deve ser **adaptado** aos templates regulatórios finais

---

## Estrutura de Incidente

### 1. Identificação

```
Incident ID: INC-2025-001234
Detection Date: 2025-11-13 14:23 UTC
Detection Channel: SIEM alert (WAF)
Reporter: Security Team
```

### 2. Classificação Inicial

```
Severity (SbD-ToE):
├─ Critical (P0): Impacto imediato em apps L3 / dados sensíveis
├─ High (P1): Impacto em apps L2 / comprometimento significativo
├─ Medium (P2): Impacto limitado / dados não-sensíveis
└─ Low (P3): Informativo

Categorization:
├─ Malware/Ransomware
├─ Unauthorized Access
├─ Data Exfiltration
├─ Denial of Service
├─ Vulnerability Exploitation
├─ Configuration Issue
├─ Operational Issue
└─ Other
```

### 3. Timeline

```
Timeline (UTC):
- 14:23 - Alert triggered (WAF logs)
- 14:25 - Manual confirmation (analyst)
- 14:30 - Team notified (on-call)
- 14:35 - Response initiated
- 14:50 - Root cause identified
- 15:10 - Remediation started
- 15:40 - Services restored
- 16:00 - Incident closed (provisional)
```

### 4. Impacto

```
Impact:
├─ Affected Systems: Gateway API (L3), Auth Service (L3)
├─ Affected Users: ~500 (active sessions)
├─ Data Exposure: None detected
├─ Downtime: 15 minutes (partial degradation, not full)
├─ Business Impact: Transactions delayed (SLA met: `<`30min recovery)
└─ Regulatory Impact: DORA Art. 18 reportable? No (within thresholds)
```

### 5. Root Cause Analysis

```
Root Cause:
- Missing rate limiting on auth endpoint
- Attacker: Automated bot (geo: RU IP)
- Attack type: Brute force authentication
- Volume: 50k attempts in 10 min
- Success: 0 (credentials not compromised)
```

### 6. Remediation

```
Immediate Actions (done):
- [ ] Rate limiting deployed (30 req/min per IP)
- [ ] IPs blocked (30-day)
- [ ] Alerts reconfigured

Follow-up Actions (planned):
- [ ] Implement CAPTCHA on auth (Sprint 12)
- [ ] Add behavioral analysis (WAF rule)
- [ ] Training: Secure coding (auth best practices)
- [ ] Retest: Penetration testing (within 30 days)
```

### 7. Lições Aprendidas

```
What went well:
- Detection fast (SIEM)
- Team response `<`10 min
- Communication clear
- No escalation to CEO

What could improve:
- Should have had rate limiting from start (code review gap)
- CAPTCHA should be standard (not opt-in)
- Post-incident review should happen faster (within 24h)

Action Items:
1. Add rate limiting to security checklist (Dev team)
2. Schedule code review training (Security)
3. Update threat model to include brute-force (Arch)
```

### 8. Conformidade DORA (Informativo)

```
DORA Art. 18 Threshold Analysis:
- Availability Impact: `<`20% (low)
- Confidentiality Impact: None
- Integrity Impact: None
- Affected Customers: Not significantly
- Reputational Impact: Low
- Regulatory Notification: No (threshold not met)

Decision: Not reportable to supervisor
(But keep audit trail for demonstration)
```

---

## Template Genérico (Excel/Jira/ServiceNow)

Este template estrutura sistemas de tickets de incidentes:

| Campo | Tipo | Obrigatório | Descrição |
|-------|------|-----------|-----------|
| Incident ID | Auto-increment | Sim | ID único (INC-YYYY-NNNN) |
| Title | Text | Sim | Resumo (max 100 chars) |
| Description | Text | Sim | Descrição detalhada do incidente |
| Detection Date | DateTime | Sim | Data/hora UTC de detecção |
| Reporter | Dropdown (staff) | Sim | Quem reportou |
| Severity | Dropdown (P0-P3) | Sim | SbD-ToE classification |
| Category | Dropdown | Sim | Tipo de incidente |
| Affected Systems | Multi-select | Sim | Apps/infra impactados |
| Root Cause | Text | Condicional (pós-investigação) | Causa identificada |
| Remediation | Text | Condicional | Ações tomadas |
| Owner | Dropdown (team) | Sim | Equipa responsável |
| Status | Dropdown (Open/Investigating/Remediated/Closed) | Sim | Estado atual |
| Resolution Date | DateTime | Condicional (pós-resolução) | Quando foi resolvido |
| Retest Date | DateTime | Condicional | Quando será testado |
| DORA Reportable | Dropdown (Yes/No/Unknown) | Condicional (pós-investigação) | Necessário notificar? |
| Related Incidents | Multi-link | Não | Incidentes relacionados |
| Attachments | Files | Não | Logs, screenshots, etc. |
| Audit Trail | Read-only log | Sim | Quem fez o quê, quando |

---

## Cronograma de Reporte

### Imediato (< 1 hora)
- [ ] Detectar e confirmar
- [ ] Criar ticket
- [ ] Notificar on-call

### Curto prazo (< 24 horas)
- [ ] Investigação completa
- [ ] Root cause identificado
- [ ] Remediation em progresso

### Médio prazo (< 7 dias)
- [ ] Remediation completa
- [ ] Testes validaram fix
- [ ] Lições aprendidas documentadas

### Compliance (conforme DORA)
- [ ] Análise DORA (reportável?)
- [ ] Notificação supervisor (se aplica)
- [ ] Arquivo para 3+ anos (audit trail)

---

## Retenção de Logs

**Conformidade [Cap. 12](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro) + DORA Art. 18:**

```
Todos os incidentes + trilho auditoria devem ser retidos:
- Mínimo: 3 anos
- Recomendado: 5 anos
- Acesso: Immutable (WORM - Write Once Read Many)
- Verificação: Integridade criptográfica (hash)
```

---

## Integração com SIEM

Exemplo de envio automático de incidentes do SIEM para sistema de tickets:

```json
{
  "incident_id": "INC-2025-001234",
  "timestamp": "2025-11-13T14:23:00Z",
  "title": "Potential brute-force attack on Auth endpoint",
  "source": "SIEM (Splunk)",
  "severity": "high",
  "details": {
    "endpoint": "/api/auth/login",
    "attempts": 50000,
    "unique_ips": 1,
    "geo": "RU",
    "detection_rule": "Authentication_Brute_Force"
  },
  "affected_systems": ["gateway-api", "auth-service"],
  "action_required": true,
  "assignee": "on-call-security-engineer"
}
```

---

## Próximos Passos

Quando DORA RTS/ITS oficiais saírem:
1. Comparar este template com oficial
2. Estender com campos adicionais DORA
3. Integrar com sistema de reporting regulatório
4. Testar integridade de audit trail

---

**Versão:** 1.0 (Exemplar)  
**Data:** Novembro 2025  
**Validação:** Aguardar templates DORA oficiais
