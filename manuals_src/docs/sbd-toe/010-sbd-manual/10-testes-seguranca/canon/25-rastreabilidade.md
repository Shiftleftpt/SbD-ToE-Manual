---
id: rastreabilidade
title: Rastreabilidade Normativa e Frameworks - Testes de Segurança
description: Mapeamento entre as práticas deste capítulo e os requisitos normativos e frameworks de segurança.
tags: [rastreabilidade, frameworks, ssdf, samm, slsa, dsoom]
sidebar_position: 25
---


# 📎 Rastreabilidade contra Frameworks - Capítulo 10: Testes de Segurança

Este ficheiro estabelece a **rastreabilidade entre as práticas prescritas neste capítulo** e os requisitos dos principais frameworks e normas de segurança associados à validação, cobertura e integração de testes de segurança no ciclo de vida de software.

> A rastreabilidade é feita de forma **top-down**, demonstrando como o SbD-ToE cobre sistematicamente os requisitos técnicos e normativos exigidos para garantir que os riscos são efetivamente mitigados por testes de segurança automatizados e manuais.

---

## 📌 Tabela de Rastreabilidade

| Requisito / Domínio (Framework)                          | Prática do Capítulo 10 que responde                            | Nível de Cobertura |
|----------------------------------------------------------|----------------------------------------------------------------|--------------------|
| **NIST SSDF** - PW.7 / RV.1 / RV.3                       | Validação automatizada, gestão de findings, cobertura por risco | ✅ Completo         |
| **OWASP SAMM v2.1** - Verification → Security Testing    | Estratégia de testes, cobertura, testes dinâmicos e manuais    | ✅ Nível 3          |
| **BSIMM13** - Security Testing (ST1–ST3)                 | Integração com CI/CD, testes múltiplos, correlação findings     | ✅ Nível 2          |
| **ISO/IEC 27001** - A.14.2.8 / A.12.6.1                  | Testes técnicos de segurança e gestão de vulnerabilidades       | ✅ Completo         |
| **ISO/IEC 27034** - Security Testing                     | Validação dos requisitos de segurança e rastreabilidade         | ✅ Completo         |
| **CIS Controls v8** - Control 16.8 / 18.3                | Testes contínuos, gestão de findings, correções proporcionais   | ✅ Completo         |
| **ENISA DevSecOps** - Secure Testing & Automation        | Validação contínua, cobertura por risco, gates e automação      | ✅ Completo         |
| **OWASP DSOMM** - Testing / Design & Development         | Testes automáticos, regressão, gates, rastreabilidade           | ✅ Nível 2/3        |

---

## 🧠 Notas explicativas por framework

### 🛠️ NIST SSDF

Cobertura total de:
- **PW.7**: testes automáticos integrados (SAST, DAST, IAST, fuzzing - Addons 01–04);
- **RV.1**: identificação e rastreio de vulnerabilidades (Addon 08);
- **RV.3**: correção, validação e aceitação formal (Addon 08).

---

### 🧱 OWASP SAMM v2.1

Atinge **nível 3** em *Security Testing*:
- Testes por tipo de aplicação e risco (Addon 00, 06);
- Automatização e regressão (Addon 07);
- Testes manuais e exploratórios (Addon 11).

---

### 📊 BSIMM13

Cobertura dos domínios:
- **ST1–ST3**: testes integrados no ciclo, rastreáveis, com foco em risco e validação contínua;
- Relacionamento direto com os requisitos definidos no Capítulo 02.

---

### 🏛️ ISO/IEC 27001

Controlos aplicáveis:
- **A.14.2.8**: testes técnicos de segurança antes da entrega;
- **A.12.6.1**: gestão de vulnerabilidades e rastreabilidade.

---

### 🔐 ISO/IEC 27034

Cobre:
- Validação formal dos requisitos de segurança;
- Rastreabilidade entre testes, código e requisitos (Addon 06).

---

### 📐 CIS Controls v8

Controlos contemplados:
- **16.8**: integração de testes no CI/CD;
- **18.3**: gestão, tratamento e aceitação formal de findings.

---

### 🔄 ENISA DevSecOps

Cobertura total de:
- Estratégia de testes segura, automatizada, escalável;
- Cobertura por tipo de risco, severidade e contexto;
- Gates de aprovação automática com rastreabilidade.

---

### 🧪 OWASP DSOMM

Cobertura sólida dos domínios **Testing** e **Design & Development**, incluindo:

- **Automated Security Testing**: execução sistemática em pipeline (Addons 01–04);
- **Test Coverage**: critérios por tipo e criticidade da aplicação (Addon 00);
- **Feedback Loop**: dashboards, PR comments e alertas automáticos (Addon 07, 08);
- **Regression Tests for Findings**: testes escritos a partir de vulnerabilidades (Addon 05);
- **PenTesting**: escopo formal e planeado (Addon 11);
- **Manage Security Findings**: gestão completa do ciclo de vida de findings (Addon 08);
- **Apply Test Gates**: thresholds e bloqueios configurados (Addon 06);
- **Document Testing Strategy**: estratégia formal (Addon 00);
- **Prioritize Security Work**: aplicação proporcional L1–L3 (Intro e matriz);
- **Measure Progress**: rastreabilidade com backlog e dashboards (Addon 08).

> 📌 O capítulo responde diretamente às práticas esperadas nos níveis 2–3 do OWASP DSOMM, sem dependência de ferramentas proprietárias e com rastreabilidade objetiva.

---

## 🔗 Ligações com outros capítulos

Este capítulo integra-se diretamente com:

- **Capítulo 01** - define a estratégia de testes proporcional ao risco;
- **Capítulo 02** - requisitos validados diretamente com cobertura rastreável;
- **Capítulo 06** - testes complementam validações em desenvolvimento;
- **Capítulo 07** - integração com pipeline CI/CD;
- **Capítulo 14** - findings e falhas ligam-se a processos de exceção e auditoria;
- **Capítulo 13** - práticas avançadas ampliam a cobertura para métricas e observabilidade;
- **Capítulo 03** - threat modeling como origem de casos de teste e vetores ofensivos;
- **Capítulo 08** - aplicação das práticas a pipelines e projetos IaC.

> 📌 Esta rastreabilidade comprova que os testes de segurança no SbD-ToE são estruturados, rastreáveis, proporcionais ao risco e operacionalmente sustentáveis.
