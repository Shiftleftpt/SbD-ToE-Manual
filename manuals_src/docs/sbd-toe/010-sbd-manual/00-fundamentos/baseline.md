---
id: baseline
title: Obrigações Mínimas Transversais
sidebar_label: 🛡️ Baseline Obrigatório
description: O núcleo duro de práticas que todas as aplicações devem cumprir, independentemente do nível de risco
tags: [obrigacoes, baseline, minimo, must, nis2, dora, gdpr]
sidebar_position: 4
---

# Obrigações Mínimas Transversais

A segurança de software não pode depender da criticidade de cada aplicação para garantir a existência de um **piso mínimo comum**.  
Sem esse alicerce, a organização fragmenta-se: algumas equipas aplicam práticas robustas, outras não aplicam nenhuma, e o resultado é um ecossistema inconsistente, vulnerável e difícil de auditar.

As **obrigações mínimas transversais** são, por isso, a base do SbD-ToE.  
Não pretendem substituir a proporcionalidade L1–L3, mas antes criar uma camada uniforme que garante que, seja qual for a aplicação, existe sempre um conjunto de controlos elementares implementados.

Estas obrigações não se aplicam apenas ao código ou à aplicação em si. Aplicam-se igualmente a **processos, pipelines, ambientes, automações e integrações externas** que participem no ciclo de vida do software.

A não aplicação de qualquer obrigação mínima **não é uma escolha técnica**, mas uma **decisão organizacional formal**, que deve ser explicitamente justificada, aprovada e rastreável conforme o modelo de governação do SbD-ToE (Cap. 14).

---

## 🎯 O Núcleo Duro: 8 Obrigações Transversais

Independentemente do nível de risco, **todas as aplicações** devem implementar:

### 1️⃣ **Classificação da Criticidade** (Cap. 01)
**O que**: Antes de iniciar qualquer desenvolvimento, classificar o nível de risco da aplicação (L1, L2, L3).

**Por quê**: Sem classificação, é impossível determinar que práticas aplicar. Torna a decisão de investimento em segurança arbitrária.

**Responsável**: Product Owner, Arquiteto, CISO

**Regulamentos**: NIS2 (assessment de risco), DORA (classificação de criticidade)

---

### 2️⃣ **Requisitos Mínimos de Segurança** (Cap. 02)
**O que**: Definir e rastrear um conjunto mínimo de requisitos de segurança que a aplicação deve cumprir.

**Por quê**: Requisitos explícitos permitem que DevOps e QA validem implementação; sem eles, segurança fica vaga.

**Responsável**: Product Owner, AppSec, QA

**Regulamentos**: NIS2 (medidas técnicas), GDPR (data protection by design)

---

### 3️⃣ **Gestão Explícita de Dependências** (Cap. 05)
**O what**: Manter um inventário atualizado de todas as dependências críticas (frameworks, bibliotecas, sistemas). Incluir versões e alertas de vulnerabilidades.

**Por quê**: A maioria das vulnerabilidades exploradas vêm de dependências não geridas ou desatualizadas. Um inventário é fundamental para incident response.

**Responsável**: DevOps, Developers, AppSec

**Regulamentos**: NIS2 (supply chain risk), DORA (vendor management)

---

### 4️⃣ **Coding Guidelines Básicas e Validação Automática** (Cap. 06)
**O que**: Aplicar um conjunto mínimo de guidelines de código seguro (ex.: evitar injection, validar inputs, usar hashing seguro). Configurar SAST (Static Application Security Testing) automático em todas as builds.

**Por quê**: Guidelines e SAST combinados eliminam a maioria das vulnerabilidades triviais com custo marginal quase nulo.

**Responsável**: Developers, AppSec, DevOps

**Regulamentos**: GDPR (security by design), NIS2 (medidas técnicas)

---

### 5️⃣ **Pipelines CI/CD com Verificações Mínimas** (Cap. 07)
**O what**: Executar pipelines CI/CD com gates mínimos de segurança (SAST, dependency scanning, secret scanning). Nunca fazer deploy sem validações.

**Por quê**: Pipelines automáticos garantem que nenhum código vulnerável chega a produção por lapso humano. Estas verificações podem ser totalmente automatizadas,desde que os critérios de execução e bloqueio sejam objetivos, determinísticos e auditáveis.

**Responsável**: DevOps, AppSec

**Regulamentos**: NIS2 (controlo de alterações), DORA (change management)

---

### 6️⃣ **Registo e Monitorização Essencial** (Cap. 12)
**O que**: Ativar logging mínimo em todos os serviços (eventos de autenticação, alterações críticas, erros). Correlacionar logs em ponto central e monitorizar anomalias.

**Por quê**: Logs são o alicerce da deteção de incidentes e da accountability regulatória.

**Responsável**: DevOps, Ops, CISO

**Regulamentos**: NIS2 (logging de incidentes), DORA (monitoring), GDPR (audit trails)

---

### 7️⃣ **Formação Inicial em Segurança** (Cap. 13)
**O que**: Garantir que todos os membros da equipa (Developers, QA, DevOps, etc.) recebem formação inicial obrigatória em segurança de software, alinhada aos papéis.

**Por quê**: Equipas conscientes de riscos evitam erros. Formação é o investimento com maior ROI em segurança.

**Responsável**: CISO, Security Champion, Gestão

**Regulamentos**: NIS2 (competência), DORA (staff training)

---

### 8️⃣ **Cláusulas Mínimas de Segurança em Fornecedores** (Cap. 14)
**O que**: Incluir em contratos com fornecedores/terceiros cláusulas mínimas de segurança (compromisso com responsabilidade de dados, direito de auditoria, notificação de incidentes).

**Por quê**: A cadeia de fornecimento é uma das maiores fontes de risco. Sem cláusulas contractuais, não há forma de exigir compliance.

**Responsável**: GRC, CISO, Jurídico

**Regulamentos**: NIS2 (cadeia de fornecimento), DORA (vendor management), GDPR (data processors)

---

## 📊 Mapa de Cobertura

| Obrigação | Capítulo | Responsável | Validação |
|-----------|----------|-------------|-----------|
| 1. Classificação | 01 | Product Owner / Arquiteto | CISO / GRC |
| 2. Requisitos | 02 | AppSec / Product Owner | QA / GRC |
| 3. Dependências | 05 | DevOps / Developers | SCA Tools / AppSec |
| 4. Coding Guidelines | 06 | Developers | SAST Tools / Code Review |
| 5. CI/CD Gates | 07 | DevOps | Automated Pipelines |
| 6. Logging | 12 | DevOps / Ops | Monitoring Tools / Auditores |
| 7. Formação | 13 | CISO / Security Champion | Attendance Tracking |
| 8. Contratos | 14 | GRC / Jurídico | Contract Review / Auditores |

---

## 💡 Racional Técnico-Científico

A definição destas obrigações mínimas baseia-se em:

### **Estudos de Incidentes Reais**
- **Verizon DBIR** (Data Breach Investigations Report): A maioria dos breaches decorre de falhas básicas — credenciais fracas, patches não aplicadas, falta de logging.
- **ENISA Threat Landscape**: Vulnerabilidades conhecidas (ex.: CVEs) são exploradas rotineiramente porque básicos não estão em lugar.

### **OWASP Top 10**
As 10 vulnerabilidades mais comuns poderiam ser impedidas por:
- **A01 Broken Access Control** → Requisitos claros (2)
- **A02 Cryptographic Failures** → Guidelines de código (4)
- **A03 Injection** → SAST + validação (4, 6)
- **A04 Insecure Design** → Threat modeling (3)
- **A05 Security Misconfiguration** → IaC + guidelines (4, 8)
- **A06 Vulnerable Components** → Dependency management (5)
- **A07 Authentication Failures** → Requisitos (2)
- **A08 Data Integrity Failures** → CI/CD gates (7)
- **A09 Logging & Monitoring Failures** → Logging obrigatório (12)
- **A10 SSRF** → Threat modeling (3)

### **Modelos de Maturidade**
Organizações avaliadas com OWASP SAMM mostram que **todas as maduras** partilham estas 8 práticas como base.  
Ausência de qualquer uma cria gaps significativos.

---

## ⚖️ Baseline vs. Proporcionalidade (L1–L3)

**Importante**: As obrigações mínimas **não substituem** a proporcionalidade L1–L3.

```
┌──────────────────────────────────────┐
│   8 Obrigações Mínimas (SEMPRE)      │
├──────────────────────────────────────┤
│  L1 (Baixo Risco)                    │
│  - Mínimos acima + validações básicas│
├──────────────────────────────────────┤
│  L2 (Risco Moderado)                 │
│  - Mínimos + práticas robustas       │
│  - Threat modeling, security reviews │
├──────────────────────────────────────┤
│  L3 (Risco Crítico)                  │
│  - Mínimos + aplicação integral      │
│  - Red teaming, auditorias rigorosas │
└──────────────────────────────────────┘
```

O que muda entre níveis é a **intensidade, profundidade e formalização**.  
Mas o baseline é transversal e **nunca é negociável**.

---

## 🔄 Pragmatismo e Aplicação Universal

Um aspeto essencial é a eficiência: em muitos casos, aplicar **determinadas práticas a todas as aplicações** é mais prático do que discussões caso a caso.

### Exemplos Práticos

**SAST em todos os repositórios**  
→ Mesmo com cost zero (ferramentas open source), elimina triviais.  
→ Menos falsos positivos do que SCA desconexo.

**Dependency scanning automático em pipelines**  
→ Um job padrão em todos os projetos simplifica política.  
→ Evita debates sobre "será que este lib é crítico?"

**Logging e monitorização por defeito**  
→ Ativar collectors em todos os serviços facilita auditorias.  
→ Detecta incidentes mais rapidamente.

**Templates contratuais mínimos**  
→ Aplicar cláusulas iguais a todos os fornecedores reduz negociação.  
→ Legal fica consistente.

---

## 📋 Checklist de Implementação

Para cada aplicação, validar:

- [ ] **Classificação (L1/L2/L3)** documentada e aprovada
- [ ] **Requisitos de segurança mínimos** definidos e rastreados
- [ ] **SBOM/inventário de dependências** atualizado
- [ ] **SAST configurado** e integrado em CI/CD
- [ ] **Dependency scanning ativo** com alertas
- [ ] **Coding guidelines** distribuídas à equipa
- [ ] **CI/CD gates** implementados (SAST, deps, secrets)
- [ ] **Logging mínimo** implementado e centralizado
- [ ] **Monitorização essencial** ativa (alertas críticos)
- [ ] **Formação de segurança** completada por todos
- [ ] **Cláusulas contratuais** em lugar com fornecedores

---

## 🔗 Alinhamento Regulatório

### **NIS2 (Directive on Network and Information Security)**
- ✅ Cobre: Medidas técnicas, logging, monitorização, avaliação de risco
- ✅ Todas as 8 obrigações contribuem para compliance NIS2

### **DORA (Digital Operational Resilience Act)**
- ✅ Cobre: Testes periódicos, gestão de fornecedores, resiliência
- ✅ Obrigações 5, 6, 7, 8 são essenciais para DORA

### **GDPR (General Data Protection Regulation)**
- ✅ Cobre: Privacy by design, security by design, logging
- ✅ Obrigações 2, 4, 6 são críticas para GDPR

### **PCI-DSS (Payment Card Industry)**
- ✅ Todas as 8 obrigações cobrem PCI-DSS mínimos

### **ISO/IEC 27001**
- ✅ Mapeamento direto: cada obrigação corresponde a controlos ISO

---

## 📈 Impacto Esperado

Com as 8 obrigações implementadas:

| Métrica | Impacto |
|---------|---------|
| **Vulnerabilidades Triviais** | ↓ 70-80% (SAST + guidelines) |
| **Incidentes por Dependências** | ↓ 60% (SCA + inventory) |
| **Tempo de Detecção (MTTD)** | ↓ 50% (logging + monitoring) |
| **Tempo de Resposta (MTTR)** | ↓ 40% (logs centralizados) |
| **Compliance Readiness** | ↑ 80%+ (rastreabilidade) |
| **Custo de Remediação** | ↓ 30% (early detection) |

---

## 🎯 Próximos Passos

1. **Audita o estado atual**: Qual destas 8 obrigações estão já implementadas?
2. **Prioriza gaps**: Qual é mais urgente? (Recomendação: começar com 1, 2, 5, 7)
3. **Aloca recursos**: Cada obrigação tem um "dono" — Define responsabilidades
4. **Define timeline**: Qual é o prazo para 100% compliance?
5. **Mede**: Estabelece KPIs para cada obrigação

---

**Leitura Relacionada**:
- [Papéis e Responsabilidades](./roles-responsabilidades/intro) — Quem implementa cada obrigação
- [Cap. 01 — Classificação](../01-classificacao-aplicacoes/intro.md) — Como classificar aplicações
- [Cap. 02 — Requisitos](../02-requisitos-seguranca/intro.md) — Como definir requisitos

---

**Nota Final**: O baseline é não-negociável, mas a sua implementação é flexível.  
Uma pequena startup pode aplicar os 8 com ferramentas open source e esforço mínimo.  
Uma enterprise aplicará com frameworks, conformidade regulatória e processos formalizados.  
Mas a essência é sempre a mesma: **nada fica sem segurança básica**.
