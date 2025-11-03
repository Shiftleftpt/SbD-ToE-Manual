---
id: guidelines-equipa
title: Guidelines de Equipa e Práticas Partilhadas
sidebar_position: 7
description: Documentação e alinhamento de práticas de segurança entre equipas, promovendo coerência e baseline técnico comum
tags: [equipa, guidelines, alinhamento, práticas seguras, segurança]
---


# 🤝 Guidelines de Equipa e Práticas Partilhadas

> 💡 **Nota prática**:  
> A disseminação de práticas seguras de desenvolvimento depende não só de regras técnicas, mas também de **cultura, exemplos práticos e partilha ativa entre elementos da equipa**.  
> Plataformas como **Confluence, GitHub Wiki, Notion, Google Docs** ou mesmo ficheiros Markdown versionados no repositório podem ser usadas para manter guidelines acessíveis e contextualizadas.  
> Estas guidelines devem evoluir com o tempo e refletir tanto a política organizacional como os erros e melhorias reais observados nos projetos.

---

## 📌 Objetivos

- Consolidar e difundir as práticas seguras de desenvolvimento entre os elementos da equipa.
- Reduzir a dependência de validações manuais repetitivas.
- Tornar explícitas as decisões de segurança recorrentes e os critérios de validação técnica.
- Apoiar o onboarding técnico de novos programadores.
- Promover melhoria contínua e documentação viva.

---

## 👥 Quem deve aplicar

- **Toda a equipa de desenvolvimento**: contribui para a melhoria e adoção das guidelines.
- **Responsáveis técnicos (tech leads, senior devs)**: curadoria, validação e atualização regular.
- **Segurança / AppSec**: garante alinhamento com políticas organizacionais.

---

## ⏱️ Quando aplicar

- Durante o planeamento técnico inicial de um projeto ou componente.
- Como parte do onboarding de novos elementos da equipa.
- Após incidentes, revisões ou auditorias internas.
- Sempre que surgirem padrões recorrentes de falhas ou exceções.

---

## 🧱 Requisitos recomendados

1. **Documentar práticas seguras, exemplos e padrões aceites**
   - Por stack tecnológica ou tipo de aplicação (frontend, backend, API, etc.)

2. **Manter as guidelines versionadas e acessíveis**
   - Idealmente junto ao código ou numa base de conhecimento integrada.

3. **Atualizar as guidelines com base em erros reais**
   - Incluir exemplos reais de findings e como os evitar ou corrigir.

4. **Integrar as guidelines nos rituais da equipa**
   - Ex: review semanal, pull request clinic, tech talks ou retros.

5. **Promover a partilha entre equipas**
   - Reutilizar padrões, snippets seguros, anti-patterns evitáveis.

---

## ✅ Como validar

- Referência explícita às guidelines nos templates de PR.
- Inclusão de link para secção da guideline relevante em revisões técnicas.
- Registos de revisão e atualização periódica do documento.
- Adoção visível nos exemplos de código e nos projetos mais recentes.

---

## 🧾 Como evidenciar

- Repositório de `guidelines/` versionado por projeto ou por stack.
- Wiki ou documento partilhado com histórico de revisões.
- Mapeamento entre findings recorrentes e secções da guideline.
- Inclusão no plano de onboarding ou no checklist de novos membros.

---

## 🔄 Ligação a outras práticas

| Tema                                | Ficheiro associado               |
|-------------------------------------|----------------------------------|
| Boas práticas de codificação segura | `addon/01-boas-praticas-codigo.md` |
| Validação por linters e revisores   | `addon/02-linters-validacoes.md`, `addon/08-validacoes-codigo.md` |
| Justificação de exceções            | `addon/05-excecoes-e-justificacoes.md` |
| Rastreabilidade de validações       | `addon/09-anotacoes-evidencia.md` |

---

> 📌 As guidelines são o elo entre a política organizacional e a prática concreta da equipa.  
> Devem ser úteis, vivas e continuamente melhoradas com base na realidade técnica dos projetos.
