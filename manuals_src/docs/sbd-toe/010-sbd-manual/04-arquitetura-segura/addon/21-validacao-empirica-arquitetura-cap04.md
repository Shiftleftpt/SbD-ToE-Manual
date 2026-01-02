---
id: addon-21-validacao-empirica-arquitetura
title: "🧪 Addon-21 — Validação Empírica de Arquitetura (I4: Empirical Validation)"
description: Framework de testes técnicos para validar que decisões de arquitetura são implementadas corretamente
tags: [I4, arquitetura, validacao-empirica, testes-integracao, compliance-check, evidencia]
---

# 🧪 Addon-21 — Validação Empírica de Arquitetura (I4)

## 🎯 Objetivo

Instituir um **framework de validação técnica** para confirmar que decisões de arquitetura documentadas em ADRs são **implementadas corretamente** no código, infraestrutura e operações, usando testes de integração, compliance checks e validação de código.

Este addon implementa a **Framework I4** (Empirical Validation and Evidence) para Cap 04, complementando:
- **US-08**: Validação de decisões de arquitetura em testes
- **US-09**: Sincronização threat model ↔ implementação
- **CI/CD**: Validação automática de controlos arquitetónicos

---

## 📋 Problema e Contexto

### Problema
- ✗ ADRs são documentadas mas não validadas em produção
- ✗ Sem evidência técnica, é impossível saber se security controls estão ativos
- ✗ Código pode violar restrições arquitetónicas (ex: unauthorized service calls)
- ✗ Sem automação, validação é manual e inconsistente
- ✗ Desvios arquitectónicos descobertos tarde (produção)

### Contexto (Proporcionalidade)

| Nível | Validação | Frequência | Cobertura |
|-------|-----------|-----------|-----------|
| **L1** | Manual | Anual | ≥50% decisões críticas |
| **L2** | Automática | Contínua | 100% decisões críticas |
| **L3** | Automática + Manual | Contínua + Auditoria | 100% todas decisões |

---

## 🧩 Estrutura: 4 Categorias de Validação

### Categoria 1: Validação de Componentes (Architecture Conformance)

#### 1.1 Objetiv

Validar que componentes definidos em DFD existem e estão deployados:

```python
# tests/architecture/test_component_conformance.py

import pytest
import requests
from kubernetes import client, config

class TestComponentConformance:
    """Validar que componentes arquitetónicos existem"""
    
    @pytest.fixture
    def k8s_client(self):
        config.load_incluster_config()
        return client.CoreV1Api()
    
    def test_api_gateway_deployed(self, k8s_client):
        """ADR-001: API Gateway must be deployed"""
        pods = k8s_client.list_namespaced_pod(
            namespace="production",
            label_selector="app=kong"
        )
        assert len(pods.items) >= 3, "API GW must have ≥3 replicas"
        
        # Check readiness
        for pod in pods.items:
            status = pod.status.conditions
            ready = any(c.type == "Ready" and c.status == "True" for c in status)
            assert ready, f"Pod {pod.metadata.name} not ready"
    
    def test_database_encryption_enabled(self):
        """ADR-002: Database encryption at rest"""
        # Connect to RDS/Postgres
        response = requests.get(
            "https://aws.amazon.com/api",
            headers={"Authorization": f"Bearer {AWS_TOKEN}"}
        )
        db_config = response.json()
        
        # Check encryption setting
        assert db_config["StorageEncrypted"] == True, "Database encryption disabled"
        assert db_config["KmsKeyId"] is not None, "KMS key not configured"
    
    def test_zero_trust_network_policies(self, k8s_client):
        """ADR-003: Zero-trust networking (deny-all + allow rules)"""
        net_policies = k8s_client.list_namespaced_network_policy(
            namespace="production"
        )
        
        # Check deny-all policy exists
        deny_all = [p for p in net_policies.items if "deny-all" in p.metadata.name]
        assert len(deny_all) > 0, "Deny-all network policy not found"
        
        # Check specific allow policies
        allow_policies = [p for p in net_policies.items if p.metadata.name.startswith("allow-")]
        assert len(allow_policies) > 0, "No allow policies configured"
        
        for policy in allow_policies:
            assert policy.spec.pod_selector is not None, f"Policy {policy.metadata.name} missing pod selector"
            assert policy.spec.ingress is not None, f"Policy {policy.metadata.name} missing ingress rules"
```

#### 1.2 Checklist de Validação

```yaml
# src/architecture/validation-checklist.yaml

components:
  api_gateway:
    - deployed: true
      replicas_min: 3
      health_check: true
      tls_enabled: true
  
  database:
    - encryption_at_rest: true
      encryption_in_transit: true
      backup_enabled: true
      audit_logging: true
  
  service_mesh:
    - deployed: true
      mtls_enabled: true
      policies_count: 10
```

---

### Categoria 2: Validação de Controlo de Acesso

#### 2.1 RBAC Validation

```python
# tests/architecture/test_rbac_validation.py

def test_api_gateway_rbac():
    """Validar RBAC policies em API Gateway"""
    # Obter policies da Kong API
    response = requests.get(
        "http://kong-admin:8001/rbac/users",
        headers={"Authorization": "Bearer kong-token"}
    )
    rbac_users = response.json()
    
    # Validar que usuarios-admin têm role=admin
    admin_users = [u for u in rbac_users if u['name'].startswith('admin-')]
    for user in admin_users:
        assert user['enabled'] == True, f"Admin user {user['name']} disabled"
        # Can't check role directly, so validate via permission tests
    
    # Validar que developers não têm acesso admin
    dev_users = [u for u in rbac_users if u['name'].startswith('dev-')]
    for user in dev_users:
        # Try to access admin endpoints
        response = requests.get(
            "http://kong-admin:8001/users",
            headers={"Authorization": f"Bearer {user['token']}"}
        )
        # Should return 403 Forbidden
        assert response.status_code == 403, f"Dev user {user['name']} has unauthorized access"

def test_database_rbac():
    """Validar RBAC em database"""
    # Connect as app user
    import psycopg2
    conn = psycopg2.connect(
        dbname="myapp",
        user="app_user",
        password=os.getenv("DB_PASS"),
        host="prod-db.rds.amazonaws.com"
    )
    cursor = conn.cursor()
    
    # App user should NOT be able to drop tables
    try:
        cursor.execute("DROP TABLE users")
        assert False, "App user should not have DROP permission"
    except psycopg2.Error as e:
        assert "permission denied" in str(e).lower(), f"Unexpected error: {e}"
    
    # App user should be able to SELECT
    cursor.execute("SELECT COUNT(*) FROM users")
    result = cursor.fetchone()
    assert result[0] >= 0, "App user can't SELECT"
```

#### 2.2 Service-to-Service Authentication

```python
# tests/architecture/test_service_mesh.py

def test_mtls_between_services():
    """ADR-004: Service-to-service must use mTLS"""
    # Get service mesh (Istio) policies
    response = requests.get(
        "http://istio-pilot:15010/debug/config_dump",
        headers={}
    )
    config = response.json()
    
    # Check that all services have PeerAuthentication policies
    peer_auth_policies = [c for c in config if c['@type'] == 'type.googleapis.com/istio.security.v1beta1.PeerAuthentication']
    assert len(peer_auth_policies) > 0, "No PeerAuthentication policies found"
    
    for policy in peer_auth_policies:
        mtls = policy['spec'].get('mtls', {})
        mode = mtls.get('mode', '')
        assert mode in ['STRICT', 'PERMISSIVE'], f"mTLS mode not configured correctly: {mode}"

def test_service_authorization_policies():
    """ADR-004: Authorization policies between services"""
    # Get authorization policies
    response = requests.get(
        "http://istio-pilot:15010/debug/config_dump",
        headers={}
    )
    config = response.json()
    
    auth_policies = [c for c in config if c['@type'] == 'type.googleapis.com/istio.security.v1beta1.AuthorizationPolicy']
    
    # Should have explicit deny-all + allow rules
    deny_all = [p for p in auth_policies if p['spec'].get('rules') == []]
    assert len(deny_all) > 0, "No deny-all authorization policy"
    
    allow_policies = [p for p in auth_policies if p['spec'].get('rules') and len(p['spec']['rules']) > 0]
    assert len(allow_policies) > 0, "No allow authorization policies"
```

---

### Categoria 3: Validação de Dados e Segredos

#### 3.1 Encryption Validation

```python
# tests/architecture/test_encryption.py

def test_database_encryption_at_rest():
    """Validar encriptação de dados em repouso"""
    import boto3
    rds = boto3.client('rds')
    
    # Get DB instance info
    response = rds.describe_db_instances(DBInstanceIdentifier='prod-db')
    db_instance = response['DBInstances'][0]
    
    # Check encryption
    assert db_instance['StorageEncrypted'] == True, "Database not encrypted at rest"
    assert db_instance['KmsKeyId'] is not None, "KMS key not configured"
    
    # Check key rotation
    kms = boto3.client('kms')
    key_metadata = kms.describe_key(KeyId=db_instance['KmsKeyId'])
    assert key_metadata['KeyMetadata']['KeyState'] == 'Enabled', "KMS key disabled"

def test_secrets_not_in_code():
    """Validar que secrets não estão hardcoded"""
    import re
    import os
    
    # Scan source code for secret patterns
    secret_patterns = [
        r'password\s*=\s*["\']([^"\']+)["\']',
        r'api[_-]?key\s*=\s*["\']([^"\']+)["\']',
        r'secret\s*=\s*["\']([^"\']+)["\']',
        r'token\s*=\s*["\']([^"\']+)["\']',
    ]
    
    for root, dirs, files in os.walk('src'):
        for file in files:
            if file.endswith('.py') or file.endswith('.js'):
                with open(os.path.join(root, file)) as f:
                    content = f.read()
                    for pattern in secret_patterns:
                        matches = re.findall(pattern, content, re.IGNORECASE)
                        # Exclude test data
                        if matches and 'test' not in file and 'mock' not in file:
                            assert False, f"Potential secret in {file}: {pattern}"

def test_transit_encryption():
    """Validar encriptação em trânsito (TLS 1.2+)"""
    import ssl
    import socket
    
    def check_tls(hostname, port):
        context = ssl.create_default_context()
        with socket.create_connection((hostname, port)) as sock:
            with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                version = ssock.version
                cipher = ssock.cipher()
                
                # TLS 1.2+ required
                assert version in ['TLSv1.2', 'TLSv1.3'], f"TLS version too old: {version}"
                
                # Strong ciphers required
                strong_ciphers = ['ECDHE', 'CHACHA20', 'AES-256']
                assert any(c in cipher[0] for c in strong_ciphers), f"Weak cipher: {cipher[0]}"
    
    # Check APIs
    check_tls('api.myapp.com', 443)
    check_tls('db.myapp.internal', 5432)
```

#### 3.2 Secret Management Validation

```python
# tests/architecture/test_secrets_management.py

def test_secrets_in_vault():
    """Validar que secrets estão em Vault, não em código"""
    import hvac
    
    client = hvac.Client(url=os.getenv('VAULT_ADDR'), token=os.getenv('VAULT_TOKEN'))
    
    # Check database secrets
    secret = client.secrets.kv.read_secret_version(path='database/prod')
    assert 'username' in secret['data']['data'], "DB username not in Vault"
    assert 'password' in secret['data']['data'], "DB password not in Vault"
    
    # Check API keys
    secret = client.secrets.kv.read_secret_version(path='api-keys/stripe')
    assert 'sk_live' in secret['data']['data'], "Stripe key not in Vault"

def test_secrets_rotation():
    """Validar que secrets são rotacionados"""
    # For database passwords, check if rotation is enabled
    import boto3
    secrets = boto3.client('secretsmanager')
    
    response = secrets.describe_secret(SecretId='prod/database/password')
    assert 'RotationRules' in response, "Rotation not configured"
    assert response['RotationRules']['AutomaticallyAfterDays'] <= 30, "Rotation not frequent enough"
```

---

### Categoria 4: Validação de Operações e Logging

#### 4.1 Audit Logging Validation

```python
# tests/architecture/test_audit_logging.py

def test_api_gateway_logging():
    """Validar que API Gateway registra todas as operações"""
    import boto3
    
    # Check CloudWatch logs
    logs = boto3.client('logs')
    
    # Check if Kong logs are being written
    response = logs.describe_log_streams(
        logGroupName='/aws/kong/prod'
    )
    
    assert len(response['logStreams']) > 0, "No Kong log streams found"
    
    # Check if recent logs exist
    for stream in response['logStreams']:
        assert stream['lastEventTimestamp'] > (time.time() - 3600) * 1000, f"Log stream {stream['logStreamName']} is stale"

def test_database_audit_logging():
    """Validar que database registra operações administrativas"""
    import psycopg2
    
    conn = psycopg2.connect(
        dbname="myapp",
        user="audit_user",
        password=os.getenv("DB_AUDIT_PASS"),
        host="prod-db.rds.amazonaws.com"
    )
    cursor = conn.cursor()
    
    # Check if pgaudit is enabled
    cursor.execute("SHOW pgaudit.log")
    result = cursor.fetchone()
    
    assert result[0] in ['ALL', 'DDL,DML,ROLE'], f"pgaudit not properly configured: {result[0]}"
    
    # Check recent audit logs
    cursor.execute("""
        SELECT COUNT(*) FROM pg_stat_statements
        WHERE query LIKE '%DROP%' OR query LIKE '%ALTER%'
    """)
    result = cursor.fetchone()
    assert result[0] > 0, "Audit logging may not be working"

def test_access_control_logging():
    """Validar que todos os acessos são registados"""
    # Check that auth failures are logged
    import subprocess
    
    result = subprocess.run(
        ["grep", "-c", "authentication failed", "/var/log/auth.log"],
        capture_output=True
    )
    
    # Should have some failed auth attempts (normal)
    assert result.returncode == 0, "Auth logging not enabled"
```

#### 4.2 Monitoring and Alerting Validation

```python
# tests/architecture/test_monitoring.py

def test_critical_alerts_configured():
    """Validar que alertas críticos estão configurados"""
    import boto3
    
    cloudwatch = boto3.client('cloudwatch')
    
    # Check for critical alerts
    critical_alerts = [
        'high-latency',
        'high-error-rate',
        'database-down',
        'unauthorized-access',
        'certificate-expiring',
    ]
    
    response = cloudwatch.describe_alarms()
    configured_alerts = [a['AlarmName'] for a in response['MetricAlarms']]
    
    for alert in critical_alerts:
        assert any(alert in ca for ca in configured_alerts), f"Critical alert not configured: {alert}"

def test_security_monitoring():
    """Validar que segurança é monitorizada"""
    # Check that security metrics are being collected
    import boto3
    
    cloudwatch = boto3.client('cloudwatch')
    
    # Check for security-related metrics
    response = cloudwatch.list_metrics(
        Namespace='SecurityMetrics'
    )
    
    security_metrics = {m['MetricName'] for m in response['Metrics']}
    
    expected_metrics = {
        'failed-auth-attempts',
        'unauthorized-api-calls',
        'privilege-escalations',
        'data-access-anomalies',
    }
    
    assert expected_metrics.issubset(security_metrics), f"Missing security metrics: {expected_metrics - security_metrics}"
```

---

## Integração com CI/CD

### Automação de Testes de Conformidade

```yaml
# .github/workflows/architecture-validation.yml

name: Architecture Validation

on:
  pull_request:
    paths:
      - 'src/architecture/adr/**'
      - 'infra/kubernetes/**'
      - 'tests/architecture/**'
  push:
    branches:
      - main
  schedule:
    # Daily validation in production
    - cron: '0 9 * * *'

jobs:
  component-conformance:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Test component deployment
        run: |
          python -m pytest tests/architecture/test_component_conformance.py -v
      
      - name: Report component status
        if: failure()
        run: |
          echo "::error::Architecture components not conformant"
          exit 1
  
  rbac-validation:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Validate RBAC policies
        run: |
          python -m pytest tests/architecture/test_rbac_validation.py -v
  
  encryption-validation:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Validate encryption
        run: |
          python -m pytest tests/architecture/test_encryption.py -v
  
  audit-logging-validation:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Validate audit logs
        run: |
          python -m pytest tests/architecture/test_audit_logging.py -v
  
  generate-report:
    runs-on: ubuntu-latest
    if: always()
    needs: [component-conformance, rbac-validation, encryption-validation, audit-logging-validation]
    steps:
      - name: Generate architecture validation report
        run: |
          python scripts/generate_architecture_report.py > architecture-validation-report.txt
      
      - name: Upload report
        uses: actions/upload-artifact@v3
        with:
          name: architecture-validation-report
          path: architecture-validation-report.txt
```

---

## Métricas de Sucesso (I4)

### Indicadores

| Métrica | Meta | Como Medir |
|---------|------|-----------|
| % ADRs validadas automaticamente | 100% (L2/L3) | Count test cases / ADRs |
| Coverage de componentes | 100% | Checklist items verified |
| Coverage de RBAC | 100% | RBAC policies tested |
| Coverage de encriptação | 100% | Encryption validations pass |
| Coverage de logging | 100% | Audit logs verified |
| Detecção de desvios | <1 semana | Tempo entre desvio e detecção |

---

## 🎯 Checklist de Implementação (I4 - Cap 04)

- [ ] Testes de conformidade de componentes implementados
- [ ] Validação de RBAC configurada
- [ ] Testes de encriptação implementados
- [ ] Validação de logging configurada
- [ ] CI/CD pipeline integrado
- [ ] Primeiras 10 ADRs validadas empiricamente
- [ ] Relatório automático gerado
- [ ] Dashboard de conformidade criado
- [ ] Feedback da equipa de DevOps incorporado

---

**Versão**: 1.0  
**Última Atualização**: Jan 2025  
**Mantido por**: DevOps + QA Team  
