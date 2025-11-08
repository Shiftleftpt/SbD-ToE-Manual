---
id: recomendacoes-avancadas
title: Práticas Avançadas em Threat Modeling
description: Recomendações reforçadas para organizações com elevada maturidade ou requisitos normativos
tags: [avançado, threat-modeling, automação, baseline, sincronização, governação]
sidebar_position: 30
---

# 🧩 Práticas Avançadas em Threat Modeling

Este anexo apresenta **práticas de nível avançado**, não obrigatórias, destinadas a organizações com maior maturidade, requisitos normativos exigentes (ex.: NIS2, DORA, ISO 27034, IEC 62443) ou equipas com processos de engenharia de segurança já consolidados.

> Estas práticas **não substituem** as prescrições do Capítulo 3, nem são usadas no cálculo de maturidade.  
> Funcionam como **extensões facultativas**, alinhadas com os níveis 3 do **OWASP SAMM**, **BSIMM** e **DSOMM – Design & Development**, reforçando a automação, rastreabilidade e governação.

---

## 🧱 1. Baselines e *Tailoring* de Modelos de Ameaça

> **Objetivo**: Normalizar o processo de Threat Modeling entre projetos e reutilizar conhecimento validado.

- Criar **baselines corporativas** por tipo de arquitetura (ex.: Web 3-tier, Micro-serviços, Event-driven).
- Cada projeto deve **importar** a baseline aplicável e documentar adaptações em `tailoring-notes.md`.
- Revisão obrigatória por AppSec antes de validação final.
- Integrar as baselines com catálogos de requisitos do Cap. 2 e controlos normativos.

> 💡 Reduz até 60 % o esforço médio de modelação mantendo cobertura equivalente (OWASP 2023).

**Artefactos esperados**
- `baseline/<pattern>.yaml`  
- `tailoring-notes.md`  
- Validação AppSec assinada

**Relação com frameworks**
| Referência | Domínio | Contribuição |
|-------------|----------|--------------|
| **BSIMM AM2.5** | Architecture Analysis | Normalização de práticas entre equipas |
| **SAMM Design 3/3** | Reutilização sistemática de modelos | Consistência organizacional |
| **DSOMM Tooling** | Threat Model Management | Integração de baselines e versionamento |

---

## 🔄 2. Sincronização com Ferramentas de Modelação

> **Objetivo**: Evitar divergências entre o repositório Git e a ferramenta de Threat Modeling (ex.: IriusRisk).

- Automatizar sincronização bidirecional (`tm-sync`), preservando identificadores `REQ-*` e `THREAT-*`.
- Gerar automaticamente relatórios `tm-coverage.csv` com percentagens de cobertura.
- Implementar verificação de idempotência e reporte de inconsistências.
- Integrar execução no pipeline CI/CD (condicional ou bloqueante por nível de risco).

**Artefactos esperados**
- `tm-sync.log`  
- `tm-coverage.csv`  
- Relatório de diferenças

**Relação com frameworks**
| Referência | Domínio | Benefício |
|-------------|----------|-----------|
| **DSOMM Tooling & Automation** | Integração de pipelines | Rastreabilidade e consistência |
| **BSIMM AM3.3** | Data Integration | Alinhamento contínuo entre código e modelos |
| **SSDF PO.3** | Security in Build Pipelines | Validação automática de artefactos |

---

## ⚖️ 3. *Gates* de Segurança Proporcionais (L1–L3)

> **Objetivo**: Assegurar que o processo de Threat Modeling condiciona a autorização de release conforme o risco.

- Definir matriz `gates-l1-l3.md` com limiares mínimos de cobertura:
  - L1 → ≥ 80 % de ameaças “Alta” mitigadas  
  - L2 → ≥ 90 % de ameaças “Alta” mitigadas  
  - L3 → 100 % de ameaças “Alta” mitigadas
- Nenhuma ameaça “Alta” pode permanecer sem *owner* ou *due date*.
- Todas as exceções “Alta” devem ter *sunset* definido (L1: ≤ 30 d / L2: ≤ 14 d / L3: ≤ 7 d).
- O *gate* deve ser auditável e documentado no relatório de cobertura.

**Artefactos esperados**
- `gates-l1-l3.md`  
- Relatório de cobertura e aprovação formal

**Relação com frameworks**
| Referência | Domínio | Benefício |
|-------------|----------|-----------|
| **SSDF RV.2** | Risk Validation | Governação objetiva de riscos antes de produção |
| **SAMM Verification 3/3** | Quality & Release Gating | Critérios de *go/no-go* de segurança |
| **DSOMM Metrics** | Continuous Maturity | Indicadores de cobertura e *readiness* |

---

## 📈 4. Métricas e *Dashboards* de Cobertura

> **Objetivo**: Medir a eficácia e a atualidade dos modelos de ameaça.

- Criar métricas automáticas:
  - % de ameaças “Alta” mitigadas  
  - Tempo médio de atualização (`last_updated`)  
  - % de modelos sincronizados  
  - Tendência de exceções aceites
- Representar graficamente por aplicação, sprint ou release.
- Usar *dashboards* ligados ao pipeline (ex.: Grafana, Power BI, DefectDojo).

> 📊 Esta prática reforça o domínio *Measurement* do **DSOMM** e fornece indicadores para auditorias NIS2/DORA.

---

## ✅ Considerações Finais

Estas práticas visam **elevar a maturidade organizacional** e alinhar o Threat Modeling com processos de governação e auditoria.  
São particularmente úteis quando:

- Existe **exigência regulatória** ou certificação (ex.: ISO 27034, IEC 62443).  
- O pipeline de desenvolvimento inclui **validações automáticas** e métricas.  
- A organização pretende atingir **nível 3 de maturidade DSOMM/SAMM**.

> 📌 Este anexo deve ser lido em conjunto com o `15-aplicacao-lifecycle.md` do capítulo, que descreve as práticas basilares obrigatórias.
