---
id: playbook
title: "SbD-ToE 4 DORA: Playbook de Implementação"
description: Roadmap prático para implementar SbD-ToE conforme requisitos DORA — mapeamento direto de artigos para ações
tags: [playbook, dora, implementacao, roadmap]
sidebar_position: 2
---

# SbD-ToE 4 DORA: Playbook de Implementação

## Visão Geral

Este playbook mapeia **requisitos DORA (Regulamento UE 2022/2554) para ações SbD-ToE práticas**.

**Princípio:** Implementar SbD-ToE = Cumprir DORA. Não é complementar, é direto.

**Estrutura:** Cada seção mostra:
- DORA requisito (artigo)
- SbD-ToE capítulo/addon aplicável
- O que fazer (ação concreta)
- Evidência regulatória

> 📚 **Recursos de Suporte:** Para templates práticos e exemplos de implementação, consultar [Exemplo-Playbook](/sbd-toe/cross-check-normativo/exemplo-playbook/indice) com toolchains, KPIs, RACI e relatórios de incidentes reutilizáveis para DORA e outros frameworks.

---

## Mapa Rápido: DORA Art. → SbD-ToE

| DORA Artigo | Requisito | Capítulo SbD-ToE | Ação Principal |
|----------|-----------|-----------------|----------------|
| **5** | Gestão de Risco TIC | [Cap. 01](/sbd-toe/sbd-manual/classificacao-aplicacoes/intro), [Cap. 14](/sbd-toe/sbd-manual/governanca-contratacao/intro) | Classificar apps; aprovar políticas; supervisão |
| **16** | Partilha de Ameaças | [Cap. 12](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro) | Integrar threat intelligence; acordos de partilha |
| **18** | Reporte de Incidentes | [Cap. 12](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro), [Cap. 14](/sbd-toe/sbd-manual/governanca-contratacao/intro) | Deteção, reporte formal, documentação |
| **19–20** | Testes de Resiliência | [Cap. 10](/sbd-toe/sbd-manual/testes-seguranca/intro), [Cap. 11](/sbd-toe/sbd-manual/deploy-seguro/intro) | Testes contínuos (SAST/DAST), TLPT readiness |
| **26–28** | Gestão de Fornecedores | [Cap. 05](/sbd-toe/sbd-manual/dependencias-sbom-sca/intro), [Cap. 14](/sbd-toe/sbd-manual/governanca-contratacao/intro) | SBOM; ciclo de vida contractors |

---

## Como Implementar (Ordem Lógica)

### Fase 1: Governação (M0–M2)
**DORA Art. 5** — Estabelecer supervisão da board

1. **Criar Comissão de Segurança Digital**
   - Membros: CISO, CTO, GRC Manager, General Counsel
   - Frequência: Mensal
   - **Evidência:** Ata de reuniões assinadas

2. **Aprovar Política de Segurança Aplicacional**
   - Referência: [Cap. 02 - Requisitos de Segurança](/sbd-toe/sbd-manual/requisitos-seguranca/intro)
   - **Aprovação:** Board signature (DORA Art. 5)
   - **Conteúdo:** Requisitos L1–L3, ciclo de vida, responsabilidades

3. **Definir RACI**
   - Quem aprova o quê (aprovações formais)
   - Escalations (quando elevar)
   - Referência: [Cap. 07 - Roles](/sbd-toe/teory-of-everything/roles)
   - 📄 **Template:** [RACI e Governance](../exemplo-playbook/exemplo-raci-governance) - Exemplos de matrizes DORA-compatíveis

---

### Fase 2: Classificação e Inventário (M2–M4)
**DORA Art. 5** — Conhecer o que é crítico

1. **Inventariar Aplicações**
   - Nome, proprietário, dados processados
   - Dependências (quem depende)
   - Referência: [Cap. 01 - Classificação de Aplicações](/sbd-toe/sbd-manual/classificacao-aplicacoes/intro)

2. **Classificar por Risco (L1–L3)**
   - L3: Impacto direto em funções críticas
   - L2: Suporta processos importantes
   - L1: Ferramentas de suporte
   - Matriz assinada por CTO + Product leads

3. **Definir Requisitos Mínimos por Nível**
   - L1: Basics (senhas, logs, code review)
   - L2: Essenciais (+ threat modeling, SAST)
   - L3: Rigorosos (+ DAST, 24x7 monitorização)
   - Referência: [Cap. 02 - Requisitos](/sbd-toe/sbd-manual/requisitos-seguranca/intro)

---

### Fase 3: Segurança Técnica (M4–M8)
**DORA Art. 19–20** — Implementar controlos de resiliência

#### 3.1 CI/CD Seguro
- **O que:** Gates de segurança no pipeline
- **Como:** SAST/SCA antes de merge; bloqueio de secrets; validação pré-deploy
- **Trilho:** Logs auditados de quem fez o quê, quando
- **Referência:** [Cap. 07 - CI/CD Seguro](/sbd-toe/sbd-manual/cicd-seguro/intro)
- 📄 **Template:** [Opções de Toolchain](../exemplo-playbook/exemplo-toolchain-options) - Comparação de ferramentas CI/CD e gates

#### 3.2 Análise de Dependências (CRÍTICO PARA DORA)
- **O que:** SBOM (Software Bill of Materials) + SCA
- **Por quê:** Art. 26–28 exige saber quem são teus fornecedores de software
- **Como:** Gerar SBOM; scan contínuo de vulnerabilidades; atualizar dependências
- **Trilho:** Manter SBOM atualizado, vulnerabilidades documentadas
- **Referência:** [Cap. 05 - Dependências & SBOM](/sbd-toe/sbd-manual/dependencias-sbom-sca/intro)

#### 3.3 Threat Modeling (L3 apps)
- **O que:** Identificar ameaças realistas
- **Como:** Mapear arquitetura; usar STRIDE/MITRE ATT&CK
- **Referência:** [Cap. 03 - Threat Modeling](/sbd-toe/sbd-manual/threat-modeling/intro)

---

### Fase 4: Operações (M8–M12)
**DORA Art. 18** — Detetar e responder a incidentes

#### 4.1 Monitorização Centralizada
- **O que:** Logs centralizados de apps, infra, acessos
- **Retenção:** 3+ anos (DORA)
- **Proteção:** Imutabilidade (impedir alteração)
- **Referência:** [Cap. 12 - Monitorização e Operações](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro)

#### 4.2 Deteção e Resposta a Incidentes
- **O que:** Identificar eventos anómalos; classificar; responder
- **Escalação:** Conforme plano (criticidade)
- **Documentação:** O quê, quando, ações, aprendizagens
- **Referência:** [Cap. 12 - Monitorização e Operações](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro)
- 📄 **Template:** [Relatório de Incidentes](../exemplo-playbook/exemplo-relatorio-incidentes) - Template DORA-compatível para reporte formal

#### 4.3 Partilha de Ameaças
- **O que:** Recolher e disseminar informação sobre ameaças/incidentes
- **Como:** Integração com STIX/TAXII; acordos de partilha
- **Referência:** [Cap. 12 - Monitorização e Operações](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro)

---

### Fase 5: Supply Chain (M8–M12)
**DORA Art. 26–28** — Gestão de fornecedores

#### 5.1 Fornecedores de Componentes (SBOM)
**Já em Fase 3.2** — [Cap. 05](/sbd-toe/sbd-manual/dependencias-sbom-sca/intro) cobre isto com SCA + SBOM

#### 5.2 Fornecedores Contratuais
- **O que:** Pessoas/empresas contratadas (contractors, outsourcing)
- **Ciclo de Vida:**
  - **Onboarding:** Validação, formação SbD, sandbox
  - **Operação:** Acesso controlado, revisão periódica
  - **Offboarding:** Revogação de acessos, auditar conclusão
- **Referência:** [Cap. 14 - Governança e Contratação](/sbd-toe/sbd-manual/governanca-contratacao/intro)

---

### Fase 6: Validação e Testes (M12–M18)
**DORA Art. 19–20** — Validar postura defensiva

#### 6.1 Testes Contínuos
- **SAST:** Análise estática de código (integrado em CI/CD)
- **DAST:** Análise dinâmica de aplicações em staging
- **Penetração:** Testes manuais baseados em threat model
- **Referência:** [Cap. 10 - Testes de Segurança](/sbd-toe/sbd-manual/testes-seguranca/intro)

#### 6.2 Validação Pré-Deploy
- **O que:** Checklist de segurança antes de produção
- **Confirmação:** Todos requisitos L1–L3 cobertos
- **Aprovação:** Formal (AppSec + Gestão para L3)
- **Referência:** [Cap. 11 - Deploy Seguro](/sbd-toe/sbd-manual/deploy-seguro/intro)

#### 6.3 TLPT (Threat-Led Penetration Testing)
- **O que:** Testes de resiliência realistas para apps L3
- **Base:** Cenários de threat model
- **Remediação:** Documentada com SLAs
- **Referência:** [Cap. 10 - Testes de Segurança](/sbd-toe/sbd-manual/testes-seguranca/intro)

---

## Checklist de Conformidade

A lista abaixo permite validar o alinhamento do programa SbD-ToE com os requisitos DORA. Recomenda-se a revisão periódica destes pontos para garantir conformidade contínua:

- [ ] **Governação:** Política assinada por board; RACI mapeado
- [ ] **Classificação:** Todas apps classificadas L1–L3
- [ ] **CI/CD:** Gates de segurança operacionais
- [ ] **SBOM:** Gerado e atualizado; SCA contínuo
- [ ] **Threat Model:** L3 apps com threat modeling completo
- [ ] **Monitorização:** Logs centralizados, retenção 3+ anos
- [ ] **Incidentes:** Processo de deteção e resposta ativo
- [ ] **Fornecedores:** Inventário de contractors; ciclo de vida operacional
- [ ] **Testes:** SAST/DAST integrados; TLPT piloto executado
- [ ] **Evidência:** Data room com documentação (políticas, testes, logs)

---

## O Que Cada Capítulo SbD-ToE Cobre (Referência Rápida)

| Capítulo | DORA Artigos | O Que Faz |
|----------|-------------|----------|
| **[Cap. 01](/sbd-toe/sbd-manual/classificacao-aplicacoes/intro)** | Art. 5 | Classificação de apps por risco (L1–L3) |
| **[Cap. 02](/sbd-toe/sbd-manual/requisitos-seguranca/intro)** | Art. 5, 19 | Requisitos de segurança mínimos por nível |
| **[Cap. 03](/sbd-toe/sbd-manual/threat-modeling/intro)** | Art. 19–20 | Threat modeling para identificar ameaças realistas |
| **[Cap. 05](/sbd-toe/sbd-manual/dependencias-sbom-sca/intro)** | Art. 26–28 | SBOM, SCA, gestão de dependências de software |
| **[Cap. 07](/sbd-toe/sbd-manual/cicd-seguro/intro)** | Art. 19–20 | CI/CD seguro, gates, trilho auditado |
| **[Cap. 10](/sbd-toe/sbd-manual/testes-seguranca/intro)** | Art. 19–20 | Testes contínuos (SAST/DAST/penetração) |
| **[Cap. 11](/sbd-toe/sbd-manual/deploy-seguro/intro)** | Art. 19–20 | Validação pré-deploy, conformidade requisitos |
| **[Cap. 12](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro)** | Art. 16, 18 | Monitorização, deteção de incidentes, threat intel |
| **[Cap. 13](/sbd-toe/sbd-manual/formacao-onboarding/intro)** | Art. 5 | Formação de staff em SbD (exigência de supervisão) |
| **[Cap. 14](/sbd-toe/sbd-manual/governanca-contratacao/intro)** | Art. 5, 26–28 | Governança, RACI, ciclo de vida fornecedores |

---

## Métrica Simples: Estou Compliant?

Se consegues responder SIM a isto, estás alinhado com DORA:

1. **Governance:** Tenho política assinada pelo board? ✓
2. **Risk Management:** Todas as apps estão classificadas? ✓
3. **Security by Design:** Meus requisitos cobrem L1–L3? ✓
4. **Software Supply:** Tenho SBOM e SCA ativo? ✓
5. **Operations:** Tenho monitorização centralizada com 3+ anos retenção? ✓
6. **Incident Response:** Conseguo detetar e reportar incidentes formalmente? ✓
7. **Vendor Management:** Tenho ciclo de vida formal de contractors? ✓
8. **Testing:** Faço SAST/DAST/TLPT? ✓
9. **Evidence:** Consigo demonstrar tudo isto em auditoria? ✓

**Se 8/9:** Estás pronto para regulador.  
**Se `<`5/9:** Prioriza governação + classificação + monitorização.

---

## Recursos Práticos de Implementação

Para suporte concreto na implementação deste playbook, consultar os seguintes exemplos reutilizáveis:

- 🛠️ **[Opções de Toolchain](../exemplo-playbook/exemplo-toolchain-options)** - Comparação de ferramentas (IaC, logs, SCA, SAST, CI/CD) com exemplos de configuração
- 📊 **[KPIs e Targets](../exemplo-playbook/exemplo-kpis-targets)** - Métricas de segurança por perfil organizacional (fintech vs. banco, pequena vs. grande empresa)
- 👥 **[RACI e Governance](../exemplo-playbook/exemplo-raci-governance)** - Matrizes de responsabilidades e aprovações DORA-compatíveis
- 📝 **[Relatório de Incidentes](../exemplo-playbook/exemplo-relatorio-incidentes)** - Templates de reporte formal com campos DORA, exemplos de classificação e escalação

Estes recursos são **reutilizáveis para múltiplos frameworks** (DORA, NIS2, ISO 27001, CRA) e demonstram como implementar as abstenções deliberadas do SbD-ToE (o manual não prescreve ferramentas específicas, os exemplos mostram opções práticas).

**Responsável:** Security/SRE  
**Evidência:** Logs de incidentes, plano de resposta

## Nota Crítica: Gestão de Exceções em DORA

DORA exige conformidade com requisitos de resiliência (Art. 5–28). Exceções (desvios) devem ser formais e auditadas, com trilho documental e aprovação adequada.

O que caracteriza uma exceção em SbD-ToE/DORA:
- Desvio formal de um requisito
- Exemplo: Deploy com vulnerabilidade alta (vs. requisito L3 = zero críticas)
- Aprovação formal, justificação, TTL (Time-To-Live), plano de remediação

Quem aprova (conforme DORA Art. 5):
- L1 (baixo risco): Tech lead / AppSec Engineer
- L2 (médio risco): CISO
- L3 (crítico): Board / CRO (Board é accountable, não é delegável)

Implicação regulatória:
- Exceções sem aprovação formal podem comprometer a supervisão (Art. 5)
- Algumas exceções são inaceitáveis (ex: SQLi nunca, MFA nunca)
- Trilho auditado é obrigatório para demonstrar controlo ao regulador

Sugere-se:
1. Política clara de quem aprova por nível de risco
2. Trilho auditado: O quê, quem, quando, justificação, TTL
3. SLAs de remediação: Critical ≤30d, High ≤90d, Medium ≤180d
4. Lista de exceções inaceitáveis (política)
5. Revisão periódica, escalação se expirada

A ausência de formalização pode comprometer a conformidade regulatória e expor a organização a riscos desnecessários.

**Referência:** [Cap. 02 - Requisitos de Segurança](/sbd-toe/sbd-manual/requisitos-seguranca/intro) (addon 08) e [Cap. 14 - Governança](/sbd-toe/sbd-manual/governanca-contratacao/intro) (exceções formalizadas)

---

## Próximos Passos

Sugere-se a seguinte abordagem para garantir conformidade e maturidade contínua:

1. Audit de conformidade atual: Verificar [Cap. 01](/sbd-toe/sbd-manual/classificacao-aplicacoes/intro)–[Cap. 14](/sbd-toe/sbd-manual/governanca-contratacao/intro) do SbD-ToE contra requisitos DORA
2. Definir roadmap: Sequenciar fases conforme contexto organizacional
3. Implementar: Iterar conforme planeado
4. Validar: Demonstrar conformidade em auditoria

Documentação completa: Ver capítulos SbD-ToE 01–14 para detalhe técnico e operacional.

---

## Referências

- **SbD-ToE Manual:** Capítulos 01–14 (detalhe técnico por domínio)
- **Cross-Check DORA:** [Análise normativa completa](/sbd-toe/cross-check-normativo/dora/intro)
- **Regulamento DORA:** UE 2022/2554
- **Frameworks de Referência:** NIST SP 800-53, OWASP SAMM, BSIMM, SSDF

---

**Versão:** 1.1 (Simplificado, alinhado com DORA)  
**Data:** Novembro 2025  
**Nota:** Este playbook complementa a [análise normativa DORA](intro) com implementação prática
