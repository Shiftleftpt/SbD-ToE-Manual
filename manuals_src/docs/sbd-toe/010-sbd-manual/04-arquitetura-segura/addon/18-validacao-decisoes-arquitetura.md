---
id: validacao-decisoes-arquitetura
title: Validação Assistida de Decisões de Arquitetura — Separação Sugestão/Decisão
description: Framework I1 para garantir que ferramenta sugere padrões/ADRs, mas humano decide e aprova
tags: [addon, validacao-assistida, i1, arquitetura, decisao, adr, trust-boundaries]
---

# 🏛️ Validação Assistida de Decisões de Arquitetura — Separação Sugestão/Decisão

## 🎯 Objetivo

Este addon estabelece o **Invariante I1 (Separação entre Sugestão e Decisão)** no contexto de Arquitetura Segura, garantindo que:

- **Ferramentas sugerem padrões arquiteturais**, mas decisão final (aceitar, adaptar, rejeitar) é **sempre humana**
- **Responsabilidade clara**: Quem decidiu ADR? Com que critério? Quem aprovou exceção?
- **Escalação estruturada**: Conflitos entre Arquiteto e AppSec resolvem-se com checklist, não com suposição
- **Conformidade regulatória**: Decisões rastreáveis (audit trail) com aprovadores nomeados

**Contexto normativo:**  
Este addon implementa o **Invariante I1 (Separação sugestão/decisão)** de [agent.md](https://github.com/your-org/agent-spec). Complementa [addon-04](./04-diagramas-referencia) (padrões) e [addon-06](./06-rastreabilidade) (rastreabilidade decisões).

---

## 🚨 Cenários de Risco — Quando I1 é Violado

### Cenário 1: Ferramenta Sugere Padrão, Ninguém Valida

**Exemplo crítico:**
```yaml
# Ferramenta: "Para app L3, use padrão Microservices com API Gateway"
# ADR gerada automaticamente: ADR-042-microservices-pattern.md
Decisor: <ninguém registado>
Validação: <não realizada>
Aprovação: <automática>
Requisito gerado: ARC-MS-001 (aplicado sem revisão)
```

**Risco:**
- Padrão pode ser inadequado (app simples, over-engineering)
- Custo operacional não considerado (Kubernetes, service mesh)
- Nenhuma auditoria possível ("por que foi decidido microservices vs. monolith?")

---

### Cenário 2: Ferramenta Rejeita Decisão Real

**Exemplo crítico:**
```yaml
# Ferramenta: "API Gateway deve usar mTLS para todas integrações"
# Realidade: Integração legacy não suporta mTLS (parceiro externo)
# Arquiteto propõe: IP whitelisting + API key como compensação
# Ferramenta bloqueia: "Não conforme com padrão"
```

**Risco:**
- Decisão técnica válida bloqueada por automação rígida
- Exceção não é documentada corretamente
- Impasse entre Arquiteto e ferramenta

---

### Cenário 3: Decisão Tomada por Papel Errado

**Exemplo crítico:**
```yaml
# Developer decide: "Trust boundary entre frontend e backend não é necessário"
# Justificação: "Está tudo no mesmo pod"
Decisor: Developer João Silva
Aprovação: <nenhuma>
AppSec não foi consultado
```

**Risco:**
- Decisão de segurança crítica tomada sem expertise
- Trust boundary removido pode levar a lateral movement
- Não há trilho de auditoria

---

## 🔐 Procedimento de Validação — Framework I1

### Fase 1: Ferramenta Sugere Decisão Arquitetural

**Entrada:** Ferramenta (Backstage, PlantUML, AWS Well-Architected Tool) sugere padrão/ADR/trust boundary

**Artefato:** `architecture-proposals/proposal-XXX.md`

```yaml
# Exemplo: Proposta de padrão sugerida por ferramenta
proposal_id: PROP-001
titulo: "Migração de Monolith para Microservices"
fonte_ferramenta: "AWS Well-Architected Tool"
data_sugestao: "2026-01-15"
justificacao_ferramenta: |
  App classificada L3 com >10 domains lógicos.
  Ferramenta sugere separação em microservices para:
  - Escalabilidade independente
  - Deploy contínuo por domínio
  - Redução de blast radius
padrão_sugerido: "Microservices + API Gateway + Service Mesh"
requisitos_associados: "ARC-MS-001, ARC-MS-002, ARC-SEC-010"
```

---

### Fase 2: Arquiteto Valida Contexto (Checklist I1)

**Papéis:** Arquiteto de Software + AppSec Engineer

**Checklist de validação:**

:::userstory
**História.**  
Como **Arquiteto de Software**, quero **validar proposta de padrão antes de aceitar**, para garantir que reflecte necessidades reais e não apenas "best practice" genérico.

**Critérios de aceitação (BDD).**
- **Dado** que ferramenta sugere padrão/ADR  
  **Quando** valido contra contexto organizacional e técnico  
  **Então** decido: aceitar, adaptar, rejeitar (com justificação)

**Checklist I1 — Validação de Proposta Arquitetural.**

- [ ] **Proposta é relevante para esta aplicação?**
  - [ ] Complexidade atual justifica padrão sugerido?
  - [ ] Equipa tem expertise para implementar/operar?
  - [ ] Custos operacionais são aceitáveis?
  - **Sim** → Ir para próximo; **Não** → Rejeitar (ver justificação abaixo)

- [ ] **Proposta foi validada empiricamente?**
  - [ ] Proof-of-concept ou piloto realizado?
  - [ ] Comparação com alternativas (ex: monolith modular vs. microservices)?
  - [ ] AppSec Engineer confirma que controlos são viáveis?
  - **Não validado empiricamente** → Marcar como "PENDENTE VALIDAÇÃO" (fase 3)

- [ ] **Controlo mitigador já existe?**
  - [ ] Arquitetura atual já implementa benefícios do padrão?
  - [ ] Ex: Monolith com módulos bem isolados = sem necessidade de microservices?
  - **Sim, objetivo já alcançado** → Rejeitar padrão (over-engineering)

- [ ] **Proposta requer novos requisitos?**
  - [ ] Se aprovada: mapeá-la para ARC-XXX existente ou criar novo?
  - [ ] Requisito está já no Catálogo Cap 02?
  - [ ] Se não: criar novo cartão no backlog

- [ ] **Propor decisão:**
  - [ ] **ACEITAR**: Padrão adequado, criar ADR formal
  - [ ] **ADAPTAR**: Padrão parcialmente relevante (simplificar ou modificar)
  - [ ] **REJEITAR**: Padrão inadequado (over-engineering, custo excessivo, expertise insuficiente)

**Artefatos esperados:**
- Template de decisão (ver Fase 3)
- ADR formal se ACEITAR
- Ligação a commit/issue no backlog (rastreabilidade)

:::

---

### Fase 3: Decisão Documentada e Aprovada

**Papéis:** Arquiteto (sugestão) + AppSec Engineer (validação) + CISO/Product Owner (aprovação se impacto alto)

**Formato:** ADR com decisores explícitos

```markdown
# ADR-042: Migração de Monolith para Microservices

## Status
**Aceite** | 2026-01-16

## Decisores
- **Proponente**: Maria Arquiteta (Arquiteto de Software), 2026-01-15
- **Validador técnico**: João AppSec (AppSec Engineer), 2026-01-16
- **Aprovador impacto**: Pedro PO (Product Owner), 2026-01-16
- **Aprovador segurança**: Rita CISO (CISO), 2026-01-17 (decisão L3 crítica)

## Contexto
Aplicação monolítica L3 com 12 domínios lógicos, 80 developers, deploy mensal (bloqueante).
AWS Well-Architected Tool sugere microservices para reduzir coupling e permitir deploy contínuo.

## Opções consideradas
1. **Microservices completo** (sugestão ferramenta)
   - Prós: Deploy independente, escalabilidade granular
   - Contras: Complexidade operacional, custo infraestrutura (+30%)
2. **Monolith modular** (Arquiteto propõe)
   - Prós: Simplicidade operacional, custo baixo
   - Contras: Deploy ainda acoplado, escalabilidade limitada
3. **Hybrid approach** (Arquiteto + AppSec propõem)
   - Prós: Extração gradual de services críticos, custo controlado
   - Contras: Período de transição complexo

## Decisão
**ADAPTAR proposta: Hybrid approach**  
Começar com monolith modular, extrair 3 services críticos:
- Auth Service (REQ-AUT, isolamento credentials)
- Payment Service (PCI-DSS, compliance separado)
- Notification Service (async, alta carga)

## Justificação
- Equipa não tem experiência em service mesh (6m formação necessária)
- Custo de Kubernetes cluster não aprovado para ano fiscal corrente
- Extração gradual reduz risco de big-bang migration
- 3 services cobrem 80% dos problemas de deploy atual

## Consequências
### Positivas
- Deploy de Auth/Payment/Notification desacoplado do monolith (release independente)
- Redução de blast radius para mudanças críticas
- Compliance PCI-DSS isolado em Payment Service

### Negativas
- Arquitetura híbrida temporária (2-year transition plan)
- Necessidade de API Gateway (novo componente)
- Developers precisam aprender async communication (Kafka)

## Controlos de Segurança Aplicados
- ARC-MS-001: Segregação de services com network policies
- ARC-SEC-010: mTLS entre services (Istio service mesh para 3 services)
- ARC-SEC-015: Secrets management com Vault (não em env vars)
- ARC-LOG-001: Logging centralizado (ELK Stack) com correlation IDs

## Risco Residual
**MÉDIO**: Período de transição com monolith + microservices simultaneamente
- Mitigação: Feature flags para rollback rápido
- Prazo: 18 meses para migração completa
- Revisão: Trimestral, avaliar se mais services devem ser extraídos

## Evidência de Validação
- **PoC**: Auth Service extraído em ambiente QA, testes de carga OK (500 req/s)
- **SAST**: Semgrep valida secrets management (nenhum hardcoded)
- **DAST**: OWASP ZAP teste de lateral movement entre services → BLOQUEADO ✅
- **Code review**: Arquiteto + AppSec aprovaram network policies

## Rastreabilidade
- GitHub issue: #4567 "Migrate to Microservices"
- Epic Jira: ARCH-123
- Commits: abc123...def456 (migration plan)
- Requisitos: ARC-MS-001 v2.0, ARC-SEC-010 v1.1

## Próxima Revisão
**2026-04-15** (3 meses) — Validar se 3 services estão estáveis em produção
**Revisor**: TBD (Arquiteto + AppSec)
```

---

### Fase 4: Escalação de Conflitos

**Cenário:** Ferramenta sugere padrão, mas Arquiteto discorda (ex: "custo operacional inviável")

**Processo de escalação:**

| Conflito | Decisor | Critério | Artefato |
|---|---|---|---|
| **Padrão viável vs. Over-engineering** | Arquiteto + AppSec + Product Owner | Custo/benefício, expertise disponível, PoC | `architecture-escalations/ESC-XXX.md` |
| **Segurança vs. Pragmatismo** | AppSec Lead + CISO | Risco aceitável vs. deadline negócio | Revisão em comité técnico |
| **Decisão vs. Execução defasada** | DevOps/SRE + Arquiteto | Validação se padrão foi implementado conforme ADR | Teste em CI/CD (policies passing?) |

**Template de escalação:**

```markdown
# Escalação — PROP-001 (Microservices Pattern)

## Conflito
Ferramenta sugere: "Microservices com Kubernetes + Istio service mesh"
Arquiteto nega: "Equipa sem experiência, custo >30%, 6 meses setup"

## Consenso necessário
Product Owner valida: Budget não disponível, prioridade é time-to-market
AppSec Engineer valida: Monolith modular + 3 services extraídos = suficiente para L3

## Decisão
**ADAPTAR proposta**: Hybrid approach (monolith + 3 extracted services)
Documentar em ADR-042 com justificação de custo e expertise.
```

---

## 🔗 Integração com Catálogo de Requisitos (Cap 02)

**Ligação:** Cada decisão arquitetural → Mapeamento para `ARC-XXX` no Cap 02

| Decisão Aceita | Tipo Decisão | Requisito Cap 02 | Status |
|---|---|---|---|
| ADR-042 (Hybrid microservices) | ADAPTAR | ARC-MS-001 v2.0, ARC-SEC-010 v1.1 | Implementado |
| ADR-043 (API Gateway pattern) | ACEITAR | ARC-GW-001 v1.0 | Pendente |
| ADR-044 (Service mesh full) | REJEITAR | N/A | N/A |

---

## 👥 Matriz de Decisores por Tipo de Decisão

| Severidade/Impacto | Papel Primário | Validação | Aprovação | SLA |
|---|---|---|---|---|
| **CRÍTICA** (mudança estrutural L3) | Arquiteto | AppSec Lead + DevOps/SRE | CISO + Product Owner | 5 dias |
| **ALTA** (novo padrão L2/L3) | Arquiteto | AppSec Engineer | AppSec Lead + Product Owner | 7 dias |
| **MÉDIA** (adaptação de padrão) | Arquiteto + Developer | AppSec Engineer | Arquiteto | 10 dias |
| **BAIXA** (decisão local L1) | Developer | Nenhuma (opcional) | N/A | 14 dias |

---

## 📊 KPIs e Monitorização

| KPI | Meta | Frequência | Ação |
|---|---|---|---|
| **% ADRs com decisor documentado** | 100% | Mensal | Bloquear release se ADR sem decisor |
| **Tempo médio de decisão** | <7 dias (ALTA) | Mensal | Elevar se SLA excedido |
| **% propostas rejeitadas** | 20-40% | Trimestral | Se <10%, ferramenta over-suggests; se >60%, ferramenta inadequada |
| **% decisões com validação técnica** | 100% (CRÍTICA, ALTA) | Mensal | Adicionar PoC se faltar |
| **% decisões com aprovação formal** | 100% (L2, L3) | Mensal | Audit log |

---

## 📐 Proporcionalidade por Nível

| Aspecto | L1 | L2 | L3 |
|---|---|---|---|
| **Checklist I1 obrigatório?** | Recomendado (decisões críticas) | Obrigatório (todas decisões estruturais) | Obrigatório (todas) |
| **Validação técnica (PoC)** | Opcional | Recomendado (crítica/alta) | Obrigatório (100%) |
| **Aprovação formal** | Não | Obrigatório (AppSec) | Obrigatório (AppSec + CISO) |
| **Tempo de decisão** | Flexível | 7 dias máximo | 5 dias máximo |
| **Rastreabilidade (audit trail)** | Mínima (ADR) | Completa (ADR + validação) | Completa + imutável |

---

## ✅ Checklist de Implementação

- [ ] Template de ADR com decisores criado (`adr/template-decision.md`)
- [ ] Matriz de decisores comunicada (Arquitetos, AppSec, Product Owner, CISO)
- [ ] Processo de escalação documentado e testado (mínimo 1 caso)
- [ ] Validação técnica configurada (PoC obrigatório para CRÍTICA?)
- [ ] Integração com Cap 02 — Cada ADR mapa para ARC-XXX
- [ ] KPIs configurados (dashboard ou planilha)
- [ ] Alertas críticos (ADR CRÍTICA sem decisão bloqueará release?)
- [ ] Formação: Arquitetos e AppSec entendem Checklist I1 e papéis

---

**Última atualização**: 2026-01-01  
**Versão do addon**: 1.0.0  
**Autores**: Arquitetos de Software + AppSec Team + DevOps/SRE  
**Aprovação**: [Nome do CISO/Gestão Executiva] — [Data]
