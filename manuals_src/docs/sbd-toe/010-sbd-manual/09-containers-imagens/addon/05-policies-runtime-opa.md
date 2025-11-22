---
id: policies-runtime-opa
title: Enforcement de Políticas no Runtime com OPA e Kyverno
description: Aplicação de políticas formais e automáticas para validar *containers* e execuções em tempo real
tags: [containers, enforcement, kubernetes, kyverno, opa, policies, runtime]
---

# 📜 Enforcement de Políticas no Runtime com OPA e Kyverno

## 🌟 Objetivo

Garantir que apenas *containers* **conformes com políticas de segurança definidas** podem ser executados em ambientes controlados - nomeadamente **Kubernetes e pipelines CI/CD** - através de mecanismos formais de enforcement como:

- OPA (Open Policy Agent)
- Kyverno
- Admission Controllers

Estas políticas asseguram a aplicação objetiva e automatizada de requisitos como:

- Uso de imagens aprovadas e assinadas;
- Execução com utilizador não-root;
- Hardening do runtime (`securityContext`);
- Proibição de execuções privilegiadas;
- Conformidade com baseline organizacional.

---

## 🧬 O que são políticas de execução

As **políticas de execução** são regras formais aplicadas automaticamente no momento da criação de um *container* ou workload. São utilizadas para:

- **Validar a conformidade de cada execução** com o baseline de segurança;
- **Bloquear execuções não conformes** com regras pré-definidas;
- **Auditar tentativas de execução fora de política**;
- **Impor requisitos de assinatura, labels, annotations, permissões, imagens**.

> 🔒 As políticas são o equivalente técnico à “governança runtime” - são o que transforma guidelines em enforcement real.

---

## 📘 Ferramentas recomendadas

| Ferramenta      | Descrição                                     | Contexto                           |
|------------------|-----------------------------------------------|------------------------------------|
| **OPA (Gatekeeper)** | Motor de políticas Rego para Kubernetes       | Regras flexíveis e expressivas     |
| **Kyverno**      | Motor de políticas YAML nativas em Kubernetes | Mais simples e adaptado a devs     |
| **Admission Webhooks** | Validação customizada de execuções           | Personalizável, mas requer dev     |
| **Validadores CI/CD** | Checks na pipeline (ex: Checkov, OPA, Semgrep) | Complementam validação em runtime  |

---

## 🛠️ Como aplicar políticas no runtime

1. **Definir os requisitos mínimos de execução**:
   - Sem `root`;
   - Imagem validada e assinada;
   - `readOnlyRootFilesystem`;
   - `capabilities: drop: ALL`;
   - Proveniência da imagem (registry autorizado).

2. **Escrever políticas**:
   - Em Rego (para OPA) ou YAML (para Kyverno);
   - Versão e aplicar via GitOps (ArgoCD, Flux).

3. **Instalar o motor de enforcement**:
   - `Gatekeeper` para OPA;
   - `Kyverno` como controller no cluster.

4. **Testar execuções contra as políticas** com modo `audit` + logs.

5. **Ativar modo `enforce`** após validação e aceitação da política.

6. **Aplicar rótulos (labels), anotações e regras de âmbito** (por namespace, equipa, tipo de workload).

---

## 📂 Onde manter políticas e como versionar

- Diretório `./policies/` em repositório Git controlado;
- Versionar com a infraestrutura (IaC);
- Validar via CI/CD antes de aplicar;
- Aplicar por ambientes (`dev`, `pre-prod`, `prod`) com âmbito diferenciado;
- Auditar logs de rejeições e execuções conformes.

---

## ✅ Boas práticas

- Começar em modo `audit` antes de `enforce`;
- Comunicar regras às equipas para evitar quebras silenciosas;
- Separar políticas por tipo de workload (apps, CI/CD, sidecars);
- Manter documentação e exemplos com racional de cada regra;
- Ligar políticas a requisitos formais do Capítulo 2 (`REQ-*`) e Capítulo 9 (`addon/`);
- Validar compatibilidade entre políticas de OPA e PSP/PSA (caso coexistam).

---

## 📎 Referências cruzadas

| Documento                      | Relação com enforcement                      |
|-------------------------------|----------------------------------------------|
| `01-imagens-base.md`             | Pode ser exigido uso apenas de imagens aprovadas |
| `03-assinatura-cadeia-trust.md` | Enforcement de imagens assinadas             |
| `04-hardening-containers.md`    | Pode validar se `securityContext` é conforme |
| `08-kubernetes-execucao.md`     | Execução segura com enforcement ativo        |
| `achievable-maturity`              | Políticas automáticas são critério de maturidade avançada |

> 🧩 As políticas de runtime são a última linha de defesa. Se a pipeline falhar, o cluster não pode executar código fora de política - essa é a essência do enforcement.
