---
id: 06-controle-versao-e-rollback
title: Controlo de Versão e Estratégias de Rollback
description: Técnicas para garantir versões rastreáveis e reversíveis com rollback automático, testado e documentado.
tags: [tipo:anexo, grupo:execucao, tema:rollback, versionamento, reversibilidade]
---


# 🔄 Controlo de Versão e Rollback Seguro {deploy-seguro:addon:06-controle-versao-e-rollback}

Garantir reversibilidade e rastreabilidade é essencial para reduzir o impacto de falhas em produção. Este documento define as práticas recomendadas para controlo de versão, rollback confiável e preparação de releases seguras.

---

## 📂 Versionamento como pilar de segurança {deploy-seguro:addon:06-controle-versao-e-rollback#versionamento_como_pilar_de_seguranca}

- Utilizar **versionamento semântico** (`vX.Y.Z`) com significado claro:
  - `X` = quebra de compatibilidade
  - `Y` = novas funcionalidades
  - `Z` = correções / hotfixes
- Associar cada release a:
  - Hash de commit ou tag Git
  - Data e hora de deploy
  - Ambiente e escopo
  - Owner da release

> 🔗 Deve existir relação 1:1 entre versão, binário e documentação de validação

---

## 🔄 Rollback: não é exceção, é plano {deploy-seguro:addon:06-controle-versao-e-rollback#rollback_nao_e_excecao_e_plano}

O rollback deve ser planeado como parte de cada release.

| Tipo de rollback        | Descrição                                     | Exemplo                          |
|-------------------------|-----------------------------------------------|----------------------------------|
| **Binário**             | Reverter o artefacto para versão anterior       | Tag Git anterior                 |
| **Configuração**        | Alterar feature flags / variáveis de ambiente   | Toggle off                       |
| **Base de dados**       | Reverter migração ou usar rollback automático | Flyway, Liquibase                |
| **Infraestrutura**      | Restaurar estado anterior de recursos         | Terraform rollback, snapshots    |

### Requisitos: {deploy-seguro:addon:06-controle-versao-e-rollback#requisitos}

- Rollback deve ser **automático ou documentado**
- Testado em staging antes do go-live
- Ligado a eventos de rollback no sistema de logs

---

## 🚫 Antipadrões a evitar {deploy-seguro:addon:06-controle-versao-e-rollback#antipadroes_a_evitar}

- Releases sem tag Git ou hash verificável
- Múltiplos artefactos com o mesmo número de versão
- Rollback não testado / manual
- Migrações sem reversão possível
- Alterar configuração de produção manualmente e sem registo

---

## 🌐 Ferramentas e boas práticas {deploy-seguro:addon:06-controle-versao-e-rollback#ferramentas_e_boas_praticas}

| Objetivo               | Ferramenta / Prática                                     |
|------------------------|-----------------------------------------------------------|
| Versionamento Git      | `git tag`, `git describe`, `git hash-object`              |
| Build idempotente      | Hash incluído no artefacto, via pipeline                 |
| Rollback infra         | Terraform, Helm + `helm rollback`                         |
| Migração reversível    | Scripts SQL reversos, Flyway `undo`, Liquibase `rollback` |
| Auditoria de releases  | Logging, CI/CD dashboards, audit trail                    |

---

## 🔀 Integração com ciclo de vida da aplicação {deploy-seguro:addon:06-controle-versao-e-rollback#integracao_com_ciclo_de_vida_da_aplicacao}

- Definir rollback como etapa formal no planeamento de releases
- Incluir testes de rollback nos ambientes de QA/staging
- Documentar rollback no changelog funcional
- Associar releases a tickets, justificativos e owners técnicos

---

## ✅ Checklist de controlo de versão e rollback {deploy-seguro:addon:06-controle-versao-e-rollback#checklist_de_controlo_de_versao_e_rollback}

- [ ] Existe uma tag Git para a versão publicada?
- [ ] O artefacto está assinado e identificado de forma única?
- [ ] Existe plano de rollback documentado e testado?
- [ ] As migrações podem ser revertidas automaticamente?
- [ ] O rollback foi validado antes do go-live?
- [ ] As alterações de configuração estão versionadas?

> 📊 Estes pontos são essenciais para manter **resiliência e confiança** em ambientes de execução sensíveis.
