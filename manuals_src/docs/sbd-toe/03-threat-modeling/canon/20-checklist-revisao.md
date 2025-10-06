---
id: checklist-revisao
title: ✅ Checklist SbD-ToE — Threat Modeling
sidebar_label: Checklist de Revisão
---

# ✅ Checklist de Revisão Periódica — Threat Modeling {threat-modeling:canon:checklist-revisao}

Este checklist aplica-se a todas as aplicações com criticidade L2 ou L3, ou que envolvam fluxos sensíveis, exposições externas ou alterações arquiteturais relevantes.

Serve como instrumento de verificação binária e auditável da **adoção prática das prescrições do Capítulo 3 — Threat Modeling**, permitindo:

- Verificação formal em revisões técnicas e auditorias;
- Controlo da rastreabilidade entre ameaças, requisitos e controlos;
- Geração de indicadores operacionais agregáveis por projeto ou equipa.

> 🗓️ **Recomenda-se a sua revisão no início de cada épico ou funcionalidade crítica, e antes de alterações significativas no sistema.**

---

## 📋 Itens de Verificação {threat-modeling:canon:checklist-revisao#itens_de_verificacao}

| Item                                                                                                  | Verificado? |
|-------------------------------------------------------------------------------------------------------|-------------|
| Foi realizada uma sessão de threat modeling para esta aplicação ou componente?                       | ☐           |
| Estão identificados os fluxos de dados, activos e trust boundaries?                                  | ☐           |
| Foram aplicadas metodologias estruturadas (ex: STRIDE, LINDDUN, PASTA)?                              | ☐           |
| As ameaças identificadas estão documentadas e priorizadas?                                           | ☐           |
| Existe plano de mitigação para cada ameaça relevante?                                                | ☐           |
| A equipa multidisciplinar participou e validou os resultados?                                        | ☐           |
| O modelo de ameaças está versionado e atualizado conforme alterações ao sistema?                     | ☐           |
| Foi considerada (e validada) a reutilização de modelo anterior (se aplicável)?                       | ☐           |
| As ameaças foram convertidas em requisitos rastreáveis ou exceções justificadas com prazo definido? | ☐           |
| Existe rastreabilidade entre ameaça, requisito e controlo aplicado?                                 | ☐           |
| O modelo de ameaça está documentado no repositório ou plataforma usada pela equipa?                  | ☐           |

---

## 🔄 Integração Operacional {threat-modeling:canon:checklist-revisao#integracao_operacional}

- Este checklist pode ser integrado em **revisões de arquitetura, gates de release, pipelines CI/CD ou sessões de planeamento de sprint.**
- Cada item deve ser validado com **evidência objetiva**: modelos DFD, ficheiros STRIDE, comentários em PRs, links para requisitos no backlog, registos de sessões, etc.

> ⚠️ Em caso de resposta negativa, deve existir exceção formal documentada, com owner e prazo de reavaliação, conforme o modelo do Cap. 2.

---

## ✅ Conformidade e KPI {threat-modeling:canon:checklist-revisao#conformidade_e_kpi}

- A validação deste checklist permite declarar **conformidade com o Capítulo 3 — Threat Modeling**.
- A contagem de respostas afirmativas pode ser usada para **medir o grau de adoção das práticas prescritas**.
- Este resultado pode ser agregado por equipa, domínio ou organização como **indicador de maturidade e cobertura de risco**.

> 📌 Este mecanismo operacional está alinhado com o modelo de rastreabilidade e controlo contínuo definido no SbD-ToE.
