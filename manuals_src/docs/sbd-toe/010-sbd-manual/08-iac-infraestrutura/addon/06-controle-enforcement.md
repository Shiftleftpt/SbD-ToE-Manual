---

id: controle-enforcement
title: Controlo de Execução e Enforcement de Políticas em IaC
sidebar_position: 6
description: Mecanismos técnicos e organizacionais para garantir o enforcement automático de políticas de segurança em pipelines IaC.
tags: [enforcement, controlo, políticas, iac, pipelines, segurança]
-------------------------------------------------------------------

# 🛡️ Enforcement Contínuo de Políticas e Regras de Segurança em IaC

## 🌟 Objetivo

Assegurar que todos os projetos de Infraestrutura como Código (IaC) cumprem **requisitos mínimos de segurança de forma automática, consistente e verificável**, através de mecanismos de *policy enforcement* integrados no ciclo de vida de desenvolvimento e operação.

Este ficheiro define **como as políticas são aplicadas tecnicamente**, não quais são as políticas — essa definição ocorre nos requisitos e nas políticas organizacionais.

> O enforcement é um **mecanismo estrutural de defesa**: quando falha, a organização depende apenas de disciplina humana.

---

## 🔖 O que deve ser feito

1. Definir **políticas organizacionais formais** aplicáveis a IaC (segurança, identidade, rede, dados);
2. Traduzir essas políticas em **regras executáveis e testáveis** (*policy-as-code*);
3. Integrar o enforcement de forma **bloqueante** nos pipelines CI/CD (pre-merge, pre-apply);
4. Centralizar as regras num **repositório controlado**, com versionamento e aprovação formal;
5. Permitir **exceções temporárias**, justificadas, rastreáveis e com *expiry* automático;
6. Medir e rever continuamente a eficácia do enforcement (bloqueios, exceções, bypass).

---

## ⚖️ Como deve ser feito

| Componente          | Prescrição técnica                                                  |
| ------------------- | ------------------------------------------------------------------- |
| Engine de políticas | OPA/Rego, Sentinel (HashiCorp), Conftest, InSpec                    |
| Modelo              | *Policy-as-Code* declarativo, versionado e testável                 |
| Trigger             | Execução obrigatória em PR/MR, *pre-merge* e *pre-apply*            |
| Severidade          | Classificação por impacto (warn / block), alinhada com L1–L3        |
| Feedback            | Mensagens claras e acionáveis por regra violada                     |
| Logging             | Registo central de resultados por projeto, commit, autor e ambiente |
| Exceções            | Controladas por regra, com justificação, TTL e aprovação AppSec/GRC |

---

## 🗓️ Quando aplicar

| Momento                      | Ação esperada                                    |
| ---------------------------- | ------------------------------------------------ |
| Pull Request com IaC         | Execução obrigatória de *policy checks*          |
| Pre-apply em ambientes reais | Enforcement bloqueante antes de qualquer `apply` |
| Atualização de políticas     | Revisão e *rollout* controlado das regras        |
| Detecção de bypass           | Alerta imediato + análise de causa raiz          |

---

## 💼 Exemplos práticos

### ✏️ Exemplo de regra Rego (OPA)

```rego
deny[msg] {
  input.resource_type == "aws_s3_bucket"
  not input.tags.Environment
  msg := "Missing mandatory 'Environment' tag on S3 bucket"
}
```

### 🌍 Integração em pipeline (GitHub Actions)

```yaml
- name: Policy enforcement (OPA)
  run: conftest test ./iac/envs/prod
```

**Resultado esperado:**

* Violação → *fail* imediato do job;
* Mensagem clara associada à regra;
* Evidência persistida para auditoria.

---

## 📈 Benefícios diretos

* Redução de risco por erro humano ou omissão;
* Aplicação consistente de políticas organizacionais;
* Auditoria objetiva e reprodutível;
* Menor dependência de revisão manual;
* Base técnica sólida para *zero trust* em IaC.

---

## 🔗 Referências cruzadas

| Documento                                       | Relação com este ficheiro                                 |
| ----------------------------------------------- | --------------------------------------------------------- |
| `addon/02-validacoes-e-checks.md`               | Validações técnicas e qualidade antes do enforcement      |
| `addon/04-principios-sbd-iac.md`                | Fail securely, privilégio mínimo, visibilidade controlada |
| `addon/11-uso-ferramentas-automatizadas-iac.md` | Regras específicas para automação e ferramentas externas  |
| `canon/20-checklist-revisao.md`                 | Verificação binária da aplicação das políticas            |
