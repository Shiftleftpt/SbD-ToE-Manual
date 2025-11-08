---
id: intro
title: Containers e Execução Isolada
description: Princípios, práticas e controlos para construir, assinar, validar e executar imagens de forma segura e rastreável
tags:
  [containers, imagens, supply-chain, proveniencia, assinatura, slsa, ssdf,
   registry, runtime-hardening, admission-control, kubernetes, cicd, dSOMM]
sidebar_position: 0
---

:::tip Capítulo Operacional
Este capítulo é considerado **operacional** no modelo *Security by Design – Theory of Everything (SbD-ToE)*.  
A sua função é **aplicar, automatizar e validar** as práticas definidas nos capítulos basilares, garantindo a sua execução contínua e mensurável.  

Os capítulos operacionais implementam o SbD-ToE em contextos técnicos específicos. Estes capítulos traduzem as prescrições basilares em práticas de **execução verificável**, promovendo a **integração contínua da segurança** ao longo do ciclo de vida do software.
:::


# Containers e Execução Isolada

A execução em containers transformou-se na norma em pipelines de CI/CD e em produção. Esta ubiquidade trouxe ganhos de agilidade, mas também riscos sérios quando as práticas de segurança não acompanham o ritmo.  
Executar código em ambientes não isolados, com imagens adulteradas ou permissões excessivas, é um convite aberto ao compromisso.  

Casos reais reforçam este alerta: falhas em registries levaram a ataques de *typosquatting* (imagens maliciosas mascaradas de oficiais), segredos hardcoded em containers expuseram credenciais em incidentes como o **Tesla Kubernetes breach (2018)**, e ataques à cadeia de fornecimento como o **SolarWinds** mostraram o impacto devastador de imagens sem proveniência validada.  

Por isso, este capítulo estabelece as bases para uma execução **confiável, rastreável e auditável**, unindo requisitos de proveniência, runtime hardening e governação de todo o ciclo. É aqui que a segurança “entra em runtime” e demonstra o seu valor científico e operacional.


Os requisitos aqui prescritos não são genéricos: tratam especificamente da **execução em containers como artefactos de software completos**.  
Isto implica olhar tanto para imagens de pipeline (builders, runners) como para imagens aplicacionais em runtime (microserviços, jobs).  

👉 O objetivo não é apenas “assegurar que corre”, mas garantir que **corre de forma confiável, validada e auditável**.  

Este capítulo está intimamente ligado a:  
- **Cap. 05 - Dependências, SBOM e SCA**, porque containers são também *supply chain artifacts*, exigindo inventário e rastreabilidade.  
- **Cap. 07 - CI/CD Seguro**, que trata a segurança global do pipeline.  
- **Cap. 12 - Monitorização & Operações**, que reforça a deteção e resposta em runtime.  

---

## 🧭 O que cobre tecnicamente

Quando falamos de containers seguros, falamos de uma cadeia de controlos que começa antes do build e continua durante toda a execução.  
Cada etapa tem de ser protegida porque, se uma falhar, o risco alastra.

- Escolha e validação de imagens base seguras e **pinned**.  
- Execução em ambientes controlados (runners, jobs, serviços).  
- Assinatura e verificação de proveniência (SLSA, Sigstore).  
- Hardening e minimização de runtime (non-root, capabilities mínimas, read-only FS).  
- Políticas de execução (OPA, Kyverno, PSP).  
- Integração com Kubernetes (RBAC, ServiceAccounts dedicadas, NetworkPolicy).  
- Geração de SBOM e rastreabilidade commit→pipeline→deploy.  

Estes elementos, aplicados em conjunto, criam a “malha de confiança” que suporta a segurança de containers.

---

## 🧪 Pilares de governação

Para além da técnica, existe a governação: **o que é obrigatório, quem aprova e como se mantém atualizado**.  
Sem governação, os controlos técnicos degradam-se e perdem eficácia.  

👉 Pensa nestes pilares como a **espinha dorsal** do programa de segurança de containers: mesmo que outros controlos falhem, são eles que mantêm a organização de pé.

1. **Allowlist de registries e digest-only** para bloquear fontes não confiáveis.  
2. **Gestão de segredos** - fora da imagem, com credenciais efémeras e auditadas.  
3. **RBAC mínimo e ServiceAccounts dedicadas**, nunca o *default SA* em L2/L3.  
4. **NetworkPolicies** com egress controlado, reduzindo o “blast radius”.  
5. **Golden Base Images** por stack, com SLA de patching e depreciação.  
6. **Builders/runners ephemerais, mínimos e assinados** para proteger pipelines.  

🔬 Em L3 (alto risco), entram controlos avançados como **sandboxes de alto isolamento (gVisor/Kata/Firecracker)**, deteção de *drift* e **promoção por estágios**.

---

## ⚙️ Como deve ser feito

A prática exige tanto disciplina como automatização.  
Não basta “confiar nos developers” ou “escolher imagens oficiais”: é necessário **mecanismos formais e repetíveis**.

- Usar imagens base minimalistas (Distroless, Alpine) mantidas e verificadas.  
- Assinar/verificar imagens (Cosign + Rekor), anexando proveniência SLSA.  
- Integrar scanners de vulnerabilidades no CI/CD com gates por severidade.  
- Correr containers com privilégios mínimos (non-root, drop capabilities, FS read-only).  
- Definir e aplicar políticas (OPA/Kyverno) sobre origem, digest, RBAC e SA.  
- Gerar SBOM em cada build, rastrear alterações e ligá-las ao pipeline.  
- Rastrear execuções de forma auditável, do commit ao runtime.  

Estes passos não são opcionais - são a base da confiança operacional.

---

## 📆 Quando aplicar

Os controlos devem ser pensados desde o desenho da pipeline, não apenas “em cima do deploy”.  
Cada fase traz o seu gatilho:

- Durante o design da pipeline CI/CD.  
- Na escolha de imagens base e definição de registries autorizados.  
- Em cada build e release de imagem.  
- Antes do deploy: verificação de assinatura e enforcement de policies.  
- Após CVEs críticos ou mudanças de arquitetura.  

👉 A aplicação contínua garante que o risco não se acumula até se tornar incontrolável.

---

## 👥 Quem está envolvido

Containers seguros não são responsabilidade exclusiva de uma equipa.  
A sua proteção depende de uma **colaboração transversal**:

| Papel                   | Contributo                                                                 |
|-------------------------|-----------------------------------------------------------------------------|
| **DevOps / Plataforma** | Define imagens aprovadas, runners seguros, enforcement (OPA/Kyverno)        |
| **Equipa de Dev**       | Usa imagens validadas, aplica controlos nos manifests, integra SBOM         |
| **AppSec / Segurança**  | Valida cadeia de confiança, controla execuções, analisa scanners            |
| **Infraestrutura**      | Garante isolamento (cgroups, namespaces, policies) em Kubernetes            |
| **GRC / Conformidade**  | Mantém rastreabilidade, políticas formais e evidências para auditoria       |

Sem esta distribuição de papéis, a segurança degrada-se - e um elo fraco compromete toda a cadeia.

---

## 🎯 Para quê

A pergunta central é: *por que investir em controlos tão rigorosos para containers?*  
A resposta é simples: porque **containers inseguros comprometem diretamente a integridade da organização**.

- Evitar execução de código adulterado ou não verificado.  
- Reduzir a superfície de ataque em pipelines e produção.  
- Aumentar a rastreabilidade e confiança em auditorias.  
- Cumprir normativos como NIS2, SSDF e SLSA.  
- Permitir resposta rápida e eficaz a incidentes em runtime.  

Exemplos como o **Equifax (2017)** - em que logs e controlos deficientes atrasaram a deteção - ou fugas via segredos mal geridos em Docker Hub mostram que o custo de não aplicar estas práticas é sempre superior ao de as adotar.  

Em última análise, trata-se de transformar agilidade em **agilidade com confiança**.

---

## 🧮 Aplicação proporcional L1–L3

Nem todas as aplicações precisam do mesmo nível de controlo, mas todas precisam de algum.  
A proporcionalidade permite balancear custo, risco e complexidade:

| Prática                  | L1 (baixo) | L2 (médio) | L3 (alto/crit.) |
|---------------------------|------------|------------|-----------------|
| Scanner de imagens        | Aviso      | Bloqueio High/Critical | Bloqueio Medium+ |
| Assinatura + SLSA         | Recomendado| Recomendado| Obrigatório |
| Digest-only / allowlist   | Aviso      | Bloqueio por origem | Bloqueio + digest-only |
| Segredos fora da imagem   | Recomendado| Obrigatório| Obrigatório + rotação automática |
| RBAC/SA dedicadas         | Recomendado| Obrigatório| Obrigatório + revisão periódica |
| NetworkPolicy egress      | Ingress básico | Ingress + egress crítico | Ingress + egress total + auditoria |
| Golden base + SLA patch   | Recomendado| Obrigatório| Obrigatório + rollout acelerado |
| Builders ephemerais       | Recomendado| Obrigatório| Obrigatório + segmentação rede |
| Sandboxes (gVisor/Kata)   | -          | -          | Recomendado p/ dados sensíveis |
| Drift & promoção estágios | -          | -          | Obrigatório em ambientes regulados |

---

## 📜 Políticas Organizacionais Relevantes

Políticas formais dão sustentabilidade a estas práticas.  
Elas garantem que não dependemos apenas da disciplina individual, mas de regras coletivas e auditáveis.

| Política organizacional         | Obrigatória | Aplicação | Conteúdo mínimo |
|---------------------------------|-------------|-----------|-----------------|
| Política de Containers Seguros  | Sim         | Todos os projetos | Allowlist + digest-only, scanners, assinatura/proveniência, RBAC/SA, NetworkPolicy |
| Política de Gestão de Segredos  | Sim         | DevOps, AppSec | OIDC/TTL curto, proibição de segredos na imagem, rotação |
| Política de Rastreabilidade     | Recomendado | GRC/Auditoria | Logs commit→pipeline→deploy, retenção, export imutável |
| Política de Golden Base Images  | Sim         | Plataforma, AppSec | Catálogo, SLA de patching, depreciação |
| Política de Builders/Runners    | Recomendado | DevOps | Ephemerais, mínimos, assinados, cache controlada |

Na versão impressa, consultar o **Anexo de Políticas Organizacionais do Manual**, onde estas políticas estão consolidadas transversalmente.

---
