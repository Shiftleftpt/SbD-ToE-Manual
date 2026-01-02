---
id: validacao-atualizacoes-assistida
title: Validação Assistida de Atualizações de Dependências — Separação Sugestão/Decisão
description: Garantir que bots de atualização (Dependabot, Renovate) sugerem mas não decidem autonomamente sobre updates críticos
tags: [addon, validacao-assistida, i1, dependencias, bots, renovate, dependabot]
---

# 🤖 Validação Assistida de Atualizações de Dependências — Separação Sugestão/Decisão

## 🎯 Objetivo

Este addon estabelece o **Invariante I1 (Separação entre Sugestão e Decisão)** no contexto de gestão de dependências, garantindo que:

- **Bots sugerem atualizações, humanos decidem** — Não há "auto-merge" cego para dependências críticas
- **Decisão baseada em checklist técnico** — Breaking changes? Team expertise? Testes cobrem?
- **Decisores explícitos** — Developer propõe, AppSec valida, Product Owner aprova impacto
- **Escalation procedures** — Conflitos entre segurança (update CVE) vs. estabilidade (breaking changes) têm caminho claro

**Contexto normativo:**  
Este addon implementa o **Invariante I1 (Separação Sugestão/Decisão)** de [agent.md](https://github.com/your-org/agent-spec). Complementa [addon-05](./05-politica-atualizacoes) (política geral) e [addon-04](./04-integracao-ci-cd) (integração CI/CD).

---

## 🚨 Cenários de Risco — Quando I1 é Violado

### Cenário 1: Bot Faz "Auto-Merge" de Update com Breaking Changes

**Exemplo crítico:**
```yaml
# Dependabot abre PR: "Bump axios 0.21.1 → 1.6.0"
# Release notes: "BREAKING: Remove deprecated methods, change timeout behavior"
# CI: ✅ Tests pass (mas testes não cobrem deprecated methods)
# Bot config: auto_merge: true (porque semver = minor)
# Resultado: Auto-merge → Deploy → Timeout de 30s mudou para 5s → Serviço falha em prod

# Risco:
# - Breaking change não detectado por testes
# - Auto-merge sem validação humana
# - Prod down
```

**Impacto:**
- Indisponibilidade de serviço crítico
- Rollback de emergência
- SLA impactado

---

### Cenário 2: Bot Rejeita Update Crítico de Segurança (CVE)

**Exemplo crítico:**
```yaml
# CVE-2023-44487: HTTP/2 Rapid Reset DoS (CRITICAL)
# Afeta: nghttp2 < 1.57.0
# Dependabot abre PR: "Bump nghttp2 1.55.0 → 1.57.0"
# Release notes: "Breaking: Removed deprecated H2 push support"
# Developer comenta: "Breaking change, postpone until Q2"
# Bot fecha PR automaticamente (flag: requires-manual-review)

# Realidade: CVE exploited in the wild, DDoS attacks em curso
# Risco: Vulnerabilidade crítica não mitigada por "postpone"
```

**Impacto:**
- Exposição ativa a CVE CRITICAL
- Potencial exploração (DoS)
- Não-conformidade (SLA de 48h para CRITICAL CVE em L3)

---

### Cenário 3: Decisão de Update sem Papel Adequado

**Exemplo crítico:**
```yaml
# Renovate abre PR: "Bump Spring Boot 2.7.8 → 3.0.0"
# Breaking: Mudança de javax.* → jakarta.*, authentication API alterada
# Developer júnior: "Auto-merge because tests green" ✅
# AppSec não consultado (autenticação API mudou)
# Product Owner não consultado (migration effort = 3 sprints)

# Resultado: Deploy → Auth falha → 500 errors → Rollback
```

**Impacto:**
- Decisão tomada por papel inadequado
- Impacto técnico + negócio não avaliado
- Re-trabalho

---

## 🔐 Procedimento de Validação Assistida — Framework I1

### Fase 1: Bot Propõe Atualização (Suggestion)

**Entrada:** Bot (Dependabot, Renovate, GitHub Advanced Security) detecta nova versão disponível

**Outputs da proposta:**
- **PR automatizado** com:
  - Título: `[Bot] Bump <library> <old_version> → <new_version>`
  - Labels: `dependencies`, `security` (se CVE), `breaking-change` (se major semver)
  - Release notes: Link para CHANGELOG, breaking changes destacados
  - Semver analysis: PATCH (x.y.Z) / MINOR (x.Y.z) / MAJOR (X.y.z)
  - CVE linkage: Se update mitiga CVE, incluir CVE-ID + severity + EPSS score
  - Test status: CI tests pass/fail
  - Impact analysis: Chamadas afetadas (static analysis), arquivos tocados

**Classificação automática:**
- **Auto-merge candidate** (PATCH, no breaking, CI green, no CVE) → Label `auto-merge-safe`
- **Requires review** (MINOR com breaking hints, MAJOR, CVE fix) → Label `requires-human-review`
- **Critical security** (CVE CRITICAL/HIGH) → Label `security-critical`

---

### Fase 2: Validação com Checklist I1

**Papel:** Developer (proposta inicial) → AppSec (validação segurança) → Product Owner (aprovação impacto)

:::userstory
**História.**  
Como **Developer**, quero validar proposta de atualização de dependência com checklist I1, para decidir ACEITAR/ADAPTAR/REJEITAR update de forma informada.

**Critérios de aceitação (BDD).**
- **Dado** que bot abre PR de atualização  
  **Quando** executo Checklist I1  
  **Então** decisão é registada com decisores explícitos e justificação

**Checklist I1 — Validação de Proposta de Atualização.**

#### **1. Relevância**
- [ ] **Breaking changes?**  
  - Ler release notes, CHANGELOG, migration guides  
  - Verificar se métodos/APIs utilizados no projeto foram alterados  
  - Resultado: SIM (major/breaking) / NÃO (compatível)
  
- [ ] **Team expertise?**  
  - Equipa conhece nova versão? Precisa formação?  
  - Tempo disponível para migration? (se breaking)  
  - Resultado: ADEQUADA / INSUFICIENTE (requer estudo)
  
- [ ] **Custos aceitáveis?**  
  - Esforço migration: 1d (patch) / 1 sprint (minor) / 3 sprints (major)?  
  - Budget aprovado para migration?  
  - Resultado: ACEITÁVEL / EXCEDE ORÇAMENTO

#### **2. Evidência Empírica**
- [ ] **Testes cobrem?**  
  - CI tests existentes validam nova versão?  
  - Precisa novos testes (ex: nova API de auth)?  
  - Resultado: COBERTURA ADEQUADA / GAPS (adicionar testes)
  
- [ ] **PoC/staging validado?**  
  - Se breaking, testar em staging antes de merge?  
  - Rollback plan existe?  
  - Resultado: VALIDADO / PENDENTE

#### **3. Controlo Existente**
- [ ] **Vulnerabilidade real?**  
  - Se update mitiga CVE, código atual é vulnerável?  
  - CVE exploitável no nosso contexto? (ver addon-21)  
  - Resultado: VULNERÁVEL (update urgente) / NÃO APLICÁVEL (FP)

#### **4. Novos Requisitos**
- [ ] **Mapeia a DEP-XXX?**  
  - Update cria novos requisitos (ex: nova config necessária)?  
  - Documentação precisa atualização?  
  - Resultado: MAPEADO / CRIAR REQ-DEP-XXX

#### **5. Decisão Proposta**
- [ ] **ACEITAR**: Update sem breaking, CI green, sem impacto → Auto-merge OK
- [ ] **ADAPTAR**: Update com breaking, mas necessário (CVE) → Migration plan + staging
- [ ] **REJEITAR**: Update breaking, sem CVE crítico, postpone para Q2 → VEX justificado

:::

---

### Fase 3: Decisão Documentada com Decisores Explícitos

**Artefato:** Comentário no PR com template decisão

```markdown
## 🔐 Decisão de Atualização — Checklist I1

**Dependência:** axios 0.21.1 → 1.6.0  
**CVE associado:** CVE-2023-45857 (HIGH — Server-Side Request Forgery)  
**Data:** 2026-01-15  

### Decisores
- **Proponente:** Renovate Bot (automated)
- **Validador técnico:** João Developer (2026-01-15)
- **Validador segurança:** Maria AppSec (2026-01-16)
- **Aprovador impacto:** Pedro Product Owner (2026-01-16)

### Checklist I1
✅ Breaking changes? **SIM** — Deprecated `axios.get(url, config)` → `axios.get({url, ...config})`  
✅ Team expertise? **ADEQUADA** — Team conhece axios, migration simples  
✅ Custos? **ACEITÁVEL** — 2 dias migration (10 chamadas afetadas)  
✅ Testes cobrem? **PARCIAL** — CI testa 8/10 chamadas, adicionar 2 testes  
✅ PoC validado? **SIM** — Staging OK, rollback plan: revert commit abc123  
✅ Vulnerabilidade real? **SIM** — SSRF exploitável em endpoint `/proxy` (L2)  
✅ Novos requisitos? **NÃO** — Config compatível  

### Decisão: **ADAPTAR**
- **Justificação:** CVE HIGH exploitável requer mitigação urgente (SLA 7d L2), mas breaking change exige migration
- **Plano:**
  1. Adicionar 2 testes para chamadas não cobertas
  2. Migration: Atualizar 10 chamadas axios (2d)
  3. Deploy staging → validação QA → prod (canary 10% → 100%)
  4. Rollback plan: Git revert + redeploy v1.2.3
- **Risco residual:** BAIXO (após migration)
- **SLA:** Completar até 2026-01-22 (7d)

### Evidências
- PoC staging: [Link logs]
- Testes adicionados: PR #456
- Migration guide: docs/axios-migration.md
- Aprovação AppSec: maria.appsec@example.com (2026-01-16)
- Aprovação PO: pedro.po@example.com (2026-01-16)

### Rastreabilidade
- CVE: CVE-2023-45857
- Jira: SEC-789
- Commits: abc123, def456
- Deploy: prod-v1.3.0 (2026-01-22)
```

---

### Fase 4: Escalation para Conflitos

**3 tipos de conflitos comuns:**

#### **Conflito 1: Segurança (CVE CRITICAL) vs. Estabilidade (Breaking Changes)**

**Cenário:**
- CVE-2024-12345 (CRITICAL — RCE) afeta library X v2.0
- Update para v3.0 mitiga CVE mas introduz 15 breaking changes
- Developer: "Postpone até Q2 (3 sprints migration)"
- AppSec: "CVE CRITICAL com exploit ativo, SLA 48h"

**Escalation path:**
1. **Análise técnica** — AppSec confirma: CVE exploitável? EPSS >0.5? Exploit público?
2. **Workaround temporário** — Existe mitigação compensatória? (WAF rule, network isolation)
3. **Decisor final:** Product Owner + AppSec + CTO (L3)
   - **SE** exploit ativo + não há workaround → **ACEITAR update imediato** (migration emergencial)
   - **SE** workaround viável → **ADAPTAR** (workaround temporário + migration Q2 com prazo)
4. **Registro:** VEX document com justificação + prazo + revisão quinzenal

#### **Conflito 2: Update Recomendado (Security Patch) vs. Freeze de Produção**

**Cenário:**
- Black Friday freeze (15 Nov - 5 Dez)
- CVE-2024-99999 (HIGH — XSS) publicado 20 Nov
- Policy: No deploys durante freeze (exceto P0 incidents)

**Escalation path:**
1. **Severidade assessment** — AppSec avalia: Impacto real? User input afetado? Exploit público?
2. **Exceção ao freeze?**
   - **SE** CVE HIGH + exploit público + user input vulnerável → **Exceção aprovada** (deploy emergencial)
   - **SE** CVE HIGH mas não exploitável no contexto → **ADIAR** para pós-freeze (6 Dez) com VEX
3. **Decisor:** Product Owner + AppSec Lead
4. **Comunicação:** Stakeholders notificados (deploy emergencial justificado)

#### **Conflito 3: Developer Propõe Update vs. AppSec Rejeita (Supply Chain Risk)**

**Cenário:**
- Developer propõe: "Add library Y v1.0 (novo feature X)"
- AppSec scan: Library Y tem 0 maintainers ativos, último commit 2 anos atrás, CVE histórico não resolvido
- Developer: "Mas é a única lib que faz X"

**Escalation path:**
1. **Supply chain assessment** — AppSec avalia: Maintainers? Funding? Security audit? Alternativas?
2. **Alternativas:**
   - Existe lib alternativa mais segura?
   - Podemos desenvolver internamente? (custo vs. risco)
3. **Decisor:** Arquiteto + AppSec + Product Owner
   - **SE** risco supply chain ALTO → **REJEITAR** (escolher alternativa ou build interno)
   - **SE** não há alternativa + feature crítico → **ACEITAR COM CONDIÇÕES** (fork interno, security hardening, monitoring)
4. **Registro:** Exceção formal com prazo revisão trimestral

---

## 📋 Matriz de Decisores por Severidade

| Severidade Update | Tipo | Decisor Técnico | Validador Segurança | Aprovador Impacto | SLA Decisão |
|---|---|---|---|---|---|
| **PATCH (x.y.Z)** | Bug fix, no breaking | Developer | - | - | Auto-merge (se CI green) |
| **MINOR (x.Y.z) sem breaking** | New features, backward-compatible | Developer | - | - | 2 dias |
| **MINOR com hints breaking** | New features, deprecated warnings | Developer | AppSec (se deps críticas) | - | 5 dias |
| **MAJOR (X.y.z)** | Breaking changes | Developer + Arquiteto | AppSec | Product Owner | 10 dias |
| **CVE CRITICAL** | RCE, SQLi, auth bypass | Developer | AppSec Lead | Product Owner | 48h (L3) |
| **CVE HIGH** | XSS, SSRF, disclosure | Developer | AppSec | - | 7 dias (L2) |
| **CVE MEDIUM** | DoS, weak crypto | Developer | - | - | 30 dias (L1) |

---

## 📊 KPIs de Validação Assistida

| KPI | Fórmula | Meta | Ação |
|---|---|---|---|
| **% PRs com decisor explícito** | (PRs com comentário I1 / Total PRs bot) × 100 | 100% (L2/L3) | Se <80%: Treinar equipa |
| **Tempo médio decisão** | Dias entre PR aberto e merge/close | <5d (MINOR), <48h (CVE CRITICAL) | Se >SLA: Gargalo processo |
| **% auto-merge seguros** | (Auto-merge PATCH OK / Total auto-merge) × 100 | >95% | Se <90%: Tuning bot config |
| **% CVE com SLA cumprido** | (CVE mitigados dentro SLA / Total CVE) × 100 | >90% | Se <80%: Escalation inadequado |
| **% updates postponed** | (PRs postponed / Total PRs) × 100 | <20% | Se >30%: Debt técnico alto |

**Decision thresholds:**
- **% auto-merge <90%** → Bot config agressivo, muitos FP de "safe"
- **Tempo decisão >SLA** → Falta clareza papéis, ou overload equipa
- **% CVE com SLA <80%** → Escalation procedures inadequados

---

## 📐 Proporcionalidade por Nível

| Aspecto | L1 | L2 | L3 |
|---|---|---|---|
| **Checklist I1 obrigatório?** | Recomendado (MAJOR, CVE HIGH+) | Obrigatório (MINOR+, CVE MEDIUM+) | Obrigatório (todas atualizações) |
| **Decisores explícitos** | Developer | Developer + AppSec (CVE) | Developer + AppSec + PO (MAJOR/CVE) |
| **PoC/staging** | Opcional | Recomendado (MAJOR) | Obrigatório (MAJOR, CVE CRITICAL) |
| **Auto-merge permitido** | PATCH (CI green) | PATCH (CI green + no CVE) | PATCH (CI green + AppSec approved) |
| **SLA decisão CVE CRITICAL** | 7 dias | 7 dias | 48 horas |
| **Audit trail** | Comentário PR | Comentário PR + Jira | Comentário PR + Jira + immutable log |

---

## ✅ Checklist de Implementação

- [ ] Bot configurado (Dependabot/Renovate) com labels automáticos (`auto-merge-safe`, `requires-human-review`, `security-critical`)
- [ ] Template comentário I1 disponível em `.github/ISSUE_TEMPLATE/dependency-decision.md`
- [ ] Matriz decisores comunicada (quem decide PATCH/MINOR/MAJOR/CVE?)
- [ ] SLAs definidos por severidade (CRITICAL 48h, HIGH 7d, MEDIUM 30d)
- [ ] Escalation procedures documentados (3 conflitos comuns)
- [ ] Training: Developers + AppSec sabem usar checklist I1
- [ ] Dashboard KPIs configurado (% decisor explícito, tempo decisão, SLA CVE)
- [ ] Integração CI/CD: Bloqueio auto-merge se label `requires-human-review`
- [ ] VEX integration: Postponed updates geram VEX document automático
- [ ] Auditoria: Quarterly review de PRs fechados sem decisão explícita

---

**Última atualização**: 2026-01-01  
**Versão do addon**: 1.0.0  
**Autores**: Developers + AppSec Engineers + Product Owners  
**Aprovação**: [Nome do AppSec Lead/CTO] — [Data]
