---
description: Integração das práticas de arquitetura segura ao longo do ciclo de desenvolvimento
genia: us-format-normalization
id: aplicacao-lifecycle
tags:
- arquitetura
- ciclo-vida
- requisitos
- seguranca
- segurança
- tipo-aplicacao
- tipo:aplicacao
title: Como Fazer
---


# 🏛️ Aplicação de Arquitetura Segura no Ciclo de Vida

Este anexo prescreve **como aplicar sistematicamente as práticas de Arquitetura Segura definidas no Capítulo 4** ao longo do ciclo de desenvolvimento, garantindo rastreabilidade, proporcionalidade ao risco e integração com os requisitos de segurança.

Inclui modelos reutilizáveis de user stories, ações por papel, artefactos esperados e quadros de aplicação por nível de criticidade (L1–L3).

---

## 🧭 Quando aplicar Arquitetura Segura

| Fase / Evento                         | Ação esperada                                                    | Quem participa                           | Artefacto principal              |
|---------------------------------------|------------------------------------------------------------------|------------------------------------------|----------------------------------|
| Início de projeto / épico             | Definir princípios de arquitetura segura                         | Arquitetos de Software, DevOps/SRE, AppSec Engineer   | `principios-arquitetura.md`      |
| Design de solução                     | Produzir ficha de arquitetura com controlos de segurança         | Arquitetos de Software + AppSec Engineer              | `solution-architecture.md`       |
| Grooming / Planeamento                | Rever padrões e aplicar requisitos de arquitetura                 | Developer + Arquitetos de Software                    | `design-review.md`               |
| Decisão da arquitetura relevante (ADR)  | Registar decisão, alternativas e impacto (segurança e risco)     | Arquitetos de Software + AppSec Engineer              | `adr/ADR-xxxx.md`                |
| Integrações / fronteiras de confiança | Rever *trust boundaries* e integrações externas/entre serviços   | Arquitetos de Software + AppSec Engineer + Developer  | `trust-boundaries.md`            |
| Alterações críticas                   | Atualizar ficha de arquitetura                                   | Developer + Arquitetos de Software + AppSec Engineer  | `arquitetura-atualizada.md`      |
| Exceção da arquitetura                  | Solicitar, avaliar e aprovar exceção com controlos compensatórios| Product Owner + AppSec Engineer + Arquitetos de Software | `excecao-da arquitetura.md`    |
| Trigger "arquitetura viva"            | Reavaliar e sincronizar docs após eventos definidos (ver US-12)  | Arquitetos de Software + DevOps/SRE + AppSec Engineer | `arquitetura-triggers.md`        |
| Release / Go-live                     | Validar que controlos de arquitetura estão cumpridos              | QA / Test Engineer + AppSec Engineer + Arquitetos de Software | `checklist-arquitetura.md`    |
| CI/CD pipeline                        | Validar controlos de arquitetura automatizáveis                   | DevOps/SRE + AppSec Engineer                          | `ci-logs-validacao.txt`          |

---

## 👥 Quem faz o quê

| Papel / Função             | Responsabilidades-chave                                                                 |
|----------------------------|-----------------------------------------------------------------------------------------|
| Arquitetos de Software     | Definir princípios, criar fichas de solução, gerir ADR e rever designs                  |
| Developer                  | Aplicar padrões e requisitos de arquitetura nas implementações                           |
| QA / Test Engineer         | Validar que requisitos de arquitetura estão refletidos nos testes e no *go-live*         |
| AppSec Engineer            | Definir controlos de segurança, rever exceções e decisões de arquitetura                 |
| Product Owner              | Validar impacto de requisitos/exceções em prazos, custo e *scope*                       |
| DevOps/SRE                 | Automatizar validações de controlos de arquitetura                                       |

---

## 📝 User Stories Reutilizáveis

### US-01 - Definição de princípios de arquitetura segura
**Contexto.**  
Logo no arranque de um projeto é necessário definir princípios de arquitetura segura.

:::userstory
**História.**   
Como **Arquitetos de Software**, quero definir princípios de arquitetura segura para orientar todas as decisões técnicas.

**Critérios de aceitação (BDD).**
- **Dado** que o projeto inicia
  **Quando** os princípios de arquitetura são documentados
  **Então** ficam aprovados e versionados para referência

**Checklist.**
- [ ] Princípios definidos
- [ ] Aprovação AppSec Engineer
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
| Início | Novo projeto | Arquitetos de Software | Antes do design detalhado |

**Ligações úteis.**
- 🔗 [Cap. 2 - Requisitos de Segurança](/sbd-toe/sbd-manual/requisitos-seguranca/intro)

---

### US-02 - Ficha de arquitetura com controlos
**Contexto.**  
Ao desenhar a solução é preciso registar controlos de segurança.

:::userstory
**História.**   
Como **Arquitetos de Software**, quero produzir ficha de arquitetura com controlos de segurança, padrão reutilizável aprovado, e minimização de exposição externa, para garantir que a solução é segura, escalável e alinhada com padrões organizacionais.

**Critérios de aceitação (BDD).**
- **Dado** que o design está em definição  
  **Quando** documento a solução de arquitetura  
  **Então** a ficha inclui: zonas de confiança, exposição externa justificada, controlos de isolamento (rate limiting, circuit breakers, segmentação), padrão aplicado, e mapeamento a requisitos ARC-XXX

**Checklist.**
- [ ] Ficha de solução criada com template aprovado (`solution-architecture.md`)
- [ ] Zonas de confiança e fronteiras identificadas
- [ ] Exposição externa minimizada e justificada
- [ ] Controlos de isolamento especificados (rate limiting, circuit breakers, segregação lógica/física)
- [ ] Padrão de referência identificado (monólito L1, microserviços L2, plataforma crítica L3)
- [ ] Mapeamento a requisitos ARC-XXX registado
- [ ] Aprovação AppSec + Arquiteto arquivada

:::

**Artefactos & evidências.**  
- `solution-architecture.md` com zona de confiança diagram
- `controlos.md` (tipos de controlo, implementação, verificação)
- Referência a padrão em `modelos-referencia.md`

**Proporcionalidade.**
| Nível | Obrigatório? | Ajustes |
|---|---|---|
| L1 | Opcional | Ficha simplificada, controlos principais |
| L2 | Sim | Ficha detalhada, todos os controlos, padrão aprovado |
| L3 | Sim | Ficha completa + validação independente, padrão especializado, segregação física + lógica |

**Integração no SDLC.**
| Fase | Trigger | Responsável | SLA |
|---|---|---|---|
| Design | Definição da solução | Arquitetos de Software + AppSec Engineer | Antes da implementação |

**Ligações úteis.**
- 🔗 [Modelos de Arquitetura Segura Reutilizáveis - Addon 04](addon/04-diagramas-referencia.md)
- 🔗 [Catálogo de Requisitos ARC-XXX - Addon 01](addon/01-catalogo-requisitos.md)

---

### US-03 - Revisão de arquitetura
**Contexto.**  
Antes de implementar, o design deve ser revisto.

:::userstory
**História.**   
Como **AppSec Engineer**, quero rever designs de arquitetura para garantir conformidade.

**Critérios de aceitação (BDD).**
- **Dado** que a solução está desenhada
  **Quando** efetuo revisão
  **Então** confirmo ou peço ajustes

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
|---|---|---|---|
| Grooming | Design completo | AppSec Engineer | Antes da implementação |

**Ligações úteis.**
- 🔗 [Cap. 3 - Threat Modeling](/sbd-toe/sbd-manual/threat-modeling/intro)

---

### US-04 - Atualização de arquitetura em alterações críticas
**Contexto.**  
Sempre que há alteração crítica é preciso atualizar documentação.

:::userstory
**História.**   
Como **Developer**, quero atualizar ficha de arquitetura em alterações críticas para manter consistência.

**Critérios de aceitação (BDD).**
- **Dado** que há alteração crítica
  **Quando** atualizo documentação
  **Então** a ficha de arquitetura é revista

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
|---|---|---|---|
| Desenvolvimento | Alteração crítica | Developer + Arquitetos de Software | No mesmo sprint |

**Ligações úteis.**
- 🔗 [Cap. 2 - Requisitos de Segurança](/sbd-toe/sbd-manual/requisitos-seguranca/intro)

---

### US-05 - Validação da arquitetura em CI/CD
**Contexto.**  
Controlos de arquitetura devem ser validados automaticamente.

:::userstory
**História.**   
Como **DevOps/SRE + AppSec Engineer**, quero validar controlos de arquitetura no pipeline (incluindo topologia, IaC e policies), para garantir conformidade automática e reforçar integração da segurança em SDLC.

**Critérios de aceitação (BDD).**
- **Dado** que o pipeline CI/CD executa  
  **Quando** corro verificações de arquitetura (topologia, IaC, policies)  
  **Então** obtenho resultado automático com pass/fail + artefactos de auditoria

**Checklist.**
- [ ] Job de validação de topologia implementado (ex: Cartography, Clair, ReGraph)
- [ ] Validação de IaC com lint/scan (ex: Checkov, tfsec, TFLint) e enforcement de policies (ex: OPA, Kyverno)
- [ ] Backend remoto validado (locking, autenticação, segregação de estado)
- [ ] Políticas de admissão testadas (rate limiting, RBAC, NetworkPolicy)
- [ ] Logs e artefactos armazenados com versionamento e hash
- [ ] Alertas configurados para desconformidades críticas/medium
- [ ] SLA de remediação definido por nível (L1: alerta, L2: bloqueio H/C, L3: bloqueio M+)

:::

**Artefactos & evidências.**  
- `ci-pipeline.yml` com jobs de validação
- Relatórios de validação (Cartography, Checkov, OPA)
- Logs de bloqueios e remediações

**Proporcionalidade.**
| Nível | Obrigatório? | Ajustes |
|---|---|---|
| L1 | Opcional | Validações básicas (lint), alertas |
| L2 | Sim | Validações formais (topologia + IaC + policies), bloqueio H/C |
| L3 | Sim | Validações completas, bloqueio M+, enforcement automático, auditoria centralizada |

**Integração no SDLC.**
| Fase | Trigger | Responsável | SLA |
|---|---|---|---|
| CI/CD | Commit/MR de arquitetura ou IaC | DevOps/SRE + AppSec Engineer | Em cada build |

**Ligações úteis.**
- 🔗 [Requisitos IaC - Addon 06](addon/06-rastreabilidade.md)
- 🔗 [Cap. 7 - CI/CD Seguro](/sbd-toe/sbd-manual/cicd-seguro/intro)

---

### US-06 - Validação de impacto no negócio
**Contexto.**  
É necessário avaliar impacto da arquitetura no negócio.

:::userstory
**História.**   
Como **Product Owner**, quero validar impacto de requisitos de arquitetura para priorizar mitigação.

**Critérios de aceitação (BDD).**
- **Dado** que existem requisitos de arquitetura
  **Quando** avalio impacto no negócio
  **Então** priorizo mitigação

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
- 🔗 [Cap. 1 - Gestão de Risco](/sbd-toe/sbd-manual/classificacao-aplicacoes/intro)

---

### US-07 - Validação da arquitetura no Go-live
**Contexto.**  
Antes da entrada em produção, a arquitetura deve ser formalmente validada contra requisitos e padrões definidos, assegurando que exceções foram aprovadas e controlos estão implementados.

:::userstory
**História.**   
Como **QA / Test Engineer + AppSec Engineer + Arquitetos de Software**, quero validar a arquitetura antes do go-live, para garantir que todos os controlos definidos estão aplicados e exceções documentadas.

**Critérios de aceitação (BDD).**
- **Dado** que a aplicação está pronta para release  
  **Quando** executo checklist de validação da arquitetura  
  **Então** confirmo que todos os controlos estão cumpridos ou exceções aprovadas

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
|---|---|---|---|
| Release / Go-live | Preparação de release | QA / Test Engineer + AppSec Engineer + Arquitetos de Software | Antes da entrada em produção |

**Ligações úteis.**
- 🔗 Critérios de validação da arquitetura - *addon* correspondente

---

### US-08 - Gestão de Decisões Arquiteturais (ADR)
**Contexto.**  
Decisões de arquitetura críticas devem ser documentadas com alternativas, *trade-offs* e impacto em segurança.

:::userstory
**História.**  
Como **Arquitetos de Software**, quero registar decisões de arquitetura (ADR - Architecture Decision Record ) com o racional de segurança para garantir rastreabilidade e consistência.

**Critérios de aceitação (BDD).**
- **Dado** que ocorre uma decisão da arquitetura relevante
  **Quando** a ADR é criada segundo *template* aprovado
  **Então** inclui contexto, opções, decisão, impacto (L1–L3), controlos e revisão AppSec Engineer

**Checklist.**
- [ ] ADR criada com *template*
- [ ] Opções e impactos comparados
- [ ] Aprovação AppSec Engineer
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

### US-09 - Revisão de Fronteiras de Confiança e Integrações
**Contexto.**  
Integrações entre serviços e terceiros exigem revisão explícita de fronteiras de confiança.

:::userstory
**História.**  
Como **Arquitetos de Software + AppSec Engineer**, quero rever *trust boundaries* e integrações (internas/terceiros) para validar autenticação, autorização, encriptação e isolamento.

**Critérios de aceitação (BDD).**
- **Dado** que existe integração nova ou alterada
  **Quando** avalio fronteiras de confiança e controlos
  **Então** documento decisões, riscos residuais e mitigação

**Checklist.**
- [ ] Inventário de integrações atualizado
- [ ] Matriz de confiança definida
- [ ] Controlos verificados (AuthN/AuthZ/TLS/segregação)

:::

**Artefactos & evidências.** `trust-boundaries.md`, `integration-review.md`

**Proporcionalidade.**
| Nível | Obrigatório? | Ajustes |
|---|---|---|
| L1 | Sim | âmbito reduzido |
| L2 | Sim | âmbito completo |
| L3 | Sim | *Pen test* / validações adicionais conforme risco |

---

### US-10 - Sincronização Threat Modeling ↔ Arquitetura
**Contexto.**  
Decisões de arquitetura devem refletir o modelo de ameaças e vice-versa.

:::userstory
**História.**  
Como **Arquitetos de Software + AppSec Engineer**, quero sincronizar o modelo de ameaças com as decisões de arquitetura para garantir que controlos cobrem as ameaças priorizadas.

**Critérios de aceitação (BDD).**
- **Dado** que há decisão ou alteração da arquitetura
  **Quando** atualizo o modelo de ameaças e a ficha de solução
  **Então** mantenho cobertura e rastreabilidade ARC-XXX ↔ ameaça ↔ controlo

**Checklist.**
- [ ] Modelo de ameaças atualizado
- [ ] Ficha de solução alinhada
- [ ] Evidência de cobertura por controlo

:::

**Artefactos & evidências.** `threat-model.md`, `architecture-checklist.md`

**Proporcionalidade.**
| Nível | Obrigatório? | Ajustes |
|---|---|---|
| L1 | Sim | Modelo simplificado |
| L2 | Sim | Modelo completo |
| L3 | Sim | Modelo detalhado + validação por Auditores Internos |

---

### US-11 - Gestão de Exceções Arquiteturais
**Contexto.**  
Algumas situações exigem exceções formais com controlos compensatórios e prazo.

:::userstory
**História.**  
Como **Product Owner + AppSec Engineer**, quero gerir exceções de arquitetura com aprovação e controlos compensatórios para equilibrar risco e entrega.

**Critérios de aceitação (BDD).**
- **Dado** que é solicitada exceção
  **Quando** avalio impacto, compensações e prazo
  **Então** aprovo/rejeito e registo evidência e *owner* do risco

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

### US-12 - trigger para atualização da arquitetura
**Contexto.**  
Definir eventos que obrigam a rever e sincronizar documentação e controlos.

:::userstory
**História.**  
Como **Arquitetos de Software + DevOps/SRE**, quero manter uma lista de triggers que despoletam a revisão da arquitetura para garantir documentação e controlos atualizados.

**Critérios de aceitação (BDD).**
- **Dado** que acontece um evento (trigger)  (ex.: nova integração, alteração de dados sensíveis, mudança de infra/pipeline, novo *threat intel*)
  **Quando** executo a revisão associada
  **Então** atualizo ADR, fichas, modelo de ameaças e *checklists*

**Checklist.**
- [ ] Lista de triggers publicada (`arquitetura-triggers.md`)
- [ ] Ações por *trigger* definidas
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
### **US-13 - Padrões de Arquitetura Segura Reutilizáveis - Catálogo e Governação**

**Contexto.**  
Padrões de arquitetura aprovados reduzem tempo de design, erros e garantem conformidade com requisitos de segurança (ARC-007).

:::userstory
**História.**  
Como **Arquitetos de Software**, quero manter um catálogo de padrões de arquitetura segura (monólito L1, microserviços L2, plataforma crítica L3) com requisitos, ameaças mitigadas e checklist de implementação, para que novos projetos reutilizem designs seguros.

**Critérios de aceitação (BDD).**
- **Dado** que é iniciado um novo projeto  
  **Quando** seleciono um padrão do catálogo  
  **Então** a ficha do padrão inclui: diagram, requisitos ARC aplicáveis, ameaças mitigadas, checklist de implementação, e rastreabilidade a threat modeling

**Checklist.**
- [ ] Catálogo publicado (`modelos-referencia.md` ou similar)
- [ ] Mínimo 3 padrões documentados (L1, L2, L3)
- [ ] Cada padrão tem: diagram (PlantUML/`.drawio`), requisitos ARC-XXX, STRIDE/ameaças mitigadas, componentes-chave
- [ ] Checklist de implementação por padrão (com referência a US operacionais)
- [ ] Aprovação formal por AppSec e Arquitetura
- [ ] Versionamento e changelog mantido

:::

**Artefactos & evidências.**  
- `modelos-referencia.md` (catalogo com diagramas)
- `padroes-checklist.md` (checklist por padrão)
- Commit com aprovação de padrão

**Proporcionalidade.**
| Nível | Obrigatório? | Ajustes |
|---|---|---|
| L1 | Opcional | Catálogo simplificado |
| L2 | Sim | Catálogo formal com 2–3 padrões |
| L3 | Sim | Catálogo completo com evolução contínua |

**Integração no SDLC.**
| Fase | Trigger | Responsável | SLA |
|---|---|---|---|
| Design | Novo projeto ou reavaliação de padrão | Arquitetos de Software + AppSec Engineer | Antes da ficha de solução |

**Ligações úteis.**
- 🔗 [Addon 04 - Modelos de Arquitetura Segura Reutilizáveis](addon/04-diagramas-referencia.md)
- 🔗 [Addon 01 - Catálogo de Requisitos ARC](addon/01-catalogo-requisitos.md)

---

### **US-14 - Controlos Técnicos de Isolamento - Especificação e Validação**

**Contexto.**  
Controlos como rate limiting, circuit breakers, segregação lógica/física (ARC-006) requerem especificação clara e validação em teste.

:::userstory
**História.**  
Como **Arquitetos de Software + AppSec Engineer**, quero especificar controlos técnicos de isolamento (rate limiting, circuit breakers, ACLs, namespaces, DMZ) para domínios sensíveis, com SLA de implementação, para que a solução resista a sobre-carga, cascata de falhas e acesso não autorizado.

**Critérios de aceitação (BDD).**
- **Dado** que identifico um domínio sensível na arquitetura  
  **Quando** defino controlos de isolamento  
  **Então** cada controlo tem: métrica (ex: req/s), limiar, ação (drop, retry, fallback), e teste de validação

**Checklist.**
- [ ] Inventário de domínios sensíveis (ex: API crítica, base de dados, serviço de pagamento)
- [ ] Controlos definidos por domínio (rate limiting, circuit breakers, timeouts, retries)
- [ ] SLA de latência, throughput, tolerância a falhas
- [ ] Testes de carga/caos para validar controlos
- [ ] Monitorização em produção (métricas, alertas)
- [ ] Documentação em `isolamento-arquitetura.md`

:::

**Artefactos & evidências.**  
- `isolamento-arquitetura.md` (inventário + controlos)
- Testes de carga/caos com relatórios
- Dashboards de monitorização

**Proporcionalidade.**
| Nível | Obrigatório? | Ajustes |
|---|---|---|
| L1 | Opcional | Apenas domínios críticos |
| L2 | Sim | Todos os domínios sensíveis |
| L3 | Sim | Cobertura completa + testes periódicos |

**Integração no SDLC.**
| Fase | Trigger | Responsável | SLA |
|---|---|---|---|
| Design + Teste | Identificação de domínios sensíveis | Arquitetos de Software + QA / Test Engineer | Antes de produção |

---

### **US-15 - Segregação de Ambientes e Governação de Acesso (ARC-011) - L3**

**Contexto.**  
Aplicações críticas (L3) requerem segregação rigorosa entre dev/stage/prod com controlo de acesso formal (ARC-011).

:::userstory
**História.**  
Como **DevOps/SRE + GRC/Compliance**, quero implementar e validar segregação de ambientes (dev, QA, stage, prod) com isolamento lógico (namespaces, VPCs) e físico (clusters, IAM roles), para que cada ambiente tenha permissões mínimas e riscos de contaminação/acesso não autorizado sejam minimizados.

**Critérios de aceitação (BDD).**
- **Dado** que uma aplicação L3 é desplegada  
  **Quando** configuro ambientes  
  **Então** cada ambiente tem: namespace/VPC dedicado, RBAC mínimo por papel, auditoria de acesso, e alertas de acesso anómalo

**Checklist.**
- [ ] Ambientes segregados (dev, QA, stage, prod)
- [ ] Isolamento de rede (VPC, namespaces, subnets por ambiente)
- [ ] RBAC configurado com mínimo privilégio (SA dedicadas, roles específicas por ambiente)
- [ ] Credenciais rotacionadas e isoladas por ambiente
- [ ] Auditoria de acesso (logs, alertas de acesso cruzado)
- [ ] Validação de IaC com policies (OPA/Kyverno) + testes de segregação

:::

**Artefactos & evidências.**  
- IaC com segregação (Terraform/Helm com ambiente-specific vars)
- RBAC manifests (`rbac/*.yaml`)
- Relatórios de auditoria de acesso

**Proporcionalidade.**
| Nível | Obrigatório? | Ajustes |
|---|---|---|
| L1 | Não | - |
| L2 | Recomendado | Segregação lógica básica |
| L3 | Sim | Segregação lógica + física, auditoria formal |

**Integração no SDLC.**
| Fase | Trigger | Responsável | SLA |
|---|---|---|---|
| Deploy | Setup de ambiente L3 | DevOps/SRE + GRC/Compliance | Antes da entrada em produção |

**Ligações úteis.**
- 🔗 [Addon 02 - Casos Práticos (Caso 1: L3 crítica)](addon/02-casos-praticos.md)
- 🔗 [Cap. 14 - Governação e Contratação](/sbd-toe/sbd-manual/governanca-contratacao/intro)

---

### **US-16 - Threat Modeling no Design Inicial - Obrigatório para L2–L3**

**Contexto.**  
ARC-005 prescreve que arquitecuras devem considerar threat modeling nos fluxos críticos. Falta US explícita que **obriga** a aplicação de TM **antes** de aprovação de design em L2–L3.

:::userstory
**História.**  
Como **Arquitetos de Software + AppSec Engineer**, quero executar Threat Modeling (STRIDE/LINDDUN) no design inicial de arquitetura para L2–L3, identificando ameaças de fluxos críticos antes da aprovação, para que controlos sejam especificados proporcionalidade ao risco real.

**Critérios de aceitação (BDD).**
- **Dado** que a ficha de solução está em draft  
  **Quando** executo sessão de Threat Modeling  
  **Então** produzo DFD anotado com ameaças, severidades e controlos mitigadores, mapeando a requisitos ARC-XXX

**Checklist.**
- [ ] DFD criado com componentes, fluxos de dados e trust boundaries
- [ ] Sessão TM realizada com Arquiteto + AppSec + Developer
- [ ] Ameaças STRIDE catalogadas (S/T/R/I/D/E)
- [ ] LINDDUN aplicado se dados pessoais presentes
- [ ] Severidades atribuídas (CVSS ou escala interna)
- [ ] Controlos de mitigação especificados
- [ ] Rastreabilidade: ameaça → controlo → requisito ARC-XXX
- [ ] Evidência arquivada (modelo TM + ata/notas sessão)

:::

**Artefactos & evidências.**  
- DFD (ferramenta ou `.drawio`)
- `threat-model-architecture.md` (ameaças + controlos)
- Ata de sessão TM

**Proporcionalidade.**
| Nível | Obrigatório? | Ajustes |
|---|---|---|
| L1 | Não | - |
| L2 | Sim | TM formal STRIDE |
| L3 | Sim | TM completo (STRIDE + LINDDUN) + validação independente |

**Integração no SDLC.**
| Fase | Trigger | Responsável | SLA |
|---|---|---|---|
| Design | Ficha de solução em draft | Arquitetos de Software + AppSec Engineer | Antes da aprovação de design |

**Ligações úteis.**
- 🔗 [Cap. 3 - Threat Modeling](/sbd-toe/sbd-manual/threat-modeling/intro)
- 🔗 [US-10 - Sincronização TM ↔ Arquitetura](#us-10)

---

### **US-17 - Validação Formal da Arquitetura para L3 - Governance e Comité Técnico**

**Contexto.**  
ARC-012 prescreve "critérios formais de aprovação para aplicações L3" (Addon 05). Falta US que **formaliza** o processo de aprovação com comité ou governance body.

:::userstory
**História.**  
Como **Gestão Executiva/CISO + Arquitetos de Software**, quero estabelecer processo formal de aprovação de arquitetura para L3, com comité técnico ou governance review, para garantir que riscos estruturais são identificados e mitigados antes do go-live.

**Critérios de aceitação (BDD).**
- **Dado** que uma aplicação L3 está pronta para aprovação de arquitetura  
  **Quando** submeto ao comité de revisão  
  **Então** recebo parecer formal, com lista de conformidades/desvios, prazos para remediação, e decisão de aprovação/rejeição/aprovação com exceções

**Checklist.**
- [ ] Comité definido (participantes, responsabilidades)
- [ ] Critérios de aprovação formalizados (`20-checklist-revisao.md` ou similar)
- [ ] Documentação submetida (ficha, ADRs, threat modeling, exceções, validações)
- [ ] Review realizado (presencial ou assíncrono)
- [ ] Parecer formal emitido com desvios identificados
- [ ] Plano de remediação (ou exceção com compensações)
- [ ] Decisão arquivada com assinaturas

:::

**Artefactos & evidências.**  
- Termo de referência do comité
- Checklist de aprovação (`governance-checklist-l3.md`)
- Parecer formal assinado
- Plano de remediação / exceções aprovadas

**Proporcionalidade.**
| Nível | Obrigatório? | Ajustes |
|---|---|---|
| L1 | Não | - |
| L2 | Recomendado | Revisão técnica peer |
| L3 | Sim | Comité formal ou governance body |

**Integração no SDLC.**
| Fase | Trigger | Responsável | SLA |
|---|---|---|---|
| Release / Go-live | Preparação de release L3 | Gestão Executiva/CISO + Comité Técnico | 2 semanas antes do go-live |

**Ligações úteis.**
- 🔗 [Addon 05 - Critérios de Validação](addon/05-validacao.md)
- 🔗 [Cap. 14 - Governação](/sbd-toe/sbd-manual/governanca-contratacao/intro)
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
