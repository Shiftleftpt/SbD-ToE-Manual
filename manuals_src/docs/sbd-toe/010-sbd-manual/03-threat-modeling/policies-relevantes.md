---
id: policies-relevantes
title: Policies
sidebar_position: 60
---

# 🏛️ Políticas Organizacionais - Threat Modeling

A adoção eficaz do Capítulo 03 - Threat Modeling - depende da existência de **políticas organizacionais formais** que sustentem:

- A obrigatoriedade da modelação de ameaças em contextos de risco médio ou elevado;
- A integração da atividade no ciclo de desenvolvimento;
- A rastreabilidade entre ameaças, requisitos e controlos aplicados;
- A reutilização e validação de modelos em ambientes padronizados.

---

## 📌 Nota fundamental

> ✅ A modelação de ameaças deve ser tratada como uma **atividade obrigatória em aplicações L2 e L3**, com critérios formais definidos por política organizacional.

Estas políticas:

- Tornam o *threat modeling* uma prática **sistemática, auditável e rastreável**;
- Sustentam a tomada de decisão baseada em risco, conforme definido nos Capítulos 01 e 02;
- Permitem alinhar as equipas técnicas com práticas maduras de engenharia segura.

> 🧩 Este capítulo **implementa, na prática, o que as políticas organizacionais determinam**. A política legitima, o capítulo operacionaliza.

---

## 🧾 Políticas recomendadas

| Nome da Política                               | Obrigatória | Aplicação                                             | Conteúdo mínimo esperado                                                                 |
|------------------------------------------------|-------------|--------------------------------------------------------|------------------------------------------------------------------------------------------|
| Política de Threat Modeling                    | ✅ Sim      | Todas as aplicações classificadas como L2 ou L3        | Critérios de obrigatoriedade, momentos de aplicação no ciclo, papéis envolvidos, ferramentas permitidas |
| Política de Validação de Modelos de Ameaça     | ⚠️ Recomendado | Projetos com arquitetura nova ou alterações críticas | Processo de revisão técnica, validação cruzada por segurança, aceitação formal de risco  |
| Política de Reutilização de Modelos de Ameaça  | ⚠️ Recomendado | Organizações com arquiteturas padronizadas           | Critérios para reaproveitamento seguro de modelos anteriores, validação por contexto     |

---

## 📋 Estrutura sugerida de cada política

Cada política organizacional deve conter, no mínimo:

- **Objetivo e âmbito** da política;
- **Quando aplicar** (ex: por nível de risco, tipo de alteração, momento no ciclo);
- **Papéis e responsabilidades** (arquitetura, segurança, desenvolvimento, produto);
- **Exigência de outputs rastreáveis** (ex: modelo STRIDE, DFD, plano de mitigação);
- **Critérios de validação e reaproveitamento**;
- **Documentação obrigatória por tipo de projeto**;
- **Periodicidade de revisão da política em si** (ex: anual);
- **Critérios de aceitação de risco e exceções justificadas**.

---

## ✅ Recomendações finais

- Estas políticas devem ser **formais, aprovadas e divulgadas** a todas as equipas técnicas;
- Devem estar **alinhadas com o Catálogo de Requisitos do Capítulo 2** e com os critérios de risco definidos no Capítulo 1;
- Devem prever **revisão periódica e reaproveitamento controlado** de modelos existentes;
- A sua aplicação deve estar **integrada no ciclo de desenvolvimento** e validada em cada release crítica.

> 📌 A ausência destas políticas compromete a aplicação proporcional, contínua e eficaz do Threat Modeling em contexto organizacional.

