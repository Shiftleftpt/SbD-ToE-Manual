---
id: ameacas-mitigadas
title: Ameaças Mitigadas - Containers e Imagens
description: Ameaças mitigadas pelas práticas deste capítulo, com mapeamento a OWASP/OSC&R, CAPEC, SSDF, SLSA, CIS e outras referências
tags: [ameacas, containers, hardening, imagens, kubernetes, proveniência, supply chain]
sidebar_position: 50
---

# 🔐 Ameaças Mitigadas — Capítulo 09: Containers e Imagens

Este capítulo prescreve práticas de **construção segura de imagens, assinatura e proveniência, governação de registos, validação de manifestos e hardening do runtime**, garantindo integridade, rastreabilidade e segurança desde o _build_ até à execução.

> 🎯 As ameaças aqui tratadas decorrem de **imagens vulneráveis ou não confiáveis, pipelines sem garantias de integridade, registos desprotegidos, configurações inseguras de runtime e falta de observabilidade/rastreabilidade**.

---

## 📦 Categoria 1 - Cadeia de fornecimento de imagens (build & base images)

| Ameaça | Fonte | Como surge | Como a prática mitiga | Controlos associados | 🧩 Mitigada apenas por este capítulo? |
|---|---|---|---|---|---|
| Imagens base vulneráveis/obsoletas | OWASP Top 10 A06, CAPEC-310, CWE-1104 | Uso de _base images_ com CVEs não corrigidas | _Image scanning_ no CI/CD, políticas de bloqueio por severidade, renovação periódica de _base images_ | *Checklist 3–4*, *Policies: Gestão de Vulnerabilidades*, *Rastreabilidade: SSDF RV.1* | ✅ |
| Inclusão de dependências inseguras no build | OSC&R **E.4/T.3**,  ST 1.x | Injeção de libs ou pacotes sem validação | Inventário de componentes na imagem, _scan_ de licenças e CVEs; falha bloqueia _merge/deploy_ | Cap. 05 (SBOM/SCA), *Checklist 3–4* | ❌ (Cap. 05) |
| Conteúdo inesperado no _context_ de build | CAPEC-649 | Ficheiros sensíveis entram no _build context_ | `.dockerignore` rigoroso; _lint_ de Dockerfile; _build_ hermético | *Policies: Construção Segura de Imagens* | ✅ |
| Configurações inseguras no Dockerfile | CIS Docker 2.x | Uso de `ADD` indevido, `latest`, _layering_ frágil | Linters (Hadolint/Regole), _policy-as-code_ para Dockerfile | *Checklist 6*, *Policies: Construção Segura* | ✅ |

---

## 🔏 Categoria 2 - Integridade, assinatura e proveniência

| Ameaça | Fonte | Como surge | Como a prática mitiga | Controlos associados | 🧩 Mitigada apenas por este capítulo? |
|---|---|---|---|---|---|
| Imagens não assinadas / sem verificação | SLSA L2–L3, SSDF PW.5 | Execução de imagens sem verificar origem | Assinatura (ex.: Sigstore/Cosign), verificação de _digest_ e _attestation_ no _admission_ | *Checklist 5 & 10–11*, *Policies: Assinatura e Proveniência* | ✅ |
| Substituição maliciosa em registo | OSC&R **T.3**, ENISA Cloud | _Pull_ de imagem com _tag_ trocada | _Digest pinning_, registos privados, _provenance attestation_ no _deploy_ | *Rastreabilidade: SLSA/SSDF*, *Policies: Repositórios* | ✅ |
| Falta de trilho de auditoria (quem construiu o quê) | BSIMM CMVM 1.3 | Ausência de registo entre commit → build → imagem → deploy | CI/CD com evidência imutável; correlação commit/SHA/pipeline/deploy | *Checklist 14–15*, *Rastreabilidade: DSOMM Ops* | ✅ |

---
## 🧰 Categoria 3 - Registos e Repositórios de Containers

| Ameaça                               | Como surge                               | Como a prática mitiga                                                                 | Controlos associados                                         | 🧩 Mitigada apenas por este capítulo? |
|-------------------------------------|-------------------------------------------|----------------------------------------------------------------------------------------|--------------------------------------------------------------|--------------------------------------|
| Acesso indevido a registos          | Controlo de acesso frouxo, credenciais partilhadas | Registos privados, RBAC, _scopes_ mínimos, _audit logs_                               | *Policies: Governação de Repositórios*, *Checklist 9*        | ✅ |
| Proliferação de imagens obsoletas   | Ausência de retenção/limpeza              | Políticas de retenção e _garbage collection_; _rebuild_ periódico                      | *Policies: Limpeza/Obsolescência*, *Checklist 12*            | ✅ |
| Upload de imagens sem controlo      | Qualquer equipa publica artefactos        | _Ownership_ formal, _review_ e aprovação de publicação                                 | *Policies: Governação de Repositórios*                      | ✅ |


## 🖧 Categoria 4 - Configuração insegura de runtime (Docker/Kubernetes)

| Ameaça | Fonte | Como surge | Como a prática mitiga | Controlos associados | 🧩 Mitigada apenas por este capítulo? |
|---|---|---|---|---|---|
| Execução como root / capabilities excessivas | CIS Docker/K8s, STRIDE (EoP) | `USER root`, `CAP_SYS_ADMIN`, `privileged: true` | *Least privilege*, `securityContext`, _drop capabilities_, _PSP/PSA_ equivalentes | *Checklist 7–9*, *Policies: Hardening de Runtime* | ✅ |
| Montagens e volumes inseguros | CIS, CAPEC-15 | `:rw` em `/var/run/docker.sock`, partilhas amplas | Regras de _mounts_, _read-only rootfs_, _tmpfs_ controlado | *Policies: Hardening de Runtime* | ✅ |
| Falta de políticas de rede | CIS K8s, ENISA | _Pods_ sem _NetworkPolicy_ | _Network policies_ obrigatórias por namespace/serviço | *Policies: Runtime*, *Checklist 8* | ✅ |
| _Admission_ permissivo | OPA/Gatekeeper, SAMM DEP 1.2 | Qualquer manifesto é aceite | _Admission controllers_ com _policy-as-code_ (Conftest/OPA) | *Checklist 11*, *Policies: Validação de Manifestos* | ✅ |

---

## 🔐 Categoria 5 - Segredos e informação sensível

| Ameaça | Fonte | Como surge | Como a prática mitiga | Controlos associados | 🧩 Mitigada apenas por este capítulo? |
|---|---|---|---|---|---|
| Segredos embebidos em imagem | CAPEC-118, SSDF PS.1 | `ENV`/`ARG` com chaves; ficheiros copiados para _layers_ | *Secrets scanning*, _build args_ efémeros, uso de _vault/secret manager_ | *Policies: Segredos*, *Checklist 3 & 5* | ❌ (Cap. 08) |
| Exposição em variáveis de ambiente | CIS, DSOMM | Injeção de segredos por ENV | *Mounts* seguros, *sealed secrets*, RBAC por namespace | *Policies: Segredos* | ❌ (Cap. 08) |

---

## 📜 Categoria 6 - Manifestos e _policy-as-code_ (deploy seguro)

| Ameaça | Fonte | Como surge | Como a prática mitiga | Controlos associados | 🧩 Mitigada apenas por este capítulo? |
|---|---|---|---|---|---|
| Manifestos inseguros aprovados | SSDF RV.1, SAMM 2.B | Falta de validação pré-deploy | _Policy-as-code_ (OPA/Conftest), _schema validation_, _review_ obrigatório | *Checklist 11*, *Policies: Validação de Manifestos* | ✅ |
| Desalinhamento imagem↔manifesto | SLSA | _Tag drift_ entre o aprovado e o executado | _Digest pinning_ e verificação no _admission_ | *Rastreabilidade: SLSA*, *Checklist 2 & 10–11* | ✅ |

---

## 📡 Categoria 7 - Observabilidade, _drift_ e *shadow containers*

| Ameaça | Fonte | Como surge | Como a prática mitiga | Controlos associados | 🧩 Mitigada apenas por este capítulo? |
|---|---|---|---|---|---|
| Falta de rastreabilidade de deploys | BSIMM CMVM 1.3 | Deploy sem trilho de auditoria | Correlação **commit → pipeline → digest → deploy** | *Checklist 14–15*, *DSOMM Ops Monitoring* | ✅ |
| _Shadow containers_ fora do pipeline | OSC&R **M.4** | Execução ad-hoc por terceiros | Inventário/monitorização de runtime; _admission_ restritivo | *Policies: Runtime/Registos*, *Rastreabilidade: DSOMM* | ✅ |
| _Drift_ de configuração | ENISA, CIS | Diferenças entre definido e executado | _Drift detection_ e reconciliação; alerta/bloqueio | *Policies: Runtime*, Cap. 08 (IaC) | ❌ (Cap. 08) |

---

## ✅ Conclusão

As práticas deste capítulo reduzem **risco sistémico na cadeia de fornecimento de software** ao:

- Garantirem **integridade e proveniência** (assinatura, _attestations_, _digest pinning_);
- Imporem **construção e execução seguras** (hardening de Docker/Kubernetes, *least privilege*, *admission controllers*);
- Assegurarem **rastreabilidade auditável** de ponta a ponta (commit → imagem → deploy);
- Reforçarem a **governação de registos** (acesso, retenção, limpeza e _ownership_ claros).

> 📌 A cobertura está alinhada com **NIST SSDF (PW.5, RV.1–RV.2, PS.1)**, **SLSA (L2–L3)**, **CIS Benchmarks (Docker/K8s)**, **ENISA Cloud Security Baseline**, **BSIMM** e **OWASP/OSC&R** — constituindo evidência sólida de conformidade técnica para auditorias **NIS 2 / DORA**.
