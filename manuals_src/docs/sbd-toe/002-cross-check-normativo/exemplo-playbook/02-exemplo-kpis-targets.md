---
description: Exemplos de KPIs e targets para diferentes perfis organizacionais
id: exemplo-kpis-targets
tags:
- cra
- exemplos
- kpis
- metricas
- monitoramento
- monitorizacao
- targets
title: 'Exemplo: KPIs e Targets'
---


# Exemplo: KPIs e Targets

## Enquadramento

O SbD-ToE prescreve ([Cap. 12](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro)):
- ✓ Métricas de segurança
- ✓ Monitorização contínua
- ✓ Melhoria baseada em dados

O SbD-ToE **NÃO prescreve** targets específicos porque contextos variam. Este documento apresenta **exemplos para diferentes tipos de organização**.

---

## Dimensões de KPIs (Todas as Organizações)

O manual define estas dimensões ([Cap. 12](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro)):

1. **Risco Aplicacional** - Cobertura de ameaças
2. **Desenvolvimento** - Qualidade de código
3. **Operações** - Tempo de resposta
4. **Supply Chain** - Gestão de fornecedores
5. **Conformidade** - Evidência de auditoria

Para cada dimensão, apresentamos targets exemplares.

---

## Cenário 1: Fintech de Pagamentos (Startup, `<`50 devs)

### Contexto
- Serviço crítico: Processamento de pagamentos
- Deadline DORA: Janeiro 2025 (curto)
- Budget: Limitado
- Risk appetite: Baixo (pagamentos = PCI-DSS + DORA)

### KPIs e Targets

| Categoria | Métrica | Target | Período | Justificativa |
|-----------|---------|--------|---------|---------------|
| **Risco Aplicacional** | % apps classificadas | 100% | M1 | Urgente: DORA requer classificação |
| | Threat modeling (L3) | 100% | M3 | Antes de TLPT |
| | Vulns críticas não remediadas | 0 | Permanente | Pagamentos: zero tolerance |
| | Vulns altas não remediadas | 0 (ou `<`48h SLA) | Permanente | Impacto direto PCI |
| **Desenvolvimento** | Cobertura de testes | ≥80% | M6 | Progressivo: começar com funções críticas |
| | SAST findings altos | 0 | Permanente | Gate de CI/CD |
| | SCA findings altos | 0 | Permanente | Gate de CI/CD |
| **Operações** | MTTR P0 (Critical) | `<`2h | Permanente | Pagamentos: impacto direto |
| | MTTR P1 (High) | `<`8h | Permanente | Business impacto |
| | Incidents detetados/month | `<`5 | M12 | Reduzir com maturidade |
| **Supply Chain** | Fornecedores no inventário | 100% | M2 | DORA Art. 26 requer |
| | % com onboarding completo | 100% | M3 | Antes de acesso |
| | % com security trainning | 100% | M3 | Obrigatório antes acesso |
| **Conformidade** | Política assinada board | ✓ | M1 | DORA Art. 5 |
| | Trilho auditoria (logs) | 3 anos | M0 | Pré-requisito |
| | Staff SbD trainning | 100% devs | M4 | Ramp-up rápido |
| | Readiness inspeção | 95% | M12 | Antes inspeção supervisor |

### Dashboard (Exemplo visual)

```mermaid
%%{init: {'theme':'base', 'themeVariables': { 'fontSize':'13px'}}}%%
graph TB
    subgraph FINTECH["📊 FINTECH SEGURANÇA - Novembro 2025"]
        subgraph RISCO["🎯 RISCO APLICACIONAL"]
            R1["Apps classificadas: 100%<br/>🟢 OK"]
            R2["Threat modeling L3: 95%<br/>target: 98% | ⚠️ DELAYED"]
            R3["Critical vulns: 0<br/>🟢 OK"]
            R4["High vulns: 2<br/>target: 0 | 🔴 CRITICAL"]
        end
        
        subgraph DEV["⚙️ DESENVOLVIMENTO"]
            D1["Cobertura testes: 72%<br/>target: 80% | ⚠️ DELAYED"]
            D2["SAST findings altos: 0<br/>🟢 OK"]
            D3["SCA findings altos: 0<br/>🟢 OK"]
        end
        
        subgraph OPS["�� OPERAÇÕES"]
            O1["MTTR P0: 1.5h<br/>🟢 OK"]
            O2["MTTR P1: 6h<br/>🟢 OK"]
            O3["Incidents/month: 3<br/>target: <5 | 🟢 OK"]
        end
        
        subgraph SUPPLY["📦 SUPPLY CHAIN"]
            S1["Fornecedores inventariados: 100%<br/>🟢 OK"]
            S2["Com onboarding: 95%<br/>target: 100% | ⚠️ DELAYED"]
            S3["Com training: 95%<br/>target: 100% | ⚠️ DELAYED"]
        end
        
        subgraph CONF["📋 CONFORMIDADE"]
            C1["Política board: Assinada<br/>🟢 OK"]
            C2["Trilho auditoria: 3 anos<br/>🟢 OK"]
            C3["Staff training: 85%<br/>target: 100% | ⚠️ DELAYED"]
            C4["Readiness DORA: 92%<br/>target: 95% | ⚠️ DELAYED"]
        end
    end
    
    style R1 fill:#d4edda,stroke:#155724,stroke-width:2px
    style R2 fill:#fff3cd,stroke:#856404,stroke-width:2px
    style R3 fill:#d4edda,stroke:#155724,stroke-width:2px
    style R4 fill:#f8d7da,stroke:#721c24,stroke-width:2px
    style D1 fill:#fff3cd,stroke:#856404,stroke-width:2px
    style D2 fill:#d4edda,stroke:#155724,stroke-width:2px
    style D3 fill:#d4edda,stroke:#155724,stroke-width:2px
    style O1 fill:#d4edda,stroke:#155724,stroke-width:2px
    style O2 fill:#d4edda,stroke:#155724,stroke-width:2px
    style O3 fill:#d4edda,stroke:#155724,stroke-width:2px
    style S1 fill:#d4edda,stroke:#155724,stroke-width:2px
    style S2 fill:#fff3cd,stroke:#856404,stroke-width:2px
    style S3 fill:#fff3cd,stroke:#856404,stroke-width:2px
    style C1 fill:#d4edda,stroke:#155724,stroke-width:2px
    style C2 fill:#d4edda,stroke:#155724,stroke-width:2px
    style C3 fill:#fff3cd,stroke:#856404,stroke-width:2px
    style C4 fill:#fff3cd,stroke:#856404,stroke-width:2px
    style FINTECH fill:#f8f9fa,stroke:#343a40,stroke-width:3px
```

---

## Cenário 2: Banco Tradicional (Regional, `>`200 devs)

### Contexto
- Apps críticas: `>`30 (múltiplas linhas de negócio)
- Deadline DORA: Janeiro 2025
- Budget: Adequado
- Risk appetite: Muito baixo (conformidade histórica)
- Compliance adicional: GDPR, NIS2, regulação local

### KPIs e Targets

| Categoria | Métrica | Target | Período | Justificativa |
|-----------|---------|--------|---------|---------------|
| **Risco Aplicacional** | % apps classificadas | 100% | M1 | Obrigatório DORA |
| | Threat modeling (L3) | 100% | M4 | Mais apps = tempo |
| | Threat modeling (L2) | 80% | M6 | Progressivo |
| | Vulns críticas não remediadas | 0 | Permanente | DORA + GDPR |
| | Vulns altas (SLA remediação) | `<`30 dias | Permanente | Conforme [Cap. 05](/sbd-toe/sbd-manual/dependencias-sbom-sca/intro) |
| | Vulns médias (SLA remediação) | `<`90 dias | Permanente | Conforme [Cap. 05](/sbd-toe/sbd-manual/dependencias-sbom-sca/intro) |
| **Desenvolvimento** | Cobertura de testes | ≥85% | M12 | Mais rigoroso: banco |
| | SAST findings altos | 0 | Permanente | Zero tolerance |
| | SCA findings altos | 0 | Permanente | Zero tolerance |
| | Code review rate | 100% | Permanente | Segregação duties |
| **Operações** | MTTR P0 (Critical) | `<`1h | Permanente | Impacto sistémico |
| | MTTR P1 (High) | `<`4h | Permanente | Impacto operacional |
| | Disponibilidade core apps | ≥99.95% | Permanente | SLA regulatório |
| | Incidents P0 resolvidos `<`24h | 100% | Permanente | Reporte DORA obrigatório |
| **Supply Chain** | Fornecedores no inventário | 100% | M1 | DORA Art. 26 |
| | % auditados (risk assessment) | 100% | M3 | DORA requer |
| | % com contrato atualizado | 100% | M6 | Cláusulas técnicas |
| | % com acesso revogado `<`24h | 100% | Permanente | Offboarding rigoroso |
| **Conformidade** | Política board + GDPR officer | ✓ | M0 | Pré-requisito |
| | Trilho auditoria (logs) | 5 anos | M0 | GDPR + DORA |
| | Staff SbD training | 100% devs | M6 | Maior volume |
| | Staff GRC training | 100% arquitetura | M3 | Entender normativos |
| | TLPT (L3 apps) | 100% | M12 | DORA Art. 19 |
| | Attestation TLPT | ✓ | M13 | Evidência board |
| | Readiness inspeção supervisor | 100% | M18 | Completa preparação |

### Novidade: Timeline Diferente

```mermaid
gantt
    title Timeline de Implementação: Fintech vs Banco
    dateFormat YYYY-MM-DD
    axisFormat %b
    
    section Fintech (12 meses)
    Foundation rápida           :f1, 2025-01-01, 60d
    Automatização              :f2, after f1, 120d
    Operação + TLPT            :f3, after f2, 180d
    Conformidade               :milestone, f4, after f3, 0d
    
    section Banco (18 meses)
    Foundation (mais apps)      :b1, 2025-01-01, 90d
    Automatização (complexa)    :b2, after b1, 180d
    Operação + TLPT             :b3, after b2, 180d
    Auditoria interna          :b4, after b3, 90d
    Conformidade               :milestone, b5, after b4, 0d
```

**Diferenças chave:**
- **Fintech:** 12 meses, foundation rápida (M0-M2), foco em velocidade
- **Banco:** 18 meses, foundation mais longa (M0-M3), mais apps e complexidade


---

## Cenário 3: Segurador Digital (PME, 20-50 devs)

### Contexto
- Apps: Subsistemas críticos (10-15 L3)
- Deadline DORA: Janeiro 2025
- Budget: Moderado
- Risk appetite: Baixo (seguros = dados sensíveis + GDPR)
- Compliance adicional: GDPR, regulação de seguros local

### KPIs e Targets

| Categoria | Métrica | Target | Período | Justificativa |
|-----------|---------|--------|---------|---------------|
| **Risco Aplicacional** | % apps classificadas | 100% | M1 | Obrigatório DORA |
| | Threat modeling (L3) | 100% | M3 | Menos apps = rápido |
| | Vulns críticas não remediadas | 0 | Permanente | GDPR + dados |
| | Vulns altas (SLA) | `<`15 dias | Permanente | Dados sensíveis |
| **Desenvolvimento** | Cobertura de testes | ≥75% | M6 | Pragmático para PME |
| | SAST findings altos | 0 | Permanente | Gate CI/CD |
| | SCA findings altos | 0 | Permanente | Gate CI/CD |
| **Operações** | MTTR P0 | `<`4h | Permanente | Seguros: impacto operacional |
| | MTTR P1 | `<`24h | Permanente | Menos crítico que banco |
| | Disponibilidade | ≥99.5% | Permanente | SLA comercial |
| **Supply Chain** | Fornecedores no inventário | 100% | M2 | DORA requer |
| | % com onboarding | 100% | M3 | Antes acesso |
| | % com training | 100% | M3 | Obrigatório |
| **Conformidade** | Política board | ✓ | M1 | DORA Art. 5 |
| | Trilho auditoria | 3 anos (GDPR) | M0 | |
| | Staff training | 100% | M4 | PME: todos conhecem |
| | TLPT readiness | Piloto L3 critical | M10 | Menos apps = pode fazer |
| | Readiness inspeção | 90% | M12 | Antes deadline DORA |

---

## Cenário 4: Empresa de Outsourcing/Serviços Financeiros

### Contexto
- Apps: Múltiplas soluções SaaS/On-prem
- Clientes: Diferentes perfis de risco
- Deadline DORA: Depende cliente
- Budget: Variável (por cliente)
- Desafio: Diferentes níveis de maturidade por cliente

### Approach: Targets por Tier

| Tier | Cliente | RTO | Vulns Altas SLA | TLPT | Training |
|------|---------|-----|-----------------|------|----------|
| **Essencial** | Banco pequeno | `<`4h | `<`30d | Sim | 100% |
| **Padrão** | PME financeira | `<`8h | `<`45d | Sim | 80% |
| **Básico** | Startup fintech | `<`24h | `<`60d | Piloto | 60% |

### Gestão de Clientes

**👤 Cada cliente tem:**
- Classificação apps (L1-L3)
- Policy própria (assinada)
- SLA customizado
- Timeline DORA específica
- KPIs rastreados em dashboard
- Relatório trimestral

**📊 Consolidação interna:**
- KPI agregado: % clientes compliant
- Risco agregado: Clientes em risco
- Training: Cobertura por região/cliente
- Alertas: Clientes que vão falhar deadline

---

## Componentes de Qualquer Dashboard

Independentemente do cenário, o dashboard deve ter:

### 📊 Dashboard Unificado

```mermaid
%%{init: {'theme':'base', 'themeVariables': { 'fontSize':'14px'}}}%%
graph TB
    subgraph DASH["📊 DASHBOARD - Período: Trimestral | Status: 92% on-track"]
        subgraph RISK["🎯 RISCO"]
            R1["Critical: 0 / target: 0<br/>🟢 OK"]
            R2["High: 3 / target: <5<br/>🟢 OK"]
            R3["Medium: 12 / target: <20<br/>�� WATCH"]
        end
        
        subgraph COMP["📋 CONFORMIDADE"]
            C1["Apps classificadas: 95%<br/>target: 100% | 🟡 DELAYED"]
            C2["Policy signed: YES<br/>🟢 OK"]
            C3["Trilho logs: 3 years<br/>🟢 OK"]
            C4["Staff trained: 80%<br/>target: 100% | 🟡 DELAYED"]
        end
        
        subgraph TREND["📈 TREND últimos 6 meses"]
            T1["Critical vulns: ↓<br/>🟢 melhorando"]
            T2["High vulns: →<br/>➡️ estável"]
            T3["Training: ↑<br/>🟢 melhorando"]
        end
        
        subgraph ALERT["⚠️ ALERTAS CRÍTICOS"]
            A1["🚨 2 fornecedores sem training<br/>Deadline: M3"]
            A2["🚨 1 app L3 sem threat modeling<br/>Status: atrasado"]
        end
    end
    
    style R1 fill:#d4edda,stroke:#155724,stroke-width:2px
    style R2 fill:#d4edda,stroke:#155724,stroke-width:2px
    style R3 fill:#fff3cd,stroke:#856404,stroke-width:2px
    style C1 fill:#fff3cd,stroke:#856404,stroke-width:2px
    style C2 fill:#d4edda,stroke:#155724,stroke-width:2px
    style C3 fill:#d4edda,stroke:#155724,stroke-width:2px
    style C4 fill:#fff3cd,stroke:#856404,stroke-width:2px
    style T1 fill:#d4edda,stroke:#155724,stroke-width:2px
    style T2 fill:#e2e3e5,stroke:#6c757d,stroke-width:2px
    style T3 fill:#d4edda,stroke:#155724,stroke-width:2px
    style A1 fill:#f8d7da,stroke:#721c24,stroke-width:2px
    style A2 fill:#f8d7da,stroke:#721c24,stroke-width:2px
    style DASH fill:#f8f9fa,stroke:#343a40,stroke-width:3px
```

---

## Cadência de Revisão

### Mensal (Quick-check)
- Critical/High vulns
- Incidentes abertos
- Fornecedores sem onboarding

### Trimestral (Formal Review)
- KPIs contra targets
- Trends últimos 3 meses
- Ajustes de targets se needed
- Board reporting

### Anual (Strategic)
- Revisão de targets conforme DORA evolução
- Lições aprendidas vs. targets
- Projeção para próximo ano

---

## Processo de Definição de Targets (Por Fazer)

1. **Baseline:** Auditar estado atual
2. **Benchmarking:** Comparar com indústria (cuidado: contextos variam)
3. **Risk Assessment:** Definir risk appetite
4. **Proposal:** Apresentar ao management
5. **Aprovação:** Board sign-off
6. **Comunicação:** Publicar targets, comunicar timeline
7. **Monitorização:** Rastrear progresso
8. **Revisão:** Trimestral + anual

---

## Importante

**Não existem "targets certos"** - cada organização deve:

- Começar conservador (melhor exceder que falhar)
- Iterar conforme capacidade
- Alinhar com DORA requirements
- Comunicar trade-offs
- Documentar decisões

Targets são **propósito prático**, não teórico - servem para orientar ação, não para parecer bem numa auditoria.

---

**Versão:** 1.0  
**Data:** Novembro 2025  
**Review:** Trimestral conforme DORA evolução
