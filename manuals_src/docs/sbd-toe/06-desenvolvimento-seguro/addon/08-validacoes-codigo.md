---
id: validacoes-codigo
title: Validações de Segurança no Código
sidebar_position: 8
description: Técnicas e ferramentas para garantir a presença de controlos de segurança diretamente no código-fonte
tags: [validação, código, segurança, automação, integração contínua]
---


# 🔍 Validações de Segurança no Código {desenvolvimento-seguro:addon:validacoes-codigo}

> 💡 **Nota prática**:  
> Ferramentas como **SonarQube**, **Checkmarx**, **Kiuwan**, **Semgrep**, **Xygeni**, **Fortify** e outras permitem executar validações de segurança diretamente no código, durante o desenvolvimento, nos PRs ou em pipelines CI/CD.  
> Estas validações automatizadas são complementares à revisão humana e devem ser **configuradas com critérios mínimos obrigatórios por projeto**.  
> A sua eficácia depende da **integração com práticas de revisão, onboarding técnico e controlo de exceções**.

---

## 📌 Objetivos {desenvolvimento-seguro:addon:validacoes-codigo#objetivos}

- Identificar vulnerabilidades no código-fonte antes da entrega.
- Automatizar verificações repetitivas e detetar falhas triviais de forma consistente.
- Suportar o processo de revisão com critérios objetivos e rastreáveis.
- Aumentar a maturidade da equipa na deteção e resposta a problemas de segurança.

---

## 👥 Quem deve aplicar {desenvolvimento-seguro:addon:validacoes-codigo#quem_deve_aplicar}

- **Desenvolvedores**: ao escrever e validar código localmente.
- **Revisores técnicos**: ao aprovar código e releases.
- **Equipa de segurança**: ao definir regras, métricas e severidade.

---

## ⏱️ Quando aplicar {desenvolvimento-seguro:addon:validacoes-codigo#quando_aplicar}

- Durante o desenvolvimento (localmente ou via IDE)
- Ao submeter um pull request
- Antes de cada release (via CI/CD)
- Em auditorias internas ou entregas certificadas

---

## 🧱 Requisitos obrigatórios {desenvolvimento-seguro:addon:validacoes-codigo#requisitos_obrigatorios}

1. **Validações automáticas obrigatórias com ferramentas SAST**
   - Devem executar em cada PR ou commit.
   - O resultado deve ser visível e rastreável.

2. **Bloqueio por falhas críticas ou não justificadas**
   - CWE de alta severidade devem impedir merge sem exceção aprovada.

3. **Integração com templates de PR**
   - Indicar se validação foi executada, qual ferramenta usada, e se existem findings pendentes.

4. **Definição de critérios mínimos por severidade**
   - Ex: rejeitar código com findings "High", permitir "Low" com anotação.

5. **Rastreabilidade de findings corrigidos, aceites ou justificados**
   - Findings devem ter justificativa ou estado claro (aceite, falso positivo, mitigado).

---

## ✅ Como validar {desenvolvimento-seguro:addon:validacoes-codigo#como_validar}

- Relatórios gerados automaticamente no CI/CD ou nos PRs.
- Checklists de revisão com referência a findings e sua resolução.
- Marcação explícita em ficheiros afetados ou comentários no PR.
- Links para evidência do scan (ex: output de Semgrep, relatório Kiuwan, painel SonarQube).

---

## 🧾 Como evidenciar {desenvolvimento-seguro:addon:validacoes-codigo#como_evidenciar}

- Logs arquivados das ferramentas de SAST/SCA.
- Anotação no PR com findings + resolução.
- Relatório por release com métricas de findings críticos resolvidos vs. justificados.
- Scripts de verificação usados nos pipelines versionados.

---

## 🔄 Ligação a outras práticas {desenvolvimento-seguro:addon:validacoes-codigo#ligacao_a_outras_praticas}

| Tema                                | Ficheiro associado               |
|-------------------------------------|----------------------------------|
| Linters e validações locais         | `addon/02-linters-validacoes.md` |
| Justificação de exceções            | `addon/05-excecoes-e-justificacoes.md` |
| Rastreabilidade e evidência         | `addon/09-anotacoes-evidencia.md` |
| Guidelines de equipa                | `addon/07-guidelines-equipa.md` |

---

> 📌 A validação automatizada do código é um dos pilares de maturidade técnica em desenvolvimento seguro.  
> Deve ser tratada como uma etapa obrigatória do SDLC, com critérios claros, evidência objetiva e integração com processos de revisão.
