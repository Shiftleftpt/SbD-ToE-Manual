---
description: Políticas para repositórios internos, proxies, mirrors e validação da
  proveniência
id: controle-registos-origem
tags:
- cat_operacional
- cicd
- dependencias
- invetario
- sbom
- sca
- supply-chai
title: Controlo de Registos e Origem de Pacotes
---


# 📂 Controlo de Registos e Origem de Pacotes

## 🌟 Objetivo

Assegurar que todas as dependências de terceiros são obtidas a partir de **origens controladas, auditadas e confiáveis**, minimizando o risco de ataques via registos públicos ou fontes não verificadas.

> ⚠️ O simples ato de instalar um pacote de um repositório público pode executar código malicioso sem qualquer alerta. Este controlo é crítico.

---

## 🔢 Conceito de repositório confiável

Um repositório é considerado confiável quando:

- É **interno ou proxyizado**, controlado pela organização
- Permite **auditar o histórico** de pacotes utilizados
- Implementa **políticas de replicação, caching e quarentena**
- Evita acesso direto a fontes externas sem validação

---

## 🏠 Opções técnicas para registo interno

| Tecnologia         | Linguagens / Formatos       | Características principais                         |
|--------------------|------------------------------|-----------------------------------------------------|
| **Verdaccio**      | npm / Yarn (Node.js)         | Docker-ready, simples, caching + fallback controlado |
| **Sonatype Nexus** | Maven, npm, PyPI, Docker     | Enterprise-ready, RBAC, auditoria e integração CI    |
| **JFrog Artifactory** | Múltiplos ecosistemas     | Escalável, policies de retenção e replicadores        |
| **GitHub Packages**| npm, Maven, Container        | Integração com GitHub Actions                      |

---

## 🚀 Estratégia de fallback controlado

1. O repositório tenta obter o pacote **localmente**.
2. Se não existir, tenta fonte externa **sob validação de política** (whitelist de domínios ou GPG keys).
3. O pacote é **cacheado localmente** para builds futuros.
4. Todos os acessos são **auditados e rastreados**.

> Esta abordagem reduz drasticamente a exposição a pacotes comprometidos.

---

## 📝 Recomendações de configuração

- Desativar `--registry` externo por defeito
- Fornecer `.npmrc`, `.pip.conf`, `settings.xml` com origem predefinida
- Proibir instalação com `latest` ou sem versionamento fixo
- Validar hashes ou assinaturas de pacotes (quando suportado)

---

## ✅ Benefícios adicionais

- Reprodutibilidade dos builds
- Menor dependência de disponibilidade externa (resiliência)
- Tempo de build mais rápido com caching local
- Conformidade com exigências de auditoria (CRA, NIS2, ISO 27001)

---

## 🔗 Ligações com outros ficheiros

| Documento                   | Ligação com registos de origem                      |
|-----------------------------|-----------------------------------------------------------|
| `06-risco-supply-chain.md`  | Mitiga typosquatting e downloads de origem desconhecida  |
| `04-integracao-ci-cd.md`    | Pipelines devem usar registos confiáveis apenas           |
| `03-governanca-libs-terceiros.md` | Define quem aprova pacotes e quais podem ser replicados |

---

> 🔒 O uso de repositórios internos com fallback controlado é uma medida de segurança **estrutural**, não opcional. Deve ser parte da baseline de qualquer pipeline seguro.
