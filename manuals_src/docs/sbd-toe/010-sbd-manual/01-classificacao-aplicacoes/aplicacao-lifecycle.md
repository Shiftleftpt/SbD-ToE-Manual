---
id: aplicacao-lifecycle
title: Como Fazer
description: Aplicação da classificação de criticidade ao longo do ciclo de vida de desenvolvimento
tags: [tipo:aplicacao, ciclo-vida, classificacao, risco, user-stories, genia:us-format-normalization]
---

# 🛠️ Aplicação da Classificação de Criticidade ao Longo do Ciclo de Vida

A correta aplicação da classificação de criticidade (L1–L3) ao longo de todo o ciclo de desenvolvimento é essencial para garantir que os controlos de segurança são sempre proporcionais ao risco real, efetivamente rastreáveis e revistos de acordo com os eventos e alterações relevantes.

Este capítulo detalha, de forma operacional e prescritiva, **quando e como implementar a classificação de criticidade na prática**, descrevendo as ações esperadas por cada papel, os artefactos produzidos, e apresentando exemplos de user stories reutilizáveis — sempre de acordo com o nível de risco da aplicação.

---

## 🧭 Abrangência e quando aplicar

| Fase / Evento                          | Ação esperada                                                   | Documento de apoio                                                                 |
|----------------------------------------|-----------------------------------------------------------------|-------------------------------------------------------------------------------------|
| 🚧 Início de projeto                   | Classificar aplicação segundo modelo E+D+I                      | [Modelo de Classificação](/sbd-toe/sbd-manual/classificacao-aplicacoes/addon/modelo-classificacao-eixos) |
| 🔄 Nova release ou integração          | Rever classificação com base em alterações relevantes           | [Ciclo de Vida do Risco](/sbd-toe/sbd-manual/classificacao-aplicacoes/addon/ciclo-vida-risco) |
| 🛠️ Mudança nos dados ou exposição      | Reclassificar eixo D ou E; avaliar risco residual               | [Risco Residual](/sbd-toe/sbd-manual/classificacao-aplicacoes/addon/risco-residual) |
| 🧪 Revisão de arquitetura              | Aplicar avaliação semiquantitativa e validar controlo aplicado  | [Avaliação Quantitativa](/sbd-toe/sbd-manual/classificacao-aplicacoes/addon/avaliacao-semiquantitativa) |
| 🚀 Go-live                             | Validar conformidade com matriz de controlos por risco          | [Matriz de controlos por Risco](/sbd-toe/sbd-manual/classificacao-aplicacoes/addon/matriz-controlos-por-risco) |
| ⚠️ Ameaça emergente ou nova CVE        | Reavaliar criticidade e cobertura de ameaças                    | [Mapeamento Ameaças por Risco](/sbd-toe/sbd-manual/classificacao-aplicacoes/addon/mapeamento-ameacas-risco) |
| 🗓️ Decurso do tempo (cadência formal) | **Revisão periódica time-based** da classificação               | [Ciclo de Vida do Risco](/sbd-toe/sbd-manual/classificacao-aplicacoes/addon/ciclo-vida-risco) |

---

## 👥 Quem executa cada ação

| Papel Formal (07-roles.md) | Responsabilidades em Cap. 01 |
|---|---|
| **Developer** | Propor classificação inicial; registar alterações E/D/I; atualizar documentação em commits |
| **Team Lead / Scrum Master** | Facilitar integração da classificação no backlog; remover bloqueios operacionais |
| **AppSec Engineer** | Validar modelo aplicado; ajustar nível (especialmente em L2/L3); mapear ameaças; parametrizar cadência; aprovar classificações |
| **Arquitetos de Software** | Rever implicações técnicas de risco, cenários de exposição, impacto em arquitetura |
| **Product Owner** | Notificado de alterações de nível (especialmente L1→L3); aprovar impacto de negócio de exceções |
| **GRC/Compliance** | Rastreabilidade normativa; definir TTL/expiração de exceções; consolidar KPIs; auditar decisões |
| **QA** | Validar cumprimento de requisitos por nível antes do go-live; documentar evidências |
| **DevOps/SRE** | Aplicar classificação a artefactos técnicos (pipeline/IaC/imagens) nos capítulos 07/08/09 |
| **Gestão Executiva / CISO** | Aprovar políticas de classificação e aceitação de risco; supervisionar exceções em L3 |
| **Auditores Internos** | Validar aplicação efetiva de classificações; auditar rastreabilidade; produzir achados |

---

## 🛠️ User stories reutilizáveis

### US-01 – Classificação inicial da aplicação

**Contexto.**  
A classificação inicial da aplicação é o ponto de entrada para a aplicação proporcional de controlos de segurança (L1–L3). Sem este passo, não é possível garantir rastreabilidade nem proporcionalidade.

:::userstory
**História.**  
Como **Developer / Team Lead**, quero **classificar a aplicação com base nos eixos Exposição, Dados e Impacto (E+D+I)**, para garantir a aplicação proporcional de controlos de segurança ao longo de todos os capítulos.

**BDD.**
- Dado uma aplicação nova ou em início de projeto  
- Quando aplico o modelo de classificação E+D+I  
- Então obtenho uma pontuação por eixo e um nível global **L1–L3 definido, validado por AppSec Engineer e documentado**

**DoD.**
- [ ] Modelo de classificação E+D+I aplicado à aplicação  
- [ ] Nível de criticidade (L1–L3) definido e **validado por AppSec Engineer**  
- [ ] Documento de classificação registado e versionado em repositório Git  
- [ ] Controlos mínimos extraídos da matriz de risco e associados à aplicação  
- [ ] **Em L2/L3: Aprovação formal por AppSec Engineer documentada**  
- [ ] **Product Owner notificado se classificação for L3**  

:::

**Artefactos & evidências.**
- Ficheiro: `classificacao-aplicacao.yaml` — Localização: Repo `security/`  
- Ficheiro: `matriz-controlos-aplicada.md` — Evidência: Anexo ao PR ou wiki

**Proporcionalidade por risco.**
| Nível | Obrigatório? | Ajustes |
|---|---|---|
| L1 | Sim | Classificação simplificada, apenas eixos principais |
| L2 | Sim | Classificação completa com **validação formal por AppSec Engineer** |
| L3 | Sim | Classificação formal, **validada e aprovada por AppSec Engineer + GRC/Compliance** |

**Integração no SDLC.**
| Fase | Trigger | Responsáveis | SLA |
|---|---|---|---|
| Início | Kick-off / Definição de projeto | **Developer + Team Lead + AppSec Engineer** | Antes da primeira release |
| Arquitetura | Revisão de design inicial | **Developer + Arquitetura + AppSec Engineer** | Antes da aprovação de arquitetura |

**Ligações úteis.**
- [Modelo de Classificação](/docs/sbd-toe/010-sbd-manual/01-classificacao-aplicacoes/addon/01-modelo-classificacao-eixos.md)  
- [Matriz de Controlos por Risco](/docs/sbd-toe/010-sbd-manual/01-classificacao-aplicacoes/addon/05-matriz-controlos-por-risco.md)  
- [07-roles.md](/docs/sbd-toe/000-teory-of-everything/07-roles.md)

---

### US-02 – Aplicação da matriz de controlo

**Contexto.**  
A matriz de controlo define quais os requisitos de segurança aplicáveis em função do nível de risco. Sem mapeamento explícito, há risco de sobreproteção ou underprotection.

:::userstory
**História.**  
Como **Developer / Team Lead**, quero **aplicar a matriz de controlos e mapear cada requisito para REQ-XXX do Capítulo 02**, para garantir que apenas os requisitos necessários são exigidos e rastreáveis.

**BDD.**
- Dado uma aplicação já classificada (L1, L2 ou L3)  
- Quando consulto a matriz de controlos  
- Então extraio apenas os requisitos correspondentes ao nível atribuído **e mapeio cada um para REQ-XXX específico**

**DoD.**
- [ ] Matriz consultada para o nível da aplicação  
- [ ] Requisitos transformados em cartões/histórias de backlog  
- [ ] **Cada requisito mapeado explicitamente para REQ-XXX do Cap. 02** (ex: REQ-LOG-001, REQ-ARC-003)  
- [ ] Tabela de rastreamento: `controlo | L1/L2/L3 | REQ-XXX | responsável`  
- [ ] Exceções documentadas, aprovadas por AppSec Engineer com justificação técnica  
- [ ] **AppSec Engineer valida mapeamento antes de entrada em backlog**  

:::

**Artefactos & evidências.**
- Ficheiro: `matriz-controlos-aplicada.md` com rastreamento REQ-XXX  
- Localização: Backlog / Wiki / Repositório de documentação

**Proporcionalidade por risco.**
| Nível | Obrigatório? | Ajustes |
|---|---|---|
| L1 | Sim | Aplicar controlos mínimos |
| L2 | Sim | Controlos completos com rastreamento obrigatório |
| L3 | Sim | Controlos completos + reforçados + validação por AppSec |

**Integração no SDLC.**
| Fase | Trigger | Responsáveis | SLA |
|---|---|---|---|
| Planeamento | Após classificação | **Developer + Team Lead + AppSec Engineer** | Antes de implementação |

**Ligações úteis.**
- [Matriz de Controlos por Risco](/docs/sbd-toe/010-sbd-manual/01-classificacao-aplicacoes/addon/05-matriz-controlos-por-risco.md)  
- [Capítulo 02 - Requisitos de Segurança](/docs/sbd-toe/010-sbd-manual/02-requisitos-seguranca/intro.md)  
- [07-roles.md](/docs/sbd-toe/000-teory-of-everything/07-roles.md)

---

### US-03 – Revisão por alteração relevante (event-based)

**Contexto.**  
A classificação deve ser revista quando existirem alterações significativas de arquitetura, dados ou exposição. Sem revisão, mudanças lentas podem gerar desalinhamento entre nível e controlos.

:::userstory
**História.**  
Como **AppSec Engineer**, quero **rever a classificação de criticidade sempre que houver alterações relevantes**, para garantir adequação contínua dos controlos ao contexto técnico real.

**BDD.**
- Dado que ocorreu uma alteração significativa (ex: nova API, novo dado sensível, mudança de exposição)  
- Quando reviso a classificação  
- Então documento se o nível foi mantido ou alterado, com justificação técnica clara

**DoD.**
- [ ] Trigger de revisão identificado e documentado  
- [ ] Documento de classificação atualizado ou revalidado  
- [ ] Justificação técnica registada (ex: "E aumentou de 1→2 por exposição a API pública")  
- [ ] **Se nível alterou: dispara revisão de matriz (US-02) e mapeamento de ameaças (US-06)**  
- [ ] **Product Owner notificado se houver impacto de negócio** (especialmente em escalação L1→L3)  
- [ ] GRC/Compliance registra alteração em auditable trail  

:::

**Artefactos & evidências.**
- Ficheiro: `classificacao-revisao.md` ou entrada em issue tracker  
- Conteúdo: `data | trigger | nível_anterior | nível_novo | justificação | responsável`  
- Evidência: commit rastreável com assinatura, issue comentada, ou registo em GRC

**Proporcionalidade por risco.**
| Nível | Obrigatório? |
|---|---|
| L1 | Sim (por alteração relevante) |
| L2 | Sim |
| L3 | Sim |

**Integração no SDLC.**
| Fase | Trigger | Responsáveis | SLA |
|---|---|---|---|
| Contínuo | Mudança arquitetura, dados ou exposição | **AppSec Engineer + Developer + GRC/Compliance + Product Owner** | 3 dias úteis após trigger |

**Ligações úteis.**
- [Ciclo de Vida do Risco](/docs/sbd-toe/010-sbd-manual/01-classificacao-aplicacoes/addon/02-ciclo-vida-risco.md)  
- [07-roles.md](/docs/sbd-toe/000-teory-of-everything/07-roles.md)

---

### **US-07 – Revisão Periódica Time-Based da Classificação (Cadência Obrigatória)**

**Contexto.**  
Para além dos triggers por alteração, a classificação deve ter **cadência periódica fixa**. Sem calendário, mudanças lentas (ex: crescimento de dados críticos) ficam não-detetadas.

:::userstory
**História.**  
Como **AppSec Engineer**, quero **rever a classificação com cadência fixa (L1 anual, L2 semestral, L3 trimestral)**, para garantir que o nível de criticidade e os controlos continuam adequados ao contexto actual.

**BDD.**
- Dado que existe uma classificação ativa com data de próxima revisão definida  
- Quando a data de revisão chega  
- Então executo reavaliação dos eixos E/D/I, documento decisão (manter/alterar) e **agenço próxima revisão**

**DoD.**
- [ ] Calendário de revisões definido por nível (L1=12m, L2=6m, L3=3m)  
- [ ] Ata ou issue de revisão criada, datada e documentada com evidência técnica  
- [ ] Justificação: "Alterado" (com novo nível e drivers) ou "Mantém-se" (com observações)  
- [ ] Próxima data de revisão agendada e alertas configurados (em ferramenta GRC se possível)  
- [ ] **Se nível alterado: dispara US-02 (matriz) e US-06 (ameaças)**  
- [ ] **Product Owner notificado se houver impacto de negócio** (especialmente L1→L3)  
- [ ] **GRC/Compliance registra em audit trail**  

:::

**Artefactos & evidências.**
- Ficheiro: `classificacao-revisoes.md` ou entrada em ferramenta GRC  
- Tabela: `data_revisao | nível_anterior | nível_novo | justificação | próxima_data | responsável`  
- Evidência: issue rastreável datada, commit versionado, ou registo auditable

**Proporcionalidade (cadência típica).**
| Nível | Frequência sugerida | Obrigatório? |
|---|---|---|
| L1 | 12 meses | Recomendado |
| L2 | 6 meses | Obrigatório |
| L3 | 3 meses (ou por sprint) | Obrigatório |

**Integração no SDLC.**
| Fase | Trigger | Responsáveis | SLA |
|---|---|---|---|
| Operações + Governação | Calendário time-based + Eventos críticos | **AppSec Engineer + GRC/Compliance + Product Owner** | Conclusão em 5 dias úteis da data de revisão |

**Ligações úteis.**
- [Ciclo de Vida do Risco](/docs/sbd-toe/010-sbd-manual/01-classificacao-aplicacoes/addon/02-ciclo-vida-risco.md)  
- [Critérios Aceitação Risco](/docs/sbd-toe/010-sbd-manual/01-classificacao-aplicacoes/addon/03-criterios-aceitacao-risco.md)  
- [07-roles.md](/docs/sbd-toe/000-teory-of-everything/07-roles.md)

---

### US-04 – Análise de risco residual

**Contexto.**  
Mesmo após aplicação da matriz, podem permanecer riscos residuais que devem ser documentados, quantificados e aprovados formalmente. Sem análise residual, exceções ficam sem justificação técnica clara.

:::userstory
**História.**  
Como **GRC/Compliance**, quero **registar o risco residual após aplicar os controlos definidos**, para fundamentar decisões de aceitação, mitigação ou transferência de risco.

**BDD.**
- Dado que alguns controlos não são aplicáveis ou foram excecionados  
- Quando documento as justificações técnicas e avalio risco residual  
- Então registo a análise de forma auditável com **aprovação de AppSec Engineer e Gestão**

**DoD.**
- [ ] Controlos não aplicados identificados explicitamente  
- [ ] Justificação técnica detalhada registada (ex: "Requisito X não aplicável porque Y")  
- [ ] **Risco residual avaliado contra limiares L1–L3** (ex: L2 máximo = risco médio)  
- [ ] **Aprovação formal por AppSec Engineer documentada**  
- [ ] **Em L3: aprovação adicional por Gestão Executiva/CISO**  
- [ ] Entrada em ferramenta GRC com audit trail  

:::

**Artefactos & evidências.**
- Ficheiro: `risco-residual.md` ou entrada em ferramenta GRC  
- Conteúdo: `id | controlo_não_aplicado | justificação | risco_residual | aprovadores | data`  
- Evidência: assinatura digital, email de aprovação, ou registo versionado

> **Referência:** Este US implementa [Cap 14-US-01: Processo formal de exceções]
> no contexto de análise de risco residual. A aprovação formal e o TTL das exceções devem seguir a política master definida em Cap 14.

**Proporcionalidade por risco.**
| L1 | L2 | L3 |
|----|----|----|
| Opcional (se crítico) | Obrigatório | Obrigatório |

**Integração no SDLC.**
| Fase | Trigger | Responsáveis | SLA |
|---|---|---|---|
| Validação | Após mapeamento de matrix; pré-release | **GRC/Compliance + AppSec Engineer + Developer** | 5 dias úteis |

**Ligações úteis.**
- [Risco Residual](/docs/sbd-toe/010-sbd-manual/01-classificacao-aplicacoes/addon/04-risco-residual.md)  
- [Critérios Aceitação Risco](/docs/sbd-toe/010-sbd-manual/01-classificacao-aplicacoes/addon/03-criterios-aceitacao-risco.md)  
- [07-roles.md](/docs/sbd-toe/000-teory-of-everything/07-roles.md)

---

### **US-08 – Aceitação de Risco com TTL e Revalidação Obrigatória**

**Contexto.**  
Quando o nível de risco residual é aceitável mas com **Time-To-Live (TTL) limitado**, o risco pode expirar. Sem revalidação automática, excepções "dormem" indefinidamente.

:::userstory
**História.**  
Como **GRC/Compliance**, quero registar aceitações com **TTL explícito e alerta de re-aprovação**, para garantir que excepções não se tornam permanentes por esquecimento.

**BDD.**
- Dado que existe uma decisão de aceitar risco residual  
- Quando defino **TTL em função do nível** (L1=12m, L2=6m, L3=3m)  
- Então configuro alerta de **revalidação 15 dias antes da expiração**  
- E documento que **sem re-aprovação explícita, a excepção expira automaticamente**

**DoD.**
- [ ] Owner da excepção designado e contactível  
- [ ] **TTL definido por nível** (L1: 12 meses | L2: 6 meses | L3: 3 meses)  
- [ ] Critérios de encerramento claros (ex: "após implementação mitigação X" ou "até data Y")  
- [ ] **Alertas configurados 15 dias antes da expiração** (email ou issue automática)  
- [ ] Registo rastreável em ferramenta GRC ou repositório (com data e decisor)  
- [ ] **Re-aprovação explícita exigida para prorrogação** (mesmo critério de aprovação original)  
- [ ] **Em L3: aprovação adicional por Gestão Executiva/CISO antes de renovação**  
- [ ] **Se biz impact relevante: Product Owner notificado e de acordo**  

:::

**Artefactos & evidências.**
- Ficheiro: `aceitacoes-risco.md` ou entrada em ferramenta GRC/JIRA  
- Tabela: `excepção_id | L1/L2/L3 | data_aceitação | TTL | data_expiração | owner | critério_encerramento | status`  
- Evidência: aprovação datada, alerta de expiração, re-aprovação documentada ou registo de encerramento

**Proporcionalidade (TTL por nível).**
| Nível | TTL Recomendado | Revalidação | Obrigatório? |
|---|---|---|---|
| L1 | 12 meses | Anual | Recomendado |
| L2 | 6 meses | Semestral | Obrigatório |
| L3 | 3 meses | Trimestral | **Obrigatório + Gestão Executiva** |

**Integração no SDLC.**
| Fase | Trigger | Responsáveis | SLA |
|---|---|---|---|
| Governação + Segurança | Decisão de aceitar risco; alerta 15d antes expiração | **GRC/Compliance (cria, registra) + AppSec Engineer (revalida, aprova) + Gestão Executiva/CISO (aprova L3) + Product Owner (notificado se impacto negócio)** | Criação: 2 dias úteis; Re-aprovação: 5 dias úteis antes da expiração |

**Ligações úteis.**
- [Critérios Aceitação Risco](/docs/sbd-toe/010-sbd-manual/01-classificacao-aplicacoes/addon/03-criterios-aceitacao-risco.md)  
- [Análise de Risco Residual](/docs/sbd-toe/010-sbd-manual/01-classificacao-aplicacoes/aplicacao-lifecycle.md#us-04--análise-de-risco-residual)  
- [07-roles.md](/docs/sbd-toe/000-teory-of-everything/07-roles.md)

---

### US-05 – Validação antes do go-live

**Contexto.**  
Antes de entrar em produção é necessário validar se todos os requisitos aplicáveis foram cumpridos. Esta etapa impede deployes com cobertura de segurança incompleta.

:::userstory
**História.**  
Como **QA**, quero **validar que os requisitos aplicáveis por nível de risco estão cumpridos antes da entrada em produção**, para garantir conformidade com a classificação atribuída.

**BDD.**
- Dado que a aplicação está pronta para go-live  
- Quando reviso a checklist de controlos aplicáveis (extraída de US-02)  
- Então confirmo que **evidências estão documentadas, testadas e aprovadas por AppSec Engineer**

**DoD.**
- [ ] Checklist de controlos revista completa (baseada em matriz aplicada)  
- [ ] Evidências documentadas (testes, relatórios, scans, revisões)  
- [ ] **Aprovação formal de AppSec Engineer registada**  
- [ ] **Em L3: aprovação adicional por Gestão/PMO ou CISO**  
- [ ] Nenhuma exceção não-aprovada pendente  
- [ ] Rastreamento: cada controlo ↔ evidência documentado  

:::

**Artefactos & evidências.**
- Ficheiro: `checklist-go-live.md` ou entrada em pipeline CI/CD  
- Conteúdo: `controlo | L1/L2/L3 | evidência | aprovação_AppSec | status_go_live`  
- Evidência: log de aprovação em pipeline, assinatura em documento, ou registo em GRC

**Proporcionalidade por risco.**
| L1 | L2 | L3 |
|----|----|----|
| Recomendado | Recomendado (obrigatório) | Obrigatório (formal + assinatura) |

**Integração no SDLC.**
| Fase | Trigger | Responsáveis | SLA |
|---|---|---|---|
| Pré-Release | Aplicação pronta para go-live | **QA + AppSec Engineer + Gestão/PMO (L3)** | 2 dias úteis antes de deploy |

**Ligações úteis.**
- [Matriz de Controlos por Risco](/docs/sbd-toe/010-sbd-manual/01-classificacao-aplicacoes/addon/05-matriz-controlos-por-risco.md)  
- [07-roles.md](/docs/sbd-toe/000-teory-of-everything/07-roles.md)

## 🚧 Cascata de Gates de Validação (US-05 em Contexto)

A validação antes do go-live é implementada através de uma **cascata de gates sequenciais**, cada um verificando dimensões específicas de segurança em capítulos distintos. A falha em qualquer gate bloqueia promoção a produção.

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                                                                                 │
│  APLICAÇÃO PRONTA PARA RELEASE                                                  │
│  └─ Trigger: Pipeline de promoção a staging/produção                            │
│                                                                                 │
│                                       ▼                                         │
│  ┌───────────────────────────────────────────────────────────────────────────┐  │
│  │ GATE 1: Requisitos & Risco (Cap 01)                                      │  │
│  │ Responsável: QA + AppSec Engineer                                        │  │
│  │ Validação:                                                               │  │
│  │   ✓ Classificação de risco atribuída (L1/L2/L3)                          │  │
│  │   ✓ Matriz de controlos aplicáveis extraída                             │  │
│  │   ✓ Ameaças esperadas mapeadas (STRIDE, MITRE ATT&CK)                   │  │
│  │   ✓ Nenhuma exceção de risco residual não-aprovada pendente             │  │
│  │ Bloqueio se: Risco residual > threshold aprovado ou exceções pendentes   │  │
│  └─────────────┬──────────────────────────────────────────────────────────┘   │
│               ▼                                                                │
│  ┌───────────────────────────────────────────────────────────────────────────┐  │
│  │ GATE 2: Requisitos de Segurança (Cap 02)                                 │  │
│  │ Responsável: AppSec Engineer                                             │  │
│  │ Validação:                                                               │  │
│  │   ✓ Requisitos funcionalidade + segurança completos                      │  │
│  │   ✓ Gestão de exceções: todas as exceções têm aprovação + SLA            │  │
│  │   ✓ Rastreamento requisito ↔ teste ↔ evidência completo                 │  │
│  │ Bloqueio se: Requisitos incompletos ou exceções sem aprovação            │  │
│  └─────────────┬──────────────────────────────────────────────────────────┘   │
│               ▼                                                                │
│  ┌───────────────────────────────────────────────────────────────────────────┐  │
│  │ GATE 3: Dependências & SBOM (Cap 05)                                     │  │
│  │ Responsável: DevOps + AppSec Engineer                                    │  │
│  │ Validação:                                                               │  │
│  │   ✓ SBOM completo em CycloneDX/SPDX (todas as dependências listadas)     │  │
│  │   ✓ Scan de vulnerabilidades: nenhuma crítica não-mitigada em L2/L3      │  │
│  │   ✓ CVEs com risco > threshold têm mitigação/exceção documentada         │  │
│  │   ✓ Dependências verificadas em repositórios de reputação                │  │
│  │ Bloqueio se: CVE crítico não-mitigado ou SBOM incompleto                 │  │
│  └─────────────┬──────────────────────────────────────────────────────────┘   │
│               ▼                                                                │
│  ┌───────────────────────────────────────────────────────────────────────────┐  │
│  │ GATE 4: Artefactos CI/CD (Cap 07)                                        │  │
│  │ Responsável: DevOps + AppSec Engineer                                    │  │
│  │ Validação:                                                               │  │
│  │   ✓ Pipeline CI/CD: versionado, auditado, secrets em manager            │  │
│  │   ✓ Assinatura & proveniência de artefactos (in-toto, Cosign)            │  │
│  │   ✓ Testes de segurança integrados (SAST, dependency scanning, SBOM)     │  │
│  │   ✓ Logs de auditoria de cada deploy recolhidos e retidos                │  │
│  │ Bloqueio se: Pipeline não-auditado ou artefactos não-assinados           │  │
│  └─────────────┬──────────────────────────────────────────────────────────┘   │
│               ▼                                                                │
│  ┌───────────────────────────────────────────────────────────────────────────┐  │
│  │ GATE 5: Infraestrutura & Containers (Cap 08/09)                          │  │
│  │ Responsável: DevOps + Arquitetos                                         │  │
│  │ Validação:                                                               │  │
│  │   ✓ IaC versionado, aprovado, testado (Terraform, Helm, CloudFormation) │  │
│  │   ✓ Imagens container: base segura, SBOM, scanning, assinadas           │  │
│  │   ✓ Policies de runtime (OPA/Kyverno) ativas e bloqueantes em L2/L3     │  │
│  │   ✓ Network policies e RBAC configurados                                 │  │
│  │ Bloqueio se: Imagem não-assinada ou policies não-ativas                  │  │
│  └─────────────┬──────────────────────────────────────────────────────────┘   │
│               ▼                                                                │
│  ┌───────────────────────────────────────────────────────────────────────────┐  │
│  │ GATE 6: Deploy & Monitorização (Cap 11/12)                               │  │
│  │ Responsável: DevOps + AppSec Engineer + SRE                              │  │
│  │ Validação:                                                               │  │
│  │   ✓ Apenas artefactos assinados são promovidos                           │  │
│  │   ✓ Ambiente staging validado (testes + aprovações concluídas)           │  │
│  │   ✓ Monitorização + alertas ativados pré-deploy (logs, métricas, eventos)│  │
│  │   ✓ Playbook de incidentes documentado e testado                         │  │
│  │   ✓ Aprovação formal registada (assinatura, timestamp, audit trail)      │  │
│  │ Bloqueio se: Monitorização não-ativa ou aprovação não-documentada        │  │
│  └─────────────┬──────────────────────────────────────────────────────────┘   │
│               ▼                                                                │
│  ✅ DEPLOY EM PRODUÇÃO AUTORIZADO                                             │
│     └─ Timestamp de aprovação registado em audit trail central (Cap 14)       │
│                                                                                │
└─────────────────────────────────────────────────────────────────────────────────┘
```

**Características Críticas da Cascata:**
- **Sequencial:** Cada gate é pré-requisito para o próximo (falha em gate N bloqueia gate N+1)
- **Distribuído:** Cada gate é propriedade de capítulo específico, mas supervisionado por AppSec centralizado (Cap 14)
- **Auditável:** Todas as decisões e aprovações são registadas com timestamp e responsável
- **Proporcional:** L1 pode ter gates mais leves (audit mode), L2/L3 são bloqueantes (enforce mode)
- **Rastreável:** Gate 6 (Cap 11/12) alimenta matriz de rastreamento em Cap 14 para evidência de conformidade

---

### US-06 – Mapeamento de ameaças por nível de risco


**Contexto.**  
Cada nível de criticidade deve ser confrontado com ameaças conhecidas (STRIDE, MITRE ATT&CK) para validar que a cobertura de controlos é adequada. Sem mapeamento, seleção de controlos fica ad-hoc.

:::userstory
**História.**  
Como **AppSec Engineer**, quero **verificar se as ameaças esperadas para o nível de criticidade estão cobertas por controlos aplicados ou exceções rastreáveis**, para garantir que a seleção de controlos é fundamentada em ameaças reais.

**BDD.**
- Dado que a aplicação tem nível de criticidade definido (L1/L2/L3)  
- Quando consulto o mapeamento de ameaças apropriado (STRIDE, MITRE ATT&CK)  
- Então verifico que **todas as ameaças críticas têm cobertura por controlo ou exceção documentada**

**DoD.**
- [ ] Ameaças identificadas por nível (ex: STRIDE para L1, MITRE ATT&CK para L2/L3)  
- [ ] **Mapeamento ameaça ↔ controlo documentado** (ex: Spoofing → MFA, Tampering → TLS)  
- [ ] Cobertura validada por controlo aplicado ou exceção aprovada  
- [ ] **Arquitetos envolvidos para validação de contexto técnico**  
- [ ] Resultados registados e rastreáveis  
- [ ] **Se ameaça crítica não coberta: dispara US-04 (risco residual) ou mitigação obrigatória**  

:::

**Artefactos & evidências.**
- Ficheiro: `ameacas-mapeamento.md` com tabela: `ameaca | categoria | controlo_aplicado | cobertura_sim_nao | exceção`  
- Localização: Repo documentação de segurança  
- Evidência: rastreamento em Jira/backlog, validação por AppSec + Arquitetos

**Proporcionalidade por risco.**
| L1 | L2 | L3 |
|----|----|----|
| Opcional (STRIDE básico) | Recomendado (STRIDE completo) | Obrigatório (STRIDE + MITRE ATT&CK) |

**Integração no SDLC.**
| Fase | Trigger | Responsáveis | SLA |
|---|---|---|---|
| Design | Após arquitetura definida | **AppSec Engineer + Arquitetos + Developer** | Antes de dev começar |
| Validação | Pré-release (L2/L3) | **AppSec Engineer** | 1 semana antes de release |

**Ligações úteis.**
- [Mapeamento de Ameaças por Risco](/docs/sbd-toe/010-sbd-manual/01-classificacao-aplicacoes/addon/06-mapeamento-ameacas-risco.md)  
- [Capítulo 03 - Threat Modeling](/docs/sbd-toe/010-sbd-manual/03-threat-modeling/intro.md)  
- [07-roles.md](/docs/sbd-toe/000-teory-of-everything/07-roles.md)

---

### **US-09 – Classificação de Artefactos Técnicos (Pipeline, IaC, Imagens)**

**Contexto.**  
A classificação da aplicação não é suficiente; **artefactos de entrega** (Dockerfile, scripts CI/CD, IaC, imagens) herdam a criticidade e exigem controlos específicos descritos nos capítulos 07 (CI/CD Seguro), 08 (IaC), 09 (Containers).

:::userstory
**História.**  
Como **DevOps/SRE**, quero classificar **artefactos técnicos da aplicação** (Dockerfile, pipeline, IaC, imagens) com a mesma criticidade, para garantir que controlos de segurança acompanham a integridade da entrega.

**BDD.**
- Dado que uma aplicação tem uma classificação L1/L2/L3  
- Quando crio/reviso artefactos de entrega (Dockerfile, script CI/CD, manifesto IaC, imagem)  
- Então aplico os **controlos de capítulos 07/08/09 equivalentes ao nível**  
- E documento **rastreabilidade: aplicação → artefacto → capítulo 07/08/09 → REQ-XXX**

**DoD.**
- [ ] Artefactos técnicos identificados (Dockerfile, pipeline/GitHub Actions/GitLab CI, Terraform/Helm, imagem registada)  
- [ ] **Classificação do artefacto registada = classificação da aplicação** (ex: L3 app → L3 Dockerfile, L3 pipeline)  
- [ ] **Controlos cap. 07 (CI/CD) aplicados se pipeline** (secrets manager, assinatura, scanning, audit log)  
- [ ] **Controlos cap. 08 (IaC) aplicados se infraestrutura-as-code** (versionamento, revisão rigorosa, scanning, tags)  
- [ ] **Controlos cap. 09 (Containers) aplicados se imagem Docker** (base image segura, scanning vulnerabilidades, runtime policy, registry autenticação)  
- [ ] **Tabela de rastreamento: artefacto | nível | capítulo | REQ-XXX | responsável | status**  
- [ ] **Arquitetos valida alinhamento entre controlos do artefacto e necessidades da aplicação**  
- [ ] **AppSec Engineer aprova antes do deploy**  

:::

**Artefactos & evidências.**
- Ficheiro: `artefactos-tecnicos.md` ou tabela em repositório  
- Tabela: `artefacto | nível | tipo (Dockerfile/pipeline/IaC) | capítulo | REQ-XXX | status | owner`  
- Evidência: commit com tags de classificação, issue rastreável, scan report, approval email

**Proporcionalidade (por tipo de artefacto).**
| Artefacto | Cap. Aplicável | L1 (Recomendado) | L2 (Obrigatório) | L3 (Reforçado) |
|---|---|---|---|---|
| Dockerfile | 09 | Base segura | Full hardening + scanning | Base segura auditada, scanning automático, registry private |
| Pipeline (GH/GL/Jenkins) | 07 | Secrets em variables | Secrets em KV, audit log, SAST | Secrets em KV, audit log, SAST+DAST, assinatura imagem, 2FA |
| IaC (Terraform/Helm) | 08 | Versionamento | Versionamento + review | Versionamento + review rigorosa + compliance scanning |
| Imagem registada | 09 | Versão explícita | Scan vulnerabilidades | Scan + runtime policy + image signing |

**Integração no SDLC.**
| Fase | Trigger | Responsáveis | SLA |
|---|---|---|---|
| Construção + Entrega | Criação/atualização de artefacto | **DevOps/SRE (proprietário, implementa controlos) + Arquitetos (valida alinhamento) + AppSec Engineer (aprova)** | Approval antes de deploy: 2 dias úteis |

**Ligações úteis.**
- [Cap. 07 - CI/CD Seguro](/docs/sbd-toe/010-sbd-manual/07-cicd-seguro/)  
- [Cap. 08 - IaC e Infraestrutura](/docs/sbd-toe/010-sbd-manual/08-iac-infraestrutura/)  
- [Cap. 09 - Containers e Imagens](/docs/sbd-toe/010-sbd-manual/09-containers-imagens/)  
- [07-roles.md](/docs/sbd-toe/000-teory-of-everything/07-roles.md)

---

### **US-10 – KPIs, Métricas e Reporting de Classificação e Conformidade**

**Contexto.**  
Sem indicadores e visibilidade executiva, não há governança efetiva nem feedback loop para melhoria contínua. É necessário consolidar métricas operacionais e de conformidade sobre o ciclo de classificação.

:::userstory
**História.**  
Como **GRC/Compliance**, quero consolidar **KPIs mensais/trimestrais** sobre a classificação, exceções e ciclos de revisão, para demonstrar maturidade de governação à **Gestão Executiva/CISO** e à **Auditoria**.

**BDD.**
- Dado que existem classificações, exceções, revisões e artefactos registados  
- Quando consolido os dados mensalmente  
- Então gero relatório com **KPIs por nível, tendências, alertas de conformidade e recomendações**  
- E distribuo a **Gestão Executiva/CISO + Auditores Internos**

**DoD.**
- [ ] **KPI 1: % de aplicações classificadas** (válidas com data de revisão/revalidação próxima)  
- [ ] **KPI 2: % de exceções ainda ativas** vs **% expiradas ou prorrogadas** (por nível)  
- [ ] **KPI 3: Lead time para classificação inicial** (dias desde criação até L1/L2/L3 atribuído)  
- [ ] **KPI 4: Lead time para revisão** (dias desde trigger até decisão final)  
- [ ] **KPI 5: Conformidade a cadência de revisão** (% de app L2/L3 revistos no prazo 6m/3m)  
- [ ] **KPI 6: % de controlos mapeados** (aplicações com todos os REQ-XXX do nível implementados ou com excepção TTL válida)  
- [ ] **KPI 7: Ameaças críticas não cobertas** (número e lista de aplicações com risco crítico residual)  
- [ ] **Série temporal (trend)**: Gráficos de KPI 1–7 dos últimos 6 meses  
- [ ] **Alertas automáticos**: Notificação se KPI 2 (exceções expiradas) > 5%, KPI 5 (conformidade) < 90%  
- [ ] **Fonte única de dados**: Ferramenta GRC, repositório, ou dashboard integrado (com rastreabilidade a aplicação original)  
- [ ] **Reporte trimestral** assinado por **GRC/Compliance**, distribuído a **Gestão Executiva/CISO + Auditores**  
- [ ] **Recomendações actionáveis**: Top 3 causas de atraso ou não-conformidade + plano de ação  

:::

**Artefactos & evidências.**
- Ficheiro: `kpi-classificacao-YYYY-MM.md` ou entrada em ferramenta BI/dashboard  
- Tabela: `data | KPI | valor | meta | % conformidade | tendência | alertas`  
- Evidência: reporte PDF/markdown datado, distribuição de email, apresentação a Gestão Executiva, registo de auditoria

**Proporcionalidade (reporte por nível de detalhe).**
| Audiência | Frequência | KPIs mínimos | Formato |
|---|---|---|---|
| **Operações/AppSec** | Semanal (opcional) | % classified, exceções próximas de expirar, atrasos revisão | Dashboard interno |
| **Product Owners** | Mensal | % classified (por negócio/squad), lead time, exceções de app |  Email com resumo ou Slack |
| **Gestão Executiva/CISO** | Trimestral | KPI 1,2,5,6,7; alertas críticos; recomendações | PDF formal com gráficos |
| **Auditores Internos** | Anual + ad-hoc | Série completa KPI 1-7; conformidade a regulamentos; draft policies; lista de exceções | PDF + acesso a repositório versionado |

**Integração no SDLC.**
| Fase | Trigger | Responsáveis | SLA |
|---|---|---|---|
| Governação + Reporting | Fim de período (mensal/trimestral) | **GRC/Compliance (coleta dados, consolida, redige) + AppSec Engineer (valida métricas técnicas) + Gestão Executiva/CISO (aprova distribuição)** | Reporte: 10 dias úteis após fim do período; Distribuição: 1 dia após aprovação |

**Ligações úteis.**
- [Critérios Aceitação Risco](/docs/sbd-toe/010-sbd-manual/01-classificacao-aplicacoes/addon/03-criterios-aceitacao-risco.md)  
- [Mapeamento de Ameaças](/docs/sbd-toe/010-sbd-manual/01-classificacao-aplicacoes/addon/06-mapeamento-ameacas-risco.md)  
- [07-roles.md](/docs/sbd-toe/000-teory-of-everything/07-roles.md)  
- [Auditoría & Rastreabilidade (Cap. 02)](/docs/sbd-toe/010-sbd-manual/02-requisitos-seguranca/intro.md)

---

### **US-11 – Políticas Organizacionais Formais (Classificação, Risco, Revisão Periódica, Rastreabilidade)**

**Contexto.**  
As user stories US-01 a US-10 definem o **como operacionalizar** a classificação. As políticas organizacionais definem o **por quê** (mandato), **quem aprova**, **qual o critério** e **como auditar**. Sem políticas, não há governança formal nem conformidade a regulamentos (NIS2, DORA, ISO 27001).

:::userstory
**História.**  
Como **Gestão Executiva/CISO**, quero que existam **4 políticas organizacionais formais aprovadas** (Classificação de Risco, Aceitação de Risco, Revisão Periódica, Rastreabilidade/Auditoria), para assegurar que **todas as equipas operam sob os mesmos critérios** e que o manual é **cumprido uniformemente e auditado**.

**BDD.**
- Dado que a organização necessita de **conformidade formal** a regulamentos (NIS2, DORA, ISO 27001)  
- Quando publico 4 políticas organizacionais assinadas por **Gestão Executiva**  
- E treinamento obrigatório é documentado com **attestation** de compreensão  
- Então **Auditores podem validar conformidade** e **todas as decisões de classificação/risco têm fundamento normativo**

**DoD.**
- [ ] **Política 1 – Classificação de Risco**: Modelo E+D+I, critérios L1/L2/L3, responsabilidades por nível, frequency de revisão (obrigatória em L2/L3)  
- [ ] **Política 2 – Aceitação de Risco**: Critérios de aceitabilidade, TTL por nível, aprovadores, exceções + revalidação obrigatória antes da expiração  
- [ ] **Política 3 – Revisão Periódica**: Cadência time-based (12m/6m/3m), owners, escalada de decisões, triggers para revisão de matriz e ameaças  
- [ ] **Política 4 – Rastreabilidade & Auditoria**: Registo centralizado de classificações, exceções, revisões; versionamento; pista de auditoria; retenção de dados; acesso restrito  
- [ ] **Cada política contém**: objetivo, âmbito, responsáveis, critérios decisão, processo aprovação, frequência revisão, ligação a capítulos do manual  
- [ ] **Assinatura formal** por **Gestão Executiva/CISO** e **GRC/Compliance** datada  
- [ ] **Publicação acessível** em Wiki interna, repositório de políticas, ou portal de compliance  
- [ ] **Treinamento obrigatório** para **todas as equipas** (Dev, AppSec, GRC, Gestão, Auditores) com **attestation de participação + quiz de compreensão**  
- [ ] **Revisão anual** por **GRC/Compliance + Auditores Internos** com registo de qualquer alteração  
- [ ] **Evidência de conformidade**: Checklist de cada aplicação validando aderência às 4 políticas (L1/L2/L3)  

:::

**Artefactos & evidências.**
- Ficheiro: `POLITICA-01-classificacao-risco.md`, `POLITICA-02-aceitacao-risco.md`, `POLITICA-03-revisao-periodica.md`, `POLITICA-04-rastreabilidade-auditoria.md`  
- Local: Wiki institucional, Repositório `docs/policies/` ou servidor de compliance  
- Evidência: PDF assinado, data/versão, distribuição de email, registo de treinamento (nome+data+assinatura), quiz scores, auditoria anual  

**Proporcionalidade (aplicação por nível).**
| Nível | Classificação | Aceitação | Revisão Periódica | Rastreabilidade |
|---|---|---|---|---|
| L1 | Recomendado (simplificado) | Recomendado | Recomendado (anual) | Recomendado |
| L2 | Obrigatório (completo) | Obrigatório + TTL | Obrigatório (semestral) | Obrigatório + audit trail |
| L3 | Obrigatório (formal com aprovações) | Obrigatório + TTL + re-aprovação Gestão | Obrigatório (trimestral) | Obrigatório + rastreamento granular |

**Integração no SDLC.**
| Fase | Trigger | Responsáveis | SLA |
|---|---|---|---|
| Governação + Conformidade | Kick-off (criação políticas), anualmente (revisão) | **Gestão Executiva/CISO (assina, aprova) + GRC/Compliance (redige, distribui, treina) + AppSec Engineer (input técnico) + Auditores Internos (valida conformidade) + Todos os equipas (treino + attestation)** | Redação: 30 dias; Assinatura: 5 dias; Distribuição: 1 dia; Treinamento inicial: 10 dias; Revisão anual: 15 dias |

**Ligações úteis.**
- [Intro Cap. 01 – Modelo E+D+I e Ciclos](/docs/sbd-toe/010-sbd-manual/01-classificacao-aplicacoes/intro.md)  
- [Criterios Aceitação Risco (addon 03)](/docs/sbd-toe/010-sbd-manual/01-classificacao-aplicacoes/addon/03-criterios-aceitacao-risco.md)  
- [Ciclo de Vida do Risco (addon 02)](/docs/sbd-toe/010-sbd-manual/01-classificacao-aplicacoes/addon/02-ciclo-vida-risco.md)  
- [NIS2 / DORA / ISO 27001 (Cap. 002)](/docs/sbd-toe/002-cross-check-normativo/intro.md)  
- [07-roles.md](/docs/sbd-toe/000-teory-of-everything/07-roles.md)

---

## 📑 Artefactos esperados (por fase)

| Fase         | Artefacto                          | Quem produz         | Onde fica                  | Evidência mínima                              |
|--------------|------------------------------------|---------------------|----------------------------|-----------------------------------------------|
| Início       | `classificacao-aplicacao.yaml`     | Developer / Team Lead     | Repo `security/`           | Commit + revisão AppSec Engineer |
| Planeamento  | `matriz-controlos.md`              | Developer / Team Lead     | Backlog / wiki             | REQ-XXX referenciados (Cap. 02); aprovado AppSec |
| Revisão      | `classificacao-revisao.md`         | AppSec Engineer      | Repo `docs/`               | Issue/ata datada; decisão justificada |
| Release      | `checklist-go-live.md`             | QA                  | Pipeline CI/CD             | Aprovação formal AppSec Engineer + Gestão (L3) |
| Operação     | `risco-residual.md`                | GRC/Compliance    | Ferramenta GRC / repo      | Owner + TTL + critérios encerramento; aprovação |
| Periódico    | `classificacao-revisao-anual.md` (L1), `semestral.md` (L2), `trimestral.md` (L3) | AppSec Engineer + GRC/Compliance | Repo docs / GRC | Data revisão, justificação manter/alterar, próxima data |
| Aceitação    | `aceitacoes-risco.md` com TTL      | GRC/Compliance    | Ferramenta GRC / repo      | TTL definido, owner, critério encerramento, alertas |
| Artefactos   | `artefactos-tecnicos.md`           | DevOps/SRE + Arquitetos | Repo `platform/docs` | Classificação por artefacto, rastreamento REQ, aprovação AppSec |
| Contínuo     | `kpi-classificacao-YYYY-MM.md`    | GRC/Compliance    | Dashboard / Repositório de reporting | KPI 1-7, série temporal, alertas, recomendações |
| Governação   | `politicas-organizacionais.md` (4 políticas) | GRC/Compliance + AppSec | Docs / Wiki / Política | Aprovação Gestão Executiva, treinamento + attestation, auditoria |

> **Formato canónico de evidência** (sugestão): `id`, `data`, `eixos` (E/D/I), `nível`, `decisão`, `owner`, `ligações` (issues/PRs), `aprovadores`, `expiração` (se aplicável).

---

## 📊 Matriz de proporcionalidade L1–L3

| Prática / Story                                 | L1 | L2 | L3 | Observações |
|-------------------------------------------------|----|----|----|-------------|
| US-01 – Classificação inicial                    | ✔  | ✔  | ✔  | Validação AppSec obrigatória em L2/L3 |
| US-02 – Aplicação da matriz (c/ REQ-XXX)        | ✔  | ✔  | ✔  | Rastreabilidade REQ para Cap. 02 |
| US-03 – Revisão por alteração relevante          | ✔  | ✔  | ✔  | Event-based, cascata a US-02/US-06 |
| **US-07-rev – Revisão periódica time-based**    | ✔ (Rec.) | ✔  | ✔  | Cadência: 12m / 6m / 3m (obrigatória em L2/L3) |
| US-04 – Risco residual                           | (opcional) | ✔ | ✔  | Aprovações formais em L3 |
| **US-08-rev – Aceitação com TTL**                | (Rec.) | ✔ | ✔  | TTL 12m/6m/3m; re-aprovação obrigatória em L2/L3 |
| US-05 – Validação go-live                        | (Rec.) | ✔ | ✔  | Aprovação AppSec + Gestão em L3 |
| US-06 – Mapeamento de ameaças                    | (opcional) | ✔ | ✔  | Validação Arquitetos; escala de risco crítico |
| US-09 – Classificação de artefactos técnicos    | ✔ (Rec.) | ✔ | ✔  | Aplica controlos Cap. 07/08/09; Arquitetos valida |
| **US-11 – Políticas Organizacionais Formais**   | (Rec.) | ✔ | ✔  | 4 políticas obrigatórias em L2/L3; treinamento + auditoria |
| **US-10 – KPIs e Reporting**                    | (Rec.) | ✔ | ✔  | Mensal (ops), trimestral (gestão), anual (auditores) |

---

## 📝 Recomendações operacionais

- Integrar a classificação de risco desde o **kick-off** do projeto.  
- Reavaliar a classificação **por alteração** e **por calendário** (time-based).  
- Manter a documentação **versionada e rastreável** em repositório controlado.  
- Mapear requisitos diretamente para **REQ-XXX (Cap. 02)** no backlog.  
- Exigir **TTL/expiração** em todas as aceitações de risco.  
- Validar proporcionalidade no go-live e documentar evidências.  
- Consolidar **KPIs** organizacionais para *compliance* e melhoria contínua.  
- Alinhar práticas com as **políticas organizacionais** de classificação, exceções e revisão periódica.

