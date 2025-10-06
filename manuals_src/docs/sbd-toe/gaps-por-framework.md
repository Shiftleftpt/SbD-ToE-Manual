---
id: gaps-por-framework
title: Gaps e Delimitações
hide_title: false
hide_table_of_contents: false
---

# Limites e Gaps do Manual SbD-ToE por Framework {gaps-por-framework}

Este documento identifica **gaps ou limites atuais** do manual _Security by Design – Theory of Everything (SbD-ToE)_ quando comparado com os níveis mais elevados das principais frameworks de maturidade. O objetivo é fornecer **clareza sobre o que está (ou não) coberto**, ajudando as organizações a tomar decisões informadas sobre evoluções futuras.

---

## OWASP SAMM {gaps-por-framework#owasp_samm}

| Domínio SAMM                   | Estado de Cobertura no SbD-ToE               | Gap Identificado                                       |
|-------------------------------|----------------------------------------------|--------------------------------------------------------|
| Governance > Strategy & Metrics | Parcial                                     | Falta de prescrição clara de métricas contínuas por domínio. |
| Design > Security Architecture | Parcial/Boa                                 | Cobre práticas essenciais, mas não formaliza artefactos reutilizáveis nem validações cruzadas. |
| Verification > Code Review     | Parcial                                     | Não define ainda modelos de peer review formal com controlo por criticidade. |
| Operations > Environment Mgmt  | Parcial                                     | Boa abordagem prática (IaC, containers), mas sem processos formais de rollback e contenção. |

---

## BSIMM {gaps-por-framework#bsimm}

| Domínio BSIMM                   | Estado de Cobertura                          | Gap Identificado                                      |
|-------------------------------|----------------------------------------------|-------------------------------------------------------|
| Intelligence                   | Parcial/Fraco                                | Não cobre práticas de threat intelligence nem feeds externos de forma estruturada. |
| SSDL Touchpoints               | Bom                                          | Coberto na prática, mas falta reforço de integração com QA e testes funcionais. |
| Deployment                    | Parcial/Boa                                  | Algumas práticas descritas, mas sem cobertura de antifrágil ou chaos engineering. |

---

## NIST SSDF {gaps-por-framework#nist_ssdf}

| Secção SSDF                    | Estado de Cobertura                          | Gap Identificado                                      |
|-------------------------------|----------------------------------------------|-------------------------------------------------------|
| Respond (RS.x)                | Parcial                                      | O manual foca-se mais na prevenção. Planos de resposta a falhas ou compromissos são genéricos. |
| Prepare (PO.5, PO.6)          | Parcial                                      | Falta documentação prescritiva para ambientes partilhados ou múltiplos fornecedores. |

---

## SLSA {gaps-por-framework#slsa}

| Nível SLSA                     | Estado de Cobertura                          | Gap Identificado                                      |
|-------------------------------|----------------------------------------------|-------------------------------------------------------|
| SLSA Level 4                   | Parcial/Limitado                             | O manual cobre até L3, mas não entra em artefactos assinados, políticas de revisão binária nem isolamento hermético de builds. |

---

## Considerações Finais {gaps-por-framework#consideracoes_finais}

Estes gaps não representam falhas, mas sim **deliberações conscientes** de âmbito: o foco do SbD-ToE é a aplicabilidade prática num contexto de adoção progressiva.

Organizações com ambição de **atingir o nível máximo** em qualquer destas frameworks podem usar este documento como guia para:

- Identificar onde expandir o processo interno
- Complementar o manual com artefactos próprios
- Reforçar práticas de validação, monitorização e resposta

> O SbD-ToE é compatível com maturidade avançada — mas é propositalmente pragmático, centrado no essencial e aplicável em contextos reais.

---

