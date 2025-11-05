---
id: intro
title: Infraestrutura como Código (IaC)
description: Práticas de segurança para definição, validação e gestão de infraestrutura como código
tags: [infraestrutura, iac, terraform, segurança, automatização, DSOMM, SAMM, SLSA, SSDF]
sidebar_position: 0
---
import Badge from '@site/src/components/Badge';

:::tip Capítulo Operacional
Este capítulo é considerado **operacional** no modelo *Security by Design – Theory of Everything (SbD-ToE)*.  
A sua função é **aplicar, automatizar e validar** as práticas definidas nos capítulos basilares, garantindo a sua execução contínua e mensurável.  

Os capítulos operacionais implementam o SbD-ToE em contextos técnicos específicos, incluindo:
- **Gestão de dependências e SBOM/SCA** (Cap. 05)  
- **Pipelines CI/CD e automação de controlo** (Cap. 07)  
- **Infraestrutura como Código (IaC)** (Cap. 08)  
- **Containers e imagens seguras** (Cap. 09)  
- **Testes de segurança e validação técnica** (Cap. 10)  
- **Deploy seguro, observabilidade e resposta** (Cap. 11 – 12)  

Estes capítulos traduzem as prescrições basilares em práticas de **execução verificável**, promovendo a **integração contínua da segurança** ao longo do ciclo de vida do software.
:::


<div style={{ display: 'flex', flexWrap: 'wrap', gap: '0.5rem', marginBottom: '1rem' }}>
  
  <Badge color="info">SAMM: 2 / 3</Badge>
  <Badge color="info">BSIMM: CMVM1.1, CMVM2.3, CP1.2</Badge>
  <Badge color="info">SSDF: PW.5, CM.1, PS.2, PW.6</Badge>
  <Badge color="info">SLSA: Nível 2 / 4</Badge>
  <Badge color="info">DSOMM: 3 / 4 (média)</Badge>
  <a href="./achievable-maturity" style={{ marginLeft: 'auto', fontSize: '0.9rem' }}>📄 Ver análise de maturidade</a>
</div>

# Segurança em Infraestrutura como Código (IaC)

A definição de infraestruturas através de código (Terraform, Pulumi, CloudFormation, etc.) tornou-se prática comum.  
Esta abordagem trouxe ganhos claros de rapidez, consistência e escalabilidade. Mas, como qualquer tecnologia transformadora, trouxe também **novos riscos**: erros de configuração, permissões excessivas, uso de módulos maliciosos ou ambientes mal segregados.  

Este capítulo prescreve como **tratar o IaC como software crítico** - com requisitos, testes, ciclo de vida e auditoria.  
A ideia central é simples: se o IaC define a base onde o software corre, então **a sua segurança determina a segurança de tudo o resto**.

---

## 🧭 O que cobre tecnicamente

Na prática, falar em segurança de IaC significa proteger cada camada, desde o primeiro ficheiro até ao último recurso aplicado em produção.  
As áreas cobertas incluem:

- Templates e scripts de provisionamento (Terraform, Pulumi, CloudFormation, etc.)  
- Automatização de ambientes via pipelines CI/CD  
- Validação e controlo de configuração de recursos cloud/on-prem  
- Deteção de más práticas, permissões excessivas ou exposição indevida  
- Origem confiável de módulos e dependências  
- Rastreabilidade e versionamento de alterações  
- Enforcement automático de políticas de segurança  

---

## 📌 O que deve ser feito

Para transformar recomendações em práticas de engenharia aplicáveis, a organização deve garantir um conjunto mínimo de passos:

1. Utilizar ferramentas declarativas e reprodutíveis para provisionamento  
2. Garantir **segregação e versionamento** de ambientes  
3. Aplicar **validações automáticas** (lint, segurança, policies) antes do deploy  
4. Controlar a origem e versão dos módulos utilizados  
5. Implementar **revisão formal de `plan`** antes de qualquer `apply`  
6. Garantir **rastreabilidade ficheiro → recurso → ambiente**  
7. Assegurar **enforcement automático** de políticas no pipeline  
8. Versionar e assinar todos os artefactos relevantes (`plan`, `apply`, manifests)  

---

## ⚙️ Como deve ser feito

A execução depende de ferramentas práticas e da sua integração disciplinada em pipelines.  
Não basta confiar na experiência da equipa - é preciso **automatizar e auditar**:

- Ferramentas de scanning: `tfsec`, `checkov`, `kics`, `terrascan`  
- Enforcement: `OPA`, `Sentinel`, `Conftest`  
- Pipelines CI/CD obrigatórios para validação antes do `apply`  
- Módulos internos certificados e pinados por versão  
- Dashboards de validação automatizada por ambiente  
- Gestão centralizada de exceções, com aprovação formal  

---

## 📆 Quando aplicar

Os controlos devem ser aplicados ao longo de todo o ciclo de vida do IaC.  
Ignorar um momento crítico significa abrir a porta a falhas acumuladas:

- Sempre que houver alterações a templates ou scripts IaC  
- Durante code review e PRs de infraestruturas  
- Antes de execução de pipelines que afetem ambientes reais  
- Ao integrar novos módulos externos  
- Em auditorias periódicas de conformidade  

---

## 👥 Quem está envolvido

A proteção de IaC é uma responsabilidade partilhada, que exige alinhamento entre várias funções.  
Cada papel tem contributos distintos:

| Papel/Função    | Contributo principal |
|-----------------|-----------------------|
| **DevOps/Infra** | Escrita e revisão de templates IaC; gestão de pipelines |
| **AppSec**       | Definir políticas, scanners obrigatórios e gates de risco |
| **Arquitetura**  | Validar padrões técnicos e desenho seguro de ambientes |
| **Produto/GRC**  | Aprovar riscos associados e validar rastreabilidade |

---

## 🎯 Para quê

Investir na segurança de IaC é investir na **confiabilidade da fundação onde todas as aplicações assentam**.  
Os objetivos são claros:

- Prevenir configurações inseguras ou permissões excessivas  
- Assegurar consistência e rastreabilidade das infraestruturas  
- Demonstrar conformidade em auditorias  
- Reduzir risco de *drift* e ataques à cadeia de fornecimento  

---

## 📜 Políticas Organizacionais Relevantes

Políticas formais garantem que as práticas não dependem apenas da disciplina individual, mas de regras coletivas, claras e auditáveis.

| Política organizacional           | Obrigatória | Aplicação         | Conteúdo mínimo |
|----------------------------------|-------------|-------------------|-----------------|
| Política de IaC Seguro            | Sim         | Todos os projetos IaC | Padrões de naming, segregação de ambientes, pipelines obrigatórios, enforcement de policies |
| Política de Gestão de Módulos IaC | Recomendado | DevOps/Infra, Arquitetura | Uso de módulos internos ou verificados, pinagem de versão, auditoria de origem |
| Política de Rastreabilidade IaC   | Sim         | DevOps, GRC       | Mapeamento ficheiro→recurso, versionamento, histórico auditável |
| Política de Aprovação de `plan`   | Sim         | DevOps, AppSec    | Revisão e aprovação antes de `apply`, critérios de impacto e rollback |

Na versão impressa, consultar o **Anexo de Políticas Organizacionais do Manual**, onde estas políticas estão consolidadas transversalmente.

---
