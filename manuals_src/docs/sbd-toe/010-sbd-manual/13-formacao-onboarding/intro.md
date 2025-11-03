---
id: intro
title: Formação e Capacitação
description: Estratégias e práticas para garantir que equipas, perfis e stakeholders estão preparados para aplicar o Security by Design
tags: [formacao, capacitacao, onboarding, champions, aprendizagem, DSOMM, SAMM, BSIMM]
sidebar_position: 0
---
import Badge from '@site/src/components/Badge';

<div style={{ display: 'flex', flexWrap: 'wrap', gap: '0.5rem', marginBottom: '1rem' }}>
  
  <Badge color="info">SAMM: 2 / 3</Badge>
  <Badge color="info">BSIMM: T1.1, T2.3, SR1.2</Badge>
  <Badge color="info">SSDF: PO.3, PO.7</Badge>
  <Badge color="info">SLSA: Nível 1 / 4</Badge>
  <Badge color="info">DSOMM: 2 / 3 (People & Training)</Badge>
  <a href="./achievable-maturity" style={{ marginLeft: 'auto', fontSize: '0.9rem' }}>📄 Ver análise de maturidade</a>
</div>

:::note Capítulo Organizacional
Este capítulo é considerado **organizacional** no modelo *Security by Design – Theory of Everything (SbD-ToE)*.  
A sua função é **assegurar a adoção, governação e evolução sustentável** das práticas de segurança definidas nos capítulos basilares e operacionais.  

Os capítulos organizacionais estabelecem a estrutura humana e processual que permite consolidar o SbD-ToE na organização, incluindo:
- **Formação, sensibilização e capacitação contínua** (Cap. 13)  
- **Governança, contratação e controlo executivo** (Cap. 14)  

Sem estes elementos, a segurança por design torna-se pontual e dependente de indivíduos, perdendo a **consistência e resiliência organizacional** necessárias à maturidade de longo prazo.
:::


# Formação e Capacitação

A **formação em segurança** é o elo que transforma prescrições técnicas em prática operacional, por exemplo:  
- **Cap. 12 — Monitorização & Operações** garante visibilidade em runtime, mas depende de equipas treinadas para interpretar alertas e reagir.  
- **Cap. 14 — Governança & Contratação** define compromissos organizacionais, mas só é eficaz se as equipas tiverem o conhecimento para os cumprir.  

Para assegurar que a "segurança se vive e respira" e é parte do DNA da organização, é essencial cultivar esse corpo. Este capitulo define como a Segurança passa a ser algo intriseco à organização através de:

- Programas de onboarding para novos elementos.  
- Formação contínua para Dev, QA, DevOps, AppSec, Gestão.  
- Programas de *champions* em segurança.  
- Exercícios práticos (labs, CTFs, simulações).  
- KPIs de eficácia formativa.  
- Integração em backlog e planos individuais de desenvolvimento.  

👉 A excecionalidade deste capítulo é que coloca as **pessoas** como vetor de resiliência: uma organização pode ter pipelines seguros e requisitos definidos, mas se os engenheiros, testers, DevOps ou gestores não tiverem formação, a segurança, na prática. degrada-se.

---

## 🧪 2. Prescrição prática

- **O que fazer:** plano formativo contínuo, onboarding com segurança, labs, métricas de eficácia.  
- **Como:** LMS com trilhas por perfil, champions por equipa, revisões periódicas.  
- **Quando:** onboarding inicial, ciclos trimestrais, sempre que novos controlos são introduzidos.  
- **Porquê:** reduzir erros humanos, criar cultura de segurança, cumprir regulatórios.  

---

## 👥 Papéis envolvidos

- **Dev** → receber formação prática em SAST, dependências, IaC.  
- **QA/Testes** → capacitação em fuzzing, regressões, validação.  
- **AppSec** → produzir conteúdos, ministrar formação, gerir champions.  
- **DevOps/SRE** → capacitação em pipelines seguros e monitorização.  
- **Gestão/PMO** → formação em aceitação de risco e governação.  
- **RH/PeopleOps** → gerir LMS, onboarding e planos individuais.  
- **Champions** → evangelizar e suportar equipas.  
- **Terceiros** → fornecedores com acesso devem receber formação mínima.  

---

## 🔗 Integração no ciclo

A capacitação deve estar presente em todo o ciclo:  
- **Planeamento:** definição de requisitos de formação para cada perfil.  
- **Desenvolvimento:** labs e trilhas específicas integradas em backlog.  
- **Testes/Release:** exercícios de validação ligados a práticas seguras.  
- **Operações:** simulações de incidentes para treino de resposta.  
- **Auditoria:** recolha de métricas de eficácia (KPIs, auditorias internas).  

👉 Assim, a formação deixa de ser “extra” e passa a ser **parte intrínseca do SDLC**.

---

## 📊 Rastreabilidade organizacional

- **KPIs de capacitação**: taxa de conclusão, retenção de conhecimento, aplicação prática em auditorias.  
- **Métricas de eficácia**: redução de findings repetidos em código, diminuição de incidentes atribuídos a erro humano.  
- **Governança**: relatórios periódicos para GRC e integração em objetivos de performance individuais.  
- **Conformidade**: mapeamento direto para SSDF PO.3/PO.7 e SAMM PO2/PO3, garantindo cobertura normativa.  

---

## 🏁 Conclusão

A formação é o que **transforma processos em cultura**.  
- Sem onboarding seguro, a organização acumula falhas básicas.  
- Sem formação contínua, as práticas ficam obsoletas.  
- Sem champions, as equipas ficam órfãs de liderança em segurança.  
- Sem métricas, não há melhoria contínua.  

👉 Por isso, este capítulo é considerado **basilar**: é nele que se garante que o SbD-ToE não é apenas documentação, mas prática viva.

---

## 📚 Alinhamento com frameworks

- **OWASP SAMM** → PO2, PO3 (Education & Guidance).  
- **BSIMM** → T1.1 (Role-specific training), T2.3 (Security features training).  
- **SSDF** → PO.3 (Role-specific training), PO.7 (Awareness).  
- **SLSA** → Nível 1 (cultura organizacional).  
- **DSOMM** → People & Training.  

---

## 📜 Políticas Organizacionais Relevantes

| Política | Obrigatória? | Aplicação | Conteúdo mínimo |
|----------|--------------|-----------|-----------------|
| Política de Formação Contínua | Sim | RH + AppSec | Plano anual, LMS, revisão periódica |
| Política de Onboarding Seguro | Sim | RH + Gestão | Formação obrigatória no início |
| Política de Security Champions | Recomendado | AppSec + Dev | Programa formal com papéis claros |
| Política de Métricas de Capacitação | Sim | GRC | KPIs, eficácia, relatórios de auditoria |
| Política de Exercícios Práticos | Recomendado | AppSec + QA/Dev | Labs, CTFs, simulações |

Na versão impressa, consultar o **Anexo de Políticas Organizacionais do manual**, onde estas políticas estão consolidadas transversalmente.

---
