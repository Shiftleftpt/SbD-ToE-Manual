---
id: iast
title: Validação Interativa com Instrumentação (IAST)
description: Instrumentação da aplicação para observação em tempo real de vulnerabilidades durante a execução.
tags: [iast, testes interativos, instrumentação, runtime]
sidebar_position: 4
---


# 🔬 Testes Interativos de Segurança (IAST)

## 🌟 Objetivo

Aproveitar a execução normal da aplicação para realizar testes de segurança **com instrumentação ativa**, combinando:

- A precisão do SAST com o contexto real do DAST;
- A monitorização contínua de chamadas inseguras, uso indevido de bibliotecas, variáveis mal validadas e outros riscos;
- A geração de findings diretamente relacionados com o comportamento da aplicação em runtime;
- A melhoria da cobertura sem duplicar esforço de testes manuais ou automáticos.

> O IAST é ideal para validar segurança **sem esforço adicional de criação de casos de teste ou scanners dedicados**.

---

## 🔍 O que é IAST

IAST (Interactive Application Security Testing) é uma abordagem de testes de segurança que usa **instrumentação no servidor da aplicação** para observar chamadas, fluxos e execuções em tempo real - enquanto a aplicação é usada em testes funcionais, manuais ou automáticos.

Permite:

- Observar dados não sanitizados propagando-se até funções críticas;
- Verificar uso inseguro de bibliotecas ou APIs nativas;
- Detetar execuções vulneráveis em tempo real com visibilidade total do stack;
- Associar findings a utilizadores, chamadas, rotas e parâmetros concretos.

> 💡 O IAST requer integração com o runtime da aplicação, sendo mais fácil em stacks como Java, .NET, Python, Node.

---

## ⚙️ Como aplicar

1. **Selecionar ferramenta IAST compatível com o stack da aplicação**;
2. **Instrumentar o servidor de staging com agentes IAST** (ou containers configurados);
3. **Executar testes funcionais, manuais ou automáticos enquanto o IAST está ativo**;
4. **Analisar os findings gerados em contexto real - por fluxo, rota, user ID**;
5. **Triar os resultados e priorizar com base na execução e impacto**;
6. **Integrar resultados nos ciclos de melhoria contínua (ex: backlog de segurança)**.

> ⚠️ IAST não substitui DAST nem SAST - atua de forma complementar para maximizar visibilidade.

---

## ✅ Boas práticas

- Usar IAST em ambientes de staging ou teste integrado;
- Validar cobertura (ex: endpoints executados durante o teste);
- Priorizar findings com base em impacto real (executado vs potencial);
- Revisar permissões e impacto de performance da instrumentação;
- Usar IAST como observador passivo em testes de QA e integração.

---

## 📎 Referências cruzadas

| Documento                       | Relevância estratégica                      |
|--------------------------------|---------------------------------------------|
| Capítulo 02 - Requisitos       | Valida `REQ-203`, `REQ-307`, `REQ-404`      |
| Capítulo 06 - Desenvolvimento  | Observa violações em tempo real             |
| `01-sast.md`                   | IAST observa falhas que SAST só deteta estaticamente |
| `02-dast.md`                   | Complementa o DAST com visibilidade no backend |
| `06-cobertura-e-priorizacao.md`| Mede cobertura por execução real            |
| `08-gestao-findings.md`        | Findings do IAST são altamente rastreáveis  |

---

> 🧠 O IAST combina visibilidade de código com execução real - tornando os testes de segurança **mais relevantes, precisos e contextualizados**, sem dependência de falsos positivos ou suposições.
