---
id: validacao-continuada
title: Validação Contínua de Governação
sidebar_position: 6
description: Estratégias e ciclos para manter validações, KPIs e exceções auditáveis
tags: [validacao, excecoes, auditoria, ciclo-continuo]
---

# 🔄 Validação Continuada e Revisões

Este anexo descreve os mecanismos de validação recorrente das aplicações, fornecedores e contratos, de forma a assegurar que os requisitos continuam aplicados, eficazes e corretamente governados ao longo do tempo.

A validação contínua garante não apenas a execução dos controlos definidos, mas também que a autoridade delegada a processos, contratos e mecanismos técnicos permanece explícita, adequada e revogável.

---

## ⏳ 1. Periodicidade de revisão sugerida

| Tipo de ativo            | Frequência sugerida            | Responsável primário         |
| ------------------------ | ------------------------------ | ---------------------------- |
| Aplicações críticas (L3) | Trimestral ou por release      | AppSec + Gestor de aplicação |
| Aplicações L2            | Semestral ou a cada 2 releases | AppSec + Dev Lead            |
| Fornecedores externos    | Anualmente ou por renovação    | Procurement + AppSec         |
| Contratos ativos         | Anualmente ou por aditamento   | Legal + Gestor funcional     |

> 🔹 As frequências devem ser ajustadas com base em incidentes, findings, mudanças de risco ou alterações relevantes a processos automatizados que executem validações, aprovações ou controlos de segurança.

---

## 🔢 2. Itens a validar por ciclo

Para além da verificação técnica e contratual, cada ciclo de validação deve confirmar que os pressupostos de governação se mantêm válidos:

* A classificação de risco da aplicação ou serviço ainda se mantém?
* Os requisitos aplicados continuam válidos e eficazes?
* Algum controlo deixou de funcionar (ex.: bypass, desativação ou alteração silenciosa)?
* A evidência continua acessível, legível e rastreável?
* Há novas exceções ou compensações a aprovar ou renovar?
* O fornecedor continua a cumprir SLA e requisitos de segurança acordados?
* Existem processos ou mecanismos automatizados que passaram a executar validações, bloqueios ou aprovações não previamente enquadrados no modelo de governação definido?
* A delegação de execução a processos técnicos continua alinhada com a autoridade organizacional atribuída?

---

## 🌎 3. Integração com ferramentas

O processo de validação contínua pode ser automatizado ou apoiado em ferramentas que permitam execução consistente e evidência rastreável, tais como:

* Jira (tarefas de revisão cíclica por aplicação ou contrato);
* SharePoint / Confluence (formulários ou registos de revisão);
* Git (labels, issues ou workflows por release);
* SIEM ou dashboards com findings e resultados de validações.

> 💡 Deve ser dada preferência a ferramentas que suportem trilha de auditoria, histórico de alterações e registo com data, permitindo identificar quando processos automatizados foram introduzidos, alterados ou desativados.

---

## 📊 4. Exemplo de plano de revisão anual

**Plano:** Revisão anual de contratos e integrações da unidade financeira

**Passos:**

1. Exportar lista de aplicações classificadas como L2/L3
2. Validar para cada uma:
   * Requisitos aplicados
   * Evidência de testes ou validação
   * SBOM e compliance de fornecedores
   * Processos automatizados ativos com impacto em segurança ou governação
3. Recolher exceções ativas, decisões associadas e prazos
4. Reportar desvios, alterações de autoridade e ações corretivas

---

## ✅ Recomendações finais

* Integrar revisões com o ciclo de release ou com mecanismos de fiscalização interna;
* Criar alertas para exceções caducadas ou não revalidadas;
* Usar este processo para alimentar os KPIs de governação (ver Cap. 14.30);
* Tratar a validação recorrente como parte integrante do ciclo de vida de segurança;
* Utilizar a validação contínua como mecanismo de deteção de delegações implícitas de autoridade a processos ou sistemas, assegurando a sua revisão ou revogação quando necessário.

---

## 🔗 Ligações cruzadas

* Cap. 1 - Revisão da classificação de risco (`addon/15-aplicacao-lifecycle.md`)
* Cap. 2 - Checklist de requisitos por projeto
* Cap. 14.3 - Onboarding e validação de fornecedores
* Cap. 14.4 - Rastreabilidade organizacional
* Cap. 14.5 - Exemplos de decisões e exceções
