---
id: 04-validacoes-pre-deploy
title: Validações Técnicas e Funcionais Pré-Deploy
description: Verificações obrigatórias antes da promoção de código para produção, incluindo segurança, funcionalidade e readiness.
tags: [grupo:execucao, pre-deploy, seguranca, tema:validacao, tipo:anexo]
---

# 🔧 Validações de Segurança antes de Deploy

Este documento define as **validações técnicas e de segurança obrigatórias antes da aprovação de um deploy**, com base no risco da aplicação, criticidade da release e contexto de execução.

Aplica-se a ambientes de **QA, staging e produção**, devendo ser incorporado como *gate* no pipeline ou validado manualmente em organizações com menor automação.

---

## 📊 Tabela de validações por tipo

| Tipo de Validação       | Descrição                                                        | Exemplo / Ferramenta             |
|-------------------------|------------------------------------------------------------------|----------------------------------|
| **Testes funcionais**   | Validação da funcionalidade principal                           | Testes de regressão / QA         |
| **Testes de segurança** | Verificação de vulnerabilidades, credenciais, misconfiguração     | SAST, DAST, trivy, Semgrep       |
| **SBOM / dependências** | Geração e validação da lista de componentes (SBOM)             | CycloneDX, Syft, OWASP Dependency Check |
| **Análise de findings** | Lista de findings abertos, com classificação e decisão justificada  | Jira, Kiuwan, backlog AppSec     |
| **Regras de controlo**  | Cumprimento de critérios específicos por risco                    | Checklists, gates condicionais   |
| **Aprovação formal**     | Aprovação por perfil segregado (AppSec, QA, gestão)             | Azure DevOps, GitHub reviewers   |

---

## 🚫 Exemplos de bloqueios (gates) recomendados

| Nível de Risco | Gate de bloqueio se...                                       |
|----------------|--------------------------------------------------------------|
| **L1 (baixo)** | Findings críticos abertos OU testes falham                    |
| **L2 (médio)** | Findings ≥ high abertos OU sem SBOM OU sem rollback definido |
| **L3 (elevado)**| Sem revisão AppSec OU sem testes dinâmicos OU sem plano de rollback validado |

> 🔎 Estes gates devem estar parametrizados no pipeline ou incluídos na checklist de validação manual.

---

## 🔗 Integração recomendada no pipeline CI/CD

1. **Etapa de build**:
   - Gera SBOM automaticamente
   - Corre SAST + linting semântico

2. **Etapa de validação**:
   - Analisa findings abertos
   - Verifica que plano de rollback está presente

3. **Etapa de gating / aprovação**:
   - Bloqueia se nível de risco ≥ L2 e não houver revisão
   - Permite aprovação manual por reviewer de segurança

---

## 🏢 Integração com controlo organizacional

- Releases devem ser ligadas a um artefacto de validação:
  - Relatório de findings por risco
  - Assinatura da release (hash, metadados, data)
  - Aprovadores e justificativos

- Deve existir registo de:
  - Quem aprovou o deploy
  - Em que condições (versão, ambiente, âmbito)
  - Ligação a testes ou rastreabilidade de requisitos

---

## ✅ Exemplos de critérios de aprovação

- [ ] Todos os testes automatizados passaram
- [ ] Foram revistos findings em aberto e justificados
- [ ] Existe rollback funcional validado
- [ ] SBOM gerado e armazenado para auditoria
- [ ] A release foi aprovada por reviewer qualificado
- [ ] Foram criados cartões/tarefas para findings pendentes (se aplicável)

> 👍 Estes critérios devem ser **binários, verificáveis e rastreáveis**.
