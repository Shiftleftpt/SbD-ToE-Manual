#!/usr/bin/env python3
import json
import os

# Carregar o ficheiro
report_path = "reports/canonical_010-sbd.json"
if not os.path.exists(report_path):
    print(f"❌ Ficheiro não encontrado: {report_path}")
    exit(1)

with open(report_path, 'r') as f:
    data = json.load(f)

# Encontrar o intro.md
found = False
for doc in data:
    if 'intro.md' in doc['file_path'] and '01-classificacao' in doc['file_path']:
        found = True
        print(f"{'='*80}")
        print(f"📋 Ficheiro: {doc['file_path']}")
        print(f"{'='*80}\n")
        
        print(f"📌 Título: {doc.get('title', 'N/A')}\n")
        
        print(f"{'='*80}")
        print("🔴 TAGS ATUALMENTE NO INDEX RAG (8 tags)")
        print(f"{'='*80}")
        indexed = doc.get('original_tags', [])
        for tag in sorted(indexed):
            print(f"   • {tag}")
        
        print(f"\n{'='*80}")
        print("🟢 TAGS PROPOSTAS (Canónicas - Semantic Matching)")
        print(f"{'='*80}")
        proposed = doc.get('canonical_suggestions', [])
        
        # Separar por tipo de match
        exact_matches = [(tag, score) for tag, score in proposed if score == 100.0]
        semantic_matches = [(tag, score) for tag, score in proposed if score < 100.0]
        
        print(f"\n✅ Correspondências Exatas (100%):")
        if exact_matches:
            for i, (tag, score) in enumerate(exact_matches, 1):
                print(f"   {i}. {tag}")
        else:
            print("   (nenhuma)")
        
        print(f"\n🔗 Correspondências Semânticas:")
        for i, (tag, score) in enumerate(semantic_matches[:10], 1):
            print(f"   {i}. {tag} ({score:.1f}%)")
        
        print(f"\n{'='*80}")
        print("📊 ANÁLISE COMPARATIVA")
        print(f"{'='*80}")
        print(f"Total de propostas: {len(proposed)}")
        print(f"Exactas (100%): {len(exact_matches)}")
        print(f"Semânticas (<100%): {len(semantic_matches)}")
        
        # Verificar intersecção
        proposed_tags = [tag for tag, _ in proposed]
        indexed_set = set(indexed)
        proposed_set = set(proposed_tags)
        
        intersect = indexed_set & proposed_set
        only_indexed = indexed_set - proposed_set
        only_proposed = proposed_set - indexed_set
        
        print(f"\n✔️  Em AMBOS (index + propostas): {len(intersect)}")
        for tag in sorted(intersect):
            print(f"   • {tag}")
        
        if only_indexed:
            print(f"\n⚠️  APENAS NO INDEX (não foram propostas): {len(only_indexed)}")
            for tag in sorted(only_indexed):
                print(f"   • {tag}")
        
        if only_proposed:
            print(f"\n💡 NOVAS SUGESTÕES (propostas mas não no index): {len(only_proposed)}")
            for tag in sorted(only_proposed)[:15]:
                print(f"   • {tag}")
        break

if not found:
    print("❌ intro.md não encontrado nos resultados")
