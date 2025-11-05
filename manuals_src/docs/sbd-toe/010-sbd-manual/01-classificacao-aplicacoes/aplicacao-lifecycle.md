---
id: aplicacao-lifecycle
title: Como Fazer
sidebar_position: 15
tags: [aplicacao, ciclo-vida, user-story, backlog]
---

# 🛠️ Aplicação da Classificação de Criticidade ao Longo do Ciclo de Vida

A correta aplicação da classificação de criticidade (L1–L3) ao longo de todo o ciclo de desenvolvimento é essencial para garantir que os controlos de segurança são sempre proporcionais ao risco real, efetivamente rastreáveis e revistos de acordo com os eventos e alterações relevantes.

Este capítulo detalha, de forma operacional e prescritiva, **quando e como implementar a classificação de criticidade na prática**, descrevendo as ações esperadas por cada papel, os artefactos produzidos, e apresentando exemplos de user stories reutilizáveis - sempre de acordo com o nível de risco da aplicação.

---

## 🧭 Abrangência e quando aplicar

| Fase / Evento                      | Ação esperada                                                  | Documento de apoio                                                        |
|------------------------------------|----------------------------------------------------------------|----------------------------------------------------------------------------|
| 🚧 Início de projeto               | Classificar aplicação segundo modelo E+D+I                     | [Modelo de Classificação](./addon/modelo-classificacao-eixos) |
| 🔄 Nova release ou integração      | Rever classificação com base em alterações relevantes          | [Ciclo de Vida do Risco](./addon/ciclo-vida-risco) |
| 🛠️ Mudança nos dados ou exposição  | Reclassificar eixo D ou E, avaliar risco residual              | [Risco Residual](./addon/risco-residual) |
| 🧪 Revisão de arquitetura          | Aplicar avaliação semiquantitativa e validar controlo aplicado | [Avaliação Semiquantitativa](./addon/avaliacao-semiquantitativa) |
| 🚀 Go-live                         | Validar conformidade com matriz de controlos por risco         | [Matriz de Controlos por Risco](./addon/matriz-controlos-por-risco) |
| ⚠️ Ameaça emergente ou nova CVE    | Reavaliar criticidade e cobertura de ameaças                   | [Mapeamento de Ameaças](./addon/mapeamento-ameacas-risco) |

---

## 👥 Quem executa cada ação

| Papel / Função       | Responsabilidades                                                                 |
|----------------------|----------------------------------------------------------------------------------|
| Dev / Tech Lead      | Propor e aplicar o modelo de classificação (E+D+I), registar alterações e evidências |
| AppSec / Segurança   | Validar modelo aplicado, ajustar nível de risco, aplicar matriz, mapear ameaças    |
| Arquitetura          | Rever implicações técnicas, cenários de exposição e dependências                   |
| Produto / Gestão     | Aprovar aceitação de risco, priorizar impacto de exceções, suportar decisões de negócio |
| GRC / Compliance     | Assegurar rastreabilidade normativa, validação de critérios de aceitação e exceções |
| QA / Testes          | Validar cumprimento dos requisitos por nível de risco antes do go-live, garantir evidências documentadas |

---

## 🛠️ User stories reutilizáveis

### US-01 – Classificação inicial da aplicação

**Contexto.**  
A classificação inicial da aplicação é o ponto de entrada para a aplicação proporcional de controlos de segurança (L1–L3). Sem este passo, não é possível garantir rastreabilidade nem proporcionalidade.

**📖 Rationale.**  
- **Referências:** ISO 27005, OWASP SAMM (Governance), SSDF PO.1.  
- **Ameaças mitigadas:** ausência de critérios de proporcionalidade → aplicações críticas tratadas como triviais (OSC&R – Risk underestimation).  
- **Valor científico:** estudos de NIST confirmam que a classificação inicial é determinante para calibrar investimento em segurança.  

:::userstory
**História.**   
Como **Dev / Tech Lead** quero classificar a aplicação com base nos eixos Exposição, Dados e Impacto (E+D+I) para garantir a aplicação proporcional de controlos de segurança.

**Critérios de aceitação (BDD).**
- Dado uma aplicação nova ou em início de projeto  
- Quando aplico o modelo de classificação E+D+I  
- Então obtenho uma pontuação por eixo e um nível global L1–L3 definido e documentado  

**Checklist.**
- [ ] Modelo de classificação E+D+I aplicado à aplicação  
- [ ] Nível de criticidade (L1–L3) definido  
- [ ] Documento de classificação registado e versionado  
- [ ] Controlos mínimos extraídos da matriz de risco e associados à aplicação  

:::

**Artefactos & evidências.**
- Artefacto: `classificacao-aplicacao.yaml` - Evidência: repositório `security/` versionado  
- Artefacto: `matriz-controlos.md` - Evidência: anexo ao PR inicial ou ao repositório de documentação  

**Proporcionalidade por risco.**
| Nível | Obrigatório? | Ajustes |
|---|---|---|
| L1 | Sim | Classificação simplificada, apenas eixos principais |
| L2 | Sim | Classificação completa com revisão por AppSec |
| L3 | Sim | Classificação formal, validada por AppSec e aprovada por GRC |

**Integração no SDLC.**
| Fase        | Gatilho                         | Responsável     | SLA/Deadline            |
|-------------|---------------------------------|-----------------|-------------------------|
| Início      | Kick-off / definição de projeto | Dev / Tech Lead | Antes da primeira release|
| Arquitetura | Revisão de design inicial       | Dev + Arquitetura | Antes da aprovação de arquitetura|

**Ligações úteis.**
- 🔗 [Modelo de Classificação](/sbd-toe/sbd-manual/classificacao-aplicacoes/addon/modelo-classificacao-eixos)  
- 🔗 [Matriz de Controlos por Risco](/sbd-toe/sbd-manual/classificacao-aplicacoes/addon/matriz-controlos-por-risco)

---

### US-02 – Aplicação da matriz de controlo

**Contexto.**  
A matriz de controlo define quais os requisitos de segurança aplicáveis em função do nível de risco.

**📖 Rationale.**  
- **Referências:** OWASP SAMM SR1, BSIMM CP1.1.  
- **Ameaças mitigadas:** excesso ou falta de controlos → falhas operacionais ou custos excessivos.  
- **Valor científico:** frameworks de maturidade demonstram que mapear controlos ao risco reduz desvios de compliance em >40%.  

:::userstory
**História.**   
Como **Dev / Tech Lead** quero aplicar a matriz de controlos para garantir que apenas os requisitos necessários são exigidos.

**Critérios de aceitação (BDD).**
- Dado uma aplicação já classificada  
- Quando consulto a matriz de controlos  
- Então extraio apenas os requisitos correspondentes ao nível atribuído  

**Checklist.**
- [ ] Matriz consultada para o nível da aplicação  
- [ ] Requisitos transformados em cartões ou histórias de backlog  
- [ ] Exceções documentadas e aprovadas  

:::

**Artefactos & evidências.**
- Artefacto: `matriz-controlos.md` - Evidência: issue tracking/backlog  

**Proporcionalidade por risco.**
| Nível | Obrigatório? | Ajustes |
|---|---|---|
| L1 | Sim | Aplicar controlos mínimos |
| L2 | Sim | Controlos completos |
| L3 | Sim | Controlos completos + reforçados |

**Integração no SDLC.**
| Fase | Gatilho | Responsável | SLA |
|---|---|---|---|
| Planeamento | Após classificação | Dev / Tech Lead + AppSec | Antes de iniciar implementação |

**Ligações úteis.**
- 🔗 [Matriz de Controlos por Risco](/sbd-toe/sbd-manual/classificacao-aplicacoes/matriz-controlos-por-risco)

---

### US-03 – Revisão periódica da classificação

**Contexto.**  
A classificação deve ser revista periodicamente para refletir alterações de arquitetura, dados ou contexto.

**📖 Rationale.**  
- **Referências:** ISO 27005, SSDF RV.1.  
- **Ameaças mitigadas:** *risk drift* → nível de risco real muda sem atualização formal.  
- **Valor científico:** revisões periódicas reduzem em 50% incidentes relacionados com mudanças não controladas.  

:::userstory
**História.**   
Como **AppSec / Segurança** quero rever a classificação de criticidade sempre que houver alterações relevantes para garantir adequação contínua dos controlos.

**Critérios de aceitação (BDD).**
- Dado que ocorreu uma alteração significativa (ex: nova API, novo dado sensível)  
- Quando reviso a classificação  
- Então documento se o nível foi mantido ou alterado, com justificação  

**Checklist.**
- [ ] Trigger de revisão identificado  
- [ ] Documento atualizado ou validado  
- [ ] Justificação registada  

:::

**Artefactos & evidências.**
- Artefacto: `classificacao-revisao.md` - Evidência: commit em repositório ou issue  

**Proporcionalidade por risco.**
| Nível | Obrigatório? | Ajustes |
|---|---|---|
| L1 | Sim | Revisão anual ou por milestones |
| L2 | Sim | Revisão em cada release significativa |
| L3 | Sim | Revisão em cada sprint ou evento crítico |

**Integração no SDLC.**
| Fase | Gatilho | Responsável | SLA |
|---|---|---|---|
| Arquitetura / Release | Alteração relevante | AppSec / Segurança | Antes da entrega |

**Ligações úteis.**
- 🔗 [Ciclo de Vida da Classificação](/sbd-toe/sbd-manual/classificacao-aplicacoes/addon/ciclo-vida-risco)

---

### US-04 – Análise de risco residual

**Contexto.**  
Mesmo após aplicação da matriz, podem permanecer riscos residuais que devem ser documentados e aprovados.

**📖 Rationale.**  
- **Referências:** SSDF PO.4, ISO 27005.  
- **Ameaças mitigadas:** riscos não documentados → aceitação implícita sem transparência.  
- **Valor científico:** registo de risco residual é prática mandatória em NIS2 e ISO 27001.  

:::userstory
**História.**   
Como **GRC / Compliance** quero registar o risco residual após aplicar os controlos definidos para fundamentar decisões de aceitação ou mitigação.

**Critérios de aceitação (BDD).**
- Dado que alguns controlos não são aplicáveis ou foram excecionados  
- Quando documento as justificações  
- Então o risco residual é registado e aprovado  

**Checklist.**
- [ ] Controlos não aplicados identificados  
- [ ] Justificação técnica registada  
- [ ] Aprovação formal por GRC ou Gestão  
:::

**Artefactos & evidências.**
- Artefacto: `risco-residual.md` - Evidência: aprovado em repositório ou ferramenta GRC  

**Proporcionalidade por risco.**
| Nível | Obrigatório? | Ajustes |
|---|---|---|
| L1 | Opcional | Apenas riscos críticos documentados |
| L2 | Sim | Documentação obrigatória |
| L3 | Sim | Justificação formal + aprovação gestão |

**Integração no SDLC.**
| Fase | Gatilho | Responsável | SLA |
|---|---|---|---|
| Planeamento / Release | Exceção a controlos | GRC / Compliance | Antes do go-live |

**Ligações úteis.**
- 🔗 [Risco Residual](/sbd-toe/sbd-manual/classificacao-aplicacoes/addon/risco-residual)

---

### US-05 – Validação antes do go-live

**Contexto.**  
Antes de entrar em produção é necessário validar se todos os requisitos aplicáveis foram cumpridos.

**📖 Rationale.**  
- **Referências:** SSDF RV.3, BSIMM SE3.5.  
- **Ameaças mitigadas:** promoção de sistemas não conformes.  
- **Valor científico:** validação formal reduz em 70% a probabilidade de findings críticos passarem para produção.  

:::userstory
**História.**   
Como **QA / Testes** quero validar que os requisitos aplicáveis por nível de risco estão cumpridos antes da entrada em produção.

**Critérios de aceitação (BDD).**
- Dado que a aplicação está pronta para go-live  
- Quando reviso a checklist de controlos  
- Então confirmo evidências documentadas e aprovação formal  

**Checklist.**
- [ ] Checklist de controlos revista  
- [ ] Evidências documentadas (testes, relatórios)  
- [ ] Aprovação formal de AppSec registada  

:::

**Artefactos & evidências.**
- Artefacto: `checklist-go-live.md` - Evidência: anexo ao PR final ou pipeline CI/CD  

**Proporcionalidade por risco.**
| Nível | Obrigatório? | Ajustes |
|---|---|---|
| L1 | Opcional | Verificação simplificada |
| L2 | Recomendado | Checklist formal |
| L3 | Sim | Validação formal + aprovação AppSec |

**Integração no SDLC.**
| Fase | Gatilho | Responsável | SLA |
|---|---|---|---|
| Release | Preparação go-live | QA / Testes + AppSec | Antes da produção |

**Ligações úteis.**
- 🔗 [Checklist de conformidade go-live](/sbd-toe/sbd-manual/classificacao-aplicacoes/checklist-go-live)

---

### US-06 – Mapeamento de ameaças por nível de risco

**Contexto.**  
Cada nível de criticidade deve ser confrontado com ameaças conhecidas para validar cobertura.

**📖 Rationale.**  
- **Referências:** OWASP Top 10, CAPEC, OSC&R.  
- **Ameaças mitigadas:** lacunas de cobertura de ameaças.  
- **Valor científico:** mapeamento sistemático aumenta eficácia de mitigação em mais de 60%.  

:::userstory
**História.**   
Como **AppSec / Segurança** quero verificar se as ameaças esperadas para o nível de criticidade estão cobertas por controlos aplicados ou exceções rastreáveis.

**Critérios de aceitação (BDD).**
- Dado que a aplicação tem nível de criticidade definido  
- Quando consulto o mapeamento de ameaças  
- Então verifico que todas as ameaças críticas têm cobertura ou exceção documentada  

**Checklist.**
- [ ] Ameaças identificadas por nível  
- [ ] Cobertura validada por controlo ou exceção  
- [ ] Resultados registados  

:::

**Artefactos & evidências.**
- Artefacto: `mapeamento-ameacas.md` - Evidência: anexo ao PR de revisão  

**Proporcionalidade por risco.**
| Nível | Obrigatório? | Ajustes |
|---|---|---|
| L1 | Opcional | Apenas ameaças mais críticas |
| L2 | Sim | Mapeamento completo |
| L3 | Sim | Mapeamento completo + validação contínua |

**Integração no SDLC.**
| Fase | Gatilho | Responsável | SLA |
|---|---|---|---|
| Revisão Arquitetura / Release | Alteração relevante | AppSec / Segurança | Antes de aprovação de design ou release |

**Ligações úteis.**
- 🔗 [Mapeamento de Ameaças por Nível de Risco](/sbd-toe/sbd-manual/classificacao-aplicacoes/addon/mapeamento-ameacas-risco)

---

## 📑 Artefactos esperados (por fase)

| Fase         | Artefacto                        | Quem produz        | Onde fica            | Evidência mínima          |
|--------------|----------------------------------|-------------------|----------------------|---------------------------|
| Início       | Documento de classificação       | Dev / Tech Lead   | Repositório `docs/`  | Commit + revisão AppSec   |
| Planeamento  | Matriz de controlos aplicada     | Dev / Tech Lead   | Backlog / wiki       | Extração de requisitos    |
| Revisão      | Documento de revisão de risco    | AppSec            | Repositório `docs/`  | Aprovação arquiteto/AppSec|
| Release      | Checklist de conformidade go-live| QA / Testes       | Pipeline CI/CD       | Aprovação formal AppSec   |
| Operação     | Registo de risco residual        | GRC / Compliance  | Repositório GRC      | Aprovação gestão          |

---

## 📊 Matriz de proporcionalidade L1–L3

| Prática / Story             | L1 | L2 | L3 | Observações |
|-----------------------------|----|----|----|-------------|
| US-01 – Classificação inicial| ✔ | ✔ | ✔ | Maior formalismo em L3 |
| US-02 – Aplicação da matriz | ✔ | ✔ | ✔ | Requisitos reforçados em L3 |
| US-03 – Revisão periódica   | ✔ | ✔ | ✔ | Frequência aumenta com risco |
| US-04 – Risco residual      | (opcional) | ✔ | ✔ | L1 apenas se risco crítico |
| US-05 – Validação go-live   | (opcional) | recomendado | ✔ | Formal em L3 |
| US-06 – Mapeamento ameaças  | (opcional) | ✔ | ✔ | Completo e contínuo em L3 |

---

## 📝 Recomendações operacionais

* Integrar a classificação de risco desde o **kick-off** do projeto.  
* Reavaliar a classificação em todas as alterações relevantes (dados, exposição, arquitetura).  
* Manter a documentação **versionada e rastreável** em repositório controlado.  
* Usar a matriz de controlo como guia direto para backlog de segurança.  
* Exigir aprovação formal de risco residual antes de qualquer exceção.  
* Validar proporcionalidade no go-live e documentar evidências.  
* Alinhar práticas com políticas organizacionais (classificação, aceitação de risco, revisão periódica).  
