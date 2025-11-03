# Guia de Contribuição – Manual SbD-ToE

Este guia define as regras para a criação e manutenção dos capítulos do manual **Security by Design – Theory of Everything**.

---

## 📁 Estrutura de capítulos

>> Nota: podem existir varios manuais, complementares ou independentes. sbd-manual é o primeiro, mas poderá existir um SSCS-manual, GenAI-manual, etc. Este documento é aplicavel ao manual inicial, sbd-manual, e a outros que venham a ser criados.

Cada capítulo técnico está localizado em:

```
docs/sbd-toe/sbd-manual/XX-nome-do-capitulo/
```

Com a seguinte estrutura:

```
├── _category_.json
├── intro.md
└── addons/
    ├── achievable-maturity              (obrigatório, conteúdo específico)
    ├── 15-aplicacao-lifecycle.md     (obrigatório, conteúdo específico)
    ├── 20-checklist-revisao.md       (obrigatório, conteúdo específico)
    ├── 01-*.md, 02-*.md, etc.         (addons específicos por capítulo)
```

---

## 📌 Ficheiros obrigatórios

cada capitulo tem que conter pelo menos o seguinte:

| Ficheiro                   | Descrição                                                                 |
|----------------------------|---------------------------------------------------------------------------|
| `intro.md`                | Corpo principal do capítulo, inclui objetivos, práticas e recomendações   |
| `achievable-maturity`        | Mapeamento do capítulo para frameworks de maturidade (SAMM, NIST, etc.)   |
| `aplicacao-lifecycle.md` | Quando e como aplicar as práticas do capítulo no ciclo de vida           |

## 📌 Ficheiros recomendados
Não obrigatorios mas, fortemente, recomendados são os:

| Ficheiro                   | Descrição                                                                 |
|----------------------------|---------------------------------------------------------------------------|
| `policies-relevantes.md`   | que descreve o documento policy que regula a pratica, que de acordo com a maturidade da organização deverá ser incluindo como policy da organização  |
| `recomendacoes-avancadas`        | caso existam praticas ou atividades a desenvolver que possam beneficiar a organização no desempenho dos conceitos do capitulo  |

---

## 🧩 Addons específicos

Cada capítulo pode ter ficheiros adicionais explicativos de cada "intro.md", que detalham com rigor técnico e cientifico o que se pretende com o capitulo Estes documentos são colocados em `addon` e deverão usar prefixos `01-`, `02-`, etc., conforme aplicável. 

Exemplos:
- `01-modelo-classificacao-eixos.md`
- `02-casos-praticos.md`
- `03-adopcao-drp-bia.md`
- `04-matriz-controlos-por-risco.md`
- `05-exemplos-aplicacao.md`

O número define a ordem no sidebar. A nomeação deve ser descritiva, curta e estável.

# 🧩 Documentos canon 

Cada capítulo dever ter ficheiros que completem numa perspectiva cientifica o manual. Esses ficheiros são colocado em `canon`, e pelo menos deverão conter:


| Ficheiro                   | Descrição                                                                 |
|----------------------------|---------------------------------------------------------------------------|
| `20-checklist-revisão.md`   | checkilist binario para medir e controlar a implementaçao do recomendado no manual |
| `25-rastreabilidade`        | backtrack do recomendado no manual com outras frameworks e com a explicação da normalizaçao efetuada entre diferentes referencias  (analise top-down)|
| `50-ameacas-mitigadas`        | lista das ameaças mitigadaas com a prática descrita, com referencias e back-track para a referencia original|


---

## ✅ Convenções e tags no frontmatter

Todos os ficheiros `.md` devem conter um frontmatter com:

```yaml
---
id: nome-unico
title: Título a apresentar no menu
tags:
  - tipo:chapter | anexo
  - grupo:base | execucao | validacao | suporte | transversal
  - tema:nome-do-tema-tecnico
---
```

> As `tags:` são usadas para organização, pesquisa e atribuição de labels no GitHub.

---

## 🛠️ Boas práticas

- Evitar markdown embutido dentro de markdown (ex: blocos de código com markdown dentro).
- Manter os títulos coerentes e a numeração dos addons sequencial.
- Não duplicar conteúdo entre capítulos; referenciar se aplicável.
- Usar linguagem objetiva, prescritiva e clara.
- Checklists, quando existam, devem ser binários (Sim/Não).

---

## 📦 Automatização

Scripts estão disponíveis para:
- Gerar ficheiros `addons` obrigatórios
- Zipar capítulos para publicação
- Criar issues e tarefas no GitHub com base nos capítulos

---

Para dúvidas ou pedidos de estrutura, contactar o responsável editorial do projeto.
