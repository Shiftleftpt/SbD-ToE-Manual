---
description: Validações do próprio código do pipeline (YAML, scripts, linters), incluindo
  controlo de lógica, permissões e uso de componentes externos.
id: seguranca-codigo-pipeline
sidebar_position: 2
tags:
- cicd
- linters
- pipelines
- scripts
- seguranca
- validacao
- validação
title: Segurança do Código dentro do Pipeline
---



# 🔒 Segurança do código dentro do pipeline

A segurança da entrega contínua depende da capacidade de **detetar automaticamente código inseguro, práticas deficientes ou vulnerabilidades conhecidas** antes da build ou do deploy. Esta prática define os **controlos técnicos de validação de segurança a aplicar diretamente dentro dos pipelines CI/CD**, de forma rastreável e proporcional ao risco.

> Nenhum código deve ser promovido sem validações de segurança automatizadas e visíveis no pipeline.

---

## 🎯 Objetivos

- Garantir que **todo o código entregue passou por validações de segurança automatizadas e consistentes**;
- Integrar testes de segurança como parte obrigatória do fluxo CI/CD;
- Prevenir a inclusão de código malicioso, inseguro ou com segredos expostos em builds ou releases.

---

## 🛠️ Práticas

1. **Integração de testes de segurança no pipeline**  
   - Inclusão de SAST (análise estática) como etapa obrigatória do pipeline;
   - Execução regular de scanners de *secrets* e credenciais hardcoded;
   - Aplicação de linters de segurança (ex: IaC, containers, políticas internas).

2. **Validação contra requisitos definidos no Capítulo 02**  
   - O pipeline deve verificar se o código cumpre requisitos de segurança aplicáveis;
   - Aplicações L2 e L3 devem ter *gates* de segurança definidos como critérios formais.

3. **Rejeição automática de código que viole critérios mínimos**  
   - A build deve falhar se forem detetadas funções inseguras, bibliotecas desatualizadas ou segredos embebidos;
   - Devem existir critérios explícitos de aprovação/rejeição (ex: qualidade mínima, findings críticos bloqueadores).

4. **Preservação e rastreabilidade dos resultados de análise**  
   - Os resultados dos testes devem ser armazenados e associados a commits, branches ou releases;
   - Aplicações L3 devem manter histórico formal e mecanismos de revisão de findings.

5. **Cobertura proporcional ao risco e ao tipo de aplicação**  
   - Aplicações críticas devem incluir testes de IaC, SBOM, análise de dependências, containers e binários;
   - A cobertura deve ser documentada e revisitada regularmente.

---

## ⚖️ Aplicação proporcional por nível de risco

| Nível | Requisitos obrigatórios                              | Requisitos reforçados                                     |
|-------|--------------------------------------------------------|------------------------------------------------------------|
| **L1** | SAST e secrets scanning básicos integrados             | -                                                          |
| **L2** | Falha da build se critérios mínimos forem violados     | Linters IaC; análise de containers e dependências          |
| **L3** | Política formal de findings; rastreabilidade por commit| Cobertura total; validação formal com gates de segurança   |

---

## 📌 Exemplos práticos

- **GitHub Actions**  
  - Integração com `CodeQL`, `TruffleHog`, linters IaC;
  - Rejeição automática com `continue-on-error: false`.

- **GitLab**  
  - Segurança integrada (`SAST`, `Secret Detection`, `Container Scanning`);
  - Exportação de findings para dashboards e artefactos.

- **Azure DevOps**  
  - Tarefas de SAST/DAST como etapas obrigatórias em `azure-pipelines.yml`;
  - `quality gates` bloqueadores via extensões (ex: SonarQube).

- **Jenkins**  
  - Integração com scanners (ex: SonarQube, Semgrep, detect-secrets);
  - Falha automática via políticas de controlo no pipeline.

---

## 📉 Riscos mitigados

- Inclusão de código malicioso ou inseguro (OSC&R: SC0001, SC0006);
- Builds com vulnerabilidades conhecidas não detetadas (OSC&R: SC0008);
- Dependências desatualizadas ou comprometidas (ligação com Cap. 05);
- Vazamento de segredos hardcoded (OSC&R: CI0010).

---
