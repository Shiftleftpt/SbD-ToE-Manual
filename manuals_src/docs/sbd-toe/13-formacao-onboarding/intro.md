---
id: intro
title: Formação e Capacitação
description: Estratégias e práticas para garantir que equipas, perfis e stakeholders estão preparados para aplicar o Security by Design
tags: [formacao, capacitacao, onboarding, champions, aprendizagem, DSOMM, SAMM, BSIMM]
sidebar_position: 0
---
import Badge from '@site/src/components/Badge';

<div style={{ display: 'flex', flexWrap: 'wrap', gap: '0.5rem', marginBottom: '1rem' }}>
  <Badge color="warning">Capítulo Basilar</Badge>
  <Badge color="info">SAMM: 2 / 3</Badge>
  <Badge color="info">BSIMM: T1.1, T2.3, SR1.2</Badge>
  <Badge color="info">SSDF: PO.3, PO.7</Badge>
  <Badge color="info">SLSA: Nível 1 / 4</Badge>
  <Badge color="info">DSOMM: 2 / 3 (People & Training)</Badge>
  <a href="./canon/10-maturidade.md" style={{ marginLeft: 'auto', fontSize: '0.9rem' }}>📄 Ver análise de maturidade</a>
</div>

:::caution Capítulo Basilar
Este capítulo é considerado **basilar** no modelo SbD-ToE.  
Sem capacitação contínua das equipas, todos os controlos técnicos falham na prática por falta de aplicação e consciencialização.  
:::

# Formação e Capacitação {cap13:intro}

## 🔎 Nota metodológica {cap13:intro#nota-metodologica}

A **formação em segurança** é o elo que transforma prescrições técnicas em prática operacional.  
- **Cap. 12 — Monitorização & Operações** garante visibilidade em runtime, mas depende de equipas treinadas para interpretar alertas e reagir.  
- **Cap. 14 — Governança & Contratação** define compromissos organizacionais, mas só é eficaz se as equipas tiverem o conhecimento para os cumprir.  

👉 A excecionalidade deste capítulo é que coloca as **pessoas** como vetor de resiliência: uma organização pode ter pipelines seguros e requisitos definidos, mas se os engenheiros, testers, DevOps ou gestores não tiverem formação, a segurança degrada-se na prática.

---

## 🧭 1. O que cobre tecnicamente {cap13:intro#o_que_cobre_tecnicamente}

- Programas de onboarding para novos elementos.  
- Formação contínua para Dev, QA, DevOps, AppSec, Gestão.  
- Programas de *champions* em segurança.  
- Exercícios práticos (labs, CTFs, simulações).  
- KPIs de eficácia formativa.  
- Integração em backlog e planos individuais de desenvolvimento.  

---

## 🧪 2. Prescrição prática {cap13:intro#prescricao}

- **O que fazer:** plano formativo contínuo, onboarding com segurança, labs, métricas de eficácia.  
- **Como:** LMS com trilhas por perfil, champions por equipa, revisões periódicas.  
- **Quando:** onboarding inicial, ciclos trimestrais, sempre que novos controlos são introduzidos.  
- **Porquê:** reduzir erros humanos, criar cultura de segurança, cumprir regulatórios.  

---

## 👥 Papéis envolvidos {cap13:intro#papeis}

- **Dev** → receber formação prática em SAST, dependências, IaC.  
- **QA/Testes** → capacitação em fuzzing, regressões, validação.  
- **AppSec** → produzir conteúdos, ministrar formação, gerir champions.  
- **DevOps/SRE** → capacitação em pipelines seguros e monitorização.  
- **Gestão/PMO** → formação em aceitação de risco e governação.  
- **RH/PeopleOps** → gerir LMS, onboarding e planos individuais.  
- **Champions** → evangelizar e suportar equipas.  
- **Terceiros** → fornecedores com acesso devem receber formação mínima.  

---

## 🔗 Integração no ciclo {cap13:intro#integracao}

A capacitação deve estar presente em todo o ciclo:  
- **Planeamento:** definição de requisitos de formação para cada perfil.  
- **Desenvolvimento:** labs e trilhas específicas integradas em backlog.  
- **Testes/Release:** exercícios de validação ligados a práticas seguras.  
- **Operações:** simulações de incidentes para treino de resposta.  
- **Auditoria:** recolha de métricas de eficácia (KPIs, auditorias internas).  

👉 Assim, a formação deixa de ser “extra” e passa a ser **parte intrínseca do SDLC**.

---

## 📊 Rastreabilidade organizacional {cap13:intro#rastreabilidade}

- **KPIs de capacitação**: taxa de conclusão, retenção de conhecimento, aplicação prática em auditorias.  
- **Métricas de eficácia**: redução de findings repetidos em código, diminuição de incidentes atribuídos a erro humano.  
- **Governança**: relatórios periódicos para GRC e integração em objetivos de performance individuais.  
- **Conformidade**: mapeamento direto para SSDF PO.3/PO.7 e SAMM PO2/PO3, garantindo cobertura normativa.  

---

## 🏁 Conclusão {cap13:intro#conclusao}

A formação é o que **transforma processos em cultura**.  
- Sem onboarding seguro, a organização acumula falhas básicas.  
- Sem formação contínua, as práticas ficam obsoletas.  
- Sem champions, as equipas ficam órfãs de liderança em segurança.  
- Sem métricas, não há melhoria contínua.  

👉 Por isso, este capítulo é considerado **basilar**: é nele que se garante que o SbD-ToE não é apenas documentação, mas prática viva.

---

## 📚 Alinhamento com frameworks {cap13:intro#frameworks}

- **OWASP SAMM** → PO2, PO3 (Education & Guidance).  
- **BSIMM** → T1.1 (Role-specific training), T2.3 (Security features training).  
- **SSDF** → PO.3 (Role-specific training), PO.7 (Awareness).  
- **SLSA** → Nível 1 (cultura organizacional).  
- **DSOMM** → People & Training.  

---

## 📜 Políticas Organizacionais Relevantes {cap13:intro#politicas}

<!--web-only-->

| Política | Obrigatória? | Aplicação | Conteúdo mínimo |
|----------|--------------|-----------|-----------------|
| Política de Formação Contínua | Sim | RH + AppSec | Plano anual, LMS, revisão periódica |
| Política de Onboarding Seguro | Sim | RH + Gestão | Formação obrigatória no início |
| Política de Security Champions | Recomendado | AppSec + Dev | Programa formal com papéis claros |
| Política de Métricas de Capacitação | Sim | GRC | KPIs, eficácia, relatórios de auditoria |
| Política de Exercícios Práticos | Recomendado | AppSec + QA/Dev | Labs, CTFs, simulações |

<!--print-only-->

Na versão impressa, consultar o **Anexo de Políticas Organizacionais do manual**, onde estas políticas estão consolidadas transversalmente.

---
