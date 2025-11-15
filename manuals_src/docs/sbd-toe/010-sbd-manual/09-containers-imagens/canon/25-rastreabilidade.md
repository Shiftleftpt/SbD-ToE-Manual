---
id: rastreabilidade
title: Rastreabilidade Top-Down – Containers e Imagens
description: Rastreabilidade entre as práticas deste capítulo e os requisitos dos principais frameworks de segurança aplicáveis a containers, imagens e registos
tags: [rastreabilidade, frameworks, containers, imagens, SAMM, SSDF, SLSA, DSOMM, CIS]
sidebar_position: 25
---

# 📎 Rastreabilidade contra Frameworks — Capítulo 09: Containers e Imagens

Este ficheiro estabelece a **rastreabilidade entre as práticas prescritas neste capítulo** e os requisitos dos principais frameworks e normas de segurança relacionados com **construção, assinatura, proveniência, hardening e execução segura de containers e imagens**.

> A rastreabilidade é feita de forma **top-down**, demonstrando como o SbD-ToE cobre sistematicamente os controlos aplicáveis à segurança de containers, desde o _build_ até ao _runtime_.

---

## 📌 Tabela de Rastreabilidade

| Requisito / Domínio (Framework)                                                                 | Práticas do Capítulo 09 que respondem                                                                                          | Nível de Cobertura |
|--------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|--------------------|
| **NIST SSDF v1.1** – PW.5 (Build integrity), RV.1–RV.2 (Verification), PS.1 (Review)            | _Image scanning_ em CI/CD, bloqueios por severidade, verificação de integridade/assinatura, validação de manifestos antes do deploy | ✅ Completo         |
| **OWASP SAMM v2.1** – Deployment (DEP 1.2), Verification (2.A/2.B), Governance (GOV 1.2)        | Pipelines rastreáveis, _policy-as-code_, revisão formal, _gates_ de segurança, controlo de registos privados                      | ✅ Nível 3          |
| **BSIMM13** – CMVM 1.3, SE 2.2, ST 1.1–1.4                                                       | _Compliance/config scanning_, gestão de vulnerabilidades em imagens, proveniência e auditoria de _builds_ e _deploys_             | ✅ Nível 2/3        |
| **SLSA v1.0** – L2–L3 (Source/Build/Provenance)                                                 | Assinatura e atestações de proveniência, _digest pinning_, _pipeline_ confiável e reprodutível                                   | ✅ Parcial→Completo |
| **CIS Benchmarks** – Docker & Kubernetes                                                         | Hardening do _daemon/runtime_, _securityContext_, políticas de rede, _admission controllers_, _seccomp/AppArmor/SELinux_          | ✅ Completo         |
| **ENISA Cloud Security Baseline** – Container Security                                           | Gestão de registos, isolamento, _least privilege_, varredura contínua de vulnerabilidades e configuração                          | ✅ Completo         |
| **OWASP DSOMM v2** – Supply Chain, Build & Deploy, Ops Monitoring                               | _Build_ determinístico, validações automáticas, observabilidade e trilhos de auditoria de alterações                              | ✅ Nível 2/3        |
| **ISO/IEC 27001/27002** – Secure development & change management (alto nível)                   | Regras formais para promoção de imagens, controlo de alteração e evidência de validação antes de produção                         | ✅ Parcial          |

> Nota: Para **ISO/IEC 27001/27002** a correspondência é intencionalmente **de alto nível**, focada em princípios de desenvolvimento/alteração segura e evidência auditável (sem dependência de numeração específica de controlos).

---

## 🧠 Notas explicativas por framework

### 🛠️ NIST SSDF v1.1
Cobertura direta de:
- **PW.5** — Integridade de _builds_: _digest pinning_, reprodutibilidade, assinatura e atestação de imagens.
- **RV.1–RV.2** — Verificação contínua: _image scanning_ (vulnerabilidades, licenças, configuração) com bloqueios por severidade.
- **PS.1** — Revisão de alterações: validação de manifestos (Kubernetes/Helm/Compose) e aprovações formais antes do _deploy_.

---

### 🧱 OWASP SAMM v2.1
Atinge **nível 3** nos domínios:
- **Deployment (DEP 1.2)** — _gates_ de segurança em CI/CD, controlo de promoção entre ambientes, registos privados e auditáveis.
- **Verification (2.A/2.B)** — _scanning_ automatizado e validação de configuração com _policy-as-code_ (OPA/Conftest, _admission controllers_).
- **Governance (GOV 1.2)** — Regras formais de operação de registos, retenção e limpeza de imagens, ownership e auditoria.

---

### 📊 BSIMM13
Práticas alinhadas com:
- **CMVM 1.3** — Monitorização de conformidade e variações (p. ex., _drift_ entre imagens definidas e executadas).
- **SE 2.2 / ST 1.1–1.4** — Integração de _scanners_ no _pipeline_, critérios de aceitação por severidade, registos de evidências e _playbooks_ de correção.

---

### 🧬 SLSA v1.0
- **L2–L3** — Foco em proveniência: assinaturas, atestações, trilho de quem construiu o quê, quando e com que entradas; empacotamento seguro do _build_ de imagens e restrições de origem.

---

### 🧰 CIS Benchmarks (Docker & Kubernetes)
- Hardening de _runtime_ (parâmetros do _daemon_, _cgroups_, _namespaces_), **utilizador não-root**, capacidades mínimas, políticas de rede, e **_admission controllers_** para impor padrões de segurança.

---

### ☁️ ENISA Cloud Security Baseline
- Boas práticas de **registos privados e controlados**, isolamento _runtime_, gestão de vulnerabilidades e **observabilidade** de _deploys_ e alterações.

---

### 🔄 OWASP DSOMM v2
- **Supply Chain / Build & Deploy** — _Builds_ determinísticos, validações automáticas e políticas de promoção.
- **Ops Monitoring** — _Audit trail_ completo: correlação entre _commit_, _pipeline run_, _digest_ e _deploy_ efetivo; deteção de _shadow containers_.

---

## 🔗 Ligações com outros capítulos

Este capítulo integra e depende de práticas descritas noutros capítulos:

- **Capítulo 05 – Dependências, SBOM e SCA**: inventário de componentes e vulnerabilidades herdadas pelas imagens base.  
- **Capítulo 07 – CI/CD Seguro**: pontos de controlo automáticos no _pipeline_ (gates, _policy enforcement_, proveniência).  
- **Capítulo 08 – IaC e Infraestrutura como Código**: coerência entre manifestos de _deploy_ (Kubernetes/Helm/Compose) e governação técnica de ambientes.  
- **Capítulo 10 – Testes de Segurança**: integração de _scanners_, testes funcionais de segurança e validações de _runtime_.  
- **Capítulo 14 – Governação e Contratação**: políticas de operação de registos, retenção, acesso e auditoria (suporte organizacional).

---

> 📌 Este capítulo fornece a camada técnica essencial para garantir **integridade, proveniência e execução segura** de artefactos em produção. As práticas aqui descritas permitem **evidenciar conformidade** com requisitos modernos de _software supply chain security_ (SSDF, SLSA) e sustentam auditorias em contexto **NIS 2 / DORA**.
