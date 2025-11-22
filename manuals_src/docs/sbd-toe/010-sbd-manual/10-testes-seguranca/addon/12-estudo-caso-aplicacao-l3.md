---
description: Exemplo prático da aplicação das práticas de testes de segurança a uma
  aplicação classificada como L3, com integração completa no pipeline e gestão de
  findings.
id: estudo-caso
sidebar_position: 12
tags:
- aplicação crítica
- devsecops
- estudo de caso
- integracao
- seguranca
- segurança
- testes
title: Caso de Estudo - Validação Contínua de Segurança numa Aplicação Crítica
---


# 🔪  Aplicacao Prática das Prescrições SbD-ToE numa Aplicação L3

O exemplo refere-se a um sistema de pagamento online para retalho e serviços públicos. 
A aplicação foi classificada como **nível L3** no Capítulo 01 - Gestão de Risco, devido à sua criticidade funcional e exposição a dados financeiros e pessoais. O processo de desenvolvimento e entrega segue integralmente o modelo prescrito no manual SbD-ToE, e aqui focamos como os processos de teste em particular, e outras areas do SbD-ToE são orquestradas.

---

## 👨‍💻 Desenvolvimento com qualidade embutida (Cap. 06)

Durante o desenvolvimento, os programadores utilizaram:

* **GenIA copilotos com regras personalizadas de segurança**;
* **Linters e SAST locais (ex: Semgrep customizado)** diretamente integrados no IDE;
* **Templates de stories e critérios de aceitação com segurança embutida** (ver Cap. 02 - Requisitos de Segurança);
* **Ambiente isolado com DevContainers e scanners preventivos** (ver Cap. 09 - *containers* e Execução Isolada).

Resultado: ao submeter um Pull Request, a maior parte dos problemas triviais já tinha sido eliminada.

---

## 🔍 Validações automáticas no Pull Request (Cap. 10, Cap. 07)

No momento do PR, são ativados:

* **SAST completo via Checkmarx**;
* **Linters de conformidade (YAML, JSON, infra)**;
* **Verificação de dependências com Xygeni e SBOMs geradas** (ver Cap. 05 - SBOM e SCA);
* **Integração de feedback automático no PR** (via GitHub + comentários inline).

Critérios de bloqueio configurados (Cap. 10 `addon/01`, `addon/02`, `addon/04`):

* Nenhum finding crítico pode estar "aberto";
* Qualquer finding alto obriga à **triagem ou exceção justificada** (Cap. 10 `addon/08`);
* O plano de testes por risco (Cap. 10 `addon/00`) valida se a matriz L3 está a ser cumprida.

---

## 🗒️ Gestão de Findings (Cap. 10, Cap. 05)

Findings são automaticamente registados no **DefectDojo**, com:

* Metadata do commit, PR, branch;
* Classificação por severidade, origem (SAST/DAST/Fuzzing), CVSS;
* Análise de reincidência ou regressão (Cap. 10 `addon/08`);
* Integração com backlog (Jira), com ownership atribuído (Cap. 06).

Exceções são submetidas com:

* Justificação técnica;
* Mitigação compensatória;
* Data de reavaliação obrigatória (Cap. 10 `addon/08` + `20-checklist`).

---

## ⚠️ Ambiente de staging e testes ofensivos (Cap. 10, Cap. 11)

Após merge:

1. O código é deployed em **staging isolado**, com variáveis seguras (Cap. 07 e Cap. 09);

2. São executados testes combinados:

   * **DAST com autenticação + spidering** (Burp Enterprise);
   * **Fuzzing dirigido por cobertura** (RESTler + ZAP add-ons);
   * **IAST por instrumentação passiva** (Contrast).

3. Paralelamente, é agendado **PenTest Grey-box** por equipa interna, com acesso à documentação e endpoints sensíveis. Os vetores explorados incluem:

   * Manipulação de sessão;
   * Escalada de permissões;
   * Bypass de validações client-side;
   * Teste de abuso em APIs transacionais.

Resultados do PenTest são integrados no mesmo processo de findings (Cap. 10 `addon/11-pen-testing.md`), com um ciclo de tratamento idêntico aos restantes testes.

---

## 🛡️ Monitorização e resposta contínua (Cap. 12 + Cap. 05)

Em produção:

* A aplicação é instrumentada com **telemetria de segurança**, cobrindo falhas de autenticação, comportamentos suspeitos, erros HTTP anómalos;
* Os artefactos em produção incluem SBOMs completas assinadas (ver Cap. 05);
* A ferramenta **Xygeni monitora continuamente o SBOM e cadeia de fornecimento** (SSCS):

  * Identifica **malware em bibliotecas**;
  * Deteta **novos CVEs com impacto direto**;
  * Para pacotes com **atualização segura**, **abre automaticamente PRs** com correção;
  * Para pacotes com impacto funcional, **cria issue crítica** com análise de risco automatizada e dependência bloqueada até revisão manual.

Este processo fecha o ciclo, pois:

* Findings são associados a versões e SBOMs específicos;
* As equipas são notificadas por canal (Slack + Jira + e-mail);
* Todas as ações ficam **documentadas para auditoria futura** (Cap. 10 `addon/08` + `addon/09`).

---

## 📦 Validação final antes do release (Cap. 11)

Antes da entrada em produção:

* É gerado **checklist de segurança (Cap. 10 `20-checklist`)** com rastreabilidade completa;
* Todas as **exceções devem estar aprovadas e documentadas**;
* Os **resultados do PenTest devem estar resolvidos ou formalmente aceites**;
* A release só é permitida se todos os testes obrigatórios tiverem cobertura positiva.

---

## 📈 Conclusão

Esta narrativa demonstra a **aplicação prática do modelo SbD-ToE de forma integrada e realista**, com:

* Aplicação proporcional por nível de risco (L3);
* Validações contínuas, ofensivas e regressivas;
* Integração de ferramentas líderes (Checkmarx, Xygeni, DefectDojo);
* Cultura de segurança sustentada por processos, políticas e automatização.

> 📌 Cada passo da história corresponde a uma ou mais prescrições explícitas do manual, validando que o SbD-ToE é exequível, auditável e eficaz - mesmo em contextos de elevada exigência.
