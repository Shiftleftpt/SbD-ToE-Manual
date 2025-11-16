import React from 'react';
import clsx from 'clsx';
import Link from '@docusaurus/Link';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import Layout from '@theme/Layout';
import styles from './index.module.css';

function HomepageHeader() {
  const {siteConfig} = useDocusaurusContext();
  const introUrl = 'sbd-toe/sbd-manual/classificacao-aplicacoes/intro';

  return (
    <header className={clsx('hero', 'hero--primary', styles.slHero)}>
      <div className="container">
        <div className="text--center">
          <h1 className={styles.heroTitle}>Security by Design</h1>
           <p className={styles.heroTagline} role="doc-subtitle" aria-describedby="hero-cta">
            Theory of <strong>Everything</strong>
          </p>
          <p className="hero__subtitle" style={{ marginBottom: '1.5rem', fontSize: '1.1rem', color: 'var(--ifm-color-emphasis-700)' }}>
            Manual prático de segurança aplicacional para todo o ciclo de vida de desenvolvimento
          </p>
          <div className={styles.ctaWrap}>
            <Link className="button button--lg button--secondary" to={introUrl}>
              Começar pelo Capítulo 01 →
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
      title: 'Manual SbD-ToE (Cap. 01-14)',
      description: '14 capítulos práticos cobrindo todo o ciclo de vida de segurança aplicacional, desde classificação até operações.',
      to: '/sbd-toe/sbd-manual/classificacao-aplicacoes/intro',
      icon: '📘',
    },
    {
      title: 'Theory of Everything',
      description: 'Fundamentos, filosofia e aplicação do modelo. Como o SbD-ToE unifica frameworks e normas.',
      to: '/sbd-toe/teory-of-everything/intro',
      icon: '🧭',
    },
    {
      title: 'Cross-check normativo',
      description: 'Mapeamento para DORA, NIS2, CRA, GDPR, ISO 27001 e outros frameworks regulatórios.',
      to: '/sbd-toe/cross-check-normativo/intro',
      icon: '🏛️',
    },
    {
      title: 'Como usar este manual',
      description: 'Guia de navegação, estrutura dos capítulos e cobertura de frameworks externos.',
      to: '/sbd-toe/how-to-manual/como-usar-este-manual',
      icon: '�',
    },
  ];

  return (
    <section className={styles.cardsSection}>
      <div className="container">
        <h2 className={styles.cardsTitle}>Explorar o manual</h2>
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
      title: '14 capítulos basilares + addons',
      description: <>Cobertura completa do ciclo de vida: classificação, requisitos, threat modeling, arquitetura, dependências, desenvolvimento, CI/CD, IaC, containers, testes, deploy, operações, formação e governança.</>,
      icon: '📋',
    },
    {
      title: 'Baseado em frameworks estabelecidos',
      description: <>Agrega OWASP SAMM, NIST SSDF, SLSA, BSIMM, MITRE ATT&CK e catálogos de ameaças (STRIDE, CWE, CAPEC) numa abordagem unificada e pragmática.</>,
      icon: '🧩',
    },
    {
      title: 'Proporcional ao risco (L1/L2/L3)',
      description: <>Controlos ajustados à criticidade da aplicação. Requisitos mínimos para L1, essenciais para L2, rigorosos para L3. Evita sobreproteção e subproteção.</>,
      icon: '⚖️',
    },
  ];

  return (
    <section className={styles.features}>
      <div className="container">
        <h2 className={styles.cardsTitle}>O que encontras aqui</h2>
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
      title={`Início - ${siteConfig.title}`}
      description="Manual prático e aberto para aplicar Security by Design em organizações modernas.">
      <HomepageHeader />
      <main>
        <SectionFeatures />
        <SectionCards />
      </main>
    </Layout>
  );
}
