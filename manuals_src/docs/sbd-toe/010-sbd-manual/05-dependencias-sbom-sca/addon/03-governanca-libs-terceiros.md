---
description: Práticas de controlo, aprovação e rastreabilidade de bibliotecas externas
  e pacotes de terceiros
id: governanca-libs-terceiros
tags:
- checklist
- dependencias
- governance
- policy
- sbom
- sca
- supply-chain
title: Governaça de Bibliotecas e Componentes de Terceiros
---


# 📄 Governaça de Bibliotecas e Componentes de Terceiros

## 🌟 Objetivo

Estabelecer regras claras e verificáveis para a **utilização, aprovação, substituição e rastreabilidade** de bibliotecas e componentes de terceiros em aplicações desenvolvidas internamente.

> 🚨 Muitos incidentes de supply chain têm origem em bibliotecas maliciosas, abandonadas ou não verificadas. Este controlo é fundamental.

---

## 🔢 Princípios de governaça

1. **Repositórios permitidos** devem ser explicitamente definidos e controlados.
2. Toda biblioteca deve ter:
   - Manutenção ativa
   - Licença compatível
   - Popularidade/comunidade mínima validada
3. Bibliotecas com CVEs ativos **não podem ser utilizadas sem exceção formalizada**.
4. O uso de bibliotecas "exóticas" ou de autor único deve ser justificado.

---

## 🚀 Processo de aprovação

| Etapa                     | Ação                                                     | Artefacto                  |
|--------------------------|-----------------------------------------------------------|-----------------------------|
| Solicitação de nova lib   | Dev submete nome, versão, função, origem             | Formulário / issue          |
| Análise de segurança       | AppSec ou revisor verifica: CVEs, origem, histórico      | Comentário com aprovação ou veto |
| Validação legal           | (opcional) Verifica compatibilidade de licença          | Lista de licenças aprovadas |
| Aprovação formal          | Registo da decisão e prazo de validade (se aplicável)    | Repositório de aprovações     |

> Este processo pode ser ligeiro (via Pull Request) ou formalizado (via ferramenta de registo).

---

## 🔎 Critérios de aceitação

| Critério                         | Recomendado? | Justificativa                                   |
|----------------------------------|--------------|--------------------------------------------------|
| Licença open source permissiva   | Sim          | Ex: MIT, Apache 2.0                             |
| Manteído ativamente (>1 ano)    | Sim          | Commits recentes e versões atualizadas          |
| Comunidade ativa (issues/PRs)   | Sim          | Evita bibliotecas abandonadas                   |
| Utilização em outros projetos   | Sim          | Reforça confiança e estabilidade                |
| Presença de testes ou CI         | Sim          | Indica maturidade do projeto                    |
| Código obfuscado ou minificado   | Não          | Evitar dependências opacas                      |
| Origem desconhecida ou suspeita  | Não          | Excluir fontes não verificadas                   |

---

## 📝 Registo de decisões

Cada biblioteca deve poder ser rastreada até uma decisão de aprovação. Sugere-se registar:

- Nome, versão, hash do pacote
- Justificação de utilização
- Resultado da análise SCA
- Aprovação ou exceção
- Responsável e data

> Este registo pode estar num ficheiro `.yaml`, num repositório Git, Confluence, Jira, etc.

---

## 📎 Referências cruzadas

| Documento                   | Relação com a governaça                            |
|-----------------------------|---------------------------------------------------------|
| `01-inventario-sbom.md`     | Controlo do que está a ser utilizado                   |
| `02-analise-sca.md`         | Base para aceitação ou bloqueio                      |
| `09-excecoes-e-aceitacao-risco.md` | Justificações formais para desvios               |

---

> 🔍 A governaça de dependências é um dos pilares da segurança moderna, especialmente em ambientes expostos ou com obrigações regulatórias (NIS2, CRA, ISO 27001).
