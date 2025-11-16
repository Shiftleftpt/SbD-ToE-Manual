---
id: exemplo-toolchain-options
title: "Exemplo: Opções de Toolchain"
description: Exemplos de como implementar princípios de toolchain com diferentes ferramentas
tags: [exemplos, toolchain, ferramentas, iac, logs, vulnerabilidades]
---

# Exemplo: Opções de Toolchain

## Enquadramento

O SbD-ToE prescreve ([Cap. 08](/sbd-toe/sbd-manual/iac-infraestrutura/intro), [Cap. 12](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro)):
- ✓ Infraestrutura como Código (IaC)
- ✓ Recolha centralizada de logs
- ✓ Análise de vulnerabilidades (SCA + SAST)
- ✓ Auditoria de acessos

O SbD-ToE **NÃO prescreve** qual ferramenta usar. Este documento apresenta **exemplos de diferentes stacks**.

---

## 1. Infraestrutura como Código (IaC)

### Princípio ([Cap. 08](/sbd-toe/sbd-manual/iac-infraestrutura/intro))
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

**Evidência Auditoria ([Cap. 12](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro)):**
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

### Princípio ([Cap. 12](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro))
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

**Conformidade Auditoria ([Cap. 12](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro)):**
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

### 2.1. Integração Aplicacional: Como Fazer Push de Logs

As opções acima mostram **onde** centralizar logs. Esta secção mostra **como** as aplicações enviam logs para essas infraestruturas.

<details>
<summary><strong>📘 .NET (ASP.NET Core) → Elasticsearch/Datadog</strong></summary>

**Opção 1: Serilog + Elasticsearch**
```csharp
// Program.cs
using Serilog;
using Serilog.Sinks.Elasticsearch;

var builder = WebApplication.CreateBuilder(args);

// Configurar Serilog
Log.Logger = new LoggerConfiguration()
    .MinimumLevel.Information()
    .MinimumLevel.Override("Microsoft", LogEventLevel.Warning)
    .Enrich.FromLogContext()
    .Enrich.WithMachineName()
    .Enrich.WithEnvironmentName()
    .Enrich.WithProperty("Application", "MyApp")
    .WriteTo.Console()
    .WriteTo.Elasticsearch(new ElasticsearchSinkOptions(new Uri("https://elasticsearch:9200"))
    {
        AutoRegisterTemplate = true,
        IndexFormat = "logs-myapp-{0:yyyy.MM.dd}",
        ModifyConnectionSettings = conn => conn
            .BasicAuthentication("user", "password")
            .ServerCertificateValidationCallback((o, cert, chain, errors) => true), // Prod: validar cert!
        EmitEventFailure = EmitEventFailureHandling.WriteToSelfLog,
        FailureCallback = e => Console.WriteLine($"Unable to submit event {e.MessageTemplate}"),
    })
    .CreateLogger();

builder.Host.UseSerilog();

var app = builder.Build();

// Exemplo de logging estruturado
app.MapGet("/api/users/{id}", (int id, ILogger<Program> logger) =>
{
    logger.LogInformation("User access: {UserId} at {Timestamp}", id, DateTime.UtcNow);
    return Results.Ok(new { id, name = "User" });
});

app.Run();
```

**Opção 2: Serilog + Datadog**
```csharp
// Program.cs
using Serilog;
using Serilog.Sinks.Datadog.Logs;

Log.Logger = new LoggerConfiguration()
    .WriteTo.DatadogLogs(
        apiKey: Environment.GetEnvironmentVariable("DD_API_KEY"),
        source: "csharp",
        service: "myapp",
        host: Environment.MachineName,
        tags: new[] { "env:prod", "version:1.0" }
    )
    .CreateLogger();
```

**NuGet Packages:**
```xml
<ItemGroup>
  <PackageReference Include="Serilog.AspNetCore" Version="8.0.0" />
  <PackageReference Include="Serilog.Sinks.Elasticsearch" Version="10.0.0" />
  <PackageReference Include="Serilog.Sinks.Datadog.Logs" Version="0.5.2" />
  <PackageReference Include="Serilog.Enrichers.Environment" Version="3.0.0" />
</ItemGroup>
```

</details>

---

<details>
<summary><strong>📗 Node.js (Express) → Elasticsearch/Datadog</strong></summary>

**Opção 1: Winston + Elasticsearch**
```javascript
// logger.js
const winston = require('winston');
const { ElasticsearchTransport } = require('winston-elasticsearch');

const esTransportOpts = {
  level: 'info',
  clientOpts: {
    node: 'https://elasticsearch:9200',
    auth: {
      username: process.env.ES_USER,
      password: process.env.ES_PASSWORD,
    },
    tls: {
      rejectUnauthorized: true, // Prod: validar certificado
    },
  },
  index: 'logs-nodeapp',
  dataStream: true, // Usar data streams do ES 8+
};

const logger = winston.createLogger({
  level: 'info',
  format: winston.format.combine(
    winston.format.timestamp(),
    winston.format.errors({ stack: true }),
    winston.format.json()
  ),
  defaultMeta: { service: 'node-api', environment: process.env.NODE_ENV },
  transports: [
    new winston.transports.Console(),
    new ElasticsearchTransport(esTransportOpts),
  ],
});

module.exports = logger;

// app.js
const express = require('express');
const logger = require('./logger');

const app = express();

app.get('/api/users/:id', (req, res) => {
  logger.info('User access', { 
    userId: req.params.id, 
    ip: req.ip,
    userAgent: req.get('user-agent'),
  });
  res.json({ id: req.params.id, name: 'User' });
});

app.listen(3000, () => logger.info('Server started on port 3000'));
```

**Opção 2: Winston + Datadog**
```javascript
const winston = require('winston');
const { createLogger } = require('datadog-winston');

const logger = createLogger({
  apiKey: process.env.DD_API_KEY,
  hostname: 'myapp-prod',
  service: 'node-api',
  ddsource: 'nodejs',
  ddtags: 'env:prod,version:1.0',
});

logger.info('Application started', { pid: process.pid });
```

**NPM Packages:**
```json
{
  "dependencies": {
    "winston": "^3.11.0",
    "winston-elasticsearch": "^0.17.4",
    "datadog-winston": "^2.0.0"
  }
}
```

</details>

---

<details>
<summary><strong>🐍 Python (FastAPI/Django) → Elasticsearch/Datadog</strong></summary>

**Opção 1: Python logging + Elasticsearch**
```python
# logging_config.py
import logging
from cmreslogging.handlers import CMRESHandler

def setup_elasticsearch_logging():
    """Configura logging para Elasticsearch"""
    
    handler = CMRESHandler(
        hosts=[{'host': 'elasticsearch', 'port': 9200}],
        auth_type=CMRESHandler.AuthType.BASIC_AUTH,
        auth_details=('user', 'password'),
        es_index_name='logs-python-app',
        use_ssl=True,
        verify_ssl=True,
        es_additional_fields={
            'app': 'python-api',
            'environment': 'production'
        }
    )
    
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    logger.addHandler(handler)
    
    # Também log para console
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    ))
    logger.addHandler(console_handler)
    
    return logger

# main.py (FastAPI)
from fastapi import FastAPI
from logging_config import setup_elasticsearch_logging

logger = setup_elasticsearch_logging()
app = FastAPI()

@app.get("/api/users/{user_id}")
async def get_user(user_id: int):
    logger.info(
        "User access",
        extra={
            'user_id': user_id,
            'endpoint': '/api/users',
            'action': 'read'
        }
    )
    return {"id": user_id, "name": "User"}
```

**Opção 2: Python + Datadog**
```python
from ddtrace import tracer
from ddtrace.contrib.logging import patch as ddtrace_patch_logging
import logging

# Patch logging para adicionar trace context
ddtrace_patch_logging()

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s [dd.service=%(dd.service)s dd.trace_id=%(dd.trace_id)s] %(message)s'
)

logger = logging.getLogger(__name__)

# FastAPI com Datadog APM
from fastapi import FastAPI
from ddtrace.contrib.asgi import TraceMiddleware

app = FastAPI()
app.add_middleware(TraceMiddleware, service="python-api")

@app.get("/api/users/{user_id}")
async def get_user(user_id: int):
    logger.info(f"User access: {user_id}")
    return {"id": user_id}
```

**PIP Requirements:**
```txt
CMRESHandler==1.0.0
python-elasticsearch==8.11.0
ddtrace==2.3.0
```

</details>

---

<details>
<summary><strong>☕ Java (Spring Boot) → Elasticsearch/Datadog</strong></summary>

**Opção 1: Logback + Elasticsearch (via Logstash)**
```xml
<!-- logback-spring.xml -->
<configuration>
    <appender name="LOGSTASH" class="net.logstash.logback.appender.LogstashTcpSocketAppender">
        <destination>logstash:5000</destination>
        
        <encoder class="net.logstash.logback.encoder.LogstashEncoder">
            <customFields>{"app":"spring-api","env":"prod"}</customFields>
        </encoder>
        
        <keepAliveDuration>5 minutes</keepAliveDuration>
        <reconnectionDelay>10 seconds</reconnectionDelay>
    </appender>
    
    <appender name="CONSOLE" class="ch.qos.logback.core.ConsoleAppender">
        <encoder>
            <pattern>%d{HH:mm:ss.SSS} [%thread] %-5level %logger{36} - %msg%n</pattern>
        </encoder>
    </appender>
    
    <root level="INFO">
        <appender-ref ref="LOGSTASH" />
        <appender-ref ref="CONSOLE" />
    </root>
</configuration>
```

```java
// UserController.java
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/api/users")
public class UserController {
    private static final Logger logger = LoggerFactory.getLogger(UserController.class);
    
    @GetMapping("/{id}")
    public User getUser(@PathVariable Long id) {
        logger.info("User access: userId={}, action=read", id);
        return new User(id, "User Name");
    }
}
```

**Opção 2: Spring Boot + Datadog**
```yaml
# application.yml
management:
  metrics:
    export:
      datadog:
        enabled: true
        api-key: ${DD_API_KEY}
        application-key: ${DD_APP_KEY}
        step: 1m
        
logging:
  pattern:
    console: "%d{yyyy-MM-dd HH:mm:ss} - %msg%n"
  level:
    root: INFO
    com.example: DEBUG
```

**Maven Dependencies:**
```xml
<dependencies>
    <dependency>
        <groupId>net.logstash.logback</groupId>
        <artifactId>logstash-logback-encoder</artifactId>
        <version>7.4</version>
    </dependency>
    <dependency>
        <groupId>io.micrometer</groupId>
        <artifactId>micrometer-registry-datadog</artifactId>
    </dependency>
</dependencies>
```

</details>

---

### Conformidade SbD-ToE ([Cap. 12](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro))

Todos os exemplos acima garantem:

✅ **Logging estruturado** (JSON) - facilita queries e alertas  
✅ **Contexto enriquecido** - app, environment, trace IDs, user IDs  
✅ **Push automático** - logs enviados em tempo real (async)  
✅ **Resiliência** - buffering local se infraestrutura indisponível  
✅ **Segurança** - TLS, autenticação, sem dados sensíveis em logs  

**Evidência de Auditoria:**
- Logs com timestamp UTC, user/session IDs, action performed
- Correlação com traces (Datadog APM, Elasticsearch APM)
- Retention policy configurada (3+ anos para L3)

---

## 3. Análise de Vulnerabilidades (SCA + SAST)

### Princípio ([Cap. 05](/sbd-toe/sbd-manual/dependencias-sbom-sca/intro), [Cap. 07](/sbd-toe/sbd-manual/cicd-seguro/intro))
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

**Conformidade [Cap. 07](/sbd-toe/sbd-manual/cicd-seguro/intro):**
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

**Conformidade [Cap. 07](/sbd-toe/sbd-manual/cicd-seguro/intro):**
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

**Conformidade [Cap. 07](/sbd-toe/sbd-manual/cicd-seguro/intro):**
- Gratuito e open-source
- Gate de segurança integrado
- Report em múltiplos formatos

---

## 4. CI/CD com Gates de Segurança

### Princípio ([Cap. 07](/sbd-toe/sbd-manual/cicd-seguro/intro))
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

**Trilho Auditoria ([Cap. 12](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro)):**
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

**Segregação Responsabilidades ([Cap. 14](/sbd-toe/sbd-manual/governanca-contratacao/intro)):**
- SAST/SCA: Automático
- Secrets: Automático
- Approval: Manual (via UI)
- Deploy: Via RBAC

---

## 5. Plataformas Integradas (All-in-One ASPM)

### Princípio (Multi-capítulo)
Uma plataforma unificada pode cobrir múltiplas áreas de segurança com correlação de dados e dashboards centralizados.

### Quando Considerar Plataformas Integradas?

**✅ Vantagens:**
- Dashboard único para múltiplas áreas de segurança
- Correlação automática entre vulnerabilidades (SCA + SAST + IaC)
- Menor esforço de integração
- Gestão unificada de políticas
- Single source of truth para compliance

**⚠️ Desafios:**
- Vendor lock-in
- Custo tipicamente mais elevado
- Menor especialização por área vs. best-of-breed tools
- Dependência de roadmap do vendor

---

### Opção D1: Xygeni (ASPM - Application Security Posture Management)

**Cobertura SbD-ToE:**

| Capacidade Xygeni | Capítulo SbD-ToE | Descrição |
|-------------------|------------------|-----------|
| **SCA** | [Cap. 05](/sbd-toe/sbd-manual/dependencias-sbom-sca/intro) | Análise de dependências, SBOM automático, deteção de malware em packages |
| **SAST** | [Cap. 06](/sbd-toe/sbd-manual/desenvolvimento-seguro/intro) | Code security analysis, deteção de vulnerabilidades no código |
| **Secrets Security** | [Cap. 06](/sbd-toe/sbd-manual/desenvolvimento-seguro/intro) + [Cap. 07](/sbd-toe/sbd-manual/cicd-seguro/intro) | Deteção de secrets hardcoded, tokens expostos |
| **CI/CD Security** | [Cap. 07](/sbd-toe/sbd-manual/cicd-seguro/intro) | Análise de segurança de pipelines, deteção de configurações inseguras |
| **IaC Security** | [Cap. 08](/sbd-toe/sbd-manual/iac-infraestrutura/intro) | Scan de Terraform/CloudFormation/Helm para misconfigurations |
| **Build Security** | [Cap. 07](/sbd-toe/sbd-manual/cicd-seguro/intro) | Verificação de integridade de builds, supply chain attacks |
| **Anomaly Detection** | [Cap. 12](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro) | Deteção de comportamentos anómalos em runtime |
| **ASPM Dashboard** | [Cap. 14](/sbd-toe/sbd-manual/governanca-contratacao/intro) | Visão unificada de postura de segurança, KPIs consolidados |

**Exemplo de Configuração:**

```yaml
# xygeni.yml
project:
  name: "my-secure-app"
  owner: "security-team"

scans:
  sca:
    enabled: true
    fail_on: critical
    sbom:
      format: cyclonedx
      output: sbom.json
  
  sast:
    enabled: true
    languages: [java, python, javascript]
    exclude_paths: [test/*, vendor/*]
  
  secrets:
    enabled: true
    max_depth: 50  # commits
    exclude_patterns:
      - "*.test.js"
      - "mock-data/*"
  
  iac:
    enabled: true
    providers: [aws, azure, kubernetes]
    severity_threshold: medium
  
  cicd:
    enabled: true
    platforms: [github-actions, gitlab-ci]

policies:
  block_critical: true
  require_review_high: true
  auto_create_tickets: true

integrations:
  jira:
    project_key: SEC
    auto_assign: true
  
  slack:
    channel: "#security-alerts"
    notify_on: [critical, high]
```

**Evidência Auditoria:**
- Dashboard central: Histórico completo de scans
- Reports consolidados: PDF/JSON exportável para compliance
- Rastreabilidade: Commit → Scan → Issue → Resolution
- Compliance mappings: NIS2, DORA, CRA, GDPR built-in

---

### Opção D2: Snyk Enterprise (Platform Approach)

**Cobertura SbD-ToE:**

```yaml
# .snyk policy file
version: v1.25.0

# SCA - Cap. 05
ignore:
  - "SNYK-JS-LODASH-590103":
      reason: "False positive - não usamos merge profundo"
      expires: "2025-12-31"

# SAST - Cap. 06
code:
  severity-threshold: high
  
# IaC - Cap. 08
infrastructure-as-code:
  providers: [terraform, kubernetes]
  severity-threshold: medium

# Container - Cap. 09
container:
  base-image-severity: critical
  
patch:
  auto-apply: true
  exclude:
    - "**/test/**"
```

**Integração CI/CD ([Cap. 07](/sbd-toe/sbd-manual/cicd-seguro/intro)):**

```yaml
# .github/workflows/snyk-security.yml
name: Snyk Security Platform

on: [push, pull_request]

jobs:
  snyk-all-in-one:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Run Snyk to check for vulnerabilities
        uses: snyk/actions@master
        env:
          SNYK_TOKEN: ${{ secrets.SNYK_TOKEN }}
        with:
          command: test
          args: >
            --all-projects
            --severity-threshold=high
            --sarif-file-output=snyk.sarif
      
      - name: Snyk IaC
        uses: snyk/actions/iac@master
        env:
          SNYK_TOKEN: ${{ secrets.SNYK_TOKEN }}
      
      - name: Snyk Container
        uses: snyk/actions/docker@master
        env:
          SNYK_TOKEN: ${{ secrets.SNYK_TOKEN }}
        with:
          image: myapp:${{ github.sha }}
      
      - name: Snyk Code (SAST)
        uses: snyk/actions/code@master
        env:
          SNYK_TOKEN: ${{ secrets.SNYK_TOKEN }}
      
      - name: Upload to GitHub Security
        uses: github/codeql-action/upload-sarif@v2
        with:
          sarif_file: snyk.sarif
```

---

### Opção D3: Checkmarx One (Unified Platform)

**Cobertura Multi-Capítulo:**

```xml
<!-- checkmarx-config.xml -->
<CheckmarxOne>
  <!-- SAST - Cap. 06 -->
  <SAST>
    <PresetName>High Security</PresetName>
    <ExcludeFolders>test,vendor</ExcludeFolders>
    <FailOnSeverity>High</FailOnSeverity>
  </SAST>
  
  <!-- SCA - Cap. 05 -->
  <SCA>
    <RiskThreshold>7.0</RiskThreshold>
    <GenerateSBOM>true</GenerateSBOM>
    <SBOMFormat>CycloneDX</SBOMFormat>
  </SCA>
  
  <!-- IaC - Cap. 08 -->
  <KICS>
    <Platforms>Terraform,Kubernetes,Helm</Platforms>
    <Severity>MEDIUM</Severity>
  </KICS>
  
  <!-- Supply Chain - Cap. 05 + 07 -->
  <SupplyChain>
    <ScanDependencies>true</ScanDependencies>
    <MalwareDetection>true</MalwareDetection>
  </SupplyChain>
  
  <!-- API Security - Cap. 04 -->
  <APITesting>
    <Enabled>true</Enabled>
    <SwaggerPath>./docs/api.yaml</SwaggerPath>
  </APITesting>
</CheckmarxOne>
```

---

### Comparação: Plataforma Integrada vs. Best-of-Breed

| Critério | Plataforma Integrada<br/>(Xygeni, Snyk, Checkmarx) | Best-of-Breed<br/>(Ferramentas especializadas) |
|----------|--------------------------------------|----------------------------------------|
| **Integração** | ✅ Plug-and-play, dashboard único | ⚠️ Requer integração manual |
| **Correlação** | ✅ Automática entre vulnerabilidades | ⚠️ Manual ou via SIEM/SOAR |
| **Especialização** | ⚠️ Boa mas não líder em todas áreas | ✅ Líder em área específica |
| **Custo** | ⚠️ Tipicamente mais alto | ✅ Pay-per-tool, mais flexível |
| **Vendor Lock-in** | ⚠️ Alto | ✅ Baixo |
| **Compliance** | ✅ Mappings built-in (NIS2, DORA) | ⚠️ Requer trabalho manual |
| **Time-to-Value** | ✅ Rápido (semanas) | ⚠️ Médio (meses) |
| **Customização** | ⚠️ Limitada a features da plataforma | ✅ Total controlo |
| **Expertise Interna** | ✅ Menor necessária | ⚠️ Maior necessária |

---

### Recomendações por Contexto

**Use Plataforma Integrada quando:**
- ✅ Equipa pequena/média sem expertise profundo em cada área
- ✅ Necessidade de compliance rápida (NIS2, DORA, CRA)
- ✅ Orçamento permite investimento inicial mais elevado
- ✅ Preferência por simplicidade operacional
- ✅ Necessidade de dashboard executivo unificado

**Use Best-of-Breed quando:**
- ✅ Equipa grande com especialistas por área
- ✅ Requisitos muito específicos (ex: análise de linguagem rara)
- ✅ Orçamento limitado ou pay-as-you-grow
- ✅ Stack tecnológico complexo/heterogéneo
- ✅ Prioridade em evitar vendor lock-in

**Abordagem Híbrida (Recomendada para muitos casos):**
```
Plataforma Integrada (core) + Best-of-Breed (especializado)

Exemplo:
- Xygeni/Snyk: SCA, SAST, IaC (cobertura base)
+ Semgrep: SAST avançado com regras custom
+ Trivy: Container scanning especializado
+ Wiz: Cloud security posture
```

---

## Síntese

| Dimensão | Princípio (SbD-ToE) | Opção A | Opção B | Opção C | Opção D (Integrada) |
|----------|---|---|---|---|---|
| **IaC** | [Cap. 08](/sbd-toe/sbd-manual/iac-infraestrutura/intro) | Terraform | CloudFormation | Helm | Xygeni IaC / Snyk IaC |
| **Logs** | [Cap. 12](/sbd-toe/sbd-manual/monitorizacao-operacoes/intro) | ELK | Datadog | Azure Sentinel | Xygeni Anomaly Detection |
| **SCA** | [Cap. 05](/sbd-toe/sbd-manual/dependencias-sbom-sca/intro) | Snyk | WhiteSource | Dep-Check | Xygeni SCA / Snyk SCA |
| **SAST** | [Cap. 06](/sbd-toe/sbd-manual/desenvolvimento-seguro/intro) | SonarQube | Custom | TruffleHog | Xygeni SAST / Checkmarx |
| **Secrets** | [Cap. 06](/sbd-toe/sbd-manual/desenvolvimento-seguro/intro) | TruffleHog | detect-secrets | GitGuardian | Xygeni Secrets / Snyk |
| **CI/CD Security** | [Cap. 07](/sbd-toe/sbd-manual/cicd-seguro/intro) | GitHub Actions | GitLab CI | Jenkins | Xygeni CI/CD Security |
| **Container** | [Cap. 09](/sbd-toe/sbd-manual/containers-imagens/intro) | Trivy | Clair | Grype | Snyk Container / Xygeni |
| **ASPM/Dashboard** | [Cap. 14](/sbd-toe/sbd-manual/governanca-contratacao/intro) | Custom | - | - | Xygeni / Checkmarx One |

**Nenhuma combinação é "correta"** - cada organização escolhe conforme:
- Arquitetura existente e stack tecnológico
- Expertise disponível na equipa
- Orçamento e modelo de licenciamento
- Compliance local (NIS2, DORA, CRA, GDPR)
- Preferência por simplicidade vs. especialização

---

## Próximas Etapas

1. **Avaliar contexto organizacional:**
   - Qual stack tecnológico já existe?
   - Qual a maturidade da equipa de segurança?
   - Plataforma integrada ou best-of-breed?

2. **Definir estratégia:**
   - **All-in-One:** Xygeni, Snyk Enterprise, Checkmarx One
   - **Best-of-Breed:** Ferramentas especializadas por área
   - **Híbrida:** Plataforma base + ferramentas especializadas

3. **Pilotar:** 
   - Implementar uma opção num projeto piloto
   - Comparar time-to-value vs. profundidade de análise

4. **Validar:** 
   - Testar gates de segurança
   - Validar trilho de auditoria
   - Medir escalabilidade e false-positive rate

5. **Iterar:** 
   - Ajustar conforme lições aprendidas
   - Avaliar ROI (Return on Investment)
   - Considerar híbrido se necessário

6. **Documentar:** 
   - Atualizar políticas internas com stack escolhido
   - Treinar equipas nas ferramentas selecionadas
   - Estabelecer SLAs de remediação

---

**Versão:** 1.0  
**Data:** Novembro 2025  
**Feedback:** Adaptar conforme evolução tecnológica
