---
description: Integração prática das práticas de capacitação e onboarding no ciclo
  de vida de desenvolvimento
genia: us-format-normalization
id: aplicacao-lifecycle
tags:
- capacitacao
- cicd
- ciclo-vida
- formacao
- onboarding
- seguranca
- tipo:aplicacao
title: Como Fazer
---


# 🎓 Aplicação de Formação e Capacitação no Ciclo de Vida

## 🧭 Quando aplicar

| Fase | Ação | Evidência |
|------|------|-----------|
| Onboarding | Formação inicial em SbD e práticas seguras | Certificação LMS |
| Desenvolvimento contínuo | Cursos, labs e revisões trimestrais | Relatórios de formação |
| Release/Operações | Exercícios práticos e simulações | Logs de exercícios |
| Auditoria | Verificação de KPIs de capacitação | Relatórios GRC |

---

## 👥 Quem executa cada ação

| Papel | Responsabilidade |
|-------|------------------|
| **Developer** | Participar em formação prática, aplicar no código |
| **Quality Assurance (QA)** | Formação em validação e regressões |
| **AppSec Engineer** | Produzir conteúdos, ministrar formação, facilitar sesões |
| **DevOps / SRE** | Capacitação em CI/CD e monitorização |
| **Security Champion** | Mentorar equipas, facilitar peer-learning |
| **Gestão Executiva** | Apoiar adoção, validar conformidade regulatória |
| **GRC / Compliance** | Gerir rastreabilidade, auditorias, KPIs |
| **RH / PeopleOps** | Operar LMS, gerir onboarding, integrar em PDI |
| **Arquitetos de Software** | Contribuir ao threat modeling e padrões seguros |
| **Operações (Ops)** | Participar em simulações, comunicação em incidentes |
| **Fornecedores / Terceiros** | Receber formação mínima obrigatória |

---

## 📖 User Stories normalizadas

### US-01 - Onboarding seguro obrigatório
**Contexto.** Novos elementos sem formação introduzem riscos básicos.  

:::userstory
**História.**   
Como **RH/PeopleOps**, quero **garantir formação obrigatória de onboarding em SbD**, para **assegurar que todos iniciam alinhados com as práticas**.  

**Critérios de aceitação (BDD).**  
- **Dado** novo colaborador  
  **Quando** inicia funções  
  **Então** só tem acesso completo após completar formação  

**Checklist.**  
- [ ] Curso concluído no LMS  
- [ ] Certificação emitida  
- [ ] Registo arquivado  
- [ ] Acesso técnico bloqueado até conclusão  
- [ ] Bloqueio automático em Git/Azure DevOps/pipelines CI/CD  
- [ ] Exceções documentadas com aprovação AppSec/Gestão  
- [ ] Reautenticação bienal ou por trigger de novo risco  

:::

**Artefactos & evidências.** Certificados LMS, registos de bloqueio em Git/Azure DevOps, documento de exceções.

**Proporcionalidade.**  
| L1 | L2 | L3 |
|----|----|----|
| Básico | Obrigatório | Obrigatório + avaliação prática |

**Integração no SDLC.**  
| Fase | Trigger | Responsável | SLA |
|------|---------|-------------|-----|
| Onboarding | Entrada de novo colaborador | RH + AppSec Engineer | Antes de acesso técnico |

**Ligações úteis.**  
[Checklist de Onboarding Técnico](formacao-onboarding/addon/10-checklist-onboarding)  
[Papéis e Responsabilidades](/sbd-toe/000-teory-of-everything/07-roles)  

---

### US-02 - Formação contínua por perfil
**Contexto.** Sem atualização contínua, práticas ficam obsoletas.  

:::userstory
**História.**   
Como **AppSec**, quero **fornecer formação contínua por perfil (Dev, QA, DevOps, Gestão)**, para **garantir atualização com práticas mais recentes**.  

**Critérios de aceitação (BDD).**  
- **Dado** ciclo trimestral (L3), anual (L1–L2)  
  **Quando** LMS disponibiliza cursos  
  **Então** cada perfil completa trilha específica  

**Checklist.**  
- [ ] Cursos definidos por perfil  
- [ ] Registo no LMS  
- [ ] Ciclo definido: trimestral para L3, anual para L1/L2  
- [ ] Triggers adicionais: novo capítulo técnico, novo risco, incidente  
- [ ] Comunicação a equipas (anúncio, deadline, critério de conclusão)  
- [ ] Integração em OKRs individuais ou avaliações de performance  
- [ ] Revisão de eficácia trimestral  

:::

**Artefactos & evidências.** Relatórios LMS, comunicações a equipas, registos de conclusão, OKRs com formação.

**Proporcionalidade.**  
| L1 | L2 | L3 |
|----|----|----|
| Básico | Obrigatório anual | Obrigatório trimestral |

**Integração no SDLC.**  
| Fase | Trigger | Responsável | SLA |
|------|---------|-------------|-----|
| Ciclo contínuo | Trimestral (L3) / Anual (L1–L2) | AppSec Engineer + RH | Deadline comunicado com 2 semanas |

**Ligações úteis.**  
[Catálogo de Formação por Perfil Técnico](formacao-onboarding/addon/01-catalogo-formativo)  
[Trilhos Formativos por Função e Risco](formacao-onboarding/addon/02-trilho-formativo)  
[Papéis e Responsabilidades](/sbd-toe/000-teory-of-everything/07-roles)  

---

### US-03 - Programa de Security Champions
**Contexto.** Sem champions, equipas carecem de liderança interna.  

:::userstory
**História.**   
Como **Champion**, quero **mentorar e evangelizar a equipa**, para **assegurar aplicação contínua das práticas SbD**.  

**Critérios de aceitação (BDD).**  
- **Dado** sprint em curso  
  **Quando** surgem dúvidas  
  **Então** champion apoia e orienta equipa  

**Checklist.**  
- [ ] Champion nomeado por equipa  
- [ ] Reuniões mensais registadas  
- [ ] Feedback recolhido  
- [ ] Comunidade de Champions formal (reunião mensal, canal Teams/Slack)  
- [ ] Documentação coletiva de práticas e antipadrões (wiki)  
- [ ] Badges ou reconhecimento institucional (email, quadro, salário)  
- [ ] Budget para eventos ou conferências de segurança (opcional por maturity)  

:::

**Artefactos & evidências.** Registos de reuniões, wiki de práticas, canal de comunidade, lista de reconhecimentos.

**Proporcionalidade.**  
| L1 | L2 | L3 |
|----|----|----|
| Opcional | Recomendado | Obrigatório |

**Integração no SDLC.**  
| Fase | Trigger | Responsável | SLA |
|------|---------|-------------|-----|
| Ciclo contínuo | Mensal | Security Champions + AppSec Engineer | Reunião mensal confirmada |

**Ligações úteis.**  
[Programa de Security Champions](formacao-onboarding/addon/03-programa-champions)  
[Papéis e Responsabilidades](/sbd-toe/000-teory-of-everything/07-roles)  

---

### US-04 - Exercícios práticos e simulações
**Contexto.** Formação teórica sem prática tem baixa retenção.  

:::userstory
**História.**   
Como **QA/Testes**, quero **realizar exercícios práticos (labs, CTFs, simulações)**, para **garantir que o conhecimento é aplicável**.  

**Critérios de aceitação (BDD).**  
- **Dado** plano de formação  
  **Quando** executo exercício  
  **Então** registo resultado e métricas de desempenho  

**Critérios de aceitação (DoD).**  
- [ ] Labs executados  
- [ ] Resultados registados  
- [ ] Métricas analisadas  

:::

**Artefactos & evidências.** Logs de exercícios  

**Proporcionalidade.**  
| L1 | L2 | L3 |
|----|----|----|
| Opcional | Recomendado | Obrigatório |

**Integração.** Ciclo de formação; Resp: QA + AppSec  

---

### US-05 - Medição de eficácia da formação
**Contexto.** Sem medir eficácia, não há melhoria contínua.  

:::userstory
**História.**   
Como **GRC**, quero **medir KPIs de capacitação (taxa de conclusão, eficácia em auditoria)**, para **avaliar impacto real da formação**.  

**Critérios de aceitação (BDD).**  
- **Dado** ciclo de formação  
  **Quando** recolho métricas  
  **Então** KPIs são reportados a gestão  

**Critérios de aceitação (DoD).**  
- [ ] KPIs definidos  
- [ ] Métricas recolhidas  
- [ ] Relatórios trimestrais  

:::

**Artefactos & evidências.** Relatórios GRC  

**Proporcionalidade.**  
| L1 | L2 | L3 |
|----|----|----|
| Básico | KPIs anuais | KPIs trimestrais com metas |

**Integração.** Auditoria; Resp: GRC  

---

### US-06 - Code Clinics Estruturadas e Recorrentes
**Contexto.** Code clinics são sessões regulares de revisão pública de código real, educando sobre padrões seguros. Sem estrutura, tornam-se ad-hoc e perdem impacto.

:::userstory
**História.**  
Como **AppSec Engineer**, quero **executar code clinics estruturadas** (revisão de PR reais, educativas, com checklist de segurança aplicado), para **garantir aprendizagem contínua e aplicação visível de padrões seguros**.

**Critérios de aceitação (BDD).**  
- **Dado** que uma ou mais PRs são selecionadas  
  **Quando** a sessão é conduzida (presencial ou assíncrona)  
  **Então** o checklist de segurança é aplicado publicamente  
- E feedback é registado e compartilhado em canal interno  
- E lições aprendidas são documentadas para reutilização  

**Checklist.**  
- [ ] Cadência definida (semanal ou quinzenal)  
- [ ] Templates de checklist por domínio (Dev, DevOps, IaC)  
- [ ] PRs exemplares arquivadas (boas práticas + falhas)  
- [ ] Sessões registadas (vídeo, sumário, discussão assíncrona)  
- [ ] Participação rotativa (Developers, Security Champions, QA)  

:::

**Artefactos & evidências.**  
- Repositório de PRs exemplares (comentados)  
- Sumários de sessões e feedback  
- Estatísticas de participação  

**Proporcionalidade L1–L3.**  
| L1 | L2 | L3 |
|----|----|----|
| Ocasional (mensal) | Recorrente (quinzenal) | Recorrente + rotativo (semanal) |

**Integração no SDLC.**  
| Fase | Trigger | Responsável | SLA |
|------|---------|-------------|-----|
| Desenvolvimento | Submissão de PRs | AppSec Engineer + Security Champions | Semanal/quinzenal |

**Ligações úteis.**  
[Técnicas Formativas Avançadas](formacao-onboarding/addon/04-tecnicas-formativas)  
[Exemplo - Pull Request Seguro](formacao-onboarding/addon/07-exemplo1-manual-formacao-dev-pr-seguro)  
[Papéis e Responsabilidades](/sbd-toe/000-teory-of-everything/07-roles)

---

### US-07 - Threat Modeling Peer-led e Rotativo
**Contexto.** Threat modeling é prática crítica mas concentrada em AppSec. Operacionalizar como atividade peer-led e rotativa aumenta distribuição de conhecimento.

:::userstory
**História.**  
Como **Developer / Security Champion**, quero **liderar sessões de threat modeling** (por feature, épico ou refactor), para **disseminar conhecimento de análise de risco e aplicar SbD em design**.

**Critérios de aceitação (BDD).**  
- **Dado** que uma feature nova ou refactor é planeado  
  **Quando** a sessão de threat modeling é agendada  
  **Então** é facilitada por Developer ou Champion com apoio de AppSec Engineer  
- E output é documentado (diagrama, matriz de riscos)  
- E decisões de segurança são rastreadas a requisitos do manual  

**Checklist.**  
- [ ] Sessão agendada antes de design finalizador  
- [ ] Template de threat modeling (ex: STRIDE) aplicado  
- [ ] Diagrama de arquitetura/fluxo documentado  
- [ ] Matriz de riscos (ameaça × impacto × controlo)  
- [ ] Decisões e exceções justificadas  
- [ ] Rotação de liderança entre Security Champions  

:::

**Artefactos & evidências.**  
- Diagramas (draw.io, Lucidchart)  
- Atas de sessão  
- Matriz de riscos com rastreabilidade a REQ-XXX  

**Proporcionalidade L1–L3.**  
| L1 | L2 | L3 |
|----|----|----|
| Opcional / ad-hoc | Recomendado por épico | Obrigatório antes de design finalizador |

**Integração no SDLC.**  
| Fase | Trigger | Responsável | SLA |
|------|---------|-------------|-----|
| Planeamento/Design | Aprovação de feature | Security Champion + AppSec Engineer | Antes do sprint de desenvolvimento |

**Ligações úteis.**  
[Técnicas Formativas Avançadas](formacao-onboarding/addon/04-tecnicas-formativas)  
[Integração Transversal com Capítulos Técnicos](formacao-onboarding/addon/05-integracao-transversal)  
[Threat Modeling - Capítulo 03](/threat-modeling/intro)  
[Papéis e Responsabilidades](/sbd-toe/000-teory-of-everything/07-roles)

---

### US-08 - War Room e Simulações de Incidentes
**Contexto.** Simulações de incidentes treinam equipas na resposta sob pressão, validam processos e criam cultura de prontidão.

:::userstory
**História.**  
Como **Gestão Executiva / GRC**, quero **executar simulações de incidentes (war room)** regularmente, para **treinar equipas na resposta e validar processos de comunicação e remediação**.

**Critérios de aceitação (BDD).**  
- **Dado** que um cenário de incidente é simulado  
  **Quando** a resposta é executada em tempo real  
  **Então** todos os papéis (Developer, DevOps, AppSec Engineer, Operações, Gestão) participam  
- E o processo é documentado e analisado num debrief educativo  
- E lições aprendidas são incorporadas em runbooks  

**Checklist.**  
- [ ] Cenários baseados em riscos reais ou históricos  
- [ ] Comunicação (alertas, escalation, comms internas/externas) validadas  
- [ ] Tempos de deteção, resposta e resolução medidos (MTTD/MTTR)  
- [ ] Papel de cada interveniente documentado (playbooks)  
- [ ] Debrief realizado com recomendações  
- [ ] Cadência definida (anual mínimo, trimestral ideal)  

:::

**Artefactos & evidências.**  
- Cenários e scripts de simulação  
- Logs de execução (timelines, comunicações)  
- Relatório de debrief com MTTD/MTTR observados  
- Playbooks e runbooks atualizados  

**Proporcionalidade L1–L3.**  
| L1 | L2 | L3 |
|----|----|----|
| Recomendado anual | Trimestral | Trimestral + rotativo por ameaça |

**Integração no SDLC.**  
| Fase | Trigger | Responsável | SLA |
|------|---------|-------------|-----|
| Operações/Auditoria | Trimestral ou pós-incidente | Gestão Executiva + GRC | Planeado anualmente |

**Ligações úteis.**  
[Técnicas Formativas Avançadas](formacao-onboarding/addon/04-tecnicas-formativas)  
[Monitorização e Operações - Capítulo 12](/monitorizacao-operacoes/intro)  
[Papéis e Responsabilidades](/sbd-toe/000-teory-of-everything/07-roles)

---

### US-09 - Manutenção e Atualização de Trilhos Formativos
**Contexto.** Trilhos formativos precisam de revisão periódica com base em novos riscos, tecnologias, lições aprendidas.

:::userstory
**História.**  
Como **AppSec Engineer / GRC**, quero **manter e atualizar trilhos formativos por perfil e risco** (anualmente ou por trigger), para **garantir que a formação reflete práticas atuais e lições aprendidas**.

**Critérios de aceitação (BDD).**  
- **Dado** que um ano passou ou um novo risco é identificado  
  **Quando** a revisão de trilhos é agendada  
  **Então** conteúdos são reavaliados contra incidentes, atualizações tecnológicas e feedback de Security Champions  
- E trilhos são atualizados ou novos conteúdos são adicionados  
- E mudanças são comunicadas a RH e às equipas  

**Checklist.**  
- [ ] Revisão anual agendada (ex: Q1 de cada ano)  
- [ ] Feedback de Security Champions recolhido (survey ou reunião)  
- [ ] Lições aprendidas de incidentes integradas  
- [ ] Novos capítulos técnicos ou práticas mapeados  
- [ ] Trilhos atualizados (documento e matriz)  
- [ ] Comunicação a stakeholders (RH, equipas, Gestão Executiva)  

:::

**Artefactos & evidências.**  
- Documento com versão e changelog  
- Survey de feedback de Security Champions  
- Mapeamento de novos conteúdos a capítulos  
- Nota de lançamento com mudanças  

**Proporcionalidade L1–L3.**  
| L1 | L2 | L3 |
|----|----|----|
| Ocasional | Anual | Anual + contínua por trigger |

**Integração no SDLC.**  
| Fase | Trigger | Responsável | SLA |
|------|---------|-------------|-----|
| Governance/Auditoria | Anual (Q1) ou novo risco | AppSec Engineer + GRC + RH | Antes do ciclo de formação novo |

**Ligações úteis.**  
[Catálogo de Formação por Perfil Técnico](formacao-onboarding/addon/01-catalogo-formativo)  
[Trilhos Formativos por Função e Risco](formacao-onboarding/addon/02-trilho-formativo)  
[Papéis e Responsabilidades](/sbd-toe/000-teory-of-everything/07-roles)

---

### US-10 - Trilhos Formativos Proporcionais por Risco (L1–L3)

**Contexto.**  
Trilhos formativos precisam de ser explicitamente proporcionais ao risco da aplicação. Embora US-02 mencione "por perfil", falta clareza sobre a aplicação L1–L3 e sua integração com matriz de classificação de risco do cap 01.

:::userstory
**História.**  
Como **AppSec Engineer / GRC**, quero **aplicar trilhos formativos de forma explicitamente proporcional ao nível de risco** (L1, L2, L3) da aplicação e ao perfil técnico, para **garantir que cada colaborador recebe formação adequada ao seu contexto e responsabilidade**.

**Critérios de aceitação (BDD).**  
- **Dado** uma aplicação classificada em L1, L2 ou L3  
  **Quando** um novo colaborador é onboarded ou trilho é atualizado  
  **Então** o trilho formativo aplicado corresponde à matriz de proporcionalidade  
- E conteúdo reflete práticas obrigatórias conforme nível de risco  
- E rastreabilidade entre classificação → trilho é documentada  

**Checklist.**  
- [ ] Classificação de risco da aplicação documentada (cap 01)  
- [ ] Matriz de trilhos (addon/02) referenciada no plano de formação  
- [ ] Trilho L1: conteúdos básicos (secure coding, dependências, políticas)  
- [ ] Trilho L2: conteúdos intermédios (threat modeling, SCA, PR seguro, scanners CI/CD)  
- [ ] Trilho L3: conteúdos avançados (arquitetura segura, labs em apps vulneráveis, fuzzing, integração IRP)  
- [ ] Atribuição explícita do trilho por colaborador em LMS ou documento  
- [ ] Rastreabilidade: link entre classificação de aplicação → trilho → RH/LMS  
- [ ] Revisão periódica (anual ou por trigger de reclassificação)  
- 
- [ ] Catálogo → Trilho: existe um artefacto de mapeamento catálogo→trilho (`catalogo_trilhos.csv` ou `catalogo_trilhos.json`) que lista, para cada capítulo/tópico do `addon/01`, o módulo/trilho recomendado e a versão L1/L2/L3 aplicável.  
- 
**Artefactos & evidências adicionais.** `catalogo_trilhos.csv` com colunas mínimas: capitulo, topico, trilho_L1, trilho_L2, trilho_L3, formato_sugerido, exemplo_import_lms. Um exemplo de importação (CSV pequeno) deve acompanhar o plano de formação.  
- 
:::

**Artefactos & evidências.**  
Documento de classificação de risco (cap 01), matriz de trilhos (addon/02) com seleção do trilho aplicado, atribuição em LMS ou documento de plano formativo, rastreabilidade documentada.

**Proporcionalidade L1–L3.**  
| L1 | L2 | L3 |
|----|----|----|
| Trilho básico (conteúdos essenciais) | Trilho intermédio (conteúdos obrigatórios + labs) | Trilho avançado (conteúdos completos + simulações + auditoria contínua) |

**Integração no SDLC.**  
| Fase | Trigger | Responsável | SLA |
|------|---------|-------------|-----|
| Onboarding / Governance | Classificação da aplicação | AppSec Engineer + RH | Antes de primeira atribuição técnica |

**Ligações úteis.**  
[Trilhos Formativos por Função e Risco](formacao-onboarding/addon/02-trilho-formativo)  
[Gestão de Risco e Classificação - Capítulo 01](/classificacao-aplicacoes/intro)  
[Papéis e Responsabilidades](/sbd-toe/000-teory-of-everything/07-roles)

---

### US-11 - Validação Formal de Onboarding via Checklist
**Contexto.** Onboarding sem validação formal deixa lacunas. Um checklist estruturado garante que todos os passos mínimos são cumpridos antes de qualquer acesso técnico.

:::userstory
**História.**  
Como **RH / GRC**, quero **validar formalmente o onboarding de cada colaborador** (via checklist estruturado), para **garantir que todos cumprem requisitos mínimos antes de acesso técnico e criar rastreabilidade auditável**.

**Critérios de aceitação (BDD).**  
- **Dado** que um novo colaborador inicia  
  **Quando** o processo de onboarding é executado  
  **Então** todos os itens do checklist são validados por responsável designado  
- E o registo formal é arquivado  
- E acesso técnico é bloqueado até conclusão  

**Checklist.**  
- [ ] Trilho formativo correto atribuído por função e risco  
- [ ] Conclusão do trilho validada (LMS ou evidência prática)  
- [ ] Validação de conhecimento concluída (quiz, exercício ou PR)  
- [ ] Acesso a repositórios de boas práticas e templates confirmado  
- [ ] Acesso técnico (Git, pipelines, ambientes) condicionado à conclusão  
- [ ] Registo formal arquivado com data e responsável  
- [ ] Contacto de apoio (Champion, SPOC) identificado  
- [ ] Aplicável a internos e externos (fornecedores com acesso técnico)  

:::

**Artefactos & evidências.**  
- Checklist preenchido e assinado (digital ou papel)  
- Registo em LMS, sistema de permissões ou GitHub/ADO  
- Evidência de conclusão (certificado, PDF, issue fechada)  

**Proporcionalidade L1–L3.**  
| L1 | L2 | L3 |
|----|----|----|
| Básico (função) | Estruturado (função + risco) | Estruturado + auditoria periódica |

**Integração no SDLC.**  
| Fase | Trigger | Responsável | SLA |
|------|---------|-------------|-----|
| Onboarding | Entrada de novo colaborador | RH + GRC | Antes de acesso técnico |

**Ligações úteis.**  
[Checklist de Onboarding Técnico](formacao-onboarding/addon/10-checklist-onboarding)  
[Trilhos Formativos por Função e Risco](formacao-onboarding/addon/02-trilho-formativo)  
[Papéis e Responsabilidades](/sbd-toe/000-teory-of-everything/07-roles)

---

### US-12 - Validação de Conhecimento via Quizzes Estruturados
**Contexto.** Formação sem validação de retenção de conhecimento é ineficaz. Quizzes estruturados garantem compreensão real e funcionam como rastreabilidade objetiva.

:::userstory
**História.**  
Como **AppSec Engineer / RH**, quero **implementar e executar quizzes de validação** (pós-onboarding, contínuos, por função) para **garantir retenção de conhecimento e criar registro auditável de competência**.

**Critérios de aceitação (BDD).**  
- **Dado** que um colaborador completa formação  
  **Quando** o quiz é aplicado  
  **Então** resultado ≥ 80% é obtido  
- E o registo (pontuação, data, validador) é arquivado  
- E acesso técnico só é desbloqueado com resultado positivo  

**Checklist.**  
- [ ] Quizzes definidos por trilho formativo (onboarding, contínuo, função)  
- [ ] Perguntas adaptadas a conteúdos reais do manual e aplicação  
- [ ] Formato acessível (LMS, formulário, ferramenta online, papel)  
- [ ] Resultado mínimo de aprovação definido (ex: 80%)  
- [ ] Feedback imediato com explicações de respostas  
- [ ] Registo com timestamp, nome, resultado e validador  
- [ ] Reciclagem periódica (ex: anual ou por trigger de novo risco)  
- [ ] Aplicável a internos, fornecedores e terceiros com acesso  

:::

**Artefactos & evidências.**  
- Templates de quiz por trilho e função  
- Registos de submissão com resultados  
- Análise de tendências (taxa de aprovação, tópicos mais falhados)  

**Proporcionalidade L1–L3.**  
| L1 | L2 | L3 |
|----|----|----|
| Pontual (onboarding) | Periódica (anual) | Periódica + adaptativa (por trigger) |

**Integração no SDLC.**  
| Fase | Trigger | Responsável | SLA |
|------|---------|-------------|-----|
| Onboarding / Contínuo | Conclusão de trilho ou anualmente | AppSec Engineer + RH | Antes/durante acesso |

**Ligações úteis.**  
[Template de Quiz para Onboarding](formacao-onboarding/addon/11-template-quiz-onboarding)  
[Quiz de Validação para Terceiros](formacao-onboarding/addon/22-template-quiz-terceiros)  
[Catálogo de Formação por Perfil Técnico](formacao-onboarding/addon/01-catalogo-formativo)  
[Papéis e Responsabilidades](/sbd-toe/000-teory-of-everything/07-roles)

---

### US-13 - Operacionalização de Formação de Terceiros
**Contexto.** Fornecedores e terceiros com acesso técnico precisam de formação mínima obrigatória para reduzir risco de falhas de segurança.

:::userstory
**História.**  
Como **GRC / Gestão Executiva**, quero **garantir que fornecedores e terceiros com acesso recebem formação mínima obrigatória**, para **reduzir risco de falhas de segurança por falta de conhecimento e cumprir obrigações regulatórias (NIS2, DORA)**.

**Critérios de aceitação (BDD).**  
- **Dado** que um fornecedor com acesso técnico é onboarded  
  **Quando** é estabelecido acesso  
  **Então** completa trilho formativo obrigatório (ex: política da organização, canais de apoio, requisitos mínimos)  
- E certificação é registada contratualmente  
- E acesso é bloqueado até conclusão  

**Checklist.**  
- [ ] Categorização de terceiros (acesso nível, sensibilidade de dados)  
- [ ] Trilho mínimo definido por categoria  
- [ ] Quiz ou validação prática com resultado ≥ 80%  
- [ ] Certificado emitido e arquivado  
- [ ] Registo de conformidade em GRC  
- [ ] Acesso condicionado a conclusão  
- [ ] Reciclagem trimestral ou anual  

:::

**Artefactos & evidências.**  
- Trilhos por categoria de terceiro (conforme addon/21)  
- Quizzes e templates de validação (conforme addon/22)  
- Certificados e registos de conclusão  
- Registo de conformidade contratual  

**Proporcionalidade L1–L3.**  
| L1 | L2 | L3 |
|----|----|----|
| Recomendado | Obrigatório | Obrigatório + anual |

**Integração no SDLC.**  
| Fase | Trigger | Responsável | SLA |
|------|---------|-------------|-----|
| Onboarding | Contrato de fornecedor | GRC + RH + AppSec Engineer | Antes de acesso |

**Ligações úteis.**  
[Modelo de Inclusão de Terceiros](formacao-onboarding/addon/20-modelo-inclusao-terceiros)  
[Plano de Formação de Terceiros](formacao-onboarding/addon/21-plano-formacao-terceiros)  
[Quiz de Validação para Terceiros](formacao-onboarding/addon/22-template-quiz-terceiros)  
[Governança e Contratação - Capítulo 14](/governanca-contratacao/intro)  
[Papéis e Responsabilidades](/sbd-toe/000-teory-of-everything/07-roles)

### US-14 - KPIs de Capacitação e Reporte (GRC)
**Contexto.** KPIs dispersos reduzem a capacidade de avaliar impacto da formação. É necessário formalizar lista, responsáveis e cadência.

:::userstory
**História.**
Como **GRC / Gestão Executiva**, quero **definir e recolher KPIs de capacitação** (taxa de conclusão, taxa de aprovação, eficácia em auditoria, MTTR em exercícios), para **avaliar impacto e reportar conformidade**.

**Critérios de aceitação (BDD).**
- **Dado** ciclo de formação definido
  **Quando** as métricas são recolhidas
  **Então** os KPIs são reportados ao dashboard e enviados trimestralmente para Gestão Executiva

**Checklist.**
- [ ] Lista de KPIs definida (ex: taxa de conclusão, taxa aprovação ≥80%, % tópicos falhados, tempo médio para completar labs)
- [ ] Responsável definido (GRC owner)
- [ ] Cadência de recolha e reporte definida (mensal/trimestral)
- [ ] Dashboard ou relatório automatizado configurado (ex: PowerBI/Looker/Grafana)
- [ ] Evidências arquivadas para auditoria (CSV/relatório PDF)

:::

**Artefactos & evidências.** Documento `KPIs_formacao.md` com definição, owner, cadência; amostra de exportação CSV; link para dashboard.

**Proporcionalidade L1–L3.**
| L1 | L2 | L3 |
|----|----|----|
| KPIs anuais | KPIs trimestrais com metas | KPIs trimestrais + metas por trilho e auditoria prática |

**Integração no SDLC.**
| Fase | Trigger | Responsável | SLA |
|------|---------|-------------|-----|
| Auditoria/Formação | Monthly/Quarterly | GRC + AppSec Engineer | Report trimestral |

---

### US-15 - Formatos de Entrega e DoD por Formato
**Contexto.** A falta de especificação mínima por formato (labs, code clinics, microlearning, simulações) dificulta replicabilidade e níveis de qualidade.

:::userstory
**História.**
Como **AppSec Engineer / RH**, quero **definir os formatos de entrega e o DoD mínimo por formato** (labs, code clinics, microlearning, quizzes, simulações), para **garantir consistência e qualidade na formação**.

**Critérios de aceitação (BDD).**
- **Dado** um formato escolhido (ex: lab)
  **Quando** a sessão é planeada
  **Então** existe um DoD mínimo (infra + cenário + scoring + registo) e artefactos associados

**Checklist / DoD por formato.**
- Labs: infra provisionada + app vulnerável (ou VM) + guia de exercícios + scoring automático/manual + logs e relatório
- Code clinics: PRs selecionadas + checklist aplicado + gravação/resumo + pacote de lições aprendidas
- Microlearning: micro‑modules ≤15min + quiz de 3–5 perguntas + material de referência
- Simulações: cenário scriptado + playbook atualizado + debrief com MTTD/MTTR e melhorias
- Quizzes: template por trilho + threshold (ex: ≥80%) + registo timestamped

:::

**Artefactos & evidências.** Exemplos: `lab_template.md`, `code_clinic_template.md`, `microlearning_manifest.csv`, `simulation_script.yaml`.

**Proporcionalidade L1–L3.**
| L1 | L2 | L3 |
|----|----|----|
| Formatos básicos (microlearning) | Labs e quizzes estructurados | Labs com scoring + simulações + auditoria |

---

## 📦 Artefactos esperados

| Artefacto | Evidência |
|-----------|-----------|
| Certificados LMS | Onboarding concluído |
| Relatórios LMS | Formação contínua |
| Registos de champions | Reuniões + feedback |
| Logs de exercícios | Resultados e métricas |
| Relatórios GRC | KPIs e eficácia |
| **Repositório de PRs exemplares** | **Code clinics registadas** |
| **Diagramas de threat modeling** | **Atas e matriz de riscos** |
| **Cenários e logs de simulações** | **Relatórios de debrief e playbooks** |
| **Documento de trilhos com changelog** | **Survey de Champions + feedback** |
| **Checklist de onboarding validado** | **Registos formais por colaborador** |
| **Registos de quizzes** | **Pontuações, datas e validadores** |
| **Certificados de terceiros** | **Registos GRC de conformidade contratual** |

---

## ⚖️ Matriz de proporcionalidade L1–L3

| Prática | L1 | L2 | L3 |
|---------|----|----|----|
| Onboarding seguro | Básico | Obrigatório | Obrigatório + avaliação prática |
| Formação contínua | Básico | Anual | Trimestral |
| Champions | Opcional | Recomendado | Obrigatório |
| Exercícios práticos | Opcional | Recomendado | Obrigatório |
| Métricas de eficácia | Básico | Anual | Trimestral com metas |
| **Code Clinics** | **Ocasional** | **Recorrente (quinzenal)** | **Recorrente + rotativo (semanal)** |
| **Threat Modeling** | **Opcional** | **Recomendado por épico** | **Obrigatório antes de design** |
| **Simulações de incidentes** | **Recomendado anual** | **Trimestral** | **Trimestral + rotativo** |
| **Manutenção de trilhos** | **Ocasional** | **Anual** | **Anual + contínua por trigger** |
| **Trilhos proporcionais por risco** | **Trilho básico** | **Trilho intermédio + labs** | **Trilho avançado + simulações + auditoria** |
| **Validação de onboarding (checklist)** | **Básico** | **Estruturado (função + risco)** | **Estruturado + auditoria periódica** |
| **Validação de conhecimento (quizzes)** | **Pontual** | **Periódica (anual)** | **Periódica + adaptativa** |
| **Formação de terceiros** | **Recomendado** | **Obrigatório** | **Obrigatório + anual** |

---

## 🏁 Recomendações finais

- **Onboarding é crítico**: sem formação inicial, erros básicos propagam-se.  
- **Validação formal via checklist** garante que todos os passos mínimos são cumpridos.  
- **Quizzes estruturados** validam retenção de conhecimento de forma auditável.  
- **Formação contínua** mantém práticas atualizadas.  
- **Champions** criam cultura de segurança dentro das equipas.  
- **Exercícios práticos** aumentam retenção e prontidão.  
- **Code Clinics estruturadas** garantem aprendizagem visível e replicável.  
- **Threat Modeling peer-led** distribui conhecimento de análise de risco.  
- **Simulações de incidentes** treinam resposta sob pressão e validam processos.  
- **Manutenção periódica de trilhos** garante relevância contínua da formação.  
- **Trilhos proporcionais por risco** garantem adequação de formação a contexto.  
- **Formação de terceiros** reduz risco de falhas por falta de conhecimento e cumpre obrigações regulatórias.  
- **Medição de KPIs** garante melhoria contínua e ligação a objetivos organizacionais.

```
