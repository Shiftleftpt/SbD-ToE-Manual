---
id: checklist-revisao
title: Checklist de Revisão — Arquitetura Segura
description: Lista de verificação binária e auditável para controlo da aplicação dos requisitos de arquitetura segura
tags: [checklist, arquitetura, validação, requisitos]
sidebar_position: 20
---

# ✅ Checklist de Revisão — Arquitetura Segura

Este checklist aplica-se a todas as aplicações avaliadas segundo os critérios definidos neste capítulo.  
Serve como instrumento de verificação binária e auditável da **adoção prática das prescrições de arquitetura segura**, permitindo:

- Controlo contínuo da aplicação dos requisitos `ARC-001` a `ARC-011`
- Verificação por projeto em momentos-chave do ciclo de vida
- Geração de indicadores operacionais agregáveis por equipa ou organização

> 🗓️ **Deve ser revisto a cada release ou alteração arquitetónica significativa**, conforme indicado no `15-aplicacao-lifecycle.md`.

---

## 📋 Itens de Verificação

| Item                                                                                                                        | Verificado? |
|-----------------------------------------------------------------------------------------------------------------------------|-------------|
| Foram definidas zonas de confiança com base em exposição, impacto e tipo de dados?                                         | ☐           |
| As fronteiras entre zonas incluem controlos de segurança explícitos (ex: API Gateway, ACLs, proxies, firewalls)?           | ☐           |
| Existe segmentação lógica entre componentes com domínios de confiança distintos (ex: produção vs admin)?                  | ☐           |
| Os fluxos interzonais foram representados e validados com base em critérios de threat modeling?                           | ☐           |
| O diagrama de arquitetura encontra-se versionado, acessível e atualizado no repositório?                                   | ☐           |
| Foi aplicada validação técnica proporcional ao risco, com base no checklist definido neste capítulo?                      | ☐           |
| Mudanças estruturais foram sujeitas a análise de impacto e atualização da rastreabilidade?                                | ☐           |
| Foram usados apenas padrões arquitetónicos aprovados (ou justificados com exceções formais)?                              | ☐           |
| Existe rastreabilidade entre requisitos de segurança e componentes da arquitetura (ex: matriz ARC ↔ componente)?          | ☐           |
| O projeto reutilizou um modelo de referência validado, ou justificou a não adesão?                                         | ☐           |
| Foi realizada threat modeling para fluxos críticos, e arquivado o modelo (ex: STRIDE)?                                     | ☐           |
| Exceções a requisitos foram aprovadas formalmente, com plano compensatório e validade definida?                           | ☐           |
| A decisão arquitetónica final foi validada por um revisor técnico e arquivada com evidência (ex: ADR, checklist, release)? | ☐           |

---

## 📌 Notas de Aplicação Prática

- Este checklist **deve ser integrado** em tarefas de sprint, gates de release ou revisões técnicas regulares.
- Deve ser usado como **instrumento de controlo e reporting operacional** por equipas de arquitetura, segurança e auditoria.
- Todos os campos devem ser validados com **evidência objetiva** (ex: ficheiros versionados, comentários de PR, ligações internas).

> ⚠️ Em caso de resposta negativa, deve existir exceção formal aprovada (ver `ARC-011`).

---

## 📊 Conformidade e KPI

- A validação deste checklist permite declarar **conformidade com o Capítulo 04 — Arquitetura Segura**.
- Os resultados por projeto podem ser **agregados para efeitos de medição de maturidade e rastreabilidade organizacional**.
- Este mecanismo pode ser integrado em **dashboards, métricas de equipa e processos de auditoria contínua**.

> ✅ Este instrumento está alinhado com a lógica de controlo contínuo definida no modelo SbD-ToE.
