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

**BDD.**  
- Dado que um controlo não pode ser cumprido numa aplicação classificada como L1, L2 ou L3  
- Quando submeto exceção com justificação técnica e compensação  
- Então ela é roteada para alçada apropriada, avaliada, e aprovada ou rejeitada  
- E um calendário de revalidação é automaticamente criado (L3: 3 meses, L2: 6 meses, L1: anual)  

**DoD.**  
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

**BDD.**  
- Dado contrato novo  
- Quando cláusulas são aplicadas  
- Então fornecedor compromete-se a cumprir práticas de segurança  

**DoD.**  
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

**BDD.**  
- Dado fornecedor ativo  
- Quando auditoria ocorre  
- Então relatório documenta conformidade  

**DoD.**  
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

**BDD.**  
- Dado projetos ativos  
- Quando métricas são recolhidas  
- Então dashboard mostra estado global  

**DoD.**  
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

**BDD.**  
- Dado ciclo trimestral  
- Quando KPIs são medidos  
- Então relatório é partilhado com direção  

**DoD.**  
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

**BDD.**  
- Dado um novo fornecedor classificado como L2 ou L3  
- Quando o fluxo de validação é iniciado  
- Então questionário é enviado, analisado por AppSec, e aprovação/exceção é registada  

**DoD.**  
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
- [Modelo de Validação de Fornecedores](governanca-contratacao/addon/03-modelo-validacao-fornecedores.md)  
- [Exemplos Práticos](governanca-contratacao/addon/05-exemplos-praticos.md)  

---

### US-07 - Ciclo contínuo de revisão e reavaliação de exceções
**Contexto.** Exceções esquecidas tornam-se risco permanente não mitigado.  

:::userstory
**História.**   
Como **AppSec Engineer**, quero **revisar e reavaliar exceções e compensações de forma periódica**, para **garantir que o risco residual continua mitigado e que compensações permanecem eficazes**.  

**BDD.**  
- Dado uma exceção ou compensação ativa com prazo de revisão  
- Quando chega a data de revisão agendada (ou ocorre evento crítico)  
- Então é reavaliada, revalidada, prorrogada ou encerrada  

**DoD.**  
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
- [Validação Continuada](governanca-contratacao/addon/06-validacao-continuada.md)  

---

### US-08 - Repositório de conformidade por aplicação (controlo sistemático)
**Contexto.** Sem repositório centralizado, estado de segurança fica invisível para auditores e gestão.  

:::userstory
**História.**   
Como **AppSec Engineer + Dev Lead**, quero **manter um repositório estruturado de conformidade para cada aplicação**, para **consolidar estado de todas as práticas SbD-ToE e facilitar auditorias internas e externas**.  

**BDD.**  
- Dado uma aplicação classificada como L1, L2 ou L3  
- Quando o repositório é criado ou atualizado  
- Então reflete estado de todos os capítulos (2–13) em checklist estruturado  

**DoD.**  
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
- [Controlo Sistemático das Práticas SbD-ToE](governanca-contratacao/addon/11-controlos-praticas-sbd.md)  
- [Rastreabilidade Organizacional](governanca-contratacao/addon/04-rastreabilidade-organizacional.md)  

---

### US-09 - Designação formal de owners de segurança por aplicação
**Contexto.** Sem owner claro, responsabilidade dispersa resulta em negligência de exceções e validações.  

:::userstory
**História.**   
Como **Gestão/PMO**, quero **designar formalmente um owner de segurança (Security Champion) por cada aplicação crítica**, para **garantir responsabilização clara, continuidade de decisões de segurança e comunicação de risco**.  

**BDD.**  
- Dado uma aplicação classificada como L2 ou L3  
- Quando um Security Champion é designado  
- Então ele é responsável pela submissão de exceções, validações, comunicação de risco e cumprimento de políticas  

**DoD.**  
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
- [Modelo de Governação](governanca-contratacao/addon/01-modelo-governancao.md)  
- [Formação e Onboarding (Cap. 13)](/formacao-onboarding/aplicacao-lifecycle.md)  

---

### US-10 - Validação periódica de aplicações (ciclo de conformidade)
**Contexto.** Sem validações recorrentes, desvios não são detetados até auditoria ou incidente.  

:::userstory
**História.**   
Como **AppSec Engineer + GRC Analyst**, quero **executar validações periódicas de conformidade com SbD-ToE em cada aplicação**, para **assegurar que requisitos continuam aplicados e eficazes, detetar desvios cedo, e manter evidência atualizada**.  

**BDD.**  
- Dado um calendário de revisões definido por criticidade (L3 trimestral, L2 semestral)  
- Quando ciclo de revisão chega  
- Então aplicação é reavaliada, evidência recolhida, e status atualizado no repositório  

**DoD.**  
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
- [Validação Continuada](governanca-contratacao/addon/06-validacao-continuada.md)  
- [Controlo Sistemático das Práticas](governanca-contratacao/addon/11-controlos-praticas-sbd.md)  

---

### US-11 - Consolidação de KPIs de governação e maturidade
**Contexto.** Sem métricas consolidadas, decisão executiva sobre eficácia do SbD-ToE fica sem base empírica.  

:::userstory
**História.**   
Como **CISO + Gestão Executiva**, quero **consolidar e reportar KPIs de governação (exceções, fornecedores auditados, conformidade por capítulo, maturidade)**, para **avaliar objetivamente a maturidade de segurança da organização e tomar decisões estratégicas**.  

**BDD.**  
- Dado dados de conformidade e exceções por aplicação  
- Quando ciclo de reporting chega (trimestral/semestral)  
- Então KPIs são calculados, visualizados e reportados à direção  

**DoD.**  
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
- [Governação e Maturidade](governanca-contratacao/addon/07-governancao-e-maturidade.md)  
- [Rastreabilidade Organizacional](governanca-contratacao/addon/04-rastreabilidade-organizacional.md)  

---

### US-12 - Formalização de modelo de governação por nível de risco
**Contexto.** Sem modelo formal documentado, decisões de segurança ficam dispersas entre AppSec, Gestão e Jurídico. A falta de critérios explícitos para aprovação por nível resulta em inconsistência, risco não rastreável, e desconfiança dos stakeholders.

:::userstory
**História.**   
Como **CISO + AppSec Manager**, quero **formalizar e documentar o modelo de governação com níveis de alçada explícitos, papéis e responsabilidades claras**, para **garantir que decisões de segurança são tomadas com autoridade apropriada, consistência, e rastreabilidade completa**.

**BDD.**  
- Dado que a organização adota SbD-ToE  
- Quando um novo modelo de governação é definido ou revisado  
- Então ele é documentado com alçadas por L1–L3, aprovado por direção, e comunicado a todos os stakeholders  

**DoD.**  
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
- [Modelo de Governação](governanca-contratacao/addon/01-modelo-governancao.md)  
- [Exemplos de Decisão](governanca-contratacao/addon/05-exemplos-praticos.md)  
- [Formação de Governação (Cap. 13)](/formacao-onboarding/aplicacao-lifecycle.md)  

---

### US-13 - Controlo sistemático e periódico por capítulo SbD-ToE
**Contexto.** Sem checklist centralizado de conformidade, o estado de conformidade de uma aplicação com Cap. 2–13 fica invisível. Desvios não são detetados até auditoria ou incidente crítico. Gestão não tem visibilidade do progresso.

:::userstory
**História.**   
Como **AppSec Engineer + Dev Lead**, quero **manter um checklist centralizado, versionado e auditável de conformidade com todos os capítulos SbD-ToE (2–13), com verificação periódica por release ou evento crítico**, para **consolidar estado real de todas as práticas e facilitar auditorias, decisão de risco, e demonstração de conformidade normativa**.

**BDD.**  
- Dado uma aplicação classificada como L1, L2 ou L3  
- Quando um ciclo de validação é acionado (por release, trimestral L3, semestral L2, ou evento crítico)  
- Então checklist é preenchido com estado, evidência é ligada, e relatório é gerado  

**DoD.**  
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
- [Controlo Sistemático das Práticas SbD-ToE](governanca-contratacao/addon/11-controlos-praticas-sbd.md)  
- [Rastreabilidade Organizacional](governanca-contratacao/addon/04-rastreabilidade-organizacional.md)  
- [Validação Periódica](governanca-contratacao/addon/06-validacao-continuada.md)  

---

### US-14 - Reavaliação contínua e rotação de fornecedores pós-onboarding
**Contexto.** Fornecedores são validados no onboarding, mas sem revisão periódica, desvios surgem ao longo do tempo (novos CVEs não mitigados, SLA não cumprido, mudanças de propriedade, evolução do risco). Risco residual acumula invisível. Contratos expiram sem renovação de validação.

:::userstory
**História.**   
Como **Procurement Officer + AppSec Engineer**, quero **reavalia e reaprovar fornecedores periodicamente (anual por defaut, semestral para L2, trimestral para L3), com validação técnica atualizada, análise de compliance SLA, e escalada para decisão de penalização ou substituição se necessário**, para **assegurar que continuam a cumprir requisitos e SLA, que risco é mitigado, e que decisões de continuidade são baseadas em evidência**.

**BDD.**  
- Dado um fornecedor ativo com contrato vigente  
- Quando chega data de revisão agendada (calendário) ou evento crítico ocorre (incidente, CVE crítico, mudança SLA)  
- Então fornecedor é reavaliado com questionário atualizado, evidência técnica validada (SBOM, SLA compliance, mudanças) e decisão é formalizada  

**DoD.**  
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
- [Modelo de Validação de Fornecedores](governanca-contratacao/addon/03-modelo-validacao-fornecedores.md)  
- [Validação Continuada](governanca-contratacao/addon/06-validacao-continuada.md)  
- [Exemplos de Aplicação](governanca-contratacao/addon/05-exemplos-praticos.md)  

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

---

## 🏁 Recomendações finais

- **Exceções sem registo = risco invisível.** Operacionalize US-01 (com alçadas claras) e US-07 para garantir rastreabilidade contínua e revalidação automática.  
- **Modelo formal é o alicerce.** US-12 documenta governação com critérios explícitos, alçadas por L1–L3, e formação obrigatória para approvers (Cap. 13).  
- **Fornecedores devem ser parte do modelo SbD-ToE.** Use US-02, US-06 e US-14 para integração contratual, validação inicial, e reavaliação periódica contínua.  
- **Designação clara de owners elimina responsabilidade dispersa.** US-09 garante continuidade de decisões de segurança com formação validada.  
- **Repositório centralizado de conformidade dá visibilidade total.** US-08 e US-13 consolidam estado de todas as práticas por aplicação, capítulo e ciclo.  
- **Validações periódicas detetam desvios cedo.** US-10 integra revisão contínua no ciclo de vida; US-13 valida por capítulo; US-14 reavalia fornecedores.  
- **KPIs de governação são a medida objetiva da maturidade.** US-05 e US-11 permitem decisão estratégica baseada em evidência (% conformidade, % exceções resolvidas, % fornecedores auditados).  
- **Rastreabilidade organizacional dá transparência à gestão.** US-04 agregada com US-08, US-10, US-13, US-14 cria visibilidade de risco em todos os níveis.  
- **Este capítulo é o "cimento" que une os restantes 2–13:** torna práticas visíveis, auditáveis, rastreáveis e sustentáveis ao longo do tempo. Sem governação formal (US-12), controlo sistemático (US-13), e reavaliação contínua (US-01, US-07, US-14), o SbD-ToE fica limitado à prática técnica pontual.
