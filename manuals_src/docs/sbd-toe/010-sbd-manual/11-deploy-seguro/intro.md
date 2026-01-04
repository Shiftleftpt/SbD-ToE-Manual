---
id: intro
title: Deploy Seguro
description: Princípios e controlos para garantir um processo de deploy seguro, validado e rastreável em ambientes de produção
tags: [deploy, seguranca, producao, rollback, gates, sdlc]
sidebar_position: 0
---

:::tip Capítulo Operacional
Este capítulo é considerado **operacional** no modelo *Security by Design – Theory of Everything (SbD-ToE)*.  
A sua função é **aplicar, automatizar e validar** práticas definidas em capítulos basilares, garantindo a sua execução contínua e mensurável.

Os capítulos operacionais implementam o SbD-ToE em contextos técnicos específicos, traduzindo prescrições basilares em práticas de **execução verificável**, com **evidência auditável** ao longo do ciclo de vida do software.
:::

# Deploy Seguro

## Contexto e objetivo

O momento de *deploy* é, por natureza, um dos mais delicados de todo o ciclo de vida. Até ao último instante, a aplicação pode estar íntegra, testada e auditada; mas se a passagem a produção for feita de forma insegura, o investimento anterior perde valor.

A evidência recolhida em relatórios e análises de incidentes mostra que compromissos relevantes ocorrem frequentemente na fase de *release* e operação inicial, por falhas de rastreabilidade, ausência de *rollback*, permissões excessivas, gestão deficiente de segredos ou promoção de artefactos sem proveniência verificável.

Este capítulo não se limita a “executar o pipeline”. Procura estabelecer práticas que tornem cada *deploy* **auditável, reversível e proporcional ao risco da aplicação**.  
A segurança do *deploy* é também governação: traduz-se na capacidade de explicar, perante auditoria ou incidente, **quem decidiu**, **o que foi aprovado**, **que evidência suportou a decisão** e **como se garantiu a integridade do que chegou a produção**.

👉 Este capítulo complementa:
- **CI/CD Seguro** — onde se garante integridade do *build*, rastreabilidade técnica e controlo do pipeline.  
- **Monitorização e Operações** — onde se cobre a deteção de anomalias, resposta a incidentes e validação em *runtime*.

---

## 🧭 O que cobre tecnicamente

O âmbito técnico do *deploy* seguro inclui, pelo menos, os seguintes eixos:

- Aprovação formal e *gates* automáticos de *release*, com critérios definidos por severidade e criticidade (L1–L3).  
- Promoção apenas a partir de artefactos assinados, com proveniência verificável e SBOM associado.  
- Validação funcional e de segurança em *staging* antes da promoção.  
- Gestão rigorosa de credenciais e segredos usados no momento do *deploy* (mínimo privilégio, curta duração, auditoria).  
- *Rollback* seguro, configurado e testado periodicamente.  
- Rastreabilidade *end-to-end*, permitindo traçar cada incidente até ao *commit* e artefacto original.  
- Monitorização pós-*deploy*, para avaliar saúde e integridade em tempo útil e suportar decisões de contenção.

Estes elementos devem ser aplicados como um **conjunto coerente de controlos**: a robustez do processo resulta da complementaridade entre prevenção (*gates* e proveniência), deteção (monitorização), contenção (*rollback* e *feature flags*) e auditoria (rastreabilidade e evidência).

---

## � Automação e Governação no Deploy

O deploy seguro combina **automação extensiva** com **governação explícita**, diferenciando:

### Decisões Determinísticas (Automação Soberana)

Quando critérios são **objetivos, reprodutíveis e isentos de contexto**, a automação pode operar sem intervenção humana:

- **Gates técnicos**: SAST detecta CVE crítico → bloqueio automático
- **Proveniência**: Assinatura de artefacto inválida → rejeição automática
- **Rollback automático**: Métrica de erro >threshold → reversão imediata
- **Secret scanning**: Credencial detectada → build interrompido

**Princípio**: Automação determinística **pode operar sem aprovação humana** se critérios estão formalmente definidos e versionados.

### Decisões Não-Determinísticas (Governação Obrigatória)

⚠️ **CRÍTICO**: Automação não-determinística **NÃO PODE** operar sem governação humana.

Quando decisões envolvem **contexto, trade-offs ou heurísticas**, exigem validação humana e rastreabilidade:

- **Exceções a findings**: CVE não-aplicável → AppSec aprova + justificativa + validade temporal
- **Aprovação de go/no-go**: Risco residual aceite → Gestão de Produto aprova + evidência
- **Rollback de BD**: Migração reversível mas com perda de dados → SRE + Gestão decidem

**Princípio**: Toda decisão não-determinística exige:
- **Quem** (papel responsável)
- **Quando** (timestamp + validade)
- **Porquê** (justificação técnica)
- **Evidência** (documentação auditável)

**Princípio**: Decisões não-determinísticas **NÃO PODEM** ser automatizadas sem validação, aprovação e rastreabilidade humanas. A automação pode **assistir**, mas nunca **decidir sozinha**.

### Guardrails de Automação

Mesmo decisões automatizadas têm **limites explícitos** para ações irreversíveis:

| Ação | Limite | Razão |
|------|--------|-------|
| Rollback automático | Até N-1 versão apenas | Prevenir cascata de reversões |
| Purga de dados | Sempre manual + aprovação | Irreversível |
| Alteração de permissões | Sempre manual + revisão | Impacto lateral alto |
| Injeção de segredos | Ambientes aprovados apenas | Prevenir vazamento |

**Princípio**: Automação **NÃO PODE** executar ações irreversíveis ou com impacto lateral crítico sem intervenção humana. Mesmo em contextos determinísticos, ações de alto risco exigem aprovação.

---

## 🔐 Gestão de Exceções

Exceções a gates automáticos (ex: CVE não-aplicável, falso positivo SAST) seguem processo formal:

1. **Template de exceção** (versionado em repo):
   ```yaml
   exception_id: EX-2026-001
   finding_id: SAST-SQL-001
   justification: "Query parametrizada, não-vulnerável"
   approved_by: "AppSec Lead (email@example.com)"
   approved_date: "2026-01-04"
   expiration_date: "2026-07-04"  # Máximo 6 meses
   evidence: "link/to/code-review-PR-123"
   ```

2. **Aprovador por severidade**:
   - CRITICAL: AppSec Lead + CTO
   - HIGH: AppSec Lead
   - MEDIUM: Tech Lead

3. **Validade temporal**: Exceções expiram automaticamente (máx 6 meses L2, 3 meses L3)

4. **Reavaliação**: Antes de expiração, nova análise obrigatória

---

## �🧪 Prescrição prática

O que distingue organizações maduras não é apenas *o que* fazem no *deploy*, mas **como operacionalizam o processo como um mecanismo repetível de validação e contenção de risco**, com evidência objetiva.

- **O que fazer**  
  Garantir que todos os *deploys* ocorrem apenas a partir de artefactos confiáveis, passam por *gates* e validações em *staging*, e têm *rollback* operacional pronto.

- **Como fazer**  
  Automatizar pipelines com configuração versionada, aplicar princípio do menor privilégio, ensaiar *rollback* em cadência definida e integrar a telemetria do *deploy* com monitorização e resposta a incidentes.

- **Quando**  
  Em cada *release*, em alterações relevantes de infraestrutura/configuração e sempre que um incidente exija contenção ou reversão.

- **Porquê**  
  Porque o *deploy* é o ponto onde uma falha pode ter impacto imediato na disponibilidade, integridade e exposição. Estas práticas alinham-se com controlos de referência (ex.: NIST SSDF na validação e verificação; SLSA na proveniência), e suportam exigências típicas de frameworks e obrigações de cibersegurança aplicáveis ao software em produção.

---

## 👥 Papéis envolvidos

Nenhum *deploy* seguro é responsabilidade de um só perfil. A prática exige coordenação transversal:

- **Dev** → garante que o artefacto está pronto, versionado e documentado.  
- **QA/Testes** → executa validações funcionais e de segurança em *staging*.  
- **AppSec** → define *gates*, critérios e processo de exceções com rastreabilidade e validade temporal.  
- **DevOps/SRE** → executa pipelines, prepara *rollback* e assegura rastreabilidade técnica e evidência.  
- **Gestão de Produto** → toma a decisão final de *go/no-go* e documenta aceitação de risco residual.

Esta matriz não é opcional: é o que garante que cada *deploy* é simultaneamente **técnico e governado**, capaz de resistir a falhas operacionais e a escrutínio regulatório.

---

## 📜 Políticas Organizacionais Relevantes

| Política | Obrigatória? | Aplicação | Conteúdo mínimo |
|----------|--------------|-----------|-----------------|
| Política de Deploy Seguro | Sim | DevOps/SRE + AppSec | Promoção apenas de artefactos assinados e rastreáveis; validações mínimas; evidência |
| Política de Aprovação de Release | Sim | Gestão de Produto + AppSec | *Gates* formais; critérios por criticidade; exceções registadas e temporais |
| Política de Rollback | Sim | DevOps/SRE | *Rollback* definido por tipo, testado periodicamente, com evidência |
| Política de Validação em Staging | Recomendado | QA/Testes | Validação funcional + segurança antes de promoção; dados controlados |
| Política de Monitorização Pós-Deploy | Sim | DevOps/SRE | Métricas/alertas; correlação com eventos de *deploy*; processo de resposta |

Na versão impressa, consultar o **Anexo de Políticas Organizacionais do manual**, onde estas políticas estão consolidadas transversalmente.
