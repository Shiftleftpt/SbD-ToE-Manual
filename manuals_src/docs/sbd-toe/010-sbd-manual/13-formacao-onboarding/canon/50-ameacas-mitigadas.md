---
id: ameacas-mitigadas
title: Ameaças Mitigadas - Formação e Onboarding Seguro
description: Ameaças mitigadas pela aplicação sistemática das práticas de capacitação, onboarding e cultura técnica segura.
tags: [ameacas, cultura, mitigacao, onboarding, osc-r, segurança humana, terceiros]
sidebar_position: 50
---


# 🔐 Ameaças Mitigadas - Capítulo 13: Formação e Onboarding Seguro

Este capítulo estabelece práticas para garantir que todas as pessoas com impacto direto ou indireto na segurança estão preparadas para agir corretamente.  
Define requisitos de **formação por perfil**, **onboarding técnico rastreável**, **validação de conhecimento** e **programas de cultura ativa** (ex: Security Champions).

> 🧠 Este é o único capítulo que atua sobre a **causa raiz humana** de falhas de segurança, mitigando riscos associados a desconhecimento, erro operacional e cultura negligente.

---

## 📚 Categoria 1 - Erros humanos evitáveis

| Ameaça                                           | Fonte                                                                 | Como surge                                                                 | Como a prática mitiga                                                                  | Controlos associados                              |
|--------------------------------------------------|------------------------------------------------------------------------|------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------|----------------------------------------------------|
| Configuração insegura por desconhecimento        | CAPEC-118, CWE-693,  T1.1                                        | Programadores aplicam defaults ou padrões inseguros sem consciência do risco | Formação obrigatória por função com contextualização dos riscos reais                  | `addon/01-catalogo-formativo.md`, `addon/02-trilho-formativo.md` |
| Reutilização indevida de segredos ou tokens      | CAPEC-137, OSC&R (Credential Management), CWE-798                     | Falta de noção sobre a gestão correta de credenciais e tokens               | Labs e exemplos práticos de uso seguro, quizzes de validação, clinics com AppSec        | `addon/04-tecnicas-formativas.md`, `addon/06-manual-formacao-por-capitulo.md` |

---

## 🔐 Categoria 2 - Acesso indevido ou onboarding negligente

| Ameaça                                         | Fonte                                                   | Como surge                                                                 | Como a prática mitiga                                                                 | Controlos associados                                          |
|------------------------------------------------|----------------------------------------------------------|------------------------------------------------------------------------------|----------------------------------------------------------------------------------------|--------------------------------------------------------------|
| Acesso técnico concedido sem validação         | SSDF PM.2 / ISO 27001 A.7.2.2 / CAPEC-233                | Colaboradores internos recebem acesso sem formação formal                   | Checklist de onboarding técnico + quiz obrigatório antes de permissões técnicas        | `addon/10-checklist-onboarding.md`, `addon/11-template-quiz-onboarding.md` |
| Inclusão de terceiros sem validação            | SSDF PM.3 / ISO A.13.2.4 / BSIMM T2.1                    | Fornecedores com acesso a ambientes ou código sem onboarding ou rastreio    | Inclusão formal com plano mínimo de formação, registo, rastreabilidade contratual      | `addon/20-modelo-inclusao-terceiros.md`, `addon/21-plano-formacao-terceiros.md` |

---

## 🧠 Categoria 3 - Cultura e motivação fraca para segurança

| Ameaça                                            | Fonte                                                          | Como surge                                                                 | Como a prática mitiga                                                           | Controlos associados                      |
|---------------------------------------------------|-----------------------------------------------------------------|------------------------------------------------------------------------------|----------------------------------------------------------------------------------|--------------------------------------------|
| Falta de ownership sobre segurança                | BSIMM SM1 / SAMM Governance / OSC&R (Developer Behavior)       | Segurança é vista como externa ou "responsabilidade do AppSec"             | Programa de Champions, responsabilização por domínio técnico, coaching contínuo | `addon/03-programa-champions.md`          |
| Regressão comportamental / cultura frágil         | NIST 800-50 / ENISA DevSecOps / BSIMM Culture                  | Formação pontual sem reforço, ausência de reforço comportamental           | Métricas, war rooms, CTFs, labs, reforço periódico e integração com SDLC        | `addon/04-tecnicas-formativas.md`, `addon/90-indicadores-metricas.md` |

---

## 📉 Categoria 4 - Falta de rastreabilidade e cobertura

| Ameaça                                             | Fonte                                              | Como surge                                                                 | Como a prática mitiga                                                       | Controlos associados                                      |
|----------------------------------------------------|-----------------------------------------------------|------------------------------------------------------------------------------|--------------------------------------------------------------------------------|------------------------------------------------------------|
| Formação não rastreável                            | ISO 27001 A.7.2.2 / SSDF PO.2.2 / BSIMM T1.3        | Não existe histórico de quem foi formado, quando, nem com que conteúdos     | Checklist com registo por pessoa, data, função e resultados de quizzes       | `addon/10-checklist-onboarding.md`, `addon/11-template-quiz-onboarding.md` |
| Formação desigual entre equipas ou funções         | CAPEC-233 / BSIMM T1.1 / T2.2                       | Umas equipas são formadas, outras não, sem critério ou controlo             | Trilho formativo padronizado por função e criticidade                        | `addon/02-trilho-formativo.md`, `addon/05-integracao-transversal.md`        |

---

## 🔗 Categoria 5 - Formação sem ligação à prática real

| Ameaça                                          | Fonte                                                      | Como surge                                                                 | Como a prática mitiga                                                           | Controlos associados                                         |
|-------------------------------------------------|-------------------------------------------------------------|------------------------------------------------------------------------------|----------------------------------------------------------------------------------|---------------------------------------------------------------|
| Formação teórica sem impacto prático            | BSIMM T2.1 / SAMM Edu / CAPEC-496 / OWASP Learning Path     | Sessões genéricas sem ligação a tarefas concretas ou à aplicação real       | Labs, war rooms, CTFs, revisão de PRs, threat modeling peer-led, clinics        | `addon/04-tecnicas-formativas.md`, `addon/06-manual-formacao-por-capitulo.md` |
| Conteúdos desatualizados ou não aplicáveis      | NIST 800-50 / SSDF PO.2.3 / ISO 27001 A.7                   | Formação desatualizada, sem lições aprendidas de incidentes ou revisões     | Atualizações contínuas ligadas a backlog, incidentes e métricas                | `addon/06-manual-formacao-por-capitulo.md`, `addon/07-exemplo1-manual-formacao-dev-pr-seguro.md` |

---

## ✅ Conclusão

As práticas definidas no Capítulo 13 **mitigam diretamente ou reduzem significativamente o impacto de pelo menos 12 ameaças críticas**, com origem em referências como:

- **CAPEC** (Common Attack Pattern Enumeration and Classification)
- **CWE** (Common Weakness Enumeration)
- **BSIMM** (Build Security In Maturity Model)
- **OWASP SAMM**
- **NIST 800-50 / SSDF v1.1**
- **ISO/IEC 27001**
- **OSC&R** (Open Software Supply Chain Attack Reference)

> 📌 Este capítulo é essencial para tratar a **componente humana e organizacional da segurança**, e serve como camada de reforço a todos os controlos técnicos descritos noutros capítulos.

> ⚠️ A ausência de práticas de formação contínua e onboarding seguro **aumenta o risco operacional, dificulta a rastreabilidade e compromete a eficácia de qualquer framework de segurança.**
