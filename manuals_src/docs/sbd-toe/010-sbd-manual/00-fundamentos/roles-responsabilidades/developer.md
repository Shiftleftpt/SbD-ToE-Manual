---
description: Responsabilidades do Developer no SbD-ToE
id: developer
sidebar_label: 👨‍💻 Developer
sidebar_position: 2
tags:
- automação
- codigo
- dev
- developer
- responsabilidades
- segurança
- threat-modeling
title: Developer
---


# 👨‍💻 Developer

## Visão Geral

Developers são a **linha da frente da implementação prática de *security by design***.  
É no ato de escrever código que se materializam grande parte das práticas de segurança prescritas no SbD-ToE.

### Responsabilidades Principais
- Escrevem código em conformidade com guidelines de segurança (Cap. 06)
- Corrigem vulnerabilidades identificadas em revisões e scans
- Contribuem para o threat modeling e fornecem informação técnica sobre fluxos de dados (Cap. 03)
- Garantem que o software cumpre requisitos funcionais **e de segurança** de forma robusta e rastreável

### Contexto Organizacional
O papel do Developer é **transversal a quase todo o manual**. A responsabilidade é dupla: entregar funcionalidade e garantir segurança. Sem a colaboração ativa dos developers, nenhuma política de segurança se concretiza.

## Enquadramento Regulatório

O trabalho do Developer concretiza obrigações de:
- **NIS2**: Práticas seguras de desenvolvimento e gestão de vulnerabilidades
- **DORA**: Resiliência digital em sistemas financeiros  
- **GDPR**: Princípios de *security by design*
- **AI Act**: Segurança e transparência em sistemas de IA

---

## Atividades por Capítulo

### Cap. 01 - Classificação da Criticidade
Fornecer informação técnica sobre **dependências, integrações e impacto operacional** da aplicação, contribuindo para a avaliação de risco e determinação do nível de criticidade (L1/L2/L3).

**User Stories:**
- [US-01: Classificação inicial da aplicação](/sbd-toe/sbd-manual/classificacao-aplicacoes/aplicacao-lifecycle#us-01---classificação-inicial-da-aplicação) — Aplicar modelo E+D+I para determinar nível L1–L3
- [US-02: Aplicação da matriz de controlo](/sbd-toe/sbd-manual/classificacao-aplicacoes/aplicacao-lifecycle#us-02---aplicação-da-matriz-de-controlo) — Mapear requisitos para REQ-XXX do Cap. 02

### Cap. 02 - Requisitos de Segurança
Implementar **requisitos mínimos de segurança** derivados da classificação, integrando-os no *definition of done* e garantindo conformidade em cada entrega.

**User Stories:**
- [US-03: Gestão de Exceções com TTL e Revalidação](/sbd-toe/sbd-manual/requisitos-seguranca/aplicacao-lifecycle#us-03---gestão-de-exceções-com-ttl-e-revalidação-obrigatória) — Registar exceções formais com TTL e aprovação por AppSec
- [US-11: Geração de SBOM e assinatura de artefactos](/sbd-toe/sbd-manual/requisitos-seguranca/aplicacao-lifecycle#us-11---geração-de-sbom-e-assinatura-de-artefactos-de-build) — SBOM automático e assinatura de artefactos
- [US-12: Validação de tags SEC-Lx-* no pipeline](/sbd-toe/sbd-manual/requisitos-seguranca/aplicacao-lifecycle#us-12---validação-de-tags-sec-lx--e-requisitos-no-pipeline) — Rastreabilidade automática de requisitos

### Cap. 03 - Threat Modeling
Participar ativamente em **sessões de threat modeling**, traduzindo diagramas e cenários de ameaças em controlos práticos implementados no código.

**User Stories:**
- [US-01: Criação do modelo de ameaça](/sbd-toe/sbd-manual/threat-modeling/aplicacao-lifecycle#us-01---criação-do-modelo-de-ameaça) — DFDs e STRIDE/LINDDUN no início do projeto

### Cap. 04 - Arquitetura Segura
Garantir que a implementação respeita os **padrões arquiteturais** definidos. Manter a ficha de arquitetura atualizada quando ocorrem alterações críticas.

**User Stories:**
- [US-04: Atualização de arquitetura em alterações críticas](/sbd-toe/sbd-manual/arquitetura-segura/aplicacao-lifecycle#us-04--atualização-de-arquitetura-em-alterações-críticas) — Atualizar ficha de arquitetura quando surgem mudanças estruturais

### Cap. 05 - Dependências e SBOM
Declarar explicitamente todas as **bibliotecas e dependências** utilizadas, suportando a criação de inventários auditáveis (SBOM) essenciais para gestão de vulnerabilidades.

**User Stories:**
- [US-01: Gestão de dependências seguras](/sbd-toe/sbd-manual/dependencias-sbom-sca/aplicacao-lifecycle#us-01---gestão-de-dependências-seguras) — Usar apenas dependências aprovadas
- [US-07: Proibir bibliotecas copiadas manualmente](/sbd-toe/sbd-manual/dependencias-sbom-sca/aplicacao-lifecycle#us-07---proibir-bibliotecas-copiadas-manualmente) — Usar package managers, nunca cópias manuais
- [US-12: Validação automática de compatibilidade de licenças](/sbd-toe/sbd-manual/dependencias-sbom-sca/aplicacao-lifecycle#us-12---validação-automática-de-compatibilidade-de-licenças) — Garantir conformidade legal

### Cap. 06 - Desenvolvimento Seguro
Seguir **guidelines de código seguro**, utilizar linters e validações automáticas, corrigir findings de SAST. Prevenir vulnerabilidades triviais através de ferramentas integradas no workflow de desenvolvimento.

**User Stories:**
- [US-01: Guidelines de Desenvolvimento Seguro](/sbd-toe/sbd-manual/desenvolvimento-seguro/aplicacao-lifecycle#us-01---guidelines-de-desenvolvimento-seguro) — Aplicar guidelines aprovadas por stack
- [US-06: Uso Validado de GenIA](/sbd-toe/sbd-manual/desenvolvimento-seguro/aplicacao-lifecycle#us-06---uso-validado-de-genia) — IA generativa com revisão obrigatória
- [US-08: Rastreabilidade com Anotações de Segurança](/sbd-toe/sbd-manual/desenvolvimento-seguro/aplicacao-lifecycle#us-08---rastreabilidade-com-anotações-de-segurança) — Anotar validações com @sec:*
- [US-12: Validações Locais Obrigatórias](/sbd-toe/sbd-manual/desenvolvimento-seguro/aplicacao-lifecycle#us-12---validações-locais-obrigatórias-pre-commit) — Linters e validações pré-commit

### Cap. 07 - CI/CD Seguro
Colaborar com DevOps na **configuração de pipelines seguros**, garantindo que o código passa por gates de segurança (SAST, dependency check) antes de ser merged ou deployed.

**User Stories:**
- [US-01: Gestão segura de código fonte](/sbd-toe/sbd-manual/cicd-seguro/aplicacao-lifecycle#us-01---gestão-segura-de-código-fonte) — PRs com revisão obrigatória e branch protection
- [US-03: Scanners integrados](/sbd-toe/sbd-manual/cicd-seguro/aplicacao-lifecycle#us-03---scanners-integrados) — SAST, secrets scanning e bloqueio de falhas críticas

### Cap. 08 - IaC (Infraestrutura como Código)
Colaborar na escrita e **validação de templates IaC seguros**, garantindo que infraestrutura é versionada e auditável.

**User Stories:**
- [US-03: Validações automáticas integradas](/sbd-toe/sbd-manual/iac-infraestrutura/aplicacao-lifecycle#us-03---validações-automáticas-integradas) — Linters, scanners e policy-as-code obrigatórios

### Cap. 09 - Containers e Imagens
Construir imagens a partir de **bases confiáveis e versionadas** (digest SHA256). Garantir que Dockerfiles seguem melhores práticas de segurança.

**User Stories:**
- [US-01: Imagens base confiáveis](/sbd-toe/sbd-manual/containers-imagens/aplicacao-lifecycle#us-01--construção-de-imagens-a-partir-de-bases-seguras-minimalistas-e-pinned-por-digest) — Usar apenas imagens oficiais com digest SHA256

### Cap. 10 - Testes de Segurança
Executar **SAST automático no PR** com comentários inline, corrigindo vulnerabilidades antes do merge. Criar testes de regressão para findings corrigidos.

**User Stories:**
- [US-02: SAST automático no PR](/sbd-toe/sbd-manual/testes-seguranca/aplicacao-lifecycle#us-02---sast-obrigatório-em-pull-request) — Análise estática com feedback contextual
- [US-05: Testes de regressão de segurança](/sbd-toe/sbd-manual/testes-seguranca/aplicacao-lifecycle#us-05---regressões-de-segurança-automatizadas) — Prevenir reintrodução de vulnerabilidades

### Cap. 11 - Deploy Seguro
Manter **versionamento semântico** com changelog técnico e de segurança. Garantir que apenas artefactos validados são promovidos entre ambientes.

**User Stories:**
- [US-01: Versionamento semântico + changelog](/sbd-toe/sbd-manual/deploy-seguro/aplicacao-lifecycle#us-01--versionamento-semântico--changelog-de-segurança) — Rastreabilidade completa de alterações

### Cap. 12 - Monitorização e Operações
Implementar **logging estruturado e centralizado**, gerando eventos com contexto suficiente para deteção e investigação de incidentes.

**User Stories:**
- [US-01: Logs estruturados + centralização](/sbd-toe/sbd-manual/monitorizacao-operacoes/aplicacao-lifecycle#us-01--logs-estruturados--centralização) — Assegurar visibilidade completa em incidentes

### Cap. 13 - Formação e Onboarding
Participar em **programas de capacitação contínua** e, como Security Champion, liderar sessões de threat modeling por feature, épico ou refactor.

**User Stories:**
- [US-06: Threat modeling por feature/épico/refactor](/sbd-toe/sbd-manual/formacao-onboarding/aplicacao-lifecycle#us-06--threat-modeling-por-featureépicorefactor) — Security Champion lidera análise de ameaças

### Cap. 14 - Governança e Contratação
Submeter **exceções de segurança** em fluxo formal com roteamento automático por nível de risco. Manter repositório estruturado de conformidade para cada aplicação (com Dev Lead).

**User Stories:**
- [US-03: Exceções de segurança + workflow de aprovação](/sbd-toe/sbd-manual/governanca-contratacao/aplicacao-lifecycle#us-03--exceções-de-segurança--workflow-de-aprovação) — Gestão formal de exceções
- [US-06: Repositório de conformidade por aplicação](/sbd-toe/sbd-manual/governanca-contratacao/aplicacao-lifecycle#us-06--repositório-de-conformidade-por-aplicação) — Centralizar evidências e documentação

---

## Referências aos Capítulos

Para contexto e enquadramento completo:

- [Cap. 01 - Classificação de Aplicações](/sbd-toe/sbd-manual/classificacao-aplicacoes/intro)
- [Cap. 02 - Requisitos de Segurança](/sbd-toe/sbd-manual/requisitos-seguranca/intro)
- [Cap. 03 - Threat Modeling](/sbd-toe/sbd-manual/threat-modeling/intro)
- [Cap. 04 - Arquitetura Segura](/sbd-toe/sbd-manual/arquitetura-segura/intro)
- [Cap. 05 - Dependências e SBOM](/sbd-toe/sbd-manual/dependencias-sbom-sca/intro)
- [Cap. 06 - Desenvolvimento Seguro](/sbd-toe/sbd-manual/desenvolvimento-seguro/intro)
- [Cap. 07 - CI/CD Seguro](/sbd-toe/sbd-manual/cicd-seguro/intro)
- [Cap. 08 - IaC e Infraestrutura](/sbd-toe/sbd-manual/iac-infraestrutura/intro)
- [Cap. 09 - Containers e Imagens](/sbd-toe/sbd-manual/containers-imagens/intro)
- [Cap. 10 - Testes de Segurança](/sbd-toe/sbd-manual/testes-seguranca/intro)
- [Cap. 11 - Deploy Seguro](/sbd-toe/sbd-manual/deploy-seguro/intro)
- [Cap. 12 - Monitorização e Operações](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro)
- [Cap. 13 - Formação e Onboarding](/sbd-toe/sbd-manual/formacao-onboarding/intro)
- [Cap. 14 - Governança e Contratação](/sbd-toe/sbd-manual/governanca-contratacao/intro)
