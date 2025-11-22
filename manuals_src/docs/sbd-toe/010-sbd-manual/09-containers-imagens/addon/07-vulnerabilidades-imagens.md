---
id: vulnerabilidades-imagens
title: Deteção e Tratamento de Vulnerabilidades em Imagens
description: Identificação, triagem e mitigação de vulnerabilidades em *containers* com base em SBOM e scanners automatizados
tags: [containers, cve, imagem, sca, syft, trivy, vulnerabilidades]
---

# 🧨 Deteção e Tratamento de Vulnerabilidades em Imagens

## 🌟 Objetivo

Garantir que todas as imagens de *container* utilizadas em execução **são analisadas quanto a vulnerabilidades conhecidas (CVEs)** antes de serem usadas em pipelines, ambientes de staging ou produção - e que existem mecanismos claros para:

- **Identificar vulnerabilidades presentes nas imagens**;
- **Classificá-las por severidade, contexto e impacto real**;
- **Definir critérios de aceitação ou bloqueio automático**;
- **Reforçar o ciclo de feedback e correção contínua**.

---

## 🧬 O que são vulnerabilidades em imagens

Cada imagem de *container* inclui **bibliotecas, runtimes e binários** que podem conter vulnerabilidades conhecidas (ex: CVE-2023-0464). Estas vulnerabilidades podem ser:

- Herdadas da imagem base (`ubuntu`, `alpine`, etc.);
- Introduzidas por `RUN apt install`, `pip install`, `npm install`;
- Transitivas - dependências de bibliotecas usadas pela aplicação.

> ⚠️ Uma imagem funcional pode conter dezenas ou centenas de vulnerabilidades - especialmente se não for minimizada.

---

## 📘 Ferramentas de análise (SCA para *containers*)

| Ferramenta      | Descrição                                | Integração recomendada               |
|------------------|--------------------------------------------|--------------------------------------|
| **Trivy**        | Scanner leve, rápido e atualizado          | GitHub Actions, CLI, K8s Admission   |
| **Grype**        | Foco em precisão e integração com Syft     | Pipelines CI/CD, build-time          |
| **Snyk Container** | Serviço SaaS com CVSS e contexto fix     | Dashboards e pipelines premium       |
| **Docker Scout** | Visual interativo de camadas e CVEs        | Docker Desktop, pipelines via CLI    |

---

## 🛠️ Como aplicar a validação

1. **Gerar SBOM da imagem** (ver `06-sbom-containers.md`);
2. **Executar scanner SCA** (ex: `trivy image nome:tag`);
3. **Analisar resultados por severidade, pacote e contexto**;
4. **Classificar CVEs como “aceitáveis”, “corrigíveis” ou “bloqueantes”**;
5. **Gerar relatório com metadados: score CVSS, fix disponível, pacote afetado**;
6. **Integrar a validação como etapa obrigatória no pipeline**;
7. **Marcar builds como falhados se violarem políticas de risco definidas**;
8. **Armazenar resultados como artefacto audível e versionado**.

---

## 📂 Onde configurar e armazenar resultados

- Diretório dedicado por imagem: `/.sca-reports/<imagem>.json`;
- Publicação como artefacto da build (GitHub, ADO, GitLab);
- Integração com sistemas de alerta contínuo;
- Armazenamento opcional em transparency log (vinculado ao SBOM).

---

## ✅ Boas práticas

- Usar **CVSS ≥ 7.0 como limite inicial** para bloqueio;
- Validar também **dependências transitivas e sistema base**;
- Integrar validação com `pull request checks` e `pre-deploy gates`;
- Estabelecer políticas claras de aceitação de risco e triagem;
- Automatizar criação de tarefas para CVEs com correção disponível;
- Sincronizar scanners com bases de dados atualizadas (NVD, GHSA, Alpine SecDB);
- Evitar `false positives` com context-aware validation (ex: exploitability).

---

## 📎 Referências cruzadas

| Documento                      | Relação com validação de vulnerabilidades     |
|-------------------------------|-----------------------------------------------|
| `01-imagens-base.md`             | Imagens devem ser validadas antes do uso       |
| `06-sbom-containers.md`         | Scanner utiliza SBOM como input                |
| `03-assinatura-cadeia-trust.md` | Pode associar validação ao registo de confiança|
| `09-exemplo-pipeline-container.md` | Exemplo de scanner no pipeline                 |
| `achievable-maturity`              | Deteção automatizada é critério de maturidade  |

> 🚨 Ignorar vulnerabilidades conhecidas em imagens de produção é aceitar riscos silenciosos. A triagem contínua deve ser integrada no ciclo de desenvolvimento.
