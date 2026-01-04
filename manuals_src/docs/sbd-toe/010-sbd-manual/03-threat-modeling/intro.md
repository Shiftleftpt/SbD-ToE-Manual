---
id: intro
title: 📘 Capítulo 3 - Threat Modeling
description: Identificação, análise e mitigação estruturada de ameaças durante o ciclo de desenvolvimento
tags: [threat-modeling, stride, linddun, requisitos, mitigacao, risco, arquitetura, SAMM, SSDF, SLSA, DSOMM]
---

:::caution Capítulo Basilar
Este capítulo é considerado **basilar** no modelo *Security by Design - Theory of Everything (SbD-ToE)*.  
A sua aplicação é **obrigatória** para garantir a coerência, rastreabilidade e eficácia das restantes práticas de segurança.

A ausência ou aplicação parcial do Threat Modeling compromete a **ligação formal entre risco, arquitetura e requisitos**, tornando inviável uma adoção consistente do SbD-ToE.
:::

# 📘 Capítulo 3 - Threat Modeling

## 1. 🧭 O que cobre tecnicamente

O **Threat Modeling** é a prática que permite **antecipar ameaças reais** antes da implementação, com base na **arquitetura, fluxos de dados e contexto de risco** da aplicação. É tratado como um **processo decisional estruturado**, sujeito a validação humana e produção de evidência verificável.  
A ausência de uma ameaça num modelo não constitui prova da sua inexistência, devendo os riscos de omissão e enviesamento ser assumidos e mitigados explicitamente.

No SbD-ToE, o Threat Modeling constitui a **origem formal dos requisitos de mitigação**, ligando diretamente:
- a classificação de risco (Cap. 1),
- os requisitos de segurança (Cap. 2),
- e as decisões de arquitetura (Cap. 4).

Este capítulo cobre:

- A integração sistemática do threat modeling no ciclo de desenvolvimento
- Métodos estruturados de análise de ameaças (STRIDE, LINDDUN, PASTA)
- Criação e manutenção de modelos de ameaça baseados em arquitetura (DFDs, trust boundaries)
- Identificação de ameaças técnicas e de negócio relevantes
- Derivação explícita de requisitos e controlos a partir das ameaças identificadas
- Rastreabilidade entre ameaça → requisito → mitigação → validação
- Reutilização controlada de modelos em arquiteturas padronizadas

---

## 2. 🧪 Prescrição prática: o quê, quem, como, quando, porquê e para quê

### 🔐 Threat Modeling como elo entre risco, arquitetura e controlo

> *Sem Threat Modeling, os requisitos de segurança perdem contexto  
> e os controlos aplicados deixam de ter origem justificada.*

### 📌 O que deve ser feito

- Realizar threat modeling com base no **nível de risco da aplicação**
- Modelar fluxos de dados e limites de confiança com base em artefactos de arquitetura
- Identificar ameaças relevantes usando modelos reconhecidos
- Associar cada ameaça a:
  - um ou mais requisitos de mitigação,
  - controlos técnicos ou organizacionais,
  - e critérios de validação
- Documentar decisões, riscos aceites e ações futuras
- Validar o modelo de ameaças como parte da revisão de arquitetura

### ⚙️ Como deve ser feito

- Utilizar diagramas claros e versionados (DFDs, context diagrams)
- Aplicar metodologias como STRIDE, LINDDUN ou PASTA de forma proporcional
- Integrar o exercício em rituais existentes (design review, refinamento técnico)
- Criar itens rastreáveis no backlog para cada mitigação relevante
- Alinhar requisitos derivados com o Catálogo de Requisitos (Cap. 2)
- Reutilizar modelos apenas quando a arquitetura e o contexto forem equivalentes

> Ferramentas especializadas podem **suportar** o processo,  
> mas **não substituem a análise humana nem a validação técnica**.

### 📆 Quando aplicar

- No início de projetos ou épicos relevantes
- Antes de integrações externas, exposições ou mudanças arquiteturais
- Sempre que a aplicação seja classificada como **L2 ou L3**
- Sempre que ocorram alterações que possam modificar o perfil de ameaça

### 👥 Quem está envolvido

| Papel/Função              | Responsabilidades principais                                   |
|---------------------------|----------------------------------------------------------------|
| Arquitetura / DevSecOps   | Facilitar o processo e manter os modelos atualizados           |
| Equipa de Desenvolvimento | Explicar fluxos, lógica e superfícies de ataque                |
| Segurança / AppSec        | Identificar ameaças, vetores e técnicas de ataque relevantes   |
| Product Owner / Negócio   | Validar impacto, prioridade e aceitabilidade do risco          |

---

## 3. ⚠️ Caveats e limitações

- Modelos demasiado abstratos tornam-se inúteis
- Documentação não versionada perde valor operacional
- Ferramentas automatizadas não capturam contexto de negócio
- A ausência de ligação a requisitos e backlog anula o valor do exercício

---

## 4. 💡 Exemplos e reutilização

- Exemplos de aplicação de STRIDE por tipo de arquitetura
- Exemplos de threat modeling focado em privacidade (LINDDUN)
- Exemplos de integração com ferramentas de suporte (ex.: IriusRisk)

---

## 5. 🔍 O que pode ser feito mais (e porquê)

- Criar bibliotecas internas de ameaças reutilizáveis por tipo de sistema
- Integrar o threat modeling com pipelines de validação e gates de arquitetura
- Usar o histórico de incidentes e findings para enriquecer os modelos
- Formar facilitadores técnicos para sessões iterativas e leves

---

## 🧩 Ligações a outros capítulos

| Capítulo | Relação técnica |
|---------|-----------------|
| Cap. 1 – Gestão de Risco | Determina quando o threat modeling é obrigatório |
| Cap. 2 – Requisitos de Segurança | Recebe requisitos derivados das ameaças |
| Cap. 4 – Arquitetura Segura | Fonte primária dos artefactos modelados |
| Cap. 7 – CI/CD Seguro | Suporta rastreabilidade e validação |
| Cap. 10 – Testes de Segurança | Valida requisitos derivados |

---

> 📌 Este capítulo é **obrigatório** para aplicações **L2 e L3**.  
> É o mecanismo que garante que os requisitos de segurança **respondem a ameaças reais**,  
> e que a arquitetura é avaliada **antes** de ser explorada em produção.
