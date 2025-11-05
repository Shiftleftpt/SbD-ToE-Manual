---
id: policies-relevantes
title: Policies Relevantes
tags: [canon, politicas, risco, classificacao, excecao]
---

# 🏛️ Políticas Organizacionais - Gestão de Risco

A adoção eficaz do Capítulo 01 - Gestão de Risco - exige a existência de **políticas organizacionais formais** que **enquadrem, legitimem e sustentem a aplicação das práticas descritas neste capítulo**.

---

## 📌 Nota fundamental

> ⚠️ As práticas operacionais prescritas neste capítulo (classificação, revisão, aceitação, rastreabilidade) **devem ser legitimadas formalmente por políticas organizacionais aprovadas**.

Estas políticas:

- Tornam **visível e vinculativa** a prática da gestão de risco aplicacional dentro da organização;
- Permitem que as decisões de segurança deixem de depender de iniciativa individual;
- Servem de base normativa para **auditorias internas e externas**.

> 📎 A exigência de políticas formais de classificação e aceitação de risco é uma **expectativa explícita** em normas como **ISO/IEC 27005**, **ENISA Risk Management**, **NIST SSDF** e **CIS Controls v8**.

> 🧩 Este capítulo **implementa, na prática, o que as políticas definem** - a política aprova, o capítulo operacionaliza.

---

## 🧾 Políticas recomendadas

| Nome da Política                                   | Obrigatória? | Aplicação                             | Conteúdo mínimo esperado                                                                                      |
|----------------------------------------------------|--------------|----------------------------------------|---------------------------------------------------------------------------------------------------------------|
| Política de Classificação de Risco Aplicacional    | ✅ Sim       | Todos os projetos e equipas de produto | Modelo de classificação obrigatório (exposição, dados, impacto); momentos de aplicação; registo e rastreio. |
| Política de Aceitação de Risco Residual            | ✅ Sim       | Segurança, gestão, donos de produto    | Critérios formais para aceitação; responsáveis; validade temporal; registo e rastreabilidade.               |
| Política de Revisão Periódica de Risco             | ✅ Sim       | Toda a organização                     | Frequência mínima (ex: 6 meses); triggers obrigatórios; evidência exigida.                                   |
| Política de Rastreabilidade de Decisões de Segurança | ⚠️ Opcional | Organizações sujeitas a auditoria      | Versionamento de classificações; ligação com arquitetura, requisitos e controlos.                           |

---

## 🧩 Correspondência com frameworks normativas

| Framework              | Requisitos cobertos pelas políticas acima                                       |
|------------------------|----------------------------------------------------------------------------------|
| **ISO/IEC 27005**      | Identificação (8.2), Avaliação (8.3), Aceitação (8.5)                            |
| **NIST SP 800-30**     | Etapas 1–4 (Caracterização, Ameaças, Vulnerabilidades, Impacto)                 |
| **NIST SSDF**          | RM.1 (Categorize SW), RM.2 (Assess Risk), RM.3 (Manage Risk)                    |
| **ENISA Risk Management** | Sec. 2.3, 3.1 - definição formal de políticas de avaliação e aceitação de risco |
| **CIS Controls v8**    | Control 2, 4 - políticas para inventário, avaliação e aceitação de risco         |
| **OWASP SAMM**         | Governance > Risk Management (níveis 1 e 2)                                      |
| **BSIMM13**            | Strategy and Metrics (SR1.1, SR1.5)                                              |

---

## 🧱 Estrutura sugerida de cada política

Cada política organizacional deve conter, no mínimo:

- **Objetivo e âmbito** da política;
- **Âmbito de aplicação**: quem, onde e quando se aplica;
- **Regras e critérios obrigatórios** (ex: quando aplicar, como classificar, quem aprova);
- **Papéis e responsabilidades** (segurança, produto, arquitetura, gestão);
- **Exigência de documentação e rastreabilidade**;
- **Periodicidade de revisão da política em si** (ex: anual).

---

## ✅ Recomendações finais

- Estas políticas devem ser **oficialmente aprovadas** pela gestão de segurança e da organização;
- Devem estar **publicadas e acessíveis** a todas as equipas;
- A sua existência é uma **pré-condição para garantir coerência, auditabilidade e maturidade real da segurança by design**;
- A sua aplicação deve estar alinhada com as práticas descritas neste capítulo.

> 📌 Templates para estas políticas poderão ser disponibilizados como ficheiros `60-*.md` complementares em futuras versões do manual.
