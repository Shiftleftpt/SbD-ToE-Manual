---
id: intro
title: GDPR - Cross-Check Normativo
description: Como o SbD-ToE cobre requisitos técnicos do RGPD (UE 2016/679)
tags: [cross-check, gdpr, privacidade, protecao-dados, art32, privacy-by-design]
sidebar_position: 7
---

# GDPR: Cross-Check Normativo

> Para implementação prática, consulte o [Playbook SbD-ToE 4 GDPR](/sbd-toe/cross-check-normativo/sbd-toe-4-gdpr-playbook).
>
> Para padrões aplicacionais universais, ver capítulos base do SbD-ToE (01–14).

## Âmbito

O **Regulamento Geral sobre a Proteção de Dados (RGPD/GDPR)** - **Regulamento (UE) 2016/679** (CELEX: [32016R0679](https://eur-lex.europa.eu/legal-content/PT/TXT/?uri=CELEX:32016R0679)) - estabelece princípios e obrigações para o tratamento de dados pessoais. Este cross‑check foca a **dimensão técnica** alinhada ao SbD-ToE (segurança e engineering), reconhecendo que várias obrigações são **jurídico‑organizacionais** (base legal, direitos dos titulares, transferências internacionais).

Sugere-se usar o SbD-ToE como núcleo técnico para os artigos que exigem medidas de segurança, privacidade‑by‑design e gestão de incidentes, articulando com jurídico/GRC para o restante.

---

## PARTE I: ANÁLISE NORMATIVA (GDPR → SbD-ToE)

### Princípios (Art. 5)
Exigem: minimização, limitação de finalidades, exatidão, limitação de conservação, integridade e confidencialidade, responsabilização.

Cobertura SbD-ToE:
- Cap. 01: Classificação e identificação de dados por criticidade (apoia minimização/retensão)
- Cap. 02: Requisitos de segurança (confidencialidade, integridade, disponibilidade)
- Cap. 04: Arquitetura segura (segregação, encriptação, logging proporcional)
- Cap. 11: Validação antes de produção (confirmações de requisitos)

Lacuna intencional: Definição de bases legais, políticas de conservação e finalidades → fora do âmbito técnico; tratar em governança/DPO.

---

### Privacy by Design/Default (Art. 25)
Exige que a privacidade esteja incorporada no design e que as configurações por defeito sejam as mais protetoras.

Cobertura SbD-ToE:
- Cap. 04: Padrões arquiteturais seguros (pseudonimização, segmentação)
- Cap. 06–07: Pipelines com gates para evitar exposições (secrets, dados excessivos)
- Cap. 11: Checklists pré‑deploy (parâmetros de privacidade por defeito)

Lacuna intencional: Catálogo de padrões de privacidade (e.g., LINDDUN) não incluído por defeito. Ação: Adicionar addon de Privacy Threat Modeling.

---

### Registos de Atividades (Art. 30)
Exige ROPA (Record of Processing Activities).

Cobertura SbD-ToE (parcial):
- Cap. 14: Governança e contratação (pode alojar o processo ROPA)
- Cap. 01: Inventário de aplicações e dados apoia ROPA

Lacuna intencional: O SbD-ToE não fornece modelo ROPA. Ação: Manter ROPA em ferramenta GRC/Jurídico e referenciar IDs de apps SbD-ToE.

---

### Segurança do Tratamento (Art. 32)
Exige medidas técnicas e organizativas adequadas: pseudonimização, cifragem, resiliência, testes periódicos da eficácia.

Cobertura SbD-ToE:
- Cap. 02: Requisitos mínimos por nível (inclui cifragem, IAM, hardening)
- Cap. 04: Arquitetura (segregação, gestão de chaves)
- Cap. 05: Gestão de vulnerabilidades e dependências (SBOM/SCA)
- Cap. 10: Testes de segurança e avaliação contínua
- Cap. 12: Monitorização, continuidade e exercícios

Lacuna intencional: Critérios legais de “adequação” e análise de risco contextual → integrar com matriz de risco jurídico.

---

### Notificação de Violação (Art. 33/34)
Exige notificar a autoridade competente em até 72h (Art. 33) e, quando aplicável, comunicar aos titulares (Art. 34).

Cobertura SbD-ToE:
- Cap. 12: Deteção, classificação e resposta a incidentes; runbooks
- Cap. 14: RACI para decisões e comunicações

Lacuna intencional: Templates formais de notificação e critérios legais de comunicação aos titulares → tratadas por Jurídico/DPO; integrar campos no runbook.

---

### DPIA - Avaliação de Impacto (Art. 35)
Exige DPIA quando o tratamento é suscetível de alto risco.

Cobertura SbD-ToE (parcial):
- Cap. 03: Threat Modeling (pode servir de base técnica)
- Cap. 04: Medidas de mitigação técnicas

Lacuna intencional: Metodologia DPIA completa (inclui análise de risco para titulares, consulta ao DPO/autoridade). Ação: Integrar artefactos do TM no relatório DPIA; adicionar add-on de Privacy TM (LINDDUN) se necessário.

---

### Subcontratantes (Art. 28) e Contratos
Exige contratos com processadores com cláusulas de proteção de dados.

Cobertura SbD-ToE:
- Cap. 14: Ciclo de vida de fornecedores/contractors e cláusulas de segurança
- Cap. 05: Transparência de componentes (SBOM) e risco de terceiros

Lacuna intencional: Cláusulas específicas de proteção de dados (SCCs, anexos de processamento) → Jurídico/DPO.

---

## PARTE II: Convergências/Interações

- Incidentes com dados pessoais podem requerer dupla notificação: RGPD (72h) + regimes setoriais (p.ex., NIS2/DORA). Sugere-se runbook único com bifurcação de reporte.
- Medidas Art. 32 complementam controlos NIS2/DORA (mesma base técnica; evidência reaproveitável).

---

## Lacunas Intencionais (Resumo)

| Área | Porquê fica fora do SbD-ToE | Ação Recomendada |
|------|------------------------------|------------------|
| Base legal, finalidades, direitos | Matéria jurídica | Processo com DPO; registo em GRC |
| ROPA (Art. 30) | Administrativo | Ferramenta GRC; referenciar IDs de apps |
| DPIA completo | Metodologia legal-organizacional | Template jurídico; incorporar anexos técnicos |
| Transfers internacionais | Legal (Cláusulas, TIAs) | Jurídico; medidas técnicas complementares |
| Notificações formais | Legal/comunicação | Templates do DPO; integração com runbook técnico |

---

## Métrica Simples (Autoavaliação)

Responda SIM:
1. As apps que tratam dados pessoais estão classificadas e têm requisitos de Art. 32 implementados? ✓
2. Privacy by default configurada (logs mínimos, retenção limitada, cifragem por defeito)? ✓
3. Existe processo de DPIA com anexos técnicos (TM, controlos) quando aplicável? ✓
4. Runbook de incidente com cronómetro 72h ativo e campos RGPD? ✓
5. Processors: contratos com cláusulas técnicas e segurança verificada? ✓

≥4/5 → Boa cobertura técnica. `<`3 → Priorizar Art. 32, PbD e incidentes 72h.

---

## Referências

- **RGPD/GDPR**: Regulamento (UE) 2016/679 (CELEX: [32016R0679](https://eur-lex.europa.eu/legal-content/PT/TXT/?uri=CELEX:32016R0679))
- ENISA - Guidelines on Security of Personal Data Processing
- EDPB - Guidelines (DPIA, Breach Notification)
- SbD-ToE Capítulos 01–14

**Versão:** 1.0  
**Data:** Novembro 2025  
**Próxima revisão:** Maio 2026
