---
id: guia-estilo-linguagem
title: Guia de Estilo de Linguagem — SbD-ToE
sidebar_position: 90
description: Guia normativo para uniformizar o tom, forma de tratamento e estilo técnico do manual
tags: [estilo, linguagem, tratamento, norma editorial, curadoria]
---

# 📝 Guia de Estilo de Linguagem — SbD-ToE

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

## 🧰 7. Ferramentas auxiliares (opcional)

- Linters de estilo Markdown (`markdownlint`, `Vale`) com regras customizadas.
- Scripts de QA editorial para detetar:
  - Uso de 2ª pessoa (“tu”, “você”)
  - Frases longas (> 25 palavras)
  - Uso de verbos modais não normativos (“convém”, “deveria”)

---

## 🧩 8. Aplicação prática

- Este guia aplica-se a todos os ficheiros `intro.md`, ``, `addon/` — exceto onde explicitamente justificado (ex: `addon/05-exemplos.md` pode usar estilo mais narrativo).
- O mesmo guia será usado para:
  - Revisão manual capítulo a capítulo;
  - Integração em scripts de validação editorial futuros;
  - Revisão final antes da publicação física.

# Guia Editorial e Convenções SbD-ToE (versão 2025-08)

## 1. Templates e Emojis Obrigatórios por Ficheiro

O manual SbD-ToE adota um sistema de templates e emojis para garantir clareza, consistência e processamento automático. Cada ficheiro, secção e bloco tem marcações obrigatórias.

| Template (comentário no topo)      | Emoji obrigatório no h1/header          | Aplicação / Destino                                 |
| ---------------------------------- | --------------------------------------- | --------------------------------------------------- |
| <!--template: sbdtoe-core -->      | 🛠️                                     | Conteúdo técnico prescritivo/normativo (addon/core) |
| <!--template: sbdtoe-addon -->     | 📎                                      | Extensões, integrações, anexos, métodos extra       |
| <!--template: sbdtoe-aplicacao --> | 🛠️                                     | Aplicação transversal ao ciclo de vida (ex-15)      |
| <!--template: sbdtoe-handson -->   | 📝                                      | Casos práticos, exemplos aplicados                  |
| <!--template: sbdtoe-userstory --> | (📝 no rendering/card, não no md)       | User stories/cartões (em secção própria)            |
| <!--template: sbdtoe-preintro -->  | 🧠 (opcional, só se rationale/contexto) | Rationale introdutório/contexto                     |

> Nota: O emoji do título principal deve ser coerente com o template do ficheiro; o emoji 🛠️ é obrigatório em todos os ficheiros aplicacao-lifecycle.md (ex-15).

## 2. Emojis obrigatórios por secção

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

Cada user story/cartão deve ser delimitada por comentários explícitos:

<!--userstory:start-->

### Story: \[Nome da User Story]

\[Descrição curta do objetivo, contexto ou ação.]

**Definition of Done:**

* [ ] Critério 1
* [ ] Critério 2

> \[Nota/referência cruzada, opcional]

<!--userstory:end-->

* Não usar emojis no header da user story (podem ser aplicados visualmente só no rendering).
* Nunca inserir outros headings, títulos ou marcas internas entre início e fim do bloco.
* O parser extrai e renderiza cada bloco como “cartão” reutilizável web ou PDF.

## 4. Exemplos canónicos completos

Inclui sempre:

* Frontmatter YAML obrigatório.
* Linha <!--template: ... --> imediatamente a seguir.
* Título principal com emoji obrigatório.
* Secções internas com emoji correto (ver tabela).
* Blocos de user story delimitados como acima.

---

# Convenção de Tags, Parsing e Build SbD-ToE

## Blocos e tags condicionais suportados

* <!--web-only--> ... <!--web-only:end-->: Só incluído na versão web.
* <!--print-only--> ... <!--print-only:end-->: Só incluído na versão impressa.
* <!--userstory:start--> ... <!--userstory:end-->: Cada bloco é um cartão/user story — será extraído e renderizado separadamente.
* <!--template: sbdtoe-[tipo] -->: Indica o tipo/natureza do ficheiro; obrigatório após o frontmatter.

## Emojis e parsing temático

* O emoji no h1 do ficheiro é obrigatório e corresponde ao template (ver tabela).
* Emojis nas headings internas são usados para parsing semântico (ex: 📅 para triggers, 👥 para papéis, ⚖️ para limiares, etc).
* O parser remove ou substitui emojis na versão impressa segundo a tabela de substituição.

| Template / Tag   | Emoji obrigatório | Parsing/Build         |
| ---------------- | ----------------- | --------------------- |
| sbdtoe-core      | 🛠️               | Título e headings     |
| sbdtoe-addon     | 📎                |                       |
| sbdtoe-aplicacao | 🛠️               |                       |
| sbdtoe-handson   | 📝                |                       |
| sbdtoe-userstory | (none, card)      | Render card block     |
| sbdtoe-preintro  | 🧠 (opcional)     | Só rationale/contexto |

* Todos os headings de user stories/card começam por ### Story:, dentro dos comentários de delimitação.
* O parser processa apenas o conteúdo entre <!--userstory:start--> e <!--userstory:end-->.

## Exemplo de bloco de user story para parsing

<!--userstory:start-->

### Story: Classificação inicial da aplicação

Como responsável técnico, quero classificar a aplicação com base nos eixos E+D+I, para garantir a aplicação proporcional de controlos de segurança.

**Definition of Done:**

* [ ] Modelo aplicado com pontuação 1–3 por eixo
* [ ] Nível L1–L3 definido
* [ ] Documento registado e versionado
* [ ] Controlos mínimos mapeados a partir da matriz

> 🔗 Suporta os domínios *Risk* e *Security Requirements* do OWASP DSOMM.

<!--userstory:end-->

---

Estas adições asseguram que qualquer editor, parser ou build vai saber exatamente como estruturar, identificar, renderizar e publicar os conteúdos do manual SbD-ToE, sem ambiguidade.
