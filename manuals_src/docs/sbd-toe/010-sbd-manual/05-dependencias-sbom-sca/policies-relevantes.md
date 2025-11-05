---
id: policies-relevantes
title: Policies
description: Políticas organizacionais que sustentam a aplicação prática deste capítulo
tags: [policy, organizacional, sbom, sca, dependencias]
sidebar_position: 60

---

# 🏛️ Políticas Organizacionais - Dependências, SBOM e SCA

A adoção eficaz do Capítulo 05 - Dependências, SBOM e SCA - exige a existência de **políticas organizacionais formais** que **regulem e sustentem a gestão segura de bibliotecas de terceiros, análise de composição de software e uso de SBOMs**.

---

## 📌 Nota fundamental

> ⚠️ As práticas técnicas descritas neste capítulo (inventário, análise SCA, integração de SBOM, registos de origem, gestão de exceções) **devem estar legitimadas por políticas organizacionais aprovadas**.

Estas políticas:

- Tornam **obrigatória e auditável** a gestão de dependências e artefactos externos;
- Permitem que decisões sobre atualização, bloqueio ou aceitação de riscos **sigam critérios definidos e consistentes**;
- São **referência obrigatória** em processos de build, CI/CD, gestão de vulnerabilidades e auditoria.

> 🧩 Este capítulo **operacionaliza as políticas formais** de dependências e componentes externos. A política define, o capítulo executa.

> 📎 A existência destas políticas é **explicitamente recomendada** por frameworks como **NIST SSDF**, **OWASP SAMM**, **SLSA** e **BSIMM**.

---

## 🧾 Políticas recomendadas

| Nome da Política                                      | Obrigatória? | Aplicação                                   | Resumo do conteúdo necessário |
|-------------------------------------------------------|--------------|----------------------------------------------|-------------------------------|
| Política de Gestão de Dependências e Bibliotecas      | ✅ Sim       | Todos os projetos com código de terceiros    | Regras para uso, aprovação, versionamento, atualização e bloqueio de dependências. |
| Política de Integração e Gestão de SBOM               | ✅ Sim       | Pipelines de build, release e auditoria      | Formato exigido (CycloneDX/SPDX), frequência de geração, artefactos obrigatórios e retenção. |
| Política de Avaliação de Vulnerabilidades em Componentes de Terceiros (SCA) | ✅ Sim       | Projetos com entrega para produção           | Obrigatoriedade de análise SCA, critérios de severidade, ciclo de resposta e registo de exceções. |
| Política de Repositórios e Registos de Origem         | ⚠️ Opcional  | CI/CD, build agents, ambientes de execução   | Lista de registries autorizados, mirrors internos, políticas de fallback e caching. |
| Política de Justificação de Vulnerabilidades Aceites  | ✅ Sim       | Quando um CVE é aceite sem patch imediato     | Requisitos para justificar exceções, aprovação formal, revalidação periódica. |
| Política de Atualização Contínua de Dependências      | ⚠️ Opcional  | Projetos com ciclos curtos e contínuos       | Frequência de atualização, uso de ferramentas automáticas, rastreabilidade de alterações. |

---

## 📎 Correspondência com frameworks normativas

| Framework            | Requisitos cobertos pelas políticas acima                                                                 |
|---------------------|------------------------------------------------------------------------------------------------------------|
| **NIST SSDF**        | PS.3 (Third-Party Components), RV.3 (Vulnerability Management), RV.5 (SBOM Generation)                     |
| **SLSA v1.0**        | Requirements on provenance, dependency control and build integrity                                         |
| **OWASP SAMM**       | Design > Threat Assessment, Implementation > Environment Hardening, Verification > Security Testing       |
| **BSIMM13**          | SFD1.3 (Track open source usage), CMVM2.2 (Detect malicious packages), SE1.4 (Scan for vulnerabilities)    |
| **CIS Controls v8**  | Control 2 (Inventory and Control of Software Assets), Control 16 (Application Software Security)           |

---

## 📋 Estrutura sugerida de cada política

Cada política organizacional deve conter, no mínimo:

- **Objetivo e âmbito** da política;
- **Âmbito de aplicação**: quem, onde e quando se aplica;
- **Regras e critérios obrigatórios** (ex: quando analisar, como aprovar dependência, formato de SBOM);
- **Papéis e responsabilidades** (segurança, produto, dev, operações, CI/CD);
- **Exigência de documentação e rastreabilidade**;
- **Periodicidade de revisão da política em si** (ex: anual);
- **Exigência de rastreabilidade entre política, prática e evidência técnica** (ex: ligação SBOM ↔ build ↔ release ↔ findings).

---

## ✅ Recomendações finais

- Estas políticas devem ser **aprovadas pela área de segurança e desenvolvimento**;
- Devem estar **documentadas, divulgadas e acessíveis** a todas as equipas técnicas;
- A sua existência é condição essencial para garantir **controlo formal da cadeia de dependências e integridade de builds**;
- A sua aplicação deve estar **automatizada** sempre que possível, integrada em pipelines e validações de release.

> 📌 Exemplos de templates de política poderão ser incluídos em ficheiros `60-*.md` complementares em versões futuras.
