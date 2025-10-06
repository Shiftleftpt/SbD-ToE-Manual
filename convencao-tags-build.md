# 🏗️ Convenções de Marcação Semântica — Web vs Livro

Este documento define as convenções técnicas e editoriais para marcação e referência nos `.md` do manual *Security by Design – Theory of Everything (SbD-ToE)*, permitindo manter **um único repositório fonte** com suporte simultâneo para:

* Versão **interativa online** (Docusaurus)
* Versão **impressa/eBook** (Pandoc + LaTeX)

Estas marcações permitem processamento automático e controlado de âncoras internas e referências cruzadas.

---

## 🧷 Âncoras editoriais automáticas (`{#...}`)

* **Todas as âncoras em headings são geradas automaticamente** por script (`add_anchors.py`) durante a curadoria e build.
* **Qualquer âncora manual `{#...}` é removida** e substituída pela âncora editorial baseada no texto do heading (normalizado).
* O formato é `{#texto-normalizado}`: minúsculas, sem acentos, pontuação ou emojis, espaços substituídos por hífen.
* **Nunca definir âncoras manualmente.** Basta escrever o heading.

**Exemplo:**

Antes:

```markdown
## 🧭 Visão Geral {#link-custom}
```

Depois do script:

```markdown
## 🧭 Visão Geral {#visao-geral}
```

---

## 🔗 Referências cruzadas semânticas (`xref:`)

* Usar sempre `[texto do link](xref:path#ancora)` para links internos entre capítulos, secções ou artefactos.
* O “path” é sempre absoluto (`xref:capNN/addon/ficheiro#ancora-normalizada`).
* A âncora de destino é **exatamente** a forma normalizada produzida por `add_anchors.py`.

**Exemplo:**

```markdown
[Consultar valores normalizados](xref:cap02/addon/tabela-valores#valores-normalizados-de-risco)
```

Destino:

```markdown
# 📊 Valores Normalizados de Risco {#valores-normalizados-de-risco}
```

> Sempre que um heading é alterado, os `xref:` que apontam para ele devem ser atualizados.

---

## 🔁 Tags de Inclusão Condicional

* `<!--web-only--> ... <!--end-web-only-->`: Conteúdo exclusivo web (Docusaurus)
* `<!--print-only--> ... <!--end-print-only-->`: Conteúdo exclusivo print (PDF/Livro)
* `<!--print-anexo:X-->`: Bloco para anexos

---

## 🧰 IDs padronizados para referência cruzada

| Tipo     | Convenção                        | Exemplo                          |
| -------- | -------------------------------- | -------------------------------- |
| Capítulo | `xref:capNN`                     | `xref:cap05`                     |
| Ficheiro | `xref:capNN/addon/ficheiro`      | `xref:cap05/addon/modelo`        |
| Secção   | `#valores-normalizados-de-risco` | `#valores-normalizados-de-risco` |

---

## 🏷️ Workflow editorial recomendado

1. **Escrever headings SEM âncoras manuais.**
2. **Usar sempre `xref:` para referências internas, indicando o path e a âncora editorial.**
3. **Executar o script de ancoragem antes do build.**
4. **Se alterar um heading, atualizar todos os `xref:` associados.**
5. **Nunca editar âncoras `{#...}` à mão.**
6. **Assegurar `.md` sem resíduos de builds anteriores.**

---

## 🚀 Estrutura do Build e Parsing

* Tags `web-only`/`print-only` são processadas para outputs finais.
* Blocos `print-anexo:X` são extraídos para anexos.
* `xref:` são convertidos conforme o destino (web ou print).
* **Âncoras de heading são recriadas em cada build** para garantir unicidade.
* Emojis são removidos ou substituídos na versão print conforme a tabela editorial.

---

## 🖨️ Substituição de Emojis para Impressão (PDF/LaTeX)

| Emoji | Substituição (print) | Observação/editorial  |
| ----- | -------------------- | --------------------- |
| 🛠️   | (remover)            | Ferramenta            |
| 📅    | (remover)            | Calendário            |
| 👥    | Responsáveis         | Papéis, funções       |
| ⚖️    | Limiar               | Proporcionalidade     |
| 📝    | Exemplo              | Casos práticos        |
| 📌    | Nota                 | Recomendação          |
| 🔄    | (remover)            | Processo              |
| 📊    | Matriz               | Estrutura comparativa |
| 🧾    | Aceitação            | Critério formal       |
| 🚀    | Maturidade           | Avançado              |
| ❌     | Não conforme         |                       |
| 🔗    | (remover)            | Ligações              |
| 🧠    | Rationale            | Só contexto           |

---

## 🏗️ Regras editoriais para templates, user stories e parsing

* **Todos os ficheiros `addon/*.md` devem começar por um template:**
  `<!--template: sbdtoe-[tipo] -->`
* **User stories** são sempre delimitadas com:

  * `<!--userstory:start-->`
  * `<!--userstory:end-->`
  * Com header: `### Story: [Nome]`
  * Descrição e Definition of Done em checklist markdown.
* **Nunca usar outros títulos ou marcas internas dentro de blocos de user story.**
* **Qualquer novo bloco** (ex: `<!--policytable:start-->`) deve ser documentado nesta convenção.

---

# 📝 Exemplo Prático — Workflow Completo de Heading + xref

### A. Fonte original (`src/cap02/addon/02-tabela-valores.md`)

```markdown
# 📊 Valores Normalizados de Risco

A tabela abaixo fornece os valores recomendados por eixo e criticidade...

## 📊 segundo anchor

Mais detalhes sobre a segunda métrica...
```

*(Sem âncoras manualmente!)*

### B. Após processamento com `add_anchors.py` (editorial)

```markdown
# 📊 Valores Normalizados de Risco {#valores-normalizados-de-risco}
## 📊 segundo anchor {#segundo-anchor}
```

### C. Como se define o xref em edição (`intro.md`)

```markdown
[Consultar valores normalizados](xref:cap02/addon/tabela-valores#valores-normalizados-de-risco)
[Ver segunda métrica](xref:cap02/addon/tabela-valores#segundo-anchor)
```

### D. Output para Web (Docusaurus)

```markdown
[Consultar valores normalizados](/cap02/addon/tabela-valores#valores-normalizados-de-risco)
[Ver segunda métrica](/cap02/addon/tabela-valores#segundo-anchor)
```

E nos headings do destino:

```markdown
# 📊 Valores Normalizados de Risco {#valores-normalizados-de-risco}
## 📊 segundo anchor {#segundo-anchor}
```

### E. Output para Print (Pandoc/LaTeX)

```latex
\hyperref[cap02_addon_tabela-valores_valores-normalizados-de-risco]{Consultar valores normalizados}
\hyperref[cap02_addon_tabela-valores_segundo-anchor]{Ver segunda métrica}
```

No destino LaTeX:

```latex
\hypertarget{cap02_addon_tabela-valores_valores-normalizados-de-risco}{}
\section*{Valores Normalizados de Risco}

\hypertarget{cap02_addon_tabela-valores_segundo-anchor}{}
\subsection*{segundo anchor}
```

---

## Quadro Resumo

| Fase             | Heading (exemplo)                                                                                                                         | xref de exemplo                                                                                                                                       |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| **SRC**          | `# 📊 Valores Normalizados de Risco`<br>`## 📊 segundo anchor`                                                                            | `[Consultar...](xref:cap02/addon/tabela-valores#valores-normalizados-de-risco)`<br>`[Ver...](xref:cap02/addon/tabela-valores#segundo-anchor)`         |
| **add\_anchors** | `# 📊 Valores Normalizados de Risco {#valores-normalizados-de-risco}`<br>`## 📊 segundo anchor {#segundo-anchor}`                         | *(idem acima)*                                                                                                                                        |
| **WEB**          | `# 📊 Valores Normalizados de Risco {#valores-normalizados-de-risco}`<br>`## 📊 segundo anchor {#segundo-anchor}`                         | `[Consultar...](/cap02/addon/tabela-valores#valores-normalizados-de-risco)`<br>`[Ver...](/cap02/addon/tabela-valores#segundo-anchor)`                 |
| **PRINT**        | `\hypertarget{cap02_addon_tabela-valores_valores-normalizados-de-risco}{}`<br>`\hypertarget{cap02_addon_tabela-valores_segundo-anchor}{}` | `\hyperref[cap02_addon_tabela-valores_valores-normalizados-de-risco]{Consultar...}`<br>`\hyperref[cap02_addon_tabela-valores_segundo-anchor]{Ver...}` |

---

## Notas finais de edição e curadoria

* O editor **NUNCA** escreve `{#...}` à mão — o script trata de tudo.
* O nome da âncora a usar no xref é o **nome normalizado** do heading de destino.
* O `xref:` nunca aponta para caminhos relativos nem para âncoras não geradas pelo script.
* Se o heading for alterado, deve-se garantir que o `xref:` no texto também é atualizado.
* O build converte tudo automaticamente conforme o destino (web/print).

---
