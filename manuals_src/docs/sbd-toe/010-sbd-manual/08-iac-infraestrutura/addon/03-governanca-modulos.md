---

id: governanca-modulos
title: Governação de Módulos e Reutilização Segura
sidebar_position: 3
description: Práticas prescritivas de governação, validação e controlo de módulos reutilizáveis em IaC, garantindo segurança, proveniência e rastreabilidade.
tags: [governação, módulos, iac, reutilização, segurança, supply-chain, rastreabilidade]
----------------------------------------------------------------------------------------

# 🛡️ Governação de Módulos Reutilizáveis em IaC

## 🌟 Objetivo

Assegurar que **todos os módulos reutilizados em projetos de Infraestrutura como Código (IaC)** — internos ou externos — são tratados como **componentes de supply chain**, sujeitos a governação formal, validação contínua e evidência auditável.

Em concreto, este ficheiro estabelece como garantir que os módulos são:

* provenientes de **fontes confiáveis e identificáveis**;
* **versionados, imutáveis e determinísticos**;
* **validados antes da reutilização**;
* **aprovados explicitamente** para uso por ambiente;
* **rastreáveis** ao longo do ciclo de vida;
* resistentes a riscos introduzidos por **automação e ferramentas assistidas**.

> A reutilização sem governação formal de módulos representa um **risco sistémico de supply chain**: uma única má prática pode propagar-se transversalmente por múltiplos projetos e ambientes.

---

## 🧩 Princípio base: módulos como código não confiável por origem

Independentemente de serem:

* internos,
* externos,
* gerados automaticamente,
* sugeridos por templates ou ferramentas assistidas,

👉 **todo o módulo deve ser tratado como código não confiável por origem**.

Consequentemente:

* nenhum módulo pode ser consumido sem validação prévia;
* a confiança não é implícita (nem pelo autor, nem pela ferramenta);
* a decisão de reutilização deve ser **explícita, rastreável e evidenciada**.

Este princípio alinha a governação de módulos IaC com práticas modernas de **segurança da cadeia de fornecimento de software**.

---

## 📌 O que deve ser feito (prescrição mínima)

A organização **deve garantir**, no mínimo:

1. Registo formal de módulos internos com:

   * origem,
   * responsável (*owner*),
   * versão,
   * estado de aprovação;
2. Validação de **proveniência e integridade** de módulos externos antes da adoção;
3. Definição de **fontes confiáveis (allowlist)** e bloqueio de origens não autorizadas;
4. Controlo rigoroso de versões, evitando referências flutuantes (`main`, `latest`, ranges abertos);
5. Documentação mínima obrigatória por módulo (inputs, outputs, dependências, efeitos);
6. Validação automática de módulos internos antes de publicação;
7. Inventário/SBOM de módulos efetivamente usados por ambiente;
8. Revisão periódica de módulos críticos em uso ativo.

---

## ⚙️ Como aplicar (mecanismos técnicos)

| Dimensão                 | Prescrição                                                                 |
| ------------------------ | -------------------------------------------------------------------------- |
| **Módulos internos**     | Repositório central versionado, CI/CD obrigatório, releases imutáveis      |
| **Módulos externos**     | Referência com versão fixa ou digest (`?ref=v1.2.3` ou SHA)                |
| **Fontes confiáveis**    | Allowlist explícita (ex.: `registry.terraform.io/org/`, `github.com/org/`) |
| **Controlo de versões**  | Proibir `main`, `latest` e ranges abertos em L2/L3                         |
| **Integridade**          | Verificação de hash/digest quando aplicável                                |
| **Aprovação**            | Associação explícita a análise de risco e decisão de aprovação             |
| **Validação automática** | Lint, segurança e documentação antes de `publish`                          |
| **Inventário / SBOM**    | Lista de módulos usados por deploy/ambiente                                |

---

## 🔍 Validação e controlo reforçado para automação/assistência

Quando módulos são:

* gerados automaticamente,
* alterados em massa,
* sugeridos por ferramentas assistidas,

devem aplicar-se **regras reforçadas**:

* validação semântica do impacto do módulo (recursos, permissões, exposição);
* revisão humana obrigatória antes de aprovação;
* evidência explícita de decisão (quem aprovou, porquê, para que ambientes).

> Este controlo evita que **erros sistemáticos ou defaults inseguros** se propaguem automaticamente.

---

## 🕒 Quando aplicar

| Momento                             | Ação esperada                                         |
| ----------------------------------- | ----------------------------------------------------- |
| Inclusão de módulo externo          | Validar origem, versão, integridade e conformidade    |
| Criação/alteração de módulo interno | Validar sintaxe, segurança e outputs antes de release |
| Pipeline de build/deploy            | Confirmar que apenas módulos aprovados são usados     |
| Revisão periódica                   | Verificar manutenção, vulnerabilidades e uso ativo    |
| Incidente ou alerta                 | Reavaliar todos os projetos dependentes do módulo     |

---

## 👥 Perfis envolvidos

| Papel              | Responsabilidade                                    |
| ------------------ | --------------------------------------------------- |
| DevOps / Infra     | Integração técnica e consumo de módulos             |
| Arquitetura        | Definição de padrões modulares e fontes autorizadas |
| AppSec / Segurança | Validação de origem, integridade e risco            |
| Cloud / Plataforma | Gestão do repositório interno e ciclo de vida       |
| GRC / Compliance   | Supervisão de aprovação e rastreabilidade           |

---

## 🧪 Exemplos práticos

**Referência segura a módulo externo**

```hcl
source = "git::https://github.com/org/vpc-module.git?ref=v1.2.3"
```

**Bloqueio de fontes não autorizadas em pipeline**

```bash
ALLOW_MODULE_SOURCES = [
  "registry.terraform.io/org/",
  "github.com/org/"
]
```

**Pipeline de publicação de módulo interno**

* `tflint` (linting)
* `checkov` ou `tfsec` (segurança)
* `terraform-docs` (documentação atualizada)
* aprovação explícita antes de `release`

**Inventário interno (exemplo)**

* Nome do módulo
* Owner
* Versão
* Última validação
* Ambientes onde é usado

---

## ⚖️ Proporcionalidade L1–L3

| Controlo              | L1          | L2          | L3                             |
| --------------------- | ----------- | ----------- | ------------------------------ |
| Allowlist de fontes   | Recomendado | Obrigatório | Obrigatório                    |
| Pinning de versão     | Obrigatório | Obrigatório | Obrigatório                    |
| Validação automática  | Recomendado | Obrigatório | Obrigatório                    |
| Aprovação formal      | Recomendado | Obrigatório | Obrigatório (reforçada)        |
| Inventário/SBOM       | Recomendado | Obrigatório | Obrigatório                    |
| Revalidação periódica | Recomendado | Obrigatório | Obrigatório + frequência maior |

---

## 🔗 Referências cruzadas

| Documento                                       | Relação                                    |
| ----------------------------------------------- | ------------------------------------------ |
| `addon/02-validacoes-e-checks.md`               | Validação e evidência de módulos           |
| `addon/11-uso-ferramentas-automatizadas-iac.md` | Automação/assistência e riscos de processo |
| SSDF (PW.4, CM.3)                               | Governação de componentes reutilizados     |
| SLSA (Source L2+)                               | Proveniência e integridade de código       |
| CIS Controls (2, 8)                             | Gestão segura de software reutilizado      |

---

> 📌 A governação de módulos é um **controlo estrutural de supply chain** em IaC. Sem validação, aprovação e evidência explícitas, a reutilização transforma-se num **multiplicador de risco**.
