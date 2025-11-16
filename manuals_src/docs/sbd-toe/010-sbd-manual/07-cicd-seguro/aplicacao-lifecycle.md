---
id: aplicacao-lifecycle
title: Como Fazer
description: Como aplicar as práticas de CI/CD seguro ao longo do ciclo de vida da aplicação, com proporcionalidade por risco, user stories normalizadas e evidências auditáveis
tags: [tipo:aplicacao, ciclo-vida, cicd, devsecops, pipelines, seguranca, rastreabilidade]
genia: us-format-normalization
---

# 📅 Aplicação no Ciclo de Vida - CI/CD Seguro

Enquanto o `intro.md` explica **porque os pipelines são críticos** e que práticas devem ser aplicadas, este documento mostra **como transformar essas prescrições em ações concretas** dentro do ciclo de vida de desenvolvimento e entrega.  
A lógica é simples mas poderosa: cada controlo deve ter um momento certo, um responsável definido, uma user story clara e uma evidência verificável.  
Só assim a segurança em CI/CD deixa de ser teórica e passa a ser **prática operacional auditável**.

---

## 🧭 Quando aplicar

A segurança em pipelines não acontece apenas quando algo corre mal - ela é parte do seu ADN desde o primeiro commit.  
Cada vez que se cria, altera ou promove um pipeline, existem triggers que exigem controlos específicos:

| Momento *trigger*                                 | Objetivo de segurança                                | Papéis principais        |
|--------------------------------------------------|------------------------------------------------------|--------------------------|
| Criação ou refactor do pipeline                   | Introduzir controlos base (proteção, scanners)       | Developers, DevOps / SRE         |
| Alteração de tooling/infra (runners, secrets)     | Rever isolamento, injeção de segredos e permissões   | DevOps / SRE, AppSec Engineers           |
| Introdução/atualização de scanners                | Aumentar cobertura e gates proporcionais ao risco    | Developers, AppSec Engineers         |
| Preparação de release / promoção a produção       | Validar assinatura e proveniência dos artefactos     | DevOps / SRE, AppSec Engineers           |
| Registo de exceção (*bypass* de gate)               | Aprovação formal, prazos e compensações              | GRC / Compliance, Auditores Internos, AppSec Engineers    |
| Auditoria ou revisão periódica                    | Demonstrar rastreabilidade ponta-a-ponta             | GRC / Compliance, Auditores Internos, DevOps / SRE    |

---

## 👥 Quem executa cada ação

A responsabilidade em CI/CD é **partilhada**.  
Um pipeline seguro resulta da soma de esforços: do programador que submete código com scanners ativos, ao DevOps que endurece runners, até ao GRC que valida exceções.

| Ação operacional                                                      | Responsável  | Apoio                | Evidência/Artefactos                          |
|-----------------------------------------------------------------------|--------------|----------------------|-----------------------------------------------|
| Definir/alterar pipeline versionado via PR                            | Developers     | DevOps / SRE               | `ci-pipeline.yml`, histórico de revisão       |
| Endurecer runners (ephemerais, não-privilegiados, segregados)         | DevOps / SRE       | AppSec Engineers               | Configuração de runners, imagens base         |
| Integrar scanners (SAST, secrets, IaC, containers, SBOM)              | Developers     | AppSec Engineers, DevOps / SRE       | Relatórios de scanners, configs no pipeline   |
| Injeção segura de segredos (OIDC, TTL curto, masked logs)             | DevOps / SRE       | AppSec Engineers               | Políticas de segredos, logs de acesso         |
| Assinar artefactos e gerar proveniência                               | DevOps / SRE       | AppSec Engineers               | Assinaturas, ficheiros de proveniência        |
| Definir políticas/gates por risco (L1–L3)                             | AppSec Engineers       | DevOps / SRE, GRC / Compliance          | Regras de gates, thresholds                   |
| Registar e aprovar exceções                                           | GRC / Compliance, Auditores Internos| AppSec Engineers               | Registo formal de exceções e aprovações       |
| Garantir rastreabilidade ponta-a-ponta                                | DevOps / SRE       | GRC / Compliance, Auditores Internos        | Logs correlacionados commit→pipeline→release  |

---

## 🧾 User Stories normalizadas

Cada prática é expressa como **user story reutilizável**, com critérios verificáveis, artefactos concretos e proporcionalidade por nível de risco.

---

### US-01 - Gestão segura de código fonte

**Contexto.**  
Sem controlo sobre o repositório, qualquer pipeline é vulnerável.

:::userstory
**História.**   
Como **Developers**, quero que todas as alterações ao repositório sejam protegidas por PR e revisão obrigatória, para garantir integridade.

**Critérios de aceitação (BDD).**
- Dado que existe um repositório protegido  
- Quando submeto um PR para `main`  
- Então só é aceite após revisão obrigatória e todos os *checks* concluídos com sucesso.  
- Dado que ocorre um *merge*  
- Quando são detetados conflitos  
- Então é exigida nova revisão e execução automática dos scanners de segurança.  

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

### US-02 - Design seguro dos pipelines

**Contexto.**  
Pipelines inseguros são alvos privilegiados de ataque.

:::userstory
**História.**   
Como **DevOps / SRE**, quero pipelines versionados e aprovados por PR, para evitar alterações não auditadas.

**Critérios de aceitação (BDD).**
- Dado que altero pipeline  
- Quando submeto PR  
- Então só é aceite após revisão por DevOps e AppSec.  
- Dado que há alteração de ferramentas  
- Quando o pipeline é modificado  
- Então é criada nova versão rastreável.  

**Checklist.**
- [ ] `ci-pipeline.yml` versionado  
- [ ] PR obrigatório  
- [ ] Triggers explícitos  
- [ ] Histórico de versões mantido
:::

**🧾 Artefactos & evidências.**  
Histórico de commits; ficheiro `ci-pipeline.yml`; aprovação PR; logs de revisão.  

**⚖️ Proporcionalidade.**  
| Nível | Obrigatório? | Ajustes |
|---|---|---|
| L1 | Sim | Versão única do pipeline com aprovação manual |
| L2 | Sim | Versionamento e revisão obrigatória |
| L3 | Sim | Controlo de alterações assinado e validação SLSA |

---

### US-03 - Scanners integrados

**Contexto.**  
Detetar cedo é mais barato e eficaz.

:::userstory
**História.**   
Como **Developers**, quero que o pipeline execute scanners de segurança, para impedir falhas graves em produção.

**Critérios de aceitação (BDD).**
- Dado que submeto código  
- Quando corre pipeline  
- Então falhas críticas bloqueiam merge.  
- Dado que é introduzido novo tipo de artefacto  
- Quando o scanner não o cobre  
- Então o AppSec define regra de deteção adicional.  

**Checklist.**
- [ ] SAST ativo  
- [ ] Secrets scanning ativo  
- [ ] IaC scanning (quando aplicável)  
- [ ] Falhas High bloqueiam merge
:::

**🧾 Artefactos & evidências.**  
Relatórios de scanners; logs CI/CD; registos de bloqueio de merges; dashboards de vulnerabilidades.  

**⚖️ Proporcionalidade.**  
| Nível | Obrigatório? | Ajustes |
|---|---|---|
| L1 | Sim | Scanners básicos (SAST, secrets) |
| L2 | Sim | Inclusão de IaC e análise de dependências |
| L3 | Sim | Scanners completos com *coverage* de containers e SBOM |

---

### US-04 - Gestão de segredos

**Contexto.**  
Segredos estáticos expõem a organização.

:::userstory
**História.**   
Como **DevOps / SRE**, quero segredos injetados por OIDC com TTL curto, para reduzir risco de abuso.

**Critérios de aceitação (BDD).**
- Dado que pipeline arranca  
- Quando credenciais são necessárias  
- Então são emitidas JIT e mascaradas em logs.  
- Dado que o token expira  
- Quando é necessário novo acesso  
- Então é gerado token temporário novo sem reutilização.  

**Checklist.**
- [ ] OIDC configurado  
- [ ] TTL curto  
- [ ] Variáveis mascaradas  
:::

**🧾 Artefactos & evidências.**  
Políticas de segredos; logs de acesso; configuração OIDC; histórico de tokens emitidos.  

**⚖️ Proporcionalidade.**  
| Nível | Obrigatório? | Ajustes |
|---|---|---|
| L1 | Opcional | Segredos armazenados encriptados |
| L2 | Sim | OIDC implementado com TTL controlado |
| L3 | Sim | Tokens efémeros automáticos e rotação diária |

---

### US-05 - Isolamento de runners

**Contexto.**  
Runners inseguros comprometem todo o ecossistema.

:::userstory
**História.**   
Como **DevOps / SRE**, quero runners ephemerais e segregados, para reduzir persistência pós-compromisso.

**Critérios de aceitação (BDD).**
- Dado que job termina  
- Quando runner encerra  
- Então é destruído sem manter estado.  
- Dado que são criados novos runners  
- Quando há pipelines paralelos  
- Então são isolados por namespace e permissões.  

**Checklist.**
- [ ] Runners efémeros  
- [ ] Sem privilégios excessivos  
- [ ] Segmentação de rede  
:::

**🧾 Artefactos & evidências.**  
Configuração de runners; logs de execução; registos de isolamento; scripts de provisionamento.  

**⚖️ Proporcionalidade.**  
| Nível | Obrigatório? | Ajustes |
|---|---|---|
| L1 | Opcional | Runners partilhados com limites |
| L2 | Sim | Segregação de runners por projeto |
| L3 | Sim | Runners efémeros, rede isolada e destruição automática |

---

### US-06 - Assinatura e proveniência

**Contexto.**  
Artefactos não assinados perdem legitimidade.

:::userstory
**História.**   
Como **DevOps / SRE**, quero que todos os artefactos sejam assinados e tenham proveniência validada, para garantir confiança.

**Critérios de aceitação (BDD).**
- Dado que artefacto é produzido  
- Quando é promovido  
- Então assinatura e proveniência são verificadas.  
- Dado que falha verificação  
- Quando assinatura não é válida  
- Então o artefacto é rejeitado e alerta emitido.  

**Checklist.**
- [ ] Assinatura automática  
- [ ] Proveniência SLSA  
- [ ] Verificação antes de release  
:::

**🧾 Artefactos & evidências.**  
Assinaturas digitais; ficheiros de proveniência; logs de promoção; auditoria de build.  

> **Referência:** Este US complementa [Cap 05-US-02: SBOM em cada build]
> ao integrar assinatura e proveniência no pipeline de CI/CD. SBOM e assinatura devem ser geradas conjuntamente como artefactos da build.

**⚖️ Proporcionalidade.**  
| Nível | Obrigatório? | Ajustes |
|---|---|---|
| L1 | Sim | Assinatura manual recomendada |
| L2 | Sim | Assinatura automática e validação SLSA L2 |
| L3 | Sim | Validação obrigatória SLSA L3 e bloqueio automático |

> **Padrão Comum:** Assinatura e verificação de proveniência ocorrem em **múltiplos contextos** (CI/CD, IaC, imagens, deploy).
> Este US foca o contexto de **pipeline de CI/CD**; ver também **Cap 08-US-09** (módulos IaC),
> **Cap 09-US-03** (imagens), **Cap 11-US-01** (deploy). Todos aplicam o **mesmo princípio** (sign → validate → use).

---

### US-07 - Gates por risco

**Contexto.**  
Nem todas as apps exigem o mesmo rigor.

:::userstory
**História.**   
Como **AppSec Engineers**, quero gates distintos por L1–L3, para aplicar segurança proporcional.

**Critérios de aceitação (BDD).**
- Dado que aplicação é L3  
- Quando há falha High  
- Então gate bloqueia promoção.  
- Dado que aplicação é L1  
- Quando há falha Medium  
- Então alerta é registado sem bloqueio.  

**Checklist.**
- [ ] Política publicada  
- [ ] Gates configurados  
- [ ] Thresholds definidos  
:::

**🧾 Artefactos & evidências.**  
Políticas de gates; relatórios CI/CD; logs de bloqueio de promoção.  

**⚖️ Proporcionalidade.**  
| Nível | Obrigatório? | Ajustes |
|---|---|---|
| L1 | Sim | Apenas bloqueio de falhas críticas |
| L2 | Sim | Bloqueio de High e Critical, aprovação AppSec |
| L3 | Sim | Bloqueio automático, revisão GRC |

---

### US-08 - Cobertura ampliada

**Contexto.**  
Cobertura limitada cria pontos cegos.

:::userstory
**História.**   
Como **AppSec Engineers**, quero scanners de containers e SBOM em pipelines, para cobrir supply chain.

**Critérios de aceitação (BDD).**
- Dado que imagem é construída  
- Quando corre pipeline  
- Então SBOM é gerado e anexado.  
- Dado que imagem base muda  
- Quando vulnerabilidade é detetada  
- Então é aberta tarefa de mitigação automática.  

**Checklist.**
- [ ] Container scanning ativo  
- [ ] SBOM gerado  
- [ ] Base images validadas  
:::

**🧾 Artefactos & evidências.**  
Relatórios de scanning; SBOM; auditoria de imagens; logs de builds.  

**⚖️ Proporcionalidade.**  
| Nível | Obrigatório? | Ajustes |
|---|---|---|
| L1 | Opcional | Scans de imagens base trimestrais |
| L2 | Sim | SBOM obrigatório e validação de base images |
| L3 | Sim | Scans contínuos e correlação automática de CVEs |

---

### US-09 - Rastreabilidade ponta-a-ponta

**Contexto.**  
Sem rastreio, auditoria é impossível.

:::userstory
**História.**   
Como **GRC / Compliance**, quero rastrear commit→pipeline→release, para suportar auditorias.

**Critérios de aceitação (BDD).**
- Dado que ocorre incidente  
- Quando analiso release  
- Então consigo traçar origem.  
- Dado que auditor pede evidências  
- Quando executo consulta  
- Então sistema exporta logs correlacionados.  

**Checklist.**
- [ ] IDs de correlação  
- [ ] Logs retidos  
- [ ] Export imutável  
:::

**🧾 Artefactos & evidências.**  
Logs de pipelines; dashboards de rastreabilidade; registos de auditoria.  

**⚖️ Proporcionalidade.**  
| Nível | Obrigatório? | Ajustes |
|---|---|---|
| L1 | Sim | Logs básicos armazenados 30 dias |
| L2 | Sim | Retenção 90 dias + correlação commit-build |
| L3 | Sim | Retenção 1 ano + exportação imutável |

---

### US-10 - Gestão de exceções

**Contexto.**  
Exceções mal geridas tornam-se risco estrutural.

:::userstory
**História.**   
Como **GRC / Compliance**, quero exceções registadas, aprovadas e temporárias, para não acumular dívida técnica.

**Critérios de aceitação (BDD).**
- **Dado** que exceção é pedida  
  **Quando** é analisada  
  **Então** só é aprovada com prazo e compensações.  
- **Dado** que o prazo expira  
  **Quando** exceção não é renovada  
  **Então** é removida e pipeline volta ao modo de controlo normal.  

**Checklist.**
- [ ] Owner registado  
- [ ] Prazo definido  
- [ ] Aprovação dupla (AppSec + GRC)  
- [ ] Registo de compensações  
:::

**🧾 Artefactos & evidências.**  
Registo de exceções; logs de aprovação; relatórios de revisão periódica; prazos automáticos no sistema de GRC.  

> **Referência:** Este US implementa [Cap 14-US-01: Processo formal de exceções]
> no contexto de pipeline CI/CD. Aprovação dupla, TTL e revalidação automática devem seguir a política master de exceções em Cap 14.

**⚖️ Proporcionalidade.**  
| Nível | Obrigatório? | Ajustes |
|---|---|---|
| L1 | Sim | Registo simples com aprovação única |
| L2 | Sim | Aprovação dupla e prazo máximo 60 dias |
| L3 | Sim | Revisão automática a cada sprint e auditoria obrigatória |

---

### US-11 - Testes de segurança dinâmicos (DAST)

**Contexto.**  
Testes estáticos apenas cobrem parcialmente; DAST em staging valida comportamento real.

:::userstory
**História.**   
Como **AppSec Engineers**, quero executar DAST em ambiente de staging após deployment, para validar vulnerabilidades comportamentais e corrigir antes de produção.

**Critérios de aceitação (BDD).**
- **Dado** que nova build é promovida a staging  
  **Quando** inicia pipeline DAST  
  **Então** são executadas análises de autenticação, autorização, injection e XSS.  
- **Dado** que DAST encontra falha High  
  **Quando** resultado é disponibilizado  
  **Então** bloqueia promoção a produção até correção validada.  

**Checklist.**
- [ ] DAST integrado no pipeline  
- [ ] Credenciais de teste segregadas  
- [ ] Relatório correlacionado com commit  
- [ ] Bloqueio automático em High/Critical  
:::

**🧾 Artefactos & evidências.**  
Relatórios DAST; logs de execução; evidências de correção; matriz de rastreabilidade.  

**⚖️ Proporcionalidade.**  
| Nível | Obrigatório? | Ajustes |
|---|---|---|
| L1 | Opcional | DAST manual trimestral |
| L2 | Sim | DAST em staging pré-release |
| L3 | Sim | DAST contínuo com bloqueio automático e retry pós-correção |

---

### US-12 - Métricas e conformidade organizacional

**Contexto.**  
Sem visibilidade centralizada, risco acumula-se invisível.

:::userstory
**História.**   
Como **Gestão Executiva / CISO**, quero visualizar dashboard de métricas de CI/CD (cobertura de scanners, exceções ativas, gate blocks, tempo de remediação), para decisão informada e ação corretiva.

**Critérios de aceitação (BDD).**
- **Dado** que pipeline executa  
  **Quando** eventos ocorrem (merge, gate block, exceção)  
  **Então** são automaticamente registados em base central com timestamp e atores.  
- **Dado** que dashboard é consultado  
  **Quando** métricas são renderizadas  
  **Então** permitem slicing por project, team, período, severidade.  

**Checklist.**
- [ ] Eventos centralizados por telemetria  
- [ ] Dashboard com KPIs (cobertura, MTTR, compliance rate)  
- [ ] Alertas automáticos em anomalias  
- [ ] Relatórios mensais para GRC  
:::

**🧾 Artefactos & evidências.**  
Dashboard de métricas; logs centralizados; relatórios de conformidade; alertas gerados.  

**⚖️ Proporcionalidade.**  
| Nível | Obrigatório? | Ajustes |
|---|---|---|
| L1 | Opcional | Relatórios manuais trimestrais |
| L2 | Sim | Dashboard com KPIs principais, atualizado diariamente |
| L3 | Sim | Dashboard em tempo real com alertas automáticos e previsões de risco |

---

### US-13 - Validação de integridade de imagens base

**Contexto.**  
Imagens base comprometidas propagam risco a todo o ecossistema.

:::userstory
**História.**   
Como **DevOps / SRE**, quero validar que imagens base não foram alteradas (hash, assinatura, drift) e correlacionar com CVEs, para evitar supply chain comprometido.

**Critérios de aceitação (BDD).**
- **Dado** que imagem base é utilizada  
  **Quando** pipeline inicia  
  **Então** hash é validado contra registry confiável.  
- **Dado** que CVE novo é publicado  
  **Quando** afeta imagem em uso  
  **Então** alerta é criado e equipa é notificada para ação.  

**Checklist.**
- [ ] Hash de imagens base armazenado  
- [ ] Validação automática no pull  
- [ ] Rejeição se mismatch detectado  
- [ ] Correlação contínua com CVE feeds  
:::

**🧾 Artefactos & evidências.**  
Hashes de imagens; logs de validação; relatórios de drift; correção de imagens.  

**⚖️ Proporcionalidade.**  
| Nível | Obrigatório? | Ajustes |
|---|---|---|
| L1 | Opcional | Validação manual mensal |
| L2 | Sim | Validação automática no pull com log |
| L3 | Sim | Validação + assinatura de imagens + alertas automáticos em drift ou CVE |

---

## 📦 Artefactos esperados

Cada prática deixa pegadas técnicas. Sem elas, não há prova de conformidade:

| Artefacto / Evidência                | Dono             | Observações                        |
|-------------------------------------|------------------|------------------------------------|
| `ci-pipeline.yml`                   | Developers    | Versionado via PR (US-01, US-02)                  |
| Assinaturas + Proveniência (SLSA)   | DevOps / SRE         | Validadas como gate (US-06)               |
| Relatórios de scanners              | Developers / AppSec Engineers | Thresholds definidos (US-03)              |
| SBOM por build                      | AppSec Engineers         | Anexado ao artefacto (US-08)               |
| Registo de exceções                 | GRC / Compliance / Auditores Internos | Inclui prazo e compensações (US-10)       |
| Logs de execuções/releases          | DevOps / SRE         | IDs de correlação armazenados (US-09)      |
| Relatórios DAST                     | AppSec Engineers         | Correlacionados com commits (US-11)       |
| Dashboard de métricas CI/CD          | Gestão Executiva / CISO         | KPIs de conformidade (US-12)                |
| Hashes e validação de imagens base  | DevOps / SRE         | Correlação com CVEs e drift (US-13)      |

---

## ⚖️ Matriz de proporcionalidade L1–L3

Nem todas as apps exigem o mesmo nível de rigor.  
A matriz assegura que **o esforço é proporcional ao risco**:

| Categoria       | L1 (baixo)                 | L2 (médio)                          | L3 (crítico)                            |
|-----------------|----------------------------|-------------------------------------|-----------------------------------------|
| Branches/PR     | 1 reviewer + build check   | Reviewer + segurança                | ≥2 reviewers + code owners              |
| Scanners        | SAST + secrets             | + IaC                               | + Containers + SBOM                     |
| Segredos        | Variáveis mascaradas       | OIDC preferido                      | OIDC obrigatório + TTL curto            |
| Runners         | Partilhados com guardrails | Segregados                          | Efémeros + segmentação de rede          |
| Artefactos      | Assinatura recomendada     | Assinatura + proveniência obrigatória | Rejeição automática se inválido       |
| Gates por risco | Aviso                      | Bloqueio High/Critical              | Bloqueio Medium+                        |
| Exceções        | Registo simples            | Aprovação AppSec                    | Dupla aprovação + prazo curto           |
| Rastreabilidade | Logs básicos               | IDs correlacionados                 | Export imutável + dashboards            |
| DAST            | Manual trimestral          | Em staging pré-release              | Contínuo com bloqueio automático        |
| Métricas        | Relatórios manuais         | Dashboard diário com KPIs           | Dashboard tempo real + alertas          |
| Imagens base    | Validação manual mensal    | Validação automática no pull        | + Assinatura + alertas em drift/CVE     |

---

## 🏁 Recomendações finais

A segurança de pipelines não é opcional: é **o coração da segurança por design**.  
Um CI/CD seguro multiplica a confiança em todo o ciclo de vida, permitindo releases rápidas e auditáveis.

- **Prefere OIDC a segredos estáticos** — elimina chaves *long-lived*.  
- **Usa runners efémeros e segregados** — reduz persistência de ataque.  
- **Assina artefactos e regista proveniência** — cada *release* deve ser verificável.  
- **Aplica gates proporcionais ao risco** — evita tanto o excesso como a negligência.  
- **Controla exceções** — com prazo, dono e compensações, nunca em aberto.  
- **Investe em rastreabilidade total** — *commit → pipeline → release* como linha de confiança.

Em suma: um pipeline seguro é **o garante silencioso** de que todo o trabalho de desenvolvimento chega a produção de forma íntegra, confiável e auditável.
