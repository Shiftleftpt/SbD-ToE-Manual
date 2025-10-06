---
id: boas-praticas-codigo
title: Boas Práticas de Escrita de Código Seguro
sidebar_position: 1
description: Recomendações para escrita de código seguro por linguagem e stack, incluindo padrões proibidos e boas práticas validadas
tags: [desenvolvimento, boas práticas, secure coding, requisitos, segurança]
---


# ✍️ Boas Práticas de Escrita de Código Seguro {desenvolvimento-seguro:addon:boas-praticas-codigo}

> 💡 **Nota prática**:  
> Muitas ferramentas de análise estática e linters modernos — como ESLint, Pylint, SonarQube, Checkmarx, Semgrep, entre outras — já incluem por omissão **regras de segurança essenciais** que cobrem várias das práticas aqui descritas.  
> Essas regras podem (e devem) ser **customizadas, auditadas e alinhadas com o contexto técnico da organização**.  
> A adoção destas ferramentas não dispensa a definição destas boas práticas, mas **facilita significativamente a sua verificação e operacionalização.**

---

Este documento estabelece o conjunto mínimo de boas práticas para a escrita de código seguro, que devem ser seguidas por todas as equipas de desenvolvimento e **validadas durante o processo de desenvolvimento, revisão e release**.

Estas práticas devem estar integradas nas guidelines técnicas da organização e nas rotinas de revisão de código.

---

## 📌 Objetivos {desenvolvimento-seguro:addon:boas-praticas-codigo#objetivos}

- Reduzir a introdução de vulnerabilidades comuns (ex: CWE Top 25)
- Aumentar a legibilidade, manutenibilidade e segurança do código
- Padronizar comportamentos entre equipas
- Integrar segurança desde o primeiro commit

---

## 👥 Quem deve aplicar {desenvolvimento-seguro:addon:boas-praticas-codigo#quem_deve_aplicar}

- **Desenvolvedores**: durante a escrita e refatoração do código.
- **Revisores técnicos** (peer reviewers, tech leads): durante a análise de PRs.
- **Equipas de segurança / AppSec**: como critério de validação transversal.

---

## ⏱️ Quando aplicar {desenvolvimento-seguro:addon:boas-praticas-codigo#quando_aplicar}

- Sempre que se inicia ou altera código-fonte de produção.
- Durante revisões técnicas de PRs.
- Em auditorias internas ou revisões de segurança.
- Durante o onboarding técnico de novos programadores.

---

## 🧱 Práticas essenciais {desenvolvimento-seguro:addon:boas-praticas-codigo#praticas_essenciais}

1. **Evitar cópia de código da internet sem validação**
   - Justificar e rever trechos copiados (StackOverflow, GitHub, etc.)
   - Validar segurança e licenciamento

2. **Separar lógica de negócio da lógica de apresentação**
   - Minimiza risco de injection (ex: XSS)
   - Melhora testabilidade e segurança por camada

3. **Evitar duplicação de código (DRY)**
   - Aumenta rastreabilidade
   - Reduz inconsistências de segurança

4. **Evitar uso de funções perigosas ou depreciadas**
   - Ex: `eval`, `exec`, `system`, `strcpy`, `innerHTML` sem sanitização
   - Substituir por alternativas seguras

5. **Usar nomes significativos e expressivos**
   - Aumenta compreensibilidade e reduz erros lógicos

6. **Manter comentários úteis e atualizados**
   - Comentários desatualizados induzem a erros críticos

7. **Eliminar código morto ou comentado antes de commits finais**
   - Código obsoleto é fonte frequente de falhas de segurança

---

## 🚨 Práticas proibidas {desenvolvimento-seguro:addon:boas-praticas-codigo#praticas_proibidas}

- Uso de *secrets* hardcoded (ex: tokens, passwords)
- Inclusão de *debug code* ou *console logging* em produção
- Acesso direto a `request` sem validação/sanitização
- Query strings construídas por concatenação
- Commit de dependências alteradas sem revisão formal

---

## ✅ Como validar {desenvolvimento-seguro:addon:boas-praticas-codigo#como_validar}

Estas práticas devem ser validadas através de:

- Checklists de revisão de código (ver `addon/08-validacoes-codigo.md`)
- Linters automáticos com regras mínimas obrigatórias (ver `addon/02-linters-validacoes.md`)
- PRs com reviewers obrigatórios e anotação semântica (ver `addon/09-anotacoes-evidencia.md`)

---

## 🧾 Como evidenciar {desenvolvimento-seguro:addon:boas-praticas-codigo#como_evidenciar}

A evidência da aplicação destas práticas pode ser:

- Presença de anotação no código (`@sec:checked`, `@sec:input-validated`)
- Validação explícita no template de PR
- Logs de execução de linters no CI/CD
- Inclusão no relatório de revisão técnica

---

## 🔄 Ligação a outras práticas {desenvolvimento-seguro:addon:boas-praticas-codigo#ligacao_a_outras_praticas}

| Tema                                 | Ficheiro associado         |
|--------------------------------------|----------------------------|
| Linters e validações automáticas     | `addon/02-linters-validacoes.md` |
| Gestão de dependências seguras       | `addon/03-seguranca-dependencias.md` |
| Revisões de código com checklist     | `addon/08-validacoes-codigo.md` |
| Rastreabilidade no código            | `addon/09-anotacoes-evidencia.md` |
| Justificação de exceções             | `addon/05-excecoes-e-justificacoes.md` |

---

> 📌 Esta prática é transversal e deve ser aplicada em todas as stacks técnicas e linguagens da organização.
> A sua ausência compromete a eficácia das validações automáticas e torna a base de código vulnerável a falhas triviais.
