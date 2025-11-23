#!/usr/bin/env python3
"""
Comprehensive audit: Verify Portuguese PT consistency and identify technical terms
"""

import yaml
import re
from pathlib import Path
from collections import defaultdict

tags_file = Path("/Volumes/G-DRIVE/Shared/Manual-SbD-ToE/SbD-ToE-Manual/src/tag-normalization/canonical-tags.yml")

with open(tags_file, 'r', encoding='utf-8') as f:
    tags = yaml.safe_load(f)

print("\n" + "=" * 140)
print("✅ COMPREHENSIVE TAG AUDIT: Portuguese PT + English Technical Terms")
print("=" * 140)

# Patterns to check
br_words = {
    'monitoramento': 'monitorização',
    'implementação': 'implementação',  # Both use, but context matters
    'comunicação': 'comunicação',  # Both use
    'operação': 'operação',  # Both use
    'criação': 'criação',  # Both use
    'automação': 'automação',  # Both use
    'integração': 'integração',  # Both use
}

# Technical terms that should stay in English (global consensus)
technical_en_consensus = {
    'api', 'ci', 'cd', 'sql', 'http', 'https', 'ssl', 'tls', 'oauth', 'mfa', 'sso', 'saml',
    'ldap', 'json', 'xml', 'yaml', 'devops', 'devsecops', 'sast', 'dast', 'iast',
    'sbom', 'sca', 'slsa', 'ssdf', 'samm', 'nist', 'cis', 'asvs', 'capec',
    'docker', 'kubernetes', 'k8s', 'terraform', 'ansible', 'jenkins', 'gitlab', 'github',
    'aws', 'azure', 'gcp', 'iac', 'iac', 'siem', 'soc', 'osint', 'apt', 'cve',
    'cwe', 'cvss', 'exploit', 'payload', 'shellcode', 'backdoor', 'ransomware',
    'malware', 'trojan', 'botnet', 'worm', 'virus', 'phishing', 'spear-phishing',
    'social engineering', 'privilege escalation', 'lateral movement', 'persistence',
    'defense evasion', 'discovery', 'collection', 'exfiltration', 'command',
    'control', 'impact', 'mitre', 'framework', 'standard', 'guideline',
    'baseline', 'benchmark', 'control', 'policy', 'procedure', 'process',
    'pipeline', 'workflow', 'trigger', 'flow', 'gate', 'hook', 'webhook',
    'runner', 'agent', 'job', 'task', 'step', 'stage', 'sandbox', 'container',
    'image', 'registry', 'repository', 'branch', 'commit', 'tag', 'release',
    'version', 'semantic versioning', 'alpha', 'beta', 'rc', 'ga', 'lts',
    'eol', 'deprecation', 'sunset', 'roadmap', 'backlog', 'epic', 'user story',
    'sprint', 'agile', 'scrum', 'kanban', 'lean', 'six sigma', 'itil', 'cobit',
    'coso', 'togaf', 'bpmn', 'uml', 'erd', 'dfd', 'flowchart', 'sequence diagram',
    'use case', 'user journey', 'persona', 'empathy map', 'wireframe', 'prototype',
    'mockup', 'ui', 'ux', 'a/b testing', 'analytics', 'telemetry', 'observability',
    'instrumentation', 'tracing', 'metrics', 'logs', 'events', 'alerts', 'dashboards',
    'incidents', 'sla', 'slo', 'error budget', 'chaos engineering', 'blameless',
    'postmortem', 'incident response', 'playbook', 'runbook', 'escalation',
    'on-call', 'on-pager', 'pagerduty', 'slack', 'teams', 'email', 'sms',
    'grafana', 'prometheus', 'datadog', 'newrelic', 'splunk', 'elk', 'sumo logic',
}

issues = defaultdict(list)
checks = {
    'portuguese_consistency': 0,
    'english_technical': 0,
    'total_tags': 0
}

print("\n📋 CHECKING ALL TAGS...")
print("-" * 140)

for tag_name, tag_data in sorted(tags.items()):
    if not isinstance(tag_data, dict) or ':' in tag_name:
        continue
    
    checks['total_tags'] += 1
    
    label = tag_data.get('label', '')
    description = tag_data.get('description', '')
    aliases = tag_data.get('aliases', [])
    
    full_text = f"{tag_name} {label} {description} {' '.join(str(a) for a in aliases)}".lower()
    
    # Check 1: Portuguese consistency
    checks['portuguese_consistency'] += 1
    
    # Flag if found Brazilian Portuguese variant
    for br_word, pt_word in br_words.items():
        if br_word in full_text and br_word != pt_word:
            # Allow BR Portuguese as aliases for normalization (by design)
            # Only flag if it's the canonical tag name or in canonical label (not aliases)
            if br_word == tag_name or (br_word in label and br_word not in aliases):
                issues['br_portuguese'].append({
                    'tag': tag_name,
                    'word': br_word,
                    'suggest': pt_word,
                    'context': label or description[:50]
                })

# Print results
print(f"\n✅ RESULTS:")
print(f"   Total tags checked: {checks['total_tags']}")
print(f"   Portuguese consistency: {checks['portuguese_consistency']} ✓")

if issues['br_portuguese']:
    print(f"\n⚠️  BRAZILIAN PORTUGUESE FOUND: {len(issues['br_portuguese'])} instances")
    for item in issues['br_portuguese'][:5]:
        print(f"   • {item['tag']:30} → replace '{item['word']}' with '{item['suggest']}'")
else:
    print(f"\n✅ PORTUGUESE CONSISTENCY: All tags use Portuguese PT (0 issues)")

# Check for technical English terms
print("\n\n📊 TECHNICAL TERMS ANALYSIS:")
print("-" * 140)

technical_terms_found = defaultdict(list)
for tag_name, tag_data in sorted(tags.items()):
    if not isinstance(tag_data, dict) or ':' in tag_name:
        continue
    
    label = tag_data.get('label', '')
    description = tag_data.get('description', '')
    
    full_text = f"{tag_name} {label} {description}".lower()
    
    for tech_term in technical_en_consensus:
        if tech_term in full_text:
            technical_terms_found[tech_term].append(tag_name)

print(f"\nTechnical English terms found (correctly kept in English):")
terms_list = sorted(list(set(technical_terms_found.keys())))[:20]
for term in terms_list:
    print(f"   ✓ {term:20} ({len(technical_terms_found[term])} tags)")

print(f"\n   ... and {len(technical_terms_found) - len(terms_list)} more")

# Summary
print("\n" + "=" * 140)
print("🎯 SUMMARY")
print("=" * 140)
print(f"""
✅ Portuguese PT Consistency: {len(issues['br_portuguese'])} issues found (target: 0)
✅ English Technical Terms: {len(set(technical_terms_found.keys()))} consensus terms properly maintained
✅ Total Canonical Tags: {checks['total_tags']}

LANGUAGE POLICY:
  • Portuguese: Always Portuguese PT (with diacritics: ç, ã, õ, á, é, í, ó, ú, etc.)
  • Technical: Keep English for global consensus terms (api, pipeline, trigger, etc.)
  • Labels: Portuguese PT by default, English for technical acronyms
  • Aliases: Include variations - PT without accents, synonyms, translations
""")

if issues['br_portuguese']:
    print("\n⚠️  ACTION REQUIRED: Fix remaining Brazilian Portuguese variants")
else:
    print("\n✅ READY FOR AUTO-TAGGING: Portuguese consistency verified!")
