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
        viewBox="0 0 1407 704"
        role="img"
        aria-label="Diagrama conceptual da Theory of Everything"
        style={{
          maxWidth: '1690px',
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
            .toe-home-title { font-weight: bold; font-size: 27px; fill: currentColor; }
            .toe-home-text { font-size: 21px; fill: var(--ifm-color-emphasis-700); }
          `}</style>
        </defs>

        {/* halo */}
        <circle cx="704" cy="353" r="260" fill="url(#toeGlow)" />

        {/* anel — 5 satélites a 72° intervalo */}
        <circle
          cx="704"
          cy="353"
          r="224"
          fill="none"
          stroke="var(--ifm-color-emphasis-400)"
          strokeWidth="3.6"
          strokeDasharray="6 6"
        />

        {/* núcleo */}
        <circle
          cx="704"
          cy="353"
          r="113"
          fill="var(--ifm-background-surface-color)"
          stroke="var(--ifm-color-primary)"
          strokeWidth="3.6"
        />
        <text
          x="704"
          y="338"
          textAnchor="middle"
          fontSize="29"
          fontWeight="bold"
          fill="currentColor"
        >
          Security by Design
        </text>
        <text
          x="704"
          y="375"
          textAnchor="middle"
          fontSize="27"
          fill="currentColor"
        >
          Theory of Everything
        </text>

        {/* cinco satélites a 72° intervalo */}
        {/* Top (0°) */}
        <circle
          cx="704"
          cy="129"
          r="47"
          fill="var(--ifm-background-surface-color)"
        />
        <circle
          cx="704"
          cy="129"
          r="47"
          fill="none"
          stroke="var(--ifm-color-emphasis-400)"
        />
        <text
          x="704"
          y="120"
          textAnchor="middle"
          className="toe-home-title"
        >
          Normativos
        </text>
        <text
          x="704"
          y="149"
          textAnchor="middle"
          className="toe-home-text"
        >
          &amp; Regulação
        </text>

        {/* NE (72°) */}
        <circle
          cx="915"
          cy="284"
          r="47"
          fill="var(--ifm-background-surface-color)"
        />
        <circle
          cx="915"
          cy="284"
          r="47"
          fill="none"
          stroke="var(--ifm-color-emphasis-400)"
        />
        <text
          x="984"
          y="270"
          textAnchor="start"
          className="toe-home-title"
        >
          Normas &
        </text>
        <text
          x="984"
          y="299"
          textAnchor="start"
          className="toe-home-text"
        >
          Frameworks
        </text>

        {/* SE (144°) */}
        <circle
          cx="834"
          cy="533"
          r="47"
          fill="var(--ifm-background-surface-color)"
        />
        <circle
          cx="834"
          cy="533"
          r="47"
          fill="none"
          stroke="var(--ifm-color-emphasis-400)"
        />
        <text
          x="834"
          y="579"
          textAnchor="middle"
          className="toe-home-title"
        >
          Ameaças
        </text>
        <text
          x="834"
          y="608"
          textAnchor="middle"
          className="toe-home-text"
        >
          &amp; incidentes
        </text>

        {/* SW (216°) */}
        <circle
          cx="572"
          cy="533"
          r="47"
          fill="var(--ifm-background-surface-color)"
        />
        <circle
          cx="572"
          cy="533"
          r="47"
          fill="none"
          stroke="var(--ifm-color-emphasis-400)"
        />
        <text
          x="572"
          y="579"
          textAnchor="middle"
          className="toe-home-title"
        >
          Engenharia
        </text>
        <text
          x="572"
          y="608"
          textAnchor="middle"
          className="toe-home-text"
        >
          &amp; ciclo de vida
        </text>

        {/* NW (288°) */}
        <circle
          cx="494"
          cy="284"
          r="47"
          fill="var(--ifm-background-surface-color)"
        />
        <circle
          cx="494"
          cy="284"
          r="47"
          fill="none"
          stroke="var(--ifm-color-emphasis-400)"
        />
        <text
          x="422"
          y="270"
          textAnchor="end"
          className="toe-home-title"
        >
          SDLC,
        </text>
        <text
          x="422"
          y="299"
          textAnchor="end"
          className="toe-home-text"
        >
          CI/CD, deploy
        </text>

        {/* ligações — 5 satélites */}
        {/* top */}
        <line
          x1="704"
          y1="240"
          x2="704"
          y2="177"
          stroke="var(--ifm-color-emphasis-400)"
          strokeWidth="3.6"
        />
        {/* NE */}
        <line
          x1="812"
          y1="317"
          x2="870"
          y2="299"
          stroke="var(--ifm-color-emphasis-400)"
          strokeWidth="3.6"
        />
        {/* SE */}
        <line
          x1="770"
          y1="443"
          x2="807"
          y2="495"
          stroke="var(--ifm-color-emphasis-400)"
          strokeWidth="3.6"
        />
        {/* SW */}
        <line
          x1="638"
          y1="443"
          x2="600"
          y2="495"
          stroke="var(--ifm-color-emphasis-400)"
          strokeWidth="3.6"
        />
        {/* NW */}
        <line
          x1="597"
          y1="317"
          x2="537"
          y2="299"
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
