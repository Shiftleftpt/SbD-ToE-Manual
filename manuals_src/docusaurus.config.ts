import type {Config} from '@docusaurus/types';
import {themes as prismThemes} from 'prism-react-renderer';

const config: Config = {
  
  title: 'Security by Design',
  tagline: 'Theory of Everything',

  favicon: 'img/brand/favicon-32.png', 

  // Ativa comportamento compatível com v4 (quebra a posição do onBrokenMarkdownLinks)
  future: { v4: true },

  // Deploy em GitHub Pages
  url: 'https://shiftleftpt.github.io',
  baseUrl: '/SbD-ToE-Manual/',
  organizationName: 'shiftleftpt',
  projectName: 'SbD-ToE-Manual',

  // Continua válido no topo
  onBrokenLinks: 'warn',

  // i18n (apenas PT por agora)
  i18n: {
    defaultLocale: 'pt',
    locales: ['pt'],
  },
  
  // Markdown / Mermaid
  markdown: {
    mermaid: true,
    // Quando future.v4=true, o onBrokenMarkdownLinks move-se para hooks
    hooks: {
      onBrokenMarkdownLinks: 'warn',
    },
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

  // Temas (usar theme-classic aqui é OK) + Mermaid
  themes: [
    '@docusaurus/theme-mermaid',
    [
      '@docusaurus/theme-classic',
      {
        customCss: './src/css/custom.css',
      },
    ],
  ],

  // Plugins
  plugins: [
    [
      '@docusaurus/plugin-content-docs',
      {
        id: 'sbd-toe',
        path: 'docs/sbd-toe',
        routeBasePath: 'sbd-toe',
        sidebarPath: require.resolve('./sidebars-sbd-toe.ts'),
        numberPrefixParser: true,
        showLastUpdateTime: false,
        showLastUpdateAuthor: false,
        admonitions: {
          keywords: ['userstory'],
          extendDefaults: true, // mantém note|tip|info|warning|danger
        },
      },
    ],
    [
      '@docusaurus/plugin-content-pages',
      { path: 'src/pages' },
    ],
  ],

  themeConfig: {
    image: 'img/docusaurus-social-card.jpg',

    // ⇣⇣ BRAND ⇣⇣
    navbar: {
      title: 'SbD–ToE',
      hideOnScroll: false,
      logo: {
        alt: 'Security by Design – Theory of Everything',
        src: 'img/brand/Shiftleft_LogoHorizontal_V5.png',   
        srcDark: 'img/brand/Shiftleft_LogoHorizontal_V5.png' 
      },
      items: [
        {
          type: 'docSidebar',
          docsPluginId: 'sbd-toe',
          sidebarId: 'manualAtual',
          docId: 'index', 
          position: 'left',
          label: 'Manual',
        },
        {
          type: 'docSidebar',
          docsPluginId: 'sbd-toe',
          sidebarId: 'toeOverview',
          docId: '000-teory-of-everything/intro',
          position: 'left',
          label: 'ToE',
        },
        {
          type: 'docSidebar',
          docsPluginId: 'sbd-toe',
          sidebarId: 'toeHowTo',
          docId: '001-how-to-manual/intro',
          position: 'left',
          label: 'Como usar',
        },
        {
          type: 'docSidebar',
          docsPluginId: 'sbd-toe',
          sidebarId: 'toeCrossCheck',
          docId: '002-cross-check-normativo/intro',
          position: 'left',
          label: 'Cross-check',
        },

        /* {
          type: 'docSidebar',
          docsPluginId: 'sbd-toe',
          sidebarId: 'toePolicies',
          docId: '003-policies-globals/intro',
          position: 'left',
          label: 'Políticas',
        }, */

        { to: '/licenciamento', label: 'Licença', position: 'right' },
        { to: '/about', label: 'Sobre', position: 'right' },
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
            { label: 'SbD-ToE', to: '/sbd-toe/' },
          ],
        },
        {
          title: 'Mais',
          items: [
            { label: 'GitHub', href: 'https://github.com/Shiftleftpt/sbd-theory-of-everything' },
          ],
        },
      ],
      copyright: `© ${new Date().getFullYear()} Shiftleft – Secure Software Engineering, Lda. Construído com Docusaurus.`,
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

export default config;
