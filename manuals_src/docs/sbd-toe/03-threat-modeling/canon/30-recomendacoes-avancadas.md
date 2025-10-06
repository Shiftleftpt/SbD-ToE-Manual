---
id: rastreabilidade
title: Rastreabilidade — Threat Modeling
description: Mapeamento das práticas de threat modeling com requisitos normativos e capítulos fundacionais
tags: [rastreabilidade, ssdf, samm, requisitos, controlo, normativo]
---

# 🔗 Rastreabilidade — Threat Modeling {threat-modeling:canon:rastreabilidade}

Este documento estabelece a rastreabilidade entre as práticas de *Threat Modeling* descritas neste capítulo e os requisitos normativos, frameworks de referência e capítulos fundacionais do manual SbD-ToE.

---

## 📐 Rastreabilidade para Capítulos Basilares {threat-modeling:canon:rastreabilidade#rastreabilidade_para_capitulos_basilares}

| Elemento                                   | Referência                           | Relação com este capítulo                               |
|--------------------------------------------|--------------------------------------|----------------------------------------------------------|
| Catálogo de Requisitos Aplicacionais       | Capítulo 2 – Requisitos de Segurança | Ameaças identificadas devem mapear para requisitos       |
| Avaliação de Risco e Classificação         | Capítulo 1 – Gestão de Risco         | Define quando o threat modeling é exigido (ex: apps L2+) |
| Processo de Validação e Justificação       | Capítulo 2 – Validação de Requisitos | Mitigações devem ser validadas ou justificadas formalmente |

---

## 🧩 Rastreabilidade para Normas e Frameworks {threat-modeling:canon:rastreabilidade#rastreabilidade_para_normas_e_frameworks}

| Fonte / Norma      | Referência                       | Prática associada em Threat Modeling                 |
|--------------------|----------------------------------|------------------------------------------------------|
| NIST SSDF          | PW.3.1 / RV.1.1                  | Identificação e documentação de ameaças              |
| OWASP SAMM         | Design → Threat Assessment       | Sessões formais, regulares, com outputs rastreáveis  |
| BSIMM13            | AA1.1, AA1.2, AA2.1              | Modelação de ameaças e revisão contínua de diagramas |
| ISO/IEC 27005      | Sec. 8.2 / 8.3                   | Identificação e avaliação de riscos                  |
| ENISA SDLC         | Threat Modeling Integrado        | Integração em fases de design e desenvolvimento      |
| SLSA (nível 3+)    | Risk Awareness (indireto)        | Contribuição para cadeia de confiança                |

---

## 🎯 Rastreabilidade para Requisitos (Cap. 2) {threat-modeling:canon:rastreabilidade#rastreabilidade_para_requisitos_cap_2}

A modelação de ameaças permite **confirmar ou gerar** os seguintes tipos de requisitos do Capítulo 2:

| Categoria de Requisito         | Exemplo relacionado com TM                                |
|--------------------------------|-------------------------------------------------------------|
| Autenticação e Sessões         | Exigir MFA, proteger endpoints críticos identificados       |
| Controlo de Acesso             | Aplicar RBAC com base em claims, como visto no exemplo JWT  |
| Tratamento de Erros            | Validar que erros não expõem detalhes técnicos              |
| Logging e Auditoria            | Confirmar que há registo de eventos sensíveis               |
| Privacidade e Dados Pessoais   | Aplicar LINDDUN para casos com RGPD                         |

---

## 📦 Rastreabilidade para Outputs Operacionais {threat-modeling:canon:rastreabilidade#rastreabilidade_para_outputs_operacionais}

| Output gerado                        | Mapeamento de rastreio                         | Onde aplicar                                                 |
|-------------------------------------|------------------------------------------------|--------------------------------------------------------------|
| Modelo de ameaças (DFD + STRIDE)   | Relacionado com requisitos + controlos         | Documentação técnica, repositório, backlog                   |
| Plano de mitigação                 | Mapeado a requisitos ou justificação de exceções| Backlog, controlo de risco, auditorias                       |
| Decisões e exceções documentadas   | Ligação ao Catálogo de Riscos do Cap. 1         | Justificações de risco aceite, revisão por stakeholders      |

---

## 🧭 Considerações Finais {threat-modeling:canon:rastreabilidade#consideracoes_finais}

A rastreabilidade entre *threat modeling*, requisitos e controlo de risco é essencial para garantir:

- Coerência entre análise e medidas aplicadas
- Justificação de decisões de segurança
- Conformidade com frameworks e auditorias
- Reutilização de conhecimento e modelos validados

> O threat modeling não é um artefacto isolado: deve estar ligado à cadeia de valor da segurança por design.

---
