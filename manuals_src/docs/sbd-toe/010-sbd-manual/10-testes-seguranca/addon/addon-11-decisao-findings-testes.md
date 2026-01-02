---
id: decisao-findings-testes
title: Framework de Decisão para Findings de Testes de Segurança
description: Framework estruturado para separar sugestão (ferramenta) de decisão (humano) em findings de SAST, DAST, IAST, fuzzing e pentesting
tags: [I1, decisão, findings, SAST, DAST, IAST, fuzzing, pentesting, escalação]
---

# 🎯 Framework de Decisão para Findings de Testes de Segurança

## 🌟 Objetivo

Implementar **Invariante I1 (Separação entre Sugestão e Decisão)** de agent.md no contexto de testes de segurança aplicacional.

Ferramentas de teste (SAST, DAST, IAST, fuzzing, scanners) **sugerem** que existe vulnerabilidade, mas não decidem se:
- O finding é exploitável no contexto da aplicação
- Existem controlos compensatórios que mitigam o risco
- A correção é viável no prazo disponível
- O risco residual é aceitável para o negócio

Este addon prescreve um **framework de decisão estruturado** que:
1. Separa explicitamente sugestão (output da ferramenta) de decisão (análise humana)
2. Define checklist de análise obrigatória (C1)
3. Prescreve template de decisão formal (T1)
4. Define matriz de decisores por severidade e nível de classificação
5. Estabelece workflow de escalação para conflitos (T2)

---

## 🎯 Contexto normativo

**Risco de não-conformidade com I1:**
- Ferramentas bloqueiam pipelines automaticamente sem contexto (finding HIGH → bloqueio, sem análise)
- Equipas aceitam riscos "às cegas" para cumprir deadlines (bypasses sem justificação)
- Conflitos entre timeline e segurança não têm processo formal de resolução
- Falsos positivos não são geridos, gerando ruído e fadiga de alertas
- Decisões não são rastreáveis (sem evidência de quem decidiu, porquê, quando)

**Consequências observadas:**
- L1/L2: Vulnerabilidades críticas aceites implicitamente para cumprir go-live
- L3: Pipelines bloqueadas por false positives, equipas fazem bypass de gates sem aprovação
- Auditoria: Incapacidade de demonstrar que decisões foram tomadas com devido diligence

---

## 📋 Framework de Decisão em 4 Fases

### Fase 1: Finding Reportado (Ferramenta sugere)

**Input:**
- Ferramenta reporta finding (SAST, DAST, IAST, fuzzing, pentesting)
- Finding inclui: ID, severidade (CRITICAL/HIGH/MEDIUM/LOW), CWE, localização (ficheiro:linha ou endpoint), descrição, CVSS score (se aplicável)

**Output:**
- Finding registado em plataforma centralizada (DefectDojo, Vulcan, etc.)
- Status inicial: `NOVO`
- Atribuído a: Developer/DevOps responsável pelo módulo

**SLA:**
- CRITICAL: 2h para iniciar análise
- HIGH: 4h para iniciar análise
- MEDIUM: 8h para iniciar análise
- LOW: 24h para iniciar análise

---

### Fase 2: Análise com Checklist C1 (Humano analisa)

**Checklist C1 — 4 Perguntas Obrigatórias:**

#### C1.1 — O finding é exploitável no contexto da aplicação?

**Análise:**
- ❓ O código vulnerável é executado em produção ou está em dead code?
- ❓ O endpoint/função está acessível externamente ou apenas internamente?
- ❓ Existe autenticação/autorização que protege o ponto vulnerável?
- ❓ O payload de exploração funciona no contexto real (encoding, validações)?

**Evidência necessária:**
- Análise de code path (call graph, stack trace)
- Teste de reachability (pode-se chegar ao código vulnerável?)
- Análise de surface de ataque (endpoint público vs. interno)
- Tentativa de exploração em staging (se CRITICAL/HIGH em L2/L3)

**Resultado:**
- ✅ EXPLOITÁVEL: Vulnerabilidade confirmada, pode ser explorada
- ⚠️ PARCIALMENTE EXPLOITÁVEL: Requer condições específicas (ex: utilizador autenticado)
- ❌ NÃO EXPLOITÁVEL: Dead code, função não-exposta, ou payload bloqueado

---

#### C1.2 — Existem controlos compensatórios ou mitigações?

**Análise:**
- ❓ WAF/IPS/IDS bloqueia o exploit?
- ❓ Network segmentation isola o componente vulnerável?
- ❓ Hardening de runtime previne a exploração (ex: seccomp, AppArmor)?
- ❓ Input validation upstream neutraliza o payload?
- ❓ Dados sensíveis estão encriptados/mascarados mesmo se exfiltrados?

**Evidência necessária:**
- Configuração de WAF/IPS com regras aplicáveis
- Network policies/firewall rules
- Runtime security policies (OPA, seccomp profiles)
- Validação de input em camadas anteriores
- Encryption at rest/in transit

**Resultado:**
- ✅ MITIGADO: Controlos compensatórios bloqueiam exploração
- ⚠️ MITIGAÇÃO PARCIAL: Reduz probabilidade mas não elimina risco
- ❌ NÃO MITIGADO: Sem controlos compensatórios efetivos

---

#### C1.3 — A remediação é viável no prazo disponível?

**Análise:**
- ❓ Correção é simples (ex: upgrade de dependência, fix de 5 linhas)?
- ❓ Correção é complexa (ex: refactor de arquitetura, migração de biblioteca)?
- ❓ Existe versão corrigida disponível (para dependências)?
- ❓ Correção quebra funcionalidades existentes (requer testing extensivo)?
- ❓ Quanto tempo estima-se para correção completa?

**Evidência necessária:**
- Análise de impacto da correção (número de ficheiros afetados, dependências)
- Availability de patch/versão corrigida
- Estimativa de esforço (horas/dias)
- Análise de breaking changes

**Resultado:**
- ✅ VIÁVEL: Correção pode ser aplicada em <24h (CRITICAL), <7d (HIGH)
- ⚠️ VIÁVEL COM ESFORÇO: Requer >7d, refactor significativo
- ❌ INVIÁVEL: Correção requer rewrite, migração major, ou não existe patch

---

#### C1.4 — Qual o contexto de negócio e timeline?

**Análise:**
- ❓ Existe deadline crítico (go-live regulatório, contractual)?
- ❓ A aplicação está em produção ou ainda em desenvolvimento?
- ❓ Qual o impacto de negócio de atrasar o release?
- ❓ Qual o impacto de negócio de um incidente de segurança?
- ❓ Existe pressão externa (cliente, regulador, auditoria)?

**Evidência necessária:**
- Timeline do projeto (datas de go-live)
- Requisitos regulatórios/contratuais
- Análise de impacto de negócio (revenue loss, penalidades)
- Risk appetite da organização

**Resultado:**
- 🚨 CRÍTICO: Go-live imediato, compliance obrigatório
- ⚠️ URGENTE: Timeline apertado mas negociável
- ✅ NORMAL: Sem pressão de timeline

---

### Fase 3: Decisão com Template T1 (Humano decide)

**Template T1 — Decisão Formal**

```markdown
# Decisão de Findings de Teste — [FINDING-ID]

**Finding:**
- ID: [SAST-2026-01-16-001]
- Severidade: [CRITICAL / HIGH / MEDIUM / LOW]
- CWE: [CWE-89 SQL Injection]
- Localização: [src/api/users.ts:142]
- Descrição: [SQL injection no endpoint GET /api/users?id=]
- Ferramenta: [Semgrep SAST]
- Data deteção: [2026-01-16]

**Análise C1:**
- **C1.1 Exploitável?** ✅ SIM — Endpoint público, sem autenticação, payload testado com sucesso em staging
- **C1.2 Mitigado?** ❌ NÃO — WAF não deteta payload encodado, sem validação upstream
- **C1.3 Remediação viável?** ✅ SIM — Fix simples: parametrized query, 15 min de trabalho
- **C1.4 Contexto negócio?** ⚠️ URGENTE — Go-live em 3 dias para cliente regulado (GDPR)

**Decisão: CORRIGIR-IMEDIATO**

**Rationale:**
Vulnerabilidade CRITICAL exploitável em endpoint público com dados pessoais (GDPR). Não existem controlos compensatórios. Correção é trivial (parametrized query). Risco de exploração é inaceitável mesmo com timeline apertado.

**Implementação:**
- [ ] PR #4523: Substituir string concatenation por parametrized query
- [ ] Teste de regressão: Adicionar caso de teste com payload SQL injection (deve ser bloqueado)
- [ ] Revalidação SAST: Confirmar que finding desaparece
- [ ] Deploy em staging: Validar correção com DAST
- [ ] Deploy em produção: Incluir em release hotfix v1.2.3

**Responsáveis:**
- Developer: João Silva
- Reviewer: Maria Costa (AppSec Engineer)
- Aprovador final: Tech Lead + CISO (se risco residual aceite)

**SLA:**
- Correção: 4h (2026-01-16 18:00)
- Testing: 2h (2026-01-16 20:00)
- Deploy staging: Imediato após testes
- Deploy produção: 2026-01-17 08:00 (janela de manutenção)

**Rastreabilidade:**
- Finding ID: SAST-2026-01-16-001
- PR: #4523
- Commit: abc123def456
- Release: v1.2.3-hotfix
- Decisão ID: DEC-2026-01-16-001
```

---

**Tipos de Decisão Possíveis:**

#### 1. CORRIGIR-IMEDIATO
- **Quando:** Finding CRITICAL/HIGH exploitável, sem mitigações, correção viável
- **Ação:** Bloquear pipeline, criar PR prioritário, validar correção
- **Aprovação:** Developer + AppSec Engineer
- **SLA:** 4h (CRITICAL), 24h (HIGH)

#### 2. CORRIGIR-PLANEJADO
- **Quando:** Finding MEDIUM/LOW ou HIGH com mitigações parciais, correção viável mas não-urgente
- **Ação:** Adicionar ao backlog com prioridade, incluir em próximo sprint
- **Aprovação:** Developer + Tech Lead
- **SLA:** Próximo sprint (MEDIUM), próximo release (LOW)

#### 3. ACEITAR-RISCO
- **Quando:** Finding não-exploitável, mitigado por controlos compensatórios, ou impacto negligível
- **Ação:** Documentar risk acceptance, registar controlos compensatórios, revisão periódica
- **Aprovação:** AppSec Engineer + CISO (se CRITICAL/HIGH)
- **SLA:** Revisão trimestral (L2), mensal (L3)

#### 4. SUPRIMIR-FALSE-POSITIVE
- **Quando:** Análise confirma que finding é falso positivo (dead code, ferramenta detecta incorretamente)
- **Ação:** Documentar razão técnica, suprimir na ferramenta, adicionar comentário inline
- **Aprovação:** AppSec Engineer
- **SLA:** Imediato após aprovação

#### 5. DEFER-COM-MITIGAÇÃO
- **Quando:** Correção inviável no curto prazo, mas controlos compensatórios temporários são aplicados
- **Ação:** Implementar mitigação temporária (ex: WAF rule, network isolation), agendar correção definitiva
- **Aprovação:** AppSec Engineer + CISO + Tech Lead
- **SLA:** Mitigação temporária em 24h, correção definitiva em 30d (L2), 14d (L3)

---

### Fase 4: Escalação com Template T2 (Conflitos)

**Template T2 — Escalação de Conflitos**

**Cenários de conflito:**
1. **Timeline vs. Segurança:** DevOps quer deploy imediato, AppSec exige correção de CRITICAL
2. **False Positive Dispute:** Developer diz FP, AppSec discorda
3. **Adequacy of Compensating Controls:** Developer propõe mitigação, AppSec considera insuficiente
4. **Risk Acceptance:** Developer quer aceitar risco, AppSec/CISO discordam

---

**Exemplo de Escalação — Timeline vs. Segurança**

```markdown
# Escalação de Conflito — [ESC-2026-01-16-001]

**Finding relacionado:**
- Finding ID: DAST-2026-01-16-042
- Severidade: HIGH
- Descrição: XSS refletido em endpoint GET /search?q=
- Decisão proposta: CORRIGIR-IMEDIATO

**Conflito:**
- **Posição DevOps (João Silva):** Go-live contratual é amanhã (2026-01-17), cliente já foi notificado, atrasar go-live custa €50k/dia de penalidade. Propõe ACEITAR-RISCO temporariamente e corrigir em hotfix em 7 dias.
- **Posição AppSec (Maria Costa):** XSS HIGH em aplicação L2 com dados pessoais (GDPR) não pode ser aceite. Controlos compensatórios (WAF) são insuficientes (payload bypass testado). Exige CORRIGIR-IMEDIATO ou DEFER-COM-MITIGAÇÃO com WAF rule específica.

**Análise de risco:**
- **Probabilidade de exploração:** ALTA (endpoint público, payload simples)
- **Impacto de exploração:** Session hijacking, exfiltração de tokens, GDPR breach
- **Impacto de atraso:** €50k/dia penalidade contratual, perda de confiança do cliente
- **Mitigação possível:** WAF rule custom para bloquear payload XSS (implementação: 2h)

**Proposta de resolução:**
1. **DEFER-COM-MITIGAÇÃO:**
   - Implementar WAF rule custom para bloquear `<script>`, `onerror`, `onclick` em parâmetro `q`
   - Testar WAF rule com fuzzing (100 payloads XSS)
   - Validar que WAF bloqueia 95%+ payloads conhecidos
   - Agendar correção definitiva (output encoding) para v1.3.0 em 7 dias
2. **Go-live com monitorização reforçada:**
   - SIEM alerta para tentativas de XSS (triggered by WAF)
   - Rate limiting em endpoint /search (10 req/min por IP)
   - Revisão de logs diária durante 7 dias
3. **Hotfix v1.3.0 em 7 dias:**
   - Output encoding correto em /search
   - Revalidação DAST
   - Remoção de WAF rule custom após validação

**Decisores:**
- Developer: João Silva — Propõe defer com mitigação
- AppSec: Maria Costa — Aprova defer se WAF rule testada e monitorização reforçada
- Tech Lead: Pedro Santos — Aprova proposta, compromete-se com hotfix em 7d
- CISO: Ana Ferreira — Aprova com condição: WAF testada + SIEM alerting + hotfix mandatory

**Decisão final: DEFER-COM-MITIGAÇÃO (Aprovado)**

**Rastreabilidade:**
- Escalação ID: ESC-2026-01-16-001
- Finding ID: DAST-2026-01-16-042
- WAF rule: /waf/rules/custom-xss-search.conf (commit def789)
- Monitorização: SIEM alert rule ID 4521
- Hotfix agendado: v1.3.0 (2026-01-24)
- Aprovações: Maria Costa (AppSec), Pedro Santos (Tech Lead), Ana Ferreira (CISO)

**SLA de resolução:**
- WAF rule implementada: 2h (2026-01-16 20:00)
- Fuzzing testing: 1h (2026-01-16 21:00)
- Go-live: 2026-01-17 08:00
- Hotfix definitivo: 2026-01-24 (v1.3.0)
```

---

## 📊 Matriz de Decisores

**Quem decide o que?**

| Severidade Finding | Nível L1 | Nível L2 | Nível L3 |
|---|---|---|---|
| **CRITICAL** | Developer + AppSec + Tech Lead | Developer + AppSec + CISO | Developer + AppSec + CISO + GRC |
| **HIGH** | Developer + AppSec | Developer + AppSec + Tech Lead | Developer + AppSec + CISO |
| **MEDIUM** | Developer + AppSec | Developer + AppSec | Developer + AppSec + Tech Lead |
| **LOW** | Developer (AppSec review opcional) | Developer + AppSec | Developer + AppSec |

**Decisão de ACEITAR-RISCO:**
| Severidade | Nível L1 | Nível L2 | Nível L3 |
|---|---|---|---|
| **CRITICAL** | ❌ Não permitido | CISO + Board (se impacto regulatório) | ❌ Não permitido |
| **HIGH** | AppSec + Tech Lead | CISO | CISO + GRC |
| **MEDIUM** | AppSec | AppSec + Tech Lead | AppSec + CISO |
| **LOW** | Developer (com justificação) | AppSec | AppSec |

**Decisão de SUPRIMIR-FALSE-POSITIVE:**
| Severidade | Nível L1 | Nível L2 | Nível L3 |
|---|---|---|---|
| **Qualquer** | AppSec Engineer (análise técnica obrigatória) | AppSec Engineer (análise técnica obrigatória) | AppSec Engineer + Peer Review (2º AppSec) |

---

## 🚨 SLA por Severidade e Nível

| Severidade | Nível L1 | Nível L2 | Nível L3 |
|---|---|---|---|
| **CRITICAL** | Análise: 4h, Decisão: 8h, Correção: 48h | Análise: 2h, Decisão: 4h, Correção: 24h | Análise: 1h, Decisão: 2h, Correção: 4h |
| **HIGH** | Análise: 8h, Decisão: 24h, Correção: 7d | Análise: 4h, Decisão: 8h, Correção: 48h | Análise: 2h, Decisão: 4h, Correção: 24h |
| **MEDIUM** | Análise: 24h, Decisão: 3d, Correção: 30d | Análise: 8h, Decisão: 24h, Correção: 14d | Análise: 4h, Decisão: 8h, Correção: 7d |
| **LOW** | Análise: 48h, Decisão: 7d, Correção: próximo release | Análise: 24h, Decisão: 3d, Correção: 30d | Análise: 8h, Decisão: 24h, Correção: 14d |

**SLA para escalações:**
- Conflito de decisão: Resolução em 4h (CRITICAL), 8h (HIGH), 24h (MEDIUM/LOW)
- False positive dispute: Peer review em 24h
- Adequacy of compensating controls: Validação por 2º AppSec Engineer em 24h

---

## 📈 KPIs de Decisão

**Objetivo:** Monitorizar qualidade do processo de decisão

1. **Cobertura de análise C1:**
   - Meta: 100% findings CRITICAL/HIGH têm C1 documentado
   - Medição: `(Findings com C1 / Total findings) × 100`
   - Frequência: Semanal
   - Alerta: Se <95% em L2/L3

2. **Tempo-de-decisão:**
   - Meta: 95% findings decididos dentro do SLA
   - Medição: Tempo desde deteção até decisão formal (T1 preenchido)
   - Frequência: Semanal
   - Alerta: Se <90% no SLA

3. **Taxa de bloqueio de pipeline:**
   - Meta: <10% pipelines bloqueadas por findings
   - Medição: `(Pipelines bloqueadas / Total pipelines) × 100`
   - Frequência: Diária
   - Alerta: Se >15% (indica ferramentas mal-configuradas ou FP excessivos)

4. **Taxa de aceitação de risco:**
   - Meta: <5% findings CRITICAL/HIGH aceites sem correção
   - Medição: `(Findings ACEITAR-RISCO / Total findings) × 100`
   - Frequência: Mensal
   - Alerta: Se >10% (indica pressão excessiva de timeline ou fadiga de alertas)

5. **Taxa de false positives:**
   - Meta: <20% findings são suprimidos como FP
   - Medição: `(Findings suprimidos FP / Total findings) × 100`
   - Frequência: Mensal
   - Alerta: Se >30% (indica ferramenta mal-configurada)

6. **Compliance com SLA de correção:**
   - Meta: ≥90% correções concluídas dentro do SLA
   - Medição: `(Correções no SLA / Total correções) × 100`
   - Frequência: Semanal
   - Alerta: Se <85%

7. **Taxa de escalação:**
   - Meta: <5% findings requerem escalação
   - Medição: `(Escalações / Total findings) × 100`
   - Frequência: Mensal
   - Alerta: Se >10% (indica processo de decisão ineficaz)

---

## ⚖️ Proporcionalidade L1–L3

| Nível | Checklist C1 Obrigatório? | Template T1 Obrigatório? | Escalação T2? | Matriz Decisores? |
|---|---|---|---|---|
| **L1** | CRITICAL/HIGH | CRITICAL/HIGH | Recomendado | Simplificada (Developer + AppSec) |
| **L2** | CRITICAL/HIGH/MEDIUM | CRITICAL/HIGH | Obrigatório | Completa (Developer + AppSec + Tech Lead + CISO) |
| **L3** | Todos (≥LOW) | CRITICAL/HIGH/MEDIUM | Obrigatório | Completa + GRC (CRITICAL) |

---

## 🔗 Integração com Outros Capítulos

- **Cap 02 (Requisitos):** Findings devem referenciar requisitos violados (ex: `REQ-AUTH-001`)
- **Cap 06 (Desenvolvimento Seguro):** SAST findings seguem mesmo framework de decisão (addon-11 de Cap 06)
- **Cap 07 (CI/CD):** Gates usam decisões formais para bloquear/permitir deploy
- **Cap 09 (Containers):** Scanner de vulnerabilidades usa mesmo framework (addon-11 de Cap 09)
- **Cap 12 (Monitorização):** Findings de runtime/produção seguem processo similar

---

## 📎 Referências Cruzadas

| Documento | Relação |
|---|---|
| [addon-12: Validação Empírica de Findings](./addon-12-validacao-empirica-findings) | Complementa com testes de exploração |
| [addon-08: Gestão de Findings](./08-gestao-findings) | Plataforma centralizada e triagem |
| [US-10: Gestão Centralizada de Findings](../aplicacao-lifecycle#us-10) | Operacionalização em SDLC |
| [Cap 02 addon-11: Validação Assistida](../../02-requisitos-seguranca/addon/11-validacao-requisitos-assistida) | FP/FN management templates |
| [agent.md: Invariante I1](https://github.com/your-org/agent-spec) | Fundamento normativo |

---

## 🔄 Revisão e Melhoria Contínua

**Revisão periódica do framework:**
- Trimestral (L2/L3): Análise de KPIs, ajuste de thresholds, feedback de equipas
- Anual (L1): Revisão de processo, atualização de templates

**Triggers de revisão:**
- Taxa de FP >30% → Reconfigurar ferramentas ou atualizar checklist C1
- Taxa de escalação >10% → Simplificar processo de decisão ou reforçar training
- SLA não cumprido em >15% casos → Rever matriz de decisores ou adicionar recursos

---

> 📌 Separar sugestão de decisão não é burocracia — é engenharia.  
> Ferramentas sugerem, humanos decidem com contexto, evidência e rastreabilidade.
