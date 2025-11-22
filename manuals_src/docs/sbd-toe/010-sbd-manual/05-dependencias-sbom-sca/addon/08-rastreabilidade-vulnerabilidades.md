---
id: rastreabilidade-vulnerabilidades
title: Rastreabilidade entre Vulnerabilidades, Componentes e Ações
description: Modelo de ligação entre findings SCA, SBOM, backlog e releases
tags: [dependencias, rastreabilidade, sbom, sca, supply-chain]
---

# 🔍 Rastreabilidade entre Vulnerabilidades, Componentes e Ações

## 🌟 Objetivo

Garantir que cada vulnerabilidade identificada em componentes de terceiros tem uma **rastreabilidade completa** desde a origem (SBOM + SCA), passando por análise, até à correção ou aceitação documentada.

> ✅ Esta rastreabilidade permite demonstrar conformidade, mitigar riscos de forma justificada, e manter controlo sobre o estado de segurança real das dependências.

---

## 🔢 Elementos da rastreabilidade

| Elemento                 | Exemplo                                      |
|--------------------------|----------------------------------------------|
| **Componente**           | `log4j:log4j-core@2.14.1`                     |
| **Identificador SBOM**   | `purl:maven/log4j/log4j-core@2.14.1`         |
| **Finding / CVE**        | `CVE-2021-44228`                             |
| **Scanner / Relatório**  | `grype`, `snyk`, `OWASP DC`, etc.            |
| **Artefacto afetado**    | `app-backend-1.2.5.jar`                      |
| **Commit de origem**     | `abc123` (pull request onde a dep foi usada) |
| **Tarefa associada**     | `SEC-456` (issue, PR ou tarefa de correção)  |
| **Estado final**         | Corrigido / Aceite com justificativo         |

---

## 📄 Template de registo

```yaml
- cve: CVE-2021-44228
  componente: log4j-core@2.14.1
  purl: pkg:maven/log4j/log4j-core@2.14.1
  artefacto: app-v1.2.5.jar
  introduzido_por: commit abc123
  tarefa: SEC-456
  decisao: corrigido
  evidencias:
    - commit: def789
    - release: v1.2.6
    - scanner: grype-scan-2024-06-02.json
```

> 📁 Sugere-se manter este registo num ficheiro versionado (`vulns.yaml`) ou numa base integrada com Jira ou GitHub Projects.

---

## 🛠️ Integração com ALM / backlog

- Findings SCA devem **criar automaticamente tarefas** de correção (via API ou webhook)
- Os tickets devem conter:
  - Link para o CVE (NVD, GH Advisory)
  - Componentes afetados
  - SBOM + pipeline afetado
  - Critério de aceite (correção validada ou exceção aprovada)

> 🔗 Usar etiquetas normalizadas: `cve`, `sca`, `seguranca`, `sbom`, `rastreabilidade`

---

## ✅ Critérios de conclusão de finding

| Estado final        | Requisitos obrigatórios                                  |
|---------------------|-------------------------------------------------------------|
| **Corrigido**       | PR com update, nova release validada por SCA                |
| **Aceite**          | Justificação técnica + aprovação AppSec/documentada        |
| **Mitigado**        | Controlo compensatório + validação técnica + prazo definido  |
| **Obsoleto**        | Pacote não está mais em uso (excluído do SBOM atual)         |

---

## 🔗 Ligações com outros ficheiros

| Documento                   | Função na rastreabilidade                          |
|-----------------------------|---------------------------------------------------------|
| `01-inventario-sbom.md`     | Fonte de componentes por versão                        |
| `02-analise-sca.md`         | Gera findings com referência a CVEs                   |
| `04-integracao-ci-cd.md`    | Conecta findings ao artefacto e release                 |
| `09-excecoes-e-aceitacao-risco.md` | Formaliza aceitação de findings se não forem corrigidos |

---

> 🔒 A rastreabilidade é um fator crítico em auditorias, resposta a incidentes e governança de segurança. Deve ser sistematizada, versionada e acessível.
