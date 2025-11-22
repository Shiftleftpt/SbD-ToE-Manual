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
      <div className="container">
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
    <div
      style={{
        textAlign: 'center',
        padding: '0.5rem 0',
        color: 'var(--ifm-font-color-base)', // para o SVG herdar a cor de texto do tema
      }}
    >
      <svg
        viewBox="0 0 600 260"
        role="img"
        aria-label="Diagrama conceptual da Theory of Everything"
        style={{
          maxWidth: '720px', // ligeiramente maior
          width: '100%',
          height: 'auto',
        }}
        preserveAspectRatio="xMidYMid meet"
      >
        <defs>
          <radialGradient id="toeGlow" cx="50%" cy="50%" r="50%">
            <stop
              offset="0%"
              stopColor="var(--ifm-color-primary)"
              stopOpacity="0.25"
            />
            <stop
              offset="60%"
              stopColor="var(--ifm-color-primary)"
              stopOpacity="0.06"
            />
            <stop offset="100%" stopColor="transparent" stopOpacity="0" />
          </radialGradient>
        </defs>

        {/* halo */}
        <circle cx="300" cy="130" r="110" fill="url(#toeGlow)" />

        {/* anel */}
        <circle
          cx="300"
          cy="130"
          r="90"
          fill="none"
          stroke="var(--ifm-color-emphasis-400)"
          strokeWidth="1.5"
          strokeDasharray="4 3"
        />

        {/* núcleo */}
        <circle
          cx="300"
          cy="130"
          r="48"
          fill="var(--ifm-background-surface-color)"
          stroke="var(--ifm-color-primary)"
          strokeWidth="1.5"
        />
        <text
          x="300"
          y="124"
          textAnchor="middle"
          fontSize="12"
          fontWeight="bold"
          fill="currentColor"
        >
          Security by Design
        </text>
        <text
          x="300"
          y="140"
          textAnchor="middle"
          fontSize="11"
          fill="currentColor"
        >
          Theory of Everything
        </text>

        {/* quatro “órbitas” */}
        {/* top */}
        <circle
          cx="300"
          cy="40"
          r="18"
          fill="var(--ifm-background-surface-color)"
        />
        <circle
          cx="300"
          cy="40"
          r="18"
          fill="none"
          stroke="var(--ifm-color-emphasis-400)"
        />
        <text
          x="300"
          y="38"
          textAnchor="middle"
          fontSize="9"
          fill="currentColor"
        >
          Normativos
        </text>
        <text
          x="300"
          y="48"
          textAnchor="middle"
          fontSize="9"
          fill="currentColor"
        >
          &amp; Regulação
        </text>

        {/* right */}
        <circle
          cx="500"
          cy="130"
          r="18"
          fill="var(--ifm-background-surface-color)"
        />
        <circle
          cx="500"
          cy="130"
          r="18"
          fill="none"
          stroke="var(--ifm-color-emphasis-400)"
        />
        <text
          x="500"
          y="128"
          textAnchor="middle"
          fontSize="9"
          fill="currentColor"
        >
          Normas &
        </text>
        <text
          x="500"
          y="138"
          textAnchor="middle"
          fontSize="9"
          fill="currentColor"
        >
          Frameworks
        </text>

        {/* bottom */}
        <circle
          cx="300"
          cy="220"
          r="18"
          fill="var(--ifm-background-surface-color)"
        />
        <circle
          cx="300"
          cy="220"
          r="18"
          fill="none"
          stroke="var(--ifm-color-emphasis-400)"
        />
        <text
          x="300"
          y="218"
          textAnchor="middle"
          fontSize="9"
          fill="currentColor"
        >
          Ameaças
        </text>
        <text
          x="300"
          y="228"
          textAnchor="middle"
          fontSize="9"
          fill="currentColor"
        >
          &amp; incidentes
        </text>

        {/* left */}
        <circle
          cx="100"
          cy="130"
          r="18"
          fill="var(--ifm-background-surface-color)"
        />
        <circle
          cx="100"
          cy="130"
          r="18"
          fill="none"
          stroke="var(--ifm-color-emphasis-400)"
        />
        <text
          x="100"
          y="128"
          textAnchor="middle"
          fontSize="9"
          fill="currentColor"
        >
          SDLC,
        </text>
        <text
          x="100"
          y="138"
          textAnchor="middle"
          fontSize="9"
          fill="currentColor"
        >
          pipelines
        </text>

        {/* ligações */}
        <line
          x1="300"
          y1="82"
          x2="300"
          y2="58"
          stroke="var(--ifm-color-emphasis-400)"
          strokeWidth="1"
        />
        <line
          x1="348"
          y1="130"
          x2="478"
          y2="130"
          stroke="var(--ifm-color-emphasis-400)"
          strokeWidth="1"
        />
        <line
          x1="300"
          y1="178"
          x2="300"
          y2="202"
          stroke="var(--ifm-color-emphasis-400)"
          strokeWidth="1"
        />
        <line
          x1="252"
          y1="130"
          x2="122"
          y2="130"
          stroke="var(--ifm-color-emphasis-400)"
          strokeWidth="1"
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
        O SbD–ToE é o núcleo onde convergem normativos, frameworks, ameaças e
        engenharia. A partir deste centro, cada capítulo do manual desdobra a
        visão em práticas e controlos concretos.
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
