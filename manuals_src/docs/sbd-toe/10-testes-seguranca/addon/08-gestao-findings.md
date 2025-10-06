---
id: gestao-findings
title: Gestão de Findings de Segurança
description: Processo de triagem, priorização, rastreio e resolução de vulnerabilidades detetadas nos testes de segurança.
tags: [findings, gestão, vulnerabilidades, segurança, rastreabilidade]
sidebar_position: 9
---


# 🗂️ Gestão de Findings de Segurança {testes-seguranca:addon:gestao-findings}

## 🌟 Objetivo {testes-seguranca:addon:gestao-findings#objetivo}

Estabelecer um processo eficaz e contínuo para gerir findings de segurança — isto é, **resultados de testes que indicam potenciais vulnerabilidades ou más práticas**, assegurando:

- Triagem por criticidade, contexto e reprodutibilidade;
- Integração com backlog e ferramentas de desenvolvimento;
- Consolidação centralizada para priorização e rastreabilidade;
- Tratamento validado por responsáveis com memória organizacional;
- Redução de ruído e redundância entre ferramentas de validação.

> ⚠️ Findings ignorados ou dispersos enfraquecem a segurança. Findings centralizados e rastreados reforçam-na.

---

## 🔍 O que são findings de segurança {testes-seguranca:addon:gestao-findings#o_que_sao_findings_de_seguranca}

Findings podem resultar de:

- SAST, DAST, IAST, fuzzing;
- Testes manuais ou revisões;
- Ferramentas de SBOM/SCA ou políticas organizacionais;
- Monitorização runtime ou alertas de produção.

Cada finding representa uma **observação de risco** que requer decisão:

- É verdadeiro? É falso positivo?
- Foi aceite, mitigado ou resolvido?
- Está associado a um requisito, release, commit?
- Foi validado ou apenas ocultado?

> 💡 Findings ≠ CVEs: são *ocorrências concretas* no contexto da aplicação e devem ser tratados como tal.

---

## ⚙️ Como aplicar {testes-seguranca:addon:gestao-findings#como_aplicar}

1. **Centralizar todos os findings num sistema consolidado** (ex: DefectDojo, Jira com plugins, Vulcan, Security Hub);
2. **Criar critérios objetivos de triagem** (ex: CWE, OWASP Top 10, risco organizacional);
3. **Associar cada finding a metadados rastreáveis**: commit, versão, módulo, requisito (REQ-XXX);
4. **Integrar findings no backlog da equipa com estado e SLA definidos**;
5. **Estabelecer fluxo formal: triado → aceite → corrigido → validado**;
6. **Consolidar dados de múltiplas ferramentas com correlação de duplicados e false positives**.

> 🔐 A centralização permite priorizar recursos, garantir resposta proporcional ao risco e gerar visibilidade executiva.

---

## ✅ Boas práticas {testes-seguranca:addon:gestao-findings#boas_praticas}

- Usar plataformas como **DefectDojo**, **Vulcan**, **Security Hub** ou soluções integradas para centralização;
- Classificar findings por risco (L1–L3) e ajustar processo:
  - **L1**: findings podem ser triados diretamente no backlog;
  - **L2–L3**: devem ser centralizados, auditáveis e acompanhados por AppSec;
- Evitar duplicações entre ferramentas — estabelecer pipelines de correlação;
- Automatizar exportação de findings para quadros de triagem e KPIs;
- Rever findings aceites a cada trimestre;
- Integrar dashboards por release, módulo, equipa ou tipo de falha.

---

## 📎 Referências cruzadas {testes-seguranca:addon:gestao-findings#referencias_cruzadas}

| Documento                       | Relevância estratégica                        |
|--------------------------------|------------------------------------------------|
| Capítulo 02 — Requisitos       | Valida requisitos e permite rastreabilidade (REQ-XXX) |
| Capítulo 06 — Desenvolvimento  | Findings evidenciam falhas recorrentes ou violação de padrões seguros |
| Capítulo 07 — CI/CD Seguro     | Findings originados em jobs de validação contínua |
| `01-sast.md`, `02-dast.md`     | Produzem findings que devem ser triados       |
| `09-feedback-equipa.md`        | Define mecanismos de comunicação e ownership   |

---

> 📊 A gestão de findings é um processo contínuo, não um ficheiro de exportação. A sua centralização e racionalização por risco são o alicerce para decisões de segurança informadas e eficazes.
