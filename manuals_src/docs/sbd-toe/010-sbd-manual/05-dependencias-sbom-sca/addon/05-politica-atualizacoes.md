---
id: politica-atualizacoes
title: Políticas de Atualização de Dependências
description: Práticas de atualização proativa, TTL, locking e gestão de versões seguras
tags: [dependencias, sbom, sca, supply-chain, policies]
---

# ♻️ Políticas de Atualização de Dependências

## 🌟 Objetivo

Estabelecer práticas sistemáticas para a **atualização proativa de bibliotecas e dependências de terceiros**, evitando acumulação de dívida técnica e exposição prolongada a riscos conhecidos.

> ⚠️ Muitas explorações de vulnerabilidades ocorrem em bibliotecas que já têm patch disponível, mas não foram atualizadas. A política de atualização é uma defesa essencial.

---

## ⏲ Princípios de atualização segura

1. Toda dependência deve ter um **TTL (Time To Live)** definido: prazo máximo até ser revista.
2. Devem ser usados mecanismos de **locking explícito de versões**, para evitar atualizações não auditadas.
3. As atualizações devem ser **automatizadas onde possível**, mas sempre **validadas** antes do deploy.
4. A atualização periódica deve ser tratada como **parte do ciclo de desenvolvimento**, não como exceção.

---

## 🛠️ Mecanismos de controlo por linguagem

| Stack       | Lockfile / Mecanismo           | Ferramentas de atualização         |
|-------------|----------------------------------|------------------------------------|
| Node.js     | `package-lock.json`, `npm ci`   | `npm-check-updates`, RenovateBot   |
| Python      | `requirements.txt`, `pip-tools` | `pip-review`, Dependabot           |
| Java (Maven)| `pom.xml`, versão fixa          | Versions Maven Plugin              |
| .NET        | `packages.lock.json`, `*.csproj`| `dotnet outdated`, NuKeeper        |
| Go          | `go.sum`, `go.mod`              | `go get -u`, Dependabot            |

> 🔐 O uso de lockfiles é essencial para reproduzibilidade e rastreabilidade.

---

## 🔧 Frequência recomendada de revisão

| Tipo de projeto         | Frequência mínima de revisão de dependências |
|--------------------------|------------------------------------------------|
| Produção crítica (L3)    | Semanal (automática + validação manual)      |
| Backend / API (L2)       | Quinzenal                                     |
| Interno / Ferramentas (L1)| Mensal                                       |

> Findings SCA devem ser tratados **fora deste ciclo**, em regime reativo (ex: CVE com alerta).

---

## 📅 Estratégias de atualização

- **Proativa automatizada**: bots que abrem PRs de atualização com testes
- **Agrupada por sprint**: tarefa periódica de "atualização de libs"
- **Controlo semântico**: limites de `^`, `~` e ranges definidos
- **Pinning de versões críticas**: ex. `express@4.18.2` vs `express@latest`

---

## 📄 Checklist de aplicação de updates

| Item                                                           | Verificado? |
|----------------------------------------------------------------|-------------|
| Existe lockfile e é versionado?                              | ☑         |
| Atualizações periódicas são feitas de forma rastreável? | ☑         |
| Todas as atualizações passam por CI/CD com testes?           | ☑         |
| As versões são auditadas por SCA após update?                 | ☑         |
| Atualizações críticas são tratadas em menos de 48h?          | ☑         |

---

## 🔗 Ligações com outros ficheiros

| Documento                   | Ligação com atualizações                            |
|-----------------------------|-------------------------------------------------------------|
| `02-analise-sca.md`         | Detecta vulnerabilidades que podem requerer atualização      |
| `04-integracao-ci-cd.md`    | Automatiza updates e aplica validadores no pipeline         |
| `03-governanca-libs-terceiros.md` | Define quais dependências podem ou não ser atualizadas |

---

> ✅ A atualização de dependências é um processo técnico e de gestão de risco. Não deve ser adiado indefinidamente, nem feito sem validação e rastreabilidade adequada.
