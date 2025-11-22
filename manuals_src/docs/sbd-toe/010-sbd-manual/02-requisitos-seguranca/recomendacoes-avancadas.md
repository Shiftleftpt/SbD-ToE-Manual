---
id: recomendacoes-avancadas
title: Práticas Avançadas em Requisitos de Segurança
description: Recomendações reforçadas para ambientes com maior exigência regulatória ou maturidade
tags: [avancado, políticas, rastreabilidade, requisitos, validacao]
sidebar_position: 30
---

# 🧐 Práticas Avançadas em Requisitos de Segurança

Este anexo apresenta **práticas avançadas não obrigatórias** que podem ser adotadas por organizações com maior maturidade, exigência normativa (ex: PCI-DSS, ISO 26262, IEC 62443), ou necessidade de rastreabilidade e auditoria formal.

> Estas recomendações **não substituem** os requisitos do catálogo SbD-ToE, nem são consideradas no cálculo de maturidade ou mitigação de ameaças.  
> Servem como **extensão facultativa** para contextos críticos, e contribuem para o alinhamento com modelos como o **DSOMM** (Design & Development).

---

## 🔀 1. Rastreabilidade Automatizada

> **Objetivo**: Permitir rastreabilidade contínua entre requisitos, código, testes e validações.

- Usar ALM com suporte a rastreabilidade (ex: Codebeamer, Jama, Polarion, Jira + plugins)
- Criar **ligações bidirecionais** entre requisitos e artefactos
- Automatizar extração de coverage por requisito (ex: CI valida que REQ-XXX está coberto)

---

## 🧪 2. Critérios de Aceitação em BDD / Linguagem Formal

> **Objetivo**: Tornar os requisitos testáveis e verificáveis por máquina.

- Usar Gherkin (Given–When–Then) ou formatos equivalentes
- Para ambientes críticos, considerar linguagens como OCL, TLA⁺ ou modelos EARS
- Exemplo em Gherkin:

```gherkin
Feature: Autenticação multifator

  Scenario: Acesso por utilizador administrativo
    Given o utilizador possui privilégios de administrador
    When efetua login com credenciais válidas
    Then é solicitado a fornecer segundo fator de autenticação
```

---

## 📦 3. Catálogos Internos e Perfis de Requisitos

> **Objetivo**: Reutilizar e padronizar requisitos comuns por tipo de aplicação.

- Criar perfis por domínio (ex: API interna, mobile app)
- Manter templates versionados com REQ-IDs e critérios por tipo
- Validar os perfis com equipas técnicas e de arquitetura

---

## 📄 4. Integração com Threat Modeling

> **Objetivo**: Alinhar os requisitos com ameaças reais modeladas.

- Ligar REQ-IDs a threats (ex: REQ-VAL-002 mitiga [STRIDE] Input Validation)
- Justificar requisitos com outputs de modelos (ex: DFDs, IriusRisk)
- Usar marcações automatizadas com ferramentas como ThreatSpec ou Diagrams as Code

---

## 📊 5. Medição e Gestão de Coverage

> **Objetivo**: Monitorizar a definição, aplicação e validação de requisitos.

- Métricas úteis:
  - % com critérios definidos
  - % com testes automatizados
  - % validados em QA
  - % rastreáveis no backlog

- Gerar relatórios por release ou pipeline com estado de cobertura

---

## 🔐 6. Integração com Conformidade Regulatória

> **Objetivo**: Garantir que os requisitos cobrem controlos normativos obrigatórios.

- Manter mapeamento com:
  - PCI-DSS v4.0
  - ISO/IEC 27001 + 27002
  - NIST 800-53, 800-171
  - HIPAA, GDPR, ENS, etc.
- Criar camadas de requisitos regulatórios com tags (ex: `#PCI-REQ-8.3`)

---

## 🧠 7. Exemplos de Maturidade Elevada

| Prática                                 | Valor acrescentado                                  | Ferramentas sugeridas              |
|-----------------------------------------|-----------------------------------------------------|-------------------------------------|
| Lig. autom. entre REQ-ID e código      | Audibilidade e conformidade                         | Semgrep, GitHub Adv. Security      |
| Critérios em Gherkin                    | Testabilidade e validação contínua                | Cucumber, Behave                   |
| Rastreabilidade bidirecional            | Suporte a auditorias reguladas                      | Jama, Jira Traceability Matrix     |
| Métricas de coverage de requisitos      | Visibilidade e melhoria contínua                   | TestRail, dashboards customizados  |
| Perfis de requisitos internos           | Escalabilidade e padronização                     | Catálogo interno versionado        |

---

## ✅ Considerações Finais

Estas práticas **não são obrigatórias**, mas recomendadas quando:

- A organização está sujeita a certificações formais
- A criticidade exige rastreabilidade total
- Existem equipas grandes e multidisciplinares
- É necessário suportar auditorias de terceiros

> 📌 Este anexo pode ser estendido com exemplos reais e scripts de rastreabilidade automática.

---

## 🤖 8. Requisitos como Código (Policy as Code)

> **Objetivo**: Representar requisitos em formato estruturado e aplicável automaticamente.

- Usar YAML, Rego (OPA), JSON Schema, `.policy`
- Integrar com pipelines para validação automática
- Exemplo em Rego:

```rego
package security.requisitos

default permitir = false

permitir {
  input.req_id == "REQ-AUT-001"
  input.mfa_ativo == true
}
```

> 📍 Esta prática responde diretamente ao **DSOMM - Policy as Code**.

---

## 🧰 9. Requisitos Derivados de Princípios de Design Seguro

> **Objetivo**: Traduzir princípios de arquitetura em requisitos verificáveis.

- Mapear REQ-IDs para princípios como *Least Privilege*, *Fail Safe Defaults*
- Criar "Design Guidelines to REQ" mappings
- Garantir que decisões de arquitetura resultam em requisitos rastreáveis

> 🧐 Esta prática reforça o alinhamento com o **DSOMM - Design & Development**.
