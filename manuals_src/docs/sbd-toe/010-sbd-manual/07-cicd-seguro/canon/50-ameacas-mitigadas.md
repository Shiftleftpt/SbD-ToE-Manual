---
id: ameacas-mitigadas
title: Ameaças Mitigadas
description: Ameaças mitigadas pelas práticas de segurança de CI/CD descritas neste capítulo
tags: [ameaças, mitigação, cicd, supply chain, osc&r, stride, dsomm]
sidebar_position: 50
---

# 🔐 Ameaças Mitigadas – Capítulo 07: CI/CD Seguro

O Capítulo 07 define práticas de **segurança operacional para pipelines CI/CD**, tratando o pipeline como **ativo crítico da cadeia de fornecimento de software**.

As ameaças aqui tratadas correspondem a vetores explorados em incidentes reais (ex.: SolarWinds, Codecov, CircleCI) e a riscos estruturais identificados em **OSC&R**, **SLSA**, **OWASP CI/CD**, **ENISA DevSecOps** e **OWASP DSOMM**.

---

## 🧨 Categoria 1 – Ataques à infraestrutura da pipeline

| Ameaça | Fonte | Como surge | Como a prática mitiga | Controlos associados | Apenas Cap. 07? |
|------|------|-----------|-----------------------|----------------------|-----------------|
| Execução de código não autorizado em pipeline | OSC&R CI0001 / ATT&CK T1059 / DSOMM Build | Execução de scripts maliciosos em jobs | Triggers restritos, revisão de pipeline, isolamento de runners | Design seguro de pipelines; isolamento de runners | ✅ |
| Comprometimento do ambiente de build | OSC&R ENV0003 / SLSA Build Integrity | Injeção de estado persistente ou tooling malicioso | Runners efémeros e ambientes limpos | Isolamento e efemeridade de runners | ✅ |
| Elevação de privilégios no pipeline | CAPEC-233 / DSOMM Build | Jobs com permissões excessivas | Princípio do menor privilégio por step | Hardening de pipelines | ✅ |

---

## 🔐 Categoria 2 – Comprometimento do código-fonte

| Ameaça | Fonte | Como surge | Como a prática mitiga | Controlos associados | Apenas Cap. 07? |
|------|------|-----------|-----------------------|----------------------|-----------------|
| Push não autorizado para branches protegidas | OWASP CI/CD / SSDF PW.3 | Falta de branch protection | PR obrigatório + validações | Gestão segura de código-fonte | ❌ Cap. 02 |
| Execução de código não auditado | OSC&R CI0011 / DSOMM Release | Execução direta sem revisão | Execução apenas em commits aprovados | Políticas de execução | ❌ Cap. 02 |
| Substituição silenciosa de código legítimo | SLSA Provenance / SSDF RV.1 | Alteração sem proveniência | Assinatura e proveniência end-to-end | Rastreabilidade e assinaturas | ❌ Cap. 05 |

---

## 📦 Categoria 3 – Artefactos falsificados e supply chain

| Ameaça | Fonte | Como surge | Como a prática mitiga | Controlos associados | Apenas Cap. 07? |
|------|------|-----------|-----------------------|----------------------|-----------------|
| Build forjado fora da pipeline | SLSA Threats / DSOMM Release | Artefactos externos ao pipeline | Assinatura + rejeição automática | Integridade e proveniência | ❌ Cap. 05 |
| Injeção de lógica dinâmica em pipeline | OWASP CI/CD / DSOMM Build | YAML/scripts dinâmicos | Revisão e validação de pipeline | Segurança do código de pipeline | ✅ |
| Uso de componentes externos inseguros | OSC&R SC0001 | Actions/scripts não verificados | Allowlist e pinning | Controlo de dependências | ❌ Cap. 05 |

---

## 🔑 Categoria 4 – Gestão insegura de segredos

| Ameaça | Fonte | Como surge | Como a prática mitiga | Controlos associados | Apenas Cap. 07? |
|------|------|-----------|-----------------------|----------------------|-----------------|
| Vazamento de segredos via logs | CAPEC-651 / DSOMM Operate | Logs excessivos | Mascaramento e política de logging | Gestão de segredos | ✅ |
| Segredos hardcoded | SSDF PW.5 / ISO 27001 A.9 | Variáveis expostas | Cofre + injeção controlada | Gestão de segredos | ❌ Cap. 02 |
| Reutilização de segredos | SSDF RV.3 / DSOMM Operate | Tokens long-lived | Rotação e TTL curto | Lifecycle de segredos | ❌ Cap. 01 |

---

## 🧾 Categoria 5 – Falhas de validação e controlo

| Ameaça | Fonte | Como surge | Como a prática mitiga | Controlos associados | Apenas Cap. 07? |
|------|------|-----------|-----------------------|----------------------|-----------------|
| Ausência de gates de segurança | OWASP CI/CD / DSOMM Govern | Promoção sem bloqueios | Gates por risco (L1–L3) | Políticas de gates | ✅ |
| Validações não executadas | SSDF PW.7 / DSOMM Test | Scanners fora do pipeline | Execução obrigatória | Validações integradas | ❌ Cap. 10 |
| Falta de rastreabilidade | OSC&R CI0016 | Resultados sem origem | Registo automático de execuções | Rastreabilidade | ❌ Cap. 02 |

---

## 🕵️ Categoria 6 – Exceções e visibilidade

| Ameaça | Fonte | Como surge | Como a prática mitiga | Controlos associados | Apenas Cap. 07? |
|------|------|-----------|-----------------------|----------------------|-----------------|
| Bypass de controlos sem rasto | DSOMM Govern | Desativação manual | Workflow de exceções | Gestão de exceções | ❌ Cap. 14 |
| Alterações críticas sem visibilidade | SSDF RM.3 | Mudanças silenciosas | Logging e alertas | Governação contínua | ❌ Cap. 14 |

---

## ⚙️ Categoria 7 – Riscos de processo em CI/CD moderno

| Ameaça | Fonte | Como surge | Como a prática mitiga | Controlos associados | Apenas Cap. 07? |
|------|------|-----------|-----------------------|----------------------|-----------------|
| Promoções sem responsável humano | DSOMM Govern | Automação implícita | Aprovação nominativa | Gates e governação | ✅ |
| Evidência plausível sem execução | ENISA DevSecOps | Relatórios sintéticos | Exigir execução observável | Evidência empírica | ✅ |
| Não-determinismo do pipeline | SLSA Threats | Configuração implícita | Registo da config efetiva | Reprodutibilidade | ✅ |
| Exfiltração de contexto sensível | OSC&R CI0014 | Integrações externas | Minimização de contexto | Controlo de integrações | ✅ |

---

## ✅ Conclusão

O Capítulo 07 é o **principal mecanismo de defesa operacional da supply chain de software**, mitigando ameaças que **não podem ser resolvidas após a execução da pipeline**.

Este capítulo:
- cobre ameaças técnicas e de processo;
- complementa, mas não substitui, controlos basilares;
- é essencial para conformidade com **SLSA**, **SSDF**, **DSOMM**, **OWASP CI/CD** e **ENISA DevSecOps**.

> 🔐 Muitas das ameaças aqui tratadas são **mitigáveis exclusivamente no momento de CI/CD**. Uma vez ultrapassada essa fase, o risco propaga-se inevitavelmente para produção.
