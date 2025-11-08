---
id: achievable-maturity
title: Mapeamento de Maturidade – Capítulo 09
sidebar_position: 10
tags: [canon, maturidade, SAMM, SSDF, SLSA, DSOMM, CIS, ENISA]
---

# 📈 Maturidade – Containers e Imagens

Este documento apresenta o **grau de alinhamento entre as práticas descritas no Capítulo 09 do SbD-ToE – *Containers e Imagens*** e os principais frameworks de segurança e maturidade de software:

- **OWASP SAMM**
- **BSIMM**
- **NIST SSDF**
- **SLSA**
- **OWASP DSOMM**
- **CIS Benchmarks / ENISA Cloud Baseline** (referências complementares)

O capítulo aborda **segurança de imagens e containers ao longo de todo o ciclo de vida**, incluindo:
- Construção segura e reprodutível de imagens;
- Assinatura, proveniência e rastreabilidade de artefactos;
- Governação de registos e pipelines;
- Hardening de *runtime* (Docker, Kubernetes, etc.);
- Validação de manifestos e observabilidade de execução.

Estas práticas integram-se diretamente com os capítulos **05 (Dependências e SBOM)** e **08 (IaC)**, reforçando a segurança da *supply chain*.

---

## 🎯 Como interpretar este mapeamento de maturidade

Este mapeamento **não mede equipas ou ferramentas**, mas sim o **nível de maturidade das práticas prescritas** neste capítulo, avaliando a sua completude e aderência a normas reconhecidas.

| Framework        | Avaliação usada                     | Justificação                                      |
|------------------|-------------------------------------|--------------------------------------------------|
| OWASP SAMM       | `n / 3`                             | 3 níveis formais por domínio                     |
| OWASP DSOMM      | `n / 4`                             | Domínios com níveis explícitos e cumulativos     |
| NIST SSDF        | Lista de controlos cobertos         | Modelo binário e prescritivo                     |
| BSIMM            | Lista de práticas observadas        | Modelo observacional, não gradual                |
| SLSA             | Nível máximo suportado (1–4)        | Modelo acumulativo de integridade da cadeia      |
| CIS / ENISA      | Conformidade qualitativa            | Benchmarks e boas práticas para execução segura  |

---

## 🧭 Visão Geral de Alinhamento

| Framework        | Domínios Relevantes | Práticas ou Objetos Cobertos | Avaliação de Maturidade |
|------------------|--------------------|------------------------------|--------------------------|
| **OWASP SAMM v2.1** | Deployment (DEP 1.2), Verification (2.A/2.B), Governance (GOV 1.2) | Build seguro, _policy-as-code_, assinatura, controlo de registos e validação de manifestos | **3 / 3** |
| **OWASP DSOMM** | Build & Deploy, Supply Chain, Ops Monitoring | Construção determinística, proveniência, hardening e observabilidade de _runtime_ | **3 / 4** |
| **NIST SSDF v1.1** | PW.5, RV.1–RV.2, PS.1 | Build integrity, verificação de artefactos e aprovação antes do deploy | **✔️ PW.5, RV.1, RV.2, PS.1** |
| **BSIMM 13** | CMVM 1.3, SE 2.2, ST 1.1–1.4 | _Scanning_ de imagens, proveniência, _compliance gates_ e governação de registos | Contributo direto |
| **SLSA v1.0** | Build Integrity, Provenance, Source Verification | Assinaturas, _attestations_, pipelines confiáveis e _digest pinning_ | **Nível 3 / 4** |
| **CIS Docker/Kubernetes** | Hardening 2–5, Runtime Isolation | Parâmetros mínimos de segurança, _least privilege_, políticas de rede | **Conforme** |
| **ENISA Cloud Security Baseline** | Container Security 4.2–4.5 | Configuração segura, gestão de registos e observabilidade | **Conforme** |

---

## 🧱 OWASP SAMM – Deployment, Verification e Governance

| Nível | Descrição SAMM | Cobertura pelo Cap. 09 |
|-------|----------------|------------------------|
| 1 | *Deploys* manuais e controlo básico | ✅ Governação mínima de imagens e registos |
| 2 | Pipelines automatizadas e validação de imagens | ✅ _Scanning_ e assinatura no CI/CD |
| 3 | Governação formal e políticas de aprovação automatizadas | ✅ _Policy-as-code_, _admission controllers_, rastreabilidade auditável |

**🧮 Maturidade atingida: 3 / 3**

---

## 🧱 OWASP DSOMM – Build & Deploy / Supply Chain / Ops Monitoring

| Domínio | Nível | Justificação técnica |
|----------|-------|----------------------|
| **Build & Deploy** | 3 / 4 | Pipelines determinísticos, verificação de proveniência e _attestation_. |
| **Supply Chain** | 3 / 4 | Assinatura, rastreabilidade e governação de registos e dependências. |
| **Ops Monitoring** | 3 / 4 | Observabilidade, deteção de _drift_ e _shadow containers_. |

---

## 🧱 NIST SSDF v1.1 – Desenvolvimento e Verificação

| Controlos | Descrição | Alinhamento |
|------------|------------|--------------|
| **PW.5** | Assegurar integridade do processo de build | ✅ Builds reproduzíveis, pipelines auditáveis |
| **RV.1** | Verificar software antes do lançamento | ✅ _Scanning_ e assinatura de imagens |
| **RV.2** | Resolver vulnerabilidades identificadas | ✅ _Patch/rebuild_ e bloqueio automático |
| **PS.1** | Revisão e aprovação de alterações | ✅ Validação formal de manifestos e políticas de aprovação |

---

## 🧱 BSIMM 13 – CMVM / SE / ST

| Prática BSIMM | Alinhamento com Cap. 09 |
|---------------|--------------------------|
| **CMVM 1.3** | Monitorização contínua de conformidade e vulnerabilidades em imagens |
| **SE 2.2** | Integração de _compliance scanning_ no CI/CD |
| **ST 1.1–1.4** | Construção segura e proveniência controlada de artefactos |

---

## 🧱 SLSA v1.0 – Build Integrity & Provenance

| Nível | Requisitos | Cobertura pelo Cap. 09 |
|-------|-------------|-------------------------|
| 1 | Builds rastreáveis e controlados | ✅ Dockerfiles versionados e CI/CD auditável |
| 2 | Proveniência autenticada | ✅ _Digest pinning_ e _attestation_ de origem |
| 3 | Build isolado e reproduzível | ✅ Assinaturas, _attestations_ e verificação automática |
| 4 | Cadeia totalmente verificada e hermética | ❌ Fora do escopo (nível de integração infraestrutural) |

**🔐 Nível atingido: SLSA 3 / 4**

---

## 🧱 CIS Benchmarks & ENISA Cloud Baseline

| Referência | Domínio | Cobertura |
|-------------|----------|------------|
| **CIS Docker v1.6** | Sec. 2–4 (Build & Runtime Hardening) | ✅ Políticas de _least privilege_, _user non-root_, controlo de capacidades |
| **CIS Kubernetes v1.25** | Network & Admission Control | ✅ _Network policies_, _admission controllers_ |
| **ENISA Cloud Baseline 4.2–4.5** | Container Security | ✅ Governação, isolamento, logging e rastreabilidade |

---

## ✅ Conclusão

- O Capítulo 09 apresenta **maturidade técnica elevada** nas práticas de *supply chain security* e *runtime hardening*.  
- Alcança **nível 3 / 3 em SAMM** e **nível 3 / 4 em DSOMM**, e cobre integralmente os controlos **PW.5, RV.1, RV.2, PS.1 do SSDF**.  
- Demonstra **conformidade com SLSA 3/4** e com os benchmarks **CIS** e **ENISA Cloud Baseline**, refletindo práticas de construção e execução seguras.  
- Estas capacidades sustentam a **governação completa da cadeia de imagens** e integram-se com os capítulos 05 (Dependências) e 08 (IaC), garantindo **proveniência, integridade e observabilidade contínua** — pilares centrais da segurança moderna de containers.
