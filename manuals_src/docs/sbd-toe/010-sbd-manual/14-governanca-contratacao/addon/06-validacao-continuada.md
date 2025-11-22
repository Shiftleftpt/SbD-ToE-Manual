---
description: Estratégias e ciclos para manter validações, KPIs e exceções auditáveis
id: validacao-continuada
sidebar_position: 6
tags:
- auditoria
- ciclo-continuo
- excecoes
- formacao
- segurança
- validacao
- validação
title: Validação Contínua de Governação
---



# 🔄 Validação Continuada e Revisões

Este anexo descreve os mecanismos de **validação recorrente** das aplicações, fornecedores e contratos, de forma a assegurar que os requisitos continuam aplicados e eficazes ao longo do tempo.

---

## ⏳ 1. Periodicidade de revisão sugerida

| Tipo de ativo            | Frequência sugerida            | Responsável primário         |
| ------------------------ | ------------------------------ | ---------------------------- |
| Aplicações críticas (L3) | Trimestral ou por release      | AppSec + Gestor de aplicação |
| Aplicações L2            | Semestral ou a cada 2 releases | AppSec + Dev Lead            |
| Fornecedores externos    | Anualmente ou por renovação    | Procurement + AppSec         |
| Contratos ativos         | Anualmente ou por aditamento   | Legal + Gestor funcional     |

> 🔹 Frequências devem ser ajustadas com base em incidentes, *findings* ou mudanças de risco.

---

## 🔢 2. Itens a validar por ciclo

* A classificação de risco da aplicação ou serviço ainda se mantém?
* Os requisitos aplicados continuam válidos e eficazes?
* Algum controlo deixou de funcionar (ex: bypass ou desativação)?
* A evidência continua acessível, legível e rastreável?
* Há novas exceções ou compensações a aprovar ou renovar?
* O fornecedor continua a cumprir SLA e requisitos de segurança acordados?

---

## 🌎 3. Integração com ferramentas

* O processo pode ser automatizado ou apoiado em:

  * Jira (tarefa de revisão cíclica por aplicação ou contrato);
  * SharePoint / Confluence (formulários ou registos de revisão);
  * Git (labels, issues ou workflows por release);
  * SIEM ou dashboards com findings / resultados de scans;

> 💡 Dê preferência a ferramentas que suportem **trilha de auditoria e registo com data**.

---

## 📊 4. Exemplo de plano de revisão anual

**Plano:** Revisão anual de contratos e integrações da unidade financeira

**Passos:**

1. Exportar lista de aplicações classificadas como L2/L3
2. Validar para cada uma:

   * Requisitos aplicados
   * Evidência de testes ou validação
   * SBOM e compliance de fornecedores
3. Recolher exceções ativas e prazos
4. Reportar desvios e acções corretivas

---

## ✅ Recomendações finais

* Integrar revisões com ciclo de release ou fiscalização interna;
* Criar alertas para exceções caducadas ou não revalidadas;
* Usar este processo para alimentar os **KPIs de governaça** (ver Cap. 14.30);
* Tratar a validação recorrente como parte do ciclo de vida de segurança.

---

## 🔗 Ligações cruzadas

* Cap. 1 - Revisão da classificação de risco (`addon/15-aplicacao-lifecycle.md`)
* Cap. 2 - Checklist de requisitos por projeto
* Cap. 14.3 - Onboarding e validação de fornecedores
* Cap. 14.4 - Rastreabilidade organizacional
* Cap. 14.5 - Exemplos de decisões e exceções

---
