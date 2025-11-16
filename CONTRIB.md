# Guia de Contribuição - Manual SbD-ToE

Este guia define as regras a colaboração Git adotado no repositório. 
Para além destas regras, a criação de conteudo deverá seguir a linha editorial definida em `guia-editorial.md`.

---

## 🔄 Utilização do Git e fluxo de contribuição {#git-fluxo-contribuicao}

O repositório utiliza o modelo **Trunk-Based Development**, tendo `master` como ramo principal.

### Estrutura de branches

| Tipo de branch         | Padrão                          | Objetivo                                                         |
| ---------------------- | ------------------------------- | ---------------------------------------------------------------- |
| **Principal**          | `master`                        | Fonte de verdade; contém sempre o conteúdo validado e publicável |
| **Feature**            | `feat/<tema>`                   | Novo conteúdo ou melhoria de capítulo                            |
| **Fix**                | `fix/<tema>`                    | Correções pontuais                                               |
| **Chore / Docs**       | `chore/<tema>` ou `docs/<tema>` | Tarefas de build, scripts ou documentação auxiliar               |
| **Release (opcional)** | `release/vX.Y.Z`                | Congelar conjunto para publicação (tag)                          |
| **Hotfix (opcional)**  | `hotfix/<tema>`                 | Correção imediata pós-release                                    |

### Fluxo de contribuição

1. Criar uma branch a partir de `master`:

   ```bash
   git switch -c feat/cap14-kpis
   ```
2. Editar e validar localmente (ver secção “Validação local obrigatória”):

   ```bash
   npm run build     # valida site web
   ```
3. Utilizar mensagens de *commit* curtas e claras:

   ```
   feat(cap14): adicionar KPIs de governação
   fix(cap05): corrigir referência cruzada no 50-ameacas
   chore(build): estabilizar anchors para LaTeX
   ```
4. Subir a branch e abrir um *Pull Request* para `master`.
5. Realizar o *merge* através de **Squash and Merge**, após a passagem dos *checks*.

#### Validação local obrigatória (Makefile `src/publish`)

Antes de submeter um *Pull Request*, é obrigatório efetuar o *build* localmente através do Makefile dedicado.
Este processo cria um diretório limpo e isolado (`_out/web`) e evita a contaminação do repositório principal.

> Requisitos: Node **>= 20** e npm.
> O Makefile executa `npm install` no diretório de *build*.

Comandos principais (a partir da raiz do repositório):

```bash
make -C src/publish web     # pipeline completo: copia fontes → instala deps → build Docusaurus
make -C src/publish serve   # servir localmente após o build
make -C src/publish clean   # limpeza do diretório de build
make -C src/publish dev     # desenvolvimento interativo (Docusaurus dev)
```

O alvo `web` executa internamente:

* `prepare` → copia `manuals_src/` para `_out/web/`
* `install` → corre `npm install` em `_out/web/`
* `build` → executa `npm run build` (Docusaurus)

> Em caso de erros de *registry* do npm, pode ser necessário executar previamente:
>
> ```bash
> npm config set registry https://registry.npmjs.org/
> ```

---

### Publicação e versões

* Cada conjunto coerente publicado é marcado com **tag** `vX.Y.Z` em `master`.
* A criação da tag aciona o *pipeline* de publicação Web (Docusaurus → `gh-pages`).
* Hotfixes pós-release utilizam `fix/<tema>` e geram uma nova tag (`vX.Y.Z+1` ou `vX.Y.Z-hotfix1`).

---

### Proteção de branches (GitHub)

**`master`** (ramo principal)

* ✅ Pull Request obrigatório
* ✅ *Status checks* obrigatórios (`build-web`, `lint-links`, `anchors-validate`)
* ✅ Branch deve estar atualizada antes do *merge*
* ✅ Histórico linear
* ✅ Commits assinados
* ✅ Branch protegida contra eliminação
* ✅ Apenas *Squash Merge* permitido

**Aprovações - política escalável com a equipa**

* Enquanto existir apenas um mantenedor: **0 approvals** (checks obrigatórios mantêm-se).
* Quando existirem dois ou mais contribuidores ativos:

  * mínimo de **1 aprovação** de pessoa diferente do autor;
  * ativar **Require review from Code Owners** (com `CODEOWNERS`);
  * ativar **Require approval from someone other than the last pusher**;
  * ativar **Dismiss stale approvals** e **Require conversation resolution**;
  * (opcional) ativar **Merge queue**.

**`gh-pages`**

* *Push* permitido apenas via GitHub Actions (deploy automático).
* Branch protegida contra eliminação.

---


Estes *checks* devem ser configurados como **Required status checks** na regra de proteção da branch `master`.
*(Opcional: adicionar `spell-pt` quando disponível.)*

---

### Fluxo local típico

```bash
git switch -c feat/cap14-kpis
# editar ficheiros…
npm run build
make -C src/publish web
make -C src/publish serve
git add -A
git commit -m "feat(cap14): adicionar KPIs de governação"
git push -u origin feat/cap14-kpis
# abrir PR → checks verdes → squash merge em master → tag vX.Y.Z
```

---

## 🧾 Integração com Issues do projeto {#integracao-issues}

As contribuições devem ser sempre rastreáveis através de *issues* no repositório principal do manual.
Este mecanismo assegura visibilidade, histórico editorial e integração direta com o fluxo Git.

### Boas práticas de utilização de *issues*

1. **Procurar antes de criar**
   Antes de iniciar uma nova contribuição, verificar se já existe um *issue* aberto para o tema.
   Caso exista, comentar no *issue* e, se aplicável, assumir a execução.

2. **Criar novo *issue***
   Quando não existir *issue* aberto, criar um novo utilizando o *template* apropriado (`enhancement`, `bug`, `documentation`, etc.).
   O título deve ser objetivo e indicar o contexto do capítulo.

   > Exemplo: `cap05: atualizar tabela de dependências no 50-ameacas-mitigadas`

3. **Relação entre *issue* e branch**
   Cada *branch* deve corresponder a **um único *issue***.
   Recomenda-se incluir o número do *issue* no nome da *branch* e na mensagem de *commit*:

   ```bash
   git switch -c feat/123-cap05-tabela-dependencias
   ```

   **Mensagem de commit:**

   ```
   feat(cap05): atualizar tabela de dependências (#123)
   ```

   Esta convenção permite o *linking automático* entre commits, *Pull Requests* e *issues* no GitHub.

4. **Fecho automático de *issues***
   O *Pull Request* que resolve o *issue* deve incluir uma referência direta no corpo da descrição:

   ```
   Closes #123
   ```

   O GitHub encerrará automaticamente o *issue* após o *merge* em `master`.

5. **Etiquetas e triagem**
   Utilizar *labels* para classificação dos *issues* (ex.: `capítulo:14`, `tipo:documentação`, `prioridade:alta`, `status:em progresso`).
   O responsável editorial realiza a triagem inicial e atribui as *labels* padrão.

6. **Workflow resumido**

   | Etapa | Ação                                  | Resultado                 |
   | ----- | ------------------------------------- | ------------------------- |
   | 1     | Criar ou identificar *issue*          | Contexto documentado      |
   | 2     | Criar branch `feat/<num>-<descrição>` | Ligação direta ao *issue* |
   | 3     | Trabalhar e *commit* com `(#num)`     | Histórico rastreável      |
   | 4     | Abrir *PR* com `Closes #num`          | Fecho automático          |
   | 5     | Merge → Tag → Deploy                  | Publicação controlada     |

---

Para esclarecimentos ou pedidos de estrutura, contactar o responsável editorial do projeto.
