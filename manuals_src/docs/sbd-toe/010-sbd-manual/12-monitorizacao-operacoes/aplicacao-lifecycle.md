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

**Ligações úteis.** [Monitorização & Operações](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro)

---

### US-03 - Alertas com SLAs definidosUm alerta sem prazo de resposta é apenas ruído.  
Para que a monitorização tenha impacto, é preciso ligar cada alerta a um **compromisso temporal**.  

**Contexto.** Sem SLAs, incidentes críticos não têm resposta garantida.  

:::userstory
**História.**   
Como **Ops**, quero **configurar alertas críticos com SLAs definidos**, para **assegurar resposta atempada a incidentes**.  

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

**Ligações úteis.** [Monitorização & Operações](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro)

---

### US-06 - Classificação e Cobertura de Domínios de Monitorização

Uma abordagem eficaz de monitorização não cobre tudo indiscriminadamente: deve ser **proporcional e focada nos domínios que mais importam** para a segurança e operação de cada aplicação.

**Contexto.** Sem mapeamento claro de domínios, a cobertura fica lacunar e ineficiente.

:::userstory
**História.**  
Como **AppSec/DevOps**, quero **classificar e mapear domínios de monitorização** (técnica, segurança, negócio, conformidade, CI/CD), para **assegurar que a cobertura de logging é proporcional ao risco e abrange fluxos críticos**.

**Critérios de aceitação (BDD).**  
- Dado uma aplicação com classificação de risco  
- Quando mapeio domínios aplicáveis  
- Então defino fontes de dados, ferramentas e retenção para cada domínio  
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
- Dado logs em central  
- Quando aplicadas políticas de proteção  
- Então logs são imutáveis, acesso auditado e integridade verificável  
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
- Dado logs estruturados emitidos  
- Quando enviados para SIEM  
- Então são parseados, normalizados em ECS/formato comum, enriquecidos com contexto  
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
- Dado eventos de múltiplas fontes centralizadas  
- Quando aplicadas regras de correlação  
- Então padrões suspeitos (ex: login + download massivo) geram alertas de severidade elevada  
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
- Dado um alerta configurado  
- Quando é testado  
- Então comporta-se conforme esperado em cenários reais e simulados  
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
- Dado uma aplicação classificada em risco L1, L2 ou L3  
- Quando defino arquitetura de monitorização  
- Então são aplicados os controlos mínimos obrigatórios conforme o nível  
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
- Dado um framework de conformidade aplicável (SSDF, NIS2, ISO 27001)  
- Quando mapéio controlos técnicos (logging, alertas, correlação, IRP, métricas)  
- Então cada controlo técnico é rastreável até um requisito regulatório específico  
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
