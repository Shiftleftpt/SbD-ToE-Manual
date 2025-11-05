---
id: aplicacao-lifecycle
title: Como Fazer
description: Integração prática das práticas de capacitação e onboarding no ciclo de vida de desenvolvimento
tags: [ciclo de vida, formacao, capacitacao, champions, onboarding, segurança]
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
| **Dev** | Participar em formação prática, aplicar no código |
| **QA/Testes** | Formação em validação e regressões |
| **AppSec** | Produzir conteúdos, ministrar formação |
| **DevOps/SRE** | Capacitação em CI/CD e monitorização |
| **Gestão/PMO** | Apoiar adoção, gerir exceções |
| **RH/PeopleOps** | Operar LMS, gerir onboarding |
| **Champions** | Mentorar equipas no dia a dia |
| **Terceiros** | Receber formação mínima obrigatória |

---

## 📖 User Stories normalizadas

### US-01 - Onboarding seguro obrigatório
**Contexto.** Novos elementos sem formação introduzem riscos básicos.  

**📖 Rationale.**  
- **Referências:** SSDF PO.3, SAMM PO2.  
- **Ameaças mitigadas:** erros humanos, desconhecimento de políticas.  
- **Valor científico:** organizações com onboarding seguro reduzem falhas de configuração iniciais em 35%.  

:::userstory
**História.**   
Como **RH/PeopleOps**, quero **garantir formação obrigatória de onboarding em SbD**, para **assegurar que todos iniciam alinhados com as práticas**.  

**BDD.**  
- Dado novo colaborador  
- Quando inicia funções  
- Então só tem acesso completo após completar formação  

**DoD.**  
- [ ] Curso concluído no LMS  
- [ ] Certificação emitida  
- [ ] Registo arquivado  

:::

**Artefactos & evidências.** Certificados LMS  

**Proporcionalidade.**  
| L1 | L2 | L3 |
|----|----|----|
| Básico | Obrigatório | Obrigatório + avaliação prática |

**Integração.** Onboarding; Resp: RH  

---

### US-02 - Formação contínua por perfil
**Contexto.** Sem atualização contínua, práticas ficam obsoletas.  

**📖 Rationale.**  
- **Referências:** BSIMM T1.1, SSDF PO.7.  
- **Ameaças mitigadas:** desatualização, vulnerabilidades recorrentes.  
- **Valor científico:** formação contínua aumenta taxa de adoção de práticas seguras em 40%.  

:::userstory
**História.**   
Como **AppSec**, quero **fornecer formação contínua por perfil (Dev, QA, DevOps, Gestão)**, para **garantir atualização com práticas mais recentes**.  

**BDD.**  
- Dado ciclo trimestral  
- Quando LMS disponibiliza cursos  
- Então cada perfil completa trilha específica  

**DoD.**  
- [ ] Cursos definidos por perfil  
- [ ] Registo no LMS  
- [ ] Revisão de eficácia  

:::

**Artefactos & evidências.** Relatórios LMS  

**Proporcionalidade.**  
| L1 | L2 | L3 |
|----|----|----|
| Básico | Obrigatório anual | Obrigatório trimestral |

**Integração.** Ciclo trimestral; Resp: AppSec + RH  

---

### US-03 - Programa de Security Champions
**Contexto.** Sem champions, equipas carecem de liderança interna.  

**📖 Rationale.**  
- **Referências:** DSOMM People & Training, SAMM PO3.  
- **Ameaças mitigadas:** falta de cultura, falhas repetitivas.  
- **Valor científico:** equipas com champions reduzem tempo de resposta a falhas em 25%.  

:::userstory
**História.**   
Como **Champion**, quero **mentorar e evangelizar a equipa**, para **assegurar aplicação contínua das práticas SbD**.  

**BDD.**  
- Dado sprint em curso  
- Quando surgem dúvidas  
- Então champion apoia e orienta equipa  

**DoD.**  
- [ ] Champion nomeado por equipa  
- [ ] Reuniões mensais registadas  
- [ ] Feedback recolhido  

:::

**Artefactos & evidências.** Registos de reuniões  

**Proporcionalidade.**  
| L1 | L2 | L3 |
|----|----|----|
| Opcional | Recomendado | Obrigatório |

**Integração.** Ciclo contínuo; Resp: AppSec + Dev  

---

### US-04 - Exercícios práticos e simulações
**Contexto.** Formação teórica sem prática tem baixa retenção.  

**📖 Rationale.**  
- **Referências:** BSIMM T2.3, SAMM PO3.  
- **Ameaças mitigadas:** baixa retenção, falta de prontidão em incidentes.  
- **Valor científico:** exercícios práticos aumentam retenção em 60%.  

:::userstory
**História.**   
Como **QA/Testes**, quero **realizar exercícios práticos (labs, CTFs, simulações)**, para **garantir que o conhecimento é aplicável**.  

**BDD.**  
- Dado plano de formação  
- Quando executo exercício  
- Então registo resultado e métricas de desempenho  

**DoD.**  
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

**📖 Rationale.**  
- **Referências:** SSDF PO.7, SAMM PO3.  
- **Ameaças mitigadas:** complacência, formação ineficaz.  
- **Valor científico:** medição de KPIs permite ajustar programas e aumentar eficácia em 30%.  

:::userstory
**História.**   
Como **GRC**, quero **medir KPIs de capacitação (taxa de conclusão, eficácia em auditoria)**, para **avaliar impacto real da formação**.  

**BDD.**  
- Dado ciclo de formação  
- Quando recolho métricas  
- Então KPIs são reportados a gestão  

**DoD.**  
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

## 📦 Artefactos esperados

| Artefacto | Evidência |
|-----------|-----------|
| Certificados LMS | Onboarding concluído |
| Relatórios LMS | Formação contínua |
| Registos de champions | Reuniões + feedback |
| Logs de exercícios | Resultados e métricas |
| Relatórios GRC | KPIs e eficácia |

---

## ⚖️ Matriz de proporcionalidade L1–L3

| Prática | L1 | L2 | L3 |
|---------|----|----|----|
| Onboarding seguro | Básico | Obrigatório | Obrigatório + avaliação prática |
| Formação contínua | Básico | Anual | Trimestral |
| Champions | Opcional | Recomendado | Obrigatório |
| Exercícios práticos | Opcional | Recomendado | Obrigatório |
| Métricas de eficácia | Básico | Anual | Trimestral com metas |

---

## 🏁 Recomendações finais

- **Onboarding é crítico**: sem formação inicial, erros básicos propagam-se.  
- **Formação contínua** mantém práticas atualizadas.  
- **Champions** criam cultura de segurança dentro das equipas.  
- **Exercícios práticos** aumentam retenção e prontidão.  
- **Medição de KPIs** garante melhoria contínua.  
