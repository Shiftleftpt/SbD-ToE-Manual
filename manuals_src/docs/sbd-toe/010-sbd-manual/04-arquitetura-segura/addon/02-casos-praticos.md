---
id: casos-praticos
title: 🧪 Casos Práticos de Aplicação de Arquitetura Segura
sidebar_label: Casos Práticos
---

# 🧪 Casos Práticos de Aplicação de Arquitetura Segura

Estes exemplos demonstram como aplicar os requisitos de arquitetura segura em contextos reais, consoante o nível de risco da aplicação (ver Capítulo 1).

---

## 🏥 Caso 1 - Aplicação de Saúde com Exposição Pública (Risco Elevado - L3)

- Web app em cloud pública com APIs para clínicas e pacientes
- Dados clínicos e pessoais tratados
- Integração com serviços externos

**Requisitos aplicados:**

| Requisito | Aplicação prática |
|-----------|--------------------|
| ARC-001   | Zonas de confiança definidas (frontend público, backend, base de dados) |
| ARC-005   | Threat modeling STRIDE aplicado aos fluxos entre componentes |
| ARC-011   | Segmentação entre ambientes dev/stage/prod com permissões isoladas |
| ARC-012   | Arquitetura validada com critérios formais por AppSec e Arquitetura |
| ARC-013   | Validação automática da topologia via `Cartography` em CI/CD |

---

## 🧾 Caso 2 - Sistema de Faturação B2B (Risco Médio - L2)

- App web interna com utilizadores autenticados
- Dados financeiros e de clientes

**Requisitos aplicados:**

| Requisito | Aplicação prática |
|-----------|--------------------|
| ARC-002   | APIs internas isoladas da exposição externa |
| ARC-003   | Revisão de arquitetura com checklist de AppSec |
| ARC-006   | Serviços críticos isolados em subnets dedicadas |
| ARC-010   | Diagrama de arquitetura versionado no repositório (`.drawio`) |

---

## 📝 Caso 3 - Plataforma de Gestão de Tarefas Internas (Risco Baixo - L1)

- Aplicação web acessível apenas em rede interna
- Sem dados sensíveis nem APIs externas

**Requisitos aplicados:**

| Requisito | Aplicação prática |
|-----------|--------------------|
| ARC-001   | Diagrama simples com zona única de confiança |
| ARC-008   | Validação básica dos fluxos de dados internos |
| ARC-010   | Diagrama incluído na wiki do projeto |

---

> 🔗 Estes exemplos mostram como aplicar os requisitos conforme o risco, promovendo proporcionalidade e eficácia sem sobrecarga.
