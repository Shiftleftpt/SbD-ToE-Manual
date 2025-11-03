---
id: validacao-regressao
title: Testes de Regressão de Segurança
description: Validação recorrente de vulnerabilidades previamente corrigidas para evitar reintroduções em versões futuras.
tags: [regressão, testes, segurança, validação contínua]
sidebar_position: 6
---


# 🔁 Validação de Regressões de Segurança

## 🌟 Objetivo

Assegurar que **vulnerabilidades previamente corrigidas não voltam a ser introduzidas** no código ao longo da evolução da aplicação, através de mecanismos sistemáticos de **validação regressiva de segurança**, incluindo:

- Reexecução automatizada de testes sobre findings resolvidos;
- Criação de casos de teste de segurança a partir de falhas reais;
- Integração no ciclo de qualidade contínua (regressão funcional + segurança);
- Rastreabilidade entre findings históricos e builds futuros.

> ⚠️ Uma regressão de segurança representa um **retrocesso evitável** — normalmente por falta de memória organizacional ou automação.

---

## 🔍 O que é validação de regressões

Validação regressiva de segurança consiste em **detetar reintroduções acidentais de vulnerabilidades conhecidas**, previamente corrigidas, mas que retornam ao código por refatoração, fusão de branches ou repetição de erros.

Formas comuns:

- **Reexecução de SAST com baseline de findings anteriores**;
- **Casos de teste manuais ou automatizados com payloads de exploits anteriores**;
- **Monitorização por hash/signature de trechos vulneráveis reintroduzidos**;
- **Blocos de CI dedicados a validação de regressões críticas**.

---

## ⚙️ Como aplicar

1. **Manter histórico de findings resolvidos**, com detalhes técnicos e commit associado;
2. **Automatizar verificação da sua ausência** em builds futuros (ex: via hash, regra SAST);
3. **Criar testes específicos de segurança** para falhas relevantes (ex: payloads de bypass anteriores);
4. **Integrar regressões de segurança na matriz de regressão funcional da equipa QA**;
5. **Usar tags ou anotações nos testes** para identificar quais são regressivos e de segurança;
6. **Reportar sempre que uma falha reaparece — com alerta explícito ao owner do módulo**.

> 💡 Sugestão: manter pasta `/tests/security-regression/` no repositório com casos de teste versionados.

---

## ✅ Boas práticas

- Reter todos os findings com status “Resolvido” e respetivo commit de correção;
- Automatizar regressões como parte do pipeline de PR;
- Criar alertas para findings que reaparecem em builds posteriores;
- Validar regressões especialmente em código partilhado ou legado;
- Incluir verificação de regressões no critério de aceitação de releases L2/L3;
- Promover cultura de "zero regressões conhecidas" como prática de maturidade.

---

## 📎 Referências cruzadas

| Documento                         | Relevância estratégica                        |
|----------------------------------|------------------------------------------------|
| Capítulo 02 — Requisitos         | Valida requisitos com histórico de findings    |
| `01-sast.md`                     | Findings do SAST podem ser base para regressão |
| `08-gestao-findings.md`          | Mantém histórico e estado das vulnerabilidades |
| `06-cobertura-e-priorizacao.md` | Ajuda a priorizar áreas com maior risco de regressão |
| Capítulo 07 — CI/CD Seguro       | Integração de regressões como jobs do pipeline |

---

> 📉 A validação regressiva protege o investimento feito na correção de falhas — e impede que vulnerabilidades antigas voltem a assombrar a segurança de novas versões.
