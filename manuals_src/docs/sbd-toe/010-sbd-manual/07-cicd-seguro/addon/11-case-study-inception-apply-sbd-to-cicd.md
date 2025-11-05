---
id: case-study-inception-apply-sbd-to-cicd
title: Estudo de Caso - Aplicar o SbD-ToE ao Próprio Pipeline CI/CDx
sidebar_position: 9
description: Regras formais para permitir exceções no pipeline, com registo, aprovação, prazo de validade e visibilidade por função.
tags: [exceções, visibilidade, cicd, governação, auditoria, segurança]
---


# 🧪 Estudo de Caso - Aplicar o SbD-ToE ao Próprio Pipeline CI/CD

Este estudo de caso descreve a aplicação transversal e rigorosa do manual **Security by Design - Theory of Everything (SbD-ToE)** ao **próprio sistema de pipelines CI/CD** de uma organização. 

> O objetivo foi tratar os pipelines como **ativos críticos (nível L3)**, com ciclo de vida, riscos e controlos equiparáveis aos de qualquer produto de software sensível.

A abordagem seguiu todas as fases do ciclo de vida descritas no manual - desde o risco à operação - com validações, rastreabilidade e automatização como pilares centrais.

---

## 🧭 Contexto e decisão

A organização opera múltiplas aplicações em ambientes regulados. Após uma avaliação baseada no Capítulo 01 - Gestão de Risco, foi identificado que:

- O pipeline CI/CD tem acesso privilegiado a código, artefactos, segredos e infraestrutura;
- É o ponto de entrada para todo o ciclo de vida de software;
- A sua integridade condiciona a segurança de todo o SDLC.

> **Decisão estratégica:** Tratar os pipelines como software de elevada criticidade (nível L3), e aplicar o SbD-ToE como se de um produto se tratasse.

---

## 📐 Arquitetura desenhada

Foi adotada uma arquitetura modular e segura (Cap. 04):

- Pipelines como código (`.yaml`) em repositório dedicado com controlo de alterações;
- Templates centrais versionados, com política de aprovação formal;
- Runners segregados (build/test/deploy), com isolamento e descarte;
- Gestão dinâmica de segredos via Vault (Cap. 03, 06);
- Mirrors internos para NPM, Maven, Docker (Cap. 05);
- Proveniência e assinatura dos artefactos gerados (Cap. 07);
- Logging completo com auditabilidade de execuções (Cap. 11).

---

## 🔍 Threat modeling

O exercício de threat modeling (Cap. 03) identificou riscos como:

- **Spoofing:** execução de pipelines em runners não autorizados → mitigado com labels restritos e workers dedicados.
- **Tampering:** alteração silenciosa de templates → mitigado com PR obrigatórios e revisões.
- **Information Disclosure:** acesso indevido a secrets → mitigado com escopo mínimo e logs validados.
- **Elevation of Privilege:** tasks inline com permissões excessivas → mitigado com revisão manual e catálogo controlado.

---

## 🛠️ Desenvolvimento seguro dos próprios pipelines

Aplicando o Cap. 06:

- Todo o código de pipeline é versionado, com revisão obrigatória;
- Linters e scanners analisam `.yaml`, scripts embutidos, módulos reutilizados;
- Tasks, Actions e extensões são incluídas num **SBOM próprio**, com validação contínua (Cap. 05);
- Foram definidos requisitos não funcionais específicos, ex. `CI-CD-004`, `CI-CD-006`, `REQ-014`, `REQ-024`.

---

## 🧪 Testes aplicados ao pipeline

Com base no Cap. 10:

- SAST sobre scripts auxiliares e tarefas embutidas;
- Análise de segredos e permissões excessivas;
- Testes de regressão para garantir enforcement de gates;
- Execuções sandbox com rastreabilidade de inputs/outputs.

---

## 🔐 Gestão de dependências, imagens e SBOM

- SBOM do pipeline gerado com `syft` + `trivy`;
- Dependências externas (ex: Actions, plugins) auditadas e versionadas;
- Runners baseados em containers verificados, hardened, com validação de assinatura (Cap. 09);
- Política de exceções com validade e rastreabilidade (Cap. 05, 14).

---

## 📦 Deploy e execução

- O próprio pipeline é deployado com rastreabilidade total;
- Logs são enviados para sistema central com alertas de anomalias;
- A cada alteração relevante, é obrigatória nova revisão de threat modeling e validação funcional.

---

## 🎓 Formação e onboarding

- Criado um módulo de formação (Cap. 13) para equipas Dev e DevOps:
  - Boas práticas de alteração de pipelines;
  - Validação e rastreabilidade;
  - Como interpretar resultados de segurança.
- User stories e cartões incluídos no backlog técnico da equipa CI/CD.

---

## 📊 Governação e visibilidade

- Scorecard de conformidade CI/CD atualizado trimestralmente;
- Exceções auditáveis e aprovadas por segurança (Cap. 14);
- Integração com auditorias internas e monitorização de maturidade.

---

## ✅ Conclusão

Este caso demonstra a **aplicação transversal e coerente do manual SbD-ToE a um sistema crítico de CI/CD**. 

> Tratar o pipeline como um produto de software, com risco L3, permitiu:
> - Reduzir drasticamente riscos de supply chain;
> - Ganhar visibilidade e rastreabilidade fim-a-fim;
> - Automatizar decisões de segurança no ciclo de vida de desenvolvimento e operação.

A abordagem é escalável e replicável noutras organizações.

> 💡 **Este é um exemplo completo da aplicação do SbD-ToE como framework operativo.**
