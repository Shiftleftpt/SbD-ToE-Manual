---
id: intro
title: Testes de Segurança
description: Estratégias e práticas para validar continuamente a segurança de aplicações através de testes automatizados, manuais e ofensivos
tags: [testes, segurança, validação contínua, SAST, DAST, fuzzing, pentesting, DSOMM, SAMM, SSDF, SLSA]
sidebar_position: 0
---

:::tip Capítulo Operacional
Este capítulo é considerado **operacional** no modelo *Security by Design – Theory of Everything (SbD-ToE)*.  
A sua função é **aplicar, automatizar e validar** as práticas definidas nos capítulos basilares, garantindo a sua execução contínua e mensurável.

Os capítulos operacionais implementam o SbD-ToE em contextos técnicos específicos, traduzindo prescrições basilares em práticas de **execução verificável**, com **evidência objetiva, rastreável e auditável**.
:::

# Testes de Segurança

Os testes de segurança são o **ponto de viragem entre teoria e prática**.  
Requisitos podem ser bem definidos e controlos bem desenhados, mas só através de **testes contínuos e verificáveis** é possível demonstrar que funcionam perante código real, integrações complexas e ameaças em evolução.

Este capítulo distingue-se por fornecer **evidência objetiva e auditável**: confirma se as medidas prescritas nos capítulos anteriores são eficazes e se resistem à pressão do uso em produção.  
Inclui técnicas automatizadas (SAST, DAST, fuzzing, IAST) e validações manuais/ofensivas (PenTesting), criando uma rede complementar de garantias.

👉 Em síntese, os testes de segurança não são uma “fase” opcional — são o **mecanismo contínuo de validação** que sustenta decisões de *go/no-go* em cada commit, build e release.

---

## ⚖️ Princípios canónicos aplicáveis a testes de segurança

No contexto de testes de segurança, o SbD-ToE assume explicitamente que:

- Ferramentas **podem detetar, priorizar e correlacionar**,  
  mas **não tomam decisões finais**.
- Resultados automáticos **não constituem evidência suficiente por si só**.
- A decisão de *pass/fail*, aceitação de exceções ou risco residual é **sempre humana**, atribuída a um papel explícito.
- Um teste só “conta” quando produz **evidência verificável, reproduzível e auditável**.
- O próprio processo de teste introduz riscos (ex.: exposição de dados, credenciais, telemetria) que devem ser **explicitamente controlados**.

As regras prescritivas que operacionalizam estes princípios estão definidas no ficheiro  
`addon/10-evidencia-reprodutibilidade.md`.

---

## 🧪 Prescrição prática

A aplicação prática deve ser entendida como um **ciclo contínuo**, não como uma lista isolada de ferramentas:

- **O que fazer:**  
  Definir uma estratégia clara, automatizar o que for possível, testar em diferentes camadas (código, runtime, integrações) e completar com validação ofensiva em aplicações críticas.

- **Como fazer (proporcional ao risco):**  
  - **L1**: testes essenciais (SAST + checklist manual).  
  - **L2**: testes automatizados integrados (DAST, regressões, *gates*).  
  - **L3**: testes avançados (fuzzing sistemático, IAST, PenTesting pré-produção).

- **Quando aplicar:**  
  - Início de cada projeto (estratégia formal).  
  - Cada commit/PR (SAST).  
  - Builds CI/CD (SCA, IAST).  
  - Staging antes de *go-live* (DAST, fuzzing).  
  - Cada release (*gates* + aceitação formal de risco).  
  - Ciclos de auditoria e validação independente (PenTesting).

- **Porquê:**  
  Porque a validação é a única forma de garantir que segurança não é promessa, mas **realidade comprovada**.  
  Os testes sustentam decisões críticas e reduzem o tempo de exposição a vulnerabilidades.

---

## 👥 Papéis envolvidos

A responsabilidade pelos testes é **coletiva**, mas cada papel tem responsabilidades explícitas:

- **Dev** → corrige findings e cria regressões automáticas verificáveis.  
- **QA/Testes** → executa DAST, fuzzing e valida critérios de aceitação.  
- **AppSec** → define estratégia, afina regras e gere exceções e evidência.  
- **DevOps** → integra scanners, *gates* e preservação de artefactos no CI/CD.  
- **Gestão de Produto** → decide *go/no-go* e aprova risco residual documentado.  
- **PenTester** → conduz validações ofensivas e fornece evidência técnica independente.

👉 Estas responsabilidades são operacionalizadas através de histórias de utilizador no `aplicacao-lifecycle.md`.

---

## 📜 Políticas Organizacionais Relevantes

| Política | Obrigatória? | Aplicação | Conteúdo mínimo |
|--------|--------------|-----------|-----------------|
| Política de Estratégia de Testes | Sim | AppSec | Documento versionado com mapeamento Cap. 2 ⇄ testes |
| Política de SAST em PR | Sim | Dev + DevOps | Execução automática em PRs, thresholds L1–L3 |
| Política de DAST/Fuzzing | Recomendado | QA/Testes | DAST autenticado, fuzzing em endpoints críticos |
| Política de Gates CI/CD | Sim | DevOps + AppSec | Critérios formais, logs preservados, exceções registadas |
| Política de Release Seguro | Sim | Gestão + AppSec | Checklist de release e aceitação de risco documentada |
| Política de PenTesting | Recomendado (L2), Obrigatório (L3) | AppSec | Âmbito por risco, relatórios técnicos e retests |

Na versão impressa, consultar o **Anexo de Políticas Organizacionais do manual**.

---

## 🏁 Conclusão

Testar é o que transforma intenções de segurança em **evidência real**.  
É o mecanismo que confirma se requisitos foram implementados, se *gates* funcionam e se a aplicação resiste a ataques credíveis.

No SbD-ToE, testes de segurança são um **processo contínuo de validação auditável**, essencial para manter confiança técnica, governança e responsabilidade ao longo de todo o ciclo de vida.

---
