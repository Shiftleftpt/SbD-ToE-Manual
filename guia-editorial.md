---
id: guia-estilo-linguagem
title: Guia de Estilo de Linguagem - SbD-ToE
sidebar_position: 90
description: Guia normativo para uniformizar o tom, forma de tratamento e estilo técnico do manual
tags: [estilo, linguagem, tratamento, norma editorial, curadoria]
---

# Guia de Contribuição – regras editoriais

Este guia define as regras para a criação e manutenção dos capítulos do manual **Security by Design – Theory 
of Everything (SbD-ToE)**


> Podem existir vários manuais, complementares ou independentes.
> `sbd-manual` é o primeiro, mas poderão existir outros (ex.: `sscs-manual`, `genai-manual`).
> Este documento aplica-se ao manual inicial e serve de referência aos seguintes.
## ✍️ Regras editoriais e formato 

Cada capítulo técnico está localizado em:

```
docs/sbd-toe/sbd-manual/XX-nome-do-capitulo/
```

---

### 📁 Estrutura de capítulos

```
├── _category_.json
├── intro.md
├── achievable-maturity.md
├── aplicacao-lifecycle.md
├── recomendacoes-avancadas.md
├── policies-relevantes.md
├── addon/
│   ├── 01-*.md … 09-*.md
│   └── ...
└── canon/
    ├── 20-checklist-revisao.md
    ├── 25-rastreabilidade.md
    └── 50-ameacas-mitigadas.md
```

---

## 📌 Ficheiros obrigatórios

| Ficheiro                 | Descrição                                                                |
| ------------------------ | ------------------------------------------------------------------------ |
| `intro.md`               | Corpo principal do capítulo; objetivos, práticas e recomendações.        |
| `achievable-maturity.md` | Alinhamento do capítulo com frameworks de maturidade (SAMM, SSDF, etc.). |
| `aplicacao-lifecycle.md` | Quando e como aplicar as práticas no ciclo de vida (SDLC).               |

---

## 📌 Ficheiros recomendados

| Ficheiro                     | Descrição                                                                                                             |
| ---------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `recomendacoes-avancadas.md` | Práticas ou atividades avançadas que podem elevar o desempenho no tema do capítulo.                                   |
| `policies-relevantes.md`     | Lista de políticas organizacionais relevantes ao tema; objetivos e conteúdo mínimo esperado (não constitui template). |

---

## 🧩 Addons específicos (`addon/`)

Documentos técnicos complementares ao `intro.md`, numerados `01–09` para definir a ordem no *sidebar*.
A nomeação deve ser curta, descritiva e estável.

**Exemplos:**

* `01-modelo-classificacao-eixos.md`
* `02-casos-praticos.md`
* `03-adopcao-drp-bia.md`
* `04-matriz-controlos-por-risco.md`
* `05-exemplos-aplicacao.md`

---

## 🧩 Documentos *canon* (`canon/`)

| Ficheiro                  | Descrição                                                                                                                   |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| `20-checklist-revisao.md` | Checklist binário (Sim/Não) para medir e controlar a aplicação prática do capítulo, por projeto.                            |
| `25-rastreabilidade.md`   | Mapeamento *top-down* do capítulo para normas e frameworks (SSDF, SAMM, BSIMM, etc.) com notas de normalização e evidência. |
| `50-ameacas-mitigadas.md` | Lista de ameaças mitigadas pelo capítulo, com “como surge”, “como mitiga” e controlos associados (OSC&R, CAPEC, etc.).      |

---

## ✅ Frontmatter (YAML)

```yaml
---
id: nome-unico
title: Título a apresentar no menu
tags:
  - tipo: chapter | anexo
  - grupo: base | execucao | validacao | suporte | transversal
  - tema: nome-do-tema-tecnico
---
```

> As *tags* são utilizadas para organização, pesquisa e rotulagem no GitHub.

---

## 🛠️ Boas práticas

* Manter títulos coerentes e numeração sequencial nos `addon/` (`01–09`).
* Evitar *markdown* dentro de *markdown* em blocos de código.
* Não duplicar conteúdo entre capítulos; preferir referências cruzadas.
* Utilizar linguagem objetiva, prescritiva e clara.
* Garantir que todas as checklists são **binárias (Sim/Não)**.

---

# 📝 Guia de Estilo de Linguagem - SbD-ToE

> Este guia estabelece o tom, estilo e forma de tratamento adotados no manual *Security by Design – Theory of Everything (SbD-ToE)*, assegurando uniformidade, clareza e autoridade técnica em todos os capítulos e formatos (web e livro).

---

## 🎯 1. Objetivo do Estilo

- Garantir linguagem **técnica, clara e impessoal**.
- Transmitir autoridade normativa e aplicabilidade prática.
- Evitar ambiguidade, opinião pessoal ou tom coloquial.

---

## 🗣️ 2. Forma de tratamento

| Situação                  | Forma adotada                       | Exemplo                                      |
|---------------------------|--------------------------------------|----------------------------------------------|
| Direções ou recomendações | ✅ Forma **atónica** (impessoal)     | “Deve ser definido um owner de segurança.”   |
| Descrição de ações        | ✅ Terceira pessoa / forma passiva   | “A validação deve ocorrer antes do deploy.”  |
| **Evitar**                | ❌ Uso de “tu”, “você”, “nós”        | “Precisas de rever o código…” ❌             |

---

## 🏗️ 3. Estilo estrutural

| Elemento                        | Regras recomendadas                                     |
|--------------------------------|----------------------------------------------------------|
| Frases                         | ✅ Curtas, diretas, foco na ação                         |
| Parágrafos                     | ✅ Breves (4–5 linhas), um conceito por parágrafo        |
| Verbos                         | ✅ Modo indicativo (ex: “deve”, “requer”)                |
| Modais                         | ✅ Normativos (RFC 2119): **deve**, **pode**, **não deve**|
| Termos técnicos                | ✅ Definidos na primeira ocorrência                      |
| Emojis / badges                | ✅ Permitidos apenas na versão online (`<Badge>` etc.)   |

---

## 🧾 4. Vocabulário prescritivo

| Termo preferido        | Uso                          | Alternativas a evitar           |
|------------------------|-------------------------------|---------------------------------|
| “deve”                 | Obrigatoriedade normativa     | “é importante que”, “convém”    |
| “pode”                 | Ação opcional mas válida      | “talvez”, “seria útil”          |
| “não deve”             | Proibição / contraindicação   | “não é boa ideia”               |
| “é recomendado que”    | Boa prática, não obrigatória  | “sugere-se”, “aconselha-se”     |

---

## ❌ 5. Expressões a evitar

| Expressão / estilo            | Porquê evitar?                               | Exemplo de correção                             |
|------------------------------|----------------------------------------------|------------------------------------------------|
| “Tu deves...”, “Precisas de...” | Tom coloquial e direto                       | “Deve ser feita validação antes do commit.”    |
| “Achamos que...”, “A nossa opinião...” | Retira autoridade                        | “A aplicação desta prática melhora a rastreabilidade.” |
| “A empresa deverá considerar…” | Ambíguo                                     | “A organização deve aplicar controlo formal…”  |
| “Isto é útil quando…”         | Vago e opinativo                            | “Esta prática deve ser aplicada quando...”     |

---

## 🔎 6. Exemplos positivos

✅ Boa:

> “Deve ser mantido um registo de todas as exceções de segurança com owner, data de expiração e compensações definidas.”

✅ Boa:

> “A organização pode optar por validadores automáticos, desde que exista cobertura mínima para os controlos críticos definidos.”

---

## 🚫 Exemplos negativos

❌ Má:

> “Tu deves rever o SBOM de vez em quando para evitar problemas.”

❌ Má:

> “Pode ser boa ideia ter políticas de segurança. Achamos que ajuda.”

---

## 🧩 7. Aplicação prática

- Este guia aplica-se a todos os ficheiros `intro.md`, ``, `addon/` - exceto onde explicitamente justificado (ex: `addon/05-exemplos.md` pode usar estilo mais narrativo).
- O mesmo guia será usado para:
  - Revisão manual capítulo a capítulo;
  - Integração em scripts de validação editorial futuros;
  - Revisão final antes da publicação física.

# Guia Editorial e Convenções SbD-ToE (versão 2025-08)

## 1. Templates e Emojis recomendados por Ficheiro

O manual SbD-ToE adota um sistema de templates e emojis para garantir clareza, consistência e processamento automático.
O emoji do título principal deve ser coerente com o template do ficheiro; por exemplo, o emoji 🛠️ é obrigatório em todos os ficheiros aplicacao-lifecycle.md .

## 2. Emojis adequados por secção

| Emoji | Tema editorial / Secção                 |
| ----- | --------------------------------------- |
| 🛠️   | Ferramenta, aplicação técnica, meios    |
| 📅    | Quando aplicar, triggers, fases         |
| 👥    | Papéis, responsabilidades               |
| ⚖️    | Limiares, proporcionalidade             |
| 📝    | Exemplos práticos                       |
| 📌    | Nota técnica, recomendação final        |
| 🔄    | Ciclo, processo iterativo               |
| 📊    | Matriz, tabela comparativa              |
| 🧾    | Critérios de aceitação, exceção         |
| 🚀    | Recomendações de maturidade             |
| ❌     | Critérios de rejeição, não conformidade |
| 🔗    | Ligações úteis, xrefs                   |
| 🧠    | Rationale/contexto (só preintro)        |

## 3. Convenção para User Stories e Cartões

O capitulo applicacao_lifecycle, descreve user stories para a aplicação do capitulo na pratica do SDLC, cada user story/cartão deve ser formatada de forma expecifica para que a formatação seja aplicada:

### Story: \[Nome da User Story]

\[Descrição curta do objetivo, contexto ou ação.]

**Definition of Done:**

* [ ] Critério 1
* [ ] Critério 2

> \[Nota/referência cruzada, opcional]


* Não usar emojis no header da user story (podem ser aplicados visualmente só no rendering).
* Nunca inserir outros headings, títulos ou marcas internas entre início e fim do bloco.
* O parser extrai e renderiza cada bloco como “cartão” reutilizável web ou PDF.

## 4. Exemplos canónicos completos

Inclui sempre:

* Frontmatter YAML obrigatório.
* Título principal com emoji obrigatório.
* Secções internas com emoji correto (ver tabela).
* Blocos de user story delimitados como acima.

---

Estas adições asseguram que qualquer editor, parser ou build vai saber exatamente como estruturar, identificar, renderizar e publicar os conteúdos do manual SbD-ToE, sem ambiguidade.
