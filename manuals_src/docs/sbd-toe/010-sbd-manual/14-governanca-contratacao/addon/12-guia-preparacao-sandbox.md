---
id: guia-preparacao-sandbox
title: Guia de Preparação Sandbox para Contractors
description: Setup e utilização de ambiente isolado para formação prática de contractors antes de acesso a sistemas reais
tags: [contractors, formacao, governanca, onboarding, pratica, sandbox]
---

# 🏜️ Guia de Preparação Sandbox para Contractors

**Versão:** 1.0  
**Última atualização:** Novembro 2025  
**Responsável:** DevOps + AppSec Engineer + Training Manager  
**Ciclo de vida:** Criação T-5 dias, ativo durante onboarding (1–2 semanas), destruição pós-conclusão

---

## 📖 Objetivo

Fornecer **ambiente isolado, seguro e controlado** onde contractors praticam:
- Uso de ferramentas corporativas (Git, CI/CD, SCA, SAST, etc.)
- Procedimentos de segurança (secrets management, MFA, etc.)
- Workflows de código seguro antes de acesso real a produção

**Benefício:** Reduz risco de erro em produção, aumenta confiança do contractor, valida compreensão de políticas.

---

## 🎯 Tipos de Sandbox (por Perfil)

### 1️⃣ Sandbox para Developers

**âmbito:** Git, CI/CD, secrets management, SAST/SCA, code review workflow

#### 1.1 GitHub/GitLab Organization Private

```
Estrutura:
├─ Org: "sandbox-contractors"
├─ Team: "contractors-L1" (se L1)
├─ Repo: "sandbox-app-basic" (demo app segura)
│   ├─ Dockerfile (para container building)
│   ├─ package.json (com dependências)
│   ├─ .github/workflows (CI/CD demo)
│   ├─ README.md (onboarding guide)
│   └─ exercises/ (exercícios práticos)
└─ Repo: "sandbox-app-vulnerable" (app com vulnerabilidades intencionais - OWASP Top 10)
    ├─ SQL injection example
    ├─ XSS example
    ├─ CSRF example
    └─ Authentication bypass example
```

**Acesso:**
- Contractor recebe invite para organização privada
- Permissões: **pull-only** inicialmente
  - Pode clonar e praticar
  - Pode comentar em issues/PRs
  - Não pode fazer push direto
- Após validação: **branch-write** (criar branches, PR)
- Nunca: acesso a main branch até aprovação final

**Duração:** 1 semana

**Exercícios Práticos:**
1. Clone repo e setup local environment
2. Identificar 3 vulnerabilidades em `sandbox-app-vulnerable`
3. Escrever test case seguro
4. Criar PR (sem merge) com melhoria de segurança

---

#### 1.2 CI/CD Pipeline Demo (GitHub Actions / GitLab CI)

```yaml
# .github/workflows/security-checks-demo.yml
name: Security Checks Demo

on: [pull_request]

jobs:
  sast:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Run SonarQube SAST (demo)
        run: |
          # Simular execução de SonarQube
          echo "SAST: Checking code for vulnerabilities..."
          # Retorna findings (demo)
  sca:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Run Snyk SCA (demo)
        run: |
          # Simular execução de Snyk
          echo "SCA: Checking dependencies for CVEs..."
  secrets:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Secrets scanning (demo)
        run: |
          # Simular secrets detection
          echo "Scanning for hardcoded secrets..."
```

**Objetivo:** Contractor vê workflow automático em ação, compreende verificações obrigatórias

---

#### 1.3 Secrets Management Demo (Vault / Azure Key Vault)

```
Setup Sandbox:
├─ Vault (local Docker ou cloud demo)
├─ Path: "/sandbox/contractors/{contractor-name}"
├─ Secrets pré-configurados:
│   ├─ API_KEY_DEMO=sk_demo_xxx (fake)
│   ├─ DB_PASSWORD=demo_password (fake)
│   └─ JWT_SECRET=demo_secret (fake)
└─ Instruções: Como aceder, rotacionar, reportar vazamento
```

**Exercício:** 
- Contractor acede ao Vault, revela um secret
- Tira screenshot do processo
- Aprende que secrets nunca devem estar hardcoded

---

### 2️⃣ Sandbox para DevOps/Infrastructure

**âmbito:** IaC, containers, Kubernetes, secrets, CI/CD pipelines

#### 2.1 Kubernetes Sandbox Cluster

```
Setup:
├─ Namespace: "sandbox-contractors"
├─ RBAC: Contractor tem role "viewer" + "editor" em namespace
├─ Deployments pré-criados:
│   ├─ demo-app (insegura)
│   ├─ demo-app-hardened (segura)
│   └─ metrics-server (para observability demo)
├─ Resources:
│   ├─ 2 pods, 1 GB RAM max, 500m CPU max
│   ├─ Network policies (demo)
│   └─ Security contexts (demo)
└─ Logs: Prometheus/Grafana acesso read-only
```

**Exercícios:**
1. Deploy aplicação simples (via YAML manifesto)
2. Comparar segurança: "insecure vs. hardened" deployment
3. Identificar 3 issues de segurança
4. Propor correções (IaC)

#### 2.2 Terraform/CloudFormation Demo

```
Scenario:
├─ Estado inicial: VPC insegura (open security groups)
├─ Contractor tarefa: Corrigir 5 issues de IaC
│   ├─ Add security group restrictions
│   ├─ Enable encryption
│   ├─ Add network policies
│   └─ Enable logging
└─ Validação: Terraform plan review (não apply)
```

---

### 3️⃣ Sandbox para QA/Testers

**âmbito:** Teste de segurança, OWASP, ferramentas de scanning

#### 3.1 Web App para Teste Manual (OWASP WebGoat / Juice Shop)

```
Setup:
├─ Deploy OWASP Juice Shop em sandbox k8s
├─ Acesso: http://sandbox-qa.internal:8080
├─ Tasks pré-definidas:
│   ├─ SQL Injection (ranked by difficulty)
│   ├─ XSS (cross-site scripting)
│   ├─ CSRF (cross-site request forgery)
│   ├─ Broken authentication
│   └─ Sensitive data exposure
└─ Scoring: Contractor completa 70% das tasks
```

#### 3.2 ZAP (OWASP Zap) Demo Scanning

```bash
# Setup ZAP no sandbox
docker run -t owasp/zap2docker-stable zap-baseline.py \
  -t http://sandbox-qa:8080 \
  -r report.html

# Contractor aprende:
# - Como executar DAST
# - Interpretar findings
# - Falsos positivos
# - Remediação
```

---

## 🚀 Processo de Criação e Provisão

### Timeline

```
T-5 dias: Setup começa
  ├─ DevOps cria infrastructure (repos, k8s ns, IaC)
  ├─ AppSec configura permissões e logging
  └─ Training Manager prepara exercícios

T-3 dias: Sandbox ready
  ├─ Teste de acesso funciona
  ├─ Documentação criada
  └─ Contractor recebe credenciais

T-0 (Onboarding):
  ├─ Contractor recebe email com links + instruções
  ├─ First exercise: "Setup environment locally"
  ├─ Daily check-ins com Tech Lead
  └─ Logging de atividade ativado

T+7 dias: Validação
  ├─ Contractor completou 70%+ de exercícios
  ├─ Quiz de compreensão passed (>80%)
  └─ Sign-off → Acesso real concedido
```

### Checklist de Provisão

```yaml
Pre-Sandbox:
  - [ ] Contractor validado (US-06 passed)
  - [ ] Role/função definida (Dev, DevOps, QA, etc.)
  - [ ] LMS enrollment completado
  - [ ] Email corporativo criado (ou temporário)

Sandbox Creation:
  - [ ] Git org criado (ou branch/namespace)
  - [ ] Demo repos clonados
  - [ ] K8s namespace criado
  - [ ] IaC templates preparados
  - [ ] Permissões RBAC configuradas (read-only initially)
  - [ ] Secrets criados (demo/fake values)
  - [ ] Logging/monitoring ativado

Access Provisioning:
  - [ ] Git credentials (SSH key ou token) entregues seguramente
  - [ ] Kubeconfig criado
  - [ ] VPN access (se necessário)
  - [ ] Email de boas-vindas com links + instruções

Validation:
  - [ ] Contractor conecta com sucesso (first login captured)
  - [ ] Pode clonar repos
  - [ ] Pode visualizar k8s namespace
  - [ ] Exercícios acessíveis
```

---

## 📋 Exercícios Padrão por Perfil

### Para Developers

| # | Exercício | Duração | Objetivo | Sucesso |
|----|-----------|---------|----------|---------|
| 1 | Clone & Setup | 1h | Familiarizar com Git, local dev env | Git clone OK, README seguido |
| 2 | Identificar Vulns | 2h | Compreender OWASP Top 10 | ≥3 vulns identificadas |
| 3 | Secure Coding | 2h | Escrever código seguro | Function com test passando |
| 4 | Create PR | 1h | Workflow PR, code review | PR criada corretamente |
| **Total** | | **6h** | | ✅ Score ≥70% |

### Para DevOps

| # | Exercício | Duração | Objetivo | Sucesso |
|----|-----------|---------|----------|---------|
| 1 | Deploy Insecure | 1h | Deploy app no k8s | Pod running |
| 2 | Identify Issues | 2h | Audit de segurança de IaC | ≥5 issues found |
| 3 | Hardening | 2h | Corrigir issues (não apply) | Terraform plan review OK |
| 4 | Network Policies | 1h | Add restrictions | Policy defined |
| **Total** | | **6h** | | ✅ Score ≥70% |

### Para QA/Testers

| # | Exercício | Duração | Objetivo | Sucesso |
|----|-----------|---------|----------|---------|
| 1 | OWASP Top 10 | 2h | Conhecimento de vulns comuns | Quiz 70% |
| 2 | Manual Testing | 2h | Explorar Juice Shop | ≥5 vulnerabilities exploited |
| 3 | DAST Scanning | 1h | Usar ZAP | Report gerado, findings interpretados |
| 4 | False Positives | 1h | Validar achados | 3+ falsos positivos identificados |
| **Total** | | **6h** | | ✅ Score ≥70% |

---

## 🔐 Segurança do Sandbox

### Isolamento

- **Network:** Sandbox conecta a sandbox network, sem acesso direto a produção
- **Storage:** Dados no sandbox são efémeros (deleted pós-onboarding)
- **Compute:** Resource limits aplicados (CPU, memory, disk)
- **Logging:** Todas as ações logged (read, write, delete)

### Monitorização

```yaml
Logging:
  - Todos os logins capturados (timestamp, IP)
  - Git commits/pushes auditados
  - K8s API calls em audit log
  - Secret access tracked
  - Alertas se comportamento suspeito:
      - Download of /etc/shadow (Linux)
      - Git push com thousands of files
      - Multiple failed login attempts
```

### Destruição Pós-Onboarding

```bash
# T+14 dias (ou após conclusão)
T-1 dia: Contractor notificado que sandbox será destruído amanhã
T+0: Backup de work realizado (se necessário)
     Contractor removido de org/namespace
     Credentials revogadas
     Resources deletados
     Logs arquivados (7 anos)
```

---

## 📚 Documentação e Instruções

Cada sandbox inclui **README.md com:**

```markdown
# Sandbox Onboarding Guide

## Bem-vindo!

Este é seu ambiente de prática seguro. Aqui pode aprender sem risco de impactar produção.

### Quick Start

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/[org]/sandbox-app.git
   ```

2. **Setup local environment:**
   ```bash
   cd sandbox-app
   cp .env.example .env
   # Não substitua secrets - use Vault
   ```

3. **Executar testes de segurança:**
   ```bash
   npm install
   npm run test:security
   ```

### Exercícios

Comece com Exercício 1: [Link]

### Pedir Ajuda

- Slack: #sandbox-support
- Email: [security-email]
- Escalação: Tech Lead [name]

### Logs de Atividade

A sua atividade está sendo monitorizada (logs auditados). Isto é normal e esperado.

### Deadline

Exercícios devem ser completados até [data]. Quiz passa em [data + 1].

---
```

---

## 🎓 Integration com Cap. 13 (Formação)

Sandbox é **componente prático de US-16 (Trilho de Formação)**:

- Trilho teórico: LMS + cursos online
- Trilho prático: Sandbox exercises
- Validação: Quiz + Exercise score

**SLA de Conclusão:** T+7 dias = onboarding completo

---

## 🏁 Checklist de Término

```
[ ] Contractor completou 70% exercícios
[ ] Quiz score ≥80%
[ ] Tech Lead validou compreensão (conversation check-in)
[ ] AppSec Engineer reviewed logs (sem red flags)
[ ] Backup de work realizado
[ ] Sandbox credentials revogadas
[ ] Sign-off de conclusão assinado
[ ] Histórico arquivado (7 anos)
[ ] Acesso real concedido (US-15 completo)
```

---

## 📎 Templates e Links

- [Contractor Validation Template](02-template-validacao-contractors.md)
- [Preparação Técnica - US-15](../aplicacao-lifecycle.md#us-15)
- [Formação e Onboarding - Cap. 13](/sbd-toe/sbd-manual/formacao-onboarding/aplicacao-lifecycle)
- [Offboarding Checklist](13-checklist-offboarding.md)

---

## 🔄 Melhoria Contínua

**Feedback Loop:**
1. Contractor completa sandbox
2. AppSec Engineer revê logs
3. Feedback capturado (what worked, what was confusing)
4. Exercises iteradas trimestralmente
5. Novos cenários de ameaça incluídos

**Propriedade:** DevOps + AppSec Engineer  
**Revisão:** Quarterly (mínimo)
