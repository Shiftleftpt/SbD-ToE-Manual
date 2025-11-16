---
id: roles-intro
title: Roles & Responsabilidades
sidebar_label: 📖 Introdução
description: Papéis organizacionais no SbD-ToE e responsabilidades no ciclo de vida de segurança, alinhadas com NIS2, DORA e outros referenciais
tags: [roles, responsabilidades, governance, organizacao, nis2, dora]
sidebar_position: 1
---

# Papéis e Responsabilidades Organizacionais

A segurança de software não é apenas técnica; é sobretudo **organizacional e cultural**.  
O que distingue uma organização madura não é apenas a qualidade das ferramentas que utiliza, mas a clareza com que os papéis são definidos e assumidos.  

No SbD-ToE, cada papel é descrito de forma prática e concreta, com responsabilidades ligadas não só às práticas prescritas em cada capítulo, mas também às obrigações impostas por regulamentos como **NIS2** e **DORA**, que exigem governação explícita, responsabilidades documentadas e capacidade de demonstração perante autoridades competentes.

---

## 🎯 Estrutura desta Secção

Cada role está documentado num ficheiro dedicado que contém:

### 1. Visão Geral
Propósito e responsabilidade principal do role no contexto organizacional.

### 2. Enquadramento Regulatório
Alinhamento com **NIS2**, **DORA**, **GDPR**, **ISO 27001** e outros referenciais aplicáveis.

### 3. Atividades por Capítulo
User Stories (US) específicas organizadas por capítulo do manual SbD-ToE, com links diretos para os lifecycle files.

### 4. Referências aos Capítulos
Links para contexto completo de cada capítulo mencionado.

---

## 👥 Os 13 Roles do SbD-ToE

### Execução Técnica

#### [👨‍💻 Developer](./developer.md) — **25 User Stories**
Linha da frente da implementação prática de *security by design*. Escrevem código em conformidade com guidelines de segurança, corrigem vulnerabilidades e contribuem para threat modeling.

**NIS2/DORA**: Controlo de vulnerabilidades, práticas seguras de desenvolvimento, resiliência operacional.

---

#### [🧪 QA / Tester](./qa.md) — **13 User Stories**
Validam requisitos de segurança transformando-os em critérios de aceitação. Executam testes funcionais e de segurança em paralelo, confirmam que correções não introduzem regressões.

**NIS2/DORA**: Verificação de medidas de segurança, testes de resiliência periódicos.

---

#### [⚙️ DevOps / SRE](./devops-sre.md) — **50 User Stories**
Integram verificações de segurança em pipelines, automatizam SBOM e scans, garantem execução segura de IaC e containers, mantêm monitorização contínua.

**NIS2/DORA**: Gestão de dependências tecnológicas, resiliência operacional, medidas técnicas adequadas.

---

#### [🛡️ AppSec Engineer](./appsec-engineer.md) — **44 User Stories**
Traduzem normas em requisitos técnicos, facilitam threat modeling e revisão de arquitetura, definem guidelines de desenvolvimento seguro, produzem evidência de segurança.

**NIS2/DORA**: Ponto de ligação técnica-governação, rastreabilidade exigida.

---

#### [🏗️ Arquitetos de Software](./arquitetos-software.md) — **16 User Stories**
Desenham soluções com padrões seguros, antecipam implicações de risco, garantem consistência da arquitetura em pipelines, IaC e deploys.

**NIS2/DORA/GDPR/AI Act**: *Security by design*, planeamento de medidas técnicas adequadas.

---

#### [🔧 Operações (Ops)](./operacoes.md) — **4 User Stories**
Asseguram execução segura em runtime, implementam patches regulares, coordenam resposta a incidentes.

**NIS2/DORA**: Resposta a incidentes (notificação 24h), continuidade operacional.

---

#### [📋 Product Owner](./product-owner.md) — **6 User Stories**
Equilibram negócio e segurança, garantem que histórias de segurança entram no backlog, aprovam critérios de aceitação com segurança.

**NIS2/DORA**: Integração de segurança e continuidade digital nos produtos, gestão de risco no negócio.

---

#### [🧭 Scrum Master / Team Lead](./scrum-master.md) — **3 User Stories**
Facilitam integração da segurança no ciclo ágil, removem bloqueios, promovem disciplina de checklists.

**NIS2/DORA**: Operacionalização da governação executiva sobre segurança digital.

---

#### [🏅 Security Champion](./security-champion.md) — **6 User Stories**
Catalisadores de boas práticas, reforçam adoção próxima do quotidiano, garantem que segurança não é ignorada.

**NIS2/DORA**: Criação de cultura de segurança, formação e sensibilização.

---

### Governação e Compliance

#### [🏛️ Gestão Executiva / CISO](./gestao-executiva.md) — **14 User Stories**
Patrocinam e asseguram condições de aplicação, definem orçamento, apoiam ferramentas e formação, assumem responsabilidade final.

**NIS2/DORA**: Responsabilidade explícita do órgão de gestão pela supervisão e execução de medidas de cibersegurança e resiliência.

---

#### [📑 GRC / Compliance](./grc-compliance.md) — **17 User Stories**
Asseguram rastreabilidade com normas e regulamentos, monitorizam exceções, garantem documentação de risco residual, coordenam auditorias.

**NIS2/DORA/GDPR**: Prova documental, auditoria, reporte, resiliência, gestão de terceiros.

---

### Validação Externa

#### [🤝 Fornecedores / Terceiros](./fornecedores-terceiros.md) — **7 Requisitos Associados**
Cumprem cláusulas contratuais de segurança, entregam SBOM atualizado, garantem conformidade de componentes externos.

**NIS2/DORA**: Gestão explícita da cadeia de fornecimento digital (Art. 21 NIS2, Art. 28-30 DORA).

---

#### [📋 Auditores Internos e Externos](./auditores.md) — **11 Requisitos Associados**
Validam aplicação efetiva das práticas, avaliam classificações de risco, rastreabilidade e evidências, produzem relatórios independentes.

**NIS2/DORA/GDPR/ISO**: Comprovar conformidade perante autoridades de supervisão.

---

## 📊 Estatísticas Globais

| Categoria | Roles | User Stories |
|-----------|-------|--------------|
| **Execução Técnica** | 9 | 167 US |
| **Governação** | 2 | 31 US |
| **Validação** | 2 | 18 Requisitos |
| **TOTAL** | **13** | **216 US** |

### Top 5 Roles com mais US
1. **DevOps/SRE**: 50 US (cobertura 12 capítulos)
2. **AppSec Engineer**: 44 US (cobertura 14 capítulos)
3. **Developer**: 25 US (cobertura 13 capítulos)
4. **GRC/Compliance**: 17 US (governação e conformidade)
5. **Arquitetos**: 16 US (design e arquitetura)

---

## 🎯 Princípios Fundamentais

### Segurança como Função Coletiva
O SbD-ToE parte do princípio de que **a segurança é responsabilidade de todos**.  
Cada interveniente compreende o seu contributo, tanto para a resiliência técnica como para a conformidade legal.

### Rastreabilidade e Accountability
Ao ligar papéis a capítulos técnicos e a exigências regulatórias, o manual garante **rastreabilidade completa** de quem faz o quê, quando e porquê.

### Conformidade Regulatória
Todos os roles estão mapeados para obrigações de:
- **NIS2** - Segurança de redes e sistemas de informação
- **DORA** - Resiliência operacional digital (setor financeiro)
- **GDPR** - Proteção de dados pessoais
- **ISO 27001/27002** - Gestão de segurança da informação
- **NIST SSDF** - Secure Software Development Framework

### Clareza e Auditabilidade
Esta clareza é o que transforma **prescrições em prática viva e auditável**.  
Cada role tem responsabilidades documentadas, User Stories rastreáveis e evidência de conformidade.

---

## 🔍 Navegação

- **[📊 Estatísticas Detalhadas](./README.md)** - Números completos e distribuição
- **Por Role**: Aceder aos ficheiros individuais listados acima
- **Por Capítulo**: Ver secção "Referências aos Capítulos" em cada role
- **Por US**: Links diretos para `aplicacao-lifecycle.md` em cada capítulo

---

## 📌 Próximos Passos

1. **Identifique o seu role** na lista acima
2. **Consulte o ficheiro dedicado** para ver suas responsabilidades completas
3. **Navegue para os capítulos** relevantes usando as referências
4. **Implemente as User Stories** aplicáveis ao seu contexto

A segurança começa com clareza de responsabilidades. **Comece hoje**.
