---
id: scrum-master
title: Scrum Master / Team Lead
sidebar_label: 🧭 Scrum Master / Team Lead
description: Responsabilidades do Scrum Master/Team Lead no SbD-ToE
tags: [agile, responsabilidades, scrum-master, team-lead]
sidebar_position: 9
---

# 🧭 Scrum Master / Team Lead

## Visão Geral

Scrum Master/Team Lead é o **guardião da disciplina ágil**.  
Assegura que segurança não é relegada para "quando houver tempo", mas **integrada no planeamento e execução diária** das equipas.

### Responsabilidades Principais
- Facilitam a integração da segurança no ciclo ágil
- Removem bloqueios que dificultem a implementação de práticas seguras
- Promovem a disciplina de aplicação dos checklists de revisão
- Moderam sessões de threat modeling

### Contexto Organizacional
Ajudam a operacionalizar a exigência de **governação executiva sobre segurança digital** constante em NIS2 e DORA, garantindo que equipas atuam segundo processos definidos.

## Enquadramento Regulatório

Operacionaliza:
- **NIS2** e **DORA**: Implementação de governação executiva sobre práticas de segurança
- Traduz políticas organizacionais em ações concretas no sprint

---

## Atividades por Capítulo

### Cap. 01-02 - Classificação e Requisitos
Facilitar **discussões sobre criticidade e requisitos**, garantindo que toda a equipa compreende o contexto de risco. Rever classificação em integrações críticas ou mudanças relevantes.

**User Stories:**
- [US-02: Revisão em alterações críticas](/sbd-toe/sbd-manual/requisitos-seguranca/aplicacao-lifecycle#us-02--revisão-em-integração-crítica-ou-mudança-relevante) — Atualizar controlos e rastreabilidade (com Arquitetos)

### Cap. 03 - Threat Modeling
**Moderar sessões de threat modeling**, criar modelo de ameaça inicial com DFDs e STRIDE/LINDDUN, garantir participação de toda a equipa.

**User Stories:**
- [US-01: Modelo de ameaça inicial](/sbd-toe/sbd-manual/threat-modeling/aplicacao-lifecycle#us-01--criação-de-modelo-de-ameaça-inicial) — Riscos visíveis desde o início (com Arquitetos)

### Cap. 06 - Desenvolvimento Seguro
Garantir que **cada PR é revisto com checklist de segurança obrigatória**, prevenindo vulnerabilidades e mantendo registo de conformidade.

**User Stories:**
- [US-01: Checklist de segurança em PR](/sbd-toe/sbd-manual/desenvolvimento-seguro/aplicacao-lifecycle#us-01--revisão-de-pr-com-checklist-de-segurança) — Prevenir vulnerabilidades

### Cap. 06-07 - Desenvolvimento e CI/CD
Assegurar que **práticas seguras entram no sprint planning**, com DoD incluindo critérios de segurança validáveis.

### Cap. 13 - Formação e Onboarding
Promover **capacitação e formação contínua**, apoiar cultura de segurança, remover impedimentos para learning time.

---

## Referências aos Capítulos

Para contexto e enquadramento completo:

- [Cap. 01 - Classificação de Aplicações](/sbd-toe/sbd-manual/classificacao-aplicacoes/intro)
- [Cap. 02 - Requisitos de Segurança](/sbd-toe/sbd-manual/requisitos-seguranca/intro)
- [Cap. 03 - Threat Modeling](/sbd-toe/sbd-manual/threat-modeling/intro)
- [Cap. 06 - Desenvolvimento Seguro](/sbd-toe/sbd-manual/desenvolvimento-seguro/intro)
- [Cap. 07 - CI/CD Seguro](/sbd-toe/sbd-manual/cicd-seguro/intro)
- [Cap. 13 - Formação e Onboarding](/sbd-toe/sbd-manual/formacao-onboarding/intro)
