---
id: checklist-revisao
title: Checklist – Deploy Seguro
sidebar_label: Checklist de Revisão
description: Verificação objetiva e binária da aplicação das práticas de deploy seguro num projeto específico.
tags: [checklist, controlo, deploy, rollback, validação]
sidebar_position: 20
---

# ✅ Checklist de Revisão Periódica — Deploy Seguro

Este checklist aplica-se a todas as aplicações em vias de serem colocadas em produção, especialmente as classificadas como L2 ou L3.
Serve como instrumento de verificação binária e auditável da **adoção prática das prescrições do Capítulo 11**, permitindo:

- Controlo formal da execução segura
- Verificação da existência de rollback testado
- Confirmação da validação operacional antes do deploy

> 🗓️ **Recomenda-se a sua revisão antes de qualquer release, rollback ou alteração de configuração relevante**, conforme indicado no `15-aplicacao-lifecycle.md`.

---

## 📋 Itens de Verificação

| Item                                                                                              | Verificado? |
|---------------------------------------------------------------------------------------------------|-------------|
| Existe aprovação formal para o deploy, com evidência documentada                                 | ☐           |
| Foram aplicadas validações funcionais e de segurança antes da promoção                           | ☐           |
| Existe SBOM atualizado ligado ao artefacto a promover                                             | ☐           |
| Todos os findings de segurança estão resolvidos ou formalmente justificados                      | ☐           |
| Existe plano de rollback validado para esta release                                               | ☐           |
| O rollback foi testado com sucesso em ambiente de staging                                         | ☐           |
| Existem mecanismos de deploy com reversibilidade imediata (blue/green, toggles, etc.)            | ☐           |
| O pipeline usado para a entrega está segregado, versionado e confiável                           | ☐           |
| Existe logging completo dos artefactos, owners, toggles e configurações aplicadas                | ☐           |
| As validações estão integradas em gates condicionais por criticidade (L1–L3)                     | ☐           |
| Existe evidência de aprovação de owners técnicos e AppSec                                         | ☐           |
| Estão definidos indicadores operacionais para acionar rollback automático (ex: métricas de erro) | ☐           |
| As releases anteriores são reversíveis e estão documentadas                                       | ☐           |
| Existe rastreabilidade entre decisão de go/no-go e evidência associada                           | ☐           |

---

## 🔄 Integração Operacional

- Este checklist pode ser integrado em **pipelines, fluxos de aprovação de release, gates de produção ou auditorias técnicas**.
- Cada item deve ser validado com **evidência objetiva** (ex: logs de aprovação, ficheiros SBOM, relatórios de rollback, prints do pipeline).
- Os resultados podem ser ligados ao ciclo de vida do artefacto, da aplicação ou do serviço.

> ⚠️ Em caso de resposta negativa, deve existir exceção formal aprovada e documentada conforme o modelo do capítulo.

---

## ✅ Conformidade e KPI

- A validação deste checklist permite declarar **conformidade com o Capítulo 11 — Deploy Seguro**.
- A contagem de respostas afirmativas pode ser usada para **medir o grau de adoção das práticas prescritas**.
- Este resultado pode ser agregado por equipa, domínio ou organização como **indicador de maturidade operacional**.

> 📌 Este mecanismo de controlo está alinhado com o modelo de confiança rastreável e reversível defendido pelo SbD-ToE.
