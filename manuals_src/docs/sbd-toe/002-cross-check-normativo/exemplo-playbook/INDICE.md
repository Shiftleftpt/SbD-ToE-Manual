---
id: indice-exemplos-playbook
title: Índice de Exemplos do Playbook
description: Guia rápido aos ficheiros de suporte com exemplos práticos (reutilizáveis para todos os normativos)
tags: [playbook, exemplos, indice, dora, nis2, iso27001]
---

# Índice de Exemplos do Playbook

## 📚 Estrutura de Ficheiros

Esta pasta (`exemplo-playbook`) contém **ficheiros exemplares** que demonstram como implementar os princípios que o SbD-ToE prescreve.

**Importante:** 
- Estes são exemplos, não prescrições
- Cada organização deve adaptar ao seu contexto
- Exemplos são **reutilizáveis para múltiplos normativos** (DORA, NIS2, ISO 27001, etc.)

---

## 📖 Ficheiros Disponíveis

### 1. **README.md** (Este ficheiro)
Visão geral, estrutura e instruções de uso

---

### 2. **01-exemplo-toolchain-options.md**
**O que aborda:** Ferramentas para implementar princípios de IaC, logs, SCA/SAST

**Relacionado com (SbD-ToE):**
- Cap. 08 - IaC
- Cap. 12 - Operações e Logs

**Abstenção deliberada coberta:**
- ❌ O manual NÃO prescreve "Usar Terraform" ou "Usar Splunk"
- ✓ Exemplo: Como implementar "IaC" com Terraform, CloudFormation ou Helm
- ✓ Exemplo: Como centralizar logs com ELK, Datadog ou Azure Sentinel

**Quando usar:**
- Avaliando qual stack technológico
- Comparando opções de ferramentas
- Validando que escolha implementa princípios SbD-ToE

**Entregáveis:**
- Comparação 3 opções por dimensão (IaC, Logs, SCA, SAST, CI/CD)
- Exemplos de código
- Trilho de auditoria para cada opção

---

### 3. **02-exemplo-kpis-targets.md**
**O que aborda:** KPIs e targets para diferentes perfis organizacionais

**Relacionado com (SbD-ToE):**
- Cap. 12 - Métricas

**Abstenção deliberada coberta:**
- ❌ O manual NÃO prescreve "Target: Zero critical vulns"
- ✓ Exemplo: Fintech (pequena) - targets agressivos, timeline curta
- ✓ Exemplo: Banco (grande) - targets conservadores, timeline longa
- ✓ Exemplo: PME (distribuída) - targets pragmáticos

**Quando usar:**
- Definindo targets para sua organização
- Comunicando com executivos ("Por que não 100%?")
- Ajustando conforme maturidade

**Entregáveis:**
- KPI dashboards visuais (por cenário)
- Tabelas de targets (por dimensão)
- Processo de definição de targets

---

### 4. **03-exemplo-raci-governance.md**
**O que aborda:** RACI e estrutura de governança

**Relacionado com (SbD-ToE):**
- Cap. 14 - Governação

**Abstenção deliberada coberta:**
- ❌ O manual NÃO prescreve "CISO reporta a CTO" ou "7 reuniões/semana"
- ✓ Exemplo: Fintech (pequena) - RACI enxuta, reuniões quinzenais
- ✓ Exemplo: Banco (grande) - RACI estruturada, múltiplos níveis
- ✓ Exemplo: PME (distribuída) - RACI híbrida, comunicação remota

**Quando usar:**
- Desenhando estrutura de governança
- Definindo responsabilidades
- Estruturando comunicação/reuniões

**Entregáveis:**
- Organogramas (por cenário)
- Matrizes RACI (por atividade)
- Calendários de reuniões
- Procedimentos de aprovação

---

### 5. **04-exemplo-relatorio-incidentes.md**
**O que aborda:** Template de reporte de incidentes

**Relacionado com (SbD-ToE):**
- Cap. 12 - Incidentes

**Abstenção deliberada coberta:**
- ❌ O manual NÃO prescreve "Template ITS oficial DORA"
- ✓ Exemplo: Como estruturar reporte (o quê, quando, como, quem, impacto, ação)
- ✓ Exemplo: Campos para rastreabilidade

**Quando usar:**
- Configurando ferramenta de incidentes (Jira, ServiceNow, etc.)
- Alinhando equipa em definição de incidente
- Preparando para auditoria DORA

---

### 6. **05-exemplo-rto-rpo.md** *(próximo a criar)*
**O que aborda:** Definição de RTO/RPO por app

**Relacionado com (SbD-ToE):**
- Cap. 01 - Classificação de apps
- Cap. 08 - IaC e Continuidade

**Abstenção deliberada coberta:**
- ❌ O manual NÃO prescreve "RTO: <1h" ou "RPO: <15min"
- ✓ Exemplo: Como definir por app L1/L2/L3
- ✓ Exemplo: Como implementar (backups, replicas, failover)

**Quando usar:**
- Desenhando arquitetura de disponibilidade
- Comunicando criticidade interna

---

### 7. **06-exemplo-roadmap-adaptado.md** *(próximo a criar)*
**O que aborda:** Roadmaps adaptados a diferentes cenários

**Relacionado com (SbD-ToE):**
- Playbook DORA - Fases 0-5

**Abstenção deliberada coberta:**
- ❌ O manual NÃO prescreve "Fase 0 sempre 2 meses"
- ✓ Exemplo: Timeline curta (Fintech: urgência DORA)
- ✓ Exemplo: Timeline longa (Banco: complexidade + governance)
- ✓ Exemplo: Timeline pragmática (PME: recursos)

**Quando usar:**
- Planeando implementação
- Comunicando timeline executiva
- Adaptando ao contexto real

---

### 8. **07-exemplo-politica-seguranca.md** *(próximo a criar)*
**O que aborda:** Template de Política de Segurança

**Relacionado com (SbD-ToE):**
- Cap. 02 - Requisitos
- Cap. 14 - Governação

**Abstenção deliberada coberta:**
- ❌ O manual NÃO prescreve "Política de Segurança genérica"
- ✓ Exemplo: Estrutura, conteúdo mínimo, assinatura
- ✓ Exemplo: Referência a SbD-ToE e DORA

**Quando usar:**
- Redigindo política interno
- Validando conteúdo essencial
- Preparando para aprovação Board

---

### 9. **08-exemplo-contrato-fornecedor.md** *(próximo a criar)*
**O que aborda:** Cláusulas técnicas de segurança em contratos

**Relacionado com (SbD-ToE):**
- Cap. 14 - Ciclo de vida fornecedores
- Cap. 05 - Inventários

**Abstenção deliberada coberta:**
- ❌ O manual NÃO prescreve "Cláusulas jurídicas específicas"
- ✓ Exemplo: Requisitos técnicos (SbD compliance, formação, etc.)
- ✓ Exemplo: SLAs de resposta (incidentes, remediação, etc.)

**Quando usar:**
- Negociando com fornecedores
- Incluindo security requirements
- Alinhando com DORA Art. 26-28

---

## 🔍 Como Encontrar o que Procura

### "Preciso escolher ferramentas"
→ **01-exemplo-toolchain-options.md**

### "Como defino targets de segurança?"
→ **02-exemplo-kpis-targets.md**

### "Como estruturo governança?"
→ **03-exemplo-raci-governance.md**

### "Como reporto incidentes?"
→ **04-exemplo-relatorio-incidentes.md**

### "Como defino RTO/RPO?"
→ **05-exemplo-rto-rpo.md**

### "Como planejo a implementação?"
→ **06-exemplo-roadmap-adaptado.md** + **Playbook DORA** (dora.md)

### "Como escrevo a política?"
→ **07-exemplo-politica-seguranca.md**

### "Como fecho um contrato seguro?"
→ **08-exemplo-contrato-fornecedor.md**

---

## 📋 Checklist de Uso

Ao usar estes exemplos:

- [ ] **Ler README** - Entender propósito
- [ ] **Selecionar exemplo relevante** - Por contexto/abstenção
- [ ] **Adaptar ao seu contexto** - Não copiar direto
- [ ] **Validar com stakeholders** - GRC, Jurídico, Compliance
- [ ] **Testar antes de implementar** - Validar trilho auditoria
- [ ] **Documentar decisões** - Porquê escolheu X vs Y
- [ ] **Iterar** - Ajustar conforme lições

---

## 🔗 Relação com Capítulos do Manual

```
SbD-ToE Manual
├─ Cap. 01 - Classificação apps
│  └─ Exemplo: 05-rto-rpo.md, 06-roadmap.md
├─ Cap. 02 - Requisitos
│  └─ Exemplo: 07-politica-seguranca.md
├─ Cap. 05 - Dependências/SBOM
│  └─ Exemplo: 01-toolchain (SCA)
├─ Cap. 08 - IaC
│  └─ Exemplo: 01-toolchain (IaC options)
├─ Cap. 12 - Operações
│  └─ Exemplo: 01-toolchain (logs), 02-kpis, 04-incidentes
├─ Cap. 14 - Governação
│  └─ Exemplo: 03-raci-governance.md, 07-politica.md, 08-contrato.md
└─ Playbook DORA
   └─ Exemplo: Todos (implementar principles)
```

---

## ⚠️ Avisos Importantes

1. **Estes exemplos são ilustrativos**
   - Não copie diretamente
   - Adapte ao seu contexto legal, regulatório, operacional

2. **Consulte especialistas**
   - GRC/Compliance para políticas
   - Jurídico para contratos
   - Segurança para arquitetura

3. **Teste antes de usar em produção**
   - Validar trilho auditoria
   - Verificar conformidade com DORA
   - Confirmar integração

4. **Atualize regularmente**
   - DORA evolui (RTS/ITS)
   - Ferramentas evoluem
   - Best practices evoluem

---

## 🔄 Processo de Atualização

Estes exemplos serão atualizados quando:
- DORA RTS/ITS mudam
- Novo major version SbD-ToE
- Feedback de implementações reais
- Mudanças em best practices

**Próxima revisão programada:** Junho 2026

---

## 📞 Feedback

Se encontrar:
- ❓ Ambiguidade nos exemplos
- 🐛 Erro técnico
- ✨ Sugestão de melhoria
- 🔄 Novo exemplo needed

**Contacte:** [guardaremos para future releases]

---

**Versão:** 1.0  
**Data:** Novembro 2025  
**Próxima atualização:** Junho 2026
