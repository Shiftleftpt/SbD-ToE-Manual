---
description: Estudo de caso completo demonstrando a aplicação das práticas de segurança
  de IaC desde o início de projeto até à sua execução em produção.
id: case-study-inception-apply-sbd-iac
sidebar_position: 10
tags:
- aplicação prática
- caso de estudo
- formacao
- iac
- inception
- seguranca
- segurança
title: Caso de Estudo - Aplicação do SbD-ToE a um Projeto IaC
---



# 🧪 Estudo de Caso - Aplicar o SbD-ToE a um Projeto de IaC

Este estudo de caso descreve a aplicação prática e transversal do manual **Security by Design - Theory of Everything (SbD-ToE)** a um **projeto real de Infraestrutura como Código (IaC)**. O objetivo foi aplicar as práticas prescritas no Capítulo 08 de forma sistemática, desde a estrutura do repositório até à auditoria e validação contínua.

> O projeto tratado aqui é responsável pela definição de ambientes (dev, QA, prod) num cluster Kubernetes e respetivos serviços de rede, autenticação e logging. Foi considerado de **criticidade L3**.

---

## 🧭 Classificação de risco

Através da metodologia do Capítulo 01 - Gestão de Risco, foi atribuída classificação **L3 (Elevado)** ao projeto IaC, com base em:

* Capacidade de impactar ambientes produtivos e múltiplas aplicações;
* Acesso a recursos críticos (VPC, certificados, serviços core);
* Potencial de causar interrupções e incidentes de segurança em larga escala.

---

## 📐 Arquitetura e modelo de repositório

* Uso de Terraform com estrutura modular por ambiente;
* Separação física de repositórios: `iac-core`, `iac-prod`, `iac-nonprod`;
* Pipelines CI/CD separados por ambiente e com controlos distintos;
* Utilização de GitHub Actions com `OPA` e `Checkov` em todos os PRs;
* Backend remoto com locking e encriptação (`S3 + DynamoDB + KMS`).

---

## 🔍 Threat modeling

Aplicado conforme Capítulo 03 - Threat Modeling:

* Análise STRIDE dos fluxos de aplicação da infraestrutura;
* Identificação de ameaças como:

  * **Tampering** (modificação maliciosa de módulos externos);
  * **Information Disclosure** (exposição por permissões abertas ou tags inadequadas);
  * **Repudiation** (alterações sem evidência ou accountability);
* Mitigações mapeadas contra requisitos `IAC-XXX` e controlos no pipeline.

---

## 🧱 Aplicação dos requisitos de segurança

Todos os requisitos `IAC-001` a `IAC-013` foram revistos e aplicados proporcionalmente:

* Drift detection ativa (`terraform plan`, `driftctl`, alarmes);
* Validações automáticas (`tfsec`, `tflint`, `OPA`, `Conftest`);
* Controlo de segredos via Vault (integração com `secrets.tf.json`);
* Versionamento com tagging, releases e rastreabilidade de `plan`;
* Separação clara de ambientes e políticas obrigatórias de tagging.

---

## 📊 Validações e evidência

Com base no Capítulo 10:

* Todos os `PRs` requerem validação automática e revisão humana;
* Relatórios de validação são arquivados automaticamente por ambiente;
* Foi implementada auditoria contínua sobre `plan vs apply`;
* Exceções são documentadas e validadas por AppSec segundo Capítulo 14.

---

## 🔐 Integração com pipeline CI/CD

* Os pipelines são validados com política de branch restrita;
* Cada `push` a `main` aciona validação + `terraform plan`, com bloqueio de `apply` sem aprovação;
* A execução dos pipelines é feita em runners dedicados, com logs centralizados;
* A assinatura dos artefactos `plan` é feita via hash e armazenada com metadados.

---

## 🎓 Formação e onboarding

Reconhecendo que o projeto IaC envolve práticas específicas e requisitos técnicos exigentes, foi criado um **módulo de formação dedicado à equipa responsável pelo desenvolvimento e manutenção do código de infraestrutura**. Este módulo cobre:

* Os requisitos de segurança aplicáveis (`REQ-XXX`, `IAC-XXX`);
* As ferramentas obrigatórias no pipeline (`tfsec`, `Checkov`, `OPA`, `driftctl`);
* Boas práticas de segregação de ambientes e tagging;
* Gestão de segredos via KMS/Vault;
* Ciclo de validação e evidência;
* Como interpretar falhas de conformidade e agir sobre elas;
* Processo de exceções e governação associada.

> A formação foi disponibilizada em formato síncrono e assíncrono, com exemplos baseados no próprio repositório do projeto.

Além disso:

* Foram incluídas **user stories de segurança no backlog** técnico da equipa;
* Foi criada uma **checklist de onboarding para novos elementos**, com foco nas práticas prescritas pelo Capítulo 08;
* O processo de formação é considerado **requisito para contribuição com permissões de escrita no repositório**.

---

## ✅ Conclusão

Este caso demonstra a **aplicação coerente e sistemática do SbD-ToE a um projeto real de Infraestrutura como Código (IaC)**. A abordagem permitiu:

* Aumentar o controlo e previsibilidade das alterações;
* Reduzir falhas causadas por erro humano ou prática obsoleta;
* Estabelecer uma base sólida para governação, rastreabilidade e auditoria.

> 💡 Este estudo pode ser reutilizado como modelo para novos projetos IaC, como base de formação ou como critério de aceitação organizacional.
