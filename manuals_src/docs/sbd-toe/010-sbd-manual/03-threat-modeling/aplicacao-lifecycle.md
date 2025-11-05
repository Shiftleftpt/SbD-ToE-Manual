---
id: aplicacao-lifecycle
title: Como Fazer
description: Integração do threat modeling ao longo do ciclo de desenvolvimento
tags: [tipo:aplicacao, execucao, ciclo de vida, threat-modeling, requisitos, mitigação, rastreabilidade]
sidebar_position: 15
---


# 🔄 Aplicação de Threat Modeling no Ciclo de Vida

Este anexo prescreve **como aplicar sistematicamente as práticas de Threat Modeling definidas no Capítulo 3** ao longo do ciclo de desenvolvimento, garantindo rastreabilidade, proporcionalidade ao risco e integração com os requisitos de segurança.

Inclui modelos reutilizáveis de user stories, ações por papel, artefactos esperados e quadros de aplicação por nível de criticidade (L1–L3).

---

## 📅 Quando aplicar Threat Modeling

| Fase / Evento              | Ação esperada                                  | Quem participa                     | Artefacto principal         |
|----------------------------|------------------------------------------------|------------------------------------|-----------------------------|
| Início de projeto / épico  | Realizar sessão inicial de threat modeling      | DevSecOps, PO, Arquitetura, AppSec | DFD + lista inicial de ameaças |
| Grooming / Planeamento     | Atualizar modelos com base em novas features    | Equipa de Desenvolvimento + AppSec | Backlog + threats.yaml      |
| Revisão de Arquitetura     | Validar ameaças antes de design final           | Arquitetura + AppSec               | Ficha de solução + mitigations.md |
| Alterações críticas        | Atualizar modelos após integrações/refactors   | Dev + QA + Segurança               | Modelo atualizado           |
| Release / Go-live          | Validar riscos e exceções aceites              | QA + AppSec                        | Checklist + decisions.md    |
| CI/CD pipeline             | Validar atualidade do modelo em build/release  | Eng. CI/CD + AppSec                | Validação automática        |

---

## 👥 Quem faz o quê

| Papel / Função             | Responsabilidades-chave                                      |
|----------------------------|--------------------------------------------------------------|
| DevSecOps / Arquitetura    | Facilitar sessões, manter modelos atualizados e documentados  |
| Equipa de Desenvolvimento  | Identificar fluxos, pontos de entrada e lógica de negócio    |
| QA / Test Engineer         | Validar critérios de aceitação derivados das ameaças         |
| Segurança / AppSec         | Identificar ameaças técnicas, apoiar mitigação e rever exceções |
| Product Owner / Negócio    | Priorizar mitigação e validar impacto no negócio             |
| Eng. CI/CD                 | Automatizar validações de threat modeling em pipelines       |

---

## 📝 User Stories e Cartões Reutilizáveis
### US-01 – Criação do modelo de ameaça

**Contexto.**  
No início do projeto, deve ser criado um modelo de ameaça proporcional ao risco da aplicação.

**📖 Rationale científico.**  
Prática prevista em **OWASP SAMM – Design/Threat Assessment (2/3)**, **BSIMM AM1.2** (realizar threat modeling inicial), **SSDF PS.1** (definir práticas de segurança no design) e **DSOMM – Design**.  
Mitiga riscos como **CWE-1059 (Incomplete Documentation of Data Flow)**, **CWE-1060 (Insufficient Analysis of Control Flow)** e falhas de análise de superfície de ataque (**OSC&R – Threat Modeling Coverage Gaps**).  
Segundo o **DBIR** e a investigação de **Adam Shostack (2014)**, equipas que realizam threat modeling no início reduzem em até 40% falhas arquiteturais críticas.  

:::userstory
**História.**   
Como **Arquitetura / Tech Lead**, quero criar um modelo de ameaça inicial com DFDs e STRIDE/LINDDUN, para que os riscos arquiteturais sejam visíveis e tratados desde o início.

**Critérios de aceitação (BDD).**
- Dado que o projeto inicia  
- Quando construo o modelo de ameaça com DFDs  
- Então todas as ameaças são registadas e ligadas a controlos/requisitos

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
| Fase | Gatilho | Responsável | SLA |
|---|---|---|---|
| Início | Kick-off do projeto | Tech Lead / AppSec | Antes do backlog inicial |

**Ligações úteis.**
- 🔗 [OWASP Threat Modeling](https://owasp.org/www-community/Threat_Modeling)  

---

### US-02 – Validação de arquitetura com threat modeling

**Contexto.**  
As revisões de arquitetura devem incluir threat modeling para identificar ameaças estruturais.

**📖 Rationale científico.**  
Previsto em **BSIMM AM2.4** (usar threat modeling em revisões de arquitetura), **SAMM – Architecture (2/3)**, e **SSDF PS.3** (revisar controlos após alterações).  
Mitiga riscos como **CWE-710 (Improper Adherence to Coding Standards)**, **CWE-16 (Configuration Issues)** e superfícies expandidas (**OSC&R – Surface Expansion**).  
Segundo o **NIST SP 800-160** e dados **BSIMM**, arquiteturas revistas com threat modeling têm menor taxa de vulnerabilidades latentes exploradas em produção.  

:::userstory
**História.**   
Como **Arquitetura / Tech Lead**, quero validar a arquitetura através de threat modeling, para identificar ameaças críticas antes de decisões de design.

**Critérios de aceitação (BDD).**
- Dado que ocorre revisão arquitetural  
- Quando aplico threat modeling  
- Então ameaças estruturais são registadas e mitigadas

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
| L2 | Sim | Revisão arquitetural com threat modeling |
| L3 | Sim | Revisão detalhada + validação independente |

**Integração no SDLC.**
| Fase | Gatilho | Responsável | SLA |
|---|---|---|---|
| Design / Revisão | Revisão arquitetural | Tech Lead / AppSec | Antes da aprovação de design |

**Ligações úteis.**
- 🔗 [BSIMM Activities – Architecture Analysis](https://www.bsimm.com/)  

---

### US-03 – Atualização do modelo após alteração técnica

**Contexto.**  
Sempre que ocorrer uma alteração significativa (nova feature, integração ou refactor), o modelo de ameaça deve ser atualizado.

**📖 Rationale científico.**  
Recomendado por **SSDF PS.3** (rever requisitos e modelos após alterações), **BSIMM AM3.1**, e boas práticas de cadeia de fornecimento **SLSA v1.0**.  
Mitiga falhas como **CWE-16 (Configuration Issues)**, **CWE-1059 (Incomplete Data Flow Analysis)** e riscos de dependências externas (**OSC&R – Dependency Expansion**).  
Segundo o **DBIR** e relatórios da **ENISA**, 1 em cada 3 incidentes críticos ocorre após alterações não acompanhadas por reavaliação de ameaças.  

:::userstory
**História.**   
Como **DevSecOps / Arquitetura**, quero atualizar o modelo de ameaça sempre que há alterações significativas, para que o modelo permaneça válido e útil.

**Critérios de aceitação (BDD).**
- Dado que ocorre alteração significativa  
- Quando atualizo o modelo  
- Então ameaças novas ou alteradas ficam registadas e mapeadas para requisitos

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
| L3 | Sim | Qualquer alteração arquitetural |

**Integração no SDLC.**
| Fase | Gatilho | Responsável | SLA |
|---|---|---|---|
| Refactor / Alteração | Alteração significativa | DevSecOps / Tech Lead | Antes da release |

**Ligações úteis.**
- 🔗 [SSDF Practices](https://csrc.nist.gov/publications/detail/sp/800-218/final)  

---
### US-04 – Justificação formal de risco aceite

**Contexto.**  
Nem todas as ameaças podem ser mitigadas; riscos residuais devem ser formalmente documentados, aprovados e revistos.

**📖 Rationale científico.**  
Prática referida em **OWASP SAMM – Governance/Policy & Compliance**, **BSIMM CP1.2** (formalização de exceções e riscos), **SSDF RV.1** (document exceptions) e **ISO/IEC 27005** (tratamento de risco residual).  
Mitiga riscos como **CAPEC-220 (Disabling Security Controls)**, **CWE-285 (Improper Authorization)** e falhas de accountability.  
Dados do **ENISA Threat Landscape** e **Verizon DBIR** mostram que riscos aceites sem documentação formal levam a dívida de risco não controlada e a falhas recorrentes em auditorias de compliance.  

:::userstory
**História.**   
Como **Equipa de Segurança / AppSec**, quero documentar e aprovar formalmente riscos residuais identificados no threat modeling, para que decisões de aceitação sejam transparentes e auditáveis.

**Critérios de aceitação (BDD).**
- Dado que há ameaças não mitigadas  
- Quando registo risco aceite  
- Então decisão é documentada, aprovada e arquivada

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
| Fase | Gatilho | Responsável | SLA |
|---|---|---|---|
| Planeamento/Release | Identificação de risco não mitigado | AppSec | Antes do go-live |

**Ligações úteis.**
- 🔗 [Gestão de exceções](/sbd-toe/sbd-manual/requisitos-seguranca/addon/gestao-excecoes) e [risco residual](/sbd-toe/sbd-manual/classificacao-aplicacoes/addon/risco-residual)  

---

### US-05 – Integração com CI/CD

**Contexto.**  
O threat modeling deve ser integrado com pipelines CI/CD, garantindo que alterações significativas acionam revisão automática do modelo e validações associadas.

**📖 Rationale científico.**  
Apoiado por **DSOMM – Automation**, **BSIMM SE3.3** (uso de automação para segurança), **SAMM Verification (2/3)** e **SSDF PO.3** (integrar segurança em pipelines).  
Mitiga riscos como **CWE-693 (Protection Mechanism Failure)** e falhas de sincronização entre modelo e implementação.  
Valor empírico: **BSIMM13** mostra que organizações com threat modeling automatizado reduzem em 25% a taxa de falhas escapadas para produção; o **DBIR** reforça que automação reduz tempo médio de deteção.  

:::userstory
**História.**   
Como **DevSecOps**, quero integrar validações de threat modeling no pipeline, para que cada alteração relevante seja revista automaticamente.

**Critérios de aceitação (BDD).**
- Dado que uma alteração é feita  
- Quando a pipeline é executada  
- Então verificações de threat modeling são acionadas e resultados registados

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
| Fase | Gatilho | Responsável | SLA |
|---|---|---|---|
| Implementação / CI | Execução de pipeline | DevSecOps | Em cada commit/release |

**Ligações úteis.**
- 🔗 [DSOMM – Automation](https://dsomm.owasp.org/)  

---

### US-06 – Validação de impacto no negócio

**Contexto.**  
As ameaças identificadas devem ser priorizadas com base no impacto para o negócio, e não apenas em métricas técnicas.

**📖 Rationale científico.**  
Previsto em **SAMM – Governance/Business Alignment**, **BSIMM SR2.4** (business impact analysis), **SSDF RM.2** (prioritization of risks) e **ISO 27005** (avaliação de impacto).  
Mitiga riscos como **CWE-1004 (Sensitive Data Exposure due to Misclassification)** e falhas de priorização que levam a esforço desperdiçado.  
Segundo relatórios da **ENISA** e **DBIR**, a priorização de riscos com alinhamento ao negócio aumenta eficácia dos controlos e reduz investimento em áreas de baixo impacto.  

:::userstory
**História.**   
Como **Product Owner / Negócio**, quero priorizar as ameaças identificadas no modelo de acordo com impacto para o negócio, para otimizar mitigação e investimento.

**Critérios de aceitação (BDD).**
- Dado que ameaças foram identificadas  
- Quando as avalio pelo impacto de negócio  
- Então prioridades são registadas e comunicadas

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
| Fase | Gatilho | Responsável | SLA |
|---|---|---|---|
| Planeamento / Grooming | Avaliação de impacto | PO / Negócio | Antes de priorização de sprint |

**Ligações úteis.**
- 🔗 [ISO/IEC 27005 Risk Assessment](https://www.iso.org/standard/75281.html)  

---
### US-07 – Automação e reutilização de modelos

**Contexto.**  
Ferramentas de threat modeling (ex.: OWASP Threat Dragon, Microsoft TMT, IriusRisk) devem ser usadas para automatizar e reutilizar modelos, garantindo consistência e eficiência.

**📖 Rationale científico.**  
Recomendado em **DSOMM – Tooling & Automation**, **BSIMM AM3.2** (uso de ferramentas para threat modeling) e **SAMM Implementation**.  
Mitiga riscos de inconsistência (**CWE-1061 – Inconsistent Implementation of Security Controls**), cobertura parcial e perda de conhecimento organizacional.  
Dados de **BSIMM13** e relatórios de mercado (Gartner, ENISA) indicam que a automação reduz o esforço manual, acelera revisões e permite reaproveitar modelos entre projetos, aumentando maturidade organizacional.

:::userstory
**História.**   
Como **DevSecOps / AppSec**, quero usar ferramentas para automação e reutilização de modelos de ameaça, para garantir consistência e reduzir trabalho manual.

**Critérios de aceitação (BDD).**
- Dado que realizo threat modeling  
- Quando uso ferramenta automatizada  
- Então o modelo é gerado/reutilizado com consistência e armazenado

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
| Fase | Gatilho | Responsável | SLA |
|---|---|---|---|
| Design / Grooming | Criação e manutenção de modelos | DevSecOps / AppSec | Por projeto e atualização contínua |

**Ligações úteis.**
- 🔗 [OWASP Threat Dragon](https://owasp.org/www-project-threat-dragon/)  
- 🔗 [IriusRisk](https://www.iriusrisk.com/)  

---

## ⚖️ Aplicação proporcional por nível de risco (L1–L2–L3)

| Prática                    | L1 (baixo risco)          | L2 (médio risco)                     | L3 (alto risco)                                  |
| -------------------------- | ------------------------- | ------------------------------------ | ------------------------------------------------ |
| Sessões de threat modeling | Básicas (checklist)       | Modelos com STRIDE                   | Modelos formais com STRIDE/LINDDUN/PASTA + automação |
| Revisão de arquitetura     | Opcional                  | Inclusão obrigatória                 | Sempre obrigatória                               |
| Integração em CI/CD        | Não aplicável             | Revisão periódica                    | Automação integrada                              |
| Risco aceite               | Informal                  | Documentado                          | Formal, aprovado por AppSec                      |
| Automação / Reutilização   | Não aplicável             | Recomendado                          | Obrigatório                                      |

---

## 📄 Templates e artefactos esperados

| Artefacto                     | Formato sugerido | Onde guardar / referenciar           |
| ----------------------------- | ---------------- | ------------------------------------ |
| Modelo de ameaça inicial      | Ferramenta / md  | Diretório `docs/` ou repositório     |
| Atualizações de modelos       | Ferramenta / md  | Diretório `docs/` ou repositório     |
| Cartões derivados (`THREAT-*`)| Board / Jira     | Backlog da equipa                    |
| Justificação de risco aceite  | Markdown / issue | Diretório `riscos/` ou board         |
| Relatórios de rastreabilidade | Export / CSV     | Arquivo de auditoria                 |
| Modelos automatizados         | Ferramenta       | Repositório central de modelos       |
