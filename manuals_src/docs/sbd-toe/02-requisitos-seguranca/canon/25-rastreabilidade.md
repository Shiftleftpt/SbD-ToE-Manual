---
id: rastreabilidade
title: Rastreabilidade Normativa — Requisitos de Segurança
description: Correspondência entre as práticas de requisitos e frameworks como SSDF, SAMM, ISO, BSIMM, DSOMM
tags: [rastreabilidade, frameworks, SSDF, SAMM, DSOMM, BSIMM, ISO]
sidebar_position: 25
---

# 📎 Rastreabilidade contra Frameworks — Capítulo 02: Requisitos de Segurança {requisitos-seguranca:canon:rastreabilidade}

Este ficheiro estabelece a **rastreabilidade entre as práticas de definição, validação e gestão de requisitos de segurança** descritas neste capítulo e os principais frameworks de segurança aplicacional.

> A rastreabilidade é feita de forma **top-down**, demonstrando como o SbD-ToE cobre os requisitos normativos e técnicos de segurança por meio de requisitos formalizados, validados e rastreáveis por risco.

---

## 📌 Tabela de Rastreabilidade {requisitos-seguranca:canon:rastreabilidade#tabela_de_rastreabilidade}

| Requisito / Domínio (Framework)                          | Prática do Capítulo 02 que responde                            | Nível de Cobertura |
|----------------------------------------------------------|----------------------------------------------------------------|--------------------|
| **NIST SSDF** – PW.1 / PW.4                              | Catálogo de requisitos, critérios, validação estruturada       | ✅ Completo         |
| **OWASP SAMM v2.1** – Design → Security Requirements     | Requisitos por risco e tipo de aplicação, rastreabilidade      | ✅ Nível 3          |
| **BSIMM13** – Requirements & Attack Models (AM1–AM2)     | Requisitos funcionais de segurança, ligados a ameaças          | ✅ Nível 2          |
| **OWASP ASVS v5** – All levels (V1–V14)                  | Base para o catálogo de requisitos REQ-XXX                     | ✅ Completo         |
| **ISO/IEC 27034** – Security Control Specification       | Requisitos testáveis, rastreáveis e auditáveis                 | ✅ Completo         |
| **CIS Controls v8** – Múltiplos                          | Aplicação prática dos requisitos por controlo específico       | ✅ Completo         |
| **ENISA SDLC / DevSecOps** – Security Requirements       | Integração de requisitos no ciclo de vida, backlog, validação  | ✅ Completo         |
| **OWASP DSOMM** – Design & Development                   | Requisitos estruturados, reutilizáveis e alinhados a práticas de maturidade | ⚠️ Parcial      |

---

## 🧠 Notas explicativas por framework {requisitos-seguranca:canon:rastreabilidade#notas_explicativas_por_framework}

### 🛠️ NIST SSDF {requisitos-seguranca:canon:rastreabilidade#nist_ssdf}

Cobertura total dos objetivos **PW.1** (definição sistemática de requisitos por risco) e **PW.4** (validação técnica e formal), suportada por:

- [Catálogo de Requisitos](xref:sbd-toe:toe:02-requisitos-seguranca:catalogo-requisitos)
- [Matriz por Risco](xref:sbd-toe:toe:01-classificacao-aplicacoes:matriz-controlos-por-risco)
- [Validação Testável](xref:sbd-toe:toe:02-requisitos-seguranca:validacao-requisitos)
- [Validação Estruturada](xref:sbd-toe:toe:02-requisitos-seguranca:validacao-requisitos)

---

### 🧱 OWASP SAMM v2.1 {requisitos-seguranca:canon:rastreabilidade#owasp_samm_v21}

Práticas que asseguram **nível 3 em “Security Requirements”**:

- Catálogo estruturado, proporcional ao risco, com rastreabilidade;
- Taxonomia de requisitos e ligação a testes e validações;
- Visibilidade operacional por backlog e exceções controladas.

---

### 📊 BSIMM13 {requisitos-seguranca:canon:rastreabilidade#bsimm13}

Cobertura das práticas AM1–AM2:

- Definição sistemática de requisitos com origem em modelos de ameaça;
- Critérios de aceitação por requisito;
- Requisitos aplicados em diferentes fases do SDLC.

---

### 🔐 OWASP ASVS v5 {requisitos-seguranca:canon:rastreabilidade#owasp_asvs_v5}

O catálogo de requisitos do SbD-ToE baseia-se no ASVS v5:

- Requisitos agrupados por temas e níveis de risco;
- Mapeamento direto às categorias V1–V14;
- Rastreabilidade e testabilidade embutidas.

---

### 🏛️ ISO/IEC 27034 {requisitos-seguranca:canon:rastreabilidade#isoiec_27034}

Práticas alinhadas com a especificação de controlos de segurança:

- Requisitos definidos com objetivos claros e validação associada;
- Integração no ciclo de vida e evidência auditável.

---

### 📐 CIS Controls v8 {requisitos-seguranca:canon:rastreabilidade#cis_controls_v8}

Requisitos do capítulo mapeiam controlos como:

- Control 6 (Account Management),
- Control 8 (Audit Log Management),
- Control 16 (Application Software Security),
- E outros, via segmentação temática por domínio técnico.

---

### 🔄 ENISA SDLC / DevSecOps {requisitos-seguranca:canon:rastreabilidade#enisa_sdlc__devsecops}

As práticas incluem:

- Integração nativa de requisitos em artefactos e processos de desenvolvimento;
- Validação por critérios, testes e revisões;
- Rastreabilidade para exceções e coverage.

---

### ⚙️ OWASP DSOMM — Domínio "Design & Development" {requisitos-seguranca:canon:rastreabilidade#owasp_dsomm__dominio_design__development}

O capítulo suporta parcialmente os objetivos de maturidade definidos no domínio **Design & Development** do DSOMM:

| Subdomínio DSOMM         | Estado no Capítulo 02                                 |
|--------------------------|-------------------------------------------------------|
| Security Requirements    | ✅ Completamente coberto — catálogo, validação, tags   |
| Reusable Controls        | ⚠️ Parcial — matriz por risco, taxonomia, exceções     |
| Design Guidelines        | ⚠️ Parcial — refletidas no conteúdo dos requisitos     |
| Policy as Code           | 🔄 Opcional — abordado em `30-recomendacoes-avancadas` |

> 📌 O capítulo permite atingir **maturidade intermédia (nível 2–3)** no DSOMM, se complementado com políticas formais e práticas de rastreabilidade reforçadas.

---

## 🔗 Ligações com outros capítulos {requisitos-seguranca:canon:rastreabilidade#ligacoes_com_outros_capitulos}

Este capítulo depende diretamente de:

- **Capítulo 01** — define a proporcionalidade por risco (L1–L3);
- **Capítulo 03** — modelo de ameaças origina requisitos;
- **Capítulo 04** — requisitos especializados por arquitetura;
- **Capítulo 10** — reforça a maturidade atingida pelas práticas aqui definidas;
- **Capítulos 13 e 14** — permitem governação contínua e exceções rastreáveis.

> ✅ Esta rastreabilidade demonstra que o Capítulo 02 fornece **a espinha dorsal normativa da segurança aplicacional**, traduzindo requisitos normativos em práticas rastreáveis e validadas ao longo do ciclo de vida.

