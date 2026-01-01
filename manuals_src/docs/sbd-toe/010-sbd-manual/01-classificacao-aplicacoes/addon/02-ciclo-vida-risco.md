---
id: ciclo-vida-risco
title: Ciclo de Vida da Classificação de Risco
sidebar_position: 2
tags: [tipo:ciclo, tema:revisao, classificacao, eventos]
---

<!--template: sbdtoe-core -->

# 🛠️ Ciclo de Vida da Classificação de Risco

A gestão de risco em software não deve ser encarada como um evento pontual, mas sim como um **processo iterativo e evolutivo** ao longo do ciclo de vida da aplicação.

No SbD-ToE, o risco é tratado como um **conceito único**, cuja relevância e severidade podem variar ao longo do tempo em função de alterações técnicas, organizacionais ou processuais.  
A capacidade de **identificar, reavaliar e tratar riscos de forma contextual** é determinante para garantir que os controlos aplicados permanecem proporcionais, eficazes e justificados.

Este ficheiro descreve as **práticas mínimas** para integrar a classificação e reavaliação de risco no ciclo de vida da aplicação.

---

## 📅 Integração por Fase do Ciclo de Vida

| Fase                     | Ações de Gestão de Risco                                                                 |
| ------------------------ | ---------------------------------------------------------------------------------------- |
| Planeamento / Requisitos | Identificação inicial de riscos com base em impacto, dados, exposição, arquitetura prevista e pressupostos de processo |
| Design / Arquitetura     | Avaliação preliminar dos riscos e respetivos **atributos**; mapeamento para controlos de arquitetura |
| Desenvolvimento          | Reavaliação de riscos existentes face a novas funcionalidades; validação de pressupostos e requisitos de controlo |
| Testes / Validação       | Confirmação da aplicação dos controlos definidos; verificação de evidência e revisão de risco pré-release |
| Release / Operacional    | Registo formal de aceitação de risco residual; monitorização contínua e deteção de regressões |

> 📌 Em todas as fases, alterações nos **atributos do risco** (ex.: detetabilidade, evidenciabilidade ou reprodutibilidade) devem desencadear reavaliação explícita.

---

## 📅 Triggers para Reavaliação de Risco

O risco deve ser reavaliado sempre que ocorra qualquer evento que altere o seu **perfil ou atributos**, nomeadamente:

- Introdução de novas funcionalidades ou fluxos relevantes;
- Alterações à arquitetura (ex.: nova exposição API, integrações externas, mudança de trust boundaries);
- Mudanças de contexto legal, regulatório ou contratual;
- Introdução ou modificação de mecanismos de automação ou apoio à decisão (incluindo IA), **quando estes alterem pressupostos de validação, evidência ou reprodutibilidade**;
- Deteção de vulnerabilidades críticas ou recorrentes;
- Resultados relevantes de auditorias, testes de segurança ou avaliações independentes.

---

## 👥 Responsabilidades ao Longo do Ciclo

| Papel                  | Responsabilidades na gestão de risco                                                |
| ---------------------- | ----------------------------------------------------------------------------------- |
| Product Owner          | Avaliar impacto do risco no negócio e na priorização                                 |
| Arquitetura / Dev Lead | Aplicar o modelo de risco, identificar alterações de atributos e propor controlos   |
| Sec / AppSec           | Validar classificação, controlos aplicados e risco residual                          |
| Equipa de Operações    | Monitorizar risco em runtime e detetar regressões de controlo ou contexto            |

> ✅ As decisões e revisões de risco devem ser sempre **registadas, atribuídas a responsáveis e rastreáveis**.

---

## 🛠️ Mecanismos de Suporte

A operacionalização do ciclo de vida do risco pode ser suportada por:

- Integração da classificação e estado do risco em ferramentas de backlog (ex.: Jira);
- Registo versionado de riscos, pressupostos e decisões (ex.: YAML ou Markdown em Git);
- Dashboards de risco baseados em métricas objetivas e scoring transparente;
- Gates explícitos de validação de risco em pipelines de CI/CD, proporcionais ao nível L1–L3.

---

## ⚖️ Ligação com os Limiares L1–L3

O ciclo de vida da classificação de risco deve ser aplicado de forma proporcional ao **nível de criticidade da aplicação**:

- Em aplicações **L3**, a reavaliação de risco deve ser obrigatória a cada release ou alteração relevante;
- Em aplicações **L2**, deve ocorrer sempre que existam mudanças significativas de arquitetura, dados ou processo;
- Em aplicações **L1**, pode ser baseada em eventos de risco identificados ou num calendário fixo.

Esta proporcionalidade permite equilíbrio entre rigor, custo operacional e eficácia.

---

## 🚀 Recomendações para Maturidade

- Formalizar a reavaliação cíclica de risco através de checklist, workflow ou policy;
- Monitorizar explicitamente o risco residual ao longo do tempo;
- Integrar decisões de risco com registo de auditoria (*audit trail*);
- Envolver decisores não técnicos sempre que o risco tenha impacto legal, reputacional ou estratégico.

> O risco não é um valor estático: é um **processo vivo**, que deve acompanhar a evolução da aplicação, do contexto e das práticas de desenvolvimento.
