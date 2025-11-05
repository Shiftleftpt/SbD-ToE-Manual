---
id: policies-relevantes
title: Policies
description: Políticas necessárias para suportar práticas de logging, deteção e resposta contínua.
tags: [policy, organizacional, monitorizacao, deteccao, resposta, operacoes]
---


# 🏛️ Políticas Organizacionais - Monitorização e Operações

A adoção eficaz do **Capítulo 12 - Monitorização e Operações** exige a existência de **políticas organizacionais formais** que regulem e sustentem a **deteção, correlação e resposta a eventos de segurança em tempo real**.

---

## 📌 Nota fundamental

> ⚠️ As práticas descritas neste capítulo - logging estruturado, regras de alerta, correlação de eventos, integração com IRP, medição de MTTD/MTTR - **devem ser sustentadas por políticas organizacionais claras, auditáveis e aplicáveis a todos os ambientes operacionais**.

Estas políticas:

- Tornam **obrigatória e mensurável** a aplicação técnica das práticas de monitorização;
- Estabelecem **responsabilidades de triagem, escalonamento e resposta a incidentes**;
- Garantem que a **visibilidade operacional é coerente e eficaz em todos os sistemas e pipelines**;
- Servem de referência para **auditorias, análises pós-incidente e melhoria contínua da maturidade operacional**.

---

## 🧾 Políticas Recomendadas

| Nome da Política                                 | Obrigatória? | Aplicação                                 | Resumo do Conteúdo Necessário                                                  |
|--------------------------------------------------|--------------|--------------------------------------------|---------------------------------------------------------------------------------|
| Política de Monitorização e Logging              | ✅ Sim        | Todos os serviços e aplicações             | Definição de eventos, níveis de logging, formatos estruturados, destinos centralizados. |
| Política de Alertas e Deteção de Comportamentos  | ✅ Sim        | Sistemas críticos e ambientes de produção  | Tipos de eventos sensíveis, thresholds, tolerância a falso-positivos, resposta. |
| Política de Observabilidade de Serviços          | ⚠️ Opcional  | Microserviços e arquiteturas distribuídas  | Métricas mínimas, dashboards obrigatórios, correlação com logs.                |
| Política de Retenção e Acesso a Registos         | ✅ Sim        | Todos os logs de segurança e operação      | Retenção ≥30 dias, ACL, cifragem, registo de acessos.                          |
| Política de Resposta a Incidentes Operacionais   | ✅ Sim        | Todos os domínios com deteção ativa        | Canais de resposta, playbooks, reporte, owners de domínio.                     |
| Política de Cobertura de Agentes e Instrumentação| ⚠️ Opcional  | Infraestrutura, cloud, endpoints           | Tipos de agentes obrigatórios, cobertura mínima, manutenção de visibilidade.   |

---

## 📎 Correspondência com Frameworks Normativas

| Framework            | Requisitos cobertos pelas políticas acima                                                             |
|---------------------|--------------------------------------------------------------------------------------------------------|
| **NIST SSDF**        | RV.1.2, RV.3.3, RV.4.1 - Logging estruturado, deteção ativa, resposta coordenada                      |
| **CIS Controls v8**  | Control 8 (Audit Log Management), Control 17 (Incident Response), Control 6 (Access Control)           |
| **OWASP SAMM**       | Operations > Incident Management; Deployment > Environment Management                                 |
| **BSIMM13**          | SE3.2 (Security Events), IR1 (Incident Response), TCM1 (Deteção e mitigação de ataques)               |
| **ENISA DevSecOps**  | Logging, observabilidade, deteção de anomalias, governação contínua                                   |

---

## 🧱 Estrutura Esperada de Cada Política

Cada política organizacional deve conter:

- **Objetivo e âmbito** (quais sistemas ou ambientes cobre);
- **Tipos de eventos ou condições monitorizadas** (ex: login falhado, elevação de privilégios);
- **Regras para triagem, escalonamento e mitigação**;
- **Retenção mínima de logs e respetivo formato e segurança**;
- **Cobertura exigida por agentes ou sensores técnicos**;
- **Integração com o ciclo de vida de desenvolvimento e resposta**;
- **Periodicidade de revisão, teste e auditoria da política**.

---

## ✅ Recomendações Finais

- As políticas devem ser **revistas regularmente** com base na evolução das ameaças e da arquitetura;
- Devem estar **acessíveis e compreendidas por todas as equipas técnicas e operacionais**;
- Devem ser **refletidas nas práticas de CI/CD, em ambientes de produção e nos requisitos de release**;
- Devem ser **validadas por auditorias internas e suportadas por evidência contínua (dashboards, alertas testados, logs visíveis)**.

> 📌 Políticas bem definidas são a base para **observabilidade e reação operacionais eficazes** - sem elas, mesmo os sistemas mais instrumentados ficam vulneráveis a falhas silenciosas.
