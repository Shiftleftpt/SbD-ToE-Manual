---
id: hardening-containers
title: Hardening e Restrições de Execução em *containers*
description: Minimização, reforço e controlo de permissões em imagens e ambientes containerizados
tags: [containers, hardening, permissões, runtime, isolamento, segurança]
---

# 🛡️ Hardening e Restrições de Execução em *containers* {containers-imagens:addon:hardening-containers}

## 🌟 Objetivo {containers-imagens:addon:hardening-containers#objetivo}

Reforçar a segurança da execução em *containers* através da **redução da superfície de ataque**, **eliminação de componentes desnecessários** e **restrição explícita de permissões de runtime**. O objetivo é que cada *container* execute **apenas o necessário, com o mínimo de privilégios possível**.

Estas medidas complementam a escolha de imagens seguras e a verificação da sua origem, sendo essenciais para evitar escaladas de privilégio, execução de binários maliciosos ou exploração de vulnerabilidades em tempo de execução.

---

## 🧬 O que significa fazer hardening de *containers* {containers-imagens:addon:hardening-containers#o_que_significa_fazer_hardening_de_containers}

**Hardening de *containers*** implica aplicar medidas que:

- **Eliminam binários e pacotes desnecessários** (ex: `curl`, `bash`, `ping`);
- **Proíbem execução como `root`** (default insecure);
- **Limitam capacidades do kernel (`capabilities`)** expostas ao *container*;
- **Ativam controlo de namespaces, cgroups e seccomp/apparmor**;
- **Aplicam diretivas de imutabilidade** ao sistema de ficheiros;
- **Desativam interfaces perigosas** como `/proc`, `/sys`, Docker socket.

> 🧱 Um *container* seguro **não é apenas uma imagem segura** — o contexto de execução é igualmente crítico.

---

## 📘 Exemplos de práticas de hardening {containers-imagens:addon:hardening-containers#exemplos_de_praticas_de_hardening}

| Prática                           | Técnica ou ferramenta                          | Notas                          |
|----------------------------------|------------------------------------------------|--------------------------------|
| Utilizador não-root              | `USER nobody` no Dockerfile                    | Obrigatório para ambientes L2+|
| Sistema de ficheiros read-only  | `readOnlyRootFilesystem: true` (K8s)           | Evita escrita não controlada   |
| Capabilities mínimas             | `drop: ALL` + adicionar só o necessário        | Evita acesso a funções perigosas |
| Seccomp                          | Perfil `runtime/default` ou personalizado      | Bloqueia syscalls perigosas    |
| AppArmor / SELinux               | Perfis reforçados (`docker-default`, etc.)     | Requer suporte no host         |
| Desativar montagem privilegiada | `--privileged=false`, `no /var/run/docker.sock`| Protege host e outros containers|

---

## 🛠️ Como aplicar no build e runtime {containers-imagens:addon:hardening-containers#como_aplicar_no_build_e_runtime}

1. **No Dockerfile**:
   - Usar `USER` para definir utilizador sem privilégios;
   - Evitar `apt install`, `curl`, `bash`, etc.;
   - Definir `CMD` ou `ENTRYPOINT` mínimos e claros;
   - Adicionar `HEALTHCHECK` e `LABELS` com metadados de segurança.

2. **No Kubernetes / CI/CD**:
   - Aplicar `securityContext` com:
     - `runAsNonRoot: true`
     - `readOnlyRootFilesystem: true`
     - `allowPrivilegeEscalation: false`
     - `capabilities: { drop: ["ALL"] }`
   - Utilizar PodSecurity Standards ou Kyverno para enforcement;
   - Validar políticas de runtime com OPA (ver `05-policies-runtime-opa.md`).

3. **Na pipeline**:
   - Validar Dockerfile com linters (ex: Hadolint);
   - Integrar scanners de permissões e configuração (ex: Kubeaudit);
   - Bloquear deploys de imagens com binários suspeitos (ex: shells interativos).

---

## 📂 Onde configurar e aplicar enforcement {containers-imagens:addon:hardening-containers#onde_configurar_e_aplicar_enforcement}

- **Dockerfile**: baseline de segurança aplicável a qualquer ambiente;
- **Templates de deployment (Helm, YAML)**: definições de `securityContext`, `PodSecurityPolicy`, etc.;
- **CI/CD**: validadores automáticos que rejeitam configurações inseguras;
- **Kubernetes Admission Controllers**: enforcement centralizado (OPA, Kyverno, PSP/PSA).

---

## ✅ Boas práticas {containers-imagens:addon:hardening-containers#boas_praticas}

- Criar catálogo de permissões mínimas por tipo de aplicação;
- Proibir por política o uso de `root` ou *containers* privilegiados;
- Isolar volumes e montar como `readOnly` sempre que possível;
- Validar imagens em build quanto a comandos como `ADD`, `RUN` inseguros;
- Utilizar perfis de seccomp reforçados, ajustados ao runtime real;
- Automatizar a verificação contínua de segurança do ambiente de execução.

---

## 📎 Referências cruzadas {containers-imagens:addon:hardening-containers#referencias_cruzadas}

| Documento                      | Relação com hardening                          |
|-------------------------------|------------------------------------------------|
| `01-imagens-base.md`             | Imagens devem ser minimizadas e não incluir ferramentas desnecessárias |
| `02-runners-isolamento.md`      | Ambientes de execução devem reforçar estas restrições |
| `05-policies-runtime-opa.md`    | Pode forçar aplicação de perfis e restrições  |
| `08-kubernetes-execucao.md`     | Exemplos de aplicação prática em K8s          |
| `10-maturidade.md`              | Aplicação de hardening é critério de maturidade intermédia a elevada |

> 🔐 O runtime é um ponto de entrada tão crítico quanto o código. A ausência de hardening expõe *containers* a ataques triviais e escaladas de privilégio evitáveis.
