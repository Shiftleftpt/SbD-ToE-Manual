import {themes as prismThemes} from 'prism-react-renderer';
import type {Config} from '@docusaurus/types';

const config: Config = {
  title: 'Security by Design – Theory of Everything',
  tagline: 'Framework prática e aberta para desenvolver software seguro',
  favicon: 'img/favicon.ico',

  future: {
    v4: true,
  },

  url: 'https://shiftleftpt.github.io',
  baseUrl: '/sbd-theory-of-everything/',

  organizationName: 'shiftleftpt',
  projectName: 'sbd-theory-of-everything',

  onBrokenLinks: 'warn',
  onBrokenMarkdownLinks: 'warn',

  i18n: {
    defaultLocale: 'pt',
    locales: ['pt'],
  },

  plugins: [
  [
    '@docusaurus/plugin-content-docs',
    {
      id: 'sbd-toe',
      path: 'docs/sbd-toe',
      routeBasePath: 'sbd-toe',
      sidebarPath: require.resolve('./sidebars-sbd-toe.ts'),
    },
  ],
  [
    '@docusaurus/plugin-content-docs',
    {
      id: 'ia',
      path: 'docs/ia',
      routeBasePath: 'ia',
      sidebarPath: undefined,
    },
  ],
  [
    '@docusaurus/plugin-content-docs',
    {
      id: 'supply-chain',
      path: 'docs/supply-chain',
      routeBasePath: 'supply-chain',
      sidebarPath: undefined,
    },
  ],
  [
    '@docusaurus/plugin-content-docs',
    {
      id: 'ameacas',
      path: 'docs/ameacas',
      routeBasePath: 'ameacas',
      sidebarPath: undefined,
    },
  ],
  [
    '@docusaurus/plugin-content-pages',
    {
      path: 'src/pages',
    },
  ],
],
  themes: [
    [
      '@docusaurus/theme-classic',
      {
        customCss: './src/css/custom.css',
      },
    ],
  ],

  themeConfig: {
    image: 'img/docusaurus-social-card.jpg',
    mermaid: {
      theme: { light: 'default', dark: 'dark' } // ✅ Tema para Mermaid
    },
    // Configuração do navbar
    navbar: {
      title: 'Security by Design – Theory of Everything',
      logo: {
        alt: 'Security by Design – Theory of Everything',
        src: 'img/logo.svg',
      },
      items: [
        {
          type: 'docSidebar',
          sidebarId: 'sbdToeSidebar',
          docsPluginId: 'sbd-toe',
          docId: 'intro',
          position: 'left',
          label: 'SbD-ToE',
        },
        {
          type: 'docSidebar',
          sidebarId: 'defaultSidebar',
          docsPluginId: 'ia',
          docId: 'intro',
          position: 'left',
          label: 'IA',
        },
        {
          type: 'docSidebar',
          sidebarId: 'defaultSidebar',
          docsPluginId: 'supply-chain',
          docId: 'intro',
          position: 'left',
          label: 'Supply Chain',
        },
        {
          type: 'docSidebar',
          sidebarId: 'defaultSidebar',
          docsPluginId: 'ameacas',
          docId: 'intro',
          position: 'left',
          label: 'Ameaças',
        },
        {
          to: '/licenciamento',
          label: 'Licença',
          position: 'right'
        },
        {
          to: '/about', //  página estática em src/pages/about.md
          label: 'Sobre',
          position: 'right'
        },
        {
          href: 'https://github.com/Shiftleftpt/sbd-theory-of-everything',
          label: 'GitHub',
          position: 'right',
        },
      ]
    },
    // Configuração do rodapé
    footer: {
      style: 'dark',
      links: [
        {
          title: 'Manuais',
          items: [
            {label: 'SbD-ToE', to: '/sbd-toe/intro'},
            {label: 'IA', to: '/ia/intro'},
            {label: 'Supply Chain', to: '/supply-chain/intro'},
            {label: 'Ameaças', to: '/ameacas/intro'},
          ],
        },
        {
          title: 'Mais',
          items: [
            {label: 'GitHub', href: 'https://github.com/facebook/docusaurus'},
          ],
        },
      ],
      copyright: `Copyright © ${new Date().getFullYear()} Shiftleft - Secure Software Engineering, Lda. Built with Docusaurus.`,
    },

    prism: {
      theme: prismThemes.github,
      darkTheme: prismThemes.dracula,
    },
  },
};

export default config;
