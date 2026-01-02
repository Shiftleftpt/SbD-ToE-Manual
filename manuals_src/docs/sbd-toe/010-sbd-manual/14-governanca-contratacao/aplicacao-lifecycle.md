---
id: aplicacao-lifecycle
title: Como Fazer
description: Integração prática das práticas de governação, exceções e contratação no ciclo de vida SbD-ToE
tags: [tipo:aplicacao, ciclo-vida, governanca, contratacao, excecoes, rastreabilidade]
genia: us-format-normalization
---

# 🏛️ Aplicação de Governança & Contratação no Ciclo de Vida

## 🧭 Quando aplicar

| Fase / Evento | Ação esperada | Evidência |
|---------------|--------------|-----------|
| Planeamento | Definir cláusulas contratuais e métricas | Documentos aprovados |
| Execução | Registar exceções, aplicar cláusulas em fornecedores | Registo GRC |
| Validação | Auditorias a fornecedores, revisões de exceções | Relatórios de auditoria |
| Operações | Reporting contínuo de KPIs | Dashboards |
| Auditoria | Revisão organizacional | Relatório consolidado |

---

## 👥 Quem executa cada ação

| Papel | Responsabilidade |
|-------|------------------|
| **Dev** | Registar exceções e cumprir políticas |
| **AppSec** | Validar exceções, supervisionar rastreabilidade |
| **DevOps/SRE** | Assegurar execução técnica conforme cláusulas |
| **Gestão/PMO** | Aprovar risco residual |
| **Jurídico/Procurement** | Integrar cláusulas de segurança em contratos |
| **GRC** | Consolidar métricas e auditar fornecedores |

---

## 📖 User Stories normalizadas

### US-01 - Processo formal de exceções com alçadas por nível de risco
**Contexto.** Sem exceções formais, práticas são ignoradas sem transparência. Sem alçadas claras por nível de risco, decisões são inconsistentes e responsabilidade dispersa.  

:::userstory
**História.**   
Como **Dev + AppSec Engineer**, quero **submeter exceções de segurança em fluxo formal com roteamento automático por nível de risco (L1→gestor app, L2→AppSec+gestor, L3→CISO+AppSec+direção)**, para **assegurar transparência, aprovação proporcional ao risco, e revalidação periódica**.  

**Critérios de aceitação (BDD).**  
- **Dado** que um controlo não pode ser cumprido numa aplicação classificada como L1, L2 ou L3  
  **Quando** submeto exceção com justificação técnica e compensação  
  **Então** ela é roteada para alçada apropriada, avaliada, e aprovada ou rejeitada  
- E um calendário de revalidação é automaticamente criado (L3: 3 meses, L2: 6 meses, L1: anual)  

**Critérios de aceitação (DoD).**  
- [ ] Exceção registada em ferramenta GRC com campos obrigatórios: aplicação, risco (L1–L3), controlo em falta, justificação, compensação, owner  
- [ ] Alçada de aprovação determinada automaticamente por nível de risco  
- [ ] Aprovação formal recebida (assinatura digital ou registo de timestamp)  
- [ ] Calendário de revalidação criado e owner notificado (30 dias antes de expiração)  
- [ ] Issue de mitigação criada no backlog de segurança para próxima release  
- [ ] Notificação automática enviada a owner se exceção se aproxima de vencer  

:::

**Artefactos & evidências.** Registo exceções versionado, Decisão formalizada com alçada, Calendário de revalidação, Issue no backlog, Notificações automáticas  

**Proporcionalidade.**  
| L1 | L2 | L3 |
|----|----|----|
| Opcional | Recomendado | Obrigatório |

**Integração.** Execução contínua; Resp: Dev (submissão) + AppSec Engineer (validação) + Gestão/CISO (aprovação conforme nível); Triggers: Sempre que há desvio; SLA: Aprovação em 5 dias (L1–L2), 3 dias (L3); Notificação de revalidação 30 dias antes do vencimento  

---

### US-02 - Cláusulas contratuais de segurança
**Contexto.** Fornecedores sem cláusulas podem comprometer toda a cadeia.  

:::userstory
**História.**   
Como **Jurídico/Procurement**, quero **incluir cláusulas SbD-ToE em contratos**, para **garantir conformidade de fornecedores**.  

**Critérios de aceitação (BDD).**  
- **Dado** contrato novo  
  **Quando** cláusulas são aplicadas  
  **Então** fornecedor compromete-se a cumprir práticas de segurança  

**Critérios de aceitação (DoD).**  
- [ ] Cláusulas publicadas em modelo contratual  
- [ ] Contratos validados juridicamente  
- [ ] Monitorização de conformidade  

:::

**Artefactos & evidências.** Contratos, cláusulas  

**Proporcionalidade.**  
| L1 | L2 | L3 |
|----|----|----|
| Recomendado | Obrigatório | Obrigatório + auditorias |

**Integração.** Planeamento; Resp: Jurídico + Procurement  

---

### US-03 - Validação contínua de fornecedores
**Contexto.** Fornecedores comprometidos propagam risco.  

:::userstory
**História.**   
Como **GRC**, quero **validar fornecedores de forma contínua**, para **assegurar conformidade e segurança contratual**.  

**Critérios de aceitação (BDD).**  
- **Dado** fornecedor ativo  
  **Quando** auditoria ocorre  
  **Então** relatório documenta conformidade  

**Critérios de aceitação (DoD).**  
- [ ] Auditoria anual  
- [ ] Relatório publicado  
- [ ] Findings registados  

:::

**Artefactos & evidências.** Relatórios de auditoria  

**Proporcionalidade.**  
| L1 | L2 | L3 |
|----|----|----|
| Opcional | Recomendado | Obrigatório |

**Integração.** Validação; Resp: GRC  

---

### US-04 - Rastreabilidade organizacional
**Contexto.** Sem rastreabilidade, a gestão não tem visibilidade real.  

:::userstory
**História.**   
Como **AppSec**, quero **agregar práticas de segurança por projeto em dashboard organizacional**, para **dar visibilidade e medir adoção**.  

**Critérios de aceitação (BDD).**  
- **Dado** projetos ativos  
  **Quando** métricas são recolhidas  
  **Então** dashboard mostra estado global  

**Critérios de aceitação (DoD).**  
- [ ] Dashboard configurado  
- [ ] Métricas por capítulo recolhidas  
- [ ] Relatórios entregues à direção  

:::

**Artefactos & evidências.** Dashboard, relatórios  

**Proporcionalidade.**  
| L1 | L2 | L3 |
|----|----|----|
| Básico | Recomendado | Obrigatório |

**Integração.** Operações; Resp: AppSec + GRC  

---

## 📊 Matriz de Rastreabilidade Global

A tabela seguinte consolida as práticas de rastreabilidade aplicadas em cada capítulo, mostrando o ponto focal para auditoria e governação:

| Capítulo | US | Contexto | Artefacto principal | Responsável |
|----------|----|---------|--------------------|-------------|
| **Cap 02** | US-07 | Requisitos com tags `SEC-Lx-*` | Backlog com rastreabilidade | QA / PO |
| **Cap 07** | US-03 | Logs e correlação commit-build-release | Relatórios CI/CD + audit trail | DevOps/SRE |
| **Cap 08** | US-02 | Módulos versionados e rastreáveis | Histórico de módulos IaC | DevOps/IaC Lead |
| **Cap 09** | US-06 | SBOM com proveniência por imagem | `sbom.json` + metadados | DevOps |
| **Cap 11** | US-02 | Rastreabilidade ponta-a-ponta (build → deploy → runtime) | Attestations + logs de deploy | DevOps/SRE |
| **Cap 12** | US-01 | Eventos de segurança correlacionados | Eventos + logs SIEM | SOC / AppSec |
| **Cap 14** | US-04 | Dashboard organizacional de métricas | Dashboard + relatórios trimestrais | AppSec + GRC |

**Notas:**
- Cada capítulo tem **um ponto focal de rastreabilidade** que se integra na matriz organizacional
- **Cap 14 - US-04** agrega dados de todos os capítulos para visibilidade executiva
- Todos os artefactos devem ser **versionados** e **auditáveis** conforme nível L1–L3
- **SLA mínimo:** Relatórios mensais (L1), quinzenais (L2), contínuos (L3)

---

### US-05 - KPIs de governação
**Contexto.** Sem métricas, não há melhoria contínua.  

:::userstory
**História.**   
Como **Gestão**, quero **definir e monitorizar KPIs de governação**, para **avaliar eficácia do programa SbD-ToE**.  

**Critérios de aceitação (BDD).**  
- **Dado** ciclo trimestral  
  **Quando** KPIs são medidos  
  **Então** relatório é partilhado com direção  

**Critérios de aceitação (DoD).**  
- [ ] KPIs definidos (ex.: exceções, fornecedores auditados)  
- [ ] Métricas recolhidas  
- [ ] Relatório partilhado  

:::

**Artefactos & evidências.** Relatórios KPIs  

**Proporcionalidade.**  
| L1 | L2 | L3 |
|----|----|----|
| Básico | Recomendado | Obrigatório |

**Integração.** Auditoria; Resp: Gestão + GRC  

---

### US-06 - Execução de fluxo formal de validação de fornecedores
**Contexto.** Fornecedores não validados introduzem risco não rastreável na cadeia de suprimentos.  

:::userstory
**História.**   
Como **Procurement Officer**, quero **executar o fluxo formal de validação de fornecedores (questionário → análise AppSec → aprovação)**, para **garantir que novos fornecedores cumprem requisitos mínimos antes do onboarding**.  

**Critérios de aceitação (BDD).**  
- **Dado** um novo fornecedor classificado como L2 ou L3  
  **Quando** o fluxo de validação é iniciado  
  **Então** questionário é enviado, analisado por AppSec, e aprovação/exceção é registada  

**Critérios de aceitação (DoD).**  
- [ ] Checklist de validação preenchido (questionário, cláusulas, evidência)  
- [ ] Análise técnica por AppSec Engineer documentada  
- [ ] Decisão formalizada (Aprovação / Rejeição / Exceção) registada em GRC  
- [ ] Owner de Fornecedor designado e notificado  

:::

**Artefactos & evidências.** Formulário de questionário, Relatório de análise AppSec, Registo GRC  

**Proporcionalidade.**  
| L1 | L2 | L3 |
|----|----|----|
| Opcional | Recomendado | Obrigatório |

**Integração.** Planeamento; Resp: Procurement Officer + AppSec Engineer + GRC Analyst; SLA: 2 semanas (L2), 1 semana (L3)  

**Ligações úteis.**  
- [Modelo de Validação de Fornecedores](addon/03-modelo-validacao-fornecedores.md)  
- [Exemplos Práticos](addon/05-exemplos-praticos.md)  

---

### US-07 - Ciclo contínuo de revisão e reavaliação de exceções
**Contexto.** Exceções esquecidas tornam-se risco permanente não mitigado.  

:::userstory
**História.**   
Como **AppSec Engineer**, quero **revisar e reavaliar exceções e compensações de forma periódica**, para **garantir que o risco residual continua mitigado e que compensações permanecem eficazes**.  

**Critérios de aceitação (BDD).**  
- **Dado** uma exceção ou compensação ativa com prazo de revisão  
  **Quando** chega a data de revisão agendada (ou ocorre evento crítico)  
  **Então** é reavaliada, revalidada, prorrogada ou encerrada  

**Critérios de aceitação (DoD).**  
- [ ] Calendário de revisão definido por criticidade (L3 trimestral, L2 semestral)  
- [ ] Registo de exceção atualizado com nova data de revisão  
- [ ] Reavaliação documentada (mantém-se, prolonga-se, encerra-se)  
- [ ] Owner de Segurança notificado e decisão aprovada  

:::

**Artefactos & evidências.** Tabela de exceções com prazos, Relatório de reavaliação, Notificação a owner  

**Proporcionalidade.**  
| L1 | L2 | L3 |
|----|----|----|
| Básico | Recomendado | Obrigatório |

**Integração.** Operações + Validação; Resp: AppSec Engineer + GRC Analyst; Triggers: Calendário (trimestral/semestral), Incidente crítico, Mudança arquitetura; SLA: Reavaliação em 5 dias úteis  

**Ligações úteis.**  
- [Validação Continuada](addon/06-validacao-continuada.md)  

---

### US-08 - Repositório de conformidade por aplicação (controlo sistemático)
**Contexto.** Sem repositório centralizado, estado de segurança fica invisível para auditores e gestão.  

:::userstory
**História.**   
Como **AppSec Engineer + Dev Lead**, quero **manter um repositório estruturado de conformidade para cada aplicação**, para **consolidar estado de todas as práticas SbD-ToE e facilitar auditorias internas e externas**.  

**Critérios de aceitação (BDD).**  
- **Dado** uma aplicação classificada como L1, L2 ou L3  
  **Quando** o repositório é criado ou atualizado  
  **Então** reflete estado de todos os capítulos (2–13) em checklist estruturado  

**Critérios de aceitação (DoD).**  
- [ ] Repositório criado (ficheiro YAML, MD versionado ou dashboard GRC)  
- [ ] Checklist por capítulo (02–13) incluído com estado binário (Sim/Não/Exceção)  
- [ ] Evidência de validação ligada (links a relatórios, testes, scans, auditorias)  
- [ ] Histórico de alterações mantido e auditável  
- [ ] Atualizado por release relevante ou evento crítico  

:::

**Artefactos & evidências.** Ficheiro de conformidade (YAML/MD), Links a relatórios de validação, Histórico de versões  

**Proporcionalidade.**  
| L1 | L2 | L3 |
|----|----|----|
| Básico | Recomendado | Obrigatório |

**Integração.** Planeamento + Execução + Validação; Resp: AppSec Engineer + Dev Lead + GRC Analyst; SLA: Atualização por release ou 5 dias após evento crítico  

**Ligações úteis.**  
- [Controlo Sistemático das Práticas SbD-ToE](addon/11-controlos-praticas-sbd.md)  
- [Rastreabilidade Organizacional](addon/04-rastreabilidade-organizacional.md)  

---

### US-09 - Designação formal de owners de segurança por aplicação
**Contexto.** Sem owner claro, responsabilidade dispersa resulta em negligência de exceções e validações.  

:::userstory
**História.**   
Como **Gestão/PMO**, quero **designar formalmente um owner de segurança (Security Champion) por cada aplicação crítica**, para **garantir responsabilização clara, continuidade de decisões de segurança e comunicação de risco**.  

**Critérios de aceitação (BDD).**  
- **Dado** uma aplicação classificada como L2 ou L3  
  **Quando** um Security Champion é designado  
  **Então** ele é responsável pela submissão de exceções, validações, comunicação de risco e cumprimento de políticas  

**Critérios de aceitação (DoD).**  
- [ ] Security Champion designado por escrito (e-mail oficial, documento, HR system)  
- [ ] Responsabilidades documentadas (exceções, validação, comunicação, rastreabilidade)  
- [ ] Formação obrigatória em SbD-ToE completada (Cap. 13 - Formação e Onboarding)  
- [ ] Registo centralizado mantido (Git, Confluence, SharePoint)  
- [ ] Notificação formal ao owner anterior (se houver rotação)  

:::

**Artefactos & evidências.** Documento de designação, Comprovativo de formação, Registo centralizado de owners  

**Proporcionalidade.**  
| L1 | L2 | L3 |
|----|----|----|
| Recomendado | Obrigatório | Obrigatório |

**Integração.** Planeamento; Resp: Gestão/PMO + Security Champion + AppSec Engineer; SLA: Designação no arranque do projeto ou mudança de owner  

**Ligações úteis.**  
- [Modelo de Governação](addon/01-modelo-governancao.md)  
- [Formação e Onboarding (Cap. 13)](/sbd-toe/sbd-manual/formacao-onboarding/aplicacao-lifecycle)  

---

### US-10 - Validação periódica de aplicações (ciclo de conformidade)
**Contexto.** Sem validações recorrentes, desvios não são detetados até auditoria ou incidente.  

:::userstory
**História.**   
Como **AppSec Engineer + GRC Analyst**, quero **executar validações periódicas de conformidade com SbD-ToE em cada aplicação**, para **assegurar que requisitos continuam aplicados e eficazes, detetar desvios cedo, e manter evidência atualizada**.  

**Critérios de aceitação (BDD).**  
- **Dado** um calendário de revisões definido por criticidade (L3 trimestral, L2 semestral)  
  **Quando** ciclo de revisão chega  
  **Então** aplicação é reavaliada, evidência recolhida, e status atualizado no repositório  

**Critérios de aceitação (DoD).**  
- [ ] Calendário de revisões definido e comunicado ao Dev Lead  
- [ ] Checklist de validação por capítulo executado  
- [ ] Evidência recolhida (testes, scans, revisões, auditorias externas)  
- [ ] Relatório de conformidade gerado com status claro  
- [ ] Findings e desvios registados em sistema de tracking (Jira, etc.)  
- [ ] Plano de ação criado para não-conformidades críticas  

:::

**Artefactos & evidências.** Relatório de validação por ciclo, Checklist preenchido, Plano de ação para findings, Histórico de ciclos  

**Proporcionalidade.**  
| L1 | L2 | L3 |
|----|----|----|
| Anual | Semestral | Trimestral |

**Integração.** Validação + Auditoria; Resp: AppSec Engineer + GRC Analyst + Dev Lead; Triggers: Calendário cíclico, Release relevante, Incidente crítico; SLA: Ciclo completado em 2 semanas desde trigger  

**Ligações úteis.**  
- [Validação Continuada](addon/06-validacao-continuada.md)  
- [Controlo Sistemático das Práticas](addon/11-controlos-praticas-sbd.md)  

---

### US-11 - Consolidação de KPIs de governação e maturidade
**Contexto.** Sem métricas consolidadas, decisão executiva sobre eficácia do SbD-ToE fica sem base empírica.  

:::userstory
**História.**   
Como **CISO + Gestão Executiva**, quero **consolidar e reportar KPIs de governação (exceções, fornecedores auditados, conformidade por capítulo, maturidade)**, para **avaliar objetivamente a maturidade de segurança da organização e tomar decisões estratégicas**.  

**Critérios de aceitação (BDD).**  
- **Dado** dados de conformidade e exceções por aplicação  
  **Quando** ciclo de reporting chega (trimestral/semestral)  
  **Então** KPIs são calculados, visualizados e reportados à direção  

**Critérios de aceitação (DoD).**  
- [ ] KPIs definidos (ex: % aplicações com rastreabilidade, % exceções resolvidas, % fornecedores auditados, nível maturidade SAMM/SSDF)  
- [ ] Dashboard configurado com métricas por capítulo e por aplicação  
- [ ] Dados agregados de todos os projetos, equipas e fornecedores  
- [ ] Relatório consolidado entregue à Gestão Executiva, CISO e GRC  
- [ ] Tendências identificadas e recomendações incluídas  
- [ ] Histórico mantido para análise evolutiva  

:::

**Artefactos & evidências.** Dashboard de KPIs, Relatório consolidado trimestral/semestral, Histórico de tendências, Análise executiva  

**Proporcionalidade.**  
| L1 | L2 | L3 |
|----|----|----|
| Básico | Recomendado | Obrigatório |

**Integração.** Auditoria + Operações; Resp: GRC Analyst + AppSec Engineer + CISO; Triggers: Trimestral (mínimo), Semestral (recomendado); SLA: Relatório publicado 5 dias após fim do período  

**Ligações úteis.**  
- [Governação e Maturidade](addon/07-governancao-e-maturidade.md)  
- [Rastreabilidade Organizacional](addon/04-rastreabilidade-organizacional.md)  

---

### US-12 - Formalização de modelo de governação por nível de risco
**Contexto.** Sem modelo formal documentado, decisões de segurança ficam dispersas entre AppSec, Gestão e Jurídico. A falta de critérios explícitos para aprovação por nível resulta em inconsistência, risco não rastreável, e desconfiança dos stakeholders.

:::userstory
**História.**   
Como **CISO + AppSec Manager**, quero **formalizar e documentar o modelo de governação com níveis de alçada explícitos, papéis e responsabilidades claras**, para **garantir que decisões de segurança são tomadas com autoridade apropriada, consistência, e rastreabilidade completa**.

**Critérios de aceitação (BDD).**  
- **Dado** que a organização adota SbD-ToE  
  **Quando** um novo modelo de governação é definido ou revisado  
  **Então** ele é documentado com alçadas por L1–L3, aprovado por direção, e comunicado a todos os stakeholders  

**Critérios de aceitação (DoD).**  
- [ ] Documento formal de "Política de Governação de Segurança SbD-ToE" aprovado por direção  
- [ ] Níveis de alçada definidos explicitamente: L1 (Gestor Aplicação), L2 (AppSec + Gestor), L3 (CISO + AppSec + Direção)  
- [ ] Papéis e responsabilidades mapeados por função (Dev, AppSec, Gestão, Jurídico, GRC, CISO)  
- [ ] Template de registo de decisão criado (Jira / SharePoint / Git) com campos obrigatórios  
- [ ] Fluxo de escalação documentado com SLAs por nível  
- [ ] Formação executada para todos os approvers (Cap. 13 - Trilho Formação Governação)  
- [ ] Comunicação oficial publicada em canais corporativos  

:::

**Artefactos & evidências.** Documento de Política, Template de Decisão, Repositório de decisões registadas, Comprovativo de formação dos approvers, Email de comunicação  

**Proporcionalidade.**  
| L1 | L2 | L3 |
|----|----|----|
| Básico | Recomendado | Obrigatório |

**Integração.** Planeamento + Execução contínua; Resp: CISO + AppSec Manager + Jurídico; Triggers: Arranque SbD-ToE, revisão anual, mudança organizacional; SLA: Publicação em 2 semanas  

**Ligações úteis.**  
- [Modelo de Governação](addon/01-modelo-governancao.md)  
- [Exemplos de Decisão](addon/05-exemplos-praticos.md)  
- [Formação de Governação (Cap. 13)](/sbd-toe/sbd-manual/formacao-onboarding/aplicacao-lifecycle)  

---

### US-13 - Controlo sistemático e periódico por capítulo SbD-ToE
**Contexto.** Sem checklist centralizado de conformidade, o estado de conformidade de uma aplicação com Cap. 2–13 fica invisível. Desvios não são detetados até auditoria ou incidente crítico. Gestão não tem visibilidade do progresso.

:::userstory
**História.**   
Como **AppSec Engineer + Dev Lead**, quero **manter um checklist centralizado, versionado e auditável de conformidade com todos os capítulos SbD-ToE (2–13), com verificação periódica por release ou evento crítico**, para **consolidar estado real de todas as práticas e facilitar auditorias, decisão de risco, e demonstração de conformidade normativa**.

**Critérios de aceitação (BDD).**  
- **Dado** uma aplicação classificada como L1, L2 ou L3  
  **Quando** um ciclo de validação é acionado (por release, trimestral L3, semestral L2, ou evento crítico)  
  **Então** checklist é preenchido com estado, evidência é ligada, e relatório é gerado  

**Critérios de aceitação (DoD).**  
- [ ] Ficheiro de checklist versionado criado em repositório (YAML, MD ou dashboard GRC) com estrutura: Capítulo | Prática | Status (Sim/Não/Exceção/N/A) | Evidência (link/referência) | Owner | Data de validação  
- [ ] Integração com sistema de controlo de versões (Git) ou GRC com histórico auditável  
- [ ] Triggers definidos e automatizados: release relevante, evento crítico (incidente, CVE), ciclo programado (L3 trimestral, L2 semestral, L1 anual)  
- [ ] Histórico mantido com alterações datadas e responsáveis (trilha de auditoria)  
- [ ] Relatório consolidado gerado por ciclo com % conformidade, achados críticos, e plano de acção  
- [ ] Artefactos de evidência ligados ou referenciados no checklist (links a testes, scans, relatórios, auditorias)  
- [ ] Notificação automática enviada a Dev Lead e AppSec Engineer quando ciclo é acionado  

:::

**Artefactos & evidências.** Ficheiro de checklist versionado (YAML/MD), Git history ou dashboard GRC, Relatórios por ciclo, Links a artefactos de validação, Plano de acção para não-conformidades, Histórico de versões  

**Proporcionalidade.**  
| L1 | L2 | L3 |
|----|----|----|
| Básico | Recomendado | Obrigatório |

**Integração.** Planeamento + Execução + Validação + Auditoria; Resp: AppSec Engineer (validação) + Dev Lead (preenchimento) + GRC Analyst (consolidação); Triggers: Release relevante, evento crítico, ciclo programado (trimestral/semestral/anual); SLA: Atualização em 5 dias úteis após trigger  

**Ligações úteis.**  
- [Controlo Sistemático das Práticas SbD-ToE](addon/11-controlos-praticas-sbd.md)  
- [Rastreabilidade Organizacional](addon/04-rastreabilidade-organizacional.md)  
- [Validação Periódica](addon/06-validacao-continuada.md)  

---

### US-14 - Reavaliação contínua e rotação de fornecedores pós-onboarding
**Contexto.** Fornecedores são validados no onboarding, mas sem revisão periódica, desvios surgem ao longo do tempo (novos CVEs não mitigados, SLA não cumprido, mudanças de propriedade, evolução do risco). Risco residual acumula invisível. Contratos expiram sem renovação de validação.

:::userstory
**História.**   
Como **Procurement Officer + AppSec Engineer**, quero **reavalia e reaprovar fornecedores periodicamente (anual por defaut, semestral para L2, trimestral para L3), com validação técnica atualizada, análise de compliance SLA, e escalonamento para decisão de penalização ou substituição se necessário**, para **assegurar que continuam a cumprir requisitos e SLA, que risco é mitigado, e que decisões de continuidade são baseadas em evidência**.

**Critérios de aceitação (BDD).**  
- **Dado** um fornecedor ativo com contrato vigente  
  **Quando** chega data de revisão agendada (calendário) ou evento crítico ocorre (incidente, CVE crítico, mudança SLA)  
  **Então** fornecedor é reavaliado com questionário atualizado, evidência técnica validada (SBOM, SLA compliance, mudanças) e decisão é formalizada  

**Critérios de aceitação (DoD).**  
- [ ] Calendário de revisão de fornecedores definido e comunicado (anual mínimo, 6 meses para L2, trimestral para L3, ou por evento crítico)  
- [ ] Questionário atualizado com perguntas de segurança e SLA enviado ao fornecedor  
- [ ] Análise técnica documentada (AppSec): SBOM validado, CVEs analisados, SLA compliance verificado, mudanças organizacionais/técnicas identificadas  
- [ ] Decisão formalizada e registada em GRC: Aprovado / Exceção criada / Penalização proposta / Rescisão iniciada  
- [ ] Owner notificado formalmente por email com decisão e próxima data de revisão  
- [ ] Plano de mitigação criado se gaps identificados (prazo, responsável AppSec, validação esperada)  
- [ ] Registo atualizado no repositório de fornecedores com data, decisor, e histórico  

:::

**Artefactos & evidências.** Calendário de revisão, Questionário atualizado + respostas, Análise técnica documentada, Decisão registada em GRC, Comunicação formal ao fornecedor, Plano de mitigação se aplicável, Histórico de decisões  

**Proporcionalidade.**  
| L1 | L2 | L3 |
|----|----|----|
| Anual | Semestral | Trimestral / evento crítico |

**Integração.** Validação + Operações; Resp: Procurement Officer (coordenação) + AppSec Engineer (análise técnica) + GRC Analyst (decisão e registo); Triggers: Calendário programado (anual/semestral), Incidente crítico, CVE crítico não mitigado, Mudança de contrato/propriedade/SLA; SLA: Reavaliação completada em 2 semanas desde trigger  

**Ligações úteis.**  
- [Modelo de Validação de Fornecedores](addon/03-modelo-validacao-fornecedores.md)  
- [Validação Continuada](addon/06-validacao-continuada.md)  
- [Exemplos de Aplicação](addon/05-exemplos-praticos.md)  

---

### US-15 - Preparação Técnica e Validação de Contractors pré-Acesso
**Contexto.** Contractors ganham acesso sem compreender políticas de segurança, ferramentas obrigatórias, ou procedimentos. Risco de erro involuntário (credenciais expostas, acesso a dados não autorizados, práticas inseguras).

:::userstory
**História.**   
Como **Security Champion + HR/Recruiter**, quero **executar processo estruturado de preparação técnica de contractors (triagem, formação obrigatória, teste de compreensão, ambiente sandbox) antes de ganhem acesso a sistemas**, para **garantir que estão preparados, compreenderam políticas fundamentais, e podem trabalhar seguramente**.

**Critérios de aceitação (BDD).**  
- **Dado** um novo contractor aprovado por Procurement (US-06) e contrato assinado  
  **Quando** chega data de início do projeto  
  **Então** trilho de preparação é acionado: formação obrigatória, quiz, sandbox setup, confirmação de NDA  

**Critérios de aceitação (DoD).**  
- [ ] Checklist de preparação preenchido (triagem de skills, nível de segurança esperado, formação requerida definida)  
- [ ] Trilho de formação baseado em perfil (Dev, DevOps, QA, etc.) iniciado em LMS ou plataforma de treino  
- [ ] Quiz de compreensão de políticas de segurança completado (score mínimo 80%)  
- [ ] Acesso a ambiente sandbox fornecido para prática (ex.: repositório Git privado, aplicação demo, ferramentas de segurança)  
- [ ] NDA e confidentiality agreement assinados digitalmente com timestamp  
- [ ] Checklist de onboarding técnico preenchido e validado pela equipa (Security Champion + Tech Lead)  
- [ ] Acesso real a sistemas concedido apenas após todos os passos de aprovação  
- [ ] Registo de "ready for access" documentado em GRC com data, validador, e referência a todas as validações  

:::

**Artefactos & evidências.** Checklist de preparação preenchido, LMS enrollment confirmado, Quiz score validado, Sandbox access credentials, Acordos assinados digitalmente, Checklist de onboarding, Registo GRC de "ready for access"

**Proporcionalidade.**  
| L1 | L2 | L3 |
|----|----|----|
| Básico | Recomendado | Obrigatório + quiz validado |

**Integração.** Planeamento; Resp: HR (coordenação) + AppSec Engineer (validação) + Tech Lead (sandbox setup); Triggers: Contrato assinado, data de início do projeto; SLA: Conclusão em 2–3 dias úteis antes de data de início; Notificação: Contractor informado via email sobre trilho  

**Ligações úteis.**  
- [Cap. 13 - Formação e Onboarding](/sbd-toe/sbd-manual/formacao-onboarding/aplicacao-lifecycle)  
- [Validação de Fornecedores - US-06](#us-06)  
- [Template de Validação de Contractors](/sbd-toe/sbd-manual/addon/02-template-validacao-contractors)  
- [Guia de Preparação Sandbox](/sbd-toe/sbd-manual/addon/12-guia-preparacao-sandbox)  

---

### US-16 - Trilho de Formação Obrigatória pré-Acesso (Contractors)
**Contexto.** Contractors iniciados sem completar formação de segurança obrigatória. Falta de integração clara entre Cap. 13 (Formação) e Cap. 14 (Governação): quem aprova, qual o SLA, como é tracked.

:::userstory
**História.**   
Como **CISO + Training Manager**, quero **definir e executar trilho de formação obrigatória por perfil de contractor, com SLA explícito de conclusão antes de acesso técnico**, para **garantir consciência de segurança mínima, conformidade regulatória (DORA, NIS2), e rastreabilidade de preparação**.

**Critérios de aceitação (BDD).**  
- **Dado** um contractor novo contratado  
  **Quando** trilho de formação é atribuído em LMS  
  **Então** deve completar cursos obrigatórios, passar quiz, e ter registo consolidado antes de acesso real  

**Critérios de aceitação (DoD).**  
- [ ] Trilho de formação definido por perfil (Developer, DevOps, QA, Arquitetura, etc.) com duração estimada  
- [ ] Cursos obrigatórios listados e mapeados a capítulos SbD-ToE:  
    - **[O1] Security Awareness Geral** (2h) → Cap. 00 + 02 + 14  
    - **[O2] SbD-ToE Overview** (1h) → Cap. 01–03 (risco, requisitos, threat modeling)  
    - **[O3] Secure Coding & SAST** (2h) → Cap. 06 (se developer)  
    - **[O4] CI/CD Security & Artefacts** (1h) → Cap. 07 (se DevOps)  
    - **[O5] Incident Response Basics** (1h) → Cap. 12  
    - **[O6] Supply Chain & Dependências** (1h) → Cap. 05 (se envolvido com builds)  
- [ ] Quiz de avaliação por curso (score mínimo 80%) completado  
- [ ] Registo centralizado atualizado (LMS ou Confluence) com datas, scores, validador  
- [ ] SLA de conclusão comunicado ao contractor: Máximo **5 dias úteis antes de data de início**  
- [ ] Notificação automática enviada se SLA em risco (ex.: 2 dias antes da deadline)  
- [ ] Sign-off de "formação completa" fornecido ao AppSec Engineer (libera acesso técnico)  
- [ ] Histórico mantido por 3 anos (DORA, NIS2 requirement)  

:::

**Artefactos & evidências.** Trilho de formação definido por perfil, LMS enrollment, Quiz completion records, Sign-off de conclusão, SLA compliance checklist, Notificações enviadas

**Proporcionalidade.**  
| L1 | L2 | L3 |
|----|----|----|
| Básico | Obrigatório | Obrigatório + 80% score requerido |

**Integração.** Planeamento + Execução; Resp: Training Manager (coordenação trilho) + AppSec Engineer (validação de conclusão) + HR (rastreabilidade); Triggers: Contractor aprovado (fim US-06/US-15); SLA: Formação completa antes de acesso real; Notificação: Semanais se em risco, daily se `<`3 dias  

**Ligações úteis.**  
- [Cap. 13 - Formação e Onboarding](/sbd-toe/sbd-manual/formacao-onboarding/aplicacao-lifecycle)  
- [Designação de Owners de Segurança - US-09](#us-09)  
- [Preparação Técnica - US-15](#us-15)  

---

### US-17 - Offboarding Seguro de Contractors e Rescisão de Fornecedores
**Contexto.** Contractors terminam projeto ou contrato sem processo formal: acesso mantém-se ativo, ativos (código, credenciais, documentos) não são recuperados. Risco de vazamento pós-rescisão, acesso residual, violação de confidencialidade.

:::userstory
**História.**   
Como **Security Champion + HR + DevOps Lead**, quero **executar processo formal e automático de offboarding seguro quando contractor termina ou fornecedor é rescindido**, para **garantir que acesso é revogado completamente, ativos recuperados, confidencialidade mantida, e conformidade legal assegurada**.

**Critérios de aceitação (BDD).**  
- **Dado** um contractor cuja data de termo é conhecida (ou fornecedor rescindido com aviso)  
  **Quando** data de offboarding chega  
  **Então** acesso é revogado, ativos recuperados, e conclusão documentada  

**Critérios de aceitação (DoD).**  
- [ ] Checklist de offboarding preparado 2 semanas antes (IT, HR, AppSec, Tech Lead)  
- [ ] Notificação formal enviada ao contractor/fornecedor com data exata de desativação  
- [ ] Acesso a sistemas revogado (no máximo 24h após data de termo):  
    - Contas de utilizador desativadas em Git, Jira, CI/CD  
    - SSH keys e API tokens removidos  
    - VPN, cloud IAM access revogado  
    - MFA removido  
    - Emails corporativos desativados (se aplicável)  
- [ ] Ativos recuperados:  
    - Código/repositórios transferidos ou archived (se contractor desenvolveu)  
    - Documentação entregue e versionada  
    - Laptop/hardware retornado, wiped, e certificação de limpeza  
    - Secrets (API keys, passwords) rotacionados  
- [ ] Last backup de trabalho do contractor realizado (ex.: clone de repos privados)  
- [ ] Sign-off formal de "offboarding completo" registado em GRC com timestamp  
- [ ] Reminder legal enviado ao contractor: Confidentiality obligations continuam pós-término (duração, consequências)  
- [ ] Relatório de offboarding arquivado por 7 anos (DORA requirement)  

:::

**Artefactos & evidências.** Checklist de offboarding preenchido, Confirmação de desativação de acesso, Backup certificate, Ativos recuperados (inventory), Sign-off GRC, Legal notice, Relatório arquivado

**Proporcionalidade.**  
| L1 | L2 | L3 |
|----|----|----|
| Básico | Obrigatório | Obrigatório + audit trail |

**Integração.** Operações + Validação; Resp: HR (coordenação timeline) + DevOps (acesso técnico) + AppSec Engineer (validação) + Security Champion (checkpoints); Triggers: Data de término conhecida (programado), Rescisão imediata (unscheduled); SLA: Offboarding completo em **`<`24h** da data de termo; Notificação: HR envia aviso 2 semanas antes  

**Ligações úteis.**  
- [Reavaliação de Fornecedores - US-14](#us-14)  
- [Preparação Técnica - US-15](#us-15)  
- [Checklist de Offboarding](/sbd-toe/sbd-manual/addon/13-checklist-offboarding)  

---

### US-18 - Monitorização Contínua de Conformidade de Fornecedores (Alertas e Escalação)
**Contexto.** Fornecedores são avaliados periodicamente (US-14), mas risco entre ciclos não é detetado. CVEs, incidentes críticos, mudanças de SLA, ou breaches não são monitorados em tempo real.

:::userstory
**História.**   
Como **AppSec Engineer + Security Monitoring Team**, quero **monitorizar continuamente conformidade de fornecedores críticos (incidentes, CVEs, SLA, mudanças organizacionais) e escalar automaticamente se gaps surgem**, para **reduzir risco residual entre ciclos de avaliação formal e detetar eventos críticos em tempo real**.

**Critérios de aceitação (BDD).**  
- **Dado** um fornecedor crítico (L2–L3) com contrato vigente  
  **Quando** incidente, CVE crítico, SLA breach, ou mudança organizacional é reportado  
  **Então** alerta automático é gerado e escalado para AppSec e Procurement  

**Critérios de aceitação (DoD).**  
- [ ] Integração com feed de incidentes do fornecedor (status page, email alerts, API)  
- [ ] Monitorização contínua de CVEs em stack técnico do fornecedor (via SBOM/SCA tool)  
- [ ] Alerta automático acionado se:  
    - CVE crítico em dependência do fornecedor não mitigado em 72h (L3) ou 7 dias (L2)  
    - Incidente de segurança reportado pelo fornecedor  
    - SLA não cumprido (ex.: uptime `<`99.5% para L3, `<`99% para L2)  
    - Mudança de propriedade, localização, ou subcontratação  
- [ ] Escalação automática com prioridade:  
    - **P0 (CVE crítico explorado):** Immediate → AppSec Engineer + Procurement Officer + CISO  
    - **P1 (CVE crítico, incidente grave):** 1h → AppSec Engineer + Procurement Officer  
    - **P2 (CVE high, incidente moderado):** 4h → AppSec Engineer  
- [ ] Trigger automático de revisão especial fora-de-ciclo (US-14) se gap crítico  
- [ ] Registo de alerta, escalonamento, e ação documentado em GRC (audit trail)  
- [ ] Dashboard em tempo real com status de fornecedores críticos e alertas ativas (visível a board)  

:::

**Artefactos & evidências.** Feed de incidentes configurado, CVE monitoring ativo, Alertas documentados com timestamps, Escalation records, Dashboard, GRC audit trail

**Proporcionalidade.**  
| L1 | L2 | L3 |
|----|----|----|
| Não | Recomendado | Obrigatório |

**Integração.** Operações contínuo; Resp: AppSec Engineer (setup inicial) + Security Monitoring (operação 24x7); Triggers: Incidente, CVE crítico, SLA breach, mudança contratual; SLA: Alerta em **`<`1h** de deteção, escalonamento em `<`15 min  

**Ligações úteis.**  
- [Reavaliação de Fornecedores - US-14](#us-14)  
- [Monitorização - Cap. 12](/sbd-toe/sbd-manual/monitorizacao-operacoes/aplicacao-lifecycle)  
- [Dependências e SCA - Cap. 05](/sbd-toe/sbd-manual/dependencias-sbom-sca/aplicacao-lifecycle)  

---

### US-19 - Revisão Trimestral de Acesso de Contractors (Least Privilege)
**Contexto.** Contractors ganham acesso inicial, mas permissões acumulam ao longo do tempo ("acesso creep"). Sem revisão periódica, principle of least privilege é violado.

:::userstory
**História.**   
Como **Security Champion + Infrastructure/Tech Lead**, quero **revisar trimestralmente acesso de contractors em ativo, validando que têm apenas acesso necessário ao projeto**, para **manter principle of least privilege, reduzir risco de acesso excessivo, e remover acesso obsoleto**.

**Critérios de aceitação (BDD).**  
- **Dado** contractors ativos com acesso a sistemas (repos, CI/CD, databases, cloud)  
  **Quando** ciclo trimestral de revisão chega  
  **Então** acesso é validado com Tech Lead, e acesso excessivo é removido no mesmo dia  

**Critérios de aceitação (DoD).**  
- [ ] Lista de contractors ativos extraída de sistemas (Git orgs, Jira, VPN, Cloud IAM, databases)  
- [ ] Por cada contractor:  
    - Acesso listado em detalhe (repositórios, CI/CD pipelines, databases, cloud resources, etc.)  
    - Tech Lead valida cada acesso: **Necessário para projeto atual?** (Sim/Não/Modificar)  
    - Se **Não necessário:** acesso removido no mesmo dia  
    - Se **Modificar:** novo scope configurado, antigo revogado  
    - Se **Sim:** mantém-se com confirmação datada  
- [ ] Checklist de revisão preenchido e assinado digitalmente por Tech Lead + Security Champion  
- [ ] Notificação enviada a cada contractor informando resultado da revisão  
- [ ] Se acesso removido: notificação clara indicando motivo e data de conclusão  
- [ ] Registo de mudanças documentado em audit trail (Git logs, IAM change log, etc.)  
- [ ] Relatório consolidado (% de acesso mantido, % removido) entregue ao AppSec Engineer  

:::

**Artefactos & evidências.** Lista de contractors e acesso, Checklist assinado, Notificações enviadas, Git/IAM logs de mudanças, Relatório consolidado, Sign-off

**Proporcionalidade.**  
| L1 | L2 | L3 |
|----|----|----|
| Semestral | Trimestral | Trimestral |

**Integração.** Validação; Resp: Security Champion (coordenação) + Tech Lead (validação de necessidade) + DevOps (mudanças técnicas); Triggers: Calendário (trimestral), Mudança de projeto, Incidente; SLA: Revisão iniciada e completada em **1 semana**  

**Ligações úteis.**  
- [Preparação Técnica - US-15](#us-15)  
- [Offboarding - US-17](#us-17)  
- [Requisitos de Autenticação e Acesso - Cap. 02](/sbd-toe/sbd-manual/requisitos-seguranca/aplicacao-lifecycle)  

---

### US-20 - Feedback Pós-Projeto e Rating de Contractors
**Contexto.** Contractors terminam projeto sem feedback sobre desempenho de segurança. Sem dados de avaliação, impossível tomar decisão informada sobre re-hire ou referência.

:::userstory
**História.**   
Como **Security Champion + Tech Lead**, quero **recolher feedback estruturado pós-projeto de contractors sobre compreensão de segurança, incidentes, e recomendações**, para **informar decisão de re-hire, melhorar programa de preparação, e criar base de dados de avaliação**.

**Critérios de aceitação (BDD).**  
- **Dado** um contractor cujo projeto termina  
  **Quando** offboarding é iniciado (US-17)  
  **Então** feedback form é enviado para Tech Lead + AppSec Engineer preencherem  

**Critérios de aceitação (DoD).**  
- [ ] Feedback form criado com perguntas estruturadas:  
    - **Segurança:** Compreensão de políticas (escala 1–5), Best practices aplicadas (Sim/Não), Incidentes durante projeto (Sim/Não + desc)  
    - **Performance:** Qualidade de código (1–5), Teste (1–5), Documentação (1–5)  
    - **Conformidade:** Contractor seguiu procedimentos obrigatórios (Sim/Não), Violações (Sim/Não + desc)  
    - **Recomendações:** Áreas de melhoria em formação/preparação, Rating de segurança geral (1–5 stars)  
    - **Decisão:** Re-hire recomendado? (Sim/Não/Talvez + justificação)  
- [ ] Feedback recolhido de Tech Lead + AppSec Engineer + Security Champion (consenso)  
- [ ] Resultado registado em sistema centralizado (HR, Procurement, GRC) com data e reviewers  
- [ ] Rating (positivo/neutro/negativo) armazenado como referência para futuras contratações  
- [ ] Se múltiplos contractors de mesmo fornecedor: insights agregados para revisão de fornecedor (US-14)  
- [ ] Resultados consolidados publicados em relatório trimestral de programa de contractors  

:::

**Artefactos & evidências.** Feedback form preenchido, Ratings registados (sistema HR/GRC), Agregação por fornecedor, Relatório trimestral, Histórico de avaliações

**Proporcionalidade.**  
| L1 | L2 | L3 |
|----|----|----|
| Opcional | Recomendado | Obrigatório |

**Integração.** Operações pós-projeto; Resp: Security Champion (coordenação) + Tech Lead + AppSec Engineer (preenchimento); Triggers: Offboarding iniciado (US-17); SLA: Feedback completado em **3 dias úteis** após fim do contrato  

**Ligações úteis.**  
- [Offboarding - US-17](#us-17)  
- [Reavaliação de Fornecedores - US-14](#us-14)  
- [Designação de Owners - US-09](#us-09)  

---

## 📦 Artefactos esperados

| Artefacto | Evidência |
|-----------|-----------|
| Registo de exceções com alçadas | Ferramenta GRC versionada, decisões auditáveis |
| Contratos com cláusulas | Documentos validados juridicamente |
| Relatórios de fornecedores | Auditorias e findings, análise técnica |
| Dashboard organizacional | Métricas por projeto e aplicação |
| Relatórios KPIs | Consolidação trimestral/semestral |
| Formulário de validação de fornecedores | Questionário preenchido, Análise AppSec, GRC registo |
| Tabela de exceções com calendário de revalidação | Rastreabilidade com datas de vencimento |
| Repositório de conformidade por app | Ficheiro YAML/MD versionado, Histórico auditável |
| Documento de designação de owners | Registo centralizado com formação validada |
| Relatórios de validação periódica | Checklist + Plano de acção, histórico ciclos |
| Dashboard de KPIs e maturidade | Métricas por capítulo, Tendências históricas |
| Política de Governação SbD-ToE | Documento aprovado, Níveis de alçada, Template de decisão |
| Checklist de conformidade centralizado | Ficheiro versionado por app (YAML/MD), Git history |
| Calendário de reavaliação de fornecedores | Planeamento trimestral/semestral/anual, Notificações automáticas |

---

### US-16 - Decisão Estruturada em Aprovação de Exceções de Risco

:::userstory
**História.**

Como **AppSec / CISO**, quero **implementar um framework decisório estruturado** (validação prévia V1 → D1 checklist → R1 decision → E1 escalation) para aprovação de exceções, para **garantir que exceções de risco são aprovadas conscientemente, com compensações adequadas ao nível, e revalidadas periodicamente**.

**Critérios de aceitação (BDD).**
- **Dado** que exceção é registada em GRC
  **Quando** passa por V1 (validação prévia: dados completos?)
  **Então** dados estão documentados (app, requisito, compensação, prazo)

- **Dado** V1 aprovada
  **Quando** D1 checklist executada (4 questões sobre risco)
  **Então** resultado codificado como GREEN/AMBER/ORANGE/RED

- **Dado** D1 resultado
  **Quando** R1 decisão tomada
  **Então** é formalizada (APPROVE/CONDITIONAL/DEFER/DENY) e assinada

- **Dado** conflito (técnico vs. negócio)
  **Quando** E1 escalation acionada
  **Então** enviada para CISO com critério de resolução e SLA 10 dias

**Checklist.**
- [ ] Template V1 (validação prévia) implementado em GRC
- [ ] Matriz D1 (4 questões + risk profiling) documentada
- [ ] Template R1 (4 decisões + justificativa) em uso
- [ ] Template E1 (escalation log) criado e monitorizado
- [ ] Alçada matrix por L1/L2/L3 definida (AppSec/CISO/CFO)
- [ ] SLA por nível comunicado (2-10 dias úteis)
- [ ] KPI-1 (% D1 documentado ≥95%) rastreado
- [ ] KPI-2 (tempo D1→R1 ≤5 dias) em dashboard
- [ ] KPI-3 (escalation rate ≤15%) monitorizado
- [ ] KPI-4 (cumprimento compensações ≥90%) validado
- [ ] KPI-5 (exceções removidas ≥30%) rastreado
- [ ] Training para approvers (AppSec, CISO, CFO) — 2h workshop
- [ ] Audit mensal de 10+ exceções para qualidade D1

:::

**Proporcionalidade L1–L3.**
| L1 | L2 | L3 |
|----|----|----|
| AppSec Engineer (se D1 GREEN) | AppSec Lead + Manager | CISO + AppSec Lead |
| SLA 3-5 dias | SLA 5-7 dias | SLA 1-3 dias |
| Revalidação anual | Revalidação 6-12 meses | Revalidação 3 meses |

**Integração no SDLC.**
| Fase | Trigger | Responsável | SLA |
|------|---------|-------------|-----|
| Planning | Controlo não viável | Dev + AppSec | Sugestão em 1 semana |
| Design Review | Exceção pendente | AppSec | D1 avaliação em 3-5 dias |
| Development | Exceção aprovada | Dev | Implementar compensações |
| Testing | Compensação validação | QA + AppSec | Confirmar ativas (alerts, audit) |
| Deployment | Pre-release final | AppSec | Validação final |
| Revalidação | 3-12 meses | AppSec + GRC | Renovação/denial/modificação |

**Artefactos & evidências.** Documento `decisoes_excecoes.md` com template V1/R1/E1, amostra de 10+ decisões mensais, quadro "Exceções Pendentes" em GRC, SLA compliance report, D1 qualidade audit.

**Ligações úteis.**
[Decisão Estruturada em Exceções](governanca-contratacao/addon/addon-11-decisao-estruturada-excecoes-cap14)
[Validação Empírica de Governação](governanca-contratacao/addon/addon-12-validacao-empirica-governanca-cap14)
[Política de Exceções](/governanca-contratacao/policies-relevantes)

---

### US-17 - Validação Empírica da Eficácia de Compensações de Exceção

:::userstory
**História.**

Como **AppSec / GRC**, quero **implementar um ciclo de validação empírica** (P1-P5: baseline → compensation testing → production monitoring → incident RCA → continuous review) para confirmar que **compensações de exceção realmente funcionam em produção** e reduzem risco (não apenas aprovadas teoricamente).

**Critérios de aceitação (BDD).**
- **Dado** exceção com compensação aprovada
  **Quando** P1 baseline recolhida (pré-exceção)
  **Então** métricas documentadas (incidentes, controlo status, compensation adequacy)

- **Dado** P1 completa
  **Quando** P2 compensation testing executada (lab/staging)
  **Então** compensação validada: funciona? latência? cobertura?

- **Dado** P2 passou
  **Quando** P3 production monitoring (canary 1-5% tráfico)
  **Então** métricas recolhidas: FP%, FN%, alert latency

- **Dado** P3 em progresso
  **Quando** P4 incident RCA (3-6 meses pós-exceção)
  **Então** templates V1/V2 preenchidos: compensação efetiva? ou falhou?

- **Dado** P4 métricas coletadas
  **Quando** P5 monthly/trimestral review agendado
  **Então** exceção renovada, modificada, ou negada baseado em eficácia real

**Checklist.**
- [ ] P1 baseline procedure documentada (métricas, coleta, archiving)
- [ ] P1 baseline recolhida para cada exceção L2+ (registro em GRC)
- [ ] P2 compensation test procedure definida (lab/staging validation)
- [ ] P2 tests executados antes aprovação R1 (funciona? latência? cobertura?)
- [ ] P3 production canary setup (1-5% tráfico com monitorização)
- [ ] P3 métricas recolhidas (FP%, FN%, alert latency, SOC response time)
- [ ] P4 V1 template (compensação efetiva) documentado
- [ ] P4 V2 template (compensação falha/RCA) documentado
- [ ] P4 RCA procedure (mensal L2, trimestral L1, semanal L3)
- [ ] P5 review cycle agenda fixa (data, participantes, template decisão)
- [ ] P5 decisão framework (RENEW/MODIFY/DENY baseado em P4 dados)
- [ ] 5 KPIs rastreados em dashboard (effectiveness%, latency, FP%, FN%, removal_rate)
- [ ] Proporcionalidade L1/L2/L3 aplicada (frequência P1-P5 diferente)
- [ ] Training para AppSec/GRC em P1-P5 framework — 2h workshop

:::

**Proporcionalidade L1–L2–L3.**
| Nivel | P1 Baseline | P2 Testing | P3 Monitoring | P4 RCA | P5 Review |
|-------|------------|-----------|---------------|--------|-----------|
| **L1** | Yearly | Yearly | 3-month | Quarterly | Quarterly |
| **L2** | Quarterly | Quarterly | Monthly | Monthly | Monthly |
| **L3** | Monthly | Monthly | Monthly | Weekly | Weekly |

**Integração no SDLC.**
| Fase | Trigger | Responsável | SLA |
|------|---------|-------------|-----|
| Planning | Exceção prevista | AppSec | P1 baseline em 2 semanas |
| Approval | Pre-approval validation | DevOps | P2 compensation testing em lab |
| Deployment | Produção com monitorização | SOC + AppSec | P3 canary setup com alerts |
| Operations | Incidente em exceção | AppSec + GRC | P4 RCA mensal/trimestral (V1/V2) |
| Audit | Revalidação periódica | GRC | P5 trimestral review (RENEW/MODIFY/DENY) |

**Artefactos & evidências.** P1: `baseline_[app]_[req]_[date].md`; P2: `compensation_test_[app].md` com resultados; P3: canary metrics export; P4: `rca_register_[month].csv` com V1/V2 análises; P5: monthly review minutes com decisões (RENEW/MODIFY/DENY); KPI dashboard export; effectiveness report.

**Ligações úteis.**
[Validação Empírica Framework](governanca-contratacao/addon/addon-12-validacao-empirica-governanca-cap14)
[Decisão Estruturada em Exceções](governanca-contratacao/addon/addon-11-decisao-estruturada-excecoes-cap14)
[KPIs de Governação](governanca-contratacao/kpis-governanca) — Reporte integrado

---

## ⚖️ Matriz de proporcionalidade L1–L3

| Prática | L1 | L2 | L3 |
|---------|----|----|----|
| Exceções formais com alçadas | Opcional | Recomendado | Obrigatório |
| Cláusulas contratuais | Recomendado | Obrigatório | Obrigatório + auditorias |
| Validação de fornecedores (inicial) | Opcional | Recomendado | Obrigatório |
| Rastreabilidade organizacional | Básico | Recomendado | Obrigatório |
| KPIs de governação | Básico | Recomendado | Obrigatório |
| Fluxo formal de validação fornecedores | Opcional | Recomendado | Obrigatório |
| Revisão contínua de exceções | Básico | Recomendado | Obrigatório |
| Repositório de conformidade por app | Básico | Recomendado | Obrigatório |
| Designação formal de owners de segurança | Recomendado | Obrigatório | Obrigatório |
| Validação periódica de conformidade | Anual | Semestral | Trimestral |
| KPIs de maturidade e reporta executiva | Básico | Recomendado | Obrigatório |
| Modelo formal de governação | Básico | Recomendado | Obrigatório |
| Checklist centralizado por capítulo | Básico | Recomendado | Obrigatório |
| Reavaliação de fornecedores pós-onboarding | Anual | Semestral | Trimestral / evento crítico |
| **Preparação técnica de contractors** | Básico | Recomendado | Obrigatório + quiz validado |
| **Trilho de formação pré-acesso** | Básico | Obrigatório | Obrigatório + 80% score |
| **Offboarding seguro** | Básico | Obrigatório | Obrigatório + audit trail |
| **Monitorização contínua de fornecedores** | Não | Recomendado | Obrigatório |
| **Revisão trimestral de acesso (contractors)** | Semestral | Trimestral | Trimestral |
| **Feedback pós-projeto** | Opcional | Recomendado | Obrigatório |

---

## 🏁 Recomendações finais

- **Exceções sem registo = risco invisível.** Operacionalize US-01 (com alçadas claras) e US-07 para garantir rastreabilidade contínua e revalidação automática.  
- **Modelo formal é o alicerce.** US-12 documenta governação com critérios explícitos, alçadas por L1–L3, e formação obrigatória para approvers (Cap. 13).  
- **Fornecedores devem ser parte do modelo SbD-ToE.** Use US-02, US-06, US-14, e US-18 para integração contratual, validação inicial, reavaliação periódica, e monitorização contínua.  
- **Contractors merecem ciclo de vida dedicado.** US-15 (preparação técnica), US-16 (formação obrigatória), US-17 (offboarding) e US-19 (revisão de acesso) garantem que contractors são preparados, mantêm least privilege, e saem seguramente.  
- **Designação clara de owners elimina responsabilidade dispersa.** US-09 garante continuidade de decisões de segurança com formação validada.  
- **Repositório centralizado de conformidade dá visibilidade total.** US-08 e US-13 consolidam estado de todas as práticas por aplicação, capítulo e ciclo.  
- **Validações periódicas detetam desvios cedo.** US-10 integra revisão contínua no ciclo de vida; US-13 valida por capítulo; US-14 reavalia fornecedores; US-19 valida acesso de contractors.  
- **KPIs de governação são a medida objetiva da maturidade.** US-05 e US-11 permitem decisão estratégica baseada em evidência (% conformidade, % exceções resolvidas, % fornecedores auditados).  
- **Rastreabilidade organizacional dá transparência à gestão.** US-04 agregada com US-08, US-10, US-13, US-14, US-20 cria visibilidade de risco em todos os níveis.  
- **Preparação e feedback contínuos melhoram qualidade de contractors.** US-15, US-16, US-20 criam ciclo de melhoria contínua e base de dados de avaliação para re-hire.  
- **Este capítulo é o "cimento" que une os restantes 2–13:** torna práticas visíveis, auditáveis, rastreáveis e sustentáveis ao longo do tempo. Sem governação formal (US-12), controlo sistemático (US-13), ciclo de vida de contractors (US-15–17, 19–20), e reavaliação contínua (US-01, US-07, US-14, US-18), o SbD-ToE fica limitado à prática técnica pontual.
