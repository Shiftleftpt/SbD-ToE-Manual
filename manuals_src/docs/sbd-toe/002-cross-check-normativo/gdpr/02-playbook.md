---
id: playbook
title: "SbD-ToE 4 GDPR: Playbook de Implementação"
description: Roadmap prático para alinhar o SbD-ToE aos requisitos técnicos do RGPD
tags: [playbook, gdpr, implementacao, privacy-by-design, art32]
sidebar_position: 8
---

# SbD-ToE 4 GDPR: Playbook de Implementação

## Visão Geral

Objetivo: operacionalizar GDPR Art. 25/30/32/33–34/35 com base nas capacidades técnicas do SbD-ToE e integrar com jurídico/DPO.

Estrutura: Requisitos → Ação → Evidência. Reutilizar controlos NIS2/DORA sempre que possível.

> 📚 **Recursos de Suporte:** Para templates práticos e exemplos de implementação, consultar [Exemplo-Playbook](/sbd-toe/cross-check-normativo/exemplo-playbook/indice) com toolchains de cifragem, KPIs de privacy e processos de incident response reutilizáveis.

---

## Mapa Rápido: GDPR Art. → SbD-ToE

| Artigo GDPR | Requisito | Capítulo SbD-ToE | Ação Principal |
|-------------|-----------|------------------|----------------|
| 5 | Princípios | [Cap. 01](/sbd-toe/sbd-manual/classificacao-aplicacoes/intro), [Cap. 02](/sbd-toe/sbd-manual/requisitos-seguranca/intro), [Cap. 04](/sbd-toe/sbd-manual/arquitetura-segura/intro), [Cap. 11](/sbd-toe/sbd-manual/deploy-seguro/intro) | Minimização, retenção, segurança |
| 25 | Privacy by design/default | [Cap. 04](/sbd-toe/sbd-manual/arquitetura-segura/intro), [Cap. 06](/sbd-toe/sbd-manual/desenvolvimento-seguro/intro)–[Cap. 07](/sbd-toe/sbd-manual/cicd-seguro/intro), [Cap. 11](/sbd-toe/sbd-manual/deploy-seguro/intro) | Configurações seguras por defeito |
| 30 | ROPA | [Cap. 01](/sbd-toe/sbd-manual/classificacao-aplicacoes/intro), [Cap. 14](/sbd-toe/sbd-manual/governanca-contratacao/intro) | Inventário apps/dados + registo GRC |
| 32 | Segurança do tratamento | [Cap. 02](/sbd-toe/sbd-manual/requisitos-seguranca/intro), [Cap. 04](/sbd-toe/sbd-manual/arquitetura-segura/intro), [Cap. 05](/sbd-toe/sbd-manual/dependencias-sbom-sca/intro), [Cap. 10](/sbd-toe/sbd-manual/testes-seguranca/intro), [Cap. 12](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro) | Cifragem, IAM, testes, resiliência |
| 33/34 | Violação de dados | [Cap. 12](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro), [Cap. 14](/sbd-toe/sbd-manual/governanca-contratacao/intro) | Runbook 72h + comunicação |
| 35 | DPIA | [Cap. 03](/sbd-toe/sbd-manual/threat-modeling/intro), [Cap. 04](/sbd-toe/sbd-manual/arquitetura-segura/intro) | TM + anexos técnicos na DPIA |

---

## Fases de Implementação (≈ 4–6 meses)

### Fase 1 (M0–M1): Governação e Enquadramento
1. Nomear DPO (se aplicável) e alinhar RACI ([Cap. 14](/sbd-toe/sbd-manual/governanca-contratacao/intro))  
2. Política "Privacidade by Design & por Defeito" aprovada  
3. Definir classificação de dados pessoais por aplicação  
**Evidências:** Ata aprovação; RACI; matriz dados/aplicações

### Fase 2 (M1–M2): Inventário & ROPA
1. Atualizar inventário SbD-ToE (apps, dados, finalidades em alto nível)  
2. Registar ROPA em ferramenta GRC (campos Art. 30)  
3. Ligar IDs de apps SbD-ToE ao ROPA  
**Evidências:** ROPA export; mapeamento IDs

### Fase 3 (M2–M3): Privacy by Design/Default (Art. 25)
1. Catálogo de padrões: pseudonimização, data minimization, retenção, logging proporcional  
2. Configs por defeito: coleta mínima, encryption at rest/in transit  
3. Gate de pipeline: bloqueio se coleta excessiva (linting de schemas, por ex.)  
**Evidências:** Catálogo PbD; pipelines; exemplos de bloqueio

### Fase 4 (M2–M3): Segurança do Tratamento (Art. 32)
1. Cifragem: TLS 1.2+; at rest com gestão de chaves  
2. IAM: MFA, least privilege, revisão periódica de acessos  
3. Testes: SAST/DAST/fuzzing; validação de eficácia  
4. Resiliência: backups, DR testado, monitorização  
**Evidências:** Registos de chaves, relatórios de testes, logs DR

### Fase 5 (M3–M4): DPIA (Art. 35)
1. Critérios de gatilho DPIA definidos  
2. Reutilizar Threat Modeling ([Cap. 03](/sbd-toe/sbd-manual/threat-modeling/intro)) como anexo técnico  
3. Adicionar Privacy TM (LINDDUN) quando alto risco  
4. Aprovação DPO e registo  
**Evidências:** DPIA #1; anexos TM; aprovação DPO

### Fase 6 (M3–M4): Processors (Art. 28)
1. Checklist de segurança para processadores  
2. Cláusulas técnicas padrão (encriptação, logs, sub-processors)  
3. Monitorização e revisão anual  
**Evidências:** Checklist; contratos; relatórios de revisão

### Fase 7 (M4–M5): Incidentes e Notificação 72h (Art. 33/34)
1. Runbook com cronómetro 72h e campos mínimos (o quê, quando, dados, medidas)  
2. Critérios de risco para comunicação a titulares  
3. Exercício anual de simulação  
**Evidências:** Runbook; registos exercício; relatório pós‑ação

### Fase 8 (M5–M6): Retenção & Eliminação Segura
1. Tabelas de retenção formalizadas (com Jurídico)  
2. Jobs de eliminação/pseudonimização agendada  
3. Provas de execução (logs, relatórios)  
**Evidências:** Tabela retenções; logs eliminação; auditorias

---

## Checklists

### PbD/PbDf
- [ ] Catálogo de padrões de privacidade publicado
- [ ] Defaults seguros aplicados (coleta mínima, cifragem)
- [ ] Gate de pipeline para schemas/dados
- [ ] Revisão periódica de configurações

### Art. 32
- [ ] TLS 1.2+/1.3 e at rest encryption
- [ ] Gestão de chaves com rotação
- [ ] MFA e revisão de privilégios
- [ ] SAST/DAST/fuzzing integrados
- [ ] Backups testados; DR exercitado

### DPIA
- [ ] Critérios de gatilho definidos
- [ ] Threat Modeling anexado
- [ ] Privacy TM (se alto risco)
- [ ] Aprovação DPO

### Incidentes 72h
- [ ] Runbook com campos GDPR
- [ ] Cronómetro 72h visível
- [ ] Exercício anual concluído
- [ ] Templates de comunicação prontos

### Processors
- [ ] Checklist de segurança aplicada
- [ ] Cláusulas técnicas padrão
- [ ] Revisão anual e registos

### Retenção
- [ ] Tabela aprovada
- [ ] Jobs automáticos configurados
- [ ] Evidência de execução

---

## Métricas-Chave
| Métrica | Definição | Objetivo |
|---------|-----------|---------|
| % apps com Art. 32 completo | Apps com cifragem+IAM+testes | ≥95% |
| Tempo médio até notificação | Evento → submissão à autoridade | ≤60h |
| % DPIA no prazo | DPIAs concluídas dentro do SLA | ≥90% |
| Conformidade retenção | Execução jobs vs. plano | ≥95% |

---

## Artefactos a Manter
- Política PbD/PbDf
- ROPA export (GRC)
- Relatórios de testes e gates
- DPIAs com anexos técnicos
- Runbook 72h + registos exercício
- Tabelas de retenção + logs de eliminação
- Checklists/processors e contratos

---

## Notas
- Incidentes podem acionar também NIS2/DORA. Recomenda-se runbook único com canais de reporte diferenciados.
- LINDDUN é recomendado para Privacy TM; manter como add‑on do [Cap. 03](/sbd-toe/sbd-manual/threat-modeling/intro).

---

## Recursos Práticos de Implementação

Para suporte concreto na implementação deste playbook, consultar os seguintes exemplos reutilizáveis:

- 🛠️ **[Opções de Toolchain](../exemplo-playbook/exemplo-toolchain-options)** - Ferramentas de cifragem, anonimização e data minimization
- 📊 **[KPIs e Targets](../exemplo-playbook/exemplo-kpis-targets)** - Métricas de privacy e retenção de dados adaptáveis ao GDPR
- 👥 **[RACI e Governance](../exemplo-playbook/exemplo-raci-governance)** - Interface técnico/DPO e responsabilidades Art. 32
- 📝 **[Relatório de Incidentes](../exemplo-playbook/exemplo-relatorio-incidentes)** - Template adaptável para violação de dados (72h) Art. 33-34

Estes recursos demonstram implementações práticas alinhadas com GDPR.

---

## Referências
- [Análise normativa GDPR](intro)
- EDPB - Guidelines DPIA, Breach Notification
- ENISA - Security of Personal Data Processing
- SbD-ToE [Cap. 01](/sbd-toe/sbd-manual/classificacao-aplicacoes/intro)–[Cap. 14](/sbd-toe/sbd-manual/governanca-contratacao/intro)

**Versão:** 1.0  
**Data:** Novembro 2025  
**Nota:** Este playbook complementa a análise normativa GDPR com ações práticas
