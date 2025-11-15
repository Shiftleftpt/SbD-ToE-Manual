---
id: governanca-legada
title: Governação em Sistemas Legados
sidebar_position: 10
description: Estratégias para aplicar governação formal de segurança em sistemas e contratos legados
tags: [legado, governanca, excecoes, migração]
---


# 🛠️ Governação de Sistemas Legados e Contextos Não Conformes

Este documento aborda a aplicação proporcional e adaptada do modelo SbD-ToE a **sistemas legados, pipelines antigos, contratos pré-existentes ou contextos organizacionais onde o controlo total não é imediato ou viável**.

---

## 🌟 Objetivo

* Permitir que projetos legados sejam enquadrados num modelo de governaça estruturado;
* Garantir visibilidade, rastreabilidade e compensações mesmo quando não é possível aplicar todos os requisitos;
* Evitar exceções silenciosas que colocam em risco a coerência do modelo SbD-ToE.

---

## 🧰 Contextos típicos

* Aplicações críticas herdadas sem documentação técnica ou owners ativos;
* Pipelines de CI/CD antigos, operacionais mas fora do controlo da equipa AppSec;
* Contratos em vigor com fornecedores que não cumprem os requisitos mínimos;
* Bibliotecas ou módulos partilhados sem revisão de segurança.

---

## 🛠️ Abordagem proposta

1. **Identificar e classificar o ativo legado** (usando critérios do Cap. 1);
2. **Mapear requisitos aplicáveis**, mesmo que não cumpridos;
3. **Analisar viabilidade de aplicação técnica de controlos**;
4. **Registar exceções formais**, se aplicável, com:

   * Justificação de negócio
   * Riscos reconhecidos
   * Compensações propostas
   * Validade e plano de reavaliação
5. **Incluir o ativo no ciclo de revisão continuada** (Cap. 14.6)

---

## 📋 Exemplo de registo de governação de legado

| Campo                    | Valor                                                |
| ------------------------ | ---------------------------------------------------- |
| Sistema                  | DataBroker interno                                   |
| Nível de risco           | L3                                                   |
| Requisitos não cumpridos | REQ-AUD-002, REQ-LOG-003                             |
| Justificação             | Sistema core dependente de arquitetura pré-existente |
| Compensações             | Monitorização por SIEM externo + controlo de acesso  |
| Owner                    | joana.sousa\@empresa                                 |
| Reavaliação agendada     | 6 meses (integração futura com novo projeto)         |

---

## ✅ Recomendações

* Nunca ignorar ativos legados: tratar como exceção formal com rastreabilidade;
* Incorporar o ciclo de revisão e melhoria contínua;
* Monitorizar compensações e documentar desvios de forma transparente;
* Incluir estes casos nos **KPIs de maturidade e governaça**.

---

## 🔗 Ligações cruzadas

* Cap. 1 - Classificação de risco
* Cap. 2 - Requisitos mínimos por risco
* Cap. 14.1 - Modelo de decisão e exceções
* Cap. 14.6 - Validação continuada
* Cap. 08 / 09 - Integração com pipelines e execução isolada

---
