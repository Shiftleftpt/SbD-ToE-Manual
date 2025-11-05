---
id: ameacas-mitigadas
title: Ameaças Mitigadas - Governança e Contratação
sidebar_position: 50
description: Tabela de ameaças mitigadas pelas práticas de exceções, rastreabilidade, onboarding e validação formal descritas neste capítulo
tags: [ameacas, governance, rastreabilidade, excecoes, contratos, osc&r, dsomm]
---


# 🔐 Ameaças Mitigadas - Capítulo 14: Governança e Contratação Segura

Este capítulo define práticas formais para **garantir que a segurança é aplicada de forma consistente e rastreável a nível organizacional**, incluindo:

- Contratação de serviços e fornecedores;
- Acordos e cláusulas contratuais;
- Modelos de validação e maturidade;
- Governança contínua, rastreabilidade e tratamento do legado.

> 📌 Este capítulo **não mitiga falhas técnicas diretamente**, mas **controla a superfície de ataque organizacional**, onde decisões erradas de contratação, governação ou aceitação de risco afetam todos os sistemas.

---

## 🧯 Categoria 1 - Adoção de software ou serviços inseguros

| Ameaça                                 | Fonte                                  | Como surge                                         | Como a prática mitiga                                                             | Controlos associados                         |
|----------------------------------------|-----------------------------------------|----------------------------------------------------|------------------------------------------------------------------------------------|----------------------------------------------|
| Adoção de fornecedor sem avaliação     | NIST 800-161 / SSDF PM.3 / DSOMM       | Equipa contrata serviço sem validação de segurança | Modelo de validação contínua e proporcional por tipo de fornecedor               | `addon/03-modelo-validacao-fornecedores.md`  |
| Falta de cláusulas contratuais         | ISO 27001 A.15 / SSDF PO.3 / DSOMM     | Contrato não exige práticas de segurança           | Conjunto prescritivo de cláusulas para segurança, confidencialidade, rastreio     | `addon/02-clausulas-contratuais.md`          |
| Uso de serviços sem rastreio           | ENISA / BSIMM / DSOMM                  | Equipa não tem registo de origem ou aprovações     | Rastreabilidade organizacional com ownership formal                              | `addon/04-rastreabilidade-organizacional.md` |

---

## 🧱 Categoria 2 - Governança inconsistente ou ineficaz

| Ameaça                                   | Fonte                              | Como surge                                           | Como a prática mitiga                                                           | Controlos associados                        |
|------------------------------------------|-------------------------------------|------------------------------------------------------|----------------------------------------------------------------------------------|---------------------------------------------|
| Iniciativas paralelas sem coordenação    | OWASP SAMM / BSIMM Governance       | Áreas técnicas atuam sem alinhamento                 | Modelo de governança com papéis, fóruns, fluxo de decisão                       | `addon/01-modelo-governancao.md`           |
| Falta de continuidade organizacional     | ISO 27001 / ENISA                   | Segurança dependente de pessoas ou equipas isoladas  | Integração de segurança como função de processo com maturidade definida         | `addon/07-governancao-e-maturidade.md`     |
| Risco de decisões legadas sem controlo   | CAPEC-310 / OWASP                   | Tecnologias antigas mantidas por inércia             | Processo formal de governação de legado e exceções documentadas                | `addon/10-governanca-legada.md`            |

---

## 🔄 Categoria 3 - Falta de revisão e validação contínua

| Ameaça                                        | Fonte                             | Como surge                                            | Como a prática mitiga                                                            | Controlos associados                          |
|-----------------------------------------------|------------------------------------|-------------------------------------------------------|-----------------------------------------------------------------------------------|------------------------------------------------|
| Decisões não revistas com mudança de contexto | ISO 27005 / SSDF RM.1 / BSIMM     | Fornecedor ou contrato mantido sem reavaliação       | Ciclo de revisão contínua com critérios de reteste ou revalidação                | `addon/06-validacao-continuada.md`            |
| Falta de governança em decisões históricas    | NIST 800-30 / DSOMM               | Adoção de prática sem base rastreável                 | Integração com rastreabilidade organizacional e critérios objetivos              | `addon/04`, `addon/06`                         |

---

## 🧠 Categoria 4 - Ausência de maturidade e rastreabilidade estratégica

| Ameaça                                   | Fonte                             | Como surge                                           | Como a prática mitiga                                                           | Controlos associados                          |
|------------------------------------------|------------------------------------|------------------------------------------------------|----------------------------------------------------------------------------------|------------------------------------------------|
| Falta de conhecimento sobre o estado de segurança | OWASP SAMM / ISO 27004 / DSOMM     | Falta de modelo de referência                        | Modelo de maturidade e autoavaliação formal                                    | `addon/07-governancao-e-maturidade.md`        |
| Estratégia de segurança desarticulada   | ENISA / BSIMM Strategy / DSOMM     | Iniciativas reativas ou não sustentadas              | Integração com KPIs, governance boards e decisão por risco                      | `30`, `90`                         |

---

## 🚫 Categoria 5 - Falha de enforcement organizacional

| Ameaça                                        | Fonte                        | Como surge                                                     | Como a prática mitiga                                                                  | Controlos associados                              |
|-----------------------------------------------|-------------------------------|----------------------------------------------------------------|-----------------------------------------------------------------------------------------|---------------------------------------------------|
| Segurança definida mas não aplicada           | DSOMM Governance              | Falta de owners, exceções não justificadas                    | Governação com owners atribuídos, exceções formais, revalidações obrigatórias          | `addon/01`, `addon/05`, `addon/06`, `60`     |
| Políticas de segurança não institucionalizadas| DSOMM Policies / ISO 27001 A.5| Políticas existem mas não são formalmente aplicadas ou auditadas| Políticas organizacionais auditáveis com ligação direta a contratos e exceções         | `60-politicas-recomendadas.md`              |

---

## ✅ Conclusão

O Capítulo 14 mitiga um conjunto vasto de **ameaças estruturais e organizacionais** que não estão presentes no código ou infraestrutura, mas que:

- Condicionam diretamente a eficácia da segurança técnica;
- Criam **riscos invisíveis** relacionados com decisões mal documentadas ou não validadas;
- Afetam **a cadeia de fornecimento, contratos, ownership e accountability organizacional**.

> ✅ Mitiga diretamente **12+ ameaças organizacionais críticas**, com base em fontes como **OWASP DSOMM, ISO 27001, SSDF, BSIMM, ENISA, CAPEC** e outras taxonomias reconhecidas.

> 📌 Este capítulo constitui o **principal pilar de enforcement e rastreabilidade organizacional do SbD-ToE**, garantindo que a segurança não é apenas definida - mas também validada, aplicada e sustentada por estruturas formais.
