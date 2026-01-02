# 🏛️ Decisão Estruturada em Aprovação de Exceções de Risco

> **Invariante I1 (agent.md):** Separação sugestão/decisão → Ferramenta sugere exceção, humano decide com checklist + templates + escalation

---

## 📋 Objetivo

Implementar um **framework decisório estruturado** para aprovação de exceções de risco (quando aplicação não pode cumprir requisito de segurança), garantindo que:
1. **Sugestões de exceção** (por Dev/AppSec, quando requisito não é viável) sejam validadas antes de aprovação
2. **Decisões** sejam tomadas por alçada apropriada (AppSec, CISO, Gestão) com checklist formal
3. **Compensações** propostas sejam adequadas ao nível de risco (L1/L2/L3)
4. **Conflitos de decisão** (técnico vs. negócio) sejam escalados com critérios claros
5. **Rastreabilidade completa** da sugestão → avaliação → decisão → revalidação

---

## 🚨 Problema: Risco & Cenários

**Cenário 1 — Exceção sem avaliação consciente:**
- Dev registra: "App não consegue retenção de logs 90 dias (requisito REQ-LOG-005), custo infraestrutura proibitivo"
- Sistema marca como "em espera de aprovação"
- **Sem estrutura:** Semanas sem decisão, app fica suspenso, negócio impactado
- **Risco:** Exceção flutua sem decisão clara ou compensações mapeadas

**Cenário 2 — Compensação inadequada ao risco:**
- L3 app (crítica, dados sensíveis) quer saltar "Criptografia em trânsito" (REQ-ENC-002)
- Compensação proposta: "Apenas acesso interno, SLA de resposta 4 horas em incidente"
- **Sem checklist:** Aprovada sem questionar (compensação é fraca para L3)
- **Risco:** Vulnerabilidade crítica aberta, risco L3 inadequadamente mitigado

**Cenário 3 — Conflito técnico/negócio não escalado:**
- AppSec nega exceção: "Sem criptografia é inaceitável, não há compensação suficiente"
- Dev/Gestão discordam: "Requisito não aplica-se, app é interna, custo é inflado"
- **Sem escalation:** Bloqueio permanente, nenhuma decisão executiva
- **Risco:** Projeto estagnado, governação não funciona

---

## 🔄 Framework: 4 Fases

```
┌─────────────────────────────────────────────────────────────┐
│ FASE 1: VALIDAÇÃO PRÉVIA (Pre-decision)                     │
│ └─ Dados de exceção completos? Compensações existem?        │
├─────────────────────────────────────────────────────────────┤
│ FASE 2: ANÁLISE D1 (Checklist de Decisão)                   │
│ └─ 4 questões críticas com risk profiling                   │
├─────────────────────────────────────────────────────────────┤
│ FASE 3: DECISÃO R1 (Decision Template)                      │
│ └─ 4 opções: APPROVE / CONDITIONAL / DEFER / DENY           │
├─────────────────────────────────────────────────────────────┤
│ FASE 4: ESCALATION E1 (Conflict Resolution)                 │
│ └─ Quando há conflito: técnico vs. negócio, custo, timing   │
└─────────────────────────────────────────────────────────────┘
```

---

## 📍 FASE 1 — Validação Prévia

**Objetivo:** Confirmar que exceção está completa antes de submeter a decisão.

**Checklist V1:**
- [ ] **Aplicação identificada:** Nome, nível de risco (L1/L2/L3), owner técnico
- [ ] **Requisito não cumprido:** Qual requisito exato? (ex: REQ-LOG-005, REQ-ENC-002)
- [ ] **Razão técnica documentada:** Impossibilidade técnica vs. custo vs. timing? (especificar)
- [ ] **Compensação(ões) proposta(s):** Quais controlos alternativos são acionados? (ex: SIEM alerts, manual audit, redução acesso)
- [ ] **Prazo de revalidação:** Quando será revisitada exceção? (data concreta)
- [ ] **Risco conhecido:** Dev/AppSec documentaram impacto de não ter este controlo?
- [ ] **Alternativas exploradas:** Escalada para Infraestrutura/Fornecedor? (confirmado que "não viável")

**Se qualquer item FALHA:**
→ Devolver exceção com feedback → Aguardar resubmissão completa

---

## 📊 FASE 2 — Análise D1 (Decisão Checklist)

**Objetivo:** Responsável (AppSec/CISO) responde 4 questões críticas sobre risco.

### Checklist D1: 4 Questões

**D1-Q1: Risco do requisito não cumprido é aceitável?**
- ✅ Qual a severidade da vulnerability sem este controlo? (Crítica/Alta/Média/Baixa)
- ✅ Quanto tempo antes de risco materializar-se? (dias/semanas/meses/nunca)
- ✅ Exploração é provável com acesso atual? (Internet-facing vs. interno)
- ✅ Impacto de violação: confidencialidade/integridade/disponibilidade? (quantificar)
- **Resultado:** ACEITÁVEL / NÃO-ACEITÁVEL / CONDICIONAL (se compensações)

**D1-Q2: Compensações são adequadas ao risco?**
- ✅ Compensação (ex: SIEM alert) realmente mitiga o risco? (testada? automatizada?)
- ✅ Compensação funciona em produção? (ex: SIEM já monitora este tipo de evento?)
- ✅ Compensação é contínua? (ou apenas pontual/manual?)
- ✅ Compensação cobre L1/L2/L3 diferente? (L3 exige compensação mais forte)
- **Resultado:** SUFICIENTE / PARCIAL / INSUFICIENTE

**D1-Q3: Prazo de revalidação é realista?**
- ✅ Plano para remover exceção? (roadmap, orçamento, timing)
- ✅ Revalidação em quanto tempo? (3 meses? 6 meses? 1 ano?)
- ✅ Quem é responsável por revalidação? (AppSec, DevOps, Dev Lead)
- ✅ Se exceção não removida: o que acontece? (nega automaticamente? escala?)
- **Resultado:** SIM (plano claro) / PARCIAL (plano vago) / NÃO (sem plano)

**D1-Q4: Proporcionalidade L1/L2/L3 é respeitada?**
- ✅ L1 (baixo risco): Exceção com compensação básica aceitável
- ✅ L2 (médio risco): Exceção exige compensação forte + revalidação 6m
- ✅ L3 (crítico): Exceção quase nunca deve ser aprovada (exceto emergência com plano concreto)
- ✅ Precedente: Se aprovada esta, quantas mais serão pedidas? (risco de "slippery slope")
- **Resultado:** ALINHADO / NÃO-ALINHADO (deve ser negada ou condicionada a mais requerimentos)

### Síntese de Risk Profiling

Após D1, codificar nível de **risco da decisão:**

| Questões | Resultado | Risk Level |
|----------|-----------|-----------|
| Q1 SIM, Q2 SUFICIENTE, Q3 SIM, Q4 ALINHADO | Todas verdes | 🟢 **GREEN** — Decisão trivial, proceder |
| 3 SIM, 1 PARCIAL | Maioria positiva | 🟡 **AMBER** — Recomendação com condições |
| 2 SIM, 2 PARCIAL | Misto | 🟠 **ORANGE** — Escalation para CISO obrigatória |
| Q1 NÃO, ou Q2 INSUFICIENTE | Maioria negativa | 🔴 **RED** — Negar a menos que redesenhada |

---

## 🎯 FASE 3 — Decisão R1 (Decision Template)

**Objetivo:** Alçada apropriada toma decisão explícita baseada em D1.

### Template R1: 4 Opções de Decisão

```markdown
## Decisão de Exceção — [App] — [Requisito]

**Data:** [YYYY-MM-DD]
**Decisor:** [Nome] — [Função/Alçada]
**D1 Risk Level:** [GREEN / AMBER / ORANGE / RED]
**Nível App:** [L1 / L2 / L3]

---

### Opção Selecionada

**☐ APPROVE**
- **Justificativa:** [Ex: L1 app, compensação SIEM suficiente, prazo revalidação 6m]
- **Compensações confirmadas:** [SIEM alert para X, manual audit trimestral, redução acesso]
- **Revalidação:** [Data exata, ex: 2025-06-30]
- **Dono revalidação:** [Nome]
- **Consentimento risco:** AppSec confirma risco aceitável para nível

**☐ APPROVE-CONDITIONAL**
- **Condições:** [Ex: Apenas aprovada se compensação X implementada antes 2025-02-15]
- **Status compensação:** [Em progresso / Pendente / Concluída]
- **Prazo implementação:** [Data]
- **Validação pré-aprovação:** [Quem confirma que compensação está pronta]
- **Revalidação:** [Data exata pós-compensação]

**☐ DEFER**
- **Razão:** [Ex: Prazo revalidação indefinido, pedir roadmap concreto para remoção]
- **Feedback para Dev:** [O que falta: plano, compensação melhor, timing]
- **Data de revisão:** [Data quando será resubmetida]
- **Critério para aprovação próxima:** [Ex: "Necessário roadmap com commit de orçamento"]

**☐ DENY**
- **Razão:** [Ex: Risco L3 sem compensação adequada, requisito não é negociável]
- **Caminho alternativo:** [Ex: "Usar solução cloud alternativa que cumpre requisito?"]
- **Escalation:** [Se negação causa bloqueio de negócio, escalar para CISO com justificação]
- **Data reavaliação:** [Se situação mudar tecnicamente ou negócio, quando reavalia]

---

### Assinatura & Timestamp
- **Decisor:** ______________________
- **Data:** _____________________
- **Arquivo em:** GRC system, Jira, ou versionado em Git
```

---

## 🔀 FASE 4 — Escalation E1 (Conflict Resolution)

**Objetivo:** Quando há conflito técnico/negócio, escalar com critério claro.

### Casos de Escalation

**Tipo 1 — Risco Técnico vs. Pressão Negócio:**
- Dev: "Não conseguimos logs 90 dias, infraestrutura não aguenta, custo €50k"
- AppSec: "Não é aceitável, requisito é obrigatório"
- **Escalação para:** CISO + CFO (decisão de risco aceitável para negócio)
- **Critério de resolução:** "Qual é a tolerância de risco para negócio? Pode custar €50k?"
- **SLA resolução:** 10 dias úteis
- **Decisão final:** CISO + CFO decidem: Aprovar com compensação, ou investir nos €50k

**Tipo 2 — Compensação Técnica Desacordo:**
- AppSec: "SIEM alert não é suficiente, precisa retenção logs"
- DevOps: "SIEM alert é melhor, logs custam 2x"
- **Escalação para:** AppSec Lead + DevOps Lead + CISO
- **Critério:** "É SIEM adequate, ou obriga retenção?"
- **SLA resolução:** 5 dias úteis
- **Decisão final:** Técnicos + CISO consenso

**Tipo 3 — Prazo Revalidação Indefinido:**
- Exception: "Log retention 90d, compensado por SIEM"
- Problema: Nenhum roadmap para remover exceção
- **Escalação para:** App Owner + AppSec
- **Critério:** "Qual é o plano real? Quando sai da exceção?"
- **SLA resolução:** 3 dias úteis
- **Decisão final:** Definem data de revalidação concreta ou DEFER

### Template E1: Escalation Log

```markdown
## Escalation Register — [Data]

| App | Requisito | Conflito | Escalação Para | Criterio | Data Resolução | Resultado | Owner |
|-----|-----------|----------|----------------|----------|----------------|-----------|-------|
| app-pay | REQ-LOG | Custo vs risco | CISO + CFO | Tolerância €50k | 2025-02-10 | Aprovado, compensação SIEM | CISO |
| api-core | REQ-ENC | SIEM vs retenção | AppSec + DevOps | Adequação mitigação | 2025-02-08 | Exige retenção, nega SIEM-only | AppSec |

```

---

## 📍 Matriz Decisória por Alçada & Nível

**Quem tem autoridade de decisão R1?**

| Contexto | Alçada | Aprovação Adicional | SLA Decisão |
|----------|--------|-------------------|-------------|
| **L1 - Exceção pequena** | AppSec Engineer | Nenhuma (se D1 GREEN) | 3 dias úteis |
| **L1 - Exceção média** | AppSec Lead | App Owner (se custo) | 5 dias úteis |
| **L2 - Exceção qualquer** | AppSec Lead + App Manager | GRC (se >6 meses) | 5-7 dias úteis |
| **L3 - Exceção qualquer** | CISO + AppSec Lead | Direção (se risco alto) | 1-2 dias úteis |
| **Conflito técnico/negócio** | CISO + CFO | Direção Executiva | 10 dias úteis |
| **Emergência (post-deployment)** | CISO | CTO, Direção | 1 dia útil |

---

## ⏱️ SLA por Proporcionalidade L1/L2/L3

| Nível | Tempo Aprovação | Revalidação | Extensão Máxima |
|-------|-----------------|-------------|-----------------|
| **L1** | 3-5 dias úteis | 6-12 meses | Max 1x, após 1a, nega |
| **L2** | 5-7 dias úteis | 3-6 meses | Max 2x, após, CISO | 
| **L3** | 1-3 dias úteis | 3 meses | Max 1x, após, nega ou investimento |

---

## 📈 KPIs & Auditória

**KPI-1: % Decisões D1 documentadas**
- **Target:** ≥95%
- **Frequência:** Mensal
- **Owner:** GRC
- **Métrica:** (Exceções com D1 completo / Total exceções) × 100

**KPI-2: Tempo de decisão (V1 → R1)**
- **Target:** ≤5 dias úteis (L1/L2), ≤2 dias (L3)
- **Frequência:** Semanal
- **Owner:** AppSec
- **Métrica:** Percentil 75 tempo entre sugestão e decisão

**KPI-3: Taxa de escalation (E1)**
- **Target:** ≤15% exceções
- **Frequência:** Mensal
- **Owner:** GRC
- **Métrica:** (Exceções escaladas / Total exceções) × 100

**KPI-4: Taxa de cumprimento compensações**
- **Target:** ≥90% compensações implementadas conforme aprovação
- **Frequência:** Mensal
- **Owner:** AppSec
- **Métrica:** (Exceções com compensação ativa / Total exceções aprovadas) × 100

**KPI-5: Exceções resolvidas (removidas)**
- **Target:** ≥30% exceções removidas após revalidação
- **Frequência:** Trimestral
- **Owner:** GRC
- **Métrica:** (Exceções removidas no período / Total exceções revalidadas) × 100

---

## 📋 Cenário Real: Decisão Completa (D1 + R1 + E1)

**App:** app-inventario | **Requisito:** REQ-LOG-005 (Retenção logs 90 dias) | **Nível:** L2

---

### FASE 1 — Validação Prévia ✅ PASS
- ✅ App identificada, L2, owner João Silva
- ✅ REQ-LOG-005 não pode ser cumprido (infraestrutura limitada)
- ✅ Razão: "Backup cloud caro (€2k/mês), retenção on-prem sem espaço"
- ✅ Compensação proposta: "SIEM alerts para anomalias access + manual audit trimestral"
- ✅ Prazo revalidação: "2025-06-30" (6 meses, quando nova infraestrutura orçada)
- ✅ Risco conhecido: "Sem logs 90d, se incidente em log não rastreado, pode haver gap investigação"
- **Resultado:** Avançar para D1

---

### FASE 2 — Análise D1 (AppSec Lead: Maria Costa)

**D1-Q1: Risco é aceitável?**
- ✅ Severidade sem logs 90d: **Alta** (gaps investigação, compliance issue)
- ✅ Timing materialização: **Semanas** (se incidente hoje, logs não existem amanhã)
- ✅ Exploração provável: L2 app, não é internet-facing, acesso controlado (interno) → Probabilidade **Média**
- ✅ Impacto: **Integridade** (rastreabilidade perdida), **Conformidade** (audit trail)
- **Resultado:** ⚠️ **CONDICIONAL** (aceitável com compensações fortes)

**D1-Q2: Compensações adequadas?**
- ✅ SIEM alert para anomalias: "Existe SIEM? Tem rules para app-inventario?" → SIM, monitorado
- ✅ Manual audit trimestral: "Quem executa? AppSec? IT?" → AppSec responsável, SLA 1 semana
- ✅ Contínua: "SIEM 24/7, audit trimestral" → Adequate
- ✅ Para L2: Compensação forte (SIEM + audit) é suficiente para L2
- **Resultado:** ✅ **SUFICIENTE** (para L2, com compromisso audit)

**D1-Q3: Prazo revalidação realista?**
- ✅ Plano remover: "Nova infraestrutura orçada Q2 2025, implementação Q3" → Concreto
- ✅ Revalidação 6m: "2025-06-30" → Realista
- ✅ Dono: "AppSec Lead", owner app confirmou
- ✅ Se não removida: "Escala para CISO, renega a menos que recurso alocado"
- **Resultado:** ✅ **SIM** (plano claro, revalidação concreta)

**D1-Q4: Proporcionalidade respeitada?**
- ✅ L2 app: Compensação (SIEM + audit) é proporcional
- ✅ Precedente: "Outras L2 apps têm exceções logging? Se raros, OK. Se comum, risco de normalizarem."
- ✅ Não é L3 (crítico), não é exceção permanente (6m deadline)
- **Resultado:** ✅ **ALINHADO**

**Risk Profile:** 🟢 **GREEN** (3-4 questões verdes, compensação forte, prazo claro)

---

### FASE 3 — Decisão R1 (AppSec Lead, sem escalation necessária)

```markdown
## Decisão de Exceção — app-inventario — REQ-LOG-005

**Data:** 2025-02-20
**Decisor:** Maria Costa (AppSec Lead)
**D1 Risk Level:** 🟢 GREEN
**Nível App:** L2

---

### Opção Selecionada

**☑ APPROVE**
- **Justificativa:** L2 app, compensação SIEM + audit suficiente para 6 meses, roadmap concreto para remoção (Q3 2025)
- **Compensações confirmadas:** 
  1. SIEM anomaly alerts (24/7, monitored by SOC)
  2. Manual audit trimestral por AppSec (SLA 1 week pós-incidente)
  3. Redução log retenção 7 dias (vs 90d), monitorado
- **Revalidação:** 2025-06-30 (ou quando infraestrutura nova pronta)
- **Dono revalidação:** Maria Costa (AppSec Lead)
- **Consentimento risco:** AppSec confirms risco aceitável para L2 com compensações ativas

---

### Assinatura & Timestamp
- **AppSec Lead:** Maria Costa ✓ 2025-02-20 14:30
- **Arquivo em:** GRC system, issue APPS-1234 (versionado)
```

---

### FASE 4 — Escalation (Não necessária)
- D1 GREEN = sem escalation
- Compensações clara, prazo definido, roadmap confirmado
- **Resultado:** Exceção aprovada, implementação compensações começa imediatamente

---

### Execução & Follow-up
- ✅ 2025-02-20: Exceção aprovada, comunicada a app team
- ✅ 2025-02-25: SIEM rules validadas, audit trimestral agendada (2025-05-20)
- 📋 2025-06-30: Revalidação automática (se infraestrutura não pronta, escala para CISO)

---

## 🔗 Integração com Ciclo de Vida (Cap 14)

| Fase SDLC | Trigger | Responsável | Ação |
|-----------|---------|-------------|------|
| **Planning** | Requisito não viável | Dev + AppSec | Sugerir exceção (V1 validate) |
| **Design Review** | Exceção pendente | AppSec | Aplicar D1, submeter R1 |
| **Development** | Exceção aprovada | Dev | Implementar compensações, log em backlog |
| **Testing** | Exceção validação | QA + AppSec | Confirmar compensações ativas (SIEM alerts, audit) |
| **Deployment** | Pre-release | AppSec | Validação final antes deployment |
| **Revalidação** | 6/12 meses | AppSec + GRC | Avaliar se exceção pode ser removida |

---

## 📚 Referências & Ligações

- [Validação Empírica de Governança](addon/addon-12-validacao-empirica-governanca-cap14.md) ← I2 framework
- [Modelo de Governação](addon/01-modelo-governancao.md) — Contexto geral
- [Políticas Organizacionais](/governanca-contratacao/policies-relevantes) — Política de exceções
- [Papéis e Responsabilidades](/sbd-toe/000-teory-of-everything/07-roles) — Alçadas por função

---

## 🎯 Checklist Final de Implementação

- [ ] Template V1 (validação prévia) implementado em GRC
- [ ] Matriz D1 (4 questões + risk profiling) documentada
- [ ] Template R1 (4 decisões) em uso em GRC/Jira
- [ ] Template E1 (escalation log) criado
- [ ] Alçada matrix por L1/L2/L3 definida e comunicada
- [ ] SLA por nível (2-10 dias) comunicado a AppSec + CISO
- [ ] KPI-1 (% D1 documentado ≥95%) rastreado
- [ ] KPI-2 (tempo D1→R1 ≤5 dias) em dashboard
- [ ] KPI-3 (escalation rate ≤15%) monitorizado
- [ ] KPI-4 (cumprimento compensações ≥90%) validado
- [ ] KPI-5 (exceções removidas ≥30%) rastreado
- [ ] Training para approvers (AppSec, CISO, CFO) — 2h workshop
- [ ] Audit mensal de 10+ exceções para qualidade D1

