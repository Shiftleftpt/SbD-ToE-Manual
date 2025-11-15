---
id: intro
title: DORA - Cross-Check Normativo
description: Análise de como o SbD-ToE cobre os requisitos técnicos do Regulamento DORA (UE 2022/2554)
tags: [cross-check, dora, regulamentacao, ict-risk, resiliencia, finanças]
sidebar_position: 1
---

# DORA: Cross-Check Normativo

> Para implementação prática, consulte o [Playbook SbD-ToE 4 DORA](/sbd-toe/cross-check-normativo/sbd-toe-4-dora-playbook).
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
- **[Cap. 01](/sbd-toe/sbd-manual/classificacao-aplicacoes/intro):** Classificação de criticidade aplicacional (L1–L3)
- **[Cap. 02](/sbd-toe/sbd-manual/requisitos-seguranca/intro):** Catálogo de requisitos de segurança por nível
- **[Cap. 03](/sbd-toe/sbd-manual/threat-modeling/intro):** Threat Modeling para identificação de riscos
- **[Cap. 12](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro):** Deteção, resposta e melhoria contínua
- **[Cap. 14](/sbd-toe/sbd-manual/governanca-contratacao/intro):** Governação e aprovação de políticas

**Lacuna intencional:** O SbD-ToE não fixa o nível hierárquico de aprovação (mantém flexibilidade organizacional). A conformidade com DORA requer mapeamento das políticas SbD-ToE para aprovação formal em órgão de gestão, com registo documental da decisão.

---

### Incidentes e Reporte (Artigo 18 DORA)

Exige processo ponta-a-ponta: deteção, registo, classificação, reporte formal com templates normalizados.

**Cobertura SbD-ToE:**
- **[Cap. 12](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro):** Processos de deteção e resposta de incidentes
- **[Cap. 14](/sbd-toe/sbd-manual/governanca-contratacao/intro):** Responsabilidades de reporte e escalonamento

**Lacuna intencional:** O SbD-ToE não define taxonomia de prioridades (P0–P3) nem templates específicos DORA, preservando universalidade. A conformidade requer configuração de campos de incidentes segundo RTS/ITS da DORA e integração com sistemas de reporte automático (ex: SIEM).

---

### Testes de Resiliência (Artigos 19–20 DORA)

Exige programa contínuo de testes, culminando em Threat-Led Penetration Testing (TLPT) para entidades elegíveis.

**Cobertura SbD-ToE:**
- **[Cap. 03](/sbd-toe/sbd-manual/threat-modeling/intro):** Threat Modeling (cenários de ataque realistas)
- **[Cap. 10](/sbd-toe/sbd-manual/testes-seguranca/intro):** Catálogo de testes (SAST, DAST, fuzzing, etc.)
- **[Cap. 11](/sbd-toe/sbd-manual/deploy-seguro/intro):** Validação de segurança pré-produção

**Lacuna intencional:** O SbD-ToE não estabelece critérios de elegibilidade para TLPT nem processos de attestation regulatório. Recomenda-se adicionar secção "Readiness TLPT" ao [Cap. 10](/sbd-toe/sbd-manual/testes-seguranca/intro) com critérios organizacionais; os relatórios SbD-ToE podem servir de base documental para processos de attestation.

---

### Gestão de Fornecedores Críticos (Artigos 26–28 DORA)

Os Artigos 26–28 estabelecem requisitos para inventário formal, avaliação de risco, cláusulas contratuais obrigatórias, supervisão contínua e planos de saída testados.

**Cobertura SbD-ToE (Duas categorias de fornecedores, uma estratégia):**

**Categoria 1: Fornecedores de Componentes de Software ([Cap. 05](/sbd-toe/sbd-manual/dependencias-sbom-sca/intro) - SBOM)**
- **Contexto DORA:** Componentes de software (bibliotecas, frameworks) de terceiros constituem fornecedores implícitos de tecnologia
- **Solução técnica:** SBOM (Software Bill of Materials) identifica dependências e respetivos fornecedores
- **Característica:** Fornecedores implícitos — os autores de componentes frequentemente desconhecem que integram a cadeia de fornecimento
- **Gestão operacional:** SCA contínuo (análise de vulnerabilidades), gestão de atualizações de segurança, rastreamento de licenças
- **Pré-requisito DORA:** Sem SBOM, a organização não consegue identificar fornecedores de software

**Categoria 2: Fornecedores Contratuais ([Cap. 14](/sbd-toe/sbd-manual/governanca-contratacao/intro) - Governance)**
- Entidades contratadas formalmente: contractors, outsourcing, prestadores de serviços
- **Característica:** Fornecedores explícitos com contratos e responsabilidades formalmente documentadas
- Ciclo de vida estruturado: preparação → onboarding → monitorização → offboarding
- User Stories US-15 a US-20: Processos de gestão de contractors/fornecedores

**Artefactos de suporte (Cap. 14):**
- Template de validação pré-acesso de contractors
- Guia de preparação técnica de sandbox
- Checklist de offboarding seguro

**Conformidade DORA (Art. 26–28):**
- Ambas as categorias exigem inventário e supervisão — não existe opcionalidade
- SBOM alimenta o inventário de risco técnico de componentes
- Fornecedores contratuais alimentam o inventário de risco organizacional
- **Lacuna intencional:** O SbD-ToE não inclui templates ITS nem fórmulas de análise de concentração DORA. A conformidade requer: manutenção de SBOM atualizado ([Cap. 05](/sbd-toe/sbd-manual/dependencias-sbom-sca/intro)), inventário formal de contractors ([Cap. 14](/sbd-toe/sbd-manual/governanca-contratacao/intro)) e templates contratuais com cláusulas de segurança alinhadas com DORA.

---

### Partilha de Informação sobre Ameaças (Artigo 16 DORA)

O Artigo 16 DORA exige mecanismos de recolha e disseminação de informação sobre incidentes e ameaças TIC, promovendo a cooperação entre entidades financeiras e autoridades.

**Cobertura SbD-ToE:**
- **[Cap. 12](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro):** Integração de indicadores de threat intelligence em processos de monitorização
- **[Cap. 14](/sbd-toe/sbd-manual/governanca-contratacao/intro):** Estruturas de governança e responsabilidades de reporte

**Lacuna intencional:** O SbD-ToE não prescreve acordos institucionais específicos nem processos de notificação ao supervisor. A integração de feeds de threat intelligence (ex: STIX/TAXII, MISP) e a formalização de canais de partilha com autoridades competentes devem ser estabelecidos em conformidade com orientações setoriais e requisitos regulatórios DORA.

---

### Gestão de Exceções e Desvios (Artigos 5, 18, 19–20, 26–28 DORA)

DORA não menciona explicitamente "exceções", porém em **conformidade regulatória**, exceções constituem **desvios formais de requisitos** que exigem:
- Aprovação documentada com autoridade formal designada
- Justificação técnica e de negócio
- Período de validade definido
- Plano de remediação estruturado

**Cobertura SbD-ToE (Parcial):**
- **[Cap. 10](/sbd-toe/sbd-manual/testes-seguranca/intro):** Gestão de exceções em testes de segurança com aprovação formal (ex: vulnerabilidades conhecidas com justificação)
- **[Cap. 08](/sbd-toe/sbd-manual/iac-infraestrutura/intro):** Rastreamento de exceções de configuração em IaC
- **[Cap. 14](/sbd-toe/sbd-manual/governanca-contratacao/intro):** Estrutura RACI para aprovações (implicitamente define autoridade para exceções)

**Lacuna intencional:** O SbD-ToE não define:
- Níveis de autoridade para aprovação de exceções em contexto DORA (board, CISO, compliance officer)
- Categorias de exceções admissíveis segundo DORA (algumas podem ser inadmissíveis)
- Templates de reporte de exceções ao regulador
- SLA de remediação por tipo de exceção

**Conformidade DORA:**
- Estabelecer política formal de exceções com estrutura de governança e rastreabilidade
- Documentar cada exceção: justificação, aprovador, data de expiração, plano de correção
- Manter trilho auditado de exceções (passível de inspeção regulatória)
- Validar admissibilidade com supervisor (algumas exceções podem violar Art. 5)

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
- Decisões de aceitação de risco (exceções) exigem aprovação documentada de autoridade formal
- O regulador interpreta conhecimento prévio de vulnerabilidade explorada sem aprovação documentada como negligência de supervisão
- Exceções requerem reavaliação periódica — a ausência de reavaliação constitui aprovação tácita indefinida, configurando falha de supervisão

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
| **[Cap. 01](/sbd-toe/sbd-manual/classificacao-aplicacoes/intro)** | Classificação L1–L3 (base para criticidade de exceções) | ✅ Modelo E+D+I claro; criterios de L1/L2/L3 definidos |
| **[Cap. 01](/sbd-toe/sbd-manual/classificacao-aplicacoes/intro), addon 03** | Critérios de aceitação de risco (limiares por nível) | ✅ L1≤9, L2≤6, L3≤4; requer validação por 2+ perfis em L2/L3 |
| **[Cap. 02](/sbd-toe/sbd-manual/requisitos-seguranca/intro), addon 08** | Gestão de exceções a requisitos (processo formal) | ✅ Identificação, justificação, avaliação, compensação, revisão periódica |
| **[Cap. 04](/sbd-toe/sbd-manual/arquitetura-segura/intro), addon 03** | Exceções a requisitos arquiteturais | ✅ Modelo de registo com horizonte temporal; responsáveis designados |
| **[Cap. 05](/sbd-toe/sbd-manual/dependencias-sbom-sca/intro), addon 09** | Exceções a CVEs (formalização, owner, TTL, impacto) | ✅ Processo completo: identificação → justificação → aceitação → TTL → revalidação |
| **[Cap. 10](/sbd-toe/sbd-manual/testes-seguranca/intro)** | Exceções a testes de segurança (com aprovação formal) | ✅ Menção explícita: "exceções formais aprovadas" |
| **[Cap. 14](/sbd-toe/sbd-manual/governanca-contratacao/intro)** | Governança de exceções (RACI, approval flow, auditoria) | ⚠️ **PARCIAL** — User Stories definem roles, mas não explicam implicações DORA |
| **[Cap. 13](/sbd-toe/sbd-manual/formacao-onboarding/intro)** | Waivers e exceções temporárias (durante formação) | ✅ "Justificação formal documentada, aprovada por AppSec/GRC/gestão" |

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

**Como manifesta:** Organização sem política formal aceita exceção inadmissível; auditoria regulatória identifica achado crítico.

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

Adicionar ao [Cap. 14](/sbd-toe/sbd-manual/governanca-contratacao/intro) (Governança) uma secção dedicada:

```markdown
## Compatibilidade DORA: Exceções Inaceitáveis vs. Aceitáveis

[Tabela acima com categorias A–D]

### Implicações Regulatórias

Se um incidente ocorre e há exceção relacionada:
- **Com aprovação documentada** → Demostra supervisão; mitigação regulatória
- **Sem aprovação documentada** → Evidência de negligência; penalidade potencial

### Processo de Escalada ao Regulador

[Template de como reportar exceção ao supervisor em contexto de incidente]
```

---

**3. Integrar em User Stories do [Cap. 14](/sbd-toe/sbd-manual/governanca-contratacao/intro)**

Expandir `US-15 (Processo formal de exceções)` com:
- Approval Matrix DORA-compatível
- Categorias de inaceitabilidade
- Template de reporte ao regulador

---

#### Resumo: Por que Ausência de Gestão Formal = Incoerência DORA

| Aspecto | Sem Gestão Formal | Com Gestão SbD-ToE + DORA Mapping |
|--------|-------------------|----------------------------------|
| **Descoberta regulatória** | Ausência de documentação de exceções ou localização desconhecida ❌ | Processo formal em sistema GRC com aprovação board-level ✅ |
| **Trilho auditado** | Exceções em canais informais (Slack/Teams/email) ❌ | Exceções em ferramenta GRC com audit trail completo ✅ |
| **Supervisão do board** | Board desconhece exceções críticas ❌ | Board recebe reporte trimestral de exceções L3 ✅ |
| **Resposta a incidentes** | Desconhecimento de vulnerabilidade explorada ❌ | Vulnerabilidade registada em exceção aprovada com plano de correção; escalada segundo protocolo ✅ |
| **Achados auditoria** | Achado crítico: falha de governance ❌ | Achado menor: oportunidades de melhoria operacional ✅ |

---

### Conformidade Prática

**Alinhamento SbD-ToE com DORA:**
1. ✅ Aplicar processo formal de exceções do SbD-ToE ([Cap. 14](/sbd-toe/sbd-manual/governanca-contratacao/intro), [Cap. 02](/sbd-toe/sbd-manual/requisitos-seguranca/intro) addon 08, [Cap. 05](/sbd-toe/sbd-manual/dependencias-sbom-sca/intro) addon 09)
2. ✅ Mapear níveis de criticidade a aprovadores DORA-compatíveis (L1→AppSec, L2→CISO, L3→Board/CRO)
3. ✅ Definir categorias de inaceitabilidade (política organizacional)
4. ✅ Implementar rastreamento centralizado com audit trail (ferramenta GRC)
5. ✅ Estabelecer reporte trimestral a estruturas de governance (exigência DORA Art. 5)
6. ✅ Definir protocolo de escalada ao regulador em contexto de incidente (Art. 18)

---

## CONCLUSÃO DO CROSS-CHECK

O **SbD-ToE cobre o núcleo técnico da DORA**. As lacunas observadas não constituem falhas do modelo, mas **abstenções deliberadas** para preservar universalidade e aplicabilidade em contextos organizacionais diversos.

**Requisitos para conformidade plena:**
- Mapeamento de políticas SbD-ToE a aprovações formais de órgão de gestão
- Configuração de campos de incidentes segundo RTS/ITS DORA
- Extensão de inventários com dados regulatórios específicos
- Cálculo de métricas DORA de concentração de fornecedores
- Formalização de acordos de partilha de informação sobre ameaças

---

## Referências

- SbD-ToE Manual (Capítulos 01–14)
- Regulamento DORA (UE 2022/2554)
- NIST SP 800-53, OWASP SAMM, BSIMM, SSDF
- [Cap. 14](/sbd-toe/sbd-manual/governanca-contratacao/intro) SbD-ToE: User Stories US-15 a US-20 (fornecedores/contractors)

---

**Versão:** 1.0  
**Data:** Novembro 2025  
**Próxima revisão:** Junho 2026
