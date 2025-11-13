---
id: sbd-toe-4-dora-playbook
title: "SbD-ToE 4 DORA: Playbook de Implementação"
description: Roadmap prático e faseado para implementar SbD-ToE conforme requisitos DORA (12-18 meses)
tags: [playbook, dora, implementacao, roadmap, fases, 12-18-meses]
sidebar_position: 2
---

# SbD-ToE 4 DORA: Playbook de Implementação

## Enquadramento Executivo

O DORA entra em vigor em **janeiro de 2025**. Organizações financeiras precisam não apenas de "ter segurança", mas de demonstrar **capacidade operacional com evidências e processos mensuráveis**.

O **SbD-ToE + este Playbook** oferecem um caminho prático para construir conformidade **"por construção"**, em vez de "auditar ao fim".

Este playbook é um **guia indicativo de 12–18 meses**. Cada organização deve:
- ✓ Adaptar fases ao seu contexto (recursos, maturidade atual, constraints)
- ✓ Validar timeline com direção executiva
- ✓ Usar exemplos práticos em `exemplos-playbook-dora/` para implementação específica

---

## Roadmap de Implementação (12–18 meses)

```
FASE 0: Preparação (M0–M2)
  └─ Alinhar estrutura, ativar toolchain, formar equipas

FASE 1: Foundation (M2–M4)
  └─ Classificação de apps, políticas, análise de vulnerabilidades

FASE 2: Automatização (M4–M8)
  └─ CI/CD seguro, threat modeling, testes contínuos

FASE 3: Operação (M8–M12)
  └─ Monitorização, deteção de incidentes, supply chain

FASE 4: Maturação (M12–M18)
  └─ Testes de resiliência, métricas avançadas, auditoria

FASE 5: Conformidade (Contínuo)
  └─ Inspeção regulatória, melhoria contínua
```

---

## FASE 0: Preparação (M0–M2)

### 0.1 Alinhar Governação

**Objetivo:** Estruturar comissão de decisão para SbD + DORA

**Atividades:**

1. **Criar Comissão de Segurança Digital**
   - Membros: CISO, CTO, Head of Product, GRC Manager, General Counsel
   - Frequência: Quinzenal (primeiros 3 meses), depois mensal
   - Função: Aprovar políticas, arbitrar trade-offs, auditar conformidade

2. **Definir Política de Segurança Aplicacional**
   - Referência: Cap. 02 SbD-ToE
   - Dimensões: Requisitos L1–L3, ciclo de vida, responsabilidades
   - Aprovação: **Board signature** (evidência DORA Art. 5 "tone at the top")

3. **Mapear RACI**
   - Responsabilidades claras por função
   - Aprovações formais documentadas
   - Escalations definidas

**Exemplos práticos:** Ver `exemplo-playbook/03-exemplo-raci-governance.md`

**Recursos:** 1 CISO, 1 GRC Manager  
**Evidência DORA:** Política assinada, RACI document, board meeting minutes

---

### 0.2 Ativar Toolchain Essencial

**Objetivo:** Infraestrutura técnica de segurança conforme Cap. 08, 12

**Atividades (princípios, não ferramentas específicas):**

1. **Infraestrutura como Código (IaC) - Cap. 08**
   - Versionar toda configuração de infraestrutura
   - Auditoria de mudanças via controle de versão
   - Trilho de quem fez o quê, quando

2. **Logs e Recolha Centralizada - Cap. 12**
   - Centralizar logs de aplicações, APIs, eventos críticos
   - Retenção: Conforme política (DORA: 3 anos mínimo)
   - Proteção contra alteração (immutability)

3. **Análise de Dependências & SBOM - Cap. 05**
   - SCA: Análise de composição de software (Software Composition Analysis)
   - SBOM: Geração de Bill of Materials (dependências, versões, licenças)
   - SAST: Análise estática do código
   - Integração: Nos gates de CI/CD
   - **Objetivo:** Rastreabilidade técnica de componentes (fornecedores implícitos)

4. **Gestão de Acessos - Cap. 14**
   - Controle de acesso baseado em responsabilidades
   - Registro auditado de quem acedeu o quê, quando
   - Revisão periódica de acessos

**Exemplos práticos:** Ver `exemplo-playbook/01-exemplo-toolchain-options.md`

**Recursos:** Security team, Infrastructure/DevOps lead  
**Evidência DORA:** Logs centralizados, política de retenção ativa

---

### 0.3 Formação Inicial

**Objetivo:** Alinhar equipa em SbD + DORA

**Atividades:**

- Security team: 3 dias intensivos SbD-ToE + DORA
- Development leads: 1 dia SbD princípios + classificação
- All-hands: 2h briefing (compliance, responsabilidades)

**Recursos:** 10 dias-pessoa

---

## FASE 1: Foundation (M2–M4)

### 1.1 Classificação de Aplicações

**Objetivo:** Classificar todas as apps por criticidade L1–L3 (Cap. 01)

**Atividades:**

1. **Inventário completo de aplicações**
   - Nome, proprietário, tipo (web, API, batch, etc.)
   - Dados processados (sensíveis? de clientes? transacionais?)
   - Dependências (quem depende desta app?)

2. **Classificação L1–L3**
   - L3 (Crítica): Impacto direto em funções críticas do negócio
   - L2 (Importante): Suporta processos importantes
   - L1 (Padrão): Ferramentas de suporte, reports

3. **Documentação formal**
   - Matriz assinada por CTO + Product leads
   - Publicada para toda a organização

**Exemplos práticos:** Ver `exemplo-playbook/02-exemplo-kpis-targets.md`

**Responsável:** CTO + Product Managers  
**Evidência:** Matriz assinada, trilho de decisões

---

### 1.2 Requisitos de Segurança por Nível

**Objetivo:** Mapear requisitos mínimos para cada nível (Cap. 02)

**Atividades:**

| Nível | Requisitos Mínimos | Exemplos |
|-------|-------------------|----------|
| **L1** | Basics | Senhas, logs, code review |
| **L2** | Essenciais | + Threat modeling, SAST, testes |
| **L3** | Rigorosos | + DAST, TLPT readiness, monitorização 24x7 |

**Documentação:** Template no Cap. 02, detalhe por nível

**Responsável:** Security team + Architecture  
**Evidência:** Requisitos documentados, aprovados

---

## FASE 2: Automatização (M4–M8)

### 2.1 CI/CD Seguro

**Objetivo:** Integrar segurança no pipeline de entrega (Cap. 07)

**Atividades (princípios, não ferramentas específicas):**

1. **Gates de Segurança no Pipeline**
   - Análise de código (SAST/SCA) antes de merge
   - Bloqueio de secrets em repositório
   - Compilação segura
   - Validação pré-deploy

2. **Segregação de Responsabilidades**
   - Code review: Aprovação obrigatória
   - Deploy: Aprovação formal
   - Trilho: Logs de quem fez o quê, quando

3. **Retenção de Logs de CI/CD**
   - Preservar histórico de builds
   - Período mínimo: Conforme política retenção
   - Imutabilidade: Protegido contra alteração

**Exemplos práticos:** Ver `exemplos-playbook-dora/01-exemplo-toolchain-options.md` (secção CI/CD)

**Responsável:** DevOps + Security  
**Evidência:** Pipeline documentado, logs auditados

---

### 2.2 Threat Modeling

**Objetivo:** Identificar ameaças realistas para apps L3 (Cap. 03)

**Atividades:**

1. **Seleção de apps L3**
   - Priorizar: críticas, com dados sensíveis, expostas

2. **Threat modeling por app**
   - Arquitetura mapeada
   - Ameaças identificadas (STRIDE, etc.)
   - Mitigações propostas

3. **Integração com development**
   - Threat model guia requirements
   - Atualizado conforme mudanças

**Responsável:** Architecture + Security  
**Evidência:** Threat models documentados, aprovados

---

## FASE 3: Operação (M8–M12)

### 3.1 Monitorização e Resposta a Incidentes

**Objetivo:** Detetar, registar, responder a incidentes (Cap. 12, DORA Art. 18)

**Atividades:**

1. **Recolha Centralizada de Eventos**
   - Logs de apps, infraestrutura, acessos
   - Correlação de eventos
   - Retenção conforme política

2. **Deteção de Incidentes**
   - Identificação de eventos anómalos
   - Classificação: Severidade + Tipo
   - Registo automatizado

3. **Resposta a Incidentes**
   - Escalação conforme plano
   - Documentação: O quê, quando, ações
   - Comunicação a stakeholders

4. **Aprendizagem Contínua**
   - Post-incident review
   - Atualização de medidas
   - Melhoria de processos

**Exemplos práticos:** Ver `exemplo-playbook/04-exemplo-relatorio-incidentes.md`

**Responsável:** Security/SRE  
**Evidência:** Logs de incidentes, plano de resposta

---

### 3.2 Ciclo de Vida de Fornecedores Contratuais

**Objetivo:** Gestão segura de fornecedores (pessoas e empresas contratadas formalmente) (Cap. 14, DORA Art. 26–28)

**Nota Important:** Este ciclo de vida aplica-se a **fornecedores contratuais explícitos** (contractors, outsourcing, prestadores). Para dependências de software (SBOM), ver Cap. 05.

**Atividades (User Stories US-15 a US-20):**

1. **US-15: Preparação Técnica Pré-Acesso**
   - Avaliação prévia (background, referências)
   - Formação técnica em SbD
   - Sandbox para exercícios práticos

2. **US-16: Onboarding e Formação**
   - Trilho de formação por função
   - Cobertura: SbD, práticas seguras, compliance
   - Validação: Formação completada

3. **US-17: Offboarding Seguro**
   - Procedimento estruturado de desligamento
   - Revogação de acessos (paralela, auditada)
   - Confirmação de conclusão

4. **US-18 a US-20: Monitorização Contínua**
   - Fornecedores em inventário (Cap. 05)
   - Revisão periódica de acessos
   - Feedback de desempenho

**Documentação:** Cap. 14, addon files

**Responsável:** GRC + Security  
**Evidência:** Inventário fornecedores, logs ciclo de vida

---

## FASE 4: Maturação (M12–M18)

### 4.1 Testes de Resiliência

**Objetivo:** Validar postura defensiva com testes contínuos (Cap. 10, 11, DORA Art. 19–20)

**Atividades:**

1. **Testes Contínuos (Cap. 10)**
   - SAST: Análise estática de código
   - DAST: Análise dinâmica
   - Testes de penetração
   - Fuzzing
   - Testes de segurança integrados no desenvolvimento

2. **Validação Pré-Produção (Cap. 11)**
   - Checklist de segurança antes de deploy
   - Confirmação de requisitos L1–L3
   - Aprovação formal

3. **Threat-Led Penetration Testing (TLPT)**
   - Para apps críticas (L3)
   - Baseado em cenários realistas (threat model)
   - Remediação documentada com SLAs
   - Evidência de conformidade técnica

**Responsável:** Security + Development  
**Evidência:** Relatórios de testes, plano de remediação

---

### 4.2 Métricas e KPIs

**Objetivo:** Monitorizar progresso conforme Cap. 12

**Dimensões essenciais:**

| Categoria | Métrica | Referência |
|-----------|---------|-----------|
| Risco Aplicacional | Apps classificadas L1-L3 | Cap. 01 |
| | Threat modeling (L3) | Cap. 03 |
| | Vulnerabilidades críticas não resolvidas | Cap. 05 |
| Desenvolvimento | Cobertura de testes | Cap. 10 |
| | Requisitos de segurança cobertos | Cap. 02 |
| Operações | Incidentes detetados e severidade | Cap. 12 |
| | MTTR por nível | Cap. 12 |
| Supply Chain | Fornecedores no inventário | Cap. 05, 14 |
| | Ciclo de vida (onboarding/offboarding) | Cap. 14 |
| Conformidade | Política assinada | Cap. 02, 14 |
| | Staff formado | Cap. 13 |
| | Trilho auditoria (logs) | Cap. 12, 14 |

**Exemplos práticos:** Ver `exemplos-playbook-dora/02-exemplo-kpis-targets.md`

**Nota:** Targets variam por organização - não prescritos no manual.

---

## FASE 5: Conformidade (Contínuo)

### 5.1 Preparação para Inspeção Regulatória

**Objetivo:** Demonstrar conformidade DORA com evidências

**Atividades:**

1. **Data Room de Conformidade**
   - Políticas de segurança (assinadas)
   - Matriz de requisitos (L1–L3 vs SbD-ToE)
   - Trilho auditoria (logs de 3+ anos)
   - Testes de resiliência (TLPT, DAST)
   - Ciclo de vida fornecedores

2. **Self-Assessment**
   - Auditoria interna contra DORA Art. 5–28
   - Gap analysis
   - Plano de remediação

3. **Comunicação com Supervisor**
   - Notificação de incidentes conforme DORA Art. 18
   - Demonstração de capacidade operacional
   - Reportes conforme regulador solicita

**Responsável:** GRC / Compliance  
**Evidência:** Data room completa, self-assessment

---

## Dimensão Crítica: Supply Chain em DORA (Cap. 05 + Cap. 14)

DORA Art. 26–28 exige supervisão de fornecedores. O SbD-ToE cobre isto com **duas dimensões separadas**:

### Dimensão 1: Dependências de Software (Cap. 05 - SBOM)
- **O quê:** Componentes usados (bibliotecas, frameworks, open source)
- **Fornecedores:** Implícitos (muitas vezes desconhecem que "fornecem")
- **Rastreabilidade:** SBOM (Software Bill of Materials)
- **Risco técnico:** Vulnerabilidades em dependências, licenças
- **Supervisão:** Análise contínua (SCA), updates de segurança

### Dimensão 2: Fornecedores Contratuais (Cap. 14 - Governance)
- **O quê:** Pessoas e empresas contratadas formalmente
- **Fornecedores:** Explícitos (contratos, acordos formais)
- **Rastreabilidade:** Inventário formal, RACI, ciclo de vida
- **Risco organizacional:** Acesso a sistemas, compliance, continuidade
- **Supervisão:** Onboarding/offboarding, formação, revisão periódica

**Integração em DORA:**
- Ambas dimensões precisam de **inventário e supervisão** (Art. 26–28)
- Mas com processos **diferentes**: técnico vs. organizacional
- **Não fusionar:** SBOM é automático/técnico; fornecedores contratuais são formais/organizacionais

### User Stories US-15 a US-20

**US-15:** Preparação Técnica e Validação Pré-Acesso
- Avaliação prévia do fornecedor (background, referências)
- Formação técnica obrigatória em SbD
- Ambiente controlado (sandbox) para exercícios práticos
- Template: `Cap. 14 addon/02-template-validacao-contractors.md`

**US-16:** Onboarding e Formação Contínua
- Trilho de formação por função (Development, DevOps, QA, etc.)
- Cobertura: Princípios SbD, práticas seguras, ferramentas, compliance
- Validação: Formação completada e documentada
- Guide: `Cap. 14 addon/12-guia-preparacao-sandbox.md`

**US-17:** Offboarding Seguro
- Procedimento estruturado de desligamento
- Revogação de acessos (paralela, documentada)
- Auditar e confirmar conclusão
- Checklist: `Cap. 14 addon/13-checklist-offboarding.md`

**US-18 a US-20:** Monitorização e Governança Contínua
- Fornecedores em inventário centralizado (Cap. 05)
- Revisão periódica de acessos e compliance
- Feedback e rating de desempenho

**Evidência Cap. 14:** Política de contratação assinada, inventário fornecedores, logs de ciclo de vida

---

## Checklist de Implementação

Este checklist mapeia cada fase aos princípios SbD-ToE:

- [ ] **Fase 0:** Política de segurança aprovada (Cap. 02, 14), RACI mapeado (Cap. 14), Toolchain essencial ativa (Cap. 08, 12)
- [ ] **Fase 1:** Apps classificadas L1–L3 (Cap. 01), Requisitos por nível definidos (Cap. 02)
- [ ] **Fase 2:** Gates de segurança em CI/CD (Cap. 07), Análise código (SAST/SCA), Threat modeling (Cap. 03), Trilho auditoria (Cap. 12)
- [ ] **Fase 3:** Recolha centralizada de eventos (Cap. 12), Deteção e resposta de incidentes (Cap. 12), Ciclo de vida fornecedores operacional (Cap. 14)
- [ ] **Fase 4:** Testes de segurança contínuos (Cap. 10), Validação pré-produção (Cap. 11), TLPT piloto (L3 apps)
- [ ] **Fase 5:** Trilho auditoria completo (Cap. 12), Data room de conformidade, Self-assessment concluído

---

## KPIs de Monitorização

Os KPIs devem alinhar com os capítulos do SbD-ToE e refletir conformidade com DORA:

| Categoria | Métrica | Referência SbD-ToE | Descrição |
|-----------|---------|-------------------|-----------|
| Risco Aplicacional | Apps classificadas por nível | Cap. 01 | % de apps com classificação L1–L3 completa |
| | Threat modeling | Cap. 03 | % de apps L3 com threat modeling |
| | Vulnerabilidades críticas | Cap. 05 | Número de vulns críticas não remediadas |
| Desenvolvimento | Cobertura de testes | Cap. 10 | % código com testes de segurança |
| | Requisitos de segurança | Cap. 02 | % de requisitos cobertos por teste |
| Operações | Incidentes detetados | Cap. 12 | Número e severidade de incidentes |
| | MTTR (Mean Time to Remediate) | Cap. 12 | Tempo médio remediação por nível |
| Supply Chain | Fornecedores no inventário | Cap. 05, 14 | % fornecedores críticos inventariados |
| | Ciclo de vida | Cap. 14 | % fornecedores com onboarding/offboarding |
| Conformidade | Política assinada | Cap. 02, 14 | Política de segurança aprovada |
| | Staff formado | Cap. 13 | % staff com formação em SbD |
| | Trilho auditoria | Cap. 12, 14 | Logs retidos conforme política |

**Exemplos práticos:** Ver `exemplo-playbook/02-exemplo-kpis-targets.md` para diferentes perfis organizacionais

---

## Próximos Passos

Este playbook é um **guia indicativo**. Implementação real deve adaptar-se ao contexto organizacional:

1. **Mapeamento Inicial:** Auditar conformidade atual contra Cap. 01–14 do SbD-ToE
2. **Definição de Roadmap:** Sequenciar fases conforme recursos disponíveis e dependências
3. **Aprovação Executiva:** Validar timeline e budget com direção
4. **Execução:** Iterar conforme planeado, ajustando conforme riscos reais
5. **Validação:** Testar conformidade com DORA requirements, documentar evidências

**Documentação:** Todos os capítulos referenciados (Cap. 01–14) oferecem detalhe técnico e operacional. Ver também exemplos práticos em `exemplo-playbook/`.

---

## Referências

- SbD-ToE Manual (Capítulos 01–14)
- SbD-ToE 002 - Cross-Check Normativo: `dora.md` (análise normativa)
- Regulamento DORA (UE 2022/2554)
- NIST SP 800-53, OWASP SAMM, BSIMM, SSDF
- Cap. 14 SbD-ToE: User Stories US-15 a US-20 (fornecedores/contractors)
- Addon files: Templates e guias operacionais
- **Exemplos práticos:** `exemplos-playbook-dora/` (reutilizáveis para NIS2, ISO 27001, etc.)

---

**Versão:** 1.0  
**Data:** Novembro 2025  
**Próxima revisão:** Junho 2026 (ou conforme DORA RTS/ITS evoluem)
