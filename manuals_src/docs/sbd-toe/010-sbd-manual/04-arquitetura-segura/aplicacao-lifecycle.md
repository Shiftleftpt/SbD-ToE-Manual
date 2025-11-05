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

| Fase / Evento              | Ação esperada                                      | Quem participa                           | Artefacto principal             |
|----------------------------|----------------------------------------------------|------------------------------------------|--------------------------------|
| Início de projeto / épico  | Definir princípios de arquitetura segura            | Arquiteto, DevSecOps, AppSec             | `principios-arquitetura.md`    |
| Design de solução          | Produzir ficha de arquitetura com controlos de segurança | Arquiteto + AppSec                       | `solution-architecture.md`     |
| Grooming / Planeamento     | Rever padrões e aplicar requisitos arquiteturais    | Developer + Arquiteto                    | `design-review.md`             |
| Alterações críticas        | Atualizar ficha de arquitetura                     | Developer + Arquiteto + AppSec           | `arquitetura-atualizada.md`    |
| Release / Go-live          | Validar que controlos arquiteturais estão cumpridos | QA + AppSec + Arquiteto                  | `checklist-arquitetura.md`     |
| CI/CD pipeline             | Validar controlos arquiteturais automatizáveis      | Eng. CI/CD + DevSecOps                   | `ci-logs-validacao.txt`        |

---

## 👥 Quem faz o quê

| Papel / Função             | Responsabilidades-chave                                      |
|----------------------------|--------------------------------------------------------------|
| Arquiteto / DevSecOps      | Definir princípios, criar fichas de solução e rever designs   |
| Developer / Equipa de Desenvolvimento | Aplicar padrões e requisitos arquiteturais nas implementações |
| QA / Test Engineer         | Validar que requisitos arquiteturais estão refletidos nos testes |
| AppSec / Segurança         | Definir controlos de segurança e rever exceções               |
| Product Owner / Negócio    | Validar impacto de requisitos arquiteturais em prazos e custo |
| Eng. CI/CD                 | Automatizar validações de controlos arquiteturais             |

---

## 📝 User Stories Reutilizáveis

### US-01 – Definição de princípios de arquitetura segura
**Contexto.**  
Logo no arranque de um projeto é necessário definir princípios de arquitetura segura.

**📖 Rationale científico.**  
Prática alinhada com **OWASP SAMM – Governance/Strategy & Metrics**, **BSIMM SR1.1**, e **SSDF PS.1** (definição de práticas de design).  
Mitiga falhas de base como **CWE-657 (Violation of Secure Design Principles)** e **CWE-1004 (Sensitive Data Exposure by Design)**.  
Segundo o **Verizon DBIR**, a ausência de princípios claros contribui para ~20% das falhas de design reportadas. O **BSIMM13** mostra que equipas com princípios formais de arquitetura têm níveis de maturidade significativamente superiores.

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
| Fase | Gatilho | Responsável | SLA |
|------|---------|-------------|-----|
| Início | Novo projeto | Arquiteto | Antes do design detalhado |

**Ligações úteis.**
- 🔗 [Cap. 2 – Requisitos de Segurança](/sbd-toe/sbd-manual/requisitos-seguranca/intro)

---

### US-02 – Ficha de arquitetura com controlos
**Contexto.**  
Ao desenhar a solução é preciso registar controlos de segurança.

**📖 Rationale científico.**  
Previsto em **SSDF PS.3** (definir controlos de design), **SAMM Architecture (2/3)** e **BSIMM AM2.4** (usar revisões arquiteturais com controlos de segurança).  
Mitiga riscos como **CWE-16 (Configuration Issues)** e **CWE-710 (Improper Adherence to Coding Standards)**.  
Segundo o **NIST SP 800-160**, fichas de arquitetura reduzem falhas arquiteturais em produção e aceleram revisões de segurança.

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
| Fase | Gatilho | Responsável | SLA |
|------|---------|-------------|-----|
| Design | Criação da solução | Arquiteto | Antes da implementação |

**Ligações úteis.**
- 🔗 [Cap. 4 – Catálogo de Requisitos Arquiteturais](./addon/catalogo-requisitos)

---

### US-03 – Revisão de arquitetura
**Contexto.**  
Antes de implementar, o design deve ser revisto.

**📖 Rationale científico.**  
Apoiado por **BSIMM AM3.1** (revisões formais), **SSDF PS.3** (revisar e atualizar requisitos), e **SAMM – Design/Threat Assessment**.  
Mitiga riscos como **CWE-657 (Violation of Secure Design Principles)** e **OSC&R – Surface Expansion**.  
Segundo a **ENISA** e o **DBIR**, revisões arquiteturais formais reduzem significativamente o risco de vulnerabilidades críticas escaparem para produção.

:::userstory
**História.**   
Como **AppSec / Segurança**, quero rever designs arquiteturais para garantir conformidade.

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
| Fase | Gatilho | Responsável | SLA |
|------|---------|-------------|-----|
| Grooming | Design completo | AppSec | Antes da implementação |

**Ligações úteis.**
- 🔗 [Cap. 3 – Threat Modeling](/sbd-toe/sbd-manual/threat-modeling/intro)

---

### US-04 – Atualização de arquitetura em alterações críticas
**Contexto.**  
Sempre que há alteração crítica é preciso atualizar documentação.

**📖 Rationale científico.**  
Apoiado em **SSDF PS.3**, **BSIMM AM3.2** e **SLSA v1.0** (gestão de proveniência).  
Mitiga riscos de **CWE-16 (Configuration Issues)** e **OSC&R – Dependency Expansion**.  
Segundo o **DBIR**, 1 em cada 3 incidentes críticos decorre de alterações não refletidas em documentação arquitetural.

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
| Fase | Gatilho | Responsável | SLA |
|------|---------|-------------|-----|
| Desenvolvimento | Alteração crítica | Developer | No mesmo sprint |

**Ligações úteis.**
- 🔗 [Cap. 2 – Requisitos de Segurança](/sbd-toe/sbd-manual/requisitos-seguranca/intro)

---

### US-05 – Validação arquitetural em CI/CD
**Contexto.**  
Controlos arquiteturais devem ser validados automaticamente.

**📖 Rationale científico.**  
Previsto em **DSOMM – Automation**, **BSIMM SE3.3**, **SAMM Verification (2/3)** e **SSDF PO.3**.  
Mitiga riscos de **CWE-693 (Protection Mechanism Failure)** e de divergência entre arquitetura e implementação real.  
O **BSIMM13** indica que organizações com validações arquiteturais em pipelines reduzem falhas escapadas em 25%.

:::userstory
**História.**   
Como **Eng. CI/CD**, quero validar controlos arquiteturais no pipeline para reforçar automação.

**Critérios de aceitação (BDD).**
- Dado que o pipeline corre
- Quando executo verificações arquiteturais
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
| Fase | Gatilho | Responsável | SLA |
|------|---------|-------------|-----|
| CI/CD | Execução pipeline | Eng. CI/CD | Em cada build |

**Ligações úteis.**
- 🔗 [Cap. 5 – Dependências e SCA](/sbd-toe/sbd-manual/dependencias-sbom-sca/intro)

---

### US-06 – Validação de impacto no negócio
**Contexto.**  
É necessário avaliar impacto arquitetural no negócio.

**📖 Rationale científico.**  
Prática recomendada por **SAMM – Governance/Business Alignment**, **BSIMM SR2.4**, **SSDF RM.2** e **ISO/IEC 27005** (avaliação de impacto).  
Mitiga falhas como **CWE-1004 (Sensitive Data Exposure due to Misclassification)** e ausência de priorização eficaz.  
Segundo o **DBIR**, a falta de alinhamento entre requisitos técnicos e impacto no negócio resulta em desperdício de recursos e exposição prolongada a riscos críticos.

:::userstory
**História.**   
Como **Product Owner**, quero validar impacto de requisitos arquiteturais para priorizar mitigação.

**Critérios de aceitação (BDD).**
- Dado que existem requisitos arquiteturais
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
| Fase | Gatilho | Responsável | SLA |
|------|---------|-------------|-----|
| Grooming | Requisitos arquiteturais definidos | Product Owner | Antes da priorização |

**Ligações úteis.**
- 🔗 [Cap. 1 – Gestão de Risco](/sbd-toe/sbd-manual/classificacao-aplicacoes/intro)

---

### US-07 – Validação arquitetural no Go-live
**Contexto.**  
Antes da entrada em produção, a arquitetura deve ser formalmente validada contra requisitos e padrões definidos, assegurando que exceções foram aprovadas e controlos estão implementados.

**📖 Rationale científico.**  
Prática prevista em **OWASP SAMM – Verification (2/3)**, **BSIMM CR3.2** (validação final antes de release), **SSDF RV.4** (formal approval of residual risk) e **ISO/IEC 27034** (Application Security Validation).  
Mitiga riscos como **CWE-693 (Protection Mechanism Failure)**, **CWE-358 (Improperly Implemented Security Check)** e lacunas de validação em runtime.  
Segundo o **Verizon DBIR** e relatórios **ENISA**, falhas não detetadas em pré-produção estão entre as principais causas de incidentes críticos pós-release.

:::userstory
**História.**   
Como **QA / AppSec / Arquiteto**, quero validar a arquitetura antes do go-live, para garantir que todos os controlos definidos estão aplicados e exceções documentadas.

**Critérios de aceitação (BDD).**
- Dado que a aplicação está pronta para release  
- Quando executo checklist de validação arquitetural  
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
| Fase | Gatilho | Responsável | SLA |
|------|---------|-------------|-----|
| Release / Go-live | Preparação de release | QA + AppSec + Arquiteto | Antes da entrada em produção |

**Ligações úteis.**
- 🔗 [Cap. 4 – Critérios de Validação Arquitetural](/sbd-toe//sbd-manual/arquitetura-segura/addon/validacao)

---

## 📑 Artefactos Esperados

| Artefacto                   | Origem / US | Evidência associada                  |
|-----------------------------|-------------|--------------------------------------|
| `principios-arquitetura.md` | US-01       | Commit + aprovação AppSec            |
| `solution-architecture.md`  | US-02       | `controles.md`                       |
| `review-arquitetura.md`     | US-03       | Issue em repositório de arquitetura  |
| `arquitetura-atualizada.md` | US-04       | Commit + issue associada             |
| `ci-pipeline.yml`           | US-05       | Logs CI/CD                           |
| `impacto-arquitetura.md`    | US-06       | Backlog atualizado                   |

---

## 📊 Matriz de Proporcionalidade L1–L3

| Nível | Aplicação de práticas de Arquitetura Segura |
|-------|---------------------------------------------|
| L1    | Aplicação opcional de princípios básicos e apenas requisitos/alterações críticas |
| L2    | Aplicação sistemática de princípios, fichas de solução, revisões formais e atualizações em alterações críticas |
| L3    | Aplicação completa e obrigatória de todas as práticas, incluindo validação em CI/CD, revisões independentes e avaliação de impacto no negócio |

---

## 📌 Recomendações Finais

- Garantir que todos os papéis participam de forma proporcional ao risco e fase do ciclo de vida.
- Centralizar artefactos em repositório versionado para auditoria e rastreabilidade.
- Estabelecer SLAs claros para revisões e aprovações (ex.: antes do design detalhado, antes da implementação, até ao fecho do sprint).
- Integrar verificações automatizadas sempre que possível no pipeline CI/CD.
- Reforçar a ligação com requisitos do Cap. 2 para rastreabilidade de ponta a ponta.
