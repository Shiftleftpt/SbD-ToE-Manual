---
id: aplicacao-lifecycle
title: Como Fazer
description: Como aplicar as práticas de CI/CD seguro ao longo do ciclo de vida da aplicação, com proporcionalidade por risco, user stories normalizadas e evidências auditáveis
tags: [cicd, devsecops, pipelines, segurança, proveniência, risco, rastreabilidade]
sidebar_position: 15
---

# 📅 Aplicação no Ciclo de Vida - CI/CD Seguro

Enquanto o `intro.md` explica **porque os pipelines são críticos** e que práticas devem ser aplicadas, este documento mostra **como transformar essas prescrições em ações concretas** dentro do ciclo de vida de desenvolvimento e entrega.  
A lógica é simples mas poderosa: cada controlo deve ter um momento certo, um responsável definido, uma user story clara e uma evidência verificável.  
Só assim a segurança em CI/CD deixa de ser teórica e passa a ser **prática operacional auditável**.

---

## 🧭 Quando aplicar

A segurança em pipelines não acontece apenas quando algo corre mal - ela é parte do seu ADN desde o primeiro commit.  
Cada vez que se cria, altera ou promove um pipeline, existem triggers que exigem controlos específicos:

| Momento gatilho                                   | Objetivo de segurança                                | Papéis principais        |
|--------------------------------------------------|------------------------------------------------------|--------------------------|
| Criação ou refactor do pipeline                   | Introduzir controlos base (proteção, scanners)       | 👨‍💻 Developers, ⚙️ DevOps         |
| Alteração de tooling/infra (runners, secrets)     | Rever isolamento, injeção de segredos e permissões   | ⚙️ DevOps, 🔐 AppSec           |
| Introdução/atualização de scanners                | Aumentar cobertura e gates proporcionais ao risco    | 👨‍💻 Developers, 🔐 AppSec         |
| Preparação de release / promoção a produção       | Validar assinatura e proveniência dos artefactos     | ⚙️ DevOps, 🔐 AppSec           |
| Registo de exceção (bypass de gate)               | Aprovação formal, prazos e compensações              | 📑 GRC, 📋 Auditores, 🔐 AppSec    |
| Auditoria ou revisão periódica                    | Demonstrar rastreabilidade ponta-a-ponta             | 📑 GRC, 📋 Auditores, ⚙️ DevOps    |

---

## 👥 Quem executa cada ação

A responsabilidade em CI/CD é **partilhada**.  
Um pipeline seguro resulta da soma de esforços: do programador que submete código com scanners ativos, ao DevOps que endurece runners, até ao GRC que valida exceções.

| Ação operacional                                                      | Responsável  | Apoio                | Evidência/Artefactos                          |
|-----------------------------------------------------------------------|--------------|----------------------|-----------------------------------------------|
| Definir/alterar pipeline versionado via PR                            | 👨‍💻 Developers     | ⚙️ DevOps               | `ci-pipeline.yml`, histórico de revisão       |
| Endurecer runners (ephemerais, não-privilegiados, segregados)         | ⚙️ DevOps       | 🔐 AppSec               | Configuração de runners, imagens base         |
| Integrar scanners (SAST, secrets, IaC, containers, SBOM)              | 👨‍💻 Developers     | 🔐 AppSec, ⚙️ DevOps       | Relatórios de scanners, configs no pipeline   |
| Injeção segura de segredos (OIDC, TTL curto, masked logs)             | ⚙️ DevOps       | 🔐 AppSec               | Políticas de segredos, logs de acesso         |
| Assinar artefactos e gerar proveniência                               | ⚙️ DevOps       | 🔐 AppSec               | Assinaturas, ficheiros de proveniência        |
| Definir políticas/gates por risco (L1–L3)                             | 🔐 AppSec       | ⚙️ DevOps, 📑 GRC          | Regras de gates, thresholds                   |
| Registar e aprovar exceções                                           | 📑 GRC, 📋 Auditores| 🔐 AppSec               | Registo formal de exceções e aprovações       |
| Garantir rastreabilidade ponta-a-ponta                                | ⚙️ DevOps       | 📑 GRC, 📋 Auditores        | Logs correlacionados commit→pipeline→release  |

---

## 🧾 User Stories normalizadas

Cada prática é expressa como **user story reutilizável**, com critérios verificáveis, artefactos concretos e proporcionalidade por nível de risco.

---

### US-01 – Gestão segura de código fonte

**Contexto.**  
Sem controlo sobre o repositório, qualquer pipeline é vulnerável.

:::userstory
**História.**   
Como **👨‍💻 Developer**, quero que todas as alterações ao repositório sejam protegidas por PR e revisão obrigatória, para garantir integridade.

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

### US-02 – Design seguro dos pipelines

**Contexto.**  
Pipelines inseguros são alvos privilegiados de ataque.

:::userstory
**História.**   
Como **⚙️ DevOps**, quero pipelines versionados e aprovados por PR, para evitar alterações não auditadas.

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

### US-03 – Scanners integrados

**Contexto.**  
Detetar cedo é mais barato e eficaz.

:::userstory
**História.**   
Como **👨‍💻 Developer**, quero que o pipeline execute scanners de segurança, para impedir falhas graves em produção.

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

### US-04 – Gestão de segredos

**Contexto.**  
Segredos estáticos expõem a organização.

:::userstory
**História.**   
Como **⚙️ DevOps**, quero segredos injetados por OIDC com TTL curto, para reduzir risco de abuso.

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

### US-05 – Isolamento de runners

**Contexto.**  
Runners inseguros comprometem todo o ecossistema.

:::userstory
**História.**   
Como **⚙️ DevOps**, quero runners ephemerais e segregados, para reduzir persistência pós-compromisso.

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

### US-06 – Assinatura e proveniência

**Contexto.**  
Artefactos não assinados perdem legitimidade.

:::userstory
**História.**   
Como **⚙️ DevOps**, quero que todos os artefactos sejam assinados e tenham proveniência validada, para garantir confiança.

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

**⚖️ Proporcionalidade.**  
| Nível | Obrigatório? | Ajustes |
|---|---|---|
| L1 | Sim | Assinatura manual recomendada |
| L2 | Sim | Assinatura automática e validação SLSA L2 |
| L3 | Sim | Validação obrigatória SLSA L3 e bloqueio automático |

---

### US-07 – Gates por risco

**Contexto.**  
Nem todas as apps exigem o mesmo rigor.

:::userstory
**História.**   
Como **🔐 AppSec**, quero gates distintos por L1–L3, para aplicar segurança proporcional.

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

### US-08 – Cobertura ampliada

**Contexto.**  
Cobertura limitada cria pontos cegos.

:::userstory
**História.**   
Como **🔐 AppSec**, quero scanners de containers e SBOM em pipelines, para cobrir supply chain.

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

### US-09 – Rastreabilidade ponta-a-ponta

**Contexto.**  
Sem rastreio, auditoria é impossível.

:::userstory
**História.**   
Como **📑 GRC**, quero rastrear commit→pipeline→release, para suportar auditorias.

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

### US-10 – Gestão de exceções

**Contexto.**  
Exceções mal geridas tornam-se risco estrutural.

:::userstory
**História.**   
Como **📑 GRC**, quero exceções registadas, aprovadas e temporárias, para não acumular dívida técnica.

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

**⚖️ Proporcionalidade.**  
| Nível | Obrigatório? | Ajustes |
|---|---|---|
| L1 | Sim | Registo simples com aprovação única |
| L2 | Sim | Aprovação dupla e prazo máximo 60 dias |
| L3 | Sim | Revisão automática a cada sprint e auditoria obrigatória |

---

## 📦 Artefactos esperados

Cada prática deixa pegadas técnicas. Sem elas, não há prova de conformidade:

| Artefacto / Evidência                | Dono             | Observações                        |
|-------------------------------------|------------------|------------------------------------|
| `ci-pipeline.yml`                   | 👨‍💻 Developers    | Versionado via PR                  |
| Assinaturas + Proveniência (SLSA)   | ⚙️ DevOps         | Validadas como gate                |
| Relatórios de scanners              | 👨‍💻 Dev / 🔐 AppSec | Thresholds definidos               |
| SBOM por build                      | 🔐 AppSec         | Anexado ao artefacto               |
| Registo de exceções                 | 📑 GRC / 📋 Auditoria | Inclui prazo e compensações        |
| Logs de execuções/releases          | ⚙️ DevOps         | IDs de correlação armazenados      |

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
