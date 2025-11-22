---
id: 02-praticas-release-management
title: Práticas de Release Management
description: Estratégias para gestão segura de releases e segregação de funcionalidades durante a entrega contínua.
tags: [grupo:execucao, seguranca, staging, tema:release, tipo:anexo]
---


# 🚀 Práticas de Release Management com Foco em Segurança

## 🌟 Objetivo

Descrever e sistematizar práticas seguras de **gestão de versões, releases e distribuição de software**, com foco em:

- Redução de risco e impacto em produção;
- Validação formal e rastreabilidade da decisão;
- Reversibilidade e recuperação rápida;
- Alinhamento com frameworks normativos (SSDF, SLSA, SAMM).

---

## 🧬 O que é Release Management Seguro

Release Management é o processo de **preparação, aprovação, distribuição e monitorização de uma nova versão de software**. Uma release segura deve:

- Ser previsível, validada e reversível;
- Ter ownership definido e critérios de aprovação;
- Ser acompanhada de documentação técnica e de segurança;
- Incluir mecanismos formais de rollback.

---

## 🛠️ Como aplicar

### 🗂️ Elementos essenciais de uma release segura

| Elemento                       | Descrição                                                                 |
|--------------------------------|---------------------------------------------------------------------------|
| **Changelog técnico**          | Lista de alterações relevantes, incluindo patches de segurança           |
| **Changelog de segurança**     | Destaque de CVEs corrigidos, dependências alteradas ou features críticas |
| **Owner de release**           | Pessoa ou equipa responsável pela release                                |
| **Checklist de aprovação**     | Critérios mínimos antes de produção (ex: findings resolvidos)            |
| **Plano de rollback**          | Estratégia clara e testada para regressar à versão anterior              |
| **Validações integradas**      | Testes automatizados, revisões, scan de SBOM, alertas                    |
| **Critérios de ativação**      | Condições de toggle, âmbito e aprovação de funcionalidade                |

---

### 🧪 Validações recomendadas por nível de risco

| Nível de Risco | Validações mínimas antes de produção                                            |
|----------------|---------------------------------------------------------------------------------|
| **L1 (baixo)** | Checklists manuais, validação funcional básica                                 |
| **L2 (médio)** | Aprovação dupla, revisão AppSec, scan de dependências                          |
| **L3 (elevado)**| Validação formal, fuzzing, análise de impacto, rollback validado em staging   |

---

### ✅ Exemplo de checklist de release (mínimo recomendado)

- [ ] Todos os testes passaram em CI/CD
- [ ] Findings críticos resolvidos ou justificados
- [ ] SBOM atualizado e assinado
- [ ] Plano de rollback definido e validado
- [ ] Toggles e feature flags documentados
- [ ] Logs e métricas definidas para observação
- [ ] Aprovação por owner funcional e reviewer técnico
- [ ] Release registada com hash, versão e data

> 💡 Este checklist pode ser usado como *gate* no pipeline de produção.

---

## 🔁 Versionamento e Reversibilidade

### 📁 Versionamento seguro

- Usar **versionamento semântico** (`MAJOR.MINOR.PATCH`) com convenções documentadas;
- Associar a cada release:
  - Hash de commit ou build;
  - Data e hora;
  - Owner / equipa responsável;
  - Justificação (ex: fix urgente, nova feature, refactor).

### 📉 Rollback

- Deve ser planeado como parte da release, não como exceção;
- Deve permitir:
  - Restaurar versão anterior sem perda de estado;
  - Desativar toggles de funcionalidades críticas;
  - Inverter migrações de base de dados (quando viável);
- Incluir testes de rollback como parte da validação pré-produção.

---

## 📊 Indicadores de risco por release

- Nº de toggles ativos;
- Nº de findings abertos;
- Nº de alterações manuais (vs automáticas);
- Score de cobertura de testes;
- Nível de confiança definido pelo owner (`alta / média / experimental`).

---

## 🧰 Ferramentas de suporte

| Categoria        | Ferramentas recomendadas                          |
|------------------|---------------------------------------------------|
| Versionamento    | Git tags, GitHub Releases                         |
| Aprovação        | Azure DevOps, Jira workflows                      |
| Releases declarativas | Argo CD, Flux, Spinnaker                    |
| Observabilidade  | Dashboards com métricas por release (ex: Grafana) |

---

## ✅ Boas práticas

- Integrar segurança no processo de release (shift-left + shift-right);
- Exigir aprovação explícita para releases em produção;
- Evitar releases manuais fora do processo documentado;
- Documentar todos os passos, alterações e decisões;
- Garantir testes de rollback e fallback antes do go-live;
- Automatizar a geração e associação de SBOMs à release;
- Rastrear cada release com artefactos versionados.

---

## 📎 Referências cruzadas

| Documento / Capítulo         | Relação com este tema                       |
|------------------------------|---------------------------------------------|
| Cap. 07 - CI/CD Seguro       | Processo automatizado e controlos por stage |
| Cap. 05 - Dependências e SBOM| SBOM como requisito para release            |
| Cap. 10 - Testes de Segurança| Validação antes do deploy                   |
| Cap. 12 - Monitorização      | Observação pós-release                      |
| SLSA L3/L4                   | Proveniência de release e rollback seguro   |
| NIST SSDF PM.3, RV.1         | Aprovação formal e gestão de riscos         |

---

> 🎯 A gestão de releases deve ser tratada como um processo formal e seguro - **não como simples deploy técnico**.  
> Um bom processo de release é essencial para sustentar práticas avançadas de segurança e garantir confiança nas alterações entregues.
