---
id: exemplo-toolchain-options
title: "Exemplo: Opções de Toolchain"
description: Exemplos de como implementar princípios de toolchain (Cap. 08, 12) com diferentes ferramentas
tags: [exemplos, toolchain, ferramentas, iac, logs, vulnerabilidades]
---

# Exemplo: Opções de Toolchain

## Enquadramento

O SbD-ToE prescreve (Cap. 08, 12):
- ✓ Infraestrutura como Código (IaC)
- ✓ Recolha centralizada de logs
- ✓ Análise de vulnerabilidades (SCA + SAST)
- ✓ Auditoria de acessos

O SbD-ToE **NÃO prescreve** qual ferramenta usar. Este documento apresenta **exemplos de diferentes stacks**.

---

## 1. Infraestrutura como Código (IaC)

### Princípio (Cap. 08)
Toda configuração de infraestrutura deve ser versionada, auditada e automatizada.

### Opção A: Terraform + AWS
```hcl
# main.tf
terraform {
  required_version = ">= 1.0"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

# Audit trail: Git commit logs, terraform state (com encryption em S3)
resource "aws_s3_bucket" "tf_state" {
  bucket = "company-terraform-state"
}

resource "aws_s3_bucket_versioning" "tf_state" {
  bucket = aws_s3_bucket.tf_state.id
  versioning_configuration {
    status = "Enabled"  # Audit trail via versioning
  }
}

resource "aws_s3_bucket_server_side_encryption_configuration" "tf_state" {
  bucket = aws_s3_bucket.tf_state.id

  rule {
    apply_server_side_encryption_by_default {
      sse_algorithm = "AES256"
    }
  }
}
```

**Evidência Auditoria (Cap. 12):**
- Git logs: `git log terraform/ --oneline --decorate`
- Terraform state history: S3 versioning
- Change approvals: GitHub branch protection + code review

---

### Opção B: CloudFormation + AWS
```yaml
AWSTemplateFormatVersion: '2010-09-09'
Description: 'CloudFormation template com auditoria'

Parameters:
  Environment:
    Type: String
    Default: prod

Resources:
  VPC:
    Type: AWS::EC2::VPC
    Properties:
      CidrBlock: 10.0.0.0/16
      EnableDnsHostnames: true
      EnableDnsSupport: true
      Tags:
        - Key: Environment
          Value: !Ref Environment
        - Key: ManagedBy
          Value: CloudFormation

  # CloudTrail para auditoria
  CloudTrailRole:
    Type: AWS::IAM::Role
    Properties:
      AssumeRolePolicyDocument:
        Version: '2012-10-17'
        Statement:
          - Effect: Allow
            Principal:
              Service: cloudtrail.amazonaws.com
            Action: sts:AssumeRole
```

**Evidência Auditoria:**
- CloudTrail logs: Quem fez deploy, o quê, quando
- Stack events: `aws cloudformation describe-stack-events`
- Change sets: Revisão antes de aplicar

---

### Opção C: Helm + Kubernetes
```yaml
# values.yaml
replicaCount: 3

image:
  repository: company/app
  tag: "1.2.3"
  pullPolicy: IfNotPresent

podSecurityContext:
  runAsNonRoot: true
  runAsUser: 1000
  fsGroup: 2000

securityContext:
  allowPrivilegeEscalation: false
  capabilities:
    drop:
      - ALL
  readOnlyRootFilesystem: true

# Audit logging
apiServer:
  auditLog:
    enabled: true
    maxAge: 30
    maxBackup: 10
    maxSize: 100
```

**Evidência Auditoria:**
- Helm release history: `helm history app-name`
- Git tags: `git tag -l v1.2.3`
- Kubernetes audit logs: Centralizados no SIEM

---

## 2. Recolha Centralizada de Logs

### Princípio (Cap. 12)
Logs de todas as aplicações, infraestrutura e acessos devem ser centralizados, retidos conforme política, e protegidos contra alteração.

### Opção A: ELK Stack (Elasticsearch + Logstash + Kibana)
```yaml
# logstash.conf
input {
  tcp {
    port => 5000
    codec => json
  }
  file {
    path => "/var/log/app/*.log"
    start_position => "beginning"
  }
}

filter {
  if [type] == "application" {
    mutate {
      add_field => { "[@metadata][index_name]" => "logs-app-%{+YYYY.MM.dd}" }
    }
    grok {
      match => { "message" => "%{TIMESTAMP_ISO8601:timestamp} %{LOGLEVEL:level} %{GREEDYDATA:msg}" }
    }
  }
}

output {
  elasticsearch {
    hosts => ["elasticsearch:9200"]
    index => "%{[@metadata][index_name]}"
    user => "${ES_USER}"
    password => "${ES_PASSWORD}"
    ssl => true
  }
}
```

**Conformidade Auditoria (Cap. 12):**
- Retenção: Policy-based (ex: 3 anos críticos, 1 ano operacional)
- Immutability: Elasticsearch read-only index após período
- Alertas: Elasticsearch Watcher para anomalias

---

### Opção B: Datadog
```python
# Python app
import logging
from datadog import initialize, statsd
from datadog_checks.base import AgentCheck

logger = logging.getLogger(__name__)

class SecurityAuditLogger:
    def __init__(self):
        self.dd_config = {
            'api_key': os.getenv('DD_API_KEY'),
            'app_key': os.getenv('DD_APP_KEY'),
        }
        initialize(**self.dd_config)
    
    def log_access(self, user, resource, action, status):
        """Log access event to Datadog"""
        event_data = {
            'title': f'Access: {action}',
            'text': f'User {user} attempted {action} on {resource}',
            'tags': ['audit', 'security', status],
            'priority': 'normal' if status == 'allowed' else 'high',
        }
        statsd.event('security.access', **event_data)
        logger.info(f"Logged: {action} by {user}")
```

**Conformidade Auditoria:**
- Retenção: Configurável (15 dias a 15 meses)
- Retention policy: API-driven
- Alerting: Query-based monitors

---

### Opção C: Azure Sentinel
```kusto
// KQL query para auditoria
SecurityEvent
| where TimeGenerated > ago(24h)
| where EventID in (4625, 4624)  // Falhas e sucessos login
| summarize FailureCount = countif(EventID == 4625), 
            SuccessCount = countif(EventID == 4624) by Account
| where FailureCount > 5
| project Account, FailureCount, SuccessCount
```

**Conformidade Auditoria:**
- Retenção: 90 dias (grátis), até 5 anos (extended)
- Immutability: Logs protegidos via Azure RBAC
- Alertas: Automation rules + Playbooks

---

## 3. Análise de Vulnerabilidades (SCA + SAST)

### Princípio (Cap. 05, 07)
Dependências e código devem ser analisados para vulnerabilidades conhecidas, integrados no CI/CD.

### Opção A: SCA + SAST com Snyk + SonarQube
```yaml
# .github/workflows/security.yml
name: Security Analysis

on: [push, pull_request]

jobs:
  sca:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Run Snyk SCA
        run: |
          npm install -g snyk
          snyk auth ${{ secrets.SNYK_TOKEN }}
          snyk test --severity-threshold=high
        continue-on-error: false  # Falha se HIGH ou CRITICAL
      
      - name: Run SonarQube SAST
        run: |
          docker run --rm \
            -e SONAR_HOST_URL=${{ secrets.SONAR_URL }} \
            -e SONAR_LOGIN=${{ secrets.SONAR_TOKEN }} \
            -v "$PWD:/src" \
            sonarsource/sonar-scanner-cli
```

**Conformidade Cap. 07:**
- Gate de segurança: Bloqueia merge se HIGH+
- Reporte: SBOM gerado (`snyk sbom --format=cyclonedx`)
- Trilho: Logs em CI/CD preservados

---

### Opção B: WhiteSource + Custom SAST
```python
# scan.py (SAST custom)
import ast
import re

class SecurityScan:
    def __init__(self, filepath):
        self.filepath = filepath
        self.vulnerabilities = []
    
    def scan_hardcoded_secrets(self):
        """Procura por secrets hardcoded"""
        with open(self.filepath, 'r') as f:
            content = f.read()
        
        patterns = [
            r'password\s*=\s*["\']([a-zA-Z0-9]+)["\']',
            r'api_key\s*=\s*["\']sk_[a-zA-Z0-9]{20,}["\']',
            r'AWS_SECRET_ACCESS_KEY\s*=\s*["\'].*["\']',
        ]
        
        for pattern in patterns:
            matches = re.finditer(pattern, content)
            for match in matches:
                self.vulnerabilities.append({
                    'type': 'Hardcoded Secret',
                    'line': content[:match.start()].count('\n') + 1,
                    'severity': 'CRITICAL',
                })
    
    def report(self):
        return {
            'file': self.filepath,
            'vulnerabilities': self.vulnerabilities,
            'status': 'PASS' if len(self.vulnerabilities) == 0 else 'FAIL'
        }
```

**Conformidade Cap. 07:**
- Gate: Rejeita se CRITICAL secrets encontrados
- Trilho: Report salvo em artefato CI/CD

---

### Opção C: Dependency Check (Open Source)
```bash
#!/bin/bash
# scan-dependencies.sh

# Análise de dependências
java -jar dependency-check/bin/dependency-check.jar \
  --scan . \
  --format JSON \
  --out ./odc-reports \
  --project "MyApp" \
  --failOnCVSS 7.0  # Falha se score >= 7.0

# Integração CI/CD
if [ $? -ne 0 ]; then
  echo "Vulnerabilities found with CVSS >= 7.0"
  exit 1
fi
```

**Conformidade Cap. 07:**
- Gratuito e open-source
- Gate de segurança integrado
- Report em múltiplos formatos

---

## 4. CI/CD com Gates de Segurança

### Princípio (Cap. 07)
Pipeline deve incluir validações de segurança, aprovações formais, e trilho auditoria completo.

### Opção A: GitHub Actions
```yaml
name: Deploy with Security Gates

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

jobs:
  security-gates:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: SAST Analysis
        run: npm run lint:security
        
      - name: SCA Analysis
        run: npm run audit --production
      
      - name: Secrets Scan
        uses: trufflesecurity/trufflehog@main
        with:
          path: ./
          base: ${{ github.event.repository.default_branch }}
          head: HEAD
      
      - name: Build Artifact
        run: npm run build
      
      - name: Sign Artifact
        run: cosign sign-blob --key cosign.key ./dist/app.tar.gz > app.tar.gz.sig
      
      - name: Upload to Registry
        run: |
          echo "${{ secrets.REGISTRY_PASSWORD }}" | docker login -u "${{ secrets.REGISTRY_USER }}" --password-stdin
          docker push myregistry/app:${{ github.sha }}
```

**Trilho Auditoria (Cap. 12):**
```
Workflow logs (7 anos retention)
├── SAST: SonarQube scan results
├── SCA: Dependency check report
├── Secrets: Trufflehog findings
├── Build: Artifact fingerprint
├── Sign: Signature verification
└── Push: Registry audit logs
```

---

### Opção B: GitLab CI
```yaml
stages:
  - security
  - build
  - deploy

sast:
  stage: security
  image: sast-scanner:latest
  script:
    - sast-scan . --format json --output sast-report.json
  artifacts:
    reports:
      sast: sast-report.json
  allow_failure: false

sca:
  stage: security
  script:
    - sca-scan . --fail-on-high
  allow_failure: false

secrets:
  stage: security
  script:
    - detect-secrets scan . --baseline .secrets.baseline
  allow_failure: false

build:
  stage: build
  script:
    - docker build -t $CI_REGISTRY_IMAGE:$CI_COMMIT_SHA .
    - docker push $CI_REGISTRY_IMAGE:$CI_COMMIT_SHA
  dependencies:
    - sast
    - sca
    - secrets

approval:
  stage: deploy
  script:
    - echo "Manual approval required for production"
  when: manual
  only:
    - main

deploy:
  stage: deploy
  script:
    - helm upgrade --install app ./chart
  environment:
    name: production
  when: on_success
  only:
    - main
```

**Segregação Responsabilidades (Cap. 14):**
- SAST/SCA: Automático
- Secrets: Automático
- Approval: Manual (via UI)
- Deploy: Via RBAC

---

## Síntese

| Dimensão | Princípio (SbD-ToE) | Opção A | Opção B | Opção C |
|----------|---|---|---|---|
| **IaC** | Cap. 08 | Terraform | CloudFormation | Helm |
| **Logs** | Cap. 12 | ELK | Datadog | Azure Sentinel |
| **SCA** | Cap. 05 | Snyk | WhiteSource | Dep-Check |
| **SAST** | Cap. 05 | SonarQube | Custom | TruffleHog |
| **CI/CD** | Cap. 07 | GitHub Actions | GitLab CI | Jenkins |

**Nenhuma combinação é "correta"** - cada organização escolhe conforme:
- Arquitetura existente
- Expertise disponível
- Orçamento
- Compliance local

---

## Próximas Etapas

1. **Avaliar contexto:** Qual stack tecnológico já existe?
2. **Pilotar:** Implementar uma opção num projeto piloto
3. **Validar:** Testar gates, trilho auditoria, escalabilidade
4. **Iterar:** Ajustar conforme lições aprendidas
5. **Documentar:** Atualizar políticas internas com stack escolhido

---

**Versão:** 1.0  
**Data:** Novembro 2025  
**Feedback:** Adaptar conforme evolução tecnológica
