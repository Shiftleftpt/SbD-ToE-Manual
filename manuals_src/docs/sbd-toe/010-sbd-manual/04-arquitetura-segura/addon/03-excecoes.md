---
id: excecoes
sidebar_position: 3
title: 📌 Exceções Justificadas aos Requisitos Arquiteturais
description: Processo formal para submissão, avaliação e controlo de exceções a requisitos de arquitetura segura
---

# 📌 Exceções Justificadas aos Requisitos Arquiteturais

Este documento define o processo para **submeter, aprovar, documentar e controlar exceções** aos requisitos de arquitetura segura (ARC-001 a ARC-011) definidos neste capítulo.

> Nenhuma exceção pode ser aceite sem registo, justificação, aprovação e plano de revisão.

---

## 🔍 Quando podem existir exceções justificadas

- Limitações técnicas ou operacionais temporárias
- Migração faseada entre ambientes ou arquiteturas
- Integração de componentes herdados ou de terceiros
- Custo desproporcional para risco L1

> Em todos os casos, deve existir plano de revisão com horizonte temporal claro e medidas compensatórias.

---

## ✏️ Critérios de aceitação de exceção

| Critério                                   | Aplicação obrigatória |
|--------------------------------------------|-------------------------|
| Justificação técnica documentada             | Sim                     |
| Risco associado identificado e aceite       | Sim                     |
| Mitigação parcial ou compensatória prevista | Sim                     |
| Horizonte temporal definido (expiração)     | Sim                     |
| Responsável nomeado                        | Sim                     |
| Revisão periódica obrigatória               | L2 e L3                 |

---

## 📄 Modelo de registo de exceção

| Campo                     | Exemplo                                                   |
|--------------------------|-----------------------------------------------------------|
| Requisito afetado        | ARC-002 - Fronteiras técnicas entre zonas de confiança     |
| Aplicação / componente     | API Publica - Integração Parceiros                    |
| Justificação            | Gateway externo ainda não integrado no ambiente interno   |
| Mitigação alternativa    | ACLs temporárias + monitorização + logging reforçado     |
| Validade                 | 3 meses (expira a 2025-11-01)                             |
| Responsável             | Arquiteto da Solução + CISO                             |
| Revisão agendada         | Sim (em Q4 2025)                                          |

---

## 🌐 Integração com rastreabilidade e auditoria

- Todas as exceções devem ser incluídas na matriz de rastreabilidade
- Devem ser mantidas como **artefactos formais** no repositório do projeto
- A aprovação deve ser atribuída a um perfil com autoridade formal (ex: AppSec, Arquitetura)

> ✉️ Exceções não documentadas ou com validade expirada devem ser tratadas como não conformidade crítica.

---

## 🏛️ Alinhamento normativo

- **ISO/IEC 27001 A.18.1.4** - Aceitação formal de riscos residuais
- **SSDF GV.3** - Aprovar exceções e desviações de processos de segurança
- **OWASP SAMM Governance** - Registo e ciclo de vida de decisões excecionais

---
