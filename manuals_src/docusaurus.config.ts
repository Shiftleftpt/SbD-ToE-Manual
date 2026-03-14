import type {Config} from '@docusaurus/types';
import {existsSync, readFileSync} from 'node:fs';
import {themes as prismThemes} from 'prism-react-renderer';

const sidebarPath = './sidebars-sbd-toe.ts';

function loadEnvFile() {
  const envPath = new URL('./.env', import.meta.url);

  if (!existsSync(envPath)) {
    return;
  }

  for (const line of readFileSync(envPath, 'utf8').split(/\r?\n/)) {
    const trimmed = line.trim();

    if (!trimmed || trimmed.startsWith('#')) {
      continue;
    }

    const separatorIndex = trimmed.indexOf('=');

    if (separatorIndex <= 0) {
      continue;
    }

    const key = trimmed.slice(0, separatorIndex).trim();

    if (!key || process.env[key] !== undefined) {
      continue;
    }

    let value = trimmed.slice(separatorIndex + 1).trim();

    if (
      (value.startsWith('"') && value.endsWith('"')) ||
      (value.startsWith("'") && value.endsWith("'"))
    ) {
      value = value.slice(1, -1);
    }

    process.env[key] = value;
  }
}

loadEnvFile();

const algoliaAppId =
  process.env.ALGOLIA_APP_ID ?? 'REPLACE_WITH_ALGOLIA_APP_ID';
const algoliaSearchApiKey =
  process.env.ALGOLIA_SEARCH_API_KEY ??
  'REPLACE_WITH_ALGOLIA_SEARCH_API_KEY';
const algoliaIndexName =
  process.env.ALGOLIA_INDEX_NAME ?? 'REPLACE_WITH_ALGOLIA_INDEX_NAME';
const algoliaAskAiAssistantId = process.env.ALGOLIA_ASK_AI_ASSISTANT_ID;
const algoliaAskAiConfig = algoliaAskAiAssistantId
  ? {
      assistantId: algoliaAskAiAssistantId,
      agentStudio: true,
      sidePanel: true,
      suggestedQuestions: true,
    }
  : undefined;

const hasAlgoliaCredentials = [
  algoliaAppId,
  algoliaSearchApiKey,
  algoliaIndexName,
].every(value => !value.startsWith('REPLACE_WITH_'));

const config: Config = {
  title: 'Security by Design',
  tagline: 'Theory of Everything',
  favicon: 'img/brand/favicon-32.png',

  // Keep this aligned with the public production hostname indexed by Algolia.
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

  themes: ['@docusaurus/theme-mermaid', '@docsearch/docusaurus-adapter'],

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
          ignorePatterns: [
            '/search',
            '/tags',
            '/tags/**',
            '/sbd-toe/tags',
            '/sbd-toe/tags/**',
          ],
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
        ...(hasAlgoliaCredentials
          ? [
              {
                type: 'search' as const,
                position: 'right' as const,
              },
            ]
          : []),
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

    // DocSearch is provided by the official Algolia adapter. The current Ask AI
    // setup expects an Agent Studio assistant ID and enables the sidepanel UI.
    docsearch: {
      appId: algoliaAppId,
      apiKey: algoliaSearchApiKey,
      indexName: algoliaIndexName,
      askAi: algoliaAskAiConfig,
      contextualSearch: false,
      searchPagePath: 'search',
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
