---
id: integridade-proveniencia
title: Integridade e Proveniência de Artefactos
sidebar_position: 5
description: Técnicas para gerar, assinar e validar artefactos com proveniência confiável, garantindo rastreabilidade de build até produção.
tags: [proveniência, artefactos, cicd, assinatura, rastreabilidade, build]
---


# 📦 Integridade e proveniência de artefactos

A segurança de uma aplicação depende da **confiança nos artefactos** que são produzidos e distribuídos. Se um artefacto (ex: binário, imagem, pacote) for manipulado em qualquer fase — build, armazenamento ou publicação — o software resultante deixa de ser fiável.

Esta prática define os controlos necessários para garantir a **integridade, autenticidade e proveniência verificável** dos artefactos gerados por pipelines CI/CD.

> Nenhum artefacto deve ser publicado ou promovido sem integridade comprovada e proveniência verificável.

---

## 🎯 Objetivos

- Garantir que cada artefacto foi produzido de forma segura e rastreável;
- Permitir a verificação automática da proveniência e integridade dos artefactos;
- Impedir a publicação de artefactos manipulados, não autorizados ou ambíguos.

---

## 🛠️ Práticas

1. **Assinatura digital dos artefactos gerados**  
   - Cada build relevante deve produzir artefactos assinados digitalmente (ex: `cosign`, `GPG`);
   - As assinaturas devem ser armazenadas de forma acessível e verificável por terceiros.

2. **Geração automática de metadados de proveniência**  
   - Os artefactos devem conter hashes, origem do código, ambiente de build, ID do pipeline e timestamp;
   - A proveniência deve seguir o modelo SLSA (ex: `.intoto`) e ser gerada automaticamente.

3. **Validação obrigatória antes da publicação ou deploy**  
   - Artefactos sem proveniência ou assinatura válida devem ser rejeitados;
   - Deve existir política formal de “no provenance, no deploy”.

4. **Armazenamento e transporte seguros dos artefactos**  
   - Repositórios devem suportar TLS, verificação de integridade e autenticação forte;
   - A publicação deve ser controlada, autorizada e auditável.

5. **Deteção de manipulações ou colisões**  
   - Devem existir mecanismos de verificação (ex: hashes, reproducible builds) que permitam garantir a não alteração dos artefactos;
   - Artefactos devem ser idempotentes e verificáveis a qualquer momento.

---

## ⚖️ Aplicação proporcional por nível de risco

| Nível | Requisitos obrigatórios                              | Requisitos reforçados                                 |
|-------|--------------------------------------------------------|--------------------------------------------------------|
| **L1** | Hashes e logs de origem do build                      | —                                                      |
| **L2** | Proveniência automatizada; controlo de publicação     | Assinaturas digitais formais                           |
| **L3** | Proveniência SLSA completa; políticas de validação    | Builds reproduzíveis; cadeia de confiança completa     |

---

## 📌 Exemplos práticos

- **GitHub Actions + Sigstore**  
  - Geração de `.intoto` provenance com `slsa-github-generator`;  
  - Assinatura com `cosign`; publicação apenas via GitHub Release com verificação.

- **GitLab CI**  
  - `job artifacts` com controlo de acesso;  
  - Integração com Keyless Signing e proveniência manual via CI metadata.

- **Azure DevOps**  
  - Artefactos SHA256 + timestamp;  
  - Publicação no Azure Artifacts com validação de origem e publisher.

- **Jenkins**  
  - Integração com GPG para assinatura de artefactos;  
  - Uso de plugins para reproducible builds e validação por política antes do `deploy`.

---

## 📉 Riscos mitigados

- Manipulação ou substituição de artefactos (OSC&R: CI0011);
- Injeção de código malicioso via build comprometido (OSC&R: CI0002);
- Publicação de artefactos sem origem conhecida (OSC&R: CI0004, CI0008);
- Uso de artefactos falsificados ou alterados em trânsito.

---

## 🧭 Referências

- [SLSA – Provenance Specification](https://slsa.dev/spec/v1.0/provenance)
- [Sigstore / Cosign](https://www.sigstore.dev/)
- [OWASP CI/CD Security – 5. Build Integrity](https://owasp.org/www-project-cicd-security/#5-build-integrity)
- [NIST SSDF – PW.7: Protect Code from Unauthorized Changes](https://csrc.nist.gov/publications/detail/sp/800-218/final)
- [BSIMM – SE3.2, CR3.2]
- [SAMM – Secure Build – Provenance Generation]
