---
id: ameacas-mitigadas
title: Ameaças Mitigadas - Desenvolvimento Seguro
description: Ameaças mitigadas pelas práticas deste capítulo, com mapeamento para OWASP, CAPEC, SSDF, entre outros
tags: [ameaças, mitigação, desenvolvimento, codificação segura, validação, GenAI]
sidebar_position: 50
---


# 🔐 Ameaças Mitigadas - Capítulo 06: Desenvolvimento Seguro

Este capítulo prescreve práticas de **codificação segura, validações automatizadas, gestão de exceções e evidência de conformidade**, com o objetivo de garantir a integridade e segurança do código-fonte desde o início do ciclo de desenvolvimento.

> 🎯 As ameaças mitigadas são originadas por **práticas de codificação inseguras, falta de validação sistemática, informalidade na aceitação de riscos técnicos e uso de GenAI sem controlo**.

---

## 🧑‍💻 Categoria 1 – Práticas inseguras de desenvolvimento

| Ameaça                                    | Fonte                               | Como surge                                         | Como a prática mitiga                                                             | Controlos associados                          | 🧩 Mitigada apenas por este capítulo? |
|-------------------------------------------|--------------------------------------|----------------------------------------------------|------------------------------------------------------------------------------------|------------------------------------------------|----------------------------------------|
| Inclusão de padrões inseguros por hábito  | OWASP Top 10 A01 / CAPEC-139        | Equipa replica código inseguro sem perceber        | Linters e regras de validação de padrões seguros                                 | `addon/02-linters-validacoes.md`              | ✅                                     |
| Uso de funções descontinuadas ou perigosas| OWASP Top 10 / SANS CWE Top 25      | Código contém APIs inseguras                       | Listas proibidas integradas em linters e validadores                             | `addon/01-boas-praticas-codigo.md`            | ✅                                     |
| Injeção de código sem escape adequado     | STRIDE / CAPEC-135 / A03-Injection  | Faltam regras de escape/validação                 | Boas práticas + linters + validações em tempo de build                            | `addon/08-validacoes-codigo.md`               | ❌ Cap. 10                             |

---

## 📉 Categoria 2 – Ausência de validação contínua e rastreável

| Ameaça                                        | Fonte                             | Como surge                                              | Como a prática mitiga                                                                | Controlos associados                          | 🧩 Mitigada apenas por este capítulo? |
|-----------------------------------------------|------------------------------------|---------------------------------------------------------|----------------------------------------------------------------------------------------|------------------------------------------------|----------------------------------------|
| Código inseguro sem deteção                   | OWASP SAMM / SSDF PW.7            | Ausência de scanners ou análise estática                | Integração de validações de segurança automatizadas por domínio técnico               | `addon/08-validacoes-codigo.md`               | ✅                                     |
| Ausência de rastreabilidade entre problemas e decisões | ISO 27034 / BSIMM13             | Ninguém sabe quando ou porque se aceitou risco          | Anotação com justificação, owner e prazo no próprio código                            | `addon/09-anotacoes-evidencia.md`             | ✅                                     |
| Validação apenas reativa (ex: testes QA)      | SSDF PW.5 / ENISA DevSecOps       | Falta de automação na fase de build                     | Checklists de segurança embutidos no pipeline de desenvolvimento                      | `addon/08-validacoes-codigo.md`               | ❌ Cap. 07                             |

---

## 🔁 Categoria 3 – Gestão informal de exceções técnicas

| Ameaça                                       | Fonte                             | Como surge                                               | Como a prática mitiga                                                             | Controlos associados                          | 🧩 Mitigada apenas por este capítulo? |
|----------------------------------------------|------------------------------------|----------------------------------------------------------|------------------------------------------------------------------------------------|------------------------------------------------|----------------------------------------|
| Segurança removida por “incompatibilidade”   | ISO 27005 / SSDF RM.1             | Developer desativa controlos sem registo                 | Processo formal de exceções em código, com anotação e aceite por owner             | `addon/05-excecoes-e-justificacoes.md`        | ✅                                     |
| Exceções não revistas ou revalidadas         | SSDF RM.3 / CAPEC-1003            | Riscos permanecem por tempo indefinido                   | Revisão forçada por ciclo ou prazo anotado diretamente no código                   | `15-aplicacao-lifecycle.md`             | ❌ Cap. 01                             |
| Desvios não rastreados entre guideline e prática | BSIMM13 / SAMM Implementation    | Guidelines são ignoradas                                 | Comparação automática entre guideline e anotação de exceção                         | `addon/07-guidelines-equipa.md`               | ✅                                     |

---

## 🤖 Categoria 4 – Risco associado a uso inseguro de GenAI

| Ameaça                                     | Fonte                              | Como surge                                          | Como a prática mitiga                                                           | Controlos associados                          | 🧩 Mitigada apenas por este capítulo? |
|--------------------------------------------|-------------------------------------|-----------------------------------------------------|----------------------------------------------------------------------------------|------------------------------------------------|----------------------------------------|
| Geração de código inseguro via IA         | OWASP Top 10 / BSIMM13             | Código gerado sem validação nem revisão            | Requisitos de validação obrigatória de código gerado por GenAI                  | `addon/10-genia-e-seguranca.md`               | ✅                                     |
| Inclusão de vulnerabilidades conhecidas   | CAPEC / SLSA Build Integrity        | AI replica padrões antigos ou vulneráveis          | Integração obrigatória de scanners e linters sobre código gerado                | `addon/10-genia-e-seguranca.md`               | ✅                                     |
| Falta de accountability sobre código gerado| SSDF / ISO 27034                    | Sem rastreio de origem, owner ou validação         | Requisitos de anotação de origem e verificação manual obrigatória               | `addon/09-anotacoes-evidencia.md`             | ✅                                     |

---

## 🧬 Categoria 5 – Ameaças detetáveis por SBOM, mas mitigáveis antecipadamente

| Ameaça                                         | Fonte                          | Como surge                                                   | Como a prática mitiga                                                                 | Controlos associados                    | 🧩 Mitigada apenas por este capítulo? |
|------------------------------------------------|---------------------------------|----------------------------------------------------------------|----------------------------------------------------------------------------------------|------------------------------------------|----------------------------------------|
| Inclusão de bibliotecas descontinuadas         | SBOM / SCA / SLSA               | Projeto inclui versões obsoletas por falta de rastreio        | Validação de dependências integrada e política de versões mínima                       | `addon/03-seguranca-dependencias.md`     | ❌ Cap. 05                             |
| Falta de justificação para uso de dependência insegura | SBOM / ISO 27034 / SSDF     | Dependência conhecida mantida sem análise de risco            | Processo formal de exceção com anotação e owner técnico                                | `addon/05-excecoes-e-justificacoes.md`   | ✅                                     |
| Componente vulnerável mantido no build final   | SBOM / CAPEC / OWASP Top 10     | Ausência de validação de segurança antes do merge             | Integração de scanners e validações automáticas na fase de build                       | `addon/08-validacoes-codigo.md`          | ❌ Cap. 07                             |

---

## 🧠 Categoria 6 – Falta de cultura e normalização de práticas seguras

| Ameaça                                      | Fonte                             | Como surge                                             | Como a prática mitiga                                                         | Controlos associados                         | 🧩 Mitigada apenas por este capítulo? |
|---------------------------------------------|------------------------------------|--------------------------------------------------------|--------------------------------------------------------------------------------|----------------------------------------------|----------------------------------------|
| Inconsistência entre equipas e projetos     | SAMM / BSIMM                      | Cada equipa aplica práticas de forma informal         | Guidelines de segurança de desenvolvimento por tipo de projeto                 | `addon/07-guidelines-equipa.md`              | ✅                                     |
| Inexistência de baseline de segurança       | SSDF PW.1 / ISO 27034             | Não há critério mínimo de codificação segura          | Boas práticas obrigatórias com controlo automatizado                           | `addon/01-boas-praticas-codigo.md`           | ✅                                     |
| Fraca responsabilização pela segurança do código | BSIMM / OWASP SAMM             | Developers não percebem impacto das decisões          | Evidência rastreável, owner técnico e justificação anotada no código           | `addon/09-anotacoes-evidencia.md`            | ✅                                     |

---

## ✅ Conclusão

O Capítulo 06 mitiga ameaças críticas à **qualidade e segurança do código-fonte**, ao longo de todo o ciclo de desenvolvimento - especialmente aquelas ligadas à informalidade, falta de validação e fraca responsabilização técnica.

> 🧩 Pelo menos **10 ameaças são mitigadas exclusivamente por este capítulo**, incluindo:
> - Justificação e rastreio de exceções em código;
> - Rastreabilidade técnica de quem validou o quê;
> - Segurança no uso de GenAI para geração de código.

> 📦 Também reduz substancialmente o risco de problemas **que viriam a ser detetados por SBOM, SCA ou scanners**, ao garantir validações estruturadas, políticas de dependência e anotação de exceções desde a origem.

> 📌 Este capítulo operacionaliza os princípios de **secure coding** e **continuous validation** de forma auditável e escalável - com impacto direto na conformidade com **SSDF, SAMM, ISO 27034, CAPEC e OWASP Top 10**.
