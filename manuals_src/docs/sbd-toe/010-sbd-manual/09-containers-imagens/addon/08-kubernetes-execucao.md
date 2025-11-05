---
id: kubernetes-execucao
title: Execução Segura de *containers* em Clusters Kubernetes
description: Aplicação de práticas de segurança, isolamento e validação para workloads containerizados em Kubernetes
tags: [kubernetes, containers, execução segura, isolation, runtime, segurança]
---

# ☸️ Execução Segura de *containers* em Clusters Kubernetes

## 🌟 Objetivo

Assegurar que a **execução de *containers* em ambientes Kubernetes** - seja para aplicações, pipelines, sidecars ou agentes - é feita com **controlo total de permissões, políticas e rastreabilidade**, evitando riscos como:

- Execução de workloads com permissões excessivas;
- Comprometimento de outros pods ou do próprio nó;
- Acesso não autorizado a segredos, volumes ou rede;
- Violação de políticas de segurança organizacionais.

---

## 🧬 O que significa execução segura em Kubernetes

Executar *containers* de forma segura em Kubernetes implica:

- **Aplicar restrições explícitas no `securityContext`**;
- **Utilizar mecanismos nativos de isolamento e controlo** (ex: namespaces, PodSecurity);
- **Evitar execuções privilegiadas ou como `root`**;
- **Validar imagens, origem, permissões e uso de recursos**;
- **Controlar e monitorizar execuções com ferramentas nativas e externas**.

> ⚠️ Um pod mal configurado pode escalar privilégios, comprometer o nó, aceder à rede interna ou violar segredos partilhados.

---

## 📘 Mecanismos de segurança aplicáveis

| Mecanismo                  | Objetivo                                      | Exemplo                                       |
|----------------------------|-----------------------------------------------|-----------------------------------------------|
| `securityContext`          | Definir UID, capabilities, privilégios        | `runAsNonRoot: true`, `readOnlyRootFilesystem`|
| Pod Security Standards     | Política de baseline para pods (`restricted`) | Enforcement automático por cluster            |
| Kyverno / OPA (Gatekeeper) | Enforcement de políticas organizacionais      | Verificar labels, permissões, origem da imagem|
| NetworkPolicies            | Isolar tráfego entre pods/namespaces          | Restringir comunicação interna                |
| RuntimeClass / Sandboxing  | Usar runtimes alternativos (gVisor, Kata)     | Maior isolamento de syscalls e processos      |
| Admission Webhooks         | Validar workload antes de ser executado       | Rejeitar pods fora de política                |

---

## 🛠️ Como aplicar na prática

1. **Aplicar `securityContext` obrigatório em todos os pods**:
   - `runAsNonRoot: true`
   - `allowPrivilegeEscalation: false`
   - `capabilities: drop: ["ALL"]`
   - `readOnlyRootFilesystem: true`

2. **Ativar e aplicar Pod Security Standards (PSA)** no cluster (`restricted`, `baseline`);

3. **Configurar enforcement com OPA ou Kyverno** para:
   - Validar origem das imagens;
   - Proibir execuções com `privileged: true`;
   - Exigir labels de controlo e rastreabilidade.

4. **Aplicar `NetworkPolicy` restritiva por namespace**;
5. **Monitorizar eventos de segurança e falhas de política**;
6. **Usar `RuntimeClass` com runtimes isolados para workloads sensíveis**;
7. **Evitar montagem de volumes sensíveis (`/var/run/docker.sock`, etc.)**;
8. **Limitar recursos (`resources.requests` e `limits`) para evitar DoS interno**.

---

## 📂 Onde configurar e versionar

- Diretório `./k8s/security/` com manifests YAML validados;
- Repositórios Git de IaC com revisão por pull request;
- Políticas versionadas com ArgoCD, Flux ou Terraform;
- Dashboards de compliance integrados com Prometheus, Grafana, Kyverno.

---

## ✅ Boas práticas

- Começar com modo `audit` e migrar para `enforce` após testes;
- Usar `pod-template` validado e partilhado entre equipas;
- Incluir segurança de execução como **aceitação obrigatória em deploys**;
- Forçar verificação automática no Admission Controller;
- Rever políticas e permissões após cada nova versão de Kubernetes;
- Evitar o uso de `hostPath`, `hostNetwork`, `hostPID`, salvo exceções muito justificadas.

---

## 📎 Referências cruzadas

| Documento                      | Relação com Kubernetes                       |
|-------------------------------|-----------------------------------------------|
| `02-runners-isolamento.md`      | Runners podem ser executados como pods        |
| `04-hardening-containers.md`    | `securityContext` aplica-se em Kubernetes     |
| `05-policies-runtime-opa.md`    | Enforcement via OPA ou Kyverno no cluster     |
| `09-exemplo-pipeline-container.md` | Caso prático inclui execução em K8s           |
| `achievable-maturity`              | Aplicação de PSA e policies é critério de maturidade|

> ☁️ Kubernetes não é seguro por omissão. A segurança da execução depende da configuração explícita e do enforcement consistente.
