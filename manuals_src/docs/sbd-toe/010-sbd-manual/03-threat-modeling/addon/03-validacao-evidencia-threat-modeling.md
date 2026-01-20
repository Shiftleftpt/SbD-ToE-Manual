---
id: validacao-evidencia-threat-modeling
title: Validação e Evidência no Threat Modeling
description: Critérios de aceitação, validação humana e evidência mínima para modelos de ameaças
tags: [threat-modeling, validacao, evidencia, decisao]
---

# 🛠️ Validação e Evidência no Threat Modeling

Um modelo de ameaças só é operacionalmente válido quando:
- foi explicitamente validado;
- tem um responsável identificado;
- produz evidência verificável.

Sem estes elementos, o Threat Modeling permanece uma atividade exploratória, não um controlo de segurança.

---

## 1. Validação humana obrigatória

Todo o modelo de ameaças deve ser:
- revisto criticamente;
- aprovado por um role explícito (ex.: Tech Lead, Security Architect).

Ferramentas, métodos ou suportes analíticos **não substituem esta decisão**.

---

## 2. Critérios mínimos de aceitação

Um Threat Model é considerado aceite quando, no mínimo:

- o contexto do sistema está claramente definido;
- a arquitetura analisada está identificada e versionada;
- as principais ameaças foram identificadas e classificadas;
- cada ameaça tem uma decisão associada:
  - mitigada,
  - aceite,
  - transferida,
  - ou rejeitada com justificação.

---

## 3. Evidência mínima obrigatória

A evidência associada a um Threat Model deve incluir, no mínimo:

- diagrama(s) arquitetural(is) versionado(s);
- lista de ameaças com decisão explícita;
- ligação clara a requisitos de segurança ou mitigações;
- identificação do responsável pela validação;
- data e versão do modelo.

A evidência deve ser:
- reproduzível;
- auditável;
- preservada de acordo com as políticas da organização.

---

## 4. Distinção entre apoio e decisão

É obrigatório distinguir explicitamente entre:
- artefactos de apoio à análise;
- o modelo de ameaças validado.

Apenas o segundo constitui base para:
- definição de requisitos;
- aceitação de risco;
- auditoria.

---

## 5. Revisão e invalidação

Um modelo de ameaças deve ser revisto sempre que ocorra:

- alteração significativa da arquitetura;
- introdução de novas dependências;
- mudança relevante no fluxo de dados;
- reclassificação do nível de risco (L1–L3).

Modelos não revistos devem ser considerados **potencialmente inválidos**.

---

## 6. Integração com outros capítulos

O Threat Modeling validado constitui:
- input direto para o Capítulo 02 — Requisitos de Segurança;
- base de justificação para decisões arquiteturais;
- evidência de aplicação proporcional ao risco definido no Capítulo 01.
