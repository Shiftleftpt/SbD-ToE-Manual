---
id: dora
title: DORA - Cross-Check Normativo
description: Análise de como o SbD-ToE cobre os requisitos técnicos do Regulamento DORA (UE 2022/2554)
tags: [cross-check, dora, regulamentacao, ict-risk, resiliencia, finanças]
sidebar_position: 1
---

# DORA: Cross-Check Normativo

> Para implementação prática, consulte o [Playbook SbD-ToE 4 DORA](/sbd-toe/002-cross-check-normativo/sbd-toe-4-dora-playbook).
> 
> Para exemplos práticos internos, ver pasta `exemplo-playbook/`.

## Enquadramento Geral

O **Digital Operational Resilience Act (DORA)** - Regulamento (UE) 2022/2554 - representa uma viragem histórica na forma como a União Europeia encara a **resiliência digital** no setor financeiro.  
A partir de janeiro de 2025, não basta às entidades financeiras protegerem dados ou cumprirem boas práticas gerais: exige-se que demonstrem, com evidências e mecanismos consistentes, que **sabem identificar, prevenir, detetar, responder e aprender com riscos tecnológicos**.

O SbD-ToE foi concebido como **modelo universal de segurança aplicacional** e cobre naturalmente os pilares técnicos da DORA. Este documento consolida:

1. **Cross-check normativo:** Como o SbD-ToE mapeia para DORA
2. **Playbook prático:** Roadmap de 12–18 meses para implementação

---

## PARTE I: ANÁLISE NORMATIVA

### Gestão de Risco TIC (Artigo 5 DORA)

O primeiro pilar da DORA reforça que a **resiliência digital é responsabilidade última do órgão de gestão**. O Artigo 5 exige: aprovação de estratégia, supervisão de execução, inventários de funções críticas, políticas de proteção/deteção/resposta.

**Cobertura SbD-ToE:**
- **Cap. 01:** Classificação de criticidade aplicacional (L1–L3)
- **Cap. 02:** Catálogo de requisitos de segurança por nível
- **Cap. 03:** Threat Modeling para identificação de riscos
- **Cap. 12:** Deteção, resposta e melhoria contínua
- **Cap. 14:** Governação e aprovação de políticas

**Lacuna intencional:** O SbD-ToE não fixa aprovação em board meeting (deixa em aberto). Para cumprir DORA: mapeie as políticas do SbD-ToE → aprove em board → registe a decisão formalmente.

---

### Incidentes e Reporte (Artigo 18 DORA)

Exige processo ponta-a-ponta: deteção, registo, classificação, reporte formal com templates normalizados.

**Cobertura SbD-ToE:**
- **Cap. 12:** Processos de deteção e resposta de incidentes
- **Cap. 14:** Responsabilidades de reporte e escalonamento

**Lacuna intencional:** O SbD-ToE não define taxonomia P0–P3 nem templates DORA (para manter universalidade). Para cumprir: configure campos de incidentes conforme RTS/ITS da DORA; exporte automaticamente do SIEM.

---

### Testes de Resiliência (Artigos 19–20 DORA)

Exige programa contínuo de testes, culminando em Threat-Led Penetration Testing (TLPT) para entidades elegíveis.

**Cobertura SbD-ToE:**
- **Cap. 03:** Threat Modeling (cenários de ataque realistas)
- **Cap. 10:** Catálogo de testes (SAST, DAST, fuzzing, etc.)
- **Cap. 11:** Validação de segurança pré-produção

**Lacuna intencional:** O SbD-ToE não fixa elegibilidade para TLPT nem processo de attestation (regulatório). Para cumprir: adicione secção no Cap. 10 "Readiness TLPT" com critérios; use relatórios SbD-ToE como base de attestation.

---

### Gestão de Fornecedores Críticos (Artigos 26–28 DORA)

Exige inventário formal, avaliação de risco, cláusulas obrigatórias, supervisão contínua, plano de saída testado.

**Cobertura SbD-ToE (Duas categorias de fornecedores, uma estratégia):**

**Categoria 1: Fornecedores de Componentes de Software (Cap. 05 - SBOM)**
- **O problema DORA:** Usas componentes (libs, frameworks) de terceiros sem saber quem são
- **A solução:** SBOM (Software Bill of Materials) identifica-os
- **Estes são fornecedores implícitos** (muitas vezes desconhecem que "fornecem")
- **Gestão:** SCA contínuo (análise de vulnerabilidades), atualizações de segurança, licenças
- **SBOM é pré-requisito para DORA:** Sem ele, não sabes quem são os teus fornecedores de software

**Categoria 2: Fornecedores Contratuais (Cap. 14 - Governance)**
- Pessoas e empresas contratadas formalmente (contractors, outsourcing, prestadores)
- **Estes são fornecedores explícitos** com contratos e responsabilidades documentadas
- Ciclo de vida formal: preparação → onboarding → monitorização → offboarding
- User Stories US-15 a US-20: Ciclo de vida de contractors/fornecedores

**Addon files (Cap. 14):**
- `02-template-validacao-contractors.md` (validação pré-acesso)
- `12-guia-preparacao-sandbox.md` (preparação técnica)
- `13-checklist-offboarding.md` (offboarding seguro)

**Conformidade DORA (Art. 26–28):**
- **Ambas categorias exigem inventário e supervisão** → não é opcional escolher uma
- SBOM alimenta inventário de risco técnico de componentes
- Fornecedores contratuais alimentam inventário de risco organizacional
- **Lacuna intencional:** O SbD-ToE não inclui templates ITS nem fórmulas DORA de análise de concentração. Para cumprir: mantenha SBOM atualizado (Cap. 05) + inventário formal de contractors (Cap. 14) + templates de contratos com cláusulas de segurança

---

### Partilha de Informação sobre Ameaças (Artigo 16 DORA)

Exige mecanismos de recolha e disseminação de informação sobre incidentes e ameaças TIC.

**Cobertura SbD-ToE:**
- **Cap. 12:** Integração de threat intelligence (STIX/TAXII)
- **Cap. 14:** Políticas de cooperação

**Lacuna intencional:** O SbD-ToE não define acordos institucionais nem processos de notificação ao supervisor. Para cumprir: use mecanismos de threat intel do Cap. 12; firme acordos conforme comunidade; notifique supervisor conforme canais estabelecidos.

---

### Gestão de Exceções e Desvios (Artigos 5, 18, 19–20, 26–28 DORA)

DORA não menciona explicitamente "exceções", mas em **conformidade regulatória**, exceções são **desvios formais de requisitos** que precisam de:
- Aprovação documentada (por quem? com que autoridade?)
- Justificação técnica/business
- Período de validade
- Plano de remediação

**Cobertura SbD-ToE (Parcial):**
- **Cap. 10:** Testes de segurança com "exceções formais aprovadas" (e.g., vulnerabilidades conhecidas com justificação)
- **Cap. 08:** IaC com "exceções de configuração" rastreadas
- **Cap. 14:** Governança com RACI para aprovações (implícito: quem aprova exceções?)

**Lacuna intencional:** O SbD-ToE não define:
- Quem tem autoridade para aprovar exceções em DORA (board? CISO? compliance officer?)
- Que exceções são admissíveis em DORA (algumas podem não ser permitidas)
- Templates de reporte de exceções ao regulador
- SLA de remediação por tipo de exceção

**Para cumprir DORA:**
- Estabeleça **política formal de exceções** (governance, aprovações, tracebilidade)
- Documente cada exceção: razão, aprovador, data de expiração, plano de fix
- Mantenha **trilho auditado** de exceções (pode ser pedido em inspeção)
- Valide com supervisor se exceções são admissíveis (algumas violações de Art. 5 podem ser inaceitáveis)

---

### Exceções Formais e Desvios de Conformidade (Artigos 5, 18, 19–20, 26–28 DORA)

#### O Problema: Exceções Informais = Incoerência com DORA

DORA Art. 5 estabelece que a **resiliência digital é responsabilidade última do órgão de gestão** (board), e **supervisão de execução** significa:
- Conhecer **todos os desvios** de políticas de segurança
- Aprovar formalmente exceções a controlos
- Documentar razões, período de validade e plano de remediação
- Manter trilho auditado para demonstrar ao regulador

**Cenário crítico (incoerência com DORA):**
| Situação | Risco | Impacto | Posição DORA |
|----------|-------|--------|-------------|
| **SQLi em produção (L3) sem exceção documentada** | Exploração, violação de dados, incident notificável | Responsabilidade não-atribuída, trilho perdido | ❌ **GRAVE** — Violação Art. 5 (sem supervisão) + Art. 18 (sem rastreamento) |
| **CVE crítico ignorado sem justificação** | Exposição contínua, compliance gap | Falha de gestão de risco TIC | ❌ **GRAVE** — Violação Art. 19–20 (teste de resiliência inadequado) |
| **Exceção aprovada verbalmente (no Teams/email informal)** | Perda de trilho, falta de autoridade formal, re-negociação ad-hoc | Impossível auditar decisões | ❌ **CRÍTICO** — Sem evidência de governance; regulador questiona: "quem aprovou?" |
| **Exceção expirada sem reavaliação** | Risco aceito torna-se risco não-aceito (drift), violação técnica silenciosa | Aplicação continua com risco acima de limite | ❌ **CRÍTICO** — Violação Art. 5 (falta de supervisão contínua) |

---

#### O que DORA Exige Explicitamente

**Art. 5 (Gestão de Risco TIC):**
> "Membros do órgão de gestão aprovam a estratégia e supervisionam a execução de políticas, incluindo respostas a riscos emergentes."

**Tradução operacional:**
- Toda decisão de aceitar risco (exceção) deve ter **aprovação documentada** de autoridade formal
- Regulador assume que se uma vulnerabilidade é explorada e você a "conhecia", **não tinha aprovação = negligência de supervisão**
- Exceções devem ser **reavaliadas periodicamente** (sem reavaliação = aprovação tácita indefinida = falha)

**Art. 18 (Incidentes):**
> "Exceções a testes de resiliência ou vulnerabilidades não-remediadas devem ser reportadas com contexto."

**Art. 19–20 (Testes):**
> "Programa contínuo de testes deve cobrir cenários realistas. Exceções (ex: componente legado não-testável) requerem compensação documentada."

**Art. 26–28 (Fornecedores):**
> "Exceções a SLAs de fornecedores ou CVEs não-mitigados devem ser escalados conforme plano de risco."

---

#### Cobertura SbD-ToE (Forte, mas com Gaps Explícitos)

**O que SbD-ToE JÁ PRESCREVE (excelente):**

| Capítulo | O que prescreve | Nível de detalhe |
|----------|-----------------|-----------------|
| **Cap. 01** | Classificação L1–L3 (base para criticidade de exceções) | ✅ Modelo E+D+I claro; criterios de L1/L2/L3 definidos |
| **Cap. 01, addon 03** | Critérios de aceitação de risco (limiares por nível) | ✅ L1≤9, L2≤6, L3≤4; requer validação por 2+ perfis em L2/L3 |
| **Cap. 02, addon 08** | Gestão de exceções a requisitos (processo formal) | ✅ Identificação, justificação, avaliação, compensação, revisão periódica |
| **Cap. 04, addon 03** | Exceções a requisitos arquiteturais | ✅ Modelo de registo com horizonte temporal; responsáveis designados |
| **Cap. 05, addon 09** | Exceções a CVEs (formalização, owner, TTL, impacto) | ✅ Processo completo: identificação → justificação → aceitação → TTL → revalidação |
| **Cap. 10** | Exceções a testes de segurança (com aprovação formal) | ✅ Menção explícita: "exceções formais aprovadas" |
| **Cap. 14** | Governança de exceções (RACI, approval flow, auditoria) | ⚠️ **PARCIAL** — User Stories definem roles, mas não explicam implicações DORA |
| **Cap. 13** | Waivers e exceções temporárias (durante formação) | ✅ "Justificação formal documentada, aprovada por AppSec/GRC/gestão" |

---

#### Gaps Identificados (Incoerências com DORA)

**Gap 1: Falta de Mapeamento Explícito de Autoridade DORA-compatível**

| Nível | SbD-ToE Prescreve | DORA Exige | Gap |
|-------|------------------|-----------|-----|
| **L1** | Validação por AppSec Engineer (informal) | Aprovação por autoridade formal designada | ⚠️ Developer-friendly, mas falta escalada clara |
| **L2** | Validação formal por AppSec + GRC | Aprovação por CISO ou equivalente formal | ✅ Adequado, mas manual não o diz explicitamente |
| **L3** | Aprovação de Gestão Executiva/CISO | **Aprovação de board ou CRO (exigência DORA)** | ❌ **GAP CRÍTICO** — Manual não especifica "board-level approval" |

**Como manifesta:** Organização aceita exceção L3 com aprovação de CISO; regulador questiona: "foi aprovada em board?" → sem ata = **falha de governance**.

---

**Gap 2: Falta de Descrição de Inaceitabilidade em DORA**

| Exceção | SbD-ToE | DORA |
|---------|---------|------|
| "Não implementar MFA porque é complexo" | Tecnicamente aceitável com TTL em L1 | ❌ **Pode violar DORA** (MFA é obrigatório em Art. 19) |
| "SQLi em endpoint legado, mantém-se" | Aceitável com compensação (ex: WAF) em L1/L2 | ❌ **Pode violar DORA** (SQLi é nunca aceitável em qualquer L) |
| "CVE P0 em runtime, sem plano de fix" | Aceitável se compensado em L1 | ❌ **Violação DORA** (Art. 19 requer plano de remediação) |

**Como manifesta:** Organização registra exceção no SbD-ToE formalmente; regulador rejeita: "esta exceção não é admissível em DORA" → perda de tempo, revisão forçada.

---

**Gap 3: Falta de Rastreamento de TTL vs. Supervisão Contínua**

| Processo | SbD-ToE | DORA Exigência | Gap |
|----------|---------|----------------|-----|
| **Criação de exceção** | Documenta com owner, TTL, critérios | ✅ Bom | ✅ Alinhado |
| **Reavaliação periódica** | Revisão 30 dias antes expiração; re-aprovação obrigatória | ✅ Bom | ✅ Alinhado |
| **Rastreamento centralizado** | Ferramenta GRC; audit trail por aplicação | ✅ Bom | ⚠️ Manual não descreve formato de reporte a DORA |
| **Escalada ao regulador** | Não mencionado no manual | ❌ DORA exige reportar exceções em contexto de incidentes | ❌ **GAP** — Sem guia de quando escalar ao regulador |

**Como manifesta:** Incidente de segurança; regulador pede: "mostre-me exceções relevantes" → organização não tem visão consolidada ou não sabe se deve reportar.

---

**Gap 4: Sem Política Organizacional Formal sobre Inaceitabilidade**

O SbD-ToE descreve **como** gerir exceções, mas não estabelece **quais categorias são inaceitáveis em DORA**:

- **Nunca aceitável (violação Art. 5):**
  - Exceções sem aprovação documentada
  - Exceções expiradas sem reavaliação
  - Violações de conformidade regulatória (ex: SQLi, injeção de comando)

- **Aceitável com restrições (compatível com DORA):**
  - Exceções com TTL, plano de fix e compensação
  - Exceções aprovadas por board/CRO
  - Exceções com trilho auditado

**Como manifesta:** Organização sem política = aceita exceção inaceitável; regulador → achado crítico.

---

#### Como Resolver a Incoerência

**1. Estabelecer Política Formal de Exceções Compatível com DORA**

```
POLÍTICA: Gestão de Exceções e Desvios de Conformidade

Objetivo: Garantir que todas as exceções a requisitos de segurança são aprovadas por autoridade formal, documentadas com trilho auditado, e compatíveis com exigências regulatórias (DORA).

Categorias de exceção:

A. Exceções INACEITÁVEIS (violação de DORA Art. 5/19):
   - Exceções sem aprovação documentada
   - Exceções expiradas sem reavaliação
   - Vulnerabilidades exploráveis sem compensação (ex: SQLi, injeção)
   - Violações de requisitos obrigatórios de conformidade
   ➜ Ação: REJEITAR; forçar mitigação

B. Exceções ACEITÁVEIS com aprovação board-level (L3 DORA):
   - Componentes legados sem patch aplicável
   - CVEs com "no fix available" + compensação (ex: isolamento de rede)
   - Arquitetura herdada em transição
   ➜ Ação: APROVAR se board/CRO assina; TTL ≤ 90 dias; reavaliação obrigatória

C. Exceções ACEITÁVEIS com aprovação CISO-level (L2 DORA):
   - Requisitos técnicos com compensação equivalente
   - Testes legítimos de resiliência suspensos (ex: TLPT adiado)
   ➜ Ação: APROVAR se CISO/AppSec assina; TTL ≤ 180 dias; reavaliação obrigatória

D. Exceções ACEITÁVEIS com aprovação AppSec-level (L1):
   - MVP com funcionalidade reduzida de segurança
   - Prototipagem com dados não-sensíveis
   ➜ Ação: APROVAR se AppSec assina; TTL ≤ 365 dias; reavaliação obrigatória

Rastreamento:
- Ferramenta GRC centralizada (SAP GRC, AuditBoard, ou custom)
- Campos: ID | Aplicação | Nível | Exceção | Justificação | Aprovador | Data | TTL | Status | Observações regulatórias
- Reporte trimestral a CISO/board
- Reporte ad-hoc a regulador se incidente relacionado
```

---

**2. Esclarecer no Manual SbD-ToE**

Adicionar ao Cap. 14 (Governança) uma secção dedicada:

```markdown
## 🚨 Compatibilidade DORA: Exceções Inaceitáveis vs. Aceitáveis

[Tabela acima com categorias A–D]

### Implicações Regulatórias

Se um incidente ocorre e há exceção relacionada:
- **Com aprovação documentada** → Demostra supervisão; mitigação regulatória
- **Sem aprovação documentada** → Evidência de negligência; penalidade potencial

### Processo de Escalada ao Regulador

[Template de como reportar exceção ao supervisor em contexto de incidente]
```

---

**3. Integrar em User Stories do Cap. 14**

Expandir `US-15 (Processo formal de exceções)` com:
- Approval Matrix DORA-compatível
- Categorias de inaceitabilidade
- Template de reporte ao regulador

---

#### Resumo: Por que Ausência de Gestão Formal = Incoerência DORA

| Aspecto | Sem Gestão Formal | Com Gestão SbD-ToE + DORA Mapping |
|--------|-------------------|----------------------------------|
| **Descoberta regulatória** | "Vocês aceitam exceções? Onde estão documentadas?" ❌ | "Sim, processo formal em GRC com aprovação board-level" ✅ |
| **Trilho auditado** | Exceções em Slack/Teams/informal ❌ | Exceções em ferramenta GRC com audit trail ✅ |
| **Supervisão do board** | Board não sabe de exceções críticas ❌ | Board recebe reporte trimestral de exceções L3 ✅ |
| **Resposta a incidentes** | "Não sabíamos desta vulnerabilidade" ❌ | "Vulnerabilidade estava em exceção aprovada com plano de fix; escalonada conforme protocolo" ✅ |
| **Achados auditoria** | Achado crítico: governance falha ❌ | Achado menor: melhorias operacionais ✅ |

---

### Conformidade Prática

**Para cumprir DORA + SbD-ToE:**
1. ✅ Usar processo formal de exceções do SbD-ToE (Cap. 14, Cap. 02 addon 08, Cap. 05 addon 09)
2. ✅ Mapear níveis a aprovadores DORA-compatíveis (L1→AppSec, L2→CISO, L3→Board/CRO)
3. ✅ Definir categorias de inaceitabilidade (política organizacional)
4. ✅ Rastreamento centralizado com audit trail (ferramenta GRC)
5. ✅ Reporte trimestral a governance (exigência DORA Art. 5)
6. ✅ Escalada ao regulador em contexto de incidente (Art. 18)

---

## CONCLUSÃO DO CROSS-CHECK

O **SbD-ToE cobre o coração técnico da DORA**. As lacunas observadas não são falhas, mas **abstenções deliberadas** para manter universalidade.

**Para conformidade plena:**
- Mapeie políticas SbD-ToE a aprovações formais (board)
- Configure campos de incidentes conforme DORA RTS/ITS
- Estenda inventários com dados regulatórios
- Calcule métricas DORA de concentração
- Formalize acordos de partilha de ameaças

---

## Referências

- SbD-ToE Manual (Capítulos 01–14)
- Regulamento DORA (UE 2022/2554)
- NIST SP 800-53, OWASP SAMM, BSIMM, SSDF
- Cap. 14 SbD-ToE: User Stories US-15 a US-20 (fornecedores/contractors)

---

**Versão:** 1.0  
**Data:** Novembro 2025  
**Próxima revisão:** Junho 2026
