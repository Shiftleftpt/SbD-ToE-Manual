---
id: rastreabilidade
title: Rastreabilidade Top-Down - Desenvolvimento Seguro
description: Rastreabilidade entre as práticas deste capítulo e os requisitos dos principais frameworks de segurança de software
tags: [rastreabilidade, frameworks, desenvolvimento, SAMM, SSDF, BSIMM, DSOMM]
sidebar_position: 25
---

# 📎 Rastreabilidade contra Frameworks - Capítulo 06: Desenvolvimento Seguro

Este ficheiro estabelece a **rastreabilidade entre as práticas prescritas neste capítulo** e os requisitos dos principais frameworks e normas de segurança de software relacionados com **codificação segura, automação, validação contínua e revisão estruturada**.

> A rastreabilidade é feita de forma **top-down**, demonstrando como o SbD-ToE cobre sistematicamente os controlos e requisitos aplicáveis ao desenvolvimento seguro.

---

## 📌 Tabela de Rastreabilidade

| Requisito / Domínio (Framework)                          | Práticas do Capítulo 06 que respondem                          | Nível de Cobertura |
|----------------------------------------------------------|----------------------------------------------------------------|--------------------|
| **NIST SSDF** – PW.5 / PW.7                              | Revisão de código, linters, validação automatizada             | ✅ Completo         |
| **OWASP SAMM v2.1** – Implementation → Secure Build / Review | Guidelines, práticas seguras, controlo automático e humano     | ✅ Nível 3          |
| **BSIMM13** – Code Review (CR1–CR3)                      | Revisão formal, integração com requisitos, evidência            | ✅ Nível 2          |
| **ISO/IEC 27001** – A.14.2.5 / A.14.2.6                   | Revisão técnica e validação de segurança                       | ✅ Completo         |
| **ISO/IEC 27034** – Coding Principles                    | Guidelines de codificação segura e verificação                 | ✅ Completo         |
| **CIS Controls v8** – Control 16.3 / 16.11 / 16.12        | Linters, scanners, revisão de código estruturada               | ✅ Completo         |
| **ENISA DevSecOps** – Secure Coding & CI Integration     | Linters, automação, rastreabilidade e revisão contínua         | ✅ Completo         |
| **OWASP DSOMM** – Design & Development                   | Build seguro, validação contínua, rastreabilidade e evidência  | ✅ Nível 2/3        |

---

## 🧠 Notas explicativas por framework

### 🛠️ NIST SSDF

Cobertura direta de:
- **PW.5** – Práticas de codificação segura formalizadas (Addon `01`, `07`);
- **PW.7** – Validação automatizada e sistemática com linters e anotadores (Addon `02`, `08`, `09`).

---

### 🧱 OWASP SAMM v2.1

Atinge **nível 3 de maturidade** nos domínios:
- *Secure Build*: aplicação de guidelines técnicas e uso de ferramentas de controlo (Addon `01`, `02`, `08`);
- *Secure Review*: validação técnica manual com rastreabilidade e evidência (Addon `09`).

---

### 📊 BSIMM13

Práticas alinhadas com:
- **CR1–CR3** – Revisão estruturada com critérios de segurança e integração com requisitos técnicos (Addon `08`);
- Evidência formal através de anotação, justificação e rastreabilidade (`09`, `05`).

---

### 🏛️ ISO/IEC 27001

Cobertura dos controlos:
- **A.14.2.5** – Revisão técnica orientada à segurança das alterações de código;
- **A.14.2.6** – Validação formal, justificação de exceções, registo e conformidade.

---

### 🔐 ISO/IEC 27034

Aplicação clara de:
- Princípios de codificação segura documentados e seguidos por norma (Addon `01`);
- Rastreabilidade entre guidelines internas e validação efetiva no ciclo de desenvolvimento (`07`, `08`).

---

### 📐 CIS Controls v8

Contempla:
- **16.3** – Uso de linters, análise estática e validadores sintáticos (Addon `02`);
- **16.11** – Validação formal de requisitos e controlos de segurança no código (`08`);
- **16.12** – Revisão manual com critérios formais, anotação e evidenciação (`09`).

---

### 🔄 ENISA DevSecOps

Cobertura total dos princípios:
- Aplicação de standards de codificação e validação estruturada (`01`, `07`);
- Linters e validações automáticas integradas na pipeline (`02`, `08`);
- Revisão técnica com evidência e rastreabilidade (`09`).

---

### 🧬 OWASP DSOMM

Domínio *Design & Development* coberto por:
- **Secure Build** – Linters (`02`), validação de dependências (`03`) e controlo formal no processo de build (`08`);
- **Security Testing** – Testes estruturados com anotação e evidência (`08`, `09`);
- **Developer Guidance** – Diretrizes internas, formação e regras de exceção (`05`, `07`);
- **Feedback Loops** – Evidência de falhas e registos que alimentam ciclos de melhoria.

---

## 🔗 Ligações com outros capítulos

O Capítulo 06 depende e contribui para os seguintes capítulos:

- **Capítulo 01 – Gestão de Risco**: define a exigência proporcional das práticas com base no nível L1–L3;
- **Capítulo 02 – Requisitos de Segurança**: estabelece os REQ-XXX validados e implementados neste capítulo;
- **Capítulo 05 – Dependências e SCA**: garante que os componentes usados em desenvolvimento são seguros e rastreáveis;
- **Capítulo 07 – CI/CD Seguro**: onde estas práticas se integram como passos automatizados na pipeline;
- **Capítulo 10 – Testes e Coverage de Segurança**: validação final e cruzamento com testes e métricas de segurança.

---

> 📌 Este capítulo fornece a camada técnica essencial para aplicar e verificar os requisitos definidos pelo SbD-ToE. As práticas aqui descritas permitem evidenciar conformidade, uniformizar validações e criar pipelines auditáveis - estabelecendo uma ponte sólida entre teoria normativa e execução prática.
