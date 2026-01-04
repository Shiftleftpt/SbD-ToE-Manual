---
id: hardening-containers
title: Hardening e Restrições de Execução em Containers
description: Minimização, reforço e verificação efetiva de permissões em imagens e ambientes containerizados
tags: [containers, hardening, permissoes, runtime, isolamento, seguranca]
---

# 🛡️ Hardening e Restrições de Execução em Containers

## 🌟 Objetivo

Reforçar a segurança da execução em containers através da **redução da superfície de ataque**, **eliminação de componentes desnecessários** e **restrição explícita de permissões em runtime**, garantindo que cada container executa **apenas o necessário, com o mínimo de privilégios possível**.

No SSDLC moderno, o hardening **não pode ser tratado como intenção declarada**.  
É necessário assegurar que as restrições definidas **são efetivamente aplicadas e verificáveis** no momento da execução.

Estas medidas complementam a escolha de imagens seguras e a validação da sua proveniência, reduzindo o impacto de vulnerabilidades exploráveis, erros de configuração e abusos em runtime.

---

## 🧬 O que significa fazer hardening de containers

**Hardening de containers** consiste na aplicação sistemática de medidas que:

- **Eliminam binários e pacotes desnecessários** (ex.: `curl`, `bash`, `ping`);
- **Impedem execução como `root`**;
- **Restringem capacidades do kernel (`capabilities`)** ao estritamente necessário;
- **Limitam syscalls e interações com o host** (seccomp, AppArmor, SELinux);
- **Aplicam imutabilidade ao sistema de ficheiros**;
- **Bloqueiam interfaces perigosas** como `/proc`, `/sys` ou o Docker socket.

> 🧱 Um container só pode ser considerado hardened se **o estado efetivo em runtime** corresponder ao que foi definido no build e nos manifests.

---

## ⚠️ Hardening configurado ≠ hardening efetivo

Um dos erros mais comuns em ambientes automatizados é assumir que:

- um `Dockerfile` bem escrito,
- um `securityContext` definido,
- ou uma policy aplicada,

garantem automaticamente um runtime seguro.

Na prática, existem três estados distintos:

1. **Hardening declarado**  
   O que está definido em código ou configuração.
2. **Hardening aplicado**  
   O que a plataforma efetivamente tenta aplicar.
3. **Hardening efetivo**  
   O que pode ser empiricamente observado no container em execução.

Este capítulo trata explicitamente o hardening como um **estado verificável**, não como uma propriedade assumida.

---

## 📘 Exemplos de práticas de hardening

| Prática                          | Técnica / Mecanismo                          | Observações operacionais                         |
|---------------------------------|-----------------------------------------------|--------------------------------------------------|
| Utilizador não-root             | `USER` no Dockerfile                          | Deve ser validado em runtime                     |
| FS read-only                    | `readOnlyRootFilesystem: true` (K8s)          | Requer verificação de mounts                     |
| Capabilities mínimas            | `drop: ALL` + add explícito                   | Evitar defaults permissivos                      |
| Seccomp                         | Perfil `runtime/default` ou custom            | Confirmar perfil ativo                           |
| AppArmor / SELinux              | Perfis restritivos                            | Depende do suporte do host                       |
| Execução não privilegiada       | Sem `--privileged`, sem Docker socket         | Deve ser bloqueado por política                  |

---

## 🛠️ Como aplicar e verificar no build e runtime

### 1️⃣ No build (imagem)

- Definir utilizador não-root (`USER`);
- Evitar instalação de ferramentas interativas;
- Minimizar `ENTRYPOINT` e `CMD`;
- Adicionar labels de segurança e contexto;
- Validar Dockerfile com linters (ex.: Hadolint).

> O build **define intenções**, não garante aplicação.

---

### 2️⃣ No deploy (orquestração / CI/CD)

- Definir `securityContext` explícito:
  - `runAsNonRoot: true`
  - `readOnlyRootFilesystem: true`
  - `allowPrivilegeEscalation: false`
  - `capabilities: drop: ["ALL"]`
- Aplicar Pod Security Standards / PSA;
- Enforce por OPA ou Kyverno (ver `05-policies-runtime-opa.md`).

> O enforcement técnico **bloqueia configurações inseguras**, mas não valida o estado real.

---

### 3️⃣ Em runtime (verificação efetiva)

- Verificar utilizador efetivo (`id`, `/proc/self/status`);
- Validar mounts e permissões;
- Confirmar perfil seccomp/AppArmor ativo;
- Detetar desvios (*drift*) face à configuração esperada;
- Registar resultados para auditoria.

Sem esta verificação, o hardening é apenas **assumido**, não demonstrado.

---

## 📂 Onde configurar e controlar

- **Dockerfile**: baseline mínima e reproduzível;
- **Manifests / Helm charts**: definição declarativa de restrições;
- **CI/CD**: validação automática de configurações inseguras;
- **Admission Controllers**: enforcement centralizado;
- **Monitorização runtime**: confirmação empírica do estado.

Cada camada reduz a probabilidade de erro, mas **nenhuma é suficiente isoladamente**.

---

## ✅ Boas práticas

- Definir perfis de hardening por tipo de workload;
- Proibir por política containers privilegiados;
- Validar hardening após deploy, não apenas antes;
- Tratar exceções como decisões formais e temporárias;
- Rever hardening após alterações de plataforma ou kernel;
- Integrar verificação contínua de runtime em ambientes críticos.

---

## 📎 Referências cruzadas

| Documento                         | Relação com hardening                          |
|----------------------------------|------------------------------------------------|
| `01-imagens-base.md`             | Minimização de superfície na imagem            |
| `02-runners-isolamento.md`       | Isolamento do ambiente de execução             |
| `05-policies-runtime-opa.md`     | Enforcement técnico de restrições              |
| `08-kubernetes-execucao.md`      | Aplicação prática em clusters                  |
| `09-riscos-processo-imagens.md`  | Diferença entre intenção e estado efetivo      |

> 🔐 Hardening só existe quando pode ser **observado, reproduzido e auditado**.  
> Configuração sem verificação é apenas suposição.
