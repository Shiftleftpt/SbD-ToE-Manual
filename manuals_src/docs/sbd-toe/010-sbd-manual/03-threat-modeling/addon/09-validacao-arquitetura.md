---
id: validacao-arquitetura
title: Integração do Threat Modeling na Validação de Arquitetura
description: Como integrar práticas de threat modeling nos artefactos de arquitetura técnica e processos de aprovação
tags: [arquitetura, rastreabilidade, revisão técnica, threat modeling, validacao]
---

# 🏗️ Integração do Threat Modeling na Validação de Arquitetura

## 🌟 Objetivo

Definir como incorporar o *Threat Modeling* de forma estruturada no processo de **revisão técnica e validação de arquitetura**, garantindo que:

- A análise de ameaças é etapa obrigatória na validação técnica;
- Os artefactos de arquitetura incluem os resultados do threat modeling;
- Existe rastreabilidade entre arquitetura, ameaças e requisitos de segurança (Cap. 2).

---

## 📁 Artefactos a validar

Este processo está alinhado com as prescrições do **Capítulo 4 - Arquitetura Segura**, que define os artefactos mínimos exigidos para validação técnica:

| Artefacto de arquitetura     | Deve conter…                                    | Validado por…               |
| ---------------------------- | ----------------------------------------------- | --------------------------- |
| Diagrama de Componentes      | Trust boundaries, fluxos sensíveis              | Arquiteto + Segurança       |
| Documento de Solução Técnica | Sumário de ameaças + mitigação ou justificação  | AppSec / PO / Equipa Dev    |
| Ficha de Release             | Confirmação de controlo implementado por ameaça | Owner técnico + QA          |
| Ficha de Exceções            | Justificações formais de riscos não mitigados   | Segurança + Gestão de Risco |

---

## ✅ Critérios de aceitação para validação técnica

| Item obrigatório                           | Fonte                                | Verificado? |
| ------------------------------------------ | ------------------------------------ | ----------- |
| Modelo de ameaça completo                  | DFD, STRIDE, LINDDUN ou PASTA        | ☐           |
| Ameaças mapeadas a requisitos do Cap. 2    | Ficheiro `threats.yaml` ou IriusRisk | ☐           |
| Mitigações definidas e testadas            | `mitigations.md`, backlog, testes    | ☐           |
| Riscos aceites justificados e documentados | `decisions.md` ou IriusRisk          | ☐           |
| Participação de Segurança na validação     | Registo de presença / revisão        | ☐           |

---

## 🧭 Quando aplicar

| Situação                                  | Requisito de validação com threat modeling   |
| ----------------------------------------- | -------------------------------------------- |
| Nova aplicação crítica                    | ✅ Obrigatório                                |
| Alteração de arquitetura existente        | ✅ Obrigatório                                |
| Integração com sistemas externos          | ✅ Obrigatório                                |
| Refatoração técnica sem impacto funcional | ⚠️ Recomendado (caso afete fluxos sensíveis) |

---

## 🔄 Integração com o ciclo de vida

Este processo deve articular-se com o **Capítulo 6 - Desenvolvimento Seguro**, garantindo que:

- A validação de arquitetura ocorre antes do desenvolvimento iniciar (gate técnico);
- O threat model está disponível para revisão e incluído como deliverable do projeto;
- Alterações ao sistema requerem atualização do modelo e revalidação (trigger automático);
- O status de validação pode ser visível no backlog, ADO, GitHub ou ferramenta de gestão.

---

## ✅ Boas práticas

- Tornar o threat model um entregável obrigatório nos projetos críticos;
- Usar ferramentas que integrem threat modeling e documentação técnica (ex: IriusRisk, PlantUML, Draw.io);
- Garantir que as decisões de exceção são formalizadas com justificativa, owner e prazo;
- Incorporar revisores de segurança nas etapas de arquitetura (design review);
- Automatizar a verificação de artefactos e validação mínima como parte do CI/CD.

---

> A integração do threat modeling na arquitetura não é opcional em contextos críticos - é parte integrante da decisão técnica informada e da rastreabilidade de segurança.
