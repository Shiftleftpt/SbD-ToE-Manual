# Addon 11: Framework de Decisão para Deployment — Separação Sugestão/Decisão

## Objetivo

Estabelecer um framework explícito para separar a **sugestão automática** (gates de validação, testes, análise) da **decisão humana** (aprovar go-live, defer, ou canary) no processo de deployment. Este addon implementa o invariante I1 (Separação sugestão/decisão) no contexto operacional de deployment, garantindo que decisões críticas sobre liberação de código em produção sejam sempre tomadas por pessoas qualificadas com informação completa e estruturada.

## Problema

Muitos deployment pipelines modernos funcionam como "tudo passa, deploya; algo falha, bloqueia". Este modelo automatizado carece de um **ponto de decisão estruturado** onde riscos são analisados, trade-offs avaliados, e decisores qualificados aprovam o go-live com plena consciência dos riscos residuais.

### Cenários de Risco

**Cenário 1 — Decisão implícita:**
- Todos os testes passam, SAST sem criticals, DAST validou, staging aprovou
- Gate automático libera para produção
- 4 horas depois: Métrica de erro sobe 10x, rollback executado
- **Problema:** Ninguém perguntou "temos confiança em deploya?" ou "monitorização está pronta?"

**Cenário 2 — Conflito timeline vs. security:**
- Staging encontra 1 HIGH na dependência X
- Security diz: "Defer até patchear"
- Product diz: "Clientes precisam disso hoje, risco aceitável"
- **Problema:** Sem matriz clara de decisores e critérios, discussão é ad-hoc e política

**Cenário 3 — Decisão isolada:**
- Encontrado 1 MEDIUM finding em teste de segurança
- Gate bloqueia automaticamente
- Ninguém verifica se: rollback está testado, monitorização ativa, business impact foi avaliado
- **Problema:** Bloqueio automático sem contexto; deve ser decidido, não apenas bloqueado

## Solução: Framework de Decisão Estruturado

### Fase 1: Readiness Validation (Automática, Gate)

Requisitos pré-requisitos verificados automaticamente. Se algum falha, go-live não é considerado:

| Requisito | Evidência | Passagem Automática |
|---|---|---|
| Todos os testes passados | Test run report | Sim (0 failures) |
| SAST sem CRITICAL | SAST report | Sim (max HIGH) |
| DAST passou em staging | DAST report | Sim (0 bloqueadores) |
| Artefato assinado (SLSA L2+) | Artifact provenance | Sim |
| Staging validado | Staging sign-off | Sim (tester ou QA) |
| Rollback testado | Rollback procedure + test results | Sim |
| Feature flags prontos (se aplicável) | Feature flag config | Sim (tested in canary) |

**Saída:** Se tudo passa → Procede para Fase 2. Se algum falha → Automaticamente bloqueado, não avança.

### Fase 2: Analysis (Structured Checklist C1)

Quando tudo passa em Readiness, segue-se análise estruturada via **Checklist C1**.

#### Checklist C1: 4 Perguntas Críticas

```markdown
## Checklist C1 — Análise de Risco para Deploy

[Data] [Versão] [Responsável]

### Pergunta 1: Todas as validações técnicas passaram e foram revistas?

Evidência esperada:
- [ ] Test report com 100% coverage e 0 failures
- [ ] SAST report revisado: máximo HIGH findings (sem CRITICAL)
- [ ] DAST staging report revisado: 0 bloqueadores
- [ ] Staging approval assinado por QA/tester
- [ ] Dependency check (SCA/SBOM) validado
- [ ] Feature flags testados em staging (se aplicável)

**Avaliação:** SIM / NÃO / COM RISCO

**Se NÃO ou COM RISCO, detalhar:**
- Qual validação não passou?
- Por que está sendo considerado risco aceitável?
- Qual é o plano de mitigação pós-deploy?

---

### Pergunta 2: Rollback está testado, pronto e documentado?

Evidência esperada:
- [ ] Rollback procedure escrito e versioned no repo
- [ ] Rollback foi executado com sucesso em staging (tempo de execução < ___ min)
- [ ] Dados podem ser recuperados (backup testado, migration reversível)
- [ ] Feature flags permitem desativar funcionalidade (se aplicável)
- [ ] Escalation path definido (quem chama rollback em produção)

**Avaliação:** SIM / NÃO / COM RISCO

**Se NÃO ou COM RISCO, detalhar:**
- O que não está pronto no rollback?
- Qual é o risco de execução em produção?
- Qual é o plano de mitigação?

---

### Pergunta 3: O impacto de negócio foi avaliado e é aceitável?

Evidência esperada:
- [ ] Afetados (internos/clientes) foram notificados
- [ ] Maintenance window é aceitável (ou zero-downtime confirmado)
- [ ] Capacidade foi planejada (load testing feito, escalada automática)
- [ ] SLA continuará sendo atendido (simulação ou análise)
- [ ] Comunicação pós-deploy está pronta (status page, customer notification)

**Avaliação:** SIM / NÃO / COM RISCO

**Se NÃO ou COM RISCO, detalhar:**
- Qual é o impacto não mitigado?
- Qual é o custo/risco aceitável?
- Há contingency plan comunicado?

---

### Pergunta 4: Monitorização, alertas e reação estão ativos e prontos?

Evidência esperada:
- [ ] Dashboards criados e validados (métricas-chave visíveis)
- [ ] Alertas configurados (latência, erro rate, business metrics)
- [ ] On-call schedule confirmado (quem responde em 15 min?)
- [ ] Runbook de resposta escrito (o que fazer se métrica X sobe?)
- [ ] Comunicação de incidente planejada (escalation, customer notification)

**Avaliação:** SIM / NÃO / COM RISCO

**Se NÃO ou COM RISCO, detalhar:**
- Qual métrica ou alerta não está pronto?
- Qual é o risco de detecção tardia?
- Qual é o plano de ativação?

---

### Síntese de Risco

| Pergunta | Status | Severidade de Risco |
|---|---|---|
| Validações técnicas | SIM / NÃO / RISCO | CRÍTICA / ALTA / MÉDIA |
| Rollback pronto | SIM / NÃO / RISCO | CRÍTICA / ALTA / MÉDIA |
| Impacto negócio | SIM / NÃO / RISCO | CRÍTICA / ALTA / MÉDIA |
| Monitorização | SIM / NÃO / RISCO | CRÍTICA / ALTA / MÉDIA |

**Perfil de Risco Geral:**
- [ ] Verde (todos SIM) → Procede para Decisão
- [ ] Amarelo (alguns NÃO, mitigações claras) → Procede com Canary
- [ ] Vermelho (risco crítico não mitigado) → DEFER até resolver
```

**Saída de C1:** Perfil de risco geral (Verde/Amarelo/Vermelho) + lista de mitigações residuais.

### Fase 3: Decision (Template T1)

Com C1 preenchido, decisor qualificado toma uma de 4 decisões:

#### Template T1: Decisão de Deploy

```markdown
## Template T1 — Decisão de Deploy

[Data] [Versão] [Decisor] [Cargo/Nível]

### Informação de Entrada

- **Status C1:** Verde / Amarelo / Vermelho
- **Risco Geral:** [CRÍTICA / ALTA / MÉDIA / BAIXA]
- **Mitigações Residuais:** [lista de C1]

### Opções de Decisão

#### Opção 1: APPROVE-NOW-PROD
- **Significado:** Deploy direto para produção
- **Quando usar:** C1=Verde, todos os riscos documentados, confiança alta
- **Tempo SLA:** Go-live em < 30 min
- **Exemplos:** Bugfix crítico com todos os testes, feature com staging completo

#### Opção 2: APPROVE-CANARY-FIRST
- **Significado:** Deploy para canary (1-5% traffic), monitorar por 2-4h antes de GA
- **Quando usar:** C1=Amarelo, alguns riscos documentados, mitigações residuais monitoráveis
- **Tempo SLA:** Canary em < 30 min, decisão GA em 4h (pode estender se anomalia)
- **Exemplos:** Dependência patchada com HIGH finding, nova feature com staging limitado

#### Opção 3: DEFER-NEXT-RELEASE
- **Significado:** Não deploya hoje, agendado para próximo release window
- **Quando usar:** C1=Amarelo/Vermelho, risco significativo, próximo window em <72h
- **Tempo SLA:** Comunicado em < 1h, pré-requisitos claros para próximo window
- **Exemplos:** Impacto de negócio não avaliado, rollback não testado suficientemente

#### Opção 4: BLOCK-UNTIL-FIXED
- **Significado:** Deploy está bloqueado até resolver pré-requisitos
- **Quando usar:** C1=Vermelho, risco crítico não mitigável
- **Tempo SLA:** Pré-requisitos claros comunicados em < 1h, timeline de resolução estimada
- **Exemplos:** CRITICAL finding não mitigado, rollback impossível, monitorização indisponível

### Decisão Tomada

**Opção selecionada:** [ ] 1 / [ ] 2 / [ ] 3 / [ ] 4

**Justificativa (máx 5 linhas):**
[Decisor descreve por que essa opção é apropriada dado o perfil de risco C1]

**Mitigações/Contingências (se aplicável):**
- [Monitorar métrica X, ativar escalação se Y acontecer]
- [Comunicado para stakeholder Z]
- [Rollback trigger definido como: Z]

**Assinado por:** [Nome] [Data] [Timestamp]
```

**Saída de T1:** Decisão clara (1-4), justificativa, contingências documentadas.

### Fase 4: Escalation (Template T2 — Quando Há Conflito)

Se há discordância entre risco técnico e pressão de negócio, ou entre decisores:

#### Template T2: Escalation Workflow

```markdown
## Template T2 — Escalation de Conflito

[Data] [Versão] [Iniciador] [Cargo]

### Conflito Identificado

**Tipo:** [ ] Timeline vs. Security / [ ] Cost vs. Availability / [ ] FP Dispute / [ ] Rollback Readiness

**Descrição:**
[Quem discorda, sobre o quê, por quê]

### Participantes

| Papel | Nome | Posição | Presente? |
|---|---|---|---|
| Líder Técnico | [TBD] | Time dev/ops | Sim / Não |
| Líder Segurança | [TBD] | Security/AppSec | Sim / Não |
| Líder Produto | [TBD] | Product/Business | Sim / Não |
| CTO / Escalation | [TBD] | Executive | Sim / Não |

### Argumentos Apresentados

**Posição A (ex: "Deploye hoje"):**
- Argumento 1: [...]
- Argumento 2: [...]
- Proposta de mitigação: [...]

**Posição B (ex: "Defer até patchear"):**
- Argumento 1: [...]
- Argumento 2: [...]
- Proposta de mitigação: [...]

### Resolução

**Decisão escalada:** [Após discussão, decisão final tomada por autoridade]
- Opção eleita: [ ] 1 / [ ] 2 / [ ] 3 / [ ] 4
- Rationale: [Por que essa opção resolve o conflito]
- Ação imediata: [O que muda, quem faz, até quando]

**Assinado por:** [Escalation Authority] [Data] [Timestamp]
```

**Saída de T2:** Conflito documentado, posições claras, resolução autorizada, ação definida.

---

## Matriz de Decisores por Classificação e Severidade

Quem pode tomar qual decisão em função de L1/L2/L3 e severidade de findings:

| Classificação | Sem Findings | LOW | MEDIUM | HIGH | CRITICAL |
|---|---|---|---|---|---|
| **L1 (Manual)** | Dev / QA | Dev / QA | L2 Lead | AppSec Lead | CTO + AppSec |
| **L2 (Auto + gates)** | Dev / L2 Lead | L2 Lead | AppSec Lead | AppSec Lead + Líder Técnico | CTO + AppSec |
| **L3 (Auto + tested)** | L2 Lead | L2 Lead | L2 Lead + AppSec | AppSec Lead | CTO + AppSec |

**Legenda:**
- **L1 (Manual):** Feature novo ou large refactor, validações manuais, baixa confiança
- **L2 (Auto + gates):** Feature médio, testes automatizados, validações em staging, confiança média
- **L3 (Auto + tested):** Bugfix, release management, testes extensivos, alta confiança

**Regras de Escalonamento:**
- Nenhum decisor abaixo do nível de classificação pode aprovar
- Se conflito surge (ex: Líder Técnico diz "deploy", AppSec diz "defer"), escalaciona para CTO
- CTO é autoridade final e pode aprovar ou rejeitar qualquer decisão

---

## Proporcionalidade L1/L2/L3

### L1 — Manual, Low Automation
- **C1 (Checklist):** Todas as 4 perguntas devem ter resposta SIM
- **T1 (Decisão):** Apenas opção 1 (APPROVE-NOW-PROD) ou 4 (BLOCK)
- **Opção 2/3 (Canary/Defer):** Requer escalation via T2
- **Frequência de Decisão:** Manual por deploy, potencialmente lenta
- **Exemplo:** Deploy de L1 app (criticalidade baixa): Dev + QA checam C1, Líder Técnico aprova via T1

### L2 — Automated + Gated
- **C1 (Checklist):** 3 de 4 perguntas podem ser "COM RISCO" se mitigações estão documentadas
- **T1 (Decisão):** Todas as 4 opções disponíveis
- **Opção 2 (CANARY):** Preferida para C1=Amarelo, permite teste em produção com baixo risco
- **Frequência de Decisão:** Semi-automatizada, acelerada com decisão em 4h
- **Exemplo:** Deploy de L2 app (criticalidade média, feature médio): Staging passa, C1=Amarelo (rollback COM RISCO mas documentado), L2 Lead aprova Opção 2 (CANARY-FIRST), canary monitora 4h, depois GA

### L3 — Automated + Tested
- **C1 (Checklist):** Pode ter 1-2 perguntas com "COM RISCO" se impacto é previsível e monitorável
- **T1 (Decisão):** Opção 1 (APPROVE-NOW-PROD) preferida, Opção 2 (CANARY) se building confidence
- **Frequência de Decisão:** Altamente automatizada, decisão em <1h
- **Exemplo:** Deploy de L3 app (criticalidade alta, bugfix crítico): Todos os testes passam, C1=Verde, L2 Lead + AppSec reviram em 30 min, T1 aprovam APPROVE-NOW-PROD, deploy em produção em <1h

---

## SLA — Tempo de Decisão

| Severidade Máxima | SLA de Decisão | Rationale |
|---|---|---|
| CRÍTICA (sem mitigação) | 4 horas | Urgência alta, mas permite escalation + análise |
| ALTA | 24 horas | Impacto significativo, permite investigação |
| MÉDIA | 48 horas | Risco baixo-médio, permite planning |
| BAIXA | 72 horas | Risco mínimo, permite agendamento |

**Medição:**
- Começa quando C1 é preenchido
- Termina quando T1 (ou T2) é assinado
- Escalações não reiniciam relógio, apenas documentam necessidade de autoridade superior

---

## KPIs de Execução

Métrica | Meta | Propósito
---|---|---
% de deploys com C1 documentado | > 95% | Consistência de processo |
Tempo médio C1 até T1 (horas) | < 4 (L1), < 2 (L2), < 1 (L3) | Velocidade de decisão por classificação |
% de deploys aprovados em CANARY (Opção 2) | 20-40% | Balanço entre velocidade e confiança |
% de deploys com escalation (T2) | < 10% | Raro, indica processos claros |
SLA compliance (decisão antes do prazo) | > 95% | Responsabilidade de decisores |
Mean time to go-live (após T1 aprovado) | < 30 min (L1), < 15 min (L2/L3) | Eficiência operacional |

---

## Implementação Prática: Exemplo Completo

### Cenário: Deploy de L2 App com 1 HIGH Finding em Staging

**Versão:** 2.4.1  
**Classificação:** L2 (feature médio, testes automatizados, confiança média)  
**Contexto:** Staging encontrou 1 HIGH em dependência X, vendedor iniciou patch, patch foi validado em staging com testes

---

#### Fase 1: Readiness Validation (Gate Automática)

| Requisito | Status |
|---|---|
| Testes (0 failures) | ✅ Passou (2,340 tests) |
| SAST (max HIGH) | ✅ Passou (0 CRITICAL, 1 HIGH em dep X, será patchado em 2.4.2) |
| DAST staging | ✅ Passou (0 bloqueadores, HIGH já patchado) |
| Artefato assinado | ✅ Passou (SLSA L2) |
| Staging validado | ✅ Passou (QA aprovou) |
| Rollback testado | ✅ Passou (DB rollback, <2 min) |
| Feature flags | ✅ Passou (flag testado em staging) |

**Resultado:** Gate passa → Procede para C1

---

#### Fase 2: Analysis (Checklist C1)

```
Data: 15 Jan 2026
Versão: 2.4.1
Responsável: Alice (L2 Lead)

Pergunta 1: Todas as validações técnicas passaram?
Status: SIM (com detalhe)
- Testes: 2,340 com 0 failures
- SAST: HIGH em dep X, mas patch foi validado em DAST staging sem nova vulnerabilidade
- Staging: QA aprovou, metrics nominais
Avaliação: SIM (validações técnicas passaram, HIGH é conhecido e mitigado via patch)

Pergunta 2: Rollback está pronto?
Status: SIM
- Rollback procedure: Revert schema, revert app, ~2 min total
- Testado: Success em staging, 100% recovery
- Escalation: Bob (on-call eng) autorizado a executar
Avaliação: SIM

Pergunta 3: Impacto de negócio é aceitável?
Status: SIM (com comunicação)
- No maintenance window (blue-green)
- Load testing: New feature pode lidar com 2x current load (simulated)
- Comunicação: Changelog pronto, notificação agendada 1h antes
Avaliação: SIM

Pergunta 4: Monitorização está pronta?
Status: NÃO / COM RISCO — Mitigação Documentada
- Dashboards: Ready (latency, error rate, feature usage)
- Alertas: Configured (erro rate > 2%, latency > 500ms)
- On-call: Bob + Charlie (2 pessoas, 24h coverage)
- PROBLEMA: Feature-flag kill-switch não está monitorado, só manual
- MITIGAÇÃO: Feature-flag será desativado manualmente em <5 min se anomalia (testado, Bob sabe procedure)
Avaliação: COM RISCO (kill-switch é manual, mas <5 min response, documentado)

SÍNTESE:
Pergunta 1: SIM (técnico OK)
Pergunta 2: SIM (rollback OK)
Pergunta 3: SIM (negócio OK)
Pergunta 4: COM RISCO (monitoring ok, kill-switch manual mas rápido)

PERFIL: Amarelo (alguns riscos residuais monitoráveis)
RECOMENDAÇÃO: Canary-first (opção 2) para testar em produção com 1% traffic antes de GA
```

**Saída C1:** Amarelo (riscos documentados e mitigáveis)

---

#### Fase 3: Decision (Template T1)

```
Data: 15 Jan 2026, 10:30 AM
Versão: 2.4.1
Decisor: Alice (L2 Lead), Time Técnico

Entrada C1:
- Status: Amarelo
- Risco geral: MÉDIA
- Mitigações: Feature-flag kill-switch manual, <5 min response

DECISÃO SELECIONADA: Opção 2 — APPROVE-CANARY-FIRST

JUSTIFICATIVA:
C1 é Amarelo com mitigações documentadas e testadas. HIGH finding é conhecido,
patch foi validado em staging, rollback é rápido. Recomendamos canary 1% traffic
por 2-4h para testar em produção real antes de full rollout (GA). Assim, confiança
na feature-flag kill-switch (manual) é validada em produção com baixo risco.

MITIGAÇÕES PARA CANARY:
- Monitorar erro rate, latência, feature usage em canary 1%
- Se erro rate > 2% por >5 min, ativar feature-flag kill-switch (manual)
- Bob (on-call) monitorará dashboards, será notificado por alerta
- Escalation: Alice (L2 Lead) será notificada se kill-switch é usado

CANARY SLA: Deploy em canary < 30 min (10:30-11:00)
GA SLA: Decisão GA em <4h (antes 14:30) — Alice revisará métricas de canary

Assinado: Alice [signature] 15 Jan 2026 10:30 AM
```

**Saída T1:** Opção 2 (CANARY-FIRST), mitigações claras, SLA definido

---

#### Fase 4 (Opcional): Escalation

Se houvesse conflito (ex: Líder Produto diz "GA agora", AppSec diz "defer"), seria documentado em T2 e CTO resolveria. Neste exemplo, sem conflito.

---

#### Resultado Final

- **10:30 AM:** Alice (L2 Lead) aprovam Opção 2 via T1
- **11:00 AM:** Deploy para canary 1% iniciado (feature-flag enabled para 1% usuários)
- **11:00-15:00:** Bob monitora canary: erro rate 0.8% (ok), latência +5% (ok), uso 2,340 requisições sem erro crítico
- **14:30:** Alice revisa métricas, confiança alta em GA
- **14:45:** GA iniciado (feature-flag ampliado para 100%)
- **16:00:** Post-deploy validation: All healthy, monitorização nominais, feature usage growing
- **Sucesso:** Deploy completo, learning: "Feature-flag kill-switch pode ficar automático em 2.4.2"

---

## Checklist de Implementação

- [ ] **Definir Decisores Matriz:** Quem aprova o quê em cada L1/L2/L3 × severidade
- [ ] **Treinar Decisores:** Como preencher C1, como tomar T1, quando usar T2
- [ ] **Integrar C1 no Processo:** Quem preenche, quando, ferramentas (Jira? Spreadsheet? Pipeline UI?)
- [ ] **Integrar T1 no Processo:** Aprovação é via comentário? Via formulário? Via CLI?
- [ ] **Monitorar KPIs:** Registrar tempo C1→T1, % canary, % escalations, SLA compliance
- [ ] **Revisar Periodicamente:** Trimestralmente, validar se decisões estão melhorando confiança

---

## Referências

- **NIST SSDF PO.3:** Implementa segregação entre validação automática e decisão humana
- **OWASP SAMM** (PO—Process Outputs): Governance de deployment decisions
- **Kubernetes Admission Control:** Inspiração para gates pré-decisão

