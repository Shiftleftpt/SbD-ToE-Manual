---
id: appsec-engineer
title: AppSec Engineer
sidebar_label: 🔐 AppSec Engineer
description: Responsabilidades do AppSec Engineer no SbD-ToE
tags: [appsec, responsabilidades, seguranca, vulnerabilidades]
sidebar_position: 5
---

# 🔐 AppSec Engineer

## Visão Geral

AppSec é a **ponte entre normas abstratas e execução técnica**.  
Transforma obrigações regulatórias em **controlos concretos, auditáveis e proporcionais ao risco**, garantindo que segurança é embutida no ciclo de vida completo.

### Responsabilidades Principais
- Traduzem normas e regulamentos em requisitos técnicos
- Facilitam sessões de threat modeling e revisão da arquitetura
- Definem guidelines de desenvolvimento seguro
- Acompanham auditorias e produzem evidência de segurança

### Contexto Organizacional
Atuam como **ponto de ligação entre equipas técnicas e governação**, assegurando rastreabilidade exigida por **NIS2** e **DORA**. Sem AppSec, as políticas de segurança ficam desligadas da realidade técnica.

## Enquadramento Regulatório

Essencial para:
- **NIS2**: Rastreabilidade e gestão de vulnerabilidades
- **DORA**: Governação de fornecedores e resiliência operacional
- **GDPR**: Security by design e privacy by default

---

## Atividades por Capítulo

### Cap. 01 - Classificação de Aplicações
Rever **classificação de criticidade** sempre que houver alterações técnicas relevantes ou com cadência fixa (L1 anual, L2 semestral, L3 trimestral). Verificar se ameaças esperadas estão cobertas por controlos aplicados.

**User Stories:**
- [US-02: Revisão de criticidade em alterações relevantes](/sbd-toe/sbd-manual/classificacao-aplicacoes/aplicacao-lifecycle#us-02--revisão-de-criticidade-em-alterações-relevantes) — Manter classificação atualizada
- [US-03: Revisão periódica de criticidade](/sbd-toe/sbd-manual/classificacao-aplicacoes/aplicacao-lifecycle#us-03--revisão-periódica-de-criticidade-cadência-fixa-l1-anual-l2-semestral-l3-trimestral) — Cadência fixa por nível
- [US-06: Verificação de cobertura de ameaças](/sbd-toe/sbd-manual/classificacao-aplicacoes/aplicacao-lifecycle#us-06--verificação-de-cobertura-de-ameaças-vs-controlos) — Validar adequação de controlos

### Cap. 02 - Requisitos de Segurança
Estabelecer e manter **catálogo de requisitos de segurança** (REQ-XXX) versionado e auditável ao longo do SDLC.

**User Stories:**
- [US-04: Catálogo de Requisitos de Segurança](/sbd-toe/sbd-manual/requisitos-seguranca/aplicacao-lifecycle#us-04--catálogo-de-requisitos-de-segurança-do-projeto) — Aplicação consistente e rastreável

### Cap. 03 - Threat Modeling
Documentar e **aprovar formalmente riscos residuais** identificados no threat modeling, garantindo decisões transparentes e auditáveis.

**User Stories:**
- [US-04: Documentação e aprovação de riscos residuais](/sbd-toe/sbd-manual/threat-modeling/aplicacao-lifecycle#us-04--documentação-e-aprovação-de-riscos-residuais) — Decisões transparentes

### Cap. 04 - Arquitetura Segura
Rever **designs de arquitetura** para garantir conformidade com padrões de segurança estabelecidos.

**User Stories:**
- [US-03: Revisão de designs de arquitetura](/sbd-toe/sbd-manual/arquitetura-segura/aplicacao-lifecycle#us-03--revisão-de-designs-de-arquitetura) — Validar conformidade técnica

### Cap. 05 - Dependências e SBOM
Executar **SCA automático em pipelines** e formalizar exceções a CVEs com governação explícita. Auditar bibliotecas copiadas manualmente.

**User Stories:**
- [US-03: SCA automático com gates](/sbd-toe/sbd-manual/dependencias-sbom-sca/aplicacao-lifecycle#us-03--sca-automático-com-gates) — Detetar CVEs antes de produção
- [US-04: Exceções a CVEs formais e temporárias](/sbd-toe/sbd-manual/dependencias-sbom-sca/aplicacao-lifecycle#us-04--exceções-a-cves-formais-e-temporárias) — Governação de risco residual
- [US-09: Auditoria de bibliotecas copiadas manualmente](/sbd-toe/sbd-manual/dependencias-sbom-sca/aplicacao-lifecycle#us-09--auditoria-periódica-de-bibliotecas-copiadas-manualmente) — Bloqueio em CI/CD

### Cap. 06 - Desenvolvimento Seguro
Validar dependências externas, registar exceções técnicas, **rever guidelines** trimestralmente, definir perfis de validação L1-L3, detetar padrões perigosos automaticamente.

**User Stories:**
- [US-02: Validação de dependências externas](/sbd-toe/sbd-manual/desenvolvimento-seguro/aplicacao-lifecycle#us-02--validação-e-justificação-de-dependências-externas) — Reduzir supply chain risk
- [US-03: Registro e aprovação de exceções técnicas](/sbd-toe/sbd-manual/desenvolvimento-seguro/aplicacao-lifecycle#us-03--registro-e-aprovação-de-exceções-técnicas) — Rastreabilidade e revisão
- [US-04: Revisão trimestral de guidelines](/sbd-toe/sbd-manual/desenvolvimento-seguro/aplicacao-lifecycle#us-04--revisão-e-publicação-trimestral-de-guidelines) — Governação formal
- [US-05: Perfis de validação L1-L3](/sbd-toe/sbd-manual/desenvolvimento-seguro/aplicacao-lifecycle#us-05--perfis-de-validação-l1l3-por-aplicação) — Adequação ao risco
- [US-06: Deteção automática de padrões perigosos](/sbd-toe/sbd-manual/desenvolvimento-seguro/aplicacao-lifecycle#us-06--deteção-automática-de-padrões-perigosos-no-pipeline) — Bloqueio com feedback educativo

### Cap. 07 - CI/CD Seguro
Aplicar **gates distintos por L1-L3** e garantir scanners de containers/SBOM em pipelines. Executar DAST em staging.

**User Stories:**
- [US-07: Gates por risco](/sbd-toe/sbd-manual/cicd-seguro/aplicacao-lifecycle#us-07--gates-por-risco) — Segurança proporcional
- [US-08: Cobertura ampliada](/sbd-toe/sbd-manual/cicd-seguro/aplicacao-lifecycle#us-08--cobertura-ampliada) — Containers e SBOM
- [US-11: DAST em staging](/sbd-toe/sbd-manual/cicd-seguro/aplicacao-lifecycle#us-11--testes-de-segurança-dinâmicos-dast) — Validação comportamental

### Cap. 08 - IaC e Infraestrutura
Governar **módulos IaC com origem confiável**, aplicar enforcement automático de políticas, auditar drift periodicamente.

**User Stories:**
- [US-04: Governança de módulos IaC](/sbd-toe/sbd-manual/iac-infraestrutura/aplicacao-lifecycle#us-04--governança-e-origem-confiável-de-módulos) — Reduzir supply chain risk
- [US-08: Enforcement automático de políticas](/sbd-toe/sbd-manual/iac-infraestrutura/aplicacao-lifecycle#us-08--enforcement-automático-de-políticas) — Conformidade sistemática
- [US-11: Auditoria periódica de drift](/sbd-toe/sbd-manual/iac-infraestrutura/aplicacao-lifecycle#us-11--deteção-e-correção-de-drift) — Coerência IaC vs infraestrutura

### Cap. 09 - Containers e Imagens
Assinar **todas as imagens digitalmente** com proveniência verificável. Monitorizar comportamento de containers em runtime.

**User Stories:**
- [US-03: Assinatura digital de imagens](/sbd-toe/sbd-manual/containers-imagens/aplicacao-lifecycle#us-03--assinatura-digital-de-imagens-e-proveniência-verificável) — Integridade e origem
- [US-05: Monitorização de comportamento em runtime](/sbd-toe/sbd-manual/containers-imagens/aplicacao-lifecycle#us-05--monitorização-de-comportamento-de-containers-em-execução) — Deteção de eventos suspeitos

### Cap. 10 - Testes de Segurança
Definir **estratégia de testes por aplicação** proporcional ao risco. Centralizar findings numa plataforma unificada e automatizar delivery às equipas.

**User Stories:**
- [US-01: Estratégia de testes de segurança](/sbd-toe/sbd-manual/testes-seguranca/aplicacao-lifecycle#us-01---estratégia-de-testes-de-segurança-por-aplicação) — Cobertura proporcional ao risco
- [US-10: Gestão centralizada de findings](/sbd-toe/sbd-manual/testes-seguranca/aplicacao-lifecycle#us-10---gestão-centralizada-de-findings-com-triagem-e-sla) — Plataforma unificada
- [US-11: Feedback automático de findings](/sbd-toe/sbd-manual/testes-seguranca/aplicacao-lifecycle#us-11---feedback-automático-de-findings-às-equipas) — Delivery contextualizado

### Cap. 11 - Deploy Seguro
Definir **gates automáticos e thresholds** no deploy. Executar validações técnicas com gates condicionais por risco.

**User Stories:**
- [US-01: Gates automáticos no deploy](/sbd-toe/sbd-manual/deploy-seguro/aplicacao-lifecycle#us-01--gates-automáticos-no-deploy) — Bloquear releases inseguras
- [US-04: Gates condicionais por risco](/sbd-toe/sbd-manual/deploy-seguro/aplicacao-lifecycle#us-04--gates-de-deploy-condicionais-por-risco) — Validações técnicas proporcionais

### Cap. 12 - Monitorização e Operações
Definir **eventos e métricas críticas** de segurança. Classificar domínios de monitorização, correlacionar eventos multi-fonte, afinar alertas, aplicar controlos proporcionais ao risco.

**User Stories:**
- [US-02: Definição de eventos críticos](/sbd-toe/sbd-manual/monitorizacao-operacoes/aplicacao-lifecycle#us-02--definição-de-eventos-e-métricas-críticas-de-segurança) — Cobertura de riscos relevantes
- [US-04: Classificação de domínios de monitorização](/sbd-toe/sbd-manual/monitorizacao-operacoes/aplicacao-lifecycle#us-04--classificação-e-mapeamento-de-domínios-de-monitorização) — Cobertura proporcional
- [US-05: Correlação de eventos multi-fonte](/sbd-toe/sbd-manual/monitorizacao-operacoes/aplicacao-lifecycle#us-05--correlação-de-eventos-entre-múltiplas-fontes) — Deteção de padrões suspeitos
- [US-06: Validação e afinação de alertas](/sbd-toe/sbd-manual/monitorizacao-operacoes/aplicacao-lifecycle#us-06--validação-e-afinação-de-alertas) — Reduzir falsos positivos
- [US-09: Controlos proporcionais ao risco](/sbd-toe/sbd-manual/monitorizacao-operacoes/aplicacao-lifecycle#us-09--controlos-de-monitorização-proporcionais-ao-risco) — Equilibrar custo e cobertura

### Cap. 13 - Formação e Onboarding
Fornecer **formação contínua por perfil**, executar code clinics, manter trilhos formativos atualizados, aplicar formação proporcional ao risco, implementar quizzes de validação, definir DoD por formato.

**User Stories:**
- [US-02: Formação contínua por perfil](/sbd-toe/sbd-manual/formacao-onboarding/aplicacao-lifecycle#us-02--formação-contínua-por-perfil) — Atualização com práticas recentes
- [US-03: Code clinics estruturadas](/sbd-toe/sbd-manual/formacao-onboarding/aplicacao-lifecycle#us-03--code-clinics-estruturadas) — Aprendizagem contínua
- [US-07: Manutenção de trilhos formativos](/sbd-toe/sbd-manual/formacao-onboarding/aplicacao-lifecycle#us-07--manutenção-e-atualização-de-trilhos-formativos) — Refletir práticas atuais
- [US-08: Trilhos proporcionais ao risco](/sbd-toe/sbd-manual/formacao-onboarding/aplicacao-lifecycle#us-08--trilhos-formativos-proporcionais-ao-nível-de-risco) — Adequação ao contexto
- [US-09: Quizzes de validação](/sbd-toe/sbd-manual/formacao-onboarding/aplicacao-lifecycle#us-09--quizzes-de-validação) — Registro auditável de competência
- [US-10: Definição de DoD por formato](/sbd-toe/sbd-manual/formacao-onboarding/aplicacao-lifecycle#us-10--definição-de-dod-por-formato-de-entrega) — Consistência e qualidade

### Cap. 14 - Governança e Contratação
Agregar práticas em **dashboard organizacional**, revisar exceções periodicamente, manter repositório de conformidade, executar validações periódicas, formalizar governação com alçadas, manter checklist centralizado, monitorizar fornecedores.

**User Stories:**
- [US-02: Dashboard organizacional](/sbd-toe/sbd-manual/governanca-contratacao/aplicacao-lifecycle#us-02--dashboard-organizacional-de-práticas-sbd) — Visibilidade e medição
- [US-04: Revisão periódica de exceções](/sbd-toe/sbd-manual/governanca-contratacao/aplicacao-lifecycle#us-04--revisão-periódica-de-exceções-e-compensações) — Validar mitigações
- [US-06: Repositório de conformidade](/sbd-toe/sbd-manual/governanca-contratacao/aplicacao-lifecycle#us-06--repositório-de-conformidade-por-aplicação) — Facilitar auditorias
- [US-07: Validações periódicas de conformidade](/sbd-toe/sbd-manual/governanca-contratacao/aplicacao-lifecycle#us-07--validações-periódicas-de-conformidade) — Detetar desvios
- [US-10: Checklist centralizado de conformidade](/sbd-toe/sbd-manual/governanca-contratacao/aplicacao-lifecycle#us-10--checklist-centralizado-de-conformidade-sbd-toe) — Estado real de todas as práticas
- [US-14: Monitorização contínua de fornecedores](/sbd-toe/sbd-manual/governanca-contratacao/aplicacao-lifecycle#us-14--monitorização-contínua-de-fornecedores-críticos) — Deteção de eventos em tempo real

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
