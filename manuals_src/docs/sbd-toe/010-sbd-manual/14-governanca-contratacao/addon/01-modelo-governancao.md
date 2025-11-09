---
id: modelo-governancao
title: Modelo de Governação para Segurança Aplicacional
sidebar_position: 1
description: Definição de papéis formais, responsabilidades e fluxo de decisão de segurança aplicacional
tags: [governanca, ownership, excecoes, validacao]
---



# 🧱 Modelo de Governação para Security by Design

## 🌟 Objetivo

Estabelecer uma **estrutura formal de decisão, validação e responsabilização**, que permita aplicar de forma coerente e sustentada as práticas definidas no modelo SbD-ToE em toda a organização.

Este modelo assegura que:

- A classificação de risco orienta decisões formais;
- A aplicação de requisitos é exigida, não opcional;
- A aceitação de risco, exceções e compensações é rastreável;
- Existe uma cadeia clara de **responsabilização técnica, funcional e executiva**.

---

## 👥 Papéis e responsabilidades

A aplicação prática do SbD-ToE depende de papéis bem definidos, atribuídos formalmente e mantidos atualizados.

| Papel / Função         | Responsabilidades principais                                                                 |
|------------------------|-----------------------------------------------------------------------------------------------|
| **AppSec / Segurança** | Definir critérios mínimos, aprovar controlos aplicados, validar exceções, consolidar evidência |
| **Arquitetura**        | Garantir que as decisões de risco se traduzem em opções técnicas coerentes                   |
| **Gestor de Produto**  | Priorizar requisitos de segurança, propor compensações ou aceitar impacto                     |
| **Equipa de DevOps**   | Aplicar controlos no pipeline, monitorizar conformidade técnica                               |
| **GRC / CISO**         | Supervisionar decisões de risco, manter políticas e indicadores de adoção                     |
| **Compras / Legal**    | Incorporar requisitos e cláusulas de segurança nos contratos com fornecedores                 |

> ✅ Estes papéis devem estar descritos em políticas formais e modelos internos de governação.

---

## 🛠️ Como aplicar

### 📌 Decisões típicas com governação formal

- Aceitação de risco quando controlos mínimos não são aplicados;
- Aprovação de exceções a práticas dos capítulos técnicos;
- Validação de compensações (ex: mitigação alternativa ou temporária);
- Aprovação de fornecedores com desvios ou lacunas de segurança;
- Escalonamento de desvios detetados em release ou produção.

### 🗂️ Evidência e rastreabilidade

Cada decisão deve incluir:

- Identificação da aplicação, risco e controlos;
- Justificação técnica e organizacional;
- Responsável pela decisão (nome e função);
- Validade (temporária ou permanente);
- Referência à evidência (scanner, revisão, formulário de exceção).

> Pode usar-se um sistema formal (Jira, wiki versionado, SharePoint, etc.) para registo estruturado.

---

## 🔁 Ciclo típico de governação

1. Classificação de risco atribuída (Cap. 1);
2. Seleção de requisitos mínimos aplicáveis (Cap. 2);
3. Validação da aplicação efetiva dos controlos;
4. Registo de exceções ou compensações;
5. Aprovação formal (conforme criticidade);
6. Revisão periódica ou auditoria planeada.

> Este ciclo repete-se por release, projeto, contrato ou mudança de risco.

---

## 📄 Documentação recomendada

- **Política de Segurança by Design** (papéis, princípios e obrigações);
- **Modelo de Decisão de Risco** (níveis de risco e alçada de aprovação);
- **Template de exceções** (campos obrigatórios e evidência);
- **Registo de owners por aplicação/projeto**.

---

## ✅ Boas práticas

- Formalizar o modelo por escrito e com validação executiva;
- Exigir a justificação e aprovação formal de exceções;
- Atribuir claramente o owner de segurança por projeto;
- Consolidar decisões num repositório rastreável;
- Rever periodicamente as decisões e exceções ativas.

---

## 🔗 Referências cruzadas

| Documento / Capítulo         | Relação com este modelo                             |
|------------------------------|-----------------------------------------------------|
| Capítulo 01 - Gestão de Risco | Ponto de partida: classificação de risco           |
| Capítulo 02 - Requisitos     | Define os requisitos aplicáveis por nível           |
| Capítulo 06 - Desenvolvimento Seguro | Implica validações formais                     |
| addon/06-validacao-continuada.md | Aplica a lógica de reavaliação e exceções        |
| canon/20-checklist-revisao.md | Verifica aplicação real da governação              |

---
