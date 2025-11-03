---
id: dast
title: Validação Dinâmica de Aplicações (DAST)
description: Testes dinâmicos em runtime para deteção de vulnerabilidades através da simulação de interações externas.
tags: [dast, testes dinâmicos, runtime, segurança]
sidebar_position: 3
---


# 🌐 Testes Dinâmicos de Segurança (DAST)

## 🌟 Objetivo

Detetar vulnerabilidades em aplicações **durante a sua execução**, simulando o comportamento de um utilizador ou atacante, com o objetivo de:

- Identificar falhas que não são visíveis no código (ex: injeções, bypass de autenticação);
- Validar a configuração real do ambiente (ex: headers, permissões, exposição de serviços);
- Testar fluxos e interações completas com a aplicação em funcionamento;
- Complementar os testes estáticos (SAST) com visibilidade runtime.

> DAST é essencial para testar aquilo que só se revela com a aplicação em funcionamento real.

---

## 🔍 O que é DAST

DAST (Dynamic Application Security Testing) consiste em executar testes automáticos de segurança **sobre uma aplicação em funcionamento** (geralmente em staging ou ambientes controlados), simulando comportamentos externos maliciosos ou errados.

Pode incluir:

- Ataques de injeção (SQLi, XSS, command injection);
- Manipulação de sessões, cookies e autenticação;
- Exploração de endpoints ou APIs públicas;
- Verificação de headers de segurança (ex: CSP, HSTS, CORS);
- Testes a workflows multi-etapa.

> ⚠️ DAST exige ambiente executável e autenticação configurada para simular utilizadores reais.

---

## ⚙️ Como aplicar

1. **Preparar ambiente isolado de staging ou pré-produção**, com dados controlados;
2. **Selecionar scanner DAST adequado ao tipo de aplicação** (web, API, mobile);
3. **Configurar autenticação, escopo e crawling adequado**;
4. **Executar scans regulares por versão ou por release**;
5. **Rever findings manualmente antes de acionar ações de correção**;
6. **Integrar resultados no backlog, com rastreabilidade por artefacto ou release**.

> 💡 Sugestão: definir perfis de scan distintos por tipo de aplicação (ex: portal vs API REST).

---

## ✅ Boas práticas

- Automatizar execução de DAST no pipeline, mas fora da linha crítica (ex: ambiente de validação);
- Usar dados fictícios ou mascarados;
- Evitar testes destrutivos em ambientes partilhados;
- Configurar tempos de espera, autenticação multi-utilizador e fallback de sessão;
- Revisar escopos de scan após mudanças de arquitetura ou rotas;
- Incluir APIs e pontos de integração externos.

---

## 📎 Referências cruzadas

| Documento                       | Relevância estratégica                     |
|--------------------------------|--------------------------------------------|
| Capítulo 02 — Requisitos       | Valida `REQ-208`, `REQ-310`, `REQ-405`     |
| Capítulo 07 — CI/CD Seguro     | Integração com pipelines paralelos         |
| `04-fuzzing.md`                | Complementa validação dinâmica com aleatoriedade |
| `06-cobertura-e-priorizacao.md`| Define criticidade de endpoints a testar   |
| `08-gestao-findings.md`        | Gestão dos resultados e follow-up          |
| `09-feedback-equipa.md`        | Envolvimento das equipas de QA e DevOps    |

---

> 🔍 O DAST vê o que o código oculta: falhas de integração, respostas inesperadas e riscos decorrentes do ambiente real de execução. É a lente externa para a segurança da aplicação.
