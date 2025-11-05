---
id: sbom-containers
title: SBOM de *containers* e Rastreabilidade de Runtime
description: Geração, versionamento e validação de SBOMs específicos de imagens e ambientes containerizados
tags: [sbom, containers, rastreabilidade, supply chain, assinatura]
---

# 🧬 SBOM de *containers* e Rastreabilidade de Runtime

## 🌟 Objetivo

Garantir que todas as **imagens de *container* utilizadas em pipelines ou produção** possuem um **SBOM (Software Bill of Materials)** completo, versionado e validado - permitindo:

- Rastreabilidade de componentes, bibliotecas e camadas;
- Análise de vulnerabilidades com base no conteúdo real da imagem;
- Verificação de integridade entre versões;
- Cumprimento de requisitos normativos (ex: SLSA, SSDF, EO 14028).

---

## 🧬 O que é um SBOM de *container*

Um **SBOM de *container*** é uma representação estruturada de todos os componentes, pacotes e camadas incluídas numa imagem, incluindo:

- Pacotes instalados (e.g. `apk`, `apt`, `npm`, `pip`);
- Dependências transitivas;
- Informação de origem e licença;
- Hashes, localizações e metadados;
- Ligações a CVEs e vulnerabilidades conhecidas.

> 🧱 É diferente de um `Dockerfile` ou de um lockfile - representa o **estado real da imagem**, após build, e pode incluir alterações que não estão no repositório.

---

## 📘 Formatos e ferramentas recomendadas

| Formato     | Ferramentas suportadas                    | Notas                            |
|-------------|--------------------------------------------|----------------------------------|
| **CycloneDX** | Syft, Trivy, Docker SBOM, GitHub          | Formato leve e auditável         |
| **SPDX**     | SPDX tools, FOSSology                      | Suporte mais comum em auditorias |
| **Syft JSON**| Syft (`syft image:tag -o json`)            | Útil para validações customizadas|

> 🌟 Recomendação SbD-ToE: **CycloneDX JSON** para SBOMs de imagens de *container*, com integração na pipeline.

---

## 🛠️ Como gerar SBOMs de *containers*

| Etapa                      | Comando típico                                   | Notas                        |
|----------------------------|--------------------------------------------------|------------------------------|
| Geração via Syft           | `syft docker:app:tag -o cyclonedx-json`         | Inclui todas as camadas      |
| Geração via Trivy          | `trivy image --format cyclonedx image:tag`      | Inclui CVEs associados       |
| Extração via CI/CD         | Adicionar como step após build                   | Pode ser feito no runner     |
| Versionamento do SBOM      | Guardar como artefacto com hash ou tag da imagem| Associar à release           |

---

## 📂 Onde armazenar e como versionar

- Diretório no repositório: `/.sbom/containers/<imagem>:<tag>.json`;
- Artefactos de pipeline: `.sbom` versionado com cada build;
- Anotação da imagem (`LABEL sbom=...`) ou registo externo (Artifactory, OCI registry);
- Inclusão opcional no transparency log (Rekor) com assinatura associada.

---

## ✅ Boas práticas

- Gerar SBOM **automaticamente após build da imagem**;
- Reter SBOM junto ao artefacto e referenciar na release;
- Incluir dependências transitivas e componentes de base;
- Validar o SBOM antes do deploy - rejeitar imagens com CVEs conhecidos;
- Integrar o SBOM com scanners SCA e com sistemas de alerta contínuo;
- Ligar SBOM à assinatura da imagem (`03-assinatura-cadeia-trust.md`).

---

## 📎 Referências cruzadas

| Documento                      | Relação com SBOM de *containers*               |
|-------------------------------|-----------------------------------------------|
| `01-imagens-base.md`             | Imagens aprovadas devem ter SBOM associado     |
| `03-assinatura-cadeia-trust.md` | SBOM pode ser assinado e registado com a imagem|
| `07-vulnerabilidades-imagens.md`| Análise SCA depende do SBOM                    |
| `09-exemplo-pipeline-container.md` | Exemplo de integração prática do SBOM          |
| `achievable-maturity`              | Geração e uso de SBOM são critério de maturidade|

> 🔍 O SBOM é a única forma de saber **o que realmente está dentro de um *container*** - e, por isso, é um pré-requisito para validação, auditoria e resposta a incidentes.
