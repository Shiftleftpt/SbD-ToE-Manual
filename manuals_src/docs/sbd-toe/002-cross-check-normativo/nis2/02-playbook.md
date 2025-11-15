---
id: playbook
title: "SbD-ToE 4 NIS2: Playbook de Implementação"
description: Roadmap prático para implementar SbD-ToE conforme requisitos NIS2 — mapeamento direto de artigos para ações
tags: [playbook, nis2, implementacao, roadmap]
sidebar_position: 3
---

# SbD-ToE 4 NIS2: Playbook de Implementação

## Visão Geral

Este playbook mapeia **requisitos NIS2 (Diretiva UE 2022/2555) para ações SbD-ToE práticas**.

**Princípio:** Implementar SbD-ToE = Cumprir NIS2. Não é complementar, é direto.

**Estrutura:** Cada seção mostra:
- NIS2 requisito (artigo)
- SbD-ToE capítulo/addon aplicável
- O que fazer (ação concreta)
- Evidência regulatória

---

## Mapa Rápido: NIS2 Art. → SbD-ToE

| NIS2 Artigo | Requisito | Capítulo SbD-ToE | Ação Principal |
|----------|-----------|-----------------|----------------|
| **20** | Governação e Responsabilização | Cap. 02, 13, 14 | Aprovar políticas (board); formação gestão |
| **21** | Medidas de Gestão de Risco | Cap. 01–14 | Implementar controlos técnicos; evidências |
| **23** | Reporte de Incidentes | Cap. 12, 14 | Deteção, reporte 24h/72h/1M; schema |
| **Cadeia Fornecimento** | Segurança de Fornecedores | Cap. 05, 14 | SBOM; avaliação terceiros; registos |
| **Continuidade** | Continuidade e Crise | Cap. 12 | Backups testados; DR; logging |

---

## Como Implementar (Ordem Lógica)

### Fase 1: Governação (M0–M2)
**NIS2 Art. 20** — Estabelecer responsabilização da board

1. **Criar Comissão de Cibersegurança**
   - Membros: Board member, CISO, CTO, GRC Manager, General Counsel
   - Frequência: Trimestral (mínimo)
   - **Evidência:** Ata de reuniões assinadas pelo board

2. **Aprovar Política de Gestão de Risco de Cibersegurança**
   - Referência: [Cap. 02 - Requisitos de Segurança](/sbd-toe/sbd-manual/requisitos-seguranca/intro)
   - **Aprovação:** Board signature (NIS2 Art. 20)
   - **Conteúdo:** Requisitos L1–L3, ciclo de vida, responsabilidades, medidas Art. 21

3. **Definir RACI**
   - Quem aprova o quê (aprovações formais)
   - Escalations (quando elevar)
   - Referência: [Cap. 07 - Roles](/sbd-toe/000-teory-of-everything/07-roles)

4. **Estabelecer Programa de Formação para a Gestão**
   - Periodicidade: Anual (mínimo)
   - Conteúdo: Ameaças, requisitos NIS2, responsabilidades
   - **Evidência:** Presenças, materiais, avaliações
   - Referência: [Cap. 13 - Formação e Onboarding](/sbd-toe/sbd-manual/formacao-onboarding/intro)

---

### Fase 2: Classificação e Inventário (M2–M4)
**NIS2 Art. 21** — Conhecer o que é crítico

1. **Inventariar Aplicações e Sistemas**
   - Nome, proprietário, dados processados, serviços suportados
   - Dependências (quem depende)
   - **Tipo de entidade:** Essencial / Importante (conforme NIS2 Anexos I/II)
   - Referência: [Cap. 01 - Classificação de Aplicações](/sbd-toe/sbd-manual/classificacao-aplicacoes/intro)

2. **Classificar por Risco (L1–L3)**
   - L3: Impacto direto em serviços críticos (essenciais)
   - L2: Suporta processos importantes
   - L1: Ferramentas de suporte
   - Matriz assinada por CTO + Product leads + CISO

3. **Definir Requisitos Mínimos por Nível**
   - L1: Basics (senhas, logs, code review)
   - L2: Essenciais (+ threat modeling, SAST)
   - L3: Rigorosos (+ DAST, 24x7 monitorização)
   - Referência: [Cap. 02 - Requisitos](/sbd-toe/sbd-manual/requisitos-seguranca/intro)

---

### Fase 3: Medidas de Gestão de Risco (M4–M8)
**NIS2 Art. 21** — Implementar medidas técnicas e organizacionais

#### 3.1 Políticas de Análise de Risco
- **O que:** Identificar e avaliar riscos de cibersegurança
- **Como:** Threat modeling (L2–L3); análise de impacto
- **Trilho:** Documentar riscos, decisões, mitigações
- **Referência:** [Cap. 03 - Threat Modeling](/sbd-toe/sbd-manual/threat-modeling/intro)

#### 3.2 Gestão de Vulnerabilidades e Patching
- **O que:** SBOM (Software Bill of Materials) + SCA
- **Por quê:** Art. 21 exige gestão de vulnerabilidades e atualização de sistemas
- **Como:** Gerar SBOM; scan contínuo; atualizar dependências
- **Trilho:** Manter SBOM atualizado, vulnerabilidades documentadas
- **Referência:** [Cap. 05 - Dependências & SBOM](/sbd-toe/sbd-manual/dependencias-sbom-sca/intro)

#### 3.3 Segurança em Desenvolvimento e Manutenção
- **O que:** Gates de segurança no pipeline
- **Como:** SAST/SCA antes de merge; bloqueio de secrets; validação pré-deploy
- **Trilho:** Logs auditados de quem fez o quê, quando
- **Referência:** [Cap. 06 - Desenvolvimento Seguro](/sbd-toe/sbd-manual/desenvolvimento-seguro/intro), [Cap. 07 - CI/CD Seguro](/sbd-toe/sbd-manual/cicd-seguro/intro)

#### 3.4 IAM e Controlo de Acessos
- **O que:** Autenticação forte, gestão de privilégios
- **Como:** MFA, princípio do menor privilégio, revisão periódica
- **Trilho:** Logs de acessos, aprovações, revogações
- **Referência:** [Cap. 02 - Requisitos de Segurança](/sbd-toe/sbd-manual/requisitos-seguranca/intro), [Cap. 04 - Arquitetura Segura](/sbd-toe/sbd-manual/arquitetura-segura/intro)

#### 3.5 Criptografia
- **O que:** Proteção de dados em trânsito e em repouso
- **Como:** TLS 1.2+; encryption at rest; key management
- **Trilho:** Inventário de certificados, rotação de chaves
- **Referência:** [Cap. 02 - Requisitos de Segurança](/sbd-toe/sbd-manual/requisitos-seguranca/intro), [Cap. 04 - Arquitetura Segura](/sbd-toe/sbd-manual/arquitetura-segura/intro)

#### 3.6 Higiene Cibernética e Formação
- **O que:** Treino de staff, awareness de ameaças
- **Como:** Programa de formação contínua, simulações
- **Trilho:** Presenças, materiais, avaliações
- **Referência:** [Cap. 13 - Formação e Onboarding](/sbd-toe/sbd-manual/formacao-onboarding/intro)

---

### Fase 4: Segurança da Cadeia de Fornecimento (M6–M10)
**NIS2 Art. 21** — Gestão de fornecedores e terceiros

#### 4.1 Fornecedores de Componentes (SBOM)
**Já em Fase 3.2** — Cap. 05 cobre isto com SCA + SBOM

#### 4.2 Fornecedores Contratuais
- **O que:** Pessoas/empresas contratadas (contractors, outsourcing)
- **Ciclo de Vida:**
  - **Onboarding:** Validação, formação SbD, sandbox
  - **Operação:** Acesso controlado, revisão periódica
  - **Offboarding:** Revogação de acessos, auditar conclusão
- **Referência:** [Cap. 14 - Governança e Contratação](/sbd-toe/sbd-manual/governanca-contratacao/intro)

#### 4.3 Registo de Fornecedores Críticos
- **O que:** Inventário de fornecedores TIC críticos
- **Como:** Campos conforme autoridade nacional (seguir guias/portais locais)
- **Trilho:** Atualizações periódicas, avaliações de risco
- **Referência:** [Cap. 05 - Dependências & SBOM](/sbd-toe/sbd-manual/dependencias-sbom-sca/intro), [Cap. 14 - Governança e Contratação](/sbd-toe/sbd-manual/governanca-contratacao/intro)

---

### Fase 5: Deteção e Resposta a Incidentes (M8–M12)
**NIS2 Art. 23** — Reporte de incidentes significativos

#### 5.1 Monitorização Centralizada
- **O que:** Logs centralizados de apps, infra, acessos
- **Retenção:** Conforme orientações ENISA/autoridade nacional
- **Proteção:** Imutabilidade (impedir alteração)
- **Referência:** [Cap. 12 - Monitorização e Operações](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro)

#### 5.2 Deteção e Classificação de Incidentes
- **O que:** Identificar eventos anómalos; classificar por severidade
- **Escalação:** Conforme plano (criticidade)
- **Documentação:** O quê, quando, ações, impacto
- **Referência:** [Cap. 12 - Monitorização e Operações](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro)

#### 5.3 Reporte de Incidentes Significativos
- **O que:** Submeter incidentes à autoridade competente
- **Prazos:**
  - **Alerta cedo:** 24h após conhecimento
  - **Notificação:** 72h com avaliação inicial
  - **Relatório final:** 1 mês (podendo haver atualizações intermédias)
- **Schema:** Parametrizar campos conforme Art. 23 e guias ENISA
- **Como:** Exportadores SIEM/ITSM → ficheiros prontos a submeter
- **Referência:** [Cap. 12 - Monitorização e Operações](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro)

---

### Fase 6: Continuidade e Crise (M8–M12)
**NIS2 Art. 21** — Garantir continuidade operacional

#### 6.1 Backups e Disaster Recovery
- **O que:** Backups regulares, testados, off-site
- **Como:** Automatização, testes de restauração periódicos
- **Trilho:** Logs de backups, testes, resultados
- **Referência:** [Cap. 12 - Monitorização e Operações](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro)

#### 6.2 Gestão de Crise
- **O que:** Plano de resposta a incidentes graves
- **Como:** Runbooks, exercícios, roles definidos
- **Trilho:** Exercícios documentados, lições aprendidas
- **Referência:** [Cap. 12 - Monitorização e Operações](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro)

---

### Fase 7: Validação e Testes (M12–M18)
**NIS2 Art. 21** — Avaliar eficácia dos controlos

#### 7.1 Testes Contínuos
- **SAST:** Análise estática de código (integrado em CI/CD)
- **DAST:** Análise dinâmica de aplicações em staging
- **Penetração:** Testes manuais baseados em threat model
- **Referência:** [Cap. 10 - Testes de Segurança](/sbd-toe/sbd-manual/testes-seguranca/intro)

#### 7.2 Validação Pré-Deploy
- **O que:** Checklist de segurança antes de produção
- **Confirmação:** Todos requisitos L1–L3 cobertos
- **Aprovação:** Formal (AppSec + Gestão para L3)
- **Referência:** [Cap. 11 - Deploy Seguro](/sbd-toe/sbd-manual/deploy-seguro/intro)

#### 7.3 Avaliação da Eficácia
- **O que:** Revisão periódica dos controlos implementados
- **Como:** Auditorias internas, métricas de segurança, testes
- **Trilho:** Relatórios de auditoria, planos de remediação
- **Referência:** [Cap. 12 - Monitorização e Operações](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro)

---

## Checklist de Conformidade

A lista abaixo permite validar o alinhamento do programa SbD-ToE com os requisitos NIS2. Sugere-se a revisão periódica destes pontos para garantir conformidade contínua:

- [ ] **Governação:** Política assinada por board; RACI mapeado; formação anual à gestão
- [ ] **Classificação:** Todas apps classificadas L1–L3; tipo de entidade (essencial/importante) definido
- [ ] **Políticas de Risco:** Threat modeling implementado (L2–L3)
- [ ] **Vulnerabilidades:** SBOM gerado e atualizado; SCA contínuo
- [ ] **CI/CD:** Gates de segurança operacionais
- [ ] **IAM:** MFA implementado; princípio do menor privilégio ativo
- [ ] **Criptografia:** TLS 1.2+; encryption at rest; key management
- [ ] **Formação:** Programa de formação contínua operacional
- [ ] **Fornecedores:** Inventário de fornecedores críticos; ciclo de vida operacional
- [ ] **Monitorização:** Logs centralizados, retenção adequada
- [ ] **Incidentes:** Processo de deteção e reporte 24h/72h/1M ativo
- [ ] **Continuidade:** Backups testados; plano de DR operacional
- [ ] **Testes:** SAST/DAST integrados; avaliação da eficácia periódica
- [ ] **Evidência:** Data room com documentação (políticas, testes, logs, formações)

---

## O Que Cada Capítulo SbD-ToE Cobre (Referência Rápida)

| Capítulo | NIS2 Artigos | O Que Faz |
|----------|-------------|----------|
| **Cap. 01** | Art. 21 | Classificação de apps por risco (L1–L3) |
| **Cap. 02** | Art. 20, 21 | Requisitos de segurança mínimos por nível |
| **Cap. 03** | Art. 21 | Threat modeling para identificar ameaças realistas |
| **Cap. 04** | Art. 21 | Arquitetura segura, IAM, criptografia |
| **Cap. 05** | Art. 21 | SBOM, SCA, gestão de vulnerabilidades |
| **Cap. 06** | Art. 21 | Desenvolvimento seguro |
| **Cap. 07** | Art. 21 | CI/CD seguro, gates, trilho auditado |
| **Cap. 08** | Art. 21 | IaC segura |
| **Cap. 09** | Art. 21 | Containers/runtime seguros |
| **Cap. 10** | Art. 21 | Testes contínuos (SAST/DAST/penetração) |
| **Cap. 11** | Art. 21 | Validação pré-deploy, conformidade requisitos |
| **Cap. 12** | Art. 21, 23 | Monitorização, deteção/reporte de incidentes, continuidade |
| **Cap. 13** | Art. 20, 21 | Formação de staff e gestão em cibersegurança |
| **Cap. 14** | Art. 20, 21 | Governança, RACI, ciclo de vida fornecedores |

---

## Métrica Simples: Estou Compliant?

Se consegues responder SIM a isto, estás alinhado com NIS2:

1. **Governance:** Tenho política assinada pelo board? ✓
2. **Board Training:** A gestão tem formação anual em cibersegurança? ✓
3. **Risk Management:** Todas as apps estão classificadas? ✓
4. **Policies:** Tenho políticas de análise de risco e segurança? ✓
5. **Vulnerabilities:** Tenho SBOM e SCA ativo? ✓
6. **Development:** CI/CD seguro com gates operacionais? ✓
7. **IAM & Crypto:** MFA e criptografia implementados? ✓
8. **Training:** Programa de formação contínua ativo? ✓
9. **Supply Chain:** Inventário de fornecedores críticos e ciclo de vida operacional? ✓
10. **Operations:** Monitorização centralizada com retenção adequada? ✓
11. **Incident Response:** Consigo detetar e reportar incidentes 24h/72h/1M? ✓
12. **Continuity:** Backups testados e plano de DR operacional? ✓
13. **Testing:** Faço SAST/DAST e avaliação da eficácia? ✓
14. **Evidence:** Consigo demonstrar tudo isto em auditoria? ✓

**Se 12/14:** Estás pronto para autoridade nacional.  
**Se `<`7/14:** Prioriza governação + classificação + monitorização + incidentes.

---

## Nota Crítica: Gestão de Exceções em NIS2

NIS2 exige conformidade com medidas de gestão de risco (Art. 21). Exceções (desvios) devem ser formais e auditadas, com trilho documental e aprovação adequada.

O que caracteriza uma exceção em SbD-ToE/NIS2:
- Desvio formal de um requisito
- Exemplo: Deploy com vulnerabilidade alta (vs. requisito L3 = zero críticas)
- Aprovação formal, justificação, TTL (Time-To-Live), plano de remediação

Quem aprova (conforme NIS2 Art. 20):
- L1 (baixo risco): Tech lead / AppSec Engineer
- L2 (médio risco): CISO
- L3 (crítico): Board / CRO (Board é accountable, não é delegável)

Implicação regulatória:
- Exceções sem aprovação formal podem comprometer a supervisão (Art. 20)
- Algumas exceções são inaceitáveis (ex: SQLi nunca, MFA nunca)
- Trilho auditado é obrigatório para demonstrar controlo à autoridade nacional

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

1. Audit de conformidade atual: Verificar Cap. 01–14 do SbD-ToE contra requisitos NIS2
2. Verificar classificação da entidade: Essencial / Importante (conforme Anexos I/II)
3. Definir roadmap: Sequenciar fases conforme contexto organizacional
4. Implementar: Iterar conforme planeado
5. Registar na autoridade nacional: Seguir guias/portais locais (se aplicável)
6. Validar: Demonstrar conformidade em auditoria

Documentação completa: Ver capítulos SbD-ToE 01–14 para detalhe técnico e operacional.

---

## Referências

- **SbD-ToE Manual:** Capítulos 01–14 (detalhe técnico por domínio)
- **Cross-Check NIS2:** [002 - NIS2.md](/sbd-toe/002-cross-check-normativo/nis2) (análise normativa completa)
- **Diretiva NIS2:** UE 2022/2555
- **ENISA:** Orientações técnicas e mapeamentos práticos (2024/2025)
- **Autoridades Nacionais:** Guias/portais de registo e requisitos locais

---

**Versão:** 1.0  
**Data:** Janeiro 2025  
**Nota:** Este playbook complementa `002-cross-check-normativo/NIS2.md` com implementação prática
