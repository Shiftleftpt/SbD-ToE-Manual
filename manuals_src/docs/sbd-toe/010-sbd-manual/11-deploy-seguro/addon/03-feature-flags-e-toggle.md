---
id: 03-feature-flags-e-toggle
title: Controlo de Funcionalidades com Feature Flags
description: Uso de feature toggles com segurança, rastreabilidade e capacidade de reversão em produção.
tags: [deploy, grupo:execucao, rastreabilidade, tema:feature-flags, tipo:anexo, toggles]
---


# 🌺 Utilização Segura de Feature Flags e Toggles

## 🌟 Objetivo

Estabelecer boas práticas para a utilização segura de **feature flags** (ou toggles), com foco em:

- Minimizar risco de falhas em produção;
- Permitir entregas progressivas e reversíveis;
- Reforçar a rastreabilidade, governança e validação formal;
- Prevenir abusos ou comportamentos não controlados no runtime.

---

## 🧬 O que são Feature Flags

Feature flags são mecanismos que permitem ativar ou desativar funcionalidades **sem novo deploy**, com base em regras de configuração. São amplamente usados para:

- Progressive delivery;
- Canary releases;
- Testes A/B;
- Contenção de falhas;
- Gestão operacional de funcionalidades críticas.

### Tipos comuns de toggles

| Tipo                    | Descrição                                                    | Exemplo prático                                  |
|-------------------------|--------------------------------------------------------------|--------------------------------------------------|
| **Release Toggle**      | Controla funcionalidades em desenvolvimento                  | Nova API visível só para a equipa interna        |
| **Ops Toggle**          | Liga/desliga fluxos técnicos ou integrações sensíveis        | Desativar envio de emails temporariamente        |
| **Permission Toggle**   | Define quem pode aceder a uma funcionalidade                 | Só admins acedem a dashboards internos           |
| **Experiment Toggle**   | Suporta experiências e otimizações por grupo de utilizadores | Mostrar novo layout a 50% dos utilizadores       |
| **Kill Switch**         | Desativa funcionalidades de forma imediata                   | Interromper notificações após incidente          |

---

## 🛠️ Como aplicar

### 🔐 Segurança e isolamento

- Nunca usar toggles como substituto de controlo de acesso;
- Avaliar toggles no **backend** - não apenas no frontend;
- Evitar **toggles client-side** para lógica sensível;
- Garantir que todos os caminhos lógicos associados são testáveis.

### 🛡️ Rastreabilidade e metadata

Cada toggle deve ter:

- Nome único e descritivo;
- Owner (equipa ou pessoa responsável);
- âmbito (ambiente, grupo, tenant, região...);
- Condição de ativação e de expiração;
- Justificação funcional e de segurança.

### 📜 Gestão como código

- Gerir toggles como infraestrutura (ex: Feature Flags as Code);
- Versionar configuração (YAML, JSON, etc.);
- Aplicar via PRs, com revisão e aprovação formal.

---

## 🧪 Exemplo de metadata de toggle

```yaml
toggle: enable_enhanced_logging
description: Ativa logging estendido para debugging
owner: equipa-devsecops
enabled_by_default: false
scope: ["staging", "grupo-beta"]
expires_after: 2025-12-01
justification: Necessário para investigação de comportamento anómalo
```

---

## ⚠️ Riscos e más práticas

| Antipadrão                        | Consequência                                      |
|----------------------------------|---------------------------------------------------|
| Toggle sem owner                 | Ninguém sabe quem o controla                      |
| Sem expiração                    | Dívida técnica acumulada                          |
| Avaliação apenas no frontend     | Bypass possível via manipulação da UI             |
| Toggle silencioso (sem logs)     | Dificuldade de debugging e auditoria              |
| Sem fallback definido            | Comportamento imprevisível se desligado           |

---

## ✅ Boas práticas

- Definir **SLA de revisão periódica** (ex: todos os toggles revistos mensalmente);
- Alertar para toggles ativos há mais de 60 dias;
- Bloquear merges de código com toggles sem metadata;
- Validar caminhos alternativos (com e sem toggle ativo);
- Incluir toggles no processo de aprovação da release.

---

## 🧰 Ferramentas de suporte

| Ferramenta         | Tipo                  | Notas                                     |
|--------------------|-----------------------|-------------------------------------------|
| **LaunchDarkly**   | SaaS                  | Dashboards, SDKs multi-linguagem          |
| **Unleash**        | Open Source / SaaS    | Self-hosted, estratégia de rollout        |
| **Flagsmith**      | SaaS / Open Source    | Integração com GitOps e RBAC              |
| **FeatureHub**     | Open Source           | Foco em múltiplas equipas, multi-tenancy  |

---

## 📎 Referências cruzadas

| Documento / Capítulo              | Relação com este tema                             |
|-----------------------------------|---------------------------------------------------|
| Cap. 01 - Gestão de Risco         | Avaliação de risco associada a toggles            |
| Cap. 06 - Desenvolvimento Seguro  | Testabilidade de caminhos condicionais            |
| Cap. 10 - Testes de Segurança     | Testes A/B, falhas induzidas e fallback           |
| Cap. 11 - Deploy Seguro           | Toggles como mecanismo de controle de execução    |
| Cap. 12 - Monitorização           | Observação ativa de comportamentos com toggles    |

---

> 🌟 Toggles são poderosos - mas só quando usados com disciplina, controlo e rastreabilidade.  
> Devem ser tratados como **ativos críticos de runtime**, com implicações diretas na segurança e no risco operacional.
