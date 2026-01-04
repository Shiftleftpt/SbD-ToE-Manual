---
id: intro
title: Infraestrutura como Código (IaC)
description: Práticas de segurança para definição, validação e gestão de infraestrutura como código
tags: [infraestrutura, iac, terraform, segurança, automatização, DSOMM, SAMM, SLSA, SSDF]
sidebar_position: 0
---

:::tip Capítulo Operacional
Este capítulo é considerado **operacional** no modelo *Security by Design – Theory of Everything (SbD-ToE)*.  
A sua função é **aplicar, automatizar e validar** as práticas definidas nos capítulos basilares, garantindo a sua execução contínua e mensurável.  

Os capítulos operacionais implementam o SbD-ToE em contextos técnicos específicos, traduzindo prescrições basilares em práticas de **execução verificável**, com evidência técnica, rastreabilidade e governação.
:::

---

## ⚠️ Nota Canónica — Infraestrutura como Processo Automatizado

A infraestrutura moderna é definida, validada e aplicada através de **processos altamente automatizados**, frequentemente apoiados por mecanismos de **geração, sugestão ou normalização automática de código e configuração**.

No contexto de IaC, esta realidade introduz riscos específicos que devem ser explicitamente controlados:

- **Sugestão não equivale a decisão**: mecanismos automáticos podem propor alterações, mas a decisão de impacto (`plan` e sobretudo `apply`) é sempre **humana, rastreável e formalmente aprovada**.
- **Plausibilidade não equivale a evidência**: código aparentemente correto ou “bem explicado” não substitui **evidência de execução real**, nomeadamente `plan` efetivo, diffs auditáveis e artefactos versionados.
- **Reprodutibilidade é obrigatória**: a segurança do IaC exige determinismo — versões de providers, módulos, políticas e ambientes de execução devem permitir reconstrução fiel e análise retrospetiva.
- **O contexto de infraestrutura é um ativo crítico**: templates, topologias, permissões, naming e parâmetros operacionais constituem informação sensível; qualquer dependência externa ao controlo direto da organização deve ser tratada como **dependência de supply chain**, com risco potencial de exfiltração.

Estas premissas são estruturais e aplicam-se **independentemente das ferramentas utilizadas**.

---

# Segurança em Infraestrutura como Código (IaC)

A definição de infraestruturas através de código (Terraform, Pulumi, CloudFormation, etc.) tornou-se prática comum.  
Esta abordagem trouxe ganhos claros de rapidez, consistência e escalabilidade. Mas, como qualquer tecnologia transformadora, trouxe também **novos riscos**: erros de configuração, permissões excessivas, uso de módulos maliciosos ou ambientes mal segregados.

Este capítulo prescreve como **tratar o IaC como software crítico** — com requisitos, testes, ciclo de vida e auditoria.  
A ideia central é simples: se o IaC define a base onde o software corre, então **a sua segurança determina a segurança de tudo o resto**.

---

## 🧭 O que cobre tecnicamente

Na prática, falar em segurança de IaC significa proteger cada camada, desde o primeiro ficheiro até ao último recurso aplicado em produção.  
As áreas cobertas incluem:

- Templates e scripts de provisionamento (Terraform, Pulumi, CloudFormation, etc.)  
- Automatização de ambientes via pipelines CI/CD  
- Validação e controlo de configuração de recursos cloud e on-prem  
- Deteção de más práticas, permissões excessivas ou exposição indevida  
- Origem confiável, integridade e versionamento de módulos e dependências  
- Rastreabilidade completa de alterações (ficheiro → recurso → ambiente)  
- Enforcement automático e bloqueante de políticas de segurança  
- Proteção de contexto e minimização de informação sensível em processos automatizados  

---

## 📌 O que deve ser feito

Para transformar recomendações em práticas de engenharia aplicáveis, a organização deve garantir, no mínimo:

1. Utilização de ferramentas declarativas, determinísticas e reprodutíveis  
2. **Segregação rigorosa e versionamento** de ambientes  
3. **Validações automáticas e bloqueantes** (lint, segurança, policies) antes de qualquer `apply`  
4. Controlo estrito da origem, integridade e versão dos módulos utilizados  
5. **Revisão formal e humana do `plan`**, com critérios de impacto claramente definidos  
6. Garantia de **rastreabilidade completa** entre código, recursos e ambientes  
7. **Enforcement automático** de políticas de segurança no pipeline  
8. Versionamento, retenção e, quando aplicável, assinatura de todos os artefactos relevantes (`plan`, relatórios, manifests)  

---

## ⚙️ Como deve ser feito

A execução depende de ferramentas práticas e da sua integração disciplinada em pipelines controlados.  
Não basta confiar na experiência individual — é necessário **automatizar, restringir e auditar**:

- Ferramentas de scanning: `tfsec`, `checkov`, `kics`, `terrascan`  
- Enforcement de políticas: `OPA`, `Sentinel`, `Conftest`  
- Pipelines CI/CD obrigatórios para validação antes de qualquer alteração efetiva  
- Catálogo de módulos internos certificados, pinados por versão e com origem auditável  
- Dashboards de validação automatizada por ambiente  
- Gestão centralizada e rastreável de exceções, com aprovação formal e validade temporal  

---

## 📆 Quando aplicar

Os controlos devem ser aplicados ao longo de todo o ciclo de vida do IaC.  
Ignorar um momento crítico significa permitir acumulação silenciosa de risco:

- Sempre que existam alterações a templates ou scripts IaC  
- Durante code review e pull/merge requests de infraestrutura  
- Antes da execução de pipelines que afetem ambientes reais  
- Ao integrar ou atualizar módulos externos  
- Em auditorias periódicas de conformidade e *drift detection*  

---

## 👥 Quem está envolvido

A proteção de IaC é uma responsabilidade partilhada, exigindo coordenação entre funções técnicas e de governação:

| Papel/Função      | Contributo principal |
|-------------------|----------------------|
| **DevOps / Infra** | Escrita, revisão e manutenção de templates IaC; gestão de pipelines |
| **AppSec**         | Definição de políticas, scanners obrigatórios e critérios de bloqueio |
| **Arquitetura**    | Validação de padrões técnicos e desenho seguro de ambientes |
| **Produto / GRC**  | Aprovação de riscos, exceções e validação de rastreabilidade |

---

## 🎯 Para quê

Investir na segurança de IaC é investir na **confiabilidade da fundação onde todas as aplicações assentam**.  
Os objetivos são claros:

- Prevenir configurações inseguras ou permissões excessivas  
- Assegurar consistência, reprodutibilidade e rastreabilidade das infraestruturas  
- Demonstrar conformidade técnica em auditorias  
- Reduzir risco de *drift*, erro humano e ataques à cadeia de fornecimento  

---

## 📜 Políticas Organizacionais Relevantes

Políticas formais garantem que as práticas não dependem apenas da disciplina individual, mas de regras coletivas, claras e auditáveis.

| Política organizacional           | Obrigatória | Aplicação                     | Conteúdo mínimo |
|----------------------------------|-------------|-------------------------------|-----------------|
| Política de IaC Seguro            | Sim         | Todos os projetos IaC         | Padrões técnicos, segregação de ambientes, pipelines obrigatórios, enforcement de policies |
| Política de Gestão de Módulos IaC | Recomendado | DevOps/Infra, Arquitetura     | Uso de módulos verificados, pinagem de versão, auditoria de origem |
| Política de Rastreabilidade IaC   | Sim         | DevOps, GRC                   | Mapeamento ficheiro → recurso → ambiente, histórico auditável |
| Política de Aprovação de `plan`   | Sim         | DevOps, AppSec                | Revisão humana obrigatória, critérios de impacto, rollback e SoD |

Na versão impressa, consultar o **Anexo de Políticas Organizacionais do Manual**, onde estas políticas estão consolidadas transversalmente.
