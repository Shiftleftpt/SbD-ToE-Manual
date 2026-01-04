---
id: intro
title: Introdução – Desenvolvimento Seguro
description: Práticas de codificação segura, curadoria e seleção de guidelines, validação automatizada e governação durante o desenvolvimento
tags: [desenvolvimento, segurança, guidelines de código, linters, SAST, governação]
sidebar_position: 0
---

:::tip Capítulo Operacional
Este capítulo é considerado **operacional** no modelo *Security by Design – Theory of Everything (SbD-ToE)*.  
A sua função é **aplicar, operacionalizar e validar** as práticas definidas nos capítulos basilares, garantindo a sua execução contínua, consistente e mensurável.

Os capítulos operacionais traduzem as prescrições fundacionais do SbD-ToE em práticas de **execução verificável**, assegurando que a segurança não depende de intenções individuais, mas de mecanismos sistemáticos integrados no ciclo de vida do software.
:::

# Desenvolvimento Seguro

O desenvolvimento é o **coração do ciclo de vida do software**.  
É neste ponto que o valor de negócio se materializa em código executável — e é também aqui que decisões técnicas aparentemente menores podem introduzir vulnerabilidades com impacto duradouro.

Por esse motivo, este capítulo assume um papel **estrutural** no manual: sem práticas consistentes de desenvolvimento seguro, todos os controlos posteriores (CI/CD, testes, IaC, containers ou operações) passam a atuar apenas de forma corretiva ou paliativa.

A evidência empírica é clara. Relatórios como o **Verizon DBIR**, bem como múltiplos estudos académicos e industriais, mostram de forma consistente que uma parte significativa das falhas exploradas tem origem em **más práticas de programação, validação insuficiente ou decisões técnicas não controladas** durante o desenvolvimento.

A boa notícia é que estas falhas são, em grande medida, **preveníveis**.  
Através de práticas sistemáticas e auditáveis — como guidelines claras, validações automatizadas, revisões formais, governação de exceções e o uso responsável de ferramentas de apoio ao desenvolvimento — é possível reduzir drasticamente a superfície de erro introduzida nesta fase.

Num contexto de utilização crescente de ferramentas avançadas de apoio ao desenvolvimento, este capítulo assume explicitamente que **a origem do código — humana ou automatizada — é irrelevante do ponto de vista do risco**, sendo sempre necessária validação técnica adequada, evidência verificável e responsabilização clara pelas decisões de incorporação.

O objetivo deste capítulo não é acrescentar burocracia, mas **estabelecer um ambiente onde cada decisão de desenvolvimento deixa evidência objetiva de segurança aplicada**, proporcional ao risco e rastreável ao longo do tempo.

---

## 🧭 O que cobre tecnicamente

Este capítulo abrange todas as práticas que tornam o desenvolvimento **seguro, rastreável e proporcional ao risco**, desde a definição de regras até à sua aplicação contínua:

- Curadoria e seleção de *guidelines* de código por stack, com governação organizacional explícita  
- Escrita de código seguro e aplicação sistemática de regras derivadas de linters e analisadores  
- Validações automáticas locais e em pipelines (linters, SAST, perfis de qualidade)  
- Gestão de dependências externas e internas com rastreabilidade (incluindo SBOM)  
- Revisões de código formais suportadas por checklists de segurança  
- Registo, justificação e governação de exceções técnicas  
- Anotações semânticas de validações e decisões de segurança (`@sec:*`)  
- Uso responsável de ferramentas avançadas de apoio ao desenvolvimento, **sob constrangimentos técnicos explícitos**, sempre sujeito a validação técnica, revisão humana e responsabilização formal

> ℹ️ **Delegação controlada para linters e analisadores**  
> As guidelines podem ser **derivadas, codificadas e aplicadas através de linters automáticos** (ex.: ESLint, Semgrep, Sonar, PSScriptAnalyzer), desde que as regras estejam **versionadas**, o *tailoring* seja explicitamente documentado e exista **aprovação formal por Gestor Técnico e AppSec**.  
> A automação reforça a consistência, mas não substitui responsabilidade.

---

## ⚙️ O que deve ser feito

Na prática, o desenvolvimento seguro implica que as equipas:

1. **Criem ou selecionem (*curem*) guidelines por stack**, publicando-as de forma versionada, acessível e auditável  
2. Utilizem **linters e *rulesets* organizacionais**, com *tailoring* controlado e aprovado  
3. **Integram ferramentas de validação de código** (ex.: SAST) nos pipelines de integração contínua  
4. **Validem e registem dependências externas**, assegurando rastreabilidade e justificação formal  
5. **Gerem exceções técnicas** com mitigação definida, aprovação explícita e prazo de validade  
6. **Rastreiem decisões de segurança** através de anotações padronizadas no código e nos testes  
7. **Apliquem checklists de segurança em pull requests**, assegurando validação objetiva  
8. **Utilizem ferramentas avançadas de apoio ao desenvolvimento apenas com revisão técnica, validação de licenças e compreensão do código incorporado**

Sempre que ferramentas de apoio ao desenvolvimento sejam utilizadas, as equipas devem assegurar que o código produzido **respeita os constrangimentos técnicos e de segurança definidos para o projeto**, independentemente da sua origem.  
Estes constrangimentos devem ser explícitos, versionados e verificáveis, constituindo parte integrante do modelo de governação do desenvolvimento seguro.

Estas práticas não são opcionais. Constituem o **alicerce de confiança** que suporta todo o SDLC.

---

## 👥 Quem está envolvido

| Papel / Função              | Responsabilidades principais |
|----------------------------|------------------------------|
| **Gestor Técnico / Lead**  | Curar guidelines, aprovar *rulesets* e rever periodicamente a sua adequação |
| **Equipa AppSec**          | Definir critérios mínimos, co-aprovar guidelines, validar exceções e mapear CWE/ASVS |
| **DevSecOps / CI/CD**      | Integrar validações no pipeline, versionar configurações e aplicar *enforcement* |
| **Revisor Técnico**        | Aplicar checklists de segurança nos PRs e garantir conformidade |
| **Desenvolvedor**          | Aplicar guidelines, executar validações locais e propor melhorias |

---

## ⏱️ Quando aplicar

O desenvolvimento seguro não é uma atividade pontual nem confinada ao final do processo.  
Aplica-se de forma contínua:

- Durante o **planeamento** (seleção de stack, guidelines e dependências)  
- Ao **escrever ou refatorar código** (validações locais e análise estática)  
- Em cada **pull request** (revisões formais, checklists e validação de exceções)  
- Na **integração contínua** (enforcement de regras e análise automatizada)  
- Antes de um **go-live ou release** (validação final e revisão de exceções)  
- Em **manutenção e operação** (patching, atualização de dependências e revisão periódica de guidelines)

---

## 🎯 Para quê

- Prevenir vulnerabilidades na origem  
- Reduzir drasticamente o custo de correção através da deteção precoce  
- Assegurar rastreabilidade de decisões técnicas e exceções  
- Demonstrar conformidade em auditorias internas e externas  
- Sustentar métricas e KPIs de maturidade em segurança aplicacional  

Em última análise, trata-se de transformar **cada linha de código** numa oportunidade de reforçar a confiança no produto.

---

## ⚖️ Proporcionalidade L1–L3

| Nível de risco | Exigência mínima |
|----------------|------------------|
| **L1 (baixo)** | Linters obrigatórios, checklist de PR, dependências justificadas |
| **L2 (médio)** | Guidelines curadas por stack, SAST obrigatório, exceções registadas |
| **L3 (alto)**  | Governação formal, revisor dedicado, *policy-as-code* em CI/CD |

---

## 📜 Políticas Organizacionais Relevantes

| Política                                   | Obrigatória | Aplicação             | Conteúdo mínimo |
|-------------------------------------------|-------------|-----------------------|-----------------|
| **Política de Curadoria de Guidelines**   | Sim         | Todas as stacks       | Responsáveis, processo de seleção, *tailoring*, ciclos de revisão |
| **Política de Revisão de Código**         | Sim         | PRs relevantes        | Checklist formal, reviewer designado, aprovação registada |
| **Política de Gestão de Exceções**        | Sim         | Todos os projetos     | Justificação, mitigação, prazo e aprovação proporcional ao risco |
| **Política de Uso de Ferramentas de Apoio ao Desenvolvimento** | Sim | Projetos aplicáveis | Regras de uso, revisão técnica, validação legal e responsabilidade |

Na versão impressa, as políticas relevantes incluem: **Curadoria de Guidelines**, **Revisão de Código**, **Gestão de Exceções** e **Uso controlado de ferramentas de apoio ao desenvolvimento**.

---
