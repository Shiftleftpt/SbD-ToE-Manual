---
id: recomendacoes-avancadas
title: Recomendações Avançadas para Segurança de CI/CD
description: Práticas de maturidade elevada para proteção de pipelines, com foco em governação, ataque simulado e Zero Trust
tags: [avançado, cicd, pipelines, devsecops, zero trust, deteção, simulação]
sidebar_position: 30
---


# 🧠 Recomendações Avançadas para Segurança de CI/CD

Este ficheiro complementa os controlos principais definidos neste capítulo com **práticas avançadas**, voltadas para organizações com maior maturidade, ambientes regulados ou necessidades críticas de rastreabilidade, auditabilidade e resistência a ataques sofisticados.

> Estas recomendações não substituem os controlos obrigatórios por nível de risco, mas fortalecem a resiliência do pipeline face a ameaças reais e comprometimentos internos ou externos.

---

## 🔁 Integração contínua de findings no ciclo de desenvolvimento

- Criação automática de issues para findings de segurança críticos ou bloqueantes (ex: GitHub Issues, Jira);
- Ligação direta entre findings do pipeline e os backlog items dos times de produto;
- Tags e labels nos findings para facilitar triagem e ownership (ex: `team:frontend`, `risk:L3`);
- Feedback em tempo real via Slack, Teams ou bots de CI/CD.

---

## 🧪 Simulação de ataques e validação adversarial de pipelines

- **Testes de bypass intencionais**: tentar forçar deploy com falha de SAST, sem proveniência ou com findings ignorados;
- **Avaliação de permissões de runners**: executar ações com escalada de privilégios simulada;
- **Execuções simuladas com tokens revogados, ambientes bloqueados ou artefactos alterados**;
- **Ataques de man-in-the-pipeline** em ambientes de staging (verificação de reação).

---

## 🔒 Aplicação de princípios de Zero Trust no pipeline

- **Confiança nula entre repositórios, runners, artefactos e ambientes** - cada elemento deve ser autenticado, validado e isolado;
- Todos os comandos do pipeline devem partir do princípio que o runner pode ser malicioso, e vice-versa;
- Integração com serviços de autorização externa (ex: Rego/OPA, ZTA gateways).

---

## 📦 Controlo de componentes externos utilizados no pipeline

- Restrições a GitHub Actions ou scripts de terceiros:  
  - Permitir apenas actions internas ou com origem validada;
  - Uso obrigatório de `@sha` (digest) ou `@version` pinning;
- Validação da integridade dos ficheiros remotos antes de execução;
- Auditoria dos artefactos usados em ferramentas de scanner (ex: atualizações de bancos de CVE, linters).

---

## 🕵️ Monitorização e deteção de anomalias nos pipelines

- Análise de comportamento anómalo em pipelines CI/CD (ex: tempo de execução irregular, novo step adicionado, novo domínio externo contactado);
- Logging centralizado com alertas para eventos como:
  - Execução fora do horário habitual;
  - Modificações em ficheiros de pipeline sem pull request aprovado;
  - Runners a executar jobs fora do seu escopo definido.

---

## 📑 Governação contínua e validação cruzada

- Integração com catálogo organizacional de aplicações e classificação de risco;
- Verificações periódicas de que:
  - As aplicações L3 mantêm os controlos obrigatórios ativos;
  - As exceções estão a ser revistas;
  - Os templates YAML e workflows estão atualizados e assinados;
- Versionamento formal das políticas de segurança aplicadas em pipelines.

---

## 📉 Riscos adicionais mitigados

- Execução de código externo malicioso sem controlo (OSC&R: CI0001, CI0011);
- Bypass intencionais com impacto operacional (OSC&R: CI0002, CI0014);
- Uso não rastreado de actions/scripts desatualizados ou inseguros;
- Falhas de deteção por ausência de feedback loop (OSC&R: SC0006, CI0016).

---
