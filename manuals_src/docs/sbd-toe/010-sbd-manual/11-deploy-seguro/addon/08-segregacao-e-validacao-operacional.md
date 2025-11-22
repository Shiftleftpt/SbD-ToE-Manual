---
id: 08-segregacao-e-validacao-operacional
title: Validação Operacional com Ambientes Segregados
description: Estratégias para validação em ambientes staging e pre-prod que garantem readiness e segurança operacional.
tags: [grupo:execucao, readiness, segregacao, staging, tema:validacao, tipo:anexo]
---


# 🏢 Segregação de Ambientes e Validação Operacional

A separação clara entre ambientes (desenvolvimento, QA, staging, produção) é uma prática essencial para mitigar riscos e evitar que código não validado seja executado em contextos sensíveis. Este documento define práticas de **segregação segura e validação antes da promoção para produção**.

---

## 🌐 Separar é proteger

| Ambiente      | Objectivo principal                           | Restrições sugeridas                        |
|---------------|-----------------------------------------------|-----------------------------------------------|
| **Dev**       | Desenvolvimento ativo                         | Acesso aberto, dados fictícios               |
| **QA/Test**   | Testes funcionais e regressão                | Dados controlados, acesso por QA              |
| **Staging**   | Ambiente idêntico a produção para validação | Mesmas versões e configuração              |
| **Produção** | Execução real e dados sensíveis               | Apenas acesso autorizado e segregado          |

> 💡 Ambientes partilhados aumentam risco de exposição de dados e efeitos colaterais inesperados.

---

## 🛡️ Requisitos de segurança por ambiente

- **Acesso e autenticação**:
  - MFA para staging e produção
  - Perfis RBAC distintos por ambiente

- **Dados utilizados**:
  - Dados reais **apenas em produção**
  - Mascaramento ou dados sintéticos nos restantes

- **Segregação de infraestrutura**:
  - VPC/sub-redes distintas
  - Segredos e cofres separados
  - Pipelines com tokens e permissões segregadas

---

## 🔢 Validação final antes de produção

| Tipo de validação                  | Descrição                                                       |
|------------------------------------|------------------------------------------------------------------|
| **Checklist funcional**            | Todos os requisitos validados?                                   |
| **Checklist de segurança**        | Findings, toggles, rollback, logging                              |
| **Teste de reversibilidade**       | Rollback funcional testado?                                       |
| **Aprovação formal**              | Por quem? QA, AppSec, gestor?                                      |
| **Auditoria de alterações**        | Que código / config foi alterado?                                  |

---

## 🚑 Testes em produção com segurança

Em alguns contextos, pode ser necessário validar em produção:
- Com feature flags e âmbito limitado
- Com logs e alertas reforçados
- Com rollback imediato preparado

> ❌ Nunca realizar testes manuais com utilizadores reais sem rastreabilidade, aprovação e rollback garantido.

---

## 💼 Registo e auditoria obrigatória

- Que versão foi promovida
- Por quem
- Que validadores passaram (segurança, funcionalidade)
- Justificação de exceções se aplicável
- Evidências de rollback testado

---

## ✅ Checklist de validação operacional

- [ ] O ambiente de staging é equivalente a produção?
- [ ] A pipeline de produção está segregada das restantes?
- [ ] Todos os acessos estão controlados por MFA e RBAC?
- [ ] As validações finais foram executadas e documentadas?
- [ ] Existe rollback testado e pronto a usar?
- [ ] As configurações estão auditadas e versionadas?

> 🔒 A segregação de ambientes é um requisito fundamental para a segurança organizacional e conformidade.
