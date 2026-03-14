# DocSearch e Ask AI

## O que foi preparado

- A configuração principal do Docusaurus foi limpa e normalizada em [`manuals_src/docusaurus.config.ts`](/Volumes/G-DRIVE/Shared/Manual-SbD-ToE/SbD-ToE-Manual/manuals_src/docusaurus.config.ts).
- O site usa agora o adapter oficial `@docsearch/docusaurus-adapter`, com configuração em `themeConfig.docsearch`.
- O bloco `themeConfig.docsearch` ficou pronto para `appId`, `apiKey`, `indexName`, `contextualSearch`, `searchPagePath` e `askAi`.
- A navbar ficou preparada para mostrar o item de pesquisa quando as 3 variáveis Algolia estiverem definidas.
- Foi criado um ficheiro de exemplo de ambiente em [`manuals_src/.env.example`](/Volumes/G-DRIVE/Shared/Manual-SbD-ToE/SbD-ToE-Manual/manuals_src/.env.example).
- Foram feitos pequenos ajustes estruturais em páginas com maior impacto na indexação (`tldr`, índice do manual e títulos genéricos em páginas `aplicacao-lifecycle`).

## Onde inserir as credenciais

Definir estas variáveis em `manuals_src/.env` ou no ambiente do deploy:

```dotenv
ALGOLIA_APP_ID=REPLACE_WITH_ALGOLIA_APP_ID
ALGOLIA_SEARCH_API_KEY=REPLACE_WITH_ALGOLIA_SEARCH_API_KEY
ALGOLIA_INDEX_NAME=REPLACE_WITH_ALGOLIA_INDEX_NAME
ALGOLIA_ASK_AI_ASSISTANT_ID=REPLACE_WITH_ALGOLIA_ASK_AI_ASSISTANT_ID
```

Notas:

- Usar a **search-only API key** do DocSearch, não uma chave admin.
- Enquanto os placeholders não forem substituídos, o site continua a buildar e a pesquisa não é mostrada na navbar.
- `ALGOLIA_ASK_AI_ASSISTANT_ID` é opcional; só é necessário quando o assistente Ask AI / Agent Studio já existir no Algolia.

## Como ativar DocSearch

1. Garantir que o crawler DocSearch está configurado para o domínio público do site.
2. Inserir `ALGOLIA_APP_ID`, `ALGOLIA_SEARCH_API_KEY` e `ALGOLIA_INDEX_NAME`.
3. Fazer novo build/deploy.
4. Confirmar que a caixa de pesquisa aparece na navbar.

## Como verificar que a pesquisa está a funcionar

Local:

```bash
cd manuals_src
npm run build
npm run serve
```

Validar:

- a navbar mostra pesquisa;
- a página `/search` responde;
- pesquisas por termos fortes como `threat modeling`, `SBOM`, `deploy seguro` e `governança` devolvem capítulos corretos;
- os resultados mostram títulos específicos, não entradas ambíguas como `Como Fazer`.

Produção:

- confirmar que o crawler indexou URLs sob `https://www.securitybydesign.dev/`;
- abrir a pesquisa e validar resultados para capítulos e páginas `aplicacao-lifecycle`;
- verificar que links do TL;DR apontam para rotas reais.

## Como confirmar se Ask AI está disponível

- Criar ou ativar um assistente Ask AI ou Agent Studio no painel Algolia para o mesmo índice DocSearch.
- Copiar o `Agent ID` / `assistantId` desse assistente para `ALGOLIA_ASK_AI_ASSISTANT_ID`.
- Fazer novo build/deploy para que o DocSearch UI passe a expor o Ask AI sidepanel.
- No painel Algolia, confirmar que o assistente está autorizado para `https://www.securitybydesign.dev/` e para os hosts locais usados em teste, por exemplo `http://localhost:3000/`.
- A configuração atual do site assume o fluxo Agent Studio e liga `agentStudio: true` com `sidePanel: true`.

## Aspetos documentais importantes para boa indexação

- Títulos específicos por página melhoram o ranking e a legibilidade dos resultados.
- Hierarquia coerente de headings (`H1` único implícito pelo frontmatter + `H2/H3` sem saltos) ajuda o crawler a extrair secções com granularidade útil.
- Páginas muito longas continuam indexáveis, mas tendem a gerar snippets menos precisos; isso é particularmente visível nas páginas `aplicacao-lifecycle`.
- Rotas duplicadas com conteúdo muito semelhante podem reduzir relevância e devem ser evitadas no crawler.

## Limitações e próximos passos

- O build atual termina com sucesso, mas ainda reporta vários `broken links` e `broken anchors` fora do escopo desta ronda, sobretudo em `about`, `faq`, cross-checks normativos e algumas páginas `aplicacao-lifecycle`; isso deve ser reduzido antes de uma indexação final mais rigorosa.
- Existe uma duplicação do conteúdo `TL;DR` entre `docs/sbd-toe/tldr.md` e `src/pages/tldr.md`; nesta ronda o conteúdo foi alinhado, mas continua a ser aconselhável escolher uma rota canónica no crawler.
- Há várias páginas longas no manual; se a qualidade dos snippets for insuficiente, o próximo passo natural é partir algumas secções mais extensas em subpáginas, sem reescrever o conteúdo.
- A qualidade final do Ask AI depende do índice Algolia, da cobertura do crawler e da estabilidade semântica dos títulos/heading do manual.
- Se o Ask AI responder com contexto demasiado amplo, o próximo ajuste natural é rever a configuração do assistente no Algolia e os atributos/facets do índice antes de mexer na estrutura editorial.
- Se optares mais tarde por um assistente Ask AI “clássico” em vez de Agent Studio, a configuração do site deve ser revista para remover `agentStudio: true`.
