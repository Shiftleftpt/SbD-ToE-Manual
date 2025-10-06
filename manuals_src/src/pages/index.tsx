import React from 'react';
import clsx from 'clsx';
import Link from '@docusaurus/Link';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import useBaseUrl from '@docusaurus/useBaseUrl';
import Layout from '@theme/Layout';
import styles from './index.module.css';

function HomepageHeader() {
  const {siteConfig} = useDocusaurusContext();
  const introUrl = useBaseUrl('/sbd-toe/intro');  // Corrigido aqui
  return (
    <header className={clsx('hero hero--primary', styles.heroBanner)}>
      <div className="container">
        <h1 className="hero__title">{siteConfig.title}</h1>
        <p className="hero__subtitle">{siteConfig.tagline}</p>
        <div className={styles.buttons}>
          <Link className="button button--secondary button--lg" to={introUrl}>
            Explorar o Manual →
          </Link>
        </div>
      </div>
    </header>
  );
}

function SectionCards() {
  const temas = [
    {
      title: 'Security by Design – Manual Principal',
      description: 'A base para todas as práticas. Do risco à operação, passo a passo.',
      to: useBaseUrl('/sbd-toe/intro'),  // Corrigido aqui
      icon: '📘',
    },
    {
      title: 'Supply Chain Security',
      description: 'Como proteger a cadeia de fornecimento – práticas, políticas e ferramentas.',
      to: useBaseUrl('/supply-chain/intro'),  // Corrigido aqui
      icon: '🔗',
    },
    {
      title: 'Segurança em IA',
      description: 'Boas práticas e controlos para o uso e desenvolvimento com IA.',
      to: useBaseUrl('/ia/intro'),  // Corrigido aqui
      icon: '🤖',
    },
    {
      title: 'Ameaças e Mitigação',
      description: 'Como o Security by Design reduz riscos reais no desenvolvimento.',
      to: useBaseUrl('/ameacas/intro'),  // Corrigido aqui
      icon: '🛡️',
    },
  ];

  return (
    <section className={styles.cardsSection}>
      <div className="container">
        <h2 className={styles.cardsTitle}>Capítulos e Temas</h2>
        <div className={clsx('row', styles.cardsGrid)}>
          {temas.map((tema, idx) => (
            <div key={idx} className="col col--6 margin-bottom--lg">
              <div className={clsx('card', styles.card)}>
                <div className="card__header">
                  <h3>{tema.icon} {tema.title}</h3>
                </div>
                <div className="card__body">
                  <p>{tema.description}</p>
                </div>
                <div className="card__footer">
                  <Link className="button button--primary button--sm" to={tema.to}>
                    Ler mais →
                  </Link>
                </div>
              </div>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}

function SectionFeatures() {
  const FeatureList = [
    {
      title: 'A "cola" entre todos os standards',
      description: (
        <>
          Reúne as melhores práticas de OWASP, NIST, SLSA, MITRE e outras fontes — criando uma abordagem agregadora e pragmática para aplicar Security by Design.
        </>
      ),
      icon: '🧩',
    },
    {
      title: 'Foco no que fazer (e quando)',
      description: (
        <>
          Abordagem prescritiva com responsabilidades claras, exemplos práticos, checklists e ações por fase do ciclo de vida do software.
        </>
      ),
      icon: '📋',
    },
    {
      title: 'Desenhado para ser adaptado',
      description: (
        <>
          Cada organização pode aplicar os conceitos ao seu contexto — seja cloud-native, DevSecOps, pipelines tradicionais ou modelos híbridos.
        </>
      ),
      icon: '⚙️',
    },
  ];

  return (
    <section className={styles.features}>
      <div className="container">
        <h2 className={styles.cardsTitle}>O que torna este manual diferente?</h2>
        <div className="row">
          {FeatureList.map((feature, idx) => (
            <div key={idx} className="col col--4">
              <div className="text--center padding-horiz--md">
                <h3>{feature.icon} {feature.title}</h3>
                <p>{feature.description}</p>
              </div>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}

export default function Home(): JSX.Element {
  const {siteConfig} = useDocusaurusContext();
  return (
    <Layout
      title={`Início – ${siteConfig.title}`}
      description="Manual prático e aberto para aplicar Security by Design em organizações modernas.">
      <HomepageHeader />
      <main>
        <SectionCards />
        <SectionFeatures />
      </main>
    </Layout>
  );
}
