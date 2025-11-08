---
id: aplicacao-lifecycle
title: Como Fazer
description: Integração prática das práticas de monitorização e resposta no ciclo de vida seguro
tags: [ciclo de vida, monitorizacao, deteção, operações, incidentes]
sidebar_position: 15
---

# 👁️ Aplicação de Monitorização & Operações no Ciclo de Vida

## 🧭 Quando aplicar

Monitorizar e operar em segurança não é uma atividade pontual: é um fio condutor que deve estar presente em todas as fases do ciclo de vida.  
Desde a primeira linha de código até à revisão de auditoria, a aplicação precisa de gerar visibilidade, suportar deteção e permitir resposta coordenada.  

A tabela seguinte mostra **os momentos críticos em que cada controlo deve ser aplicado** e a forma como pode ser evidenciado:

| Fase / Evento | Ação esperada | Evidência |
|---------------|---------------|-----------|
| Desenvolvimento | Instrumentação de código com métricas e logs | Código + logs de dev |
| QA/Staging | Validação de geração de eventos e alertas | Relatórios QA |
| Deploy | Configuração de pipelines de logging e métricas | Logs centralizados |
| Produção | Monitorização contínua + alertas | Dashboards + alertas |
| Incidente | Execução de playbooks IRP | Relatórios de resposta |
| Auditoria | Revisão de métricas (MTTD/MTTR) | Relatórios GRC |

---

## 👥 Quem executa cada ação

Monitorização e operações seguras exigem responsabilidades bem distribuídas.  
Não basta que uma equipa “tenha logs”: cada papel deve assumir uma função clara na criação, validação e reação aos eventos.  

| Papel | Responsabilidade |
|-------|------------------|
| **Dev** | Expor métricas e logs estruturados |
| **QA/Testes** | Validar geração de eventos e thresholds |
| **AppSec** | Definir eventos críticos e monitorizar alertas |
| **DevOps/SRE** | Configurar pipelines e dashboards |
| **Resposta a Incidentes (IR)** | Analisar alertas e executar playbooks |
| **GRC** | Rever métricas e garantir conformidade |

---

## 📖 User Stories Reutilizáveis

As histórias de utilizador seguintes traduzem os princípios do capítulo em práticas concretas.  
Cada uma reflete situações reais de risco e as medidas necessárias para garantir visibilidade, deteção e resposta.

### US-01 - Logging estruturado e centralizado

O primeiro passo para uma operação segura é **garantir visibilidade**.  
Sem logs consistentes e centralizados, qualquer investigação começa às cegas.  

**Contexto.** Logs dispersos e não normalizados dificultam a deteção de incidentes.  

:::userstory
**História.**   
Como **Dev**, quero **gerar logs estruturados e centralizados**, para **assegurar visibilidade completa em incidentes**.  

**Critérios de aceitação (BDD).**  
- Dado código em execução  
- Quando ocorre evento relevante  
- Então é registado em formato estruturado e enviado ao log central  

**Checklist.**  
- [ ] Logs em formato JSON/ECS  
- [ ] Pipeline de centralização configurado  
- [ ] Retenção conforme política  

:::

**Artefactos & evidências.** Logs centralizados.  

**Proporcionalidade L1–L3.**  
| L1 | L2 | L3 |
|----|----|----|
| Básico | Estruturado | Estruturado + correlação em SIEM |

**Integração no SDLC.**  
| Fase | Trigger | Responsável | SLA |
|------|---------|-------------|-----|
| Desenvolvimento/Deploy | Execução de código | Dev + DevOps | Contínuo |

**Ligações úteis.** xref:sbd-toe:cap11:intro  

---

### US-02 - Definição de eventos e métricas críticas

Visibilidade sem contexto gera apenas ruído.  
É fundamental decidir **o que merece ser observado** e quais eventos devem acionar alertas.  

**Contexto.** Sem definição clara, alertas não refletem riscos reais.  

:::userstory
**História.**   
Como **AppSec**, quero **definir eventos e métricas críticas de segurança**, para **assegurar que a monitorização cobre riscos relevantes**.  

**Critérios de aceitação (BDD).**  
- Dado sistema em produção  
- Quando defino métricas críticas  
- Então dashboards refletem riscos reais e alertas são configurados  

**Checklist.**  
- [ ] Lista de eventos críticos aprovada  
- [ ] Dashboards configurados  
- [ ] Alertas testados  

:::

**Artefactos & evidências.** Lista de eventos + dashboards.  

**Proporcionalidade L1–L3.**  
| L1 | L2 | L3 |
|----|----|----|
| Básico | Definição parcial | Definição completa + revisão trimestral |

**Integração no SDLC.**  
| Fase | Trigger | Responsável | SLA |
|------|---------|-------------|-----|
| Planeamento/Operações | Entrada em produção | AppSec | Trimestral |

**Ligações úteis.** xref:sbd-toe:cap12:intro  

---

### US-03 - Alertas com SLAs definidos

Um alerta sem prazo de resposta é apenas ruído.  
Para que a monitorização tenha impacto, é preciso ligar cada alerta a um **compromisso temporal**.  

**Contexto.** Sem SLAs, incidentes críticos não têm resposta garantida.  

:::userstory
**História.**   
Como **IR**, quero **configurar alertas críticos com SLAs definidos**, para **assegurar resposta atempada a incidentes**.  

**Critérios de aceitação (BDD).**  
- Dado alerta crítico  
- Quando SLA é excedido  
- Então incidente é escalado automaticamente  

**Checklist.**  
- [ ] SLAs documentados  
- [ ] Alertas configurados  
- [ ] Escalonamento testado  

:::

**Artefactos & evidências.** Configuração de alertas + relatórios SLA.  

**Proporcionalidade L1–L3.**  
| L1 | L2 | L3 |
|----|----|----|
| Aviso | SLA crítico | SLA crítico + automação |

**Integração no SDLC.**  
| Fase | Trigger | Responsável | SLA |
|------|---------|-------------|-----|
| Produção | Incidente crítico | IR + AppSec | Conforme SLA |

**Ligações úteis.** xref:sbd-toe:cap13:intro  

---

### US-04 - Integração com processos de resposta a incidentes

A deteção só cria valor quando conduz a uma resposta.  
Alertas isolados não resolvem nada: precisam de estar ligados a **playbooks claros e testados**.  

**Contexto.** Alertas isolados sem IRP tornam-se inúteis.  

:::userstory
**História.**   
Como **IR**, quero **integrar alertas com playbooks de resposta a incidentes**, para **assegurar ação rápida e coordenada**.  

**Critérios de aceitação (BDD).**  
- Dado alerta de segurança  
- Quando é confirmado  
- Então playbook associado é executado  

**Checklist.**  
- [ ] Playbooks definidos  
- [ ] Integração com SIEM/SOAR  
- [ ] Execução validada  

:::

**Artefactos & evidências.** Playbooks + logs SOAR.  

**Proporcionalidade L1–L3.**  
| L1 | L2 | L3 |
|----|----|----|
| Manual | Playbooks definidos | Playbooks automatizados |

**Integração no SDLC.**  
| Fase | Trigger | Responsável | SLA |
|------|---------|-------------|-----|
| Operações | Alerta confirmado | IR | ≤ 30 min |

**Ligações úteis.** xref:sbd-toe:cap13:intro  

---

### US-05 - Métricas de eficácia (MTTD/MTTR)

Só é possível melhorar aquilo que se mede.  
Sem métricas de eficácia, qualquer esforço de monitorização corre o risco de se tornar estático e complacente.  

**Contexto.** Sem medir eficácia, não há melhoria contínua.  

:::userstory
**História.**   
Como **GRC**, quero **medir MTTD e MTTR de incidentes**, para **avaliar eficácia da monitorização e resposta**.  

**Critérios de aceitação (BDD).**  
- Dado incidentes registados  
- Quando calculo métricas  
- Então MTTD e MTTR são reportados periodicamente  

**Checklist.**  
- [ ] Métricas definidas  
- [ ] Cálculo automático  
- [ ] Relatórios trimestrais  

:::

**Artefactos & evidências.** Relatórios de métricas.  

**Proporcionalidade L1–L3.**  
| L1 | L2 | L3 |
|----|----|----|
| Básico | Métricas calculadas | Métricas + metas definidas |

**Integração no SDLC.**  
| Fase | Trigger | Responsável | SLA |
|------|---------|-------------|-----|
| Auditoria | Revisão periódica | GRC | Trimestral |

**Ligações úteis.** xref:sbd-toe:cap12:intro  

---

## 📦 Artefactos esperados

Cada prática deixa rastos verificáveis.  
Estes artefactos constituem a evidência objetiva que sustenta auditorias e conformidade regulatória:  

| Artefacto | Evidência |
|-----------|-----------|
| Logs estruturados | JSON/ECS centralizados |
| Lista de eventos críticos | Documento versionado |
| Configuração de alertas | Dashboards + relatórios |
| Playbooks IRP | Documento + logs SOAR |
| Relatórios métricas | Relatórios GRC |

---

## ⚖️ Matriz de proporcionalidade L1–L3

Nem todas as aplicações têm o mesmo risco ou exigem o mesmo esforço.  
A matriz seguinte traduz os controlos em níveis proporcionais (L1–L3), equilibrando custo e impacto:  

| Prática | L1 | L2 | L3 |
|---------|----|----|----|
| Logging | Básico | Estruturado | Estruturado + SIEM |
| Eventos críticos | Básico | Definição parcial | Completa + revisão trimestral |
| Alertas | Aviso | SLA crítico | SLA crítico + automação |
| Integração IRP | Manual | Playbooks definidos | Playbooks automatizados |
| Métricas | Básico | Calculadas | Calculadas + metas |

---

## 🏁 Recomendações finais

- **Visibilidade é chave**: sem logging e métricas, não há segurança em produção.  
- **Alertas devem ser acionáveis**: sem SLAs e playbooks, apenas geram ruído.  
- **Proporcionalidade importa**: L1 foca no essencial, L3 exige automação e metas.  
- **Integração com IRP**: deteção sem resposta não traz valor.  
- **Medição contínua**: métricas MTTD/MTTR permitem aprender e evoluir.  
