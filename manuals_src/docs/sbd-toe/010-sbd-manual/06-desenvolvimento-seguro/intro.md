---
id: intro
title: Introdução - Desenvolvimento Seguro
description: Práticas de codificação segura, curadoria e seleção de guidelines, validação automatizada e governação durante o desenvolvimento
tags: [SAST, cat_basilar, desenvolvimento, governanca, grp_implementacao_automacao, guidelines de código, implementacao-automacao, linters, seguranca]
sidebar_position: 0
---

:::caution Capítulo Basilar
Este capítulo é considerado **basilar** no modelo *Security by Design - Theory of Everything (SbD-ToE)*.  
A sua aplicação é **obrigatória** para garantir a coerência, rastreabilidade e eficácia das restantes práticas de segurança.  

Os capítulos basilares constituem a **fundação técnica e metodológica** do modelo, a ausência ou aplicação parcial de qualquer um destes compromete a **integridade global** do SbD-ToE, tornando inviável a adoção coerente das práticas operacionais e de governação.
:::

# Desenvolvimento Seguro

O desenvolvimento é o **coração do ciclo de vida do software**.  
É aqui que se escreve o código que cria valor de negócio, mas também é aqui que podem nascer vulnerabilidades que acompanham o produto até produção.  
Por isso, este capítulo é considerado **basilar**: sem práticas consistentes de codificação segura, todos os controlos posteriores (CI/CD, testes, IaC ou containers) tornam-se apenas paliativos.

A evidência é clara: o **Verizon DBIR** e vários estudos académicos mostram que mais de um quarto das falhas exploradas têm origem em más práticas de programação.  
A boa notícia é que estas falhas podem ser prevenidas com medidas sistemáticas e auditáveis - desde guidelines claras e linters automatizados até revisões formais, governação de exceções e, mais recentemente, o **uso validado de GenIA**.  
O objetivo não é burocracia, mas criar um ambiente onde cada decisão de desenvolvimento deixa **evidência objetiva** de segurança aplicada.

---

## 🧭 O que cobre tecnicamente

Este capítulo abrange todas as práticas que tornam o desenvolvimento **seguro, rastreável e proporcional ao risco**:

- Curadoria e seleção de *guidelines* de código por stack, com governação organizacional
- Escrita de código seguro e uso de regras derivadas de linters/analisadores
- Validações automáticas locais e em pipelines (linters, SAST, perfis de qualidade)
- Gestão de dependências externas e internas com rastreabilidade (SBOM)
- Revisões de código formais com checklists de segurança
- Registo e governação de exceções técnicas
- Anotações semânticas de validações e decisões de segurança (`@sec:*`)
- Uso responsável e validado de GenIA no processo de desenvolvimento

> ℹ️ **Delegação para linters/analisadores**  
> As guidelines podem ser **derivadas e aplicadas via linters automáticos** (ex.: ESLint, Semgrep, Sonar, PSScriptAnalyzer), desde que as regras estejam **versionadas**, o ***tailoring*** documentado e exista **aprovação por Gestor Técnico + AppSec**.

---

## ⚙️ O que deve ser feito

Na prática, o que isto significa é que as equipas devem:

1. **Criar ou selecionar (*curar*) guidelines por stack**, publicando-as de forma versionada e auditável  
2. Usar **linters e *rulesets* organizacionais** com *tailoring* controlado e aprovado  
3. **Integrar ferramentas de validação de código** (SAST, Sonar, Semgrep) no pipeline  
4. **Validar dependências externas** e registá-las formalmente em SBOM  
5. **Gerir exceções técnicas** com mitigação, aprovação e prazo de validade  
6. **Rastrear decisões de segurança** via anotações padronizadas no código e testes  
7. **Aplicar checklists de segurança em PRs** para validação objetiva  
8. **Permitir GenIA**, mas sempre com revisão técnica e validação de licenças

Estas práticas não são opcionais: são o alicerce de confiança que suporta todo o SDLC.

---

## 👥 Quem está envolvido

| Papel/Função                | Responsabilidades principais |
|------------------------------|------------------------------|
| **Gestor Técnico / Lead**   | Curar guidelines, aprovar *rulesets* e rever periodicamente |
| **Equipa AppSec**           | Definir critérios mínimos, co-aprovar guidelines, validar exceções, mapear ASVS/CWE |
| **DevSecOps / CI/CD**       | Integrar linters e SAST no pipeline, versionar configs e aplicar *enforcement* |
| **Revisor Técnico**         | Aplicar checklist de segurança nos PRs e garantir conformidade |
| **Desenvolvedor**           | Aplicar guidelines, executar validações locais, propor ajustes de regras |

---

## ⏱️ Quando aplicar

O desenvolvimento seguro não se aplica apenas “no fim” do processo.  
Ele acompanha toda a linha temporal do projeto:

- Durante o **planeamento** (definição de stack, guidelines e dependências)  
- Ao **escrever ou refatorar código** (validações locais e linters)  
- Em cada **pull request** (checklists, revisões formais, validação de exceções)  
- Na **integração contínua** (SAST, enforcement de rulesets, SBOM)  
- Antes de um **go-live ou release** (validação de exceções e checklist final)  
- Em **operações e manutenção** (patching, atualização de dependências, revisão de guidelines)

---

## 🎯 Para quê

- Prevenir a introdução de vulnerabilidades ainda na fase de desenvolvimento  
- Reduzir o custo de correção através da deteção precoce  
- Assegurar rastreabilidade de decisões e exceções  
- Demonstrar conformidade em auditorias internas e externas  
- Sustentar métricas e KPIs de maturidade em segurança aplicacional  

No fundo, trata-se de transformar cada linha de código numa oportunidade de reforçar a confiança no produto.

---

## ⚖️ Proporcionalidade L1–L3

| Nível de risco | Exigência mínima |
|----------------|------------------|
| **L1 (baixo)** | Linters obrigatórios, checklist de PR, dependências justificadas |
| **L2 (médio)** | Guidelines curadas por stack, SAST obrigatório, exceções registadas |
| **L3 (alto)**  | Governação formal (revisão periódica), revisor dedicado, *policy-as-code* em CI/CD |

---

## 📜 Políticas Organizacionais Relevantes

| Política                                   | Obrigatória | Aplicação               | Conteúdo mínimo |
|-------------------------------------------|-------------|-------------------------|-----------------|
| **Política de Curadoria de Guidelines**   | Sim         | Todas as stacks         | Responsáveis, processo de seleção, *tailoring*, ciclos de revisão |
| **Política de Revisão de Código**         | Sim         | Todos os PRs críticos   | Checklist formal, reviewer designado, aprovação registada |
| **Política de Gestão de Exceções**        | Sim         | Todos os projetos       | Justificação, mitigação, prazo, aprovação dupla (em L3) |
| **Política de Uso de GenIA no Código**    | Sim         | Projetos com IA         | Anotação obrigatória, revisão técnica, validação de licenças |

Na versão impressa, as políticas relevantes incluem: **Curadoria de Guidelines**, **Revisão de Código**, **Gestão de Exceções** e **Uso de GenIA** no desenvolvimento.

---
