---
id: aplicacao-lifecycle
title: Como Fazer
description: Integração do threat modeling ao longo do ciclo de desenvolvimento
tags: [tipo:aplicacao, ciclo-vida, threat-modeling, requisitos, mitigacao, rastreabilidade]
genia: us-format-normalization
---


# 🔄 Aplicação de Threat Modeling no Ciclo de Vida

Este anexo prescreve **como aplicar sistematicamente as práticas de Threat Modeling definidas no Capítulo 3** ao longo do ciclo de desenvolvimento, garantindo rastreabilidade, proporcionalidade ao risco e integração com os requisitos de segurança.

Inclui modelos reutilizáveis de user stories, ações por papel, artefactos esperados e quadros de aplicação por nível de criticidade (L1–L3).

---

## 📅 Quando aplicar Threat Modeling

| Fase / Evento              | Ação esperada                                  | Quem participa                     | Artefacto principal         |
|----------------------------|------------------------------------------------|------------------------------------|-----------------------------|
| Início de projeto / épico  | Realizar sessão inicial de threat modeling      | DevOps/SRE, Product Owner, Arquitetos de Software, AppSec Engineer | DFD + lista inicial de ameaças |
| Grooming / Planeamento     | Atualizar modelos com base em novas features    | Developer + AppSec Engineer | Backlog + threats.yaml      |
| Revisão de Arquitetura     | Validar ameaças antes de design final           | Arquitetos de Software + AppSec Engineer               | Ficha de solução + mitigations.md |
| Alterações críticas        | Atualizar modelos após integrações/refactors   | Developer + QA / Test Engineer + AppSec Engineer               | Modelo atualizado           |
| Release / Go-live          | Validar riscos e exceções aceites              | QA / Test Engineer + AppSec Engineer                        | Checklist + decisions.md    |
| CI/CD pipeline             | Validar atualidade do modelo em build/release  | DevOps/SRE + AppSec Engineer                | Validação automática        |

---

## 👥 Quem faz o quê

| Papel / Função             | Responsabilidades-chave                                      |
|----------------------------|--------------------------------------------------------------|
| Arquitetos de Software     | Facilitar sessões, manter modelos atualizados e documentados  |
| Developer                  | Identificar fluxos, pontos de entrada e lógica de negócio    |
| QA / Test Engineer         | Validar critérios de aceitação derivados das ameaças         |
| AppSec Engineer            | Identificar ameaças técnicas, apoiar mitigação e rever exceções |
| Product Owner              | Priorizar mitigação e validar impacto no negócio             |
| DevOps/SRE                 | Automatizar validações de threat modeling em pipelines       |

---

## 📝 User Stories e Cartões Reutilizáveis
### US-01 - Criação do modelo de ameaça

**Contexto.**  
No início do projeto, deve ser criado um modelo de ameaça proporcional ao risco da aplicação.

:::userstory
**História.**   
Como **Arquitetos de Software** e **Team Lead / Scrum Master**, quero criar um modelo de ameaça inicial com DFDs e STRIDE/LINDDUN, para que os riscos de arquitetura sejam visíveis e tratados desde o início.

**Critérios de aceitação (BDD).**
- **Dado** que o projeto inicia  
  **Quando** construo o modelo de ameaça com DFDs  
  **Então** todas as ameaças são registadas e ligadas a controlos/requisitos

**Checklist.**
- [ ] Sessão de threat modeling realizada  
- [ ] DFDs criados e documentados  
- [ ] Ameaças catalogadas (STRIDE, LINDDUN, PASTA)  
- [ ] Ameaças ligadas a requisitos de mitigação  
- [ ] Evidência arquivada em repositório de arquitetura

:::

**Artefactos & evidências.**
- Artefacto: modelo de ameaça inicial (ferramenta ou Markdown)  
- Evidência: ligação a backlog `THREAT-*`

**Proporcionalidade por risco.**
| Nível | Obrigatório? | Ajustes |
|---|---|---|
| L1 | Opcional | Checklist simplificada |
| L2 | Sim | Modelos formais com STRIDE |
| L3 | Sim | Modelos completos com STRIDE/LINDDUN/PASTA |

**Integração no SDLC.**
| Fase | Trigger | Responsável | SLA |
|---|---|---|---|
| Início | Kick-off do projeto | Arquitetos de Software + AppSec Engineer | Antes do backlog inicial |

**Ligações úteis.**
- 🔗 [OWASP Threat Modeling](https://owasp.org/www-community/Threat_Modeling)  

---

### US-04 - Validação assistida de ameaças com decisão documentada

**Contexto.**  
Ferramentas sugerem ameaças, mas decisão final (aceitar, rejeitar, adaptar) deve ser sempre humana e registada.

:::userstory
**História.**   
Como **Arquiteto de Software** e **AppSec Engineer**, quero **validar e documentar cada ameaça sugerida**, para garantir rastreabilidade e separação entre sugestão (ferramenta) e decisão (humano).

**Critérios de aceitação (BDD).**
- **Dado** que ferramenta sugere ameaça TM-GEN-XXX  
  **Quando** executo checklist I1 (separação sugestão/decisão)  
  **Então** decido e documento: ACEITAR, ADAPTAR ou REJEITAR (com justificação)

**Checklist.**
- [ ] Ameaça é relevante para esta aplicação?
- [ ] DFD contém componentes mencionados na ameaça?
- [ ] Fluxo de dados descrito existe no design?
- [ ] Controlo mitigador já existe na arquitetura?
- [ ] Aplicação realmente está exposta a este risco?
- [ ] Propor decisão (ACEITAR/ADAPTAR/REJEITAR) com justificação
- [ ] Mapeamento para REQ-XXX (se ACEITAR)
- [ ] Aprovações necessárias (AppSec Lead, Product Owner conforme severidade)
- [ ] Decisão documentada em `threat-model/decisions/TM-GEN-XXX-decision.md`

:::

**Artefactos & evidências.**
- Artefacto: template de decisão de ameaça (ver [addon-14](./addon/14-validacao-ameacas-assistida))  
- Evidência: ficheiro `decisions/*.md`, ligação a issue/commit no backlog

**Proporcionalidade por risco.**
| Nível | Obrigatório? | Ajustes |
|---|---|---|
| L1 | Opcional | Apenas ameaças CRÍTICA |
| L2 | Sim | Todas as ameaças sugeridas |
| L3 | Sim | Todas as ameaças, com teste técnico |

**Integração no SDLC.**
| Fase | Trigger | Responsável | SLA |
|---|---|---|---|
| Design / Validação | Ferramenta sugere ameaça | Arquitetos de Software + AppSec Engineer | <5 dias (CRÍTICA), <10 dias (ALTA) |

**Ligações úteis.**
- 🔗 [addon-14: Validação Assistida — Framework I1](./addon/14-validacao-ameacas-assistida)  
- 🔗 [Matriz de Decisores](./addon/14-validacao-ameacas-assistida#-matriz-de-decisores-por-tipo-de-ameaça)  
- 🔗 [Template de Decisão de Ameaça](./addon/14-validacao-ameacas-assistida#fase-3-decisão-documentada-e-aprovada)

---

### US-05 - Validação manual e empírica de ameaças

**Contexto.**  
Ameaças não são aceites apenas porque "parecem plausíveis" — Requerem validação técnica com testes (manual, SAST, DAST).

:::userstory
**História.**   
Como **QA Engineer** e **AppSec Engineer**, quero **validar empiricamente cada ameaça CRÍTICA/ALTA**, para confirmar que é real antes de exigir mitigação.

**Critérios de aceitação (BDD).**
- **Dado** que ameaça foi aceita em I1 (US-04)  
  **Quando** executo teste empírico (manual + SAST + DAST)  
  **Então** confirmo se vulnerabilidade existe (VALIDADO) ou é falso positivo (FP)

**Checklist.**
- [ ] Categorizei ameaça (A: Input Validation, B: Auth, C: Authorization, D: Crypto, E: Data, F: Config)
- [ ] Executei teste técnico apropriado para categoria
  - [ ] Teste manual (ex: SQL injection payload, JWT bypass)
  - [ ] SAST (ex: Semgrep, SonarQube deteta padrão vulnerável?)
  - [ ] DAST (ex: OWASP ZAP, Burp Scanner)
  - [ ] Code review (ex: validação de assinatura está presente?)
- [ ] Documentei resultado: VALIDADO, FALSO_POSITIVO, ou FALSO_NEGATIVO
- [ ] Se VALIDADO: requisito já associado? Requisito em backlog?
- [ ] Se FALSO_POSITIVO: Registei em `threat-model/falsos-positivos/FP-TM-XXX.md`, suppressed em ferramenta
- [ ] Se FALSO_NEGATIVO: RCA, PR crítico, documentei em `threat-model/falsos-negativos/FN-2026-XXX.md`
- [ ] Aprovação AppSec: Resultado validado por AppSec Lead

:::

**Artefactos & evidências.**
- Artefacto: relatório de validação `threat-model/validation-results/TM-GEN-XXX-validation.md`  
- Evidência: testes executados (screenshots, logs SAST/DAST, code review), resultado FP/FN registado

**Proporcionalidade por risco.**
| Nível | Obrigatório? | Cobertura |
|---|---|---|
| L1 | Recomendado | ≥50% ameaças CRÍTICA |
| L2 | Sim | 100% CRÍTICA, ≥70% ALTA |
| L3 | Sim | 100% todas ameaças com >1 método (manual + SAST + DAST) |

**Integração no SDLC.**
| Fase | Trigger | Responsável | SLA |
|---|---|---|---|
| Validação / Pre-release | Ameaça CRÍTICA/ALTA aceita | QA Engineer + AppSec Engineer | <2 dias CRÍTICA, <5 dias ALTA |

**KPIs esperados.**
- % ameaças validadas empiricamente: 100% (L2/L3)
- FP rate: <15% (se >30%, avaliar qualidade ferramenta)
- FN rate: <5% (se >10%, melhorar modelo DFD)
- Tempo validação: <5 dias (meta)

**Ligações úteis.**
- 🔗 [addon-15: Validação Manual — Framework I2](./addon/15-validacao-manual-ameacas)  
- 🔗 [Taxonomia de Ameaças (6 Categorias)](./addon/15-validacao-manual-ameacas#fase-1-categorizar-ameaça-por-tipo-de-validação)  
- 🔗 [Testes Empíricos por Categoria](./addon/15-validacao-manual-ameacas#fase-2-teste-empírico-por-categoria)  
- 🔗 [Gestão de Falsos Positivos/Negativos](./addon/15-validacao-manual-ameacas#fase-4-gestão-de-falsos-positivos-e-falsos-negativos)

---

### US-02 - Validação de arquitetura com threat modeling

**Contexto.**  
As revisões de arquitetura devem incluir threat modeling para identificar ameaças estruturais.

:::userstory
**História.**   
Como **Arquitetos de Software** e **AppSec Engineer**, quero validar a arquitetura através de threat modeling, para identificar ameaças críticas antes de decisões de design.

**Critérios de aceitação (BDD).**
- **Dado** que ocorre revisão da arquitetura  
  **Quando** aplico threat modeling  
  **Então** ameaças estruturais são registadas e mitigadas

**Checklist.**
- [ ] Revisão de arquitetura formal realizada  
- [ ] Modelo de ameaça atualizado  
- [ ] Decisões de design documentadas  
- [ ] Evidência arquivada

:::

**Artefactos & evidências.**
- Artefacto: relatórios de revisão de arquitetura  
- Evidência: ameaças registadas ligadas a requisitos

**Proporcionalidade por risco.**
| Nível | Obrigatório? | Ajustes |
|---|---|---|
| L1 | Opcional | Revisão simplificada |
| L2 | Sim | Revisão da arquitetura com threat modeling |
| L3 | Sim | Revisão detalhada + validação independente |

**Integração no SDLC.**
| Fase | Trigger | Responsável | SLA |
|---|---|---|---|
| Design / Revisão | Revisão da arquitetura | Arquitetos de Software + AppSec Engineer | Antes da aprovação de design |

---

### US-03 - Atualização do modelo após alteração técnica

**Contexto.**  
Sempre que ocorrer uma alteração significativa (nova feature, integração ou refactor), o modelo de ameaça deve ser atualizado.

:::userstory
**História.**   
Como **Arquitetos de Software** e **DevOps/SRE**, quero atualizar o modelo de ameaça sempre que há alterações significativas, para que o modelo permaneça válido e útil.

**Critérios de aceitação (BDD).**
- **Dado** que ocorre alteração significativa  
  **Quando** atualizo o modelo  
  **Então** ameaças novas ou alteradas ficam registadas e mapeadas para requisitos

**Checklist.**
- [ ] Alteração significativa identificada  
- [ ] Modelo de ameaça atualizado  
- [ ] Ameaças novas registadas  
- [ ] Evidência arquivada

:::

**Artefactos & evidências.**
- Artefacto: modelo de ameaça atualizado  
- Evidência: commit ou issue ligada a alteração

**Proporcionalidade por risco.**
| Nível | Obrigatório? | Ajustes |
|---|---|---|
| L1 | Opcional | Apenas integrações externas |
| L2 | Sim | Todas as mudanças críticas |
| L3 | Sim | Qualquer alteração da arquitetura |

**Integração no SDLC.**
| Fase | Trigger | Responsável | SLA |
|---|---|---|---|
| Refactor / Alteração | Alteração significativa | Arquitetos de Software + Team Lead / Scrum Master | Antes da release |

**Ligações úteis.**
- 🔗 [SSDF Practices](https://csrc.nist.gov/publications/detail/sp/800-218/final)  

---
### US-04 - Justificação formal de risco aceite

**Contexto.**  
Nem todas as ameaças podem ser mitigadas; riscos residuais devem ser formalmente documentados, aprovados e revistos.

:::userstory
**História.**   
Como **AppSec Engineer** e **GRC/Compliance**, quero documentar e aprovar formalmente riscos residuais identificados no threat modeling, para que decisões de aceitação sejam transparentes e auditáveis.

**Critérios de aceitação (BDD).**
- **Dado** que há ameaças não mitigadas  
  **Quando** registo risco aceite  
  **Então** decisão é documentada, aprovada e arquivada

**Checklist.**
- [ ] Risco residual identificado  
- [ ] Justificação documentada  
- [ ] Aprovação formal por AppSec  
- [ ] Prazo e reavaliação definidos  
- [ ] Evidência anexada ao repositório de riscos

:::

**Artefactos & evidências.**
- Artefacto: ficheiros `riscos/*.md`  
- Evidência: issue ou PR com aprovação

**Proporcionalidade por risco.**
| Nível | Obrigatório? | Ajustes |
|---|---|---|
| L1 | Opcional | Aceitação informal |
| L2 | Sim | Documentação formal |
| L3 | Sim | Documentação formal + mitigação compensatória |

**Integração no SDLC.**
| Fase | Trigger | Responsável | SLA |
|---|---|---|---|
| Planeamento/Release | Identificação de risco não mitigado | AppSec Engineer | Antes do go-live |

**Ligações úteis.**
- 🔗 [Gestão de exceções](/sbd-toe/sbd-manual/requisitos-seguranca/addon/gestao-excecoes) e [risco residual](/sbd-toe/sbd-manual/classificacao-aplicacoes/addon/risco-residual)  

---

### US-05 - Integração com CI/CD

**Contexto.**  
O threat modeling deve ser integrado com pipelines CI/CD, garantindo que alterações significativas acionam revisão automática do modelo e validações associadas.

:::userstory
**História.**   
Como **DevOps/SRE** e **AppSec Engineer**, quero integrar validações de threat modeling no pipeline, para que cada alteração relevante seja revista automaticamente.

**Critérios de aceitação (BDD).**
- **Dado** que uma alteração é feita  
  **Quando** a pipeline é executada  
  **Então** verificações de threat modeling são acionadas e resultados registados

**Checklist.**
- [ ] Pipeline CI/CD inclui job de threat modeling  
- [ ] Resultados armazenados automaticamente  
- [ ] Requisitos derivados atualizados no backlog  
- [ ] Evidência disponível em logs de pipeline

:::

**Artefactos & evidências.**
- Artefacto: pipelines CI/CD  
- Evidência: logs de execução com validações

**Proporcionalidade por risco.**
| Nível | Obrigatório? | Ajustes |
|---|---|---|
| L1 | Não aplicável | - |
| L2 | Sim | Revisão periódica em pipeline |
| L3 | Sim | Automação obrigatória e bloqueante |

**Integração no SDLC.**
| Fase | Trigger | Responsável | SLA |
|---|---|---|---|
| Implementação / CI | Execução de pipeline | DevOps/SRE | Em cada commit/release |

**Ligações úteis.**
- 🔗 [DSOMM - Automation](https://dsomm.owasp.org/)  

---

### US-06 - Validação de impacto no negócio

**Contexto.**  
As ameaças identificadas devem ser priorizadas com base no impacto para o negócio, e não apenas em métricas técnicas.

:::userstory
**História.**   
Como **Product Owner**, quero priorizar as ameaças identificadas no modelo de acordo com impacto no negócio, para otimizar mitigação e investimento.

**Critérios de aceitação (BDD).**
- **Dado** que ameaças foram identificadas  
  **Quando** as avalio pelo impacto de negócio  
  **Então** prioridades são registadas e comunicadas

**Checklist.**
- [ ] Impacto avaliado (financeiro, reputacional, legal)  
- [ ] Priorização documentada  
- [ ] Requisitos derivados priorizados no backlog  
- [ ] Evidência arquivada

:::

**Artefactos & evidências.**
- Artefacto: matriz de impacto vs ameaça  
- Evidência: backlog priorizado

**Proporcionalidade por risco.**
| Nível | Obrigatório? | Ajustes |
|---|---|---|
| L1 | Opcional | Avaliação simplificada |
| L2 | Sim | Análise de impacto formal |
| L3 | Sim | Análise formal + revisão executiva |

**Integração no SDLC.**
| Fase | Trigger | Responsável | SLA |
|---|---|---|---|
| Planeamento / Grooming | Avaliação de impacto | Product Owner + Gestão Executiva/CISO | Antes de priorização de sprint |

**Ligações úteis.**
- 🔗 [ISO/IEC 27005 Risk Assessment](https://www.iso.org/standard/75281.html)  

---
### US-07 - Automação e reutilização de modelos

**Contexto.**  
Ferramentas de threat modeling (ex.: OWASP Threat Dragon, Microsoft TMT, IriusRisk) devem ser usadas para automatizar e reutilizar modelos, garantindo consistência e eficiência.

:::userstory
**História.**   
Como **DevOps/SRE + AppSec Engineer**, quero usar ferramentas para automação e reutilização de modelos de ameaça, para garantir consistência e reduzir trabalho manual.

**Critérios de aceitação (BDD).**
- **Dado** que realizo threat modeling  
  **Quando** uso ferramenta automatizada  
  **Então** o modelo é gerado/reutilizado com consistência e armazenado

**Checklist.**
- [ ] Ferramenta definida e adotada  
- [ ] Modelos armazenados em repositório central  
- [ ] Reutilização de modelos em novos projetos validada  
- [ ] Evidência de execução disponível

:::

**Artefactos & evidências.**
- Artefacto: modelos em ferramenta ou repositório central  
- Evidência: relatórios automáticos exportados

**Proporcionalidade por risco.**
| Nível | Obrigatório? | Ajustes |
|---|---|---|
| L1 | Opcional | Modelos simplificados |
| L2 | Sim | Automação recomendada |
| L3 | Sim | Automação obrigatória e reutilização padronizada |

**Integração no SDLC.**
| Fase | Trigger | Responsável | SLA |
|---|---|---|---|
| Design / Grooming | Criação e manutenção de modelos | Arquitetos de Software + DevOps/SRE | Por projeto e atualização contínua |

**Ligações úteis.**
- 🔗 [OWASP Threat Dragon](https://owasp.org/www-project-threat-dragon/)  
- 🔗 [IriusRisk](https://www.iriusrisk.com/)  

---

### US-08 - Aplicação LINDDUN quando existir tratamento de dados pessoais  *(novo)*

**Contexto.**  
Quando o sistema trata dados pessoais, a análise de privacidade deve complementar a análise de segurança.

:::userstory
**História.**  
Como **Arquitetos de Software + AppSec Engineer**, quero aplicar **LINDDUN** quando exista tratamento de dados pessoais, para garantir cobertura de ameaças de privacidade.

**Critérios de aceitação (BDD).**
- **Dado** que o sistema trata dados pessoais  
  **Quando** executo Threat Modeling  
  **Então** **incluo análise LINDDUN** com ameaças, mitigação e **mapeamento para `REQ-PRIV-*`**  
- E **crio `privacy-dfd`** com trust boundaries específicos  

**Checklist.**
- [ ] `privacy-dfd` criado  
- [ ] Lista LINDDUN preenchida  
- [ ] **Ligação a `REQ-PRIV-*` do Cap. 2**  
- [ ] **Ameaças classificadas quanto a severidade e mitigação**  
- [ ] Evidência arquivada no repositório de arquitetura  
:::

**Artefactos & evidências.**
- `privacy-dfd.*`  
- `privacy-threats.md`  
- Relatório LINDDUN exportado / validado  

**Proporcionalidade por risco.**
| Nível | Obrigatório? | Ajustes |
|:---|:---|:---|
| L1 | Opcional | Checklist simplificada |
| L2 | Sim | Análise formal de privacidade |
| L3 | Sim | LINDDUN completo + validação independente (DPO) |

**Integração no SDLC.**
| Fase | Trigger | Responsável | SLA |
|:---|:---|:---|:---|
| Design / Revisão | Presença de dados pessoais | Arquitetos de Software + GRC/Compliance | Antes da aprovação de design |

**Ligações úteis.**
- 🔗 [LINDDUN Framework](https://www.linddun.org/)  
- 🔗 [ENISA - Privacy by Design Guidelines](https://www.enisa.europa.eu/)  



## ⚖️ Aplicação proporcional por nível de risco (L1–L2–L3)
## ⚖️ Aplicação proporcional por nível de risco (L1–L2–L3)

| Prática / Atividade              | L1 (baixo risco)                         | L2 (médio risco)                                | L3 (alto risco)                                                  |
|----------------------------------|------------------------------------------|-------------------------------------------------|------------------------------------------------------------------|
| Sessões de Threat Modeling       | Básicas (checklist STRIDE simplificada)  | Modelos formais com STRIDE                     | Modelos completos com STRIDE **e LINDDUN** (quando aplicável) + PASTA + automação |
| Revisão de arquitetura           | Opcional                                 | Inclusão obrigatória                           | Sempre obrigatória com revisão independente                      |
| Integração em CI/CD              | Não aplicável                            | Revisão periódica                              | Automação integrada e bloqueante                                 |
| Risco aceite                     | Informal                                 | Documentado                                    | Formal, aprovado por AppSec e com sunset definido                |
| Automação / Reutilização         | Não aplicável                            | Recomendado (ferramenta ou script)             | Obrigatório (ferramenta centralizada, integração contínua)       |
| **Análise LINDDUN (privacidade)**| Não aplicável                            | Obrigatória se houver dados pessoais           | Sempre obrigatória, com revisão por DPO                          |

---

## 📄 Templates e artefactos esperados

| Artefacto                          | Formato sugerido     | Onde guardar / referenciar                |
|-----------------------------------|----------------------|-------------------------------------------|
| Modelo de ameaça inicial (STRIDE) | Ferramenta / `.md`   | Diretório `docs/` ou repositório          |
| **Modelo de privacidade (LINDDUN)** | Ferramenta / `.md`  | Diretório `docs/privacy/` ou subpasta do modelo |
| Atualizações de modelos            | Ferramenta / `.md`   | Diretório `docs/` ou repositório          |
| Cartões derivados (`THREAT-*`)     | Board / Jira         | Backlog da equipa                         |
| **Cartões de privacidade (`PRIV-*`)** | Board / Jira        | Backlog da equipa                         |
| Justificação de risco aceite       | Markdown / issue     | Diretório `riscos/` ou board              |
| Relatórios de rastreabilidade      | Export / `.csv`      | Arquivo de auditoria                      |
| **Relatórios LINDDUN**             | Export / `.pdf`/`.csv`| Diretório `docs/privacy/` ou auditoria    |
| Modelos automatizados              | Ferramenta           | Repositório central de modelos            |
