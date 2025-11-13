# 📋 Síntese: Gestão de Exceções e Conformidade DORA

> **Contexto:** Este documento consolida como o SbD-ToE prescreve exceções formais **e como ausência de gestão formal as torna incoerentes com DORA Art. 5 (Supervisão de Gestão de Risco TIC)**.

---

## 1. O Que o SbD-ToE JÁ Prescreve

O manual tem **cobertura forte** sobre exceções formais, distribuída por capítulos:

| Capítulo | Artefacto | O que prescreve | Nível de formalidade |
|----------|-----------|-----------------|-------------------|
| **Cap. 01, addon 03** | `criterios-aceitacao-risco.md` | Limiares de aceitação por nível (L1≤9, L2≤6, L3≤4) | ✅ Quantitativo |
| **Cap. 02, addon 08** | `gestao-excecoes.md` | Processo formal: identificação → justificação → avaliação → compensação → revisão | ✅ Prescritivo |
| **Cap. 04, addon 03** | `excecoes.md` | Exceções a requisitos arquiteturais com TTL e responsáveis | ✅ Formal |
| **Cap. 05, addon 09** | `excecoes-e-aceitacao-risco.md` | Formalização de exceções a CVEs com owner e critério de encerramento | ✅ Formal |
| **Cap. 10** | `aplicacao-lifecycle.md` | Testes com "exceções formais aprovadas" | ✅ Mencionado |
| **Cap. 13** | `20-checklist-revisao.md` | Waivers/exceções temporárias aprovadas por AppSec/GRC/gestão | ✅ Formal |
| **Cap. 14** | User Stories US-15+ | RACI de aprovação, governança de exceções, auditoria | ⚠️ Parcial |

---

## 2. Os Gaps Críticos (Incoerência com DORA)

### Gap 1: Falta de Mapping de Autoridade DORA-compatível

**O Problema:**
- SbD-ToE diz: "AppSec Engineer valida L1" (informal)
- DORA exige: "Autoridade formal aprova" (governança explícita)
- **Resultado:** Organização aprova exceção informalmente → regulador questiona: "Quem aprovou?" → sem ata = falha de supervisão

**Exemplo:**
```
Situação: L3 aplicação com CVE crítico
SbD-ToE: "AppSec Engineer + GRC/Compliance aprovam"
DORA:    "Board ou CRO deve aprovar"
Risco:   Aprovação de CISO sem board = insuficiente para DORA
```

**Impacto regulatório:** Achado crítico de governance.

---

### Gap 2: Sem Categorização de Exceções Inaceitáveis em DORA

**O Problema:**
- SbD-ToE permite exceções com compensação (ex: "SQLi com WAF")
- DORA proíbe certos tipos (ex: "SQLi nunca é aceitável")
- **Resultado:** Organização registra exceção no SbD-ToE formalmente → regulador rejeita: "Esta exceção viola DORA" → revisão forçada, credibilidade questionada

**Exemplos de inaceitabilidade DORA:**
| Exceção | SbD-ToE | DORA | Risco |
|---------|---------|------|-------|
| "MFA opcional para MVP" | Tecnicamente aceitável em L1 | ❌ Viola Art. 19 (controlo obrigatório) | Regulador rejeita |
| "SQLi em endpoint legado com WAF" | Tecnicamente aceitável com compensação | ❌ Nunca aceitável (exploração direta) | Achado crítico |
| "CVE P0 sem plano de fix" | Aceitável se compensado | ❌ Viola Art. 19 (remediação obrigatória) | Violação normativa |

**Impacto:** Esforço desperdiçado, perda de confiança com regulador.

---

### Gap 3: Sem Processo de Escalada ao Regulador

**O Problema:**
- SbD-ToE registra exceções em ferramenta GRC (certo)
- DORA exige: "Reportar exceções críticas em contexto de incidente" (não-especificado)
- **Resultado:** Incidente de segurança; regulador pede: "Mostre exceções relacionadas" → organização não tem visão consolidada

**Cenário crítico:**
```
Incidente: SQLi explorado em produção
Descoberta: Havia exceção aprovada há 6 meses
Questão regulatória: "Porque não reportaram a exceção ao escalar o incidente?"
Impacto: Penalidade por falta de reporte
```

**Impacto:** Incumprimento de obrigação de reporte (Art. 18).

---

### Gap 4: Sem Política Organizacional Explícita

**O Problema:**
- SbD-ToE prescreve **como** gerir exceções (processo)
- Falta política **o que é aceitável** (governança)
- **Resultado:** Equipas interpretam diferente; inconsistência; regulador questiona: "Qual é a vossa política?" → sem resposta formal = violation

**Impacto:** Achado crítico de governance.

---

## 3. Incoerências Concretas Observadas

### Cenário A: Exceção Sem Documentação Formal

```
Realidade: Developer comunica por email: "Vamos aceitar CVE X porque recurso está escasso"
SbD-ToE compliance: ❌ Não está em ferramenta GRC; sem owner; sem TTL; sem aprovação formal
DORA compliance: ❌ GRAVE — Violação Art. 5 (falta de supervisão) + Art. 18 (sem trilho)
Resultado: Se incidente ocorre → regulador identifica negligência
```

---

### Cenário B: Exceção Expirada Silenciosamente

```
Realidade: Exceção L3 criada em Jan/2025 com TTL=90d; reavaliação agendada para Abr/2025
O que acontece: Reavaliação skipped; aplicação continua em produção com risco aceito
SbD-ToE compliance: ⚠️ FALHA — Revalidação obrigatória não aconteceu
DORA compliance: ❌ GRAVE — Violação Art. 5 (supervisão não-contínua)
Resultado: Risco aceito torna-se risco não-aceito; aplicação em non-compliance silencioso
```

---

### Cenário C: Exceção Inaceitável em DORA

```
Realidade: L3 app sem MFA; aprovado por AppSec como exceção com compensação (IP-restrict)
SbD-ToE compliance: ✅ OK — Processo formal seguido, aprovação documentada
DORA compliance: ❌ FALHA — MFA é obrigatório em Art. 19; compensação não é adequada
Resultado: Regulador descobre; achado crítico; credibilidade da organização questionada
```

---

### Cenário D: Incidente Sem Contexto de Exceção

```
Realidade: Exploração de CVE; organização tinha exceção registada há 2 meses
Incidente reportado, mas sem mencionar exceção
Investigação regulatória: Descobre que havia exceção; questiona por quê não foi escalada
SbD-ToE compliance: ✅ Exceção estava registada
DORA compliance: ❌ FALHA — Exceção-related incident não reportado conforme Art. 18
Resultado: Penalidade adicional por incumprimento de reporte
```

---

## 4. Como Resolver: Roadmap

### Passo 1: Política Organizacional Formal (semana 1–2)

```markdown
**Aprovação necessária:** Board/CISO

Definir:
- Categorias de exceção inaceitável (nunca aceitável em DORA)
- Mapeamento de aprovadores DORA-compatível:
  - L1: AppSec Engineer
  - L2: CISO / AppSec Engineer
  - L3: Board / CRO (exigência DORA)
- TTLs por nível (L1=12m, L2=6m, L3=3m)
- Processo de reavaliação obrigatória 15d antes da expiração
- Escalonamento ao regulador em contexto de incidente
```

### Passo 2: Ferramenta GRC (semana 3–4)

```
Configurar:
- Campos obrigatórios: id | aplicação | nível | exceção | justificação | aprovador | data | TTL | status
- Alertas automáticos: 15d antes da expiração
- Rastreamento de reavaliação: quem aprovou? quando? com que justificação?
- Reporte trimestral a governance (CISO/board)
- Integração com SIEM: escalada automática se incidente relacionado
```

### Passo 3: Template de Documentação (semana 5)

```
Para cada exceção (em GRC + repositório de segurança):

ID: EXC-2025-001
Aplicação: Pagamentos-Core (L3)
Exceção: CVE-2024-XXXXX em runtime (sem patch disponível)
Nível de Risco: P1 / Crítico
Justificação Técnica: Fornecedor não libertou patch; necessita refactoring de arquitetura
Compensação: Isolamento de rede + monitorização de comportamento reforçada + plano de migração para Jun/2025
Aprovador: CRO / Board (aprovação formal em ata Nº 2025-XXX)
Data: 2025-01-15
TTL: 2025-04-15 (90 dias)
Critério de Encerramento: Migração completa para novo runtime com patch aplicável
Observações DORA: Exceção temporária; plano de remediação em progresso; monitorização contínua
```

### Passo 4: Integração em User Stories Cap. 14 (semana 6)

Expandir `US-15 (Processo formal de exceções)` e adicionar `US-X (Compliance DORA de exceções)`.

---

## 5. Checklist de Conformidade

### Antes de Aceitar uma Exceção

- [ ] Exceção está em categoria **aceitável** (não é inaceitável per DORA)?
- [ ] **Aprovador apropriado** conforme nível (L1→AppSec, L2→CISO, L3→Board)?
- [ ] **TTL definido** (L1=12m, L2=6m, L3=3m)?
- [ ] **Critério de encerramento claro** (ex: "após implementação de fix X" ou "até data Y")?
- [ ] **Compensação documentada** (ex: controlo alternativo, monitorização reforçada)?
- [ ] **Entrada em GRC** com audit trail?
- [ ] **Alertas configurados** 15d antes da expiração?

### Quando Reavaliação Chega

- [ ] **Re-aprovação explícita exigida** (mesmo critério da aprovação original)?
- [ ] Se **expirada sem re-aprovação** → exceção encerrada automaticamente (risco volta a não-aceito)?
- [ ] Se **prorrogação necessária** → documentar nova justificação + novo TTL?

### Se Incidente Relacionado Ocorre

- [ ] **Exceção é escalada** ao regulador em contexto de incidente?
- [ ] **Trilho auditado** demonstra que exceção era conhecida e aprovada (mitigação regulatória)?

---

## 6. Referências Cruzadas

| Origem | O que prescreve | Para Conformidade DORA Adicionar |
|--------|-----------------|--------------------------------|
| Cap. 01, addon 03 | Critérios de aceitação de risco | Mapeamento a categoria DORA inaceitável |
| Cap. 02, addon 08 | Processo de gestão de exceções | Aprovadores DORA-compatível |
| Cap. 05, addon 09 | Exceções a CVEs | Template de reporte a regulador |
| Cap. 14, US-15+ | Governança de exceções | Política formal + approval matrix DORA |

---

## 7. Impacto de Ausência

**Se não resolver os gaps:**

| Gap | Impacto | Achado Regulatório |
|-----|--------|------------------|
| Sem mapeamento de autoridade | Aprovações informais; sem trilho | Achado crítico: Governance falha (Art. 5) |
| Sem categorização inaceitável | Exceções rejeitadas; revisão forçada | Achado crítico: Compliance falha |
| Sem escalada ao regulador | Incidente não-reportado com contexto | Achado crítico + Penalidade (Art. 18) |
| Sem política formal | Inconsistência; interpretação diferente | Achado crítico: Governance falha |

**Suma:** Organização com gaps identificados = risco elevado de penalidade regulatória em inspeção DORA.

---

**Próxima ação:** Implementar os 4 passos acima e validar com CISO/board.
