---
id: ameacas-mitigadas
title: Ameaças Mitigadas - Capítulo 05
description: Análise das ameaças mitigadas pelas práticas deste capítulo, com base em OSC&R, CAPEC, STRIDE, DSOMM e outros modelos
tags: [ameaças, mitigação, sbom, sca, supply-chain, dsomm, capec, oscar, ]
sidebar_position: 50

---

# 🔐 Ameaças Mitigadas - Capítulo 05: Dependências, SBOM e SCA

Este capítulo estabelece práticas de **inventário, validação, rastreabilidade e governação de bibliotecas e artefactos de terceiros**, com base em SBOMs, SCA, políticas de origem e integração com CI/CD.

> ⚠️ A ausência destas práticas representa risco direto e crítico - evidenciado por falhas de cadeia de fornecimento como SolarWinds, log4j e event-stream.

As ameaças identificadas foram analisadas com base em **OSC&R**, **CAPEC**, **BSIMM**, **OWASP Top 10**, **SSDF**, **SLSA** e **OWASP DSOMM**, com foco em práticas de mitigação concretas e controlos auditáveis.

---

## 📦 Categoria 1 - Uso de componentes vulneráveis

| Ameaça                                   | Fonte                                 | Como surge                                           | Como a prática mitiga                                                              | Controlos associados                        | 🧩 Mitigada apenas por este capítulo? |
|------------------------------------------|----------------------------------------|------------------------------------------------------|-------------------------------------------------------------------------------------|---------------------------------------------|----------------------------------------|
| Inclusão de bibliotecas com CVEs ativos  | OWASP A06 / CAPEC-469 / DSOMM (Hardening) | Falta de scanner ou inventário                      | SCA automatizado em pipeline, com bloqueios por política                           | `addon/02-analise-sca.md`                  | ✅                                     |
| Dependências desatualizadas              | BSIMM13 - SFD1.2 / OSC&R VUL-2 / DSOMM | Bibliotecas não atualizadas                         | Política formal de atualização + revisão periódica                                 | `addon/05-politica-atualizacoes.md`        | ✅                                     |
| Ausência de registo de versões           | SLSA / SSDF PW.3 / ISO 27034           | Versão da biblioteca não rastreada                  | SBOM com versão + hash em CI/CD                                                    | `addon/01-inventario-sbom.md`              | ✅                                     |
| Inclusão de bibliotecas não auditadas    | SAMM / BSIMM / DSOMM (Policy)          | Biblioteca adicionada sem processo de aprovação     | Governação formal com critérios e registo de aceitação                             | `addon/03-governanca-libs-terceiros.md`    | ✅                                     |

---

## 🔗 Categoria 2 - Rastreabilidade e visibilidade técnica

| Ameaça                                       | Fonte                                 | Como surge                                               | Como a prática mitiga                                                     | Controlos associados                          | 🧩 Mitigada apenas por este capítulo? |
|----------------------------------------------|----------------------------------------|----------------------------------------------------------|------------------------------------------------------------------------------|------------------------------------------------|----------------------------------------|
| Desconhecimento de bibliotecas utilizadas   | SSDF PW.4 / OSC&R Discovery / DSOMM (Build & Deploy) | Equipa não sabe o que está no build                      | Inventário contínuo por CI/CD e geração de SBOMs                            | `addon/01-inventario-sbom.md`                | ✅                                     |
| Falta de associação entre vulnerabilidade e artefacto | CAPEC-310 / NVD / DSOMM            | É identificada uma CVE mas não se sabe onde se aplica    | Mapeamento automático SBOM → CVE via scanner + rastreabilidade               | `addon/08-rastreabilidade-vulnerabilidades.md`| ✅                                     |
| Falta de histórico de introdução de pacotes | OSC&R Traceability / DSOMM (Governance) | Ninguém sabe quem introduziu, quando ou porquê           | Registo de origem no repositório e pipeline com tagging                     | `addon/07-controle-registos-origem.md`       | ✅                                     |

---

## 🔁 Categoria 3 - Supply Chain e proveniência de artefactos

| Ameaça                                        | Fonte                                | Como surge                                               | Como a prática mitiga                                                       | Controlos associados                        | 🧩 Mitigada apenas por este capítulo? |
|-----------------------------------------------|---------------------------------------|----------------------------------------------------------|--------------------------------------------------------------------------------|---------------------------------------------|----------------------------------------|
| Inclusão de pacotes de repositórios maliciosos| CAPEC-111 / SLSA / MITRE T1195        | npm/pypi/etc com nomes similares                         | Políticas de origem + bloqueios por allowlist + verificação de proveniência  | `addon/07-controle-registos-origem.md`      | ✅                                     |
| Dependência transitiva com componente inseguro| OWASP A06 / BSIMM / OSC&R DEP-2       | CVE não está na dependência direta                       | SCA com verificação de árvore de dependências + bloqueios recursivos         | `addon/02-analise-sca.md`                   | ✅                                     |
| Pipeline injeta versão não autenticada        | SLSA L2 / ENISA / DSOMM (Build & Deploy) | Build usa artefacto sem hash ou assinatura               | SBOM + assinatura e verificação de integridade                               | `addon/04-integracao-ci-cd.md`              | ❌ Cap. 07                             |

---

## 🚨 Categoria 4 - Falhas na gestão de exceções e aceitação de risco

| Ameaça                                      | Fonte                             | Como surge                                              | Como a prática mitiga                                                          | Controlos associados                         | 🧩 Mitigada apenas por este capítulo? |
|---------------------------------------------|------------------------------------|---------------------------------------------------------|----------------------------------------------------------------------------------|----------------------------------------------|----------------------------------------|
| CVEs ignoradas sem justificação             | CAPEC-1003 / SSDF RM.2 / DSOMM (Policy) | Biblioteca mantida mesmo após alerta                    | Processo de exceção com owner, impacto, justificação e prazo                    | `addon/09-excecoes-e-aceitacao-risco.md`     | ❌ Cap. 14                             |
| Mitigações aplicadas sem rastreio           | BSIMM13 - CMVM / SSDF RV.3        | Workaround ou patch sem rasto                            | Registo de decisão + impacto + revisão posterior em backlog                     | `addon/09-excecoes-e-aceitacao-risco.md`     | ✅                                     |
| Falta de ciclo de revisão de exceções       | NIST 800-30 / ISO 27005            | CVEs abertas por tempo indefinido                       | Ciclo de vida com reavaliação forçada por tempo ou nova versão                 | `15-aplicacao-lifecycle.md`            | ❌ Cap. 01                             |

---

## 🏛️ Categoria 5 - Ausência de governação de bibliotecas e políticas de uso

| Ameaça                                    | Fonte                              | Como surge                                           | Como a prática mitiga                                                              | Controlos associados                        | 🧩 Mitigada apenas por este capítulo? |
|-------------------------------------------|-------------------------------------|------------------------------------------------------|-------------------------------------------------------------------------------------|---------------------------------------------|----------------------------------------|
| Uso arbitrário de bibliotecas             | SAMM / BSIMM / DSOMM (Policy)       | Equipa escolhe dependências sem controlo             | Definição de critérios de aceitação + processo formal                              | `addon/03-governanca-libs-terceiros.md`     | ✅                                     |
| Bibliotecas proibidas são usadas          | SSDF PW.7 / CIS Control 16.12       | Não há mecanismo de bloqueio                         | Política de denylist/allowlist em CI/CD com enforcement automático                 | `addon/04-integracao-ci-cd.md`              | ✅                                     |
| Falta de política de substituição         | ENISA / ISO 27034 / DSOMM (Governance) | Não se sabe quando substituir bibliotecas inseguras  | Política de atualização + ciclo de vida de substituição                            | `addon/05-politica-atualizacoes.md`         | ✅                                     |

---
## Dependências emergentes e não rastreadas

| Ameaça | Fonte | Como surge | Como a prática mitiga | Controlos associados |
|-------|-------|------------|------------------------|----------------------|
| Introdução de dependência vulnerável não declarada | Supply Chain | Plugins, build tools, pipelines, code generation | Definição de fronteira SBOM + deteção de *delta* | SBOM boundary, revisão de dependências |
| Confusão de dependências | Supply Chain | Resolução implícita ou automática de pacotes | Baseline aprovada e validação de origem | SCA, validação de origem |
| Backdoor via ferramenta de build | Supply Chain | Atualização automática de tooling | Aprovação explícita de dependências emergentes | Governance de tooling |
| Drift de composição entre builds | Operacional | Mudanças não controladas entre releases | Comparação automática SBOM vs baseline | CI/CD gating |

---

## ✅ Conclusão

O Capítulo 05 mitiga um conjunto vasto de ameaças diretamente ligadas a **uso inseguro de software de terceiros**, um dos maiores vetores de ataque contemporâneos.  
A sua aplicação permite:

- Identificar e inventariar componentes com precisão;
- Avaliar vulnerabilidades antes de produção;
- Estabelecer controlo total sobre exceções e decisões técnicas;
- Reduzir risco sistémico em CI/CD e cadeia de fornecimento.

> ✅ Pelo menos **12 ameaças mapeadas são mitigadas exclusivamente por este capítulo**, e **todas as restantes dependem dele para rastreabilidade e governação efetiva**.

> 📌 Este capítulo é **obrigatório para conformidade com SLSA, SSDF, OWASP SAMM, ISO 27034, CIS Controls v8 e DSOMM**, cobrindo os domínios de `Build & Deploy`, `Policy`, `Verification` e `Governance`.

