---
id: sbom-containers
title: SBOM de Containers e Rastreabilidade de Runtime
description: Geração, versionamento e utilização de SBOMs como evidência de composição, não como prova de segurança
tags: [sbom, containers, rastreabilidade, supply-chain, assinatura]
---

# 🧬 SBOM de Containers e Rastreabilidade de Runtime

## 🌟 Objetivo

Garantir que todas as **imagens de container utilizadas em pipelines ou produção** possuem um **SBOM (Software Bill of Materials)** gerado a partir do artefacto real, versionado e rastreável, permitindo:

- Visibilidade objetiva sobre componentes, bibliotecas e camadas;
- Análise de vulnerabilidades com base no conteúdo efetivo da imagem;
- Comparação entre versões e deteção de alterações inesperadas;
- Suporte a requisitos normativos (ex.: SLSA, SSDF, EO 14028).

No modelo SbD-ToE, o SBOM é tratado como **evidência de composição**, não como garantia de segurança nem como substituto de análise de risco.

---

## 🧬 O que é um SBOM de container

Um **SBOM de container** representa o **estado efetivo da imagem após o build**, incluindo:

- Pacotes instalados (ex.: `apk`, `apt`, `npm`, `pip`);
- Dependências transitivas;
- Informação de origem e licenciamento;
- Hashes, localizações e metadados;
- Ligações conhecidas a CVEs.

> 🧱 Um SBOM **não é equivalente** a um `Dockerfile`, lockfile ou manifesto declarativo.  
> Ele descreve **o que está realmente presente**, incluindo efeitos colaterais do processo de build.

---

## ⚠️ SBOM completo ≠ ausência de risco

Em ambientes automatizados, é essencial evitar interpretações incorretas:

- ✔️ SBOM existente → composição visível  
- ❌ SBOM existente ≠ imagem segura  
- ❌ SBOM sem CVEs ≠ risco inexistente

Limitações típicas incluem:
- dependências não detetadas;
- binários estáticos;
- componentes incorporados manualmente;
- diferenças entre ambientes de build.

Por isso, o SBOM deve ser usado como **input técnico para análise**, não como conclusão.

---

## 📘 Formatos e ferramentas recomendadas

| Formato         | Ferramentas suportadas                    | Observações técnicas                   |
|-----------------|--------------------------------------------|----------------------------------------|
| **CycloneDX**   | Syft, Trivy, Docker SBOM, GitHub          | Leve, extensível, adequado a pipelines |
| **SPDX**        | SPDX tools, FOSSology                      | Frequente em auditorias formais        |
| **Syft JSON**   | Syft (`syft image:tag -o json`)            | Útil para validações customizadas      |

> 🌟 Recomendação SbD-ToE: **CycloneDX JSON** como formato base para SBOMs de imagens de container.

---

## 🛠️ Como gerar SBOMs de containers

| Etapa                | Exemplo técnico                                   | Notas operacionais                     |
|----------------------|--------------------------------------------------|----------------------------------------|
| Geração pós-build    | `syft docker:app:tag -o cyclonedx-json`          | Deve refletir a imagem final           |
| Geração alternativa  | `trivy image --format cyclonedx image:tag`       | Pode enriquecer com CVEs               |
| Integração CI/CD     | Step obrigatório após build                      | Execução automática                    |
| Versionamento        | Artefacto associado ao digest da imagem          | Correlação inequívoca                  |

A geração automática **não elimina** a necessidade de interpretação humana dos resultados.

---

## 📂 Armazenamento, versionamento e correlação

Para garantir rastreabilidade real:

- Armazenar SBOM como artefacto versionado;
- Associar explicitamente:
  - imagem (digest),
  - build,
  - pipeline;
- Referenciar SBOM via labels ou metadados OCI;
- Opcionalmente assinar SBOM ou ligá-lo à assinatura da imagem.

A ausência desta correlação reduz o SBOM a um ficheiro informativo sem valor auditável.

---

## 🔍 Utilização correta do SBOM

No SbD-ToE, o SBOM deve ser usado para:

- Alimentar scanners SCA e processos de análise;
- Detetar alterações inesperadas entre builds;
- Apoiar resposta a incidentes;
- Justificar decisões de aceitação ou mitigação.

Não deve ser usado como:
- selo de aprovação;
- substituto de análise contextual;
- prova de ausência de vulnerabilidades.

---

## ✅ Boas práticas

- Gerar SBOM automaticamente após cada build;
- Tratar SBOM como artefacto versionado;
- Rever SBOM após alterações de base image;
- Correlacionar SBOM com assinatura e proveniência;
- Usar SBOM como input para decisão humana documentada;
- Rever critérios de análise após incidentes relevantes.

---

## 📎 Referências cruzadas

| Documento                         | Relação com SBOM de containers              |
|----------------------------------|---------------------------------------------|
| `01-imagens-base.md`             | Imagens aprovadas devem ter SBOM associado  |
| `03-assinatura-cadeia-trust.md` | Ligação entre integridade e composição      |
| `07-vulnerabilidades-imagens.md`| Análise SCA baseada no SBOM                 |
| `09-riscos-processo-imagens.md` | SBOM como evidência, não decisão            |
| `15-aplicacao-lifecycle.md`     | Integração operacional no ciclo de vida     |

> 🔍 O SBOM responde à pergunta **“o que está aqui?”**.  
> A pergunta **“isto é aceitável?”** continua a exigir análise e decisão humana.
