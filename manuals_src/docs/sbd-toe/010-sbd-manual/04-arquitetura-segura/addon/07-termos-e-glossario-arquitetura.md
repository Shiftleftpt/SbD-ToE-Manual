id: termos-e-glossario-arquitetura
title: Glossário Operacional
description: Termos usados no Capítulo 04 com definições operacionais e artefactos associados
tags: [tipo:addon, jargao, arquitetura-segura, rastreabilidade, adr, threat-modeling, trust-boundaries]
sidebar_position: 7
template: sbdtoe-addon
---

> Este **glossário operacional** normaliza o vocabulário usado no Cap. 04 e nos seus artefactos    
> **Objetivo:** garantir que termos críticos têm significado único, aplicação clara e ligação a evidências.

---

## 🧭 Contexto: Arquitetura como prática, não como cargo

Nem todas as equipas que aplicam o SbD-ToE têm uma função formal de *Arquiteto*.  
Em muitos projetos, **a arquitetura “acontece” naturalmente** — nas decisões tomadas durante o desenho e implementação do software.  
O Capítulo 4 parte deste princípio: não é preciso instituir um processo pesado ou um órgão de governação; basta **tornar explícitas e rastreáveis as decisões técnicas que já existem**.
Para tal é necessário adoptar uma taxonomia comum que permita a partilha de informação e conhecimento e assim possivel de aplicar nas atividades embebidas neste capitulo.

- **A arquitetura segura é uma prática coletiva.**  
  Qualquer decisão técnica que afete segurança, escalabilidade ou dependências é, na prática, uma decisão arquitetural — mesmo que tomada por um developer.

- **O objetivo é capturar raciocínio, não criar burocracia.**  
  Um *Architecture Decision Record* (ADR), uma ficha de arquitetura ou um *trust boundary* são apenas mecanismos para guardar o “porquê” técnico das escolhas feitas.

- **A formalidade cresce com o risco.**  
  O SbD-ToE não impõe formato; define proporcionalidade:  
  - *L1*: registos simples em Markdown ou tickets.  
  - *L2*: rastreabilidade completa (decisão ↔ requisito ↔ controlo).  
  - *L3*: processo formal com revisão independente.

- **Desenhar com consciência é desenhar seguro.**  
  O capítulo não cria nova documentação, mas ajuda a transformar o design implícito em **evidência verificável de segurança**.

> 💬 Em resumo: *Security by Design* não é desenhar mais — é desenhar conscientemente, e assegurar a produção de evidencia e forma de manter o conhecimento.

---


## 📘 Convenções Gerais {#convencoes-gerais}
- **ARC-XXX**: identificador de requisito arquitetural definido no *catálogo* do capítulo.  
- **AuthN / AuthZ**: Autenticação / Autorização.  
- **L1–L3**: níveis de **criticidade da aplicação** (não maturidade organizacional).  
- **Artefacto**: documento ou evidência versionada (Markdown, issue, ticket, export CI/CD).  
- **Rastreabilidade**: ligação verificável entre requisitos, decisões, controlos e evidências.

## 📚 Termos Núcleo (Definição → Onde aplicar → Artefactos) {#termos-nucleo}

| Termo | Definição Operacional | Onde aplicar | Artefactos / Evidências |
|---|---|---|---|
| **ADR (Architecture Decision Record)** | Registo de uma decisão arquitetural relevante, incluindo contexto, alternativas, decisão, impacto em segurança e rastreabilidade. | Sempre que há decisão com impacto em segurança, risco, custo de mudança ou dependências críticas. | `adr/ADR-xxxx.md` (ou secção “Decisões” na `solution-architecture.md`), *review* AppSec. |
| **Fronteira de Confiança (*Trust Boundary*)** | Delimitação explícita onde muda o nível de confiança entre componentes/serviços, equipas ou terceiros. | Integrações internas/externas, multitenancy, interfaces expostas. | `trust-boundaries.md`, `integration-review.md`, diagramas C4/DFD anotados. |
| **Arquitetura Viva** | Conjunto de *trigger* e rotinas que mantêm a documentação e controlos sincronizados com a realidade (evitar *drift*). | Após eventos definidos (ver “Triggers”). | `arquitetura-triggers.md`, commits/PRs de atualização, notas de *review*. |
| **Drift Arquitetural** | Divergência entre o desenho documentado e a implementação real em runtime/pipeline. | Mudanças rápidas, *hotfixes*, alterações infra, *feature flags*. | Issues de desalinhamento, diffs nos diagramas, *logs* de validação CI/CD. |
| **Exceção Arquitetural** | Desvio aprovado a um requisito ARC-XXX com controlo compensatório e prazo. | Quando o custo/tempo inviabiliza cumprimento imediato sem comprometer segurança de base. | `excecao-arquitetural.md`, decisão e prazo, *owner* do risco, *review* periódico. |
| **Controlo Compensatório** | Medida alternativa que reduz risco quando o controlo primário não é possível. | Em exceções, *workarounds*, fases transitórias. | Plano de compensação, *evidence logs*, monitorização. |
| **Sincronização TM ↔ Arquitetura** | Atualização consistente entre o **modelo de ameaças** (Cap. 03) e as decisões/diagramas de arquitetura. | Antes de *builds* significativos, depois de ADR/integração nova. | `tm-sync-arquitetura.md`, ligações ameaça → controlo → ARC-XXX. |
| **Ficha de Arquitetura** | Documento de solução com decisões, *rationale* e controlos de segurança aplicados. | Em cada projeto/épico/macro-funcionalidade com impacto estrutural. | `solution-architecture.md`, anexos com controlos, ligações a ADR/diagramas. |
| **Checklist de Arquitetura (Go-live)** | Lista de verificação final dos controlos e exceções aprovadas. | *Gate* de release. | `checklist-arquitetura.md`, assinaturas QA/AppSec/Arquiteto. |
| ***Triggers** | Eventos que obrigam a revisão arquitetural. | Ver tabela “Triggers de revisão de Arquitetura”. | `arquitetura-triggers.md`, *tasks* de atualização, PRs. |
| **Proveniência** | Capacidade de provar origem/integraidade de *artefactos* (código, *builds*), alinhada com boas práticas de *supply chain*. | Pipelines, dependências, imagens. | Registos CI/CD, SBOM, assinaturas, logs. |

## 🗺️ Triggers de revisão de Arquitetura 
| Trigger | Ação mínima | Evidência |
|---|---|---|
| Nova integração (interna/terceiro) | Rever *trust boundaries*, atualizar ficha e modelo de ameaças | `integration-review.md`, `tm-sync-arquitetura.md` |
| Alteração de dados sensíveis (tipo, volume, fluxo) | Rever classificação, encriptação, retenção | Atualização de `solution-architecture.md` e DFD/C4 |
| Mudança de infraestrutura/pipeline | Rever dependências e controlo compensatório | PR de pipeline, *logs* de validação |
| Decisão arquitetural relevante | Criar/atualizar ADR e impactos L1–L3 | `adr/ADR-xxxx.md` |
| Incidente ou *near-miss* | Retroalimentar controlos, ajustar desenho | RCA, *post-mortem*, atualização de controlos |
| Ameaça emergente (*threat intel*) | Rever cobertura e priorização | `tm-sync-arquitetura.md` |

## 🧩 Mapa rápido: ARC-XXX → Prática/Artefacto 
> Exemplo de como referenciar no *lifecycle* (ajustar aos teus ARC reais):

| ARC-ID | Prática associada | Artefacto esperado |
|---|---|---|
| **ARC-015 - AuthN centralizada** | Integração OIDC; revisão *trust boundary* | ADR, `integration-review.md`, `solution-architecture.md` |
| **ARC-023 - Segregação por contexto** | *Trust boundaries*, *least privilege* | Diagrama C4 anotado, *review* AppSec |
| **ARC-031 - Criptografia em trâns./repouso** | *Key management*, *KMS* | `solution-architecture.md`, *evidence* CI/CD |
| **ARC-042 - Observabilidade de segurança** | *Tracing*, *audit logs* | Plano de *logging*, métricas, *dashboards* |

## 🔄 Como usar este jargão nas User Stories 
- **US-08 (ADR)**: aceitar como válido ADR em Markdown, *wiki* ou *issue*, desde que haja contexto → decisão → impacto → rastreabilidade (ARC-XXX).  
- **US-09 (Trust Boundaries)**: exigir *inventário de integrações* e matriz de confiança; apontar AuthN/AuthZ/TLS/segregação.  
- **US-10 (TM ↔ Arquitetura)**: garantir ligação ameaça → controlo → ARC-XXX nos artefactos.  
- **US-11 (Exceções)**: incluir prazo, controlo compensatório, *owner* e *review* periódico.  
- **US-12 (Arquitetura Viva)**: publicar a lista de trigger e evidenciar execução quando ocorrem.

## 🧭 Proporcionalidade L1–L3 (aplicação do jargão) 
- **L1**: Registos simplificados (decisões chave, integrações críticas, *checklist* leve).  
- **L2**: ADR para decisões significativas; *trust boundaries* completos; sincronização TM; exceções formais.  
- **L3**: Cobertura integral, *reviews* independentes, validações em CI/CD, automação de trigger onde possível.

## 🔗 Ligações Internas Úteis 
- Cap. 01 — Gestão de Risco: `/sbd-toe/sbd-manual/01-classificacao-aplicacoes/intro`  
- Cap. 02 — Requisitos de Segurança: `/sbd-toe/sbd-manual/02-requisitos-seguranca/intro`  
- Cap. 03 — Threat Modeling: `/sbd-toe/sbd-manual/03-threat-modeling/intro`  
- Cap. 04 — Arquitetura Segura (ficheiro *lifecycle*): `/sbd-toe/sbd-manual/04-arquitetura-segura/aplicacao-lifecycle`
