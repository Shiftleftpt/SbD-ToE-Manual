---
id: ameacas-mitigadas
title: Ameaças Mitigadas
description: Ameaças mitigadas pela definição e validação estruturada de requisitos de segurança
tags: [ameaças, mitigação, requisitos, rastreabilidade, exceções, validação, SSDF, DSOMM, OSC&R, CAPEC]
sidebar_position: 50
---


# 🔐 Ameaças Mitigadas - Capítulo 02: Requisitos de Segurança

Este capítulo define o **catálogo base de requisitos de segurança aplicacionais** do modelo SbD-ToE, bem como os mecanismos de validação, exceção e rastreabilidade.  
As ameaças mitigadas estão diretamente ligadas à **ausência, má definição, aplicação inconsistente ou aceitação informal de requisitos de segurança.**

> 📌 Este capítulo é **um dos principais pilares de controlo técnico do modelo SbD-ToE**, sendo aplicado a todos os projetos conforme o seu nível de risco.

---

## 📚 Categoria 1 – Falha na definição ou ausência de requisitos

| Ameaça                                 | Fonte                                                  | Como surge                                         | Como a prática mitiga                                                            | Controlos associados                      | 🧩 Mitigada apenas por este capítulo? |
|----------------------------------------|---------------------------------------------------------|----------------------------------------------------|-----------------------------------------------------------------------------------|-------------------------------------------|----------------------------------------|
| Ausência de requisitos de segurança    | DSOMM – Design & Development / SSDF PW.1 / ASVS V1.1    | Segurança não está incluída nas histórias ou specs | Catálogo completo, taxonomia clara, rastreável por categoria e risco             | `addon/01-catalogo-requisitos.md`        | ✅                                     |
| Definição ambígua ou não testável      | OWASP SAMM / ISO 27034                                  | Requisitos não permitem validação ou medição       | Requisitos SMART, com critérios de aceitação, testabilidade e mapeamento técnico | `addon/07-validacao-requisitos.md`       | ✅                                     |
| Requisitos genéricos não específicos   | BSIMM13 – Requirements                                  | Políticas ou ideias vagas de "deveria ser seguro"  | Cada requisito mapeado a domínio técnico específico e controlos concretos        | `addon/09-taxonomia-rastreabilidade.md`  | ✅                                     |
| Falta de requisitos em sistemas legados| OSC&R – Requirements / SSDF                             | Equipa não aplica catálogos em manutenção          | Aplicação sistemática por risco, com exceções formalizadas                       | `addon/08-gestao-excecoes.md`            | ❌ Cap. 14                             |
| Requisitos não alinhados com risco     | DSOMM – Design & Development / SSDF PW.1 / ISO 27005    | Mesmos requisitos para todas as apps               | Matriz de requisitos ajustada por classificação de risco                         | `addon/06-matriz-controlos-por-risco.md` | ✅                                     |

---

## 🧪 Categoria 2 – Validação deficiente de requisitos

| Ameaça                                    | Fonte                                                           | Como surge                                        | Como a prática mitiga                                                              | Controlos associados                      | 🧩 Mitigada apenas por este capítulo? |
|-------------------------------------------|------------------------------------------------------------------|---------------------------------------------------|-------------------------------------------------------------------------------------|-------------------------------------------|----------------------------------------|
| Requisitos definidos mas nunca verificados| DSOMM – Design & Development / SSDF PW.4 / ASVS V1.13            | Falta de integração com testes ou revisões       | Catálogo inclui critérios de validação + plano de verificação                      | `addon/10-validacao-requisitos.md`       | ✅                                     |
| Validações inconsistentes entre projetos  | DSOMM – Design & Development / BSIMM13 – Intelligence I1.6       | Cada equipa valida à sua maneira                 | Definição unificada de validação por domínio técnico e ciclo de vida               | `addon/07-validacao-requisitos.md`       | ✅                                     |
| Ausência de rastreio entre requisito e teste| ISO 27034 / OWASP SAMM                                         | Sem rastreabilidade entre o que é exigido e o que é testado | Taxonomia + estrutura ALM permitem bidirecionalidade                              | `addon/04-rastreabilidade-controlo.md`   | ✅                                     |
| Requisitos não verificados em CI/CD       | SLSA / OSC&R Build & Policy                                     | Pipelines não integram verificação de requisitos | Integração com Cap. 07 (CI/CD) para enforcement automático                         | `addon/10-validacao-requisitos.md`       | ❌ Cap. 07                             |
| Risco aceite sem validação documental     | CAPEC-1003 / SSDF RM.2                                          | Requisito omitido sob pretexto de "não aplicável"| Política de exceções com rastreabilidade e obrigatoriedade de justificação         | `addon/08-gestao-excecoes.md`            | ❌ Cap. 14                             |

---

## 🧾 Categoria 3 – Gestão deficiente de exceções e escopo

| Ameaça                                 | Fonte                          | Como surge                                              | Como a prática mitiga                                                            | Controlos associados                       | 🧩 Mitigada apenas por este capítulo? |
|----------------------------------------|---------------------------------|---------------------------------------------------------|-----------------------------------------------------------------------------------|--------------------------------------------|----------------------------------------|
| Exceções a requisitos não documentadas | ISO 27005 / SSDF RV.3           | Equipa decide informalmente não aplicar requisito       | Processo formal de exceção com owner, prazo e impacto                             | `addon/08-gestao-excecoes.md`             | ❌ Cap. 14                             |
| Segurança omitida por “não ser funcional” | ENISA SDLC / BSIMM13           | Funcionalidade lança sem controlo de segurança          | Requisitos mapeados a features e tipos de controlo por design                     | `addon/01-catalogo-requisitos.md`         | ✅                                     |
| Aceitação de exceções sem aprovação    | CAPEC-115 / SSDF RM.2           | Developer isenta requisito sem revisão superior         | Política obriga aprovação formal, justificação, revisão periódica                 | `addon/08-gestao-excecoes.md`             | ❌ Cap. 14                             |
| Exceções não reverificadas no tempo    | NIST 800-30 / SSDF RM.3         | Requisito omitido para sempre                           | Checklist e ciclo de vida obrigam reavaliação de exceções                         | `15-aplicacao-lifecycle.md`         | ❌ Cap. 01                             |

---

## 🔄 Categoria 4 – Falhas de rastreabilidade e cobertura

| Ameaça                                  | Fonte                                                  | Como surge                                           | Como a prática mitiga                                                             | Controlos associados                      | 🧩 Mitigada apenas por este capítulo? |
|-----------------------------------------|---------------------------------------------------------|------------------------------------------------------|------------------------------------------------------------------------------------|-------------------------------------------|----------------------------------------|
| Não saber se requisitos foram aplicados | DSOMM – Design & Development / SSDF PW.5 / OWASP SAMM   | Falta de mapeamento entre requisito e código         | Rastreabilidade entre requisito, validação, código e risco                        | `addon/04-rastreabilidade-controlo.md`   | ✅                                     |
| Requisitos aplicados mas não testados  | BSIMM / SLSA / ENISA DevSecOps                          | Existe definição mas ausência de verificação         | Validação associada a cada item do catálogo + teste no ciclo de vida              | `addon/07-validacao-requisitos.md`       | ✅                                     |
| Mudanças de requisitos não propagadas  | OSC&R / ISO 27034                                        | Alteração ao requisito sem atualização de impacto    | Modelo de versionamento e rastreio de alterações aplicados ao catálogo            | `addon/01-catalogo-requisitos.md`        | ✅                                     |
| Ambiguidade entre requisito e controlo | STRIDE / NIST 800-53                                     | Confusão entre o que é exigido e o que é implementado| Matriz de rastreabilidade requisito → controlo técnico                            | `addon/04-rastreabilidade-controlo.md`   | ✅                                     |

---

## ✅ Conclusão

Este capítulo mitiga um conjunto vasto de ameaças estruturais associadas à **definição, rastreabilidade, validação e exceção de requisitos de segurança**, funcionando como base de governação técnica do SbD-ToE.

> O seu impacto é transversal: **não há controlo técnico no modelo que não dependa de um requisito bem definido, proporcional e validado.**

> Mitiga de forma **exclusiva pelo menos 10 ameaças críticas**, com destaque para a ausência, ambiguidade e não testabilidade de requisitos - pontos não tratados nos restantes capítulos.

> As práticas aqui descritas são indispensáveis para atingir conformidade com modelos como **SSDF, ASVS, OWASP SAMM, ISO 27034 e SLSA**.
