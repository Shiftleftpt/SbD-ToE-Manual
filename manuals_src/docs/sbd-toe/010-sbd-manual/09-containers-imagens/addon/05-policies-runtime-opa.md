---
id: policies-runtime-opa
title: Enforcement Técnico de Políticas no Runtime com OPA e Kyverno
description: Aplicação automática de políticas formais para bloquear execuções não conformes, sem substituir decisão humana
tags: [opa, kyverno, policies, enforcement, kubernetes, runtime, containers]
---

# 📜 Enforcement Técnico de Políticas no Runtime com OPA e Kyverno

## 🌟 Objetivo

Garantir que *containers* **que não cumprem requisitos mínimos de segurança definidos pela organização não podem ser executados**, através de mecanismos formais e automáticos de enforcement, nomeadamente em **Kubernetes e pipelines CI/CD**.

As políticas descritas neste capítulo **não decidem se um container é aceitável**.  
Elas **impedem execuções manifestamente não conformes**, fornecendo um **mecanismo técnico de bloqueio** que suporta — mas não substitui — a governação e a decisão humana.

Este ficheiro define como usar OPA, Kyverno e mecanismos equivalentes **como guardrails técnicos**, não como autoridade de risco.

---

## 🧬 O que são políticas de execução (no modelo SbD-ToE)

As **políticas de execução** são regras formais avaliadas automaticamente no momento da criação de um workload. No modelo SbD-ToE, elas servem para:

- **Bloquear configurações inseguras conhecidas**;
- **Impor requisitos mínimos não negociáveis**;
- **Produzir evidência objetiva de não conformidade**;
- **Reduzir a margem de erro operacional** em ambientes automatizados.

> 🔒 Uma política **nunca concede autorização** — apenas **recusa ausência de requisitos mínimos**.

A aceitação de risco, a concessão de exceções e a promoção entre ambientes **são sempre decisões humanas explícitas**, tratadas fora do mecanismo de policy.

---

## ⚠️ Enforcement não é aceitação de risco

Um erro conceptual comum é assumir que:

- workload aprovado por policy = workload seguro
- execução permitida = risco aceite

No SbD-ToE, esta equivalência é **explicitamente proibida**.

As políticas:
- validam **condições mínimas objetivas**;
- não avaliam contexto, impacto ou risco residual;
- não substituem análise nem responsabilidade.

Uma execução pode:
- cumprir todas as políticas,
- estar tecnicamente correta,
- e ainda assim **não ser aceitável** para um determinado contexto (ex.: PROD, dados sensíveis, L3).

---

## 📘 Ferramentas e mecanismos recomendados

| Ferramenta              | Função técnica                                         | Papel no SbD-ToE                    |
|-------------------------|--------------------------------------------------------|-------------------------------------|
| **OPA (Gatekeeper)**    | Avaliação de regras Rego em admission time             | Bloqueio técnico                    |
| **Kyverno**             | Políticas declarativas em YAML                         | Bloqueio e mutação controlada       |
| **Admission Webhooks** | Validação customizada                                  | Enforcement específico              |
| **Validadores CI/CD**  | Checks antecipados (ex.: OPA, Checkov, Semgrep)        | Redução de falhas antes do runtime  |

Estas ferramentas **produzem decisões técnicas binárias (allow / deny)** — não decisões de risco.

---

## 🛠️ Como aplicar políticas de forma correta

### 1️⃣ Definir requisitos mínimos não negociáveis

Exemplos típicos:
- Execução como utilizador não-root;
- Proibição de containers privilegiados;
- Uso de imagens provenientes de registries autorizados;
- Verificação de assinatura (integridade);
- Aplicação de `securityContext` mínimo.

Estes requisitos devem ser:
- claros,
- objetivos,
- tecnicamente verificáveis.

---

### 2️⃣ Implementar políticas como código

- Usar Rego (OPA) ou YAML (Kyverno);
- Versionar em Git, junto da infraestrutura;
- Aplicar via GitOps;
- Associar cada política a um requisito organizacional explícito.

---

### 3️⃣ Testar e aplicar enforcement progressivo

- Iniciar em modo `audit`;
- Analisar rejeições e falsos positivos;
- Comunicar regras às equipas;
- Ativar `enforce` apenas após validação.

O objetivo é **reduzir erro**, não criar bloqueios opacos.

---

## 📂 Onde manter políticas e como governar

- Repositório Git dedicado (`policies/`);
- Versionamento e histórico de alterações;
- Aplicação diferenciada por ambiente;
- Logs imutáveis de rejeições e execuções conformes;
- Processo formal para exceções temporárias.

Qualquer exceção **fora da policy** deve ser:
- explicitamente aprovada;
- limitada no tempo;
- rastreável.

---

## 🔍 Relação com decisão humana

No modelo SbD-ToE:

- **Policies** bloqueiam o que é objetivamente inseguro;
- **Pessoas** decidem o que é aceitável.

Esta separação garante:
- responsabilidade clara;
- auditabilidade real;
- prevenção de confiança implícita induzida por automação.

Sem esta distinção, a policy torna-se um substituto indevido da governação.

---

## ✅ Boas práticas

- Tratar políticas como *guardrails*, não como selo de aprovação;
- Manter políticas simples, objetivas e justificadas;
- Separar claramente:
  - enforcement técnico,
  - decisão de risco,
  - exceção formal;
- Rever políticas após incidentes ou mudanças de plataforma;
- Documentar o racional de cada regra aplicada.

---

## 📎 Referências cruzadas

| Documento                         | Relação com enforcement                        |
|----------------------------------|------------------------------------------------|
| `01-imagens-base.md`             | Bloqueio de imagens não aprovadas              |
| `03-assinatura-cadeia-trust.md` | Verificação de integridade como evidência      |
| `04-hardening-containers.md`    | Enforcement de restrições mínimas              |
| `09-riscos-processo-imagens.md` | Separação entre sinal, bloqueio e decisão      |
| `15-aplicacao-lifecycle.md`     | Integração operacional no ciclo de vida        |

> 🧩 Policies são **limites técnicos**, não decisões de confiança.  
> Quando uma policy decide por nós, a governação já falhou.
