---
id: recomendacoes-avancadas
title: Recomendações Avançadas - Arquitetura Segura
description: Práticas avançadas para contextos de elevada maturidade em arquitetura segura
tags: [avancado, arquitetura, maturidade, zero-trust, sbomm]
sidebar_position: 30
---

# 🧠 Recomendações Avançadas - Arquitetura Segura

Este documento complementa as práticas fundamentais do capítulo com recomendações orientadas a contextos de **elevada maturidade organizacional**, sistemas críticos ou ambientes regulamentados.

> As recomendações aqui descritas são opcionais, mas altamente desejáveis para equipas que já aplicam os requisitos ARC de forma consistente.

---

## 🧱 Recomendações Arquitetónicas Avançadas

| Prática / Recomendação                             | Benefício direto                             | Requisitos reforçados |
|------------------------------------------------------|------------------------------------------------|------------------------|
| Adotar o princípio de Zero Trust entre microserviços  | Reduz risco de lateral movement                | ARC-002, ARC-006       |
| Aplicar OPA ou rego para enforcement dinâmico        | Governa políticas de acesso arquitetural       | ARC-001, ARC-008       |
| Usar sidecars para segurança e comunicação interservice | Cria controlo de rede e logging distribuído   | ARC-002, ARC-003       |
| Aplicar segmentação em ambiente de CI/CD             | Garante que a execução reflete o desenho arquitetónico | ARC-004, ARC-007 |
| Integrar threat modeling em stories e epics          | Deteta falhas antes do desenho detalhado       | ARC-005, ARC-010       |
| Formalizar ADRs para todas as decisões arquiteturais  | Melhora auditabilidade e revisão futura        | ARC-004, ARC-011       |
| Validar consistência entre arquitetura e SBOMs       | Garante que o SBOM reflete a arquitetura planeada | ARC-006, ARC-007       |

---

## 🧩 Modelos e Frameworks Recomendados

- **Modelo de Confiança por Contexto** (Context-Aware Trust Models)
- **Architecture Decision Records (ADRs)** com integração Git
- **Modelos de Zoneamento Baseado em Risco**
- **Threat Modeling como parte da Definition of Done**
- **Frameworks**: SABSA, ISO/IEC 42010, NIST SP 800-160 Vol 1
- **SBOMM** (Security BOM Maturity Model) - integração entre arquitetura e composição de software

---

## ✅ Quando aplicar estas recomendações?

- Ambientes regulamentados (financeiro, saúde, defesa)
- Arquiteturas distribuídas de alta complexidade (ex: multicloud, event-driven)
- Plataformas com alto volume de integração externa
- Organizações com função de arquitetura ou segurança dedicada

> 🧭 Estas recomendações alinham com os níveis mais elevados de maturidade em SAMM, BSIMM, SSDF e DSOMM.

---

## 📌 Consideração Final

Estas práticas não substituem os requisitos normativos (ARC), mas representam **próximos passos naturais para equipas que já aplicam arquitetura segura de forma estruturada e consistente**.

> Aplicar estas recomendações de forma seletiva pode acelerar a maturidade e prepara a organização para modelos de governaça baseados em evidência e controlo distribuído.
