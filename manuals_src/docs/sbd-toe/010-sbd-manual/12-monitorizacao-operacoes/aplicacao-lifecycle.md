---
id: aplicacao-lifecycle
title: Como Fazer
description: Integração prática das práticas de monitorização e resposta no ciclo de vida seguro
tags: [tipo:aplicacao, ciclo-vida, monitorizacao, deteccao, operacoes, incidentes]
genia: us-format-normalization
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
- **Dado** código em execução  
  **Quando** ocorre evento relevante  
  **Então** é registado em formato estruturado e enviado ao log central  

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

**Ligações úteis.** [Deploy Seguro](/sbd-toe/sbd-manual/deploy-seguro/intro)  

---

### US-02 - Definição de eventos e métricas críticas

Visibilidade sem contexto gera apenas ruído.  
É fundamental decidir **o que merece ser observado** e quais eventos devem acionar alertas.  

**Contexto.** Sem definição clara, alertas não refletem riscos reais.  

:::userstory
**História.**   
Como **AppSec**, quero **definir eventos e métricas críticas de segurança**, para **assegurar que a monitorização cobre riscos relevantes**.  

**Critérios de aceitação (BDD).**  
- **Dado** sistema em produção  
  **Quando** defino métricas críticas  
  **Então** dashboards refletem riscos reais e alertas são configurados  

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

**Ligações úteis.** [Monitorização & Operações](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro)

---

### US-03 - Alertas com SLAs definidosUm alerta sem prazo de resposta é apenas ruído.  
Para que a monitorização tenha impacto, é preciso ligar cada alerta a um **compromisso temporal**.  

**Contexto.** Sem SLAs, incidentes críticos não têm resposta garantida.  

:::userstory
**História.**   
Como **Ops**, quero **configurar alertas críticos com SLAs definidos**, para **assegurar resposta atempada a incidentes**.  

**Critérios de aceitação (BDD).**  
- **Dado** alerta crítico  
  **Quando** SLA é excedido  
  **Então** incidente é escalado automaticamente  

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
| Produção | Incidente crítico | Ops + AppSec | Conforme SLA |

**Ligações úteis.** [Formação & Onboarding](/sbd-toe/sbd-manual/formacao-onboarding/intro)

---

### US-04 - Integração com processos de resposta a incidentes

A deteção só cria valor quando conduz a uma resposta.  
Alertas isolados não resolvem nada: precisam de estar ligados a **playbooks claros e testados**.  

**Contexto.** Alertas isolados sem IRP tornam-se inúteis.  

:::userstory
**História.**   
Como **Ops**, quero **integrar alertas com playbooks de resposta a incidentes**, para **assegurar ação rápida e coordenada**.  

**Critérios de aceitação (BDD).**  
- **Dado** alerta de segurança  
  **Quando** é confirmado  
  **Então** playbook associado é executado  

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

**Ligações úteis.** [Formação & Onboarding](/sbd-toe/sbd-manual/formacao-onboarding/intro)

---

### US-05 - Métricas de eficácia (MTTD/MTTR)

Só é possível melhorar aquilo que se mede.  
Sem métricas de eficácia, qualquer esforço de monitorização corre o risco de se tornar estático e complacente.  

**Contexto.** Sem medir eficácia, não há melhoria contínua.  

:::userstory
**História.**   
Como **GRC**, quero **medir MTTD e MTTR de incidentes**, para **avaliar eficácia da monitorização e resposta**.  

**Critérios de aceitação (BDD).**  
- **Dado** incidentes registados  
  **Quando** calculo métricas  
  **Então** MTTD e MTTR são reportados periodicamente  

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

**Ligações úteis.** [Monitorização & Operações](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro)

---

### US-06 - Classificação e Cobertura de Domínios de Monitorização

Uma abordagem eficaz de monitorização não cobre tudo indiscriminadamente: deve ser **proporcional e focada nos domínios que mais importam** para a segurança e operação de cada aplicação.

**Contexto.** Sem mapeamento claro de domínios, a cobertura fica lacunar e ineficiente.

:::userstory
**História.**  
Como **AppSec/DevOps**, quero **classificar e mapear domínios de monitorização** (técnica, segurança, negócio, conformidade, CI/CD), para **assegurar que a cobertura de logging é proporcional ao risco e abrange fluxos críticos**.

**Critérios de aceitação (BDD).**  
- **Dado** uma aplicação com classificação de risco  
  **Quando** mapeio domínios aplicáveis  
  **Então** defino fontes de dados, ferramentas e retenção para cada domínio  
- E a cobertura é documentada e validada periodicamente  

**Checklist.**  
- [ ] Mapeamento de domínios por aplicação  
- [ ] Fontes de dados identificadas por domínio  
- [ ] Ferramentas selecionadas (logs app, métricas infra, eventos CI/CD, etc.)  
- [ ] Proporcionalidade ao risco definida  
- [ ] Cobertura revisada anualmente  

:::

**Artefactos & evidências.** Documento de mapeamento de domínios, lista de fontes, matriz de cobertura.

**Proporcionalidade L1–L3.**  
| L1 | L2 | L3 |
|----|----|----|
| Básico (técnica) | Técnica + segurança | Completo (técnica, segurança, negócio, conformidade, CI/CD) |

**Integração no SDLC.**  
| Fase | Trigger | Responsável | SLA |
|------|---------|-------------|-----|
| Design/Planeamento | Classificação da aplicação | AppSec + DevOps | Antes do design |

**Ligações úteis.** [Domínios de Monitorização](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/dominios-monitorizacao)

---

### US-07 - Segurança e Integridade de Logs

Logs são evidência: se forem alteráveis, a evidência perde valor.  
Garantir imutabilidade, acesso auditado e retenção apropriada transforma logs em ativos de segurança e conformidade.

**Contexto.** Logs alteráveis ou perdidos comprometem investigações e auditorias.

:::userstory
**História.**  
Como **DevOps/GRC**, quero **garantir segurança e integridade de logs** (retenção WORM, acesso restrito, assinatura/hash, isolamento de função), para **impedir alteração ou perda de evidência em caso de incidente**.

**Critérios de aceitação (BDD).**  
- **Dado** logs em central  
  **Quando** aplicadas políticas de proteção  
  **Então** logs são imutáveis, acesso auditado e integridade verificável  
- E retenção respeita requisitos regulatórios  

**Checklist.**  
- [ ] Retenção WORM ativada no armazenamento  
- [ ] Acesso a logs restrito e auditado  
- [ ] Hash ou assinatura digital aplicada por lote  
- [ ] Logs separados de aplicação (forwarder, sidecar, serviço)  
- [ ] Retenção mínima: 30d (L1), 90d (L2/L3)  
- [ ] Teste de reversão de retenção trimestralmente  

:::

**Artefactos & evidências.** Configuração de WORM, políticas de acesso, logs de auditoria de acesso, hashes/assinaturas.

**Proporcionalidade L1–L3.**  
| L1 | L2 | L3 |
|----|----|----|
| Local (sem retenção) | WORM + 90d | WORM + 180d + integridade verificável |

**Integração no SDLC.**  
| Fase | Trigger | Responsável | SLA |
|------|---------|-------------|-----|
| Deploy/Operações | Entrada em produção | DevOps + GRC | Imediato |

**Ligações úteis.** [Controlos de Logging Centralizado](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/controles-logging-centralizado)

---

### US-08 - Integração com SIEM e Normalização de Eventos

Logs isolados têm valor limitado.  
Um SIEM com eventos normalizados permite **correlação, busca rápida e deteção automatizada** que seria impossível em silos de dados.

**Contexto.** Logs não integrados em SIEM tornam-se invisíveis operacionalmente.

:::userstory
**História.**  
Como **DevOps/AppSec**, quero **integrar logs com SIEM** (parsing, normalização, enriquecimento), para **permitir correlação eficaz e deteção centralizada de anomalias**.

**Critérios de aceitação (BDD).**  
- **Dado** logs estruturados emitidos  
  **Quando** enviados para SIEM  
  **Então** são parseados, normalizados em ECS/formato comum, enriquecidos com contexto  
- E disponíveis para queries, dashboards e alertas  

**Checklist.**  
- [ ] Forwarder configurado (Filebeat, Fluentbit, Vector)  
- [ ] Canal seguro (TLS 1.2+) com autenticação  
- [ ] Parser/ingest pipeline configurado  
- [ ] Tagging por aplicação/ambiente  
- [ ] Validação de ingestão (volume, latência, formato)  
- [ ] Teste de failover e buffering  

:::

**Artefactos & evidências.** Configuração de forwarder, parsing rules, dashboards SIEM, logs de ingestão.

**Proporcionalidade L1–L3.**  
| L1 | L2 | L3 |
|----|----|----|
| Opcional | Obrigatório | Obrigatório + normalização ECS completa |

**Integração no SDLC.**  
| Fase | Trigger | Responsável | SLA |
|------|---------|-------------|-----|
| Deploy/Operações | Construção de pipeline | DevOps + AppSec | Antes do go-live |

**Ligações úteis.** [Integração SIEM](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/integracao-siem)

---

### US-09 - Correlação de Eventos e Deteção Comportamental

Eventos isolados podem ser inofensivos; padrões de eventos revelam intenções.  
A correlação transforma dados em **inteligência** e permite antecipar ataques ou falhas encadeadas.

**Contexto.** Sem correlação, ataques sofisticados (multi-etapa) permanecem invisíveis.

:::userstory
**História.**  
Como **AppSec/IR**, quero **correlacionar eventos entre múltiplas fontes** (aplicação, infraestrutura, CI/CD) e detetar padrões comportamentais suspeitos, para **antecipar ataques ou falhas encadeadas**.

**Critérios de aceitação (BDD).**  
- **Dado** eventos de múltiplas fontes centralizadas  
  **Quando** aplicadas regras de correlação  
  **Então** padrões suspeitos (ex: login + download massivo) geram alertas de severidade elevada  
- E desvios de baseline por utilizador/IP/role são detetados  

**Checklist.**  
- [ ] Regras de correlação temporal/contextual definidas  
- [ ] Baselines de comportamento por utilizador/role criadas  
- [ ] Janelas temporais para correlação ajustadas (5m, 15m, 1h)  
- [ ] IDs persistentes (user.id, session.id, trace.id) normalizados  
- [ ] Alertas de correlação testados com eventos simulados  
- [ ] Score agregado por utilizador/device/aplicação implementado  

:::

**Artefactos & evidências.** Regras de correlação (SIEM), baselines comportamentais, alertas de correlação testados, documentação de padrões.

**Proporcionalidade L1–L3.**  
| L1 | L2 | L3 |
|----|----|----|
| Não aplicável | Opcional | Obrigatório |

**Integração no SDLC.**  
| Fase | Trigger | Responsável | SLA |
|------|---------|-------------|-----|
| Operações | Após 1 mês de dados em produção | AppSec + IR | Implementação contínua |

**Ligações úteis.** [Correlação de Anomalias](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/correlacao-anomalias)

---

### US-10 - Validação e *Tuning* de Alertas

Um alerta mal calibrado é pior que nenhum alerta: causa ruído e descredibiliza o sistema.  
Validar e afinar alertas é **trabalho contínuo**, não pontual.

**Contexto.** Alertas não validados geram falsos positivos e fadiga de alertas.

:::userstory
**História.**  
Como **AppSec/IR**, quero **validar e afinar alertas** (teste de *trigger*, simulação ativa, replay com dados reais, *tuning* de *thresholds*), para **reduzir falsos positivos e assegurar que alertas refletem risco real**.

**Critérios de aceitação (BDD).**  
- **Dado** um alerta configurado  
  **Quando** é testado  
  **Então** comporta-se conforme esperado em cenários reais e simulados  
- E threshold está ajustado para minimizar falsos positivos  
- E está documentado com runbook associado  

**Checklist.**  
- [ ] Simulação ativa (*trigger* evento em staging)  
- [ ] Unit test de regra (testes automáticos de lógica)  
- [ ] Replay com dados históricos para validação retroativa  
- [ ] Threshold ajustado com base em estatísticas reais  
- [ ] Falsos positivos documentados e causa identificada  
- [ ] Runbook/playbook associado ao alerta  
- [ ] Validação trimestral dos alertas  

:::

**Artefactos & evidências.** Testes de alertas, logs de simulação, relatório de ajustes, runbooks, documentação de falsos positivos.

**Proporcionalidade L1–L3.**  
| L1 | L2 | L3 |
|----|----|----|
| Manual ocasional | Validação periódica | Validação contínua + automação |

**Integração no SDLC.**  
| Fase | Trigger | Responsável | SLA |
|------|---------|-------------|-----|
| Operações | Criação/revisão de alerta | AppSec + IR | Antes de ativação em produção |

**Ligações úteis.** [Alertas e Eventos Críticos](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/alertas-eventos-criticos)

---

### US-11 - Proporcionalidade de Controlos por Risco (L1–L3) e Domínios

Nem todas as aplicações exigem o mesmo nível de monitorização. É fundamental que organizações apliquem controlos de forma proporcional ao risco, garantindo eficiência sem subestimar ameaças.

**Contexto.** Controlos de monitorização devem ser proporcionais ao risco da aplicação, não aplicados indiscriminadamente.

:::userstory
**História.**  
Como **AppSec/GRC**, quero **aplicar controlos de monitorização de forma proporcional ao nível de risco da aplicação**, para **equilibrar custo operacional com cobertura de segurança adequada**.

**Critérios de aceitação (BDD).**  
- **Dado** uma aplicação classificada em risco L1, L2 ou L3  
  **Quando** defino arquitetura de monitorização  
  **Então** são aplicados os controlos mínimos obrigatórios conforme o nível  
- E documentação reflete a matriz de proporcionalidade  
- E exceções (ex: L1 com dados sensíveis) são aprovadas e auditadas  

**Checklist.**  
- [ ] Classificação de risco da aplicação realizada  
- [ ] Matriz de proporcionalidade L1–L3 referenciada  
- [ ] Controlos mínimos por nível identificados (logging, retenção, alertas, SIEM, correlação)  
- [ ] Justificação de exceções documentada se aplicável  
- [ ] Revisão anual de proporcionalidade agendada  
- [ ] Rastreabilidade entre classificação → controlos aplicados  

:::

**Artefactos & evidências.**  
Documento de classificação de risco, matriz de proporcionalidade com controlos selecionados, justificação de exceções, revisão anual documentada.

**Proporcionalidade L1–L3.**  
| L1 | L2 | L3 |
|----|----|----|
| Logging local + mapeamento de domínios básico | Matriz aplicada; SIEM e alertas implementados | Matriz aplicada + revisão contínua com métricas |

**Integração no SDLC.**  
| Fase | Trigger | Responsável | SLA |
|------|---------|-------------|-----|
| Design/Risco | Classificação da aplicação | AppSec + GRC | Antes do design |

**Ligações úteis.**  
[Matriz de Controlos por Risco](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/matriz-controles-por-risco)

---

### US-12 - Rastreabilidade e Conformidade com Regulações (SSDF, NIS2, ISO 27001)

A monitorização não é um exercício técnico isolado: é um requisito regulatório cada vez mais exigente. Deve existir rastreabilidade clara entre controlos técnicos e requisitos regulatórios, com evidência auditável.

**Contexto.** Sem rastreabilidade regulatória, postura de segurança fica desalinhada com conformidade.

:::userstory
**História.**  
Como **GRC/Auditoria**, quero **documentar e demonstrar conformidade entre controlos de monitorização e requisitos regulatórios** (SSDF, NIS2, ISO 27001), para **assegurar que a postura de segurança está alinhada com regulações**.

**Critérios de aceitação (BDD).**  
- **Dado** um framework de conformidade aplicável (SSDF, NIS2, ISO 27001)  
  **Quando** mapéio controlos técnicos (logging, alertas, correlação, IRP, métricas)  
  **Então** cada controlo técnico é rastreável até um requisito regulatório específico  
- E existe evidência auditável (logs, dashboards, relatórios, métricas)  
- E relatórios de conformidade são gerados trimestralmente  

**Checklist.**  
- [ ] Mapeamento de controlo técnico → requisito regulatório criado e versionado  
- [ ] Matriz de rastreabilidade (ex: US-01 Logging → ISO 27001 A.12.4.1)  
- [ ] Evidência técnica documentada (screenshots, logs, configurações)  
- [ ] Métricas de compliance (% de controls active, MTTD vs alvo, etc.)  
- [ ] Relatórios trimestrais gerados e revistos por auditoria  
- [ ] Gaps identificados e plano de remediação criado  
- [ ] Auditorias internas agendadas (anual)  

:::

**Artefactos & evidências.**  
Matriz de rastreabilidade (controlo → regulação), evidência técnica por controlo, relatórios de conformidade trimestrais, métricas de compliance, plano de remediação, relatórios de auditoria interna.

**Proporcionalidade L1–L3.**  
| L1 | L2 | L3 |
|----|----|----|
| Mapeamento básico | Mapeamento + evidência documentada | Mapeamento + evidência + métricas + auditoria contínua |

**Integração no SDLC.**  
| Fase | Trigger | Responsável | SLA |
|------|---------|-------------|-----|
| Conformidade | Requisito regulatório, auditoria | GRC + Auditoria Interna | Trimestral |

**Ligações úteis.**  
[Monitorização & Operações](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro); [Requisitos de Segurança](/sbd-toe/sbd-manual/requisitos-seguranca/intro) (requisitos)

---

### US-25 - Decisão Estruturada em Resposta a Alertas (Separação Sugestão/Decisão)

Sem um framework claro de aprovação, alertas disparam e geram resposta automática ou caótica, sem contexto humano estruturado.

**Contexto.** Alertas necessitam separação clara entre detecção automática (sugestão) e aprovação humana (decisão de ação).

:::userstory
**História.**  
Como **On-Call Engineer / Ops Lead**, quero **documentar e executar um processo de decisão estruturado para resposta a alertas** (checklist de validação, decisão com 4 opções claras, escalation em caso de conflito), para **assegurar que cada resposta a incidente é conscientemente aprovada por autoridade competente**.

**Critérios de aceitação (BDD).**  
- **Dado** um alerta de segurança/operacional disparado  
  **Quando** iniciamos processo de resposta  
  **Então**:
    - Checklist D1 com 4 perguntas críticas é preenchido (alerta é válido? impacto é real? remédio é testado? timing é apropriado?)
    - Response template R1 com 4 opções é explícito: REMEDIATE-NOW / ESCALATE-INVESTIGATE / DEFER-MONITOR / FALSE-POSITIVE
    - Se conflito entre Ops e Security (ex: "remediemos agora" vs. "investigar primeiro"), escalation template E1 documenta posições e resolução
    - Decisor qualificado (por matriz L1/L2/L3 × severidade) assina decisão com justificativa

**Checklist.**  
- [ ] Matriz de decisores definida (quem aprova o quê em função de L1/L2/L3 × severidade)  
- [ ] Checklist D1 com 4 perguntas preenchido antes de R1 (para >90% de alertas)  
- [ ] Template R1 com 4 opções e justificativa documentado  
- [ ] Template E1 de escalation ready para conflitos  
- [ ] SLA de decisão definido (CRÍTICA: 1h, ALTA: 4h, MÉDIA: 24h)  
- [ ] Decisor autorizado e treinado no processo  
- [ ] Rastreio de todas as decisões (D1, R1, E1) em auditoria  
- [ ] KPIs monitorados: % alertas com D1, tempo D1→R1, rate escalations, remediation success  

:::

**Artefactos & evidências.**  
Checklist D1 preenchido por alerta, Response Template R1 assinado, Escalation logs (quando E1 foi usado), Matriz de decisores versionada, KPI dashboard (time-to-decision, remediation success rate, escalation rate).

**Proporcionalidade L1–L3.**  
| L1 | L2 | L3 |
|----|----|----|
| D1 + R1 manual, todas 4 Q's = SIM | D1 com tolerância INCERTO se mitigado, R1 com 4 opções | D1 com tolerância para riscos monitoráveis, R1 preferência REMEDIATE-NOW |
| Escalation moderado | Escalation moderado | Escalation raro (confiança alta) |

**Integração no SDLC.**  
| Fase | Trigger | Responsável | SLA |
|------|---------|-------------|-----|
| Resposta a Alerta | Alerta disparado, confirmado válido | On-Call / Ops Lead | CRÍTICA: 1h, ALTA: 4h, MÉDIA: 24h |

**Ligações úteis.** [Addon 11: Framework de Decisão para Alertas](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/addon-11-alerta-decisao-cap12); [Cap 11-US-23: Deploy com Decisão Estruturada](/sbd-toe/sbd-manual/deploy-seguro/aplicacao-lifecycle#us-23---deploy-com-decisão-estruturada-separação-sugestãodecisão)

---

### US-26 - Tuning Empírico de Alertas (Evidência acima de Plausibilidade)

Alertas podem ser configurados teoricamente mas falhar em produção: falsos positivos causam alert fatigue, falsos negativos deixam ameaças passar.

**Contexto.** Decidir sobre resposta a alerta baseado apenas em configuração estática é insuficiente; validação empírica em produção é crítica.

:::userstory
**História.**  
Como **Security / Operations**, quero **executar framework de tuning empírico para alertas** (estabelecer baseline de produção, gerar ameaças teste, validar detecção, medir FP/FN, tuning contínuo), para **confirmar que alertas detectam ameaças reais em produção, não apenas baseadas em configuração teórica**.

**Critérios de aceitação (BDD).**  
- **Dado** um conjunto de alertas configurados  
  **Quando** executamos framework de 5 fases (P1-P5)  
  **Então**:
    - P1 (Baseline): Recolhemos p50/p95/p99 de produção normal (2-4 semanas)
    - P2 (Synthetic tests): Geramos 5-10 tipos de ameaça, validamos alertas disparam
    - P3 (Production validation): Executamos testes em canary (1% traffic), medimos latências
    - P4 (FP measurement): Recolhemos alertas reais, classificamos TP/FP, calculamos taxa
    - P5 (Continuous tuning): Monthly review, whitelist + rule tuning baseado em dados
  - E caso FP/FN descoberto:
    - V1 template: FP (alerta disparou, não era ameaça) → documentar, tuning
    - V2 template: FN (ameaça real, alerta não disparou) → RCA, melhoria

**Checklist.**  
- [ ] P1: Baseline recolhido de 2-4 semanas clean, p50/p95/p99 documentados  
- [ ] P2: 5-10 cenários de ameaça definidos e testados em staging  
- [ ] P3: Testes executados em canary production, latências de detecção medidas  
- [ ] P4: Alertas reais de 1 semana classificados TP/FP, taxa de FP calculada  
- [ ] P5: Monthly alert review, tuning log documentado (whitelist, thresholds, rules)  
- [ ] V1/V2: Templates preenchidos quando FP/FN descobertos  
- [ ] Métricas: FP rate, FN rate, alert accuracy, detection latency monitorados  
- [ ] Quarterly synthetic test re-run para revalidação  

:::

**Artefactos & evidências.**  
Baseline document (p50/p95/p99), P2 synthetic test scenarios + results, P3 canary test logs (latencies), P4 FP/FN classification report, P5 monthly alert metrics + tuning changes, V1/V2 RCA templates (when FP/FN found), KPI dashboard (FP rate, alert accuracy, detection latency).

**Proporcionalidade L1–L3.**  
| L1 | L2 | L3 |
|----|----|----|
| P1-P5 manual, baseline simple, tests quarterly | P1-P5 semi-automated, baseline detailed, tests monthly | P1-P5 automated, continuous baseline, tests weekly/continuous |
| Tolerância FP rate: 20% | Tolerância FP rate: 10% | Tolerância FP rate: 5% |
| Monthly tuning review | Monthly tuning review | Continuous tuning + ML suggestions |

**Integração no SDLC.**  
| Fase | Trigger | Responsável | SLA |
|------|---------|-------------|-----|
| Tuning / Maintenance | Alerta disparado (validação), revisão periódica | AppSec + Ops | Monthly review, Quarterly tests |

**Ligações úteis.** [Addon 12: Tuning Empírico de Alertas](/sbd-toe/sbd-manual/monitorizacao-operacoes/addon/addon-12-empirical-alert-tuning-cap12); [Cap 10-US-22: Validação Empírica de Achados](/sbd-toe/sbd-manual/testes-seguranca/aplicacao-lifecycle#us-22---validação-empírica-achados-de-teste)

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
| Mapeamento de domínios | Documento de cobertura por domínio |
| Configuração WORM e integridade | Logs imutáveis + hashes/assinaturas |
| Configuração de forwarder e SIEM | Parsing rules + dashboards SIEM |
| Regras de correlação | Baselines comportamentais + alertas correlacionados |
| Testes de alertas | Simulações, unit tests, relatórios de *tuning* |
| Matriz de proporcionalidade L1–L3 | Controlos aplicados por nível + justificações |
| Rastreabilidade regulatória | Matriz de mapeamento controlo → regulação + evidência auditável |

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
| Domínios de monitorização | Técnica apenas | Técnica + segurança | Completo (técnica, segurança, negócio, conformidade, CI/CD) |
| Segurança de logs | Básico | WORM + acesso controlado | WORM + assinatura + isolamento de função |
| Integração SIEM | Opcional | Forwarder configurado | SIEM + parsing + dashboards |
| Correlação comportamental | Não aplicável | Opcional | Obrigatório |
| Validação de alertas | Manual ocasional | Periódica | Contínua + automação |
| Proporcionalidade por domínio | Logging local + mapeamento básico | Matriz aplicada; SIEM e alertas implementados | Matriz aplicada + revisão contínua com métricas |
| Rastreabilidade regulatória | Mapeamento básico | Mapeamento + evidência documentada | Mapeamento + evidência + métricas + auditoria contínua |

---

## 🏁 Recomendações finais

- **Visibilidade é chave**: sem logging e métricas, não há segurança em produção.  
- **Alertas devem ser acionáveis**: sem SLAs e playbooks, apenas geram ruído.  
- **Proporcionalidade importa**: L1 foca no essencial, L3 exige automação e metas.  
- **Integração com IRP**: deteção sem resposta não traz valor.  
- **Medição contínua**: métricas MTTD/MTTR permitem aprender e evoluir.  
