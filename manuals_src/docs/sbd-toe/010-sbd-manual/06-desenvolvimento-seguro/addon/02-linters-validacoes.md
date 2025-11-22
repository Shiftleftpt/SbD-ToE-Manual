---
id: linters-validacoes
title: Linters e Validações Locais de Segurança
sidebar_position: 2
description: Regras e ferramentas para validação de segurança diretamente no ambiente de desenvolvimento (pre-commit, IDE, CLI)
tags: [IDE, automação, linters, pre-commit, seguranca, validacao]
---

# 🧪 Linters e Validações Locais de Segurança

> 💡 **Nota prática**:  
> A maior parte das linguagens e frameworks modernas já possui **linters e validadores configuráveis** (como ESLint, Pylint, RuboCop, etc.), muitos dos quais incluem **regras básicas de segurança por omissão**.  
> Ferramentas como **Semgrep**, **SonarLint** ou IDEs como VSCode e IntelliJ também permitem aplicar políticas personalizadas.  
> A sua adoção permite reforçar a segurança ainda antes do commit e evita a propagação de más práticas para o repositório principal.

---

## 📌 Objetivos

- Garantir que erros comuns e más práticas são detetados antes da submissão de código.
- Aumentar a consistência e qualidade técnica do código produzido.
- Automatizar validações de segurança, reduzindo dependência exclusiva de revisão humana.
- Estabelecer critérios mínimos auditáveis de validação antes de integrar alterações no repositório.

---

Este documento define os requisitos mínimos de **validação local e linting de segurança** que devem estar presentes em qualquer projeto ativo.

A aplicação consistente destas validações **reduz significativamente a introdução de erros triviais de segurança** e melhora a rastreabilidade das correções.

---

## 👥 Quem deve aplicar

- **Todos os programadores** durante a escrita de código.
- **Responsáveis técnicos** ao configurar o repositório e pipelines.
- **Revisores de PRs**, garantindo que os linters foram executados e aprovados.

---

## ⏱️ Quando aplicar

- Antes de qualquer commit ou push.
- No momento da criação do PR (via hook ou pipeline).
- Durante revisões técnicas.
- Periodicamente, como parte de tarefas de manutenção.

---

## 🧱 Requisitos mínimos

1. **Execução local obrigatória de linters com regras mínimas de segurança**
   - Deve fazer parte do fluxo de desenvolvimento
   - Ex: ESLint com plugin `eslint-plugin-security`, Bandit para Python

2. **Validação integrada no PR via CI/CD**
   - O pipeline deve bloquear merges em caso de falhas críticas
   - Regras devem ser visíveis e justificáveis

3. **Regras alinhadas com as guidelines internas de codificação segura**
   - Linters devem reforçar o que está definido em `addon/01-boas-praticas-codigo.md`

4. **Configuração versionada e auditável**
   - Os ficheiros `.eslintrc`, `.pylintrc`, `.semgrep.yml`, etc., devem estar no repositório
   - Atualizações devem ser rastreadas e justificadas

---

## 🚨 Falhas comuns detetáveis com linters

- Uso de `eval`, `exec`, `innerHTML` sem escaping
- Falta de verificação de parâmetros obrigatórios
- Inclusão de código morto, comentários sensíveis ou debugging
- Instâncias de vulnerabilidades conhecidas (por CWE) com autofix

---

## ✅ Como validar

- Execução local antes do commit (`pre-commit`, `make lint`, etc.)
- Execução automática nos pipelines de build ou PR
- Presença de relatórios ou logs no PR
- Integração com IDE e alertas visíveis durante o desenvolvimento

---

## 🧾 Como evidenciar

- Logs da pipeline com execução dos linters
- Screenshot ou output integrado no PR
- Ficheiros de configuração de linters versionados
- Marcação de validação no template de PR (`[x] Linter executado e sem falhas`)

---

## 🔄 Ligação a outras práticas

| Tema                                | Ficheiro associado               |
|-------------------------------------|----------------------------------|
| Guidelines de desenvolvimento seguro | `addon/01-boas-praticas-codigo.md` |
| Validações no pipeline CI/CD        | `addon/08-validacoes-codigo.md` |
| Justificação de exceções            | `addon/05-excecoes-e-justificacoes.md` |
| Anotação de validações              | `addon/09-anotacoes-evidencia.md` |

---

> 📌 A ausência de linting ou a sua execução opcional é um dos sinais mais claros de baixa maturidade técnica e de risco latente.  
> Estas práticas devem ser **obrigatórias, verificadas e auditáveis por projeto**.
