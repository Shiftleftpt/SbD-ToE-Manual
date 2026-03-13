import type {Config} from '@docusaurus/types';
import {themes as prismThemes} from 'prism-react-renderer';
// Node-style require needed for sidebarPath (TypeScript + ESM)
// Sidebar path: use plain string (Docusaurus will resolve). Avoid Node require to keep TS happy without @types/node.
const sidebarPath = './sidebars-sbd-toe.ts';

const config: Config = {
  
  title: 'Security by Design',
  tagline: 'Theory of Everything',

  favicon: 'img/brand/favicon-32.png', 

  // REMOVIDO future.v4 para diagnosticar falta de hidratação Mermaid
  // future: { v4: true },

  // Deploy em GitHub Pages
  url: 'https://shiftleftpt.github.io',
  baseUrl: '/',
  organizationName: 'shiftleftpt',
  projectName: 'SbD-ToE-Manual',

  // Continua válido no topo
  onBrokenLinks: 'warn',

  // i18n (apenas PT por agora)
  i18n: {
    defaultLocale: 'pt',
    locales: ['pt'],
  },
  
  // Markdown / Mermaid (revert para suporte nativo)
  markdown: {
    mermaid: true,

  },
  
  // Tags extra no <head> (manifest + apple-touch-icon)
  headTags: [
    {
      tagName: 'link',
      attributes: { rel: 'manifest', href: '/img/brand/site.webmanifest' },
    },
    {
      tagName: 'link',
      attributes: { rel: 'apple-touch-icon', href: '/img/brand/favicon-180.png' },
    },
  ],
  
  // ⤵️ injeta apenas script de analítica (removido fallback mermaid)
  scripts: [
    {
      src: 'https://plausible.io/js/pa-vrvyYynlF73FkPELUrY4w.js',
      async: true,
    },
  ],

  // Temas
  themes: ['@docusaurus/theme-mermaid'],

  // Presets (usar classic preset como no projeto limpo)
  presets: [
    [
      'classic',
      {
        docs: {
          path: 'docs/sbd-toe',
          routeBasePath: 'sbd-toe',
          sidebarPath,
          numberPrefixParser: true,
          showLastUpdateTime: false,
          showLastUpdateAuthor: false,
          admonitions: {
            keywords: ['userstory'],
            extendDefaults: true,
          },
        },
        pages: {
          path: 'src/pages',
        },
        theme: {
          customCss: './src/css/custom.css',
        },
      },
    ],
  ],

  themeConfig: {
    image: 'img/docusaurus-social-card.jpg',

    // ⇣⇣ BRAND ⇣⇣
    navbar: {
      title: 'SbD–ToE',
      hideOnScroll: false,
      logo: {
        alt: 'Security by Design - Theory of Everything',
        src: 'img/brand/Shiftleft_LogoHorizontal_V5.png',   
        srcDark: 'img/brand/Shiftleft_LogoHorizontal_V5.png' 
      },
      items: [
        // === ESQUERDA ===
        {
          type: 'docSidebar',
          sidebarId: 'manualAtual',
          position: 'left',
          label: 'Manual',
        },
        {
          type: 'docSidebar',
          sidebarId: 'toeCrossCheck',
          position: 'left',
          label: 'Cross-check',
        },
        
        // === DIREITA ===
        {
          type: 'docSidebar',
          sidebarId: 'toeOverview',
          position: 'right',
          label: 'ToE',
        },
        {
          to: '/about',
          label: 'Sobre',
          position: 'right',
        },
        {
          to: '/faq',
          label: 'FAQ',
          position: 'right',
        },
        { 
          to: '/licenciamento', 
          label: 'Licença', 
          position: 'right' 
        },
        {
          href: 'https://github.com/Shiftleftpt/SbD-ToE-Manual',
          label: 'GitHub',
          position: 'right',
        },
      ],
    },

    // Footer
    footer: {
      style: 'dark',
      links: [
        {
          title: 'Manuais',
          items: [
            { label: 'SbD-ToE', to: '/sbd-toe/sbd-manual/' },
          ],
        },
        {
          title: 'Mais',
          items: [
            { label: 'GitHub', href: 'https://github.com/Shiftleftpt/SbD-ToE-Manual' },
          ],
        },
      ],
      copyright: `© ${new Date().getFullYear()} Shiftleft - Secure Software Engineering, Lda. Construído com Docusaurus.`,
    },

    // UX/tema
    colorMode: {
      respectPrefersColorScheme: true,
      defaultMode: 'dark', // mantive como tinhas; posso trocar para 'light' se preferires
    },
    docs: {
      sidebar: {
        autoCollapseCategories: true,
        hideable: true,
      },
    },

    // Prism
    prism: {
      theme: prismThemes.github,
      darkTheme: prismThemes.dracula,
      additionalLanguages: ['bash', 'powershell', 'java', 'json', 'yaml', 'docker', 'diff'],
    },

    // Mermaid tema
    mermaid: {
      theme: { light: 'default', dark: 'dark' },
    },

    // SEO simples
    metadata: [
      { name: 'keywords', content: 'Security by Design, SbD, DevSecOps, SAMM, SSDF, SLSA, DSOMM' },
      { name: 'og:type', content: 'website' },
    ],
  },
};

          // Algolia DocSearch
          // Para credenciais reais, inserir appId, apiKey e indexName abaixo.
          // Ask AI: Quando disponível, Algolia irá ativar automaticamente (ver documentação Algolia).
          // Para campos ou configurações específicas de Ask AI, consulte https://docsearch.algolia.com/ask-ai/
          algolia: {
            appId: process.env.ALGOLIA_APP_ID || 'REPLACE_WITH_ALGOLIA_APP_ID',
            apiKey: process.env.ALGOLIA_SEARCH_API_KEY || 'REPLACE_WITH_ALGOLIA_SEARCH_API_KEY',
            indexName: process.env.ALGOLIA_INDEX_NAME || 'REPLACE_WITH_ALGOLIA_INDEX_NAME',
            contextualSearch: true,
            searchPagePath: 'search',
            // askAI: true // Descomente quando Algolia Ask AI estiver disponível
          },
export default config;
