---
description: Processo formal de exceção e aceitação de risco associado a requisitos
id: gestao-excecoes
tags:
- excecoes
- exceções
- políticas
- requisitos
- risco
- validacao
- validação
title: Gestão de Exceções a Requisitos de Segurança
---


# ⚠️ Gestão de Exceções a Requisitos de Segurança

## 🌟 Objetivo

Estabelecer um processo claro e controlado para tratar situações em que um ou mais **requisitos de segurança aplicacionais definidos no catálogo não possam ser aplicados na totalidade** a um determinado projeto, funcionalidade ou componente.

Este processo assegura que:

- A **não aplicação de um requisito é sempre conhecida, justificada e controlada**;
- **Limitações técnicas, operacionais ou contextuais** não se tornam falhas silenciosas;
- **Medidas compensatórias** são avaliadas e documentadas;
- A rastreabilidade e auditabilidade são preservadas.

---

## 🧭 Quando aplicar

A consideração de exceções pode ser aceitável nos seguintes casos:

- **Dependência externa incontrolável**  
  Ex: sistema legado ou SaaS sem suporte a MFA.
- **Custo técnico desproporcional ao risco**  
  Ex: controlo não viável num MVP de baixo impacto.
- **Conflito funcional ou contratual documentado**
- **Falta temporária de recurso ou suporte**, com plano de mitigação associado.

> ❗️ Exceções não podem ser tratadas informalmente. Mesmo que aprovadas, devem ser **documentadas, justificadas e revistas** periodicamente.

---

## 🛠️ Como aplicar

O processo de gestão de exceções deve incluir os seguintes passos e elementos:

### 1. Identificação

- Qual o requisito em causa? (ex: `SEC-L2-AUTH-MFA`)
- Em que componente ou funcionalidade a exceção se aplica?

### 2. Justificação formal

- Qual o motivo técnico, organizacional ou externo que impede a aplicação?
- A exceção é temporária ou estrutural?

### 3. Avaliação de impacto

- Qual o risco residual criado pela exceção?
- Que tipo de ameaça deixa de estar mitigada?

### 4. Medidas compensatórias

- Que controlos alternativos estão ou podem ser aplicados?
  - Ex: logging reforçado, monitorização de comportamento, controlo de acesso externo.

### 5. Aprovação formal

- Quem autoriza a exceção?
  - Idealmente: **segurança + dono do produto + gestão**.
- A aprovação é por tempo indeterminado? Há data de reavaliação?

### 6. Registo e evidência

- Onde fica registada a exceção? (ex: Jira, Confluence, registo de segurança).
- Como é ligada ao requisito original e ao projeto?

---

## 📆 Validade e revisão periódica

- Toda exceção deve ter **prazo máximo de validade ou trigger de revisão**, como:
  - Período fixo (ex: 6 meses);
  - Alteração funcional relevante;
  - Incidente de segurança relacionado.

- Exceções devem ser revistas em:
  - Auditorias internas;
  - Mudanças de arquitetura;
  - Avaliações formais de risco.

---

## 📎 Referências cruzadas

Este processo está diretamente ligado a outros elementos do capítulo:

| Documento relacionado                  | Função na gestão de exceções                          |
|----------------------------------------|--------------------------------------------------------|
| [Catalogo Requisitos](./catalogo-requisitos)      | Requisitos que podem ter exceções associadas           |
| [Controlos por niveis](./matriz-controlos-por-risco) | Classificação do risco e criticidade do requisito    |


---

## ✅ Boas práticas

- Tratar exceções como excecionais, não como norma;
- Usar o número de exceções por projeto como **indicador de maturidade**;
- Garantir que cada exceção tem:
  - **ID único**
  - **Descrição clara**
  - **Prazo definido**
  - **Responsável designado**
- Assegurar que todas as exceções estão ligadas a artefactos e justificações verificáveis.

> 📌 Exceções não anulam o modelo. Tornam-no mais robusto - porque permitem reconhecer e controlar o que não é possível aplicar totalmente, sem esconder falhas ou informalidades.
