---
id: intro
title: Introdução - Cross-Check Normativo
description: Enquadramento do capítulo de análise normativa, que demonstra como o SbD-ToE se cruza com diferentes normativos e regulações
tags: [cross-check, normativos, compliance, dora, nis2, hipaa, iso27001, pci-dss, gdpr, soc2]
sidebar_position: 0
---



# Introdução - Cross-Check Normativo

A segurança do software não acontece num vácuo técnico.  
Organizações de diferentes setores estão sujeitas a **regulações, normas e frameworks** que estabelecem requisitos explícitos para garantir proteção adequada de sistemas, dados e operações.  
Neste contexto, o **Security by Design – Theory of Everything (SbD-ToE)** não é apenas um manual prescritivo de boas práticas: é também um **instrumento de convergência normativa**, permitindo alinhar práticas de desenvolvimento e operação segura com as múltiplas exigências externas.

O **Capítulo 002 - Cross-Check Normativo** tem precisamente este papel:  
- Demonstrar, de forma clara e verificável, **como o SbD-ToE responde a requisitos regulatórios e normativos**.  
- Identificar onde o modelo garante **compliance "por construção"**, e onde existem **lacunas** que exigem complementaridade com processos legais, organizacionais ou contratuais.  
- Apoiar **equipas de GRC, auditores, equipas técnicas e de gestão** na tarefa de articular segurança operacional com conformidade formal.
- Para **organizações que possuem ou contratam desenvolvimento de software**, oferecer **playbooks práticos** para implementar requisitos normativos de forma coerente com a disciplina de segurança aplicacional.

---

## Contexto e Justificação

Historicamente, o panorama normativo de segurança evoluiu de forma fragmentada:  
- **Há duas décadas**, poucas normas existiam, muitas vezes limitadas a requisitos de gestão de risco genéricos.  
- **Com a digitalização**, assistimos a uma explosão de normativos setoriais e regulamentares: **HIPAA** para saúde, **PCI-DSS** para pagamentos, **GDPR** para proteção de dados pessoais, **NIS2** e **DORA** para ciber-resiliência europeia, entre muitos outros.  
- Hoje, o desafio não é a falta de normativos, mas sim o **excesso de sobreposição** e a consequente dificuldade de aplicação prática coerente.

O SbD-ToE foi concebido como resposta a este problema.  
Ao ser construído **top-down**, com base em múltiplas referências normativas, frameworks técnicas e modelos de maturidade (ISO, ENISA, NIST, OWASP SAMM, BSIMM, SSDF, DSOMM, SLSA, etc.), o manual assegura que:  

- **As exigências normativas são incorporadas desde a raiz**, não tratadas como camadas externas ou aditivas.  
- **A conformidade não é um objetivo isolado**, mas sim um **efeito colateral positivo** de aplicar práticas seguras em todo o ciclo de vida.  
- **Cada área de conhecimento** (requisitos, arquitetura, CI/CD, containers, governança, etc.) contribui para que o modelo **construa “compliance by design”**.

---

## Objetivos deste capítulo

1. **Mostrar a correspondência** entre práticas do SbD-ToE e requisitos de normativos internacionais e europeus.  
2. **Evidenciar as áreas de cobertura plena**, onde a adoção do modelo conduz a conformidade quase imediata.  
3. **Revelar lacunas e zonas cinzentas**, ajudando as organizações a perceberem onde necessitam de medidas adicionais (jurídicas, processuais ou técnicas).  
4. **Fornecer um repositório comparativo**, que possa ser reutilizado em auditorias, certificações ou relatórios de conformidade.
5. **Oferecer playbooks de implementação** para organizações que contratam ou desenvolvem software, garantindo que a aquisição/desenvolvimento seja coerente com requisitos normativos específicos.

---

## Metodologia adotada

A análise segue uma estrutura sistemática, comum a todos os normativos:  

- **Enquadramento** → breve descrição do normativo, âmbito e objetivos.  
- **Tabela de Cross-Check** → requisitos principais do normativo vs. práticas do SbD-ToE:  
  - Se existe cobertura, indicar **capítulo(s)** onde está tratado.  
  - Se a cobertura é parcial, detalhar as limitações.  
  - Se não existe cobertura, indicar explicitamente o gap.  
- **Notas Críticas** → observações sobre interpretação, sobreposição ou complementaridade.  
- **Conclusão** → até que ponto o SbD-ToE assegura alinhamento com esse normativo.
- **Playbook Prático** (quando aplicável) → roadmap de implementação para organizações com disciplina de desenvolvimento/AppSec, orientando como integrar requisitos normativos na aquisição ou desenvolvimento de software.

---

## Filosofia de Conformidade Integrada

O **SbD-ToE não é uma norma**, mas foi desenhado para **dialogar com todas as normas**.  
Isto acontece porque:  

- **Normas e regulamentos são, por definição, subset requirements**: focam-se em dimensões específicas (governação, risco, reporte, proteção de dados, etc.).  
- O SbD-ToE, ao contrário, prescreve práticas **abrangentes e integradas**, que **por construção já cumprem muitos desses requisitos**.  
- A abordagem do SbD-ToE é **“compliance built-in”**: a conformidade é consequência natural da aplicação prática das medidas, e não um esforço paralelo ou burocrático.  

Esta visão **mitiga a fragmentação regulatória** e oferece às organizações um **modelo unificado de aplicação prática**, onde segurança, risco e conformidade convergem.

---

## Nota Importante: Normativos e Desenvolvimento Aplicacional

Muitos normativos (ex.: **DORA**, **NIS2**, **ISO 27001**) **não são específicos de desenvolvimento de software**, mas cobrem a **gestão integral de risco TIC** em organizações.

No entanto, quando uma organização **possui ou contrata desenvolvimento de software**, a disciplina de **segurança aplicacional (AppSec)** torna-se um **componente crítico** para demonstrar conformidade com esses normativos.

**Consequência prática:**  
- O normativo exige "gestão de risco TIC" (âmbito amplo)
- A organização implementa isso através de múltiplos controles (arquitetura, operações, contratos, etc.)
- Se existe desenvolvimento/aquisição de software, os playbooks deste capítulo orientam **como integrar práticas de AppSec** de forma **coerente e proporcional** com o regulamento

**Exemplo:** **DORA** é regulação financeira, mas se uma entidade financeira desenvolve software internamente, deve aplicar os princípios do SbD-ToE para demonstrar que a sua **postura de ciber-resiliência** (DORA Art. 5) inclui **development security practices**.

---

## Estrutura do Capítulo

Este capítulo está organizado por **framework/normativo**, cada um numa pasta dedicada com introdução e playbook de implementação:

### Frameworks Atualmente Cobertos

#### **[DORA](dora/intro)** (Digital Operational Resilience Act)
- 📂 `dora/`
  - [Enquadramento do regulamento](dora/intro)
  - [Playbook de implementação prática](dora/playbook)
  - [Análise de convergência com NIS2](dora/convergencia-nis2)

#### **[NIS2](nis2/intro)** (Network and Information Security Directive)
- 📂 `nis2/`
  - [Enquadramento da diretiva](nis2/intro)
  - [Playbook de implementação prática](nis2/playbook)
  - [Análise de convergência com DORA](nis2/convergencia-dora)

#### **[CRA](cra/intro)** (Cyber Resilience Act)
- 📂 `cra/`
  - [Enquadramento do regulamento](cra/intro)
  - [Playbook de implementação prática](cra/playbook)

#### **[GDPR](gdpr/intro)** (General Data Protection Regulation)
- 📂 `gdpr/`
  - [Enquadramento do regulamento](gdpr/intro)
  - [Playbook de implementação prática](gdpr/playbook)

#### **[ENISA CSA](enisa-csa/intro)** (Cloud Security Alliance Certification)
- 📂 `enisa-csa/`
  - [Enquadramento do esquema de certificação](enisa-csa/intro)

### Exemplos e Templates de Suporte

#### **[Exemplo-Playbook](exemplo-playbook/indice)**
- 📂 [`exemplo-playbook/`](exemplo-playbook/indice)
  - Templates e exemplos reutilizáveis para implementação de qualquer framework
  - Ferramentas, KPIs, governance, relatórios, políticas, contratos
  - [Ver índice completo](exemplo-playbook/indice) para detalhes

---

### Frameworks a Incluir (Roadmap)

Os seguintes frameworks estão no roadmap para adição futura:

- **ISO 27001** → Norma de Gestão de Segurança da Informação
- **HIPAA** → Health Insurance Portability and Accountability Act
- **PCI-DSS** → Payment Card Industry Data Security Standard
- **SOC2** → Service Organization Control 2
- **FedRAMP** → Federal Risk and Authorization Management Program
- **CSA STAR** → Cloud Security Alliance Security Trust Assurance and Risk

---

### Estrutura Comum de Cada Framework

Cada pasta de framework segue esta estrutura consistente:

1. **Introdução**
   - Enquadramento legal/regulatório
   - Âmbito de aplicação
   - Objetivos principais

2. **Playbook de Implementação**
   - Cross-check: Requisitos vs. SbD-ToE
   - Roadmap de implementação
   - Fases e milestones
   - Checklists práticas

3. **Análises de Convergência** (quando aplicável)
   - Sobreposição entre frameworks
   - Princípio *lex specialis*
   - Estratégias de implementação harmonizada

---

## Leitura recomendada

- Este capítulo deve ser lido **em articulação com o [Capítulo 00 - Theory of Everything](/sbd-toe/teory-of-everything/intro)**, que explica a filosofia global do manual.  
- Para organizações **com desenvolvimento/aquisição de software**, recomenda-se começar pelos playbooks (ex.: [DORA](dora/playbook), [NIS2](nis2/playbook)), que orientam implementação coerente.
- Pode também ser utilizado como **documento autónomo**, servindo de guia de referência rápida para quem procura verificar alinhamento do SbD-ToE com exigências específicas.  

---
