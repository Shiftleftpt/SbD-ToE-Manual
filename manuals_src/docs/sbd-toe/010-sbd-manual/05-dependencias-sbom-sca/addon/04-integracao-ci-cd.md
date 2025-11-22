---
description: Integração automatizada de SBOM, SCA e controlo de exceções no ciclo
  de build e release
id: integracao-ci-cd
tags:
- ci-cd
- cicd
- containers
- dependencias
- sbom
- sca
- supply-chain
title: Integração com Pipelines CI/CD
---


# ⚙️ Integração com Pipelines CI/CD

## 🌟 Objetivo

Garantir que as práticas de SBOM, SCA e governaça de dependências são aplicadas de forma **automatizada e rastreável** nos pipelines de build, teste e release das aplicações.

> 🚀 A automação destas práticas assegura aplicação consistente, deteção precoce de riscos e bloqueio controlado de releases com findings graves.

---

## 🛠️ Ações esperadas em pipelines CI/CD

| Fase CI/CD        | Ação esperada                                           | Resultado                              |
|-------------------|---------------------------------------------------------------|----------------------------------------|
| Build             | Geração automática de SBOM (ex: Syft, CycloneDX)           | Artefacto `.json` ou `.xml` versionado |
| Análise de segurança | Execução de SCA com scanner open source ou comercial       | Relatório de findings (SARIF/JSON/HTML) |
| Validação         | Verifica severidade dos findings e aplica policies         | Blocker ou aviso + registo              |
| Release           | Anexa SBOM e findings ao artefacto final                     | Rastreabilidade por versião            |

---

## 💡 Exemplos de integração (pseudocódigo)

```yaml
steps:
  - name: Generate SBOM
    run: syft . -o cyclonedx-json > sbom.json

  - name: Run SCA
    run: grype sbom:sbom.json -o sarif > results.sarif

  - name: Validate findings
    run: ./scripts/validate-findings.sh results.sarif
```

> Pode ser integrado em GitHub Actions, Azure DevOps, GitLab CI, Jenkins, etc.

---

## 🔐 Políticas de bloqueio (exemplos)

| Critério                              | Ação              |
|----------------------------------------|----------------------|
| CVSS >= 9.0 e não mitigado             | Bloqueia pipeline    |
| Vulnerabilidade com exploit conhecido | Requer aprovação formal |
| Finding "medium" com patch disponível | Gera aviso + tarefa  |

> As regras podem ser mantidas num ficheiro versionado (`policy.yaml`) ou num sistema central.

---

## 🔧 Integração com backlog e rastreabilidade

- Findings devem gerar automaticamente:
  - Tarefa em Jira/Azure DevOps
  - Associação ao commit/PR
  - Referência cruzada ao SBOM e artefacto de release

> 📄 Sugere-se uso de formatos como SARIF para permitir importação automática por IDEs e plataformas ALM.

---

## 🔒 Práticas recomendadas por risco

| Risco da aplicação | Prática CI/CD obrigatória                                |
|---------------------|-------------------------------------------------------------|
| L1 (baixo)          | Geração de SBOM + SCA leve (ex: `npm audit`)              |
| L2 (médio)          | SCA formal + bloqueio de findings críticos                 |
| L3 (elevado)        | SBOM completo, SCA automatizado, registo e aprovação de exceções |

---

## 🔗 Ligações com outros ficheiros

| Documento                   | Relação com o pipeline                              |
|-----------------------------|---------------------------------------------------------|
| `01-inventario-sbom.md`     | Fonte de input obrigatória                            |
| `02-analise-sca.md`         | Scanner e validação integrados                       |
| `09-excecoes-e-aceitacao-risco.md` | Controlo de findings com justificação documentada |

---

> 🚀 A integração de SBOM e SCA em pipelines é a ponte entre teoria e execução. Assegura que as políticas definidas pela equipa de segurança são efetivamente aplicadas, auditáveis e repetíveis.
