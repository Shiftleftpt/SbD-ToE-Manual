---
id: checklist-revisao
title: Checklist – Testes de Segurança
description: Instrumento de verificação binária e auditável da adoção prática das práticas de validação contínua de segurança.
tags: [checklist, revisão, testes, segurança, conformidade, rastreabilidade]
sidebar_position: 20
---


# ✅ Checklist de Revisão Periódica — Testes de Segurança {testes-seguranca:canon:checklist-revisao}

Este checklist aplica-se a todas as aplicações que exigem validação de segurança no seu ciclo de vida, e serve como instrumento de verificação **binária e auditável** da **adoção prática das prescrições do Capítulo 10 – Testes de Segurança**, permitindo:

- Controlo da aplicação proporcional de testes (por nível L1–L3);
- Verificação objetiva da presença, execução e tratamento dos testes;
- Geração de indicadores operacionais agregáveis por projeto, equipa ou organização.

> 🗓️ **Recomenda-se a sua revisão a cada release, mudança de arquitetura, ou regressão relevante**, conforme indicado no `15-aplicacao-lifecycle.md`.

---

## 📋 Itens de Verificação {testes-seguranca:canon:checklist-revisao#itens_de_verificacao}

| Item                                                                                                      | Verificado? |
|-----------------------------------------------------------------------------------------------------------|-------------|
| Existe uma estratégia de testes documentada, proporcional ao risco da aplicação (L1–L3)                   | ☐           |
| A estratégia de testes considera a arquitetura da aplicação e os vetores de ameaça mais críticos          | ☐           |
| Foram aplicados testes mínimos obrigatórios conforme o tipo de aplicação (ex: APIs, serviços, UI, mobile) | ☐           |
| O pipeline executa SAST de forma automática e rastreável                                                  | ☐           |
| O pipeline executa DAST com escopo, cobertura e autenticação definidos (quando aplicável)                | ☐           |
| A aplicação foi submetida a fuzzing ou testes dinâmicos aleatórios                                        | ☐           |
| Foram realizados testes manuais exploratórios dirigidos por threat modeling (quando aplicável)           | ☐           |
| Existem testes de regressão de segurança para vulnerabilidades previamente resolvidas                     | ☐           |
| Os resultados dos testes estão ligados ao commit, branch ou release correspondente                        | ☐           |
| Os findings gerados são triados, classificados e rastreados com ciclo de vida definido                    | ☐           |
| Existem critérios de aceitação de segurança por release, com thresholds mínimos                           | ☐           |
| Existem *test gates* que impedem releases quando os critérios mínimos de segurança não são atingidos      | ☐           |
| O pipeline bloqueia builds com findings críticos não justificados                                         | ☐           |
| As exceções de segurança são aprovadas formalmente, com prazo e justificação                              | ☐           |
| As exceções vencidas são revistas periodicamente e revalidadas                                            | ☐           |
| Os resultados de SAST e DAST são comunicados automaticamente à equipa (ex: comentários no PR)             | ☐           |
| As equipas de desenvolvimento têm visibilidade dos findings e participam na triagem                       | ☐           |
| Existe rastreabilidade entre testes realizados e requisitos de segurança definidos (ex: REQ-XXX)          | ☐           |
| O plano de testes de segurança está versionado no repositório ou documentado como artefacto de release    | ☐           |
| As práticas de validação estão integradas no ciclo de vida da aplicação (build, test, release, operação)  | ☐           |
| Foi realizado PenTesting com escopo definido e rastreabilidade dos findings (quando aplicável)            | ☐           |
| Os resultados do PenTesting foram integrados com os restantes findings e tratados formalmente             | ☐           |
| A eficácia dos testes é medida com métricas (ex: taxa de deteção, regressão, cobertura funcional)         | ☐           |

---

## 🔄 Integração Operacional {testes-seguranca:canon:checklist-revisao#integracao_operacional}

- Este checklist pode ser integrado em **pipelines, revisões de release, auditorias internas ou gates de produção**;
- Os resultados podem ser rastreados por **commit, release, aplicação ou equipa**;
- Cada item deve ser validado com **evidência objetiva** (ex: logs de pipeline, relatórios de testes, issues, comentários em PRs, relatórios de PenTesting).

> ⚠️ Em caso de resposta negativa, deve existir exceção formal aprovada e documentada.

---

## ✅ Conformidade e KPI {testes-seguranca:canon:checklist-revisao#conformidade_e_kpi}

- A validação deste checklist permite declarar **conformidade com o Capítulo 10 — Testes de Segurança**;
- A contagem de respostas afirmativas pode ser usada para **medir o grau de adoção das práticas prescritas**;
- Este resultado pode ser agregado por equipa ou projeto como **indicador de maturidade operacional**.

> 📌 Este mecanismo está alinhado com o modelo de controlo contínuo, rastreabilidade e proporcionalidade definido no SbD-ToE.
