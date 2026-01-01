---
id: validacao-assistida-ferramentas
title: Validação Assistida por Ferramentas — Risco de Processo
sidebar_position: 11
tags: [tipo:risco-processo, tema:automacao, validacao, decisao, rastreabilidade]
---

<!--template: sbdtoe-core -->

# 🛠️ Validação Assistida por Ferramentas — Risco de Processo

## 🎯 Objetivo

Este documento prescreve como gerir **riscos de processo** quando ferramentas automatizadas (algoritmos de scoring, sistemas de análise, ou outras formas de assistência) participam na **classificação de aplicações, deteção de alterações, ou mapeamento de ameaças**.

O objetivo **não é proibir ferramentas**, mas sim:

- garantir que **sugestões de ferramentas nunca substituem decisões humanas**;
- identificar **erros plausíveis** que máquinas podem introduzir;
- exigir **validação obrigatória** e **rastreabilidade explícita**;
- estabelecer **trilhos de escalação** em caso de discordância;
- manter **evidência auditável** de todas as decisões.

---

## 📋 Invariantes Fundamentais (do agent.md)

Independentemente do tipo de ferramenta ou fase do ciclo de vida, **todo o uso de automação na classificação deve respeitar**:

### I1 — Separação entre Sugestão e Decisão

- Ferramentas **sugerem, analisam, ou correlacionam**.
- A **decisão final é sempre humana**, atribuída a um role explícito (Developer, AppSec Engineer, GRC/Compliance).
- A sugestão pode ser ignorada, modificada, ou aceite — mas a responsabilidade é sempre do decisor humano.

### I2 — Evidência Acima de Plausibilidade

- Um resultado **plausível** (ex: "L2 porque E=2, D=2, I=1") não substitui **evidência verificável**.
- Exemplos de evidência:
  - Arquitetura técnica documentada e revisada.
  - Dados especificados e classificados manualmente.
  - Ameaças validadas por especialistas de domínio.
  - Exceções aprovadas formalmente.

### I3 — Reprodutibilidade e Auditabilidade

- Toda a sugestão deve ser **reproduzível** e **rastreável**:
  - Que ferramenta foi usada? (nome, versão, data)
  - Que inputs recebeu? (aplicação, eixos, dados brutos)
  - Que output gerou? (score, pontuação E/D/I, nível proposto)
  - Que critério de decisão foi aplicado? (threshold, regras, ponderação)

### I4 — Proteção de Ativos Críticos

- Qualquer ferramenta externa (SaaS, cloud, ou terceiros) é um **risco de supply chain**:
  - Dados sensíveis da aplicação (dados tratados, arquitetura, clientes) não devem ser enviados para sistemas desconhecidos.
  - Aprovação explícita requerida antes de usar qualquer ferramenta em L2/L3.

### I5 — Rastreabilidade de Decisão e Execução

- Toda a decisão de classificação deve responder:
  - **Quem decidiu?** (Developer, AppSec Engineer, Product Owner, etc.)
  - **Com base em quê?** (E/D/I manual, sugestão de ferramenta, feedback de Arquitetos, etc.)
  - **Que validações foram realizadas?** (checklist, revisão, testes)
  - **Que evidência suporta a decisão?** (documentação, relatórios, scans, aprovações)

---

## 🚨 Erros Plausíveis — Por Tipo de Assistência

### A. Scoring Automático de E/D/I

**Como funciona**: Ferramenta analisa descrição de projeto, endpoints, tipos de dados, e propõe scores para E, D, I.

**Erros plausíveis típicos**:

| Erro | Exemplos | Impacto | Mitigação |
|---|---|---|---|
| **Sobreponderação de um eixo** | "Tem muitos endpoints públicos → E=3 sempre", negligenciando que dados são públicos | Classificação enviesada, Controlos desproporcionais | Explicação narrativa obrigatória: "Por quê E=3?" |
| **Omissão de contexto** | Não detecta que uma dependência crítica é opcional ou que isolamento é possível | Subestimação de risco | Revisão manual de dependências + feedback de Arquitetos |
| **Regras inflexíveis** | "Aplicação com mais de 10 APIs → sempre L3", sem considerar que podem ser internas | Sobre-classificação | Critério "se ferramenta propõe L3, AppSec Engineer valida presença de exposição pública real" |
| **Falta de nuance temporal** | Classifica com base em estado actual, ignora crescimento previsto de dados | Risco de reclassificação precipitada | Incluir "previsão de 12 meses" na avaliação; revisar periodicamente |
| **Desalinhamento com modelo organizacional** | Ferramenta usa threshold genérico (ex: "dados PII=D2"), org usa "dados de cliente=D3" | Inconsistência com política | Policy explícita: "Todos os resultados de ferramenta são re-calibrados contra política organisacional" |

---

### B. Deteção Automática de Alterações (Event-Based Triggers)

**Como funciona**: Ferramenta analisa commits, PRs, configurações, e propõe reclassificação (ex: "Nova dependência crítica detectada").

**Erros plausíveis típicos**:

| Erro | Exemplos | Impacto | Mitigação |
|---|---|---|---|
| **Falso positivo** | Detecta `npm update lodash` como "alteração crítica" | Alarme excessivo, desconfiança em sistema | Whitelist + contexto: "Atualizações de patch são ignoradas; apenas minor/major geram alerta" |
| **Omissão de contexto** | Vê "integração com API externa" mas não sabe se é crítica ou opcional | Subdeteção | AppSec Engineer faz validação: "Este novo integração é crítica para o negócio?" |
| **Lag temporal** | Ferramenta detecta mudança 2 semanas depois | Atraso em revisão | Análise semanal ou por sprint, não ad-hoc |
| **Falta de priorização** | Trata "novo endpoint de telemetria" com mesma urgência que "novo acesso a dados de cliente" | Confusão de prioridades | Categorização: crítica (reclassifica já), importante (agenda revisão), informativa (log apenas) |

---

### C. Mapeamento Automático de Ameaças

**Como funciona**: Ferramenta gera STRIDE ou MITRE ATT&CK mapping baseado em tipo de aplicação.

**Erros plausíveis típicos**:

| Erro | Exemplos | Impacto | Mitigação |
|---|---|---|---|
| **Ameaças genéricas não-contextuais** | Mapeia "Denial of Service" para todas as apps, sem considerar SLA crítico | Ruído, wasted effort | Filtro: "Incluir apenas ameaças com probabilidade alta ou impacto crítico para este domínio" |
| **Omissão de ameaças contextuais** | Gera STRIDE genérico, ignora "roubo de IP por insider" (ameaça específica de R&D) | Risco residual não-identificado | Validação por Arquitetos + especialistas de domínio: "Faltam ameaças específicas?" |
| **Falta de priorização** | Lista 50 ameaças, sem indicar críticas vs. menores | Paralisia de análise | Classificação: crítica (cobertura obrigatória), major (cobertura recomendada), minor (opcional) |
| **Desalinhamento com nível de risco** | Mesmo mapeamento para L1 e L3 | Proporção perdida | Requerimento: "Ameaças críticas +60% para L3, +30% para L2, -50% para L1" |

---

## ✅ Checklist de Validação — Por Prática

### Checklist 1: US-01 (Classificação Inicial — Assistida)

**Quando**: Ferramenta propõe E/D/I ou nível L1/L2/L3.

**Checklist (DoD adicional)**:

- [ ] **Fonte de dados clara**: Ferramenta recebeu quais inputs? (descrição projeto, endpoints, tipos de dados)
- [ ] **Explicação narrativa**: Ferramenta justificou por quê E=X, D=Y, I=Z? (output com raciocínio anexado)
- [ ] **Validação de eixo**: Developer/Team Lead validou manualmente cada eixo contra realidade técnica
- [ ] **Revisão de contexto**: Arquitetos confirmam que E/D/I refletem exposição, dados, e impacto reais
- [ ] **Decisão assinada**: AppSec Engineer assinou a decisão final com registo explícito:
  ```
  Classificação: L2
  Origem: Sugestão de ferramenta (v1.2, data: 2025-01-15)
  Ajustes humanos: E mantido em 2 (confirmado por Arquitetos), 
                   D aumentado para 3 (dados de cliente identificados), 
                   I mantido em 1
  Aprovação: AppSec Engineer [nome], data
  ```
- [ ] **Benchmark vs. histórico**: Comparado com aplicações similares já classificadas?
- [ ] **TTL de re-validação**: Próxima revisão agendada (time-based per nivel + event-based triggers)

---

### Checklist 2: US-03 & US-07 (Revisão — Assistida por Deteção de Alteração)

**Quando**: Ferramenta detecta mudança e propõe reclassificação.

**Checklist (DoD adicional)**:

- [ ] **Trigger documentado**: O quê foi detectado? (nova dependência, novo endpoint, novo dado, etc.)
- [ ] **Ferramenta & método**: Quem detectou? (análise manual de commit, ferramenta X versão Y, etc.)
- [ ] **Contexto técnico**: AppSec Engineer/Arquitetos confirmam que alteração é relevante e não falso positivo
- [ ] **Impacto em E/D/I**: Qual eixo é afetado? (exemplo: "E aumenta por novo endpoint", "D aumenta por novo tipo de dado")
- [ ] **Reclassificação proposta**: E/D/I antigo → novo (com explicação de cada mudança)
- [ ] **Trilho de validação**: Se discordância (máquina propõe L2, AppSec quer L3):
  - Documentar: "Ferramenta propôs L2 por [razão X], AppSec override para L3 por [razão Y]"
  - Escalação: Product Owner informado se impacto de negócio
  - Decisão final registada com assinatura
- [ ] **GRC/Compliance audit trail**: Registo em ferramenta de conformidade com timestamp

---

### Checklist 3: US-06 (Mapeamento de Ameaças — Assistido)

**Quando**: Ferramenta gera STRIDE/MITRE ATT&CK mapping.

**Checklist (DoD adicional)**:

- [ ] **Ferramenta & versão**: Qual algoritmo? (ex: "Automated STRIDE Generator v2.1")
- [ ] **Escopo correto**: Mapping inclui ameaças apropriadas para nível L1/L2/L3?
- [ ] **Filtro de ruído**: Omitidas ameaças genéricas não-contextuais? (ex: filtrar "slow DDoS" se criticidade baixa)
- [ ] **Validação por especialistas**: Arquitetos/AppSec Engineer validou:
  - Ameaças criticas não foram omitidas?
  - Ameaças específicas de domínio foram incluídas?
  - Priorização (crítica vs. minor) está correcta?
- [ ] **Rastreamento**: Cada ameaça tem:
  - [ ] Descrição clara
  - [ ] Controlo aplicado (ou exceção com justificação)
  - [ ] Status: coberta / parcialmente coberta / não coberta (risco residual)
- [ ] **Escalação se risco crítico não coberto**: Dispara US-04 (risco residual) ou mitigação obrigatória

---

## 🔀 Trilho de Escalação — Discordância Humano ↔ Máquina

### Cenário 1: Developer propõe L1, Ferramenta propõe L2

```
┌─────────────────────────────────────────────────────┐
│ DISCORDÂNCIA DETECTADA                              │
│ Developer: "Apenas APIs internas, dados públicos"   │
│ Ferramenta: "E=2 (múltiplos endpoints) → L2"        │
└──────────────────┬──────────────────────────────────┘
                   ▼
         ┌─────────────────────┐
         │ AppSec Engineer     │
         │ Valida contexto:    │
         │ - Endpoints realmente│
         │   apenas internos?   │
         │ - Dados realmente    │
         │   públicos?          │
         └────────┬────────────┘
                  ▼
        ┌──────────────────────────────┐
        │ Decisão Final:               │
        │ L1 (concordou com Developer) │
        │ Motivo: "Ferramenta         │
        │  incorreu em falso positivo" │
        │ Registro: [assinado]         │
        └──────────────────────────────┘
```

### Cenário 2: AppSec propõe L3, Ferramenta propõe L1 (Subdeteção)

```
┌──────────────────────────────────────────────────────┐
│ DISCORDÂNCIA CRÍTICA DETECTADA                       │
│ AppSec: "Dados de cliente + APIs públicas → L3"      │
│ Ferramenta: "Apenas E=1, D=1 → L1"                   │
└───────────────────┬────────────────────────────────────┘
                    ▼
        ┌─────────────────────────────────────┐
        │ Investigação: Por quê ferramenta    │
        │ sub-classificou?                    │
        │ - Não detectou dados de cliente?    │
        │ - Não mapeou APIs públicas?         │
        │ Ação: Feedback para ferramenta      │
        │ (treino, ajuste de regras, etc.)    │
        └──────────┬──────────────────────────┘
                   ▼
        ┌──────────────────────────────┐
        │ Decisão Final:               │
        │ L3 (concordou com AppSec)    │
        │ Motivo: "Ferramenta errou;   │
        │  dados de cliente omissos"   │
        │ Escalação: Product Owner     │
        │  (impacto de negócio L3)     │
        │ Registro: [assinado]         │
        └──────────────────────────────┘
```

### Cenário 3: Discordância não resolvida no SLA

```
┌────────────────────────────────────────────┐
│ Sem consenso em 5 dias úteis (SLA)         │
├────────────────────────────────────────────┤
│ Developer: L1                              │
│ Ferramenta: L2                             │
│ AppSec Engineer: Indeciso                  │
└─────────────────┬──────────────────────────┘
                  ▼
        ┌────────────────────────────┐
        │ Escalonamento automático:  │
        │ Product Owner arbitral     │
        │ (aspectos de negócio)      │
        │ + CISO (aspectos técnicos) │
        └──────────┬─────────────────┘
                   ▼
        ┌────────────────────────┐
        │ Decisão Final Oficial  │
        │ Registro formal com    │
        │ assinatura(s)          │
        │ Motivo documentado     │
        └────────────────────────┘
```

---

## 📝 Exemplos — Boas e Más Práticas

### ❌ Má Prática 1: Aceitar Sugestão sem Validação

```
Ferramenta: "L2" (score: E=2, D=2, I=1)
Developer: "OK, vou com L2"
AppSec Engineer: (não revê)
Artefacto registado: classificacao-app.yaml com L2, sem explicação

PROBLEMA:
- Ninguém sabe por quê L2
- Impossível auditar decisão
- Ferramenta pode ter errado (ex: omitiu dados sensíveis)
- Reclassificação futura sem baseline
```

### ✅ Boa Prática 1: Validação com Rastreabilidade

```
Ferramenta: "L2" (E=2, D=2, I=1)
Output: {
  "eixos": {
    "exposicao": 2,
    "dados": 2,
    "impacto": 1
  },
  "raciocinio": "E=2: APIs internas (5 endpoints), 
                 D=2: Dados de utilizador, 
                 I=1: Downtime ~30min aceitável"
}

Developer + Arquitetos: Revisam E/D/I narrativa
- E=2: Confirmado? SIM (APIs internas, não públicas)
- D=2: Confirmado? SIM (dados de utilizador, não PII)
- I=1: Confirmado? NÃO — se cair, impacto é crítico → I=2

AppSec Engineer: Reclassifica E/D/I → L2 mantém-se (após ajuste I)

Artefacto registado:
  classificacao-app.yaml:
    nível: L2
    eixos_originais: {E: 2, D: 2, I: 1}
    eixos_finais: {E: 2, D: 2, I: 2}
    assistida_por_ferramenta: true
    ferramenta: "Automated Classifier v1.2"
    data_ferramenta: "2025-01-15"
    validadores: ["Developer-X", "Arquiteto-Y"]
    aprovador: "AppSec-Z"
    data_aprovacao: "2025-01-16"
    observações: "I ajustado de 1→2 por Arquitetos (impacto crítico)"

VANTAGENS:
✓ Totalmente rastreável
✓ Auditável ("quem decidiu o quê, quando, por quê")
✓ Benchmarkável contra outras apps
✓ Reclassificações futuras têm baseline claro
```

---

### ❌ Má Prática 2: Ferramenta Detecta Alteração, Ninguém Valida

```
Commit: "Add dependency on critical-auth v2.0"
Ferramenta: [Alerta automático] "Nova dependência crítica detectada!"
GRC/Compliance: Vê alerta, não faz nada (assume que já foi validado)
Developer: Não vê alerta (não subscrito)
AppSec Engineer: Não viu (não reviewou)

Resultado: Ninguém reviu, classificação não foi atualizada
RISCO: Controlo de segurança insuficiente, gap de conformidade
```

### ✅ Boa Prática 2: Deteção com Validação Explícita

```
Commit: "Add dependency on critical-auth v2.0"
Ferramenta: [Alerta] "Nova dependência crítica detectada!"
Email automático: AppSec Engineer + GRC/Compliance
Issue automática: "Reclassifique se necessário"

AppSec Engineer (3 dias úteis):
- Valida: "critical-auth é realmente crítica?"
- Resultado: SIM, acesso centralizado a dados de cliente
- Decisão: E (exposição) não muda; D (dados) permanece 2
- Nível: L2 → L2 (sem mudança, mas com ameaças críticas agora)
- Ação: Dispara US-06 (mapeamento de ameaças para nova dependência)

Artefacto registado:
  classificacao-revisao.md:
    data: 2025-01-20
    trigger: "Nova dependência crítica (critical-auth v2.0)"
    ferramenta_detetor: "Dependency Scanner v1.5"
    nível_anterior: L2
    nível_novo: L2
    decisão: "Mantém-se L2; novo mapeamento de ameaças requerido"
    validador: "AppSec-Z"
    próxima_revisão: "2025-02-20" (30 dias)

GRC/Compliance: Registra em audit trail
```

---

## 🔗 Integração com User Stories

### Para US-01 (Classificação Inicial)

Adicionar ao DoD:

```markdown
- [ ] **Se assistida por ferramenta:**
  - [ ] Output de ferramenta (scores, raciocínio) anexado
  - [ ] Justificação narrativa humana clara (por quê E=X, D=Y, I=Z)
  - [ ] Validação de cada eixo por especialistas (Developer, Arquitetos)
  - [ ] Aprovação final por AppSec Engineer com registo explícito
  - [ ] Ferramenta, versão, data documentados
```

### Para US-03 (Revisão Event-Based)

Adicionar ao DoD:

```markdown
- [ ] **Se assistida por ferramenta detetor:**
  - [ ] Ferramenta & método de deteção documentados
  - [ ] Trigger técnico validado (falso positivo excluído)
  - [ ] Contexto de negócio confirmado (alteração realmente relevante)
  - [ ] Impacto em E/D/I explicado
  - [ ] Se nível alterou: trilho de escalação documentado
```

### Para US-07 (Revisão Time-Based)

Adicionar ao DoD:

```markdown
- [ ] **Se assistida por ferrameta de análise:**
  - [ ] Ferramenta forneceu re-scoring de E/D/I?
  - [ ] Comparação: score anterior vs. score novo documentada
  - [ ] Se discordância (máquina vs. AppSec): trilho de resolução registado
```

### Para US-06 (Mapeamento de Ameaças)

Adicionar ao DoD:

```markdown
- [ ] **Se assistido por ferramenta de mapeamento:**
  - [ ] Ferramenta & versão documentados
  - [ ] Ameaças genéricas não-contextuais filtradas?
  - [ ] Ameaças específicas de domínio adicionadas (validação especialistas)?
  - [ ] Priorização (crítica vs. minor) correcta?
  - [ ] Ameaças críticas não cobertas dispararam US-04 (risco residual)?
```

---

## 📊 Matriz de Proporcionalidade — Esforço de Validação

| Prática | L1 | L2 | L3 |
|---|---|---|---|
| **Validação obrigatória de sugestão** | Recomendada | Obrigatória | Obrigatória + Gestão Executiva |
| **Benchmark vs. histórico** | Opcional | Recomendado | Obrigatório |
| **Trilho de escalação formalizado** | Ad-hoc | Documentado | Documentado + SLA |
| **TTL de re-validação assistida** | 12m | 6m | 3m |
| **Auditoria de decisões assistidas** | Anual | Semestral | Trimestral |

---

## 🎯 Resumo & Recomendações Operacionais

1. **Ferramentas são auxiliares, não autoridades**: Sugestões são valiosas, decisões são humanas.
2. **Rastreabilidade é não-negociável**: Todo o uso de automação deve deixar pista auditável.
3. **Validação proporcional ao risco**: L1 pode ser mais leve, L3 requer rigor máximo.
4. **Erros de ferramenta são esperados**: Ter checklist de erros plausíveis + mitigações.
5. **Escalação clara**: Quando máquina e humano discordam, processo formalizado leva a consenso.
6. **Feedback contínuo**: Se ferramenta errou sistematicamente, ajustar (treino, regras, etc.).
7. **Conformidade regulatória**: Auditorias devem conseguir rastrear "quem decidiu com base em quê".

---

## 🔗 Referências Internas

- [agent.md — Invariantes Canonicos](../../../000-teory-of-everything/agent#4-invariantes-canónicos-aplicáveis-a-todos-os-capítulos)
- [US-01 — Classificação Inicial](../../aplicacao-lifecycle#us-01---classificação-inicial-da-aplicação)
- [US-03 — Revisão Event-Based](../../aplicacao-lifecycle#us-03---revisão-por-alteração-relevante-event-based)
- [US-06 — Mapeamento de Ameaças](../../aplicacao-lifecycle#us-06---mapeamento-de-ameaças-por-nível-de-risco)
- [US-07 — Revisão Time-Based](../../aplicacao-lifecycle#us-07---revisão-periódica-time-based-da-classificação-cadência-obrigatória)
