---
id: playbook
title: "SbD-ToE 4 CRA: Playbook de Implementação"
description: Roadmap prático para alinhar o programa SbD-ToE aos requisitos técnicos do Cyber Resilience Act
tags: [playbook, cra, implementacao, roadmap, produtos-digitais]
sidebar_position: 6
---

# SbD-ToE 4 CRA: Playbook de Implementação

## Visão Geral

Objetivo: Transformar requisitos CRA em ações concretas usando controlos existentes do SbD-ToE.

Princípio: Reutilizar > Inventar. Muitas capacidades (SBOM, patching, testes) já existem — ajusta-se formato, rigor e evidência.

> 📚 **Recursos de Suporte:** Para templates práticos e exemplos de implementação, consultar [Exemplo-Playbook](/sbd-toe/cross-check-normativo/exemplo-playbook/indice) com toolchains, KPIs, RACI e processos de vulnerability handling reutilizáveis.

## Mapa Rápido CRA → SbD-ToE

| Área CRA | SbD-ToE | Ação | Evidência |
|----------|---------|------|----------|
| Ciclo de Vida Seguro | [Cap. 02](/sbd-toe/sbd-manual/requisitos-seguranca/intro), [Cap. 06](/sbd-toe/sbd-manual/desenvolvimento-seguro/intro), [Cap. 07](/sbd-toe/sbd-manual/cicd-seguro/intro), [Cap. 11](/sbd-toe/sbd-manual/deploy-seguro/intro) | Política ciclo de vida + gates | Política aprovada; pipeline YAML |
| Vulnerability Handling | [Cap. 05](/sbd-toe/sbd-manual/dependencias-sbom-sca/intro), [Cap. 10](/sbd-toe/sbd-manual/testes-seguranca/intro), [Cap. 12](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro) | Processo triagem + SLA | Registos triagem; métricas SLA |
| SBOM | [Cap. 05](/sbd-toe/sbd-manual/dependencias-sbom-sca/intro) | Geração contínua + export | Ficheiros CycloneDX por release |
| Patching Rápido | [Cap. 05](/sbd-toe/sbd-manual/dependencias-sbom-sca/intro), [Cap. 07](/sbd-toe/sbd-manual/cicd-seguro/intro) | Workflow patch automático | Pull requests patch + tempos |
| Reporte Exploração | [Cap. 12](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro) | Runbook exploração ativa | Runbook + JSON exemplo |
| Documentação Segurança | [Cap. 04](/sbd-toe/sbd-manual/arquitetura-segura/intro), [Cap. 11](/sbd-toe/sbd-manual/deploy-seguro/intro) | Guia de segurança do produto | PDF/Markdown guia publicado |
| Exceções | [Cap. 02](/sbd-toe/sbd-manual/requisitos-seguranca/intro) addon 08, [Cap. 14](/sbd-toe/sbd-manual/governanca-contratacao/intro) | Política exceções CRA | Registos exceções + aprovadores |
| Cadeia Fornecimento | [Cap. 05](/sbd-toe/sbd-manual/dependencias-sbom-sca/intro), [Cap. 09](/sbd-toe/sbd-manual/containers-runtime/intro), [Cap. 14](/sbd-toe/sbd-manual/governanca-contratacao/intro) | Checklist supply chain físico | Checklist preenchida |

---

## Fases de Implementação (≈ 6–9 meses)

### Fase 1 (M0–M1): Fundamentos & Governance
1. Designar Owner CRA (GRC + AppSec)  
2. Criar Política "Segurança de Produto & CRA" (aprovada por gestão)  
3. Mapear roles SbD-ToE → papéis CRA (fabricante, importador — se aplicável)  
4. Definir matriz criticidade produto (base L1–L3 adaptada)  
**Evidências:** Ata aprovação; matriz criticidade; política versão 1.0

### Fase 2 (M1–M2): SBOM & Inventário
1. Ativar geração automática SBOM (build pipeline)  
2. Validar cobertura (≥95% componentes listados)  
3. Criar export sanitized CycloneDX  
4. Repositório "SBOM Releases" (controlado, versionado)  
**Evidências:** SBOM v1; relatório cobertura; script export

### Fase 3 (M2–M3): Vulnerability Handling & SLAs
1. Definir severidade (Critical/High/Medium/Low)  
2. Estabelecer SLA patch (Critical ≤15d, High ≤30d, Medium ≤90d)  
3. Automatizar criação de issue para CVE crítico  
4. Dashboard patch compliance  
**Evidências:** Política SLA; dashboard inicial; issues exemplo

### Fase 4 (M3–M4): Testes & Gate Release
1. Integrar SAST/DAST/fuzzing pipeline  
2. Criar gate "no-critical-known" (release bloqueada)  
3. Processo exceção crítica (board-level)  
4. Template relatório qualidade release  
**Evidências:** Logs pipeline; configuração gate; relatório release #1

### Fase 5 (M4–M5): Disclosure & Comunicação Externa
1. Publicar security.txt + chave PGP  
2. Página "Vulnerability Disclosure Policy"  
3. Runbook triagem reporte externo  
4. Canal email/portal dedicado  
**Evidências:** Página pública; registo primeiro teste reporte

### Fase 6 (M5–M6): Reporte de Exploração Ativa
1. Definir critérios de "explorada ativamente" (IOC, telemetria confirmada)  
2. Criar script export JSON incidente + SBOM componente afetado  
3. Runbook notificação autoridade (ENISA/ponto nacional)  
4. Simulação exercício interno  
**Evidências:** Script; runbook; relatório exercício

### Fase 7 (M6–M7): Documentação de Segurança do Produto
1. Escrever Guia Segurança (instalação segura, atualização, contacto)  
2. Validar com AppSec + engenharia  
3. Publicar versão 1.0 (Markdown/PDF)  
4. Processo atualização por release  
**Evidências:** Guia v1; diff v1→v2 (exemplo)

### Fase 8 (M7–M8): Cadeia Fornecimento Expandida
1. Inventariar firmware/hardware (se aplicável)  
2. Checklist integridade (hash, assinatura, origem)  
3. Processo atualização segura (secure channel)  
4. Métrica cobertura supply chain (≥90%)  
**Evidências:** Checklist preenchida; métrica cobertura

### Fase 9 (M8–M9): Métricas & Melhoria Contínua
1. Métricas: MTTP (Mean Time To Patch), % SLA cumprido, vulns abertas por severidade  
2. Reunião retrospectiva trimestral  
3. Plano melhoria (top 3 blockers)  
4. Ajuste políticas conforme revisão legal/regulatória  
**Evidências:** Dashboard; ata retrospectiva; plano melhoria

---

## Checklists

### Checklist SBOM
- [ ] Pipeline gera SBOM automaticamente
- [ ] Formato CycloneDX/SPDX validado
- [ ] Export sanitized criado
- [ ] Versão SBOM associada a release
- [ ] Cobertura ≥95% componentes
- [ ] Processo atualização documentado

### Checklist Vulnerability Handling
- [ ] Severidade definida (Critical/High/Medium/Low)
- [ ] SLA patch documentado
- [ ] Issues automáticas para críticos
- [ ] Dashboard patch compliance ativo
- [ ] Política exceções CRA publicada
- [ ] Exceções críticas aprovadas board

### Checklist Release Gate
- [ ] SAST integrado
- [ ] DAST integrado
- [ ] Fuzzing (se aplicável)
- [ ] Gate bloqueia CVE crítico conhecido
- [ ] Relatório qualidade release arquivado
- [ ] Processo override exceção formal

### Checklist Disclosure
- [ ] security.txt publicado
- [ ] Chave PGP acessível
- [ ] Página política disclosure publicada
- [ ] Canal reporte funcional (email/portal)
- [ ] Runbook triagem interna
- [ ] Tempo resposta médio `<`5 dias úteis

### Checklist Reporte Exploração
- [ ] Critérios "explorada ativamente" definidos
- [ ] Script export JSON pronto
- [ ] Runbook notificação autoridade
- [ ] Simulação concluída
- [ ] Evidência testes arquivada

### Checklist Documentação Segurança
- [ ] Guia instalação segura
- [ ] Guia atualização + rollback
- [ ] Contacto segurança (security@)
- [ ] Recomendações configuração endurecida
- [ ] Secção gestão de vulnerabilidades
- [ ] Versão e data

### Checklist Supply Chain Física (se aplicável)
- [ ] Lista firmware/hardware
- [ ] Hashes/assinaturas verificados
- [ ] Canal atualização seguro
- [ ] Processo de validação integridade
- [ ] Registos auditáveis

---

## Métricas-Chave
| Métrica | Definição | Objetivo Inicial |
|---------|-----------|------------------|
| MTTP Crítico | Tempo médio até patch crítico | ≤15 dias |
| % SLA Cumprido | (Vulns patch dentro SLA) / total | ≥90% |
| Cobertura SBOM | % componentes identificados | ≥95% |
| Tempo Médio Resposta Disclosure | Receção → primeira resposta | ≤5 dias úteis |
| Gate Efetividade | Releases bloqueadas por CVE crítico | 100% bloqueadas |
| Exceções Críticas Ativas | Nº exceções críticas abertas | Tendência decrescente |

---

## Artefactos a Manter (Data Room)
| Artefacto | Tipo | Frequência Atualização |
|-----------|------|------------------------|
| Política Segurança Produto & CRA | Documento | Anual / quando requisito muda |
| SBOM Releases | Ficheiros | Cada release major/minor |
| Dashboard Vulnerabilidades | Painel | Contínuo (live) |
| Relatórios Qualidade Release | Documento | Cada release |
| Guia Segurança Produto | Documento | Cada release major |
| Runbook Exploração Ativa | Documento | Anual / exercícios |
| Registos Disclosure | Tickets / Issues | Contínuo |
| Checklist Supply Chain | Documento | Trimestral |

---

## Exceções (Política Resumida)
Categorias:
- Inaceitáveis: RCE crítico, bypass autenticação, exposure credenciais em claro
- Aceitáveis (TTL curto ≤30d): Crítico sem patch disponível + compensação robusta
- Aceitáveis (TTL médio ≤90d): High com mitigação parcial

Registos: ID | Vulnerabilidade | Severidade | Justificação | Aprovador | TTL | Mitigação | Data Revisão

Escalação: Crítico → Board; High → CISO/AppSec; Medium/Low → AppSec.

---

## Próximos Passos Depois da Fase 9
1. Avaliação formal conformidade (legal + técnico)  
2. Preparar documentação para eventual auditoria/regulador  
3. Integração com outras normas (ex: DORA, NIS2) — evitar duplicação  
4. Refinar métricas (MTTP por componente, densidade vulnerabilidades)  
5. Automatizar geração relatório trimestral CRA

---

## Recursos Práticos de Implementação

Para suporte concreto na implementação deste playbook, consultar os seguintes exemplos reutilizáveis:

- 🛠️ **[Opções de Toolchain](../exemplo-playbook/exemplo-toolchain-options)** - Comparação de ferramentas SCA, SBOM e vulnerability management
- 📊 **[KPIs e Targets](../exemplo-playbook/exemplo-kpis-targets)** - Métricas de patching e SBOM coverage adaptáveis ao CRA
- 👥 **[RACI e Governance](../exemplo-playbook/exemplo-raci-governance)** - Matrizes de responsabilidades para vulnerability handling
- 📝 **[Relatório de Incidentes](../exemplo-playbook/exemplo-relatorio-incidentes)** - Template adaptável para reporte de exploração ativa (CRA)

Estes recursos demonstram implementações práticas das abstenções deliberadas do SbD-ToE.

---

## Referências
- [Análise normativa CRA](intro)
- SbD-ToE Capítulos 01–14
- ENISA: Vulnerability Disclosure Guidelines
- ISO/IEC 29147 & 30111
- CycloneDX, SPDX

**Versão:** 1.0  
**Data:** Novembro 2025  
**Nota:** Este playbook complementa a análise normativa CRA com abordagem sequencial prática
