---
id: gestao-segredos-pipeline
title: Gestão e Injeção Segura de Segredos
sidebar_position: 3
description: Estratégias para proteger segredos em pipelines, evitar hardcoded e garantir injeção segura via vaults ou variáveis.
tags: [segredos, cicd, vault, pipelines, segurança, variáveis]
---


# 🔐 Gestão e injeção segura de segredos

A gestão de segredos nos pipelines CI/CD é um dos vetores de ataque mais críticos da cadeia de desenvolvimento. Tokens de acesso, chaves API, credenciais de deploy e outros segredos são frequentemente expostos acidentalmente em variáveis, logs ou ficheiros versionados.

Esta prática define os controlos obrigatórios para garantir a **confidencialidade, escopo mínimo e injeção controlada** de segredos durante a execução de pipelines.

> A confidencialidade dos segredos deve ser preservada mesmo em caso de falha no pipeline.

---

## 🎯 Objetivos

- Impedir o acesso não autorizado a segredos utilizados por pipelines;
- Prevenir a exposição acidental de segredos em logs, repositórios ou ficheiros temporários;
- Reduzir o impacto de compromissos parciais, através de segregação, escopo limitado e rotação periódica.

---

## 🛠️ Práticas

1. **Separação completa entre código e segredos**  
   - Segredos nunca devem ser armazenados diretamente no código fonte ou ficheiros YAML de pipeline;
   - A injeção deve ser feita através de mecanismos externos (ex: `secrets.*`, vaults, variable groups).

2. **Segregação por ambiente, aplicação e função**  
   - Segredos devem ter escopo mínimo (ex: apenas leitura, apenas para um job específico);
   - Evitar o uso de “segredos globais” partilhados entre pipelines ou ambientes.

3. **Injeção temporária e em tempo de execução**  
   - Os segredos devem ser injetados apenas durante a execução;
   - Nunca devem ser persistidos em disco ou em artefactos gerados;
   - Devem ser automaticamente eliminados após uso.

4. **Proteção de logs e variáveis sensíveis**  
   - Variáveis contendo segredos devem estar marcadas como protegidas (`masked`, `secureString`);
   - O output dos comandos que acedem a segredos deve ser ocultado nos logs (`stdout` desativado se necessário).

5. **Rotação periódica e revogação automática**  
   - Deve existir política formal de rotação de segredos;
   - Segredos comprometidos devem ser revogados imediatamente, com impacto minimizado;
   - Aplicações L3 devem usar vaults externos com rotação automática e auditoria.

---

## ⚖️ Aplicação proporcional por nível de risco

| Nível | Requisitos obrigatórios                              | Requisitos reforçados                                  |
|-------|--------------------------------------------------------|---------------------------------------------------------|
| **L1** | Segredos como variáveis seguras; logs protegidos       | —                                                       |
| **L2** | Segregação por ambiente e job; injeção em runtime      | Revogação centralizada; desativação de roaming          |
| **L3** | Vault externo; rotação automática; segregação fina     | Auditoria de uso; alertas de acesso indevido            |

---

## 📌 Exemplos práticos

- **GitHub Actions**  
  - Uso de `secrets.*` com escopo mínimo e proteção `masked: true`;  
  - Ativação de audit logs no GitHub Enterprise.

- **GitLab CI**  
  - `CI/CD Variables` com `masked`, `protected` e escopo por ambiente;  
  - Integração com HashiCorp Vault.

- **Azure DevOps**  
  - `Variable Groups` com escopo por pipeline e ambiente;  
  - Uso de `SecureString` e `Key Vault References`.

- **Jenkins**  
  - Gestão de credenciais com `Credentials Plugin`;  
  - Injeção via `withCredentials` e integração com Vault externo.

---

## 📉 Riscos mitigados

- Vazamento de segredos via logs ou ficheiros temporários (OSC&R: CI0013);
- Utilização indevida de tokens com permissões excessivas (OSC&R: CI0007, CI0012);
- Persistência indevida de credenciais em disco;
- Acesso lateral por pipelines não autorizados ou jobs maliciosos.

---

## 🧭 Referências

- [OWASP CI/CD Security – 2. Secret Management](https://owasp.org/www-project-cicd-security/#2-secret-management)
- [NIST SSDF – PW.6: Manage Secrets](https://csrc.nist.gov/publications/detail/sp/800-218/final)
- [SLSA – Build Isolation & Parameter Injection](https://slsa.dev/spec/v1.0/)
- [BSIMM – SE2.5, CR2.3]
- [SAMM – Secure Build – Environment Hardening]
