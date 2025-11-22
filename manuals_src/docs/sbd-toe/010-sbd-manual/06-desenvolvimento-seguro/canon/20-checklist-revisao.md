---
id: checklist-revisao
title: Checklist - Desenvolvimento Seguro
sidebar_label: Checklist de Revisão
description: Checklist binário e auditável para avaliar a adoção prática das práticas prescritas no Capítulo 06 - Desenvolvimento Seguro
tags: [auditoria, checklist, conformidade, desenvolvimento, validacao]
sidebar_position: 20
---

# ✅ Checklist de Revisão Periódica - Desenvolvimento Seguro

Este checklist aplica-se a todas as aplicações sujeitas às práticas definidas no Capítulo 06 - Desenvolvimento Seguro.  
Serve como instrumento de verificação binária e auditável da **adoção prática das prescrições deste capítulo**, permitindo:

- Controlo contínuo da aplicação de práticas seguras de desenvolvimento
- Verificação por projeto em momentos-chave do ciclo de vida
- Geração de indicadores operacionais agregáveis por equipa

> 🗓️ **Recomenda-se a sua aplicação a cada release significativa**, ou sempre que existirem alterações de stack, dependências ou zonas críticas de código.

---

## 📋 Itens de verificação

| Item                                                                                                   | Verificado? |
|--------------------------------------------------------------------------------------------------------|-------------|
| Existe uma guideline de desenvolvimento seguro aprovada e divulgada à equipa?                         | ☐           |
| As boas práticas de codificação segura estão documentadas e aplicadas nos PRs?                         | ☐           |
| Estão ativos mecanismos locais de validação (ex: linters em pre-commit, CI ou IDE)?                   | ☐           |
| Estão integradas ferramentas de validação automatizada de segurança no pipeline (ex: Semgrep, SAST)?  | ☐           |
| Todas as dependências externas estão justificadas, controladas e atualizadas?                         | ☐           |
| Existe um registo de SBOM ou equivalente (CycloneDX, SPDX, etc.)?                                      | ☐           |
| As exceções técnicas estão formalmente justificadas, anotadas e aprovadas com owner responsável?       | ☐           |
| Os PRs incluem anotação de validação de segurança (ex: `@sec:`) ou equivalentes?                      | ☐           |
| As evidências de validação (linters, scanners, testes) estão versionadas ou arquivadas?               | ☐           |
| Existe uma validação de segurança obrigatória antes de cada release?                                  | ☐           |
| Os controlos implementados estão alinhados com o nível de risco da aplicação definido no Cap. 01?     | ☐           |
| O uso de GenAI para gerar código foi validado, justificado e rastreado com owner?                     | ☐           |

---

## 🔄 Notas de aplicação prática

- Este checklist pode ser transformado em **formulário digital, step de CI/CD ou dashboard de conformidade técnica**.
- Cada item pode ser convertido em KPI binário (sim/não) por projeto, equipa ou stack tecnológica.
- A validação completa deste checklist permite afirmar **conformidade técnica com o Capítulo 06**, para efeitos de maturidade organizacional SbD-ToE.

> ❗ Este capítulo é **essencial** para a aplicação coerente dos requisitos definidos no Capítulo 2.  
> A ausência destas práticas compromete a validação objetiva e auditável da segurança no desenvolvimento.
