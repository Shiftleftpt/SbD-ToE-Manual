import React from 'react';
import clsx from 'clsx';
import Link from '@docusaurus/Link';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import Layout from '@theme/Layout';
import styles from './index.module.css';

function HomepageHeader() {
  const {siteConfig} = useDocusaurusContext();
  const introUrl = 'sbd-toe/sbd-manual/';

  return (
    <header className={clsx('hero', 'hero--primary', styles.slHero)}>
      <div className="container">
        <div className="text--center">
          <h1 className={styles.heroTitle}>Security by Design</h1>
          <p className={styles.heroTagline}>Theory of Everything</p>
          <div className={styles.ctaWrap}>
            <Link className="button button--lg button--secondary" to={introUrl}>
              Explorar o Manual →
            </Link>
          </div>
        </div>
      </div>
    </header>
  );
}

function SectionCards() {
  const cards = [
    {
      title: 'Theory of Everything',
      description: 'Visão global: princípios, governação e aplicação do SbD-ToE.',
      to: '/sbd-toe/teory-of-everything/intro',
      icon: '📘',
    },
    {
      title: 'Como usar este manual',
      description: 'Guia prático para navegar e aplicar o conteúdo na organização.',
      to: '/sbd-toe/how-to-manual/como-usar-este-manual',
      icon: '🧭',
    },
    {
      title: 'Cross-check normativo',
      description: 'Como o SbD-ToE cobre (ou liga a) NIS2, DORA, ISO/IEC 27001, SSDF, SLSA, etc.',
      to: '/sbd-toe/cross-check-normativo/intro',
      icon: '🏛️',
    },
    {
      title: 'Políticas globais do manual',
      description: 'Conjunto de políticas organizacionais transversais ao SbD-ToE.',
      to: '/sbd-toe/policies-globals/intro',
      icon: '📜',
    },
  ];

  return (
    <section className={styles.cardsSection}>
      <div className="container">
        <h2 className={styles.cardsTitle}>Capítulos e temas</h2>
        <div className={clsx('row', styles.cardsGrid)}>
          {cards.map((c, idx) => (
            // menos espaço vertical entre cards
            <div key={idx} className="col col--6 margin-bottom--md">
              <div className={clsx('card', styles.card)}>
                <div className="card__header">
                  <h3>{c.icon} {c.title}</h3>
                </div>
                <div className="card__body">
                  <p>{c.description}</p>
                </div>
                <div className="card__footer">
                  <Link className="button button--primary button--sm" to={c.to}>
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
  const features = [
    {
      title: 'A “cola” entre standards',
      description: <>Agrega OWASP, NIST SSDF, SLSA, MITRE e outros, com aplicação pragmática.</>,
      icon: '🧩',
    },
    {
      title: 'Foco no que fazer (e quando)',
      description: <>Prescritivo, com responsabilidades, exemplos, checklists e ações por fase do SDLC.</>,
      icon: '📋',
    },
    {
      title: 'Desenhado para adaptar',
      description: <>Aplicável a contextos cloud-native, DevSecOps, pipelines tradicionais e modelos híbridos.</>,
      icon: '⚙️',
    },
  ];

  return (
    <section className={styles.features}>
      <div className="container">
        <h2 className={styles.cardsTitle}></h2>
        <div className="row">
          {features.map((f, idx) => (
            <div key={idx} className="col col--4">
              <div className="text--center padding-horiz--md">
                <h3>{f.icon} {f.title}</h3>
                <p>{f.description}</p>
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
        <SectionFeatures />
        <SectionCards />
      </main>
    </Layout>
  );
}
