import React from 'react';
import clsx from 'clsx';
import styles from '@site/src/pages/index.module.css';

type FeatureItem = {
  title: string;
  description: JSX.Element;
};

const FeatureList: FeatureItem[] = [
  {
    title: 'A "cola" entre os standards',
    description: (
      <>
        OWASP, NIST, SLSA, MITRE... o manual sintetiza tudo o que interessa e aplica uma abordagem prática, prescritiva e realista.
        Nada de generalidades — apenas o que é necessário para proteger o desenvolvimento.
      </>
    ),
  },
  {
    title: 'Foco no que é preciso fazer',
    description: (
      <>
        Práticas por fase do ciclo de vida, com responsáveis definidos, critérios claros e ferramentas sugeridas.
        Cada equipa sabe o que tem de fazer — e quando.
      </>
    ),
  },
  {
    title: 'Pronto a usar',
    description: (
      <>
        Inclui exemplos de políticas, checklists, templates de cláusulas contratuais, integrações CI/CD e dashboards.
        Tudo em formato aberto e reutilizável.
      </>
    ),
  },
  {
    title: 'Aplicável a qualquer organização',
    description: (
      <>
        Desde startups a grandes empresas, o manual adapta-se à maturidade, recursos e contexto de cada equipa — promovendo uma adoção progressiva.
      </>
    ),
  },
  {
    title: 'Pensado para Devs, Arquitetos e Segurança',
    description: (
      <>
        Não é um manual genérico: é orientado para quem decide, desenvolve e opera software todos os dias. Com linguagem direta e sem ambiguidades.
      </>
    ),
  },
  {
    title: 'Visão de ciclo de vida completo',
    description: (
      <>
        Não se limita ao código — cobre também integração, deploy, operação, fornecedores e automação, com práticas claras por fase.
      </>
    ),
  },
];

function Feature({title, description}: FeatureItem) {
  return (
    <div className={clsx('col col--4')}>
      <div className="text--center padding-horiz--md">
        <h3>{title}</h3>
        <p>{description}</p>
      </div>
    </div>
  );
}

export default function HomepageFeatures(): JSX.Element {
  return (
    <section className={styles.features}>
      <div className="container">
        <div className="row">
          {FeatureList.map((props, idx) => (
            <Feature key={idx} {...props} />
          ))}
        </div>
      </div>
    </section>
  );
}
