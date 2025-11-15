---
id: inventario-sbom
title: Inventário de Dependências e SBOM
description: Geração e gestão de Software Bill of Materials (SBOM) com rastreabilidade no ciclo de vida
tags: [dependencias, sbom, sca, supply-chain]
---

# 📦 Inventário de Dependências e SBOM

## 🌟 Objetivo

Garantir que todas as aplicações têm um **inventário completo, rastreável e versionado** das bibliotecas e componentes utilizados - conhecido como **SBOM (Software Bill of Materials)** - como medida fundamental para:

- Mitigar riscos de terceiros e da cadeia de fornecimento;
- Acelerar a resposta a vulnerabilidades públicas (ex: CVE);
- Suportar conformidade com normas e exigências regulatórias (ex: NIS2, CRA, EO 14028);
- Viabilizar auditorias técnicas e análises de impacto.

---

## 🧬 O que é um SBOM

Um **SBOM** é um ficheiro estruturado que descreve todos os componentes de software de um sistema, incluindo:

- Nome do pacote e versão
- Origem (repositório, fornecedor)
- Licença
- Hashes/assinaturas
- Dependências transitivas
- Relacionamentos (ex: runtime, dev, optional)

> ⚠️ Um SBOM **não é um lockfile** - é um artefacto formal, estandardizado e processável por ferramentas de segurança.

---

## 📘 Formatos suportados

| Formato     | Descrição                                           | Ferramentas compatíveis                   |
|-------------|-----------------------------------------------------|-------------------------------------------|
| **CycloneDX** | Formato leve, extensível e amplamente suportado    | Syft, Trivy, OWASP tools, GitHub, Snyk    |
| **SPDX**     | Formato normativo mantido pela Linux Foundation     | SPDX tools, FOSSology, Black Duck         |
| **SWID**     | Usado em ambientes regulados (ex: fed. gov.)        | Requer tooling especializado              |

> 🌟 Recomendado pelo SbD-ToE: **CycloneDX**, em formato `JSON` ou `XML`, com suporte a múltiplas linguagens.

---

## 🛠️ Como gerar SBOMs

| Stack / Linguagem | Comando típico                              | Notas                                       |
|-------------------|---------------------------------------------|---------------------------------------------|
| Node.js           | `syft . -o cyclonedx-json`                  | Inclui `package.json` e transitivas         |
| Java/Maven        | `cyclonedx-maven-plugin`                    | Output direto no build (`target/`)          |
| Python            | `syft . -o cyclonedx-json`                  | Inclui `requirements.txt`, `pipfile.lock`   |
| Docker/Containers | `syft docker:imagem:tag -o cyclonedx-json`  | Gera SBOM de imagem completa (base + app)   |
| C# (.NET)         | `cyclonedx-dotnet`                          | SBOM por projeto `.csproj` ou `.sln`        |

> 💡 Sugestão: gerar o SBOM **automaticamente a cada build** como artefacto versionado do pipeline.

---

## 📂 Onde armazenar SBOMs

- Diretório dedicado no repositório: `/.sbom/`
- Artefacto CI/CD associado à build (ex: Azure Artifacts, GitHub Releases)
- SBOMs versionados em controlo de código ou sistemas externos (Artifactory, Nexus, etc.)

---

## 🧬 Exemplos de campos num SBOM CycloneDX

```json
{
  "bomFormat": "CycloneDX",
  "specVersion": "1.5",
  "version": 1,
  "components": [
    {
      "type": "library",
      "name": "lodash",
      "version": "4.17.21",
      "purl": "pkg:npm/lodash@4.17.21",
      "hashes": [{ "alg": "SHA-256", "content": "..." }],
      "licenses": [{ "license": { "id": "MIT" } }]
    }
  ]
}
```

> Cada componente pode estar ligado a CVEs, licença e metadados que suportam rastreabilidade e validação.

---

## ✅ Boas práticas

- Gerar SBOM **em todos os builds de produção**
- Incluir dependências **transitivas**, não apenas diretas
- Versão e reter cada SBOM junto ao artefacto correspondente
- Automatizar comparação de SBOMs entre versões (detetar introdução de risco)
- Integrar SBOM com scanners SCA e sistemas de gestão de vulnerabilidades

---

## 📎 Referências cruzadas

| Documento                   | Relação com SBOM                                 |
|-----------------------------|--------------------------------------------------|
| `02-analise-sca.md`         | Usa o SBOM como input para análise de vulnerabilidades |
| `04-integracao-ci-cd.md`    | Integração da geração de SBOM no pipeline        |
| `08-rastreabilidade-vulnerabilidades.md` | Mapeamento entre findings e componentes de SBOM |

---

> 🔒 O SBOM é um **pré-requisito técnico e documental** para a detecção eficaz de riscos, cumprimento de frameworks (SSDF, SLSA) e resposta célere a incidentes de segurança.
