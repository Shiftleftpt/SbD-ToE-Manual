---
id: aplicacao-lifecycle
title: Como Fazer
sidebar_position: 15
tags: [aplicacao, ciclo-vida, user-story, backlog]
---

# 🛠️ Aplicação da Classificação de Criticidade ao Longo do Ciclo de Vida

A correta aplicação da classificação de criticidade (L1–L3) ao longo de todo o ciclo de desenvolvimento é essencial para garantir que os controlos de segurança são sempre proporcionais ao risco real, efetivamente rastreáveis e revistos de acordo com os eventos e alterações relevantes.

Este capítulo detalha, de forma operacional e prescritiva, **quando e como implementar a classificação de criticidade na prática**, descrevendo as ações esperadas por cada papel, os artefactos produzidos, e apresentando exemplos de user stories reutilizáveis — sempre de acordo com o nível de risco da aplicação.

---

## 🧭 Abrangência e quando aplicar

| Fase / Evento                          | Ação esperada                                                   | Documento de apoio                                                                 |
|----------------------------------------|-----------------------------------------------------------------|-------------------------------------------------------------------------------------|
| 🚧 Início de projeto                   | Classificar aplicação segundo modelo E+D+I                      | [Modelo de Classificação](/sbd-toe/sbd-manual/classificacao-aplicacoes/addon/modelo-classificacao-eixos) |
| 🔄 Nova release ou integração          | Rever classificação com base em alterações relevantes           | [Ciclo de Vida do Risco](/sbd-toe/sbd-manual/classificacao-aplicacoes/addon/ciclo-vida-risco) |
| 🛠️ Mudança nos dados ou exposição      | Reclassificar eixo D ou E; avaliar risco residual               | [Risco Residual](/sbd-toe/sbd-manual/classificacao-aplicacoes/addon/risco-residual) |
| 🧪 Revisão de arquitetura              | Aplicar avaliação semiquantitativa e validar controlo aplicado  | [Avaliação Quantitativa](/sbd-toe/sbd-manual/classificacao-aplicacoes/addon/avaliacao-semiquantitativa) |
| 🚀 Go-live                             | Validar conformidade com matriz de controlos por risco          | [Matriz de controlos por Risco](/sbd-toe/sbd-manual/classificacao-aplicacoes/addon/matriz-controlos-por-risco) |
| ⚠️ Ameaça emergente ou nova CVE        | Reavaliar criticidade e cobertura de ameaças                    | [Mapeamento Ameaças por Risco](/sbd-toe/sbd-manual/classificacao-aplicacoes/addon/mapeamento-ameacas-risco) |
| 🗓️ Decurso do tempo (cadência formal) | **Revisão periódica time-based** da classificação               | [Ciclo de Vida do Risco](/sbd-toe/sbd-manual/classificacao-aplicacoes/addon/ciclo-vida-risco) |

---

## 👥 Quem executa cada ação

| Papel / Função       | Responsabilidades                                                                                         |
|----------------------|------------------------------------------------------------------------------------------------------------|
| Dev / Tech Lead      | Propor e aplicar o modelo de classificação (E+D+I); registar alterações e evidências                      |
| AppSec / Segurança   | Validar modelo aplicado; ajustar nível; aplicar matriz; mapear ameaças; parametrizar cadência de revisão  |
| Arquitetura          | Rever implicações técnicas, cenários de exposição e dependências                                           |
| Produto / Gestão     | Aprovar aceitação de risco; priorizar impacto de exceções; suportar decisões de negócio                   |
| GRC / Compliance     | Assegurar rastreabilidade normativa; definir validade/expiração de exceções; **consolidar KPIs**          |
| QA / Testes          | Validar cumprimento dos requisitos por nível de risco antes do go-live; garantir evidências documentadas  |
| Plataforma/DevOps    | **Aplicar classificação a artefactos técnicos** (pipeline/IaC/imagens) quando aplicável                  |

---

## 🛠️ User stories reutilizáveis

### US-01 – Classificação inicial da aplicação

**Contexto.**  
A classificação inicial da aplicação é o ponto de entrada para a aplicação proporcional de controlos de segurança (L1–L3). Sem este passo, não é possível garantir rastreabilidade nem proporcionalidade.

<<<<<<< HEAD
=======
**📖 Rationale.**  
- **Referências:** ISO 27005, OWASP SAMM (Governance), SSDF PO.1.  
- **Ameaças mitigadas:** ausência de critérios de proporcionalidade → aplicações críticas tratadas como triviais (OSC&R – Risk underestimation).  
- **Valor científico:** estudos do NIST confirmam que a classificação inicial é determinante para calibrar investimento em segurança.

>>>>>>> feat/cap1-complete-user-stories
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
- Artefacto: `classificacao-aplicacao.yaml` — Evidência: repositório `security/` versionado  
- Artefacto: `matriz-controlos.md` — Evidência: anexo ao PR inicial ou ao repositório de documentação

**Proporcionalidade por risco.**
| Nível | Obrigatório? | Ajustes |
|---|---|---|
| L1 | Sim | Classificação simplificada, apenas eixos principais |
| L2 | Sim | Classificação completa com revisão por AppSec |
| L3 | Sim | Classificação formal, validada por AppSec e aprovada por GRC |

**Integração no SDLC.**
<<<<<<< HEAD
| Fase        | Trigger                         | Responsável       | SLA/Deadline              |
=======
| Fase        | Gatilho                         | Responsável       | SLA/Deadline              |
>>>>>>> feat/cap1-complete-user-stories
|-------------|---------------------------------|-------------------|---------------------------|
| Início      | Kick-off / definição de projeto | Dev / Tech Lead   | Antes da primeira release |
| Arquitetura | Revisão de design inicial       | Dev + Arquitetura | Antes da aprovação de arquitetura |

**Ligações úteis.**
- 🔗 [modelo de classificação](/sbd-toe/sbd-manual/classificacao-aplicacoes/addon/modelo-classificacao-eixos)  
- 🔗 [Matrix de Controlos por Risco](/sbd-toe/sbd-manual/classificacao-aplicacoes/addon/matriz-controlos-por-risco)

---

### US-02 – Aplicação da matriz de controlo

**Contexto.**  
A matriz de controlo define quais os requisitos de segurança aplicáveis em função do nível de risco.

<<<<<<< HEAD
=======
**📖 Rationale.**  
- **Referências:** OWASP SAMM SR1, BSIMM CP1.1.  
>>>>>>> feat/cap1-complete-user-stories
- **Ameaças mitigadas:** excesso ou falta de controlos → falhas operacionais ou custos excessivos.

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
- [ ] **Cada requisito mapeado referencia explicitamente os REQ-XXX do Cap. 02**  
- [ ] Exceções documentadas e aprovadas
:::

**Artefactos & evidências.**
- Artefacto: `matriz-controlos.md` — Evidência: issue tracking/backlog

**Proporcionalidade por risco.**
| Nível | Obrigatório? | Ajustes |
|---|---|---|
| L1 | Sim | Aplicar controlos mínimos |
| L2 | Sim | Controlos completos |
| L3 | Sim | Controlos completos + reforçados |

**Integração no SDLC.**
<<<<<<< HEAD
| Fase       | Trigger            | Responsável           | SLA                     |
=======
| Fase       | Gatilho            | Responsável           | SLA                     |
>>>>>>> feat/cap1-complete-user-stories
|------------|--------------------|-----------------------|-------------------------|
| Planeamento| Após classificação | Dev / TL + AppSec     | Antes de implementação  |

**Ligações úteis.**
- 🔗 [Matrix de Controlos por Risco](/sbd-toe/sbd-manual/classificacao-aplicacoes/addon/matriz-controlos-por-risco)

---

### US-03 – Revisão por alteração relevante (event-based)

**Contexto.**  
A classificação deve ser revista quando existirem alterações significativas de arquitetura, dados ou exposição.
<<<<<<< HEAD
=======

**📖 Rationale.**  
- **Referências:** ISO 27005, SSDF RV.1.  
- **Ameaças mitigadas:** *risk drift* → nível de risco real muda sem atualização formal.
>>>>>>> feat/cap1-complete-user-stories

:::userstory
**História.**  
Como **AppSec / Segurança** quero rever a classificação de criticidade sempre que houver alterações relevantes para garantir adequação contínua dos controlos.

**Critérios de aceitação (BDD).**
- Dado que ocorreu uma alteração significativa (ex.: nova API, novo dado sensível)  
- Quando reviso a classificação  
- Então documento se o nível foi mantido ou alterado, com justificação

**Checklist.**
- [ ] Trigger de revisão identificado  
- [ ] Documento atualizado ou validado  
- [ ] Justificação registada
:::

**Artefactos & evidências.**
- Artefacto: `classificacao-revisao.md` — Evidência: commit/issue

**Proporcionalidade por risco.**
| Nível | Obrigatório? |
|---|---|
| L1 | Sim (por alteração relevante) |
| L2 | Sim |
| L3 | Sim |

**Ligações úteis.**
- 🔗 [Ciclo de Vida do Risco](/sbd-toe/sbd-manual/classificacao-aplicacoes/addon/ciclo-vida-risco)

---

### **US-07 – Revisão periódica time-based (calendário)**

**Contexto.**  
Para além dos triggers por alteração, a classificação deve ter **cadência de revisão**.

<<<<<<< HEAD
=======
**📖 Rationale.**  
- **Referências:** SSDF RV.1, GRC.  
- **Valor:** garante atualização mesmo sem eventos visíveis.

>>>>>>> feat/cap1-complete-user-stories
:::userstory
**História.**  
Como **GRC / AppSec** quero rever a classificação com **cadência fixa** para assegurar que a criticidade e os controlos continuam adequados.

**Critérios de aceitação (BDD).**
- Dado que existe uma classificação ativa  
- Quando alcanço a **data de revisão** (ex.: 6/12 meses consoante L1–L3)  
- Então realizo a revisão, documento decisão (manter/alterar) e **rego agendamento da próxima data**

**Checklist.**
- [ ] Data de revisão definida no registo  
- [ ] Ata/issue da revisão arquivada  
- [ ] Próxima data de revisão marcada
:::

**Proporcionalidade (cadência típica).**
| Nível | Frequência sugerida |
|---|---|
| L1 | 12 meses |
| L2 | 6 meses |
| L3 | 3 meses (ou por sprint em sistemas críticos) |

---

### US-04 – Análise de risco residual

**Contexto.**  
Mesmo após aplicação da matriz, podem permanecer riscos residuais que devem ser documentados e aprovados.

<<<<<<< HEAD
=======
**📖 Rationale.**  
- **Referências:** SSDF PO.4, ISO 27005.

>>>>>>> feat/cap1-complete-user-stories
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
- Artefacto: `risco-residual.md` — Evidência: ferramenta GRC/repo

---

### **US-08 – Aceitação de risco com validade (TTL e revalidação)**

**Contexto.**  
Aceitações de risco **não podem ser permanentes**.

<<<<<<< HEAD
=======
**📖 Rationale.**  
- **Referências:** SSDF PO.4; práticas GRC.

>>>>>>> feat/cap1-complete-user-stories
:::userstory
**História.**  
Como **GRC / Gestão** quero que cada aceitação de risco tenha **owner, prazo de validade (TTL)**, **critérios de encerramento** e **notificação automática** antes da expiração.

**Critérios de aceitação (BDD).**
- Dado que uma exceção/aceitação é registada  
- Quando a aprovo  
- Então ficam definidos **owner**, **TTL**, **condições de fecho** e **alertas de expiração**

**Checklist.**
- [ ] Owner designado  
- [ ] TTL definido e registado  
- [ ] Critérios de encerramento documentados  
- [ ] Notificação/alerta configurado
:::

---

### US-05 – Validação antes do go-live

**Contexto.**  
Antes de entrar em produção é necessário validar se todos os requisitos aplicáveis foram cumpridos.

<<<<<<< HEAD
=======
**📖 Rationale.**  
- **Referências:** SSDF RV.3, BSIMM SE3.5.

>>>>>>> feat/cap1-complete-user-stories
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

---

### US-06 – Mapeamento de ameaças por nível de risco

**Contexto.**  
Cada nível de criticidade deve ser confrontado com ameaças conhecidas para validar cobertura.

<<<<<<< HEAD
=======
**📖 Rationale.**  
- **Referências:** OWASP Top 10, CAPEC, OSC&R.

>>>>>>> feat/cap1-complete-user-stories
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

**Ligações úteis.**
- 🔗 [Mapeamento de Ameças com Risco](/sbd-toe/sbd-manual/classificacao-aplicacoes/addon/mapeamento-ameacas-risco)
<<<<<<< HEAD

---

### **US-09 – Classificar artefactos técnicos (Pipeline / IaC / Imagem)**

**Contexto.**  
Pipelines CI/CD, projetos IaC e imagens/container são **produtos** e devem ter criticidade e controlos proporcionais (Cap. 07, 08, 09).

:::userstory
**História.**  
Como **Plataforma / DevOps** quero **classificar os artefactos técnicos** relacionados (pipeline, IaC, imagens) e aplicar **controlos proporcionais** nos capítulos respetivos.

=======

---

### **US-09 – Classificar artefactos técnicos (Pipeline / IaC / Imagem)**

**Contexto.**  
Pipelines CI/CD, projetos IaC e imagens/container são **produtos** e devem ter criticidade e controlos proporcionais (Cap. 07, 08, 09).

**📖 Rationale.**  
- **Referências:** DSOMM (Tooling/Build), SSDF PW.5, Cap. 07/08/09.

:::userstory
**História.**  
Como **Plataforma / DevOps** quero **classificar os artefactos técnicos** relacionados (pipeline, IaC, imagens) e aplicar **controlos proporcionais** nos capítulos respetivos.

>>>>>>> feat/cap1-complete-user-stories
**Critérios de aceitação (BDD).**
- Dado que existem artefactos técnicos associados ao projeto  
- Quando aplico o modelo de classificação adaptado  
- Então atribuo nível L1–L3 e **ligo os controlos** aos capítulos 07/08/09

**Checklist.**
- [ ] Artefactos identificados (pipeline/IaC/imagem)  
- [ ] Nível atribuído por artefacto  
- [ ] Controlos proporcionais de 07/08/09 associados e registados
:::

---

### **US-10 – KPIs e reporting de classificação e conformidade**

**Contexto.**  
Sem indicadores, não há governança efetiva nem melhoria contínua.

<<<<<<< HEAD
=======
**📖 Rationale.**  
- **Referências:** SAMM Governance, DSOMM Metrics.

>>>>>>> feat/cap1-complete-user-stories
:::userstory
**História.**  
Como **GRC / Plataforma** quero consolidar **KPIs** sobre a classificação e exceções para medir adoção e conformidade.

**Critérios de aceitação (BDD).**
- Dado que existem classificações e aceitações ativas  
- Quando consolido os dados  
- Então obtenho KPI(s): **% apps com classificação válida**, **% exceções expiradas**, **lead time para reclassificar**

**Checklist.**
- [ ] Dashboard/KPI publicado  
- [ ] Fonte única de dados definida  
- [ ] Periodicidade de reporte acordada
:::

---

## 📑 Artefactos esperados (por fase)

| Fase         | Artefacto                          | Quem produz         | Onde fica                  | Evidência mínima                              |
|--------------|------------------------------------|---------------------|----------------------------|-----------------------------------------------|
| Início       | `classificacao-aplicacao.yaml`     | Dev / Tech Lead     | Repo `security/`           | Commit + revisão AppSec                       |
| Planeamento  | `matriz-controlos.md`              | Dev / Tech Lead     | Backlog / wiki             | REQ-XXX referenciados (Cap. 02)               |
| Revisão      | `classificacao-revisao.md`         | AppSec              | Repo `docs/`               | Ata/issue datada                              |
| Release      | `checklist-go-live.md`             | QA / Testes         | Pipeline CI/CD             | Aprovação formal AppSec                       |
| Operação     | `risco-residual.md`                | GRC / Compliance    | Ferramenta GRC / repo      | Owner + TTL + critérios de encerramento       |
| Contínuo     | `kpi-classificacao.csv/md`         | GRC / Plataforma    | Repositório de reporting   | Série temporal de KPIs + data de atualização  |

> **Formato canónico de evidência** (sugestão): `id`, `data`, `eixos` (E/D/I), `nível`, `decisão`, `owner`, `ligações` (issues/PRs), `expiração` (se aplicável).

---

## 📊 Matriz de proporcionalidade L1–L3

| Prática / Story                                 | L1 | L2 | L3 | Observações |
|-------------------------------------------------|----|----|----|-------------|
| US-01 – Classificação inicial                    | ✔  | ✔  | ✔  | Maior formalismo em L3 |
| US-02 – Aplicação da matriz (c/ REQ-XXX)        | ✔  | ✔  | ✔  | Rastreabilidade para Cap. 02 |
| US-03 – Revisão por alteração relevante          | ✔  | ✔  | ✔  | Event-based |
| **US-07 – Revisão periódica time-based**         | ✔  | ✔  | ✔  | 12/6/3 meses (típico) |
| US-04 – Risco residual                           | (opcional) | ✔ | ✔ | L1 apenas se risco crítico |
| **US-08 – Aceitação com TTL**                    | (opcional) | ✔ | ✔ | Obrigatório TTL em L2/L3 |
| US-05 – Validação go-live                        | (opcional) | recomendado | ✔ | Formal em L3 |
| US-06 – Mapeamento de ameaças                    | (opcional) | ✔ | ✔ | Completo/contínuo em L3 |
| **US-09 – Classificação de artefactos técnicos** | (conforme) | ✔ | ✔ | Aplica 07/08/09 |
| **US-10 – KPIs e reporting**                     | ✔  | ✔  | ✔  | Governação contínua |

---

## 📝 Recomendações operacionais

- Integrar a classificação de risco desde o **kick-off** do projeto.  
- Reavaliar a classificação **por alteração** e **por calendário** (time-based).  
- Manter a documentação **versionada e rastreável** em repositório controlado.  
- Mapear requisitos diretamente para **REQ-XXX (Cap. 02)** no backlog.  
- Exigir **TTL/expiração** em todas as aceitações de risco.  
- Validar proporcionalidade no go-live e documentar evidências.  
- Consolidar **KPIs** organizacionais para *compliance* e melhoria contínua.  
- Alinhar práticas com as **políticas organizacionais** de classificação, exceções e revisão periódica.

