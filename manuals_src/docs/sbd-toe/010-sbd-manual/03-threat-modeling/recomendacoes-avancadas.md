---
id: recomendacoes-avancadas
title: Práticas Avançadas em Threat Modeling
description: Recomendações reforçadas para organizações com elevada maturidade ou requisitos normativos exigentes
tags: [avançado, threat-modeling, baseline, sincronizacao, governação, métricas]
sidebar_position: 30
---

# 🧩 Práticas Avançadas em Threat Modeling

Este anexo apresenta práticas **facultativas** destinadas a organizações com maior maturidade, obrigações normativas exigentes (ex.: NIS2, DORA, ISO 27034, IEC 62443) ou equipas com processos de engenharia de segurança já consolidados.

> Estas práticas **não substituem** as prescrições basilares do Capítulo 3.  
> São extensões opcionais que **reforçam governança, rastreabilidade e evidência**, contribuindo para níveis superiores de maturidade (ex.: OWASP SAMM / OWASP DSOMM), quando adotadas.

---

## 🧱 1. Baselines e *Tailoring* de Modelos de Ameaça

**Objetivo:** Normalizar o processo de Threat Modeling entre projetos e reutilizar conhecimento previamente validado, reduzindo variabilidade e risco de omissão.

- Definir **baselines organizacionais** por padrões arquiteturais relevantes (ex.: web 3-tier, micro-serviços, event-driven, batch/ETL, integrações B2B).
- Cada projeto deve **adotar uma baseline** como ponto de partida e documentar alterações (*tailoring*) com:
  - diferenças de contexto (dados, trust boundaries, dependências, exposição);
  - ameaças removidas e porquê;
  - ameaças adicionadas e porquê.
- A revisão de *tailoring* deve ser **aprovada** por um role explícito (ex.: AppSec / Security Architect) antes de considerar o modelo como “aprovado”.
- As baselines devem manter **ligações estáveis** a requisitos e controlos relevantes (ex.: `REQ-*`, `THREAT-*`, `ARC-*` quando aplicável).

**Artefactos esperados**
- `baseline/<pattern>.(md|yaml|json)`
- `tailoring-notes.md`
- Registo de aprovação (PR/issue/assinatura conforme processo)

---

## 🔄 2. Sincronização entre Representações do Modelo

**Objetivo:** Evitar divergências entre a representação do Threat Model no repositório versionado e outras representações usadas pela equipa (ex.: exportações, templates internos, formatos estruturados).

- Definir um **formato canónico** do Threat Model para versionamento (ex.: Markdown + YAML estruturado, ou outro formato interno estável).
- Implementar um processo de sincronização que garanta:
  - **identificadores estáveis** para ameaças e decisões (`THREAT-*`, `DEC-*`, etc.);
  - **idempotência** (executar novamente não deve degradar nem duplicar informação);
  - registo de **diferenças** (*diff report*) quando existirem incongruências.
- Gerar relatórios de consistência e cobertura **como outputs** (artefactos), não como decisão:
  - cobertura de decisões (todas as ameaças têm decisão);
  - cobertura de ligações (ameaças ligadas a requisitos/mitigações);
  - percentagem de modelos “frescos” (revistos dentro da janela definida).

**Artefactos esperados**
- `tm-sync.log` (ou equivalente)
- `tm-diff-report.(md|csv|json)`
- `tm-coverage.(md|csv|json)` (métricas objetivas e auditáveis)

---

## ⚖️ 3. *Gates* de Segurança Proporcionais (L1–L3)

**Objetivo:** Garantir que o Threat Modeling influencia efetivamente decisões de release, de forma proporcional ao risco, e com evidência auditável.

Em vez de percentagens rígidas, usar **critérios determinísticos baseados em estado**:

### 3.1 Critérios mínimos (por nível L1–L3)

- **L1 (baixo risco)**
  - Threat Model existente **ou** justificativa de não aplicabilidade aprovada.
  - Nenhuma ameaça “Alta” em estado “Sem decisão”.
  - Exceções permitidas com registo simples e prazo de revisão.

- **L2 (médio risco)**
  - Threat Model **aprovado** (baseline + revisões) para a versão/arquitetura a libertar.
  - Todas as ameaças “Alta”:
    - com decisão explícita (mitigar/aceitar/transferir/rejeitar com justificação),
    - com *owner*,
    - com evidência de mitigação ou aceitação formal.
  - Exceções com *sunset* e mitigação compensatória quando aplicável.

- **L3 (alto risco)**
  - Threat Model aprovado com **segregação de funções** (revisão independente).
  - Nenhuma ameaça “Alta” pode ir para produção sem:
    - mitigação implementada **ou**
    - aceitação formal com compensações, *sunset* curto e aprovação apropriada.
  - Revalidação obrigatória quando existirem alterações estruturais desde a última aprovação.

### 3.2 Evidência do *gate*
O *gate* deve produzir evidência verificável:
- versão do Threat Model referenciada (commit/tag);
- relatório de estado (ameaças altas, decisões, owners, prazos);
- registo de aprovações e exceções.

**Artefactos esperados**
- `gates-l1-l3.md` (regras e limiares definidos)
- `tm-gate-report.(md|csv|json)`
- Aprovação formal registada

**Relação com frameworks**
| Referência | Domínio | Benefício |
|---|---|---|
| SSDF (RV) | Risk Validation | Governação objetiva antes de produção |
| OWASP SAMM (Verification) | Quality & Release Gating | Critérios *go/no-go* baseados em evidência |
| OWASP DSOMM (Measurement/Metrics) | Continuous Improvement | Métricas auditáveis e acionáveis |

---

## 📈 4. Métricas e *Dashboards* de Cobertura

**Objetivo:** Medir eficácia, atualidade e disciplina do processo de Threat Modeling sem incentivar “gaming”.

Métricas recomendadas (objetivas e auditáveis):
- **Freshness**: tempo desde a última revisão/aprovação do Threat Model;
- **Decision Coverage**: % de ameaças com decisão explícita;
- **High-Risk Hygiene**:
  - nº de ameaças “Alta” sem owner,
  - nº de ameaças “Alta” sem evidência associada,
  - nº de exceções “Alta” fora de prazo (*sunset* expirado);
- **Traceability Coverage**: % de ameaças ligadas a requisitos/mitigações e a evidência de testes/validações;
- **Delta Volume**: nº de alterações significativas desde a última revisão (proxy de risco de obsolescência).

Os *dashboards* devem ser:
- derivados de artefactos versionados e outputs de controlo (não de opinião);
- reproduzíveis (mesma fonte, mesmo resultado);
- usados para decisão organizacional (prioridade, dívida de risco, auditoria).

---

## ✅ Considerações finais

Estas práticas elevam maturidade e disciplina operacional quando:
- existe exigência regulatória/certificação;
- há múltiplas equipas/projetos e necessidade de normalização;
- se pretende controlo sistemático de risco com evidência auditável.

> 📌 Este anexo complementa o `15-aplicacao-lifecycle.md` do capítulo, que define as práticas basilares obrigatórias e a integração no SSDLC.
