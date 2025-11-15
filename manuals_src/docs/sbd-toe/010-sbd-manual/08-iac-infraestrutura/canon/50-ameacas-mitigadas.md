---
id: ameacas-mitigadas
title: Ameaças Mitigadas - Infraestrutura como Código (IaC)
sidebar_position: 50
description: Ameaças específicas mitigadas pelas práticas prescritas no capítulo, com base em fontes como OSC&R, CAPEC e SSDF.
tags: [ameaças, mitigação, segurança, iac, osc&r, capec, ssdf]
---

# 🔐 Ameaças Mitigadas - Capítulo 08: IaC e Infraestrutura como Código

Este capítulo define práticas seguras para projetos de **Infraestrutura como Código (IaC)**, incluindo: controlo de módulos, validações de segurança, enforcement em CI/CD, rastreabilidade de alterações e gestão de exceções.

> As ameaças mitigadas são especialmente críticas por se tratarem de **artefactos que gerem ambientes de produção** - a sua falha representa risco direto à confidencialidade, integridade e disponibilidade do sistema.

---

## ⚙️ Categoria 1 – Erros de configuração e falhas de validação

| Ameaça                                         | Fonte                                 | Como surge                                                | Como a prática mitiga                                                              | Controlos associados                            | 🧩 Mitigada apenas por este capítulo? |
|-----------------------------------------------|----------------------------------------|-----------------------------------------------------------|-------------------------------------------------------------------------------------|--------------------------------------------------|----------------------------------------|
| Defaults inseguros ou permissivos             | OSC&R MIS-3 / STRIDE (Elevation)      | Recursos criados sem configuração explícita               | Regras de validação automática (ex: tfsec, checkov) com enforcement                | `addon/02-validacoes-e-checks.md`               | ✅                                     |
| Configurações sem validação                   | CAPEC-34 / MITRE T1578                | Código IaC aplicado sem checks prévios                    | Integração de validadores no pipeline com bloqueio de execuções inseguras         | `addon/06-controle-enforcement.md`              | ✅                                     |
| Campos críticos deixados em branco ou default | SSDF PW.5 / ISO 27005 / DSOMM         | Tags, políticas, rotas sem definição                      | Políticas obrigatórias de tagging e rastreabilidade                               | `addon/07-rastreabilidade-e-tags.md`            | ✅                                     |
| Ambientes inconsistentes entre execuções      | DSOMM (Drift Detection)               | Mudanças manuais ou drift após `apply`                    | Ciclo forçado de validação, recomendações de detecção de drift                    | `addon/06`, `addon/30-recomendacoes-avancadas`  | ⚠️ Parcial                             |

---

## 🏗️ Categoria 2 – Falhas na definição e controlo de arquitetura de IaC

| Ameaça                                        | Fonte                               | Como surge                                           | Como a prática mitiga                                                             | Controlos associados                        | 🧩 Mitigada apenas por este capítulo? |
|-----------------------------------------------|--------------------------------------|------------------------------------------------------|------------------------------------------------------------------------------------|---------------------------------------------|----------------------------------------|
| Uso de módulos inseguros ou sem validação     | OSC&R DEP-2 / OWASP IaC / DSOMM     | Reutilização de código sem controlo de qualidade     | Governação formal com critérios de aceitação de módulos                          | `addon/03-governanca-modulos.md`            | ✅                                     |
| Hardcoded de parâmetros críticos              | STRIDE / CAPEC-137 / DSOMM          | Parâmetros como endpoints, keys, portas fixos        | Controlo com regras e linting IaC                                                  | `addon/02-validacoes-e-checks.md`           | ✅                                     |
| Ambientes inseguros provisionados por erro    | BSIMM Deployment / SLSA / DSOMM     | IaC aplica em produção sem validação ou owner        | Ciclo de vida forçado e controlo de alterações com regras de approval             | `addon/01-planeamento-e-controle.md`        | ✅                                     |

---

## 🔐 Categoria 3 – Exposição de dados, chaves ou permissões excessivas

| Ameaça                                        | Fonte                                     | Como surge                                          | Como a prática mitiga                                                            | Controlos associados                        | 🧩 Mitigada apenas por este capítulo? |
|-----------------------------------------------|--------------------------------------------|-----------------------------------------------------|-----------------------------------------------------------------------------------|---------------------------------------------|----------------------------------------|
| Provisionamento com permissões excessivas     | OSC&R MIS-3 / STRIDE / DSOMM              | Políticas de IAM mal configuradas                  | Validação obrigatória com políticas de permissões mínimas definidas               | `addon/04-principios-sbd-iac.md`            | ✅                                     |
| Falta de tags de classificação de dados       | SSDF / ISO 27034 / DSOMM                  | Dados sensíveis sem rastreio por ambiente ou owner | Política de tagging com eixos de criticidade e sensibilidade                     | `addon/07-rastreabilidade-e-tags.md`        | ✅                                     |
| Uso de dados reais em ambientes de teste      | NIST 800-53 / ISO 27001 / DSOMM           | Variáveis partilhadas, cópias de dados reais       | Controlo de separação de ambientes e validação explícita de escopos               | `addon/01-planeamento-e-controle.md`        | ✅                                     |
| Segredos hardcoded ou mal geridos             | DSOMM / CAPEC-798                         | `key = "..."` embebida em código                   | Enforcement de boas práticas + segregação e injeção segura via pipeline           | `addon/06-controle-enforcement.md`          | ✅                                     |

---

## 🔁 Categoria 4 – Falta de rastreabilidade e visibilidade de alterações

| Ameaça                                     | Fonte                                 | Como surge                                          | Como a prática mitiga                                                                | Controlos associados                          | 🧩 Mitigada apenas por este capítulo? |
|--------------------------------------------|----------------------------------------|-----------------------------------------------------|---------------------------------------------------------------------------------------|------------------------------------------------|----------------------------------------|
| Alterações aplicadas sem revisão           | BSIMM Code Review / SSDF RM.2         | CI aplica sem controlo do que mudou                | Políticas de aprovação por PR com evidência e rastreio por tag                       | `addon/01-planeamento-e-controle.md`          | ✅                                     |
| Falta de owner e accountability            | OWASP IaC / OSC&R / DSOMM             | Recursos sem owner designado                       | Mapeamento obrigatório de owner por módulo ou tag                                    | `addon/07-rastreabilidade-e-tags.md`          | ✅                                     |
| Reutilização de módulos sem tracking       | OSC&R / SAMM Implementation           | Reuso de código sem referência nem origem          | Política de registo e versionamento por módulo compartilhado                         | `addon/03-governanca-modulos.md`              | ✅                                     |

---

## 📉 Categoria 5 – Falta de enforcement e exceções não geridas

| Ameaça                                     | Fonte                                   | Como surge                                      | Como a prática mitiga                                                            | Controlos associados                        | 🧩 Mitigada apenas por este capítulo? |
|--------------------------------------------|------------------------------------------|-------------------------------------------------|-----------------------------------------------------------------------------------|---------------------------------------------|----------------------------------------|
| Aplicação de alterações inseguras por bypass | SSDF PW.7 / CAPEC-1003 / DSOMM         | Skipping de validadores via flags ou commit     | Enforcement obrigatório + política formal de exceções                            | `addon/06-controle-enforcement.md`          | ✅                                     |
| Justificações informais ou inexistentes     | SSDF RM.3 / ISO 27005 / DSOMM          | Ninguém sabe por que uma regra foi desativada   | Registo formal de exceções com owner, motivo, prazo                              | `addon/09-gestao-excecoes.md`               | ✅                                     |
| Ambientes provisionados com exceções acumuladas | OWASP IaC / BSIMM13 / DSOMM          | Sem política de revisão ou limpeza de exceções  | Ciclo de vida com reapreciação e auditoria contínua                              | `15-aplicacao-lifecycle.md`           | ❌ Cap. 01                             |

---

## ✅ Conclusão

O Capítulo 08 oferece defesa abrangente contra ameaças específicas a projetos de IaC, mitigando falhas que, se exploradas, podem comprometer **a segurança da infraestrutura completa de execução de software**.

> ✅ Pelo menos **12 ameaças são mitigadas exclusivamente por este capítulo**, incluindo: validação de IaC, governação de módulos, rastreabilidade por tags, controlo de segredos e enforcement de regras aplicadas ao ciclo de vida da infraestrutura.
