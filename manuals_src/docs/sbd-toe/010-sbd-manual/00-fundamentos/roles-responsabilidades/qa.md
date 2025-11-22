---
id: qa
title: Quality Assurance (QA)
sidebar_label: 🧪 Quality Assurance (QA)
description: Responsabilidades de QA no SbD-ToE
tags: [qa, quality-assurance, testes, responsabilidades]
sidebar_position: 3
---

# 🧪 Quality Assurance (QA)

## Visão Geral

QA **valida requisitos de segurança transformando-os em critérios de aceitação** claros e testáveis.  
Já não basta validar que o software "funciona": é necessário comprovar que funciona de forma resiliente e protegida contra ameaças.

### Responsabilidades Principais
- Validam requisitos de segurança (Cap. 02)
- Executam testes funcionais e de segurança em paralelo
- Confirmam que correções não introduzem regressões
- Asseguram que controlos de segurança funcionam como esperado

### Contexto Organizacional
QA é a primeira linha de defesa contra vulnerabilidades que escapam ao desenvolvimento. Sem testes de segurança robustos, o código inseguro chega a produção.

## Enquadramento Regulatório

QA materializa exigências de:
- **NIS2**: Verificação de medidas técnicas
- **DORA**: Testes regulares de resiliência digital

---

## Atividades por Capítulo

### Cap. 01 - Classificação de Aplicações
Validar que **requisitos aplicáveis por nível de risco estão cumpridos** antes da entrada em produção, garantindo conformidade com a classificação atribuída.

**User Stories:**
- [US-05: Validação antes do go-live](/sbd-toe/sbd-manual/classificacao-aplicacoes/aplicacao-lifecycle#us-05---validação-antes-do-go-live) — Verificar cumprimento de requisitos por nível

### Cap. 02 - Requisitos de Segurança
Garantir que todos os **requisitos têm rastreabilidade no backlog** e validação associada, prevenindo falsos positivos ou ausência de controlo.

**User Stories:**
- [US-04: Rastreabilidade de requisitos](/sbd-toe/sbd-manual/requisitos-seguranca/aplicacao-lifecycle#us-04---rastreabilidade-de-requisitos) — Auditoria e verificação de rastreamento
- [US-05: Definição de critérios de validação](/sbd-toe/sbd-manual/requisitos-seguranca/aplicacao-lifecycle#us-05---definição-de-critérios-de-validação) — Todos os requisitos com validação clara
- [US-09: Validação por requisito/domínio](/sbd-toe/sbd-manual/requisitos-seguranca/aplicacao-lifecycle#us-09---validação-por-requisitodomínio-req-xxx--evidência) — Evidência objetiva e rastreável de cumprimento
- [US-12: Validação de tags SEC-Lx-* no pipeline](/sbd-toe/sbd-manual/requisitos-seguranca/aplicacao-lifecycle#us-12---validação-de-tags-sec-lx--e-requisitos-no-pipeline) — Rastreabilidade automática

### Cap. 03 - Threat Modeling
Traduzir **cenários de threat modeling em testes objetivos**, garantindo que ameaças identificadas têm correspondência em validações práticas.

### Cap. 04 - Arquitetura Segura
Validar a **arquitetura antes do go-live**, garantindo que todos os controlos definidos estão aplicados e exceções documentadas.

**User Stories:**
- [US-08: Validação de arquitetura antes de go-live](/sbd-toe/sbd-manual/arquitetura-segura/aplicacao-lifecycle#us-08--validação-de-arquitetura-antes-de-go-live) — Verificar controlos e exceções documentadas

### Cap. 06 - Desenvolvimento Seguro
Conduzir **testes estáticos e dinâmicos** em colaboração com AppSec, validando que código cumpre standards de segurança.

**User Stories:**
- [US-11: Arquivo Central de Evidências de Validação](/sbd-toe/sbd-manual/desenvolvimento-seguro/aplicacao-lifecycle#us-11---arquivo-central-de-evidências-de-validação) — Rastreabilidade e auditoria centralizada

### Cap. 07 - CI/CD Seguro
Assegurar que **pipelines incorporam verificações automáticas de segurança**, validando que gates funcionam corretamente.

### Cap. 10 - Testes de Segurança
Executar testes dinâmicos autenticados, fuzzing em endpoints críticos e instrumentação IAST em staging para detetar vulnerabilidades exploráveis em runtime.

**User Stories:**
- [US-03: DAST autenticado em Staging](/sbd-toe/sbd-manual/testes-seguranca/aplicacao-lifecycle#us-03---dast-autenticado-em-staging) — Detetar vulnerabilidades exploráveis em runtime
- [US-06: Fuzzing dirigido a APIs críticas](/sbd-toe/sbd-manual/testes-seguranca/aplicacao-lifecycle#us-06---fuzzing-dirigido-a-apis-críticas) — Detetar falhas invisíveis em testes convencionais
- [US-09: IAST com Instrumentação em Staging](/sbd-toe/sbd-manual/testes-seguranca/aplicacao-lifecycle#us-09---iast-com-instrumentação-em-staging) — Observar chamadas inseguras em runtime

### Cap. 11 - Deploy Seguro
Validar releases em **staging com ambiente segregado**, dados controlados e testes funcionais + segurança. Executar validações técnicas com gates condicionais por risco.

**User Stories:**
- [US-03: Validação em staging pré-produção](/sbd-toe/sbd-manual/deploy-seguro/aplicacao-lifecycle#us-03--validação-em-staging-pré-produção) — Ambiente segregado com testes completos
- [US-04: Gates de deploy condicionais por risco](/sbd-toe/sbd-manual/deploy-seguro/aplicacao-lifecycle#us-04--gates-de-deploy-condicionais-por-risco) — Validações técnicas proporcionais

### Cap. 12 - Monitorização
Validar que **alertas e métricas de runtime** estão configurados corretamente, confirmando que eventos críticos são detetados.

### Cap. 13 - Formação
Participar em **exercícios práticos estruturados** (labs, CTFs, simulações) para garantir conhecimento aplicável em contexto real.

**User Stories:**
- [US-05: Exercícios práticos estruturados](/sbd-toe/sbd-manual/formacao-onboarding/aplicacao-lifecycle#us-05--exercícios-práticos-estruturados-labs-ctfs-simulações) — Consolidar conhecimento através da prática

---

## Referências aos Capítulos

Para contexto e enquadramento completo:

- [Cap. 01 - Classificação de Aplicações](/sbd-toe/sbd-manual/classificacao-aplicacoes/intro)
- [Cap. 02 - Requisitos de Segurança](/sbd-toe/sbd-manual/requisitos-seguranca/intro)
- [Cap. 03 - Threat Modeling](/sbd-toe/sbd-manual/threat-modeling/intro)
- [Cap. 04 - Arquitetura Segura](/sbd-toe/sbd-manual/arquitetura-segura/intro)
- [Cap. 06 - Desenvolvimento Seguro](/sbd-toe/sbd-manual/desenvolvimento-seguro/intro)
- [Cap. 07 - CI/CD Seguro](/sbd-toe/sbd-manual/cicd-seguro/intro)
- [Cap. 10 - Testes de Segurança](/sbd-toe/sbd-manual/testes-seguranca/intro)
- [Cap. 11 - Deploy Seguro](/sbd-toe/sbd-manual/deploy-seguro/intro)
- [Cap. 12 - Monitorização e Operações](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro)
- [Cap. 13 - Formação e Onboarding](/sbd-toe/sbd-manual/formacao-onboarding/intro)
