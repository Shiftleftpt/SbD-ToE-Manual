---
id: intro
title: Capítulo 4 - Arquitetura Segura
description: Fundamentos, objetivos e enquadramento do capítulo dedicado à arquitetura segura no ciclo de vida de software
tags: [introducao, arquitetura, requisitos, segurança]
sidebar_position: 4
---

:::caution Capítulo Basilar
Este capítulo é considerado **basilar** no modelo *Security by Design - Theory of Everything (SbD-ToE)*.  
A sua aplicação é **obrigatória** para garantir a coerência, rastreabilidade e eficácia das restantes práticas de segurança.  

Os capítulos basilares constituem a **fundação técnica e metodológica** do modelo, a ausência ou aplicação parcial de qualquer um destes compromete a **integridade global** do SbD-ToE, tornando inviável a adoção coerente das práticas operacionais e de governação.
:::


# 🏛️ Arquitetura Segura

Este capítulo define as práticas para garantir que a arquitetura de uma aplicação **atua como contenção e mitigação do risco estrutural**, através de:

- Delimitação de **zonas de confiança** e respetivas fronteiras
- **Segmentação lógica e física** de componentes e dados
- Controlo e validação de **fluxos interzonais**
- Suporte a **threat modeling, autenticação, controlo de acesso, validação e operações seguras**
- Documentação formal da arquitetura e rastreabilidade das decisões

Cobre diferentes estilos de arquitetura:

- Monólitos modernos e aplicações em 3 camadas
- Microserviços e API-first
- Ambientes híbridos e cloud-native
- Serverless e pipelines como arquitetura

---

## 🧪 2. Prescrição prática: o quê, quem, como, quando, porquê e para quê

### 📌 O que deve ser feito

1. **Definir zonas de confiança** e fronteiras explícitas
2. **Estabelecer padrões de arquitetura** proporcionais ao risco
3. **Documentar decisões de arquitetura** (ex: ADRs, diagramas versionados)
4. **Validar arquitetura antes de go-live** e em alterações significativas
5. **Registar e gerir exceções** quando requisitos não possam ser cumpridos

### ⚙️ Como deve ser feito

- Aplicar técnicas de **Threat Modeling** (ex: DFD, STRIDE)
- Utilizar **modelos de referência reutilizáveis** (`04-diagramas-referencia.md`)
- Implementar controlos como:
  - API Gateway com autenticação mútua
  - Segmentação de tráfego (ex: ACLs, namespaces, sub-redes)
  - Mecanismos de contenção (rate limiting, circuit breakers)
- Validar arquitetura com base nos critérios de `05-validacao.md`

### 📆 Quando aplicar

| Momento                              | Ação esperada                                         |
|--------------------------------------|-------------------------------------------------------|
| Início de projeto                    | Definir ZTCs e padrão da arquitetura                    |
| Nova funcionalidade ou serviço       | Rever fronteiras e controlos interzonais              |
| Integração com terceiros             | Analisar implicações de confiança e exposição         |
| Refactoring ou migração tecnológica  | Avaliar risco de exposição adicional                  |
| Pré-produção                         | Validar arquitetura segundo requisitos e padrões      |

### 👥 Quem está envolvido e como

| Papel/Função               | Responsabilidades técnicas                                         |
|----------------------------|--------------------------------------------------------------------|
| **Arquiteto / DevSecOps**  | Definir modelos, diagramas e decisões                               |
| **Developer**              | Implementar e manter os controlos definidos                         |
| **QA / Test Engineer**     | Validar requisitos de arquitetura em testes                          |
| **AppSec / Segurança**     | Participar em threat modeling e revisões de arquitetura              |
| **Product Owner / Negócio**| Avaliar impacto em prazos e custo                                   |
| **Eng. CI/CD**             | Automatizar verificações de controlos de arquitetura                 |

> ✅ Toda exceção da arquitetura deve ser **registada, justificada e validada** com plano compensatório.

### 🎯 Porquê / Para quê

- Reduzir a superfície de ataque e limitar a propagação de falhas.
- Estabelecer uma fundação técnica sólida para todos os restantes controlos de segurança.
- Permitir decisões de design mais informadas, rastreáveis e auditáveis.
- Garantir proporcionalidade dos controlos com base no risco da aplicação.

---

## ⚠️ 3. Caveats ou limitações da prescrição

- Nem todos os controlos podem ser aplicados a todas as arquiteturas - o modelo deve ser adaptado.
- Modelos inconsistentes, incompletos ou desatualizados **geram risco não rastreável**.
- Threat modeling sem arquitetura clara **é ineficaz**.
- Exceções não documentadas **invalidam a rastreabilidade e o controlo de risco residual**.

---

## 💡 4. Exemplos de aplicação

Num sistema L3 com microserviços e exposição a terceiros:

- A arquitetura define 4 zonas de confiança (frontend, backend, admin, terceiros).
- Cada fluxo interzonal está validado com autenticação, controlo de acesso e logging.
- O diagrama versionado é mantido no repositório, validado antes de cada release.
- Foi aprovada uma exceção justificada para uma dependência circular entre dois serviços, mitigada com timeouts e circuit breakers.
- A revisão de arquitetura foi feita com base no checklist de `05-validacao.md`, com evidência de threat modeling e ADRs.

---

## 🧩 Ligações a outros capítulos

| Capítulo                      | Relação técnica e de processo                                       |
|-------------------------------|---------------------------------------------------------------------|
| `01-gestao-risco`             | O nível de risco define a exigência e profundidade da arquitetura     |
| `02-requisitos-seguranca`     | Define os requisitos técnicos do tipo `ARC-00x`                     |
| `03-threat-modeling`          | Usa a arquitetura como base para modelar ameaças                    |
| `06-desenvolvimento-seguro`   | Aplica controlos definidos pela arquitetura (ex: validações, filtros)|
| `09-containers-imagens`       | Define padrões de execução e isolamento coerentes com a arquitetura |

---

## 📜 Políticas Organizacionais Relevantes

| Política | Obrigatória | Aplicação | Conteúdo mínimo |
|----------|-------------|-----------|-----------------|
| Política de Arquitetura Segura | Sim | Todos os projetos | Definição de princípios, padrões e controlos mínimos de arquitetura |
| Política de Revisões Arquiteturais | Recomendado | Projetos L2–L3 | Critérios formais de revisão e aprovação AppSec |
| Política de Automação em Pipelines | Recomendado | Projetos com CI/CD | Regras para validação automatizada de controlos de arquitetura |

Na versão impressa, as políticas relevantes encontram-se no **anexo de políticas do manual**, incluindo: Política de Arquitetura Segura, Política de Revisões Arquiteturais e Política de Automação em Pipelines.

---

> 🧱 Este capítulo é **basilar** para a aplicação coerente do modelo SbD-ToE. A sua ausência compromete a proporcionalidade dos controlos, a eficácia do threat modeling e a integridade das medidas de segurança em runtime.