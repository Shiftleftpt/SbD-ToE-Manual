---
id: ameacas-mitigadas
title: Ameaças Mitigadas
description: Ameaças mitigadas pelas práticas de segurança de CI/CD descritas neste capítulo
tags: [ameaças, mitigação, cicd, supply chain, osc&r, stride, dsomm]
sidebar_position: 50
---


# 🔐 Ameaças Mitigadas - Capítulo 07: CI/CD Seguro

Este capítulo define práticas para **segurança de pipelines CI/CD**, incluindo controlo de código-fonte, validações automáticas, proteção de runners, gestão de segredos, rastreabilidade e proveniência de artefactos.

> ⚠️ As ameaças mitigadas estão entre as mais críticas da cadeia de software moderno - como demonstrado pelos incidentes de SolarWinds, Codecov, CircleCI, entre outros.

---

## 🧨 Categoria 1 - Ataques à infraestrutura da pipeline

| Ameaça                                       | Fonte                                         | Como surge                                             | Como a prática mitiga                                                            | Controlos associados                          | 🧩 Mitigada apenas por este capítulo? |
|----------------------------------------------|-----------------------------------------------|--------------------------------------------------------|-----------------------------------------------------------------------------------|------------------------------------------------|----------------------------------------|
| Execução remota não autorizada               | STRIDE / MITRE T1190 / DSOMM Build            | Pipeline executa código malicioso                     | Controlo de origem, triggers e isolamento de eventos                             | `addon/01-design-seguro-pipelines.md`         | ✅                                     |
| Manipulação de ambientes de build            | OSC&R ENV-3 / SLSA Build Integrity / DSOMM Build | Injeção de comandos, configurações ou segredos         | Runners isolados e revalidados, ambientes limpos e efémeros                     | `addon/04-isolamento-runners.md`              | ✅                                     |
| Elevação de privilégios no pipeline          | OWASP CI/CD / CAPEC-233 / DSOMM Build         | Scripts com permissões excessivas                     | Hardening por step, restrição mínima de permissões                              | `addon/01-design-seguro-pipelines.md`         | ✅                                     |

---

## 🔐 Categoria 2 - Comprometimento do código-fonte

| Ameaça                                      | Fonte                                         | Como surge                                          | Como a prática mitiga                                                        | Controlos associados                          | 🧩 Mitigada apenas por este capítulo? |
|---------------------------------------------|-----------------------------------------------|-----------------------------------------------------|--------------------------------------------------------------------------------|------------------------------------------------|----------------------------------------|
| Push não autorizado para branch principal   | OWASP CI/CD / SSDF PW.3 / DSOMM Govern        | Falta de proteção de branches                       | Proteção de branches + PR com validações obrigatórias                         | `addon/00-gestao-segura-codigo-fonte.md`      | ✅                                     |
| Pipeline invocado com código não auditado   | OSC&R Code Execution / BSIMM / DSOMM Release  | Alteração direta no repositório                     | Regras de execução só em commits revistos e aprovados                          | `addon/06-politicas-gates-pipeline.md`        | ✅                                     |
| Substituição silenciosa de código legítimo  | SLSA Provenance / SSDF RV.1 / DSOMM Release   | Código alterado sem rasto ou proveniência           | Assinaturas e rastreio de proveniência desde o commit até à publicação         | `addon/08-rastreabilidade-assinaturas.md`     | ✅                                     |

---

## 📦 Categoria 3 - Risco de injeção de artefactos ou builds falsificados

| Ameaça                                       | Fonte                                             | Como surge                                              | Como a prática mitiga                                                            | Controlos associados                          | 🧩 Mitigada apenas por este capítulo? |
|----------------------------------------------|----------------------------------------------------|---------------------------------------------------------|-----------------------------------------------------------------------------------|------------------------------------------------|----------------------------------------|
| Build reproduzível falsificado               | SLSA Build L2 / CAPEC-233 / DSOMM Release         | Artefactos gerados fora da pipeline                    | Assinatura dos artefactos + restrição da cadeia de build                         | `addon/05-integridade-proveniencia.md`        | ✅                                     |
| Injecção de código em tempo de pipeline      | OWASP CI/CD / STRIDE / DSOMM Build               | Scripts com lógica dinâmica sem controlo               | Validação de código YAML + linters e revisão de pipelines                        | `addon/02-seguranca-codigo-pipeline.md`       | ✅                                     |
| Inclusão de ferramentas inseguras no build   | OSC&R ENV / OWASP SAMM / DSOMM Test              | Ações externas não verificadas                         | Allowlist de ações/plugins + revisão periódica                                  | `addon/06-politicas-gates-pipeline.md`        | ✅                                     |

---

## 🔑 Categoria 4 - Gestão insegura de segredos

| Ameaça                                 | Fonte                                 | Como surge                                           | Como a prática mitiga                                                          | Controlos associados                        | 🧩 Mitigada apenas por este capítulo? |
|----------------------------------------|----------------------------------------|------------------------------------------------------|----------------------------------------------------------------------------------|---------------------------------------------|----------------------------------------|
| Vazamento de credenciais via logs     | CAPEC-651 / OWASP CI/CD / DSOMM Operate | Segredos escritos em logs                            | Mascaramento automático e logging com política de exclusão                     | `addon/03-gestao-segredos-pipeline.md`      | ✅                                     |
| Segredos hardcoded ou em variáveis públicas | SSDF PW.5 / ISO 27001 A.9 / DSOMM Test | Uso de variáveis de ambiente mal geridas             | Cofre externo + injecção com restrições e ciclo de vida                        | `addon/03-gestao-segredos-pipeline.md`      | ✅                                     |
| Reutilização de segredos sem rotação | SLSA / SSDF RV.3 / DSOMM Operate        | Segredos válidos para múltiplos ambientes            | Política de rotação automática + ciclo de expiração                            | `15-aplicacao-lifecycle.md`           | ❌ Cap. 01                             |

---

## 🧾 Categoria 5 - Falta de validação e controlo sistemático

| Ameaça                                   | Fonte                                     | Como surge                                               | Como a prática mitiga                                                          | Controlos associados                        | 🧩 Mitigada apenas por este capítulo? |
|------------------------------------------|--------------------------------------------|----------------------------------------------------------|---------------------------------------------------------------------------------|---------------------------------------------|----------------------------------------|
| Falta de gates de segurança              | OWASP CI/CD / BSIMM13 / DSOMM Govern      | Qualquer código é promovido sem bloqueios                | Política de gates com regras por tipo de aplicação                             | `addon/06-politicas-gates-pipeline.md`      | ✅                                     |
| Pipeline não executa scanners            | SSDF PW.7 / OWASP SAMM / DSOMM Test       | Validações não integradas na automação                   | Execução obrigatória de validadores (SAST, SCA, secrets, etc.)                 | `addon/07-validacoes-seguranca-integradas.md`| ✅                                     |
| Não rastreabilidade entre execução e resultado | OSC&R Traceability / SSDF PW.5 / DSOMM Release | Não se sabe o que foi validado, nem quando               | Registo automático de execuções, resultados e evidência                        | `addon/08-rastreabilidade-assinaturas.md`   | ✅                                     |

---

## 🕵️ Categoria 6 - Exceções e visibilidade negligenciadas

| Ameaça                                     | Fonte                                   | Como surge                                           | Como a prática mitiga                                                            | Controlos associados                         | 🧩 Mitigada apenas por este capítulo? |
|--------------------------------------------|------------------------------------------|------------------------------------------------------|-----------------------------------------------------------------------------------|----------------------------------------------|----------------------------------------|
| Segurança desativada em tempo de build     | CAPEC-1003 / STRIDE / DSOMM Govern      | Steps de segurança desativados sem rastreio          | Política de exceção formal com justificação, owner e prazo                       | `addon/09-controle-excecoes-visibilidade.md` | ✅                                     |
| Decisões sem visibilidade para a equipa    | SSDF RM.3 / BSIMM Governance / DSOMM Operate | Configurações críticas mudadas sem rasto             | Log e alertas em alterações de segurança da pipeline                             | `addon/09-controle-excecoes-visibilidade.md` | ✅                                     |
| Falta de aprovação formal para bypass      | OWASP SAMM / DSOMM Govern               | Permissões técnicas sobrepõem processo de aprovação  | Integração de workflow de aprovação por função ou criticidade                   | `addon/09-controle-excecoes-visibilidade.md` | ✅                                     |

---

## ✅ Conclusão

O Capítulo 07 é o principal **mecanismo de defesa operacional contra ataques à pipeline e cadeia de fornecimento**, garantindo:

- Validação contínua e bloqueio automático de riscos;
- Rastreamento e verificação de proveniência de código e artefactos;
- Isolamento de execução e integridade da build;
- Gestão controlada de segredos e exceções.

> ✅ Pelo menos **12 ameaças são mitigadas exclusivamente por este capítulo**, sendo muitas delas **inalcançáveis por qualquer outro controlo posterior à execução da pipeline**.

> 📌 O capítulo é essencial para conformidade com **SLSA**, **SSDF**, **BSIMM**, **OWASP CI/CD**, **ENISA DevSecOps**, e para evitar falhas sistémicas na cadeia de produção de software.

> 🧩 As práticas descritas neste capítulo alinham-se diretamente com os cinco domínios operacionais do **OWASP DSOMM** - *Build*, *Test*, *Release*, *Operate* e *Govern* - mitigando ameaças estruturais e sistémicas da automação CI/CD moderna.
