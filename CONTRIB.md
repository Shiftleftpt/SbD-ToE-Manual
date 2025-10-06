# Guia de Contribuição – Manual SbD-ToE

Este guia define as regras para a criação e manutenção dos capítulos do manual **Security by Design – Theory of Everything**.

---

## 📁 Estrutura de capítulos

Cada capítulo técnico está localizado em:

```
docs/sbd-toe/XX-nome-do-capitulo/
```

Com a seguinte estrutura:

```
├── _category_.json
├── intro.md
└── addons/
    ├── 10-maturidade.md              (obrigatório, conteúdo específico)
    ├── 15-aplicacao-lifecycle.md     (obrigatório, conteúdo específico)
    ├── 20-checklist-revisao.md       (obrigatório, conteúdo específico)
    ├── 01-*.md, 02-*.md, etc.         (addons específicos por capítulo)
```

---

## 📌 Ficheiros obrigatórios

| Ficheiro                   | Descrição                                                                 |
|----------------------------|---------------------------------------------------------------------------|
| `intro.md`                | Corpo principal do capítulo, inclui objetivos, práticas e recomendações   |
| `10-maturidade.md`        | Mapeamento do capítulo para frameworks de maturidade (SAMM, NIST, etc.)   |
| `15-aplicacao-lifecycle.md` | Quando e como aplicar as práticas do capítulo no ciclo de vida           |
| `20-checklist-revisao.md` | Checklist binário para validar adoção do capítulo                         |
| `_category_.json`         | Entrada de navegação Docusaurus                                           |

> ⚠️ Os ficheiros `10`, `15` e `20` são **comuns em nome e função**, mas **o conteúdo é sempre específico do capítulo**.

---

## 🧩 Addons específicos

Cada capítulo pode ter ficheiros adicionais com prefixos `01-`, `02-`, etc., conforme aplicável.

Exemplos:
- `01-modelo-classificacao-eixos.md`
- `02-casos-praticos.md`
- `03-adopcao-drp-bia.md`
- `04-matriz-controlos-por-risco.md`
- `05-exemplos-aplicacao.md`

O número define a ordem no sidebar. A nomeação deve ser descritiva, curta e estável.

---

## ✅ Convenções e tags no frontmatter

Todos os ficheiros `.md` devem conter um frontmatter com:

```yaml
---
id: nome-unico
title: Título a apresentar no menu
sidebar_position: XX
tags:
  - tipo:chapter | anexo
  - grupo:base | execucao | validacao | suporte | transversal
  - tema:nome-do-tema-tecnico
---
```

> As `tags:` são usadas para organização, pesquisa e atribuição de labels no GitHub.

---

## 🛠️ Boas práticas

- Evita markdown embutido dentro de markdown (ex: blocos de código com markdown dentro).
- Mantém os títulos coerentes e a numeração dos addons sequencial.
- Não duplicar conteúdo entre capítulos; referenciar se aplicável.
- Usa linguagem objetiva, prescritiva e clara.
- Checklists devem ser binários (Sim/Não).

---

## 📦 Automatização

Scripts estão disponíveis para:
- Gerar ficheiros `addons` obrigatórios
- Zipar capítulos para publicação
- Criar issues e tarefas no GitHub com base nos capítulos

---

Para dúvidas ou pedidos de estrutura, contactar o responsável editorial do projeto.
