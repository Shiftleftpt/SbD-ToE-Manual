---
id: policies-relevantes
title: Policies
description: Políticas organizacionais necessárias para garantir segurança, rastreabilidade e governação de containers e imagens ao longo do ciclo de vida.
tags: [políticas, containers, imagens, supply chain, kubernetes, devsecops, cloud]
sidebar_position: 60
---

# 🏠 Políticas Organizacionais — Containers e Imagens

A aplicação eficaz do **Capítulo 09 - Containers e Imagens** requer a existência de **políticas organizacionais formais** que enquadrem e reforcem as práticas de construção, validação, assinatura, governação e execução de containers e imagens.

Estas políticas asseguram que:

- As imagens são construídas de forma **segura, rastreável e reprodutível**, com proveniência verificável;  
- A execução de containers ocorre em ambientes **protegidos, auditáveis e controlados**;  
- Existe **governação clara sobre os registos e pipelines** que manipulam artefactos de containerização.

---

## 📄 Políticas Organizacionais Relevantes

| Nome da Política | Obrigatória? | Aplicação | Resumo do Conteúdo Necessário |
|------------------|--------------|------------|--------------------------------|
| **Política de Construção Segura de Imagens** | ✅ Sim | Todos os pipelines de build | Define requisitos de base segura, _digest pinning_, versões fixas, _linting_ e validação automática de Dockerfiles; obriga revisão e aprovação antes de publicação. |
| **Política de Gestão de Vulnerabilidades em Imagens** | ✅ Sim | Registos e pipelines CI/CD | Obriga _scanning_ automatizado (SCA, CVE, licenças); define critérios de severidade e prazos de correção; bloqueio em vulnerabilidades críticas. |
| **Política de Assinatura e Proveniência de Imagens** | ✅ Sim | Registos internos e externos | Exige assinatura digital (Sigstore/Cosign), _attestations_ SLSA e verificação de integridade antes da execução. |
| **Política de Governação de Registos e Repositórios de Containers** | ✅ Sim | Todos os registos e repositórios internos | Define _ownership_, controlo de acesso, _RBAC_, retenção, limpeza periódica, auditoria e _access logs_. |
| **Política de Hardening e Execução Segura de Containers** | ⚠️ Reforçada | Ambientes de execução (Docker, Kubernetes, etc.) | Define parâmetros mínimos de isolamento (seccomp, AppArmor, SELinux), _network policies_, _least privilege_ e _read-only rootfs_. |
| **Política de Gestão de Imagens Obsoletas e Limpeza** | ⚠️ Recomendável | Repositórios e pipelines | Estabelece prazos de retenção, políticas de _rebuild_ e remoção de imagens vulneráveis ou sem uso. |
| **Política de Validação e Aprovação de Manifestos de Deploy** | ⚠️ Reforçada | Kubernetes, Compose, Helm | Obriga validação automatizada de manifestos com _policy-as-code_ (OPA, Conftest) e _admission controllers_ de segurança. |
| **Política de Observabilidade e Auditoria de Execução de Containers** | ⚠️ Reforçada | Ambientes produtivos | Determina recolha de métricas, _runtime logs_, correlação commit-digest-deploy e alertas automáticos para _shadow containers_. |

---

## 📃 Estrutura mínima de cada política

Cada política deve conter:

- **Objetivo e âmbito** (artefactos, pipelines, ambientes abrangidos);  
- **Papéis e responsabilidades** (DevOps, Cloud Ops, AppSec, Auditoria);  
- **Controlos técnicos obrigatórios** (validações automáticas, gates, segregação de funções);  
- **Integração CI/CD** (pontos de controlo e bloqueios automáticos);  
- **Evidências e métricas** (relatórios de _scan_, logs, _attestations_, auditorias);  
- **Frequência de revisão** e procedimento de atualização da política.

---

## ✅ Recomendações finais

- Todas as políticas devem ser **publicadas e aprovadas pela direção de segurança e engenharia**, e integradas nos processos de *DevSecOps*.  
- A conformidade deve ser **validada periodicamente** através de _checklists_, auditorias técnicas e métricas de maturidade.  
- As políticas devem alinhar-se com as práticas de **Gestão de Dependências** (Cap. 05) e **IaC** (Cap. 08) para garantir coerência da cadeia de fornecimento.  
- Recomenda-se automatizar a verificação de conformidade via **_policy-as-code_**, integrando as regras nos _pipelines_ de build e deploy.  
- A aplicação destas políticas constitui evidência direta de conformidade com **SSDF, SLSA, CIS, ENISA e SAMM** em contexto de **software supply chain security**.

> 📁 Templates e exemplos práticos poderão ser incluídos em futuras versões do manual como ficheiros complementares `60-*.md`.
