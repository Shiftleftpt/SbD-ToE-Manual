---
id: policies-relevantes
title: Policies
description: Políticas organizacionais que suportam a adoção das práticas de arquitetura segura
tags: [arquitetura, governanca, politicas]
sidebar_position: 60
---

# 🏛️ Políticas Organizacionais - Arquitetura Segura

A adoção eficaz do Capítulo 04 - Arquitetura Segura - exige a existência de **políticas organizacionais formais** que sustentem, legitimem e tornem auditável a aplicação das práticas aqui descritas.

---

## 📌 Nota fundamental

> ⚠️ As práticas técnicas de definição de zonas de confiança, validação da arquitetura, exceções justificadas e rastreabilidade **devem estar suportadas por políticas organizacionais aprovadas e divulgadas**.

Estas políticas:

- Formalizam responsabilidades e critérios de aceitação técnica;
- Tornam visível a governação da arquitetura ao longo do ciclo de vida;
- Permitem auditoria objetiva de decisões e exceções arquitetónicas;
- Suportam a rastreabilidade entre requisitos, arquitetura e evidência técnica.

> 🧩 Este capítulo operacionaliza decisões formais sobre arquitetura - a política define, o capítulo executa.

---

## 🧾 Políticas recomendadas

| Nome da Política                                 | Obrigatória? | Aplicação                                 | Conteúdo mínimo esperado                                                                 |
|--------------------------------------------------|--------------|--------------------------------------------|--------------------------------------------------------------------------------------------|
| Política de Arquitetura Segura                   | ✅ Sim       | Todas as equipas com responsabilidade técnica | Padrões obrigatórios, definição de zonas de confiança, segmentação, requisitos mínimos     |
| Política de Aprovação Técnica de Design          | ✅ Sim       | Projetos com impacto da arquitetura            | Processo formal de revisão, papéis e responsabilidades, critérios técnicos de aceitação    |
| Política de Documentação e Versionamento Arquitetural | ✅ Sim   | Sistemas com criticidade L2 ou L3            | Regras de diagrama, versão controlada, atualização em alterações estruturais               |
| Política de Rastreabilidade Arquitetónica        | ✅ Sim       | Projetos sujeitos a controlo ou auditoria    | Mapeamento de requisitos (ARC-00x) → componente → controlo técnico                         |
| Política de Exceções Técnicas em Arquitetura     | ✅ Sim       | Sempre que um requisito não for aplicável    | Formulário formal, ciclo de revisão, plano compensatório, validade e owner técnico         |

---

## 📋 Estrutura sugerida de cada política

Cada política organizacional deve conter:

- **Objetivo e âmbito** (ex: aplica-se a todos os projetos L2+);
- **Critérios técnicos obrigatórios** (ex: ZTCs, checklists, modelo de exceções);
- **Papéis e responsabilidades** (arquitetura, segurança, desenvolvimento, operações);
- **Exigência de evidência e rastreabilidade** (ex: diagrama, registos de validação);
- **Processo de revisão e atualização da própria política** (ex: anual);
- **Integração com processos de release e auditoria técnica**.

---

## ✅ Recomendações finais

- Estas políticas devem ser **formais, acessíveis e aprovadas pelas áreas de arquitetura e segurança**;
- A sua aplicação deve estar **integrada no ciclo de vida** via templates, gates e práticas de CI/CD;
- A existência destas políticas **viabiliza a arquitetura segura como prática auditável e transversal**, garantindo rastreabilidade e consistência.

> 📌 A sua ausência compromete a coerência das decisões técnicas, a validação de exceções e a auditabilidade da arquitetura - tanto em projetos internos como em contextos regulados.
