#!/usr/bin/env python3
"""
Audit canonical tags for Portuguese consistency and language mixing
"""

import yaml
from pathlib import Path
from collections import defaultdict

# Load tags
tags_file = Path("/Volumes/G-DRIVE/Shared/Manual-SbD-ToE/SbD-ToE-Manual/src/tag-normalization/canonical-tags.yml")

with open(tags_file, 'r', encoding='utf-8') as f:
    tags = yaml.safe_load(f)

print("\n" + "=" * 140)
print("🔍 CANONICAL TAGS AUDIT: Portuguese Consistency & Language")
print("=" * 140)

# Patterns for Brazilian Portuguese (common differences)
br_pt_patterns = {
    'ão': 'ão',  # Both use this, but check context
    'monitoramento': 'monitorização',
    'operação': 'operação',  # Both use
    'comunicação': 'comunicação',  # Both use
}

# Common technical terms that should stay in English
technical_en = {
    'framework', 'security', 'framework', 'standard', 'pattern', 'pipeline',
    'deployment', 'container', 'kubernetes', 'docker', 'ci/cd', 'devops',
    'siem', 'sast', 'dast', 'sbom', 'exploit', 'threat', 'vulnerability',
    'scanner', 'runner', 'webhook', 'trigger', 'flow', 'gate', 'gate',
    'sandbox', 'registry', 'repository', 'branch', 'commit', 'tag'
}

# Check for issues
issues = {
    'portuguese_variant_mixing': [],  # Mixed PT/BR
    'inconsistent_accents': [],  # accents missing/extra
    'potential_br_portuguese': [],  # Likely Brazilian Portuguese
    'english_mixed_incorrectly': [],  # English where should be PT
}

print("\n📋 CHECKING TAGS...")
print("-" * 140)

for tag_name, tag_data in sorted(tags.items()):
    if not isinstance(tag_data, dict):
        continue
    
    # Get label and description
    label = tag_data.get('label', '')
    description = tag_data.get('description', '')
    aliases = tag_data.get('aliases', [])
    
    # Check if this is a category/prefix (like "tipo:", "tema:", etc)
    if ':' in tag_name:
        continue
    
    # Check for mixed Portuguese variants
    all_text = f"{tag_name} {label} {description} {' '.join(aliases)}".lower()
    
    # Check for monitoramento (BR) instead of monitorização
    if 'monitoramento' in all_text and tag_name != 'monitorizacao':
        issues['potential_br_portuguese'].append({
            'tag': tag_name,
            'context': f"Found 'monitoramento' (BR) - should be 'monitorização' (PT)"
        })
    
    # Check for other common BR/PT differences
    if 'ção' in tag_name or 'ção' in label:
        # This is typically PT, but check for context
        if any(br_word in all_text.lower() for br_word in ['implementação', 'execução', 'operação', 'comunicação']):
            # These are valid in both, but mark for review
            pass

# Print findings
print("\n🚨 POTENTIAL ISSUES FOUND:")
print("-" * 140)

if issues['potential_br_portuguese']:
    print(f"\n🇧🇷 BRAZILIAN PORTUGUESE DETECTED ({len(issues['potential_br_portuguese'])} items):")
    for item in issues['potential_br_portuguese'][:10]:
        print(f"   • {item['tag']:30} - {item['context']}")

# Check label consistency
print("\n\n📊 LABEL LANGUAGE ANALYSIS:")
print("-" * 140)

languages = defaultdict(list)
for tag_name, tag_data in sorted(tags.items()):
    if not isinstance(tag_data, dict):
        continue
    if ':' in tag_name:
        continue
    
    label = tag_data.get('label', '')
    
    # Classify language
    if label.startswith('Tipo:') or label.startswith('Grupo:') or label.startswith('Tema:') or label.startswith('Categoria:'):
        lang = 'Portuguese (with prefix)'
    elif any(c.isascii() and ord(c) < 128 and c.isalpha() for c in label) and not any(c in label for c in 'áéíóúàâêôãõç'):
        # Has ASCII letters but no accents - might be technical term or English
        if label.lower() in technical_en or any(tech in label.lower() for tech in ['api', 'sql', 'http', 'ssl', 'tls', 'oauth', 'mfa', 'sso', 'saml', 'ldap']):
            lang = 'English (technical term)'
        else:
            lang = 'English/Mixed'
    else:
        lang = 'Portuguese'
    
    languages[lang].append(label)

for lang, labels in sorted(languages.items()):
    print(f"\n{lang}: {len(labels)} tags")
    if len(labels) <= 5:
        for label in sorted(labels)[:5]:
            print(f"   • {label}")
    else:
        for label in sorted(labels)[:5]:
            print(f"   • {label}")
        print(f"   ... and {len(labels) - 5} more")

# Check for accent inconsistencies
print("\n\n🔤 ACCENT CONSISTENCY CHECK:")
print("-" * 140)

accent_variants = defaultdict(list)
for tag_name in tags.keys():
    if ':' in tag_name:
        continue
    
    # Remove accents for comparison
    unaccented = tag_name.replace('á', 'a').replace('é', 'e').replace('í', 'i').replace('ó', 'o').replace('ú', 'u').replace('ã', 'a').replace('õ', 'o').replace('ç', 'c')
    
    if unaccented != tag_name:
        accent_variants[unaccented].append(tag_name)

print("\nTags with accentuation variants:")
for unaccented, variants in sorted(accent_variants.items()):
    if len(variants) > 1:
        print(f"   ⚠️  {unaccented}:")
        for v in variants:
            print(f"       • {v}")

print("\n" + "=" * 140)
print("✅ AUDIT COMPLETE")
print("=" * 140)

print("\n📝 RECOMMENDATIONS:")
print("-" * 140)
print("""
1. PORTUGUESE CONSISTENCY:
   ✅ Primary tags should use Portuguese PT spelling (with accents where needed)
   ✅ Aliases can include variations (PT without accents, technical English terms)
   ✅ Brazilian Portuguese should only appear as aliases, not canonical keys

2. ENGLISH TECHNICAL TERMS:
   ✅ Keep: framework, pipeline, docker, kubernetes, api, webhook, trigger, flow, etc.
   ✅ These are technical consensus terms understood globally
   ✅ Add as aliases if Portuguese translation exists, but keep English as canonical

3. MIXED LANGUAGE APPROACH:
   ✅ Canonical key: English (for technical) or Portuguese PT (for concepts)
   ✅ Aliases: Include variations, translations, common synonyms
   ✅ Label: Descriptive, Portuguese PT by default
""")
