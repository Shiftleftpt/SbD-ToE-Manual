---
id: inclusao-terceiros
title: Modelo de Inclusão de Terceiros e Fornecedores
description: Procedimento padronizado para onboarding seguro de terceiros, com formação mínima exigida.
tags: [terceiros, onboarding, formacao, rastreabilidade, inclusao]
---


# 🤝 Inclusão de Terceiros em Programas de Formação {formacao-onboarding:addon:inclusao-terceiros}

Este documento define uma abordagem prática e verificável para garantir que **fornecedores externos, contractors e outsourcing** estão devidamente integrados nos programas de formação em segurança, antes de obterem acesso técnico a projetos, sistemas ou dados sensíveis.

---

## 🎯 Objetivo {formacao-onboarding:addon:inclusao-terceiros#objetivo}

- **Uniformizar critérios de formação** para elementos externos com impacto técnico
- Evitar disparidades de segurança entre equipas internas e externas
- **Garantir rastreabilidade e responsabilização** em auditorias e pós-incidente
- Formalizar a formação como **pré-condição para acesso técnico**

---

## ✅ Requisitos mínimos aplicáveis {formacao-onboarding:addon:inclusao-terceiros#requisitos_minimos_aplicaveis}

Cada terceiro (indivíduo ou organização) deve cumprir os seguintes pontos **antes de obter permissões técnicas**:

| Requisito                                                                                   | Obrigatório? |
|---------------------------------------------------------------------------------------------|--------------|
| Assinatura de termo de responsabilidade (pode ser digital)                                  | ✔️           |
| Atribuição formal de trilho formativo conforme função técnica                               | ✔️           |
| Conclusão e validação da formação (ex: quiz, PR validado)                                   | ✔️           |
| Registo de formação num repositório validado (projeto, LMS, GitHub, etc.)                   | ✔️           |
| Sessão de integração com elemento interno (ex: AppSec, PO, Champion)                        | ✔️           |

---

## 🧩 Modalidades práticas por tipo de terceiro {formacao-onboarding:addon:inclusao-terceiros#modalidades_praticas_por_tipo_de_terceiro}

| Tipo de terceiro         | Modalidade formativa sugerida                                      | Registo esperado                        |
|--------------------------|---------------------------------------------------------------------|------------------------------------------|
| Contractor individual    | Trilho técnico + quiz online + validação de PR                     | Checkpoint no onboarding                 |
| Fornecedor com equipa    | Sessão síncrona + conteúdos partilhados (LMS, repositório interno) | Lista de presenças + evidência por user |
| Outsourcing contínuo     | Formação formal com cláusula contratual + controlo por SLA         | Contrato + logs LMS                     |

---

## 🧭 Boas práticas de implementação {formacao-onboarding:addon:inclusao-terceiros#boas_praticas_de_implementacao}

- Incluir referência ao **Capítulo 13 – Formação** no processo de contratação
- Formalizar exigências via **Capítulo 14 – Governança e Contratação**
- Manter um **repositório interno de evidência de onboarding de terceiros**
- Garantir que os **Champions** ou AppSec estão envolvidos na receção de terceiros
- Prever **auditorias periódicas** de formação em fornecedores críticos

---

## 🔗 Ligações a outros documentos {formacao-onboarding:addon:inclusao-terceiros#ligacoes_a_outros_documentos}

| Documento                         | Relevância                                   |
|-----------------------------------|----------------------------------------------|
| `03-checklist-onboarding.md`      | Aplicável também a terceiros com acesso técnico |
| `trilho-formativo.md`            | Define os trilhos a aplicar por função        |
| `14-governanca-contratacao.md`   | Formaliza exigências via cláusulas contratuais |

---

> 🔐 Garantir que terceiros estão formados **não é uma cortesia — é uma obrigação de segurança organizacional.**
>  
> A aplicação deste modelo contribui diretamente para a redução de riscos de supply chain e exposição por má prática externa.
