---
id: policies-relevantes
title: Policies
description: Políticas necessárias para enquadrar e reforçar as práticas de desenvolvimento seguro definidas neste capítulo
tags: [GenAI, codificação segura, desenvolvimento, exceções, políticas, validacao]
sidebar_position: 60
---


# 🏠 Políticas Organizacionais - Desenvolvimento Seguro

A aplicação eficaz do Capítulo 06 - Desenvolvimento Seguro - requer a existência de **políticas organizacionais formais** que enquadrem, reforcem e legitimem as práticas de codificação segura, revisão de código e validação.

Estas políticas garantem que:

- A segurança é tratada como critério de qualidade essencial;
- Os requisitos de segurança têm expressão concreta no ciclo de vida de desenvolvimento;
- Existem regras claras, auditáveis e aplicáveis transversalmente pelas equipas de engenharia.

---

## 📄 Políticas Organizacionais Relevantes

| Nome da Política                                  | Obrigatória? | Aplicação                            | Resumo do conteúdo necessário |
|---------------------------------------------------|--------------|---------------------------------------|-------------------------------|
| Política de Padrões de Codificação Segura         | ✅ Sim       | Todas as equipas de desenvolvimento  | Guia formal com boas práticas, padrões proibidos, regras obrigatórias por stack ou linguagem. |
| Política de Validação e Revisão de Código         | ✅ Sim       | Todos os repositórios e pipelines     | Requisitos para revisão por pares, uso de linters, tags `@sec:`, rastreabilidade e bloqueios. |
| Política de Aprovação de Dependências de Código   | ✅ Sim       | Introdução de bibliotecas e pacotes    | Processo formal para aprovar e rastrear dependências externas ou internas reutilizadas. |
| Política de Justificação de Exceções Técnicas     | ⚠️ Opcional | Equipa de segurança, tech leads        | Casos aceitáveis de exceção, requisitos de documentação, prazo e aprovação formal. |
| Política de Uso Controlado de GenIA em Desenvolvimento | ⚠️ Opcional | Equipas com acesso a ferramentas GenIA | Critérios para uso de sugestões automáticas (ex: Copilot); validação, anotação de origem, revisão obrigatória. |

---

## 📃 Estrutura mínima de cada política

Cada política organizacional deve conter, no mínimo:

- **Objetivo e âmbito** da política;
- **Critérios obrigatórios** por tipo de aplicação, linguagem, stack ou equipa;
- **Papéis e responsabilidades** (devs, reviewers, tech leads, segurança);
- **Pontos de integração obrigatórios** no SDLC ou pipeline;
- **Exigência de evidências rastreáveis** (tags, logs, relatórios);
- **Frequência de revisão** e validação da própria política.

---

## ✅ Recomendações finais

- As políticas devem ser **oficialmente aprovadas e publicadas** pela gestão de segurança e engenharia;
- Devem estar acessíveis, ser comunicadas de forma eficaz e integradas nos processos de onboarding e revisão técnica;
- Devem existir **mecanismos de validação e auditoria da aplicação das políticas**;
- A sua existência e aplicação são **critérios formais de maturidade em desenvolvimento seguro**;
- Recomenda-se que as políticas sejam acompanhadas de exemplos práticos, checklists e templates reutilizáveis.

> 📁 Templates de políticas poderão ser incluídos como ficheiros `60-*.md` complementares em futuras versões do manual.
