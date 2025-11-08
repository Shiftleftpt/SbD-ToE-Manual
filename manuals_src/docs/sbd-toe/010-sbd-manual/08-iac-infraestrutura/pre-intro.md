---
id: pre-intro
title: Fundamentação
description: Porque este capítulo é excecional, que fontes suportam o catálogo IAC-XXX e como criar/adaptar o catálogo organizacional
tags: [iac, rationale, requisitos, catálogo, segurança, pipelines, terraform, kubernetes, cloud]
sidebar_position: -1
---

# 📑 Rationale - Catálogo de Requisitos de IaC

## 🧠 Porque este capítulo é **excecional**

Este capítulo é diferente dos restantes.  
Enquanto o **Cap. 02 - Requisitos de Segurança** define uma base comum aplicável a qualquer software, aqui apresentamos um **catálogo técnico especializado (`IAC-XXX`)** que cobre riscos e controlos específicos da **Infraestrutura como Código (IaC)**.  

Falamos de aspetos como:  
- integridade do estado,  
- validações automáticas em *plan/apply*,  
- composição de ambientes,  
- rastreabilidade ficheiro→recurso→ambiente,  
- enforcement no pipeline.  

👉 Cada requisito `IAC-XXX` dá origem a uma **user story própria**, permitindo uma cobertura exaustiva e auditável, sem lacunas nem ambiguidades.

---

## 🔑 Pontos fundamentais da excecionalidade

### a) Ciclo de vida e equipas diferentes

Projetos de **IaC têm um ciclo de vida distinto** dos projetos aplicacionais.  
Normalmente:

- **Arquitetura/Infra/Plataforma** mantêm o IaC, definindo clusters, rede, permissões, storage, etc.  
- **Equipas de Desenvolvimento Aplicacional** usam essa infraestrutura para colocar software em produção, mas não controlam a sua configuração de base.

👉 Esta separação significa que os leitores deste capítulo podem ser diferentes dos de outros: aqui o foco está em quem constrói e governa a infraestrutura, não apenas em quem desenvolve aplicações.

### b) IaC também é software

Apesar de peculiar, um projeto de IaC **é, no fundo, um projeto de software**.  
Logo, deve cumprir os controlos transversais já definidos no SbD-ToE:

- Classificação de risco (Cap. 01)  
- Threat modeling (Cap. 03)  
- Pipelines seguros (Cap. 07)  
- Gestão de dependências e SBOM (Cap. 05)  
- Validações automáticas (linters, SAST para IaC)  
- Governação e auditoria (Cap. 14)

⚠️ A diferença é que um erro no IaC **não afeta apenas uma aplicação**, mas sim todas as aplicações que dependem dessa infraestrutura.  
Daí o rigor: IaC deve ser tratado com a mesma disciplina científica aplicada ao código que serve.

---

## 📚 Fontes técnicas que fundamentam o catálogo

O catálogo `IAC-XXX` não é arbitrário: resulta da síntese de **fontes normativas e de mercado**.  
Entre elas:

- **CIS Benchmarks** (AWS, Azure, GCP, Kubernetes, Docker, Terraform)  
- **Kubernetes** (Pod Security Standards, Network Policies, Admission Control, Audit Logging)  
- **NIST SP 800-53** e **NIST SP 800-190**  
- **Cloud Security Alliance – CCM**  
- **ISO/IEC 27001** (Annex A: change control, least privilege, segregation of duties)  
- **SSDF (NIST 800-218)** e **SLSA** (supply chain)  
- **Práticas de mercado** (Terraform, Pulumi, OPA, Sentinel, Kyverno)

---

## 🧩 Relação com o Cap. 02 - Requisitos de Segurança

- Os requisitos `IAC-XXX` **complementam** os `SEC-XXX` do Cap. 02.  
- Sempre que possível, estabelecemos rastreabilidade direta:  

| Requisito IaC | Objetivo | Mapeamento Cap. 02 | Nota |
|---------------|----------|--------------------|------|
| IAC-001 Backend remoto com locking | Integridade do estado | SEC-CFG-STATE | Uso de S3+DynamoDB+KMS |
| IAC-003 Validações automáticas | Evitar más práticas | SEC-VAL-SHIFTLEFT | `tflint`, `tfsec`, `OPA` em PR |
| IAC-007 Revisão de `plan` | Change control formal | SEC-CRL-PR | `plan` anexado a PR; gate de aprovação |
| IAC-010 Assinatura/Proveniência | Supply chain | SEC-SUPPLY-PROV | Assinatura + proveniência verificada |

---

## 🧱 Como adaptar o catálogo organizacional

O catálogo aqui publicado (`IAC-001` a `IAC-010`) é um **baseline prescritivo**.  
Cada organização deve adaptá-lo à sua realidade, seguindo uma metodologia clara:

1. Inventariar *stacks* e *providers* usados  
2. Classificar riscos (L1–L3)  
3. Selecionar requisitos aplicáveis  
4. Definir thresholds/gates (falhas High/Critical bloqueiam em L2/L3)  
5. Especificar evidências esperadas (logs, `plan`, SBOM, assinaturas)  
6. Automatizar validações (linters, policies, proveniência)  
7. Governar exceções (registo, prazo, compensações, dupla aprovação em L3)  
8. Auditar e melhorar continuamente (scorecards, métricas de drift, falhas bloqueadas)  

---

## 🧾 Porquê user stories por requisito

Ao contrário de outros capítulos, aqui não trabalhamos apenas com práticas macro.  
Cada `IAC-XXX` transforma-se numa **user story própria**, porque isso:

- Garante que nenhum requisito fica esquecido  
- Permite integração direta em backlog (cartões reutilizáveis)  
- Assegura rastreabilidade requisito → evidência → prática  
- Facilita a proporcionalidade L1–L3 requisito a requisito

---

## ⚖️ Proporcionalidade L1–L3 (princípios aplicados a IaC)

| Domínio | L1 (baixo) | L2 (médio) | L3 (crítico) |
|---------|------------|------------|--------------|
| Validações automáticas | Aviso | Bloqueio High/Critical | Bloqueio Medium+ |
| Aprovação de `plan` | Recomendado | Obrigatório | Obrigatório + dupla aprovação |
| Backend remoto/estado | Recomendado | Remoto com locking | Remoto + monitorização e break-glass |
| Origem de módulos | Pinagem recomendada | Pinagem obrigatória | Allowlist + revisão formal + SBOM |
| Assinatura/proveniência | Recomendado | Obrigatório | Obrigatório + rejeição automática |

---

## 📦 Evidências esperadas

- Estrutura de repo por ambiente; `backend.tf`  
- Pipelines com lint/security/policies em PR e main  
- `terraform plan` anexado a PR, aprovado antes de `apply`  
- Registo de exceções com prazo e compensações  
- SBOM de módulos/providers  
- Assinaturas + proveniência (SLSA)  
- Logs correlacionados commit→pipeline→apply  
- Dashboards de compliance e drift  

---

## 🚫 Anti-padrões frequentes em IaC

Aprender com erros recorrentes é essencial.  
Entre os anti-padrões mais perigosos, destacam-se:

- **Terraform local state sem locking** → corrupção concorrente  
- **Apply direto a produção sem plan aprovado** → alterações não rastreáveis  
- **Módulos externos pinados a branch (`main`)** → risco de supply chain  
- **Ausência de network policies/admission control** → superfícies de ataque expandidas  
- **Segredos hardcoded em variáveis IaC** → exposição acidental  
- **Falta de SBOM/assinatura de artefactos** → builds e deploys não confiáveis  

---

## 🏛️ Governação e métricas

Um catálogo só é eficaz se for governado e medido.  
Recomendamos:

- **Ownership**: Arquitetura/Plataforma + AppSec  
- **Revisão periódica**: trimestral do catálogo `IAC-XXX`  
- **KPIs/KRIs**:  
  - % de PRs com `plan` aprovado antes de `apply`  
  - Cobertura de scanners em IaC  
  - % de módulos pinados/validados  
  - Nº e idade média de exceções ativas  
  - Drift detetado e tempo até correção  

---

## 📌 Como ler este capítulo

1. Ler este **Rationale** para compreender a excecionalidade e metodologia.  
2. Seguir para o **intro.md** para o enquadramento, papéis e políticas.  
3. Usar o **aplicacao-lifecycle.md** para integração prática no SDLC.  
4. Consultar o **20-checklist-revisao.md** para controlo operacional.  
5. Rever exemplos e templates no diretório `addon/`.

👉 Em resumo: **Requisitos → User Stories → Evidências → Proporcionalidade → Auditoria.**  
É esta cadeia que assegura que o IaC é tratado com o mesmo rigor científico de qualquer outro artefacto crítico de software.

---
