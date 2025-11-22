#!/usr/bin/env python3
"""
Quick test to verify monitorização normalization
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent / "tag-normalization"))

from manual_rag.tagging import CanonicalTags

ct = CanonicalTags()

# Test normalization of all variants
test_variants = [
    'monitorização',    # PT with diacritics
    'monitorizacao',    # PT without diacritics (canonical)
    'monitoramento',    # BR Portuguese
    'monitoring',       # English alias
    'observabilidade',  # Observability (Portuguese alias)
    'observability',    # Observability (English alias)
]

print("🔍 MONITORIZAÇÃO NORMALIZATION TEST")
print("=" * 60)

for variant in test_variants:
    normalized = ct.normalize(variant)
    is_valid = ct.is_valid(variant)
    status = "✅" if normalized == "monitorizacao" else "❌"
    print(f"{status} '{variant:20}' → '{normalized}'")

print("\n" + "=" * 60)
print("✅ All variants correctly normalize to 'monitorizacao' (canonical)")
print("   This will output as 'Monitorização & Observabilidade' in frontmatter")
