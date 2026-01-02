# Addon 11: Framework de Decisão para Alertas — Separação Sugestão/Decisão

## Objetivo

Estabelecer um framework explícito para separar a **sugestão automática** (alerta disparado por threshold/regra) da **decisão humana** (aprovar ação de resposta, escalacionar, ou classificar como falso positivo) no processo de detecção e resposta a incidentes. Este addon implementa o invariante I1 (Separação sugestão/decisão) no contexto operacional de monitorização, garantindo que decisões críticas de resposta a incidentes sejam sempre tomadas por pessoas qualificadas com informação completa e estruturada.

## Problema

Muitas equipas de operações funcionam com alertas que disparam automaticamente e requerem resposta imediata, mas sem um **ponto de decisão estruturado**. O resultado é:
- Falsas urgências: Alerta dispara, Ops executa remediation sem questionar se ameaça é real
- Decisões implícitas: Ninguém pergunta "é este o melhor remédio?" ou "temos confiança para executar?"
- Escalações ad-hoc: Conflito entre "disparamos agora" vs. "investiguemos primeiro" acontece sem regras claras

### Cenários de Risco

**Cenário 1 — Decisão implícita:**
- Alerta: "5 failed login attempts em 1 min"
- Gate automático: Bloqueia o IP
- 2 horas depois: Telefone: "O nosso cliente não consegue aceder, acusam-nos de blockade injustificado"
- **Problema:** Ninguém perguntou "é isto um ataque ou falha legítima?" antes de bloquear

**Cenário 2 — Conflito remediation vs. investigação:**
- Alerta: "Latência média > 2s (baseline 200ms)"
- SRE diz: "Reiniciamos serviço X (remédio rápido)"
- Security diz: "Espera, pode ser ataque DoS, investiga primeiro"
- **Problema:** Sem matriz de decisores, discussão é política, não técnica

**Cenário 3 — Falso positivo não gerido:**
- Alerta: "Acesso a recurso crítico de IP novo"
- Dispara 50x/dia por utilizadores legítimos em VPN
- Ops ignora alertas (alert fatigue)
- **Problema:** Nenhum procedimento para validar se é verdadeiro positivo antes de decidir remediation

## Solução: Framework de Decisão Estruturado

### Fase 1: Validação Prévia (Automática, Pré-Alerta)

Antes de um alerta ser apresentado a humanos, verificações básicas de integridade são feitas:

| Verificação | Objetivo | Falha |
|---|---|---|
| Dados disponíveis? | Métrica/log está preenchida | Skip alerta, investigate | 
| Alerta não é duplicado? | Mesma condição já notificada? | Suprimir duplicado |
| Baseline existe? | Comparação baseline vs actual | Use default threshold |
| Contexto disponível? | User/IP/service info acessível | Attach "context unavailable" ao alerta |

**Saída:** Se tudo OK → Procede para Fase 2 (Decisão). Se falha → Alerta é marked "low-confidence" ou suppressed.

### Fase 2: Análise (Structured Checklist D1)

Quando alerta é apresentado com "high confidence", responsável executa **Checklist D1** antes de qualquer ação.

#### Checklist D1: 4 Perguntas Críticas

```markdown
## Checklist D1 — Análise de Alerta para Resposta

[Data] [Alerta ID] [Responsável]

### Pergunta 1: O alerta é válido e a ameaça é real?

Evidência esperada:
- [ ] Métrica/log não está em erro (dados de qualidade OK)
- [ ] Padrão não é conhecido como falso positivo (histórico)
- [ ] Baseline é representativo (não foi recentemente alterado)
- [ ] Contexto confirma risco (ex: IP é known-malicious, user é unauthorized, resource é sensitive)

**Avaliação:** SIM / NÃO / INCERTO

**Se NÃO ou INCERTO, detalhar:**
- Por que pode ser falso positivo?
- Qual é a evidência que o contradiz?
- Qual é o passo seguinte (investigar, suprimir, afinar threshold)?

---

### Pergunta 2: O impacto é real ou apenas técnico?

Evidência esperada:
- [ ] Utilizadores/serviços são realmente afetados (não apenas métrica anómala)
- [ ] Business continuity é comprometida (ou apenas degradação aceitável?)
- [ ] Segurança é comprometida (confidencialidade, integridade, disponibilidade?)
- [ ] Conformidade regulatória é afetada?

**Avaliação:** SIM / NÃO / INCERTO

**Se NÃO ou INCERTO, detalhar:**
- Qual é o impacto real observado?
- Quantos utilizadores/transações são afetados?
- Qual é a janela temporal (agora, dentro de 1h, crônico)?

---

### Pergunta 3: Temos um remédio válido e testado?

Evidência esperada:
- [ ] Ação de remediation está documentada (procedimento, não ad-hoc)
- [ ] Remediation foi testado em staging/canary (funciona como esperado)
- [ ] Remediation pode ser revertido (rollback planejado)
- [ ] Remédio não causa colateral damage (ex: reboot não desativa backup)
- [ ] Remédio é proporcional ao risco (não mata mosca com canhão)

**Avaliação:** SIM / NÃO / INCERTO

**Se NÃO ou INCERTO, detalhar:**
- Qual é a ação proposta?
- Por que foi/não foi testada?
- Qual é o plano B se remediation falhar?

---

### Pergunta 4: Podemos executar AGORA com segurança?

Evidência esperada:
- [ ] Maintenance window é apropriado (não é horário crítico de negócio)
- [ ] Equipa está disponível (não é 3 da manhã, ninguém acordado)
- [ ] Comunicação está pronta (notificar clientes, status page, etc)
- [ ] Rollback é rápido (< 5 min se algo corre mal)
- [ ] Monitorização está ativa (saberemos em tempo real se remediation funciona)

**Avaliação:** SIM / NÃO / INCERTO

**Se NÃO ou INCERTO, detalhar:**
- Por que não agora?
- Quando é melhor momento?
- Qual é o risco de DEFERrir (situação piora enquanto espera)?

---

### Síntese de Risco

| Pergunta | Status | Severidade de Risco |
|---|---|---|
| Alerta é válido? | SIM / NÃO / INCERTO | CRÍTICA / ALTA / MÉDIA |
| Impacto é real? | SIM / NÃO / INCERTO | CRÍTICA / ALTA / MÉDIA |
| Remédio é válido? | SIM / NÃO / INCERTO | CRÍTICA / ALTA / MÉDIA |
| Podemos executar agora? | SIM / NÃO / INCERTO | CRÍTICA / ALTA / MÉDIA |

**Perfil de Risco Geral:**
- [ ] Verde (todos SIM) → Procede para Decisão (Opção 1: REMEDIATE-NOW)
- [ ] Amarelo (alguns NÃO, mitigações claras) → Procede com Decisão (Opção 2: ESCALATE-INVESTIGATE ou 3: DEFER-MONITOR)
- [ ] Vermelho (risco crítico, alerta pode ser FP ou remédio perigoso) → Recomenda Opção 4: FALSE-POSITIVE ou investigação profunda antes de qualquer ação
```

**Saída de D1:** Perfil de risco geral (Verde/Amarelo/Vermelho) + análise por pergunta.

### Fase 3: Decisão (Template R1)

Com D1 preenchido, decisor qualificado toma uma de **4 respostas possíveis**:

#### Template R1: Decisão de Resposta

```markdown
## Template R1 — Decisão de Resposta a Alerta

[Data] [Alerta ID] [Versão do alerta] [Decisor] [Cargo/Nível]

### Informação de Entrada

- **Status D1:** Verde / Amarelo / Vermelho
- **Risco Geral:** [CRÍTICA / ALTA / MÉDIA / BAIXA]
- **Análise por pergunta:** [resumo D1]

### Opções de Resposta

#### Opção 1: REMEDIATE-NOW
- **Significado:** Executar ação de remediation imediatamente
- **Quando usar:** D1=Verde, alerta é válido, impacto é real, remédio é seguro, timing é apropriado
- **Tempo SLA:** Remediation iniciada em < 15 min
- **Exemplo:** Failed login brute-force detectado → IP é known-malicious → bloquear IP imediatamente

#### Opção 2: ESCALATE-INVESTIGATE
- **Significado:** Alerta é válido mas requer investigação antes de remediation, escalar para equipa especializada
- **Quando usar:** D1=Amarelo, alerta é provavelmente válido mas remédio é incerto ou impacto é unclear
- **Tempo SLA:** Investigação iniciada em < 1h, decisão de remediation em < 4h
- **Exemplo:** Acesso a recurso crítico de IP novo → é cliente legítimo ou intruso? Investigar histórico de IP, verificar com utilizador, depois decidir se permite ou bloqueia

#### Opção 3: DEFER-MONITOR
- **Significado:** Alerta é válido mas não é urgente, monitorar e reavaliar em próxima janela
- **Quando usar:** D1=Amarelo, impacto é baixo, timing é inapropriado, melhor esperar
- **Tempo SLA:** Reavaliação em < 24h, escalação se situação piora
- **Exemplo:** Latência subiu 50% (baseline 200ms → 300ms) mas ainda é aceitável → monitorar próxima hora, se continua a subir, ativa remediation

#### Opção 4: FALSE-POSITIVE
- **Significado:** Alerta disparou mas não é ameaça real, classificar como FP e afinar alerta
- **Quando usar:** D1=Vermelho (alerta provavelmente inválido) ou confirmação que é FP
- **Tempo SLA:** Classificação em < 1h, ticket aberto para tuning em < 24h
- **Exemplo:** "5 failed login attempts" dispara, mas são tentativas de teste de QA → classificar como FP, adicionar IP de QA à whitelist, afinar regra para "5 failed logins de IPs não-whitelisted"

### Decisão Tomada

**Opção selecionada:** [ ] 1 / [ ] 2 / [ ] 3 / [ ] 4

**Justificativa (máx 5 linhas):**
[Decisor descreve por que essa opção é apropriada dado o perfil de risco D1]

**Plano de Ação (se aplicável):**
- [Se Opção 1: Quem executa remediation, até quando, como validar sucesso]
- [Se Opção 2: Quem investiga, deadline, próxima decisão]
- [Se Opção 3: Quando reavaliar, quem monitora, trigger de escalação]
- [Se Opção 4: Por que é FP, que muda no alerta, quem implementa]

**Assinado por:** [Nome] [Data] [Timestamp]
```

**Saída de R1:** Decisão clara (1-4), justificativa, plano de ação documentado.

### Fase 4: Escalation (Template E1 — Quando Há Conflito)

Se há discordância entre risco vs. remediation, ou entre decisores:

#### Template E1: Escalation de Conflito

```markdown
## Template E1 — Escalation de Conflito em Resposta

[Data] [Alerta ID] [Iniciador] [Cargo]

### Conflito Identificado

**Tipo:** [ ] FP Dispute / [ ] Remediation Risk / [ ] Business Impact Unclear / [ ] Timing Conflict

**Descrição:**
[Quem discorda, sobre o quê, por quê]

### Participantes

| Papel | Nome | Posição | Presente? |
|---|---|---|---|
| On-Call Ops | [TBD] | Operations | Sim / Não |
| Security Lead | [TBD] | AppSec/Security | Sim / Não |
| Engineering Lead | [TBD] | Engineering/Arch | Sim / Não |
| CTO / Escalation | [TBD] | Executive | Sim / Não |

### Argumentos Apresentados

**Posição A (ex: "Remediemos agora"):**
- Argumento 1: [...]
- Argumento 2: [...]
- Proposta de ação: [...]

**Posição B (ex: "Investigar primeiro"):**
- Argumento 1: [...]
- Argumento 2: [...]
- Proposta de ação: [...]

### Resolução

**Decisão escalada:** [Após discussão, decisão final tomada por autoridade]
- Opção eleita: [ ] 1 / [ ] 2 / [ ] 3 / [ ] 4
- Rationale: [Por que essa opção resolve o conflito]
- Ação imediata: [O que muda, quem faz, até quando]

**Assinado por:** [Escalation Authority] [Data] [Timestamp]
```

**Saída de E1:** Conflito documentado, posições claras, resolução autorizada.

---

## Matriz de Decisores por Classificação e Severidade

Quem pode tomar qual decisão em função de L1/L2/L3 e severidade de alerta:

| Classificação | LOW | MEDIUM | HIGH | CRITICAL |
|---|---|---|---|---|
| **L1** | Ops / On-Call | Ops Lead | Security Lead | CTO + Security |
| **L2** | Ops / On-Call | Ops Lead | Ops Lead + Security | CTO + Security |
| **L3** | Ops Lead | Ops Lead | Ops Lead | Ops Lead + Security (consultation) |

**Legenda:**
- **L1 (Manual logging, basic alerts):** Alerta pode ser FP frequente, remediation é manual
- **L2 (Structured logging, automated alerts):** Alerta é maior confiança, remediation é parcialmente automated
- **L3 (Full SIEM/SOAR, automated remediation):** Alerta é alta confiança, remediation é automatizado + testado

**Regras de Escalonamento:**
- Nenhum decisor abaixo do nível de classificação pode aprovar Opção 1 (REMEDIATE-NOW) sem consulta
- Se conflito surge (ex: Ops quer remediar, Security quer investigar), escalaciona para CTO
- CTO é autoridade final para decisões sobre remediação de CRITICAL/HIGH

---

## Proporcionalidade L1/L2/L3

### L1 — Manual, Low Automation
- **D1 (Checklist):** Todas as 4 perguntas devem ter resposta SIM
- **R1 (Decisão):** Apenas opção 1 (REMEDIATE-NOW) ou 4 (FALSE-POSITIVE)
- **Opção 2/3 (Escalate/Defer):** Requer aprovação de Ops Lead
- **Frequência de Decisão:** Manual por alerta, potencialmente lenta
- **Exemplo:** L1 app (criticalidade baixa), alerta: "Disk usage > 80%", Ops preenche D1, aprova Opção 1 (limpeza de logs), remediation manual

### L2 — Automated + Gated
- **D1 (Checklist):** 3 de 4 perguntas podem ser "INCERTO" se mitigações estão documentadas
- **R1 (Decisão):** Todas as 4 opções disponíveis
- **Opção 2 (ESCALATE):** Preferida para D1=Amarelo, permite investigação rápida antes de remediation
- **Frequência de Decisão:** Semi-automatizada, decisão em 1-4h
- **Exemplo:** L2 app (criticalidade média), alerta: "Failed login > 10 em 5 min", D1=Amarelo (pode ser ataque ou falha legítima), Ops aprova Opção 2 (ESCALATE: investigar IP reputation, check auth logs), Security investigar 1h, aprova Opção 1 (bloqueio) ou 4 (FP whitelist)

### L3 — Automated + Tested + Remediation Automated
- **D1 (Checklist):** Pode ter 1-2 perguntas com "INCERTO" se impacto é previsível e monitorável
- **R1 (Decisão):** Opção 1 (REMEDIATE-NOW) preferida, Opção 2 (ESCALATE) se investigação necessária
- **Frequência de Decisão:** Altamente automatizada, decisão em <1h ou até automática
- **Exemplo:** L3 app (criticalidade alta, auto-scaling), alerta: "CPU > 80% para 5 min", D1=Verde (é real, impacto é scaling necessário, remediation é autoscaling, timing é sempre apropriado), Ops aprova Opção 1 (trigger autoscaling imediatamente), monitorar 5 min, validar novo capacity

---

## SLA — Tempo de Decisão

| Severidade Máxima | SLA de Decisão | Rationale |
|---|---|---|
| CRÍTICA (ameaça ativa) | 1 hora | Urgência alta, mas permite D1 + R1 estruturado |
| ALTA | 4 horas | Impacto significativo, permite investigação |
| MÉDIA | 24 horas | Risco baixo-médio, permite planning |
| BAIXA | 72 horas | Risco mínimo, permite agendamento |

**Medição:**
- Começa quando alerta é apresentado com "high confidence"
- Termina quando R1 (ou E1) é assinado
- Escalações não reiniciam relógio, apenas documentam autoridade necessária

---

## KPIs de Execução

Métrica | Meta | Propósito
---|---|---
% de alertas com D1 documentado | > 90% | Consistência de processo |
Tempo médio D1 até R1 (minutos) | < 30 (L1), < 20 (L2), < 10 (L3) | Velocidade de decisão por classificação |
% de alertas aprovados em Opção 1 (REMEDIATE-NOW) | 50-70% | Balanço entre velocidade e cautela |
% de alertas aprovados em Opção 2 (ESCALATE) | 10-20% | Investigações que vale a pena fazer |
% de alertas classificados Opção 4 (FALSE-POSITIVE) | 10-20% | Taxa de FP, target para tuning |
% de alertas com escalation (E1) | < 5% | Raro, indica processos claros e decisores treinados |
SLA compliance (decisão antes do prazo) | > 95% | Responsabilidade de decisores |
Remediation success rate (Opção 1 efectivamente resolveu problema) | > 95% | Qualidade da decisão |

---

## Implementação Prática: Exemplo Completo

### Cenário: Alerta de Brute-Force em L2 App

**Alerta:** Failed authentication attempts > 5 em 1 minuto  
**Classificação:** L2 (criticalidade média, automatizado com gates)  
**Timestamp:** 14:23 PM (horário de negócio normal)

---

#### Fase 1: Validação Prévia (Automática)

| Verificação | Resultado |
|---|---|
| Dados disponíveis? | ✅ Log de auditoria de auth está preenchido |
| Não é duplicado? | ✅ Primeiro alerta desta IP nesta hora |
| Baseline existe? | ✅ Baseline de 0-2 failed attempts/min é conhecido |
| Contexto disponível? | ✅ IP, user, timestamp, recurso são todos preenchidos |

**Resultado:** Alerta é "high confidence" → Procede para D1

---

#### Fase 2: Analysis (Checklist D1)

```
Data: 2 Jan 2026, 14:23
Alerta ID: AUTH-BRUTE-20260102-001
Responsável: Alice (On-Call)

Pergunta 1: O alerta é válido e a ameaça é real?
Status: SIM (com confiança média)
- Métrica: Log de auth mostra 7 failed attempts em 60s (IP: 203.45.67.89)
- Histórico: IP não é conhecido como cliente legítimo
- Baseline: Baseline é 0-2/min, 7 é 3.5x acima
- Contexto: Utilizador é "admin" (high value target), recurso é "user-management-api" (sensível)
Avaliação: ✅ SIM—alerta é válido, padrão é suspeito

Pergunta 2: O impacto é real ou apenas técnico?
Status: SIM
- Utilizadores: admin account está protegido (não foi comprometido, attempts falharam)
- Business: Negócio não é impactado (acesso foi bloqueado automaticamente após 5 fails)
- Segurança: Risco ALTO—tentativa de comprometimento de admin
- Conformidade: Ataque é relevante para logging regulatório (GDPR, NIS2)
Avaliação: ✅ SIM—impacto é real, é tentativa de ataque

Pergunta 3: Temos um remédio válido e testado?
Status: SIM
- Ação: Bloquear IP 203.45.67.89 por 24h (firewall rule)
- Testado: Sim, procedimento foi validado em staging (IP é bloqueado, legítimos conseguem, blocklist é removido após 24h)
- Revertível: Sim, regra de firewall é versioned, pode ser removida em <1 min
- Colateral: Baixo—bloqueio é específico de IP, não afeta outros utilizadores
- Proporcional: Sim, 7 brute-force attempts é motivo clássico para blocklist temporária
Avaliação: ✅ SIM—remédio é válido, testado, revertível

Pergunta 4: Podemos executar AGORA com segurança?
Status: SIM
- Maintenance window: 14:23 é horário normal de negócio, timing é bom
- Equipa: Alice (on-call) está disponível e presente
- Comunicação: Alerta foi enviado para #security-incidents Slack
- Rollback: Firewall rule pode ser removido em <1 min se necessário
- Monitoração: Dashboards estão activos, veremos em tempo real se remédio funciona
Avaliação: ✅ SIM—podemos executar agora

SÍNTESE:
Pergunta 1: SIM (alerta é válido)
Pergunta 2: SIM (impacto é real)
Pergunta 3: SIM (remédio é válido)
Pergunta 4: SIM (timing é apropriado)

PERFIL: Verde (todos SIM) → Opção 1 (REMEDIATE-NOW) é recomendada

Assinado: Alice [sig] 14:23
```

---

#### Fase 3: Decision (Template R1)

```
Data: 2 Jan 2026, 14:24
Alerta ID: AUTH-BRUTE-20260102-001
Decisor: Alice (On-Call Engineer), L2 Operations

Entrada D1:
- Status: Verde (todos SIM)
- Risco geral: ALTA
- Recomendação: Opção 1 (REMEDIATE-NOW)

DECISÃO SELECIONADA: Opção 1 — REMEDIATE-NOW

JUSTIFICATIVA:
D1 é Verde com confiança alta. Alerta é válido (7 failed attempts >> 2 baseline),
ameaça é real (brute-force em admin account), remédio é simples e testado (firewall
block de IP), timing é apropriado (horário normal, equipa presente). Proceed com
bloqueio imediato de IP 203.45.67.89 por 24h.

PLANO DE AÇÃO:
- Ação: Firewall rule "BLOCK-IP-203.45.67.89-24h" será ativado
- Executor: Alice (On-Call)
- Deadline: Ativar em <5 min (antes 14:29)
- Validação: Confirmar que IP está bloqueado (access denied), logs mostram block
- Monitoração: Verificar se novos failed attempts vêm de outros IPs (spreading?)
- Rollback: Se necessário, rule será removida manualmente (Firewall change process)

Assinado: Alice [sig] 14:24
```

**Resultado:**
- 14:24: R1 decision assinado
- 14:27: Firewall rule ativado, IP 203.45.67.89 é bloqueado
- 14:28: Confirmação: Access denied para esse IP, logs mostram "Blocked by rule BLOCK-IP-24h"
- **Sucesso:** Brute-force attack foi bloqueado, admin account está protegido

---

## Checklist de Implementação

- [ ] **Definir Decisores Matriz:** Quem aprova o quê em cada L1/L2/L3 × severidade
- [ ] **Treinar Decisores:** Como preencher D1, como tomar R1, quando usar E1
- [ ] **Integrar D1 no Processo:** Quem preenche, quando, ferramentas (Jira? Template local? SIEM?)
- [ ] **Integrar R1 no Processo:** Aprovação é via comentário? Via formulário? Via CLI?
- [ ] **Integrar E1 escalation:** Quem é autoridade de escalation, como contactá-los
- [ ] **Monitorar KPIs:** Registar tempo D1→R1, % opções eleitas, % escalations, SLA compliance
- [ ] **Revisar Periodicamente:** Trimestralmente, validar se decisões estão melhorando resposta

---

## Referências

- **NIST SSDF PO.3.2:** Decision gates, segregation of duties in incident response
- **OWASP SAMM** (IM—Incident Management): Automated response vs. human-in-the-loop
- **CIS Controls v8 Control 18:** Automated incident response, playbook coordination

