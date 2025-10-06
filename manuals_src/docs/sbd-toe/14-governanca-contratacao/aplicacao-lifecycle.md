---
id: aplicacao-lifecycle
title: Aplicação no Ciclo de Vida — Governança & Contratação
description: Integração prática das práticas de governação, exceções e contratação no ciclo de vida SbD-ToE
tags: [ciclo de vida, governanca, contratacao, excecoes, fornecedores, rastreabilidade]
sidebar_position: 15
---

# 🏛️ Aplicação de Governança & Contratação no Ciclo de Vida {cap14:aplicacao-lifecycle}

## 🧭 Quando aplicar {cap14:aplicacao-lifecycle#quando-aplicar}

| Fase / Evento | Ação esperada | Evidência |
|---------------|--------------|-----------|
| Planeamento | Definir cláusulas contratuais e métricas | Documentos aprovados |
| Execução | Registar exceções, aplicar cláusulas em fornecedores | Registo GRC |
| Validação | Auditorias a fornecedores, revisões de exceções | Relatórios de auditoria |
| Operações | Reporting contínuo de KPIs | Dashboards |
| Auditoria | Revisão organizacional | Relatório consolidado |

---

## 👥 Quem executa cada ação {cap14:aplicacao-lifecycle#quem-executa}

| Papel | Responsabilidade |
|-------|------------------|
| **Dev** | Registar exceções e cumprir políticas |
| **AppSec** | Validar exceções, supervisionar rastreabilidade |
| **DevOps/SRE** | Assegurar execução técnica conforme cláusulas |
| **Gestão/PMO** | Aprovar risco residual |
| **Jurídico/Procurement** | Integrar cláusulas de segurança em contratos |
| **GRC** | Consolidar métricas e auditar fornecedores |

---

## 📖 User Stories normalizadas {cap14:aplicacao-lifecycle#user-stories}

### US-01 — Processo formal de exceções {#us-01}
**Contexto.** Sem exceções formais, práticas são ignoradas sem transparência.  

**📖 Rationale.**  
- **Referências:** SSDF PO.4, BSIMM SM1.3.  
- **Ameaças mitigadas:** shadow IT, bypass de controlos.  
- **Valor científico:** exceções formais reduzem risco oculto e permitem aceitação consciente.  

**História.**  
Como **Dev**, quero **submeter exceções de segurança em fluxo formal**, para **assegurar transparência e aprovação de risco**.  

**BDD.**  
- Dado que um controlo não pode ser cumprido  
- Quando submeto exceção  
- Então ela é avaliada e aprovada ou rejeitada  

**DoD.**  
- [ ] Exceção registada em ferramenta GRC  
- [ ] Aprovação AppSec + Gestão  
- [ ] Prazo definido para mitigação  

**Artefactos.** Registo exceções  

**Proporcionalidade.**  
| L1 | L2 | L3 |
|----|----|----|
| Opcional | Recomendado | Obrigatório |

**Integração.** Execução; Resp: Dev + AppSec  

---

### US-02 — Cláusulas contratuais de segurança {#us-02}
**Contexto.** Fornecedores sem cláusulas podem comprometer toda a cadeia.  

**📖 Rationale.**  
- **Referências:** SLSA, SSDF GV.1.  
- **Ameaças mitigadas:** supply chain compromise.  
- **Valor científico:** cláusulas contratuais asseguram enforcement organizacional.  

**História.**  
Como **Jurídico/Procurement**, quero **incluir cláusulas SbD-ToE em contratos**, para **garantir conformidade de fornecedores**.  

**BDD.**  
- Dado contrato novo  
- Quando cláusulas são aplicadas  
- Então fornecedor compromete-se a cumprir práticas de segurança  

**DoD.**  
- [ ] Cláusulas publicadas em modelo contratual  
- [ ] Contratos validados juridicamente  
- [ ] Monitorização de conformidade  

**Artefactos.** Contratos, cláusulas  

**Proporcionalidade.**  
| L1 | L2 | L3 |
|----|----|----|
| Recomendado | Obrigatório | Obrigatório + auditorias |

**Integração.** Planeamento; Resp: Jurídico + Procurement  

---

### US-03 — Validação contínua de fornecedores {#us-03}
**Contexto.** Fornecedores comprometidos propagam risco.  

**📖 Rationale.**  
- **Referências:** ISO 27036, BSIMM CMVM3.3.  
- **Ameaças mitigadas:** fornecedores inseguros, backdoors.  
- **Valor científico:** validação contínua reduz risco de supply chain em 40%.  

**História.**  
Como **GRC**, quero **validar fornecedores de forma contínua**, para **assegurar conformidade e segurança contratual**.  

**BDD.**  
- Dado fornecedor ativo  
- Quando auditoria ocorre  
- Então relatório documenta conformidade  

**DoD.**  
- [ ] Auditoria anual  
- [ ] Relatório publicado  
- [ ] Findings registados  

**Artefactos.** Relatórios de auditoria  

**Proporcionalidade.**  
| L1 | L2 | L3 |
|----|----|----|
| Opcional | Recomendado | Obrigatório |

**Integração.** Validação; Resp: GRC  

---

### US-04 — Rastreabilidade organizacional {#us-04}
**Contexto.** Sem rastreabilidade, a gestão não tem visibilidade real.  

**📖 Rationale.**  
- **Referências:** SSDF PO.1, SAMM Governance.  
- **Ameaças mitigadas:** falta de accountability.  
- **Valor científico:** dashboards centralizados aumentam transparência organizacional.  

**História.**  
Como **AppSec**, quero **agregar práticas de segurança por projeto em dashboard organizacional**, para **dar visibilidade e medir adoção**.  

**BDD.**  
- Dado projetos ativos  
- Quando métricas são recolhidas  
- Então dashboard mostra estado global  

**DoD.**  
- [ ] Dashboard configurado  
- [ ] Métricas por capítulo recolhidas  
- [ ] Relatórios entregues à direção  

**Artefactos.** Dashboard, relatórios  

**Proporcionalidade.**  
| L1 | L2 | L3 |
|----|----|----|
| Básico | Recomendado | Obrigatório |

**Integração.** Operações; Resp: AppSec + GRC  

---

### US-05 — KPIs de governação {#us-05}
**Contexto.** Sem métricas, não há melhoria contínua.  

**📖 Rationale.**  
- **Referências:** BSIMM SM1.3, SAMM Governance.  
- **Ameaças mitigadas:** complacência organizacional.  
- **Valor científico:** KPIs permitem medir eficácia e justificar investimento.  

**História.**  
Como **Gestão**, quero **definir e monitorizar KPIs de governação**, para **avaliar eficácia do programa SbD-ToE**.  

**BDD.**  
- Dado ciclo trimestral  
- Quando KPIs são medidos  
- Então relatório é partilhado com direção  

**DoD.**  
- [ ] KPIs definidos (ex.: exceções, fornecedores auditados)  
- [ ] Métricas recolhidas  
- [ ] Relatório partilhado  

**Artefactos.** Relatórios KPIs  

**Proporcionalidade.**  
| L1 | L2 | L3 |
|----|----|----|
| Básico | Recomendado | Obrigatório |

**Integração.** Auditoria; Resp: Gestão + GRC  

---

## 📦 Artefactos esperados {cap14:aplicacao-lifecycle#artefactos}

| Artefacto | Evidência |
|-----------|-----------|
| Registo de exceções | Ferramenta GRC |
| Contratos com cláusulas | Documentos validados |
| Relatórios de fornecedores | Auditorias e findings |
| Dashboard organizacional | Métricas por projeto |
| Relatórios KPIs | Consolidação trimestral |

---

## ⚖️ Matriz de proporcionalidade L1–L3 {cap14:aplicacao-lifecycle#proporcionalidade}

| Prática | L1 | L2 | L3 |
|---------|----|----|----|
| Exceções formais | Opcional | Recomendado | Obrigatório |
| Cláusulas contratuais | Recomendado | Obrigatório | Obrigatório + auditorias |
| Validação de fornecedores | Opcional | Recomendado | Obrigatório |
| Rastreabilidade organizacional | Básico | Recomendado | Obrigatório |
| KPIs de governação | Básico | Recomendado | Obrigatório |

---

## 🏁 Recomendações finais {cap14:aplicacao-lifecycle#recomendacoes}

- **Exceções sem registo = risco invisível.**  
- **Fornecedores devem ser parte do modelo SbD-ToE.**  
- **Rastreabilidade organizacional dá transparência à gestão.**  
- **KPIs de governação são a medida objetiva da maturidade.**  
- **Este capítulo é o “cimento” que une os restantes:** torna práticas visíveis, auditáveis e sustentáveis.  
