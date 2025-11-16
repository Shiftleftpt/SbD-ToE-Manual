---
id: aplicacao-lifecycle
title: Como Fazer
description: Integração prática das práticas de validação contínua nas diferentes fases do ciclo de vida da aplicação
tags: [tipo:aplicacao, ciclo-vida, testes, seguranca, integracao, validacao]
genia: us-format-normalization
---

# 🧪 Aplicação de Testes de Segurança ao Longo do Ciclo de Vida

## 🧭 Quando aplicar

Os testes de segurança acompanham a aplicação em todas as fases - não são uma etapa final, mas um **ritmo contínuo** de validação.  
Desde a definição inicial de requisitos até à auditoria final, cada momento do ciclo de vida deve gerar **evidência objetiva** de que a aplicação está protegida contra falhas conhecidas e ameaças emergentes.  

| Fase SDLC / Evento | Ação de testes | Artefacto/Evidência |
|--------------------|----------------|---------------------|
| Especificação      | Definir requisitos de segurança testáveis e critérios de aceitação | Matriz de requisitos + Plano de testes |
| Desenvolvimento    | Executar SAST e linters; criar testes de regressão | Relatórios SAST + regressões |
| Pull request       | Executar SAST automático com comentários inline | Logs CI + SARIF |
| Build / CI         | Executar SCA, SAST, IAST (se aplicável), gerar SBOM | Logs pipeline + SBOM |
| Staging            | Executar DAST autenticado e fuzzing de endpoints críticos | Relatórios DAST + fuzzing |
| Pré-release        | Validar critérios de release e gerir exceções | Checklist release |
| Pós-release        | Fuzzing contínuo / IAST; monitorização dinâmica | Alertas + relatórios |
| Auditoria          | Realizar PenTesting ofensivo baseado em risco | Relatório técnico de PenTest |

---

## 👥 Quem executa cada ação

A responsabilidade pela qualidade dos testes é **coletiva**.  
Cada papel contribui com uma perspetiva única, mas só em conjunto se obtém um processo de validação robusto e auditável.  

| Papel | Responsabilidade |
|-------|------------------|
| **Dev** | Corrigir findings, criar regressões automatizadas |
| **QA/Testes** | Executar DAST, fuzzing, validar critérios |
| **AppSec** | Definir estratégia, *tuning* de regras, gerir findings e exceções |
| **DevOps** | Integrar scanners, gates e evidências no CI/CD |
| **Gestão de Produto** | Aprovar risco residual e decidir *go/no-go* |
| **PenTester** | Validar ofensivamente controlos e relatar impacto |

---

## 📖 User Stories Reutilizáveis

As histórias seguintes transformam princípios em prática.  
Cada US representa um **controlo essencial**, pensado para ser integrado diretamente no backlog da equipa e aplicado proporcionalmente ao risco da aplicação (L1–L3).  

---

### US-01 - Estratégia formal de testes por aplicação

A validação começa com planeamento.  
Sem uma estratégia clara, a cobertura torna-se desigual e impossível de auditar.  

**Contexto.**  
Sem estratégia, a cobertura é desigual e difícil de auditar.

:::userstory
**História.**   
Como **AppSec**, quero **definir uma estratégia de testes de segurança por aplicação**, para **assegurar cobertura proporcional ao risco e rastreabilidade com requisitos do Cap. 02**.

**Critérios de aceitação (BDD).**  
- **Dado** que a aplicação tem criticidade Lx  
  **Quando** defino a estratégia  
  **Então** os tipos de teste e gates ficam estabelecidos por L1–L3 e ligados a requisitos

**Checklist.**  
- [ ] Documento de estratégia versionado  
- [ ] Cobertura mínima por L1–L3 definida  
- [ ] Mapeamento Cap. 2 ⇄ testes publicado  

:::

**Artefactos & evidências.** Documento `strategy-testing.md`, matriz requisitos⇄testes.  

**Proporcionalidade por risco.**  
| Nível | Obrigatório? | Cobertura mínima |
|---|---|---|
| L1 | Sim | SAST + checklist |
| L2 | Sim | + DAST autenticado |
| L3 | Sim | + fuzzing/IAST + PenTest |

**Integração no SDLC.**  
| Fase | Trigger | Responsável | SLA |
|------|---------|-------------|-----|
| Planeamento | Classificação Lx / kick-off | AppSec | Até ao fim do 1.º sprint |

---

### US-02 - SAST obrigatório em Pull Request

Detetar cedo é sempre mais barato.  
Executar SAST no momento do PR garante que vulnerabilidades nunca chegam à *branch* principal.  

**Contexto.**  
PRs sem SAST permitem que vulnerabilidades entrem cedo no código base.

:::userstory
**História.**   
Como **Dev**, quero **executar SAST automático no PR com comentários inline**, para **corrigir vulnerabilidades antes do merge**.

**Critérios de aceitação (BDD).**  
- **Dado** que abro um PR  
  **Quando** o pipeline corre SAST  
  **Então** resultados aparecem inline e bloqueiam acima do threshold definido  

**Checklist.**  
- [ ] Trigger em PR ativo  
- [ ] Relatório SARIF anexado  
- [ ] Threshold por Lx aplicado  

:::

**Artefactos & evidências.** Logs CI + SARIF.  

**Proporcionalidade por risco.**  
| Nível | Política de gate |
|---|---|
| L1 | Aviso |
| L2 | Bloqueio High/Critical |
| L3 | Bloqueio Medium+ |

**Integração no SDLC.**  
| Fase | Trigger | Responsável | SLA |
|------|---------|-------------|-----|
| Revisão de código | Abertura de PR | Dev + DevOps | Antes do merge |

---

### US-03 - DAST autenticado em Staging

Muitas falhas críticas só se revelam após login.  
Executar DAST autenticado em staging é o passo natural antes de promover uma release.  

**Contexto.**  
Muitas falhas surgem apenas autenticadas.

:::userstory
**História.**   
Como **QA**, quero **executar DAST autenticado em staging**, para **detetar vulnerabilidades exploráveis em runtime**.

**Critérios de aceitação (BDD).**  
- **Dado** ambiente staging configurado  
  **Quando** executo DAST autenticado  
  **Então** relatórios são gerados e findings abertos no backlog  

**Checklist.**  
- [ ] Login flow configurado  
- [ ] Scope definido  
- [ ] Relatório anexado à release  

:::

**Artefactos & evidências.** Relatórios DAST.  

**Proporcionalidade por risco.**  
| Nível | Cobertura |
|---|---|
| L1 | Manual/exploratório |
| L2 | Automático autenticado |
| L3 | Automático + cobertura ampliada |

**Integração no SDLC.**  
| Fase | Trigger | Responsável | SLA |
|------|---------|-------------|-----|
| Staging | Build/Deploy em staging | QA | Antes da aprovação da release |

---

### US-04 - Gates de segurança no CI/CD

Sem gates, findings tornam-se meros relatórios ignorados.  
Gates automáticos são a barreira que impede regressões graves de avançar.  

**Contexto.**  
Sem gates, findings não impedem regressões.

:::userstory
**História.**   
Como **DevOps**, quero **integrar gates automáticos no pipeline (SAST/SCA/IAST) com thresholds por Lx**, para **evitar builds inseguros**.

**Critérios de aceitação (BDD).**  
- **Dado** um pipeline em execução  
  **Quando** um finding excede o threshold Lx  
  **Então** o job falha e a promoção é bloqueada até correção ou exceção aprovada  

**Checklist.**  
- [ ] Pipelines versionados com gates declarados  
- [ ] Thresholds por Lx publicados  
- [ ] Logs exportados  
- [ ] Exceções aprovadas (L3: dupla aprovação)  

:::

**Artefactos & evidências.** Configuração `ci.yml`, relatórios e registo de exceções.  

**Proporcionalidade por risco.**  
| Nível | Política |
|---|---|
| L1 | Aviso |
| L2 | Bloqueio High/Critical |
| L3 | Bloqueio Medium+ |

**Integração no SDLC.**  
| Fase | Trigger | Responsável | SLA |
|------|---------|-------------|-----|
| CI/CD | Execução pipeline | DevOps + AppSec | Em cada build |

**Detalhes de rastreabilidade (expandido):**  
- Logs de cada execução com timestamp, commit, branch, ferramentas executadas, thresholds aplicados  
- Relatório de exceptions aprovadas (ficheiro JSON com PR, justificação, aprovador, data de expiração)  
- Métricas de gates: % bloqueios por severidade, taxa de override, tempo médio de remediação  
- Dashboard Prometheus/Grafana com série histórica de findings bloqueados vs permitidos  
- Integração com backlog para abertura automática de issues para findings bloqueados  

---

### US-05 - Regressões de segurança automatizadas

Corrigir não chega - é preciso garantir que a mesma falha não regressa.  
Testes de regressão automatizados transformam cada correção numa proteção futura.  

**Contexto.**  
Falhas corrigidas voltam sem regressão automatizada.

:::userstory
**História.**   
Como **Dev**, quero **criar testes de regressão para findings corrigidos**, para **evitar reintrodução futura**.

**Critérios de aceitação (BDD).**  
- **Dado** um finding resolvido  
  **Quando** crio o teste de regressão  
  **Então** ele falha se a vulnerabilidade regressar  

**Checklist.**  
- [ ] Teste criado e versionado  
- [ ] Ligação ao finding original (ID)  
- [ ] Execução em builds futuros  

:::

**Artefactos & evidências.** Código de regressão + logs CI.  

**Proporcionalidade por risco.**  
| Nível | Exigência |
|---|---|
| L1 | Casos críticos |
| L2 | Por falha conhecida |
| L3 | Cobertura obrigatória |

**Integração no SDLC.**  
| Fase | Trigger | Responsável | SLA |
|------|---------|-------------|-----|
| Dev/CI | Fecho de finding | Dev | No PR de correção |

---

### US-06 - Fuzzing dirigido a APIs críticas

Testes convencionais não capturam todas as falhas.  
O fuzzing, ao explorar entradas inesperadas, revela vulnerabilidades invisíveis a olho nu.  

**Contexto.**  
Entradas complexas revelam falhas não cobertas.

:::userstory
**História.**   
Como **QA**, quero **aplicar fuzzing a endpoints críticos**, para **detectar falhas invisíveis em testes convencionais**.

**Critérios de aceitação (BDD).**  
- **Dado** endpoints críticos definidos  
  **Quando** executo fuzzing  
  **Então** anomalias são registadas com PoC mínima  

**Checklist.**  
- [ ] Targets e perfis definidos  
- [ ] Ambiente isolado de teste  
- [ ] Relatório com casos reproduzíveis  

:::

**Artefactos & evidências.** Relatório de fuzzing + corpora.  

**Proporcionalidade por risco.**  
| Nível | Cobertura |
|---|---|
| L1 | Opcional |
| L2 | Endpoints prioritários |
| L3 | Endpoints críticos obrigatórios |

**Integração no SDLC.**  
| Fase | Trigger | Responsável | SLA |
|------|---------|-------------|-----|
| Staging | Release candidate | QA | Antes do go-live |

---

### US-07 - Critérios de release e aceitação de risco

Cada release é também uma decisão de risco.  
Formalizar critérios e aceitar explicitamente o risco residual é parte da governação.  

**Contexto.**  
Lançamentos sem critérios claros diluem responsabilidade.

:::userstory
**História.**   
Como **Gestão de Produto**, quero **estabelecer critérios de aceitação de segurança por release e um processo de aceitação de risco residual**, para **decisões go/no-go informadas**.

**Critérios de aceitação (BDD).**  
- **Dado** uma release pronta  
  **Quando** verifico critérios e findings  
  **Então** aprovo, atraso ou exceciono com prazo e compensações  

**Checklist.**  
- [ ] Checklist preenchida  
- [ ] Findings críticos: 0 ou exceção formal  
- [ ] Justificação de risco registada  

:::

**Artefactos & evidências.** Checklist de release + registo de exceções.  

**Proporcionalidade por risco.**  
| Nível | Política |
|---|---|
| L1 | Checklist simples |
| L2 | Bloqueio High/Critical |
| L3 | Nenhum crítico sem exceção formal |

**Integração no SDLC.**  
| Fase | Trigger | Responsável | SLA |
|------|---------|-------------|-----|
| Pré-release | Release candidate | Gestão + AppSec | Até D-1 do go-live |

**Template de Checklist de Release (L3):**  

```markdown
## 📋 Checklist de Release - v{VERSION}

**Release:** v2.3.0  
**Data planeada:** YYYY-MM-DD  
**Owner:** Product Manager X, AppSec Lead Y  

| Critério | Status | Evidência | Observação |
|---|---|---|---|
| **Findings Críticos** | ✅ ZERO | Screenshot dashboard | Aceite se mitigação documentada |
| **SAST Thresholds** | ✅ OK | Build log #4521 | Bloqueio High/Critical não acionado |
| **DAST Cobertura** | ✅ 85% | Relatório DAST | Meta L3 = 80%+ |
| **Fuzzing endpoints críticos** | ✅ Completo | Log fuzzer noturno | 3 findings Low resolvidos |
| **Regressões** | ✅ PASS | CI #4521 | Nenhuma regressão detetada |
| **PenTest (se L3)** | ⚠️ Em curso | Relatório preliminar | Conclusão em +5d |
| **SCA cobertura** | ✅ 100% | SBOM + scanning | 0 CVE não mitigadas |
| **Documentação segurança** | ✅ Atualizada | Wiki link | Ameaças, controlos, mitigações |
| **Aprovação formal risco** | ⏳ Pendente | - | Aguarda AppSec + Produto |

**Risco residual aceite:**  
- [X] 1 CVE Medium em dependência com patch disponível, mas adquirido em PR separado (até 2025-12-31)  
- [X] Endpoint POST /admin/users sem DAST (acesso VPN, compensado por network policy)  

**Aprovações:**  
- AppSec Lead Y - aprovado em YYYY-MM-DD  
- Product Manager X - aprovado em YYYY-MM-DD  
```

---

### US-08 - PenTesting ofensivo baseado em risco

Automação é fundamental, mas não suficiente.  
O olhar humano ofensivo identifica cadeias de ataque que scanners nunca simulam.  

**Contexto.**  
Validação humana complementa automação.

:::userstory
**História.**   
Como **PenTester**, quero **validar ofensivamente a eficácia dos controlos**, para **detetar falhas exploráveis antes da produção**.

**Critérios de aceitação (BDD).**  
- **Dado** âmbito baseado em risco  
  **Quando** executo PenTest  
  **Então** emito relatório com vetores, impacto e recomendações  

**Checklist.**  
- [ ] âmbito definido e consentimento  
- [ ] Relatório com PoCs e severidade  
- [ ] Retest planeado para críticos  

:::

**Artefactos & evidências.** Relatório técnico PenTest + evidências.  

**Proporcionalidade por risco.**  
| Nível | Exigência |
|---|---|
| L1 | Não aplicável |
| L2 | Ocasional por risco |
| L3 | Obrigatório pré-produção |

**Integração no SDLC.**  
| Fase | Trigger | Responsável | SLA |
|------|---------|-------------|-----|
| Auditoria / Pré-produção | Janela de auditoria ou L3 crítico | PenTester + AppSec | Relatório antes do go-live |

---

### US-09 - IAST com Instrumentação em Staging

DAST valida externamente, mas IAST oferece visibilidade interna de fluxos não sanitizados, chamadas inseguras e uso indevido de bibliotecas.  
Essencial para L2/L3 de criticidade elevada.  

**Contexto.**  
DAST valida externamente, mas IAST oferece visibilidade interna.

:::userstory
**História.**   
Como **QA + AppSec**, quero **instrumentar a aplicação em staging com IAST para observar chamadas inseguras em tempo real durante testes**, para **correlacionar findings com contexto de execução real e reduzir falsos positivos**.

**Critérios de aceitação (BDD).**  
- **Dado** que uma aplicação é instrumentada com agent IAST em staging  
  **Quando** testes funcionais ou automáticos são executados  
  **Então** findings são capturados com visibilidade total do stack (função, linha, parâmetro, valor)  

- **Dado** um finding de IAST observado  
- **Quando** é correlacionado com DAST/SAST  
- **Então** o resultado é priorizado como crítico/alto se confirmado em múltiplas camadas  

**Checklist.**  
- [ ] Agent IAST instalado e configurado em staging  
- [ ] Cobertura de instrumentação de endpoints críticos validada  
- [ ] Performance da aplicação monitorizada (overhead `<10%` aceito)  
- [ ] Findings de IAST exportados em formato estruturado  
- [ ] Integração com ferramenta centralizada de findings (DefectDojo ou similar)  
- [ ] Dados sensíveis mascarados nos logs de IAST  
- [ ] Retest após correção de findings críticos agendado  

:::

**Artefactos & evidências.** Configuração de agent IAST (YAML/HCL versionado), relatórios IAST (JSON/XML), logs de performance, dashboard de correlação SAST↔DAST↔IAST, métricas de cobertura.  

**Proporcionalidade por risco.**  
| Nível | Obrigatório? | Ajustes |
|---|---|---|
| L1 | Não | Opcional, investigativo |
| L2 | Recomendado | Em endpoints críticos (autenticação, pagamento) |
| L3 | Obrigatório | Cobertura total + correlação com DAST |

**Integração no SDLC.**  
| Fase | Trigger | Responsável | SLA |
|------|---------|-------------|-----|
| Staging | Deploy de candidato a release | QA + AppSec | Antes de aprovação formal |

---

### US-10 - Gestão Centralizada de Findings com Triagem e SLA

Findings dispersos em ferramentas isoladas criam redundância, ruído e falta de visibilidade.  
Centralização com triagem formal, SLA e rastreabilidade é imperativa para governação.  

**Contexto.**  
Findings dispersos criam ruído e falta de visibilidade.

:::userstory
**História.**   
Como **AppSec + DevOps**, quero **centralizar todos os findings de SAST, DAST, IAST, SCA, fuzzing e testes manuais numa plataforma unificada com triagem por criticidade, estado e SLA**, para **garantir rastreabilidade completa e priorização eficaz**.

**Critérios de aceitação (BDD).**  
- **Dado** que findings são produzidos por múltiplas ferramentas  
  **Quando** são correlacionados na plataforma centralizada  
  **Então** duplicados são consolidados e metadados unificados (CVE, CWE, CVSS, commit, módulo)  

- **Dado** um finding triado  
- **Quando** obtém estado (Aberto/Em investigação/Aceite/Corrigido/Validado)  
- **Então** SLA é associado e alertas disparados se excedido  

- **Dado** um finding corrigido  
- **Quando** validação ocorre  
- **Então** é marcado como Fechado e rastreabilidade de correção (commit, release) é registada  

**Checklist.**  
- [ ] Plataforma centralizada deployada (DefectDojo, Vulcan, Security Hub, etc.)  
- [ ] Conectores para todas as ferramentas (SAST, DAST, IAST, SCA) configurados  
- [ ] Regras de deduplica e correlação ativas  
- [ ] Critérios de triagem documentados (CWE, OWASP, risco organizacional)  
- [ ] SLA definidos por severidade e Lx (Crítico: `<24h`, Alto: `<7d`, Médio: `<30d`)  
- [ ] Dashboard públicos com KPIs (findings abertos, taxa de resolução, tempo médio)  
- [ ] Integração com backlog (Jira/Azure Boards) para atribuição automática  
- [ ] Auditoria de exceções com dupla aprovação para L2/L3  

:::

**Artefactos & evidências.** Configuração plataforma centralizada versionada, regras de deduplica, dashboard de findings, SLA documento, logs de mudança de estado, relatórios mensais KPIs.  

**Proporcionalidade por risco.**  
| Nível | Exigência | Detalhes |
|---|---|---|
| L1 | Centralização simples | Triagem manual, SLA recomendado |
| L2 | Centralização com SLA | Estados formais, alertas por exceção |
| L3 | Centralização + auditoria | SLA rigoroso, dupla aprovação, relatório mensal |

**Integração no SDLC.**  
| Fase | Trigger | Responsável | SLA |
|------|---------|-------------|-----|
| Contínua | Produção de findings | AppSec + DevOps | Em tempo real |

---

### US-11 - Feedback Automático de Findings às Equipas

Findings não comunicados eficazmente são ignorados.  
Feedback automático em canais onde os developers trabalham reduz fricção e acelera correção.  

**Contexto.**  
Findings não comunicados são ignorados.

:::userstory
**História.**   
Como **AppSec + DevOps**, quero **automatizar delivery de findings nos pontos de contacto das equipas (comentários em PR, notificações Slack, dashboards IDE)**, para **assegurar visibilidade e acelerar remediação**.

**Critérios de aceitação (BDD).**  
- **Dado** que SAST detecta uma vulnerabilidade num PR  
  **Quando** o pipeline conclui  
  **Então** comentário inline é publicado no PR com contexto (CWE, severidade, recomendação de fix)  

- **Dado** um finding crítico detetado  
- **Quando** é triado na plataforma centralizada  
- **Então** alerta é enviado a Slack/Teams para o team owner com urgência  

- **Dado** um developer a trabalhar  
- **Quando** IDE integrado com SonarQube/Semgrep está ativo  
- **Então** warnings aparecem em tempo real com sugestões de correção  

**Checklist.**  
- [ ] Integração de comentários automáticos em PRs ativa (ex: GitHub Actions, GitLab CI)  
- [ ] Webhooks configurados para envio de notificações (Slack, Teams, Email)  
- [ ] Severidade e contexto incluídos em cada notificação  
- [ ] Evitar duplicação de notificações (coalescing de alerts)  
- [ ] Dashboard público de findings por projeto/team  
- [ ] Feedback de satisfação das equipas coletado (ex: "Muito útil", "Falso positivo")  
- [ ] Ajustes de rules baseado em feedback periodicamente (mensal/trimestral)  

:::

**Artefactos & evidências.** Configuração webhooks e integrações (YAML versionado), templates de comentários em PR, dashboard comunicação, feedback logs, relatório trimestral eficácia.  

**Proporcionalidade por risco.**  
| Nível | Canais | Frequência |
|---|---|---|
| L1 | Email/relatório semanal | Agregado |
| L2 | PR comments + Slack diário | Por severidade |
| L3 | PR comments + Slack + IDE + dashboard | Real-time críticos |

**Integração no SDLC.**  
| Fase | Trigger | Responsável | SLA |
|------|---------|-------------|-----|
| Contínua | Geração/triagem de findings | AppSec + DevOps | `<15min` para críticos |

---

## 📦 Artefactos esperados

Cada teste deixa um rasto tangível.  
Estes artefactos são o que permite comprovar segurança perante auditorias ou clientes:  

| Artefacto | Evidência |
|-----------|-----------|
| Estratégia de testes | Documento versionado |
| Relatórios SAST/DAST/IAST | SARIF / HTML |
| SBOM | CycloneDX/SPDX |
| Regressões | Código + CI logs |
| Checklist de release | Documento PR final + assinaturas |
| Relatório PenTest | PDF/MD + PoCs |
| Registo de exceções | Ferramenta GRC |
| **Plataforma centralizada de findings** | **DefectDojo, Vulcan, ou similar** |
| **Webhooks e integrações de feedback** | **Configuração YAML + logs notificações** |
| **Dashboard de KPIs** | **Prometheus/Grafana + relatórios mensais** |

---

## ⚖️ Matriz de proporcionalidade L1–L3

A proporcionalidade evita tanto excesso como insuficiência.  
O objetivo é calibrar testes de acordo com a criticidade da aplicação:  

| Prática | L1 | L2 | L3 |
|---------|----|----|----|
| SAST | Aviso | Bloqueio High/Critical | Bloqueio Medium+ |
| DAST | Manual | Automático autenticado | Automático + cobertura ampliada |
| **IAST** | **N/A** | **Recomendado (críticos)** | **Obrigatório (cobertura total)** |
| Fuzzing | Opcional | Endpoints prioritários | Endpoints críticos |
| Regressões | Casos críticos | Por findings | Obrigatório |
| PenTesting | N/A | Ocasional | Pré-produção obrigatório |
| **Gestão findings** | **Backlog simples** | **Centralizado com SLA** | **Centralizado + auditoria** |
| Release | Checklist simples | Bloqueio High/Critical | Nenhum crítico sem exceção |

---

## 🏁 Recomendações finais

- **Testar cedo e sempre**: integrar SAST no PR e regressões desde o 1.º sprint.  
- **Validar runtime**: DAST autenticado e fuzzing em staging são essenciais.  
- **Ajustar ao risco**: thresholds e políticas devem seguir L1–L3.  
- **Evidência concreta**: relatórios, SBOM e logs versionados são a base da auditoria.  
- **Complementaridade**: Pentesting humano desafia e confirma a automação.  
- **Cultura contínua**: testes não são fim, mas ciclo permanente de validação.  

---
