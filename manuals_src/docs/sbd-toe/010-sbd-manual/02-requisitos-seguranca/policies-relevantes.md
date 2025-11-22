---
description: Políticas que sustentam a definição, exceção e validação de requisitos
id: policies-relevantes
sidebar_position: 60
tags:
- excecoes
- exceções
- políticas
- rastreabilidade
- requisitos
- validacao
- validação
title: Policies Relevantes
---



# 🏛️ Políticas Organizacionais - Requisitos de Segurança

A adoção eficaz do Capítulo 02 - Requisitos de Segurança - exige a existência de **políticas organizacionais formais** que **enquadrem, legitimem e sustentem a aplicação das práticas descritas neste capítulo**.

---

## 📌 Nota fundamental

> ⚠️ As práticas operacionais prescritas neste capítulo (catálogo, seleção por risco, rastreabilidade, critérios de aceitação) **devem ser legitimadas formalmente por políticas organizacionais aprovadas**.

Estas políticas:

- Tornam **vinculativa** a aplicação de requisitos de segurança desde o início do desenvolvimento;
- Permitem que os controlos aplicados estejam **proporcionais ao risco identificado**;
- Servem de base normativa para **auditorias internas, revisões técnicas e contratualização com terceiros**.

> 🧩 Este capítulo **implementa, na prática, o que as políticas definem**. A política aprova, o capítulo operacionaliza.

> 📎 A exigência de políticas formais sobre requisitos de segurança é explicitamente referida em frameworks como **NIST SSDF**, **ISO/IEC 27001**, **OWASP SAMM**, **ENISA SDLC** e **CIS Controls v8** - estas políticas não são apenas boas práticas, são uma expectativa normativa.

---

## 🧾 Políticas recomendadas

| Nome da Política                                        | Obrigatória? | Aplicação                                | Resumo do conteúdo necessário |
|---------------------------------------------------------|--------------|-------------------------------------------|-------------------------------|
| Política de Requisitos de Segurança Aplicacionais       | ✅ Sim       | Todos os projetos e equipas de produto    | Catálogo obrigatório, seleção por risco, rastreabilidade, critérios de aceitação |
| Política de Integração de Requisitos no Backlog         | ⚠️ Opcional  | Equipa de desenvolvimento, PO, QA         | Requisitos devem constar nos artefactos de planeamento (stories/tasks) com tags |
| Política de Validação de Requisitos em Pipelines        | ⚠️ Opcional  | DevOps, QA, segurança                     | Critérios mínimos automatizados para bloqueio de builds e validação de releases |

---

## 🧩 Estrutura sugerida de cada política

Cada política organizacional deve conter, no mínimo:

- **Objetivo e âmbito** da política;
- **Âmbito de aplicação**: quem, onde e quando se aplica;
- **Critérios e regras obrigatórias** (ex: quando aplicar, como selecionar requisitos, quando rever);
- **Papéis e responsabilidades** (equipa de produto, arquitetura, segurança, gestão);
- **Mecanismos de rastreabilidade e evidência**;
- **Periodicidade de revisão da própria política** (ex: anual, com revisão após incidentes).

---

## ✅ Recomendações finais

- As políticas devem ser **aprovadas pela liderança de segurança** e comunicação transversal à organização;
- Devem estar **documentadas, acessíveis e versionadas**;
- A existência destas políticas é pré-condição para:
  - Garantir **coerência e maturidade organizacional**;
  - Sustentar **auditorias de segurança ou certificações**;
  - Servir de base a processos de **contratação de software e avaliação de fornecedores**.

> 📌 Templates para estas políticas poderão ser disponibilizados como ficheiros `60-*.md` complementares em futuras versões do manual.
