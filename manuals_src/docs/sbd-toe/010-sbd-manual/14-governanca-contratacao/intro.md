---
id: intro
title: Governança & Contratação
description: Estruturas, políticas e práticas para assegurar governação organizacional, integração de fornecedores e transparência no ciclo SbD-ToE
tags: [governanca, contratacao, fornecedores, excecoes, rastreabilidade, conformidade, KPIs]
sidebar_position: 0
---

:::note Capítulo Organizacional
Este capítulo é considerado **organizacional** no modelo *Security by Design - Theory of Everything (SbD-ToE)*.  
A sua função é **assegurar a adoção, governação e evolução sustentável** das práticas de segurança definidas nos capítulos basilares e operacionais.

Os capítulos organizacionais estabelecem a estrutura humana, processual e decisória
que permite consolidar o SbD-ToE na organização.
Sem estes elementos, a segurança por design torna-se pontual e dependente de indivíduos,
perdendo a **consistência, autoridade e resiliência organizacional** necessárias à maturidade de longo prazo.
:::


# Governança & Contratação

Este capítulo assume um papel **excecional e fundacional** no SbD-ToE.
Enquanto capítulos anteriores prescrevem *o que* deve ser feito a nível técnico,
é aqui que se define **como essas práticas se tornam obrigatórias, visíveis,
auditáveis e governadas** ao nível organizacional.

Este capítulo estabelece explicitamente o **modelo de governação e autoridade** que enquadra todas as práticas de segurança do SbD-ToE, definindo **quem decide**, **com que legitimidade**, **em que condições** e **com que evidência**.

Fornece a estrutura para **unificar esforços dispersos** de equipas técnicas, garantindo que a segurança é controlada como responsabilidade organizacional, e introduz mecanismos formais de **exceções**, **contratação**, **rastreabilidade**
e **medição**, que transformam a segurança de um exercício local num **sistema de governação e responsabilização corporativa**, através de:

- Definição de **modelos formais de governação** para segurança.  
- Processo explícito de **gestão de exceções e aceitação de risco**, com registo e aprovação.  
- Integração obrigatória de **cláusulas contratuais de segurança** em procurement e outsourcing.  
- **Validação contínua de fornecedores** (auditorias, due diligence).  
- **Rastreabilidade organizacional**: visão consolidada de práticas por projeto.  
- Definição, recolha e análise de **KPIs de governação** (exceções, incidentes, cobertura formativa, etc.).  

Em contextos de elevada automação, a organização deve definir explicitamente que tipos de decisões podem ser executadas automaticamente, quais os seus limites e quem mantém responsabilidade final sobre os seus efeitos.

A delegação de execução a processos ou sistemas é sempre uma decisão organizacional consciente, documentada e revogável.

👉 É este capítulo que permite responder, de forma objetiva e defensável, à pergunta crítica:  
*“A organização consegue demonstrar, com evidência, o que está a ser feito em segurança por todas as equipas e fornecedores?”*

---

## 🧪 2. Prescrição prática

- **O que fazer:**  
  - Criar um **modelo formal e aprovado** de governação de segurança.  
  - Estabelecer um **fluxo explícito** de exceções e aceitação de risco.  
  - Integrar **cláusulas contratuais de SbD-ToE** em fornecedores e parceiros.  
  - Definir auditorias e mecanismos de **validação contínua de terceiros**.  
  - Recolher, analisar e reportar **KPIs de governação** de forma sistemática.  

- **Como fazer:**  
  - Através de documentos de governação **aprovados pela direção**.  
  - Utilizando ferramenta de **GRC** para rastrear exceções, decisões e métricas.  
  - Integrando jurídico e procurement nos processos de contratação.  
  - Assegurando **reporting periódico** à gestão e órgãos de decisão.  

- **Quando:**  
  - Em todos os novos projetos e processos de contratação.  
  - Sempre que existam exceções às práticas prescritas.  
  - Em ciclos regulares (ex.: trimestrais) de governação e revisão.  

- **Porquê:**  
  - Transformar segurança numa **prática institucionalizada e governada**.  
  - Tornar **visível, mensurável e auditável** o estado de adoção.  
  - Garantir conformidade normativa (ISO 27001, NIS2, SSDF, entre outras).  

---

## 👥 Papéis envolvidos

A governação eficaz exige papéis claramente definidos, com autoridade proporcional e responsabilidades explícitas.

- **Dev** → regista exceções e aplica práticas acordadas.  
- **AppSec** → valida exceções e supervisiona a rastreabilidade.  
- **DevOps/SRE** → garante aplicação prática em pipelines e deploy.  
- **Gestão / PMO** → aprova risco residual e governa a adoção organizacional.  
- **Jurídico / Procurement** → integra cláusulas de segurança em contratos.  
- **GRC / Conformidade** → recolhe evidências, gere métricas e auditorias.  

👉 Cada papel exerce autoridade **derivada do modelo de governação definido**
e tem **user stories associadas** no `aplicacao-lifecycle.md`.

---

## 🔗 Integração no ciclo

A governação atua como camada **horizontal e transversal** em todo o ciclo SbD-ToE:

- **Planeamento:** definição de cláusulas, políticas e métricas.  
- **Execução:** registo de exceções, integração contratual, reporting contínuo.  
- **Validação:** auditorias a fornecedores, verificação de KPIs.  
- **Operações:** integração com incidentes e monitorização.  
- **Auditoria organizacional:** evidência consolidada de adoção por capítulo.  

A existência de mecanismos técnicos automatizados não cria, por si só, autoridade, nem substitui os modelos de governação aqui definidos.

---

## 📊 Rastreabilidade organizacional

A governação eficaz exige rastreabilidade completa e consistente:

- **Exceções registadas e aprovadas** em ferramenta de GRC.  
- **Cláusulas contratuais rastreadas** nos contratos de fornecedores.  
- **KPIs consolidados** em dashboard organizacional
  (ex.: % de equipas com champions, nº de exceções aprovadas, tempo médio de resolução).  
- **Ligação explícita a frameworks normativos**
  (ISO, NIS2, SSDF) assegura completude e conformidade.  

---

## 🏁 Conclusão

Este capítulo é o que **fecha e legitima o ciclo do SbD-ToE**:

- Transforma práticas isoladas em **processo organizacional governado e auditável**.  
- Dá **autoridade, visibilidade e transparência** à gestão.  
- Permite **medir eficácia real** através de KPIs.  
- Integra segurança de forma explícita em **fornecedores e contratos**.  

👉 Sem este capítulo, o SbD-ToE fica limitado à prática técnica local.  
👉 Com ele, torna-se um **sistema de governação organizacional explícito,
defensável e sustentável**.

---

## 📜 Políticas Organizacionais Relevantes

| Política | Obrigatória? | Aplicação | Conteúdo mínimo |
|----------|--------------|-----------|-----------------|
| Política de Exceções de Segurança | Sim | AppSec + Gestão | Fluxo formal de pedido, aprovação e prazo |
| Política de Contratação Segura | Sim | Jurídico / Procurement | Cláusulas SbD-ToE, validação contínua |
| Política de Rastreabilidade Organizacional | Sim | GRC | Registo centralizado, dashboards |
| Política de Auditoria de Fornecedores | Recomendado | Procurement + AppSec | Auditorias periódicas de segurança |
| Política de KPIs de Governação | Sim | GRC + Direção | Métricas, relatórios, objetivos |

Na versão impressa, consultar o **Anexo de Políticas Organizacionais do manual**,
onde estas políticas estão consolidadas transversalmente.
