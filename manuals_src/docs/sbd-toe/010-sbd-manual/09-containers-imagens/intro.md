---
id: intro
title: Containers e Execução Isolada
description: Princípios, práticas e controlos para construir, validar e executar imagens de forma segura, auditável e rastreável
tags:
  [containers, imagens, supply-chain, proveniencia, assinatura, slsa, ssdf,
   registry, runtime-hardening, admission-control, kubernetes, cicd, dSOMM]
sidebar_position: 0
---

:::tip Capítulo Operacional
Este capítulo é considerado **operacional** no modelo *Security by Design – Theory of Everything (SbD-ToE)*.  
A sua função é **aplicar, automatizar e validar** as práticas definidas nos capítulos basilares, garantindo a sua execução contínua, mensurável e auditável.

Os capítulos operacionais assumem explicitamente o uso extensivo de automação no SSDLC moderno e tratam os **riscos introduzidos pelo próprio processo de execução**, não apenas pela tecnologia utilizada.
:::


# Containers e Execução Isolada

A execução em containers tornou-se a norma em pipelines de CI/CD e em produção.  
Esta ubiquidade trouxe ganhos significativos de agilidade e portabilidade, mas introduziu **novos riscos de processo** quando a construção, validação e promoção de imagens passam a ser fortemente mediadas por pipelines automatizados.

Hoje, imagens são frequentemente **derivadas, geradas, recombinadas ou promovidas automaticamente**, muitas vezes sem intervenção humana direta.  
Neste contexto, falhas de governação — e não apenas falhas técnicas — tornam-se o vetor dominante de compromisso.

Casos reais ilustram este risco: ataques por *typosquatting* em registries públicos, segredos embebidos em imagens explorados em ambientes Kubernetes (como no **Tesla Kubernetes breach, 2018**), e incidentes de cadeia de fornecimento como o **SolarWinds** demonstram que **artefactos aparentemente válidos podem ser operacionalmente inseguros**.

Este capítulo estabelece, por isso, as bases para uma execução **confiável, rastreável e auditável**, tratando containers como **artefactos de software completos**, sujeitos a decisão humana explícita, validação independente e evidência verificável ao longo de todo o ciclo.

👉 O objetivo não é apenas garantir que “o container corre”, mas assegurar que **corre por decisão consciente, com risco conhecido e evidência suficiente**.


Os requisitos aqui prescritos aplicam-se tanto a:
- imagens de pipeline (*builders*, *runners*, jobs técnicos),
- como a imagens aplicacionais executadas em runtime (serviços, workloads, batch jobs).

Em ambos os casos, a automação **produz sinais**, não decisões.  
A aceitação do risco, a promoção entre ambientes e a autorização de execução são **responsabilidades humanas não delegáveis**.

Este capítulo articula-se diretamente com:
- **Cap. 05 — Dependências, SBOM e SCA**, tratando imagens como *supply chain artifacts* com proveniência verificável;
- **Cap. 07 — CI/CD Seguro**, onde o pipeline é reconhecido como ator crítico de risco;
- **Cap. 12 — Monitorização & Operações**, que assegura deteção e resposta em runtime.

---

## 🧭 O que cobre tecnicamente

A segurança de containers depende de uma **cadeia contínua de controlos**, desde o desenho da pipeline até à execução em produção.  
Qualquer quebra nesta cadeia compromete a confiança global.

Este capítulo cobre, de forma integrada:

- Seleção, validação e **fixação determinística** de imagens base.
- Execução em ambientes controlados (builders, runners, clusters).
- Assinatura e verificação de proveniência (ex.: SLSA, Sigstore).
- Hardening de runtime (non-root, capacidades mínimas, FS read-only).
- Políticas de execução e admissão (OPA, Kyverno).
- Integração segura com Kubernetes (RBAC, ServiceAccounts dedicadas, NetworkPolicy).
- Geração de SBOM e rastreabilidade **commit → pipeline → imagem → execução**.

Estas práticas não substituem decisão humana; fornecem **evidência técnica** que suporta essa decisão.

---

## 🧪 Pilares de governação

Sem governação explícita, a automação degrada-se rapidamente em confiança implícita.  
Este capítulo define pilares mínimos que garantem **disciplina operacional contínua**:

1. **Allowlist de registries e execução por digest**, prevenindo substituições silenciosas.
2. **Gestão de segredos fora da imagem**, com credenciais efémeras e auditáveis.
3. **RBAC mínimo e ServiceAccounts dedicadas**, nunca o *default SA* em L2/L3.
4. **NetworkPolicies com egress controlado**, limitando o *blast radius*.
5. **Golden Base Images por stack**, com SLA de patching e descontinuação.
6. **Builders e runners efémeros, mínimos e assinados**, protegendo a cadeia de build.

🔬 Em contextos L3, aplicam-se ainda controlos reforçados como **isolamento avançado (gVisor, Kata, Firecracker)**, deteção de *drift* e **promoção por estágios com aprovação explícita**.

---

## ⚙️ Como deve ser feito

A prática segura exige mecanismos **formais, repetíveis e auditáveis**.  
Resultados “plausíveis” ou “verdes” não substituem validação empírica.

De forma não exaustiva:

- Usar imagens base minimalistas, mantidas e verificadas.
- Assinar imagens e verificar proveniência antes da execução.
- Integrar scanners no CI/CD como **sinal**, com gates definidos por política.
- Executar containers com privilégios mínimos.
- Aplicar políticas de admissão sobre origem, digest, identidade e contexto.
- Gerar SBOM em cada build e ligar resultados ao pipeline.
- Manter registos auditáveis da decisão de aceitação e promoção.

Estes passos são obrigatórios porque **reduzem incerteza**, não porque eliminam risco.

---

## 📆 Quando aplicar

Os controlos devem existir desde o desenho da pipeline e manter-se ao longo do ciclo:

- Design e evolução do CI/CD.
- Seleção e manutenção de imagens base.
- Cada build e release.
- Antes de qualquer promoção ou deploy.
- Após CVEs críticos ou alterações estruturais.

A aplicação contínua evita acumulação silenciosa de risco.

---

## 👥 Quem está envolvido

A segurança de containers é transversal:

| Papel                   | Responsabilidade principal |
|-------------------------|----------------------------|
| **DevOps / Plataforma** | Definir imagens aprovadas, runners seguros e enforcement |
| **Equipa de Dev**       | Usar imagens validadas e integrar controlos nos manifests |
| **AppSec / Segurança**  | Validar cadeia de confiança e analisar sinais técnicos |
| **Infraestrutura**     | Garantir isolamento e políticas no cluster |
| **GRC / Conformidade** | Manter evidência, rastreabilidade e políticas |

A ausência de um destes papéis compromete toda a cadeia.

---

## 🎯 Para quê

Containers inseguros comprometem diretamente a integridade organizacional.

Este capítulo permite:
- Evitar execução de código adulterado.
- Reduzir superfície de ataque em pipeline e produção.
- Sustentar auditorias com evidência verificável.
- Cumprir requisitos como NIS2, SSDF e SLSA.
- Responder rapidamente a incidentes em runtime.

Agilidade só é vantagem quando acompanhada de **confiança operacional**.

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

---
