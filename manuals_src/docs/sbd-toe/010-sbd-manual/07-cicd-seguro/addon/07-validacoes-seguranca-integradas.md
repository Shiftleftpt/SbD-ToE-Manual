---
id: validacoes-seguranca-integradas
title: Validações de Segurança Integradas no Pipeline
sidebar_position: 7
description: Integração de validadores de segurança (SAST, secrets, IaC, containers) diretamente na pipeline, com execução obrigatória.
tags: [cicd, validações, sast, segurança, scanner, automação]
---


# 🧪 Validações de segurança integradas no pipeline

A integração de validações de segurança diretamente nos pipelines permite **detetar vulnerabilidades precocemente**, automatizar controlos e garantir que a entrega contínua respeita os requisitos de segurança definidos.

Estas validações devem ser proporcionais ao nível de risco da aplicação, mas **sistemáticas, objetivas e auditáveis** em todos os projetos.

> A ausência de validações integradas transforma o pipeline num vetor de propagação de riscos.

---

## 🎯 Objetivos

- Integrar a segurança como parte natural e automatizada do ciclo de integração e entrega;
- Garantir cobertura consistente de testes e scanners, proporcional ao tipo e criticidade da aplicação;
- Automatizar decisões com base em critérios objetivos de segurança (ex: severidade de findings).

---

## 🛠️ Práticas

1. **SAST – Static Application Security Testing**  
   - Análise do código fonte para deteção de padrões inseguros, más práticas ou funções perigosas;
   - Deve incluir código de aplicação e de configuração (ex: YAML, JSON, Dockerfile).

2. **Secrets detection**  
   - Scanners de segredos hardcoded ou tokens expostos;
   - Devem ser aplicados a todas as branches e commits.

3. **IaC scanning (Infrastructure as Code)**  
   - Validação de ficheiros Terraform, CloudFormation, etc.;
   - Deteção de permissões excessivas, configurações perigosas ou recursos inseguros.

4. **Container security scanning**  
   - Análise de imagens Docker utilizadas ou geradas durante o pipeline;
   - Identificação de CVEs em camadas base, binários e bibliotecas.

5. **DAST – Dynamic Application Security Testing**  
   - Testes dinâmicos sobre aplicações já deployadas (ex: staging);
   - Devem ser realizados preferencialmente em ambientes isolados.

6. **SBOM + Dependency Analysis**  
   - Geração de SBOMs (Software Bill of Materials);
   - Validação de dependências vulneráveis com base em CVEs/NVD, OSS Index, etc.

7. **Enforcement de critérios de aceitação**  
   - Aplicação de política automatizada com base em findings de segurança:  
     - Severidade máxima permitida;  
     - Findings aceites manualmente (com justificação);  
     - Número total de findings por tipo.

---

## ⚖️ Aplicação proporcional por nível de risco

| Nível | Validações obrigatórias             | Validações reforçadas                                |
|-------|--------------------------------------|------------------------------------------------------|
| **L1** | SAST + secrets detection             | -                                                    |
| **L2** | IaC scanning, SBOM, análise CVEs     | Container scanning                                   |
| **L3** | DAST, enforcement de findings, políticas automatizadas | Fuzzing, análise semântica, revisão manual assistida |

---

## 📌 Exemplos práticos

- **GitHub Actions**  
  - Integração com `CodeQL`, `TruffleHog`, `checkov`, `grype`;  
  - SBOM com `cyclonedx-action`; enforcement com `scorecard-action`.

- **GitLab CI**  
  - Templates pré-definidos: `security-sast`, `secret-detection`, `container-scanning`;  
  - Enforcement via `Security Dashboard` e regras de aprovação no Merge Request.

- **Azure DevOps**  
  - Integração com ferramentas como SonarQube, Checkmarx, WhiteSource;  
  - Tasks obrigatórias no pipeline para segurança, com qualidade gates definidos.

- **Jenkins**  
  - Scanners executados via stages (`semgrep`, `trivy`, `syft`);  
  - Blocos de enforcement com `if (!pass) { error("blocked") }`.

---

## 📉 Riscos mitigados

- Inclusão de código vulnerável ou bibliotecas inseguras (OSC&R: CI0001, SC0007);
- Deploy de aplicações sem validações mínimas (OSC&R: CI0014);
- Ocultação, subvalorização ou omissão de findings críticos em produção.

---

## 🧭 Referências

- [OWASP CI/CD Security – 3. Validation and Testing](https://owasp.org/www-project-cicd-security/#3-validation-and-testing)
- [NIST SSDF – PS.3, PW.7, RV.3](https://csrc.nist.gov/publications/detail/sp/800-218/final)
- [OpenSSF Scorecard](https://github.com/ossf/scorecard)
- [BSIMM – SE1.4, CR3.1, CMVM1.5]
- [SAMM – Verification – Security Testing Automation]
