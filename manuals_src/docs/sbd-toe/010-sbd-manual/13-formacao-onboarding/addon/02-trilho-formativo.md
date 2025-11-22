---
id: trilho-formativo
title: Trilho de Formação por Nível de Risco
description: Caminho formativo adaptado ao nível de risco (L1–L3) e ao perfil técnico de cada colaborador.
tags: [formacao, onboarding, perfis, risco, trilho]
---


# 🎓 Trilhos Formativos por Função e Risco

## 🌟 Objetivo

Definir os **conteúdos mínimos obrigatórios** a incluir na formação inicial (onboarding) e contínua, por perfil funcional e **nível de risco da aplicação**, em alinhamento com o Capítulo 01 - Gestão de Risco.

> 📌 Esta matriz permite configurar trilhos formativos coerentes em plataformas como LMS, portais internos, backlog técnico ou pipelines de permissões.

---

## 🧬 O que é um Trilho Formativo

Um **trilho formativo** é um conjunto de conteúdos obrigatórios ou recomendados atribuídos a um colaborador ou função, com base no seu papel técnico e no risco da aplicação em que participa. Estes trilhos permitem alinhar o conhecimento com as exigências de segurança específicas do projeto.

---

## 📋 Matriz Base por Perfil e Nível de Risco

| Função / Risco | L1 (baixo)                                    | L2 (médio)                                                  | L3 (elevado)                                                          |
|----------------|-----------------------------------------------|-------------------------------------------------------------|------------------------------------------------------------------------|
| **Dev**        | Secure coding básico, dependências            | Threat modeling leve, SCA, PR seguro                        | Threat modeling formal, arquitetura segura, labs em apps vulneráveis |
| **QA**         | Testes de segurança básicos                   | Critérios de aceitação, fuzzing leve                        | Fuzzing avançado, validação de exceções, SAST/DAST                    |
| **PO**         | Requisitos mínimos, backlog seguro            | Classificação de risco, exceções justificadas               | Processo formal de aceitação, revisão com AppSec                      |
| **DevOps**     | Gestão de segredos, configuração de ambientes | Integração segura no CI/CD, pipelines com scanners          | SLSA, proveniência, alertas contínuos, hardening                      |
| **AppSec**     | -                                             | Ferramentas base, políticas internas                        | Aprofundamento técnico, coaching a equipas, threat modeling avançado |
| **Terceiros**  | Política da organização, canais de apoio      | Requisitos mínimos, PR template seguro                      | Formação customizada, acesso condicionado, registo formal             |

---

## 🛠️ Como aplicar

- Instanciar a matriz em:
  - 🎓 Trilhos no sistema de gestão de aprendizagem (LMS)
  - 📋 Checklists de onboarding por função
  - 📦 Tarefas em backlog técnico (ex: `formacao:secure-coding`)
- Garantir:
  - Atribuição explícita por projeto e função
  - Registo formal de conclusão (LMS, ticket, assinatura)
  - Atualizações regulares face a novos riscos ou tecnologias

---

## ✅ Boas práticas

- Incorporar os trilhos formativos no plano de formação anual da organização
- Rever os conteúdos com base em lições aprendidas de incidentes
- Ajustar os trilhos com base no feedback de champions e equipas técnicas
- Ligar os trilhos aos perfis de permissões ou acesso a ambientes

---

## 📎 Referências cruzadas

| Documento                         | Relevância                                       |
|-----------------------------------|--------------------------------------------------|
| `01-catalogo-formativo.md`        | Define os tópicos de formação por capítulo       |
| `10-checklist-onboarding.md`      | Usa esta matriz como base para verificação       |
| `03-programa-champions.md`        | Champions ajudam a manter e ajustar os trilhos   |
| `90-indicadores-metricas.md`      | Mede a cobertura e adesão aos trilhos            |

---

> 🔒 Esta matriz operacionaliza a **aplicação proporcional do SbD-ToE**, garantindo que todos os intervenientes recebem formação adequada ao seu papel e ao risco envolvido.
