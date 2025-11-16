---
id: exemplo-manual-dev-pr
title: Exemplo de Manual de Formação - Pull Request Seguro
description: Exemplo concreto de manual formativo para desenvolvedores sobre práticas seguras em PRs.
tags: [exemplo, formacao, pull request, dev, aplicacao]
---


# 🛠️ Módulo Formativo - Pull Request Seguro

## 🎯 Objetivo

Capacitar developers para:

- Escrever Pull Requests com critérios mínimos de segurança aplicados
- Identificar más práticas em código submetido por colegas
- Justificar decisões de segurança diretamente no PR

---

## 📋 Pré-requisitos

- Experiência básica com Git e fluxo de Pull Request
- Participação prévia em pelo menos 1 sprint ativa
- Conhecimento dos padrões internos de código (naming, logging, validações)

---

## 🧪 Formato da sessão

| Bloco              | Duração | Objetivo                                                                 |
|-------------------|---------|--------------------------------------------------------------------------|
| Introdução         | 5 min   | Enquadrar a importância do PR seguro para o ciclo de desenvolvimento    |
| Exemplo positivo   | 10 min  | Rever um PR real ou simulado com boas práticas                          |
| Exemplo com falhas | 15 min  | Identificar más práticas, omissões e falhas de validação                 |
| Revisão guiada     | 10 min  | Aplicar checklist e redigir comentários de melhoria                      |
| Quiz ou validação  | 10 min  | 5 perguntas ou desafio rápido de consolidação                            |

> 💡 A sessão pode ser síncrona (formação, peer-review em grupo) ou assíncrona (exercício em tempo próprio com revisão posterior).

---

## 📦 Materiais necessários

- Dois PRs reais ou simulados (um exemplar, um com falhas)
- Guia interno de revisão segura (ex: `checklist-pr-seguro.md`)
- Plataforma de quiz (Kahoot, LMS, Markdown com validação manual)
- Canal interno para partilha e discussão (ex: Confluence, GitHub Discussions)

---

## ✅ Critérios de conclusão

- Participação ativa na sessão ou entrega do exercício
- Aprovação no quiz (mínimo 80%)
- Submissão de um PR real com justificações explícitas de segurança (ex: validação de input, logging, controlo de permissões)

---

## 🔗 Referências cruzadas no SbD-ToE

| Capítulo                    | Relevância                                   |
|-----------------------------|----------------------------------------------|
| Capítulo 6 - Desenvolvimento Seguro | Aplicação direta de requisitos REQ-114, REQ-115 e REQ-118 |
| Capítulo 2 - Requisitos de Segurança | Integração com user stories com critérios de segurança     |
| Capítulo 13 - Formação e Onboarding | Pode integrar trilho formativo do perfil Developer         |

---

## 🧭 Recomendações operacionais

- Repetir esta sessão quinzenalmente com novos exemplos
- Partilhar internamente o “PR da semana” como modelo educativo
- Criar um repositório com PRs exemplares (bons e maus) para consulta e discussão
- Associar o módulo a permissões: ex. devs só podem aprovar após completar este módulo

---

> ✅ A aprendizagem consolidada sobre revisão segura de código reduz significativamente a introdução de vulnerabilidades e acelera a maturidade das equipas técnicas.
