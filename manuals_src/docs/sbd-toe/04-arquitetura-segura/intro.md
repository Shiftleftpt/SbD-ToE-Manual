---
id: intro
title: Capítulo 4 – Arquitetura Segura
description: Fundamentos, objetivos e enquadramento do capítulo dedicado à arquitetura segura no ciclo de vida de software
tags: [introducao, arquitetura, requisitos, segurança]
sidebar_position: 4
---
import Badge from '@site/src/components/Badge';

<a name="xref:cap04"></a>

# 🏛️ Arquitetura Segura {arquitetura-segura:intro}

<!--web-only-->
<div style={{ display: 'flex', flexWrap: 'wrap', gap: '0.5rem', marginBottom: '1rem' }}>
  <Badge color="warning">Capítulo Basilar</Badge>
  <Badge color="info">SAMM: 2 / 3</Badge>
  <Badge color="info">BSIMM: AA1.2, AA2.1, CMVM1.1</Badge>
  <Badge color="info">SSDF: PW.4, PW.7</Badge>
  <Badge color="info">SLSA: Nível 2 / 4</Badge>
  <Badge color="info">DSOMM: 3 / 4 (média)</Badge>
  <a href="./canon/10-maturidade.md" style={{ marginLeft: 'auto', fontSize: '0.9rem' }}>📄 Ver análise de maturidade</a>
</div>
<!--/web-only-->

## 🧭 1. O que cobre tecnicamente {arquitetura-segura:intro#1_o_que_cobre_tecnicamente}

Este capítulo define as práticas para garantir que a arquitetura de uma aplicação **atua como contenção e mitigação do risco estrutural**, através de:

- Delimitação de **zonas de confiança (ZTC)** e respetivas fronteiras
- **Segmentação lógica e física** de componentes e dados
- Controlo e validação de **fluxos interzonais**
- Suporte a **threat modeling, autenticação, controlo de acesso, validação e operações seguras**
- Documentação formal da arquitetura e rastreabilidade das decisões

Cobre diferentes estilos arquiteturais:

- Monólitos modernos e aplicações em 3 camadas
- Microserviços e API-first
- Ambientes híbridos e cloud-native
- Serverless e pipelines como arquitetura

---

## 🧪 2. Prescrição prática: o quê, quem, como, quando, porquê e para quê {arquitetura-segura:intro#2_prescricao_pratica_o_que_quem_como_quando_porque_e_para_que}

### 📌 O que deve ser feito {arquitetura-segura:intro#o_que_deve_ser_feito}

1. **Definir zonas de confiança** e fronteiras explícitas
2. **Estabelecer padrões arquiteturais** proporcionais ao risco
3. **Documentar decisões arquiteturais** (ex: ADRs, diagramas versionados)
4. **Validar arquitetura antes de go-live** e em alterações significativas
5. **Registar e gerir exceções** quando requisitos não possam ser cumpridos

### ⚙️ Como deve ser feito {arquitetura-segura:intro#como_deve_ser_feito}

- Aplicar técnicas de **Threat Modeling** (ex: DFD, STRIDE)
- Utilizar **modelos de referência reutilizáveis** (`04-diagramas-referencia.md`)
- Implementar controlos como:
  - API Gateway com autenticação mútua
  - Segmentação de tráfego (ex: ACLs, namespaces, sub-redes)
  - Mecanismos de contenção (rate limiting, circuit breakers)
- Validar arquitetura com base nos critérios de `05-validacao.md`

### 📆 Quando aplicar {arquitetura-segura:intro#quando_aplicar}

| Momento                              | Ação esperada                                         |
|--------------------------------------|-------------------------------------------------------|
| Início de projeto                    | Definir ZTCs e padrão arquitetural                    |
| Nova funcionalidade ou serviço       | Rever fronteiras e controlos interzonais              |
| Integração com terceiros             | Analisar implicações de confiança e exposição         |
| Refactoring ou migração tecnológica  | Avaliar risco de exposição adicional                  |
| Pré-produção                         | Validar arquitetura segundo requisitos e padrões      |

### 👥 Quem está envolvido e como {arquitetura-segura:intro#quem_esta_envolvido_e_como}

| Papel/Função               | Responsabilidades técnicas                                         |
|----------------------------|--------------------------------------------------------------------|
| **Arquiteto / DevSecOps**  | Definir modelos, diagramas e decisões                               |
| **Developer**              | Implementar e manter os controlos definidos                         |
| **QA / Test Engineer**     | Validar requisitos arquiteturais em testes                          |
| **AppSec / Segurança**     | Participar em threat modeling e revisões arquiteturais              |
| **Product Owner / Negócio**| Avaliar impacto em prazos e custo                                   |
| **Eng. CI/CD**             | Automatizar verificações de controlos arquiteturais                 |

> ✅ Toda exceção arquitetural deve ser **registada, justificada e validada** com plano compensatório.

### 🎯 Porquê / Para quê {arquitetura-segura:intro#porque__para_que}

- Reduzir a superfície de ataque e limitar a propagação de falhas.
- Estabelecer uma fundação técnica sólida para todos os restantes controlos de segurança.
- Permitir decisões de design mais informadas, rastreáveis e auditáveis.
- Garantir proporcionalidade dos controlos com base no risco da aplicação.

---

## ⚠️ 3. Caveats ou limitações da prescrição {arquitetura-segura:intro#3_caveats_ou_limitacoes_da_prescricao}

- Nem todos os controlos podem ser aplicados a todas as arquiteturas — o modelo deve ser adaptado.
- Modelos inconsistentes, incompletos ou desatualizados **geram risco não rastreável**.
- Threat modeling sem arquitetura clara **é ineficaz**.
- Exceções não documentadas **invalidam a rastreabilidade e o controlo de risco residual**.

---

## 💡 4. Exemplos de aplicação {arquitetura-segura:intro#4_exemplos_de_aplicacao}

Num sistema L3 com microserviços e exposição a terceiros:

- A arquitetura define 4 zonas de confiança (frontend, backend, admin, terceiros).
- Cada fluxo interzonal está validado com autenticação, controlo de acesso e logging.
- O diagrama versionado é mantido no repositório, validado antes de cada release.
- Foi aprovada uma exceção justificada para uma dependência circular entre dois serviços, mitigada com timeouts e circuit breakers.
- A revisão de arquitetura foi feita com base no checklist de `05-validacao.md`, com evidência de threat modeling e ADRs.

---

## 🧩 Ligações a outros capítulos {arquitetura-segura:intro#ligacoes_a_outros_capitulos}

| Capítulo                      | Relação técnica e de processo                                       |
|-------------------------------|---------------------------------------------------------------------|
| `01-gestao-risco`             | O nível de risco define a exigência e profundidade arquitetural     |
| `02-requisitos-seguranca`     | Define os requisitos técnicos do tipo `ARC-00x`                     |
| `03-threat-modeling`          | Usa a arquitetura como base para modelar ameaças                    |
| `06-desenvolvimento-seguro`   | Aplica controlos definidos pela arquitetura (ex: validações, filtros)|
| `09-containers-imagens`       | Define padrões de execução e isolamento coerentes com a arquitetura |

---

## 📜 Políticas Organizacionais Relevantes {arquitetura-segura:intro#politicas_relevantes}

<!--web-only-->
| Política | Obrigatória | Aplicação | Conteúdo mínimo |
|----------|-------------|-----------|-----------------|
| Política de Arquitetura Segura | Sim | Todos os projetos | Definição de princípios, padrões e controlos mínimos de arquitetura |
| Política de Revisões Arquiteturais | Recomendado | Projetos L2–L3 | Critérios formais de revisão e aprovação AppSec |
| Política de Automação em Pipelines | Recomendado | Projetos com CI/CD | Regras para validação automatizada de controlos arquiteturais |

<!--print-only-->
Na versão impressa, as políticas relevantes encontram-se no **anexo de políticas do manual**, incluindo: Política de Arquitetura Segura, Política de Revisões Arquiteturais e Política de Automação em Pipelines.

---

> 🧱 Este capítulo é **basilar** para a aplicação coerente do modelo SbD-ToE. A sua ausência compromete a proporcionalidade dos controlos, a eficácia do threat modeling e a integridade das medidas de segurança em runtime.