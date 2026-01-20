---
id: runners-isolamento
title: Runners, Execução Isolada e Ambientes Controlados
description: Garantia de execução segura e controlada de containers em pipelines e ambientes partilhados
tags: [runners, isolamento, pipelines, execucao, seguranca, cicd]
---

# 🏃‍♂️ Runners, Execução Isolada e Ambientes Controlados

## 🌟 Objetivo

Garantir que todos os containers são executados em **ambientes isolados, controlados e auditáveis**, em especial no contexto de **pipelines CI/CD e execução automatizada**, mitigando riscos de processo e de compromisso técnico, nomeadamente:

- Compromisso do host ou de outros jobs;
- Escalada de privilégios;
- Persistência indevida de dados sensíveis entre execuções;
- Execução de artefactos não avaliados em ambientes partilhados;
- Aceitação implícita de risco por via da automação.

Num SSDLC moderno, runners **não são apenas infraestrutura**:  
são **pontos de materialização de confiança**, onde artefactos passam de “construídos” a “executados”.

---

## 🧬 O que são runners e ambientes de execução

**Runners** são agentes de execução responsáveis por correr tarefas de CI/CD ou workloads de containers, tipicamente em plataformas como:

- GitHub Actions (`runners`)
- GitLab CI (`runners`)
- Azure DevOps (`agents`)
- Jenkins (`executors`)
- Kubernetes Jobs, CronJobs ou pods temporários

Independentemente da plataforma, um runner representa sempre um **ambiente onde decisões implícitas ocorrem**:  
qual imagem é executada, com que permissões, em que contexto e com que impacto.

Um **ambiente de execução isolado** deve garantir, no mínimo:

- Separação de namespaces (processo, rede, filesystem);
- Ausência de persistência entre execuções;
- Execução com utilizador não-root e permissões mínimas;
- Limitação explícita de recursos (CPU, memória, storage);
- Impossibilidade de afetar execuções paralelas ou futuras.

> ⚠️ Runners partilhados e genéricos são **pontos críticos de risco de processo**, pois uma execução bem-sucedida pode ser interpretada, erradamente, como autorização implícita.

---

## 📘 Tipos de runners e níveis de risco

| Tipo                     | Exemplos                               | Risco associado                       | Notas operacionais                                  |
|--------------------------|----------------------------------------|---------------------------------------|-----------------------------------------------------|
| Partilhado (multi-tenant)| GitHub hosted, GitLab shared            | Elevado – superfície comum            | Evitar em pipelines L2/L3                           |
| Autogerido               | Azure DevOps agent, runners on-prem     | Moderado – depende de hardening       | Aceitável se isolado e auditável                    |
| Efémero e dedicado       | K8s Jobs, runners temporários           | Baixo – isolamento forte              | Preferencial: recriado por execução                 |

A escolha do tipo de runner **é uma decisão de risco**, não apenas de conveniência operacional.

---

## 🛠️ Como aplicar execução isolada

A execução segura exige que o runner **não introduza confiança implícita** nem amplifique erros a montante:

1. **Evitar runners partilhados** em projetos críticos ou regulados (L3);
2. **Executar containers em ambientes efémeros**, destruídos após cada execução;
3. **Proibir execução privilegiada** (`--privileged`, `--cap-add`, acesso a `/var/run/docker.sock`);
4. **Aplicar limites explícitos de recursos** (CPU, RAM, storage);
5. **Garantir que o utilizador de execução não tem permissões administrativas**;
6. **Aplicar sandboxing adicional** (ex.: gVisor, Kata Containers) quando o risco o justifica;
7. **Restringir as imagens permitidas no runner** (ver `01-imagens-base.md`);
8. **Controlar e justificar qualquer acesso a rede ou storage externo**;
9. **Registar e monitorizar execuções**, incluindo falhas de isolamento e tentativas de evasão.

Estes controlos não substituem decisão humana, mas **reduzem o impacto de decisões erradas ou implícitas**.

---

## 📂 Onde e como configurar

| Plataforma       | Prática recomendada de isolamento                                  |
|------------------|---------------------------------------------------------------------|
| GitHub Actions   | Runners self-hosted em ambientes efémeros (ex.: Kubernetes)         |
| Azure DevOps     | Agentes em containers dedicados; sem acesso ao host                 |
| GitLab CI        | Runners Docker/Kubernetes com política de isolamento rígida         |
| Jenkins          | Execução em containers efémeros com filesystem read-only            |
| Kubernetes       | Pods temporários com `securityContext`, PSA e quotas                |

Independentemente da plataforma, a regra é invariável:  
**o runner não deve sobreviver à execução**.

---

## 🔍 Runners como ponto de decisão implícita

Sempre que um runner executa um container:

- uma imagem foi implicitamente aceite;
- um contexto de permissões foi implicitamente autorizado;
- um impacto potencial foi implicitamente assumido.

Por isso:
- a execução **deve ser rastreável**;
- o contexto **deve ser reproduzível**;
- a decisão **deve ser justificável a posteriori**.

Sem estes elementos, a automação transforma-se em risco sistémico.

---

## ✅ Boas práticas

- Isolar runners por projeto, domínio ou namespace;
- Recriar runners a cada execução (sem cache persistente);
- Monitorizar uso de recursos e anomalias de execução;
- Proibir acesso à rede interna por omissão;
- Usar labels e restrições para forçar execução segura;
- Integrar enforcement técnico (OPA/Kyverno) sem substituir governação.

---

## 📎 Referências cruzadas

| Documento                         | Relação com runners e execução                  |
|----------------------------------|-------------------------------------------------|
| `01-imagens-base.md`             | Imagens permitidas nos ambientes de execução    |
| `05-policies-runtime-opa.md`    | Enforcement técnico de políticas                |
| `06-sbom-containers.md`         | Inventário do ambiente de execução              |
| `09-riscos-processo-imagens.md` | Separação entre execução automática e decisão   |
| `15-aplicacao-lifecycle.md`     | Aplicação operacional no ciclo de vida          |

> 🧱 A segurança do pipeline começa na execução.  
> Um runner inseguro **não é apenas um risco técnico** — é um mecanismo de aceitação implícita de risco.
