---
id: ciclo-vida-risco
title: Ciclo de Vida da Classificação de Risco
sidebar_position: 7
tags: [tipo:ciclo, tema:revisao, classificacao, eventos]
---

<!--template: sbdtoe-core -->

# 🛠️ Ciclo de Vida da Classificação de Risco {classificacao-aplicacoes:addon:ciclo-vida-risco}

A gestão de risco em software não deve ser encarada como um evento pontual, mas sim como um **processo iterativo e evolutivo** ao longo do ciclo de vida da aplicação. A capacidade de identificar, reavaliar e tratar riscos de forma contextual é determinante para garantir a relevância e atualidade dos controlos aplicados.

Este ficheiro descreve as práticas mínimas de integração da gestão de risco no ciclo de vida da aplicação.

---

## 📅 Integração por Fase do Ciclo de Vida {classificacao-aplicacoes:addon:ciclo-vida-risco#integracao_por_fase_do_ciclo_de_vida}

| Fase                     | Ações de Gestão de Risco                                                         |
| ------------------------ | -------------------------------------------------------------------------------- |
| Planeamento / Requisitos | Identificação de riscos iniciais com base em BIA e arquitetura prevista          |
| Design / Arquitetura     | Avaliação preliminar de risco; mapeamento para controlos arquiteturais           |
| Desenvolvimento          | Validação de risco residual em features novas; revisão de requisitos de controlo |
| Testes / Validação       | Confirmação de aplicação dos controlos; reavaliação de risco pré-release         |
| Release / Operacional    | Registo de aceitação formal de risco residual; monitorização de risco dinâmico   |

---

## 📅 Gatilhos para Reavaliação de Risco {classificacao-aplicacoes:addon:ciclo-vida-risco#gatilhos_para_reavaliacao_de_risco}

O risco deve ser reavaliado sempre que ocorra:

* Introdução de novas funcionalidades
* Alterações à arquitetura (ex: exposição API, integração externa)
* Mudanças de contexto legal ou contratual (ex: entrada em vigor de regulamento)
* Detecção de vulnerabilidades críticas
* Auditorias, pen tests ou resultados de SAST/DAST significativos

---

## 👥 Responsabilidades ao Longo do Ciclo {classificacao-aplicacoes:addon:ciclo-vida-risco#responsabilidades_ao_longo_do_ciclo}

| Papel                  | Responsabilidades na gestão de risco                  |
| ---------------------- | ----------------------------------------------------- |
| Product Owner          | Avalia impacto de riscos no negócio e priorização     |
| Arquitetura / Dev Lead | Aplica modelos de risco e propõe controlos            |
| Sec / AppSec           | Valida aplicação dos controlos e risco residual       |
| Equipa de Operações    | Monitoriza riscos em runtime e regressões de controlo |

---

## 🛠️ Mecanismos de Suporte {classificacao-aplicacoes:addon:ciclo-vida-risco#mecanismos_de_suporte}

* Integração da matriz de risco em ferramentas de backlog (Jira, etc.)
* Registo versionado dos riscos em repositórios (ex: YAML ou Markdown em Git)
* Dashboards de risco com base em scoring dinâmico
* Gate de validação de risco nos pipelines de CI/CD

---

## ⚖️ Ligação com os Limiares L1–L3 {classificacao-aplicacoes:addon:ciclo-vida-risco#ligacao_com_os_limiares_l1l3}

O ciclo de vida do risco deve ser adaptado ao **nível da aplicação**:

* Em aplicações **L3**, a reavaliação de risco deve ser obrigatória a cada release.
* Em aplicações **L2**, deve ocorrer em releases com mudanças significativas.
* Em aplicações **L1**, pode ser baseada em eventos de risco ou calendário fixo.

---

## 🚀 Recomendações para Maturidade {classificacao-aplicacoes:addon:ciclo-vida-risco#recomendacoes_para_maturidade}

* Formalizar processo de reavaliação cíclica com checklist ou policy
* Monitorizar risco residual ao longo do tempo
* Integrar decisões de risco com registo de auditoria (auditable trail)
* Envolver decisores não técnicos sempre que o risco afete requisitos legais ou reputacionais

> O risco não é um valor estático: é um processo vivo que deve acompanhar a realidade da aplicação e do contexto.
