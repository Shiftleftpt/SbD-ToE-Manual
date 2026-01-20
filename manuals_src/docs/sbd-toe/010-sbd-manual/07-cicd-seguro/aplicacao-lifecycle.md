---
id: aplicacao-lifecycle
title: Como Fazer
description: Como aplicar as práticas de CI/CD seguro ao longo do ciclo de vida da aplicação, com proporcionalidade por risco, user stories normalizadas e evidências auditáveis
tags: [tipo:aplicacao, ciclo-vida, cicd, devsecops, pipelines, seguranca, rastreabilidade]
genia: us-format-normalization
---

# 📅 Aplicação no Ciclo de Vida - CI/CD Seguro

Enquanto o `intro.md` explica **porque os pipelines são críticos** e que práticas devem ser aplicadas, este documento mostra **como transformar essas prescrições em ações concretas** ao longo do ciclo de vida de desenvolvimento e entrega.

O princípio orientador é simples e não negociável:

- o pipeline pode automatizar **execução** e produzir **sinais**;
- mas a organização só ganha segurança quando existe **decisão humana atribuída**, **validação empírica** e **evidência auditável**.

À medida que a automação se torna mais sofisticada, surgem riscos de processo adicionais: não-determinismo, “aprovação implícita” por outputs, evidência plausível sem execução real, fuga de contexto e diluição de responsabilidade.  
Este documento operacionaliza essas preocupações sem “falar de tecnologia”: trata-as como **controlos de engenharia** e **governação do pipeline**.

---

## 🧭 Quando aplicar

A segurança em pipelines não acontece apenas quando algo corre mal — ela é parte do seu ADN desde o primeiro commit.  
Sempre que se cria, altera, executa ou promove um pipeline, existem *triggers* que exigem controlos específicos:

| Momento *trigger*                                                   | Objetivo de segurança                                                                 | Papéis principais                               |
|--------------------------------------------------------------------|----------------------------------------------------------------------------------------|------------------------------------------------|
| Criação ou refactor do pipeline                                    | Introduzir controlos base, garantir auditabilidade e evitar alterações “fora do PR”    | Developers, DevOps / SRE                       |
| Alteração de regras de decisão (gates/thresholds)                  | Garantir separação entre sinal automático e decisão; evitar bypass implícito           | AppSec Engineers, DevOps / SRE, GRC / Compliance |
| Alteração de tooling/infra (runners, permissões, segredos)         | Rever isolamento, injeção de segredos, blast radius e não-repúdio                      | DevOps / SRE, AppSec Engineers                 |
| Introdução/atualização de validadores (scanners, testes, policies) | Aumentar cobertura e gates proporcionais ao risco; garantir evidência de execução real | Developers, AppSec Engineers, DevOps / SRE     |
| Integração de serviços externos no pipeline                        | Tratar como dependência; minimizar contexto; mitigar risco de exfiltração              | DevOps / SRE, AppSec Engineers, GRC / Compliance |
| Preparação de release / promoção a produção                        | Validar assinatura, proveniência, rastreabilidade e responsabilidade humana            | DevOps / SRE, AppSec Engineers                 |
| Registo de exceção (*bypass* de gate)                              | Aprovação formal, prazos, compensações e reversão automática                            | GRC / Compliance, Auditores Internos, AppSec Engineers |
| Auditoria ou revisão periódica                                     | Demonstrar rastreabilidade ponta-a-ponta e reprodutibilidade                            | GRC / Compliance, Auditores Internos, DevOps / SRE |

---

## 👥 Quem executa cada ação

A responsabilidade em CI/CD é **partilhada**.  
Um pipeline seguro resulta da soma de esforços: do programador que submete código com validações ativas, ao DevOps que endurece runners e segredos, até ao GRC que controla exceções e evidencia governação.

| Ação operacional                                                                 | Responsável                 | Apoio                                  | Evidência/Artefactos |
|----------------------------------------------------------------------------------|-----------------------------|----------------------------------------|----------------------|
| Definir/alterar pipeline versionado via PR                                        | Developers                  | DevOps / SRE                           | `ci-pipeline.yml`, histórico de revisão |
| Definir regras de decisão (gates/thresholds) explícitas e binárias por risco      | AppSec Engineers            | DevOps / SRE, GRC / Compliance         | Regras de gates, critérios publicados, registos de alteração |
| Endurecer runners (ephemerais, não-privilegiados, segregados)                     | DevOps / SRE                | AppSec Engineers                       | Configuração de runners, imagens base, evidência de isolamento |
| Integrar validadores (SAST, secrets, IaC, containers, SBOM, DAST quando aplicável)| Developers                  | AppSec Engineers, DevOps / SRE         | Relatórios + logs de execução + *exit codes* |
| Injeção segura de segredos (OIDC, TTL curto, masked logs)                         | DevOps / SRE                | AppSec Engineers                       | Políticas de segredos, logs de acesso, evidência de rotação/TTL |
| Assinar artefactos e gerar proveniência                                           | DevOps / SRE                | AppSec Engineers                       | Assinaturas, proveniência, logs de verificação antes de promoção |
| Aprovar promoção/deploy (ações irreversíveis) com owner explícito                 | DevOps / SRE                | AppSec Engineers (L2/L3), GRC (L3)     | Registo nominal de aprovação, contexto e evidência associada |
| Registar e aprovar exceções (com prazo e compensações)                            | GRC / Compliance, Auditores Internos | AppSec Engineers                   | Registo formal de exceções e aprovações, TTL, plano compensatório |
| Garantir rastreabilidade commit→pipeline→release                                  | DevOps / SRE                | GRC / Compliance, Auditores Internos   | Logs correlacionados, IDs, export imutável (quando aplicável) |
| Garantir higiene de logs/outputs (minimização de contexto sensível)               | DevOps / SRE                | AppSec Engineers                       | Política de logging, evidência de mascaramento/redação, revisão periódica |

---

## 🧾 User Stories normalizadas

Cada prática é expressa como **user story reutilizável**, com critérios verificáveis, artefactos concretos e proporcionalidade por nível de risco.

> Nota editorial: estas user stories assumem explicitamente que **“output bonito” não é evidência** e que **sugestões nunca equivalem a decisão**.  
> Sempre que existam sinais automáticos (scores, recomendações, flags), estes são tratados como *inputs* para uma decisão humana formal.

---

### US-01 - Gestão segura de código fonte

**Contexto.**  
Sem controlo sobre o repositório, qualquer pipeline é vulnerável.

:::userstory
**História.**  
Como **Developers**, quero que todas as alterações ao repositório sejam protegidas por PR e revisão obrigatória, para garantir integridade.

**Critérios de aceitação (BDD).**
- **Dado** que existe um repositório protegido  
  **Quando** submeto um PR para `main`  
  **Então** só é aceite após revisão obrigatória e todos os *checks* concluídos com sucesso.  
- **Dado** que ocorre um *merge*  
  **Quando** são detetados conflitos ou alterações relevantes na superfície de ataque  
  **Então** é exigida nova revisão e reexecução automática dos validadores definidos.  

**Checklist.**
- [ ] Branch protection ativa  
- [ ] Reviewer obrigatório  
- [ ] Status checks configurados  
- [ ] Proibido `force push`
:::

**🧾 Artefactos & evidências.**  
Políticas de branch protection; logs de revisão; histórico Git; auditoria de merges.

**⚖️ Proporcionalidade.**
| Nível | Obrigatório? | Ajustes |
|-------|---------------|----------|
| L1 | Sim | Revisão simples e *build check* obrigatório |
| L2 | Sim | Revisor técnico + validação de segurança ativa |
| L3 | Sim | Revisão dupla (code owner + AppSec) e bloqueio em falhas High |

---

### US-02 - Design seguro dos pipelines (versionamento, determinismo e revisão)

**Contexto.**  
Pipelines inseguros são alvos privilegiados de ataque — e pipelines não reprodutíveis destroem auditoria.

:::userstory
**História.**  
Como **DevOps / SRE**, quero pipelines versionados e aprovados por PR, com comportamento determinístico, para evitar alterações não auditadas e resultados não reproduzíveis.

**Critérios de aceitação (BDD).**
- **Dado** que altero a definição do pipeline  
  **Quando** submeto PR  
  **Então** só é aceite após revisão por DevOps e AppSec (em L2/L3).  
- **Dado** que o pipeline depende de configuração ou parâmetros  
  **Quando** é executado  
  **Então** a configuração efetiva usada é registada como evidência (sem dados sensíveis).  
- **Dado** que há alteração de ferramentas, etapas ou regras de execução  
  **Quando** o pipeline é modificado  
  **Então** é criada nova versão rastreável e auditável (commit/hash + changelog no PR).  

**Checklist.**
- [ ] `ci-pipeline.yml` versionado  
- [ ] PR obrigatório  
- [ ] Triggers explícitos  
- [ ] Configuração efetiva registada (sem segredos)  
- [ ] Histórico de versões mantido
:::

**🧾 Artefactos & evidências.**  
Histórico de commits; ficheiro `ci-pipeline.yml`; aprovação PR; logs de revisão; registo de configuração efetiva.

**⚖️ Proporcionalidade.**
| Nível | Obrigatório? | Ajustes |
|---|---|---|
| L1 | Sim | Versão única do pipeline com aprovação manual |
| L2 | Sim | Versionamento e revisão obrigatória |
| L3 | Sim | Controlo de alterações assinado e validação reforçada de proveniência |

---

### US-03 - Scanners integrados (validação empírica obrigatória)

**Contexto.**  
Detetar cedo é mais barato e eficaz — mas só conta se houver execução real.

:::userstory
**História.**  
Como **Developers**, quero que o pipeline execute validadores de segurança com execução observável, para impedir falhas graves em produção.

**Critérios de aceitação (BDD).**
- **Dado** que submeto código  
  **Quando** corre o pipeline  
  **Então** os validadores obrigatórios são executados e produzem logs/artefactos rastreáveis.  
- **Dado** que existem falhas críticas  
  **Quando** os resultados são avaliados  
  **Então** o merge/promoção é bloqueado de acordo com os gates definidos.  
- **Dado** que é introduzido novo tipo de artefacto  
  **Quando** o conjunto atual de validação não o cobre  
  **Então** o AppSec define regra adicional e a mudança é versionada e aprovada.

**Checklist.**
- [ ] SAST ativo  
- [ ] Secrets scanning ativo  
- [ ] IaC scanning (quando aplicável)  
- [ ] Logs/artefactos de execução guardados  
- [ ] Falhas High bloqueiam merge (L2/L3)
:::

**🧾 Artefactos & evidências.**  
Relatórios de scanners; logs CI/CD; *exit codes*; registos de bloqueio; dashboards de vulnerabilidades.

**⚖️ Proporcionalidade.**
| Nível | Obrigatório? | Ajustes |
|---|---|---|
| L1 | Sim | Validação base (SAST, secrets) |
| L2 | Sim | Inclusão de IaC e análise de dependências |
| L3 | Sim | Validação completa incluindo containers e SBOM |

---

### US-04 - Gestão de segredos

**Contexto.**  
Segredos estáticos expõem a organização — e logs descuidados tornam-se um canal de fuga.

:::userstory
**História.**  
Como **DevOps / SRE**, quero segredos injetados por OIDC com TTL curto e outputs mascarados, para reduzir risco de abuso e exposição indireta.

**Critérios de aceitação (BDD).**
- **Dado** que o pipeline arranca  
  **Quando** credenciais são necessárias  
  **Então** são emitidas *just-in-time*, com TTL curto e sem exposição em logs.  
- **Dado** que o token expira  
  **Quando** é necessário novo acesso  
  **Então** é gerado token temporário novo sem reutilização.  

**Checklist.**
- [ ] OIDC configurado  
- [ ] TTL curto  
- [ ] Variáveis mascaradas  
- [ ] Logging revisto para não expor contexto sensível
:::

**🧾 Artefactos & evidências.**  
Políticas de segredos; logs de acesso; configuração OIDC; evidência de TTL/rotação.

**⚖️ Proporcionalidade.**
| Nível | Obrigatório? | Ajustes |
|---|---|---|
| L1 | Opcional | Segredos armazenados encriptados + masking |
| L2 | Sim | OIDC implementado com TTL controlado |
| L3 | Sim | Tokens efémeros automáticos e rotação frequente |

---

### US-05 - Isolamento de runners

**Contexto.**  
Runners inseguros comprometem todo o ecossistema.

:::userstory
**História.**  
Como **DevOps / SRE**, quero runners ephemerais e segregados, para reduzir persistência pós-compromisso e limitar blast radius.

**Critérios de aceitação (BDD).**
- **Dado** que um job termina  
  **Quando** o runner encerra  
  **Então** é destruído sem manter estado.  
- **Dado** que há pipelines paralelos  
  **Quando** são executados  
  **Então** estão isolados por permissões, namespace e segmentação de rede.  

**Checklist.**
- [ ] Runners efémeros  
- [ ] Sem privilégios excessivos  
- [ ] Segmentação de rede  
- [ ] Sem estado persistente entre jobs
:::

**🧾 Artefactos & evidências.**  
Configuração de runners; logs de execução; registos de isolamento; scripts de provisionamento.

**⚖️ Proporcionalidade.**
| Nível | Obrigatório? | Ajustes |
|---|---|---|
| L1 | Opcional | Runners partilhados com limites e hardening |
| L2 | Sim | Segregação de runners por projeto |
| L3 | Sim | Runners efémeros + rede isolada + destruição automática |

---

### US-06 - Assinatura e proveniência

**Contexto.**  
Artefactos não assinados perdem legitimidade — e artefactos sem proveniência enfraquecem auditoria e confiança.

:::userstory
**História.**  
Como **DevOps / SRE**, quero que todos os artefactos sejam assinados e tenham proveniência validada, para garantir confiança e permitir verificação independente.

**Critérios de aceitação (BDD).**
- **Dado** que um artefacto é produzido  
  **Quando** é promovido  
  **Então** assinatura e proveniência são verificadas antes da promoção.  
- **Dado** que falha verificação  
  **Quando** a assinatura/proveniência não é válida  
  **Então** o artefacto é rejeitado e é emitido alerta.

**Checklist.**
- [ ] Assinatura automática  
- [ ] Proveniência gerada  
- [ ] Verificação antes de release  
- [ ] Rejeição automática em falha (L2/L3)
:::

**🧾 Artefactos & evidências.**  
Assinaturas digitais; ficheiros de proveniência; logs de promoção; auditoria de build.

> **Referência:** Este US complementa o princípio de gerar SBOM por build, integrando assinatura e proveniência como artefactos de build.

**⚖️ Proporcionalidade.**
| Nível | Obrigatório? | Ajustes |
|---|---|---|
| L1 | Sim | Assinatura recomendada + verificação manual em releases |
| L2 | Sim | Assinatura automática + verificação obrigatória |
| L3 | Sim | Bloqueio automático + validações reforçadas de proveniência |

---

### US-07 - Gates por risco (separação sinal/decisão)

**Contexto.**  
Nem todas as apps exigem o mesmo rigor — mas em nenhuma app um “sinal” substitui decisão.

:::userstory
**História.**  
Como **AppSec Engineers**, quero gates distintos por L1–L3 e explicitamente binários, para aplicar segurança proporcional e evitar bypass implícito.

**Critérios de aceitação (BDD).**
- **Dado** que uma aplicação é L3  
  **Quando** há falha High ou Critical  
  **Então** o gate bloqueia a promoção e exige decisão humana formal para qualquer exceção.  
- **Dado** que uma aplicação é L1  
  **Quando** há falha Medium  
  **Então** é registado alerta sem bloqueio, mas com rastreabilidade e backlog de remediação.  
- **Dado** que existe um output automático (score/recomendação)  
  **Quando** é apresentado  
  **Então** é tratado apenas como input, nunca como aprovação.

**Checklist.**
- [ ] Política publicada  
- [ ] Gates configurados  
- [ ] Thresholds definidos  
- [ ] Separação entre sinal e decisão documentada
:::

**🧾 Artefactos & evidências.**  
Políticas de gates; logs de bloqueio; registos de alteração de thresholds; evidência de decisão em exceções.

**⚖️ Proporcionalidade.**
| Nível | Obrigatório? | Ajustes |
|---|---|---|
| L1 | Sim | Bloqueio apenas em Critical |
| L2 | Sim | Bloqueio High/Critical + aprovação AppSec para exceções |
| L3 | Sim | Bloqueio automático + governança reforçada (incl. GRC em exceções) |

---

### US-08 - Cobertura ampliada (containers e SBOM)

**Contexto.**  
Cobertura limitada cria pontos cegos e fragiliza supply chain.

:::userstory
**História.**  
Como **AppSec Engineers**, quero validação de containers e SBOM em pipelines, para cobrir supply chain e permitir rastreabilidade de componentes.

**Critérios de aceitação (BDD).**
- **Dado** que uma imagem é construída  
  **Quando** corre o pipeline  
  **Então** o SBOM é gerado e anexado ao artefacto.  
- **Dado** que uma imagem base muda  
  **Quando** vulnerabilidade é detetada  
  **Então** é aberta tarefa de mitigação e o risco é rastreável ao release afetado.

**Checklist.**
- [ ] Container scanning ativo  
- [ ] SBOM gerado  
- [ ] Base images validadas  
- [ ] Evidência de execução guardada
:::

**🧾 Artefactos & evidências.**  
Relatórios de scanning; SBOM; auditoria de imagens; logs de builds.

**⚖️ Proporcionalidade.**
| Nível | Obrigatório? | Ajustes |
|---|---|---|
| L1 | Opcional | Scans de imagens base periódicos |
| L2 | Sim | SBOM obrigatório + validação de base images |
| L3 | Sim | Scans contínuos + correlação de CVEs + bloqueios em risco crítico |

---

### US-09 - Rastreabilidade ponta-a-ponta (commit→pipeline→release)

**Contexto.**  
Sem rastreio, auditoria é impossível — e investigação de incidentes torna-se especulativa.

:::userstory
**História.**  
Como **GRC / Compliance**, quero rastrear commit→pipeline→release, para suportar auditorias e investigação de incidentes.

**Critérios de aceitação (BDD).**
- **Dado** que ocorre um incidente  
  **Quando** analiso um release  
  **Então** consigo traçar origem até commit e execução do pipeline.  
- **Dado** que um auditor pede evidências  
  **Quando** executo consulta  
  **Então** o sistema exporta logs correlacionados e verificáveis (sem dados sensíveis).

**Checklist.**
- [ ] IDs de correlação  
- [ ] Logs retidos  
- [ ] Export imutável (quando aplicável)  
- [ ] Ligação explícita entre artefactos e execução
:::

**🧾 Artefactos & evidências.**  
Logs de pipelines; dashboards; registos de auditoria; exports (imutáveis quando exigido).

**⚖️ Proporcionalidade.**
| Nível | Obrigatório? | Ajustes |
|---|---|---|
| L1 | Sim | Logs básicos armazenados 30 dias |
| L2 | Sim | Retenção 90 dias + correlação commit-build |
| L3 | Sim | Retenção ≥1 ano + exportação imutável + auditoria reforçada |

---

### US-10 - Gestão de exceções (bypass controlado)

**Contexto.**  
Exceções mal geridas tornam-se risco estrutural e normalizam bypass.

:::userstory
**História.**  
Como **GRC / Compliance**, quero exceções registadas, aprovadas e temporárias, para evitar acumulação de dívida e manter governação.

**Critérios de aceitação (BDD).**
- **Dado** que uma exceção é pedida  
  **Quando** é analisada  
  **Então** só é aprovada com prazo, owner e compensações definidas.  
- **Dado** que o prazo expira  
  **Quando** não há renovação formal  
  **Então** a exceção é removida e o pipeline volta ao modo normal de controlo.

**Checklist.**
- [ ] Owner registado  
- [ ] Prazo definido  
- [ ] Aprovação dupla (AppSec + GRC) em L2/L3  
- [ ] Registo de compensações  
- [ ] Reversão automática no fim do prazo
:::

**🧾 Artefactos & evidências.**  
Registo de exceções; logs de aprovação; relatórios de revisão; prazos automáticos no sistema de GRC.

**⚖️ Proporcionalidade.**
| Nível | Obrigatório? | Ajustes |
|---|---|---|
| L1 | Sim | Registo simples com aprovação única |
| L2 | Sim | Aprovação dupla e prazo máximo (ex.: 60 dias) |
| L3 | Sim | Revisão frequente + auditoria obrigatória |

---

### US-11 - Testes de segurança dinâmicos (DAST)

**Contexto.**  
Testes estáticos apenas cobrem parcialmente; DAST em staging valida comportamento real.

:::userstory
**História.**  
Como **AppSec Engineers**, quero executar DAST em staging após deployment, para validar vulnerabilidades comportamentais antes de produção.

**Critérios de aceitação (BDD).**
- **Dado** que uma build é promovida a staging  
  **Quando** inicia pipeline DAST  
  **Então** são executadas análises relevantes e os resultados são rastreáveis ao commit/release.  
- **Dado** que DAST encontra falha High  
  **Quando** o resultado é disponibilizado  
  **Então** bloqueia promoção a produção até correção validada.

**Checklist.**
- [ ] DAST integrado no pipeline  
- [ ] Credenciais de teste segregadas  
- [ ] Relatório correlacionado com commit  
- [ ] Bloqueio automático em High/Critical (L2/L3)
:::

**🧾 Artefactos & evidências.**  
Relatórios DAST; logs de execução; evidências de correção; rastreabilidade.

**⚖️ Proporcionalidade.**
| Nível | Obrigatório? | Ajustes |
|---|---|---|
| L1 | Opcional | DAST manual periódico |
| L2 | Sim | DAST em staging pré-release |
| L3 | Sim | DAST contínuo + bloqueio automático + revalidação pós-correção |

---

### US-12 - Métricas e conformidade organizacional

**Contexto.**  
Sem visibilidade centralizada, risco acumula-se invisível.

:::userstory
**História.**  
Como **Gestão Executiva / CISO**, quero visualizar métricas de CI/CD (cobertura, gates, exceções, bloqueios, MTTR), para decisão informada e ação corretiva.

**Critérios de aceitação (BDD).**
- **Dado** que o pipeline executa  
  **Quando** ocorrem eventos (merge, bloqueio, exceção, promoção)  
  **Então** são registados com timestamp, contexto e atores.  
- **Dado** que consulto o dashboard  
  **Quando** filtro por projeto/período/risco  
  **Então** obtenho indicadores acionáveis e auditáveis.

**Checklist.**
- [ ] Eventos centralizados  
- [ ] Dashboard com KPIs (cobertura, MTTR, compliance rate)  
- [ ] Alertas em anomalias  
- [ ] Relatórios periódicos para GRC
:::

**🧾 Artefactos & evidências.**  
Dashboard; logs centralizados; relatórios; alertas; evidência de retenção.

**⚖️ Proporcionalidade.**
| Nível | Obrigatório? | Ajustes |
|---|---|---|
| L1 | Opcional | Relatórios manuais periódicos |
| L2 | Sim | Dashboard com KPIs principais, atualizado diariamente |
| L3 | Sim | Dashboard quase em tempo real + alertas automáticos |

---

### US-13 - Validação de integridade de imagens base

**Contexto.**  
Imagens base comprometidas propagam risco a todo o ecossistema.

:::userstory
**História.**  
Como **DevOps / SRE**, quero validar integridade de imagens base (hash/assinatura/drift) e correlacionar com vulnerabilidades, para evitar supply chain comprometido.

**Critérios de aceitação (BDD).**
- **Dado** que uma imagem base é usada  
  **Quando** o pipeline inicia  
  **Então** o identificador esperado é validado contra fonte confiável.  
- **Dado** que surge vulnerabilidade relevante  
  **Quando** afeta imagens em uso  
  **Então** é criado alerta e aberta ação de mitigação rastreável ao release.

**Checklist.**
- [ ] Hash/assinatura de imagens base registado  
- [ ] Validação automática no pull  
- [ ] Rejeição em mismatch (L2/L3)  
- [ ] Correlação contínua com vulnerabilidades
:::

**🧾 Artefactos & evidências.**  
Registos de hashes/assinaturas; logs de validação; relatórios de drift; ações de mitigação.

**⚖️ Proporcionalidade.**
| Nível | Obrigatório? | Ajustes |
|---|---|---|
| L1 | Opcional | Validação manual periódica |
| L2 | Sim | Validação automática no pull com logs |
| L3 | Sim | Validação + assinatura + alertas automáticos em drift/vulnerabilidade |

---

## 🆕 User Stories adicionais (riscos de processo do CI/CD moderno)

As user stories seguintes tornam explícitas as preocupações de processo que, na prática, mais degradam a segurança quando a automação aumenta: **não-determinismo, confusão sinal/decisão, evidência fraca, fuga de contexto e diluição de responsabilidade**.

---

### US-14 - Reprodutibilidade e determinismo do pipeline

**Contexto.**  
Sem reprodutibilidade, não há auditoria nem investigação de incidentes.

:::userstory
**História.**  
Como **DevOps / SRE**, quero que execuções do pipeline sejam reprodutíveis e determinísticas (na medida do possível), para permitir verificação independente e auditoria.

**Critérios de aceitação (BDD).**
- **Dado** que um build é executado  
  **Quando** volto a executar o mesmo pipeline sobre o mesmo commit  
  **Então** obtenho resultados equivalentes (ou divergências justificadas e registadas).  
- **Dado** que existem parâmetros/configuração  
  **Quando** o pipeline corre  
  **Então** a configuração efetiva usada é registada como evidência (sem segredos).  

**Checklist.**
- [ ] Definição do pipeline versionada  
- [ ] Dependências e versões relevantes estabilizadas/identificadas  
- [ ] Configuração efetiva registada  
- [ ] Divergências documentadas quando inevitáveis
:::

**🧾 Artefactos & evidências.**  
Execução rastreável (logs + config efetiva); ligação a commit; registos de divergência; artefactos produzidos.

**⚖️ Proporcionalidade.**
| Nível | Obrigatório? | Ajustes |
|---|---|---|
| L1 | Sim | Reprodutibilidade “boa-fé” com logging suficiente |
| L2 | Sim | Reprodutibilidade como requisito; validação periódica |
| L3 | Sim | Reprodutibilidade obrigatória + auditoria reforçada e retenção prolongada |

---

### US-15 - Separação formal entre sinal automático e decisão de promoção

**Contexto.**  
Um “score verde” não é uma decisão; uma decisão exige owner e evidência.

:::userstory
**História.**  
Como **AppSec Engineers**, quero que qualquer recomendação/score/flag seja formalmente classificada como *sinal*, e que a promoção exija decisão humana explícita, para evitar aprovação implícita.

**Critérios de aceitação (BDD).**
- **Dado** que o pipeline produz sinais (scores/recomendações)  
  **Quando** a promoção é considerada  
  **Então** a decisão é registada com owner humano e evidência associada.  
- **Dado** que alguém tenta promover sem decisão formal  
  **Quando** o pipeline avalia a ação  
  **Então** bloqueia e exige registo nominal de aprovação.

**Checklist.**
- [ ] Distinção “sinal” vs “decisão” documentada  
- [ ] Promoção exige aprovação nominal  
- [ ] Registo inclui evidência referenciada  
- [ ] Bloqueio automático a promoções “sem owner”
:::

**🧾 Artefactos & evidências.**  
Registo de aprovação; evidência associada; logs de bloqueio; política publicada.

**⚖️ Proporcionalidade.**
| Nível | Obrigatório? | Ajustes |
|---|---|---|
| L1 | Sim | Aprovação nominal para produção |
| L2 | Sim | Aprovação nominal + regra de separação de funções |
| L3 | Sim | Aprovação nominal + auditoria reforçada + regra estrACI (approval control integrity) |

---

### US-16 - Evidência empírica obrigatória (anti-“relatórios sem execução”)

**Contexto.**  
Resultados plausíveis não substituem execução real.

:::userstory
**História.**  
Como **GRC / Compliance**, quero que qualquer evidência de controlo em CI/CD seja baseada em execução observável (logs, *exit codes*, artefactos), para impedir conformidade aparente sem validação real.

**Critérios de aceitação (BDD).**
- **Dado** que existe um relatório de validação  
  **Quando** é usado como evidência  
  **Então** contém referência verificável à execução (job/run id, logs, artefactos).  
- **Dado** que não existe execução observável  
  **Quando** alguém tenta registar um resultado como evidência  
  **Então** é rejeitado como “não verificável”.

**Checklist.**
- [ ] Evidência liga a uma execução real  
- [ ] Logs e *exit codes* disponíveis  
- [ ] Artefactos preservados conforme retenção  
- [ ] Rejeição de evidência não verificável
:::

**🧾 Artefactos & evidências.**  
Run IDs; logs; *exit codes*; artefactos; política de evidência.

**⚖️ Proporcionalidade.**
| Nível | Obrigatório? | Ajustes |
|---|---|---|
| L1 | Sim | Evidência mínima por execução |
| L2 | Sim | Evidência obrigatória + retenção reforçada |
| L3 | Sim | Evidência obrigatória + export imutável e auditoria |

---

### US-17 - Contenção de contexto e higiene de logs/outputs

**Contexto.**  
O pipeline “vê” tudo — logo, é onde a fuga de contexto é mais provável.

:::userstory
**História.**  
Como **DevOps / SRE**, quero que logs e outputs do pipeline sejam minimizados e higienizados, para impedir exposição de segredos, dados sensíveis ou propriedade intelectual.

**Critérios de aceitação (BDD).**
- **Dado** que o pipeline executa  
  **Quando** gera logs  
  **Então** segredos e identificadores sensíveis são mascarados/redigidos por defeito.  
- **Dado** que é necessário debug  
  **Quando** é ativado temporariamente  
  **Então** exige aprovação, é limitado no tempo e produz evidência de desativação.

**Checklist.**
- [ ] Política de logging publicada  
- [ ] Masking/redação ativa por defeito  
- [ ] Debug temporário controlado e auditável  
- [ ] Revisão periódica de logs e configurações
:::

**🧾 Artefactos & evidências.**  
Configuração de logging; evidência de masking; registos de ativação/desativação de debug; relatórios de revisão.

**⚖️ Proporcionalidade.**
| Nível | Obrigatório? | Ajustes |
|---|---|---|
| L1 | Sim | Masking básico + revisão pontual |
| L2 | Sim | Masking + controlo formal de debug |
| L3 | Sim | Controlo formal + auditoria + retenção e export conforme exigência |

---

### US-18 - Não-repúdio e ownership de promoções (ações irreversíveis)

**Contexto.**  
Se ninguém “assina” a promoção, ninguém responde pelo incidente.

:::userstory
**História.**  
Como **DevOps / SRE**, quero que qualquer promoção para produção tenha owner humano explícito e registo de decisão, para garantir não-repúdio e responsabilização.

**Critérios de aceitação (BDD).**
- **Dado** que uma promoção para produção é solicitada  
  **Quando** é executada  
  **Então** existe registo nominal de aprovação e contexto de decisão (evidência referenciada).  
- **Dado** que não existe owner  
  **Quando** alguém tenta promover  
  **Então** o pipeline bloqueia a ação.

**Checklist.**
- [ ] Promoção exige owner humano  
- [ ] Registo nominal e timestamp  
- [ ] Evidência referenciada (runs, artefactos, relatórios)  
- [ ] Bloqueio a promoções sem registo
:::

**🧾 Artefactos & evidências.**  
Registo de aprovação; logs do pipeline; evidência associada; trilho de auditoria.

**⚖️ Proporcionalidade.**
| Nível | Obrigatório? | Ajustes |
|---|---|---|
| L1 | Sim | Aprovação nominal para produção |
| L2 | Sim | Aprovação nominal + separação de funções |
| L3 | Sim | Aprovação nominal + auditoria reforçada e retenção prolongada |

---

## 📦 Artefactos esperados

Cada prática deixa pegadas técnicas. Sem elas, não há prova de conformidade:

| Artefacto / Evidência                              | Dono                         | Observações |
|---------------------------------------------------|------------------------------|------------|
| `ci-pipeline.yml`                                 | Developers                   | Versionado via PR (US-01, US-02) |
| Registo de configuração efetiva (sem segredos)     | DevOps / SRE                 | Suporta reprodutibilidade (US-02, US-14) |
| Regras de gates/thresholds publicadas              | AppSec Engineers             | Separação sinal/decisão (US-07, US-15) |
| Logs + *exit codes* + artefactos de execução       | DevOps / SRE                 | Evidência empírica (US-03, US-16) |
| Assinaturas + proveniência                         | DevOps / SRE                 | Verificação antes de promoção (US-06) |
| Relatórios de validadores (SAST, secrets, etc.)    | Developers / AppSec Engineers| Sempre ligados a execução real (US-03, US-16) |
| SBOM por build                                     | AppSec Engineers             | Anexado ao artefacto (US-08) |
| Registo de exceções (TTL, compensações, approvals) | GRC / Compliance             | Governação de bypass (US-10) |
| Logs correlacionados commit→pipeline→release        | DevOps / SRE                 | Rastreabilidade auditável (US-09) |
| Política e evidência de higiene de logs            | DevOps / SRE                 | Minimização de contexto (US-17) |
| Registos nominais de promoção/deploy               | DevOps / SRE                 | Não-repúdio (US-18) |
| Dashboard de métricas e eventos                     | Gestão Executiva / CISO      | Visibilidade organizacional (US-12) |

---

## ⚖️ Matriz de proporcionalidade L1–L3

Nem todas as apps exigem o mesmo nível de rigor.  
A matriz assegura que o esforço é proporcional ao risco **sem nunca comprometer**: decisão humana, evidência empírica e rastreabilidade.

| Categoria           | L1 (baixo)                        | L2 (médio)                                 | L3 (crítico) |
|--------------------|-----------------------------------|--------------------------------------------|--------------|
| Branches/PR         | 1 reviewer + build check          | Reviewer + validação de segurança           | ≥2 reviewers + code owners + AppSec |
| Determinismo        | Logging suficiente                 | Reprodutibilidade como requisito            | Reprodutibilidade + auditoria reforçada |
| Sinal vs decisão    | Aprovação nominal para produção    | Aprovação nominal + separação de funções    | Aprovação nominal + controlo reforçado + auditoria |
| Evidência empírica  | Logs básicos + artefactos chave    | Logs + *exit codes* + retenção reforçada    | Evidência completa + export imutável (quando exigido) |
| Scanners            | SAST + secrets                     | + IaC + dependências                        | + containers + SBOM + cobertura alargada |
| Segredos            | Masking + armazenamento seguro     | OIDC preferido + TTL controlado             | OIDC obrigatório + TTL curto + rotação frequente |
| Runners             | Partilhados com hardening          | Segregados por projeto                       | Efémeros + segmentação de rede + destruição automática |
| Artefactos          | Assinatura recomendada             | Assinatura + verificação obrigatória        | Bloqueio automático em falha + proveniência reforçada |
| Exceções            | Registo simples                    | Aprovação dupla + TTL                         | Aprovação dupla + revisão frequente + auditoria |
| Rastreabilidade     | Logs 30 dias                       | Logs 90 dias + correlação commit-build        | ≥1 ano + export imutável + dashboards |
| DAST                | Manual periódico                   | Em staging pré-release                       | Contínuo + bloqueio automático |
| Métricas            | Relatórios manuais                 | Dashboard diário                              | Quase tempo real + alertas |

---

## 🏁 Recomendações finais

A segurança de pipelines não é opcional: é o **mecanismo de confiança** de toda a entrega contínua.

- **Versiona e revê o pipeline como código** — e exige determinismo suficiente para auditoria.  
- **Define gates binários e governáveis** — e nunca confundas sinais automáticos com decisões.  
- **Exige evidência empírica** — logs, *exit codes* e artefactos, não apenas relatórios.  
- **Protege segredos e minimiza contexto** — o pipeline é um ponto privilegiado de exfiltração.  
- **Atribui ownership às ações irreversíveis** — promoções sem owner são um risco estrutural.  
- **Controla exceções com TTL e compensações** — bypass só existe quando é governado.

Um CI/CD seguro é o garante silencioso de que tudo o que chega a produção é **íntegro, verificável, rastreável e assumido por responsáveis reais**.
