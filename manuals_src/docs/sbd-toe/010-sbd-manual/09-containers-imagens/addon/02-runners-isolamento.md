---
id: runners-isolamento
title: Runners, Execução Isolada e Ambientes Controlados
description: Garantia de execução segura e controlada de *containers* em pipelines e ambientes partilhados
tags: [ci-cd, execucao, isolamento, pipelines, runners, seguranca]
---

# 🏃‍♂️ Runners, Execução Isolada e Ambientes Controlados

## 🌟 Objetivo

Garantir que todos os *containers* são executados em **ambientes isolados, controlados e auditáveis**, especialmente no contexto de **pipelines CI/CD** e execução automatizada de tarefas, mitigando riscos de:

- Compromisso do host ou de outros jobs;
- Escalada de privilégios;
- Persistência de dados sensíveis entre execuções;
- Utilização indevida de runners partilhados com permissões excessivas.

---

## 🧬 O que são runners e ambientes de execução

**Runners** são agentes de execução responsáveis por correr tarefas de CI/CD ou workloads de containers, tipicamente em plataformas como:

- GitHub Actions (`runners`)
- GitLab CI (`runners`)
- Azure DevOps (`agents`)
- Jenkins (`executors`)
- Kubernetes Jobs, CronJobs ou pods temporários

Um **ambiente isolado** deve garantir:

- Separação de namespaces (processo, rede, filesystem);
- Zero persistência entre execuções;
- Execução com utilizador não-root e permissões mínimas;
- Capacidade limitada (ex: CPU, memória, storage).

> ⚠️ Runners partilhados e genéricos são **ponto crítico de ataque** se não forem isolados e verificados continuamente.

---

## 📘 Tipos de runners e níveis de risco

| Tipo                    | Exemplos                  | Risco associado             | Notas                               |
|-------------------------|---------------------------|-----------------------------|--------------------------------------|
| Partilhado (multi-tenant)| GitHub hosted, GitLab shared | Elevado - superfície comum | Evitar em pipelines críticas         |
| Autogerido (on-prem/cloud)| Azure DevOps agent, K8s pod | Moderado - depende do hardening | Ideal se gerido com boas práticas    |
| Ephemeral e dedicados   | K8s jobs, ephemeral containers | Baixo - isolamento total   | Recriado por build, não partilhado   |

---

## 🛠️ Como aplicar execução isolada

1. **Evitar uso de runners partilhados** para projetos críticos (L3);
2. **Executar *containers* em ambientes efémeros** - destruídos após uso;
3. **Desativar privilégios no runtime** (`--privileged`, `--cap-add`, `--mount /var/run/docker.sock`);
4. **Aplicar limites de recursos (`CPU`, `RAM`) e quotas**;
5. **Validar que o utilizador de execução não tem permissões administrativas**;
6. **Utilizar sandboxing (ex: gVisor, Kata Containers) quando aplicável**;
7. **Controlar imagens utilizadas no runner** (ver `01-imagens-base.md`);
8. **Impedir acesso direto à rede ou storage externo sem validação explícita**;
9. **Monitorizar execuções e registar métricas de isolamento e falhas**.

---

## 📂 Onde e como configurar

| Plataforma       | Configuração de isolamento sugerida                       |
|------------------|------------------------------------------------------------|
| GitHub Actions   | Usar runners self-hosted com sandbox (ex: K8s), revogar após uso |
| Azure DevOps     | Agentes em containers dedicados; evitar acesso a `host`    |
| GitLab CI        | Runners Docker/Kubernetes com política de isolamento       |
| Jenkins          | Docker plugin com `--rm`, `--read-only`, user não-root     |
| Kubernetes       | Pods efémeros com `securityContext`, `PodSecurity` e `PSA` |

---

## ✅ Boas práticas

- Isolar por projeto/cliente: um runner por repositório ou namespace;
- Recriar runners a cada execução (não persistir imagens ou cache);
- Monitorizar tempo de execução, uso de disco e falhas de segurança;
- Proibir acesso à rede interna sem validação explícita;
- Utilizar **labels e restrições** para forçar execução segura (ex: `no-root`, `trusted-image`);
- Integrar com enforcement de política via OPA/Kyverno.

---

## 📎 Referências cruzadas

| Documento                      | Relação com ambientes de execução         |
|-------------------------------|--------------------------------------------|
| `01-imagens-base.md`             | Runners devem usar imagens aprovadas       |
| `05-policies-runtime-opa.md`    | Enforcement de políticas de execução segura|
| `06-sbom-containers.md`         | SBOM pode incluir runtime e dependências do runner |
| `09-exemplo-pipeline-container.md` | Caso prático de execução controlada         |
| `achievable-maturity`              | Uso de ambientes isolados é indicador de maturidade |

> 🧱 A segurança do pipeline começa na segurança da execução. Runners mal configurados são portas abertas para comprometimento da supply chain.
