# DocSearch + Ask AI Setup

Este documento explica como preparar e ativar a pesquisa Algolia DocSearch e Ask AI no manual SbD-ToE.

## O que foi preparado
- Configuração base Algolia DocSearch adicionada ao ficheiro `docusaurus.config.ts`.
- Placeholders para credenciais Algolia (`appId`, `apiKey`, `indexName`).
- Comentários para futura ativação do Ask AI.
- Uso de variáveis de ambiente para credenciais, com fallback seguro.

## Como inserir credenciais Algolia
- Edite o ficheiro `manuals_src/docusaurus.config.ts`.
- No bloco `themeConfig.algolia`, substitua os valores:
  - `appId`: `REPLACE_WITH_ALGOLIA_APP_ID`
  - `apiKey`: `REPLACE_WITH_ALGOLIA_SEARCH_API_KEY`
  - `indexName`: `REPLACE_WITH_ALGOLIA_INDEX_NAME`
- Alternativamente, defina as variáveis de ambiente `ALGOLIA_APP_ID`, `ALGOLIA_SEARCH_API_KEY`, `ALGOLIA_INDEX_NAME`.

## Como ativar DocSearch
- Após inserir as credenciais, execute:
  - `npm install` (se necessário)
  - `npm run start` para testar localmente
  - `npm run build` para produção
- A barra de pesquisa aparecerá automaticamente na navbar.

## Como verificar funcionamento
- A pesquisa deve aparecer no topo do site.
- Teste consultas e verifique resultados.
- Para Ask AI, consulte https://docsearch.algolia.com/ask-ai/.

## Estrutura documental para boa indexação
- Use headings claros e hierarquia consistente.
- Evite páginas demasiado longas ou secções sem heading.
- Garanta navegação lateral bem estruturada.

## Limitações e próximos passos
- Credenciais reais não estão incluídas.
- Ask AI depende de ativação Algolia.
- Recomenda-se rever headings e títulos para melhor indexação.

## Checklist rápido
- [ ] Inserir credenciais Algolia
- [ ] Testar pesquisa localmente
- [ ] Confirmar Ask AI quando disponível
- [ ] Rever estrutura dos docs
- [ ] Validar resultados em produção

---

Para dúvidas ou problemas, consulte a documentação oficial do Algolia DocSearch.
