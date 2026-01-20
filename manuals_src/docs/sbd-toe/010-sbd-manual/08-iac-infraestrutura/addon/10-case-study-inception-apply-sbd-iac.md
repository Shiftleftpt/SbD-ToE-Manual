---
id: case-study-inception-apply-sbd-iac
title: Caso de Estudo – Aplicação do SbD-ToE a um Projeto IaC
sidebar_position: 10
description: Estudo de caso demonstrando a aplicação integrada, independente da autoria, das práticas de Segurança em Infraestrutura como Código ao longo de todo o ciclo de vida.
tags: [caso-de-estudo, iac, sbd-toe, aplicacao-pratica, seguranca]
---

# 🧪 Caso de Estudo – Aplicar o SbD-ToE a um Projeto de Infraestrutura como Código (IaC)

Este estudo de caso descreve a **aplicação prática, integrada e rastreável** do manual **Security by Design – Theory of Everything (SbD-ToE)** a um projeto real de **Infraestrutura como Código (IaC)**.

O objetivo não é ilustrar ferramentas, estilos de autoria ou processos criativos, mas demonstrar **como as prescrições do Capítulo 08 são aplicadas de forma objetiva e verificável**, desde a fase de *inception* até à operação contínua em produção.

> **Nota fundamental:**  
> Neste estudo assume-se explicitamente que **qualquer código IaC pode ter sido produzido total ou parcialmente com apoio de ferramentas automatizadas**, incluindo sistemas de geração de código.  
> Por essa razão, **nenhuma confiança é atribuída à autoria ou origem do código**.  
> Todos os artefactos são tratados como **input não confiável até validação técnica completa**, de acordo com o modelo SbD-ToE.

O projeto analisado define ambientes `dev`, `staging` e `prod` para um cluster Kubernetes e respetivos serviços de rede, identidade e observabilidade. Foi classificado como **criticidade L3 (elevada)**.

---

## 🧭 Classificação de risco

A classificação foi realizada segundo o **Capítulo 01 — Gestão de Risco**, tendo resultado em **L3**, com base nos seguintes fatores:

* Capacidade de impactar diretamente ambientes produtivos;
* Controlo de recursos críticos (rede, identidade, certificados, logging);
* Efeito transversal sobre múltiplas aplicações e equipas;
* Potencial elevado de impacto operacional e reputacional.

Esta classificação determinou a **aplicação integral dos requisitos, validações e gates de aceitação** previstos para L3 no Capítulo 08, independentemente da origem do código.

---

## 📐 Arquitetura e modelo de repositório

O desenho técnico do projeto seguiu princípios de desacoplamento, segregação e controlo explícito:

* Terraform como ferramenta declarativa principal;
* Estrutura modular por domínio técnico;
* Separação física de repositórios:

  * `iac-core` (módulos e políticas comuns);
  * `iac-nonprod` (ambientes não produtivos);
  * `iac-prod` (produção, com controlos reforçados);
* Pipelines CI/CD distintos por ambiente;
* Backend remoto com *locking* e encriptação (`S3 + DynamoDB + KMS`).

Esta estrutura assegura que **nenhuma alteração pode ser aplicada sem passar pelos mecanismos formais de validação, aprovação e evidência**, independentemente de quem ou do que produziu o código.

---

## 🔍 Threat Modeling aplicado a IaC

O *threat modeling* foi conduzido de acordo com o **Capítulo 03 — Threat Modeling**, tratando o projeto IaC como um **ativo crítico**.

Foram analisados os principais fluxos e superfícies de ataque, considerando explicitamente cenários de:

* alterações introduzidas por automação;
* reutilização de módulos externos;
* geração de código a partir de templates ou sugestões.

As ameaças identificadas incluíram:

* **Tampering**: modificação maliciosa ou inadvertida de módulos ou *plans*;
* **Information Disclosure**: exposição de topologia, permissões ou *tags* sensíveis;
* **Repudiation**: alterações sem evidência ou responsabilização clara;
* **Elevation of Privilege**: permissões IAM excessivas introduzidas por erro humano ou automatização.

Cada ameaça foi mapeada para requisitos `IAC-XXX` e respetivos controlos técnicos no pipeline.

---

## 🧱 Aplicação dos requisitos de segurança

Todos os requisitos **IAC-001 a IAC-013** foram avaliados e aplicados segundo a matriz de proporcionalidade L3:

* Backend remoto com *locking* obrigatório;
* Validações automáticas completas (`tflint`, `tfsec`, `Checkov`, OPA/Conftest);
* *Drift detection* ativa (`terraform plan`, `driftctl`, alertas);
* Governação formal de módulos internos e externos;
* Gestão de segredos via Vault e *workload identity*;
* Rastreabilidade total entre código, *plan*, *apply* e ambiente;
* Enforcement bloqueante de políticas em todos os *pipelines*.

Em nenhum momento a aceitação de alterações dependeu da autoria do código, mas **exclusivamente da evidência técnica produzida**.

---

## 📊 Validação, evidência e auditoria

A estratégia de validação seguiu o modelo definido no **Capítulo 10 — Validação**:

* Todos os *Pull Requests* exigem validação automática e revisão humana;
* Relatórios de validação são arquivados por ambiente e *build*;
* Comparação contínua entre `plan` aprovado e `apply` executado;
* Exceções formalizadas, temporárias e aprovadas por AppSec, conforme **Capítulo 14**.

Este modelo garante que **qualquer contribuição — humana ou automatizada — é sujeita ao mesmo escrutínio técnico**.

---

## 🔐 Integração com pipelines CI/CD

Os pipelines CI/CD foram desenhados como **mecanismos de controlo e decisão**, não apenas de automação:

* *Branch protection* e regras de *merge* restritivas;
* Execução obrigatória de `terraform plan` em PR;
* *Apply* apenas permitido após aprovação explícita e validação de artefactos;
* *Runners* dedicados e isolados;
* Assinatura e hash dos artefactos (`plan`, relatórios, manifests).

---

## 🎓 Formação e capacitação da equipa

Reconhecendo que IaC seguro exige competências específicas, foi criado um **programa de formação dedicado**, cobrindo:

* Requisitos `REQ-XXX` e `IAC-XXX`;
* Interpretação de *findings* e impactos reais;
* Validação de alterações independentemente da autoria;
* Gestão de segredos e identidade;
* Ciclo completo de validação, evidência e exceções.

A formação tornou-se **pré-requisito para permissões de escrita**, reforçando que **a responsabilidade final é sempre humana**, mesmo quando existem ferramentas de apoio automatizado.

---

## ✅ Conclusão

Este caso de estudo demonstra que o **SbD-ToE aplica-se de forma uniforme e robusta a projetos IaC**, assumindo por defeito que **o código não é confiável até prova em contrário**.

A abordagem permite:

* Neutralizar riscos introduzidos por automação ou reutilização;
* Manter critérios de aceitação estáveis ao longo do tempo;
* Escalar IaC seguro sem depender de confiança implícita em pessoas ou ferramentas.

> 💡 Este estudo constitui o **modelo canónico de aplicação do SbD-ToE a IaC**, válido independentemente da evolução das ferramentas de autoria.
