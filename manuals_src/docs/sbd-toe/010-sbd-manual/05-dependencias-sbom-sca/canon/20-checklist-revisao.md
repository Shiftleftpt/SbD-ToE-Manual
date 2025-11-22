---
description: Verificação binária da aplicação das práticas prescritas no Capítulo
  05
id: checklist-revisao
sidebar_label: Checklist de Revisão
sidebar_position: 20
tags:
- checklist
- controlo
- dependencias
- desenvolvimento
- sbom
- sca
- supply-chain
title: Checklist - Dependências, SBOM e SCA
---



# ✅ Checklist de Revisão Periódica - Dependências, SBOM e SCA

Este checklist aplica-se a todas as aplicações que utilizem bibliotecas de terceiros, SDKs, pacotes open-source ou artefactos binários.
Serve como instrumento de verificação binária e auditável da **adoção prática das prescrições do Capítulo 05**, permitindo:

* Controlo contínuo da aplicação de práticas de SCA e SBOM
* Verificação por projeto em momentos-chave do ciclo de vida
* Geração de indicadores operacionais agregáveis por equipa ou organização

> 🗓️ **Recomenda-se a sua revisão a cada release, alteração de dependência ou exceção de segurança**, conforme indicado no `15-aplicacao-lifecycle.md`.

---

## 📋 Itens de Verificação

Todos os itens abaixo devem ser verificados com base em **evidência objetiva** de aplicação prática das práticas do Capítulo 05.

| Item                                                                                               | Verificado? |
| -------------------------------------------------------------------------------------------------- | ----------- |
| Existe um SBOM gerado automaticamente por build                                                    | ☐           |
| O SBOM está versionado e ligado ao artefacto correspondente                                        | ☐           |
| O SBOM inclui dependências transitivas e está em formato normativo (ex: CycloneDX)                 | ☐           |
| Existe scanner SCA integrado no pipeline CI/CD                                                     | ☐           |
| O pipeline bloqueia a entrega se existirem findings críticos não justificados                      | ☐           |
| Relatórios SCA estão acessíveis e associados a versões/releases                                    | ☐           |
| Existe uma política formal de uso e aprovação de bibliotecas                                       | ☐           |
| As exceções a vulnerabilidades conhecidas são justificadas com prazo e impacto documentado         | ☐           |
| As exceções vencidas são periodicamente revistas e renovadas ou eliminadas                         | ☐           |
| Existe política de atualização de bibliotecas com TTL definido                                     | ☐           |
| Há mecanismo para identificar e notificar bibliotecas desatualizadas (ex: bot, CI, tarefa)         | ☐           |
| As atualizações passam por validação (scanner + CI) antes de serem aplicadas                       | ☐           |
| Apenas repositórios autorizados são usados no build (ex: proxy interno, repositório privado)       | ☐           |
| O fallback para registries externos está controlado e auditado                                     | ☐           |
| Existe rastreabilidade entre findings, exceções e artefactos entregues (ex: ligação CVE → release) | ☐           |
| Todas as práticas estão documentadas e rastreáveis no repositório ou pipeline                      | ☐           |


---

## 🔄 Integração Operacional

* Este checklist pode ser integrado em **pipelines, revisões de PR, gates de release ou auditorias técnicas**.
* Os resultados podem ser rastreados por commit, por release ou por artefacto.
* Cada item deve ser validado com **evidência objetiva** (ex: ficheiros `.sbom.json`, relatórios, comentários de PR, issues).

> ⚠️ Em caso de resposta negativa, deve existir exceção formal aprovada e documentada conforme o modelo de exceções do capítulo.

---

## ✅ Conformidade e KPI

* A validação deste checklist permite declarar **conformidade com o Capítulo 05 - Dependências, SBOM e SCA**.
* A contagem de respostas afirmativas pode ser usada para **medir o grau de adoção das práticas prescritas**.
* Este resultado pode ser agregado por equipa, domínio ou organização como **indicador de maturidade operacional**.

> 📌 Este mecanismo operacional está alinhado com o modelo de controlo contínuo e rastreabilidade definido no SbD-ToE.
