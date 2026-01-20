---

id: kubernetes-execucao
title: Execução Segura de Containers em Clusters Kubernetes
description: Aplicação e verificação efetiva de práticas de segurança, isolamento e controlo para workloads containerizados
tags: [kubernetes, containers, execucao-segura, isolamento, runtime, seguranca]
-------------------------------------------------------------------------------

# ☸️ Execução Segura de Containers em Clusters Kubernetes

## 🌟 Objetivo

Assegurar que a **execução de containers em ambientes Kubernetes** — aplicações, pipelines, sidecars ou agentes — ocorre com **restrições explícitas, enforcement técnico e evidência verificável**, reduzindo riscos como:

* Execução com privilégios excessivos;
* Escalada de permissões ao nível do nó;
* Acesso indevido a segredos, volumes ou rede;
* Execuções fora do baseline organizacional.

Kubernetes fornece **mecanismos**, não garantias.
A segurança da execução depende de **configuração correta, enforcement ativo e verificação contínua**.

---

## 🧬 O que significa execução segura em Kubernetes (no SbD-ToE)

No modelo SbD-ToE, executar containers de forma segura em Kubernetes implica:

* **Declarar restrições de execução** (`securityContext`, PSA);
* **Impor essas restrições tecnicamente** (admission control);
* **Verificar que o estado real do pod corresponde ao esperado**;
* **Manter rastreabilidade entre decisão, configuração e execução**.

> ⚠️ Um pod pode ser aceite pelo cluster e ainda assim violar expectativas de segurança se o estado efetivo não for verificado.

---

## ⚠️ Configuração não é garantia de segurança

É essencial evitar a equivalência implícita:

* ✔️ `securityContext` definido
* ❌ execução automaticamente segura

Existem três níveis distintos:

1. **Capacidade da plataforma**
   O que Kubernetes permite configurar.
2. **Configuração declarada**
   O que está nos manifests.
3. **Estado efetivo de execução**
   O que o pod realmente aplica em runtime.

Este ficheiro trata explicitamente os **três níveis**, não apenas o segundo.

---

## 📘 Mecanismos de segurança aplicáveis

| Mecanismo                  | Função técnica                             | Limitação inerente                |
| -------------------------- | ------------------------------------------ | --------------------------------- |
| `securityContext`          | Define UID, capabilities, privilégios      | Pode ser ignorado se mal aplicado |
| Pod Security Standards     | Baseline de aceitação de pods              | Não valida estado pós-admission   |
| Kyverno / OPA (Gatekeeper) | Bloqueio de configurações fora de política | Não avalia risco contextual       |
| NetworkPolicies            | Isolamento de tráfego                      | Requer cobertura completa         |
| RuntimeClass / Sandboxing  | Isolamento reforçado                       | Não elimina risco lógico          |
| Admission Webhooks         | Validação pré-execução                     | Atua antes do runtime             |

---

## 🛠️ Como aplicar de forma correta

### 1️⃣ Declarar restrições mínimas obrigatórias

Todos os pods devem declarar explicitamente:

```yaml
securityContext:
  runAsNonRoot: true
  allowPrivilegeEscalation: false
  readOnlyRootFilesystem: true
  capabilities:
    drop: ["ALL"]
```

Estas declarações são **necessárias**, mas não suficientes.

---

### 2️⃣ Impor enforcement técnico

* Ativar Pod Security Admission (`restricted` ou `baseline`);
* Aplicar políticas via Kyverno ou OPA para:

  * proibir `privileged: true`;
  * bloquear imagens fora de origem autorizada;
  * exigir labels e metadados de rastreabilidade.

O enforcement **reduz erro humano**, não substitui governação.

---

### 3️⃣ Verificar estado efetivo em runtime

Para workloads críticos (L2/L3), é necessário:

* Confirmar UID efetivo do processo;
* Validar mounts e permissões reais;
* Verificar perfil seccomp / AppArmor ativo;
* Detetar desvios (*drift*) após admission;
* Registar evidência para auditoria.

Sem esta verificação, a segurança é apenas **assumida**.

---

## 📂 Onde configurar, versionar e observar

* Manifests em repositórios Git versionados;
* Políticas como código via GitOps;
* Logs de admission e rejeições preservados;
* Métricas de compliance e desvios monitorizadas;
* Evidência de execução associada ao workload.

---

## ✅ Boas práticas

* Tratar Kubernetes como **plataforma de execução**, não como barreira de segurança autónoma;
* Separar claramente:

  * configuração,
  * enforcement,
  * verificação;
* Aplicar políticas progressivamente (`audit` → `enforce`);
* Rever permissões após upgrades de cluster;
* Documentar exceções como decisões temporárias e rastreáveis;
* Assumir que **configuração sem observação é hipótese, não facto**.

---

## 📎 Referências cruzadas

| Documento                       | Relação com execução em Kubernetes     |
| ------------------------------- | -------------------------------------- |
| `02-runners-isolamento.md`      | Runners como pods efémeros             |
| `04-hardening-containers.md`    | Restrições aplicadas ao runtime        |
| `05-policies-runtime-opa.md`    | Enforcement técnico no admission       |
| `09-riscos-processo-imagens.md` | Separação entre intenção e estado real |
| `15-aplicacao-lifecycle.md`     | Integração no SSDLC                    |

> ☁️ Kubernetes executa o que lhe é pedido.
> A segurança existe apenas quando **o que é executado corresponde ao que foi conscientemente decidido**.
