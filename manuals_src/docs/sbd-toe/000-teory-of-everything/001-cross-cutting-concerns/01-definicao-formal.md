---
id: 01-definicao-formal
title: Definição Formal
description: Enquadramento, critérios e papel dos cross-cutting concerns na arquitetura do SbD-ToE
sidebar_label: 1️⃣ Definição Formal
sidebar_position: 2
ai_generated: false
---

# Definição Formal de Cross-Cutting Concerns

## 1. Enquadramento e Motivação

A engenharia de software segura contemporânea deixou de poder ser descrita como uma sequência linear de fases técnicas independentes. O *Security by Design – Theory of Everything (SbD‑ToE)* parte explicitamente do pressuposto de que a segurança emerge da **interação contínua entre decisões técnicas, organizacionais e humanas**, ao longo de todo o ciclo de vida do software.

Neste contexto, certos temas de segurança não pertencem a um único domínio técnico (ex.: código, infraestrutura, testes), nem a uma fase isolada do SDLC. Pelo contrário, **atravessam transversalmente múltiplos capítulos, práticas e artefactos**. Estes temas são designados, no SbD‑ToE, como *cross‑cutting concerns*.

A identificação, formalização e governação explícita destes *cross‑cutting concerns* constitui um dos elementos diferenciadores do SbD‑ToE face a abordagens fragmentadas ou puramente técnicas de Secure SDLC.

---

## 2. Definição Formal

No âmbito do SbD‑ToE, um *cross‑cutting concern* é definido como uma preocupação de segurança que cumpre **cumulativamente** os seguintes critérios:

### 2.1 Transversalidade Técnica
Afeta múltiplos domínios técnicos (ex.: desenvolvimento, arquitetura, CI/CD, operações, governação), não apenas um.

### 2.2 Persistência Temporal
Manifesta‑se em várias fases do ciclo de vida do software, e não apenas num momento específico. É uma preocupação contínua, não uma fotografia.

### 2.3 Impacto Dual (Produto e Processo)
Influencia tanto as propriedades de segurança do artefacto final como o modo como esse artefacto é concebido, produzido e operado.

### 2.4 Carácter Normativo
Deve ser definido ao nível de princípios e requisitos abstratos, **independentes de tecnologia concreta**. Permanece válido mesmo quando a stack muda.

### 2.5 Materialização Distribuída
A sua implementação ocorre através de múltiplas práticas especializadas, descritas em capítulos distintos do manual. Não existe um "lugar único" onde é implementado.

---

## 3. Papel na Arquitetura do SbD‑ToE

O SbD‑ToE adota uma separação estrutural clara entre:

### Camada Normativa
Define **o que deve existir** para que o desenvolvimento seja considerado seguro. Estabelece princípios, requisitos e contadores mensuráveis.

### Camada de Concretização Técnica
Descreve **como** esses requisitos são operacionalizados em domínios específicos. Fornece práticas, checklists, artefactos e validações.

---

## 4. Regra de Ouro

O manual impõe, como regra editorial e conceptual:

> **Um cross-cutting concern é definido uma única vez, de forma abstrata, e nunca reescrito ou redefinido nos capítulos técnicos.**

Os capítulos técnicos limitam-se a demonstrar a **concretização prática** desses concerns, mantendo rastreabilidade explícita para a definição normativa.

Esta abordagem evita redundância, contradições e permite manutenção coerente.

---

## 5. Diferenciador Científico

A explicitação formal dos *cross-cutting concerns* constitui:

- Um **contributo conceptual** para a engenharia de software segura
- Um **mecanismo de integração** entre normas, frameworks e práticas
- Uma **base sólida** para avaliação de maturidade e governação
- Um **elemento diferenciador** com valor académico e aplicacional

Ao tratar a segurança como propriedade emergente de um sistema sociotécnico, o SbD-ToE ultrapassa abordagens prescritivas fragmentadas, oferecendo um modelo coerente, extensível e auditável de Secure Software Engineering.
