---
id: addon-24-validacao-empirica-dependencias
title: "🧪 Addon-24 — Validação Empírica de Dependências (I4: Empirical Validation)"
description: Framework de testes técnicos para validar SBOM, SCA findings e impacto de atualizações
tags: [I4, dependencias, sbom, sca, validacao-empirica, testes, compliance-check]
---

# 🧪 Addon-24 — Validação Empírica de Dependências (I4)

## 🎯 Objetivo

Instituir um **framework de validação técnica** para confirmar que SBOM está correto, vulnerabilidades detectadas por SCA são reais, e atualizações de dependências não introduzem regressions ou breaking changes.

Este addon implementa a **Framework I4** (Empirical Validation and Evidence) para Cap 05, complementando:
- **SBOM Validation**: Verifique se SBOM está completo e preciso
- **SCA Validation**: Confirme se findings são reais (não falsos positivos)
- **Update Validation**: Teste impacto de atualizações em testes e produção
- **Compliance Check**: Validação automática em CI/CD

---

## 📋 Problema e Contexto

### Problema
- ✗ SBOM é gerado mas nunca validado contra código real
- ✗ SCA ferramentas geram falsos positivos/negativos
- ✗ Atualizações são aplicadas sem testar impacto
- ✗ Sem evidência técnica, é impossível priorizar remediation
- ✗ Conformidade de supply chain não é verificada

### Contexto (Proporcionalidade)

| Nível | SBOM Validation | SCA Validation | Update Testing |
|-------|-----------------|---|---|
| **L1** | Manual | SAST só | Teste básico |
| **L2** | Automática | SAST + manual | Teste integração |
| **L3** | Automática + Auditoria | SAST + DAST + manual | Teste integração + staging |

---

## 🧩 Estrutura: 4 Categorias de Validação

### Categoria 1: Validação de SBOM Completude

#### 1.1 SBOM Generation Validation

```python
# tests/sbom/test_sbom_completeness.py

import subprocess
import json
import os
from cyclonedx import BOM, Component, ComponentType
from cyclonedx.output.json import Json as JsonOutput

class TestSBOMCompleteness:
    """Validar que SBOM está completo e preciso"""
    
    def test_sbom_generated_on_build(self):
        """SBOM deve ser gerado em cada build"""
        # Trigger build
        result = subprocess.run([
            "npm", "run", "build:sbom"
        ], capture_output=True, text=True, cwd=".")
        
        assert result.returncode == 0, f"Build failed: {result.stderr}"
        
        # Check SBOM exists
        sbom_path = "dist/sbom.json"
        assert os.path.exists(sbom_path), "SBOM not generated"
        
        # Parse SBOM
        with open(sbom_path) as f:
            sbom_data = json.load(f)
        
        assert sbom_data["specVersion"] in ["1.3", "1.4"], "Unsupported SBOM version"
        assert sbom_data["version"] >= 1, "SBOM version number missing"
        assert sbom_data["components"] is not None, "No components in SBOM"
    
    def test_sbom_includes_all_dependencies(self):
        """SBOM deve incluir todas as dependências diretas e transitivas"""
        # Parse package.json
        with open("package.json") as f:
            package_data = json.load(f)
        
        direct_deps = set(package_data.get("dependencies", {}).keys())
        dev_deps = set(package_data.get("devDependencies", {}).keys())
        all_declared_deps = direct_deps | dev_deps
        
        # Parse SBOM
        with open("dist/sbom.json") as f:
            sbom_data = json.load(f)
        
        sbom_components = {c["name"] for c in sbom_data.get("components", [])}
        
        # Check all declared deps are in SBOM
        missing_deps = all_declared_deps - sbom_components
        assert not missing_deps, f"Dependencies missing from SBOM: {missing_deps}"
        
        # Check for extra/unexpected deps
        extra_deps = sbom_components - all_declared_deps
        # Some transitive deps are OK, but should not have unknown sources
        for dep in extra_deps:
            # Verify transitive dep is actually a transitive dependency
            result = subprocess.run(
                ["npm", "list", dep],
                capture_output=True,
                text=True
            )
            assert result.returncode == 0, f"Unexpected dependency in SBOM: {dep}"
    
    def test_sbom_includes_licenses(self):
        """SBOM deve incluir informações de licença"""
        with open("dist/sbom.json") as f:
            sbom_data = json.load(f)
        
        for component in sbom_data.get("components", []):
            # Each component should have license info
            assert "licenses" in component or "licenses" in component.get("externalReferences", []), \
                f"Component {component['name']} missing license info"
    
    def test_sbom_includes_vulnerability_refs(self):
        """SBOM deve incluir referências de vulnerabilidades conhecidas"""
        with open("dist/sbom.json") as f:
            sbom_data = json.load(f)
        
        # Components with known vulnerabilities should reference them
        # (This is populated by SCA tool integration)
        for component in sbom_data.get("components", []):
            # Should have external references for CVEs if known
            ext_refs = component.get("externalReferences", [])
            # At minimum, should have a reference type for vulnerability tracking
            
            # Check for vulnerability reference
            has_vuln_ref = any(
                ref.get("type") == "vulnerability" 
                for ref in ext_refs
            )
            # OK if no vulns, but if known vulns exist, should be documented
    
    def test_sbom_timestamps_present(self):
        """SBOM deve incluir timestamp de geração"""
        with open("dist/sbom.json") as f:
            sbom_data = json.load(f)
        
        assert "metadata" in sbom_data, "SBOM missing metadata"
        assert "timestamp" in sbom_data["metadata"], "SBOM missing generation timestamp"
        
        # Timestamp should be recent (within last hour)
        from datetime import datetime, timedelta
        sbom_time = datetime.fromisoformat(sbom_data["metadata"]["timestamp"].replace('Z', '+00:00'))
        now = datetime.now(sbom_time.tzinfo)
        age = now - sbom_time
        
        assert age < timedelta(hours=1), f"SBOM is stale ({age} old)"
```

#### 1.2 SBOM Signature Validation

```python
# tests/sbom/test_sbom_integrity.py

def test_sbom_signed_and_verified():
    """SBOM deve ser assinado para garantir integridade"""
    import subprocess
    import hashlib
    
    # Generate signature (if not already present)
    result = subprocess.run([
        "cosign", "sign-blob",
        "--key", "sbom.key",
        "dist/sbom.json",
        "--output-signature", "dist/sbom.json.sig"
    ], capture_output=True, text=True)
    
    assert result.returncode == 0, f"Failed to sign SBOM: {result.stderr}"
    
    # Verify signature
    result = subprocess.run([
        "cosign", "verify-blob",
        "--key", "sbom.pub",
        "--signature", "dist/sbom.json.sig",
        "dist/sbom.json"
    ], capture_output=True, text=True)
    
    assert result.returncode == 0, "SBOM signature verification failed"

def test_sbom_not_tampered():
    """Detectar se SBOM foi modificado"""
    import hashlib
    
    # Read SBOM
    with open("dist/sbom.json", "rb") as f:
        sbom_content = f.read()
    
    # Calculate hash
    sbom_hash = hashlib.sha256(sbom_content).hexdigest()
    
    # Compare with hash stored in metadata (if present)
    import json
    with open("dist/sbom.json") as f:
        sbom_data = json.load(f)
    
    stored_hash = sbom_data.get("metadata", {}).get("contentHash", {}).get("value")
    if stored_hash:
        assert sbom_hash == stored_hash, "SBOM hash mismatch - may be tampered"
```

---

### Categoria 2: Validação de SCA Findings

#### 2.1 False Positive/Negative Analysis

```python
# tests/sca/test_sca_validation.py

def test_sca_findings_are_real():
    """Validar que SCA findings são vulnerabilidades reais, não FP"""
    import subprocess
    import json
    
    # Run SCA (e.g., npm audit, safety, snyk)
    result = subprocess.run([
        "npm", "audit", "--json"
    ], capture_output=True, text=True)
    
    sca_report = json.loads(result.stdout)
    
    # Iterate through findings
    for finding in sca_report.get("vulnerabilities", {}).items():
        vuln_id, details = finding
        
        # Check severity
        severity = details.get("severity")
        cvss_score = details.get("cvss_score", 0)
        
        # For CRITICAL findings, always validate
        if severity == "critical" or cvss_score >= 9.0:
            is_real = validate_vulnerability_empirically(
                library=details.get("name"),
                version=details.get("version"),
                vuln_id=vuln_id,
                cwe=details.get("cwe")
            )
            
            if not is_real:
                print(f"⚠️ FALSE POSITIVE: {vuln_id}")
                # Could suppress in SCA tool or document exception

def validate_vulnerability_empirically(library, version, vuln_id, cwe):
    """
    Validar se vulnerabilidade é exploitável neste código
    
    Estratégia:
    1. Procurar se função vulnerável é chamada
    2. Se não é chamada, é false positive (FP)
    3. Se é chamada, validar se é exploitável
    """
    import subprocess
    
    # 1. Find if vulnerable function is used in code
    vuln_function = get_vulnerable_function(vuln_id)
    
    result = subprocess.run([
        "grep", "-r", vuln_function, "src/",
        "--include=*.js", "--include=*.ts"
    ], capture_output=True, text=True)
    
    if result.returncode != 0:
        # Function not used → false positive
        return False
    
    # 2. If function is used, check if with untrusted input
    usages = parse_usages(result.stdout)
    for usage in usages:
        if is_untrusted_input(usage):
            # Vulnerable function called with untrusted data
            return True
    
    # 3. All usages are with trusted input → false positive
    return False

def is_untrusted_input(usage_context):
    """Verificar se entrada é untrusted (user input, network, etc.)"""
    untrusted_sources = [
        "req.body",
        "req.query",
        "req.params",
        "process.argv",
        "fetch(",
        "axios(",
        "socket.on("
    ]
    
    return any(source in usage_context for source in untrusted_sources)
```

#### 2.2 CVE Correlation Validation

```python
# tests/sca/test_cve_correlation.py

def test_sca_findings_correlated_to_cves():
    """Validar que SCA findings estão correlacionados a CVEs conhecidas"""
    import json
    import requests
    
    # Get SCA report
    with open("dist/sca-report.json") as f:
        sca_report = json.load(f)
    
    # For each vulnerability, verify it exists in NVD/CVE databases
    for vuln in sca_report.get("vulnerabilities", []):
        cve_id = vuln.get("cveId")
        if cve_id:
            # Query NVD API
            response = requests.get(
                f"https://services.nvd.nist.gov/rest/json/cves/2.0",
                params={"keywordSearch": cve_id},
                headers={"apiKey": os.getenv("NVD_API_KEY")}
            )
            
            assert response.status_code == 200, f"NVD lookup failed for {cve_id}"
            nvd_data = response.json()
            
            # Verify CVE exists and details match
            assert len(nvd_data.get("vulnerabilities", [])) > 0, \
                f"CVE {cve_id} not found in NVD (may be invalid)"
            
            nvd_vuln = nvd_data["vulnerabilities"][0]["cve"]
            
            # Validate severity matches
            nvd_severity = nvd_vuln["metrics"]["cvssMetricV31"]["cvssData"]["baseSeverity"]
            sca_severity = vuln.get("severity")
            
            assert severity_matches(nvd_severity, sca_severity), \
                f"Severity mismatch for {cve_id}: NVD={nvd_severity}, SCA={sca_severity}"

def severity_matches(nvd_severity, sca_severity):
    """Map severity levels"""
    severity_map = {
        "CRITICAL": ["CRITICAL", "CRITICAL/9.9"],
        "HIGH": ["HIGH", "CRITICAL", "HIGH/8.9"],
        "MEDIUM": ["MEDIUM", "HIGH", "MEDIUM/6.9"],
        "LOW": ["LOW", "MEDIUM", "LOW/3.9"],
    }
    
    return sca_severity in severity_map.get(nvd_severity, [])
```

---

### Categoria 3: Validação de Atualizações

#### 3.1 Update Impact Analysis

```python
# tests/updates/test_update_impact.py

def test_dependency_update_breaks_nothing():
    """Validar que atualização de dependência não quebra código"""
    import subprocess
    
    # List pending updates
    result = subprocess.run([
        "npm", "outdated", "--json"
    ], capture_output=True, text=True)
    
    pending_updates = json.loads(result.stdout)
    
    for package, details in pending_updates.items():
        current_version = details["current"]
        latest_version = details["latest"]
        
        # Determine if update is breaking
        is_breaking = is_breaking_change(
            package=package,
            from_version=current_version,
            to_version=latest_version
        )
        
        if is_breaking:
            print(f"Breaking change: {package} {current_version} → {latest_version}")
            # Require human review
            continue
        
        # If not breaking, can auto-update
        print(f"Safe to auto-update: {package} {current_version} → {latest_version}")
        
        # Test with new version
        subprocess.run([
            "npm", "install", f"{package}@{latest_version}"
        ])
        
        # Run tests
        result = subprocess.run([
            "npm", "test"
        ], capture_output=True, text=True)
        
        assert result.returncode == 0, \
            f"Tests failed with {package}@{latest_version}"

def is_breaking_change(package, from_version, to_version):
    """Detectar se atualização é breaking"""
    from packaging import version
    
    current = version.parse(from_version)
    latest = version.parse(to_version)
    
    # Breaking change if major version changes
    if current.major != latest.major:
        return True
    
    # Check changelog/release notes
    changelog = fetch_changelog(package, from_version, to_version)
    if "BREAKING" in changelog.upper() or "BREAKING CHANGE" in changelog.upper():
        return True
    
    return False

def fetch_changelog(package, from_version, to_version):
    """Fetch changelog from npm/GitHub"""
    # Implementation would fetch from package repo
    pass
```

#### 3.2 Regression Testing

```python
# tests/updates/test_regression_suite.py

def test_security_regression_with_new_dependency():
    """Executar security tests com nova versão de dependência"""
    import subprocess
    
    # Run security-specific tests
    test_suites = [
        "tests/security/authentication.test.js",
        "tests/security/authorization.test.js",
        "tests/security/input-validation.test.js",
        "tests/security/cryptography.test.js",
    ]
    
    for suite in test_suites:
        result = subprocess.run([
            "npm", "test", "--", suite
        ], capture_output=True, text=True)
        
        assert result.returncode == 0, \
            f"Security regression in {suite}: {result.stderr}"

def test_dependency_licensing_unchanged():
    """Validar que atualização não muda licença"""
    import subprocess
    import json
    
    # Get current SBOM
    with open("dist/sbom.json") as f:
        current_sbom = json.load(f)
    
    current_licenses = {
        c["name"]: c.get("licenses", [])
        for c in current_sbom.get("components", [])
    }
    
    # After update, regenerate SBOM
    subprocess.run(["npm", "install"], check=True)
    subprocess.run(["npm", "run", "build:sbom"], check=True)
    
    with open("dist/sbom.json") as f:
        updated_sbom = json.load(f)
    
    updated_licenses = {
        c["name"]: c.get("licenses", [])
        for c in updated_sbom.get("components", [])
    }
    
    # Compare licenses
    for package, current_lic in current_licenses.items():
        if package in updated_licenses:
            updated_lic = updated_licenses[package]
            if current_lic != updated_lic:
                print(f"License changed for {package}: {current_lic} → {updated_lic}")
                # May need approval if license becomes incompatible
```

---

### Categoria 4: Compliance Checks

#### 4.1 Supply Chain Integrity

```python
# tests/compliance/test_supply_chain.py

def test_no_shadow_dependencies():
    """Validar que não há dependências copiadas manualmente"""
    import os
    import subprocess
    
    # List declared dependencies
    result = subprocess.run([
        "npm", "list", "--depth=0", "--json"
    ], capture_output=True, text=True)
    
    declared_deps = set(json.loads(result.stdout).get("dependencies", {}).keys())
    
    # Scan node_modules for unexpected files
    node_modules = set(os.listdir("node_modules"))
    
    # Check for files that shouldn't be there
    suspicious = []
    for item in node_modules:
        if item.startswith("."):
            continue
        
        if item not in declared_deps and item not in ["@types", "@babel", ".bin"]:
            suspicious.append(item)
    
    assert not suspicious, f"Unexpected items in node_modules (possible shadow deps): {suspicious}"

def test_all_dependencies_in_lockfile():
    """Validar que todas as dependências estão no lockfile"""
    import json
    
    # Parse package.json
    with open("package.json") as f:
        package = json.load(f)
    
    declared = set(package.get("dependencies", {}).keys()) | \
               set(package.get("devDependencies", {}).keys())
    
    # Parse lock file
    with open("package-lock.json") as f:
        lockfile = json.load(f)
    
    locked = set(lockfile.get("packages", {}).keys())
    
    # All declared should be in lockfile
    missing = declared - locked
    assert not missing, f"Dependencies not in lockfile: {missing}"

def test_dependency_integrity_hashes():
    """Validar que packages têm checksums"""
    import json
    
    with open("package-lock.json") as f:
        lockfile = json.load(f)
    
    for package_name, package_info in lockfile.get("packages", {}).items():
        if package_name.startswith("node_modules/"):
            # Should have integrity hash
            assert "integrity" in package_info, \
                f"Package {package_name} missing integrity hash"
```

---

## Integração com CI/CD

```yaml
# .github/workflows/dependency-validation.yml

name: Dependency Validation

on:
  pull_request:
    paths:
      - 'package.json'
      - 'package-lock.json'
      - 'requirements.txt'
  push:
    branches:
      - main

jobs:
  sbom-validation:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Generate SBOM
        run: npm run build:sbom
      
      - name: Validate SBOM completeness
        run: python -m pytest tests/sbom/test_sbom_completeness.py -v
      
      - name: Validate SBOM integrity
        run: python -m pytest tests/sbom/test_sbom_integrity.py -v
  
  sca-validation:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Run SCA
        run: npm audit --json > dist/sca-report.json || true
      
      - name: Validate SCA findings
        run: python -m pytest tests/sca/test_sca_validation.py -v
      
      - name: Correlate to CVEs
        run: python -m pytest tests/sca/test_cve_correlation.py -v
  
  update-validation:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Test pending updates
        run: python -m pytest tests/updates/test_update_impact.py -v
      
      - name: Run regression tests
        run: python -m pytest tests/updates/test_regression_suite.py -v
  
  compliance-check:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Check supply chain integrity
        run: python -m pytest tests/compliance/test_supply_chain.py -v
      
      - name: Generate compliance report
        run: python scripts/generate_dependency_compliance_report.py
      
      - name: Upload report
        uses: actions/upload-artifact@v3
        with:
          name: dependency-validation-report
          path: dependency-validation-report.txt
```

---

## Métricas de Sucesso (I4)

### Indicadores

| Métrica | Meta | Como Medir |
|---------|------|-----------|
| SBOM completude | 100% | Coverage analysis |
| % findings validados | 100% CRÍTICA, ≥70% ALTA | Validation report |
| FP rate (SCA) | <10% | Count FP / total findings |
| Tempo validação updates | <2 dias | Timestamp test → merge |
| Supply chain integrity checks | 100% | Compliance report pass rate |

---

## 🎯 Checklist de Implementação (I4 - Cap 05)

- [ ] SBOM generation e validação implementadas
- [ ] SCA findings validation configurada
- [ ] FP/FN analysis framework criado
- [ ] Update impact testing implementado
- [ ] Regression test suite criado
- [ ] Supply chain compliance checks ativados
- [ ] CI/CD pipeline integrado
- [ ] Dashboard de validação criado
- [ ] Relatório automático gerado

---

**Versão**: 1.0  
**Última Atualização**: Jan 2025  
**Mantido por**: QA + DevOps Team  
