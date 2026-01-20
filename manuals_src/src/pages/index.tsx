import React from 'react';
import clsx from 'clsx';
import Link from '@docusaurus/Link';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import Layout from '@theme/Layout';
import styles from './index.module.css';

// URL central para o Capítulo 00 / Theory of Everything
// (se mudares o slug para 'theory-of-everything', atualizas aqui apenas)
const toeIntroUrl = 'sbd-toe/teory-of-everything/intro';

/* ===================== HERO ===================== */

function HomepageHeader() {
  return (
    <header className={clsx('hero', 'hero--primary', styles.slHero)}>
      <div className="container">
        <div className="text--center">
          <h1 className={styles.heroTitle}>
            Security by Design - Theory of Everything
          </h1>
          <p
            className={styles.heroTagline}
            role="doc-subtitle"
          >
            Um modelo unificado para pensar, desenhar e operar segurança em
            desenvolvimento de software.
          </p>
          <p
            className="hero__subtitle"
            style={{
              marginBottom: '1.75rem',
              fontSize: '1.05rem',
              color: 'var(--ifm-color-emphasis-700)',
            }}
          >
            O SbD–ToE liga regulamentos europeus, normas técnicas, frameworks de
            maturidade, ameaças reais e engenharia de software num manual
            prescritivo, reutilizável e proporcional ao risco.
          </p>

        </div>
      </div>
    </header>
  );
}

/* ===================== DIAGRAMA CENTRADO ===================== */

function ToeDiagramSection() {
  return (
    <section className={styles.features}>
      <div className={clsx('container', styles.diagramContainer)}>
        <div className="text--center">
          {/* Diagrama clicável para o Capítulo 00 / ToE */}
          <Link to={toeIntroUrl} className={styles.diagramLink}>
            <ToeDiagram />
          </Link>
        </div>
      </div>
    </section>
  );
}

function ToeDiagram() {
  return (
    <div className={styles.diagramWrapper}>
      <svg
        viewBox="0 -20 1407 744"
        role="img"
        aria-label="Diagrama conceptual da Theory of Everything"
        className={styles.diagramSvg}
        preserveAspectRatio="xMidYMid meet"
      >
        <defs>
          <radialGradient id="toeGlow" cx="50%" cy="50%" r="50%">
            <stop
              offset="0%"
              stopColor="var(--ifm-color-primary)"
              stopOpacity="0.18"
            />
            <stop
              offset="60%"
              stopColor="var(--ifm-color-primary)"
              stopOpacity="0.05"
            />
            <stop offset="100%" stopColor="transparent" stopOpacity="0" />
          </radialGradient>
          <style>{`
            .toe-home-title { font-weight: bold; font-size: 31px; fill: currentColor; }
            .toe-home-text { font-size: 24px; fill: var(--ifm-color-emphasis-700); }
          `}</style>
        </defs>

        {/* halo */}
        <circle cx="704" cy="353" r="185" fill="url(#toeGlow)" />

        {/* anel tracejado — 3 eixos */}
        <circle
          cx="704"
          cy="353"
          r="205"
          fill="none"
          stroke="var(--ifm-color-emphasis-400)"
          strokeWidth="3.6"
          strokeDasharray="6 6"
        />

        {/* núcleo */}
        <circle
          cx="704"
          cy="353"
          r="85"
          fill="var(--ifm-background-surface-color)"
          stroke="var(--ifm-color-primary)"
          strokeWidth="3.6"
        />
        <text
          x="704"
          y="347"
          textAnchor="middle"
          fontSize="22"
          fontWeight="bold"
          fill="currentColor"
        >
          Security by Design
        </text>
        <text
          x="704"
          y="362"
          textAnchor="middle"
          fontSize="19"
          fill="currentColor"
        >
          Theory of Everything
        </text>

        {/* Top-Down satélite */}
        <circle
          cx="704"
          cy="148"
          r="47"
          fill="var(--ifm-background-surface-color)"
        />
        <circle
          cx="704"
          cy="148"
          r="47"
          fill="none"
          stroke="var(--ifm-color-emphasis-400)"
        />
        <text
          x="704"
          y="70"
          textAnchor="middle"
          className="toe-home-title"
        >
          Top-Down
        </text>
        <text
          x="704"
          y="92"
          textAnchor="middle"
          className="toe-home-text"
        >
          Normas &amp; Regulação
        </text>
        <line
          x1="704"
          y1="195"
          x2="704"
          y2="268"
          stroke="var(--ifm-color-emphasis-400)"
          strokeWidth="3.6"
        />

        {/* Bottom-Up satélite */}
        <circle
          cx="704"
          cy="558"
          r="47"
          fill="var(--ifm-background-surface-color)"
        />
        <circle
          cx="704"
          cy="558"
          r="47"
          fill="none"
          stroke="var(--ifm-color-emphasis-400)"
        />
        <text
          x="704"
          y="635"
          textAnchor="middle"
          className="toe-home-title"
        >
          Bottom-Up
        </text>
        <text
          x="704"
          y="657"
          textAnchor="middle"
          className="toe-home-text"
        >
          Ameaças &amp; Incidentes
        </text>
        <line
          x1="704"
          y1="511"
          x2="704"
          y2="438"
          stroke="var(--ifm-color-emphasis-400)"
          strokeWidth="3.6"
        />

        {/* Engineering satélite */}
        <circle
          cx="499"
          cy="353"
          r="47"
          fill="var(--ifm-background-surface-color)"
        />
        <circle
          cx="499"
          cy="353"
          r="47"
          fill="none"
          stroke="var(--ifm-color-emphasis-400)"
        />
        <text
          x="420"
          y="345"
          textAnchor="end"
          className="toe-home-title"
        >
          Engineering
        </text>
        <text
          x="420"
          y="365"
          textAnchor="end"
          className="toe-home-text"
        >
          Execução &amp; Ciclo de vida
        </text>
        <line
          x1="546"
          y1="353"
          x2="619"
          y2="353"
          stroke="var(--ifm-color-emphasis-400)"
          strokeWidth="3.6"
        />
      </svg>

      <p
        style={{
          fontSize: '0.9rem',
          marginTop: '0.75rem',
          maxWidth: 520,
          marginInline: 'auto',
        }}
      >
        O SbD–ToE é o núcleo onde convergem normas, ameaças e engenharia.
        A partir deste centro, cada capítulo do manual desdobra a visão em
        práticas e controlos concretos.
      </p>
    </div>
  );
}

/* ===================== 2 CARDS PRINCIPAIS ===================== */

function SectionCards() {
  const manualUrl = 'sbd-toe/sbd-manual/';
  const crossCheckUrl = 'sbd-toe/cross-check-normativo/intro';

  const cards = [
    {
      title: 'Manual SbD–ToE',
      description:
        'Capítulos 01–14. Corpo principal do manual, organizado por tema técnico ao longo do ciclo de vida.',
      to: manualUrl,
      icon: '📘',
    },
    {
      title: 'Cross-check normativo',
      description:
        'Matriz que mostra como o SbD–ToE responde a NIS2, DORA, CRA, ISO 27001/27034 e outras referências.',
      to: crossCheckUrl,
      icon: '🏛️',
    },
  ];

  const colSizeClass = cards.length === 2 ? 'col col--6' : 'col col--4';

  return (
    <section className={styles.cardsSection}>
      <div className="container">
        <div className={clsx('row', styles.cardsGrid)}>
          {cards.map((c, idx) => (
            <div key={idx} className={clsx(colSizeClass, 'margin-bottom--md')}>
              <div className={clsx('card', styles.card)}>
                <div className="card__header">
                  <h3>
                    {c.icon} {c.title}
                  </h3>
                </div>
                <div className="card__body">
                  <p>{c.description}</p>
                </div>
                <div className="card__footer">
                  <Link className="button button--primary button--sm" to={c.to}>
                    Abrir →
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

/* ===================== ROOT LAYOUT ===================== */

export default function Home(): JSX.Element {
  const {siteConfig} = useDocusaurusContext();
  return (
    <Layout
      title={`Início - ${siteConfig.title}`}
      description="Security by Design - Theory of Everything. Manual prático, aberto e prescritivo para aplicar segurança por desenho em organizações modernas."
    >
      <HomepageHeader />
      <main>
        <ToeDiagramSection />
        <SectionCards />
      </main>
    </Layout>
  );
}
