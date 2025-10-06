---
id: threat-modeling-ci
title: Threat Modeling em CI/CD
description: Requisitos e validações práticas para garantir a existência, integridade e impacto do threat modeling no ciclo de vida CI/CD
tags: [ci, cd, devsecops, threat modeling, automação, validação, iriusrisk]
---

# ⚙️ Threat Modeling em CI/CD {threat-modeling:addon:threat-modeling-ci}

## 🌟 Objetivo {threat-modeling:addon:threat-modeling-ci#objetivo}

Definir como garantir — de forma testável e automatizável — que a atividade de *threat modeling*:

- Foi realizada e está atualizada;
- Produziu artefactos rastreáveis e úteis para o projeto;
- Influenciou decisões reais e controlos de segurança;
- Está integrada no ciclo de vida via CI/CD;
- Cumpre requisitos de frameworks como NIST SSDF, SAMM ou SLSA.

---

## 📌 Requisitos mínimos por projeto {threat-modeling:addon:threat-modeling-ci#requisitos_minimos_por_projeto}

A presença de threat modeling não pode ser apenas simbólica: deve resultar em **artefactos rastreáveis, controlos efetivos e validações mensuráveis**.

| Elemento obrigatório                           | Descrição                                                                 |
| ---------------------------------------------- | ------------------------------------------------------------------------- |
| Modelo de ameaça versionado                    | Diagrama DFD (`dfd.drawio`, `dfd.mmd`), lista de ameaças (`threats.yaml`) |
| Mapeamento threat → requisito → controlo       | Ficheiro `mitigations.md` com status e referência cruzada                 |
| Justificações documentadas para riscos aceites | Ficheiro `decisions.md` com data, autor, razão de aceitação               |
| Rastreabilidade no backlog ou código           | Identificadores como `TM-001` ou `REQ-AC-003` referenciados em PRs/issues |
| Data da última revisão                         | Campo `last_reviewed` num ficheiro `threat-model.yml`                     |

---

## 🧲 Como validar no pipeline (CI/CD) {threat-modeling:addon:threat-modeling-ci#como_validar_no_pipeline_cicd}

A pipeline de CI/CD deve verificar não apenas a presença de ficheiros, mas também se:

- Estão atualizados face a alterações no código;
- Foram usados como base para decisões de desenvolvimento;
- Geraram tickets, commits ou testes relacionados.

| Etapa           | Validação recomendada                                                |
| --------------- | -------------------------------------------------------------------- |
| `pre-commit`    | Ficheiros obrigatórios existem (`dfd`, `threats.yaml`)               |
| `build`         | Linting dos modelos (`yaml`, `mermaid`), parsing de `mitigations.md` |
| `security test` | Ligação threat → controlo existe (ou tem justificação)               |
| `release`       | Última revisão foi realizada + ameaças críticas têm planos definidos |

---

## ✅ Checklist CI/CD de conformidade mínima {threat-modeling:addon:threat-modeling-ci#checklist_cicd_de_conformidade_minima}

| Item                                                                | Verificado |
| ------------------------------------------------------------------- | ---------- |
| Estrutura `/threat-model/` presente no repositório                  | ☑️         |
| Ficheiros principais existem (`dfd`, `threats.yaml`, `mitigations`) | ☑️         |
| Ficheiro `mitigations.md` ou `yaml` tem estado definido por threat  | ☑️         |
| `decisions.md` documenta riscos aceites com data + justificação     | ☑️         |
| Commits ou issues referenciam ameaças (`TM-001`, etc.)              | ☑️         |
| Última revisão do modelo realizada nos últimos 30 dias              | ☑️         |

---

## 📂 Estrutura sugerida do modelo {threat-modeling:addon:threat-modeling-ci#estrutura_sugerida_do_modelo}

```
📁 threat-model/
📌 README.md              # Escopo e método
📌 dfd.drawio             # Diagrama técnico ou .mmd (Mermaid)
📌 threats.yaml           # Lista de ameaças (id, descrição, severidade, requisito associado)
📌 mitigations.md         # Tabela com status (mitigado, em curso, aceite)
📌 decisions.md           # Justificações de risco aceite
📌 threat-model.yml       # Metadados: última revisão, revisores, etc.
```

---

## 🛠️ Exemplos práticos e validações automatizadas {threat-modeling:addon:threat-modeling-ci#exemplos_praticos_e_validacoes_automatizadas}

### Linting de artefactos: {threat-modeling:addon:threat-modeling-ci#linting_de_artefactos}

```yaml
- name: Verificar syntax YAML
  run: yamllint threat-model/threats.yaml
```

### Validação de referências cruzadas: {threat-modeling:addon:threat-modeling-ci#validacao_de_referencias_cruzadas}

```bash
grep -E 'TM-[0-9]{3}' threat-model/mitigations.md \
  | while read threat_id; do
    git log --oneline | grep "$threat_id" || echo "❌ Threat $threat_id sem commit associado"
  done
```

### Verificar última revisão: {threat-modeling:addon:threat-modeling-ci#verificar_ultima_revisao}

```bash
REVIEWED=$(yq '.last_reviewed' threat-model/threat-model.yml)
if [ "$REVIEWED" < "$(date -d '30 days ago' +%F)" ]; then
  echo "❌ Threat model desatualizado"; exit 1;
fi
```

---

## 🔄 Integração com IriusRisk {threat-modeling:addon:threat-modeling-ci#integracao_com_iriusrisk}

### 🧠 O que IriusRisk pode fazer automaticamente: {threat-modeling:addon:threat-modeling-ci#o_que_iriusrisk_pode_fazer_automaticamente}

| Capacidade                              | Detalhe                                               |
| --------------------------------------- | ----------------------------------------------------- |
| Derivar ameaças com base em componentes | Templates modelam ameaças por tipo (ex: JWT, API, S3) |
| Gerar requisitos e controlos            | Automático, com criticidade e estado                  |
| Exportar dados via API                  | JSON/YAML para integração com CI/CD                   |
| Criar tickets em Jira / ADO             | Integração com fluxos de backlog                      |

### 🧲 O que ainda precisa ser verificado no CI/CD: {threat-modeling:addon:threat-modeling-ci#o_que_ainda_precisa_ser_verificado_no_cicd}

| Validação necessária                         | Como fazer                                                 |
| -------------------------------------------- | ---------------------------------------------------------- |
| As ameaças exportadas têm controlo aplicado? | Scripts cruzam IDs com código, PRs ou testes               |
| As justificativas estão documentadas?        | `decisions.md` extraído do IriusRisk ou mantido localmente |
| A revisão foi recente?                       | Verificar metadados ou sincronização com API               |

---

## ⚠️ Comportamento esperado da pipeline {threat-modeling:addon:threat-modeling-ci#comportamento_esperado_da_pipeline}

| Tipo de falha                                 | Reação recomendada da pipeline    |
| --------------------------------------------- | --------------------------------- |
| Modelo inexistente                            | ❌ Falha crítica                   |
| Modelo desatualizado (> 30 dias)              | ⚠️ Alerta + bloqueio condicional  |
| Threats não mitigadas nem justificadas        | ⚠️ Aviso + requer issue/documento |
| Linting falha (YAML, Mermaid inválido)        | ❌ Build falha                     |
| Nenhuma ligação entre threat e código/backlog | ⚠️ Alerta para revisão manual     |

---

## ✅ Boas práticas {threat-modeling:addon:threat-modeling-ci#boas_praticas}

- Tratar threat modeling como **artefacto obrigatório e verificável**;
- Garantir rastreabilidade entre ameaça, controlo, requisito e backlog;
- Automatizar validações de frescura e cobertura na pipeline;
- Integrar resultados com ferramentas de gestão de risco (ex: IriusRisk);
- Incluir referência a ameaças em commits, issues e PRs relevantes.

---

## 📎 Referências cruzadas {threat-modeling:addon:threat-modeling-ci#referencias_cruzadas}

| Documento                      | Relação com este ficheiro                            |
|-------------------------------|------------------------------------------------------|
| `addon/06-metodologias-e-ferramentas.md` | Metodologias e ferramentas recomendadas para threat modeling |
| `addon/01-metodologia-base.md`            | Estratégia geral para threat modeling no SbD-ToE             |
| `canon/15-aplicacao-lifecycle.md`         | Aplicação ao ciclo de vida e user stories                   |

---

## 🛍️ Considerações finais {threat-modeling:addon:threat-modeling-ci#consideracoes_finais}

O objetivo do CI/CD não é apenas **detetar a presença do modelo**, mas **confirmar o seu impacto real no projeto**.
Este impacto manifesta-se em:

- Decisões documentadas;
- Mitigações implementadas;
- Requisitos derivados;
- Riscos aceites com responsabilidade.

> Esta abordagem reforça a rastreabilidade e dá evidência concreta do cumprimento de *Security by Design* com Threat Modeling.
