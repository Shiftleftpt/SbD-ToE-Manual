---
id: aplicacao-lifecycle
title: Como Fazer
description: Como aplicar práticas de desenvolvimento seguro em cada fase do SDLC, com user stories reutilizáveis, artefactos auditáveis e matriz proporcional L1–L3
tags: [desenvolvimento, ciclo-de-vida, codificação-segura, validação, user-stories]
sidebar_position: 15
---

# ⚙️ Aplicação no Ciclo de Vida - Desenvolvimento Seguro

O desenvolvimento seguro não é um exercício teórico ou uma “boa prática” vaga: exige aplicação consistente em cada fase do ciclo de vida do software.  
Neste documento mostramos **como transformar as prescrições do capítulo em prática diária**, detalhando quando aplicar, quem executa, que user stories devem entrar no backlog e quais as evidências que permitem auditoria e governação.  
O objetivo é simples mas ambicioso: fazer do desenvolvimento seguro um hábito mensurável, rastreável e parte intrínseca da qualidade do produto.

---

## 🧭 Quando aplicar

A segurança acompanha o projeto desde o início e não pode ser relegada para fases finais.  
O quadro seguinte mostra **em que momentos concretos do SDLC** cada prática deve ser aplicada e qual a ação esperada em cada um deles.

| Fase do SDLC          | Momento específico                         | Ação esperada                                       |
|-----------------------|---------------------------------------------|-----------------------------------------------------|
| Planeamento           | Definição de stack, dependências, guidelines| Criar/adaptar guidelines seguras                    |
| Desenvolvimento       | Ao escrever/refatorar código                | Aplicar linters, validações locais                  |
| Revisão de Código     | Em cada PR / merge                         | Checklist e validação formal                        |
| Integração Contínua   | Execução do pipeline                        | SAST, validação de dependências e *rulesets*        |
| Pré-produção          | Go-live / release                          | Validação de exceções, checklist final              |
| Operação / Manutenção | Atualizações, patches, refatorizações       | Revisão de guidelines, dependências e exceções      |

---

## 👥 Quem executa cada ação

A segurança no desenvolvimento é um **esforço coletivo**: diferentes papéis contribuem de forma complementar, formando uma cadeia de confiança.  
A tabela seguinte explicita estas responsabilidades.

| Papel/Função                      | Responsabilidades principais |
|-----------------------------------|------------------------------|
| **Desenvolvedor**                 | Aplicar guidelines, linters e validações locais; propor *tailoring* de regras quando necessário |
| **Revisor Técnico**               | Validar PRs, confirmar critérios de segurança e exceções; aplicar checklist formal |
| **Equipa AppSec**                 | Definir critérios mínimos, aprovar exceções, validar dependências críticas; mapear ASVS/CWE |
| **DevSecOps / CI/CD**             | Automatizar linters/SAST, versionar e distribuir *rulesets* organizacionais; aplicar enforcement |
| **Gestor Técnico / Lead de Stack**| Criar/selecionar guidelines base por stack; aprovar derivadas de linters/analisadores; assegurar revisão periódica |

---

## 📖 User Stories reutilizáveis
### US-01 - Guidelines de Desenvolvimento Seguro

**Contexto.**  
Guidelines claras e versionadas por *stack* evitam decisões ad-hoc e asseguram consistência. Mais do que um documento estático, são um **mecanismo vivo** de governação: atualizadas, revistas e aplicadas diariamente. A existência de *rulesets* derivadas de linters e analisadores automáticos, com *tailoring* documentado, reduz significativamente riscos de interpretação subjetiva.

:::userstory
**História.**   
Como **Desenvolvedor**, quero aplicar as guidelines de código seguro aprovadas, para garantir consistência e reduzir vulnerabilidades desde o início.

**Critérios de aceitação (BDD).**
- Dado que inicio desenvolvimento numa *stack* definida  
- Quando consulto as guidelines aprovadas  
- Então aplico as regras mínimas obrigatórias e registo qualquer desvio justificado

**Checklist.**
- [ ] `guidelines-stack.md` referenciado no README do projeto  
- [ ] Ficheiros de configuração de linters/analisadores presentes e versionados  
- [ ] Regras mínimas aplicadas  
- [ ] *Tailoring* documentado (`rules/README.md`) e aprovado  
- [ ] Desvios registados em `excecoes-seguranca.md`  
- [ ] Evidência de revisão do PR

:::

**Artefactos & evidências.**
- Artefactos: `guidelines-stack.md`, diretório `rules/`  
- Evidência: commit IDs + histórico do PR

**Proporcionalidade por risco.**
| Nível | Obrigatório? | Ajustes |
|-------|--------------|---------|
| L1    | Sim          | Regras upstream com ajustes mínimos |
| L2    | Sim          | Conjunto organizacional curado |
| L3    | Sim          | Auditoria periódica e *policy-as-code* |

**Integração no SDLC.**
| Fase        | Trigger           | Responsável              | SLA             |
|-------------|-------------------|--------------------------|-----------------|
| Planeamento | Definição de stack| Gestor Técnico + Dev     | Antes do 1.º sprint |

**Ligações úteis.**  
xref:sbd-toe:cap06:intro

---

### US-02 - Revisão de Código Segura

**Contexto.**  
Revisões de código não são apenas uma prática de qualidade, mas um **ponto de controlo de segurança**. Quando sistematizadas com checklist, previnem vulnerabilidades, promovem partilha de conhecimento e criam registo formal de conformidade.

:::userstory
**História.**   
omo **Scrum Master/Team Lead**, quero garantir que cada PR é revisto com checklist de segurança obrigatória, para prevenir vulnerabilidades e manter registo de conformidade.
*Critérios de aceitação (BDD).**
- Dado que um PR é criado  
- Quando é submetido à revisão  
- Então a checklist de segurança é preenchida e o PR apenas é aceite após validação

**Checklist.**
- [ ] `checklist-pr.md` incluído no **template de PR**  
- [ ] Itens críticos validados (autenticação, entradas, dependências)  
- [ ] Comentários de segurança registados quando aplicável  
- [ ] **PR rejeitado automaticamente se checklist não estiver completa**
:::

**Artefactos & evidências.** 
`checklist-pr.md` (PR template), histórico e comentários no PR

**Proporcionalidade por risco.**
| Nível | Obrigatório? | Ajustes |
|-------|--------------|---------|
| L1    | Sim          | Checklist básica |
| L2    | Sim          | Checklist completa + dupla revisão |
| L3    | Sim          | Revisão dedicada com foco em segurança |

**Integração no SDLC.**
| Fase            | Trigger   | Responsável      | SLA          |
|-----------------|-----------|------------------|--------------|
| Revisão de Código| PR aberto| Revisor Técnico  | Antes do merge |


---

### US-03 - Gestão de Dependências no Código

**Contexto.**  
Cada dependência externa adicionada ao projeto é uma potencial porta de entrada para riscos de cadeia de fornecimento. A gestão rigorosa destas dependências garante que não se introduz software obsoleto, vulnerável ou malicioso.

:::userstory
**História.**   
Como **AppSec**, quero validar e justificar dependências externas, para reduzir riscos de supply chain e garantir compliance.

**Critérios de aceitação (BDD).**
- Dado que foi proposta uma nova dependência  
- Quando avalio licença, manutenção e CVEs associados  
- Então aprovo ou recuso com decisão registada

**Checklist.**
- [ ] Dependência listada em `sbom-deps.json`  
- [ ] Licença compatível com política da organização  
- [ ] Sem CVEs críticos (ou exceção formal aprovada)  
- [ ] Decisão documentada em ticket

:::

**Artefactos & evidências.**
- Artefacto: `sbom-deps.json`  
- Evidência: ticket de aprovação com justificativa

**Proporcionalidade por risco.**
| Nível | Obrigatório? | Ajustes |
|-------|--------------|---------|
| L1    | Sim          | Aprovação simplificada |
| L2    | Sim          | Aprovação formal + proveniência registada |
| L3    | Sim          | Política de pinning/lockfile obrigatório |

**Integração no SDLC.**
| Fase          | Trigger             | Responsável        | SLA            |
|---------------|---------------------|--------------------|----------------|
| Desenvolvimento | Inclusão dependência | Dev + AppSec       | Antes do merge |

**Nota - cruza com outras práticas**
Esta user story cruza com praticas como [Dependências, SBOM e SCA](/sbd-toe/sbd-manual/dependencias-sbom-sca) e, de certa forma permite a monitorização de *drift* como indicado em [Monitorização & Operações](/sbd-toe/sbd-manual/monitorixacao-operacoes).

---

### US-04 - Automatização em CI/CD (Linters & SAST)

**Contexto.**  
A automatização de validações em pipelines CI/CD garante consistência, acelera a deteção de falhas e cria evidência contínua. Automatizar significa **remover o fator humano de distração ou esquecimento** em controlos repetitivos.

:::userstory
**História.**   
Como **DevSecOps**, quero integrar linters e SAST no pipeline, para detetar falhas precocemente e gerar evidência contínua.

**Critérios de aceitação (BDD).**
- Dado que o pipeline é executado  
- Quando correm linters e SAST  
- Então relatórios são arquivados e a build falha em findings críticos

**Checklist.**
- [ ] Jobs configurados no pipeline  
- [ ] Thresholds de severidade definidos  
- [ ] Relatórios arquivados de forma imutável  
- [ ] Build falha em findings críticos

:::

**Artefactos & evidências.**
- Artefacto: `ci/pipeline.yml`  
- Evidência: relatórios SARIF/JSON arquivados

**Proporcionalidade por risco.**
| Nível | Obrigatório? | Ajustes |
|-------|--------------|---------|
| L1    | Sim          | Linters básicos + SAST leve |
| L2    | Sim          | SAST completo + *gating* de severidade |
| L3    | Sim          | SAST + validações adicionais (IaC/DAST) |

**Integração no SDLC.**
| Fase | Trigger           | Responsável | SLA       |
|------|-------------------|-------------|-----------|
| CI/CD| Execução pipeline | DevSecOps   | Cada build|

**Ligações úteis.**  
xref:sbd-toe:cap07:intro

---
### US-05 - Gestão de Exceções Técnicas

**Contexto.**  
Nem sempre todos os controlos podem ser aplicados em tempo útil. É inevitável lidar com exceções técnicas - mas se estas não forem **formalmente registadas, aprovadas e temporárias**, tornam-se dívida de risco e criam vulnerabilidades persistentes.

:::userstory
**História.**   
Como **AppSec**, quero registar e aprovar exceções técnicas, para garantir rastreabilidade, mitigação e revisão futura.

**Critérios de aceitação (BDD).**
- Dado que uma exceção é solicitada  
- Quando avalio justificação e mitigação propostas  
- Então aprovo ou recuso e defino prazo de validade

**Checklist.**
- [ ] Exceção registada em `excecoes-seguranca.md`  
- [ ] Mitigação alternativa definida  
- [ ] Prazo de validade atribuído  
- [ ] Reavaliação agendada  

:::

**Artefactos & evidências.**
- Artefacto: `excecoes-seguranca.md`  
- Evidência: aprovação formal em issue/PR

**Proporcionalidade por risco.**
| Nível | Obrigatório? | Ajustes |
|-------|--------------|---------|
| L1    | Sim          | Exceções simples e raras |
| L2    | Sim          | Revalidação por sprint |
| L3    | Sim          | Aprovação executiva + plano compensatório |

**Integração no SDLC.**
| Fase   | Trigger          | Responsável     | SLA             |
|--------|------------------|-----------------|-----------------|
| Release| Exceção solicitada| AppSec + PO     | Antes do go-live|

**Ligações úteis.**  
xref:sbd-toe:cap02:intro

---

### US-06 - Uso Validado de GenIA

**Contexto.**  
Ferramentas de IA generativa (GenIA) aceleram a escrita de código, mas podem introduzir **vulnerabilidades ou violações de licença**. O seu uso deve ser rastreável, validado e sempre sujeito a revisão técnica humana.

:::userstory
**História.**   
Como **Desenvolvedor**, quero usar IA generativa com revisão obrigatória, para acelerar produtividade sem comprometer segurança.

**Critérios de aceitação (BDD).**
- Dado que gero código com GenIA  
- Quando anoto origem e submeto a revisão  
- Então só é aceite se cumprir guidelines e licenciamento

**Checklist.**
- [ ] Uso registado em `uso-genia.md`  
- [ ] Revisão técnica aplicada  
- [ ] Conformidade de licença verificada  
- [ ] Evidência anexada ao PR  

:::

**Artefactos & evidências.**
- Artefacto: `uso-genia.md`  
- Evidência: comentários de revisão + validações no PR

**Proporcionalidade por risco.**
| Nível | Obrigatório? | Ajustes |
|-------|--------------|---------|
| L1    | Opcional     | Registo simples |
| L2    | Sim          | Registo + revisão técnica |
| L3    | Sim          | Revisão formal + validações adicionais |

**Integração no SDLC.**
| Fase          | Trigger  | Responsável        | SLA           |
|---------------|----------|--------------------|---------------|
| Desenvolvimento| Uso GenIA| Dev + Revisor Técnico| Antes do merge|

**Ligações úteis.**  
xref:sbd-toe:cap06:intro

---

### US-07 - Governação e Curadoria de Guidelines

**Contexto.**  
A governação ativa das guidelines assegura que estas evoluem com as tecnologias e com as vulnerabilidades emergentes.  
A publicação formal e a revisão periódica são mecanismos de controlo e conformidade.

:::userstory
**História.**   
::userstory
**História.**  
Como **AppSec Engineer**, quero rever e publicar guidelines curadas trimestralmente, para garantir atualização contínua e governação formal das práticas de desenvolvimento seguro.

**Critérios de aceitação (BDD).**
- Dado que decorre o ciclo de revisão ou surge nova *stack*  
- Quando as *rulesets* são atualizadas  
- Então é publicada uma **release/tag** aprovada por **Gestão Executiva** e **AppSec Engineer**

**Checklist.**
- [ ] *Rulesets* avaliados e documentados  
- [ ] *Tailoring* validado  
- [ ] Configurações versionadas e publicadas  
- [ ] Changelog incluído na release  
- [ ] Revisão periódica registada  
- [ ] Mapeamento atualizado para ASVS/CWE
:::

**Artefactos & evidências.**
- Artefacto: diretório `rules/`  
- Evidência: release/tag + changelog
- Aprovação AppSec 

**Proporcionalidade por risco.**
| Nível | Obrigatório? | Ajustes |
|-------|--------------|---------|
| L1    | Opcional     | Uso de regras upstream *default* |
| L2    | Sim          | Curadoria organizacional obrigatória |
| L3    | Sim          | *Policy-as-code* + distribuição controlada |

**Integração no SDLC.**
| Fase      | Trigger             | Responsável           | SLA     |
|-----------|---------------------|-----------------------|---------|
| Governação| Nova stack ou revisão| Gestor Técnico + AppSec| Até 2 sem.|


---

### US-08 - Rastreabilidade com Anotações de Segurança

**Contexto.**  
Validações de segurança devem ser rastreáveis até aos requisitos originais. Anotações padronizadas (`@sec:*`) no código e nos testes permitem **ligar implementação, requisitos e evidência de auditoria** de forma inequívoca.

:::userstory
**História.**   
Como **Desenvolvedor**, quero anotar validações de segurança com `@sec:*`, para garantir rastreabilidade ponta-a-ponta até ao backlog.

**Critérios de aceitação (BDD).**
- Dado que implemento requisito de segurança  
- Quando adiciono anotação `@sec:*`  
- Então o requisito fica rastreável até ao backlog e relatórios de CI/CD

**Checklist.**
- [ ] Anotações incluídas em código/testes  
- [ ] Referência cruzada a requisitos (`SEC-*`)  
- [ ] Relatórios exportam anotações  
- [ ] Evidência arquivada  

:::

**Artefactos & evidências.**
- Artefacto: código comentado, testes anotados  
- Evidência: relatórios de CI/CD

**Proporcionalidade por risco.**
| Nível | Obrigatório? | Ajustes |
|-------|--------------|---------|
| L1    | Opcional     | Apenas em módulos críticos |
| L2    | Sim          | Todas as validações de segurança |
| L3    | Sim          | Anotações + validação automática |

**Integração no SDLC.**
| Fase              | Trigger                | Responsável | SLA        |
|-------------------|------------------------|-------------|------------|
| Desenvolvimento   | Implementação de requisito | Dev + QA   | Até ao merge|

---

### US-08 – Rastreabilidade com Anotações de Segurança

*(mantida, terminologia normalizada – Dev e QA responsáveis pela rastreabilidade `@sec:*`)*

---

### US-09 – Gate de Segurança Pré-release

**Contexto.**  
Antes de cada *release* deve existir um ponto de controlo objetivo que consolide todas as evidências de segurança — relatórios SAST, SBOM, exceções, checklists e aprovações.

:::userstory
**História.**  
Como **DevOps/SRE**, quero executar um **gate de segurança pré-release** que agregue todas as evidências de validação, para só permitir publicações conformes com os requisitos de segurança.

**Critérios de aceitação (BDD).**
- Dado que existe uma *release* candidata  
- E o nível de risco L1–L3 foi atribuído  
- Quando o *security gate* é executado  
- Então o resultado é binário (Aprovado/Rejeitado) e é registado como artefacto da release

**Checklist.**
- [ ] *Job* `release-security-gate` configurado no pipeline  
- [ ] Relatório agregado anexado à *tag/release*  
- [ ] Ligações a SAST, SBOM, exceções e checklist de PR  
- [ ] Bloqueio automático em caso de falha  
- [ ] Aprovação final por **AppSec Engineer** e **Gestão Executiva** (L3)
:::

**Artefactos & evidências.** `gate-relatorio.md`, anexos CI/CD, *tag/release* assinada

**Proporcionalidade.**
| Nível | Obrigatório? | Ajustes |
|-------|---------------|---------|
| L1 | Sim | Gate básico (SAST + SBOM + checklist) |
| L2 | Sim | Gate reforçado com política de exceções |
| L3 | Sim | *Policy-as-code* e dupla aprovação formal |

---

### US-10 – Perfis de Validação por Nível de Risco (L1–L3)

**Contexto.**  
A aplicação proporcional dos controlos é essencial para garantir eficiência e consistência.  
Cada aplicação deve herdar um perfil técnico de validação compatível com a sua classificação de risco.

:::userstory
**História.**  
Como **AppSec Engineer**, quero definir e aplicar **perfis de validação L1–L3** que determinem regras, limiares e *quality gates* adequados ao risco, para uniformizar a execução e auditoria.

**Critérios de aceitação (BDD).**
- Dado que a aplicação tem classificação L1/L2/L3  
- Quando é executado o pipeline  
- Então são aplicadas as regras e limiares correspondentes ao perfil definido

**Checklist.**
- [ ] Perfis L1–L3 documentados e aprovados  
- [ ] *Rulesets* correspondentes no pipeline  
- [ ] Métricas de severidade e cobertura definidas  
- [ ] Auditoria trimestral aos perfis e thresholds
:::

**Artefactos & evidências.** `matriz-proporcionalidade-dev.md`, `ci/pipeline.yml`, relatórios de auditoria

**Proporcionalidade.**
| Nível | Obrigatório? | Ajustes |
|-------|---------------|---------|
| L1 | Sim | Cada aplicação tera o seu nivel de controlos adequado ao nivel de classificação|
| L2 | Sim | Cada aplicação tera o seu nivel de controlos adequado ao nivel de classificação |
| L3 | Sim | Cada aplicação tera o seu nivel de controlos adequado ao nivel de classificação |

---

### US-11 – Arquivo Central de Evidências de Validação

**Contexto.**  
A retenção controlada de evidências é requisito de auditoria e conformidade.  
As provas de execução dos controlos devem ser exportadas e arquivadas de forma segura, imutável e auditável.

:::userstory
**História.**  
Como **QA** e **DevOps/SRE**, quero **arquivar centralmente todas as evidências de validação** (relatórios SAST, SBOM, exceções, `@sec:*`), para garantir rastreabilidade e cumprimento de requisitos de auditoria.

**Critérios de aceitação (BDD).**
- Dado que o pipeline executa validações  
- Quando conclui a execução  
- Então exporta e arquiva relatórios e evidências num repositório controlado e versionado

**Checklist.**
- [ ] Repositório de evidências definido (preferencialmente WORM)  
- [ ] Export automático por *build/release*  
- [ ] Índice de evidências por aplicação e *commit*  
- [ ] Política de retenção definida (≥ 2 anos; L3 ≥ 5 anos)  
- [ ] Acesso auditado e controlado
:::

**Artefactos & evidências.** 
diretório `evidencias/`, `evidencias-index.json`, registos de acesso

**Proporcionalidade.**
| Nível | Obrigatório? | Ajustes |
|-------|---------------|---------|
| L1 | Sim | Retenção mínima e export básico |
| L2 | Sim | Export assinado + índice por componente |
| L3 | Sim | Armazenamento imutável e verificação periódica de integridade |

---

## 📦 Artefactos Esperados

| Artefacto               | Evidência auditável                                   |
|--------------------------|-------------------------------------------------------|
| `guidelines-stack.md`    | Guidelines curadas e aprovadas, com *changelog*      |
| `rules/`                 | *Rulesets* versionados e aprovados                   |
| `checklist-pr.md`        | Checklist formal integrada em PRs                    |
| `sbom-deps.json`         | SBOM validado e aprovado                             |
| `gate-relatorio.md`      | Relatório consolidado do *security gate*             |
| `excecoes-seguranca.md`  | Registo de exceções e aprovações                     |
| `uso-genia.md`           | Registo e revisão de uso de GenIA                    |
| `evidencias/`            | Arquivo centralizado e indexado de evidências        |

---

## ⚖️ Matriz de Proporcionalidade L1–L3

| Prática / Controlo | L1 (baixo) | L2 (médio) | L3 (crítico) |
|--------------------|------------|-------------|--------------|
| Guidelines | Regras upstream | Curadas por stack | Auditadas e *policy-as-code* |
| Revisão de código | Checklist básica | Dupla revisão | Revisão formal AppSec |
| Dependências | Validação simples | Validação formal | SBOM rastreável |
| CI/CD | Linters básicos | SAST obrigatório | SAST + IaC/DAST + políticas |
| Exceções | Registo simples | Reavaliação periódica | Dupla aprovação |
| GenIA | Registo opcional | Revisão técnica | Revisão formal e licenças |
| Governação | Curadoria anual | Trimestral | Contínua e automatizada |
| Evidências | Export manual | Export automático | Arquivo imutável e auditado |
| *Security Gate* | Básico | Completo | Reforçado e automatizado |

---

## 🏁 Recomendações Finais

O desenvolvimento seguro deve ser tratado como um **processo contínuo e mensurável**.  
As *user stories* deste capítulo operacionalizam as prescrições normativas, assegurando que cada prática deixa rasto verificável e que o grau de aplicação é proporcional ao risco.  
A integração destas ações no *backlog* e no pipeline transforma a segurança de software em disciplina diária e auditável.

Em síntese: o capítulo demonstra que **desenvolvimento seguro é a fundação sobre a qual o resto do ciclo de vida assenta**.  
Sem ele, nenhuma prática subsequente - seja CI/CD, IaC ou runtime - consegue oferecer confiança total.
