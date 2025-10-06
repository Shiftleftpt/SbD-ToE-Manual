import React from 'react';
import ComponentCreator from '@docusaurus/ComponentCreator';

export default [
  {
    path: '/sbd-theory-of-everything/about',
    component: ComponentCreator('/sbd-theory-of-everything/about', '7cf'),
    exact: true
  },
  {
    path: '/sbd-theory-of-everything/licenciamento',
    component: ComponentCreator('/sbd-theory-of-everything/licenciamento', '0d1'),
    exact: true
  },
  {
    path: '/sbd-theory-of-everything/ameacas',
    component: ComponentCreator('/sbd-theory-of-everything/ameacas', '4dd'),
    routes: [
      {
        path: '/sbd-theory-of-everything/ameacas',
        component: ComponentCreator('/sbd-theory-of-everything/ameacas', 'b6d'),
        routes: [
          {
            path: '/sbd-theory-of-everything/ameacas',
            component: ComponentCreator('/sbd-theory-of-everything/ameacas', '72c'),
            routes: [
              {
                path: '/sbd-theory-of-everything/ameacas/🔰-introdução-e-propósito',
                component: ComponentCreator('/sbd-theory-of-everything/ameacas/🔰-introdução-e-propósito', 'f47'),
                exact: true,
                sidebar: "defaultSidebar"
              },
              {
                path: '/sbd-theory-of-everything/ameacas/🧩-anexo-a-–-dependency-confusion',
                component: ComponentCreator('/sbd-theory-of-everything/ameacas/🧩-anexo-a-–-dependency-confusion', '931'),
                exact: true,
                sidebar: "defaultSidebar"
              },
              {
                path: '/sbd-theory-of-everything/ameacas/🧩-anexo-b-–-ci-cd-poisoning',
                component: ComponentCreator('/sbd-theory-of-everything/ameacas/🧩-anexo-b-–-ci-cd-poisoning', 'fc9'),
                exact: true,
                sidebar: "defaultSidebar"
              },
              {
                path: '/sbd-theory-of-everything/ameacas/🧩-anexo-c-–-comprometimento-de-dependências',
                component: ComponentCreator('/sbd-theory-of-everything/ameacas/🧩-anexo-c-–-comprometimento-de-dependências', '729'),
                exact: true,
                sidebar: "defaultSidebar"
              },
              {
                path: '/sbd-theory-of-everything/ameacas/🧩-anexo-d-–-roubo-de-credenciais---segredos',
                component: ComponentCreator('/sbd-theory-of-everything/ameacas/🧩-anexo-d-–-roubo-de-credenciais---segredos', 'c82'),
                exact: true,
                sidebar: "defaultSidebar"
              },
              {
                path: '/sbd-theory-of-everything/ameacas/🧩-anexo-f-–-maintainers-maliciosos---insiders',
                component: ComponentCreator('/sbd-theory-of-everything/ameacas/🧩-anexo-f-–-maintainers-maliciosos---insiders', '22d'),
                exact: true,
                sidebar: "defaultSidebar"
              },
              {
                path: '/sbd-theory-of-everything/ameacas/🧩-anexo-g-–-má-configuração---permissões-excessivas',
                component: ComponentCreator('/sbd-theory-of-everything/ameacas/🧩-anexo-g-–-má-configuração---permissões-excessivas', '061'),
                exact: true,
                sidebar: "defaultSidebar"
              },
              {
                path: '/sbd-theory-of-everything/ameacas/🧩-anexo-h-–-execução-não-autorizada-de-código-(prs,-forks,-triggers)',
                component: ComponentCreator('/sbd-theory-of-everything/ameacas/🧩-anexo-h-–-execução-não-autorizada-de-código-(prs,-forks,-triggers)', '224'),
                exact: true,
                sidebar: "defaultSidebar"
              },
              {
                path: '/sbd-theory-of-everything/ameacas/🧩-anexo-i-–-dependências-sombra-e-transitivas-maliciosas',
                component: ComponentCreator('/sbd-theory-of-everything/ameacas/🧩-anexo-i-–-dependências-sombra-e-transitivas-maliciosas', 'e9d'),
                exact: true,
                sidebar: "defaultSidebar"
              },
              {
                path: '/sbd-theory-of-everything/ameacas/🧩-anexo-j-–-ataques-por-engenharia-social---prs-maliciosos-disfarçados',
                component: ComponentCreator('/sbd-theory-of-everything/ameacas/🧩-anexo-j-–-ataques-por-engenharia-social---prs-maliciosos-disfarçados', '46d'),
                exact: true,
                sidebar: "defaultSidebar"
              },
              {
                path: '/sbd-theory-of-everything/ameacas/🧩-anexo-k-–-manipulação-de-configurações-ou-metadados-(ex:-sbom,-labels,-tags)',
                component: ComponentCreator('/sbd-theory-of-everything/ameacas/🧩-anexo-k-–-manipulação-de-configurações-ou-metadados-(ex:-sbom,-labels,-tags)', 'be8'),
                exact: true,
                sidebar: "defaultSidebar"
              },
              {
                path: '/sbd-theory-of-everything/ameacas/estrutura-deste-capítulo',
                component: ComponentCreator('/sbd-theory-of-everything/ameacas/estrutura-deste-capítulo', '5cf'),
                exact: true,
                sidebar: "defaultSidebar"
              },
              {
                path: '/sbd-theory-of-everything/ameacas/fontes-e-referências-utilizadas-para-identificação-de-ameaças',
                component: ComponentCreator('/sbd-theory-of-everything/ameacas/fontes-e-referências-utilizadas-para-identificação-de-ameaças', 'b5b'),
                exact: true,
                sidebar: "defaultSidebar"
              },
              {
                path: '/sbd-theory-of-everything/ameacas/intro',
                component: ComponentCreator('/sbd-theory-of-everything/ameacas/intro', 'a17'),
                exact: true,
                sidebar: "defaultSidebar"
              },
              {
                path: '/sbd-theory-of-everything/ameacas/mapa-consolidado-de-ameaças-e-mitigações',
                component: ComponentCreator('/sbd-theory-of-everything/ameacas/mapa-consolidado-de-ameaças-e-mitigações', 'ecc'),
                exact: true,
                sidebar: "defaultSidebar"
              }
            ]
          }
        ]
      }
    ]
  },
  {
    path: '/sbd-theory-of-everything/ia',
    component: ComponentCreator('/sbd-theory-of-everything/ia', '7f5'),
    routes: [
      {
        path: '/sbd-theory-of-everything/ia',
        component: ComponentCreator('/sbd-theory-of-everything/ia', '18f'),
        routes: [
          {
            path: '/sbd-theory-of-everything/ia',
            component: ComponentCreator('/sbd-theory-of-everything/ia', '026'),
            routes: [
              {
                path: '/sbd-theory-of-everything/ia/01-0.-enquadramento-e-objetivos',
                component: ComponentCreator('/sbd-theory-of-everything/ia/01-0.-enquadramento-e-objetivos', 'df1'),
                exact: true,
                sidebar: "defaultSidebar"
              },
              {
                path: '/sbd-theory-of-everything/ia/02-1.-princípios-fundamentais',
                component: ComponentCreator('/sbd-theory-of-everything/ia/02-1.-princípios-fundamentais', 'dbf'),
                exact: true,
                sidebar: "defaultSidebar"
              },
              {
                path: '/sbd-theory-of-everything/ia/03-2.-integração-transversal-por-fase-do-sdlc',
                component: ComponentCreator('/sbd-theory-of-everything/ia/03-2.-integração-transversal-por-fase-do-sdlc', '9e4'),
                exact: true,
                sidebar: "defaultSidebar"
              },
              {
                path: '/sbd-theory-of-everything/ia/04-3.-taxonomia-de-riscos-associados-a-ia',
                component: ComponentCreator('/sbd-theory-of-everything/ia/04-3.-taxonomia-de-riscos-associados-a-ia', '2f1'),
                exact: true,
                sidebar: "defaultSidebar"
              },
              {
                path: '/sbd-theory-of-everything/ia/05-4.-controles-e-checklists-por-fase-do-sdlc',
                component: ComponentCreator('/sbd-theory-of-everything/ia/05-4.-controles-e-checklists-por-fase-do-sdlc', 'bd3'),
                exact: true,
                sidebar: "defaultSidebar"
              },
              {
                path: '/sbd-theory-of-everything/ia/06-5.-frameworks-de-referência-e-aderência',
                component: ComponentCreator('/sbd-theory-of-everything/ia/06-5.-frameworks-de-referência-e-aderência', 'cc2'),
                exact: true,
                sidebar: "defaultSidebar"
              },
              {
                path: '/sbd-theory-of-everything/ia/07-6.-papéis,-responsabilidades-e-estrutura-organizacional',
                component: ComponentCreator('/sbd-theory-of-everything/ia/07-6.-papéis,-responsabilidades-e-estrutura-organizacional', 'bc7'),
                exact: true,
                sidebar: "defaultSidebar"
              },
              {
                path: '/sbd-theory-of-everything/ia/08-7.-governação-e-programas-internos',
                component: ComponentCreator('/sbd-theory-of-everything/ia/08-7.-governação-e-programas-internos', '2b0'),
                exact: true,
                sidebar: "defaultSidebar"
              },
              {
                path: '/sbd-theory-of-everything/ia/09-8.-inventário-e-visibilidade-de-usos-de-ia',
                component: ComponentCreator('/sbd-theory-of-everything/ia/09-8.-inventário-e-visibilidade-de-usos-de-ia', 'c2b'),
                exact: true,
                sidebar: "defaultSidebar"
              },
              {
                path: '/sbd-theory-of-everything/ia/10-9.-instrumentos-práticos',
                component: ComponentCreator('/sbd-theory-of-everything/ia/10-9.-instrumentos-práticos', '6f0'),
                exact: true,
                sidebar: "defaultSidebar"
              },
              {
                path: '/sbd-theory-of-everything/ia/11-10.-apêndice-técnico',
                component: ComponentCreator('/sbd-theory-of-everything/ia/11-10.-apêndice-técnico', 'c8e'),
                exact: true,
                sidebar: "defaultSidebar"
              },
              {
                path: '/sbd-theory-of-everything/ia/intro',
                component: ComponentCreator('/sbd-theory-of-everything/ia/intro', '421'),
                exact: true,
                sidebar: "defaultSidebar"
              }
            ]
          }
        ]
      }
    ]
  },
  {
    path: '/sbd-theory-of-everything/sbd-toe',
    component: ComponentCreator('/sbd-theory-of-everything/sbd-toe', 'fce'),
    routes: [
      {
        path: '/sbd-theory-of-everything/sbd-toe',
        component: ComponentCreator('/sbd-theory-of-everything/sbd-toe', 'd79'),
        routes: [
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags', '091'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/aceitacao',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/aceitacao', 'f1b'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/acesso-seguro',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/acesso-seguro', '5a3'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/adocao',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/adocao', '8ef'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/ai',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/ai', 'a4b'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/alertas',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/alertas', '3af'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/alinhamento',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/alinhamento', '99d'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/alm',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/alm', 'f20'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/ameacas',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/ameacas', 'c49'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/analise-estatica',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/analise-estatica', 'bbd'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/anexo',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/anexo', '694'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/anomalias',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/anomalias', 'c71'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/anotacao',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/anotacao', '99e'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/aplicacao',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/aplicacao', '7c6'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/aplicacao-critica',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/aplicacao-critica', 'd8d'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/aplicacao-pratica',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/aplicacao-pratica', 'b27'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/apoio',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/apoio', '0c9'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/aprendizagem-continua',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/aprendizagem-continua', '722'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/aprovacao',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/aprovacao', '501'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/arquitetura',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/arquitetura', 'ceb'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/arquitetura-segura',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/arquitetura-segura', '1db'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/artefactos',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/artefactos', '88b'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/assinatura',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/assinatura', 'e39'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/asvs',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/asvs', 'a59'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/auditoria',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/auditoria', '59a'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/automacao',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/automacao', '584'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/automatizacao',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/automatizacao', '741'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/avancadas',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/avancadas', 'bce'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/avancado',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/avancado', 'd72'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/backlog',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/backlog', '71e'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/base',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/base', 'ae5'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/bia',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/bia', 'ea3'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/black-box',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/black-box', '126'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/boas-praticas',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/boas-praticas', '90f'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/branches',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/branches', '9a9'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/bsimm',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/bsimm', '1f7'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/build',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/build', '5d5'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/canon',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/canon', '1f8'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/capec',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/capec', '8ea'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/capitulo-2',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/capitulo-2', '464'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/capitulos',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/capitulos', 'df2'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/caso-de-estudo',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/caso-de-estudo', '85c'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/catalogo',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/catalogo', '8da'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/cd',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/cd', '33d'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/centralizacao',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/centralizacao', '90a'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/champions',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/champions', '88d'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/checklist',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/checklist', '56f'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/checkov',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/checkov', '12a'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/ci',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/ci', '609'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/ci-cd',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/ci-cd', 'a21'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/cicd',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/cicd', '0cd'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/ciclo-continuo',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/ciclo-continuo', 'ea8'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/ciclo-de-vida',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/ciclo-de-vida', '59f'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/ciclo-vida',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/ciclo-vida', 'c37'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/cis',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/cis', '05f'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/classificacao',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/classificacao', 'a8d'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/cobertura',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/cobertura', 'fab'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/codificacao-segura',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/codificacao-segura', 'be8'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/codigo',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/codigo', '7cf'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/codigo-fonte',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/codigo-fonte', 'f3b'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/codigo-gerado',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/codigo-gerado', '88e'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/codigo-seguro',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/codigo-seguro', '454'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/compliance',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/compliance', '1ab'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/comunicacao',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/comunicacao', '961'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/conformidade',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/conformidade', '2b6'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/conhecimento',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/conhecimento', 'be6'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/containers',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/containers', '102'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/conteudos',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/conteudos', '56c'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/contratacao',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/contratacao', '35f'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/contratados',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/contratados', 'a9f'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/contratos',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/contratos', '1de'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/controles',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/controles', 'a6a'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/controlo',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/controlo', '304'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/controlo-organizacional',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/controlo-organizacional', 'ca3'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/controlos',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/controlos', '2fc'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/correlacao',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/correlacao', '980'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/cosign',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/cosign', 'add'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/criticidade',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/criticidade', '258'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/cultura',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/cultura', '87c'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/cve',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/cve', 'ced'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/dashboards',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/dashboards', '1bd'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/dast',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/dast', '1d9'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/dependencias',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/dependencias', '4b2'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/deploy',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/deploy', 'cce'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/desenvolvimento',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/desenvolvimento', 'eeb'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/detecao',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/detecao', '249'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/deteccao',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/deteccao', 'f5a'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/dev',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/dev', 'a8a'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/dev-sec-ops',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/dev-sec-ops', '19f'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/devops',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/devops', 'b91'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/devsecops',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/devsecops', '597'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/dfd',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/dfd', '190'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/diagramas',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/diagramas', '3f2'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/dominios',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/dominios', 'a19'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/dsomm',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/dsomm', 'f98'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/dsoom',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/dsoom', '19d'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/ecs',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/ecs', '777'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/eixo',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/eixo', 'bf4'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/enforcement',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/enforcement', '0c2'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/equipa',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/equipa', '6b0'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/equipas',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/equipas', 'e18'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/estrutura',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/estrutura', 'bde'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/estruturacao',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/estruturacao', 'fba'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/estudo-de-caso',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/estudo-de-caso', 'c39'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/eventos',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/eventos', 'ed9'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/eventos-criticos',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/eventos-criticos', '40a'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/evidencia',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/evidencia', '334'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/evidencias',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/evidencias', 'baf'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/evolucao',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/evolucao', 'dc6'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/excecao',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/excecao', '1ac'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/excecoes',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/excecoes', 'cb6'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/exceptions',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/exceptions', '8bd'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/execucao',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/execucao', '6e1'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/execucao-segura',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/execucao-segura', '706'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/execucoes',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/execucoes', 'f15'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/exemplo',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/exemplo', '59d'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/exemplos',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/exemplos', '8b6'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/feedback',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/feedback', '67e'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/ferramentas',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/ferramentas', '011'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/findings',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/findings', 'c39'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/fluxo',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/fluxo', '103'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/formacao',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/formacao', '357'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/fornecedores',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/fornecedores', 'fc7'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/frameworks',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/frameworks', '891'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/fundamentos',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/fundamentos', '3e3'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/fuzzers',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/fuzzers', '832'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/fuzzing',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/fuzzing', '6bf'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/gamificacao',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/gamificacao', 'dd1'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/gates',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/gates', 'bd7'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/gen-ai',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/gen-ai', '575'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/genia',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/genia', 'a82'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/gestao',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/gestao', '656'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/git',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/git', '1c2'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/governacao',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/governacao', 'd05'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/governanca',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/governanca', 'ecd'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/governance',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/governance', 'da3'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/grey-box',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/grey-box', 'b6f'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/grupo-avancado',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/grupo-avancado', '48b'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/grupo-execucao',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/grupo-execucao', 'eab'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/guidelines',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/guidelines', '395'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/hardening',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/hardening', '0ef'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/iac',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/iac', 'a43'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/iast',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/iast', '97b'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/ide',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/ide', 'bd0'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/imagem',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/imagem', '72f'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/imagens',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/imagens', '692'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/imagens-base',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/imagens-base', '55c'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/inception',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/inception', '6c6'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/inclusao',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/inclusao', '77e'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/indicadores',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/indicadores', 'e11'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/infraestrutura',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/infraestrutura', '5bf'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/infraestrutura-como-codigo',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/infraestrutura-como-codigo', '2c9'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/instrumentacao',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/instrumentacao', '67d'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/integracao',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/integracao', '126'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/integracao-continua',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/integracao-continua', '5e3'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/introducao',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/introducao', 'f6f'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/invetario',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/invetario', 'e44'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/iriusrisk',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/iriusrisk', '721'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/irp',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/irp', 'c5a'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/iso',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/iso', '603'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/isolamento',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/isolamento', '85b'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/isolation',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/isolation', '7e6'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/kpi',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/kpi', '420'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/kubernetes',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/kubernetes', '420'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/kyverno',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/kyverno', '1de'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/l-1',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/l-1', '8ae'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/l-2',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/l-2', '106'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/l-3',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/l-3', '35b'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/legado',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/legado', '83e'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/lifecycle',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/lifecycle', '5b0'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/linddun',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/linddun', '774'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/linters',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/linters', '0d8'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/lms',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/lms', '75d'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/logging',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/logging', '6cd'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/logs',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/logs', '7ba'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/manual',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/manual', 'a44'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/mapeamento',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/mapeamento', '038'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/matriz',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/matriz', '1be'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/maturidade',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/maturidade', '425'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/metodologia',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/metodologia', '6fb'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/metodologias',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/metodologias', '115'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/metricas',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/metricas', 'f53'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/migracao',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/migracao', '1ca'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/mitigacao',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/mitigacao', '4b9'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/modulos',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/modulos', '883'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/monitorizacao',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/monitorizacao', '689'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/mttd',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/mttd', 'dbd'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/mttr',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/mttr', 'd0e'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/multi-sistema',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/multi-sistema', 'f8d'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/nist',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/nist', '52b'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/normas',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/normas', '2fb'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/normativo',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/normativo', '36b'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/notary',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/notary', 'db3'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/observabilidade',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/observabilidade', 'f52'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/onboarding',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/onboarding', 'd7d'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/opa',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/opa', 'c51'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/operacoes',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/operacoes', '91d'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/organizacional',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/organizacional', 'fc3'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/osc-r',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/osc-r', '6d7'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/oscar',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/oscar', 'c57'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/ownership',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/ownership', '889'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/parsing',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/parsing', 'e45'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/pasta',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/pasta', '790'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/pedagogia',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/pedagogia', 'ffe'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/pentesting',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/pentesting', '06b'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/perfis',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/perfis', '297'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/permissao',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/permissao', '244'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/permissoes',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/permissoes', '5a5'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/pipeline',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/pipeline', '356'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/pipelines',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/pipelines', '3e1'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/planeamento',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/planeamento', '1e4'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/plano',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/plano', 'e5d'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/playbooks',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/playbooks', '37d'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/policies',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/policies', '2d0'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/policy',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/policy', '257'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/politicas',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/politicas', '3ce'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/por-capitulo',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/por-capitulo', '0c5'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/praticas-avancadas',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/praticas-avancadas', '395'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/praticas-seguras',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/praticas-seguras', '12e'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/pre-commit',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/pre-commit', 'a94'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/pre-deploy',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/pre-deploy', 'a34'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/principios',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/principios', '760'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/priorizacao',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/priorizacao', 'e2e'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/privacidade',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/privacidade', '891'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/projeto',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/projeto', '372'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/proporcionalidade',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/proporcionalidade', '241'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/proveniencia',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/proveniencia', '89c'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/pull-request',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/pull-request', 'db6'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/quiz',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/quiz', '49d'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/rastreabilidade',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/rastreabilidade', '9b1'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/readiness',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/readiness', 'ba7'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/recomendacoes',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/recomendacoes', '588'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/referencia-cruzada',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/referencia-cruzada', '482'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/reforco',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/reforco', '0de'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/regressao',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/regressao', '284'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/rekor',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/rekor', 'c67'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/repositorios',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/repositorios', '654'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/requisitos',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/requisitos', '067'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/responsabilidade',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/responsabilidade', '013'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/resposta',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/resposta', '315'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/resposta-a-incidentes',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/resposta-a-incidentes', '5e8'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/reutilizacao',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/reutilizacao', '011'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/reversibilidade',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/reversibilidade', '664'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/revisao',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/revisao', 'cb1'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/revisao-tecnica',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/revisao-tecnica', '312'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/risco',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/risco', 'e0e'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/risco-residual',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/risco-residual', '181'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/risks',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/risks', '2a5'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/rollback',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/rollback', 'ea9'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/runners',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/runners', 'b8d'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/runtime',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/runtime', '7e6'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/samm',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/samm', 'c8c'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/sast',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/sast', '007'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/sbd-toe',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/sbd-toe', '1eb'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/sbdtoe',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/sbdtoe', 'd2f'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/sbom',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/sbom', '8c6'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/sbomm',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/sbomm', 'd83'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/sca',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/sca', 'e3c'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/scanner',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/scanner', '003'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/scm',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/scm', 'c77'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/scripts',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/scripts', '1cf'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/sdcl',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/sdcl', '62d'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/sdlc',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/sdlc', '06e'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/secure-coding',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/secure-coding', '419'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/security-by-design',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/security-by-design', '662'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/segredos',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/segredos', 'fba'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/segregacao',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/segregacao', '39a'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/seguranca',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/seguranca', '062'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/seguranca-aplicada',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/seguranca-aplicada', 'f6a'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/seguranca-humana',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/seguranca-humana', '2ff'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/seguranca-ofensiva',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/seguranca-ofensiva', 'd7a'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/seguranca-organizacional',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/seguranca-organizacional', '017'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/severidade',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/severidade', 'ecb'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/siem',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/siem', '578'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/simulacao',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/simulacao', 'c03'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/slsa',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/slsa', '866'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/soar',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/soar', '6f0'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/ssdf',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/ssdf', '871'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/staging',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/staging', '021'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/stride',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/stride', '283'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/supply-chai',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/supply-chai', '281'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/supply-chain',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/supply-chain', '3da'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/syft',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/syft', '64b'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/tags',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/tags', 'bd7'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/taxonomia',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/taxonomia', '646'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/tecnicas',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/tecnicas', '984'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/telemetria',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/telemetria', '590'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/tema-classificacao',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/tema-classificacao', 'dc1'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/tema-criticidade',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/tema-criticidade', 'b86'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/tema-deploy',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/tema-deploy', 'c55'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/tema-deploy-progressivo',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/tema-deploy-progressivo', '324'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/tema-drp',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/tema-drp', 'c39'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/tema-feature-flags',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/tema-feature-flags', '7e2'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/tema-iac',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/tema-iac', '33e'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/tema-monitorizacao',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/tema-monitorizacao', '31d'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/tema-pipeline',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/tema-pipeline', '1f0'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/tema-release',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/tema-release', '691'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/tema-requisitos',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/tema-requisitos', 'ad5'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/tema-resumo',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/tema-resumo', 'bf1'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/tema-revisao',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/tema-revisao', 'e2d'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/tema-risco',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/tema-risco', 'e94'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/tema-rollback',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/tema-rollback', 'e17'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/tema-threat-modeling',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/tema-threat-modeling', 'add'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/tema-validacao',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/tema-validacao', '86f'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/temas',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/temas', '3ff'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/terceiros',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/terceiros', '5cc'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/terraform',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/terraform', 'caa'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/teste',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/teste', 'f1d'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/testes',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/testes', 'ee6'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/testes-aleatorios',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/testes-aleatorios', '0cf'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/testes-dinamicos',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/testes-dinamicos', '0b1'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/testes-interativos',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/testes-interativos', '543'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/testes-manuais',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/testes-manuais', 'c3d'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/tfsec',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/tfsec', 'd36'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/threat-modeling',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/threat-modeling', '4fe'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/threats',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/threats', '03b'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/thresholds',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/thresholds', '700'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/tipo-aceitacao',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/tipo-aceitacao', '79c'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/tipo-analise',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/tipo-analise', '3e8'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/tipo-anexo',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/tipo-anexo', 'e42'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/tipo-aplicacao',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/tipo-aplicacao', '102'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/tipo-avaliacao',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/tipo-avaliacao', 'fe8'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/tipo-avancado',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/tipo-avancado', 'c8e'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/tipo-catalogo',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/tipo-catalogo', '148'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/tipo-ciclo',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/tipo-ciclo', 'b10'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/tipo-criterios',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/tipo-criterios', 'f1a'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/tipo-exemplo',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/tipo-exemplo', '2d4'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/tipo-ligacao',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/tipo-ligacao', 'd8d'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/tipo-mapeamento',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/tipo-mapeamento', '7ec'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/tipo-matriz',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/tipo-matriz', 'e58'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/tipo-modelo',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/tipo-modelo', '2a6'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/tipo-prescricao',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/tipo-prescricao', '7c4'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/toggle',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/toggle', 'b77'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/toggles',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/toggles', 'c65'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/tooling',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/tooling', 'f38'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/transporte-seguro',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/transporte-seguro', '2ec'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/triggers',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/triggers', '7b6'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/trilho',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/trilho', 'fcb'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/trivy',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/trivy', '226'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/trust',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/trust', '7ac'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/user-stories',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/user-stories', 'a1a'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/user-story',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/user-story', 'd0b'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/validacao',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/validacao', 'dca'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/validacao-continua',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/validacao-continua', '957'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/validacoes',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/validacoes', '0e3'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/variaveis',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/variaveis', 'c42'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/vault',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/vault', '947'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/versionamento',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/versionamento', '94f'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/visibilidade',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/visibilidade', '99b'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/vulnerabilidades',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/vulnerabilidades', '22a'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/yaml',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/yaml', '655'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe/tags/zero-trust',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/tags/zero-trust', '3da'),
            exact: true
          },
          {
            path: '/sbd-theory-of-everything/sbd-toe',
            component: ComponentCreator('/sbd-theory-of-everything/sbd-toe', '936'),
            routes: [
              {
                path: '/sbd-theory-of-everything/sbd-toe/',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/', '422'),
                exact: true,
                sidebar: "sbdToeSidebar"
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/arquitetura-segura/addon/01-catalogo-requisitos-aplicacionais',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/arquitetura-segura/addon/01-catalogo-requisitos-aplicacionais', 'a68'),
                exact: true,
                sidebar: "sbdToeSidebar"
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/arquitetura-segura/addon/casos-praticos',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/arquitetura-segura/addon/casos-praticos', 'f1f'),
                exact: true,
                sidebar: "sbdToeSidebar"
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/arquitetura-segura/addon/criterios-validacao',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/arquitetura-segura/addon/criterios-validacao', '8dd'),
                exact: true,
                sidebar: "sbdToeSidebar"
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/arquitetura-segura/addon/diagramas-referencia',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/arquitetura-segura/addon/diagramas-referencia', '282'),
                exact: true,
                sidebar: "sbdToeSidebar"
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/arquitetura-segura/addon/excecoes',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/arquitetura-segura/addon/excecoes', '92d'),
                exact: true,
                sidebar: "sbdToeSidebar"
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/arquitetura-segura/addon/matriz-requisitos-iac',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/arquitetura-segura/addon/matriz-requisitos-iac', '57f'),
                exact: true,
                sidebar: "sbdToeSidebar"
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/arquitetura-segura/canon/ameacas-mitigadas',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/arquitetura-segura/canon/ameacas-mitigadas', '86c'),
                exact: true
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/arquitetura-segura/canon/aplicacao-lifecycle',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/arquitetura-segura/canon/aplicacao-lifecycle', '3a3'),
                exact: true,
                sidebar: "sbdToeSidebar"
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/arquitetura-segura/canon/checklist-revisao',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/arquitetura-segura/canon/checklist-revisao', '017'),
                exact: true
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/arquitetura-segura/canon/maturidade',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/arquitetura-segura/canon/maturidade', '12a'),
                exact: true
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/arquitetura-segura/canon/policies-relevantes',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/arquitetura-segura/canon/policies-relevantes', 'f6f'),
                exact: true
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/arquitetura-segura/canon/rastreabilidade',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/arquitetura-segura/canon/rastreabilidade', '3da'),
                exact: true
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/arquitetura-segura/canon/recomendacoes-avancadas',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/arquitetura-segura/canon/recomendacoes-avancadas', '270'),
                exact: true
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/arquitetura-segura/intro',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/arquitetura-segura/intro', '1e1'),
                exact: true,
                sidebar: "sbdToeSidebar"
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/capitulos-basilares',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/capitulos-basilares', '51d'),
                exact: true,
                sidebar: "sbdToeSidebar"
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/cicd-seguro/addon/controle-excecoes-visibilidade',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/cicd-seguro/addon/controle-excecoes-visibilidade', '1a0'),
                exact: true,
                sidebar: "sbdToeSidebar"
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/cicd-seguro/addon/controle-excecoes-visibilidade',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/cicd-seguro/addon/controle-excecoes-visibilidade', '4c9'),
                exact: true,
                sidebar: "sbdToeSidebar"
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/cicd-seguro/addon/controle-excecoes-visibilidade',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/cicd-seguro/addon/controle-excecoes-visibilidade', 'df0'),
                exact: true,
                sidebar: "sbdToeSidebar"
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/cicd-seguro/addon/design-seguro-pipelines',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/cicd-seguro/addon/design-seguro-pipelines', 'f19'),
                exact: true,
                sidebar: "sbdToeSidebar"
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/cicd-seguro/addon/gestao-codigo-fonte',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/cicd-seguro/addon/gestao-codigo-fonte', '3d4'),
                exact: true,
                sidebar: "sbdToeSidebar"
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/cicd-seguro/addon/gestao-segredos-pipeline',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/cicd-seguro/addon/gestao-segredos-pipeline', 'd7e'),
                exact: true,
                sidebar: "sbdToeSidebar"
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/cicd-seguro/addon/integridade-proveniencia',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/cicd-seguro/addon/integridade-proveniencia', 'e99'),
                exact: true,
                sidebar: "sbdToeSidebar"
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/cicd-seguro/addon/isolamento-runners',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/cicd-seguro/addon/isolamento-runners', '635'),
                exact: true,
                sidebar: "sbdToeSidebar"
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/cicd-seguro/addon/politicas-gates-pipeline',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/cicd-seguro/addon/politicas-gates-pipeline', '164'),
                exact: true,
                sidebar: "sbdToeSidebar"
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/cicd-seguro/addon/rastreabilidade-assinaturas',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/cicd-seguro/addon/rastreabilidade-assinaturas', '6eb'),
                exact: true,
                sidebar: "sbdToeSidebar"
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/cicd-seguro/addon/seguranca-codigo-pipeline',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/cicd-seguro/addon/seguranca-codigo-pipeline', '79d'),
                exact: true,
                sidebar: "sbdToeSidebar"
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/cicd-seguro/addon/validacoes-seguranca-integradas',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/cicd-seguro/addon/validacoes-seguranca-integradas', '5e6'),
                exact: true,
                sidebar: "sbdToeSidebar"
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/cicd-seguro/canon/ameacas-mitigadas',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/cicd-seguro/canon/ameacas-mitigadas', '6e6'),
                exact: true
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/cicd-seguro/canon/aplicacao-lifecycle',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/cicd-seguro/canon/aplicacao-lifecycle', '0ac'),
                exact: true,
                sidebar: "sbdToeSidebar"
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/cicd-seguro/canon/checklist-revisao',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/cicd-seguro/canon/checklist-revisao', '08d'),
                exact: true
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/cicd-seguro/canon/maturidade',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/cicd-seguro/canon/maturidade', '963'),
                exact: true
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/cicd-seguro/canon/policies-relevantes',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/cicd-seguro/canon/policies-relevantes', '341'),
                exact: true
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/cicd-seguro/canon/rastreabilidade',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/cicd-seguro/canon/rastreabilidade', 'cb3'),
                exact: true
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/cicd-seguro/canon/recomendacoes-avancadas',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/cicd-seguro/canon/recomendacoes-avancadas', '320'),
                exact: true
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/cicd-seguro/intro',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/cicd-seguro/intro', 'e18'),
                exact: true,
                sidebar: "sbdToeSidebar"
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/classificacao-aplicacoes/addon/adopcao-drp-bia',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/classificacao-aplicacoes/addon/adopcao-drp-bia', 'e40'),
                exact: true,
                sidebar: "sbdToeSidebar"
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/classificacao-aplicacoes/addon/avaliacao-semiquantitativa',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/classificacao-aplicacoes/addon/avaliacao-semiquantitativa', '554'),
                exact: true,
                sidebar: "sbdToeSidebar"
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/classificacao-aplicacoes/addon/casos-praticos',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/classificacao-aplicacoes/addon/casos-praticos', '147'),
                exact: true,
                sidebar: "sbdToeSidebar"
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/classificacao-aplicacoes/addon/ciclo-vida-risco',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/classificacao-aplicacoes/addon/ciclo-vida-risco', 'c15'),
                exact: true,
                sidebar: "sbdToeSidebar"
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/classificacao-aplicacoes/addon/criterios-aceitacao-risco',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/classificacao-aplicacoes/addon/criterios-aceitacao-risco', '24c'),
                exact: true,
                sidebar: "sbdToeSidebar"
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/classificacao-aplicacoes/addon/mapeamento-ameacas-risco',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/classificacao-aplicacoes/addon/mapeamento-ameacas-risco', '1f9'),
                exact: true,
                sidebar: "sbdToeSidebar"
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/classificacao-aplicacoes/addon/matriz-controlos-por-risco',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/classificacao-aplicacoes/addon/matriz-controlos-por-risco', '7ee'),
                exact: true,
                sidebar: "sbdToeSidebar"
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/classificacao-aplicacoes/addon/modelo-classificacao-eixos',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/classificacao-aplicacoes/addon/modelo-classificacao-eixos', 'ad7'),
                exact: true,
                sidebar: "sbdToeSidebar"
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/classificacao-aplicacoes/addon/risco-residual',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/classificacao-aplicacoes/addon/risco-residual', '0cb'),
                exact: true,
                sidebar: "sbdToeSidebar"
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/classificacao-aplicacoes/aplicacao-lifecycle',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/classificacao-aplicacoes/aplicacao-lifecycle', 'e36'),
                exact: true,
                sidebar: "sbdToeSidebar"
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/classificacao-aplicacoes/canon/ameacas-mitigadas',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/classificacao-aplicacoes/canon/ameacas-mitigadas', '093'),
                exact: true
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/classificacao-aplicacoes/canon/checklist-revisao',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/classificacao-aplicacoes/canon/checklist-revisao', '78e'),
                exact: true
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/classificacao-aplicacoes/canon/maturidade',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/classificacao-aplicacoes/canon/maturidade', '1a3'),
                exact: true
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/classificacao-aplicacoes/canon/policies-relevantes',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/classificacao-aplicacoes/canon/policies-relevantes', '9c5'),
                exact: true
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/classificacao-aplicacoes/canon/rastreabilidade',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/classificacao-aplicacoes/canon/rastreabilidade', '0c4'),
                exact: true
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/classificacao-aplicacoes/canon/recomendacoes-avancadas',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/classificacao-aplicacoes/canon/recomendacoes-avancadas', 'f79'),
                exact: true
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/classificacao-aplicacoes/intro',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/classificacao-aplicacoes/intro', '36b'),
                exact: true,
                sidebar: "sbdToeSidebar"
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/classificacao-aplicacoes/pre-intro-rationale',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/classificacao-aplicacoes/pre-intro-rationale', '5f5'),
                exact: true
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/como-usar-este-manual',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/como-usar-este-manual', 'a6c'),
                exact: true,
                sidebar: "sbdToeSidebar"
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/containers-imagens/addon/assinatura-cadeia-trust',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/containers-imagens/addon/assinatura-cadeia-trust', '414'),
                exact: true,
                sidebar: "sbdToeSidebar"
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/containers-imagens/addon/exemplo-pipeline-container',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/containers-imagens/addon/exemplo-pipeline-container', '2c6'),
                exact: true,
                sidebar: "sbdToeSidebar"
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/containers-imagens/addon/hardening-containers',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/containers-imagens/addon/hardening-containers', '5e8'),
                exact: true,
                sidebar: "sbdToeSidebar"
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/containers-imagens/addon/imagens-base',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/containers-imagens/addon/imagens-base', 'c25'),
                exact: true,
                sidebar: "sbdToeSidebar"
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/containers-imagens/addon/kubernetes-execucao',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/containers-imagens/addon/kubernetes-execucao', '864'),
                exact: true,
                sidebar: "sbdToeSidebar"
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/containers-imagens/addon/policies-runtime-opa',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/containers-imagens/addon/policies-runtime-opa', '238'),
                exact: true,
                sidebar: "sbdToeSidebar"
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/containers-imagens/addon/runners-isolamento',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/containers-imagens/addon/runners-isolamento', 'f73'),
                exact: true,
                sidebar: "sbdToeSidebar"
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/containers-imagens/addon/sbom-containers',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/containers-imagens/addon/sbom-containers', 'df9'),
                exact: true,
                sidebar: "sbdToeSidebar"
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/containers-imagens/addon/vulnerabilidades-imagens',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/containers-imagens/addon/vulnerabilidades-imagens', 'fb8'),
                exact: true,
                sidebar: "sbdToeSidebar"
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/containers-imagens/canon/ameacas-mitigadas',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/containers-imagens/canon/ameacas-mitigadas', '6be'),
                exact: true
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/containers-imagens/canon/aplicacao-lifecycle',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/containers-imagens/canon/aplicacao-lifecycle', 'e7a'),
                exact: true,
                sidebar: "sbdToeSidebar"
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/containers-imagens/canon/checklist-revisao',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/containers-imagens/canon/checklist-revisao', 'ea3'),
                exact: true
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/containers-imagens/canon/maturidade',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/containers-imagens/canon/maturidade', '70e'),
                exact: true
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/containers-imagens/canon/policies-relevantes',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/containers-imagens/canon/policies-relevantes', 'ee1'),
                exact: true
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/containers-imagens/canon/rastreabilidade',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/containers-imagens/canon/rastreabilidade', '223'),
                exact: true
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/containers-imagens/canon/recomendacoes-avancadas',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/containers-imagens/canon/recomendacoes-avancadas', 'fb1'),
                exact: true
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/containers-imagens/intro',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/containers-imagens/intro', '916'),
                exact: true,
                sidebar: "sbdToeSidebar"
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/coverage-frameworks',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/coverage-frameworks', '681'),
                exact: true,
                sidebar: "sbdToeSidebar"
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/dependencias-sbom-sca/addon/analise-sca',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/dependencias-sbom-sca/addon/analise-sca', '4b9'),
                exact: true,
                sidebar: "sbdToeSidebar"
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/dependencias-sbom-sca/addon/controle-registos-origem',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/dependencias-sbom-sca/addon/controle-registos-origem', 'b94'),
                exact: true,
                sidebar: "sbdToeSidebar"
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/dependencias-sbom-sca/addon/excecoes-e-aceitacao-risco',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/dependencias-sbom-sca/addon/excecoes-e-aceitacao-risco', '5f4'),
                exact: true,
                sidebar: "sbdToeSidebar"
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/dependencias-sbom-sca/addon/governanca-libs-terceiros',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/dependencias-sbom-sca/addon/governanca-libs-terceiros', '8c7'),
                exact: true,
                sidebar: "sbdToeSidebar"
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/dependencias-sbom-sca/addon/integracao-ci-cd',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/dependencias-sbom-sca/addon/integracao-ci-cd', 'e80'),
                exact: true,
                sidebar: "sbdToeSidebar"
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/dependencias-sbom-sca/addon/inventario-sbom',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/dependencias-sbom-sca/addon/inventario-sbom', 'bd0'),
                exact: true,
                sidebar: "sbdToeSidebar"
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/dependencias-sbom-sca/addon/politica-atualizacoes',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/dependencias-sbom-sca/addon/politica-atualizacoes', 'bd7'),
                exact: true,
                sidebar: "sbdToeSidebar"
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/dependencias-sbom-sca/addon/rastreabilidade-vulnerabilidades',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/dependencias-sbom-sca/addon/rastreabilidade-vulnerabilidades', 'b8a'),
                exact: true,
                sidebar: "sbdToeSidebar"
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/dependencias-sbom-sca/addon/risco-supply-chain',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/dependencias-sbom-sca/addon/risco-supply-chain', 'c77'),
                exact: true,
                sidebar: "sbdToeSidebar"
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/dependencias-sbom-sca/canon/ameacas-mitigadas',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/dependencias-sbom-sca/canon/ameacas-mitigadas', 'c68'),
                exact: true
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/dependencias-sbom-sca/canon/aplicacao-lifecycle',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/dependencias-sbom-sca/canon/aplicacao-lifecycle', '893'),
                exact: true,
                sidebar: "sbdToeSidebar"
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/dependencias-sbom-sca/canon/checklist-revisao',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/dependencias-sbom-sca/canon/checklist-revisao', '4c6'),
                exact: true
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/dependencias-sbom-sca/canon/maturidade',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/dependencias-sbom-sca/canon/maturidade', '8e2'),
                exact: true
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/dependencias-sbom-sca/canon/policies-relevantes',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/dependencias-sbom-sca/canon/policies-relevantes', '881'),
                exact: true
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/dependencias-sbom-sca/canon/rastreabilidade',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/dependencias-sbom-sca/canon/rastreabilidade', '464'),
                exact: true
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/dependencias-sbom-sca/canon/recomendacoes-avancadas',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/dependencias-sbom-sca/canon/recomendacoes-avancadas', '6b6'),
                exact: true
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/dependencias-sbom-sca/intro',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/dependencias-sbom-sca/intro', '515'),
                exact: true,
                sidebar: "sbdToeSidebar"
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/deploy-seguro/',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/deploy-seguro/', '9d2'),
                exact: true
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/deploy-seguro/addon/01-modelo-controle-execucao',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/deploy-seguro/addon/01-modelo-controle-execucao', 'c38'),
                exact: true,
                sidebar: "sbdToeSidebar"
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/deploy-seguro/addon/02-praticas-release-management',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/deploy-seguro/addon/02-praticas-release-management', 'de5'),
                exact: true,
                sidebar: "sbdToeSidebar"
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/deploy-seguro/addon/03-feature-flags-e-toggle',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/deploy-seguro/addon/03-feature-flags-e-toggle', '959'),
                exact: true,
                sidebar: "sbdToeSidebar"
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/deploy-seguro/addon/04-validacoes-pre-deploy',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/deploy-seguro/addon/04-validacoes-pre-deploy', '1b3'),
                exact: true,
                sidebar: "sbdToeSidebar"
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/deploy-seguro/addon/05-monitorizacao-e-reacao',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/deploy-seguro/addon/05-monitorizacao-e-reacao', '109'),
                exact: true,
                sidebar: "sbdToeSidebar"
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/deploy-seguro/addon/06-controle-versao-e-rollback',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/deploy-seguro/addon/06-controle-versao-e-rollback', '588'),
                exact: true,
                sidebar: "sbdToeSidebar"
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/deploy-seguro/addon/07-deploy-progressivo-e-risco',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/deploy-seguro/addon/07-deploy-progressivo-e-risco', '6af'),
                exact: true,
                sidebar: "sbdToeSidebar"
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/deploy-seguro/addon/08-segregacao-e-validacao-operacional',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/deploy-seguro/addon/08-segregacao-e-validacao-operacional', 'ebf'),
                exact: true,
                sidebar: "sbdToeSidebar"
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/deploy-seguro/canon/ameacas-mitigadas',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/deploy-seguro/canon/ameacas-mitigadas', 'ffb'),
                exact: true
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/deploy-seguro/canon/aplicacao-lifecycle',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/deploy-seguro/canon/aplicacao-lifecycle', 'a9d'),
                exact: true,
                sidebar: "sbdToeSidebar"
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/deploy-seguro/canon/checklist-revisao',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/deploy-seguro/canon/checklist-revisao', '7ea'),
                exact: true
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/deploy-seguro/canon/maturidade',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/deploy-seguro/canon/maturidade', '06d'),
                exact: true
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/deploy-seguro/canon/policies-deploy-seguro',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/deploy-seguro/canon/policies-deploy-seguro', '33d'),
                exact: true
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/deploy-seguro/canon/rastreabilidade',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/deploy-seguro/canon/rastreabilidade', '058'),
                exact: true
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/deploy-seguro/canon/recomendacoes-avancadas-deploy',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/deploy-seguro/canon/recomendacoes-avancadas-deploy', 'd20'),
                exact: true
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/deploy-seguro/intro',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/deploy-seguro/intro', '409'),
                exact: true,
                sidebar: "sbdToeSidebar"
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/desenvolvimento-seguro/addon/anotacoes-evidencia',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/desenvolvimento-seguro/addon/anotacoes-evidencia', '40d'),
                exact: true,
                sidebar: "sbdToeSidebar"
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/desenvolvimento-seguro/addon/boas-praticas-codigo',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/desenvolvimento-seguro/addon/boas-praticas-codigo', '0c3'),
                exact: true,
                sidebar: "sbdToeSidebar"
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/desenvolvimento-seguro/addon/excecoes-e-justificacoes',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/desenvolvimento-seguro/addon/excecoes-e-justificacoes', '11a'),
                exact: true,
                sidebar: "sbdToeSidebar"
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/desenvolvimento-seguro/addon/genia-e-seguranca',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/desenvolvimento-seguro/addon/genia-e-seguranca', 'f91'),
                exact: true,
                sidebar: "sbdToeSidebar"
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/desenvolvimento-seguro/addon/guidelines-equipa',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/desenvolvimento-seguro/addon/guidelines-equipa', '520'),
                exact: true,
                sidebar: "sbdToeSidebar"
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/desenvolvimento-seguro/addon/linters-validacoes',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/desenvolvimento-seguro/addon/linters-validacoes', '495'),
                exact: true,
                sidebar: "sbdToeSidebar"
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/desenvolvimento-seguro/addon/seguranca-dependencias',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/desenvolvimento-seguro/addon/seguranca-dependencias', '2dd'),
                exact: true,
                sidebar: "sbdToeSidebar"
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/desenvolvimento-seguro/addon/validacoes-codigo',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/desenvolvimento-seguro/addon/validacoes-codigo', '183'),
                exact: true,
                sidebar: "sbdToeSidebar"
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/desenvolvimento-seguro/canon/ameacas-mitigadas',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/desenvolvimento-seguro/canon/ameacas-mitigadas', '624'),
                exact: true
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/desenvolvimento-seguro/canon/aplicacao-lifecycle',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/desenvolvimento-seguro/canon/aplicacao-lifecycle', '41e'),
                exact: true,
                sidebar: "sbdToeSidebar"
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/desenvolvimento-seguro/canon/checklist-revisao',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/desenvolvimento-seguro/canon/checklist-revisao', 'ae8'),
                exact: true
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/desenvolvimento-seguro/canon/desenvolvimento-seguro-policies',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/desenvolvimento-seguro/canon/desenvolvimento-seguro-policies', 'cad'),
                exact: true
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/desenvolvimento-seguro/canon/maturidade',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/desenvolvimento-seguro/canon/maturidade', '243'),
                exact: true
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/desenvolvimento-seguro/canon/rastreabilidade',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/desenvolvimento-seguro/canon/rastreabilidade', '997'),
                exact: true
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/desenvolvimento-seguro/canon/recomendacoes-avancadas',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/desenvolvimento-seguro/canon/recomendacoes-avancadas', '43d'),
                exact: true
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/desenvolvimento-seguro/intro',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/desenvolvimento-seguro/intro', '697'),
                exact: true,
                sidebar: "sbdToeSidebar"
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/formacao-onboarding/addon/22-quiz-terceiros',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/formacao-onboarding/addon/22-quiz-terceiros', 'c73'),
                exact: true,
                sidebar: "sbdToeSidebar"
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/formacao-onboarding/addon/catalogo-formativo',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/formacao-onboarding/addon/catalogo-formativo', 'f88'),
                exact: true,
                sidebar: "sbdToeSidebar"
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/formacao-onboarding/addon/checklist-onboarding',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/formacao-onboarding/addon/checklist-onboarding', '851'),
                exact: true,
                sidebar: "sbdToeSidebar"
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/formacao-onboarding/addon/exemplo-manual-dev-pr',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/formacao-onboarding/addon/exemplo-manual-dev-pr', '6f6'),
                exact: true,
                sidebar: "sbdToeSidebar"
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/formacao-onboarding/addon/formacao-iac',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/formacao-onboarding/addon/formacao-iac', '550'),
                exact: true,
                sidebar: "sbdToeSidebar"
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/formacao-onboarding/addon/inclusao-terceiros',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/formacao-onboarding/addon/inclusao-terceiros', 'd79'),
                exact: true,
                sidebar: "sbdToeSidebar"
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/formacao-onboarding/addon/indicadores-metricas',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/formacao-onboarding/addon/indicadores-metricas', '0d8'),
                exact: true,
                sidebar: "sbdToeSidebar"
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/formacao-onboarding/addon/integracao-transversal',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/formacao-onboarding/addon/integracao-transversal', '61d'),
                exact: true,
                sidebar: "sbdToeSidebar"
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/formacao-onboarding/addon/manual-formacao-capitulos',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/formacao-onboarding/addon/manual-formacao-capitulos', 'd7d'),
                exact: true,
                sidebar: "sbdToeSidebar"
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/formacao-onboarding/addon/plano-formacao-terceiros',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/formacao-onboarding/addon/plano-formacao-terceiros', 'd46'),
                exact: true,
                sidebar: "sbdToeSidebar"
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/formacao-onboarding/addon/programa-champions',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/formacao-onboarding/addon/programa-champions', 'd1f'),
                exact: true,
                sidebar: "sbdToeSidebar"
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/formacao-onboarding/addon/quiz-onboarding',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/formacao-onboarding/addon/quiz-onboarding', '584'),
                exact: true,
                sidebar: "sbdToeSidebar"
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/formacao-onboarding/addon/tecnicas-formativas',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/formacao-onboarding/addon/tecnicas-formativas', 'c15'),
                exact: true,
                sidebar: "sbdToeSidebar"
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/formacao-onboarding/addon/trilho-formativo',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/formacao-onboarding/addon/trilho-formativo', 'a79'),
                exact: true,
                sidebar: "sbdToeSidebar"
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/formacao-onboarding/canon/ameacas-mitigadas',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/formacao-onboarding/canon/ameacas-mitigadas', '1b4'),
                exact: true
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/formacao-onboarding/canon/aplicacao-lifecycle',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/formacao-onboarding/canon/aplicacao-lifecycle', 'eb2'),
                exact: true,
                sidebar: "sbdToeSidebar"
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/formacao-onboarding/canon/checklist-revisao',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/formacao-onboarding/canon/checklist-revisao', 'b0b'),
                exact: true
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/formacao-onboarding/canon/checklist-revisao',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/formacao-onboarding/canon/checklist-revisao', '538'),
                exact: true
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/formacao-onboarding/canon/maturidade',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/formacao-onboarding/canon/maturidade', '425'),
                exact: true
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/formacao-onboarding/canon/policies-relevantes',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/formacao-onboarding/canon/policies-relevantes', 'e0c'),
                exact: true
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/formacao-onboarding/canon/recomendacoes-avancadas',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/formacao-onboarding/canon/recomendacoes-avancadas', '471'),
                exact: true
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/formacao-onboarding/intro',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/formacao-onboarding/intro', '93f'),
                exact: true,
                sidebar: "sbdToeSidebar"
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/gaps-por-framework',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/gaps-por-framework', '12b'),
                exact: true,
                sidebar: "sbdToeSidebar"
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/governanca-contratacao/addon/controlos-praticas-sbd',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/governanca-contratacao/addon/controlos-praticas-sbd', '9e0'),
                exact: true,
                sidebar: "sbdToeSidebar"
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/governanca-contratacao/addon/diagramas-governanca',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/governanca-contratacao/addon/diagramas-governanca', 'b2f'),
                exact: true,
                sidebar: "sbdToeSidebar"
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/governanca-contratacao/addon/exemplos-aplicacao-governanca',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/governanca-contratacao/addon/exemplos-aplicacao-governanca', '091'),
                exact: true,
                sidebar: "sbdToeSidebar"
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/governanca-contratacao/addon/governanca-legada',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/governanca-contratacao/addon/governanca-legada', '0b2'),
                exact: true,
                sidebar: "sbdToeSidebar"
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/governanca-contratacao/addon/governancao-maturidade',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/governanca-contratacao/addon/governancao-maturidade', 'a84'),
                exact: true,
                sidebar: "sbdToeSidebar"
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/governanca-contratacao/addon/modelo-governancao',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/governanca-contratacao/addon/modelo-governancao', '9ea'),
                exact: true,
                sidebar: "sbdToeSidebar"
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/governanca-contratacao/addon/modelo-validacao-fornecedores',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/governanca-contratacao/addon/modelo-validacao-fornecedores', 'f09'),
                exact: true,
                sidebar: "sbdToeSidebar"
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/governanca-contratacao/addon/modelo-validacao-fornecedores',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/governanca-contratacao/addon/modelo-validacao-fornecedores', 'ae1'),
                exact: true,
                sidebar: "sbdToeSidebar"
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/governanca-contratacao/addon/rastreabilidade-organizacional',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/governanca-contratacao/addon/rastreabilidade-organizacional', '52d'),
                exact: true,
                sidebar: "sbdToeSidebar"
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/governanca-contratacao/addon/validacao-continuada',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/governanca-contratacao/addon/validacao-continuada', 'bf7'),
                exact: true,
                sidebar: "sbdToeSidebar"
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/governanca-contratacao/canon/ameacas-mitigadas',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/governanca-contratacao/canon/ameacas-mitigadas', '66d'),
                exact: true
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/governanca-contratacao/canon/aplicacao-lifecycle',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/governanca-contratacao/canon/aplicacao-lifecycle', 'c47'),
                exact: true,
                sidebar: "sbdToeSidebar"
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/governanca-contratacao/canon/checklist-revisao',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/governanca-contratacao/canon/checklist-revisao', '0e6'),
                exact: true
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/governanca-contratacao/canon/kpis-governanca',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/governanca-contratacao/canon/kpis-governanca', '06c'),
                exact: true
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/governanca-contratacao/canon/maturidade',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/governanca-contratacao/canon/maturidade', 'e1c'),
                exact: true
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/governanca-contratacao/canon/policies-relevantes',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/governanca-contratacao/canon/policies-relevantes', 'c2b'),
                exact: true
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/governanca-contratacao/canon/rastreabilidade',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/governanca-contratacao/canon/rastreabilidade', '513'),
                exact: true
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/governanca-contratacao/canon/recomendacoes-avancadas',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/governanca-contratacao/canon/recomendacoes-avancadas', '38b'),
                exact: true
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/governanca-contratacao/intro',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/governanca-contratacao/intro', '47e'),
                exact: true,
                sidebar: "sbdToeSidebar"
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/iac-infraestrutura/',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/iac-infraestrutura/', '3f4'),
                exact: true
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/iac-infraestrutura/addon/case-study-inception-apply-sbd-iac',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/iac-infraestrutura/addon/case-study-inception-apply-sbd-iac', '703'),
                exact: true,
                sidebar: "sbdToeSidebar"
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/iac-infraestrutura/addon/controle-enforcement',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/iac-infraestrutura/addon/controle-enforcement', '51e'),
                exact: true,
                sidebar: "sbdToeSidebar"
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/iac-infraestrutura/addon/exemplos-praticas-boas',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/iac-infraestrutura/addon/exemplos-praticas-boas', 'fba'),
                exact: true,
                sidebar: "sbdToeSidebar"
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/iac-infraestrutura/addon/gestao-excecoes',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/iac-infraestrutura/addon/gestao-excecoes', '7c8'),
                exact: true,
                sidebar: "sbdToeSidebar"
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/iac-infraestrutura/addon/governanca-modulos',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/iac-infraestrutura/addon/governanca-modulos', '582'),
                exact: true,
                sidebar: "sbdToeSidebar"
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/iac-infraestrutura/addon/matriz-requisitos-iac',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/iac-infraestrutura/addon/matriz-requisitos-iac', '583'),
                exact: true,
                sidebar: "sbdToeSidebar"
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/iac-infraestrutura/addon/planeamento-e-controle',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/iac-infraestrutura/addon/planeamento-e-controle', '81c'),
                exact: true,
                sidebar: "sbdToeSidebar"
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/iac-infraestrutura/addon/planeamento-e-controle',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/iac-infraestrutura/addon/planeamento-e-controle', '82f'),
                exact: true,
                sidebar: "sbdToeSidebar"
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/iac-infraestrutura/addon/principios-sbd-iac',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/iac-infraestrutura/addon/principios-sbd-iac', '6f2'),
                exact: true,
                sidebar: "sbdToeSidebar"
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/iac-infraestrutura/addon/rastreabilidade-e-tags',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/iac-infraestrutura/addon/rastreabilidade-e-tags', 'af0'),
                exact: true,
                sidebar: "sbdToeSidebar"
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/iac-infraestrutura/canon/ameacas-mitigadas',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/iac-infraestrutura/canon/ameacas-mitigadas', '1e9'),
                exact: true
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/iac-infraestrutura/canon/aplicacao-lifecycle',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/iac-infraestrutura/canon/aplicacao-lifecycle', '9f6'),
                exact: true,
                sidebar: "sbdToeSidebar"
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/iac-infraestrutura/canon/checklist-revisao',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/iac-infraestrutura/canon/checklist-revisao', '06f'),
                exact: true
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/iac-infraestrutura/canon/maturidade',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/iac-infraestrutura/canon/maturidade', '4d2'),
                exact: true
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/iac-infraestrutura/canon/policies-iac',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/iac-infraestrutura/canon/policies-iac', 'eaf'),
                exact: true
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/iac-infraestrutura/canon/rastreabilidade',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/iac-infraestrutura/canon/rastreabilidade', 'cff'),
                exact: true
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/iac-infraestrutura/canon/recomendacoes-avancadas-iac',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/iac-infraestrutura/canon/recomendacoes-avancadas-iac', 'dfc'),
                exact: true
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/iac-infraestrutura/intro',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/iac-infraestrutura/intro', 'b1f'),
                exact: true,
                sidebar: "sbdToeSidebar"
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/matriz-frameworks',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/matriz-frameworks', '5db'),
                exact: true,
                sidebar: "sbdToeSidebar"
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/monitorizacao-operacoes/',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/monitorizacao-operacoes/', 'f6c'),
                exact: true
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/monitorizacao-operacoes/addon/alertas-eventos-criticos',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/monitorizacao-operacoes/addon/alertas-eventos-criticos', 'b73'),
                exact: true,
                sidebar: "sbdToeSidebar"
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/monitorizacao-operacoes/addon/controles-logging-centralizado',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/monitorizacao-operacoes/addon/controles-logging-centralizado', 'bc5'),
                exact: true,
                sidebar: "sbdToeSidebar"
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/monitorizacao-operacoes/addon/correlacao-anomalias',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/monitorizacao-operacoes/addon/correlacao-anomalias', '179'),
                exact: true,
                sidebar: "sbdToeSidebar"
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/monitorizacao-operacoes/addon/dominios-monitorizacao',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/monitorizacao-operacoes/addon/dominios-monitorizacao', '9a8'),
                exact: true,
                sidebar: "sbdToeSidebar"
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/monitorizacao-operacoes/addon/exemplos-eventos',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/monitorizacao-operacoes/addon/exemplos-eventos', '8ab'),
                exact: true,
                sidebar: "sbdToeSidebar"
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/monitorizacao-operacoes/addon/integracao-siem',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/monitorizacao-operacoes/addon/integracao-siem', 'a17'),
                exact: true,
                sidebar: "sbdToeSidebar"
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/monitorizacao-operacoes/addon/matriz-controles-por-risco',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/monitorizacao-operacoes/addon/matriz-controles-por-risco', '651'),
                exact: true,
                sidebar: "sbdToeSidebar"
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/monitorizacao-operacoes/addon/metricas-indicadores',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/monitorizacao-operacoes/addon/metricas-indicadores', '70a'),
                exact: true,
                sidebar: "sbdToeSidebar"
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/monitorizacao-operacoes/addon/monitorizacao-resposta',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/monitorizacao-operacoes/addon/monitorizacao-resposta', '68f'),
                exact: true,
                sidebar: "sbdToeSidebar"
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/monitorizacao-operacoes/canon/ameacas-mitigadas',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/monitorizacao-operacoes/canon/ameacas-mitigadas', 'f51'),
                exact: true
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/monitorizacao-operacoes/canon/aplicacao-lifecycle',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/monitorizacao-operacoes/canon/aplicacao-lifecycle', 'af5'),
                exact: true,
                sidebar: "sbdToeSidebar"
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/monitorizacao-operacoes/canon/casos-praticos-monitorizacao',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/monitorizacao-operacoes/canon/casos-praticos-monitorizacao', 'eb3'),
                exact: true
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/monitorizacao-operacoes/canon/checklist-revisao',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/monitorizacao-operacoes/canon/checklist-revisao', '0ec'),
                exact: true
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/monitorizacao-operacoes/canon/maturidade',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/monitorizacao-operacoes/canon/maturidade', '26d'),
                exact: true
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/monitorizacao-operacoes/canon/policies-monitorizacao-operacoes',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/monitorizacao-operacoes/canon/policies-monitorizacao-operacoes', 'cb7'),
                exact: true
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/monitorizacao-operacoes/canon/rastreabilidade',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/monitorizacao-operacoes/canon/rastreabilidade', '685'),
                exact: true
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/monitorizacao-operacoes/canon/recomendacoes-avancadas',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/monitorizacao-operacoes/canon/recomendacoes-avancadas', 'ae1'),
                exact: true
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/monitorizacao-operacoes/intro',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/monitorizacao-operacoes/intro', '512'),
                exact: true,
                sidebar: "sbdToeSidebar"
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/rastreabilidade_global',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/rastreabilidade_global', 'ad9'),
                exact: true
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/requisitos-seguranca/',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/requisitos-seguranca/', '4c4'),
                exact: true
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/requisitos-seguranca/addon/catalogo-requisitos',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/requisitos-seguranca/addon/catalogo-requisitos', '31c'),
                exact: true,
                sidebar: "sbdToeSidebar"
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/requisitos-seguranca/addon/catalogo-requisitos',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/requisitos-seguranca/addon/catalogo-requisitos', '478'),
                exact: true,
                sidebar: "sbdToeSidebar"
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/requisitos-seguranca/addon/criterios-aceitacao',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/requisitos-seguranca/addon/criterios-aceitacao', '195'),
                exact: true,
                sidebar: "sbdToeSidebar"
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/requisitos-seguranca/addon/exemplos-aplicacao',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/requisitos-seguranca/addon/exemplos-aplicacao', 'fa9'),
                exact: true,
                sidebar: "sbdToeSidebar"
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/requisitos-seguranca/addon/gestao-excecoes',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/requisitos-seguranca/addon/gestao-excecoes', '17b'),
                exact: true,
                sidebar: "sbdToeSidebar"
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/requisitos-seguranca/addon/lista-requisitos-base',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/requisitos-seguranca/addon/lista-requisitos-base', '2a6'),
                exact: true,
                sidebar: "sbdToeSidebar"
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/requisitos-seguranca/addon/matriz-controlos-por-risco',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/requisitos-seguranca/addon/matriz-controlos-por-risco', '1f6'),
                exact: true,
                sidebar: "sbdToeSidebar"
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/requisitos-seguranca/addon/plano-validacao',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/requisitos-seguranca/addon/plano-validacao', '4da'),
                exact: true,
                sidebar: "sbdToeSidebar"
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/requisitos-seguranca/addon/rastreabilidade-controlo',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/requisitos-seguranca/addon/rastreabilidade-controlo', '503'),
                exact: true,
                sidebar: "sbdToeSidebar"
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/requisitos-seguranca/addon/rastreabilidade-frameworks',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/requisitos-seguranca/addon/rastreabilidade-frameworks', '88e'),
                exact: true,
                sidebar: "sbdToeSidebar"
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/requisitos-seguranca/addon/taxonomia-rastreabilidade',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/requisitos-seguranca/addon/taxonomia-rastreabilidade', '592'),
                exact: true,
                sidebar: "sbdToeSidebar"
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/requisitos-seguranca/addon/validacao-requisitos',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/requisitos-seguranca/addon/validacao-requisitos', '1ea'),
                exact: true,
                sidebar: "sbdToeSidebar"
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/requisitos-seguranca/aplicacao-lifecycle',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/requisitos-seguranca/aplicacao-lifecycle', 'da4'),
                exact: true,
                sidebar: "sbdToeSidebar"
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/requisitos-seguranca/canon/ameacas-mitigadas',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/requisitos-seguranca/canon/ameacas-mitigadas', 'fa5'),
                exact: true
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/requisitos-seguranca/canon/checklist-revisao',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/requisitos-seguranca/canon/checklist-revisao', '10c'),
                exact: true
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/requisitos-seguranca/canon/maturidade',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/requisitos-seguranca/canon/maturidade', 'fbb'),
                exact: true
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/requisitos-seguranca/canon/policies-relevantes',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/requisitos-seguranca/canon/policies-relevantes', '325'),
                exact: true
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/requisitos-seguranca/canon/rastreabilidade',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/requisitos-seguranca/canon/rastreabilidade', 'a46'),
                exact: true
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/requisitos-seguranca/canon/recomendacoes-avancadas',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/requisitos-seguranca/canon/recomendacoes-avancadas', 'd94'),
                exact: true
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/requisitos-seguranca/intro',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/requisitos-seguranca/intro', 'ecf'),
                exact: true,
                sidebar: "sbdToeSidebar"
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/requisitos-seguranca/rationale-catalogo',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/requisitos-seguranca/rationale-catalogo', 'c6f'),
                exact: true
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/testes-seguranca/',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/testes-seguranca/', '53c'),
                exact: true
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/testes-seguranca/addon/cobertura-e-priorizacao',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/testes-seguranca/addon/cobertura-e-priorizacao', '474'),
                exact: true,
                sidebar: "sbdToeSidebar"
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/testes-seguranca/addon/dast',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/testes-seguranca/addon/dast', '6c3'),
                exact: true,
                sidebar: "sbdToeSidebar"
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/testes-seguranca/addon/estudo-caso',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/testes-seguranca/addon/estudo-caso', '1d7'),
                exact: true,
                sidebar: "sbdToeSidebar"
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/testes-seguranca/addon/feedback-equipa',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/testes-seguranca/addon/feedback-equipa', 'ece'),
                exact: true,
                sidebar: "sbdToeSidebar"
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/testes-seguranca/addon/fuzzing',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/testes-seguranca/addon/fuzzing', '1c9'),
                exact: true,
                sidebar: "sbdToeSidebar"
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/testes-seguranca/addon/gestao-findings',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/testes-seguranca/addon/gestao-findings', '745'),
                exact: true,
                sidebar: "sbdToeSidebar"
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/testes-seguranca/addon/iast',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/testes-seguranca/addon/iast', 'd70'),
                exact: true,
                sidebar: "sbdToeSidebar"
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/testes-seguranca/addon/integracao-pipeline',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/testes-seguranca/addon/integracao-pipeline', 'a8a'),
                exact: true,
                sidebar: "sbdToeSidebar"
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/testes-seguranca/addon/intro',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/testes-seguranca/addon/intro', 'd3e'),
                exact: true,
                sidebar: "sbdToeSidebar"
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/testes-seguranca/addon/pen-testing',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/testes-seguranca/addon/pen-testing', '996'),
                exact: true,
                sidebar: "sbdToeSidebar"
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/testes-seguranca/addon/sast',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/testes-seguranca/addon/sast', 'e88'),
                exact: true,
                sidebar: "sbdToeSidebar"
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/testes-seguranca/addon/validacao-regressao',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/testes-seguranca/addon/validacao-regressao', '8d2'),
                exact: true,
                sidebar: "sbdToeSidebar"
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/testes-seguranca/canon/ameacas-mitigadas',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/testes-seguranca/canon/ameacas-mitigadas', '75f'),
                exact: true
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/testes-seguranca/canon/aplicacao-lifecycle',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/testes-seguranca/canon/aplicacao-lifecycle', 'c41'),
                exact: true,
                sidebar: "sbdToeSidebar"
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/testes-seguranca/canon/checklist-revisao',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/testes-seguranca/canon/checklist-revisao', '685'),
                exact: true
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/testes-seguranca/canon/maturidade',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/testes-seguranca/canon/maturidade', '8bf'),
                exact: true
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/testes-seguranca/canon/policies-relevantes',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/testes-seguranca/canon/policies-relevantes', '323'),
                exact: true
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/testes-seguranca/canon/rastreabilidade',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/testes-seguranca/canon/rastreabilidade', 'e27'),
                exact: true
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/testes-seguranca/canon/recomendacoes-avancadas',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/testes-seguranca/canon/recomendacoes-avancadas', '2a1'),
                exact: true
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/testes-seguranca/intro',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/testes-seguranca/intro', '487'),
                exact: true,
                sidebar: "sbdToeSidebar"
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/threat-modeling/addon/exemplo-privacidade',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/threat-modeling/addon/exemplo-privacidade', '385'),
                exact: true,
                sidebar: "sbdToeSidebar"
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/threat-modeling/addon/exemplos-aplicacao',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/threat-modeling/addon/exemplos-aplicacao', '892'),
                exact: true,
                sidebar: "sbdToeSidebar"
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/threat-modeling/addon/integracao-iriusrisk',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/threat-modeling/addon/integracao-iriusrisk', '036'),
                exact: true,
                sidebar: "sbdToeSidebar"
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/threat-modeling/addon/mapeamento-threats-requisitos',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/threat-modeling/addon/mapeamento-threats-requisitos', '7c2'),
                exact: true,
                sidebar: "sbdToeSidebar"
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/threat-modeling/addon/metodologias-e-ferramentas',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/threat-modeling/addon/metodologias-e-ferramentas', 'fdd'),
                exact: true,
                sidebar: "sbdToeSidebar"
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/threat-modeling/addon/threat-modeling-ci',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/threat-modeling/addon/threat-modeling-ci', 'a8d'),
                exact: true,
                sidebar: "sbdToeSidebar"
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/threat-modeling/addon/validacao-arquitetura',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/threat-modeling/addon/validacao-arquitetura', '328'),
                exact: true,
                sidebar: "sbdToeSidebar"
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/threat-modeling/canon/ameacas-mitigadas',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/threat-modeling/canon/ameacas-mitigadas', '683'),
                exact: true
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/threat-modeling/canon/aplicacao-lifecycle',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/threat-modeling/canon/aplicacao-lifecycle', '1ad'),
                exact: true,
                sidebar: "sbdToeSidebar"
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/threat-modeling/canon/checklist-revisao',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/threat-modeling/canon/checklist-revisao', 'ed1'),
                exact: true
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/threat-modeling/canon/maturidade',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/threat-modeling/canon/maturidade', 'bfb'),
                exact: true
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/threat-modeling/canon/policies-relevantes',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/threat-modeling/canon/policies-relevantes', '0e8'),
                exact: true
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/threat-modeling/canon/rastreabilidade',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/threat-modeling/canon/rastreabilidade', '777'),
                exact: true
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/threat-modeling/canon/rastreabilidade',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/threat-modeling/canon/rastreabilidade', '27e'),
                exact: true
              },
              {
                path: '/sbd-theory-of-everything/sbd-toe/threat-modeling/intro',
                component: ComponentCreator('/sbd-theory-of-everything/sbd-toe/threat-modeling/intro', '530'),
                exact: true,
                sidebar: "sbdToeSidebar"
              }
            ]
          }
        ]
      }
    ]
  },
  {
    path: '/sbd-theory-of-everything/supply-chain',
    component: ComponentCreator('/sbd-theory-of-everything/supply-chain', '1aa'),
    routes: [
      {
        path: '/sbd-theory-of-everything/supply-chain',
        component: ComponentCreator('/sbd-theory-of-everything/supply-chain', '0f3'),
        routes: [
          {
            path: '/sbd-theory-of-everything/supply-chain',
            component: ComponentCreator('/sbd-theory-of-everything/supply-chain', 'a6a'),
            routes: [
              {
                path: '/sbd-theory-of-everything/supply-chain/01-1.-introdução',
                component: ComponentCreator('/sbd-theory-of-everything/supply-chain/01-1.-introdução', 'edd'),
                exact: true,
                sidebar: "defaultSidebar"
              },
              {
                path: '/sbd-theory-of-everything/supply-chain/02-2.-enquadramento-estratégico-e-de-risco',
                component: ComponentCreator('/sbd-theory-of-everything/supply-chain/02-2.-enquadramento-estratégico-e-de-risco', 'd9b'),
                exact: true,
                sidebar: "defaultSidebar"
              },
              {
                path: '/sbd-theory-of-everything/supply-chain/03-3.-princípios-fundamentais-da-segurança-na-cadeia-de-fornecimento',
                component: ComponentCreator('/sbd-theory-of-everything/supply-chain/03-3.-princípios-fundamentais-da-segurança-na-cadeia-de-fornecimento', '1a8'),
                exact: true,
                sidebar: "defaultSidebar"
              },
              {
                path: '/sbd-theory-of-everything/supply-chain/04-4.-mapeamento-por-fase-do-ciclo-de-vida-do-software',
                component: ComponentCreator('/sbd-theory-of-everything/supply-chain/04-4.-mapeamento-por-fase-do-ciclo-de-vida-do-software', '43d'),
                exact: true,
                sidebar: "defaultSidebar"
              },
              {
                path: '/sbd-theory-of-everything/supply-chain/05-5.-modelos-de-governação-e-responsabilidade',
                component: ComponentCreator('/sbd-theory-of-everything/supply-chain/05-5.-modelos-de-governação-e-responsabilidade', '5a4'),
                exact: true,
                sidebar: "defaultSidebar"
              },
              {
                path: '/sbd-theory-of-everything/supply-chain/06-6.-automação-e-integração-com-o-pipeline',
                component: ComponentCreator('/sbd-theory-of-everything/supply-chain/06-6.-automação-e-integração-com-o-pipeline', '529'),
                exact: true,
                sidebar: "defaultSidebar"
              },
              {
                path: '/sbd-theory-of-everything/supply-chain/07-7.-ferramentas-recomendadas-por-categoria',
                component: ComponentCreator('/sbd-theory-of-everything/supply-chain/07-7.-ferramentas-recomendadas-por-categoria', '269'),
                exact: true,
                sidebar: "defaultSidebar"
              },
              {
                path: '/sbd-theory-of-everything/supply-chain/08-8.-casos-de-uso-e-exemplos-práticos',
                component: ComponentCreator('/sbd-theory-of-everything/supply-chain/08-8.-casos-de-uso-e-exemplos-práticos', 'ec6'),
                exact: true,
                sidebar: "defaultSidebar"
              },
              {
                path: '/sbd-theory-of-everything/supply-chain/09-9.-integração-com-o-programa-security-by-design-(sbd-toe)',
                component: ComponentCreator('/sbd-theory-of-everything/supply-chain/09-9.-integração-com-o-programa-security-by-design-(sbd-toe)', '77c'),
                exact: true,
                sidebar: "defaultSidebar"
              },
              {
                path: '/sbd-theory-of-everything/supply-chain/10-10.-referências-e-normativos',
                component: ComponentCreator('/sbd-theory-of-everything/supply-chain/10-10.-referências-e-normativos', 'af8'),
                exact: true,
                sidebar: "defaultSidebar"
              },
              {
                path: '/sbd-theory-of-everything/supply-chain/apêndices-práticos',
                component: ComponentCreator('/sbd-theory-of-everything/supply-chain/apêndices-práticos', '1db'),
                exact: true,
                sidebar: "defaultSidebar"
              },
              {
                path: '/sbd-theory-of-everything/supply-chain/intro',
                component: ComponentCreator('/sbd-theory-of-everything/supply-chain/intro', 'e07'),
                exact: true,
                sidebar: "defaultSidebar"
              },
              {
                path: '/sbd-theory-of-everything/supply-chain/licenciamento-e-termos-de-reutilização',
                component: ComponentCreator('/sbd-theory-of-everything/supply-chain/licenciamento-e-termos-de-reutilização', '7aa'),
                exact: true,
                sidebar: "defaultSidebar"
              }
            ]
          }
        ]
      }
    ]
  },
  {
    path: '/sbd-theory-of-everything/',
    component: ComponentCreator('/sbd-theory-of-everything/', '062'),
    exact: true
  },
  {
    path: '*',
    component: ComponentCreator('*'),
  },
];
