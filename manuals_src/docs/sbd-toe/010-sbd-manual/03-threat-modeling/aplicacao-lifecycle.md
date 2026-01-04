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

| Fase / Evento                    | Ação esperada                                                                 | Quem participa                                                     | Evidência mínima (artefacto principal) |
|----------------------------------|------------------------------------------------------------------------------|--------------------------------------------------------------------|----------------------------------------|
| Início de projeto / épico        | Criar baseline do Threat Model e definir âmbito/assunções                     | DevOps/SRE, Product Owner, Arquitetos, AppSec, Team Lead           | DFD + lista inicial de ameaças + registo de decisão (*baseline*) |
| Grooming / Planeamento           | Rever impacto de novas user stories no Threat Model (delta)                   | Developer, Arquiteto (quando aplicável), AppSec                    | Atualização versionada + ligação a backlog (`THREAT-*`)          |
| Revisão de Arquitetura / ADR     | Validar ameaças antes de decisões arquiteturais irreversíveis                 | Arquitetos, AppSec, Team Lead                                      | ADR + Threat Model revisto + decisões por ameaça                 |
| Alterações críticas / refactors  | Revalidar o modelo quando há mudança estrutural (fluxos, trust boundaries, deps) | Developer, QA/Test, Arquiteto, AppSec                              | Modelo atualizado + diffs + justificações                         |
| Release / Go-live                | Confirmar ameaças abertas, exceções, risco residual e compensações            | QA/Test, AppSec, Product Owner (impacto), Team Lead                | Decisões (mitigar/aceitar) + evidência de aprovação              |
| CI/CD (gate de controlo)         | Verificar “frescura” do Threat Model face a mudanças relevantes (determinístico) | DevOps/SRE, AppSec                                                 | Resultado de verificação + link para versão do modelo             |

---

## 👥 Quem faz o quê

| Papel / Função             | Responsabilidades-chave |
|----------------------------|--------------------------|
| Arquitetos de Software     | Facilitar sessões, manter modelos atualizados e garantir consistência arquitetural |
| Team Lead / Tech Lead      | **Responsável pela decisão final do modelo** no contexto da equipa/projeto (aprovação do baseline e revisões) |
| Developer                  | Identificar fluxos, pontos de entrada, regras de negócio e mudanças técnicas relevantes |
| QA / Test Engineer         | Traduzir ameaças em critérios de aceitação e validar evidência de mitigação/testes |
| AppSec Engineer            | Identificar ameaças técnicas, rever mitigação, validar risco residual e apoiar decisões de exceção |
| Product Owner              | Priorizar mitigação pelo impacto no negócio e aceitar trade-offs explícitos |
| DevOps/SRE                 | Implementar gates determinísticos, assegurar rastreabilidade e retenção de evidência |

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
  **Então** as ameaças identificadas ficam registadas com decisões explícitas e evidência mínima,
  **e** as assunções/limites do modelo ficam documentados.

**Checklist.**
- [ ] Sessão de threat modeling realizada  
- [ ] DFDs criados e documentados  
- [ ] Ameaças catalogadas (STRIDE, LINDDUN, PASTA)  
- [ ] Ameaças ligadas a requisitos de mitigação  
- [ ] Evidência arquivada em repositório de arquitetura
- [ ] Âmbito, assunções e limites do modelo documentados
- [ ] Responsável pela aprovação do baseline identificado

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

### US-05 - Gate de controlo de consistência no CI/CD

**Contexto.**  
O pipeline deve garantir que mudanças relevantes não passam sem atualização/revisão do Threat Model, mantendo rastreabilidade e evidência.

:::userstory
**História.**  
Como **DevOps/SRE** e **AppSec Engineer**, quero aplicar um **gate determinístico** que verifique se o Threat Model está atualizado face a alterações relevantes, para impedir releases com modelo obsoleto.

**Critérios de aceitação (BDD).**
- **Dado** que uma alteração relevante é introduzida (ex.: novo fluxo, nova dependência, nova trust boundary)  
  **Quando** a pipeline é executada  
  **Então** o gate exige referência a uma versão atualizada do Threat Model ou uma justificação aprovada  
- **E** a evidência do gate fica registada e auditável

**Checklist.**
- [ ] Critérios objetivos de “alteração relevante” definidos e versionados
- [ ] Gate implementado com verificação determinística (regras, metadados, diffs)
- [ ] Saída do gate registada (logs + referência ao artefacto versionado)
- [ ] Exceções seguem workflow de aprovação (quando aplicável)

:::

**Artefactos & evidências.**
- Artefacto: regra/versionamento de critérios + referência ao Threat Model aprovado
- Evidência: logs de pipeline + link para commit/tag do modelo

**Proporcionalidade por risco.**
| Nível | Obrigatório? | Ajustes |
|---|---|---|
| L1 | Não | Apenas revisão manual em releases maiores |
| L2 | Sim | Gate não-bloqueante com alerta e obrigação de revisão |
| L3 | Sim | Gate bloqueante com exceções formais e prazo |

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

---
### US-07 - Reutilização controlada e revisão de modelos anteriores

**Contexto.**  
A reutilização de modelos anteriores é útil, mas introduz risco quando o contexto mudou. Deve existir revisão explícita antes de considerar um modelo como válido.

:::userstory
**História.**  
Como **Arquitetos de Software** e **AppSec Engineer**, quero reutilizar modelos anteriores apenas com revisão explícita de mudanças de contexto, para reduzir omissões e evitar decisões herdadas incorretas.

**Critérios de aceitação (BDD).**
- **Dado** que existe um modelo anterior semelhante  
  **Quando** o reutilizo como base  
  **Então** documento diferenças de contexto/arquitetura e valido novamente decisões críticas  
- **E** registo um responsável pela aprovação da revisão

**Checklist.**
- [ ] Modelo anterior identificado (referência versionada)
- [ ] Diferenças de arquitetura/fluxos/dependências analisadas
- [ ] Decisões críticas revalidadas (mitigar/aceitar/transferir)
- [ ] Aprovação registada e auditável

:::

**Artefactos & evidências.**
- Artefacto: delta de revisão + referência ao modelo aprovado
- Evidência: PR/issue de revisão com aprovação

**Proporcionalidade por risco.**
| Nível | Obrigatório? | Ajustes |
|---|---|---|
| L1 | Opcional | Revisão simplificada |
| L2 | Sim | Revisão formal com diffs |
| L3 | Sim | Revisão formal + revisão independente |


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

---
### US-09 - Aprovação formal do Threat Model (baseline e revisões)

**Contexto.**  
O Threat Modeling só é controlo de segurança quando existe um modelo aprovado, com responsável e evidência mínima.

:::userstory
**História.**  
Como **Team Lead / Tech Lead** e **AppSec Engineer**, quero aprovar formalmente o Threat Model (baseline e revisões), para garantir decisão explícita, rastreabilidade e auditabilidade.

**Critérios de aceitação (BDD).**
- **Dado** que o Threat Model foi atualizado  
  **Quando** concluo a revisão  
  **Então** existe uma decisão formal de aprovação com responsável identificado  
- **E** a evidência mínima obrigatória está presente e versionada

**Checklist.**
- [ ] Âmbito, assunções e limites documentados
- [ ] Ameaças identificadas com decisão por item (mitigar/aceitar/transferir/rejeitar)
- [ ] Ligações a requisitos/mitigações criadas (ex.: `REQ-*`, `THREAT-*`)
- [ ] Evidência mínima anexada (diagramas/versionamento/decisão)
- [ ] Aprovação registada (PR/issue/assinatura conforme processo)

:::

**Artefactos & evidências.**
- Artefacto: Threat Model aprovado (versão/tag) + `decisions.md`
- Evidência: registo de aprovação + links para backlog e requisitos

**Proporcionalidade por risco.**
| Nível | Obrigatório? | Ajustes |
|---|---|---|
| L1 | Opcional | Aprovação leve (registo simples) |
| L2 | Sim | Aprovação formal por TL + AppSec |
| L3 | Sim | Aprovação formal + revisão independente (segregação) |

---

### US-10 - Controlo de acesso, classificação e retenção dos artefactos de Threat Modeling

**Contexto.**  
Diagramas e decisões de threat modeling são ativos sensíveis e devem ter proteção proporcional ao risco.

:::userstory
**História.**  
Como **Arquitetos de Software** e **DevOps/SRE**, quero controlar acesso e retenção dos artefactos de Threat Modeling, para reduzir risco de exposição de arquitetura e decisões críticas.

**Critérios de aceitação (BDD).**
- **Dado** que artefactos de Threat Modeling são produzidos  
  **Quando** são armazenados e partilhados  
  **Então** seguem regras de acesso mínimo, classificação e retenção definidas  
- **E** existe evidência de onde estão guardados e quem tem acesso

**Checklist.**
- [ ] Local de armazenamento definido e versionado
- [ ] Controlo de acesso aplicado (least privilege)
- [ ] Classificação definida (sensibilidade/partilha interna)
- [ ] Retenção e eliminação definidas (quando aplicável)
- [ ] Evidência de acessos e alterações disponível/auditável

:::

**Artefactos & evidências.**
- Artefacto: política/regras do repositório + estrutura de diretórios
- Evidência: ACLs/grupos + registos de auditoria (quando aplicável)

**Proporcionalidade por risco.**
| Nível | Obrigatório? | Ajustes |
|---|---|---|
| L1 | Sim | Controlo básico e armazenamento interno |
| L2 | Sim | Controlo formal + rastreio de alterações |
| L3 | Sim | Controlo reforçado + segregação e auditoria |

---
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
