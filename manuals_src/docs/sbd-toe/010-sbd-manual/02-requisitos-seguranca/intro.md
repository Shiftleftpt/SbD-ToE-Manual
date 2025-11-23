---
description: Definição, aplicação, validação e rastreabilidade de requisitos de segurança
  aplicacionais por nível de risco
id: intro
sidebar_position: 1
tags:
- arquitetura
- threat-modeling
- dependencias
- segurança
- cicd
- dsomm
- samm
title: Requisitos de Segurança
categoria: basilar
group: engenharia_segura
---



:::caution Capítulo Basilar
Este capítulo é considerado **basilar** no modelo *Security by Design - Theory of Everything (SbD-ToE)*.  
A sua aplicação é **obrigatória** para garantir a coerência, rastreabilidade e eficácia das restantes práticas de segurança.  

Os capítulos basilares constituem a **fundação técnica e metodológica** do modelo, a ausência ou aplicação parcial de qualquer um destes compromete a **integridade global** do SbD-ToE, tornando inviável a adoção coerente das práticas operacionais e de governação.
:::



# 🛠️ Requisitos de Segurança

Este capítulo aborda a definição, estruturação e validação de **requisitos de segurança** desde o início do ciclo de desenvolvimento, com foco na **proporcionalidade ao risco**, **rastreabilidade** e **verificabilidade prática**.  
Abrange também boas práticas de gestão, critérios de aceitação, utilização de catálogos reutilizáveis e integração com processos ágeis (ex: backlog, histórias de utilizador, critérios de aceitação).

Inclui:

- Um [catálogo normativo de requisitos técnicos por tema e tipo de aplicação](/sbd-toe/sbd-manual/requisitos-seguranca/addon/catalogo-requisitos)
- Uma [taxonomia de rastreabilidade com tags normalizadas](/sbd-toe/sbd-manual/requisitos-seguranca/addon/rastreabilidade-controlo)
- Recomendações para [validação testável dos requisitos](/sbd-toe/sbd-manual/requisitos-seguranca/addon/validacao-requisitos)
- Um processo para [gestão de exceções e não aplicação justificada](/sbd-toe/sbd-manual/requisitos-seguranca/addon/gestao-excecoes)
- Explicações detalhadas sobre o racional e o alinhamento com frameworks como ASVS e SSDF (ver secções correspondentes neste capítulo)

---

## 📊 Tabela-Resumo dos Temas de Requisitos

O catálogo de requisitos está organizado por **20 temas técnicos**, identificados com códigos T01–T20.  
Cada tema agrupa requisitos com afinidade técnica e operacional, e é aplicado consoante o **nível de risco da aplicação**.

| Código | Tema                                     | Descrição resumida                                                     |
|--------|------------------------------------------|------------------------------------------------------------------------|
| T01    | Autenticação e Gestão de Identidade      | MFA, sessões, gestão de credenciais                                    |
| T02    | Controlo de Acesso                       | RBAC, privilégio mínimo, separação de funções                          |
| T03    | Registo, Auditoria e Monitorização       | Logs, eventos críticos, retenção, SIEM                                 |
| T04    | Gestão de Sessões                        | Tokens, timeouts, logout, proteção contra roubo                        |
| T05    | Validação e Sanitização de Dados         | Validação de input, output seguro, proteção contra injeções            |
| T06    | Proteção de Dados Sensíveis              | Cifras, hashing, classificação, políticas de acesso                     |
| T07    | Criptografia e Gestão de Chaves          | Algoritmos, rotação, armazenamento seguro, uso de cofres               |
| T08    | Tratamento de Erros e Mensagens          | Stack traces, mensagens genéricas, exceções                            |
| T09    | Segurança de APIs e Integrações          | Autenticação mútua, whitelisting, rate limiting, segurança mTLS        |
| T10    | Configuração Segura                      | Separação de ambientes, parametrização, validação de config            |
| T11    | Segurança do Código e Build              | Linters, SAST, pipelines, dependências internas                         |
| T12    | Gestão de Dependências e SBOM            | Atualizações, SCA, SBOM, política de severidade                        |
| T13    | CI/CD Seguro                             | Controlo de ambientes, proveniência, pipelines e validação             |
| T14    | Infraestrutura como Código               | Segurança em Terraform, Ansible, validação de políticas                |
| T15    | Containers e Execução Isolada            | Imagens fiáveis, hardening, scanning, runtime controls                 |
| T16    | Deploy, Release e Runtime Controls       | Reversibilidade, validação antes de produção, segregação de ambientes  |
| T17    | Testes de Segurança                      | SAST, DAST, fuzzing, integração no pipeline                            |
| T18    | Monitorização Contínua e Alertas         | Deteção de incidentes, alertas em tempo real                           |
| T19    | Formação, Onboarding e Perfis            | Perfis seguros, segregação, sensibilização                             |
| T20    | Governança, Revisões e Conformidade      | Revisões de segurança, cláusulas contratuais, aceitação de risco       |

> 📌 A seleção dos temas a aplicar é feita com base na [matriz de controlo por risco](./addon/matriz-controlos-por-risco).

---

## 🧪 2. Prescrição prática: o quê, quem, como, quando, porquê e para quê

### 📌 O que deve ser feito

1. Identificar e documentar requisitos de segurança com base no risco ([ver Capítulo 1](/sbd-toe/sbd-manual/classificacao-aplicacoes/intro))
2. Assegurar que os requisitos são **verificáveis e testáveis**
3. Incluir requisitos de segurança no **backlog funcional**
4. Garantir rastreabilidade sistemática entre risco, requisito, controlo e evidência, usando a [taxonomia definida](/sbd-toe/sbd-manual/requisitos-seguranca/addon/taxonomia-rastreabilidade)
5. Estabelecer **critérios de aceitação claros** para cada requisito
6. Rever, manter e justificar exceções com base em [critérios definidos](/sbd-toe/sbd-manual/requisitos-seguranca/addon/gestao-excecoes)

### ⚙️ Como deve ser feito

- Usar catálogos como o proposto neste manual, ou como base [ASVS v5.0](https://owasp.org/www-project-application-security-verification-standard/) como referência para requisitos técnicos
- Adaptar os requisitos ao **nível de risco e tipo de aplicação**
- Manter os requisitos num formato versionado e ligado ao repositório (Markdown, Excel, Jira)
- Integrar requisitos com critérios de aceitação claros (ex: Gherkin, checklist)
- Identificar requisitos com tags normalizadas da [taxonomia SEC-Lx-XXX](./addon/taxonomia-rastreabilidade)
- Validar com base nos critérios descritos na [secção de validação de requisitos](./addon/validacao-requisitos)

> 🧩 Usar planilhas de rastreabilidade (risco → requisito → controlo → validação)  
> 🎯 Estabelecer regras claras para a testabilidade de cada requisito

### 📆 Quando aplicar

- Na fase de definição de requisitos ou arquitetura
- Após conclusão de [Threat Modeling (Cap. 3)](/sbd-toe/sbd-manual/threat-modeling/intro)
- Sempre que o risco ou exposição da aplicação se alterem
- Em revisões de segurança, design reviews, sprint planning ou milestones

### 👥 Quem está envolvido e como

| Papel/Função             | Contributo principal                                                     |
|--------------------------|--------------------------------------------------------------------------|
| Arquitectura / DevSecOps | Tradução dos riscos em requisitos técnicos concretos                    |
| Product Owner / BA       | Integração no backlog e histórias de utilizador                          |
| Equipa de Segurança      | Definição de modelos e validação de alinhamento                          |
| QA / Testes              | Elaboração de critérios de aceitação de segurança e validação prática    |

> ✅ A rastreabilidade e testabilidade são responsabilidades partilhadas por todas as funções.

### 🎯 Porquê / Para quê

- Reduzir risco desde as fases iniciais
- Evitar retrabalho e custos de correção tardios
- Suportar auditorias e conformidade
- Aumentar a confiança nas releases
- Integrar a segurança nos processos de entrega ágil

---

## ⚠️ 3. Caveats ou limitações da prescrição

- Requisitos genéricos não testáveis não trazem valor (ex: "deve ser seguro")  
- Copiar checklists sem adaptação ao risco real resulta em sobrecarga ou falsa segurança  
- A rastreabilidade manual pode ser difícil sem apoio de ferramentas (Jira, traceability plugins)

---

## 🔍 5. O que pode ser feito mais (e porquê)

- Criar um catálogo interno com requisitos típicos reutilizáveis (tomando por base por exemplo o [catalogo deste manual](./addon/lista-requisitos-base))
- Adotar uma linguagem formal ou semi-formal para critérios de aceitação ([regras de taxonomia](./addon/taxonomia-rastreabilidade))
- Ligar requisitos à documentação técnica, diagramas e testes automatizados ([rastreabilidade](./addon/rastreabilidade-controlo), [como fazer avalidação dos requisitos](./addon/validacao-requisitos)
- Automatizar a rastreabilidade entre risco e requisito com ferramentas de ALM (Application Lifecycle Management)

---

## 📌 Nota sobre âmbito e extensibilidade

Este capítulo define um conjunto essencial e transversal de requisitos aplicacionais, aplicáveis à maioria dos sistemas empresariais, web e cloud-native. No entanto, aplicações com perfis técnicos específicos - como sistemas embebidos, IoT, SCADA, aplicações móveis, médicas ou industriais - poderão necessitar de requisitos e controlos adicionais.

É recomendada a consulta e curadoria adicional com base em fontes como:

- [OWASP Mobile Security Testing Guide (MSTG)](https://owasp.org/www-project-mobile-security-testing-guide/) <!-- Precisa revisão manual -->
- [OWASP Internet of Things Project](https://owasp.org/www-project-internet-of-things/) <!-- Precisa revisão manual -->
- [IEC 62443 - Segurança em Sistemas Industriais](https://webstore.iec.ch/publication/7033) <!-- Precisa revisão manual -->
- [NIST SP 800-213 - IoT Device Cybersecurity](https://csrc.nist.gov/publications/detail/sp/800-213/final) <!-- Precisa revisão manual -->


> A definição e manutenção do catálogo de requisitos e respetivo documento de validação devem seguir o mesmo padrão técnico e editorial: estrutura coerente, proporcionalidade por nível de risco, e rastreabilidade completa.

---

## 📜 Políticas Organizacionais Relevantes

| Política                          | Obrigatória | Aplicação           | Conteúdo mínimo esperado                                 |
|------------------------------------|:-----------:|---------------------|----------------------------------------------------------|
| Política de Requisitos de Segurança|   Sim       | Todas as aplicações | Definição, revisão, rastreabilidade, aceitação de risco  |
| Política de Testes de Segurança    |   Sim       | Apps L2/L3          | Critérios, evidência, aceitação, ciclo de revisão        |
| Política de Rastreabilidade        |   Opcional  | Apps críticas       | Mapeamento requisitos→controlo→validação, auditoria      |
| Política de Gestão de Exceções     |   Sim       | Todas               | Processo formal de justificação, registo e aceitação     |

[📎 Ver detalhe das políticas recomendadas para este capítulo](./policies-relevantes)
Para a versão impressa, ver o **anexo de políticas do manual**.
