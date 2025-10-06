---
id: aplicacao-lifecycle
title: Aplicação no Ciclo de Vida — Testes de Segurança
description: Integração prática das práticas de validação contínua nas diferentes fases do ciclo de vida da aplicação
tags: [ciclo de vida, testes, segurança, integração, validação, sdlc]
sidebar_position: 15
---

# 🧪 Aplicação de Testes de Segurança ao Longo do Ciclo de Vida {cap10:aplicacao-lifecycle}

## 🧭 Quando aplicar {cap10:aplicacao-lifecycle#quando-aplicar}

Os testes de segurança acompanham a aplicação em todas as fases — não são uma etapa final, mas um **ritmo contínuo** de validação.  
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

## 👥 Quem executa cada ação {cap10:aplicacao-lifecycle#quem-executa}

A responsabilidade pela qualidade dos testes é **coletiva**.  
Cada papel contribui com uma perspetiva única, mas só em conjunto se obtém um processo de validação robusto e auditável.  

| Papel | Responsabilidade |
|-------|------------------|
| **Dev** | Corrigir findings, criar regressões automatizadas |
| **QA/Testes** | Executar DAST, fuzzing, validar critérios |
| **AppSec** | Definir estratégia, tuning de regras, gerir findings e exceções |
| **DevOps** | Integrar scanners, gates e evidências no CI/CD |
| **Gestão de Produto** | Aprovar risco residual e decidir *go/no-go* |
| **PenTester** | Validar ofensivamente controlos e relatar impacto |

---

## 📖 User Stories Reutilizáveis {cap10:aplicacao-lifecycle#user-stories}

As histórias seguintes transformam princípios em prática.  
Cada US representa um **controlo essencial**, pensado para ser integrado diretamente no backlog da equipa e aplicado proporcionalmente ao risco da aplicação (L1–L3).  

---

### US-01 — Estratégia formal de testes por aplicação {#us-01}

A validação começa com planeamento.  
Sem uma estratégia clara, a cobertura torna-se desigual e impossível de auditar.  

**Contexto.**  
Sem estratégia, a cobertura é desigual e difícil de auditar.

**📖 Rationale científico.**  
Referências: SSDF **RV.1**, **PS.2**; OWASP SAMM **ST.1**; BSIMM **T1.3**; ISO/IEC **27005**; DSOMM (Testing).  
Mitiga: OSC&R *Missing Validation*, **CWE-693**.  
Evidência: programas BSIMM/DBIR mostram que equipas com estratégia formal detetam falhas mais cedo e com menor variabilidade.  

**História.**  
Como **AppSec**, quero **definir uma estratégia de testes de segurança por aplicação**, para **assegurar cobertura proporcional ao risco e rastreabilidade com requisitos do Cap. 02**.

**Critérios de aceitação (BDD).**  
- Dado que a aplicação tem criticidade Lx  
- Quando defino a estratégia  
- Então os tipos de teste e gates ficam estabelecidos por L1–L3 e ligados a requisitos

**Checklist (binária, auditável).**  
- [ ] Documento de estratégia versionado  
- [ ] Cobertura mínima por L1–L3 definida  
- [ ] Mapeamento Cap. 2 ⇄ testes publicado  

**Artefactos & evidências.** Documento `strategy-testing.md`, matriz requisitos⇄testes.  

**Proporcionalidade por risco.**  
| Nível | Obrigatório? | Cobertura mínima |
|---|---|---|
| L1 | Sim | SAST + checklist |
| L2 | Sim | + DAST autenticado |
| L3 | Sim | + fuzzing/IAST + PenTest |

**Integração no SDLC.**  
| Fase | Gatilho | Responsável | SLA |
|------|---------|-------------|-----|
| Planeamento | Classificação Lx / kick-off | AppSec | Até ao fim do 1.º sprint |

---

### US-02 — SAST obrigatório em Pull Request {#us-02}

Detetar cedo é sempre mais barato.  
Executar SAST no momento do PR garante que vulnerabilidades nunca chegam à *branch* principal.  

**Contexto.**  
PRs sem SAST permitem que vulnerabilidades entrem cedo no código base.

**📖 Rationale científico.**  
Referências: SSDF **PW.6**, **RV.3**; SAMM **SM.2**; BSIMM **T2.4**; OWASP Top 10.  
Mitiga: **CWE-20**, **CWE-79**, **CWE-89**, OSC&R *Source Code Weaknesses*.  
Evidência: NIST/SEI mostram que correções em PR custam ordens de magnitude menos que em produção.  

**História.**  
Como **Dev**, quero **executar SAST automático no PR com comentários inline**, para **corrigir vulnerabilidades antes do merge**.

**Critérios de aceitação (BDD).**  
- Dado que abro um PR  
- Quando o pipeline corre SAST  
- Então resultados aparecem inline e bloqueiam acima do threshold definido  

**Checklist (binária, auditável).**  
- [ ] Trigger em PR ativo  
- [ ] Relatório SARIF anexado  
- [ ] Threshold por Lx aplicado  

**Artefactos & evidências.** Logs CI + SARIF.  

**Proporcionalidade por risco.**  
| Nível | Política de gate |
|---|---|
| L1 | Aviso |
| L2 | Bloqueio High/Critical |
| L3 | Bloqueio Medium+ |

**Integração no SDLC.**  
| Fase | Gatilho | Responsável | SLA |
|------|---------|-------------|-----|
| Revisão de código | Abertura de PR | Dev + DevOps | Antes do merge |

---

### US-03 — DAST autenticado em Staging {#us-03}

Muitas falhas críticas só se revelam após login.  
Executar DAST autenticado em staging é o passo natural antes de promover uma release.  

**Contexto.**  
Muitas falhas surgem apenas autenticadas.

**📖 Rationale científico.**  
Referências: SSDF **RV.3**; SAMM **ST.2**; BSIMM **T1.3**.  
Mitiga: **CWE-285**, **CWE-306/307**, CAPEC-115; OSC&R *Broken Access Controls*.  
Evidência: dados de bug bounties e DBIR confirmam que vulnerabilidades críticas são maioritariamente exploráveis apenas autenticadas.  

**História.**  
Como **QA**, quero **executar DAST autenticado em staging**, para **detetar vulnerabilidades exploráveis em runtime**.

**Critérios de aceitação (BDD).**  
- Dado ambiente staging configurado  
- Quando executo DAST autenticado  
- Então relatórios são gerados e findings abertos no backlog  

**Checklist (binária, auditável).**  
- [ ] Login flow configurado  
- [ ] Scope definido  
- [ ] Relatório anexado à release  

**Artefactos & evidências.** Relatórios DAST.  

**Proporcionalidade por risco.**  
| Nível | Cobertura |
|---|---|
| L1 | Manual/exploratório |
| L2 | Automático autenticado |
| L3 | Automático + cobertura ampliada |

**Integração no SDLC.**  
| Fase | Gatilho | Responsável | SLA |
|------|---------|-------------|-----|
| Staging | Build/Deploy em staging | QA | Antes da aprovação da release |

---

### US-04 — Gates de segurança no CI/CD {#us-04}

Sem gates, findings tornam-se meros relatórios ignorados.  
Gates automáticos são a barreira que impede regressões graves de avançar.  

**Contexto.**  
Sem gates, findings não impedem regressões.

**📖 Rationale científico.**  
Referências: SSDF **PS.2**, **PW.7**; SLSA **L2+**; SAMM **SM.2**.  
Mitiga: OSC&R *CI/CD Compromise*, **CWE-693**.  
Evidência: relatórios BSIMM mostram que *release gates* reduzem em >50% a ocorrência de críticos em produção.  

**História.**  
Como **DevOps**, quero **integrar gates automáticos no pipeline (SAST/SCA/IAST) com thresholds por Lx**, para **evitar builds inseguros**.

**Critérios de aceitação (BDD).**  
- Dado um pipeline em execução  
- Quando um finding excede o threshold Lx  
- Então o job falha e a promoção é bloqueada até correção ou exceção aprovada  

**Checklist (binária, auditável).**  
- [ ] Pipelines versionados com gates declarados  
- [ ] Thresholds por Lx publicados  
- [ ] Logs exportados  
- [ ] Exceções aprovadas (L3: dupla aprovação)  

**Artefactos & evidências.** Configuração `ci.yml`, relatórios e registo de exceções.  

**Proporcionalidade por risco.**  
| Nível | Política |
|---|---|
| L1 | Aviso |
| L2 | Bloqueio High/Critical |
| L3 | Bloqueio Medium+ |

**Integração no SDLC.**  
| Fase | Gatilho | Responsável | SLA |
|------|---------|-------------|-----|
| CI/CD | Execução pipeline | DevOps + AppSec | Em cada build |

---

### US-05 — Regressões de segurança automatizadas {#us-05}

Corrigir não chega — é preciso garantir que a mesma falha não regressa.  
Testes de regressão automatizados transformam cada correção numa proteção futura.  

**Contexto.**  
Falhas corrigidas voltam sem regressão automatizada.

**📖 Rationale científico.**  
Referências: SSDF **RV.6**; SAMM **ST.2**.  
Mitiga: **CWE-459**, **CWE-388**.  
Evidência: regressões ligadas a findings reduzem reaberturas e aceleram remediação.  

**História.**  
Como **Dev**, quero **criar testes de regressão para findings corrigidos**, para **evitar reintrodução futura**.

**Critérios de aceitação (BDD).**  
- Dado um finding resolvido  
- Quando crio o teste de regressão  
- Então ele falha se a vulnerabilidade regressar  

**Checklist (binária, auditável).**  
- [ ] Teste criado e versionado  
- [ ] Ligação ao finding original (ID)  
- [ ] Execução em builds futuros  

**Artefactos & evidências.** Código de regressão + logs CI.  

**Proporcionalidade por risco.**  
| Nível | Exigência |
|---|---|
| L1 | Casos críticos |
| L2 | Por falha conhecida |
| L3 | Cobertura obrigatória |

**Integração no SDLC.**  
| Fase | Gatilho | Responsável | SLA |
|------|---------|-------------|-----|
| Dev/CI | Fecho de finding | Dev | No PR de correção |

---

### US-06 — Fuzzing dirigido a APIs críticas {#us-06}

Testes convencionais não capturam todas as falhas.  
O fuzzing, ao explorar entradas inesperadas, revela vulnerabilidades invisíveis a olho nu.  

**Contexto.**  
Entradas complexas revelam falhas não cobertas.

**📖 Rationale científico.**  
Referências: SSDF **RV.4**; BSIMM **T2.5**; literatura DARPA sobre fuzzing.  
Mitiga: **CWE-119**, **CWE-20**, **CWE-400**, CAPEC-28/125.  
Evidência: fuzzing sistemático aumenta a taxa de descoberta de falhas desconhecidas.  

**História.**  
Como **QA**, quero **aplicar fuzzing a endpoints críticos**, para **detectar falhas invisíveis em testes convencionais**.

**Critérios de aceitação (BDD).**  
- Dado endpoints críticos definidos  
- Quando executo fuzzing  
- Então anomalias são registadas com PoC mínima  

**Checklist (binária, auditável).**  
- [ ] Targets e perfis definidos  
- [ ] Ambiente isolado de teste  
- [ ] Relatório com casos reproduzíveis  

**Artefactos & evidências.** Relatório de fuzzing + corpora.  

**Proporcionalidade por risco.**  
| Nível | Cobertura |
|---|---|
| L1 | Opcional |
| L2 | Endpoints prioritários |
| L3 | Endpoints críticos obrigatórios |

**Integração no SDLC.**  
| Fase | Gatilho | Responsável | SLA |
|------|---------|-------------|-----|
| Staging | Release candidate | QA | Antes do go-live |

---

### US-07 — Critérios de release e aceitação de risco {#us-07}

Cada release é também uma decisão de risco.  
Formalizar critérios e aceitar explicitamente o risco residual é parte da governação.  

**Contexto.**  
Lançamentos sem critérios claros diluem responsabilidade.

**📖 Rationale científico.**  
Referências: SSDF **PS.2**, **GV.2–3**; SAMM **GO.3**; ISO/IEC **27005**; SLSA.  
Mitiga: **CWE-668**, risco residual não governado.  
Evidência: releases com critérios claros reduzem incidentes pós-go-live.  

**História.**  
Como **Gestão de Produto**, quero **estabelecer critérios de aceitação de segurança por release e um processo de aceitação de risco residual**, para **decisões go/no-go informadas**.

**Critérios de aceitação (BDD).**  
- Dado uma release pronta  
- Quando verifico critérios e findings  
- Então aprovo, atraso ou exceciono com prazo e compensações  

**Checklist (binária, auditável).**  
- [ ] Checklist preenchida  
- [ ] Findings críticos: 0 ou exceção formal  
- [ ] Justificação de risco registada  

**Artefactos & evidências.** Checklist de release + registo de exceções.  

**Proporcionalidade por risco.**  
| Nível | Política |
|---|---|
| L1 | Checklist simples |
| L2 | Bloqueio High/Critical |
| L3 | Nenhum crítico sem exceção formal |

**Integração no SDLC.**  
| Fase | Gatilho | Responsável | SLA |
|------|---------|-------------|-----|
| Pré-release | Release candidate | Gestão + AppSec | Até D-1 do go-live |

---

### US-08 — PenTesting ofensivo baseado em risco {#us-08}

Automação é fundamental, mas não suficiente.  
O olhar humano ofensivo identifica cadeias de ataque que scanners nunca simulam.  

**Contexto.**  
Validação humana complementa automação.

**📖 Rationale científico.**  
Referências: BSIMM **PT1.1**; SAMM **ST.3**; OWASP Testing Guide; ISO/IEC **27001**.  
Mitiga: vetores avançados fora do escopo de scanners (chaining), **CWE-352**, CAPEC-35/152/170.  
Evidência: em L3, Pentests mantêm maior *hit rate* de vulnerabilidades críticas.  

**História.**  
Como **PenTester**, quero **validar ofensivamente a eficácia dos controlos**, para **detetar falhas exploráveis antes da produção**.

**Critérios de aceitação (BDD).**  
- Dado escopo baseado em risco  
- Quando executo PenTest  
- Então emito relatório com vetores, impacto e recomendações  

**Checklist (binária, auditável).**  
- [ ] Escopo definido e consentimento  
- [ ] Relatório com PoCs e severidade  
- [ ] Retest planeado para críticos  

**Artefactos & evidências.** Relatório técnico PenTest + evidências.  

**Proporcionalidade por risco.**  
| Nível | Exigência |
|---|---|
| L1 | Não aplicável |
| L2 | Ocasional por risco |
| L3 | Obrigatório pré-produção |

**Integração no SDLC.**  
| Fase | Gatilho | Responsável | SLA |
|------|---------|-------------|-----|
| Auditoria / Pré-produção | Janela de auditoria ou L3 crítico | PenTester + AppSec | Relatório antes do go-live |

---

## 📦 Artefactos esperados {cap10:aplicacao-lifecycle#artefactos}

Cada teste deixa um rasto tangível.  
Estes artefactos são o que permite comprovar segurança perante auditorias ou clientes:  

| Artefacto | Evidência |
|-----------|-----------|
| Estratégia de testes | Documento versionado |
| Relatórios SAST/DAST/IAST | SARIF / HTML |
| SBOM | CycloneDX/SPDX |
| Regressões | Código + CI logs |
| Checklist de release | Documento PR final |
| Relatório PenTest | PDF/MD + PoCs |
| Registo de exceções | Ferramenta GRC |

---

## ⚖️ Matriz de proporcionalidade L1–L3 {cap10:aplicacao-lifecycle#proporcionalidade}

A proporcionalidade evita tanto excesso como insuficiência.  
O objetivo é calibrar testes de acordo com a criticidade da aplicação:  

| Prática | L1 | L2 | L3 |
|---------|----|----|----|
| SAST | Aviso | Bloqueio High/Critical | Bloqueio Medium+ |
| DAST | Manual | Automático autenticado | Automático + cobertura ampliada |
| IAST | N/A | Opcional | Recomendado |
| Fuzzing | Opcional | Endpoints prioritários | Endpoints críticos |
| Regressões | Casos críticos | Por findings | Obrigatório |
| PenTesting | N/A | Ocasional | Pré-produção obrigatório |
| Release | Checklist | Bloqueio High/Critical | Nenhum crítico sem exceção |
| Gestão de findings | Backlog simples | Estruturado | Ferramenta dedicada |

---

## 🏁 Recomendações finais {cap10:aplicacao-lifecycle#recomendacoes}

- **Testar cedo e sempre**: integrar SAST no PR e regressões desde o 1.º sprint.  
- **Validar runtime**: DAST autenticado e fuzzing em staging são essenciais.  
- **Ajustar ao risco**: thresholds e políticas devem seguir L1–L3.  
- **Evidência concreta**: relatórios, SBOM e logs versionados são a base da auditoria.  
- **Complementaridade**: Pentesting humano desafia e confirma a automação.  
- **Cultura contínua**: testes não são fim, mas ciclo permanente de validação.  

---
