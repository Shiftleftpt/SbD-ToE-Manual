---
id: intro
title: Requisitos de Segurança
description: Definição, aplicação, validação e rastreabilidade de requisitos de segurança aplicacionais por nível de risco
tags: [tipo:prescricao, tema:requisitos, segurança, rastreabilidade, validação, proporcionalidade, SSDF, SAMM, DSOMM, ASVS]
sidebar_position: 1
---

:::caution Capítulo Basilar
Este capítulo é considerado **basilar** no modelo *Security by Design – Theory of Everything (SbD-ToE)*.  
A sua aplicação é **obrigatória** para garantir a coerência, rastreabilidade e eficácia das restantes práticas de segurança.

Os capítulos basilares constituem a **fundação técnica e metodológica** do modelo. A ausência ou aplicação parcial de qualquer um destes compromete a **integridade global** do SbD-ToE, tornando inviável a adoção coerente das práticas operacionais e de governação.
:::

# 🛠️ Requisitos de Segurança

Este capítulo define o **quadro normativo de requisitos de segurança aplicacionais** do SbD-ToE, bem como o **processo para a sua correta aplicação, validação e rastreabilidade** ao longo de todo o ciclo de vida de desenvolvimento.

O foco central incide sobre:
- **proporcionalidade ao risco**, determinada pela classificação da aplicação (L1–L3);
- **verificabilidade prática**, assegurando que cada requisito pode ser validado de forma objetiva;
- **rastreabilidade completa**, ligando risco, requisito, controlo e evidência.

O capítulo aborda igualmente boas práticas de **gestão de requisitos**, definição de **critérios de aceitação**, utilização de **catálogos reutilizáveis** e integração dos requisitos de segurança em processos de desenvolvimento ágeis (ex.: backlog, histórias de utilizador, critérios de aceitação).

Inclui, em particular:

- Um **catálogo normativo de requisitos técnicos**, organizado por tema e tipo de aplicação  
  → ver [Catálogo de Requisitos](/sbd-toe/sbd-manual/requisitos-seguranca/addon/catalogo-requisitos)
- Uma **taxonomia de rastreabilidade** com identificadores e tags normalizadas  
  → ver [Taxonomia de Rastreabilidade](/sbd-toe/sbd-manual/requisitos-seguranca/addon/rastreabilidade-controlo)
- Recomendações para **validação objetiva e testável** dos requisitos  
  → ver [Validação de Requisitos](/sbd-toe/sbd-manual/requisitos-seguranca/addon/validacao-requisitos)
- Um **processo formal de gestão de exceções**, incluindo justificação e aceitação de risco  
  → ver [Gestão de Exceções](/sbd-toe/sbd-manual/requisitos-seguranca/addon/gestao-excecoes)
- Explicações detalhadas sobre o **racional dos requisitos** e o seu alinhamento com frameworks como **OWASP ASVS** e **NIST SSDF** (ver secções correspondentes neste capítulo)

---

## 📊 Tabela-Resumo dos Temas de Requisitos

O catálogo de requisitos está organizado em **20 temas técnicos**, identificados pelos códigos **T01–T20**.  
Cada tema agrupa requisitos com afinidade técnica e operacional, sendo aplicável de forma proporcional ao **nível de risco da aplicação**.

| Código | Tema                                     | Descrição resumida                                                     |
|--------|------------------------------------------|------------------------------------------------------------------------|
| T01    | Autenticação e Gestão de Identidade       | MFA, sessões, gestão de credenciais                                    |
| T02    | Controlo de Acesso                        | RBAC, privilégio mínimo, separação de funções                          |
| T03    | Registo, Auditoria e Monitorização        | Logs, eventos críticos, retenção, SIEM                                 |
| T04    | Gestão de Sessões                         | Tokens, timeouts, logout, proteção contra roubo                        |
| T05    | Validação e Sanitização de Dados          | Validação de input, output seguro, proteção contra injeções            |
| T06    | Proteção de Dados Sensíveis               | Cifras, hashing, classificação, políticas de acesso                    |
| T07    | Criptografia e Gestão de Chaves           | Algoritmos, rotação, armazenamento seguro, uso de cofres               |
| T08    | Tratamento de Erros e Mensagens           | Stack traces, mensagens genéricas, exceções                            |
| T09    | Segurança de APIs e Integrações            | Autenticação mútua, whitelisting, rate limiting, mTLS                  |
| T10    | Configuração Segura                       | Separação de ambientes, parametrização, validação de configuração      |
| T11    | Segurança do Código e Build               | Linters, SAST, pipelines, dependências internas                        |
| T12    | Gestão de Dependências e SBOM             | Atualizações, SCA, SBOM, políticas de severidade                       |
| T13    | CI/CD Seguro                              | Controlo de ambientes, proveniência, pipelines e validação             |
| T14    | Infraestrutura como Código                | Terraform, Ansible, validação de políticas                             |
| T15    | Containers e Execução Isolada             | Imagens fiáveis, hardening, scanning, controlos em runtime             |
| T16    | Deploy, Release e Runtime Controls        | Reversibilidade, validação pré-produção, segregação de ambientes       |
| T17    | Testes de Segurança                       | SAST, DAST, fuzzing, integração em pipeline                            |
| T18    | Monitorização Contínua e Alertas          | Deteção de incidentes, alertas em tempo real                           |
| T19    | Formação, Onboarding e Perfis             | Perfis seguros, segregação, sensibilização                             |
| T20    | Governança, Revisões e Conformidade       | Revisões de segurança, cláusulas contratuais, aceitação de risco       |

> 📌 A seleção dos temas a aplicar é realizada com base na  
> [Matriz de Controlo por Risco](./addon/matriz-controlos-por-risco).

---

## 🧪 Prescrição prática: o quê, quem, como, quando, porquê e para quê

### 📌 O que deve ser feito

1. Identificar e documentar requisitos de segurança com base no risco  
   (ver [Capítulo 1 — Classificação](/sbd-toe/sbd-manual/classificacao-aplicacoes/intro))
2. Assegurar que todos os requisitos são **verificáveis e testáveis**
3. Integrar requisitos de segurança no **backlog funcional** da aplicação
4. Garantir **rastreabilidade sistemática** entre risco, requisito, controlo e evidência, utilizando a taxonomia definida
5. Estabelecer **critérios de aceitação claros** para cada requisito
6. Rever, manter e justificar exceções com base em critérios formais de aceitação de risco

### ⚙️ Como deve ser feito

- Utilizar catálogos como o proposto neste manual ou referências consolidadas como o **OWASP ASVS**
- Adaptar os requisitos ao **nível de risco e tipo de aplicação**
- Manter os requisitos em formato **versionado e auditável** (ex.: Markdown, Excel, Jira)
- Associar requisitos a **critérios de aceitação claros** (ex.: Gherkin, checklists)
- Identificar requisitos com **tags normalizadas** da taxonomia `SEC-Lx-XXX`
- Validar os requisitos com base nos critérios definidos na secção de validação

> 🧩 Utilizar matrizes de rastreabilidade (risco → requisito → controlo → validação)  
> 🎯 Definir regras objetivas para a testabilidade de cada requisito

### 📆 Quando aplicar

- Na fase de definição de requisitos e/ou arquitetura
- Após a conclusão de **Threat Modeling** (Cap. 3)
- Sempre que o risco, exposição ou contexto da aplicação se alterem
- Em revisões de segurança, *design reviews*, *sprint planning* ou *milestones*

### 👥 Quem está envolvido

| Papel/Função             | Contributo principal                                                  |
|--------------------------|------------------------------------------------------------------------|
| Arquitetura / DevSecOps  | Tradução de riscos em requisitos técnicos concretos                    |
| Product Owner / BA       | Integração no backlog e histórias de utilizador                        |
| Equipa de Segurança      | Definição de modelos, validação e alinhamento                          |
| QA / Testes              | Definição de critérios de aceitação e validação prática                |

> ✅ A rastreabilidade e a testabilidade são responsabilidades partilhadas.

### 🎯 Porquê / Para quê

- Reduzir o risco desde as fases iniciais
- Evitar retrabalho e custos de correção tardios
- Suportar auditorias e obrigações de conformidade
- Aumentar a confiança nas *releases*
- Integrar segurança de forma nativa nos processos ágeis

---

## ⚠️ Caveats e limitações

- Requisitos genéricos ou não testáveis não acrescentam valor
- A aplicação acrítica de checklists pode gerar falsa sensação de segurança
- A rastreabilidade manual pode ser onerosa sem apoio de ferramentas adequadas
- A utilização de processos fortemente automatizados **não dispensa validação independente, responsabilidade explícita nem evidência verificável**

---

## 🔍 O que pode ser feito mais (e porquê)

- Criar catálogos internos reutilizáveis, tomando como base o catálogo deste manual
- Adotar linguagens formais ou semi-formais para critérios de aceitação
- Ligar requisitos à documentação técnica, diagramas e testes automatizados
- Automatizar a rastreabilidade entre risco e requisito com ferramentas de ALM

---

## 📌 Nota sobre âmbito, processo e extensibilidade

Este capítulo define um conjunto **essencial e transversal de requisitos de segurança aplicacionais**, aplicáveis à maioria dos sistemas empresariais, web e *cloud-native*.

As **características do processo de desenvolvimento e entrega** — incluindo elevado grau de automação, geração automática de artefactos, utilização de plataformas *low-code/no-code* ou maior dependência de terceiros — **não alteram o catálogo base de requisitos nem a classificação L1–L3 da aplicação**, que continuam a ser determinadas pelo impacto e exposição do sistema.

No entanto, esses contextos **exigem maior rigor na aplicação, validação, evidência e rastreabilidade dos requisitos**, implicando o reforço das práticas descritas nos capítulos técnicos do manual, nomeadamente **Arquitetura Segura, CI/CD, Infraestrutura como Código, Desenvolvimento Seguro e Testes de Segurança**.

Aplicações com perfis técnicos específicos (ex.: sistemas embebidos, IoT, SCADA, aplicações móveis, médicas ou industriais) poderão igualmente necessitar de requisitos e controlos adicionais, devendo ser complementadas com referências especializadas como:

- OWASP Mobile Security Testing Guide (MSTG)
- OWASP Internet of Things Project
- IEC 62443 — Segurança em Sistemas Industriais
- NIST SP 800-213 — IoT Device Cybersecurity

> A definição e manutenção do catálogo de requisitos e respetiva validação devem seguir sempre os princípios de coerência estrutural, proporcionalidade por nível de risco e rastreabilidade completa.

---

## 📜 Políticas Organizacionais Relevantes

| Política                           | Obrigatória | Aplicação           | Conteúdo mínimo esperado                                 |
|------------------------------------|:-----------:|---------------------|----------------------------------------------------------|
| Política de Requisitos de Segurança | Sim         | Todas as aplicações | Definição, revisão, rastreabilidade, aceitação de risco  |
| Política de Testes de Segurança    | Sim         | Apps L2/L3          | Critérios, evidência, aceitação, ciclo de revisão        |
| Política de Rastreabilidade        | Opcional    | Apps críticas       | Mapeamento requisito→controlo→validação, auditoria       |
| Política de Gestão de Exceções     | Sim         | Todas               | Processo formal de justificação, registo e aceitação     |

[📎 Ver detalhe das políticas recomendadas para este capítulo](./policies-relevantes)  
Para a versão impressa, ver o **anexo de políticas do manual**.
