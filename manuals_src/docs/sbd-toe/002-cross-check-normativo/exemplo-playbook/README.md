---
id: exemplos-playbook
title: Exemplos de Suporte aos Playbooks
description: Ficheiros exemplares para demonstrar como implementar os princípios do SbD-ToE (reutilizáveis para DORA, NIS2, ISO 27001, etc.)
tags: [playbook, exemplos, dora, nis2, iso27001, implementacao, suporte]
---

# Exemplos de Suporte aos Playbooks

Este folder contém **exemplos e templates** que ilustram como implementar os princípios prescritos no SbD-ToE.

Estes exemplos são **reutilizáveis para múltiplos playbooks** (DORA, NIS2, ISO 27001, etc.)

## ⚠️ Importante

**Estes ficheiros são exemplos, NÃO prescrições do manual.**

O SbD-ToE prescreve *princípios*; organizações devem adaptar estes exemplos a:
- Stack tecnológico específico
- Constraints de orçamento e recursos
- Governance existente
- Contexto regulatório adicional

---

## Estrutura de Ficheiros

### 1. **01-exemplo-toolchain-options.md**
Apresenta opções de ferramentas para implementar os princípios do Cap. 08, 12, etc.

**Exemplos cobertos:**
- Infraestrutura como Código (IaC)
- Recolha centralizada de logs
- Análise de vulnerabilidades (SCA/SAST)
- CI/CD seguro

**Nota:** Não é prescrição de qual ferramenta usar, mas ilustra como diferentes stacks podem implementar os *princípios*.

---

### 2. **02-exemplo-kpis-targets.md**
Apresenta exemplos de KPIs e targets para diferentes perfis organizacionais.

**Exemplos cobertos:**
- Banco pequeno (PME financeira)
- Banco médio (regional)
- Fintech de pagamentos
- Segurado digital

**Nota:** Targets variam conforme risk appetite, não são obrigatórios.

---

### 3. **03-exemplo-raci-governance.md**
Template RACI exemplar mostrando como estruturar responsabilidades.

**Exemplos cobertos:**
- Governance committee
- Security team
- Development squads
- Operations

**Nota:** Organigrama específico depende de estrutura existente.

---

### 4. **04-exemplo-relatorio-incidentes.md**
Exemplo de template de reporte de incidentes alinhado com DORA RTS/ITS (informativo).

**Nota:** Templates oficiais vêm de regulador (EBA, BCB, ESMA); este é apenas ilustrativo.

---

### 5. **05-exemplo-rto-rpo.md**
Exemplo de definição de RTO/RPO por app, baseado em classificação L1–L3.

**Exemplos cobertos:**
- App L1 (não crítica): RTO 48h, RPO 24h
- App L2 (crítica): RTO 4h, RPO 1h
- App L3 (core banking): RTO `<`1h, RPO `<`15min

**Nota:** Valores são exemplares; cada org define conforme criticidade real.

---

### 6. **06-exemplo-roadmap-adaptado.md**
Exemplos de roadmaps adaptados para diferentes cenários.

**Exemplos cobertos:**
- Cenário: Startup fintech (poucos recursos, deadline DORA curto)
- Cenário: Banco tradicional (mais recursos, governance complexa)
- Cenário: PME com outsourcing parcial

---

### 7. **07-exemplo-politica-seguranca.md**
Template exemplar de Política de Segurança Aplicacional.

**Conteúdo:**
- Princípios (referência SbD-ToE Cap. 02)
- Governança (Cap. 14)
- Responsabilidades (RACI)
- Ciclo de vida apps (Cap. 01–14)
- Conformidade DORA (mapeamento)

---

### 8. **08-exemplo-contrato-fornecedor.md**
Exemplo de cláusulas técnicas para contrato de fornecedor.

**Conteúdo:**
- Security by Design obligations
- Ciclo de vida (onboarding/offboarding)
- Testes de segurança
- Liability e conformidade

---

## Como Usar Estes Exemplos

1. **Não copie diretamente** - Adapte ao seu contexto
2. **Use como referência** - Combine com outras boas práticas
3. **Valide com stakeholders** - Governança, GRC, Jurídico
4. **Itere** - Atualize conforme lições aprendidas

---

## Relação com o Manual

| Ficheiro | Prescrição SbD-ToE | Abstenção Deliberada |
|----------|---|---|
| 01-toolchain-options | Cap. 08, 12 (princípios) | Ferramentas específicas |
| 02-kpis-targets | Cap. 12 (métricas) | Targets quantitativos |
| 03-raci-governance | Cap. 14 (governança) | Estrutura organizacional |
| 04-relatorio-incidentes | Cap. 12 (incidentes) | Templates DORA RTS/ITS |
| 05-rto-rpo | Cap. 01, 08 (disponibilidade) | Valores específicos |
| 06-roadmap-adaptado | Playbook (fases) | Timeline executiva |
| 07-politica-seguranca | Cap. 02, 14 | Política específica org |
| 08-contrato-fornecedor | Cap. 14 | Cláusulas jurídicas |

---

## Aviso Legal

Estes exemplos são fornecidos como referência educativa e de suporte ao playbook DORA.

**Cada organização é responsável por:**
- Adaptar a seu contexto legal, regulatório e operacional
- Validar com GRC, Compliance, Jurídico
- Assegurar conformidade com DORA e regulações locais
- Testar antes de implementar em produção

---

**Data:** Novembro 2025  
**Versão:** 1.0  
**Próxima atualização:** Junho 2026
