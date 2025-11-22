---
id: assinatura-cadeia-trust
title: Assinatura de Imagens e Cadeia de Confiança
description: Validação da proveniência, integridade e autenticidade de imagens de *containers*
tags: [assinatura, containers, cosign, notary, rekor, supply chain, trust]
---

# 🔏 Assinatura de Imagens e Cadeia de Confiança

## 🌟 Objetivo

Assegurar que todas as imagens de *container* utilizadas em pipelines, ambientes de execução e produção **foram validadas quanto à sua origem, integridade e autenticidade**, através de assinatura digital e registo verificável.

A cadeia de confiança garante que:

- Só são utilizadas imagens aprovadas e rastreáveis;
- As imagens não foram modificadas após build;
- A origem e o responsável por cada imagem são auditáveis;
- O processo está conforme com práticas como SLSA, SSDF e NIS2.

---

## 🧬 O que é a cadeia de confiança em imagens

A **cadeia de confiança** aplica-se à origem e uso de imagens de *containers*, incluindo:

- **Assinatura digital da imagem** no momento do build;
- **Verificação da assinatura antes da execução** (enforcement);
- **Registo imutável da assinatura** (ex: transparency log);
- **Associação entre imagem, build e entidade que a produziu**.

> 🎯 Não basta confiar no registry. É necessário validar **quem construiu a imagem**, **com que ferramentas** e **se foi modificada**.

---

## 📘 Ferramentas e mecanismos recomendados

| Componente     | Ferramenta / Padrão    | Função                                         |
|----------------|-------------------------|------------------------------------------------|
| Assinatura     | [Cosign](https://docs.sigstore.dev/) | Assinar imagens com chave ou OIDC             |
| Transparency Log | [Rekor](https://rekor.sigstore.dev/) | Registo público e imutável de assinaturas     |
| Verificação    | Cosign + Policy Controller (Gatekeeper/Kyverno) | Enforcement na execução                        |
| Alternativa    | Notary v2               | Projeto CNCF para assinatura OCI              |

---

## 🛠️ Como aplicar assinatura e validação

1. **Assinar imagens no momento do build**, usando `cosign sign` com chave privada ou identidade federada (OIDC);
2. **Publicar a assinatura juntamente com a imagem** (como anotações OCI no registry);
3. **Registar a assinatura no transparency log Rekor**, garantindo integridade e auditabilidade;
4. **Configurar o runtime (ex: Kubernetes, CI/CD) para verificar assinaturas antes de executar**;
5. **Associar políticas de execução a imagens assinadas e verificadas**;
6. **Integrar verificação no pipeline**, como fase obrigatória;
7. **Armazenar as chaves e certificados de forma segura**, idealmente com HSM ou KMS.

---

## 📂 Onde armazenar e como versionar

- Assinaturas devem ser **armazenadas com a imagem** no registry (ex: `ghcr.io`, `gcr.io`, `Harbor`);
- Utilizar labels, anotações e tags de versão para rastreabilidade;
- Transparência adicional com logs Rekor públicos ou privados;
- Pode ser incluído como metadado adicional no SBOM da imagem.

---

## ✅ Boas práticas

- Usar identidades OIDC (ex: GitHub Actions, CI/CD) para assinar imagens sem gestão de chaves local;
- Evitar execução de imagens não assinadas em ambientes L2/L3;
- Verificar assinaturas no runtime via Kyverno/OPA com políticas explícitas;
- Associar build ID ao hash da imagem (relação unívoca);
- Integrar verificação no processo de revisão de segurança antes de promover imagens para produção.

---

## 📎 Referências cruzadas

| Documento                      | Relação com a assinatura                      |
|-------------------------------|-----------------------------------------------|
| `01-imagens-base.md`             | Imagens devem ser assinadas após validação     |
| `05-policies-runtime-opa.md`    | Pode reforçar políticas que exigem imagens assinadas |
| `06-sbom-containers.md`         | SBOM pode incluir referência à assinatura       |
| `achievable-maturity`              | Assinatura é critério de maturidade elevada    |
| `25-rastreabilidade.md`         | Requisito associado à integridade do runtime   |

> 🔐 A assinatura de imagens não é opcional - é o pilar técnico da confiança no código executado em *containers*.

