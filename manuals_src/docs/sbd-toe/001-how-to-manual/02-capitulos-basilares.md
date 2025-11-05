---
id: estrutura-capitulos
title: Estrutura dos Capítulos do Manual SbD-ToE
hide_title: false
hide_table_of_contents: false
description: Classificação dos capítulos do manual em Basilares, Operacionais e Organizacionais, e respetiva função no modelo Security by Design – Theory of Everything.
---

# Estrutura dos Capítulos do Manual SbD-ToE

O manual *Security by Design – Theory of Everything (SbD-ToE)* organiza os seus 14 capítulos em **três agrupamentos complementares**, que refletem a natureza e o papel de cada tema dentro do modelo global de segurança.

Cada agrupamento representa um **nível distinto de responsabilidade** no ciclo de vida e governação da segurança de software:

- **🧱 Capítulos Basilares** — fundação técnica e metodológica  
- **⚙️ Capítulos Operacionais** — execução e automatização das práticas  
- **🏛️ Capítulos Organizacionais** — governação, capacitação e sustentabilidade

---

## 🧱 Capítulos Basilares

Os capítulos **basilares** representam os **fundamentos essenciais** sobre os quais todo o modelo SbD-ToE é construído.  
A sua aplicação é **obrigatória** para garantir coerência, rastreabilidade e eficácia das práticas de segurança.

| Nº | Capítulo | Função principal |
|----|-----------|------------------|
| 01 | [Classificação de Aplicações](/sbd-toe/sbd-manual/classificacao-aplicacoes/intro) | Define o risco e a proporcionalidade da segurança a aplicar. |
| 02 | [Requisitos de Segurança](/sbd-toe/sbd-manual/requisitos-seguranca/intro) | Estabelece o catálogo de requisitos que serve de base a todos os controlos. |
| 03 | [Threat Modeling](/sbd-toe/sbd-manual/threat-modeling/intro) | Traduz o risco em ameaças e define prioridades de mitigação. |
| 04 | [Arquitetura Segura](/sbd-toe/sbd-manual/arquitetura-segura/intro) | Define como os requisitos e ameaças se refletem nas decisões de design técnico. |
| 06 | [Desenvolvimento Seguro](/sbd-toe/sbd-manual/desenvolvimento-seguro/intro) | Garante a execução disciplinada e controlada do código seguro. |

> Estes capítulos são o **núcleo conceptual e técnico** do SbD-ToE.  
> Sem eles, não é possível aplicar de forma consistente as práticas operacionais nem demonstrar maturidade organizacional.

---

## ⚙️ Capítulos Operacionais

Os capítulos **operacionais** **implementam e automatizam** as práticas definidas nos basilares, garantindo que a segurança é **integrada no ciclo de vida** de forma contínua, mensurável e auditável. 

| Nº | Capítulo | Função principal |
|----|-----------|------------------|
| 05 | [Dependências, SBOM e SCA](/sbd-toe/sbd-manual/dependencias-sbom-sca/intro) | Garante visibilidade e controlo sobre componentes externos e cadeia de fornecimento. |
| 07 | [CI/CD Seguro](/sbd-toe/sbd-manual/cicd-seguro/intro) | Automatiza controlos e validações de segurança nos pipelines. |
| 08 | [Infraestrutura como Código (IaC)](/sbd-toe/sbd-manual/iac-infraestrutura/intro) | Aplica o SbD à gestão e automação da infraestrutura. |
| 09 | [Containers e Imagens](/sbd-toe/sbd-manual/containers-imagens/intro) | Estende as práticas de segurança à execução e ao runtime. |
| 10 | [Testes de Segurança](/sbd-toe/sbd-manual/testes-seguranca/intro) | Verifica e mede a eficácia das práticas implementadas. |
| 11 | [Deploy Seguro](/sbd-toe/sbd-manual/deploy-seguro/intro) | Garante que a entrega mantém as propriedades de segurança definidas. |
| 12 | [Monitorização e Resposta](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro) | Fecha o ciclo de feedback, assegurando deteção e melhoria contínua. |

> Estes capítulos traduzem o *Security by Design* em **execução prática**.  
> Dependem dos basilares para definir o que controlar e dos organizacionais para garantir que o processo é sustentado.

---

## 🏛️ Capítulos Organizacionais

Os capítulos **organizacionais** sustentam a aplicação e evolução do modelo SbD-ToE ao nível **humano, processual e estratégico**.  
Asseguram que as práticas se tornam parte da cultura e governação da organização.

| Nº | Capítulo | Função principal |
|----|-----------|------------------|
| 13 | [Formação e Capacitação](/sbd-toe/sbd-manual/formacao-onboarding/intro) | Promove a literacia, competências e cultura de *Security by Design*. |
| 14 | [Governança e Contratação](/sbd-toe/sbd-manual/governanca-contratacao/intro) | Garante o controlo executivo, rastreabilidade e alinhamento com políticas e contratos. |

> Estes capítulos asseguram que o SbD-ToE **é adotado, mantido e auditado** como parte integrante da gestão organizacional e não apenas como prática técnica.

---

## 🔄 Relação entre os agrupamentos

| Tipo | Função | Dependência | Resultado |
|------|---------|--------------|------------|
| 🧱 **Basilares** | Definem o *quê* e o *porquê* da segurança | — | Fundamento técnico e metodológico |
| ⚙️ **Operacionais** | Definem o *como fazer* | Dependem dos basilares | Execução verificável e automatizada |
| 🏛️ **Organizacionais** | Definem o *quem* e o *como governar* | Dependem dos dois anteriores | Sustentação e melhoria contínua |

---

## 📌 Como usar esta classificação

- Serve para **planear a adoção** do modelo SbD-ToE por fases.  
- Orienta **auditorias e medições de maturidade**, permitindo identificar lacunas estruturais.  
- Facilita a **formação** e a **priorização de esforços**, concentrando recursos nos capítulos basilares antes da expansão operacional.  
- Apoia a **rastreabilidade vertical**: do risco (cap. 01) até à governação (cap. 14).

---

## 🔗 Conclusão

A aplicação bem-sucedida do SbD-ToE requer equilíbrio entre os três níveis:

> 🧱 **Basilares** — criam o alicerce  
> ⚙️ **Operacionais** — executam o ciclo de segurança  
> 🏛️ **Organizacionais** — garantem continuidade e governação  

Juntos, formam a estrutura completa do *Security by Design – Theory of Everything*, onde **a segurança é construída por design e sustentada por cultura**.
