---
id: integracao-pipeline
title: Integração de Testes no Pipeline
description: Execução automatizada de testes de segurança como parte de pipelines CI/CD, com rastreabilidade e thresholds.
tags: [integração contínua, pipelines, rastreabilidade, seguranca, testes]
sidebar_position: 8
---


# 🛠️ Integração dos Testes de Segurança no Pipeline CI/CD

## 🌟 Objetivo

Assegurar que os testes de segurança são **executados automaticamente e com critérios bem definidos** em todos os pipelines de CI/CD relevantes, garantindo:

- Detecção precoce de falhas e bloqueio de builds quando necessário;
- Rastreabilidade entre resultados, artefactos e commits;
- Reforço da cultura de segurança como parte do processo de entrega;
- Cumprimento de requisitos regulatórios e internos sem depender de ações manuais.

> A segurança que não está integrada no pipeline é invisível - e portanto, ineficaz.

---

## 🔍 O que significa “integrar testes no pipeline”

Integrar testes no pipeline significa **automatizar a execução dos testes de segurança como parte do processo de build, validação, release ou deploy**. Pode incluir:

- Execução de SAST, SCA, DAST, fuzzing, regressões e linters;
- Geração de SBOMs e análise de cobertura de segurança;
- Validações de findings, thresholds e gates por severidade;
- Produção de artefactos rastreáveis com evidência de validação.

---

## ⚙️ Como aplicar

1. **Mapear estágios do pipeline onde cada tipo de teste deve ocorrer**:
   - Pré-build (linters, SBOM);
   - Build (SAST, SCA);
   - Staging (DAST, IAST, fuzzing);
   - Release (validação final e regressões);
2. **Criar jobs específicos para segurança, com output visível e versionado**;
3. **Definir gates e critérios de bloqueio por severidade, tipo de falha ou ausência de validação**;
4. **Incluir metadados nos artefactos de build** (ex: commit, ambiente, tool version, hash);
5. **Garantir isolamento dos ambientes de teste**, especialmente para fuzzing e DAST;
6. **Executar testes de segurança em paralelo, sem impactar tempo total de entrega**.

> 💡 Testes como SAST e regressão podem ser bloqueantes; testes como DAST e fuzzing podem ser informativos em pipelines assíncronos.

---

## ✅ Boas práticas

- Criar pipelines dedicados a segurança, quando possível (ex: nightly ou pós-release);
- Manter histórico de execuções e resultados por commit, branch e release;
- Integrar findings com backlog ou sistema de triagem (Jira, Azure Boards);
- Garantir que ferramentas estão versionadas e controladas como dependências;
- Validar a cobertura e frequência real dos testes no pipeline (não apenas presença dos jobs);
- Envolver equipas DevOps na orquestração e manutenção contínua.

---

## 📎 Referências cruzadas

| Documento                       | Relevância estratégica                          |
|--------------------------------|--------------------------------------------------|
| Capítulo 07 - CI/CD Seguro     | Condições de execução segura e segregação       |
| `01-sast.md`, `02-dast.md`     | Tipos de teste que devem ser automatizados       |
| `06-cobertura-e-priorizacao.md`| Define o quê, quando e como testar no pipeline   |
| `08-gestao-findings.md`        | Garante tratamento eficaz dos resultados         |
| Capítulo 12 - Monitorização    | Rastreio de falhas de segurança em runtime       |

---

> 📦 A integração dos testes no pipeline transforma segurança numa **atividade contínua, auditável e verificável** - em vez de uma checklist pontual antes da entrega.
