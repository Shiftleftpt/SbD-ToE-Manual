---
id: aplicacao-lifecycle
title: Como Fazer
description: Integração das práticas de arquitetura segura ao longo do ciclo de desenvolvimento
tags: [tipo:aplicacao, execucao, ciclo de vida, arquitetura, requisitos, segurança]
sidebar_position: 15
---

# 🏛️ Aplicação de Arquitetura Segura no Ciclo de Vida

Este anexo prescreve **como aplicar sistematicamente as práticas de Arquitetura Segura definidas no Capítulo 4** ao longo do ciclo de desenvolvimento, garantindo rastreabilidade, proporcionalidade ao risco e integração com os requisitos de segurança.

Inclui modelos reutilizáveis de user stories, ações por papel, artefactos esperados e quadros de aplicação por nível de criticidade (L1–L3).

---

## 🧭 Quando aplicar Arquitetura Segura

| Fase / Evento                         | Ação esperada                                                    | Quem participa                           | Artefacto principal              |
|---------------------------------------|------------------------------------------------------------------|------------------------------------------|----------------------------------|
| Início de projeto / épico             | Definir princípios de arquitetura segura                         | Arquiteto, DevSecOps, AppSec             | `principios-arquitetura.md`      |
| Design de solução                     | Produzir ficha de arquitetura com controlos de segurança         | Arquiteto + AppSec                       | `solution-architecture.md`       |
| Grooming / Planeamento                | Rever padrões e aplicar requisitos de arquitetura                 | Developer + Arquiteto                    | `design-review.md`               |
| Decisão da arquitetura relevante (ADR)  | Registar decisão, alternativas e impacto (segurança e risco)     | Arquiteto + AppSec                       | `adr/ADR-xxxx.md`                |
| Integrações / fronteiras de confiança | Rever *trust boundaries* e integrações externas/entre serviços   | Arquiteto + AppSec + Equipas integradas  | `trust-boundaries.md`            |
| Alterações críticas                   | Atualizar ficha de arquitetura                                   | Developer + Arquiteto + AppSec           | `arquitetura-atualizada.md`      |
| Exceção da arquitetura                  | Solicitar, avaliar e aprovar exceção com controlos compensatórios| Product Owner + AppSec + Arquiteto       | `excecao-da arquitetura.md`        |
| Trigger “arquitetura viva”            | Reavaliar e sincronizar docs após eventos definidos (ver US-12)  | Arquiteto + DevSecOps + AppSec           | `arquitetura-triggers.md`        |
| Release / Go-live                     | Validar que controlos de arquitetura estão cumpridos              | QA + AppSec + Arquiteto                  | `checklist-arquitetura.md`       |
| CI/CD pipeline                        | Validar controlos de arquitetura automatizáveis                   | Eng. CI/CD + DevSecOps                   | `ci-logs-validacao.txt`          |

---

## 👥 Quem faz o quê

| Papel / Função             | Responsabilidades-chave                                                                 |
|----------------------------|-----------------------------------------------------------------------------------------|
| Arquiteto / DevSecOps      | Definir princípios, criar fichas de solução, gerir ADR e rever designs                  |
| Developer / Equipa de Desenvolvimento | Aplicar padrões e requisitos de arquitetura nas implementações                           |
| QA / Test Engineer         | Validar que requisitos de arquitetura estão refletidos nos testes e no *go-live*         |
| AppSec / Segurança         | Definir controlos de segurança, rever exceções e decisões de arquitetura                 |
| Product Owner / Negócio    | Validar impacto de requisitos/exceções em prazos, custo e *scope*                       |
| Eng. CI/CD                 | Automatizar validações de controlos de arquitetura                                       |

---

## 📝 User Stories Reutilizáveis

### US-01 – Definição de princípios de arquitetura segura
**Contexto.**  
Logo no arranque de um projeto é necessário definir princípios de arquitetura segura.

:::userstory
**História.**   
Como **Arquiteto**, quero definir princípios de arquitetura segura para orientar todas as decisões técnicas.

**Critérios de aceitação (BDD).**
- Dado que o projeto inicia
- Quando os princípios de arquitetura são documentados
- Então ficam aprovados e versionados para referência

**Checklist.**
- [ ] Princípios definidos
- [ ] Aprovação AppSec
- [ ] Evidência arquivada em repositório

:::

**Artefactos & evidências.** `principios-arquitetura.md`

**Proporcionalidade.**
| Nível | Obrigatório? | Ajustes |
|---|---|---|
| L1 | Opcional | Apenas princípios básicos |
| L2 | Sim | Princípios detalhados |
| L3 | Sim | Princípios completos + independentes |

**Integração no SDLC.**
| Fase | Trigger | Responsável | SLA |
|------|---------|-------------|-----|
| Início | Novo projeto | Arquiteto | Antes do design detalhado |

**Ligações úteis.**
- 🔗 [Cap. 2 – Requisitos de Segurança](/sbd-toe/sbd-manual/requisitos-seguranca/intro)

---

### US-02 – Ficha de arquitetura com controlos
**Contexto.**  
Ao desenhar a solução é preciso registar controlos de segurança.

:::userstory
**História.**   
Como **Arquiteto**, quero produzir ficha de arquitetura com controlos de segurança para garantir implementação consistente.

**Critérios de aceitação (BDD).**
- Dado que o design está em curso
- Quando registo controlos de segurança
- Então a ficha fica aprovada

**Checklist.**
- [ ] Ficha criada
- [ ] Controlos registados
- [ ] Aprovação AppSec
- [ ] Evidência arquivada

:::

**Artefactos & evidências.** `solution-architecture.md`

**Proporcionalidade.**
| Nível | Obrigatório? | Ajustes |
|---|---|---|
| L1 | Opcional | Controlos principais |
| L2 | Sim | Controlos detalhados |
| L3 | Sim | Controlos completos + independentes |

**Integração no SDLC.**
| Fase | Trigger | Responsável | SLA |
|------|---------|-------------|-----|
| Design | Criação da solução | Arquiteto | Antes da implementação |

**Ligações úteis.**
- 🔗 Catálogo de requisitos de arquitetura (ARC-XXX) – ver *addon* correspondente

---

### US-03 – Revisão de arquitetura
**Contexto.**  
Antes de implementar, o design deve ser revisto.

:::userstory
**História.**   
Como **AppSec / Segurança**, quero rever designs de arquitetura para garantir conformidade.

**Critérios de aceitação (BDD).**
- Dado que a solução está desenhada
- Quando efetuo revisão
- Então confirmo ou peço ajustes

**Checklist.**
- [ ] Revisão efetuada
- [ ] Feedback registado
- [ ] Aprovação arquivada

:::

**Artefactos & evidências.** `review-arquitetura.md`

**Proporcionalidade.**
| Nível | Obrigatório? | Ajustes |
|---|---|---|
| L1 | Opcional | Revisão simplificada |
| L2 | Sim | Revisão formal |
| L3 | Sim | Revisão independente |

**Integração no SDLC.**
| Fase | Trigger | Responsável | SLA |
|------|---------|-------------|-----|
| Grooming | Design completo | AppSec | Antes da implementação |

**Ligações úteis.**
- 🔗 [Cap. 3 – Threat Modeling](/sbd-toe/sbd-manual/threat-modeling/intro)

---

### US-04 – Atualização de arquitetura em alterações críticas
**Contexto.**  
Sempre que há alteração crítica é preciso atualizar documentação.

:::userstory
**História.**   
Como **Developer**, quero atualizar ficha de arquitetura em alterações críticas para manter consistência.

**Critérios de aceitação (BDD).**
- Dado que há alteração crítica
- Quando atualizo documentação
- Então a ficha de arquitetura é revista

**Checklist.**
- [ ] Alteração identificada
- [ ] Documentação atualizada
- [ ] Revisão arquivada

:::

**Artefactos & evidências.** `arquitetura-atualizada.md`

**Proporcionalidade.**
| Nível | Obrigatório? | Ajustes |
|---|---|---|
| L1 | Opcional | Apenas alterações maiores |
| L2 | Sim | Todas as alterações críticas |
| L3 | Sim | Todas + validação independente |

**Integração no SDLC.**
| Fase | Trigger | Responsável | SLA |
|------|---------|-------------|-----|
| Desenvolvimento | Alteração crítica | Developer | No mesmo sprint |

**Ligações úteis.**
- 🔗 [Cap. 2 – Requisitos de Segurança](/sbd-toe/sbd-manual/requisitos-seguranca/intro)

---

### US-05 – Validação da arquitetura em CI/CD
**Contexto.**  
Controlos de arquitetura devem ser validados automaticamente.

:::userstory
**História.**   
Como **Eng. CI/CD**, quero validar controlos de arquitetura no pipeline para reforçar automação.

**Critérios de aceitação (BDD).**
- Dado que o pipeline corre
- Quando executo verificações de arquitetura
- Então obtenho resultado automático

**Checklist.**
- [ ] Scripts de validação implementados
- [ ] Pipeline atualizado
- [ ] Logs arquivados

:::

**Artefactos & evidências.** `ci-pipeline.yml`

**Proporcionalidade.**
| Nível | Obrigatório? | Ajustes |
|---|---|---|
| L1 | Opcional | Validações básicas |
| L2 | Sim | Validações formais |
| L3 | Sim | Validações completas |

**Integração no SDLC.**
| Fase | Trigger | Responsável | SLA |
|------|---------|-------------|-----|
| CI/CD | Execução pipeline | Eng. CI/CD | Em cada build |

**Ligações úteis.**
- 🔗 [Cap. 5 – Dependências e SCA](/sbd-toe/sbd-manual/dependencias-sbom-sca/intro)

---

### US-06 – Validação de impacto no negócio
**Contexto.**  
É necessário avaliar impacto da arquitetura no negócio.

:::userstory
**História.**   
Como **Product Owner**, quero validar impacto de requisitos de arquitetura para priorizar mitigação.

**Critérios de aceitação (BDD).**
- Dado que existem requisitos de arquitetura
- Quando avalio impacto no negócio
- Então priorizo mitigação

**Checklist.**
- [ ] Impacto avaliado
- [ ] Priorização registada
- [ ] Evidência arquivada

:::

**Artefactos & evidências.** `impacto-arquitetura.md`

**Proporcionalidade.**
| Nível | Obrigatório? | Ajustes |
|---|---|---|
| L1 | Opcional | Apenas impactos críticos |
| L2 | Sim | Avaliação formal |
| L3 | Sim | Avaliação detalhada |

**Integração no SDLC.**
| Fase | Trigger | Responsável | SLA |
|------|---------|-------------|-----|
| Grooming | Requisitos de arquitetura definidos | Product Owner | Antes da priorização |

**Ligações úteis.**
- 🔗 [Cap. 1 – Gestão de Risco](/sbd-toe/sbd-manual/classificacao-aplicacoes/intro)

---

### US-07 – Validação da arquitetura no Go-live
**Contexto.**  
Antes da entrada em produção, a arquitetura deve ser formalmente validada contra requisitos e padrões definidos, assegurando que exceções foram aprovadas e controlos estão implementados.

:::userstory
**História.**   
Como **QA / AppSec / Arquiteto**, quero validar a arquitetura antes do go-live, para garantir que todos os controlos definidos estão aplicados e exceções documentadas.

**Critérios de aceitação (BDD).**
- Dado que a aplicação está pronta para release  
- Quando executo checklist de validação da arquitetura  
- Então confirmo que todos os controlos estão cumpridos ou exceções aprovadas

**Checklist.**
- [ ] Checklist de arquitetura preenchido  
- [ ] Controlos críticos validados  
- [ ] Exceções aprovadas e documentadas  
- [ ] Evidência arquivada

:::

**Artefactos & evidências.** `checklist-arquitetura.md`

**Proporcionalidade.**
| Nível | Obrigatório? | Ajustes |
|---|---|---|
| L1 | Opcional | Checklist simplificado |
| L2 | Sim | Checklist formal  
| L3 | Sim | Checklist completo + revisão independente |

**Integração no SDLC.**
| Fase | Trigger | Responsável | SLA |
|------|---------|-------------|-----|
| Release / Go-live | Preparação de release | QA + AppSec + Arquiteto | Antes da entrada em produção |

**Ligações úteis.**
- 🔗 Critérios de validação da arquitetura – *addon* correspondente

---

### US-08 – Gestão de Decisões Arquiteturais (ADR)
**Contexto.**  
Decisões de arquitetura críticas devem ser documentadas com alternativas, *trade-offs* e impacto em segurança.

:::userstory
**História.**  
Como **Arquiteto**, quero registar decisões de arquitetura (ADR - Architecture Decision Record ) com o racional de segurança para garantir rastreabilidade e consistência.

**Critérios de aceitação (BDD).**
- Dado que ocorre uma decisão da arquitetura relevante
- Quando a ADR é criada segundo *template* aprovado
- Então inclui contexto, opções, decisão, impacto (L1–L3), controlos e revisão AppSec

**Checklist.**
- [ ] ADR criada com *template*
- [ ] Opções e impactos comparados
- [ ] Aprovação AppSec
- [ ] Referência a requisitos ARC-XXX

:::

**Artefactos & evidências.** `adr/ADR-xxxx.md`

**Proporcionalidade.**
| Nível | Obrigatório? | Ajustes |
|---|---|---|
| L1 | Opcional | Apenas ADR de alto impacto |
| L2 | Sim | ADR para decisões significativas |
| L3 | Sim | ADR para todas as decisões relevantes + *review* independente |

---

### US-09 – Revisão de Fronteiras de Confiança e Integrações
**Contexto.**  
Integrações entre serviços e terceiros exigem revisão explícita de fronteiras de confiança.

:::userstory
**História.**  
Como **Arquiteto/AppSec**, quero rever *trust boundaries* e integrações (internas/terceiros) para validar autenticação, autorização, encriptação e isolamento.

**Critérios de aceitação (BDD).**
- Dado que existe integração nova ou alterada
- Quando avalio fronteiras de confiança e controlos
- Então documento decisões, riscos residuais e mitigação

**Checklist.**
- [ ] Inventário de integrações atualizado
- [ ] Matriz de confiança definida
- [ ] Controlos verificados (AuthN/AuthZ/TLS/segregação)

:::

**Artefactos & evidências.** `trust-boundaries.md`, `integration-review.md`

**Proporcionalidade.**
| Nível | Obrigatório? | Ajustes |
|---|---|---|
| L1 | Sim | Escopo reduzido |
| L2 | Sim | Escopo completo |
| L3 | Sim | *Pen test* / validações adicionais conforme risco |

---

### US-10 – Sincronização Threat Modeling ↔ Arquitetura
**Contexto.**  
Decisões de arquitetura devem refletir o modelo de ameaças e vice-versa.

:::userstory
**História.**  
Como **Arquiteto/AppSec**, quero sincronizar o modelo de ameaças com as decisões de arquitetura para garantir que controlos cobrem as ameaças priorizadas.

**Critérios de aceitação (BDD).**
- Dado que há decisão ou alteração da arquitetura
- Quando atualizo o modelo de ameaças e a ficha de solução
- Então mantenho cobertura e rastreabilidade ARC-XXX ↔ ameaça ↔ controlo

**Checklist.**
- [ ] Modelo de ameaças atualizado
- [ ] Ficha de solução alinhada
- [ ] Evidência de cobertura por controlo

:::

**Artefactos & evidências.** `tm-sync-arquitetura.md`

**Proporcionalidade.**
| Nível | Obrigatório? | Ajustes |
|---|---|---|
| L1 | Sim | Sincronização leve |
| L2 | Sim | Sincronização formal |
| L3 | Sim | *Review* independente e métricas de cobertura |

---

### US-11 – Gestão de Exceções Arquiteturais
**Contexto.**  
Algumas situações exigem exceções formais com controlos compensatórios e prazo.

:::userstory
**História.**  
Como **Product Owner/AppSec**, quero gerir exceções de arquitetura com aprovação e controlos compensatórios para equilibrar risco e entrega.

**Critérios de aceitação (BDD).**
- Dado que é solicitada exceção
- Quando avalio impacto, compensações e prazo
- Então aprovo/rejeito e registo evidência e *owner* do risco

**Checklist.**
- [ ] Formulário de exceção preenchido
- [ ] Avaliação de impacto e compensações
- [ ] Decisão e prazo registados
- [ ] Revisão periódica agendada

:::

**Artefactos & evidências.** `excecao-da arquitetura.md`

**Proporcionalidade.**
| Nível | Obrigatório? | Ajustes |
|---|---|---|
| L1 | Sim | Processo simplificado |
| L2 | Sim | Processo formal |
| L3 | Sim | *Governance* com auditoria |

---

### US-12 – trigger para atualização da arquitetura
**Contexto.**  
Definir eventos que obrigam a rever e sincronizar documentação e controlos.

:::userstory
**História.**  
Como **Arquiteto/DevSecOps**, quero manter uma lista de triggers que despoletam a revisão da arquitetura para garantir documentação e controlos atualizados.

**Critérios de aceitação (BDD).**
- Dado que acontece um evento (trigger)  (ex.: nova integração, alteração de dados sensíveis, mudança de infra/pipeline, novo *threat intel*)
- Quando executo a revisão associada
- Então atualizo ADR, fichas, modelo de ameaças e *checklists*

**Checklist.**
- [ ] Lista de triggers publicada (`arquitetura-triggers.md`)
- [ ] Ações por gatilho definidas
- [ ] Evidências de execução arquivadas

:::

**Artefactos & evidências.** `arquitetura-triggers.md`, atualizações nas fichas/ADR

**Proporcionalidade.**
| Nível | Obrigatório? | Ajustes |
|---|---|---|
| L1 | Sim | Subconjunto mínimo de triggers |
| L2 | Sim | Conjunto completo |
| L3 | Sim | Automação de deteção e *alerts* (quando possível) |

---

## 📑 Artefactos Esperados

| Artefacto                       | Origem / US | Evidência associada                      |
|---------------------------------|-------------|------------------------------------------|
| `principios-arquitetura.md`     | US-01       | Commit + aprovação AppSec                |
| `solution-architecture.md`      | US-02       | `controles.md`                           |
| `review-arquitetura.md`         | US-03       | Issue em repositório de arquitetura      |
| `arquitetura-atualizada.md`     | US-04       | Commit + issue associada                 |
| `ci-pipeline.yml`               | US-05       | Logs CI/CD                               |
| `impacto-arquitetura.md`        | US-06       | Backlog atualizado                       |
| `checklist-arquitetura.md`      | US-07       | Assinatura QA/AppSec/Arquiteto           |
| `adr/ADR-xxxx.md`               | US-08       | *Template* ADR + revisão AppSec          |
| `trust-boundaries.md`           | US-09       | Matriz de confiança + integrações        |
| `integration-review.md`         | US-09       | Lista de controlos por integração        |
| `tm-sync-arquitetura.md`        | US-10       | Rastreabilidade ameaça ↔ controlo        |
| `excecao-da arquitetura.md`       | US-11       | Decisão, compensações, prazo, *owner*    |
| `arquitetura-triggers.md`       | US-12       | Lista de triggers + ações e evidências   |

---

## 📊 Matriz de Proporcionalidade L1–L3

| Nível | Aplicação de práticas de Arquitetura Segura |
|-------|---------------------------------------------|
| L1    | Princípios básicos, ADR apenas para decisões de alto impacto, *trust boundaries* essenciais, *checklist* simplificado, triggers mínimos |
| L2    | Princípios completos, fichas de solução detalhadas, revisões formais, ADR para decisões significativas, gestão de exceções formal, sincronização com Threat Modeling |
| L3    | Cobertura integral, revisões independentes, validações CI/CD completas, rastreabilidade ARC-XXX ↔ design ↔ ameaça ↔ controlo, detecção/automação de triggers |

---

## 📌 Recomendações Finais

- Garantir SLAs claros para ADR, revisões e exceções (antes do design detalhado, antes da implementação, até ao fecho do sprint).
- Centralizar artefactos em repositório versionado e com *index* navegável (ADR, fichas, integrações, exceções).
- Integrar verificações automatizadas no pipeline (onde possível) e alertas de “arquitetura viva”.
- As *user stories* acima representam a prescrição **atual**; conteúdos de `recomendacoes-avancadas.md` permanecem como evolução futura.
