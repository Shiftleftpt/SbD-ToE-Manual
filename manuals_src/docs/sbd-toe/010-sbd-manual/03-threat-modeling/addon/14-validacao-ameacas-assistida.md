---
id: validacao-ameacas-assistida
title: Validação Assistida de Ameaças — Separação Sugestão/Decisão
description: Framework para garantir que ferramenta sugere ameaças, mas humano decide e aprova
tags: [addon, validacao-assistida, i1, ameacas, threat-modeling, ferramenta, decisao]
---

# 🛠️ Validação Assistida de Ameaças — Separação Sugestão/Decisão

## 🎯 Objetivo

Este addon estabelece o **Invariante I1 (Separação entre Sugestão e Decisão)** no contexto de Threat Modeling, garantindo que:

- **Ferramentas sugerem ameaças**, mas decisão final (aceitar, rejeitar, adaptar) é **sempre humana**
- **Responsabilidade clara**: Quem decidiu aplicar/rejeitar ameaça? Com que critério?
- **Escalação estruturada**: Conflitos entre ferramenta e arquiteto resolvem-se com checklist, não com suposição
- **Conformidade regulatória**: Decisões rastreáveis (audit trail) com aprovadores nomeados

**Contexto normativo:**  
Este addon implementa o **Invariante I1 (Separação sugestão/decisão)** de [agent.md](https://github.com/your-org/agent-spec). Complementa [addon-01](./01-metodologias-e-ferramentas) (ferramentas) e [addon-07](./07-mapeamento-threats-requisitos) (mapeamento threats→requisitos).

---

## 🚨 Cenários de Risco — Quando I1 é Violado

### Cenário 1: Ferramenta Sugere Ameaça, Ninguém Valida

**Exemplo crítico:**
```yaml
# IriusRisk gera automaticamente (❌ MAU)
TM-GENERATED-001: "OWASP A01:2021 Broken Access Control — Endpoint /admin não valida role"
Severidade: CRÍTICA
Decisor: <ninguém registado>
Validação: <não realizada>
Requisito gerado: REQ-AC-001 (automático, sem aprovação)
```

**Risco:**
- Ameaça pode ser falsa (endpoint já está protegido)
- Requisito gerado pode ser inadequado para contexto
- Nenhuma auditoria possível ("por que foi decidido isto?")

---

### Cenário 2: Ferramenta Rejeita Ameaça Real

**Exemplo crítico:**
```yaml
# IriusRisk não deteta (porque modelo DFD incompleto):
# TM-MISSING-042: "JWT token armazenado em localStorage (XSS) vs. httpOnly"
# Ameaça real, mas ferramenta não sugeriu → ninguém realiza teste
```

**Risco:**
- Ameaça real não é mitigada
- Vulnerabilidade descobre-se apenas em teste manual ou em produção

---

### Cenário 3: Decisão Tomada por Papel Errado

**Exemplo crítico:**
```yaml
# Developer decide que TM-GENERATED-102 (Sensitive Data Exposure) é "aceitável por negócio"
# Sem aprovação de AppSec ou Product Owner
Decisor: Developer João Silva
Justificação: "O negócio precisa desta feature"
Aprovação: <nenhuma>
```

**Risco:**
- Decisão não foi validada tecnicamente (AppSec não avaliou mitigação)
- Decisão não foi priorizada pelo negócio (Product Owner não foi consultado)
- Não há trilho de auditoria

---

## 🔐 Procedimento de Validação — Framework I1

### Fase 1: Ferramenta Sugere Ameaça

**Entrada:** Ferramenta (IriusRisk, OWASP Threat Dragon, análise manual) gera lista de ameaças

**Artefato:** `threats.yaml` ou issue em backlog

```yaml
# Exemplo: threats.yaml gerado por IriusRisk
threats:
  - id: TM-GEN-001
    titulo: "Spoofing de Identidade — JWT sem verificação de assinatura"
    severidade: CRÍTICA
    categoria: "STRIDE - Spoofing"
    descrição: "Aplicação aceita JWT com alg:none"
    fonte_ferramenta: "IriusRisk v2024.01"
    data_sugestao: "2026-01-15"
    
  - id: TM-GEN-002
    titulo: "Tampering — Dados em localStorage acessíveis via XSS"
    severidade: ALTA
    categoria: "STRIDE - Tampering"
    descrição: "localStorage não é protegido contra XSS; httpOnly não usado"
    fonte_ferramenta: "OWASP Threat Dragon"
    data_sugestao: "2026-01-15"
```

---

### Fase 2: Arquiteto Valida Contexto (Checklist I1)

**Papéis:** Arquiteto de Software + AppSec Engineer

**Checklist de validação:**

:::userstory
**História.**  
Como **Arquiteto de Software**, quero **validar ameaça sugerida antes de aceitar**, para garantir que reflecte riscos reais da aplicação.

**Critérios de aceitação (BDD).**
- **Dado** que ferramenta sugere ameaça TM-GEN-XXX  
  **Quando** valido contra arquitetura e contexto  
  **Então** decido: aceitar, adaptar, rejeitar (com justificação)

**Checklist I1 — Validação de Ameaça.**

- [ ] **Ameaça é relevante para esta aplicação?**
  - [ ] DFD contém componente mencionado na ameaça?
  - [ ] Fluxo de dados descrito existe no design?
  - [ ] Aplicação realmente está exposta a este risco?
  - **Sim** → Ir para próximo; **Não** → Rejeitar (ver justificação abaixo)

- [ ] **Ameaça foi validada empiricamente?**
  - [ ] Teste manual já realizado (ex: tentei fazer JWT com alg:none)?
  - [ ] Teste automático passa na pipeline (SAST detecta)?
  - [ ] AppSec Engineer confirma que é risco real?
  - **Não validado empiricamente** → Marcar como "PENDENTE VALIDAÇÃO" (fase 3)

- [ ] **Controlo mitigador já existe?**
  - [ ] Arquitetura já implementa proteção contra esta ameaça?
  - [ ] Ex: JWT sempre tem alg:HS256 (nunca é aceito alg:none)?
  - **Sim, controlo existe** → Ameaça é "MITIGADA" (teste e rejeitar ou reclassificar para LOW)

- [ ] **Ameaça requer novo requisito?**
  - [ ] Se aprovada: mapeá-la para REQ-XXX existente ou criar novo?
  - [ ] Requisito está já no Catálogo Cap 02?
  - [ ] Se não: criar novo cartão no backlog

- [ ] **Propor decisão:**
  - [ ] **ACEITAR**: Ameaça é real, sem controlo, criou novo REQ ou mapeia para existente
  - [ ] **ADAPTAR**: Ameaça é parcialmente real (contexto diferente), precisa refinamento
  - [ ] **REJEITAR**: Ameaça não é relevante (ex: aplicação não usa localStorage, ou controlo já existe)

**Artefatos esperados:**
- Template de decisão (ver Fase 3)
- Ligação a commit/issue no backlog (rastreabilidade)

:::

---

### Fase 3: Decisão Documentada e Aprovada

**Papéis:** Arquiteto (sugestão) + AppSec Engineer (validação) + Product Owner (prioridade)

**Formato:** Template de decisão de ameaça

```yaml
# Arquivo: threat-model/decisions/TM-GEN-001-decision.md

---
threat_id: TM-GEN-001
titulo: "Spoofing de Identidade — JWT sem verificação de assinatura"
data_decisao: "2026-01-15"
data_validade: "2026-07-15" # Reavalia em 6 meses para L2

# Quem decidiu
decididor_primario: "Maria Arquiteta (Arquiteto de Software)"
data_decisao: "2026-01-15"
validador: "João AppSec (AppSec Engineer)"
data_validacao: "2026-01-16"
aprovador_produto: "Pedro PO (Product Owner)"
data_aprovacao_produto: "2026-01-16"

# Decisão
decisao: "ACEITAR" # [ACEITAR | ADAPTAR | REJEITAR]
justificacao: |
  Ameaça é real. DFD mostra que JWT é gerado em /auth/login e validado em todos os endpoints.
  Teste manual (alg:none) confirma vulnerabilidade.
  Controlo recomendado: Validação de JWT com alg:HS256 obrigatório, nunca aceitar alg:none.
  Integrado com REQ-AUT-003 (JWT signature obrigatória).

# Mitigação proposta
requisito_associado: "REQ-AUT-003"
versao_requisito: "v2.0"
tipo_mitigacao: "Código" # [Código | Arquitetura | Operacional | Aceitação]
prazo_mitigacao: "2026-02-28" # Sprint 6
responsavel_mitigacao: "Equipa Auth Backend"

# Evidência de validação
validacao_tecnica: |
  - SAST (Semgrep): Detecção de alg:none em JWT → PASSING
  - Teste manual: tentei JWT com alg:none → BLOQUEADO ✅
  - Code review: JWT validation.ts linha 42-48 valida assinatura → OK
  - Teste de segurança (DAST): POST /auth/token com alg:none → 401 Unauthorized ✅

# Risco aceitável ou não?
risco_residual: "MUITO BAIXO" # [CRÍTICO | ALTO | MÉDIO | BAIXO | MUITO BAIXO]
risco_justificacao: "JWT é validado em todos os endpoints. Alg:none é rejeitado."

# Rastreabilidade
github_issue: "https://github.com/org/app/issues/1234"
commit_mitigacao: "abc123def (PR #567)"

# Próxima revisão
data_proxima_revisao: "2026-07-15"
revisor_proxima: "TBD"

---
```

---

### Fase 4: Escalação de Conflitos

**Cenário:** Ferramenta sugere ameaça, mas Arquiteto discorda (ex: "aplicação não está exposta a este risco")

**Processo de escalação:**

| Conflito | Decisor | Critério | Artefato |
|---|---|---|---|
| **Ameaça real vs. Falso Positivo** | AppSec Engineer + Arquiteto | Teste técnico (SAST, manual, DAST) prove ou refute | `threat-model/escalations/TM-GEN-XXX-escalation.md` |
| **Risco aceitável vs. Não aceitável** | AppSec Lead + Product Owner | Balanço risco/impacto negócio + deadline | Revisão em stand-up de segurança |
| **Decisão vs. Execução defasada** | DevOps/SRE + Arquiteto | Validação se mitigação foi implementada | Teste em CI/CD (SAST passing?) |

**Template de escalação:**

```markdown
# Escalação de Conflito — TM-GEN-XXX

## Conflito
Ferramenta sugere: "SQL Injection em endpoint /search"
Arquiteto nega: "Aplicação usa ORM (Sequelize) com prepared statements"

## Consenso necessário
AppSec Engineer valida: Teste manual SQL injection attempt → BLOQUEADO ✅
Conclusão: Falso Positivo (controlo já existe no ORM)

## Decisão
Rejeitar ameaça. Ameaça TM-GEN-XXX marcada como "FALSO POSITIVO".
Documentar em `falsos-positivos/FP-TM-GEN-XXX.md` para evitar sugestão repetida.
```

---

## 🔗 Integração com Catálogo de Requisitos (Cap 02)

**Ligação:** Cada ameaça aceita → Mapeamento para `REQ-XXX` no Cap 02

| Ameaça Aceita | Tipo Decisão | Requisito Cap 02 | Status |
|---|---|---|---|
| TM-GEN-001 (JWT alg:none) | ACEITAR | REQ-AUT-003 v2.0 | Implementado |
| TM-GEN-002 (localStorage XSS) | ADAPTAR | REQ-SES-002 v1.1 (novo: "Use httpOnly cookies") | Pendente |
| TM-GEN-003 (SQL injection) | REJEITAR (FP) | N/A | N/A |

---

## 👥 Matriz de Decisores por Tipo de Ameaça

| Severidade | Papel Primário | Validação | Aprovação | SLA |
|---|---|---|---|---|
| **CRÍTICA** | AppSec Engineer | AppSec Lead + Arquiteto | CISO + Product Owner | 2 dias |
| **ALTA** | Arquiteto | AppSec Engineer | AppSec Lead | 5 dias |
| **MÉDIA** | Developer + Arquiteto | AppSec Engineer | AppSec Engineer | 10 dias |
| **BAIXA** | Developer | Nenhuma (opcional) | N/A | 30 dias |

---

## 📊 KPIs e Monitorização

| KPI | Meta | Frequência | Ação |
|---|---|---|---|
| **% ameaças com decisão documentada** | 100% | Mensal | Bloquear release se ameaça sem decisão |
| **Tempo médio de decisão** | <5 dias (CRÍTICA) | Mensal | Elevar se SLA excedido |
| **% falsos positivos detectados** | >15% das ameaças | Trimestral | Avaliar qualidade da ferramenta |
| **% ameaças com teste técnico** | 100% (CRÍTICA, ALTA) | Mensal | Adicionar teste se faltar |
| **% decisões com aprovação formal** | 100% (L2, L3) | Mensal | Audit log |

---

## 📐 Proporcionalidade por Nível

| Aspecto | L1 | L2 | L3 |
|---|---|---|---|
| **Checklist I1 obrigatório?** | Recomendado (ameaças críticas) | Obrigatório (todas ameaças) | Obrigatório (todas) |
| **Validação técnica (teste)** | Opcional | Recomendado (crítica/alta) | Obrigatório (100%) |
| **Aprovação formal** | Não | Obrigatório (AppSec) | Obrigatório (AppSec + CISO) |
| **Tempo de decisão** | Flexível | 5 dias máximo | 2 dias máximo |
| **Rastreabilidade (audit trail)** | Mínima (decisão) | Completa (decisão + validação) | Completa + imutável |

---

## ✅ Checklist de Implementação

- [ ] Template de decisão de ameaça criado (`threat-model/decisions/template.md`)
- [ ] Matriz de decisores comunicada (AppSec, Arquitetos, Product Owner)
- [ ] Processo de escalação documentado e testado (mínimo 1 caso de escalação)
- [ ] Validação técnica configurada (SAST passing é pré-requisito?)
- [ ] Integração com Cap 02 — Cada ameaça aceita mapa para REQ-XXX
- [ ] KPIs configurados (dashboard ou planilha)
- [ ] Alertas críticos (ameaça CRÍTICA sem decisão bloqueará release?)
- [ ] Formação: Arquitetos e AppSec entendem Checklist I1 e papéis

---

**Última atualização**: 2026-01-01  
**Versão do addon**: 1.0.0  
**Autores**: AppSec Team + Arquitetos de Software + GRC/Compliance  
**Aprovação**: [Nome do CISO/Gestão Executiva] — [Data]
