import type {Config} from '@docusaurus/types';
import {themes as prismThemes} from 'prism-react-renderer';

const sidebarPath = './sidebars-sbd-toe.ts';

const config: Config = {
  title: 'Security by Design',
  tagline: 'Theory of Everything',
  favicon: 'img/brand/favicon-32.png',

  url: 'https://www.securitybydesign.dev',
  baseUrl: '/',
  organizationName: 'shiftleftpt',
  projectName: 'SbD-ToE-Manual',

  onBrokenLinks: 'warn',

  i18n: {
    defaultLocale: 'pt',
    locales: ['pt'],
  },

  markdown: {
    mermaid: true,
  },

  headTags: [
    {
      tagName: 'link',
      attributes: {rel: 'manifest', href: '/img/brand/site.webmanifest'},
    },
    {
      tagName: 'link',
      attributes: {rel: 'apple-touch-icon', href: '/img/brand/favicon-180.png'},
    },
    {
      tagName: 'meta',
      attributes: {
        name: 'algolia-site-verification',
        content: 'DC1E056DBDDFA537',
      },
    },
  ],

  scripts: [
    {
      src: 'https://plausible.io/js/pa-vrvyYynlF73FkPELUrY4w.js',
      async: true,
    },
  ],

  themes: ['@docusaurus/theme-mermaid'],

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
        blog: false,
        theme: {
          customCss: './src/css/custom.css',
        },
        sitemap: {
          changefreq: 'weekly',
          priority: 0.5,
          filename: 'sitemap.xml',
          ignorePatterns: ['/search', '/tags/**'],
        },
      },
    ],
  ],

  themeConfig: {
    image: 'img/docusaurus-social-card.jpg',

    navbar: {
      title: 'SbD–ToE',
      hideOnScroll: false,
      logo: {
        alt: 'Security by Design - Theory of Everything',
        src: 'img/brand/Shiftleft_LogoHorizontal_V5.png',
        srcDark: 'img/brand/Shiftleft_LogoHorizontal_V5.png',
      },
      items: [
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
          position: 'right',
        },
        {
          href: 'https://github.com/Shiftleftpt/SbD-ToE-Manual',
          label: 'GitHub',
          position: 'right',
        },
      ],
    },

    footer: {
      style: 'dark',
      links: [
        {
          title: 'Manuais',
          items: [{label: 'SbD-ToE', to: '/sbd-toe/sbd-manual/'}],
        },
        {
          title: 'Mais',
          items: [
            {label: 'GitHub', href: 'https://github.com/Shiftleftpt/SbD-ToE-Manual'},
          ],
        },
      ],
      copyright: `© ${new Date().getFullYear()} Shiftleft - Secure Software Engineering, Lda. Construído com Docusaurus.`,
    },

    colorMode: {
      respectPrefersColorScheme: true,
      defaultMode: 'dark',
    },

    docs: {
      sidebar: {
        autoCollapseCategories: true,
        hideable: true,
      },
    },

    prism: {
      theme: prismThemes.github,
      darkTheme: prismThemes.dracula,
      additionalLanguages: [
        'bash',
        'powershell',
        'java',
        'json',
        'yaml',
        'docker',
        'diff',
      ],
    },

    mermaid: {
      theme: {light: 'default', dark: 'dark'},
    },

    metadata: [
      {
        name: 'keywords',
        content: 'Security by Design, SbD, DevSecOps, SAMM, SSDF, SLSA, DSOMM',
      },
      {name: 'og:type', content: 'website'},
    ],
  },
};

export default config;