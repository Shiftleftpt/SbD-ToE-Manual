---
id: controle-enforcement
title: Controlo de Execução e Enforcement de Políticas em IaC
sidebar_position: 6
description: Mecanismos técnicos e organizacionais para garantir o enforcement automático de políticas de segurança em pipelines IaC.
tags: [enforcement, controlo, políticas, iac, pipelines, segurança]
---


# 🛡️ Enforcement Contínuo de Políticas e Regras de Segurança em IaC

## 🌟 Objetivo

Assegurar que todos os projetos de Infraestrutura como Código (IaC) cumprem requisitos mínimos de segurança através de **enforcement automático e validado** de políticas técnicas, sem depender exclusivamente de revisão humana.

> O enforcement é um mecanismo crítico de proteção organizacional e deve ser tratado como parte integrante do ciclo de vida de segurança de qualquer projeto IaC.

---

## 🔖 O que deve ser feito

1. **Definir políticas organizacionais de segurança para IaC**, com base em requisitos e boas práticas;
2. **Traduzir essas políticas em regras executáveis** (ex: OPA, Sentinel, Rego);
3. **Integrar o enforcement nos pipelines CI/CD**, com bloqueio de merges ou aplicações em caso de violação;
4. **Manter um repositório centralizado de regras**, versionado, auditável e com gestão de aprovações;
5. **Permitir exceções rastreáveis e com prazo**, validadas por equipas de segurança;
6. **Avaliar continuamente a eficácia das regras aplicadas** e rever conforme ameaças evoluem.

---

## ⚖️ Como deve ser feito

| Componente          | Prática recomendada                                                  |
| ------------------- | -------------------------------------------------------------------- |
| Engine de políticas | OPA/Rego, Sentinel, Conftest, InSpec                                 |
| Formato             | Regras declarativas em YAML, Rego, JSON schemas ou equivalente       |
| Trigger             | Execução obrigatória em pull request, no pre-merge ou pre-apply      |
| Feedback            | Output legível para humanos com explicação por regra falhada         |
| Logging             | Armazenamento central dos resultados por projeto, commit, PR e autor |
| Exceções            | Definidas por regra, justificadas, rastreáveis, aprovadas por AppSec |

---

## 🗓️ Quando aplicar

| Momento               | Ação esperada                                                          |
| --------------------- | ---------------------------------------------------------------------- |
| PR com mudança em IaC | Execução obrigatória de políticas de conformidade                      |
| Pre-apply em staging  | Validação de segurança com regras Rego ou Sentinel                     |
| Revisão de regras     | Atualização em base trimestral ou a cada mudança relevante no contexto |
| Detecção de bypass    | Alerta imediato + revisão do pipeline e da regra falhada               |

---

## 💼 Exemplos práticos

### ✏️ Exemplo de regra Rego (OPA)

```rego
deny[msg] {
  input.resource_type == "aws_s3_bucket"
  not input.tags.Environment
  msg := "Missing 'Environment' tag on S3 bucket."
}
```

### 🌍 Integração em pipeline GitHub Actions

```yaml
- name: Run policy check
  run: conftest test ./iac/envs/prod
```

---

## 📈 Benefícios diretos

* Reforça segurança preventiva e sistemática
* Garante conformidade organizacional com requisitos definidos
* Reduz dependência de revisão manual de código
* Facilita auditoria e resposta a incidentes
* Aumenta confiança no uso de IaC em ambientes críticos

---

> 🔗 Este ficheiro está alinhado com os requisitos `IAC-009`, `REQ-005`, `REQ-006`, com boas práticas de SSDF (PW\.5), SLSA (Build L3), SAMM (AA2.3), e BSIMM (CMVM2.1).
