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
- **Cap. 02:** Catálogo de requisitos de segurança por nível; gestão formal de exceções (addon 08)
- **Cap. 03:** Threat Modeling para identificação de riscos
- **Cap. 12:** Deteção, resposta e melhoria contínua
- **Cap. 14:** Governação e aprovação de políticas; RACI de exceções

**Evidência crítica de controlo (DORA Art. 5):**

A gestão formal de exceções é **demonstração direta de supervisão e controlo** do processo de desenvolvimento. Quando uma organização mantém trilho auditado de exceções (o quê, quem aprovou, quando, com que justificação, por quanto tempo), evidencia que:

1. **Conhece os seus riscos:** Identificou desvios e classificou-os formalmente
2. **Exerce supervisão:** Aprovou exceções com autoridade apropriada (board para L3, CISO para L2)
3. **Mantém controlo:** Reavalia periodicamente; encerra exceções expiradas; documenta compensações

**Cenário de auditoria DORA:**
- **Com gestão formal:** Regulador pede "mostre-me como gere desvios de requisitos" → organização apresenta ferramenta GRC com trilho completo → evidência de governance ✅
- **Sem gestão formal:** Regulador encontra vulnerabilidade conhecida em produção → questiona "aprovaram isto?" → sem documentação = falha de supervisão ❌

O SbD-ToE prescreve este processo formal em múltiplos capítulos (Cap. 02 addon 08, Cap. 04 addon 03, Cap. 05 addon 09, Cap. 14), garantindo que exceções não são "aceites informalmente", mas sim **governadas como decisões de risco documentadas**.

**Lacuna intencional:** O SbD-ToE não fixa aprovação em board meeting (deixa em aberto). Para cumprir DORA: mapeie as políticas do SbD-ToE → aprove em board → registe a decisão formalmente → mantenha exceções em ferramenta GRC com trilho auditado.

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

### Gestão de Exceções e Desvios de Conformidade (Artigos 5, 18, 19–20, 26–28 DORA)

DORA não menciona explicitamente "exceções", mas em **conformidade regulatória**, exceções são **desvios formais de requisitos** que evidenciam controlo e governação do processo de desenvolvimento.

#### Por Que Gestão Formal de Exceções É Crítica para DORA

**Exceções documentadas = Evidência de supervisão (Art. 5)**

Quando uma organização mantém trilho auditado de exceções com aprovação formal, demonstra ao regulador:
- Conhece os seus riscos (identificou desvios)
- Exerce supervisão (aprovou com autoridade apropriada)
- Mantém controlo (reavalia periodicamente, documenta compensações)

**Cenário regulatório:**
| Situação | Sem Gestão Formal | Com Gestão SbD-ToE |
|----------|-------------------|-------------------|
| Vulnerabilidade crítica em produção | "Não sabíamos" → negligência | "Exceção aprovada por board em [data], com compensação [X], TTL [90d]" → supervisão demonstrada |
| Auditoria DORA | "Como gerem desvios?" → sem resposta | Ferramenta GRC com trilho completo → evidência de governance |
| Incidente de segurança | Responsabilidade não-atribuída | Exceção relacionada escalada conforme protocolo → controlo demonstrado |

#### Cobertura SbD-ToE (Forte)

O SbD-ToE prescreve gestão formal de exceções em múltiplos capítulos:

| Capítulo | O que prescreve | Evidência de controlo |
|----------|-----------------|---------------------|
| **Cap. 01, addon 03** | Critérios de aceitação de risco (limiares L1≤9, L2≤6, L3≤4) | Quantifica tolerância ao risco por nível |
| **Cap. 02, addon 08** | Processo formal: identificação → justificação → avaliação → compensação → revisão | Demonstra supervisão contínua |
| **Cap. 04, addon 03** | Exceções arquiteturais com TTL e responsáveis | Governação de decisões técnicas |
| **Cap. 05, addon 09** | Exceções a CVEs com owner, TTL, critério de encerramento | Controlo de vulnerabilidades conhecidas |
| **Cap. 14** | RACI de aprovação, governança de exceções, auditoria | Autoridade formal e trilho |

**Requisitos críticos para DORA:**
- **Aprovação documentada:** Quem aprovou (board para L3, CISO para L2, AppSec para L1)
- **Justificação técnica:** Por que o desvio é necessário
- **TTL (Time-To-Live):** Período de validade (L3≤90d, L2≤180d, L1≤365d)
- **Compensação:** Controlos alternativos ou mitigação
- **Reavaliação:** Revisão obrigatória antes da expiração
- **Trilho auditado:** Ferramenta GRC centralizada

#### Gaps Face a DORA

**Gap 1: Mapeamento de Autoridade de Aprovação**

| Nível | SbD-ToE Prescreve | DORA Exige | Gap |
|-------|------------------|-----------|-----|
| **L1** | Validação por AppSec Engineer | Aprovação por autoridade formal designada | ⚠️ Falta formalização explícita |
| **L2** | Validação formal por AppSec + GRC | Aprovação por CISO ou equivalente | ✅ Adequado |
| **L3** | Aprovação de Gestão Executiva/CISO | **Board ou CRO** (Art. 5: accountable) | ❌ Manual não especifica board-level |

**Gap 2: Categorias de Inaceitabilidade**

Algumas exceções podem violar DORA mesmo com processo formal:
- SQLi em qualquer nível → nunca aceitável (exploração direta)
- Ausência de MFA em L3 → viola Art. 19 (controlo obrigatório)
- CVE crítico sem plano de remediação → viola Art. 19–20

**Gap 3: Escalada ao Regulador**

Se incidente ocorre e há exceção relacionada, DORA Art. 18 exige reporte com contexto. SbD-ToE não define quando/como escalar.

#### Como Cumprir DORA com SbD-ToE

Para garantir conformidade plena:

1. **Política formal de exceções:** Mapear aprovadores (L1→AppSec, L2→CISO, L3→Board/CRO); definir categorias inaceitáveis
2. **Ferramenta GRC:** Campos obrigatórios (id, aplicação, nível, exceção, justificação, aprovador, data, TTL, status); alertas 15d antes expiração
3. **Trilho auditado:** Rastreamento de quem aprovou, quando, com que justificação; reavaliação obrigatória
4. **Reporte trimestral:** Dashboard de exceções ativas apresentado a CISO/board
5. **Escalada regulatória:** Se incidente relacionado, incluir exceção no reporte Art. 18

**Referências SbD-ToE:**
- [Cap. 02 - Requisitos de Segurança](/sbd-toe/sbd-manual/requisitos-seguranca/intro) (addon 08: gestão de exceções)
- [Cap. 14 - Governança](/sbd-toe/sbd-manual/governanca-contratacao/intro) (RACI, aprovações, auditoria)

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
