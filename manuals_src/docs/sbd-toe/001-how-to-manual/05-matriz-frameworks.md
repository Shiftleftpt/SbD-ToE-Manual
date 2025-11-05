---
id: matriz-frameworks
title: Mapeamento com Frameworks de Maturidade
hide_title: false
hide_table_of_contents: false
---

# Mapeamento com Frameworks de Maturidade

Este manual está alinhado com diversas frameworks internacionais que definem maturidade e boas práticas no desenvolvimento de software seguro.

A tabela abaixo mostra a correspondência entre os **14 capítulos técnicos do SbD-ToE** e os domínios ou controlos equivalentes das seguintes referências:

- [OWASP SAMM](https://owaspsamm.org/) – Software Assurance Maturity Model
- [BSIMM](https://www.bsimm.com/) – Building Security In Maturity Model
- [NIST SSDF](https://csrc.nist.gov/publications/detail/white-paper/2022/02/01/secure-software-development-framework-ssdf)
- [SLSA](https://slsa.dev/) – Supply-chain Levels for Software Artifacts
- [CIS Controls v8](https://www.cisecurity.org/controls/cis-controls-list/)
- [ISO/IEC 27001 / 27034](https://www.iso.org/standard/44379.html) – Segurança da informação / aplicações

---

## 🧭 Tabela de Correspondência

| Nº | Capítulo                                | OWASP SAMM               | BSIMM                    | NIST SSDF      | SLSA     | CIS Controls | ISO 27001/27034 |
|----|------------------------------------------|---------------------------|---------------------------|----------------|----------|----------------|------------------|
| 1  | Gestão de Risco e Classificação         | Governance > Risk Mgmt    | Strategy & Metrics        | PO.1, PO.2      | -        | 2, 4, 14        | A.5, A.6, A.8     |
| 2  | Requisitos de Segurança                 | Design > Requirements     | Requirements              | PO.3            | -        | 3, 5, 16        | A.14.2, A.18      |
| 3  | Threat Modeling                         | Design > Threat Assessment| Architecture Analysis     | PO.3, RV.1      | -        | 12              | A.6.1.2, A.18     |
| 4  | Arquitetura Segura                      | Design > Architecture     | Architecture & Design     | PO.3, RV.1      | -        | 12, 16          | A.14.2, A.18      |
| 5  | Controlo de Dependências (SBOM, SCA)    | Implementation > Construction | Software Composition | RV.3, RV.4      | L2+      | 2, 5, 10         | A.14.2.8, A.12.1  |
| 6  | Desenvolvimento Seguro                  | Implementation > Coding   | Code Review, SAST         | RV.1, RV.2      | -        | 3, 5, 16        | A.14.2, A.18      |
| 7  | CI/CD Seguro                            | Implementation > Deployment| Deployment                | RV.5, RV.6      | L3+      | 6, 10, 16        | A.14.2.1          |
| 8  | Infraestrutura como Código (IaC)        | Operations > Environment  | Environment Hardening     | PO.5, RV.5      | L3+      | 11, 13, 14       | A.12.1, A.14.2    |
| 9  | *containers* & Imagens                   | Operations > Environment  | Environment Hardening     | PO.5, RV.4      | L3+      | 11, 12           | A.14.2.5          |
| 10 | Testes de Segurança                     | Verification > Testing    | Pen Testing, DAST         | RV.2            | -        | 17              | A.18, A.14.2.9    |
| 11 | Deploy Seguro                           | Implementation > Deployment| Release Management        | RV.5            | L3+      | 6, 16            | A.12.1.2, A.14.2  |
| 12 | Monitorização e Operações               | Operations > Incident Mgmt| Operations                | PO.6, RV.6      | -        | 8, 13, 16        | A.16.1, A.12.4    |
| 13 | Formação e Onboarding                   | Governance > Education    | Training                  | PO.4            | -        | 14               | A.7.2.2, A.18     |
| 14 | Governança e Contratação                | Governance > Strategy     | Governance                | PO.1, PO.7      | -        | 1, 2, 17         | A.5.1, A.15, A.18 |

---

## 📝 Legenda

- **PO.x / RV.x** – Práticas organizacionais (PO) e de verificação (RV) no [NIST SSDF](https://csrc.nist.gov/publications/detail/white-paper/2022/02/01/secure-software-development-framework-ssdf)
- **L2+, L3+** – Níveis mínimos recomendados de conformidade no [SLSA](https://slsa.dev/)
- **CIS Controls** – Controlos numerados da versão 8 dos [CIS Controls](https://www.cisecurity.org/controls/cis-controls-list/)
- **ISO/IEC** – Controlos extraídos de 27001:2022 (Anexo A) e ISO/IEC 27034 (segurança de aplicações)

---

## 🔍 Como usar esta matriz

Esta tabela permite:

- Verificar se um capítulo contribui para conformidade com frameworks internacionais
- Integrar o SbD-ToE em auditorias de segurança ou programas regulatórios
- Justificar investimento e prioridades com base em requisitos externos

---

Se precisares de versões desta matriz em Excel ou CSV para relatórios ou auditorias, podes gerar facilmente a partir deste conteúdo.

=============== outra versão ==========

# 📊 Matriz de Maturidade por Capítulo

Este quadro resume o **alinhamento entre os capítulos do manual SbD-ToE** e os domínios dos principais frameworks de referência:

- **OWASP SAMM**
- **BSIMM**
- **NIST SSDF**
- **SLSA**

A pontuação é indicativa e representa o **nível de maturidade** que a aplicação coerente do capítulo permite atingir dentro de cada framework (ex: 2/3 em SAMM, 1/4 em SLSA).

---

| Capítulo                                                                 | SAMM   | BSIMM  | SSDF   | SLSA   |
|--------------------------------------------------------------------------|--------|--------|--------|--------|
| 1. Gestão de Risco e Classificação de Aplicações                         | 2 / 3  | 1 / 3  | 2 / 3  | 1 / 4  |
| 2. Requisitos de Segurança                                               | 2 / 3  | 2 / 3  | 2 / 3  | –      |
| 3. Threat Modeling                                                       | 2 / 3  | 2 / 3  | 2 / 3  | –      |
| 4. Arquitetura Segura                                                    | 2 / 3  | 2 / 3  | 1 / 3  | –      |
| 5. Controlo de Dependências (SBOM, SCA)                                  | 3 / 3  | 2 / 3  | 2 / 3  | 2 / 4  |
| 6. Desenvolvimento Seguro                                                | 2 / 3  | 3 / 3  | 2 / 3  | 1 / 4  |
| 7. CI/CD Seguro                                                          | 2 / 3  | 2 / 3  | 2 / 3  | 3 / 4  |
| 8. Infraestrutura como Código (IaC)                                      | 2 / 3  | 2 / 3  | 1 / 3  | 2 / 4  |
| 9. *containers* e Imagens                                                 | 2 / 3  | 2 / 3  | 2 / 3  | 3 / 4  |
| 10. Testes de Segurança (DAST, fuzzing, etc.)                            | 2 / 3  | 2 / 3  | 2 / 3  | –      |
| 11. Deploy Seguro                                                        | 2 / 3  | 1 / 3  | 1 / 3  | 3 / 4  |
| 12. Monitorização e Operações                                            | 2 / 3  | 2 / 3  | 2 / 3  | 1 / 4  |
| 13. Formação e Onboarding                                                | 2 / 3  | 3 / 3  | 1 / 3  | –      |
| 14. Governança e Contratação                                             | 2 / 3  | 2 / 3  | 2 / 3  | –      |

---

> ℹ️ Esta matriz será complementada com os ficheiros `04-maturidade.md` por capítulo, com o **racional detalhado e as limitações por framework**.

> ⚠️ Os capítulos **1 (Risco)**, **2 (Requisitos)**, **3 (Threat Modeling)** e **5 (Dependências)** são considerados **basilares** no modelo SbD-ToE. A sua ausência compromete a coerência e eficácia da implementação.

---

## 🗺️ Notas de Interpretação

- Um valor “–” indica que o framework não cobre explicitamente o domínio em causa.
- A pontuação (ex: `2 / 3`) indica **até onde a prática prescrita neste manual permite chegar**, **não** o nível atingido automaticamente.
- A maturidade efetiva depende da **aplicação rigorosa, registo rastreável e melhoria contínua**.

