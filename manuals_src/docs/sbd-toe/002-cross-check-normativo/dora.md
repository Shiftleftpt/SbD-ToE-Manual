---
id: dora
title: DORA - Cross-Check Normativo
description: Análise de como o SbD-ToE cobre os requisitos técnicos do Regulamento DORA (UE 2022/2554)
tags: [cross-check, dora, regulamentacao, ict-risk, resiliencia, finanças]
sidebar_position: 1
---

# DORA: Cross-Check Normativo

> **Para o playbook de implementação:** Ver `sbd-toe-4-dora-playbook.md`
> 
> **Para exemplos práticos:** Ver pasta `exemplo-playbook/`

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
