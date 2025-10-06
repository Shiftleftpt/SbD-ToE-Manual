---
id: rastreabilidade-assinaturas
title: Rastreabilidade de Execuções, Assinaturas e Deploys
sidebar_position: 8
description: Garantir que cada execução de pipeline e cada artefacto podem ser rastreados até ao commit, origem e responsável associado.
tags: [rastreabilidade, cicd, execuções, deploy, logs, auditoria]
---


# 🧾 Rastreabilidade de assinaturas e deploys {cicd-seguro:addon:rastreabilidade-assinaturas}

Rastreabilidade é a capacidade de **comprovar o que foi feito, por quem, com que artefactos e em que contexto**. No contexto de pipelines CI/CD, esta capacidade é essencial para garantir responsabilização, suporte a auditorias e possibilidade de reversão segura.

Esta prática define os mecanismos necessários para assegurar que **cada execução crítica, build, release ou deploy é identificável, verificável e auditável a qualquer momento**.

> Uma cadeia CI/CD sem rastreabilidade não pode ser considerada confiável.

---

## 🎯 Objetivos {cicd-seguro:addon:rastreabilidade-assinaturas#objetivos}

- Registar de forma fiável e verificável todas as execuções relevantes do pipeline;
- Associar artefactos a builds, utilizadores, commits e ambientes específicos;
- Suportar auditorias, investigações e reversões com base em evidência concreta e persistente.

---

## 🛠️ Práticas {cicd-seguro:addon:rastreabilidade-assinaturas#praticas}

1. **Assinatura digital de builds e releases críticas**  
   - Cada artefacto publicado deve ser assinado digitalmente (ex: GPG, Sigstore, JWT);
   - A assinatura deve conter commit hash, autor, timestamp, ID de pipeline.

2. **Preservação de registos e metadados de execução**  
   - Logs e variáveis relevantes devem ser armazenados conforme política de retenção;
   - Devem incluir: utilizador, repositório, pipeline, tempo, resultado, parâmetros principais.

3. **Registo formal de deploys**  
   - Cada deploy deve referenciar o artefacto específico por hash;
   - Devem ser registados: responsável (humano ou serviço), pipeline, ambiente e timestamp.

4. **Ligação ponta-a-ponta: commit → build → release → deploy**  
   - Toda a cadeia de eventos deve ser rastreável, incluindo alterações de configuração;
   - Essa rastreabilidade deve ser acessível por auditoria ou API.

5. **Conservação de hashes, proveniência e evidência associada**  
   - Metadados (ex: SLSA provenance) devem ser arquivados juntamente com os artefactos;
   - Devem permitir validação retrospetiva e comparação com builds futuros.

---

## ⚖️ Aplicação proporcional por nível de risco {cicd-seguro:addon:rastreabilidade-assinaturas#aplicacao_proporcional_por_nivel_de_risco}

| Nível | Registos obrigatórios                                 | Requisitos reforçados                                      |
|-------|--------------------------------------------------------|-------------------------------------------------------------|
| **L1** | Logs de execução e hash de build                      | —                                                           |
| **L2** | Registo de pipeline, artefacto e deploy               | Proveniência simples; assinatura de release                 |
| **L3** | Proveniência SLSA completa; deploy auditável          | Cadeia ponta-a-ponta; logs invioláveis; verificação periódica |

---

## 📌 Exemplos práticos {cicd-seguro:addon:rastreabilidade-assinaturas#exemplos_praticos}

- **GitHub Actions**  
  - Uso de `github.run_id`, `github.sha`, `GITHUB_ACTOR` nos artefactos e tags;  
  - Assinaturas com `cosign` e proveniência com `slsa-github-generator`.

- **GitLab CI**  
  - Inclusão de `pipeline_id`, `commit`, `project.path` nos artefactos;  
  - Uso de `release-cli` para associar metadados e alterações à release.

- **Azure DevOps**  
  - Identificadores como `Build.BuildId` e `Release.ReleaseId`;  
  - Assinaturas com certificados e auditoria de deployment em `AuditLogs`.

- **Jenkins**  
  - Registo manual com `BUILD_ID`, `BUILD_URL`, `GIT_COMMIT`;  
  - Assinatura com GPG e logs estruturados via plugins.

---

## 📉 Riscos mitigados {cicd-seguro:addon:rastreabilidade-assinaturas#riscos_mitigados}

- Ambiguidade sobre a origem de deploys (OSC&R: CI0004);
- Ausência de cadeia de confiança auditável (OSC&R: CI0011, CI0016);
- Dificuldade em apurar responsabilidades em caso de incidente;
- Publicações não rastreáveis, alteradas ou não autorizadas.

---

## 🧭 Referências {cicd-seguro:addon:rastreabilidade-assinaturas#referencias}

- [SLSA – Provenance Attestations](https://slsa.dev/spec/v1.0/provenance)
- [NIST SSDF – RV.3: Record Retention and Traceability](https://csrc.nist.gov/publications/detail/sp/800-218/final)
- [OWASP CI/CD Security – 7. Auditability](https://owasp.org/www-project-cicd-security/#7-auditability)
- [BSIMM – CR1.5, SE3.2]
- [SAMM – Secure Build – Traceability]
