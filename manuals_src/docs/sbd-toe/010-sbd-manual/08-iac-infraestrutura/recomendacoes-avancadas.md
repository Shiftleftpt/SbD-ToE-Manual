---
id: recomendacoes-avancadas
title: Recomendações Avançadas para Segurança em Infraestrutura como Código (IaC)
sidebar_position: 30
description: Práticas reforçadas para contextos de maior maturidade ou requisitos regulatórios em projetos de IaC.
tags: [grupo:avancado, maturidade, reforço, tema:iac, tipo:anexo]
---


# 🔐 Recomendações Avançadas para IaC Seguro

Este anexo apresenta **práticas reforçadas** para segurança em projetos de **Infraestrutura como Código (IaC)**. As recomendações aqui descritas **não são obrigatórias**, mas devem ser consideradas em:

* Organizações com elevada maturidade de segurança;
* Ambientes regulados ou com requisitos de certificação;
* Projetos com elevada exposição ou risco (ex: infraestrutura crítica);
* Cadeias de fornecimento que exijam prova de conformidade (ex: SLSA, ISO 27001, DSOMM nível 3).

---

## 📌 Enforcement político e semântico com OPA / Sentinel

| Tema                               | Descrição                                                            |
| ---------------------------------- | -------------------------------------------------------------------- |
| OPA com regras Rego detalhadas     | Criar regras por tipo de recurso, ambiente, projeto                  |
| Enforcement com Sentinel (TFC/TFE) | Aplicar políticas de organização com gate de execução Terraform      |
| Linters com rulesets adaptados     | Uso de Conftest, Checkov ou tfsec com perfil customizado por projeto |
| Comparação com baseline de segurança | Validar desvios face a política por repositório/projeto             |
| Integração com CI/CD               | CI falha caso a execução viole políticas                             |

> 🎯 Reforça a confiança, uniformiza a aplicação de regras, permite provas de conformidade.

---

## 📊 Proveniência e rastreabilidade reforçada

| Tema                                 | Descrição                                                                   |
| ------------------------------------ | --------------------------------------------------------------------------- |
| Hash e retenção dos ficheiros `plan` | Cada execução deve gerar ficheiro `plan` com hash e retenção por versão     |
| Metadata de execução                 | Commit, branch, tag, utilizador, runner e hash associados ao plano aplicado |
| Versão do template IaC               | Incluir no repositório e no artefacto em deploy                             |
| Registo inviolável de aplicação      | Guardar o `plan` e `apply` efetivos em repositório auditável                |

> 📎 Facilita auditoria, rollback, comprovação de estado e análise forense.

---

## 🔁 Integração com custo e “drift”

| Tema                                 | Descrição                                                            |
| ------------------------------------ | -------------------------------------------------------------------- |
| Integração com `Infracost`           | Comparar custo estimado por `plan` com baseline aprovado             |
| Detecção contínua de drift           | Monitorização ativa de diferenças entre código e infraestrutura real |
| Alertas por modificações fora do Git | Verificação se `apply` ocorreu fora de PRs ou pipeline               |

> 🧩 A integração com custo e drift permite deteção precoce de anomalias, controlo financeiro e técnico.

---

## 🔐 Segurança na proveniência de módulos

| Tema                             | Descrição                                                                 |
| -------------------------------- | ------------------------------------------------------------------------- |
| Geração de SBOM dos templates    | Registar módulos, recursos, providers usados em formato legível           |
| Validação semântica de providers | Bloqueio de versões não auditadas ou não testadas                         |
| Substituição de fontes externas  | Especificar mirrors internos, registos privados, repositórios confiáveis  |
| Auditoria de mudanças em módulos | Validar se mudanças introduzem configurações inseguras (ex: ACLs abertas) |

> 💡 Estas práticas ajudam a tratar módulos IaC como software e sujeitos a SDLC seguro.

---

## 🧪 Testes programáticos de infraestrutura

| Tema                         | Descrição                                                                 |
|------------------------------|---------------------------------------------------------------------------|
| `terratest` com Go           | Testes de aplicação e rollback de recursos, validando outputs e rotas     |
| `opa test` para políticas    | Testes unitários para regras de segurança escritas em Rego                |
| `kitchen-terraform`          | Testes de integração de ambientes provisórios                             |
| Integração no pipeline       | Testes automáticos por PR ou release, com logs e resultados arquivados    |

> 🧬 Garante que a infraestrutura provisionada é funcional e segura, validando o comportamento além da sintaxe.

---

## 📋 Governação de exceções técnicas

| Tema                                | Descrição                                                                 |
|-------------------------------------|---------------------------------------------------------------------------|
| Validação de exceções com ciclo     | Cada exceção com owner, prazo, revisão formal                            |
| Auditoria de execuções com bypass   | Logs de bypass ou flags forçadas analisadas periodicamente               |
| Automação de reapreciação           | Jobs que sinalizam exceções expiradas ou por rever                       |
| Relatórios de exceções por stack    | Dashboards de conformidade por projeto e ambiente                         |

> 🧾 A governação contínua de exceções assegura que *"security debt"* técnico é visível, rastreável e revisto.

---

## ✅ Conclusão

Estas recomendações **não são obrigatórias**, mas constituem **reforços valiosos para equipas com maturidade elevada** ou que operam em contextos regulados.

> 📌 A sua aplicação reforça diretamente os domínios **Design & Development**, **Build & Test** e **Operate & Monitor** do OWASP DSOMM, permitindo atingir **maturidade de nível 3** em práticas de segurança aplicadas a IaC.

Para aplicações com classificacão de risco **L3**, recomenda-se considerar um subconjunto destas práticas como baseline obrigatória.
