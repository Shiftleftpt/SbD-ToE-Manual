# 🎓 Decisão Estruturada em Atribuição de Formação

> **Invariante I1 (agent.md):** Separação sugestão/decisão → Ferramenta sugere, humano decide com checklist + templates + escalation

---

## 📋 Objetivo

Implementar um **framework decisório estruturado** para atribuição de formação e capacitação, garantindo que:
1. **Sugestões de formação** (baseadas em gaps, promoções, onboarding) sejam validadas antes da atribuição
2. **Decisões** sejam tomadas por responsável apropriado (AppSec, GRC, Manager) com checklist formal
3. **Proporcionalidade L1/L2/L3** seja respeitada (não sobrecarregar L1, exigir Labs em L3)
4. **Conflitos de recurso** ou prioridade sejam escalados com critérios claros
5. **Rastreabilidade completa** da sugestão → decisão → execução → validação

---

## 🚨 Problema: Risco & Cenários

**Cenário 1 — Sugestão sem decisão consciente:**
- AppSec identifica gap: "Devs não compreendem threat modeling"
- Sistema propõe: "Oferecer course OWASP TM a todos L1"
- **Sem estrutura:** 10 Devs inscritos, mas ninguém aprovou timing ou orçamento → course cancelado, gap persiste
- **Risco:** Recursos gastos em inscrições que não avançam, gaps não resolvidos

**Cenário 2 — Proporcionalidade violada:**
- Manager quer inscrever L1 Dev em "Advanced Fuzzing Workshop" (3 dias, conteúdo L3)
- **Sem checklist:** Dev não tem prerequisitos (secure coding básico não consolidado)
- **Risco:** Formação ineficaz, Dev desmotivado, desperdício de tempo

**Cenário 3 — Conflito de recurso não escalado:**
- L3 AppSec selecionado para formação em "Security Incident Response" (obrigatória L3)
- Mas está em deployment crítico (Cap 11) na mesma semana
- **Sem escalation:** AppSec desiste de formação OU deixa deployment sem cobertura
- **Risco:** Qualidade comprometida (formação negligenciada ou produção em risco)

---

## 🔄 Framework: 4 Fases

```
┌─────────────────────────────────────────────────────────────┐
│ FASE 1: VALIDAÇÃO PRÉVIA (Pre-decision)                     │
│ └─ Dados de sugestão completos? Candidato ativo?            │
├─────────────────────────────────────────────────────────────┤
│ FASE 2: ANÁLISE D1 (Checklist de Decisão)                   │
│ └─ 4 questões críticas com risk profiling                   │
├─────────────────────────────────────────────────────────────┤
│ FASE 3: DECISÃO R1 (Decision Template)                      │
│ └─ 4 opções: ASSIGN / DEFER / ESCALATE / HOLD               │
├─────────────────────────────────────────────────────────────┤
│ FASE 4: ESCALATION E1 (Conflict Resolution)                 │
│ └─ Quando há conflito: horário, orçamento, prereq.          │
└─────────────────────────────────────────────────────────────┘
```

---

## 📍 FASE 1 — Validação Prévia

**Objetivo:** Confirmar que sugestão está completa antes de submeter a decisão.

**Checklist V1:**
- [ ] **Candidato identificado:** Nome, função, nível aplicação (L1/L2/L3), data onboarding/promoção
- [ ] **Sugestão clara:** Trilho/formação específica, duração, formato (lab/code clinic/quiz/microlearning)
- [ ] **Justificativa documentada:** Gap identificado? Promoção? Onboarding obrigatório? Regulatória? 
- [ ] **Candidato ativo:** Não em licença, não planeado para saída próxima, acesso ativo
- [ ] **Prereq. verificados:** Se trilho L2+ exigir prereq, confirmar conclusão anterior
- [ ] **Data/horário preliminar:** Sugestão não conflita com outros compromissos (deploy, audit, férias)?

**Se qualquer item FALHAR:**
→ Devolver sugestão com feedback → Aguardar resubmissão completa

---

## 📊 FASE 2 — Análise D1 (Decisão Checklist)

**Objetivo:** Responsável (AppSec/GRC/Manager) responde 4 questões críticas.

### Checklist D1: 4 Questões

**D1-Q1: Candidato está qualificado?**
- ✅ Tem pré-requisitos? (ex: L1 antes de L2)
- ✅ Tem background técnico mínimo? (ex: não inscrever QA em "advanced code fuzzing")
- ✅ Tem tempo disponível? (capacidade de 30-40h formação + prática)
- **Resultado:** SIM / NÃO / CONDICIONAL (com condições claras)

**D1-Q2: Trilho é apropriado?**
- ✅ Alinha-se com função atual ou carreira planeada? (não prescrever formação irrelevante)
- ✅ Proporcionalidade respeitada? (L1 básico, L2 intermédio, L3 avançado)
- ✅ Timing apropriado? (não durante período de crise, deployment, audit)
- **Resultado:** SIM / NÃO / REFORMULAR

**D1-Q3: Recursos disponíveis?**
- ✅ Orçamento alocado? (se formação externa, instructor, lab infra)
- ✅ Mentor/coach disponível? (se exigido pela formação)
- ✅ Candidato tem tempo de trabalho alocado? (30% tempo, 50% tempo, etc.)
- **Resultado:** SIM / NÃO / PARCIAL (com mitigação)

**D1-Q4: Impacto & proporcionalidade?**
- ✅ Se negar, qual o gap? (continuará vulnerability explorado?)
- ✅ Se atribuir, impacto em produção? (deve suspender feature development?)
- ✅ Alinha-se com estratégia de formação anual? (budget, roadmap)
- **Resultado:** PRIORITÁRIO / NORMAL / SECUNDÁRIO

### Síntese de Risk Profiling

Após D1, codificar nível de **risco da decisão:**

| Questões | Resultado | Risk Level |
|----------|-----------|-----------|
| 4 SIM | Todas positivas | 🟢 **GREEN** — Decisão trivial, proceder |
| 3-4 SIM | Maioria positiva | 🟡 **AMBER** — Recomendação, revisar com manager |
| 2 SIM | Misto | 🟠 **ORANGE** — Escalation para GRC obrigatória |
| <2 SIM | Maioria negativa | 🔴 **RED** — Negar ou fundamentalmente reformular |

---

## 🎯 FASE 3 — Decisão R1 (Decision Template)

**Objetivo:** Responsável toma decisão explícita baseada em D1.

### Template R1: 4 Opções de Decisão

```markdown
## Decisão de Atribuição — [Candidato] — [Trilho]

**Data:** [YYYY-MM-DD]
**Decisor:** [Nome] — [Função]
**D1 Risk Level:** [GREEN / AMBER / ORANGE / RED]

---

### Opção Selecionada

**☐ ASSIGN-IMMEDIATELY**
- **Justificativa:** [Ex: L3 Audit Lead, obrigatório anual, formação já paga]
- **Timing:** [Data início — data fim]
- **SLA:** Confirmado com candidato em 2 dias úteis
- **Follow-up:** Validação via quiz/labs em [data]

**☐ ASSIGN-WITH-CONDITIONS**
- **Condições:** [Ex: Apenas se completa "Secure Coding 101" antes de 2025-02-15]
- **Timing:** Diferida para [data]
- **Owner de validação:** [Quem confirma pré-req.]
- **Follow-up:** Revalidar em [data]

**☐ DEFER-RESKILL**
- **Razão:** [Ex: Candidato não tem timing, ou pré-req. missing]
- **Plano alternativo:** [Ex: Microlearning mensal até consolidar prereq.]
- **Data de revisão:** [Q2 2026]
- **Owner:** [Quem valida consolidação]

**☐ ESCALATE-CONFLICT**
- **Conflito:** [Ex: Timing clash com deployment L3, orçamento não aprovado]
- **Escalação para:** [GRC / Gestão Executiva]
- **Critério de resolução:** [Ex: Deploy termina 2025-02-01, depois formação]
- **Data revisão:** [Data pós-resolução]

**☐ HOLD-PENDING**
- **Razão:** [Ex: Candidato em licença, volta [data]]
- **Revalidar em:** [Data]
- **Critério para reativação:** [Ex: Candidato ativo, orçamento confirmado]

---

### Assinatura & Timestamp
- **Decisor:** ______________________
- **Data:** _____________________
- **Arquivo em:** [GRC system, LMS, ou GitHub issue]
```

---

## 🔀 FASE 4 — Escalation E1 (Conflict Resolution)

**Objetivo:** Quando há conflito, escalar com critério claro.

### Casos de Escalation

**Tipo 1 — Timing/Recurso:**
- L3 AppSec está em deployment crítico + formação "Incident Response" (obrigatória L3)
- **Escalação para:** GRC + Gestão Executiva (conflito de prioridade)
- **Critério de resolução:** "Deployment é 2-3 semanas. Formação pode ser adiada para pós-deployment?"
- **SLA resolução:** 5 dias úteis
- **Decisão final:** GRC + Gestão Executiva aprovam adiamento ou alocam recurso alternativo

**Tipo 2 — Orçamento:**
- Manager quer inscrever 5 Devs em "Advanced Threat Modeling" (€2500/pessoa)
- Orçamento formação L2 é €5000/ano, já consumido
- **Escalação para:** GRC + Financeiro
- **Critério:** "Pode-se usar budget Q2 adiantado?"
- **SLA resolução:** 10 dias úteis
- **Decisão final:** GRC aprova ou nega com justificativa alternativa (microlearning em vez de workshop)

**Tipo 3 — Pré-requisito Missing:**
- Dev quer formação "Advanced API Security" sem ter completado "Secure Coding 101"
- **Escalação para:** AppSec Lead + Manager
- **Critério:** "Pode começar em paralelo, ou obrigatório sequencial?"
- **SLA resolução:** 3 dias úteis
- **Decisão final:** AppSec propõe caminho (sequencial vs. paralelo)

### Template E1: Escalation Log

```markdown
## Escalation Register — [Data]

| Candidato | Trilho | Conflito | Escalação Para | Data Resolução | Resultado | Owner |
|-----------|--------|----------|----------------|----------------|-----------|-------|
| João Silva | IRP L3 | Timing com deployment | GRC + Exec | 2025-02-10 | Adiado p/ Mar | GRC |
| Equipa QA | OWASP TM | Orçamento 5 pessoas | GRC + FIN | 2025-02-15 | 2 aprovadas | GRC |
| Maria Costa | API Sec | Pré-req missing | AppSec + Mgr | 2025-02-05 | Sequencial obr. | AppSec |

```

---

## 📍 Matriz Decisória por Papel & Nível

**Quem tem autoridade de decisão R1?**

| Contexto | Responsável | Aprovação Adicional | SLA Decisão |
|----------|-------------|-------------------|-------------|
| **Onboarding L1** | Manager + RH | Nenhuma (se D1 GREEN) | 5 dias úteis |
| **Formação contínua L1** | AppSec Engineer | Manager (se timing impacta sprint) | 5 dias úteis |
| **Trilho L2 especializado** | AppSec Lead + Manager | GRC (se orçamento >€1000) | 7 dias úteis |
| **Formação L3 obrigatória** | GRC + Gestão Executiva | Audit/Compliance (se regulatória) | 10 dias úteis |
| **Formação externa 3ª parte** | GRC + Financeiro | Gestão Executiva (se >€5000) | 10 dias úteis |
| **Conflito de timing** | GRC | Gestão Executiva | 5 dias úteis |

---

## ⏱️ SLA por Proporcionalidade L1/L2/L3

| Nível | Timing | Revisão | Reavaliação |
|-------|--------|---------|-------------|
| **L1** | Onboarding obrigatório (2 semanas após início) | Revisão mensal | Anual |
| **L2** | Normal (até 30 dias úteis) | Revisão quinzenal | Semestral |
| **L3** | Prioritário (até 10 dias úteis) | Revisão semanal | Trimestral |

---

## 📈 KPIs & Auditoría

**KPI-1: % Decisões D1 documentadas**
- **Target:** ≥95%
- **Frequência:** Mensal
- **Owner:** GRC
- **Métrica:** (Decisões com D1 completo / Total decisões) × 100

**KPI-2: Tempo de decisão (D1 → R1)**
- **Target:** ≤5 dias úteis (L1/L2), ≤3 dias (L3)
- **Frequência:** Semanal
- **Owner:** AppSec
- **Métrica:** Percentil 75 tempo entre sugestão e decisão

**KPI-3: Taxa de escalation (E1)**
- **Target:** ≤10% decisões
- **Frequência:** Mensal
- **Owner:** GRC
- **Métrica:** (Decisões escaladas / Total decisões) × 100
- **Nota:** >15% indica processo D1 inadequado

**KPI-4: Taxa de cumprimento (Decisão → Execução)**
- **Target:** ≥90% atribuições executadas conforme aprovado
- **Frequência:** Mensal
- **Owner:** RH + AppSec
- **Métrica:** (Formações iniciadas conforme R1 / Total R1 aprovados) × 100

**KPI-5: Satisfação & eficácia**
- **Target:** ≥8/10 satisfação candidato, ≥75% taxa aprovação quiz pós-formação
- **Frequência:** Trimestral
- **Owner:** AppSec
- **Métrica:** Survey pós-formação + resultados validação

---

## 📋 Cenário Real: Decisão Completa (D1 + R1 + E1)

**Candidato:** João Silva | **Função:** Senior Dev L2 | **Aplicação:** Payment Gateway (CRÍTICA, L3)

**Sugestão:** Inscrição em "Advanced Threat Modeling" (3 dias, workshop presencial, €1500)

---

### FASE 1 — Validação Prévia ✅ PASS
- ✅ Candidato ativo, não em férias
- ✅ Tem "Secure Coding 101" completado (pré-req.)
- ✅ Timing: 2025-03-10 a 12 proposto
- ✅ Justificativa: "Payment Gateway viu 2 vulns por threat modeling inadequado em design review Q4"
- **Resultado:** Avançar para D1

---

### FASE 2 — Análise D1 (AppSec Lead: Maria Costa)

**D1-Q1: Candidato qualificado?**
- ✅ Tem Secure Coding 101 (pré-req.)
- ✅ Background: 8 anos, 3 code reviews anteriores com feedback "threat model weak"
- ✅ Capacidade: Sim, 30h formação factível em 3 dias + prática semanal mês seguinte
- **Resultado:** ✅ **SIM**

**D1-Q2: Trilho apropriado?**
- ✅ Função: Dev L2, Payment Gateway (crítico)
- ✅ Proporcionalidade: L2 intermédio + labs → Apropriado
- ✅ Timing: "Advanced TM" em mar faz sentido, antes Q2 feature roadmap (abril-maio)
- **Resultado:** ✅ **SIM**

**D1-Q3: Recursos?**
- ⚠️ Orçamento Q1 formação L2: €8000. Já consumido €6500 (3 pessoas em Secure Coding avançado)
- ⚠️ €1500 restante é insuficiente
- ✅ Workshop tem versão online (€800), alternativa factível
- **Resultado:** ⚠️ **PARCIAL** (online instead of presencial, reduz custo)

**D1-Q4: Impacto & prioridade?**
- ✅ Gap real: 2 vulns por TM inadequado → Alta prioridade reduzir
- ⚠️ Timing conflita com sprint crítico (Pagamento: "PCI compliance audit" 2025-03-15)
- Mitigation: "Workshop 2025-03-10-12, audit é 2025-03-15 (5 dias). Factível, mas apertado."
- **Resultado:** 🟡 **AMBER** (apropriado, mas timing apertado com audit)

**Risk Profile:** 🟡 **AMBER** → Requer revisão com manager

---

### FASE 3 — Decisão R1 (AppSec Lead + Manager Pagamento)

**Reunião:** 2025-02-20 | **Participantes:** Maria Costa (AppSec), Pedro (Manager Pagamento)

```markdown
## Decisão de Atribuição — João Silva — Advanced Threat Modeling

**Data:** 2025-02-20
**Decisor:** Maria Costa (AppSec Lead) + Pedro (Manager Pagamento)
**D1 Risk Level:** 🟡 AMBER (timing PCI audit, orçamento limitado)

---

### Opção Selecionada

**☑ ASSIGN-WITH-CONDITIONS**
- **Condições:** 
  1. Workshop online (€800) em vez de presencial (€1500) → Orçamento aprovado
  2. Timing: 2025-03-10 a 12 (antes audit PCI 2025-03-15)
  3. João confirma compatibilidade com sprint (max 4h/dia trabalho durante 3 dias)
  4. Pós-workshop (2025-03-17+), aplicar threat modeling em design review reale (2+ sessões com AppSec)
  
- **Timing:** 2025-03-10 a 12
- **SLA:** Confirmado com candidato em 3 dias (by 2025-02-23)
- **Follow-up:** Validação via design review threat models em 2025-04-30

**Justificativa:** Gap real, candidato qualificado, timing apertado mas factível com online format. Pós-formação aplicação em design reviews confirmará eficácia.

---

### Assinatura & Timestamp
- **AppSec Lead:** Maria Costa ✓ 2025-02-20 14:30
- **Manager:** Pedro ✓ 2025-02-20 14:45
- **Arquivo em:** GRC LMS + Cap13/decisions/2025-02-20-joao-silva-tm.md
```

---

### FASE 4 — Escalation (Não necessária, verde)
- D1 AMBER foi revisado com ambos stakeholders
- Condições resolvem timing + orçamento
- **Resultado:** Decisão aprovada, sem escalation

---

### Execução & Follow-up
- ✅ 2025-02-23: João confirmado em workshop online
- ✅ 2025-03-10-12: Workshop executado
- 📋 2025-04-30: AppSec revê threat models em 2+ design reviews para validar aprendizado (Cap 13, addon-12)

---

## 🔗 Integração com Ciclo de Vida (Cap 13)

| Fase SDLC | Trigger | Responsável | Ação |
|-----------|---------|-------------|------|
| **Planning** | Nova feature L2+ | AppSec | Sugerir formação threat modeling se gap detectado |
| **Onboarding** | New hire | RH + AppSec | Aplicar D1 para assigned trilho + D1 checklist |
| **Development** | Code review feedback | AppSec | Sugerir formação específica se padrão errado |
| **Audit/Compliance** | Annual training review | GRC | Validar D1 aplicado a 95%+ decisões |

---

## 📚 Referências & Ligações

- [Trilhos Formativos por Função](addon/02-trilho-formativo)
- [Validação Empírica de Formação](addon/addon-12-validacao-empirica-formacao-cap13.md) ← I2 framework
- [Papéis e Responsabilidades](/sbd-toe/000-teory-of-everything/07-roles) — Cap 13 roles
- [Classificação Aplicações](/classificacao-aplicacoes/intro) — L1/L2/L3 contexto

---

## 🎯 Checklist Final de Implementação

- [ ] Template D1 e R1 documentados em wiki/sharepoint
- [ ] Quadro "Decisões Pendentes" criado (Jira/ADO com D1 status)
- [ ] SLA por nível (L1/L2/L3) comunicado a AppSec + RH + GRC
- [ ] KPIs configurados em dashboard (% D1, tempo médio, escalations)
- [ ] Training para decision-makers (AppSec, GRC, Managers) — 1h workshop
- [ ] Audit trimestral de decisões (amostra 10+ casos)
- [ ] Feedback loop: KPIs mensurados, resultado reportado a Gestão

