---
id: devops-sre
title: DevOps / SRE
sidebar_label: ⚙️ DevOps / SRE
description: Responsabilidades de DevOps/SRE no SbD-ToE
tags: [cicd, devops, responsabilidades, sre]
sidebar_position: 4
---

# ⚙️ DevOps / SRE

## Visão Geral

DevOps/SRE são os **artesãos da automação e da infraestrutura**.  
Garantem que segurança está embutida nos pipelines e no runtime, não aplicada como adereço posterior. Constroem **autopistas de segurança** que verificam, validam e bloqueiam código inseguro.

### Responsabilidades Principais
- Integram verificações de segurança em pipelines (Cap. 07)
- Automatizam criação de SBOM e scans de dependências (Cap. 05)
- Garantem execução segura de IaC e containers (Cap. 08-09)
- Mantêm monitorização contínua em produção (Cap. 12)

### Contexto Organizacional
Respondem diretamente a requisitos de **DORA** (resiliência operacional digital) e **NIS2** (medidas técnicas adequadas). São a ponte entre desenvolvimento e operações seguras.

## Enquadramento Regulatório

Essenciais para:
- **DORA**: Resiliência operacional digital
- **NIS2**: Implementação de medidas técnicas adequadas

---

## Atividades por Capítulo

### Cap. 01 - Classificação de Aplicações
Classificar **artefactos técnicos** (Dockerfile, pipeline, IaC, imagens) com a mesma criticidade da aplicação, garantindo que controlos de segurança acompanham a integridade da entrega.

**User Stories:**
- [US-09: Classificação de artefactos técnicos](/sbd-toe/sbd-manual/classificacao-aplicacoes/aplicacao-lifecycle#us-09---classificação-de-artefactos-técnicos) — Rastreabilidade de segurança em artefactos

### Cap. 02 - Requisitos de Segurança
Garantir que **pipeline CI/CD verifica automaticamente** requisitos de segurança (SAST, SCA, DAST, SBOM, assinaturas), bloqueando merges e releases não conformes.

**User Stories:**
- [US-10: Gates automáticos em CI/CD](/sbd-toe/sbd-manual/requisitos-seguranca/aplicacao-lifecycle#us-10---gates-automáticos-em-cicd-para-requisitos-de-segurança) — Verificação automática de requisitos
- [US-11: Geração de SBOM e assinatura](/sbd-toe/sbd-manual/requisitos-seguranca/aplicacao-lifecycle#us-11---geração-de-sbom-e-assinatura-de-artefactos-de-build) — SBOM e assinaturas no pipeline

### Cap. 03 - Threat Modeling
Atualizar **modelo de ameaça** em alterações significativas e integrar validações no pipeline para revisão automática.

**User Stories:**
- [US-03: Atualização do modelo após alteração](/sbd-toe/sbd-manual/threat-modeling/aplicacao-lifecycle#us-03---atualização-do-modelo-após-alteração-técnica) — Manter modelo atualizado
- [US-05: Integração com CI/CD](/sbd-toe/sbd-manual/threat-modeling/aplicacao-lifecycle#us-05---integração-com-cicd) — Validações automáticas
- [US-07: Automação e reutilização de modelos](/sbd-toe/sbd-manual/threat-modeling/aplicacao-lifecycle#us-07---automação-e-reutilização-de-modelos) — Ferramentas para consistência

### Cap. 04 - Arquitetura Segura
Validar **controlos de arquitetura no pipeline** (topologia, IaC, policies). Implementar **segregação de ambientes** (dev, QA, stage, prod) com isolamento lógico e físico.

**User Stories:**
- [US-05: Validação da arquitetura em CI/CD](/sbd-toe/sbd-manual/arquitetura-segura/aplicacao-lifecycle#us-05--validação-da-arquitetura-em-cicd) — Garantir conformidade automática
- [US-13: Segregação de ambientes](/sbd-toe/sbd-manual/arquitetura-segura/aplicacao-lifecycle#us-13--segregação-de-ambientes-devqastage---prod) — Isolamento com permissões mínimas

### Cap. 05 - Dependências e SBOM
Automatizar **geração e gestão de SBOM**, integrando análise de vulnerabilidades em dependências no pipeline.

**User Stories:**
- [US-02: SBOM em cada build](/sbd-toe/sbd-manual/dependencias-sbom-sca/aplicacao-lifecycle#us-02--sbom-em-cada-build) — Rastreabilidade completa de componentes
- [US-06: Repositórios internos como fonte única](/sbd-toe/sbd-manual/dependencias-sbom-sca/aplicacao-lifecycle#us-06--repositórios-internos-como-fonte-única) — Proveniência e consistência
- [US-08: Automação da atualização com avaliação de impacto](/sbd-toe/sbd-manual/dependencias-sbom-sca/aplicacao-lifecycle#us-08--automação-da-atualização-com-avaliação-de-impacto) — PRs seguros automatizados
- [US-10: Inventário e SBOM por Build](/sbd-toe/sbd-manual/dependencias-sbom-sca/aplicacao-lifecycle#us-10--inventário-e-sbom-por-build) — SBOM assinado por artefacto
- [US-11: Alertas sobre vulnerabilidades](/sbd-toe/sbd-manual/dependencias-sbom-sca/aplicacao-lifecycle#us-11---alertas-sobre-vulnerabilidades-em-componentes-usados) — Notificações proativas

### Cap. 06 - Desenvolvimento Seguro
Integrar **linters e SAST no pipeline** para detetar falhas precocemente e gerar evidência contínua de conformidade.

**User Stories:**
- [US-04: Automatização em CI/CD](/sbd-toe/sbd-manual/desenvolvimento-seguro/aplicacao-lifecycle#us-04---automatização-em-cicd-linters--sast) — Linters e SAST automáticos
- [US-09: Gate de segurança pré-release](/sbd-toe/sbd-manual/desenvolvimento-seguro/aplicacao-lifecycle#us-09---gate-de-segurança-pré-release) — Consolidação de evidências
- [US-12: Validações locais obrigatórias](/sbd-toe/sbd-manual/desenvolvimento-seguro/aplicacao-lifecycle#us-12---validações-locais-obrigatórias-pre-commit) — Pre-commit hooks

### Cap. 07 - CI/CD Seguro
Desenhar **pipelines com scanners, gates e assinaturas** de release, garantindo que apenas artefactos validados avançam entre fases.

**User Stories:**
- [US-02: Design seguro dos pipelines](/sbd-toe/sbd-manual/cicd-seguro/aplicacao-lifecycle#us-02--design-seguro-dos-pipelines) — Pipelines versionados e auditáveis
- [US-04: Gestão de segredos](/sbd-toe/sbd-manual/cicd-seguro/aplicacao-lifecycle#us-04--gestão-de-segredos) — OIDC com TTL curto
- [US-05: Isolamento de runners](/sbd-toe/sbd-manual/cicd-seguro/aplicacao-lifecycle#us-05--isolamento-de-runners) — Runners ephemerais e segregados
- [US-06: Assinatura e proveniência](/sbd-toe/sbd-manual/cicd-seguro/aplicacao-lifecycle#us-06--assinatura-e-proveniência) — Confiança em artefactos
- [US-13: Validação de integridade de imagens base](/sbd-toe/sbd-manual/cicd-seguro/aplicacao-lifecycle#us-13--validação-de-integridade-de-imagens-base) — Proteção contra supply chain

### Cap. 08 - IaC
Aplicar **enforcement de políticas** em IaC com *policy-as-code*, validando conformidade antes do deployment.

**User Stories:**
- [US-01: Backend remoto, locking e rastreabilidade](/sbd-toe/sbd-manual/iac-infraestrutura/aplicacao-lifecycle#us-01--backend-remoto-locking-e-rastreabilidade) — Estado seguro e sem drift
- [US-02: Segregação de ambientes, tagging e permissões mínimas](/sbd-toe/sbd-manual/iac-infraestrutura/aplicacao-lifecycle#us-02--segregação-de-ambientes-tagging-e-permissões-mínimas) — Isolamento e rastreabilidade
- [US-05: Rastreabilidade, versionamento e naming](/sbd-toe/sbd-manual/iac-infraestrutura/aplicacao-lifecycle#us-05--rastreabilidade-versionamento-e-naming) — Histórico completo com rollback
- [US-06: Revisão formal de plan antes de apply](/sbd-toe/sbd-manual/iac-infraestrutura/aplicacao-lifecycle#us-06--revisão-formal-de-plan-antes-de-apply) — Validação de impacto
- [US-09: Assinatura e Proveniência de artefactos IaC](/sbd-toe/sbd-manual/iac-infraestrutura/aplicacao-lifecycle#us-09--assinatura-e-proveniência-de-artefactos-iac) — Integridade ponta-a-ponta
- [US-10: Gestão de segredos e identidades para IaC](/sbd-toe/sbd-manual/iac-infraestrutura/aplicacao-lifecycle#us-10--gestão-de-segredos-e-identidades-para-iac) — OIDC com permissões mínimas
- [US-12: Rollback e salvaguarda de destroy](/sbd-toe/sbd-manual/iac-infraestrutura/aplicacao-lifecycle#us-12--rollback-e-salvaguarda-de-destroy) — Pontos de restauração

### Cap. 09 - Containers e Imagens
Executar scanners de vulnerabilidades em cada build, validar execuções com políticas formais (OPA/Kyverno), gerar SBOM automaticamente, impor allowlist de registries e digest SHA256, proibir credenciais estáticas, aplicar RBAC mínimo e NetworkPolicy, manter catálogo de Golden Images.

**User Stories:**
- [US-02: Validação automática de vulnerabilidades em imagens](/sbd-toe/sbd-manual/containers-imagens/aplicacao-lifecycle#us-02--validação-automática-de-vulnerabilidades-em-imagens-no-pipeline-cicd) — SCA com bloqueio automático
- [US-04: Políticas formais de segurança no runtime](/sbd-toe/sbd-manual/containers-imagens/aplicacao-lifecycle#us-04--aplicação-de-políticas-formais-de-segurança-no-runtime-com-opakyverno) — OPA/Kyverno para validação
- [US-06: Geração e Rastreabilidade de SBOM](/sbd-toe/sbd-manual/containers-imagens/aplicacao-lifecycle#us-06--geração-e-rastreabilidade-de-sbom-em-imagens) — SBOM versionado por build
- [US-07: Governação de Registries](/sbd-toe/sbd-manual/containers-imagens/aplicacao-lifecycle#us-07--governação-de-registries-com-allowlist-e-digest-only) — Allowlist + digest SHA256
- [US-08: Gestão de Segredos com OIDC](/sbd-toe/sbd-manual/containers-imagens/aplicacao-lifecycle#us-08--gestão-de-segredos-fora-da-imagem-com-oidc-e-workload-identity) — Identidades efémeras
- [US-09: RBAC Mínimo e ServiceAccounts](/sbd-toe/sbd-manual/containers-imagens/aplicacao-lifecycle#us-09--rbac-mínimo-e-serviceaccounts-dedicadas) — Isolamento por workload
- [US-10: Segmentação de Rede](/sbd-toe/sbd-manual/containers-imagens/aplicacao-lifecycle#us-10--segmentação-de-rede-e-networkpolicy) — NetworkPolicy por namespace
- [US-11: Golden Base Images](/sbd-toe/sbd-manual/containers-imagens/aplicacao-lifecycle#us-11--golden-base-images-com-patching-automático) — Catálogo padronizado com SLA
- [US-12: Builders e Runners Seguros](/sbd-toe/sbd-manual/containers-imagens/aplicacao-lifecycle#us-12--builders-e-runners-ephemerais-assinados-e-com-auditoria) — Proteção do pipeline CI/CD

### Cap. 10 - Testes de Segurança
Integrar **gates automáticos no pipeline** (SAST/SCA/IAST) com thresholds por Lx. Centralizar findings numa plataforma unificada e automatizar delivery às equipas.

**User Stories:**
- [US-04: Gates de segurança no CI/CD](/sbd-toe/sbd-manual/testes-seguranca/aplicacao-lifecycle#us-04---gates-de-segurança-no-cicd) — Thresholds por nível de criticidade
- [US-10: Gestão Centralizada de Findings](/sbd-toe/sbd-manual/testes-seguranca/aplicacao-lifecycle#us-10---gestão-centralizada-de-findings-com-triagem-e-sla) — Plataforma unificada
- [US-11: Feedback Automático de Findings](/sbd-toe/sbd-manual/testes-seguranca/aplicacao-lifecycle#us-11---feedback-automático-de-findings-às-equipas) — Delivery contextualizado

### Cap. 11 - Deploy Seguro
Executar deploy **apenas de artefactos assinados e versionados**. Implementar rollback rápido testado periodicamente, ativar monitorização pós-deploy, implementar feature flags com metadados, garantir que segredos nunca são embebidos, implementar deploy progressivo (canary/blue-green).

**User Stories:**
- [US-02: Deploy apenas de artefactos assinados](/sbd-toe/sbd-manual/deploy-seguro/aplicacao-lifecycle#us-02--deploy-apenas-de-artefactos-assinados-e-versionados) — Integridade criptográfica
- [US-05: Rollback rápido e testado](/sbd-toe/sbd-manual/deploy-seguro/aplicacao-lifecycle#us-05--rollback-rápido-e-testado-periodicamente) — Documentado e validado
- [US-06: Monitorização pós-deploy](/sbd-toe/sbd-manual/deploy-seguro/aplicacao-lifecycle#us-06--monitorização-pós-deploy-para-deteção-imediata-de-anomalias) — Deteção de anomalias
- [US-08: Feature Flags com Governança](/sbd-toe/sbd-manual/deploy-seguro/aplicacao-lifecycle#us-08--feature-flags-com-metadados-owner-e-expiração) — Metadados e expiração
- [US-09: Gestão Segura de Segredos](/sbd-toe/sbd-manual/deploy-seguro/aplicacao-lifecycle#us-09--gestão-segura-de-segredos-zero-embebidos-em-artefactos) — Zero segredos em artefactos
- [US-10: Deploy Progressivo](/sbd-toe/sbd-manual/deploy-seguro/aplicacao-lifecycle#us-10--deploy-progressivo-canaryblue-green-com-validação-automática) — Canary/Blue-Green
- [US-11: Rollback documentado por tipo](/sbd-toe/sbd-manual/deploy-seguro/aplicacao-lifecycle#us-11--rollback-documentado-por-tipo-de-alteração) — Procedimentos de rollback testados

### Cap. 12 - Monitorização e Operações
Configurar ambientes de produção com **monitorização contínua** e coordenar resposta a alertas. Garantir segurança e integridade de logs (retenção WORM), integrar com SIEM.

**User Stories:**
- [US-06: Domínios de monitorização](/sbd-toe/sbd-manual/monitorizacao-operacoes/aplicacao-lifecycle#us-06--classificação-e-mapeamento-de-domínios-de-monitorização) — Cobertura proporcional ao risco
- [US-07: Segurança e integridade de logs](/sbd-toe/sbd-manual/monitorizacao-operacoes/aplicacao-lifecycle#us-07--segurança-e-integridade-de-logs) — Retenção WORM + acesso restrito
- [US-08: Integração com SIEM](/sbd-toe/sbd-manual/monitorizacao-operacoes/aplicacao-lifecycle#us-08--integração-com-siem-parsing-normalização-enriquecimento) — Parsing e normalização

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
