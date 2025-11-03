---
id: excecoes-e-justificacoes
title: Justificação Formal de Exceções
sidebar_position: 5
description: Mecanismos formais para registar, aprovar e controlar exceções às regras de segurança durante o desenvolvimento
tags: [exceções, validação, rastreabilidade, segurança, risco]
---

# 📝 Justificação Formal de Exceções

> 💡 **Nota prática**:  
> Em qualquer equipa ou projeto, haverá situações onde **nem todas as práticas recomendadas podem ser cumpridas** — por motivos técnicos, contextuais ou de legado.  
> Ferramentas como **Kiuwan**, **SonarQube**, **Xygeni**, **Checkmarx** ou **Semgrep** já permitem registar exceções diretamente no relatório de findings, usando mecanismos como `mute`, `waive`, `false positive accepted`, ou comentários inline com anotação.  
> Estas marcações são úteis, mas **não dispensam uma política clara de aprovação, justificação e rastreabilidade** — que deve ser transversal ao pipeline e ao repositório.

---

## 📌 Objetivos

- Evitar a aplicação informal ou silenciosa de práticas inseguras.
- Fornecer uma estrutura clara para aprovar, justificar e mitigar exceções.
- Garantir que exceções não se tornam permanentes ou invisíveis.
- Rastrear decisões de risco e assegurar responsabilização.
- Integrar as exceções nos fluxos de revisão, CI/CD e auditoria.
---

## 👥 Quem deve aplicar

- **Equipa de desenvolvimento**: quando identifica a necessidade de exceção.
- **Responsáveis técnicos (TLs, arquitetos)**: ao rever a proposta.
- **Equipa de segurança / AppSec**: responsável pela aprovação formal.

---

## ⏱️ Quando aplicar

- Quando uma prática obrigatória não pode ser seguida por motivos justificados.
- Antes da aceitação de código com potenciais desvios críticos.
- Sempre que um PR introduz uma violação conhecida das guidelines.
- Periodicamente, para rever exceções já aceites.

---

## 🧱 Requisitos mínimos

1. **Documentar a exceção num registo rastreável**
   - Inclui descrição, motivo, impacto e risco identificado.

2. **Justificar tecnicamente com base em contexto e restrições**
   - Ex: limitações de framework, retrocompatibilidade, dependência externa.

3. **Propor mitigação proporcional**
   - Ex: testes adicionais, monitorização, plano de refatoração.

4. **Submeter para aprovação formal**
   - Deve ser avaliado por segurança ou owner técnico autorizado.

5. **Definir validade temporal ou condição de revisão**
   - A exceção não deve ser indefinida sem reavaliação.

---

## ✅ Como validar

- PR com link para o registo de exceção (issue, ficheiro, anotação).
- Aprovação explícita por parte do revisor técnico ou AppSec.
- Presença de comentário `@sec:justificado` no código afetado.
- Registo incluído em artefactos de release ou auditoria.

---

## 🧾 Como evidenciar

- Ficheiro `excecoes-aprovadas.yml` versionado no repositório.
- Issue/documento de exceção referenciado no PR ou merge commit.
- Anotação explícita no código com referência a exceção aprovada.
- Relatórios de segurança com mapeamento de exceções pendentes/revistas.

---

## 🔄 Ligação a outras práticas

| Tema                                    | Ficheiro associado               |
|-----------------------------------------|----------------------------------|
| Guidelines e práticas obrigatórias      | `addon/01-boas-praticas-codigo.md` |
| Validação via linters                   | `addon/02-linters-validacoes.md` |
| Validação de dependências               | `addon/03-seguranca-dependencias.md` |
| Revisão de código e bloqueios em PRs    | `addon/08-validacoes-codigo.md` |
| Evidência e tagging                     | `addon/09-anotacoes-evidencia.md` |

---

> 📌 A gestão formal de exceções **não é um desvio da segurança**, mas uma forma madura de lidar com restrições reais.  
> A ausência de registo e justificação transforma exceções técnicas em falhas organizacionais.
