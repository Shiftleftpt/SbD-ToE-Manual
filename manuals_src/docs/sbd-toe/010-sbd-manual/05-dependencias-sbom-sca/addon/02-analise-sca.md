---
id: analise-sca
title: Análise de Vulnerabilidades em Dependências (SCA)
description: Práticas de Software Composition Analysis para detetar, priorizar e mitigar vulnerabilidades conhecidas
tags: [dependencias, sbom, sca, supply-chain]
---

# ⚠️ Análise de Vulnerabilidades em Dependências (SCA)

## 🌟 Objetivo

Assegurar que todas as dependências externas (diretas e transitivas) são analisadas automaticamente e de forma recorrente quanto a **vulnerabilidades conhecidas**, com rastreabilidade entre:

- Componente identificado no SBOM
- Vulnerabilidade associada (CVE)
- Artefacto e versão afetados
- Tarefa de correção, exceção ou mitigacão

> O processo de SCA é essencial para reduzir o risco associado à reutilização de bibliotecas e pacotes de terceiros.

---

## 🚀 Como funciona o processo de SCA

1. O SBOM gerado é usado como input para o scanner.
2. Cada componente é comparado com bases de dados de vulnerabilidades (NVD, GitHub Advisories, OSV, etc.).
3. Para cada CVE encontrado, são identificados:
   - Severidade (CVSS base score ou equivalente)
   - Vetor de exploração (local, remoto, etc.)
   - Estado do patch / correção
4. É gerado um **relatório processável** (ex: JSON, HTML, SARIF) e, se aplicável, bloqueado o pipeline.

---

## 🤖 Ferramentas open source recomendadas

| Ferramenta     | Linguagens / Suporte           | Observações                             |
|----------------|-------------------------------|--------------------------------------------|
| **Syft**       | Multi-stack (Node, Java, etc.) | Gera SBOM + integra com Grype              |
| **Grype**      | Multi-stack                    | Scanner de vulnerabilidades com OSV/NVD    |
| **Trivy**      | Apps, containers, IaC          | SCA + SAST + secret scanning               |
| **OWASP DC**   | Java/Maven/Gradle              | OWASP Dependency-Check, bem suportado      |
| **OSV-Scanner**| Node, Go, Rust, Python         | Usa base OSV.dev, integra com GitHub       |

> 💡 Syft + Grype é uma combinação particularmente eficaz para pipelines modernos.

---

## 💳 Ferramentas comerciais com cobertura alargada

| Ferramenta       | Destaques relevantes para o SbD-ToE                               |
|------------------|--------------------------------------------------------------------|
| **Snyk**          | SCA, IaC scanning, CI/CD integration, policy enforcement          |
| **GitHub Advanced Security** | CodeQL + SCA + Secret scanning integrados no repositório     |
| **Jfrog Xray**    | Repositórios, SCA, container scanning, SBOM centralizado           |
| **WhiteSource (Mend)** | Licenças, riscos, policies, alertas centralizados                |
| **Checkmarx One** | SAST, SCA, IaC, API Security com integração por linguagem e pipeline |

> Estas ferramentas podem ser justificadas em ambientes regulados ou com grandes volumes de projetos.

---

## 🌐 Integração no ciclo de vida

| Momento                          | Ação esperada                            | Resultado                           |
|----------------------------------|--------------------------------------|-------------------------------------|
| 📁 Build                  | Scanner SCA executado com input do SBOM | Relatório + status do build         |
| 📑 Pull Request           | Alertas visíveis e findings triados        | Aprovação condicionada ou bloqueio |
| ✅ Release                     | Verificação de findings pendentes         | Go/no-go                            |
| 🚨 Vuln. divulgada       | Notificação, triagem e correção associada   | Issue/ticket com rastreabilidade    |

---

## ⚠️ Priorizando findings

Os findings devem ser triados com base em:

- **Severidade**: CVSS > 7.0 = Crítico
- **Exposição**: A aplicação é pública? A função afetada está acessível?
- **Impacto**: Dados sensíveis ou ações críticas estão envolvidos?
- **Mitigação alternativa**: Existe controle compensatório documentado?
- **Fix disponível?**: Versão corrigida existe?

> Findings sem exploração plausível **não devem ser ignorados**, mas classificados como "aceite" com base em risco justificado.

---

## 🔗 Ligação com backlog e rastreabilidade

| Elemento                     | Forma recomendada                            |
|-----------------------------|-----------------------------------------------|
| Finding (ex: CVE-2023-1234) | Criar issue com referência ao SBOM/component |
| Estado                      | "Pendente", "Corrigido", "Aceite c/ justificativo" |
| Tags                        | `sca`, `vuln`, `sbom`, `seguranca`, `cve`     |
| Evidência de correção         | PR, commit, release, artefacto atualizado     |

> 💡 Sugere-se um dashboard por projeto com estado de findings ativos + link para tarefa associada.

---

## 🔒 Referências cruzadas

| Documento                   | Ligação com SCA                                |
|-----------------------------|-----------------------------------------------|
| `01-inventario-sbom.md`     | Fonte de componentes a analisar               |
| `04-integracao-ci-cd.md`    | Execução automatizada no pipeline              |
| `08-rastreabilidade-vulnerabilidades.md` | Mapping entre finding, ação e release |

---

> 🔎 A análise SCA deve ser **documentada, automatizada e priorizada**, integrando-se com ferramentas de backlog, repositórios de código e artefactos de release.
