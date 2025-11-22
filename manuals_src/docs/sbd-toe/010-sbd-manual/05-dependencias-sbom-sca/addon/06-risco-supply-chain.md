---
id: risco-supply-chain
title: Ameaças à Cadeia de Fornecimento (Supply Chain)
description: Tipos de ataque via dependências e práticas para deteção e mitigação
tags: [dependencias, risks, sbom, sca, supply-chain]
---

# 🚨 Ameaças à Cadeia de Fornecimento (Supply Chain)

## 🌟 Objetivo

Identificar os principais vetores de ataque na cadeia de fornecimento de software, com ênfase em dependências externas, e estabelecer contramedidas técnicas e organizacionais eficazes.

> ⚠️ Os ataques de supply chain são dos mais críticos na atualidade, pois exploram a **confiança implícita em pacotes terceiros** usados em build ou runtime.

---

## 🔧 Tipos comuns de ataque

| Tipo de Ameaça            | Descrição                                                        | Exemplo real                    |
|----------------------------|------------------------------------------------------------------|---------------------------------|
| **Typosquatting**          | Pacote com nome parecido ao de um famoso                        | `lodashs` em vez de `lodash`    |
| **Dependency Confusion**  | Resolver pacotes do registo público em vez do privado            | `internal-lib` publicado externamente |
| **Hijack de conta**        | Conta de dev comprometida publica update malicioso             | `ua-parser-js` (2021)           |
| **Pacote abandonado**      | Biblioteca sem manutenção usada como vetor                     | `event-stream` (2018)           |
| **Code Injection**         | Payload malicioso no `postinstall` ou script                    | `node-ipc` (2022)               |

---

## 🔐 Estratégias de mitigação

### 1. **Verificação de origem**

- Usar repositórios internos, proxies ou mirrors
- Bloquear instalação de pacotes fora de origem aprovada

### 2. **Monitorização de nomes**

- Auditar novos pacotes adicionados ao `package.json`, `pom.xml`, etc.
- Usar alertas de typosquatting com ferramentas (ex: Socket.dev, npm-proxy-check)

### 3. **Revisão de scripts embutidos**

- Detetar `postinstall`, `preinstall`, `install` com scripts executáveis
- Usar flags como `--ignore-scripts` quando apropriado

### 4. **Políticas de aprovação e timeout**

- Exigir revisão de pacotes novos antes de uso
- Aplicar TTL a dependências abandonadas

### 5. **Isolamento e validação de build**

- Usar ambientes limpos e imutáveis para build
- Assinar artefactos e validar integridade

---

## 📖 Casos de estudo

### `event-stream`

- Pacote popular do npm com acesso transferido
- Atualização introduziu dependência `flatmap-stream` com malware
- Afetou aplicações financeiras

### `ua-parser-js`

- Hijack da conta npm do maintainer
- Versão publicada com minerador de criptomoedas
- Detetado pela comunidade via GitHub Actions

---

## ✅ Recomendações operacionais

| Prática                                   | Aplicar em               |
|-------------------------------------------|---------------------------|
| Proxy interno com lista branca de origem  | Todos os projetos        |
| Aprovação formal de novos pacotes        | L2 e L3                  |
| Scan de scripts maliciosos em pacotes     | L2 e L3                  |
| TTL para dependências não atualizadas     | L2 e L3                  |
| Alertas de typosquatting e nomes suspeitos| L3 (elevado)             |

---

## 🔗 Ligações com outros ficheiros

| Documento                   | Ligação com supply chain                           |
|-----------------------------|---------------------------------------------------------|
| `03-governanca-libs-terceiros.md` | Aprovação de pacotes suspeitos ou com risco         |
| `04-integracao-ci-cd.md`    | Execução de validadores e scripts de bloqueio         |
| `07-controle-registos-origem.md` | Reforço de origem confiável e mirrors internos      |

---

> 🚫 O controlo da cadeia de fornecimento é inseparável da segurança moderna. Ignorá-la é confiar cegamente em código executado fora do teu controlo.
