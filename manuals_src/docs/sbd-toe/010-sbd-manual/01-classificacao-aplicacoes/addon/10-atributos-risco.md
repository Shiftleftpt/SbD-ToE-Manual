---
id: atributos-risco
title: 🛠️ Atributos do Risco
description: Modelo unificado de caracterização do risco no SbD-ToE, aplicável a riscos técnicos e processuais
---

## 🎯 Objetivo

Este documento define um **modelo unificado de caracterização do risco** no contexto do **Security by Design – Theory of Everything (SbD-ToE)**.

O objetivo **não é criar categorias distintas de risco** (ex.: “risco técnico” vs. “risco de processo”), mas sim estabelecer um **conjunto de atributos internos** que permitam:

- descrever rigorosamente qualquer risco relevante;
- compreender a sua origem e mecanismo de materialização;
- determinar **requisitos, controlos e validações proporcionais**;
- manter o modelo **intemporal**, extensível e tecnologicamente neutro.

Este modelo aplica-se a **todo o ciclo de vida da aplicação** e a **todos os capítulos do manual**.

---

## 🧠 Princípio fundamental

No SbD-ToE, **o risco é tratado como um conceito único e indivisível**.

Um risco pode ter origem técnica, processual, organizacional ou externa, mas **o seu impacto materializa-se sempre no sistema entregue**, na sua operação ou na sua conformidade.

O que varia **não é o tipo de risco**, mas sim:
- **como surge**;
- **como se manifesta**;
- **como pode (ou não) ser observado, validado e mitigado**.

Essas variações são capturadas através de **atributos do risco**.

---

## 🧩 Modelo de atributos do risco

Cada risco identificado no âmbito do SbD-ToE deve ser descrito, explícita ou implicitamente, através dos atributos abaixo.

### 1️⃣ Origem do risco

Identifica **onde o risco se introduz** no sistema ou no processo.

Valores típicos (não exclusivos):
- Técnica (arquitetura, código, configuração)
- Processual (decisão, omissão, automação)
- Organizacional (governação, responsabilidades)
- Externa (fornecedores, dependências, serviços)

> Exemplo:  
> Um erro introduzido por geração automática de código tem **origem processual**, mesmo que se materialize como vulnerabilidade técnica.

---

### 2️⃣ Mecanismo de introdução

Descreve **como o risco é introduzido**.

Exemplos comuns:
- Vulnerabilidade técnica conhecida
- Erro humano
- Omissão de análise ou validação
- Decisão inadequada
- Confiança excessiva em resultados automatizados
- Configuração implícita ou herdada

Este atributo é crítico para definir **controlos preventivos vs. detetivos**.

---

### 3️⃣ Superfície de materialização

Indica **onde o impacto se manifesta** quando o risco se concretiza.

Valores típicos:
- Produto (software, dados, interfaces)
- Operação (disponibilidade, integridade, continuidade)
- Conformidade (legal, regulatória, contratual)
- Reputação / negócio

Um mesmo risco pode materializar-se em **mais do que uma superfície**.

---

### 4️⃣ Detetabilidade

Caracteriza **a facilidade com que o risco pode ser identificado** antes ou após a sua materialização.

- Alta – facilmente detetável por testes ou controlos objetivos
- Média – requer análise especializada ou correlação
- Baixa – dificilmente observável sem incidentes ou auditorias profundas

Riscos de baixa detetabilidade exigem **controlos mais fortes a montante**.

---

### 5️⃣ Reprodutibilidade

Indica se o comportamento associado ao risco é:

- Determinístico – reproduzível de forma consistente
- Parcialmente determinístico – dependente de contexto
- Não determinístico – resultados variáveis para o mesmo input

Este atributo é particularmente relevante em contextos de:
- automação avançada;
- sistemas de apoio à decisão;
- análise baseada em heurísticas.

Baixa reprodutibilidade **aumenta o risco operacional e de validação**.

---

### 6️⃣ Evidenciabilidade

Descreve **o grau em que o risco e a sua mitigação podem ser suportados por evidência verificável**.

- Elevada – evidência objetiva, versionada e auditável
- Limitada – evidência indireta ou interpretativa
- Fraca – baseada em plausibilidade ou confiança implícita

No SbD-ToE, **risco sem evidência adequada não pode ser considerado mitigado**, independentemente da sofisticação da análise.

---

## 🧪 Exemplo ilustrativo (não normativo)

Um risco identificado através de uma análise assistida por IA pode ser caracterizado como:

- Origem: Processual  
- Mecanismo: Decisão assistida com validação insuficiente  
- Superfície: Produto e conformidade  
- Detetabilidade: Média  
- Reprodutibilidade: Baixa  
- Evidenciabilidade: Limitada  

👉 A consequência **não é rejeitar a ferramenta**, mas **exigir controlos adicionais**, como:
- revisão humana explícita;
- validação empírica independente;
- registo da decisão e da evidência utilizada.

Este exemplo é equivalente, do ponto de vista do modelo, a:
- um ORM mal configurado;
- uma pipeline CI com gates implícitos;
- um scanner com regras excessivamente permissivas.

---

## 🔗 Relação com outros elementos do SbD-ToE

- A **classificação L1–L3** continua a refletir **impacto e criticidade do sistema**, não atributos internos do risco.
- Os **atributos do risco** influenciam:
  - requisitos de segurança (Cap. 02);
  - threat modeling (Cap. 03);
  - decisões arquiteturais (Cap. 04);
  - critérios de aceitação e evidência;
  - governação e auditoria (Cap. 14).

Este modelo permite que o manual evolua **sem necessidade de redefinir conceitos-base** sempre que surgem novas formas de automação ou abstração.

---

## ✅ Conclusão

O SbD-ToE trata o risco como um **conceito único**, rico em atributos, capaz de capturar tanto riscos técnicos clássicos como riscos introduzidos por práticas modernas de desenvolvimento.

Esta abordagem:
- evita fragmentação conceptual;
- suporta definição proporcional de controlos;
- mantém o manual intemporal;
- reforça a exigência de responsabilidade, validação e evidência.

Os capítulos seguintes assumem este modelo como **pressuposto canónico**.
