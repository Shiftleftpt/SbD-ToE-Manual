---
id: politicas-gates-pipeline
title: Políticas e Gates por Nível de Aplicação
sidebar_position: 6
description: Definição de políticas automáticas no pipeline com gates de segurança que variam segundo o nível de risco da aplicação.
tags: [cicd, gates, políticas, risco, segurança, validações]
---


# 🛂 Políticas e gates por nível de aplicação

Nem todas as aplicações requerem o mesmo nível de segurança, mas **todas devem obedecer a políticas claras**, proporcionais ao seu risco. Esta prática define a aplicação automatizada de **políticas, gates e controlos por nível de aplicação**, garantindo que:

- A criticidade dita o rigor dos mecanismos de controlo;
- O bypass só é possível mediante justificação formal e auditável.

> A ausência de política clara leva inevitavelmente a pipelines inconsistentes e permissivos.

---

## 🎯 Objetivos

- Impedir que aplicações críticas avancem no pipeline sem validações obrigatórias;
- Assegurar que políticas de segurança são aplicadas de forma coerente, automática e auditável;
- Prevenir bypass informal de etapas críticas no CI/CD.

---

## 🛠️ Práticas

1. **Classificação explícita da aplicação (L1–L3)**  
   - O nível de risco da aplicação deve estar definido (ex: em ficheiro `.risk-level.yml`, variável de ambiente, tag do repositório);
   - Essa classificação deve condicionar o comportamento do pipeline.

2. **Aplicação condicional de políticas e controlos**  
   - Aplicações L3 requerem proveniência assinada, revisão formal de findings, cobertura mínima, etc.;
   - As políticas devem ser codificadas diretamente no pipeline (ex: YAML templates, workflows condicionais, policy-as-code).

3. **Gates de segurança automáticos e bloqueantes**  
   - Verificações automatizadas devem impedir o avanço do pipeline se controlos não forem cumpridos;
   - Devem ser obrigatórios para níveis L2 e L3 (ex: SAST, coverage, SBOM, análise de findings).

4. **Gestão formal de exceções e bypass**  
   - Exceções devem ser registadas, justificadas e aprovadas formalmente (ex: via `change request`);
   - Não é permitido avançar com aplicações críticas sem validação explícita de segurança.

5. **Revisão e atualização periódica das políticas**  
   - As políticas devem ser mantidas em templates versionados e auditáveis;
   - Deve haver mecanismo de verificação da versão da política aplicada (ex: `policy-version.yml`).

---

## ⚖️ Aplicação proporcional por nível de risco

| Nível | Requisitos de política                                     | Critérios de bloqueio                                   |
|-------|-------------------------------------------------------------|----------------------------------------------------------|
| **L1** | Regras básicas (ex: build clean, SAST leve)                 | Build falha com erro crítico                             |
| **L2** | Findings validados; cobertura mínima; segredos verificados | Findings de severidade alta impedem promoção             |
| **L3** | Gates completos: SAST, DAST, IaC, SBOM, proveniência        | Só avança com aprovação formal de segurança              |

---

## 📌 Exemplos práticos

- **GitHub Actions**  
  - Workflows condicionais com `.risk-level.yml`;  
  - `required status checks` para gates específicos (SAST passed, coverage OK).

- **GitLab CI**  
  - `rules:` com variáveis como `APP_CRITICALITY=L3`;  
  - Etapas `when: manual` com aprovação de segurança para L3.

- **Azure DevOps**  
  - `Environments` com `approval gates` e `branch protection`;  
  - YAML + políticas de branch para enforce condicional.

- **Jenkins**  
  - Uso de `when { expression { isCritical() } }` para ativar etapas reforçadas;  
  - Integração com ferramentas de policy-as-code (ex: Open Policy Agent – OPA).

---

## 📉 Riscos mitigados

- Deploys de aplicações críticas sem validação obrigatória (OSC&R: CI0006, CI0014);
- Divergência entre política organizacional e o que o pipeline aplica;
- Bypass informal ou acidental de etapas de segurança (OSC&R: CI0002).

---

## 🧭 Referências

- [OWASP CI/CD Security – 6. Policy Enforcement](https://owasp.org/www-project-cicd-security/#6-policy-enforcement)
- [NIST SSDF – Governance (GV.x)](https://csrc.nist.gov/publications/detail/sp/800-218/final)
- [Open Policy Agent (OPA)](https://www.openpolicyagent.org/)
- [SLSA – Policy Controls & Provenance Gates](https://slsa.dev/spec/v1.0/)
- [BSIMM – SM1.2, CR1.4]
- [SAMM – Governance – Policy & Compliance Automation]
